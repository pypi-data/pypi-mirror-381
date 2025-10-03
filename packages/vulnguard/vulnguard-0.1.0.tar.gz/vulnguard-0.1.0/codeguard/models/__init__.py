"""Data models for CodeGuard"""

from codeguard.models.issue import SecurityIssue, Severity
from codeguard.models.result import ScanResult

__all__ = ["SecurityIssue", "Severity", "ScanResult"]
