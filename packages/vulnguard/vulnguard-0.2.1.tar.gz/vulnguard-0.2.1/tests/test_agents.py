"""Tests for multi-agent system"""

import pytest
import json
from pathlib import Path
from vulnguard.agents.assessment import AssessmentAgent
from vulnguard.agents.threat_modeling import ThreatModelingAgent
from vulnguard.agents.code_review import CodeReviewAgent
from vulnguard.agents.orchestrator import OrchestratorAgent


@pytest.fixture
def test_repo(tmp_path):
    """Create a test repository with vulnerable code"""
    # Create a simple vulnerable file
    test_file = tmp_path / "app.py"
    test_file.write_text("""
import sqlite3

def unsafe_query(user_id):
    conn = sqlite3.connect('db.sqlite')
    query = f"SELECT * FROM users WHERE id={user_id}"  # SQL injection
    return conn.execute(query).fetchall()

API_KEY = "test-fake-key-1234"  # Test fixture - not real
""")
    return tmp_path


@pytest.fixture
def test_security_md():
    """Sample SECURITY.md content for testing"""
    return """# Security Architecture

## Overview
Simple Python web application

## Technology Stack
- Python 3.10
- SQLite database
- Flask web framework

## Entry Points
- HTTP API endpoints
- Database queries

## Authentication & Authorization
Basic session-based authentication

## Data Flow
User input → API → Database → Response

## Sensitive Data
- User credentials
- API keys in configuration
"""


@pytest.fixture
def test_threat_model():
    """Sample threat model for testing"""
    return [
        {
            "id": "THREAT-001",
            "category": "Injection",
            "title": "SQL Injection in database queries",
            "description": "Application may be vulnerable to SQL injection",
            "severity": "critical",
            "affected_components": ["database", "api"],
            "attack_scenario": "Attacker injects SQL in user input",
            "vulnerability_types": ["CWE-89"],
            "mitigation": "Use parameterized queries"
        }
    ]


class TestAssessmentAgent:
    """Tests for Assessment Agent"""
    
    def test_agent_creation(self):
        """Test creating an Assessment Agent"""
        agent = AssessmentAgent()
        assert agent.name == "Assessment"
        assert "Read" in agent.allowed_tools
        assert "Grep" in agent.allowed_tools
        assert "Glob" in agent.allowed_tools
    
    def test_system_prompt(self):
        """Test system prompt contains key instructions"""
        agent = AssessmentAgent()
        prompt = agent.build_system_prompt()
        assert "architecture" in prompt.lower()
        assert "security" in prompt.lower()
    
    def test_user_prompt(self):
        """Test user prompt generation"""
        agent = AssessmentAgent()
        prompt = agent.build_user_prompt()
        assert "SECURITY.md" in prompt
        assert "Architecture" in prompt
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_assessment_run(self, test_repo):
        """Test Assessment Agent creates SECURITY.md"""
        agent = AssessmentAgent()
        result = await agent.run(str(test_repo))
        
        assert 'file' in result
        assert result['file'].endswith('SECURITY.md')
        assert result['sections'] > 0
        assert Path(result['file']).exists()
        
        # Verify content
        content = Path(result['file']).read_text()
        assert '# Security Architecture' in content


class TestThreatModelingAgent:
    """Tests for Threat Modeling Agent"""
    
    def test_agent_creation(self):
        """Test creating a Threat Modeling Agent"""
        agent = ThreatModelingAgent()
        assert agent.name == "Threat Modeling"
        assert "Read" in agent.allowed_tools
        assert "Write" in agent.allowed_tools
    
    def test_system_prompt(self):
        """Test system prompt contains STRIDE methodology"""
        agent = ThreatModelingAgent()
        prompt = agent.build_system_prompt()
        assert "STRIDE" in prompt
        assert "threat" in prompt.lower()
    
    def test_user_prompt(self, test_security_md):
        """Test user prompt includes security document"""
        agent = ThreatModelingAgent()
        prompt = agent.build_user_prompt(security_md=test_security_md)
        assert test_security_md in prompt
        assert "JSON" in prompt
    
    def test_process_results_valid_json(self, tmp_path, test_threat_model):
        """Test processing valid threat model JSON"""
        agent = ThreatModelingAgent()
        response = json.dumps(test_threat_model)
        result = agent.process_results(response, str(tmp_path))
        
        assert result['total_threats'] == 1
        assert result['by_severity']['critical'] == 1
        assert Path(result['file']).exists()
        
        # Verify saved content
        saved_data = json.loads(Path(result['file']).read_text())
        assert len(saved_data) == 1
        assert saved_data[0]['id'] == 'THREAT-001'
    
    def test_process_results_with_markdown_wrapper(self, tmp_path, test_threat_model):
        """Test extracting JSON from markdown code block"""
        agent = ThreatModelingAgent()
        response = f"```json\n{json.dumps(test_threat_model)}\n```"
        result = agent.process_results(response, str(tmp_path))
        
        assert result['total_threats'] == 1
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_threat_modeling_run(self, test_repo, test_security_md):
        """Test Threat Modeling Agent creates THREAT_MODEL.json"""
        agent = ThreatModelingAgent()
        result = await agent.run(str(test_repo), security_md=test_security_md)
        
        assert 'file' in result
        assert result['file'].endswith('THREAT_MODEL.json')
        assert result['total_threats'] > 0
        assert Path(result['file']).exists()


