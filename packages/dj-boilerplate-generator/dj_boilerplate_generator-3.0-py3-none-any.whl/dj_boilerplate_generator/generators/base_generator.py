# dj_boilerplate_generator/generators/base_generator.py
"""
Base Generator Class - Core project structure and architecture
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List
import jinja2

from dj_boilerplate_generator.utils.file_ops import FileOperations
from  dj_boilerplate_generator.utils.validators import ProjectValidator


class BaseGenerator:
    """Base generator for enterprise Django projects"""
    
    def __init__(self):
        self.file_ops = FileOperations()
        self.validator = ProjectValidator()
        self.template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader('templates/phase1'),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def create_project_structure(self, config: Dict):
        """Create enterprise project structure"""
        project_path = Path(config['output_dir']) / config['project_name']
        
        # Core directories
        directories = [
            # Project root
            project_path,
            project_path / config['project_name'],  # Python package
            project_path / config['project_name'] / 'settings',
            project_path / config['project_name'] / 'apps',
            project_path / config['project_name'] / 'apps' / 'core',
            project_path / config['project_name'] / 'apps' / 'api',
            
            # Static files
            project_path / 'static',
            project_path / 'static' / 'css',
            project_path / 'static' / 'js',
            project_path / 'static' / 'images',
            
            # Templates
            project_path / 'templates',
            project_path / 'templates' / 'admin',
            project_path / 'templates' / 'registration',
            
            # Documentation
            project_path / 'docs',
            project_path / 'docs' / 'architecture',
            project_path / 'docs' / 'deployment',
            
            # Configuration
            project_path / 'config',
            project_path / 'config' / 'environments',
            
            # Scripts
            project_path / 'scripts',
            project_path / 'scripts' / 'deployment',
            project_path / 'scripts' / 'monitoring',
        ]
        
        # Add SRE directories if enabled
        if 'sre' in config['features']:
            directories.extend([
                project_path / 'monitoring',
                project_path / 'monitoring' / 'dashboards',
                project_path / 'monitoring' / 'alerts',
            ])
        
        # Add Docker directories if enabled
        if 'docker' in config['features']:
            directories.extend([
                project_path / 'docker',
                project_path / 'docker' / 'development',
                project_path / 'docker' / 'production',
            ])
        
        # Create directories
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            
            # Add __init__.py to Python packages
            if any(x in str(directory) for x in ['apps', config['project_name']]):
                (directory / '__init__.py').touch()
    
    def generate_settings(self, config: Dict):
        """Generate modular settings architecture"""
        project_path = Path(config['output_dir']) / config['project_name']
        settings_dir = project_path / config['project_name'] / 'settings'
        
        # Context for templates
        context = {
            'project_name': config['project_name'],
            'database': config['database'],
            'features': config['features'],
            'python_version': config['python_version']
        }
        
        # Generate settings files
        settings_files = {
            'base.py.j2': 'base.py',
            'development.py.j2': 'development.py',
            'production.py.j2': 'production.py',
            'testing.py.j2': 'testing.py',
        }
        
        for template_name, output_name in settings_files.items():
            template = self.template_env.get_template(f'settings/{template_name}')
            content = template.render(**context)
            (settings_dir / output_name).write_text(content, encoding="utf-8")
        
        # Generate __init__.py for settings
        (settings_dir / '__init__.py').write_text("""
# Enterprise Django Settings Package
from .base import *

# Environment-specific settings
import os
env = os.environ.get('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
elif env == 'testing':
    from .testing import *
else:
    from .development import *
""", encoding="utf-8")
    
    def generate_core_app(self, config: Dict):
        """Generate core application with enterprise patterns"""
        project_path = Path(config['output_dir']) / config['project_name']
        core_app_dir = project_path / config['project_name'] / 'apps' / 'core'
        
        context = {
            'project_name': config['project_name'],
            'features': config['features']
        }
        
        # Core app files
        app_files = {
            'models.py.j2': 'models.py',
            'admin.py.j2': 'admin.py',
            'views.py.j2': 'views.py',
            'urls.py.j2': 'urls.py',
            'services.py.j2': 'services.py',
        }
        
        for template_name, output_name in app_files.items():
            template = self.template_env.get_template(f'core_app/{template_name}')
            content = template.render(**context)
            (core_app_dir / output_name).write_text(content, encoding="utf-8")
        
        # Generate apps.py
        apps_content = f"""
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{config['project_name']}.apps.core'
    verbose_name = 'Core Application'
    
    def ready(self):
        # Import signals and other startup code
        import {config['project_name']}.apps.core.signals
"""
        (core_app_dir / 'apps.py').write_text(apps_content, encoding="utf-8")
    
    def setup_development_tools(self, config: Dict):
        """Setup development tools and configuration"""
        project_path = Path(config['output_dir']) / config['project_name']
        
        # Ensure requirements directory exists
        requirements_dir = project_path / 'requirements'
        requirements_dir.mkdir(parents=True, exist_ok=True)

        # Requirements files
        requirements_content = self._generate_requirements(config)
        (requirements_dir / 'base.txt').write_text(requirements_content['base'], encoding="utf-8")
        (requirements_dir / 'dev.txt').write_text(requirements_content['dev'], encoding="utf-8")
        (requirements_dir / 'production.txt').write_text(requirements_content['production'], encoding="utf-8")

        # Pre-commit configuration
        pre_commit_config = """
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        args: [--safe]
        
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]
        
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=88]
        
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
"""
        (project_path / '.pre-commit-config.yaml').write_text(pre_commit_config, encoding="utf-8")
        
        # Docker configuration if enabled
        if 'docker' in config['features']:
            self._generate_docker_config(config, project_path)
    
    def configure_security(self, config: Dict):
        """Configure security foundations"""
        project_path = Path(config['output_dir']) / config['project_name']
        
        # Environment template
        env_template = """
