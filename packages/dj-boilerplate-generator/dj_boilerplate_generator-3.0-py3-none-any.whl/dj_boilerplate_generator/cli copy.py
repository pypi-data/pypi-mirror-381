# dj_boilerplate_generator/cli.py
"""
Enterprise CLI Interface with Interactive Prompts and Advanced Features
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from generators.base_generator import BaseGenerator
from utils.validators import ProjectValidator
from utils.file_ops import FileOperations

console = Console()


class EnterpriseCLI:
    """Advanced CLI with interactive prompts and rich UI"""
    
    def __init__(self):
        self.validator = ProjectValidator()
        self.file_ops = FileOperations()
        self.generator = BaseGenerator()
        
    def display_banner(self):
        """Display enterprise banner"""
        banner = """
╔════════════════════════════════════════════════════════════════╗
║                   ENTERPRISE DJANGO GENERATOR                  ║
║                 Phase 1: Foundation & Architecture             ║
╚════════════════════════════════════════════════════════════════╝
        """
        console.print(Panel(banner, style="bold cyan"))
    
    def parse_arguments(self) -> argparse.Namespace:
        """Parse command line arguments with advanced options"""
        parser = argparse.ArgumentParser(
            description='Generate enterprise-grade Django projects',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  django-enterprise myproject                    # Interactive mode
  django-enterprise myproject --non-interactive  # Quick start
  django-enterprise myproject --with-docker --with-sre
            """
        )
        
        parser.add_argument(
            'project_name', 
            nargs='?', 
            help='Name of your enterprise project'
        )
        
        # Core features
        parser.add_argument(
            '--non-interactive', 
            action='store_true',
            help='Skip interactive prompts'
        )
        
        parser.add_argument(
            '--with-docker', 
            action='store_true',
            help='Include Docker multi-stage setup'
        )
        
        parser.add_argument(
            '--with-sre', 
            action='store_true',
            help='Include basic SRE foundations'
        )
        
        parser.add_argument(
            '--output-dir',
            type=str,
            default='.',
            help='Output directory for project generation'
        )
        
        parser.add_argument(
            '--python-version',
            type=str,
            default='3.11',
            choices=['3.10', '3.11', '3.12'],
            help='Python version for the project'
        )
        
        parser.add_argument(
            '--database',
            type=str,
            default='postgresql',
            choices=['postgresql', 'mysql', 'sqlite'],
            help='Database backend'
        )
        
        return parser.parse_args()
    
    def interactive_setup(self) -> Dict:
        """Interactive project configuration with rich prompts"""
        console.print("\n[bold blue]🎯 Project Configuration[/bold blue]")
        
        # Project name with validation
        project_name = questionary.text(
            "Project name:",
            validate=lambda text: self.validator.validate_project_name(text)
        ).ask()
        
        # Database selection
        database = questionary.select(
            "Select database:",
            choices=[
                {"name": "PostgreSQL (Recommended)", "value": "postgresql"},
                {"name": "MySQL", "value": "mysql"},
                {"name": "SQLite (Development only)", "value": "sqlite"}
            ]
        ).ask()
        
        # Feature selection
        features = questionary.checkbox(
            "Select enterprise features:",
            choices=[
                {"name": "Docker & Containerization", "value": "docker"},
                {"name": "SRE Foundations (Monitoring)", "value": "sre"},
                {"name": "API-First Architecture", "value": "api"},
                {"name": "Advanced Security", "value": "security"}
            ]
        ).ask()
        
        # Python version
        python_version = questionary.select(
            "Python version:",
            choices=["3.10", "3.11", "3.12"],
            default="3.11"
        ).ask()
        
        return {
            'project_name': project_name,
            'database': database,
            'features': features,
            'python_version': python_version,
            'output_dir': '.'
        }
    
    def generate_project(self, config: Dict):
        """Generate project with progress tracking"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            console=console
        ) as progress:
            
            task1 = progress.add_task("[cyan]Validating configuration...", total=100)
            progress.update(task1, advance=20)
            
            # Validate project configuration
            if not self.validator.validate_configuration(config):
                console.print("[red]❌ Configuration validation failed[/red]")
                sys.exit(1)
            progress.update(task1, advance=80)
            
            task2 = progress.add_task("[green]Creating project structure...", total=100)
            self.generator.create_project_structure(config)
            progress.update(task2, advance=100)
            
            task3 = progress.add_task("[yellow]Generating enterprise settings...", total=100)
            self.generator.generate_settings(config)
            progress.update(task3, advance=100)
            
            task4 = progress.add_task("[magenta]Setting up development tools...", total=100)
            self.generator.setup_development_tools(config)
            progress.update(task4, advance=100)
            
            task5 = progress.add_task("[blue]Configuring security foundations...", total=100)
            self.generator.configure_security(config)
            progress.update(task5, advance=100)
    
    def run(self):
        """Main CLI entry point"""
        try:
            self.display_banner()
            args = self.parse_arguments()
            
            if args.non_interactive and not args.project_name:
                console.print("[red]Error: Project name required in non-interactive mode[/red]")
                sys.exit(1)
            
            if args.non_interactive:
                # Non-interactive mode
                config = {
                    'project_name': args.project_name,
                    'database': args.database,
                    'features': [],
                    'python_version': args.python_version,
                    'output_dir': args.output_dir
                }
                
                if args.with_docker:
                    config['features'].append('docker')
                if args.with_sre:
                    config['features'].append('sre')
                    
            else:
                # Interactive mode
                config = self.interactive_setup()
                if args.project_name:
                    config['project_name'] = args.project_name
            
            console.print(f"\n[bold green]🚀 Generating: {config['project_name']}[/bold green]")
            console.print(f"📊 Database: {config['database']}")
            console.print(f"🐍 Python: {config['python_version']}")
            console.print(f"✨ Features: {', '.join(config['features']) if config['features'] else 'Standard'}")
            
            # Confirm generation
            if not args.non_interactive:
                confirm = questionary.confirm(
                    "Proceed with project generation?"
                ).ask()
                if not confirm:
                    console.print("[yellow]Generation cancelled[/yellow]")
                    return
            
            self.generate_project(config)
            
            # Show success message
            self.show_success_message(config)
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled by user[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            sys.exit(1)
    
    def show_success_message(self, config: Dict):
        """Display success message with next steps"""
        project_path = Path(config['output_dir']) / config['project_name']
        
        success_panel = Panel.fit(
            f"""
🎉 [bold green]Enterprise Django Project Generated Successfully![/bold green]

📁 Project Location: [cyan]{project_path}[/cyan]

🚀 [bold]Next Steps:[/bold]
1. [yellow]cd {project_path}[/yellow]
2. [yellow]python -m venv venv[/yellow]
3. [yellow]source venv/bin/activate[/yellow] (Linux/Mac)
   [yellow]venv\\Scripts\\activate[/yellow] (Windows)
4. [yellow]pip install -r requirements/dev.txt[/yellow]
5. [yellow]cp .env.example .env[/yellow]
6. [yellow]python manage.py migrate[/yellow]
7. [yellow]python manage.py runserver[/yellow]

🔧 [bold]Development Tools:[/bold]
• Pre-commit hooks installed
• Docker setup ready
• Monitoring configured
• Security best practices applied

📚 Documentation: [cyan]README.md[/cyan] for detailed instructions
            """,
            title="Project Ready 🚀",
            border_style="green"
        )
        
        console.print(success_panel)


def main():
    """Main entry point"""
    cli = EnterpriseCLI()
    cli.run()


if __name__ == "__main__":
    main()