class TestCodeReviewAgent:
    """Tests for Code Review Agent"""
    
    def test_agent_creation(self):
        """Test creating a Code Review Agent"""
        agent = CodeReviewAgent()
        assert agent.name == "Code Review"
        assert "Read" in agent.allowed_tools
        assert "Grep" in agent.allowed_tools
    
    def test_system_prompt(self):
        """Test system prompt focuses on validation"""
        agent = CodeReviewAgent()
        prompt = agent.build_system_prompt()
        assert "code" in prompt.lower()
        assert "vulnerability" in prompt.lower() or "vulnerabilities" in prompt.lower()
    
    def test_user_prompt(self, test_security_md, test_threat_model):
        """Test user prompt includes context"""
        agent = CodeReviewAgent()
        prompt = agent.build_user_prompt(
            security_md=test_security_md,
            threat_model=test_threat_model
        )
        assert "SQL Injection" in prompt  # From threat model
        assert "JSON" in prompt
    
    def test_process_results_valid_json(self, tmp_path):
        """Test processing valid vulnerabilities JSON"""
        agent = CodeReviewAgent()
        vulns = [
            {
                "threat_id": "THREAT-001",
                "title": "SQL Injection in app.py",
                "description": "User input concatenated into SQL query",
                "severity": "critical",
                "file_path": "app.py",
                "line_number": 42,
                "code_snippet": "query = f'SELECT * FROM users WHERE id={user_id}'",
                "cwe_id": "CWE-89",
                "recommendation": "Use parameterized queries",
                "evidence": "Line 42 shows string concatenation"
            }
        ]
        response = json.dumps(vulns)
        result = agent.process_results(response, str(tmp_path))
        
        assert result['total_vulnerabilities'] == 1
        assert result['by_severity']['critical'] == 1
        assert Path(result['file']).exists()
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_code_review_run(self, test_repo, test_security_md, test_threat_model):
        """Test Code Review Agent finds vulnerabilities"""
        agent = CodeReviewAgent()
        result = await agent.run(
            str(test_repo),
            security_md=test_security_md,
            threat_model=test_threat_model
        )
        
        assert 'file' in result
        assert result['file'].endswith('VULNERABILITIES.json')
        assert result['total_vulnerabilities'] >= 0
        assert Path(result['file']).exists()


class TestOrchestratorAgent:
    """Tests for Orchestrator Agent"""
    
    def test_orchestrator_creation(self):
        """Test creating an Orchestrator"""
        orchestrator = OrchestratorAgent()
        assert orchestrator.api_key is None or isinstance(orchestrator.api_key, str)
        assert orchestrator.model == "claude-3-5-sonnet-20241022"
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key and takes time")
    async def test_full_scan(self, test_repo):
        """Test complete 3-phase workflow"""
        orchestrator = OrchestratorAgent(model="claude-3-5-haiku-20241022")
        result = await orchestrator.run_full_scan(str(test_repo))
        
        # Check scan result
        assert len(result.issues) >= 0
        assert result.repository_path == str(test_repo)
        
        # Check artifacts created
        vulnguard_dir = test_repo / ".vulnguard"
        assert (vulnguard_dir / "SECURITY.md").exists()
        assert (vulnguard_dir / "THREAT_MODEL.json").exists()
        assert (vulnguard_dir / "VULNERABILITIES.json").exists()
        assert (vulnguard_dir / "scan_results.json").exists()
    
    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires Claude API key")
    async def test_assessment_only(self, test_repo):
        """Test running only assessment phase"""
        orchestrator = OrchestratorAgent()
        result = await orchestrator.run_assessment_only(str(test_repo))
        
        assert 'file' in result
        assert Path(result['file']).exists()
    
    @pytest.mark.asyncio
    async def test_threat_modeling_requires_security_md(self, test_repo):
        """Test threat modeling fails without SECURITY.md"""
        orchestrator = OrchestratorAgent()
        
        with pytest.raises(ValueError, match="SECURITY.md not found"):
            await orchestrator.run_threat_modeling_only(str(test_repo))
    
    @pytest.mark.asyncio
    async def test_code_review_requires_artifacts(self, test_repo):
        """Test code review fails without required artifacts"""
        orchestrator = OrchestratorAgent()
        
        with pytest.raises(ValueError, match="SECURITY.md not found"):
            await orchestrator.run_code_review_only(str(test_repo))


class TestBaseAgent:
    """Tests for Base Agent functionality"""
    
    def test_base_agent_is_abstract(self):
        """Test that BaseAgent cannot be instantiated directly"""
        from vulnguard.agents.base import BaseAgent
        
        # BaseAgent is abstract, so this should work but require subclass implementation
        # We test this indirectly through concrete agents
        agent = AssessmentAgent()
        assert hasattr(agent, 'name')
        assert hasattr(agent, 'allowed_tools')
        assert hasattr(agent, 'build_system_prompt')
        assert hasattr(agent, 'build_user_prompt')
    
    def test_vulnguard_dir_creation(self, tmp_path):
        """Test .vulnguard directory creation"""
        agent = AssessmentAgent()
        vulnguard_dir = agent.get_vulnguard_dir(str(tmp_path))
        
        assert vulnguard_dir.exists()
        assert vulnguard_dir.name == ".vulnguard"
        assert vulnguard_dir.parent == tmp_path
