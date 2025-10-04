"""Code Review Agent - Validates threats in actual code"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional
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
    
    def build_user_prompt(
        self, 
        security_md: str, 
        threat_model: List[Dict],
        code_evidence: Optional[Dict[str, Any]] = None,
        use_staged_output: bool = False,
        **kwargs
    ) -> str:
        """Build prompt with optional pre-gathered evidence"""
        
        # If we have pre-gathered evidence, use no-tools prompt
        if code_evidence:
            return self._build_prompt_with_evidence(
                security_md, threat_model, code_evidence
            )
        
        # Otherwise use tools with staged output
        if use_staged_output:
            return self._build_staged_prompt(security_md, threat_model)
        
        # Original prompt (kept for compatibility)
        return self._build_original_prompt(security_md, threat_model)
    
    def _build_original_prompt(self, security_md: str, threat_model: List[Dict]) -> str:
        """Original prompt for backwards compatibility"""
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
    
    def _build_prompt_with_evidence(
        self,
        security_md: str,
        threat_model: List[Dict],
        code_evidence: Dict[str, Any]
    ) -> str:
        """Prompt with pre-gathered code evidence - no tools needed"""
        
        # Build comprehensive threat data with code
        threats_with_context = []
        
        for threat in threat_model[:15]:
            threat_id = threat['id']
            evidence = code_evidence.get(threat_id, [])
            
            threats_with_context.append({
                'id': threat_id,
                'title': threat['title'],
                'description': threat['description'],
                'severity': threat['severity'],
                'cwe': threat.get('vulnerability_types', []),
                'code_context': evidence
            })
        
        threats_json = json.dumps(threats_with_context, indent=2)
        
        return f"""Validate security threats using provided code context.

THREATS WITH CODE CONTEXT:
{threats_json}

For each threat, review the provided code context to determine if it's a confirmed vulnerability.

<validation_criteria>
A vulnerability is CONFIRMED if:
1. The code pattern matches the threat description
2. There is no proper input validation/sanitization
3. The vulnerability is exploitable
4. You have concrete evidence (file path, line number, code snippet)
</validation_criteria>

<output_format>
Output ONLY a valid JSON array. No explanation text.

Start with: [
End with: ]

Each confirmed vulnerability must have:
{{
  "threat_id": "THREAT-XXX",
  "title": "Brief title",
  "description": "How this is exploitable",
  "severity": "critical|high|medium|low",
  "file_path": "relative/path/file.py",
  "line_number": 123,
  "code_snippet": "actual vulnerable code",
  "cwe_id": "CWE-XXX",
  "recommendation": "How to fix",
  "evidence": "Why this is confirmed"
}}

If no vulnerabilities are confirmed, output: []
</output_format>

CRITICAL: Output must be ONLY the JSON array. Do not include any explanation, markdown, or other text.

Begin validation now:"""
    
    def _build_staged_prompt(
        self,
        security_md: str,
        threat_model: List[Dict]
    ) -> str:
        """Prompt for staged output with tools"""
        
        threats_summary = "\n".join([
            f"- {t['id']}: {t['title']} (severity: {t['severity']})"
            for t in threat_model[:15]
        ])
        
        return f"""Validate security threats using a TWO-STAGE process.

SECURITY CONTEXT:
{security_md[:2000]}

THREATS TO VALIDATE:
{threats_summary}

<process>
STAGE 1 - INVESTIGATION:
Use Read, Grep, and Glob tools to investigate each threat.
Document your findings as you go.
When investigation is complete, output exactly: "===INVESTIGATION COMPLETE==="

STAGE 2 - STRUCTURED OUTPUT:
After the marker, output ONLY valid JSON array of confirmed vulnerabilities.
No markdown, no explanation, just the JSON array.

Format:
[{{"threat_id": "...", "title": "...", ...}}]
</process>

Begin Stage 1 investigation now:"""
    
    def process_results(self, response: str, repo_path: str, **kwargs) -> Dict[str, Any]:
        """Parse vulnerabilities with enhanced extraction"""
        
        # Check for staged output
        investigation_notes = ""
        json_part = response
        
        if "===INVESTIGATION COMPLETE===" in response:
            parts = response.split("===INVESTIGATION COMPLETE===", 1)
            investigation_notes = parts[0]
            json_part = parts[1]
        
        # Extract JSON
        vulnerabilities = self._extract_json_robust(json_part)
        
        # Validate and save
        vulnerabilities = self._validate_vulnerabilities(vulnerabilities)
        
        vulnguard_dir = self.get_vulnguard_dir(repo_path)
        
        # Save investigation notes if present
        if investigation_notes:
            notes_file = vulnguard_dir / "INVESTIGATION_NOTES.md"
            notes_file.write_text(investigation_notes)
        
        # Save vulnerabilities
        vuln_file = vulnguard_dir / "VULNERABILITIES.json"
        vuln_file.write_text(json.dumps(vulnerabilities, indent=2))
        
        # Calculate stats
        severity_counts = {}
        for vuln in vulnerabilities:
            sev = vuln.get('severity', 'unknown')
            severity_counts[sev] = severity_counts.get(sev, 0) + 1
        
        return {
            "file": str(vuln_file),
            "total_vulnerabilities": len(vulnerabilities),
            "by_severity": severity_counts,
            "summary": f"Found {len(vulnerabilities)} confirmed vulnerabilities",
            "had_investigation_notes": bool(investigation_notes)
        }
    
    def _extract_json_robust(self, text: str) -> List[Dict]:
        """Robust JSON extraction with multiple strategies"""
        
        # Strategy 1: Pure JSON
        try:
            return json.loads(text.strip())
        except json.JSONDecodeError:
            pass
        
        # Strategy 2: Code block extraction
        if '```json' in text:
            match = re.search(r'```json\s*(\[.*?\])\s*```', text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except json.JSONDecodeError:
                    pass
        
        # Strategy 3: Find array boundaries
        start = text.find('[')
        end = text.rfind(']')
        if start != -1 and end > start:
            try:
                return json.loads(text[start:end+1])
            except json.JSONDecodeError:
                pass
        
        # Strategy 4: Multi-line array with regex
        pattern = r'\[\s*\{.*?\}\s*\]'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
        
        # Log failure
        print(f"⚠️  Failed to parse JSON from response")
        print(f"Response preview: {text[:500]}")
        
        return []
    
    def _validate_vulnerabilities(self, vulnerabilities: List) -> List[Dict]:
        """Validate each vulnerability has required fields"""
        
        required_fields = [
            'threat_id', 'title', 'description', 'severity',
            'file_path', 'line_number', 'code_snippet',
            'cwe_id', 'recommendation'
        ]
        
        valid = []
        
        for vuln in vulnerabilities:
            if not isinstance(vuln, dict):
                continue
            
            # Check required fields
            if all(field in vuln for field in required_fields):
                # Normalize severity
                if vuln['severity'] not in ['critical', 'high', 'medium', 'low']:
                    vuln['severity'] = 'medium'
                
                # Ensure line_number is int
                try:
                    vuln['line_number'] = int(vuln['line_number'])
                except (ValueError, TypeError):
                    vuln['line_number'] = 0
                
                valid.append(vuln)
            else:
                missing = [f for f in required_fields if f not in vuln]
                print(f"⚠️  Skipping invalid vulnerability (missing: {missing})")
        
        return valid
