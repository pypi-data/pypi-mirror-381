"""Scan result data model"""

from dataclasses import dataclass, field
from vulnguard.models.issue import SecurityIssue


@dataclass
class ScanResult:
    """Results from a security scan"""
    
    repository_path: str
    issues: list[SecurityIssue] = field(default_factory=list)
    files_scanned: int = 0
    scan_time_seconds: float = 0.0
    
    @property
    def critical_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity.value == "critical")
    
    @property
    def high_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity.value == "high")
    
    @property
    def medium_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity.value == "medium")
    
    @property
    def low_count(self) -> int:
        return sum(1 for issue in self.issues if issue.severity.value == "low")
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "repository_path": self.repository_path,
            "issues": [issue.to_dict() for issue in self.issues],
            "files_scanned": self.files_scanned,
            "scan_time_seconds": self.scan_time_seconds,
            "summary": {
                "total": len(self.issues),
                "critical": self.critical_count,
                "high": self.high_count,
                "medium": self.medium_count,
                "low": self.low_count,
            }
        }
