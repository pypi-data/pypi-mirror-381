import asyncio
import time
import zipfile
import json
from io import BytesIO
from typing import Dict, List, Any, Optional, Tuple, Union
from urllib.parse import quote
from pathlib import Path

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False

from .config import Config
from .exceptions import (
    NetworkError,
    RateLimitExceededError,
    AuthenticationError,
    RepositoryNotFoundError,
    RepositoryTooLargeError,
    TimeoutError as AnalyzerTimeoutError,
    handle_github_api_error
)
from .utils import URLParser, ValidationUtils
from .logger import AnalyzerLogger


class AsyncRateLimitManager:
    """Async-safe GitHub API rate limit management"""

    def __init__(self, token: Optional[str] = None):
        self.token = token
        self.limit = 5000 if token else 60
        self.remaining = self.limit
        self.reset_time = int(time.time()) + 3600
        self._lock = asyncio.Lock()

    async def update_from_headers(self, headers: Dict[str, str]):
        """Update rate limit info from response headers"""
        async with self._lock:
            self.limit = int(headers.get('x-ratelimit-limit', self.limit))
            self.remaining = int(headers.get('x-ratelimit-remaining', self.remaining))
            self.reset_time = int(headers.get('x-ratelimit-reset', self.reset_time))

    async def check_rate_limit(self, required_calls: int = 1) -> bool:
        """Check if we have enough API calls remaining"""
        async with self._lock:
            return self.remaining >= (required_calls + Config.RATE_LIMIT_BUFFER)

    async def consume_calls(self, count: int = 1):
        """Consume API calls from remaining count"""
        async with self._lock:
            self.remaining = max(0, self.remaining - count)

    def wait_time_until_reset(self) -> int:
        """Calculate wait time until rate limit resets"""
        return max(0, self.reset_time - int(time.time()))

    async def wait_for_rate_limit_reset(self):
        """Wait for rate limit to reset if necessary"""
        wait_time = self.wait_time_until_reset()
        if wait_time > 0 and self.remaining <= Config.RATE_LIMIT_BUFFER:
            await asyncio.sleep(min(wait_time, 300))  # Max 5 minutes wait


