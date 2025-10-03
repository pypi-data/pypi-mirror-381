# CodeGuard Core

Core scanning engine for CodeGuard - AI-powered code security scanner.

See main [README](../../README.md) for full documentation.

## Installation

```bash
pip install codeguard
```

## Usage

```python
from codeguard import SecurityScanner

scanner = SecurityScanner()
result = await scanner.scan("/path/to/repo")

print(f"Found {len(result.issues)} security issues")
for issue in result.issues:
    print(f"- [{issue.severity.value}] {issue.title} in {issue.file_path}")
```

## License

AGPL-3.0
