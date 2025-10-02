#!/usr/bin/env python3
"""
GitHub Analyzer - Quick Start Guide
===================================

This file demonstrates various ways to use GitHub Analyzer.
Analyze GitHub repositories and convert them into AI-friendly formats.

Author: Han Jun-hee <createbrain2heart@gmail.com>
Repository: https://github.com/creatorjun/github-analyzer
Contact: +82-010-2435-6344

Prerequisites:
1. pip install py-github-analyzer (install the package)
2. (Optional) Set up GitHub token for API access

Usage:
python quick_start.py
"""

import json
import time
import asyncio
from pathlib import Path
from py_github_analyzer import (
    GitHubRepositoryAnalyzer, 
    analyze_repository,
    get_logger,
    set_verbose,
    is_async_available
)

# Enable verbose logging
set_verbose(True)
logger = get_logger()


def example_1_basic_usage():
    """Example 1: Basic Usage - Simple repository analysis"""
    print("\n" + "="*60)
    print("📚 Example 1: Basic Usage")
    print("="*60)
    
    # Test various URL formats that now work perfectly
    test_urls = [
        "https://github.com/octocat/Hello-World",
        "github.com/octocat/Hello-World",  # Now supported!
        "https://github.com/octocat/Hello-World.git"
    ]
    
    for i, repo_url in enumerate(test_urls, 1):
        print(f"\n🔍 Test {i}: URL Format - {repo_url}")
        print("📋 Testing improved URL parsing capabilities.")
        
        try:
            result = analyze_repository(repo_url)
            if result.get('success'):
                metadata = result['metadata']
                print(f"✅ Analysis completed!")
                print(f"   📁 Repository: {metadata.get('repo', 'Unknown')}")
                print(f"   📊 Files: {metadata.get('files', 0)}")
                print(f"   🔤 Languages: {metadata.get('lang', ['Unknown'])}")
                print(f"   📏 Size: {metadata.get('size', 'Unknown')}")
                if metadata.get('fallback_mode'):
                    print("   ⚠️  Note: Analysis ran in fallback mode")
                return True
            else:
                print(f"   ❌ Failed: {result}")
        except Exception as e:
            print(f"   💥 Error: {e}")
            continue
    return False


def example_2_output_formats():
    """Example 2: Different Output Formats"""
    print("\n" + "="*60)
    print("📋 Example 2: Different Output Formats")
    print("="*60)
    
    repo_url = "https://github.com/github/gitignore"
    formats = [
        ("json", "JSON format (human-readable)"),
        ("bin", "Compressed format (space-efficient)"),
        ("both", "JSON + Compressed (both formats)")
    ]
    for format_type, description in formats:
        print(f"\n🔧 {description}")
        try:
            start_time = time.time()
            result = analyze_repository(
                repo_url=repo_url,
                output_format=format_type,
                output_dir=f"./results_{format_type}",
                verbose=False
            )
            end_time = time.time()
            if result.get('success'):
                print(f"✅ {format_type.upper()} format saved ({end_time-start_time:.1f}s)")
                output_paths = result.get('output_paths', {})
                for file_type, file_path in output_paths.items():
                    if Path(file_path).exists():
                        size = Path(file_path).stat().st_size
                        print(f"   📄 {file_type}: {Path(file_path).name} ({size:,} bytes)")
        except Exception as e:
            print(f"❌ {format_type} format failed: {e}")


