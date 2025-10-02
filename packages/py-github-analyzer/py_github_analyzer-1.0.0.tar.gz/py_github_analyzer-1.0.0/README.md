GitHub Analyzer v1.0.0 🚀
Advanced GitHub repository analyzer with AI-optimized code extraction and metadata generation.

✨ Features
🚀 Fast Analysis: Async/sync repository analysis

🧠 AI-Optimized: Compressed output format for LLM processing

📊 Rich Metadata: Language detection, dependency extraction

🔄 Multiple Formats: JSON, Binary, Both

⚡ CLI Support: Command-line interface

🛡️ Robust: Error handling, rate limiting, fallbacks

🔧 Installation
Bash

pip install py-github-analyzer
🚀 Quick Start
Python API
Python

from py_github_analyzer import analyze_repository

# Simple analysis
result = analyze_repository('https://github.com/user/repo')
print(f"Files: {result['metadata']['files']}")
print(f"Languages: {result['metadata']['lang']}")

# Async analysis
import asyncio
from py_github_analyzer import analyze_repository_async

async def main():
    result = await analyze_repository_async('https://github.com/user/repo')
    print(f"Analysis complete: {result['metadata']['files']} files")

asyncio.run(main())
Command Line
Bash

# Basic usage
py-github-analyzer https://github.com/user/repo

# With options
py-github-analyzer https://github.com/user/repo --output ./results --format json --token YOUR_GITHUB_TOKEN --verbose

# Short form
pga https://github.com/user/repo -f both -v
📖 Documentation
Configuration
You can set your GitHub token as an environment variable for convenience.

Python

import os
os.environ['GITHUB_TOKEN'] = 'your_github_token_here'
Output Formats
json: Human-readable JSON format

bin: Compressed binary format (recommended for AI)

both: Both formats

Advanced Usage
Python

from py_github_analyzer import GitHubRepositoryAnalyzer

analyzer = GitHubRepositoryAnalyzer(token='your_token')
result = analyzer.analyze_repository(
    repo_url='https://github.com/user/repo',
    output_dir='./custom_output',
    output_format='both'
)
🤝 Contributing
Contributions welcome! Please read our contributing guidelines.

📄 License
MIT License - see LICENSE file for details.

👨‍💻 Author
Han Jun-hee (createbrain2heart@gmail.com)

GitHub: @creatorjun