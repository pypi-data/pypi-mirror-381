"""Code Review Agent - Validates threats in actual code"""

import json
from pathlib import Path
from typing import Dict, Any, List
from vulnguard.agents.base import BaseAgent


class CodeReviewAgent(BaseAgent):
    """Agent that finds concrete vulnerabilities based on threat model"""
    
    @property
    def name(self) -> str:
        return "Code Review"
    
    @property
    def allowed_tools(self) -> list[str]:
        return ["Read", "Grep", "Glob"]
    
    def build_system_prompt(self) -> str:
        return """You are a security code reviewer validating specific threats in code.

Your task is to examine actual source code and determine if identified threats manifest as real vulnerabilities.

For each vulnerability you find, provide:
1. Exact file path (relative to repo root)
2. Exact line number
3. Code snippet showing the vulnerability
4. Explanation of how it's exploitable
5. CWE ID
6. Severity
7. Recommendation for fixing

Be PRECISE:
- Provide actual line numbers, not ranges
- Include actual vulnerable code, not pseudocode
- Distinguish between real vulnerabilities and false positives
- Map findings to specific threats from the threat model

Only report CONFIRMED vulnerabilities with concrete evidence."""
    
    def build_user_prompt(self, security_md: str, threat_model: List[Dict], **kwargs) -> str:
        threats_summary = "\n".join([
            f"- {t.get('id')}: {t.get('title')} ({t.get('severity')})"
            for t in threat_model[:10]  # Limit to avoid token overflow
        ])
        
        return f"""Validate these threats by finding actual vulnerabilities in the code.

SECURITY ARCHITECTURE:
{security_md[:2000]}...

THREATS TO VALIDATE:
{threats_summary}

---

For each threat, search the codebase to find if it actually exists as a vulnerability.

Output a JSON array of confirmed vulnerabilities:

```json
[
  {{
    "threat_id": "THREAT-001",
    "title": "SQL Injection in user login",
    "description": "Detailed explanation of the vulnerability",
    "severity": "critical|high|medium|low",
    "file_path": "relative/path/to/file.py",
    "line_number": 42,
    "code_snippet": "cursor.execute('SELECT * FROM users WHERE username=' + username)",
    "cwe_id": "CWE-89",
    "recommendation": "Use parameterized queries",
    "evidence": "How you verified this is exploitable"
  }}
]
```

Steps:
1. For each threat, use Grep to search for vulnerability patterns
2. Read files to confirm the vulnerability exists
3. Get exact line numbers and code snippets
4. Only report CONFIRMED vulnerabilities

Output ONLY the JSON array."""
    
    def process_results(self, response: str, repo_path: str, **kwargs) -> Dict[str, Any]:
        """Parse vulnerabilities JSON and save to file"""
        
        # Extract JSON from response
        json_str = response.strip()
        
        # Try to find JSON array
        if '```json' in json_str:
            start = json_str.find('```json') + 7
            end = json_str.find('```', start)
            json_str = json_str[start:end].strip()
        elif '```' in json_str:
            start = json_str.find('```') + 3
            end = json_str.find('```', start)
            json_str = json_str[start:end].strip()
        
        # Find JSON array bounds
        if not json_str.startswith('['):
            start = json_str.find('[')
            if start != -1:
                json_str = json_str[start:]
        
        if not json_str.endswith(']'):
            end = json_str.rfind(']') + 1
            if end > 0:
                json_str = json_str[:end]
        
        try:
            vulnerabilities = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"⚠️  Failed to parse vulnerabilities JSON: {e}")
            print(f"Response preview: {json_str[:500]}")
            vulnerabilities = []
        
        # Save to file
        vulnguard_dir = self.get_vulnguard_dir(repo_path)
        vuln_file = vulnguard_dir / "VULNERABILITIES.json"
        vuln_file.write_text(json.dumps(vulnerabilities, indent=2))
        
        # Summary stats
        severity_counts = {}
        for vuln in vulnerabilities:
            sev = vuln.get('severity', 'unknown')
            severity_counts[sev] = severity_counts.get(sev, 0) + 1
        
        return {
            "file": str(vuln_file),
            "total_vulnerabilities": len(vulnerabilities),
            "by_severity": severity_counts,
            "summary": f"Found {len(vulnerabilities)} confirmed vulnerabilities"
        }
