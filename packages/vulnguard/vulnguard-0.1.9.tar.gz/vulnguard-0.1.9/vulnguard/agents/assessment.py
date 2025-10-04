"""Code Assessment Agent - Maps architecture and creates SECURITY.md"""

from pathlib import Path
from typing import Dict, Any
from vulnguard.agents.base import BaseAgent


class AssessmentAgent(BaseAgent):
    """Agent that analyzes codebase architecture for security documentation"""
    
    @property
    def name(self) -> str:
        return "Assessment"
    
    @property
    def allowed_tools(self) -> list[str]:
        return ["Read", "Grep", "Glob", "LS"]
    
    def build_system_prompt(self) -> str:
        return """You are a software architect specializing in security documentation.

Your task is to analyze a codebase and create comprehensive security architecture documentation.

Focus on:
1. Overall architecture and component structure
2. Data flow between components
3. Authentication and authorization mechanisms
4. External dependencies and APIs
5. Sensitive data paths (user data, credentials, etc.)
6. Entry points (APIs, forms, endpoints)
7. Technology stack and frameworks

Create a well-structured Markdown document that security engineers can use for threat modeling."""
    
    def build_user_prompt(self, **kwargs) -> str:
        return """Analyze this codebase and create a comprehensive SECURITY.md document.

STRUCTURE YOUR ANALYSIS AS FOLLOWS:

# Security Architecture

## Overview
[Brief description of the application and its purpose]

## Architecture
[Component diagram in text/ASCII or description of major components]

## Technology Stack
[Languages, frameworks, databases, external services]

## Entry Points
[All ways users/external systems interact with the application]
- API endpoints
- Web forms
- CLI commands
- External webhooks

## Authentication & Authorization
[How users authenticate and what authorization mechanisms exist]

## Data Flow
[How data moves through the system, especially sensitive data]
1. User input → Processing → Storage
2. External API → Internal processing
3. Database → Application → Output

## Sensitive Data
[What sensitive data is handled and where]
- User credentials
- Personal information
- API keys/secrets
- Financial data

## External Dependencies
[Third-party libraries, APIs, services]

## Security Controls
[Existing security measures, if any]
- Input validation
- CSRF protection
- Rate limiting
- Encryption

## Notes
[Any other security-relevant observations]

---

Use Read, Grep, and Glob tools to explore the codebase thoroughly.
Output the complete SECURITY.md document."""
    
    def process_results(self, response: str, repo_path: str, **kwargs) -> Dict[str, Any]:
        """Save SECURITY.md and return summary"""
        
        # Extract markdown content
        security_md = response.strip()
        
        # Ensure it starts with # Security Architecture
        if not security_md.startswith("# Security Architecture"):
            # Try to extract if it's embedded in explanation
            if "# Security Architecture" in security_md:
                start = security_md.find("# Security Architecture")
                security_md = security_md[start:]
            else:
                # Wrap the content
                security_md = f"# Security Architecture\n\n{security_md}"
        
        # Save to file
        vulnguard_dir = self.get_vulnguard_dir(repo_path)
        security_file = vulnguard_dir / "SECURITY.md"
        security_file.write_text(security_md)
        
        # Extract summary stats
        lines = security_md.split('\n')
        sections = [line for line in lines if line.startswith('## ')]
        
        return {
            "file": str(security_file),
            "size_bytes": len(security_md),
            "sections": len(sections),
            "summary": f"Created SECURITY.md with {len(sections)} sections"
        }