def example_3_advanced_options():
    """Example 3: Advanced Options with Smart Fallback"""
    print("\n" + "="*60)
    print("⚙️ Example 3: Advanced Options with Smart Fallback")
    print("="*60)
    repo_url = "https://github.com/creatorjun/github-analyzer.git"
    github_token = None  # Replace with: "your_github_token_here"
    print("🛠️ Running advanced analysis with smart fallback...")
    print("🧠 System will automatically choose best method (ZIP/API) based on rate limits")
    try:
        analyzer = GitHubRepositoryAnalyzer(token=github_token)
        result = analyzer.analyze_repository(
            repo_url=repo_url,
            output_dir="./advanced_results",
            output_format="both",
            method="auto",
            verbose=True,
            fallback=True
        )
        if result.get('success'):
            metadata = result['metadata']
            processing_meta = result.get('processing_metadata', {})
            print("📊 Detailed Analysis Results:")
            print(f"   🏷️  Repository: {metadata.get('repo')}")
            print(f"   📝 Description: {metadata.get('desc', 'No description')[:100]}...")
            print(f"   🔤 Languages: {', '.join(metadata.get('lang', []))}")
            print(f"   📏 Size: {metadata.get('size')}")
            print(f"   📁 Files Processed: {metadata.get('files')}")
            print(f"   🔗 Dependencies: {len(metadata.get('deps', []))}")
            print(f"   📋 Main Files: {len(metadata.get('main', []))}")
            frameworks = metadata.get('frameworks', [])
            if frameworks:
                print(f"   🚀 Frameworks: {', '.join(frameworks)}")
            download_method = processing_meta.get('download_method', 'Unknown')
            print(f"   🔄 Method Used: {download_method}")
            dependencies = metadata.get('deps', [])
            if dependencies:
                print(f"   📦 Top Dependencies: {', '.join(dependencies[:5])}")
            main_files = metadata.get('main', [])
            if main_files:
                print(f"   🎯 Entry Points: {', '.join(main_files[:3])}")
        return True
    except Exception as e:
        print(f"❌ Advanced analysis failed: {e}")
        return False


def example_4_async_features():
    """Example 4: Asynchronous Analysis (High Performance)"""
    print("\n" + "="*60)
    print("🚀 Example 4: Asynchronous Analysis (High Performance)")
    print("="*60)
    if not is_async_available():
        print("❌ Async features not available. All dependencies should be installed by default in v1.0.0+")
        return False
    print("✅ Async features available! Demonstrating high-performance analysis...")
    repositories = [
        "https://github.com/creatorjun/github-analyzer.git",
        "https://github.com/octocat/Hello-World"
    ]
    async def analyze_async_single(repo_url):
        try:
            analyzer = GitHubRepositoryAnalyzer()
            result = await analyzer.analyze_repository_async(
                repo_url=repo_url,
                output_dir="./async_results",
                output_format="json",
                verbose=False
            )
            return result
        except Exception as e:
            return {'success': False, 'error': str(e), 'url': repo_url}
    async def analyze_concurrent():
        print("🔄 Running concurrent analysis...")
        start_time = time.time()
        tasks = [analyze_async_single(url) for url in repositories]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        end_time = time.time()
        print(f"⚡ All analyses completed in {end_time-start_time:.2f} seconds")
        successful = 0
        for i, result in enumerate(results):
            repo_url = repositories[i] if i < len(repositories) else f"Repository {i+1}"
            if isinstance(result, dict) and result.get('success'):
                successful += 1
                metadata = result['metadata']
                print(f"✅ {metadata.get('repo', 'Unknown')}: {metadata.get('files', 0)} files")
            else:
                error_msg = str(result) if not isinstance(result, dict) else result.get('error', 'Unknown error')
                print(f"❌ {repo_url}: {error_msg}")
        print(f"\n📊 Summary: {successful}/{len(repositories)} successful")
        return results
    try:
        results = asyncio.run(analyze_concurrent())
        print("🎉 Async analysis demonstration completed!")
        return True
    except Exception as e:
        print(f"❌ Async analysis failed: {e}")
        return False


def example_5_in_memory_usage():
    """Example 5: In-memory Result Usage (Non-file transmission)"""
    print("\n" + "="*60)
    print("📡 Example 5: In-Memory Result Data Transmission")
    print("="*60)
    repo_url = "https://github.com/octocat/Hello-World"
    print(f"🔍 Analyzing repository in-memory: {repo_url}")
    try:
        result = analyze_repository(
            repo_url=repo_url,
            output_dir="/tmp",    # Minimal output
            output_format="json",
            verbose=False
        )
        # Serialize for transmission (files + metadata only)
        payload = json.dumps({
            "metadata": result.get("metadata"),
            "files": result.get("files")
        }, ensure_ascii=False)
        print(f"🟢 Ready to transmit {len(payload):,} bytes of JSON data (no intermediate files needed!)")
        print("💡 This data can be used for:")
        print("   • REST API responses")
        print("   • WebSocket transmission")
        print("   • Message queue publishing")
        print("   • AI model input preparation")
        print("   • Database storage")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def example_6_programmatic_usage():
    """Example 6: Programmatic Usage with Error Handling"""
    print("\n" + "="*60)
    print("🐍 Example 6: Programmatic Usage")
    print("="*60)
    repositories = [
        "https://github.com/octocat/Hello-World",
        "github.com/github/gitignore",  # No protocol - works!
        "https://github.com/nonexistent/repo123456789"  # Non-existent
    ]
    results = []
    for i, repo_url in enumerate(repositories, 1):
        print(f"\n📋 [{i}/{len(repositories)}] Analyzing: {repo_url}")
        try:
            start_time = time.time()
            result = analyze_repository(
                repo_url=repo_url,
                output_dir=f"./batch_results/repo_{i}",
                output_format="json",
                verbose=False,
                fallback=True
            )
            analysis_time = time.time() - start_time
            if result.get('success'):
                metadata = result.get('metadata', {})
                repo_result = {
                    'url': repo_url,
                    'name': metadata.get('repo', 'Unknown'),
                    'languages': metadata.get('lang', []),
                    'files': metadata.get('files', 0),
                    'size': metadata.get('size', '0KB'),
                    'analysis_time': round(analysis_time, 2),
                    'fallback_mode': metadata.get('fallback_mode', False),
                    'success': True
                }
                results.append(repo_result)
                fallback_note = " (fallback)" if repo_result['fallback_mode'] else ""
                print(f"   ✅ Success ({analysis_time:.1f}s) - {metadata.get('files', 0)} files{fallback_note}")
            else:
                results.append({
                    'url': repo_url,
                    'name': 'Failed',
                    'success': False,
                    'analysis_time': round(analysis_time, 2)
                })
                print(f"   ❌ Failed after {analysis_time:.1f}s")
        except Exception as e:
            print(f"   💥 Exception: {str(e)[:100]}...")
            results.append({
                'url': repo_url,
                'name': 'Error',
                'error': str(e),
                'success': False
            })
    # Summary report
    print(f"\n📈 Batch Analysis Summary:")
    print(f"   Total repositories: {len(repositories)}")
    successful = [r for r in results if r.get('success')]
    print(f"   Successful: {len(successful)}")
    print(f"   Failed: {len(repositories) - len(successful)}")
    if successful:
        avg_time = sum(r['analysis_time'] for r in successful) / len(successful)
        total_files = sum(r.get('files', 0) for r in successful)
        fallback_count = sum(1 for r in successful if r.get('fallback_mode'))
        print(f"   Average time: {avg_time:.1f}s")
        print(f"   Total files processed: {total_files}")
        print(f"   Fallback mode used: {fallback_count} times")
    return results


def example_7_cli_usage():
    """Example 7: Command Line Interface Usage Examples"""
    print("\n" + "="*60)
    print("💻 Example 7: CLI Usage Examples")
    print("="*60)
    print("The GitHub Analyzer provides a powerful command-line interface.")
    print("Here are example commands you can run:\n")
    cli_examples = [
        {
            'command': 'py-github-analyzer https://github.com/octocat/Hello-World',
            'description': 'Basic analysis with smart method selection'
        },
        {
            'command': 'py-github-analyzer github.com/user/repo -f json -v',
            'description': 'JSON output with verbose logging (protocol optional)'
        },
        {
            'command': 'py-github-analyzer https://github.com/user/repo --sync',
            'description': 'Force synchronous mode (async is default)'
        },
        {
            'command': 'py-github-analyzer https://github.com/user/repo -o ./my_results -f both',
            'description': 'Custom output directory with both formats'
        },
        {
            'command': 'py-github-analyzer https://github.com/user/repo -t YOUR_GITHUB_TOKEN',
            'description': 'Using GitHub token for authentication'
        },
        {
            'command': 'pga https://github.com/user/repo -m zip --dry-run',
            'description': 'Dry run with ZIP method and short alias'
        },
        {
            'command': 'py-github-analyzer --check-features',
            'description': 'Check available features and dependencies'
        },
        {
            'command': 'py-github-analyzer --version',
            'description': 'Show version information'
        }
    ]
    for i, example in enumerate(cli_examples, 1):
        print(f"📋 Example {i}: {example['description']}")
        print(f"   $ {example['command']}\n")
    print("💡 Tips:")
    print("   • You can use 'pga' as a shorter alias for 'py-github-analyzer'.")
    print("   • URLs work with or without https:// protocol.")
    print("   • Async processing is enabled by default for better performance.")
    print("   • Smart fallback automatically handles rate limits.")
    print("   • Use -v flag for detailed progress information.")


def example_8_error_handling():
    """Example 8: Error Handling and Best Practices"""
    print("\n" + "="*60)
    print("🛡️ Example 8: Error Handling Best Practices")
    print("="*60)
    error_scenarios = [
        ("Invalid URL", "totally-invalid-url"),
        ("Missing Protocol (Now Supported!)", "github.com/octocat/Hello-World"),
        ("Non-existent Repository", "https://github.com/user/nonexistent999999")
    ]
    for scenario_name, repo_url in error_scenarios:
        print(f"\n🧪 Testing: {scenario_name}")
        print(f"   URL: {repo_url}")
        try:
            result = analyze_repository(
                repo_url=repo_url,
                output_dir="./error_test",
                verbose=False,
                fallback=True
            )
            if result.get('success'):
                if result.get('metadata', {}).get('fallback_mode'):
                    print("   ✅ Succeeded with smart fallback mode")
                else:
                    print("   ✅ Succeeded normally")
            else:
                print("   ❌ Failed even with fallback")
        except Exception as e:
            print(f"   💥 Exception caught: {type(e).__name__}")
            print(f"      Message: {str(e)[:100]}...")
    print("\n💡 Best Practices for Error Handling:")
    print("   • Always enable fallback mode for production use")
    print("   • Wrap analysis calls in try-except blocks")
    print("   • Check result['success'] before processing")
    print("   • Use GitHub tokens to avoid rate limiting")


def main():
    print("🚀 GitHub Analyzer (py-github-analyzer) v1.0.0 - Quick Start Examples")
    print("=" * 60)
    print("Author: Han Jun-hee <createbrain2heart@gmail.com>")
    print("Repository: https://github.com/creatorjun/github-analyzer")
    print("Contact: +82-010-2435-6344")
    print()
    print("This script demonstrates various ways to use the analyzer.")
    async_status = "✅ Available" if is_async_available() else "❌ Not available"
    print(f"Async features: {async_status}")
    print()
    examples = [
        ("Basic Usage", example_1_basic_usage),
        ("Output Formats", example_2_output_formats),
        ("Advanced Options", example_3_advanced_options),
        ("Async Features", example_4_async_features),
        ("In-Memory Transmission", example_5_in_memory_usage),
        ("Programmatic Usage", example_6_programmatic_usage),
        ("CLI Usage", example_7_cli_usage),
        ("Error Handling", example_8_error_handling)
    ]
    print("Available examples:")
    for i, (name, _) in enumerate(examples, 1):
        if i == 4 and not is_async_available():
            print(f"  {i}. {name} [⚠️  Dependencies missing]")
        else:
            print(f"  {i}. {name}")
    print("\nChoose an example to run:")
    print("  • Enter a number (1-8) to run a specific example")
    print("  • Enter 'all' to run all examples")
    print("  • Enter 'quit' to exit")
    while True:
        try:
            choice = input("\nYour choice: ").strip().lower()
            if choice == 'quit':
                print("👋 Thanks for using the analyzer!")
                break
            elif choice == 'all':
                print("\n🏃 Running all examples...")
                for name, func in examples:
                    print(f"\n🎯 Running: {name}")
                    try:
                        func()
                    except KeyboardInterrupt:
                        print("\n⏹️ Interrupted by user")
                        break
                    except Exception as e:
                        print(f"❌ Example failed: {e}")
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(examples):
                idx = int(choice) - 1
                name, func = examples[idx]
                print(f"\n🎯 Running: {name}")
                func()
            else:
                print(f"❌ Invalid choice. Please enter 1-{len(examples)}, 'all', or 'quit'")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()