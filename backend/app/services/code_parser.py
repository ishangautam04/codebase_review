"""
Code parsing and analysis service
"""
import os
from pathlib import Path
from typing import List, Dict, Set
import json

class CodeParserService:
    """Service for parsing and analyzing code files"""
    
    SUPPORTED_EXTENSIONS = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.jsx': 'javascript',
        '.java': 'java',
        '.go': 'go',
        '.rs': 'rust',
        '.rb': 'ruby',
        '.php': 'php',
        '.cpp': 'cpp',
        '.c': 'c',
        '.cs': 'csharp',
    }
    
    IGNORE_DIRS = {
        'node_modules', '.git', '__pycache__', 'venv', 'env',
        'dist', 'build', '.next', 'out', 'target', 'vendor'
    }
    
    CONFIG_FILES = {
        'package.json': 'node',
        'requirements.txt': 'python',
        'Pipfile': 'python',
        'pyproject.toml': 'python',
        'Cargo.toml': 'rust',
        'go.mod': 'go',
        'pom.xml': 'java',
        'Gemfile': 'ruby',
    }
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
    
    def parse_structure(self) -> Dict:
        """Parse repository file structure"""
        structure = self._build_tree(self.repo_path)
        return structure
    
    def _build_tree(self, path: Path, max_depth: int = 5, current_depth: int = 0) -> Dict:
        """Recursively build file tree"""
        if current_depth > max_depth:
            return None
        
        name = path.name
        
        if path.is_file():
            ext = path.suffix
            return {
                'name': name,
                'type': 'file',
                'path': str(path.relative_to(self.repo_path)),
                'language': self.SUPPORTED_EXTENSIONS.get(ext, 'unknown'),
                'size': path.stat().st_size
            }
        
        elif path.is_dir():
            # Skip ignored directories
            if name in self.IGNORE_DIRS:
                return None
            
            children = []
            try:
                for child in sorted(path.iterdir()):
                    child_node = self._build_tree(child, max_depth, current_depth + 1)
                    if child_node:
                        children.append(child_node)
            except PermissionError:
                pass
            
            return {
                'name': name,
                'type': 'directory',
                'path': str(path.relative_to(self.repo_path)),
                'children': children
            }
    
    def identify_entry_points(self) -> List[Dict]:
        """Identify application entry points"""
        entry_points = []
        
        # Common entry point files
        entry_files = [
            ('main.py', 'python', 'Python application entry'),
            ('app.py', 'python', 'Python Flask/FastAPI app'),
            ('__main__.py', 'python', 'Python module entry'),
            ('index.js', 'javascript', 'JavaScript entry'),
            ('index.ts', 'typescript', 'TypeScript entry'),
            ('main.go', 'go', 'Go application entry'),
            ('main.rs', 'rust', 'Rust application entry'),
            ('Main.java', 'java', 'Java application entry'),
        ]
        
        for file_name, language, description in entry_files:
            matches = list(self.repo_path.rglob(file_name))
            for match in matches:
                # Skip files in node_modules, etc.
                if any(ignore in match.parts for ignore in self.IGNORE_DIRS):
                    continue
                
                entry_points.append({
                    'file': str(match.relative_to(self.repo_path)),
                    'type': 'application_entry',
                    'language': language,
                    'description': description
                })
        
        return entry_points
    
    def parse_dependencies(self) -> List[Dict]:
        """Parse project dependencies"""
        dependencies = []
        
        # Parse package.json
        package_json = self.repo_path / 'package.json'
        if package_json.exists():
            try:
                with open(package_json, 'r') as f:
                    data = json.load(f)
                    
                    for dep, version in data.get('dependencies', {}).items():
                        dependencies.append({
                            'name': dep,
                            'version': version,
                            'type': 'production',
                            'language': 'javascript'
                        })
                    
                    for dep, version in data.get('devDependencies', {}).items():
                        dependencies.append({
                            'name': dep,
                            'version': version,
                            'type': 'development',
                            'language': 'javascript'
                        })
            except:
                pass
        
        # Parse requirements.txt
        requirements = self.repo_path / 'requirements.txt'
        if requirements.exists():
            try:
                with open(requirements, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            parts = line.split('==')
                            name = parts[0]
                            version = parts[1] if len(parts) > 1 else 'unknown'
                            dependencies.append({
                                'name': name,
                                'version': version,
                                'type': 'production',
                                'language': 'python'
                            })
            except:
                pass
        
        return dependencies
    
    def get_statistics(self) -> Dict:
        """Calculate repository statistics"""
        stats = {
            'total_files': 0,
            'total_lines': 0,
            'languages': {},
            'file_types': {}
        }
        
        for file_path in self.repo_path.rglob('*'):
            # Skip directories and ignored paths
            if not file_path.is_file():
                continue
            if any(ignore in file_path.parts for ignore in self.IGNORE_DIRS):
                continue
            
            ext = file_path.suffix
            language = self.SUPPORTED_EXTENSIONS.get(ext, 'other')
            
            stats['total_files'] += 1
            stats['languages'][language] = stats['languages'].get(language, 0) + 1
            stats['file_types'][ext] = stats['file_types'].get(ext, 0) + 1
            
            # Count lines
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = len(f.readlines())
                    stats['total_lines'] += lines
            except:
                pass
        
        return stats