class AsyncGitHubSession:
    """Async HTTP session for GitHub API using httpx"""

    def __init__(self, token: Optional[str] = None, timeout: int = 30):
        if not HTTPX_AVAILABLE:
            raise ImportError("httpx library is required for async operations. Install with: pip install httpx")

        self.token = token
        self.timeout = timeout

        # Setup headers
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': f'{Config.PACKAGE_NAME}/{Config.VERSION}'
        }

        if self.token:
            headers['Authorization'] = f'token {self.token}'

        # Create httpx client with retry configuration
        limits = httpx.Limits(
            max_keepalive_connections=20,
            max_connections=100,
            keepalive_expiry=30
        )

        timeout_config = httpx.Timeout(timeout)
        self.client = httpx.AsyncClient(
            headers=headers,
            timeout=timeout_config,
            limits=limits,
            follow_redirects=True
        )

    async def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Make async HTTP request with error handling"""
        try:
            response = await self.client.request(method, url, **kwargs)
            
            # Handle GitHub API errors
            if not response.is_success:
                error_data = None
                try:
                    if response.content:
                        error_data = response.json()
                except:
                    pass
                
                error = handle_github_api_error(response.status_code, error_data)
                raise error
            
            return response
            
        except httpx.TimeoutException:
            raise AnalyzerTimeoutError(f"Request timeout after {self.timeout} seconds", self.timeout)
        except httpx.ConnectError as e:
            raise NetworkError(f"Connection error: {e}")
        except httpx.HTTPError as e:
            raise NetworkError(f"HTTP error: {e}")

    async def get(self, url: str, **kwargs) -> httpx.Response:
        """GET request"""
        return await self.request('GET', url, **kwargs)

    async def close(self):
        """Close session"""
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class AsyncGitHubClient:
    """Async GitHub API client for improved performance"""

    def __init__(self, token: Optional[str] = None, logger: Optional[AnalyzerLogger] = None):
        self.token = token
        self.logger = logger or AnalyzerLogger()
        self.rate_limit_manager = AsyncRateLimitManager(token)
        self.session = None
        self._semaphore = None

    async def __aenter__(self):
        self.session = AsyncGitHubSession(self.token)
        # Limit concurrent connections based on token availability
        max_concurrent = 50 if self.token else 10
        self._semaphore = asyncio.Semaphore(max_concurrent)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def get_repository_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """Get basic repository information"""
        url = URLParser.build_api_url(owner, repo, "")
        
        try:
            response = await self.session.get(url)
            await self.rate_limit_manager.update_from_headers(dict(response.headers))
            await self.rate_limit_manager.consume_calls(1)
            
            repo_data = response.json()
            
            return {
                'name': repo_data['name'],
                'full_name': repo_data['full_name'],
                'description': repo_data.get('description', ''),
                'language': repo_data.get('language', 'Unknown'),
                'size': repo_data.get('size', 0),  # Size in KB
                'default_branch': repo_data.get('default_branch', 'main'),
                'private': repo_data.get('private', False),
                'archived': repo_data.get('archived', False),
                'disabled': repo_data.get('disabled', False),
                'topics': repo_data.get('topics', []),
                'license': repo_data.get('license', {}).get('name') if repo_data.get('license') else None,
                'created_at': repo_data.get('created_at'),
                'updated_at': repo_data.get('updated_at'),
                'clone_url': repo_data.get('clone_url'),
                'html_url': repo_data.get('html_url')
            }
            
        except Exception as e:
            self.logger.debug(f"Failed to get repository info: {e}")
            # Return minimal info for fallback
            return {
                'name': repo,
                'full_name': f'{owner}/{repo}',
                'description': '',
                'language': 'Unknown',
                'size': 0,
                'default_branch': 'main',
                'private': False
            }

    async def detect_default_branch(self, owner: str, repo: str) -> str:
        """Detect the default branch of repository"""
        # Try repository info first
        try:
            repo_info = await self.get_repository_info(owner, repo)
            if repo_info.get('default_branch'):
                return repo_info['default_branch']
        except:
            pass
        
        # Fallback: try common branch names
        for branch in Config.DEFAULT_BRANCH_PRIORITY:
            try:
                url = URLParser.build_api_url(owner, repo, f"branches/{branch}")
                response = await self.session.get(url)
                await self.rate_limit_manager.update_from_headers(dict(response.headers))
                await self.rate_limit_manager.consume_calls(1)
                
                if response.is_success:
                    self.logger.debug(f"Detected default branch: {branch}")
                    return branch
            except:
                continue
        
        self.logger.warning("Could not detect default branch, using 'main'")
        return 'main'

    async def get_repository_tree_api(self, owner: str, repo: str, branch: str = None) -> List[Dict[str, Any]]:
        """Get repository file tree using GitHub API (recursive) - FIXED METHOD"""
        if not branch:
            branch = await self.detect_default_branch(owner, repo)
        
        url = URLParser.build_api_url(owner, repo, f"git/trees/{branch}?recursive=1")
        
        try:
            async with self._semaphore:
                response = await self.session.get(url)
                await self.rate_limit_manager.update_from_headers(dict(response.headers))
                await self.rate_limit_manager.consume_calls(1)
                
                tree_data = response.json()
                files = []
                
                for item in tree_data.get('tree', []):
                    if item['type'] == 'blob':  # Only files, not directories
                        files.append({
                            'path': item['path'],
                            'size': item.get('size', 0),
                            'sha': item['sha'],
                            'url': item.get('url', ''),
                            'download_url': f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{quote(item['path'])}"
                        })
                
                self.logger.debug(f"Retrieved {len(files)} files via API")
                return files
                
        except Exception as e:
            self.logger.error(f"Failed to get repository tree via API: {e}")
            raise NetworkError(f"Failed to get repository tree: {e}")

    async def download_repository_zip(self, owner: str, repo: str, branch: str = None) -> List[Dict[str, Any]]:
        """Download repository as ZIP and extract file information"""
        if not branch:
            branch = await self.detect_default_branch(owner, repo)
        
        zip_url = URLParser.build_zip_url(owner, repo, branch)
        
        try:
            self.logger.debug(f"Downloading ZIP from: {zip_url}")
            
            async with self.session.client.stream('GET', zip_url, timeout=Config.TIMEOUT_CONFIG['zip_timeout']) as response:
                # Check content length
                content_length = response.headers.get('content-length')
                if content_length:
                    size_mb = int(content_length) / (1024 * 1024)
                    if size_mb > Config.MAX_TOTAL_SIZE_MB * 2:  # Allow 2x for ZIP compression
                        raise RepositoryTooLargeError(
                            f"Repository ZIP too large: {size_mb:.1f}MB",
                            size_mb, Config.MAX_TOTAL_SIZE_MB * 2
                        )
                
                # Download content
                content = b''
                downloaded = 0
                chunk_size = 8192
                
                async for chunk in response.aiter_bytes(chunk_size):
                    content += chunk
                    downloaded += len(chunk)
                    
                    # Progress update for large downloads
                    if content_length:
                        progress = (downloaded / int(content_length)) * 100
                        if downloaded % (chunk_size * 100) == 0:  # Update every ~800KB
                            self.logger.debug(f"Download progress: {progress:.1f}%")
                
                return await self._extract_zip_contents_async(content, f"{repo}-{branch}")
                
        except httpx.TimeoutException:
            raise AnalyzerTimeoutError(
                f"ZIP download timeout after {Config.TIMEOUT_CONFIG['zip_timeout']} seconds",
                Config.TIMEOUT_CONFIG['zip_timeout']
            )
        except Exception as e:
            self.logger.error(f"Failed to download ZIP: {e}")
            raise NetworkError(f"ZIP download failed: {e}")

    async def _extract_zip_contents_async(self, zip_content: bytes, expected_prefix: str) -> List[Dict[str, Any]]:
        """Extract file information from ZIP content asynchronously"""
        # Run CPU-intensive ZIP extraction in thread pool
        loop = asyncio.get_event_loop()
        files = await loop.run_in_executor(
            None,
            self._extract_zip_contents_sync,
            zip_content,
            expected_prefix
        )
        return files

    def _extract_zip_contents_sync(self, zip_content: bytes, expected_prefix: str) -> List[Dict[str, Any]]:
        """Synchronous ZIP extraction (runs in thread pool)"""
        files = []
        
        try:
            with zipfile.ZipFile(BytesIO(zip_content)) as zip_file:
                for zip_info in zip_file.infolist():
                    if zip_info.is_dir():
                        continue
                    
                    # Remove the repository prefix from path
                    file_path = zip_info.filename
                    if file_path.startswith(f"{expected_prefix}/"):
                        file_path = file_path[len(f"{expected_prefix}/"):]
                    elif "/" in file_path:
                        # Handle different branch name format
                        file_path = "/".join(file_path.split("/")[1:])
                    
                    if not file_path:  # Skip root files with no path
                        continue
                    
                    # Skip excluded directories and binary files
                    if any(Config.is_excluded_directory(part) for part in file_path.split('/')):
                        continue
                    
                    if Config.is_binary_file(file_path):
                        continue
                    
                    # Read file content
                    try:
                        with zip_file.open(zip_info) as file:
                            content = file.read()
                            
                            # Skip large files
                            if len(content) > Config.MAX_FILE_SIZE_BYTES:
                                continue
                            
                            # Try to decode as text
                            try:
                                text_content = content.decode('utf-8')
                            except UnicodeDecodeError:
                                try:
                                    text_content = content.decode('latin-1')
                                except UnicodeDecodeError:
                                    continue
                            
                            files.append({
                                'path': file_path,
                                'size': len(content),
                                'content': text_content,
                                'priority': Config.get_file_priority(file_path)
                            })
                    except Exception:
                        continue
            
            return files
            
        except zipfile.BadZipFile as e:
            raise NetworkError(f"Invalid ZIP file: {e}")
        except Exception as e:
            raise NetworkError(f"ZIP extraction failed: {e}")

    async def download_single_file(self, file_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Download a single file asynchronously"""
        async with self._semaphore:  # Limit concurrent downloads
            if not await self.rate_limit_manager.check_rate_limit(1):
                await self.rate_limit_manager.wait_for_rate_limit_reset()
            
            try:
                response = await self.session.get(
                    file_info['download_url'],
                    timeout=Config.TIMEOUT_CONFIG['http_timeout']
                )
                
                await self.rate_limit_manager.update_from_headers(dict(response.headers))
                await self.rate_limit_manager.consume_calls(1)
                
                # Check file size
                content = response.content
                if len(content) > Config.MAX_FILE_SIZE_BYTES:
                    self.logger.debug(f"Skipping large file: {file_info['path']} ({len(content)} bytes)")
                    return None
                
                # Decode content
                try:
                    text_content = content.decode('utf-8')
                except UnicodeDecodeError:
                    try:
                        text_content = content.decode('latin-1')
                    except UnicodeDecodeError:
                        self.logger.debug(f"Skipping binary file: {file_info['path']}")
                        return None
                
                return {
                    'path': file_info['path'],
                    'size': len(content),
                    'content': text_content,
                    'priority': file_info.get('priority', Config.get_file_priority(file_info['path']))
                }
                
            except Exception as e:
                self.logger.debug(f"Failed to download {file_info['path']}: {e}")
                return None

    async def download_files_concurrently(self, files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Download multiple files concurrently with improved async handling"""
        if not files:
            return []
        
        self.logger.debug(f"Starting async download of {len(files)} files")
        
        # Create download tasks
        tasks = []
        for file_info in files:
            task = asyncio.create_task(self.download_single_file(file_info))
            tasks.append(task)
        
        # Execute downloads with progress tracking
        completed_files = []
        completed_count = 0
        
        # Process downloads as they complete
        for coro in asyncio.as_completed(tasks):
            try:
                result = await coro
                completed_count += 1
                if result:
                    completed_files.append(result)
                
                # Progress update
                if completed_count % 10 == 0:
                    self.logger.debug(f"Downloaded {completed_count}/{len(files)} files")
            except Exception as e:
                self.logger.debug(f"Download task failed: {e}")
        
        self.logger.debug(f"Async download completed: {len(completed_files)} successful files")
        return completed_files

    async def analyze_repository(self, owner: str, repo: str, method: str = "auto") -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """Main async method to analyze repository"""
        # Get repository information
        repo_info = await self.get_repository_info(owner, repo)
        
        # Check if repository is accessible
        if repo_info.get('private') and not self.token:
            raise AuthenticationError("Private repository requires GitHub token")
        
        if repo_info.get('disabled'):
            raise RepositoryNotFoundError("Repository is disabled")
        
        if repo_info.get('archived'):
            self.logger.warning("Repository is archived")
        
        # Determine method
        if method == "auto":
            # Estimate file count and suggest method
            estimated_files = min(repo_info.get('size', 0) // 10, 1000)
            if not await self.rate_limit_manager.check_rate_limit(estimated_files):
                method = "zip"
            else:
                method = "api" if self.token else "zip"
            self.logger.debug(f"Auto-selected method: {method}")
        
        try:
            if method == "zip":
                files = await self.download_repository_zip(owner, repo, repo_info['default_branch'])
            elif method == "api":
                # Get file tree first
                tree_files = await self.get_repository_tree_api(owner, repo, repo_info['default_branch'])
                # Filter and prioritize files
                filtered_files = self._filter_and_prioritize_files(tree_files)
                # Download file contents
                files = await self.download_files_concurrently(filtered_files)
            else:
                raise ValueError(f"Unknown method: {method}")
            
            # Ensure files is always a list
            if not isinstance(files, list):
                self.logger.warning(f"Expected list from {method} method, got {type(files)}")
                files = []
            
            return files, repo_info
            
        except (NetworkError, RateLimitExceededError) as e:
            # Try fallback method
            if method == "api":
                self.logger.warning(f"API method failed: {e}. Trying ZIP method...")
                try:
                    files = await self.download_repository_zip(owner, repo, repo_info['default_branch'])
                    return files if isinstance(files, list) else [], repo_info
                except Exception as fallback_e:
                    self.logger.error(f"ZIP fallback also failed: {fallback_e}")
                    return [], repo_info
            elif method == "zip":
                self.logger.warning(f"ZIP method failed: {e}. Trying API method...")
                try:
                    tree_files = await self.get_repository_tree_api(owner, repo, repo_info['default_branch'])
                    filtered_files = self._filter_and_prioritize_files(tree_files)
                    files = await self.download_files_concurrently(filtered_files)
                    return files if isinstance(files, list) else [], repo_info
                except Exception as fallback_e:
                    self.logger.error(f"API fallback also failed: {fallback_e}")
                    return [], repo_info
            else:
                raise

    def _filter_and_prioritize_files(self, files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter and prioritize files for download"""
        # Add priority scores
        for file_info in files:
            file_info['priority'] = Config.get_file_priority(file_info['path'])
        
        # Filter out excluded files
        filtered_files = []
        for file_info in files:
            path = file_info['path']
            
            # Skip excluded directories
            if any(Config.is_excluded_directory(part) for part in path.split('/')):
                continue
            
            # Skip binary files
            if Config.is_binary_file(path):
                continue
            
            # Skip large files
            if file_info.get('size', 0) > Config.MAX_FILE_SIZE_BYTES:
                continue
            
            filtered_files.append(file_info)
        
        # Sort by priority (highest first)
        filtered_files.sort(key=lambda x: x['priority'], reverse=True)
        
        # Limit total size
        total_size = 0
        selected_files = []
        for file_info in filtered_files:
            file_size = file_info.get('size', 0)
            if total_size + file_size <= Config.MAX_TOTAL_SIZE_BYTES:
                selected_files.append(file_info)
                total_size += file_size
            else:
                break
        
        self.logger.debug(f"Selected {len(selected_files)} files out of {len(files)} total")
        return selected_files

    async def get_rate_limit_info(self) -> Dict[str, Any]:
        """Get current rate limit information"""
        return {
            'limit': self.rate_limit_manager.limit,
            'remaining': self.rate_limit_manager.remaining,
            'reset_time': self.rate_limit_manager.reset_time,
            'reset_in_seconds': self.rate_limit_manager.wait_time_until_reset()
        }


# ========================================
# MISSING FUNCTION: analyze_repository_async
# ========================================

async def analyze_repository_async(
    repo_url: str,
    output_dir: str = "./results",
    output_format: str = "bin",
    github_token: Optional[str] = None,
    method: str = "auto"
) -> Dict[str, Any]:  # ← Returns Dict, not Tuple!
    """
    Async convenience function that returns Dict format (fixes 'get' attribute error)
    This was the missing function causing all the import errors!
    """
    # Local imports to avoid circular dependencies
    from .file_processor import FileProcessor
    from .metadata_generator import MetadataGenerator
    from .utils import FileUtils, CompressionUtils
    
    try:
        # Parse GitHub URL
        parsed_url = URLParser.parse_github_url(repo_url)
        owner, repo = parsed_url['owner'], parsed_url['repo']
        
        # Use async client - returns tuple (files, repo_info)
        async with AsyncGitHubClient(github_token) as client:
            files, repo_info = await client.analyze_repository(owner, repo, method)
            
            # Process files synchronously
            file_processor = FileProcessor()
            processed_files, processing_metadata = file_processor.process_files(files)
            
            # Generate metadata
            metadata_generator = MetadataGenerator()
            metadata = metadata_generator.generate_metadata(
                processed_files, processing_metadata, repo_info, repo_url
            )
            
            compact_metadata = metadata_generator.generate_compact_metadata(
                processed_files, processing_metadata, repo_info, repo_url
            )
            
            # Create output directory
            base_output_dir = Path(output_dir)
            repo_output_dir = base_output_dir / f"{owner}_{repo}"
            FileUtils.ensure_directory(repo_output_dir)
            base_filename = f"{owner}_{repo}"
            output_paths = {}
            
            # Save metadata files
            meta_path = repo_output_dir / f"{base_filename}_meta.json"
            with open(meta_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
            output_paths['metadata'] = str(meta_path)
            
            compact_meta_path = repo_output_dir / f"{base_filename}_compact_meta.json"
            with open(compact_meta_path, 'w', encoding='utf-8') as f:
                json.dump(compact_metadata, f, ensure_ascii=False, separators=(',', ':'))
            output_paths['compact_metadata'] = str(compact_meta_path)
            
            # Create code data structure
            code_data = {"f": {}}  # Minimal key for AI parsing
            for file_info in processed_files:
                path = file_info.get('path', '')
                content = file_info.get('content', '')
                if path and content:
                    code_data["f"][path] = content
            
            # Save based on output format
            if output_format in ["json", "both"]:
                code_json_path = repo_output_dir / f"{base_filename}_code.json"
                with open(code_json_path, 'w', encoding='utf-8') as f:
                    json.dump(code_data, f, ensure_ascii=False, separators=(',', ':'))
                output_paths['code_json'] = str(code_json_path)
            
            if output_format in ["bin", "both"]:
                code_bin_path = repo_output_dir / f"{base_filename}_code.json.gz"
                json_str = json.dumps(code_data, ensure_ascii=False, separators=(',', ':'))
                compressed_data = CompressionUtils.compress_data(json_str, "gzip")
                with open(code_bin_path, 'wb') as f:
                    f.write(compressed_data)
                output_paths['code_binary'] = str(code_bin_path)
            
            # Return consistent dictionary structure (not tuple!)
            return {
                'metadata': metadata,
                'compact_metadata': compact_metadata,
                'files': processed_files,
                'repo_info': repo_info,
                'processing_metadata': processing_metadata,
                'output_paths': output_paths,
                'success': True
            }
            
    except Exception as e:
        # Return error structure that's still a dictionary
        return {
            'metadata': {},
            'compact_metadata': {},
            'files': [],
            'repo_info': {},
            'processing_metadata': {},
            'output_paths': {},
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }
