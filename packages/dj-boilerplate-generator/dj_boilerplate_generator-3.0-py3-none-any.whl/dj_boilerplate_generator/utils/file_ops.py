# dj_boilerplate_generator/utils/file_ops.py
"""
Advanced file operations with template rendering
"""

import shutil
from pathlib import Path
from typing import Dict
import jinja2


class FileOperations:
    """Enterprise file operations with template support"""
    
    def __init__(self):
        self.template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates'),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def copy_template(self, template_path: str, destination: Path, context: Dict = None):
        """Copy and render template file"""
        if context is None:
            context = {}
        
        try:
            template = self.template_env.get_template(template_path)
            rendered_content = template.render(**context)
            destination.write_text(rendered_content,encoding="utf-8")
        except Exception as e:
            raise Exception(f"Template rendering failed: {e}")
    
    def create_symlink(self, source: Path, destination: Path):
        """Create symbolic link (platform independent)"""
        try:
            if destination.exists():
                destination.unlink()
            destination.symlink_to(source)
        except OSError:
            # Fallback to copy on Windows or when symlinks aren't supported
            shutil.copy2(source, destination)
    
    def ensure_directory(self, path: Path):
        """Ensure directory exists with proper permissions"""
        path.mkdir(parents=True, exist_ok=True)
        # Set secure permissions (read/write for owner, read for group/others)
        path.chmod(0o755)