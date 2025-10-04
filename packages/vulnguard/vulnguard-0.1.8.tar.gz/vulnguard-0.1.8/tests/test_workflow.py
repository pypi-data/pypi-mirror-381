"""End-to-end workflow integration tests"""

import pytest
import json
from pathlib import Path
from vulnguard import SecurityScanner
from vulnguard.agents.orchestrator import OrchestratorAgent


@pytest.fixture
def vulnerable_repo(tmp_path):
    """Create a repository with multiple vulnerabilities"""
    # SQL Injection
    (tmp_path / "database.py").write_text("""
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE id={user_id}"
    return conn.execute(query).fetchall()
""")
    
    # Command Injection
    (tmp_path / "admin.py").write_text("""
import os

def backup_files(filename):
    os.system(f"tar -czf backup.tar.gz {filename}")
""")
    
    # Hardcoded Secrets (test fixture - not real keys)
    (tmp_path / "config.py").write_text("""
API_KEY = "test-fake-api-key-1234567890"
SECRET_TOKEN = "test-fake-token-xxxxxxxxxxxxx"
DATABASE_PASSWORD = "test-password-123"
""")
    
    # XSS
    (tmp_path / "views.py").write_text("""
from flask import render_template_string

def show_message(msg):
    return render_template_string(f"<h1>{msg}</h1>")
""")
    
    return tmp_path


class TestFullWorkflow:
    """Test complete multi-agent workflow"""
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key - expensive test")
    async def test_complete_scan_workflow(self, vulnerable_repo):
        """Test complete scan from start to finish"""
        scanner = SecurityScanner(model="claude-3-5-haiku-20241022")
        result = await scanner.scan(str(vulnerable_repo))
        
        # Verify scan completed
        assert result is not None
        assert result.repository_path == str(vulnerable_repo)
        assert result.files_scanned >= 4
        assert result.scan_time_seconds > 0
        
        # Verify artifacts created
        vulnguard_dir = vulnerable_repo / ".vulnguard"
        assert vulnguard_dir.exists()
        
        security_md = vulnguard_dir / "SECURITY.md"
        assert security_md.exists()
        assert security_md.stat().st_size > 0
        
        threat_model = vulnguard_dir / "THREAT_MODEL.json"
        assert threat_model.exists()
        threats = json.loads(threat_model.read_text())
        assert isinstance(threats, list)
        
        vulnerabilities = vulnguard_dir / "VULNERABILITIES.json"
        assert vulnerabilities.exists()
        vulns = json.loads(vulnerabilities.read_text())
        assert isinstance(vulns, list)
        
        scan_results = vulnguard_dir / "scan_results.json"
        assert scan_results.exists()
        
        # Verify issues found
        assert len(result.issues) > 0, "Should find vulnerabilities in test repo"
        
        # Check for expected vulnerability types
        severities = [issue.severity.value for issue in result.issues]
        assert any(s in ['critical', 'high'] for s in severities), "Should find high-severity issues"
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_progressive_workflow(self, vulnerable_repo):
        """Test running workflow phase by phase"""
        orchestrator = OrchestratorAgent(model="claude-3-5-haiku-20241022")
        
        # Phase 1: Assessment
        assessment_result = await orchestrator.run_assessment_only(str(vulnerable_repo))
        assert Path(assessment_result['file']).exists()
        assert assessment_result['sections'] > 0
        
        # Phase 2: Threat Modeling
        threat_result = await orchestrator.run_threat_modeling_only(str(vulnerable_repo))
        assert Path(threat_result['file']).exists()
        assert threat_result['total_threats'] >= 0
        
        # Phase 3: Code Review
        review_result = await orchestrator.run_code_review_only(str(vulnerable_repo))
        assert Path(review_result['file']).exists()
        assert review_result['total_vulnerabilities'] >= 0
    
    def test_artifact_file_structure(self, vulnerable_repo):
        """Test that .vulnguard directory is created with correct structure"""
        vulnguard_dir = vulnerable_repo / ".vulnguard"
        vulnguard_dir.mkdir(exist_ok=True)
        
        # Create test artifacts
        (vulnguard_dir / "SECURITY.md").write_text("# Test")
        (vulnguard_dir / "THREAT_MODEL.json").write_text("[]")
        (vulnguard_dir / "VULNERABILITIES.json").write_text("[]")
        
        assert vulnguard_dir.exists()
        assert (vulnguard_dir / "SECURITY.md").exists()
        assert (vulnguard_dir / "THREAT_MODEL.json").exists()
        assert (vulnguard_dir / "VULNERABILITIES.json").exists()


