"""Tests for CodeReviewAgent JSON parsing"""

import json
import pytest
from vulnguard.agents.code_review import CodeReviewAgent


@pytest.fixture
def code_review_agent():
    """Create CodeReviewAgent instance"""
    return CodeReviewAgent(api_key="test-key")


def test_extract_json_pure_array(code_review_agent):
    """Test extracting pure JSON array"""
    response = '[{"threat_id": "THREAT-001", "title": "Test"}]'
    
    result = code_review_agent._extract_json_robust(response)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]['threat_id'] == 'THREAT-001'


def test_extract_json_with_code_block(code_review_agent):
    """Test extracting JSON from markdown code block"""
    response = '''
Here are my findings:

```json
[
  {
    "threat_id": "THREAT-001",
    "title": "SQL Injection"
  }
]
```

That's all.
'''
    
    result = code_review_agent._extract_json_robust(response)
    
    assert isinstance(result, list)
    assert len(result) == 1


def test_extract_json_with_surrounding_text(code_review_agent):
    """Test extracting JSON with surrounding narrative"""
    response = '''
I found the following vulnerabilities:

[
  {
    "threat_id": "THREAT-001",
    "title": "XSS"
  }
]

This completes my analysis.
'''
    
    result = code_review_agent._extract_json_robust(response)
    
    assert isinstance(result, list)
    assert len(result) == 1


def test_extract_json_empty_array(code_review_agent):
    """Test extracting empty array"""
    response = '[]'
    
    result = code_review_agent._extract_json_robust(response)
    
    assert isinstance(result, list)
    assert len(result) == 0


def test_extract_json_narrative_only(code_review_agent):
    """Test handling pure narrative (no JSON)"""
    response = "I'll systematically validate each threat..."
    
    result = code_review_agent._extract_json_robust(response)
    
    assert isinstance(result, list)
    assert len(result) == 0


def test_validate_vulnerabilities_complete(code_review_agent):
    """Test validating complete vulnerabilities"""
    vulns = [
        {
            'threat_id': 'THREAT-001',
            'title': 'SQL Injection',
            'description': 'Test description',
            'severity': 'critical',
            'file_path': 'views.py',
            'line_number': 42,
            'code_snippet': 'query = ...',
            'cwe_id': 'CWE-89',
            'recommendation': 'Use parameterized queries'
        }
    ]
    
    result = code_review_agent._validate_vulnerabilities(vulns)
    
    assert len(result) == 1
    assert result[0]['threat_id'] == 'THREAT-001'


def test_validate_vulnerabilities_missing_fields(code_review_agent):
    """Test validating vulnerabilities with missing fields"""
    vulns = [
        {
            'threat_id': 'THREAT-001',
            'title': 'SQL Injection',
            # Missing required fields
        }
    ]
    
    result = code_review_agent._validate_vulnerabilities(vulns)
    
    assert len(result) == 0


def test_validate_vulnerabilities_invalid_severity(code_review_agent):
    """Test normalizing invalid severity"""
    vulns = [
        {
            'threat_id': 'THREAT-001',
            'title': 'Test',
            'description': 'Test',
            'severity': 'SUPER_CRITICAL',  # Invalid
            'file_path': 'test.py',
            'line_number': 1,
            'code_snippet': '',
            'cwe_id': '',
            'recommendation': ''
        }
    ]
    
    result = code_review_agent._validate_vulnerabilities(vulns)
    
    assert result[0]['severity'] == 'medium'


def test_staged_output_parsing(code_review_agent):
    """Test parsing staged output format"""
    response = '''
I'm investigating threat THREAT-001...

Using Read tool to check views.py...

Found SQL injection at line 157.

===INVESTIGATION COMPLETE===

[
  {
    "threat_id": "THREAT-001",
    "title": "SQL Injection",
    "description": "Test",
    "severity": "critical",
    "file_path": "views.py",
    "line_number": 157,
    "code_snippet": "query = ...",
    "cwe_id": "CWE-89",
    "recommendation": "Fix it"
  }
]
'''
    
    # Test the marker split
    assert '===INVESTIGATION COMPLETE===' in response
    parts = response.split('===INVESTIGATION COMPLETE===')
    assert len(parts) == 2
    assert 'investigating' in parts[0]
    assert '"threat_id"' in parts[1]
