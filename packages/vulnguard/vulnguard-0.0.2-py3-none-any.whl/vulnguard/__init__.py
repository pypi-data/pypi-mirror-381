"""
VulnGuard - AI-powered code security scanner
"""

from vulnguard.scanner.analyzer import SecurityScanner
from vulnguard.models.issue import SecurityIssue, Severity
from vulnguard.models.result import ScanResult

__version__ = "0.1.7"

__all__ = [
    "SecurityScanner",
    "SecurityIssue",
    "Severity",
    "ScanResult",
]
