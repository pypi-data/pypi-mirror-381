"""Orchestrator Agent - Coordinates the multi-agent workflow"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from vulnguard.agents.assessment import AssessmentAgent
from vulnguard.agents.threat_modeling import ThreatModelingAgent
from vulnguard.agents.code_review import CodeReviewAgent
from vulnguard.scanner.context_gatherer import ContextGatherer
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
        
        # Phase 3: Code Review with Smart Context Gathering
        print("━━━ Phase 3/3: Security Code Review ━━━")
        threat_file = Path(results['threat_modeling']['file'])
        threat_model = json.loads(threat_file.read_text())
        
        # Attempt 1: Smart pre-gathering (no tools)
        results['code_review'] = await self._try_smart_review(
            str(repo), security_md, threat_model
        )
        
        # Check if successful
        if results['code_review']['total_vulnerabilities'] == 0:
            if not self._looks_complete(results['code_review']):
                print("⚠️  Pre-gathered approach found no vulnerabilities, trying with tool access...")
                
                # Attempt 2: Fallback with tools
                results['code_review'] = await self._try_tool_based_review(
                    str(repo), security_md, threat_model
                )
        
        print()
        
        # Convert to SecurityIssue objects
        vuln_file = Path(results['code_review']['file'])
        vulnerabilities = json.loads(vuln_file.read_text())
        issues = self._convert_to_issues(vulnerabilities)
        
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
    
    async def _try_smart_review(
        self,
        repo_path: str,
        security_md: str,
        threat_model: List[Dict]
    ) -> Dict[str, Any]:
        """Attempt code review with smart pre-gathered context"""
        
        try:
            # Gather comprehensive context
            print("🔍 Gathering comprehensive code context...")
            gatherer = ContextGatherer(repo_path)
            code_evidence = gatherer.gather_comprehensive_context(threat_model)
            
            print(f"✅ Gathered context for {len(code_evidence)} threats")
            
            # Run review agent without tools
            review_agent = CodeReviewAgent(
                api_key=self.api_key,
                model=self.model,
                debug=self.debug
            )
            
            # Override allowed_tools for this run
            original_tools = review_agent.allowed_tools
            review_agent.allowed_tools = []  # No tools
            
            result = await review_agent.run(
                repo_path,
                security_md=security_md,
                threat_model=threat_model,
                code_evidence=code_evidence
            )
            
            # Restore original tools
            review_agent.allowed_tools = original_tools
            
            self.total_cost += review_agent.total_cost
            
            return result
            
        except Exception as e:
            print(f"❌ Smart review failed: {e}")
            # Return empty result to trigger fallback
            return {
                'file': '',
                'total_vulnerabilities': 0,
                'by_severity': {},
                'summary': 'Failed to complete smart review'
            }
    
    async def _try_tool_based_review(
        self,
        repo_path: str,
        security_md: str,
        threat_model: List[Dict]
    ) -> Dict[str, Any]:
        """Fallback: code review with tool access and staged output"""
        
        review_agent = CodeReviewAgent(
            api_key=self.api_key,
            model=self.model,
            debug=self.debug
        )
        
        result = await review_agent.run(
            repo_path,
            security_md=security_md,
            threat_model=threat_model,
            use_staged_output=True  # Enable staged output mode
        )
        
        self.total_cost += review_agent.total_cost
        
        return result
    
    def _looks_complete(self, result: Dict[str, Any]) -> bool:
        """Check if result looks like a complete analysis"""
        
        # If we have vulnerabilities, it's complete
        if result.get('total_vulnerabilities', 0) > 0:
            return True
        
        # If we have investigation notes, agent did work
        if result.get('had_investigation_notes'):
            return True
        
        # Check if file was actually created
        file_path = result.get('file')
        if file_path and Path(file_path).exists():
            # Check file size - should be more than just []
            size = Path(file_path).stat().st_size
            return size > 10  # More than empty array
        
        return False
    
    def _convert_to_issues(self, vulnerabilities: List[Dict]) -> List[SecurityIssue]:
        """Convert vulnerability dicts to SecurityIssue objects"""
        
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
        
        return issues
