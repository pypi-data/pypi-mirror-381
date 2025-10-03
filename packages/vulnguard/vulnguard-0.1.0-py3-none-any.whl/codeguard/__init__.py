"""
CodeGuard - AI-powered code security scanner
"""

from codeguard.scanner.analyzer import SecurityScanner
from codeguard.models.issue import SecurityIssue, Severity
from codeguard.models.result import ScanResult

__version__ = "0.1.0"

__all__ = [
    "SecurityScanner",
    "SecurityIssue",
    "Severity",
    "ScanResult",
]
