"""Anthropic SDK client for security analysis (public API)"""

import os
import json
from pathlib import Path
from typing import Optional
import anthropic
from vulnguard.models.issue import SecurityIssue, Severity


class AnthropicSecurityAnalyzer:
    """Uses standard Anthropic API to analyze code for security issues"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20240620"):
        """
        Initialize with Anthropic API key
        
        Args:
            api_key: Anthropic API key. If not provided, reads from ANTHROPIC_API_KEY env var
            model: Claude model to use (default: claude-3-5-sonnet-20240620)
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter. Get your key at: https://console.anthropic.com/"
            )
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model
    
    async def analyze_repository(self, repo_path: str) -> list[SecurityIssue]:
        """
        Analyze a repository for security vulnerabilities
        
        Args:
            repo_path: Path to the repository to analyze
            
        Returns:
            List of SecurityIssue objects found
        """
        repo = Path(repo_path)
        if not repo.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")
        
        # Collect code files to analyze
        code_files = self._collect_code_files(repo)
        
        if not code_files:
            print("⚠️  No code files found to analyze")
            return []
        
        print(f"📁 Found {len(code_files)} code files to analyze")
        
        # Read file contents
        file_contents = {}
        for file_path in code_files[:20]:  # Limit to 20 files for now
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                relative_path = file_path.relative_to(repo)
                file_contents[str(relative_path)] = content
            except Exception as e:
                print(f"⚠️  Could not read {file_path}: {e}")
        
        # Build prompt with file contents
        prompt = self._build_prompt(file_contents)
        
        # Call Anthropic API
        print("🤖 Analyzing with Claude...")
        response = self.client.messages.create(
            model=self.model,
            max_tokens=8000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Extract text from response
        response_text = ""
        for block in response.content:
            if block.type == "text":
                response_text += block.text
        
        print(f"\n📝 Claude Response Preview:\n{response_text[:500]}...\n")
        
        # Parse issues
        issues = self._parse_issues_from_response(response_text, str(repo))
        return issues
    
    def _collect_code_files(self, repo_path: Path) -> list[Path]:
        """Collect code files from repository (multiple languages)"""
        code_files = []
        
        # Supported file extensions
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx',  # Python, JavaScript, TypeScript
            '.java', '.go', '.rb', '.php',         # Java, Go, Ruby, PHP
            '.c', '.cpp', '.h', '.hpp',            # C, C++
            '.cs', '.rs', '.kt', '.swift',         # C#, Rust, Kotlin, Swift
            '.sql', '.sh', '.bash',                # SQL, Shell scripts
        }
        
        # Patterns to exclude
        exclude_patterns = {
            'venv', 'env', '.venv', '__pycache__', '.git', 
            'node_modules', '.pytest_cache', 'dist', 'build',
            '.eggs', '*.egg-info', 'vendor', 'target'
        }
        
        for file_path in repo_path.rglob("*"):
            # Check if it's a code file
            if not file_path.is_file() or file_path.suffix not in code_extensions:
                continue
            
            # Skip excluded directories
            if any(pattern in str(file_path) for pattern in exclude_patterns):
                continue
            
            code_files.append(file_path)
        
        return code_files
    
    def _build_prompt(self, file_contents: dict[str, str]) -> str:
        """Build analysis prompt with file contents"""
        
        files_text = ""
        for file_path, content in file_contents.items():
            files_text += f"\n\n{'='*80}\nFile: {file_path}\n{'='*80}\n{content}"
        
        prompt = f"""You are a security expert analyzing Python code for vulnerabilities.

Analyze the following files for security issues:
{files_text}

FOCUS ON:
1. SQL Injection - String concatenation in queries
2. Command Injection - Unsanitized input to os.system, subprocess
3. Hardcoded Secrets - API keys, passwords, tokens in code
4. Path Traversal - Unvalidated file paths
5. Code Injection - eval(), exec() with user data
6. XSS - Unescaped user input in HTML
7. Insecure Deserialization - pickle with untrusted data
8. Weak Cryptography - MD5, SHA1, hardcoded keys

For each vulnerability found, provide:
- Exact file path and line number
- Type of vulnerability
- Severity (critical/high/medium/low)
- Brief description
- Recommendation to fix

At the END of your analysis, provide a JSON summary in this format:

```json
[
  {{
    "severity": "critical",
    "title": "SQL Injection",
    "description": "...",
    "file_path": "path/to/file.py",
    "line_number": 42,
    "code_snippet": "...",
    "recommendation": "...",
    "cwe_id": "CWE-89"
  }}
]
```

If no vulnerabilities found, return: ```json\\n[]\\n```

Begin your analysis:"""
        
        return prompt
    
    def _parse_issues_from_response(self, response: str, repo_path: str) -> list[SecurityIssue]:
        """Parse SecurityIssue objects from Claude's response"""
        issues = []
        
        try:
            json_str = None
            
            # Method 1: Look for FINDINGS: marker
            if 'FINDINGS:' in response:
                findings_start = response.find('FINDINGS:') + 9
                findings_section = response[findings_start:].strip()
                json_start = findings_section.find('[')
                json_end = findings_section.rfind(']') + 1
                if json_start != -1 and json_end > json_start:
                    json_str = findings_section[json_start:json_end]
            
            # Method 2: Look for ```json code blocks
            if not json_str and '```json' in response:
                start = response.find('```json') + 7
                end = response.find('```', start)
                if end > start:
                    json_str = response[start:end].strip()
            
            # Method 3: Look for any JSON array
            if not json_str:
                start = response.find('[')
                end = response.rfind(']') + 1
                if start != -1 and end > start:
                    json_str = response[start:end]
            
            if not json_str:
                print("❌ No JSON array found, trying natural language parsing")
                return self._parse_natural_language(response, repo_path)
            
            data = json.loads(json_str)
            
            if not isinstance(data, list):
                print(f"⚠️  Expected JSON array, got {type(data)}")
                return issues
            
            # Convert to SecurityIssue objects
            for idx, item in enumerate(data):
                try:
                    issue = SecurityIssue(
                        id=f"vulnguard-{idx+1:03d}",
                        severity=Severity(item.get('severity', 'medium')),
                        title=item.get('title', 'Security Issue'),
                        description=item.get('description', ''),
                        file_path=item.get('file_path', 'unknown'),
                        line_number=item.get('line_number', 0),
                        code_snippet=item.get('code_snippet', ''),
                        recommendation=item.get('recommendation'),
                        cwe_id=item.get('cwe_id')
                    )
                    issues.append(issue)
                except Exception as e:
                    print(f"⚠️  Error creating issue {idx}: {e}")
            
            return issues
            
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON decode error: {e}")
            return self._parse_natural_language(response, repo_path)
        except Exception as e:
            print(f"❌ Error parsing issues: {e}")
            return []
    
    def _parse_natural_language(self, response: str, repo_path: str) -> list[SecurityIssue]:
        """Parse issues from natural language response as fallback"""
        issues = []
        lines = response.split('\n')
        
        current_issue = {}
        issue_counter = 0
        
        for line in lines:
            line_stripped = line.strip()
            
            # Detect issue headers
            if any(vuln_type in line_stripped.upper() for vuln_type in [
                'SQL INJECTION', 'COMMAND INJECTION', 'XSS', 'CSRF', 
                'PATH TRAVERSAL', 'HARDCODED SECRET', 'CODE INJECTION',
                'EVAL', 'INSECURE', 'VULNERABILITY'
            ]):
                # Save previous issue
                if current_issue:
                    issue = self._create_issue_from_dict(current_issue, issue_counter)
                    if issue:
                        issues.append(issue)
                        issue_counter += 1
                
                # Start new issue
                current_issue = {
                    'title': line_stripped.lstrip('*#-0123456789. ').rstrip('*'),
                    'description': '',
                    'line_number': 0,
                    'file_path': 'unknown',
                    'severity': 'high'
                }
                
                # Extract line number
                if 'line' in line_stripped.lower():
                    import re
                    match = re.search(r'line[s]?\s*(\d+)', line_stripped, re.IGNORECASE)
                    if match:
                        current_issue['line_number'] = int(match.group(1))
            
            # Collect description
            elif current_issue and line_stripped:
                if 'description' in current_issue:
                    current_issue['description'] += ' ' + line_stripped
        
        # Don't forget last issue
        if current_issue:
            issue = self._create_issue_from_dict(current_issue, issue_counter)
            if issue:
                issues.append(issue)
        
        return issues
    
    def _create_issue_from_dict(self, data: dict, idx: int) -> Optional[SecurityIssue]:
        """Create SecurityIssue from parsed data"""
        try:
            return SecurityIssue(
                id=f"vulnguard-{idx+1:03d}",
                severity=Severity(data.get('severity', 'medium')),
                title=data.get('title', 'Security Issue')[:200],
                description=data.get('description', 'See analysis above')[:1000],
                file_path=data.get('file_path', 'unknown'),
                line_number=data.get('line_number', 0),
                code_snippet=data.get('code_snippet', ''),
                recommendation=data.get('recommendation'),
                cwe_id=data.get('cwe_id')
            )
        except Exception as e:
            print(f"❌ Error creating issue: {e}")
            return None
