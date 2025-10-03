"""Claude Code SDK client for security analysis"""

import json
from vulnguard.models.issue import SecurityIssue, Severity

# Import Factory SDK components (only available in Factory environment)
try:
    from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock
    FACTORY_SDK_AVAILABLE = True
except ImportError:
    FACTORY_SDK_AVAILABLE = False
    # Define dummy classes so the module can still be imported
    query = None
    ClaudeAgentOptions = None
    AssistantMessage = None
    TextBlock = None


class ClaudeSecurityAnalyzer:
    """Uses Claude Code SDK to analyze code for security issues"""
    
    def __init__(self):
        if not FACTORY_SDK_AVAILABLE:
            raise ImportError(
                "Factory SDK (claude_agent_sdk) is not available. "
                "This analyzer only works in Factory/Droid environments. "
                "Use AnthropicSecurityAnalyzer for public API access."
            )
        self.options = ClaudeAgentOptions(
            allowed_tools=["Read", "LS", "Grep", "Glob"],
            max_turns=15
        )
    
    async def analyze_repository(self, repo_path: str) -> list[SecurityIssue]:
        """
        Analyze a repository for security vulnerabilities
        
        Args:
            repo_path: Path to the repository to analyze
            
        Returns:
            List of SecurityIssue objects found
        """
        prompt = f"""You are a security expert. Analyze the repository at {repo_path} for security vulnerabilities.

TASK: Scan code files and identify security issues.

TOOLS: Use Read, LS, Grep, Glob to explore files systematically.

FOCUS AREAS:
1. SQL Injection - String concatenation in queries
2. Command Injection - Unsanitized input to os.system, subprocess
3. Hardcoded Secrets - API keys, passwords, tokens in code
4. Path Traversal - Unvalidated file paths
5. XSS - Unescaped user input in HTML
6. Insecure Deserialization - pickle, eval, exec with user data
7. CSRF - Missing CSRF tokens
8. Weak Crypto - MD5, SHA1, hardcoded keys
9. Authentication Issues - Missing checks, weak passwords
10. Dependency Vulnerabilities - Outdated packages

PROCESS:
1. List all code files (skip tests, docs, configs)
2. Read each file looking for vulnerability patterns
3. For each issue, note exact location and vulnerable code

OUTPUT FORMAT (must be valid JSON array):
[
  {{
    "severity": "critical|high|medium|low",
    "title": "Brief issue description",
    "description": "Detailed explanation of the vulnerability and its impact",
    "file_path": "relative/path/to/file.py",
    "line_number": 42,
    "code_snippet": "actual vulnerable code here",
    "recommendation": "Specific fix suggestion",
    "cwe_id": "CWE-###"
  }}
]

After exploring files, provide findings.

At the END of your response, after all analysis, add this exact line:
FINDINGS:

Then immediately after that line, provide a JSON array (and nothing else after the JSON).

Format:
FINDINGS:
[
  {{"severity": "high", "title": "SQL Injection", "description": "...", "file_path": "file.py", "line_number": 10, "code_snippet": "...", "recommendation": "...", "cwe_id": "CWE-89"}}
]

If no issues: FINDINGS:\n[]

Begin analysis."""

        try:
            content_parts = []
            async for message in query(prompt=prompt, options=self.options):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            content_parts.append(block.text)
            
            full_response = "\n".join(content_parts)
            
            # Debug: Print response (first 500 chars)
            print(f"\n📝 Claude Response Preview:\n{full_response[:500]}...\n")
            
            # Parse issues from Claude's natural language response
            issues = self._parse_issues_from_response(full_response, repo_path)
            return issues
            
        except Exception as e:
            print(f"Error during analysis: {e}")
            return []
    
    def _parse_issues_from_response(self, response: str, repo_path: str) -> list[SecurityIssue]:
        """Parse SecurityIssue objects from Claude's response"""
        issues = []
        
        try:
            json_str = None
            
            # Method 1: Look for FINDINGS: marker
            if 'FINDINGS:' in response:
                findings_start = response.find('FINDINGS:') + 9
                # Extract from FINDINGS: to end of response
                findings_section = response[findings_start:].strip()
                # Get the JSON array (first [ to last ])
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
                print("❌ No JSON array found in response")
                print("💡 Response format may need adjustment")
                return issues
            
            data = json.loads(json_str)
            
            if not isinstance(data, list):
                print(f"Expected JSON array, got {type(data)}")
                return issues
            
            for idx, item in enumerate(data):
                if not isinstance(item, dict):
                    print(f"Skipping non-dict item at index {idx}")
                    continue
                
                try:
                    # Normalize severity
                    severity_str = item.get("severity", "medium").lower()
                    if severity_str not in ["critical", "high", "medium", "low", "info"]:
                        severity_str = "medium"
                    
                    issue = SecurityIssue(
                        id=f"vulnguard-{idx+1:03d}",
                        severity=Severity(severity_str),
                        title=item.get("title", "Unknown Security Issue"),
                        description=item.get("description", "No description provided"),
                        file_path=item.get("file_path", "unknown"),
                        line_number=int(item.get("line_number", 0)),
                        code_snippet=item.get("code_snippet", ""),
                        recommendation=item.get("recommendation"),
                        cwe_id=item.get("cwe_id"),
                    )
                    issues.append(issue)
                except (ValueError, TypeError) as e:
                    print(f"Error parsing issue {idx}: {e}")
                    continue
                    
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            print(f"Attempted to parse: {json_str[:200] if 'json_str' in locals() else 'N/A'}...")
        except Exception as e:
            print(f"Unexpected error parsing issues: {e}")
        
        # If JSON parsing failed, try natural language parsing as fallback
        if not issues:
            issues = self._parse_natural_language(response, repo_path)
        
        return issues
    
    def _parse_natural_language(self, response: str, repo_path: str) -> list[SecurityIssue]:
        """Parse issues from natural language response as fallback"""
        issues = []
        
        # Look for numbered issues or bullet points
        lines = response.split('\n')
        
        current_issue = {}
        issue_counter = 0
        
        for line in lines:
            line_stripped = line.strip()
            
            # Detect issue headers (patterns like "1. SQL Injection" or "**1. SQL Injection**")
            if any(vuln_type in line_stripped.upper() for vuln_type in [
                'SQL INJECTION', 'COMMAND INJECTION', 'XSS', 'CSRF', 
                'PATH TRAVERSAL', 'HARDCODED SECRET', 'CODE INJECTION',
                'EVAL', 'INSECURE', 'VULNERABILITY'
            ]):
                # Save previous issue if exists
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
                
                # Try to extract line number from same line
                if 'line' in line_stripped.lower() or 'Line' in line_stripped:
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
    
    def _create_issue_from_dict(self, data: dict, idx: int) -> SecurityIssue | None:
        """Create SecurityIssue from parsed natural language data"""
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
            print(f"Error creating issue from data: {e}")
            return None
