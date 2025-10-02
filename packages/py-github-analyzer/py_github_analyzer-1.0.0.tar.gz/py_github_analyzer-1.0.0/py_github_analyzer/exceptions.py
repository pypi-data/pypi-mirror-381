class GitHubAnalyzerError(Exception):
    """Base exception for GitHub Analyzer"""
    def __init__(self, message: str, details: str = None):
        self.message = message
        self.details = details
        super().__init__(self.message)
    
    def __str__(self):
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message


class NetworkError(GitHubAnalyzerError):
    """Network-related errors"""
    pass


class RateLimitExceededError(GitHubAnalyzerError):
    """GitHub API rate limit exceeded"""
    def __init__(self, message: str, reset_time: int = None, remaining: int = None):
        super().__init__(message)
        self.reset_time = reset_time
        self.remaining = remaining


class AuthenticationError(GitHubAnalyzerError):
    """GitHub authentication failed"""
    pass


class RepositoryNotFoundError(GitHubAnalyzerError):
    """Repository not found or not accessible"""
    pass


class RepositoryTooLargeError(GitHubAnalyzerError):
    """Repository exceeds size limits"""
    def __init__(self, message: str, size_mb: float, limit_mb: float):
        super().__init__(message)
        self.size_mb = size_mb
        self.limit_mb = limit_mb


class InvalidRepositoryURLError(GitHubAnalyzerError):
    """Invalid repository URL format"""
    pass


class FileProcessingError(GitHubAnalyzerError):
    """Error during file processing"""
    def __init__(self, message: str, file_path: str = None):
        super().__init__(message)
        self.file_path = file_path


class CompressionError(GitHubAnalyzerError):
    """Error during compression/decompression"""
    pass


class OutputError(GitHubAnalyzerError):
    """Error during output generation"""
    pass


class ConfigurationError(GitHubAnalyzerError):
    """Configuration-related errors"""
    pass


class MemoryLimitExceededError(GitHubAnalyzerError):
    """Memory usage exceeded limits"""
    def __init__(self, message: str, current_mb: float, limit_mb: float):
        super().__init__(message)
        self.current_mb = current_mb
        self.limit_mb = limit_mb


class TimeoutError(GitHubAnalyzerError):
    """Operation timeout"""
    def __init__(self, message: str, timeout_seconds: int):
        super().__init__(message)
        self.timeout_seconds = timeout_seconds


class ValidationError(GitHubAnalyzerError):
    """Data validation error"""
    pass


class UnsupportedFormatError(GitHubAnalyzerError):
    """Unsupported output format"""
    def __init__(self, message: str, format_name: str, supported_formats: list):
        super().__init__(message)
        self.format_name = format_name
        self.supported_formats = supported_formats


class CircuitBreakerOpenError(GitHubAnalyzerError):
    """Circuit breaker is open due to consecutive failures"""
    def __init__(self, message: str, failure_count: int, threshold: int):
        super().__init__(message)
        self.failure_count = failure_count
        self.threshold = threshold


class DependencyError(GitHubAnalyzerError):
    """Missing or incompatible dependency"""
    def __init__(self, message: str, dependency_name: str, required_version: str = None):
        super().__init__(message)
        self.dependency_name = dependency_name
        self.required_version = required_version


class PartialAnalysisError(GitHubAnalyzerError):
    """Analysis completed with some failures"""
    def __init__(self, message: str, processed_files: int, failed_files: int, errors: list):
        super().__init__(message)
        self.processed_files = processed_files
        self.failed_files = failed_files
        self.errors = errors


def handle_github_api_error(status_code: int, response_data: dict = None) -> GitHubAnalyzerError:
    """Convert GitHub API error responses to appropriate exceptions"""
    
    if status_code == 401:
        return AuthenticationError("GitHub authentication failed. Check your token.")
    
    elif status_code == 403:
        if response_data and "rate limit" in str(response_data).lower():
            reset_time = response_data.get("reset", 0) if response_data else 0
            remaining = response_data.get("remaining", 0) if response_data else 0
            return RateLimitExceededError(
                "GitHub API rate limit exceeded",
                reset_time=reset_time,
                remaining=remaining
            )
        else:
            return AuthenticationError("Access forbidden. Repository may be private or token lacks permission.")
    
    elif status_code == 404:
        return RepositoryNotFoundError("Repository not found or not accessible")
    
    elif status_code == 422:
        return ValidationError("Invalid request parameters")
    
    elif status_code >= 500:
        return NetworkError(f"GitHub server error (HTTP {status_code})")
    
    else:
        return GitHubAnalyzerError(f"Unexpected GitHub API error (HTTP {status_code})")


def format_error_for_user(error: Exception, context: str = None) -> str:
    """Format error messages for user-friendly display"""
    
    if isinstance(error, RateLimitExceededError):
        if error.reset_time:
            import time
            wait_time = max(0, error.reset_time - int(time.time()))
            hours, remainder = divmod(wait_time, 3600)
            minutes, _ = divmod(remainder, 60)
            
            if hours > 0:
                time_str = f"{hours}h {minutes}m"
            else:
                time_str = f"{minutes}m"
            
            return f"GitHub API rate limit exceeded. Reset in {time_str}. Consider using a GitHub token for higher limits."
        else:
            return "GitHub API rate limit exceeded. Please wait before retrying."
    
    elif isinstance(error, AuthenticationError):
        return f"{error.message} Visit https://github.com/settings/tokens to create a personal access token."
    
    elif isinstance(error, RepositoryNotFoundError):
        return f"{error.message} Check the repository URL and ensure it's publicly accessible."
    
    elif isinstance(error, RepositoryTooLargeError):
        return f"Repository is too large ({error.size_mb:.1f}MB > {error.limit_mb}MB). Only core files will be analyzed."
    
    elif isinstance(error, NetworkError):
        return f"Network error: {error.message} Check your internet connection and try again."
    
    elif isinstance(error, PartialAnalysisError):
        return f"Analysis completed with warnings: {error.processed_files} files processed, {error.failed_files} files failed."
    
    elif isinstance(error, GitHubAnalyzerError):
        base_msg = error.message
        if context:
            return f"{context}: {base_msg}"
        return base_msg
    
    else:
        error_type = type(error).__name__
        if context:
            return f"{context}: {error_type} - {str(error)}"
        return f"{error_type}: {str(error)}"