# Django Settings
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/{project_name}

# Security
SECURE_SSL_REDIRECT=True
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True

# Monitoring (if SRE enabled)
PROMETHEUS_ENABLED=True
HEALTH_CHECK_ENDPOINT=/health/
""".format(project_name=config['project_name'])
        
        (project_path / '.env.example').write_text(env_template, encoding="utf-8")
        
        # Security middleware configuration
        security_config = """
# Security headers configuration
SECURITY_CONFIG = {
    'CSP_ENABLED': True,
    'HSTS_ENABLED': True,
    'XSS_FILTER_ENABLED': True,
    'CONTENT_TYPE_NOSNIFF': True,
    'REFERRER_POLICY': 'same-origin',
}
"""
        (project_path / 'config' / 'security.py').write_text(security_config)
    
    def _generate_requirements(self, config: Dict) -> Dict[str, str]:
        """Generate requirements files based on configuration"""
        
        base_requirements = [
            "Django",
            "psycopg2-binary>=2.9.6" if config['database'] == 'postgresql' else "",
            "mysqlclient>=2.1.1" if config['database'] == 'mysql' else "",
            "python-decouple>=3.8",
            "whitenoise>=6.4.0",
            "gunicorn>=20.1.0",
            "django-extensions>=3.2.1",
        ]
        
        dev_requirements = base_requirements + [
            "pytest>=7.3.1",
            "pytest-django>=4.5.2",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "pre-commit>=3.3.0",
            "django-debug-toolbar>=4.1.0",
        ]
        
        production_requirements = base_requirements + [
            "django-prometheus>=2.3.0" if 'sre' in config['features'] else "",
            "sentry-sdk>=1.28.1" if 'sre' in config['features'] else "",
        ]
        
        return {
            'base': '\n'.join(filter(None, base_requirements)),
            'dev': '\n'.join(filter(None, dev_requirements)),
            'production': '\n'.join(filter(None, production_requirements))
        }

    def _generate_docker_config(self, config: Dict, project_path: Path):
        """Generate Docker configuration using f-strings."""

        # Assign variables for clarity
        python_version = config['python_version']
        project_name = config['project_name']

        # --- Dockerfile ---
        dockerfile = f"""
    # Multi-stage Docker build for Enterprise Django
    FROM python:{python_version}-slim as builder

    # Install build dependencies
    RUN apt-get update && apt-get install -y \\
        gcc \\
        postgresql-dev \\
        && rm -rf /var/lib/apt/lists/*

    # Create virtual environment
    RUN python -m venv /opt/venv
    ENV PATH="/opt/venv/bin:$PATH"

    # Install dependencies
    COPY requirements/production.txt .
    RUN pip install --upgrade pip
    RUN pip install -r production.txt

    # --- Runtime stage ---
    FROM python:{python_version}-slim

    # Install runtime dependencies
    RUN apt-get update && apt-get install -y \\
        libpq5 \\
        && rm -rf /var/lib/apt/lists/*

    # Copy virtual environment
    COPY --from=builder /opt/venv /opt/venv
    ENV PATH="/opt/venv/bin:$PATH"

    # Create app user
    RUN useradd --create-home --shell /bin/bash app
    USER app
    WORKDIR /home/app

    # Copy project
    COPY --chown=app:app . .

    # Collect static files
    RUN python manage.py collectstatic --noinput

    # Run gunicorn
    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "{project_name}.wsgi:application"]
    """
        
        # --- docker-compose.yml ---
        compose_docker_file = f"""
    version: '3.8'

    services:
    web:
        build: .
        command: gunicorn --bind 0.0.0.0:8000 {project_name}.wsgi:application
        volumes:
        - .:/app
        ports:
        - "8000:8000"
        environment:
        - DATABASE_URL=postgres://user:password@db:5432/{project_name}
        - DJANGO_ENV=production
        depends_on:
        - db

    db:
        image: postgres:13
        environment:
        - POSTGRES_DB={project_name}
        - POSTGRES_USER=user
        - POSTGRES_PASSWORD=password
        volumes:
        - postgres_data:/var/lib/postgresql/data

    volumes:
    postgres_data:
    """
        
        try:
            (project_path / 'Dockerfile_ttt').write_text(dockerfile, encoding="utf-8")
            (project_path / 'docker-compose.yml').write_text(compose_docker_file, encoding="utf-8")
        except Exception as e:
            print(f"Error generating Docker configuration: {e}")