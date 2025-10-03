"""Claude Agent SDK client for security analysis"""

import json
import os
from pathlib import Path
from typing import Optional
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock, ResultMessage
from vulnguard.models.issue import SecurityIssue, Severity


class ClaudeSecurityAnalyzer:
    """Uses Claude Agent SDK to analyze code for security issues"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        """
        Initialize with Claude API key
        
        Args:
            api_key: Claude API key. If not provided, reads from CLAUDE_API_KEY env var
            model: Claude model to use (default: claude-3-5-sonnet-20241022)
        """
        # Set API key in environment if provided
        if api_key:
            os.environ["CLAUDE_API_KEY"] = api_key
        
        self.model = model
        self.total_cost = 0.0
    
    async def analyze_repository(self, repo_path: str) -> list[SecurityIssue]:
        """
        Analyze a repository for security vulnerabilities
        
        Args:
            repo_path: Path to the repository to analyze
            
        Returns:
            List of SecurityIssue objects found
        """
        # Verify API key is available
        if not os.environ.get("CLAUDE_API_KEY"):
            raise ValueError(
                "Claude API key required. Set CLAUDE_API_KEY environment variable "
                "or pass api_key parameter. Get your key at: https://console.anthropic.com/"
            )
        
        repo = Path(repo_path).resolve()
        if not repo.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")
        
        print(f"📁 Analyzing repository: {repo}")
        
        # Configure Claude Agent SDK with appropriate tools
        options = ClaudeAgentOptions(
            # Allow Claude to explore files using built-in tools
            allowed_tools=["Read", "Grep", "Glob", "LS"],
            
            # Set working directory to the repository
            cwd=str(repo),
            
            # System prompt to guide the analysis
            system_prompt="""You are a security expert specializing in code vulnerability analysis.
Your task is to systematically scan code repositories for security vulnerabilities.""",
            
            # Limit conversation turns to control costs
            max_turns=20,
            
            # Auto-accept file reads (we're only reading, not writing)
            permission_mode='default',
        )
        
        # Build the analysis prompt
        prompt = self._build_analysis_prompt()
        
        print("🤖 Starting security analysis with Claude Agent SDK...")
        
        # Collect all response content and track usage
        content_parts = []
        usage_data = None
        
        try:
            async for message in query(prompt=prompt, options=options):
                # Collect assistant messages
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            content_parts.append(block.text)
                
                # Track usage from result message
                if isinstance(message, ResultMessage):
                    usage_data = message.usage
                    if usage_data and hasattr(usage_data, 'total_cost_usd'):
                        self.total_cost = usage_data.total_cost_usd or 0.0
            
            # Combine all content
            full_response = "\n".join(content_parts)
            
            # Debug: Print response preview
            print(f"\n📝 Claude Response Preview:\n{full_response[:500]}...\n")
            
            # Display cost information
            if usage_data:
                print(f"💰 Scan Cost: ${self.total_cost:.4f}")
                if hasattr(usage_data, 'input_tokens'):
                    print(f"   Input tokens: {usage_data.input_tokens}")
                if hasattr(usage_data, 'output_tokens'):
                    print(f"   Output tokens: {usage_data.output_tokens}")
            
            # Parse issues from Claude's response
            issues = self._parse_issues_from_response(full_response, str(repo))
            return issues
            
        except Exception as e:
            print(f"❌ Error during analysis: {e}")
            raise
    
    def _build_analysis_prompt(self) -> str:
        """Build the security analysis prompt"""
        return """You are a security vulnerability scanner. Your job is to analyze code and output ONLY structured JSON results.

CRITICAL INSTRUCTIONS:
1. Do NOT include conversational text or explanations in your response
2. Use tools (Glob, Grep, Read) to explore the codebase SILENTLY
3. After analyzing, output ONLY a JSON array of vulnerabilities
4. Your ENTIRE response should be ONLY the JSON array, nothing else

ANALYSIS STEPS (do these silently):
1. Use Glob to find code files: *.py, *.js, *.ts, *.java, *.go, *.rb, *.php, *.c, *.cpp, *.cs, *.rs
2. Use Grep to search for vulnerability patterns
3. Use Read to examine suspicious files
4. Collect findings with exact file paths and line numbers

