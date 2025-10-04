"""Threat Modeling Agent - Identifies threats based on architecture"""

import json
from pathlib import Path
from typing import Dict, Any, List
from vulnguard.agents.base import BaseAgent


class ThreatModelingAgent(BaseAgent):
    """Agent that performs threat modeling based on SECURITY.md"""
    
    @property
    def name(self) -> str:
        return "Threat Modeling"
    
    @property
    def allowed_tools(self) -> list[str]:
        return ["Read", "Write"]
    
    def build_system_prompt(self) -> str:
        return """You are a threat modeling expert specializing in application security.

Your task is to analyze a security architecture document and identify specific, actionable threats using STRIDE methodology.

STRIDE Categories:
- Spoofing: Impersonating users/systems
- Tampering: Unauthorized data modification
- Repudiation: Denying actions
- Information Disclosure: Unauthorized data access
- Denial of Service: Service availability attacks
- Elevation of Privilege: Gaining unauthorized permissions

For each threat, provide:
1. Category (STRIDE)
2. Title (brief, specific)
3. Description (detailed, context-aware)
4. Severity (critical, high, medium, low)
5. Affected Components
6. Attack Scenario
7. Potential Vulnerability Types (CWE references)

Focus on SPECIFIC threats based on the ACTUAL architecture, not generic security advice."""
    
    def build_user_prompt(self, security_md: str, **kwargs) -> str:
        return f"""Based on this security architecture document, identify specific threats.

{security_md}

---

Output a JSON array of threats with this structure:

```json
[
  {{
    "id": "THREAT-001",
    "category": "Spoofing|Tampering|Repudiation|Information Disclosure|Denial of Service|Elevation of Privilege",
    "title": "Brief specific title",
    "description": "Detailed description based on actual architecture",
    "severity": "critical|high|medium|low",
    "affected_components": ["Component1", "Component2"],
    "attack_scenario": "Step-by-step how this attack would work",
    "vulnerability_types": ["CWE-89", "CWE-78"],
    "mitigation": "How to prevent this threat"
  }}
]
```

Output ONLY the JSON array, no other text."""
    
    def process_results(self, response: str, repo_path: str, **kwargs) -> Dict[str, Any]:
        """Parse threat model JSON and save to file"""
        
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
            threats = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"⚠️  Failed to parse threat model JSON: {e}")
            print(f"Response preview: {json_str[:500]}")
            threats = []
        
        # Save to file
        vulnguard_dir = self.get_vulnguard_dir(repo_path)
        threat_file = vulnguard_dir / "THREAT_MODEL.json"
        threat_file.write_text(json.dumps(threats, indent=2))
        
        # Summary stats
        severity_counts = {}
        for threat in threats:
            sev = threat.get('severity', 'unknown')
            severity_counts[sev] = severity_counts.get(sev, 0) + 1
        
        return {
            "file": str(threat_file),
            "total_threats": len(threats),
            "by_severity": severity_counts,
            "summary": f"Identified {len(threats)} threats"
        }
