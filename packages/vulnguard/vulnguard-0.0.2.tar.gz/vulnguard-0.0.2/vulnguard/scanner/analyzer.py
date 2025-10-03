"""Main security scanner"""

import time
from pathlib import Path
from typing import Optional
from vulnguard.models.result import ScanResult
from vulnguard.reporters.json_reporter import JSONReporter
from vulnguard.claude.client import ClaudeSecurityAnalyzer


class SecurityScanner:
    """Main security scanner that orchestrates the analysis"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        """
        Initialize scanner with Claude Agent SDK
        
        Args:
            api_key: Claude API key (optional, reads from CLAUDE_API_KEY env var)
            model: Claude model to use (default: claude-3-5-sonnet-20241022)
        """
        self.claude = ClaudeSecurityAnalyzer(api_key=api_key, model=model)
        print(f"🔧 Using Claude Agent SDK with model: {model}")
    
    async def scan(self, repository_path: str, save_results: bool = True) -> ScanResult:
        """
        Scan a repository for security vulnerabilities
        
        Args:
            repository_path: Path to the repository to scan
            save_results: Whether to save results to .vulnguard directory
            
        Returns:
            ScanResult containing found issues
        """
        start_time = time.time()
        
        # Validate path
        repo_path = Path(repository_path).resolve()
        if not repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repository_path}")
        
        # Count files (for reporting)
        files_scanned = self._count_code_files(repo_path)
        
        # Use Claude Agent SDK to analyze
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
        # Supported code file extensions
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx',  # Python, JavaScript, TypeScript
            '.java', '.go', '.rb', '.php',         # Java, Go, Ruby, PHP
            '.c', '.cpp', '.h', '.hpp', '.cc',     # C, C++
            '.cs', '.rs', '.kt', '.swift',         # C#, Rust, Kotlin, Swift
            '.sql', '.sh', '.bash',                # SQL, Shell scripts
        }
        
        # Directories to exclude
        exclude_dirs = {
            '.git', 'node_modules', 'venv', '.venv', 'env',
            '__pycache__', '.pytest_cache', 'dist', 'build',
            'vendor', 'target', '.eggs', 'eggs'
        }
        
        count = 0
        
        try:
            for file_path in repo_path.rglob('*'):
                if not file_path.is_file():
                    continue
                
                # Check if file has code extension
                if file_path.suffix not in code_extensions:
                    continue
                
                # Skip excluded directories
                if any(excluded in file_path.parts for excluded in exclude_dirs):
                    continue
                
                # Skip hidden files/directories
                if any(part.startswith('.') for part in file_path.parts[len(repo_path.parts):]):
                    continue
                
                count += 1
                
        except Exception as e:
            print(f"⚠️  Error counting files: {e}")
        
        return count