VULNERABILITY TYPES TO DETECT:

🔴 CRITICAL:
- SQL Injection (CWE-89): String concatenation in SQL queries
- Command Injection (CWE-78): os.system(), subprocess with shell=True
- Code Injection (CWE-95): eval(), exec() with user input
- Path Traversal (CWE-22): Unvalidated file paths

🟠 HIGH:
- Hardcoded Secrets (CWE-798): API keys, passwords in code
- Authentication Bypass (CWE-287): Missing auth checks
- Insecure Deserialization (CWE-502): pickle.loads() with untrusted data
- XXE (CWE-611): Unsafe XML parsing

🟡 MEDIUM:
- XSS (CWE-79): Unescaped HTML output
- CSRF (CWE-352): Missing CSRF tokens
- Weak Crypto (CWE-327): MD5, SHA1 for passwords
- Info Disclosure (CWE-200): Sensitive data in logs

🟢 LOW:
- Insecure Random (CWE-330): random.random() for security
- Missing Validation (CWE-20): Unvalidated input
- Deprecated APIs

SEARCH PATTERNS:
- SQL: "execute(", ".format(", f"SELECT", f"INSERT"
- Command: "os.system", "subprocess", "shell=True"
- Secrets: "password =", "api_key =", "secret =", "AWS_", "sk-"
- Path: "../", "open(", user input in paths
- Injection: "eval(", "exec(", "compile("
- Deserialize: "pickle.loads", "yaml.load"

OUTPUT FORMAT (THIS IS YOUR ENTIRE RESPONSE):

```json
[
  {
    "severity": "critical",
    "title": "SQL Injection in login function",
    "description": "User input concatenated directly into SQL query without parameterization",
    "file_path": "app/views.py",
    "line_number": 42,
    "code_snippet": "query = f\"SELECT * FROM users WHERE username='{username}'\"",
    "recommendation": "Use parameterized queries or ORM",
    "cwe_id": "CWE-89"
  }
]
```

REMEMBER:
- NO conversational text
- NO explanations or commentary
- ONLY output the JSON array
- Include actual file paths and line numbers
- If NO vulnerabilities: output ```json\n[]\n```

