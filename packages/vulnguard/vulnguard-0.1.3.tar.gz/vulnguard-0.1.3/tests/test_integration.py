"""Integration tests with vulnerable code fixtures"""

import pytest
from pathlib import Path
from vulnguard.scanner.analyzer import SecurityScanner


@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires Claude API key - run manually")
async def test_scan_vulnerable_code():
    """Test scanner can detect vulnerabilities in test fixture"""
    scanner = SecurityScanner()
    
    # Point to the fixtures directory
    fixtures_path = Path(__file__).parent / "fixtures"
    
    result = await scanner.scan(str(fixtures_path))
    
    # Should find issues in vulnerable_code.py
    assert len(result.issues) > 0, "Should detect vulnerabilities in test fixture"
    
    # Check for specific vulnerability types
    issue_titles = [issue.title.lower() for issue in result.issues]
    
    # Should detect at least some of these
    expected_patterns = ['sql', 'injection', 'command', 'secret', 'eval', 'path']
    found_patterns = [p for p in expected_patterns if any(p in title for title in issue_titles)]
    
    assert len(found_patterns) > 0, f"Should detect common vulnerability patterns. Found: {issue_titles}"
    
    print(f"\n✅ Detected {len(result.issues)} issues")
    for issue in result.issues:
        print(f"  - [{issue.severity.value}] {issue.title}")


def test_scanner_counts_files_correctly():
    """Test file counting works correctly"""
    scanner = SecurityScanner()
    
    fixtures_path = Path(__file__).parent / "fixtures"
    count = scanner._count_code_files(fixtures_path)
    
    # Should count vulnerable_code.py
    assert count >= 1, "Should count at least the vulnerable_code.py file"
