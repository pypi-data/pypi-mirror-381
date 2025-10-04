# dj_boilerplate_generator/utils/validators.py
"""
Project validation utilities with enterprise standards
"""

import re
import keyword
from typing import Dict, List
from pathlib import Path


class ProjectValidator:
    """Enterprise project validation"""
    
    def __init__(self):
        self.reserved_names = [
            'django', 'test', 'admin', 'api', 'static', 'media',
            'user', 'group', 'contenttypes', 'sessions', 'auth'
        ]
    
    def validate_project_name(self, name: str) -> bool:
        """Validate project name against Django and Python standards"""
        if not name:
            return False
        
        # Check if it's a Python keyword
        if keyword.iskeyword(name):
            return False
        
        # Check if it's a reserved name
        if name.lower() in self.reserved_names:
            return False
        
        # Check naming conventions
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
            return False
        
        # Check for special characters
        if re.search(r'[^a-zA-Z0-9_]', name):
            return False
        
        return True
    
    def validate_configuration(self, config: Dict) -> bool:
        """Validate complete project configuration"""
        required_fields = ['project_name', 'database', 'python_version']
        
        for field in required_fields:
            if field not in config or not config[field]:
                return False
        
        # Validate project name
        if not self.validate_project_name(config['project_name']):
            return False
        
        # Validate output directory
        output_dir = Path(config.get('output_dir', '.'))
        if not output_dir.exists():
            return False
        
        return True
    
    def sanitize_project_name(self, name: str) -> str:
        """Sanitize project name to be Django-compatible"""
        # Replace hyphens and spaces with underscores
        sanitized = re.sub(r'[-\s]+', '_', name)
        
        # Remove special characters
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '', sanitized)
        
        # Ensure it starts with a letter
        if sanitized and not sanitized[0].isalpha():
            sanitized = 'project_' + sanitized
        
        return sanitized.lower()