"""Main security scanner"""

import time
from pathlib import Path
from typing import Optional
from vulnguard.models.result import ScanResult
from vulnguard.reporters.json_reporter import JSONReporter


class SecurityScanner:
    """Main security scanner that orchestrates the analysis"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20240620"):
        """
        Initialize scanner
        
        Args:
            api_key: Anthropic API key (optional, reads from ANTHROPIC_API_KEY env var)
            model: Claude model to use (default: claude-3-5-sonnet-20240620)
        """
        # Try to use Factory SDK first, fall back to Anthropic API
        try:
            from vulnguard.claude.client import ClaudeSecurityAnalyzer
            self.claude = ClaudeSecurityAnalyzer()
            self.using_factory_sdk = True
            print("🔧 Using Factory SDK (Droid environment)")
        except ImportError:
            from vulnguard.claude.anthropic_client import AnthropicSecurityAnalyzer
            self.claude = AnthropicSecurityAnalyzer(api_key=api_key, model=model)
            self.using_factory_sdk = False
            print(f"🔧 Using Anthropic API (public) with model: {model}")
    
    async def scan(self, repository_path: str, save_results: bool = True) -> ScanResult:
        """
        Scan a repository for security vulnerabilities
        
        Args:
            repository_path: Path to the repository to scan
            
        Returns:
            ScanResult containing found issues
        """
        start_time = time.time()
        
        # Validate path
        repo_path = Path(repository_path).resolve()
        if not repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repository_path}")
        
        # Count files
        files_scanned = self._count_code_files(repo_path)
        
        # Use Claude to analyze
        issues = await self.claude.analyze_repository(str(repo_path))
        
        # Calculate scan time
        scan_time = time.time() - start_time
        
        result = ScanResult(
            repository_path=str(repo_path),
            issues=issues,
            files_scanned=files_scanned,
            scan_time_seconds=round(scan_time, 2)
        )
        
        # Auto-save results to .vulnguard directory
        if save_results:
            output_dir = repo_path / ".vulnguard"
            output_file = output_dir / "scan_results.json"
            JSONReporter.save(result, output_file)
            print(f"💾 Results saved to: {output_file}")
        
        return result
    
    def _count_code_files(self, repo_path: Path) -> int:
        """Count number of code files in repository"""
        code_extensions = {'.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rb', '.php'}
        count = 0
        
        try:
            for file_path in repo_path.rglob('*'):
                if file_path.is_file() and file_path.suffix in code_extensions:
                    # Skip common non-source directories
                    if any(part.startswith('.') or part in {'node_modules', 'venv', '__pycache__', 'dist', 'build'} 
                           for part in file_path.parts):
                        continue
                    count += 1
        except Exception:
            pass
        
        return count
