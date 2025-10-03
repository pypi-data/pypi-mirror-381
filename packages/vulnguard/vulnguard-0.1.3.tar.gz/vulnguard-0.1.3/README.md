# VulnGuard

AI-powered code security scanner using Claude AI.

## Installation

```bash
pip install vulnguard
```

## Usage

```python
from vulnguard import SecurityScanner

scanner = SecurityScanner()
result = await scanner.scan("/path/to/repo")

print(f"Found {len(result.issues)} security issues")
for issue in result.issues:
    print(f"- [{issue.severity.value}] {issue.title} in {issue.file_path}")
```

## License

AGPL-3.0
