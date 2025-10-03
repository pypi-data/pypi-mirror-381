# VulnGuard

AI-powered code security scanner using Claude Agent SDK.

## Installation

```bash
pip install vulnguard
```

## Setup

Set your Claude API key:

```bash
export CLAUDE_API_KEY="sk-ant-your-key-here"
```

Get your API key from: https://console.anthropic.com/

## Usage

### CLI

```bash
# Scan current directory
vulnguard scan .

# Scan specific project
vulnguard scan /path/to/project

# Output as JSON
vulnguard scan . --format json --output results.json

# Filter by severity
vulnguard scan . --severity high
```

### Python API

```python
import asyncio
from vulnguard import SecurityScanner

async def main():
    scanner = SecurityScanner()
    result = await scanner.scan("/path/to/repo")
    
    print(f"Found {len(result.issues)} security issues")
    for issue in result.issues:
        print(f"- [{issue.severity.value}] {issue.title} in {issue.file_path}")

asyncio.run(main())
```

## License

AGPL-3.0
