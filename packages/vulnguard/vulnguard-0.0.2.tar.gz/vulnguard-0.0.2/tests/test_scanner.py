"""Tests for scanner"""

import pytest
from pathlib import Path
from vulnguard.scanner.analyzer import SecurityScanner


@pytest.mark.asyncio
async def test_scanner_invalid_path():
    """Test scanner with invalid path"""
    scanner = SecurityScanner()
    
    with pytest.raises(ValueError, match="does not exist"):
        await scanner.scan("/nonexistent/path")


def test_scanner_creation():
    """Test creating a SecurityScanner"""
    scanner = SecurityScanner()
    assert scanner is not None
    assert scanner.claude is not None


def test_count_code_files(tmp_path):
    """Test counting code files"""
    # Create test files
    (tmp_path / "test.py").touch()
    (tmp_path / "test.js").touch()
    (tmp_path / "README.md").touch()
    (tmp_path / "test.txt").touch()
    
    scanner = SecurityScanner()
    count = scanner._count_code_files(tmp_path)
    
    # Should count .py and .js, not .md or .txt
    assert count == 2
