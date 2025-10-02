from pathlib import Path

class Config:
    
    # Project Information
    PACKAGE_NAME = "github-analyzer"
    VERSION = "1.0.0"
    
    # File Size Limits
    MAX_FILES_COUNT = 1000
    MAX_TOTAL_SIZE_MB = 100
    MAX_FILE_SIZE_MB = 1
    MAX_TOTAL_SIZE_BYTES = MAX_TOTAL_SIZE_MB * 1024 * 1024
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
    
    # GitHub API Configuration
    GITHUB_API_BASE = "https://api.github.com"
    DEFAULT_BRANCH_PRIORITY = ["main", "master", "develop", "dev", "gh-pages"]
    
    # Rate Limit Management
    RATE_LIMIT_BUFFER = 10
    MAX_CONCURRENT_DOWNLOADS = {
        "with_token": 10,
        "without_token": 3
    }
    
    # Async-specific settings (새로 추가)
    ASYNC_CONFIG = {
        "max_semaphore_size": 50,  # 최대 동시 비동기 작업 수
        "connection_pool_size": 100,  # httpx 연결 풀 크기
        "keepalive_connections": 20,  # 유지 연결 수
        "keepalive_expiry": 30,  # 연결 유지 시간 (초)
        "chunk_size": 8192,  # 스트리밍 다운로드 청크 크기
        "progress_update_interval": 100  # 진행률 업데이트 간격 (청크 단위)
    }
    
    # Compression Settings
    COMPRESSION_CONFIG = {
        "format": "gzip",
        "level": 6,
        "threshold_mb": 10
    }
    
    # Retry Configuration
    RETRY_CONFIG = {
        "max_retries": 3,
        "base_delay": 1,
        "max_delay": 32,
        "backoff_factor": 2,
        "jitter": True
    }
    
    # Network Timeouts (동기/비동기 공용)
    TIMEOUT_CONFIG = {
        "http_timeout": 30,    # HTTP 요청 타임아웃
        "zip_timeout": 120,    # ZIP 다운로드 타임아웃
        "api_timeout": 15,     # API 호출 타임아웃
        "connect_timeout": 10, # 연결 타임아웃 (새로 추가)
        "read_timeout": 30,    # 읽기 타임아웃 (새로 추가)
        "write_timeout": 30    # 쓰기 타임아웃 (새로 추가)
    }
    
    # File Priority Patterns (1000 point system)
    FILE_PRIORITY_PATTERNS = {
        # Entry points (1000 points)
        "main.py": 1000,
        "app.py": 1000,
        "index.js": 1000,
        "index.ts": 1000,
        "server.js": 1000,
        "run.py": 1000,
        "__main__.py": 1000,
        
        # Configuration files (900 points)
        "package.json": 900,
        "pyproject.toml": 900,
        "setup.py": 900,
        "requirements.txt": 900,
        "dockerfile": 900,
        "docker-compose.yml": 900,
        "makefile": 900,
        "cmake.txt": 900,
        
        # Documentation (800 points)
        "readme.md": 800,
        "readme.txt": 800,
        "license": 800,
        "license.txt": 800,
        "license.md": 800,
        "changelog.md": 800,
        "contributing.md": 800,
        
        # Source directories (700-600 points)
        "src/": 700,
        "lib/": 600,
        "app/": 650,
        "core/": 620,
        "utils/": 580,
        "components/": 580,
        "modules/": 580,
        
        # Test files (400 points)
        "test/": 400,
        "tests/": 400,
        "__tests__/": 400,
        "spec/": 400,
        
        # Build and deployment (300 points)
        ".github/": 300,
        "scripts/": 300,
        "build/": 200,
        "dist/": 200,
        
        # Low priority (100 points)
        "node_modules/": 50,
        ".git/": 50,
        "__pycache__/": 50,
        ".pytest_cache/": 50,
        "venv/": 50,
        ".venv/": 50
    }
    
    # Language-specific priority patterns
    LANGUAGE_PRIORITY_PATTERNS = {
        "python": {
            "entry_points": ["__main__.py", "main.py", "app.py", "run.py", "manage.py"],
            "config_files": ["setup.py", "pyproject.toml", "requirements.txt", "setup.cfg", "tox.ini"],
            "important_dirs": ["src/", "app/", "lib/", "core/"],
            "framework_files": {
                "django": ["manage.py", "settings.py", "urls.py", "wsgi.py", "asgi.py"],
                "flask": ["app.py", "run.py", "config.py", "__init__.py"],
                "fastapi": ["main.py", "app.py", "api.py"],
                "pytest": ["conftest.py", "test_*.py", "*_test.py"]
            }
        },
        "javascript": {
            "entry_points": ["index.js", "main.js", "app.js", "server.js", "index.ts", "main.ts"],
            "config_files": ["package.json", "webpack.config.js", "vite.config.js", "tsconfig.json", ".eslintrc.js"],
            "important_dirs": ["src/", "lib/", "app/", "components/"],
            "framework_files": {
                "react": ["App.jsx", "App.tsx", "index.jsx", "index.tsx", "src/App.js"],
                "vue": ["main.js", "App.vue", "vue.config.js", "nuxt.config.js"],
                "nextjs": ["next.config.js", "pages/_app.js", "pages/index.js"],
                "express": ["server.js", "app.js", "index.js"],
                "nestjs": ["main.ts", "app.module.ts", "app.controller.ts"]
            }
        },
        "typescript": {
            "entry_points": ["index.ts", "main.ts", "app.ts", "server.ts"],
            "config_files": ["tsconfig.json", "package.json", "webpack.config.ts"],
            "important_dirs": ["src/", "lib/", "types/"],
            "framework_files": {
                "angular": ["main.ts", "app.module.ts", "app.component.ts"],
                "nestjs": ["main.ts", "app.module.ts", "app.controller.ts"]
            }
        },
        "java": {
            "entry_points": ["Main.java", "Application.java", "App.java"],
            "config_files": ["pom.xml", "build.gradle", "application.properties", "application.yml"],
            "important_dirs": ["src/main/", "src/test/"],
            "framework_files": {
                "spring": ["Application.java", "Controller.java", "Service.java", "Repository.java"],
                "maven": ["pom.xml"],
                "gradle": ["build.gradle", "settings.gradle"]
            }
        },
        "go": {
            "entry_points": ["main.go", "cmd/main.go"],
            "config_files": ["go.mod", "go.sum", "Makefile", "Dockerfile"],
            "important_dirs": ["cmd/", "internal/", "pkg/", "api/"],
            "framework_files": {
                "gin": ["main.go", "router.go"],
                "echo": ["main.go", "handler.go"]
            }
        },
        "rust": {
            "entry_points": ["main.rs", "lib.rs"],
            "config_files": ["Cargo.toml", "Cargo.lock"],
            "important_dirs": ["src/", "tests/"],
            "framework_files": {
                "actix": ["main.rs", "handlers.rs"],
                "rocket": ["main.rs", "routes.rs"]
            }
        }
    }
    
    # File extensions to language mapping
    EXTENSION_TO_LANGUAGE = {
        ".py": "python",
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".java": "java",
        ".go": "go",
        ".rs": "rust",
        ".c": "c",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".cxx": "cpp",
        ".h": "c",
        ".hpp": "cpp",
        ".php": "php",
        ".rb": "ruby",
        ".swift": "swift",
        ".kt": "kotlin",
        ".scala": "scala",
        ".cs": "csharp",
        ".fs": "fsharp",
        ".clj": "clojure",
        ".hs": "haskell",
        ".ml": "ocaml",
        ".r": "r",
        ".m": "matlab",
        ".sh": "shell",
        ".bash": "shell",
        ".zsh": "shell",
        ".fish": "shell",
        ".ps1": "powershell",
        ".sql": "sql",
        ".html": "html",
        ".css": "css",
        ".scss": "scss",
        ".sass": "sass",
        ".less": "less",
        ".xml": "xml",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".toml": "toml",
        ".ini": "ini",
        ".cfg": "ini",
        ".conf": "conf",
        ".md": "markdown",
        ".txt": "text"
    }
    
    # Binary file extensions to exclude
    BINARY_EXTENSIONS = {
        # Images
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".webp", ".tiff", ".tga",
        # Audio
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a",
        # Video
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v",
        # Archives
        ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar", ".tar.gz", ".tar.bz2",
        # Executables
        ".exe", ".dll", ".so", ".dylib", ".app", ".deb", ".rpm", ".msi", ".dmg",
        # Documents
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        # Fonts
        ".ttf", ".otf", ".woff", ".woff2", ".eot",
        # Databases
        ".db", ".sqlite", ".sqlite3", ".mdb",
        # Other binaries
        ".bin", ".dat", ".dump", ".img", ".iso", ".lock"
    }
    
    # Directories to exclude
    EXCLUDED_DIRECTORIES = {
        ".git", ".svn", ".hg", ".bzr",
        "node_modules", "__pycache__", ".pytest_cache",
        "venv", ".venv", "env", ".env",
        "build", "dist", "target", "out", "bin", "obj",
        ".idea", ".vscode", ".vs",
        "logs", "log", "tmp", "temp",
        ".tox", ".coverage", ".nyc_output",
        "vendor", "Pods",
        ".next", ".nuxt", ".cache"
    }
    
    # Performance limits
    PERFORMANCE_LIMITS = {
        "memory_limit_mb": 500,
        "file_cache_size": 100,
        "max_concurrent_files": 50
    }
    
    # Output format configurations
    OUTPUT_FORMATS = ["bin", "json", "both"]
    
    @classmethod
    def get_file_priority(cls, file_path: str) -> int:
        """Calculate file priority based on patterns"""
        file_path_lower = file_path.lower()
        
        # Check exact matches first
        filename = Path(file_path_lower).name
        if filename in cls.FILE_PRIORITY_PATTERNS:
            return cls.FILE_PRIORITY_PATTERNS[filename]
        
        # Check directory patterns
        for pattern, priority in cls.FILE_PRIORITY_PATTERNS.items():
            if pattern.endswith("/") and pattern[:-1] in file_path_lower:
                return priority
        
        # Default priority
        return 100
    
    @classmethod
    def is_binary_file(cls, file_path: str) -> bool:
        """Check if file is binary based on extension"""
        extension = Path(file_path).suffix.lower()
        return extension in cls.BINARY_EXTENSIONS
    
    @classmethod
    def is_excluded_directory(cls, dir_path: str) -> bool:
        """Check if directory should be excluded"""
        dir_name = Path(dir_path).name.lower()
        return dir_name in cls.EXCLUDED_DIRECTORIES
    
    @classmethod
    def get_language_from_extension(cls, file_path: str) -> str:
        """Get programming language from file extension"""
        extension = Path(file_path).suffix.lower()
        return cls.EXTENSION_TO_LANGUAGE.get(extension, "unknown")
    
    @classmethod
    def get_max_concurrency(cls, has_token: bool, rate_remaining: int = None) -> int:
        """Calculate optimal concurrency based on token and rate limits"""
        base_concurrency = cls.MAX_CONCURRENT_DOWNLOADS["with_token" if has_token else "without_token"]
        
        if rate_remaining is not None and has_token:
            # Conservative approach: use only 1/20 of remaining calls
            safe_concurrency = max(1, rate_remaining // 20)
            return min(base_concurrency, safe_concurrency)
        
        return base_concurrency
    
    @classmethod
    def get_async_semaphore_size(cls, has_token: bool, rate_remaining: int = None) -> int:
        """Get optimal semaphore size for async operations (새로 추가)"""
        base_size = cls.ASYNC_CONFIG["max_semaphore_size"]
        
        if has_token:
            # Token이 있는 경우 더 많은 동시 작업 허용
            if rate_remaining is not None:
                # 잔여 API 호출량의 1/10을 동시 작업으로 사용
                safe_size = max(5, min(rate_remaining // 10, base_size))
                return safe_size
            return min(base_size, 30)  # 토큰 있는 경우 기본 30개
        else:
            # Token이 없는 경우 제한적 사용
            return min(base_size, 10)
    
    @classmethod
    def get_httpx_timeout(cls) -> dict:
        """Get httpx timeout configuration (새로 추가)"""
        return {
            "connect": cls.TIMEOUT_CONFIG["connect_timeout"],
            "read": cls.TIMEOUT_CONFIG["read_timeout"],
            "write": cls.TIMEOUT_CONFIG["write_timeout"],
            "pool": cls.TIMEOUT_CONFIG["api_timeout"]
        }
