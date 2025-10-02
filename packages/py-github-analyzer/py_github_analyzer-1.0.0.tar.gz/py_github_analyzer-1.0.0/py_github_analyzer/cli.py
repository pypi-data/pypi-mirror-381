import sys
import os
import argparse
import asyncio
from pathlib import Path

# Windows UTF-8 environment setup
if os.name == 'nt':  # Windows
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    os.environ['PYTHONLEGACYWINDOWSFSENCODING'] = '0'

# Console encoding setup
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    # Python < 3.7
    pass
except Exception:
    # Ignore other errors
    pass

from .core import GitHubRepositoryAnalyzer, analyze_repository, analyze_repository_async
from .logger import get_logger, set_verbose
from . import is_async_available


def main():
    """Main CLI entry point with native async support"""
    # Additional encoding setup for Windows
    if os.name == 'nt':
        import locale
        try:
            # Attempt to set console code page to UTF-8
            locale.setlocale(locale.LC_ALL, '')
        except:
            pass
    
    parser = argparse.ArgumentParser(
        description="github-analyzer: AI-optimized GitHub repository analysis tool with native async support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic analysis (async by default in v2.0+)
  github-analyzer https://github.com/user/repo
  
  # Force sync mode
  github-analyzer https://github.com/user/repo --sync
  
  # With token and JSON output
  github-analyzer https://github.com/user/repo -t YOUR_TOKEN -f json
  
  # API method with verbose logging
  github-analyzer https://github.com/user/repo -m api -v
  
  # Dry run simulation
  github-analyzer https://github.com/user/repo --dry-run

Author: Han Jun-hee <createbrain2heart@gmail.com>
Repository: https://github.com/creatorjun/github-analyzer
Contact: createbrain2heart@gmail.com
Version: 1.0.0 - Native Async Support
"""
    )
    
    # POSITIONAL ARGUMENT
    parser.add_argument(
        "repo_url",
        type=str,
        help="GitHub repository URL to analyze"
    )
    
    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default="./results",
        help="Directory to save analysis results (default: ./results)"
    )
    
    parser.add_argument(
        "-f", "--output-format",
        type=str,
        choices=["bin", "json", "both"],
        default="bin",
        help="Output format: bin (compressed), json, or both (default: bin)"
    )
    
    parser.add_argument(
        "-t", "--github-token",
        type=str,
        default=None,
        help="GitHub personal access token for API authentication"
    )
    
    parser.add_argument(
        "-m", "--method",
        type=str,
        choices=["auto", "zip", "api"],
        default="auto",
        help="Download method: auto, zip, or api (default: auto)"
    )
    
    # Performance and async options (changed defaults)
    parser.add_argument(
        "--sync",
        action="store_true",
        dest="sync_mode",
        help="Force synchronous processing (async is default in v2.0+)"
    )
    
    parser.add_argument(
        "--async",
        action="store_true",
        dest="async_mode",
        help="Use async processing (default behavior in v2.0+, kept for compatibility)"
    )
    
    # Logging options
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose debug logging"
    )
    
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress non-error output"
    )
    
    # Execution options
    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        help="Simulate analysis without downloading files"
    )
    
    parser.add_argument(
        "--no-fallback",
        action="store_true",
        help="Disable fallback strategies on failures"
    )
    
    # Feature checking
    parser.add_argument(
        "--check-features",
        action="store_true",
        help="Check available features and dependencies"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="github-analyzer 1.0.0 by Han Jun-hee - Native Async Support"
    )
    
    args = parser.parse_args()
    
    # Handle feature check
    if args.check_features:
        check_and_print_features()
        sys.exit(0)
    
    # Validate async options
    if args.async_mode and args.sync_mode:
        print("Error: --async and --sync options are mutually exclusive", file=sys.stderr)
        sys.exit(1)
    
    # Setup logging
    if args.quiet:
        set_verbose(False)
        logger = get_logger(False)
        import logging
        logging.getLogger("github-analyzer").setLevel(logging.ERROR)
    else:
        set_verbose(args.verbose)
        logger = get_logger(args.verbose)
    
    # Determine async mode (default: True in v2.0+)
    use_async = not args.sync_mode  # Default to async unless --sync is specified
    
    if use_async:
        logger.debug("Using async processing mode (default in v2.0+)")
    else:
        logger.debug("Using synchronous processing mode (explicitly requested)")
    
    logger.info(f"Starting analysis for repository: {args.repo_url}")
    
    # Handle dry run
    if args.dry_run:
        run_dry_run(args, logger)
        return
    
    # Run analysis
    try:
        if use_async:
            result = asyncio.run(run_async_analysis(args, logger))
        else:
            result = run_sync_analysis(args, logger)
        
        handle_success(result, args, logger)
        
    except KeyboardInterrupt:
        logger.warning("Analysis interrupted by user.")
        sys.exit(130)
    except Exception as e:
        handle_error(e, args, logger)


def run_dry_run(args, logger):
    """Run dry-run simulation"""
    logger.info("Dry-run mode enabled: No files will be downloaded.")
    
    try:
        from .utils import URLParser
        parsed_url = URLParser.parse_github_url(args.repo_url)
        logger.info(f"Repository URL parsed successfully: {parsed_url['owner']}/{parsed_url['repo']} (dry run)")
        
        # Show what would be done
        logger.info(f"Would save results to: {Path(args.output_dir).resolve()}")
        logger.info(f"Would use output format: {args.output_format}")
        logger.info(f"Would use method: {args.method}")
        logger.info(f"Would use async mode: {not args.sync_mode}")
        
        if args.github_token:
            logger.info("Would use provided GitHub token for authentication")
        else:
            logger.info("Would use anonymous access (rate limited)")
        
        logger.info("Dry-run simulation complete.")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Dry-run simulation failed: {e}")
        sys.exit(1)


def run_sync_analysis(args, logger):
    """Run synchronous analysis"""
    logger.debug("Initializing synchronous analyzer...")
    analyzer = GitHubRepositoryAnalyzer(token=args.github_token)
    
    return analyzer.analyze_repository(
        repo_url=args.repo_url,
        output_dir=args.output_dir,
        output_format=args.output_format,
        github_token=args.github_token,
        method=args.method,
        verbose=args.verbose,
        fallback=not args.no_fallback,
        async_mode=False  # Explicit sync mode
    )


async def run_async_analysis(args, logger):
    """Run asynchronous analysis (default in v2.0+)"""
    logger.debug("Initializing async analyzer...")
    
    # Use the direct async function for better performance
    return await analyze_repository_async(
        repo_url=args.repo_url,
        output_dir=args.output_dir,
        output_format=args.output_format,
        github_token=args.github_token,
        verbose=args.verbose
    )


def handle_success(result, args, logger):
    """Handle successful analysis completion"""
    logger.success("Repository analysis completed successfully.")
    
    output_dir_path = Path(args.output_dir)
    logger.info(f"Results saved under: {output_dir_path.resolve()}")
    
    # Print brief summary
    if 'metadata' in result:
        metadata = result['metadata']
        logger.info(f"Repository: {metadata.get('repo', 'Unknown')}")
        logger.info(f"Files processed: {metadata.get('files', 0)}")
        logger.info(f"Languages detected: {len(metadata.get('lang', []))}")
        
        if metadata.get('fallback_mode'):
            logger.warning("Analysis completed in fallback mode")
    
    # Show performance info if available
    if 'processing_metadata' in result:
        proc_meta = result['processing_metadata']
        
        if 'processing_time' in proc_meta:
            logger.info(f"Processing time: {proc_meta['processing_time']:.2f}s")
        
        if 'download_method' in proc_meta:
            logger.info(f"Download method used: {proc_meta['download_method']}")
        
        # Show async/sync mode used
        if proc_meta.get('async_mode'):
            logger.info("✅ Async mode used (high performance)")
        elif proc_meta.get('sync_mode'):
            logger.info("🔄 Sync mode used")
    
    sys.exit(0)


def handle_error(error, args, logger):
    """Handle analysis errors"""
    logger.error(f"Analysis failed: {error}")
    
    # Provide helpful error messages
    error_name = type(error).__name__
    
    if error_name == "AuthenticationError":
        logger.error("GitHub authentication failed. Please check your token.")
        logger.info("Get a token at: https://github.com/settings/tokens")
    elif error_name == "RepositoryNotFoundError":
        logger.error("Repository not found or not accessible.")
    elif error_name == "NetworkError":
        logger.error("Network connection failed. Please check your internet connection.")
    elif error_name == "RateLimitExceededError":
        logger.error("GitHub API rate limit exceeded. Please wait or use a token.")
    elif error_name == "RepositoryTooLargeError":
        logger.error("Repository is too large for analysis.")
        logger.info("Try using --method zip for large repositories")
    elif error_name == "ImportError" and "httpx" in str(error):
        logger.error("Async dependencies missing. Install with:")
        logger.info("pip install httpx aiofiles")
        logger.info("Or run with --sync flag to use synchronous mode")
    
    if args.verbose:
        import traceback
        traceback.print_exc()
    
    sys.exit(1)


def check_and_print_features():
    """Check and print available features"""
    print("GitHub Analyzer v1.0.0 Feature Status")
    print("=" * 50)
    print("Author: Han Jun-hee <createbrain2heart@gmail.com>")
    print("Repository: https://github.com/creatorjun/github-analyzer")
    print("Contact: createbrain2heart@gmail.com")
    print()
    
    # Core features
    print("Core Features:")
    print(" ✓ Repository analysis")
    print(" ✓ Multiple output formats")
    print(" ✓ GitHub API integration")
    print(" ✓ Smart fallback mechanisms")
    
    # Async support (now native)
    print(" ✅ Native async processing (v2.0+)")
    print(" ✓ Concurrent downloads")
    print(" ✓ High-performance analysis")
    
    # Dependencies
    print("\nDependency Status:")
    deps_to_check = {
        "requests": "HTTP client (required)",
        "rich": "Rich terminal output (required)", 
        "httpx": "Async HTTP client (required in v2.0+)",
        "aiofiles": "Async file operations (required in v2.0+)",
        "asyncio": "Async runtime (built-in)"
    }
    
    for dep, description in deps_to_check.items():
        try:
            if dep == "asyncio":
                import asyncio
                status = "✅"
            else:
                __import__(dep)
                status = "✅"
        except ImportError:
            status = "❌"
        
        print(f"  {status} {dep} - {description}")
    
    # System info
    print(f"\nSystem Information:")
    print(f"  Python version: {sys.version.split()[0]}")
    print(f"  Platform: {sys.platform}")
    print(f"  Encoding: {sys.getdefaultencoding()}")
    print(f"  Async available: {is_async_available()}")
    
    # Usage recommendations
    print(f"\nRecommended Usage (v2.0+):")
    print(f"  Default: github-analyzer https://github.com/user/repo")
    print(f"  Sync only: github-analyzer https://github.com/user/repo --sync")
    print(f"  With token: github-analyzer https://github.com/user/repo -t YOUR_TOKEN")


if __name__ == "__main__":
    main()