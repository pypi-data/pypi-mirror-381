"""Tests for context gatherer"""

import pytest
from pathlib import Path
from vulnguard.scanner.context_gatherer import ContextGatherer


@pytest.fixture
def sample_threat_model():
    """Sample threat model for testing"""
    return [
        {
            'id': 'THREAT-001',
            'title': 'SQL Injection',
            'description': 'SQL injection vulnerability in login',
            'severity': 'critical',
            'affected_components': [
                'introduction/views.py::sql_lab (line 157)'
            ],
            'vulnerability_types': ['CWE-89']
        },
        {
            'id': 'THREAT-002',
            'title': 'Command Injection',
            'description': 'Command injection in cmd_lab',
            'severity': 'critical',
            'affected_components': [
                'introduction/views.py::cmd_lab (line 423)'
            ],
            'vulnerability_types': ['CWE-78']
        }
    ]


def test_context_gatherer_initialization(tmp_path):
    """Test ContextGatherer initialization"""
    gatherer = ContextGatherer(str(tmp_path))
    assert gatherer.repo_path == tmp_path


def test_get_surrounding_lines(tmp_path):
    """Test getting surrounding lines"""
    test_file = tmp_path / "test.py"
    content = "\n".join([f"line {i}" for i in range(1, 21)])
    test_file.write_text(content)
    
    gatherer = ContextGatherer(str(tmp_path))
    result = gatherer._get_surrounding_lines(test_file, 10, context_lines=3)
    
    assert result['target_line'] == 10
    assert 'line 7' in result['lines']
    assert 'line 10' in result['lines']
    assert 'line 13' in result['lines']


def test_get_function_definition(tmp_path):
    """Test extracting function definition"""
    test_file = tmp_path / "test.py"
    test_file.write_text('''
def vulnerable_function(user_input):
    """A vulnerable function"""
    query = f"SELECT * FROM users WHERE name='{user_input}'"
    return execute_query(query)
''')
    
    gatherer = ContextGatherer(str(tmp_path))
    result = gatherer._get_function_definition(test_file, 'vulnerable_function')
    
    assert 'vulnerable_function' in result['source']
    assert result['start_line'] > 0
    assert 'user_input' in result.get('parameters', [])


def test_get_file_imports(tmp_path):
    """Test extracting imports"""
    test_file = tmp_path / "test.py"
    test_file.write_text('''
import os
import sys
from pathlib import Path
from typing import Dict, List
''')
    
    gatherer = ContextGatherer(str(tmp_path))
    imports = gatherer._get_file_imports(test_file)
    
    assert 'os' in imports
    assert 'sys' in imports
    assert 'pathlib' in imports
    assert 'typing' in imports


def test_analyze_data_flow(tmp_path):
    """Test data flow analysis"""
    test_file = tmp_path / "test.py"
    test_file.write_text('''
def process():
    user_input = request.GET['data']
    sanitized = clean(user_input)
    result = query_db(sanitized)
    return result
''')
    
    gatherer = ContextGatherer(str(tmp_path))
    # Line 4 is: sanitized = clean(user_input)
    flow = gatherer._analyze_data_flow(test_file, 'process', 4)
    
    assert 'variables' in flow
    assert 'sources' in flow


def test_extract_config_keywords():
    """Test config keyword extraction"""
    gatherer = ContextGatherer('.')
    
    threat = {
        'description': 'SQL injection vulnerability allows database access'
    }
    
    keywords = gatherer._extract_config_keywords(threat)
    
    assert 'DEBUG' in keywords
    assert 'SECRET' in keywords
    assert 'DATABASE' in keywords or 'DB_' in keywords


def test_comprehensive_context_gathering(tmp_path, sample_threat_model):
    """Test full context gathering"""
    # Create minimal file structure
    views_dir = tmp_path / "introduction"
    views_dir.mkdir()
    
    views_file = views_dir / "views.py"
    views_file.write_text('''
def sql_lab(request):
    name = request.POST.get('name')
    query = f"SELECT * FROM users WHERE name='{name}'"
    return execute(query)

def cmd_lab(request):
    domain = request.POST.get('domain')
    result = subprocess.run(f"ping {domain}", shell=True)
    return result
''')
    
    gatherer = ContextGatherer(str(tmp_path))
    evidence = gatherer.gather_comprehensive_context(sample_threat_model)
    
    assert 'THREAT-001' in evidence
    assert 'THREAT-002' in evidence
    assert len(evidence['THREAT-001']) > 0
    assert len(evidence['THREAT-002']) > 0
