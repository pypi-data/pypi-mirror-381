"""Data models for CodeGuard"""

from vulnguard.models.issue import SecurityIssue, Severity
from vulnguard.models.result import ScanResult

__all__ = ["SecurityIssue", "Severity", "ScanResult"]
