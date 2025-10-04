# src/dj_boilerplate_generator/generators/django_core.py
"""
Leverage Django's built-in startproject command for project creation
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import Dict, List
from django.core.management import execute_from_command_line
from django.core.management.commands.startproject import Command as StartProjectCommand

from dj_boilerplate_generator.utils.file_ops import FileOperations
from  dj_boilerplate_generator.utils.validators import ProjectValidator


class DjangoCoreGenerator:
    """Generator that uses Django's startproject as foundation"""
    
    def __init__(self):
        self.file_ops = FileOperations()
        self.validator = ProjectValidator()
    
    def create_django_project(self, config: Dict):
        """Use Django's startproject command to create the base project"""
    
        project_path = Path(config['output_dir']) / config['project_name']
        project_name = config['project_name']

        print(f"🚀 Creating Django project using django-admin startproject...")

        # Ensure the project directory exists and is empty
        project_path.mkdir(parents=True, exist_ok=True)
        if any(project_path.iterdir()):
            print(f"❌ Target directory {project_path} is not empty. Please choose an empty directory.")
            return

        try:
            # Run startproject inside the new directory
            result = subprocess.run([
                sys.executable, '-m', 'django', 'startproject',
                project_name,
                '.'
            ], capture_output=True, text=True, cwd=str(project_path))

            if result.returncode != 0:
                raise Exception(f"Django startproject failed: {result.stderr}")

            print(f"✅ Django project created successfully")

        except Exception as e:
            print(f"❌ Django command failed: {e}")
            # Fallback to manual method
            self._create_project_manually(project_path, project_name)
    
    def _create_project_manually(self, project_path: Path, project_name: str):
        """Fallback method if django-admin is not available"""
        print("🔄 Using manual project creation...")
        
        # Create basic Django project structure
        project_dir = project_path / project_name
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Create manage.py
        manage_content = f"""#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)
"""
        (project_path / 'manage.py').write_text(manage_content,encoding="utf-8")
        (project_path / 'manage.py').chmod(0o755)
        
        # Create project package
        (project_dir / '__init__.py').touch()
        
        # Create basic settings.py
        settings_content = f"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-change-this-in-production'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = '{project_name}.urls'

TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]

WSGI_APPLICATION = '{project_name}.wsgi.application'

DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }}
}}

STATIC_URL = '/static/'
"""
        (project_dir / 'settings.py').write_text(settings_content)
        
        # Create urls.py
        urls_content = f"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
        (project_dir / 'urls.py').write_text(urls_content)
        
        # Create wsgi.py
        wsgi_content = f"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')

application = get_wsgi_application()
"""
        (project_dir / 'wsgi.py').write_text(wsgi_content)
        
        print("✅ Manual project creation completed")