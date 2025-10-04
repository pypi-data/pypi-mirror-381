"""Smart context gathering for vulnerability validation"""

import ast
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


class ContextGatherer:
    """Gathers comprehensive code context for vulnerability validation"""
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
    
    def gather_comprehensive_context(
        self, 
        threat_model: List[Dict[str, Any]]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Gather comprehensive context for each threat
        
        Returns:
            Dict mapping threat_id to list of context objects
        """
        evidence = {}
        
        for threat in threat_model[:15]:  # Process top 15 threats
            threat_id = threat['id']
            contexts = []
            
            # Parse affected components
            for component in threat.get('affected_components', []):
                context = self._gather_component_context(component, threat)
                if context:
                    contexts.append(context)
            
            if contexts:
                evidence[threat_id] = contexts
        
        return evidence
    
    def _gather_component_context(
        self, 
        component: str, 
        threat: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Gather context for a single component"""
        
        # Parse component format: "file.py::function (line 123)"
        match = re.match(
            r'([^:]+)::([^(]+)\s*\(.*?line[s]?\s*(\d+)', 
            component
        )
        
        if not match:
            return None
        
        file_path, func_name, line_num = match.groups()
        line_num = int(line_num)
        
        full_path = self.repo_path / file_path
        if not full_path.exists():
            return None
        
        # Gather comprehensive context
        return {
            'file_path': file_path,
            'line_number': line_num,
            'function_name': func_name,
            'primary_code': self._get_function_definition(full_path, func_name),
            'surrounding_context': self._get_surrounding_lines(full_path, line_num),
            'function_calls': self._find_function_calls(full_path, func_name),
            'imports': self._get_file_imports(full_path),
            'callers': self._find_callers(file_path, func_name),
            'data_flow': self._analyze_data_flow(full_path, func_name, line_num),
            'related_config': self._find_related_config(threat),
        }
    
    def _get_function_definition(
        self, 
        file_path: Path, 
        func_name: str
    ) -> Dict[str, Any]:
        """Extract complete function definition using AST"""
        
        try:
            with open(file_path) as f:
                content = f.read()
            
            tree = ast.parse(content)
            lines = content.split('\n')
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == func_name:
                    start = node.lineno
                    end = node.end_lineno or start
                    
                    # Get decorators
                    decorators = []
                    for dec in node.decorator_list:
                        if isinstance(dec, ast.Name):
                            decorators.append(dec.id)
                        elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name):
                            decorators.append(dec.func.id)
                    
                    return {
                        'source': '\n'.join(lines[start-1:end]),
                        'start_line': start,
                        'end_line': end,
                        'decorators': decorators,
                        'parameters': [arg.arg for arg in node.args.args]
                    }
        except Exception as e:
            print(f"⚠️  Could not parse {file_path}: {e}")
        
        return {'source': '', 'start_line': 0, 'end_line': 0}
    
    def _get_surrounding_lines(
        self, 
        file_path: Path, 
        line_num: int, 
        context_lines: int = 10
    ) -> Dict[str, Any]:
        """Get surrounding lines with context"""
        
        try:
            with open(file_path) as f:
                lines = f.readlines()
            
            start = max(0, line_num - context_lines - 1)
            end = min(len(lines), line_num + context_lines)
            
            return {
                'lines': [l.rstrip() for l in lines[start:end]],
                'start_line': start + 1,
                'target_line': line_num,
                'target_content': lines[line_num - 1].rstrip() if line_num <= len(lines) else ''
            }
        except Exception:
            return {'lines': [], 'start_line': 0, 'target_line': line_num}
    
    def _find_function_calls(
        self, 
        file_path: Path, 
        func_name: str
    ) -> List[str]:
        """Find what functions are called within this function"""
        
        try:
            with open(file_path) as f:
                content = f.read()
            
            tree = ast.parse(content)
            calls = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == func_name:
                    # Find all function calls within this function
                    for child in ast.walk(node):
                        if isinstance(child, ast.Call):
                            if isinstance(child.func, ast.Name):
                                calls.append(child.func.id)
                            elif isinstance(child.func, ast.Attribute):
                                calls.append(child.func.attr)
            
            return list(set(calls))[:10]  # Limit to 10
        except Exception:
            return []
    
    def _get_file_imports(self, file_path: Path) -> List[str]:
        """Extract imports from file"""
        
        try:
            with open(file_path) as f:
                content = f.read()
            
            tree = ast.parse(content)
            imports = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
            
            return imports
        except Exception:
            return []
    
    def _find_callers(
        self, 
        file_path: str, 
        func_name: str
    ) -> List[Dict[str, Any]]:
        """Find places where this function is called"""
        
        try:
            # Use subprocess to run grep
            result = subprocess.run(
                ['grep', '-rn', f'{func_name}(', str(self.repo_path)],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            callers = []
            for line in result.stdout.split('\n')[:15]:  # Limit to 15
                if ':' not in line:
                    continue
                
                parts = line.split(':', 2)
                if len(parts) >= 3:
                    caller_file = parts[0].replace(str(self.repo_path) + '/', '')
                    caller_line = parts[1]
                    caller_code = parts[2].strip()
                    
                    # Skip the definition itself
                    if f'def {func_name}' in caller_code:
                        continue
                    
                    callers.append({
                        'file': caller_file,
                        'line': caller_line,
                        'code': caller_code[:200]  # Limit length
                    })
            
            return callers
        except Exception:
            return []
    
    def _analyze_data_flow(
        self, 
        file_path: Path, 
        func_name: str, 
        line_num: int
    ) -> Dict[str, Any]:
        """Basic data flow analysis for the target line"""
        
        try:
            with open(file_path) as f:
                lines = f.readlines()
            
            if line_num > len(lines):
                return {}
            
            target_line = lines[line_num - 1]
            
            # Extract variables used in the line
            variables = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', target_line)
            
            # Find variable sources (simple backward scan)
            sources = {}
            for var in set(variables):
                # Look backward up to 30 lines
                for i in range(line_num - 2, max(0, line_num - 30), -1):
                    line = lines[i]
                    if f'{var} =' in line or f'{var}=' in line:
                        sources[var] = {
                            'line': i + 1,
                            'source': line.strip()[:150]
                        }
                        break
            
            return {
                'target_line': target_line.strip(),
                'variables': list(set(variables)),
                'sources': sources
            }
        except Exception:
            return {}
    
    def _find_related_config(self, threat: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Find configuration related to this threat"""
        
        configs = []
        
        # Config file patterns
        config_files = [
            'settings.py', 'config.py', 'config.yaml', 
            'config.json', '.env.example', 'pyproject.toml'
        ]
        
        # Keywords to look for based on threat
        keywords = self._extract_config_keywords(threat)
        
        for config_name in config_files:
            config_path = self.repo_path / config_name
            if not config_path.exists():
                continue
            
            try:
                with open(config_path) as f:
                    content = f.read()
                
                relevant_lines = []
                for line in content.split('\n'):
                    if any(kw.upper() in line.upper() for kw in keywords):
                        relevant_lines.append(line.strip())
                
                if relevant_lines:
                    configs.append({
                        'file': config_name,
                        'lines': relevant_lines[:10]
                    })
            except Exception:
                continue
        
        return configs
    
    def _extract_config_keywords(self, threat: Dict[str, Any]) -> List[str]:
        """Extract relevant config keywords from threat"""
        
        keywords = ['DEBUG', 'SECRET', 'KEY', 'PASSWORD']
        
        # Add threat-specific keywords
        threat_keywords = {
            'sql injection': ['DATABASE', 'DB_'],
            'xss': ['ALLOWED_HOSTS', 'CORS'],
            'csrf': ['CSRF'],
            'command injection': ['SHELL', 'EXEC'],
            'deserialization': ['PICKLE', 'YAML'],
        }
        
        description = threat.get('description', '').lower()
        for pattern, kws in threat_keywords.items():
            if pattern in description:
                keywords.extend(kws)
        
        return keywords