Output your JSON findings now (JSON ONLY, no other text):
    
    def _parse_issues_from_response(self, response: str, repo_path: str) -> list[SecurityIssue]:
        """Parse SecurityIssue objects from Claude's response"""
        issues = []
        
        try:
            json_str = None
            
            # Method 1: Look for ```json code block (most reliable)
            if '```json' in response:
                start = response.find('```json') + 7
                end = response.find('```', start)
                if end > start:
                    json_str = response[start:end].strip()
            
            # Method 2: Look for JSON array
            if not json_str:
                start = response.find('[')
                end = response.rfind(']') + 1
                if start != -1 and end > start:
                    json_str = response[start:end]
            
            # Method 3: Look for FINDINGS: marker (legacy)
            if not json_str and 'FINDINGS:' in response:
                findings_start = response.find('FINDINGS:') + 9
                findings_section = response[findings_start:].strip()
                json_start = findings_section.find('[')
                json_end = findings_section.rfind(']') + 1
                if json_start != -1 and json_end > json_start:
                    json_str = findings_section[json_start:json_end]
            
            if not json_str:
                print("⚠️  No JSON array found, trying natural language parsing")
                return self._parse_natural_language(response, repo_path)
            
            # Parse JSON
            data = json.loads(json_str)
            
            if not isinstance(data, list):
                print(f"⚠️  Expected JSON array, got {type(data)}")
                return self._parse_natural_language(response, repo_path)
            
            # Convert to SecurityIssue objects
            for idx, item in enumerate(data):
                if not isinstance(item, dict):
                    print(f"⚠️  Skipping non-dict item at index {idx}")
                    continue
                
                try:
                    # Normalize severity
                    severity_str = item.get("severity", "medium").lower()
                    if severity_str not in ["critical", "high", "medium", "low", "info"]:
                        severity_str = "medium"
                    
                    # Extract line number (handle string or int)
                    line_num = item.get("line_number", 0)
                    if isinstance(line_num, str):
                        line_num = int(line_num) if line_num.isdigit() else 0
                    
                    issue = SecurityIssue(
                        id=f"vulnguard-{idx+1:03d}",
                        severity=Severity(severity_str),
                        title=item.get("title", "Unknown Security Issue"),
                        description=item.get("description", "No description provided"),
                        file_path=item.get("file_path", "unknown"),
                        line_number=line_num,
                        code_snippet=item.get("code_snippet", ""),
                        recommendation=item.get("recommendation"),
                        cwe_id=item.get("cwe_id"),
                    )
                    issues.append(issue)
                    
                except (ValueError, TypeError) as e:
                    print(f"⚠️  Error parsing issue {idx}: {e}")
                    continue
            
            return issues
            
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON decode error: {e}")
            if 'json_str' in locals() and json_str:
                print(f"   Attempted to parse: {json_str[:200]}...")
            return self._parse_natural_language(response, repo_path)
            
        except Exception as e:
            print(f"❌ Unexpected error parsing issues: {e}")
            return []
    
    def _parse_natural_language(self, response: str, repo_path: str) -> list[SecurityIssue]:
        """Parse issues from natural language response as fallback"""
        issues = []
        lines = response.split('\n')
        
        current_issue = {}
        issue_counter = 0
        
        # Common vulnerability keywords
        vuln_keywords = [
            'SQL INJECTION', 'COMMAND INJECTION', 'XSS', 'CSRF', 
            'PATH TRAVERSAL', 'HARDCODED SECRET', 'CODE INJECTION',
            'EVAL', 'EXEC', 'INSECURE', 'VULNERABILITY', 'WEAK CRYPTO',
            'AUTHENTICATION', 'AUTHORIZATION', 'DESERIALIZATION'
        ]
        
        for line in lines:
            line_stripped = line.strip()
            
            # Detect issue headers
            if any(keyword in line_stripped.upper() for keyword in vuln_keywords):
                # Save previous issue
                if current_issue and current_issue.get('title'):
                    issue = self._create_issue_from_dict(current_issue, issue_counter)
                    if issue:
                        issues.append(issue)
                        issue_counter += 1
                
                # Start new issue
                current_issue = {
                    'title': line_stripped.lstrip('*#-0123456789. ').rstrip('*:'),
                    'description': '',
                    'line_number': 0,
                    'file_path': 'unknown',
                    'severity': 'high'
                }
                
                # Try to extract line number from same line
                if 'line' in line_stripped.lower():
                    import re
                    match = re.search(r'line[s]?\s*(\d+)', line_stripped, re.IGNORECASE)
                    if match:
                        current_issue['line_number'] = int(match.group(1))
            
            # Collect description and other details
            elif current_issue:
                if 'file:' in line_stripped.lower() or 'path:' in line_stripped.lower():
                    # Extract file path
                    parts = line_stripped.split(':', 1)
                    if len(parts) > 1:
                        current_issue['file_path'] = parts[1].strip()
                elif line_stripped:
                    # Add to description
                    if current_issue.get('description'):
                        current_issue['description'] += ' ' + line_stripped
                    else:
                        current_issue['description'] = line_stripped
        
        # Don't forget last issue
        if current_issue and current_issue.get('title'):
            issue = self._create_issue_from_dict(current_issue, issue_counter)
            if issue:
                issues.append(issue)
        
        return issues
    
    def _create_issue_from_dict(self, data: dict, idx: int) -> Optional[SecurityIssue]:
        """Create SecurityIssue from parsed natural language data"""
        try:
            return SecurityIssue(
                id=f"vulnguard-{idx+1:03d}",
                severity=Severity(data.get('severity', 'medium')),
                title=data.get('title', 'Security Issue')[:200],
                description=data.get('description', 'See analysis above')[:1000].strip(),
                file_path=data.get('file_path', 'unknown'),
                line_number=data.get('line_number', 0),
                code_snippet=data.get('code_snippet', ''),
                recommendation=data.get('recommendation'),
                cwe_id=data.get('cwe_id')
            )
        except Exception as e:
            print(f"⚠️  Error creating issue from data: {e}")
            return None
