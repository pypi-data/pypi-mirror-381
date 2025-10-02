"""
github-analyzer: AI-optimized GitHub repository analysis tool with native async support

This package provides tools to analyze GitHub repositories and generate
AI-friendly code context and metadata for enhanced understanding.
"""

__version__ = "1.0.0"
__author__ = "Han Jun-hee"
__email__ = "createbrain2heart@gmail.com"
__license__ = "MIT"
__description__ = "AI-optimized GitHub repository analysis tool with native async support"

# Core imports
from .core import GitHubRepositoryAnalyzer, analyze_repository
from .config import Config
from .logger import get_logger, set_verbose, AnalyzerLogger
from .exceptions import (
    GitHubAnalyzerError,
    NetworkError,
    RateLimitExceededError,
    AuthenticationError,
    RepositoryNotFoundError,
    RepositoryTooLargeError,
    ValidationError,
    UnsupportedFormatError,
    OutputError
)

# Utility imports
from .utils import URLParser, CompressionUtils, FileUtils, TextUtils
from .github_client import GitHubClient
from .file_processor import FileProcessor, LanguageDetector, DependencyExtractor
from .metadata_generator import MetadataGenerator

# Async imports (now mandatory)
from .async_github_client import AsyncGitHubClient, analyze_repository_async

# Public API
__all__ = [
    # Version info
    "__version__", "__author__", "__email__", "__license__", "__description__",
    
    # Main classes
    "GitHubRepositoryAnalyzer", "Config", "AnalyzerLogger",
    
    # Convenience functions
    "analyze_repository", "analyze_repository_async", "get_logger", "set_verbose", 
    "is_async_available",
    
    # Core components
    "GitHubClient", "AsyncGitHubClient", "FileProcessor", "MetadataGenerator",
    "LanguageDetector", "DependencyExtractor",
    
    # Utilities
    "URLParser", "CompressionUtils", "FileUtils", "TextUtils",
    
    # Exceptions
    "GitHubAnalyzerError", "NetworkError", "RateLimitExceededError",
    "AuthenticationError", "RepositoryNotFoundError", "RepositoryTooLargeError",
    "ValidationError", "UnsupportedFormatError", "OutputError"
]

# Package-level configuration
def configure(verbose: bool = False, log_level: str = "WARNING"):
    """Configure package-wide settings"""
    set_verbose(verbose)
    if log_level.upper() in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        import logging
        logging.getLogger("github-analyzer").setLevel(getattr(logging, log_level.upper()))

# Convenience aliases for common usage patterns
Analyzer = GitHubRepositoryAnalyzer
analyze = analyze_repository

# Async aliases (now always available)
AsyncAnalyzer = AsyncGitHubClient
analyze_async = analyze_repository_async

def is_async_available() -> bool:
    """Check if async features are available"""
    return True

def get_async_requirements() -> list:
    """Get list of packages required for async support"""
    return ["httpx>=0.24.0", "aiofiles>=23.0.0"]

# Package info for help()
def get_package_info():
    """Get package information"""
    return {
        "name": "github-analyzer",
        "version": __version__,
        "description": __description__,
        "author": __author__,
        "email": __email__,
        "license": __license__,
        "homepage": "https://github.com/creatorjun/github-analyzer",
        "repository": "https://github.com/creatorjun/github-analyzer.git",
        "contact": "createbrain2heart@gmail.com",
        "async_available": True,  # Always True in v2.0+
        "async_native": True
    }

# Feature detection helper
def check_dependencies():
    """Check availability of all dependencies"""
    deps = {
        "requests": False,
        "rich": False,
        "httpx": False,
        "aiofiles": False,
        "asyncio": True  # Built-in since Python 3.4+
    }
    
    # Check core dependencies
    try:
        import requests
        deps["requests"] = True
    except ImportError:
        pass
    
    try:
        import rich
        deps["rich"] = True
    except ImportError:
        pass
    
    # Check async dependencies (now required)
    try:
        import httpx
        deps["httpx"] = True
    except ImportError:
        pass
    
    try:
        import aiofiles
        deps["aiofiles"] = True
    except ImportError:
        pass
    
    return deps

def print_feature_status():
    """Print current feature availability status"""
    print(f"GitHub Analyzer v{__version__}")
    print(f"Author: {__author__} <{__email__}>")
    print(f"Repository: https://github.com/creatorjun/github-analyzer")
    print("Async support: ✓ Native (built-in)")
    
    deps = check_dependencies()
    print("\nDependency Status:")
    for dep, available in deps.items():
        status = "✓" if available else "✗"
        print(f"  {dep}: {status}")

# Module-level docstring continuation
__doc__ += f"""
Version: {__version__}
Author: {__author__}
Email: {__email__}
License: {__license__}
Repository: https://github.com/creatorjun/github-analyzer

Async Support: Native (built-in)

Quick Start:
>>> from github_analyzer import analyze_repository
>>> result = analyze_repository("https://github.com/user/repo")
>>> print(result['metadata']['repo'])

Async Usage (native support):
>>> import asyncio
>>> from github_analyzer import analyze_repository_async
>>> result = asyncio.run(analyze_repository_async("https://github.com/user/repo"))

For feature status, call github_analyzer.print_feature_status()
"""
