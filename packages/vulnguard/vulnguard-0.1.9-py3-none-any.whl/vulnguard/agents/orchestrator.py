"""Orchestrator Agent - Coordinates the multi-agent workflow"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from vulnguard.agents.assessment import AssessmentAgent
from vulnguard.agents.threat_modeling import ThreatModelingAgent
from vulnguard.agents.code_review import CodeReviewAgent
from vulnguard.models.result import ScanResult
from vulnguard.models.issue import SecurityIssue, Severity


class OrchestratorAgent:
    """Orchestrates the multi-agent security analysis workflow"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        debug: bool = False
    ):
        """
        Initialize orchestrator
        
        Args:
            api_key: Claude API key
            model: Claude model to use for all agents
            debug: Enable debug output
        """
        self.api_key = api_key
        self.model = model
        self.debug = debug
        self.total_cost = 0.0
    
    async def run_full_scan(self, repo_path: str) -> ScanResult:
        """
        Run the complete multi-agent workflow
        
        Args:
            repo_path: Path to repository
            
        Returns:
            ScanResult with all findings
        """
        repo = Path(repo_path).resolve()
        
        print("VulnGuard - AI-Powered Vulnerability Detection and Fixing")
        print(f"🔧 Using Claude Agent SDK with model: {self.model}")
        print(f"📁 Target: {repo}")
        print()
        
        results = {}
        
        # Phase 1: Assessment
        print("━━━ Phase 1/3: Architecture Assessment ━━━")
        assessment_agent = AssessmentAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        results['assessment'] = await assessment_agent.run(str(repo))
        self.total_cost += assessment_agent.total_cost
        print()
        
        # Phase 2: Threat Modeling
        print("━━━ Phase 2/3: Threat Modeling ━━━")
        
        # Read SECURITY.md
        security_file = Path(results['assessment']['file'])
        security_md = security_file.read_text()
        
        threat_agent = ThreatModelingAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        results['threat_modeling'] = await threat_agent.run(
            str(repo),
            security_md=security_md
        )
        self.total_cost += threat_agent.total_cost
        print()
        
        # Phase 3: Code Review
        print("━━━ Phase 3/3: Security Code Review ━━━")
        
        # Read THREAT_MODEL.json
        threat_file = Path(results['threat_modeling']['file'])
        threat_model = json.loads(threat_file.read_text())
        
        review_agent = CodeReviewAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        results['code_review'] = await review_agent.run(
            str(repo),
            security_md=security_md,
            threat_model=threat_model
        )
        self.total_cost += review_agent.total_cost
        print()
        
        # Convert vulnerabilities to SecurityIssue objects
        vuln_file = Path(results['code_review']['file'])
        vulnerabilities = json.loads(vuln_file.read_text())
        
        issues = []
        for idx, vuln in enumerate(vulnerabilities):
            try:
                severity_str = vuln.get('severity', 'medium').lower()
                if severity_str not in ['critical', 'high', 'medium', 'low', 'info']:
                    severity_str = 'medium'
                
                issue = SecurityIssue(
                    id=f"vulnguard-{idx+1:03d}",
                    severity=Severity(severity_str),
                    title=vuln.get('title', 'Unknown Security Issue'),
                    description=vuln.get('description', ''),
                    file_path=vuln.get('file_path', 'unknown'),
                    line_number=int(vuln.get('line_number', 0)),
                    code_snippet=vuln.get('code_snippet', ''),
                    recommendation=vuln.get('recommendation'),
                    cwe_id=vuln.get('cwe_id'),
                )
                issues.append(issue)
            except Exception as e:
                print(f"⚠️  Error converting vulnerability {idx}: {e}")
                continue
        
        # Create scan result
        scan_result = ScanResult(
            repository_path=str(repo),
            issues=issues
        )
        
        # Save final results
        vulnguard_dir = repo / ".vulnguard"
        results_file = vulnguard_dir / "scan_results.json"
        results_file.write_text(scan_result.to_json())
        
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"💰 Total Cost: ${self.total_cost:.4f}")
        print(f"📊 Artifacts Created:")
        print(f"   📄 {results['assessment']['file']}")
        print(f"   📄 {results['threat_modeling']['file']}")
        print(f"   📄 {results['code_review']['file']}")
        print(f"   📄 {results_file}")
        print()
        
        return scan_result
    
    async def run_assessment_only(self, repo_path: str) -> Dict[str, Any]:
        """Run only the assessment phase"""
        agent = AssessmentAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        return await agent.run(repo_path)
    
    async def run_threat_modeling_only(self, repo_path: str) -> Dict[str, Any]:
        """Run only threat modeling (requires existing SECURITY.md)"""
        repo = Path(repo_path).resolve()
        security_file = repo / ".vulnguard" / "SECURITY.md"
        
        if not security_file.exists():
            raise ValueError("SECURITY.md not found. Run assessment first.")
        
        security_md = security_file.read_text()
        
        agent = ThreatModelingAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        return await agent.run(repo_path, security_md=security_md)
    
    async def run_code_review_only(self, repo_path: str) -> Dict[str, Any]:
        """Run only code review (requires SECURITY.md and THREAT_MODEL.json)"""
        repo = Path(repo_path).resolve()
        vulnguard_dir = repo / ".vulnguard"
        
        security_file = vulnguard_dir / "SECURITY.md"
        threat_file = vulnguard_dir / "THREAT_MODEL.json"
        
        if not security_file.exists():
            raise ValueError("SECURITY.md not found. Run assessment first.")
        if not threat_file.exists():
            raise ValueError("THREAT_MODEL.json not found. Run threat modeling first.")
        
        security_md = security_file.read_text()
        threat_model = json.loads(threat_file.read_text())
        
        agent = CodeReviewAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        return await agent.run(
            repo_path,
            security_md=security_md,
            threat_model=threat_model
        )