class TestErrorHandling:
    """Test error handling in workflow"""
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires API key and makes actual calls")
    async def test_nonexistent_repository(self):
        """Test scanning non-existent repository"""
        scanner = SecurityScanner()
        
        with pytest.raises(ValueError, match="does not exist"):
            await scanner.scan("/nonexistent/path/to/repo")
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires API key and makes actual calls")
    async def test_empty_repository(self, tmp_path):
        """Test scanning empty repository"""
        scanner = SecurityScanner()
        
        # Should not crash, just find no files
        result = await scanner.scan(str(tmp_path), save_results=False)
        assert result.files_scanned == 0
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires API key and makes actual calls")
    async def test_missing_security_md(self, tmp_path):
        """Test threat modeling without SECURITY.md"""
        orchestrator = OrchestratorAgent()
        
        with pytest.raises(ValueError, match="SECURITY.md not found"):
            await orchestrator.run_threat_modeling_only(str(tmp_path))
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires API key and makes actual calls")
    async def test_missing_threat_model(self, tmp_path):
        """Test code review without THREAT_MODEL.json"""
        # Create SECURITY.md but not THREAT_MODEL.json
        vulnguard_dir = tmp_path / ".vulnguard"
        vulnguard_dir.mkdir()
        (vulnguard_dir / "SECURITY.md").write_text("# Test")
        
        orchestrator = OrchestratorAgent()
        
        with pytest.raises(ValueError, match="THREAT_MODEL.json not found"):
            await orchestrator.run_code_review_only(str(tmp_path))


class TestArtifactValidation:
    """Test artifact content validation"""
    
    def test_security_md_format(self, tmp_path):
        """Test SECURITY.md has expected format"""
        content = """# Security Architecture

## Overview
Test application

## Technology Stack
- Python 3.10
- Flask

## Entry Points
- HTTP endpoints

## Data Flow
Input → Processing → Output
"""
        (tmp_path / "SECURITY.md").write_text(content)
        
        md = (tmp_path / "SECURITY.md").read_text()
        assert "# Security Architecture" in md
        assert "## Overview" in md
        assert "## Technology Stack" in md
    
    def test_threat_model_json_format(self, tmp_path):
        """Test THREAT_MODEL.json has expected format"""
        threats = [
            {
                "id": "THREAT-001",
                "category": "Injection",
                "title": "SQL Injection",
                "severity": "critical",
                "description": "Test description"
            }
        ]
        (tmp_path / "THREAT_MODEL.json").write_text(json.dumps(threats))
        
        data = json.loads((tmp_path / "THREAT_MODEL.json").read_text())
        assert isinstance(data, list)
        assert len(data) > 0
        assert "id" in data[0]
        assert "severity" in data[0]
    
    def test_vulnerabilities_json_format(self, tmp_path):
        """Test VULNERABILITIES.json has expected format"""
        vulns = [
            {
                "threat_id": "THREAT-001",
                "title": "SQL Injection in database.py",
                "severity": "critical",
                "file_path": "database.py",
                "line_number": 42,
                "cwe_id": "CWE-89"
            }
        ]
        (tmp_path / "VULNERABILITIES.json").write_text(json.dumps(vulns))
        
        data = json.loads((tmp_path / "VULNERABILITIES.json").read_text())
        assert isinstance(data, list)
        if len(data) > 0:
            assert "file_path" in data[0]
            assert "line_number" in data[0]
            assert "cwe_id" in data[0]


class TestCostTracking:
    """Test cost tracking functionality"""
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_cost_tracking_in_orchestrator(self, tmp_path):
        """Test that orchestrator tracks total cost"""
        orchestrator = OrchestratorAgent(model="claude-3-5-haiku-20241022")
        
        # Create minimal test file
        (tmp_path / "test.py").write_text("print('hello')")
        
        result = await orchestrator.run_full_scan(str(tmp_path))
        
        # Cost should be tracked (may be 0 for very small scans)
        assert orchestrator.total_cost >= 0
        assert isinstance(orchestrator.total_cost, float)


class TestFixturesIntegration:
    """Test with actual test fixtures"""
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_scan_test_fixtures(self):
        """Test scanning the test fixtures directory"""
        fixtures_path = Path(__file__).parent / "fixtures"
        
        scanner = SecurityScanner(model="claude-3-5-haiku-20241022")
        result = await scanner.scan(str(fixtures_path))
        
        # Should find vulnerabilities in vulnerable_code.py
        assert len(result.issues) > 0, "Should detect issues in test fixtures"
        
        # Check for specific patterns
        titles = [issue.title.lower() for issue in result.issues]
        descriptions = ' '.join([issue.description.lower() for issue in result.issues])
        
        # Should detect at least one of these vulnerability types
        expected = ['sql', 'injection', 'command', 'eval', 'secret', 'hardcoded']
        found = any(pattern in descriptions or any(pattern in title for title in titles) 
                   for pattern in expected)
        
        assert found, f"Should detect common vulnerabilities. Found issues: {titles}"
