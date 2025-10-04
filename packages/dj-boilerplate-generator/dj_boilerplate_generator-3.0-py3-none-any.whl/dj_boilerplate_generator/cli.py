# src/dj_boilerplate_generator/cli.py
"""
Enterprise CLI Interface - Leveraging Django's startproject command
Phase 1: Foundation & Core Architecture
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Optional rich dependencies with fallbacks
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

try:
    import questionary
    QUESTIONARY_AVAILABLE = True
except ImportError:
    QUESTIONARY_AVAILABLE = False

# Local imports
from dj_boilerplate_generator.generators.enhanced_generator import EnhancedProjectGenerator
from dj_boilerplate_generator.utils.validators import ProjectValidator

# Create console only if rich is available
console = Console() if RICH_AVAILABLE else None


class EnterpriseCLI:
    """Advanced CLI with interactive prompts that uses Django's startproject as foundation"""
    
    def __init__(self):
        self.validator = ProjectValidator()
        self.generator = EnhancedProjectGenerator()
        
    def display_banner(self):
        """Display enterprise banner"""
        banner = """
╔════════════════════════════════════════════════════════════════╗
║                   ENTERPRISE DJANGO GENERATOR                  ║
║           Leveraging Django's startproject + Enhancements      ║
╚════════════════════════════════════════════════════════════════╝
        """
        if console:
            console.print(Panel(banner, style="bold cyan"))
        else:
            print(banner)
    
    def parse_arguments(self) -> argparse.Namespace:
        """Parse command line arguments with advanced options"""
        parser = argparse.ArgumentParser(
            description='Generate enterprise-grade Django projects using Django\'s startproject',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  django-enterprise myproject                    # Interactive mode
  django-enterprise myproject --non-interactive  # Quick start
  django-enterprise myproject --with-docker --with-sre
  django-enterprise myproject --simple-mode      # Basic output

Advanced:
  This tool uses Django's official startproject command as a foundation,
  then enhances it with enterprise features and best practices.
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
            help='Include Docker configuration and multi-stage setup'
        )
        
        parser.add_argument(
            '--with-sre', 
            action='store_true',
            help='Include SRE foundations (monitoring, health checks)'
        )
        
        parser.add_argument(
            '--with-api', 
            action='store_true',
            help='Include API-first architecture (DRF ready)'
        )
        
        parser.add_argument(
            '--with-security', 
            action='store_true',
            help='Include advanced security configurations'
        )
        
        # Configuration options
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
            help='Database backend (postgresql recommended for production)'
        )
        
        # Output options
        parser.add_argument(
            '--simple-mode',
            action='store_true',
            help='Use simple output without rich formatting'
        )
        
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Show detailed output during generation'
        )
        
        return parser.parse_args()
    
    def interactive_setup(self, args: argparse.Namespace) -> Dict:
        """Interactive project configuration with rich prompts"""
        if console and not args.simple_mode:
            console.print("\n[bold blue]🎯 Project Configuration[/bold blue]")
        
        # If questionary is not available or non-interactive mode, use simple input
        if not QUESTIONARY_AVAILABLE or args.non_interactive or args.simple_mode:
            return self._simple_setup(args)
        
        # Project name with validation
        project_name = questionary.text(
            "Project name:",
            validate=lambda text: self.validator.validate_project_name(text),
            default=args.project_name or ""
        ).ask()
        
        if not project_name:
            if args.project_name:
                project_name = args.project_name
            else:
                print("Project name is required!")
                sys.exit(1)
        
        # Database selection
        # Use questionary.Choice objects for compatibility
        database_choices = [
            questionary.Choice(title="PostgreSQL (Recommended for production)", value="postgresql"),
            questionary.Choice(title="MySQL", value="mysql"),
            questionary.Choice(title="SQLite (Development only)", value="sqlite"),
        ]
        default_database_value = args.database if args.database in [c.value for c in database_choices] else database_choices[0].value
        database = questionary.select(
            "Select database:",
            choices=database_choices,
            default=default_database_value
        ).ask()
        
        # Feature selection
        default_features = []
        if args.with_docker:
            default_features.append('docker')
        if args.with_sre:
            default_features.append('sre')
        if args.with_api:
            default_features.append('api')
        if args.with_security:
            default_features.append('security')
        
        features = questionary.checkbox(
            "Select enterprise features:",
            choices=[
                {"name": "Docker & Containerization", "value": "docker", "checked": 'docker' in default_features},
                {"name": "SRE Foundations (Monitoring, Health Checks)", "value": "sre", "checked": 'sre' in default_features},
                {"name": "API-First Architecture (DRF ready)", "value": "api", "checked": 'api' in default_features},
                {"name": "Advanced Security Configurations", "value": "security", "checked": 'security' in default_features}
            ]
        ).ask()
        
        # Python version
        python_version = questionary.select(
            "Python version:",
            choices=["3.10", "3.11", "3.12"],
            default=args.python_version
        ).ask()
        
        return {
            'project_name': project_name,
            'database': database,
            'features': features or [],
            'python_version': python_version,
            'output_dir': args.output_dir,
            'verbose': args.verbose,
            'simple_mode': args.simple_mode
        }
    
    def _simple_setup(self, args: argparse.Namespace) -> Dict:
        """Simple setup without rich dependencies"""
        if args.project_name:
            project_name = args.project_name
        else:
            project_name = input("Project name: ").strip()
            
        if not self.validator.validate_project_name(project_name):
            print("Invalid project name! Use only letters, numbers, and underscores. Start with a letter.")
            sys.exit(1)
        
        print("Database options:")
        print("1. PostgreSQL (Recommended for production)")
        print("2. MySQL") 
        print("3. SQLite (Development only)")
        db_choice = input(f"Select database [1-3, default: {args.database}]: ").strip() or args.database
        
        database_map = {"1": "postgresql", "2": "mysql", "3": "sqlite", "postgresql": "postgresql", "mysql": "mysql", "sqlite": "sqlite"}
        database = database_map.get(db_choice, args.database)
        
        features = []
        if args.with_docker or input("Include Docker? (y/n) [n]: ").lower().strip() in ('y', 'yes'):
            features.append('docker')
        if args.with_sre or input("Include SRE foundations? (y/n) [n]: ").lower().strip() in ('y', 'yes'):
            features.append('sre')
        if args.with_api or input("Include API-first architecture? (y/n) [n]: ").lower().strip() in ('y', 'yes'):
            features.append('api')
        if args.with_security or input("Include advanced security? (y/n) [n]: ").lower().strip() in ('y', 'yes'):
            features.append('security')
        
        return {
            'project_name': project_name,
            'database': database,
            'features': features,
            'python_version': args.python_version,
            'output_dir': args.output_dir,
            'verbose': args.verbose,
            'simple_mode': True  # Force simple mode in non-interactive
        }
    
    def generate_project(self, config: Dict):
        """Generate project with appropriate progress tracking"""
        if console and not config.get('simple_mode'):
            self._generate_with_progress(config)
        else:
            self._generate_simple(config)
    
    def _generate_with_progress(self, config: Dict):
        """Generate with rich progress bars"""
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                console=console
            ) as progress:
                
                # Main generation tasks
                main_task = progress.add_task("[cyan]Generating enterprise Django project...", total=400)
                
                # Step 1: Create Django base project using startproject
                progress.update(main_task, advance=50, description="[green]Creating Django base project...")
                self.generator.create_django_project(config)
                
                # Step 2: Convert to modular settings
                progress.update(main_task, advance=100, description="[yellow]Converting to modular settings...")
                project_path = Path(config['output_dir']) / config['project_name']
                self.generator._convert_to_modular_settings(project_path, config)
                
                # Step 3: Create enterprise structure
                progress.update(main_task, advance=50, description="[magenta]Creating enterprise structure...")
                self.generator._create_enterprise_structure(project_path, config)
                
                # Step 4: Enhance settings with enterprise features
                progress.update(main_task, advance=50, description="[blue]Adding enterprise features...")
                self.generator._enhance_settings_with_enterprise_features(project_path, config)
                
                # Step 5: Setup development environment
                progress.update(main_task, advance=75, description="[cyan]Setting up development tools...")
                self.generator._setup_development_environment(project_path, config)
                
                # Step 6: Add enterprise configurations
                progress.update(main_task, advance=75, description="[green]Finalizing configurations...")
                self.generator._add_enterprise_configurations(project_path, config)
                
                progress.update(main_task, advance=100, description="[bold green]Project generation completed!")
                    
        except Exception as e:
            if console:
                console.print(f"[red]❌ Project generation failed: {e}[/red]")
            else:
                print(f"❌ Project generation failed: {e}")
            sys.exit(1)
    
    def _generate_simple(self, config: Dict):
        """Simple generation without rich but with detailed output"""
        try:
            if config.get('verbose'):
                print("\n" + "="*60)
                print("ENTERPRISE DJANGO PROJECT GENERATION")
                print("="*60)
            
            steps = [
                ("Creating Django base project...", lambda: self.generator.create_django_project(config)),
                ("Converting to modular settings...", lambda: self.generator._convert_to_modular_settings(
                    Path(config['output_dir']) / config['project_name'], config
                )),
                ("Creating enterprise structure...", lambda: self.generator._create_enterprise_structure(
                    Path(config['output_dir']) / config['project_name'], config
                )),
                ("Adding enterprise features...", lambda: self.generator._enhance_settings_with_enterprise_features(
                    Path(config['output_dir']) / config['project_name'], config
                )),
                ("Setting up development tools...", lambda: self.generator._setup_development_environment(
                    Path(config['output_dir']) / config['project_name'], config
                )),
                ("Finalizing configurations...", lambda: self.generator._add_enterprise_configurations(
                    Path(config['output_dir']) / config['project_name'], config
                )),
            ]
            
            for description, step_function in steps:
                if config.get('verbose'):
                    print(f"🔧 {description}")
                else:
                    print(f"⏳ {description.split('...')[0]}...", end="", flush=True)
                
                step_function()
                
                if not config.get('verbose'):
                    print(" ✅")
            
            if config.get('verbose'):
                print("="*60)
                print("✅ Project generation completed successfully!")
            else:
                print("🎉 Project generation completed!")
                
        except Exception as e:
            print(f"❌ Project generation failed: {e}")
            if config.get('verbose'):
                import traceback
                traceback.print_exc()
            sys.exit(1)
    
    def run(self):
        """Main CLI entry point"""
        try:
            self.display_banner()
            args = self.parse_arguments()
            
            # Set simple mode if rich is not available
            if not RICH_AVAILABLE:
                args.simple_mode = True
            
            # Validate project name requirement
            if args.non_interactive and not args.project_name:
                error_msg = "Error: Project name required in non-interactive mode"
                if console and not args.simple_mode:
                    console.print(f"[red]{error_msg}[/red]")
                else:
                    print(error_msg)
                sys.exit(1)
            
            # Get configuration
            config = self.interactive_setup(args)
            
            # Display configuration summary
            self._display_configuration_summary(config)
            
            # Confirm generation
            if not self._confirm_generation(args, config):
                return
            
            # Generate project
            self.generate_project(config)
            
            # Show success message
            self.show_success_message(config)
            
        except KeyboardInterrupt:
            cancel_msg = "Operation cancelled by user"
            if console and not args.simple_mode:
                console.print(f"\n[yellow]{cancel_msg}[/yellow]")
            else:
                print(f"\n{cancel_msg}")
        except Exception as e:
            error_msg = f"Error: {e}"
            if console and not args.simple_mode:
                console.print(f"[red]{error_msg}[/red]")
            else:
                print(error_msg)
            sys.exit(1)
    
    def _display_configuration_summary(self, config: Dict):
        """Display configuration summary before generation"""
        if console and not config.get('simple_mode'):
            console.print(f"\n[bold green]🚀 Configuration Summary[/bold green]")
            console.print(f"📁 Project: [cyan]{config['project_name']}[/cyan]")
            console.print(f"📊 Database: [cyan]{config['database']}[/cyan]")
            console.print(f"🐍 Python: [cyan]{config['python_version']}[/cyan]")
            console.print(f"📂 Output: [cyan]{config['output_dir']}[/cyan]")
            
            if config['features']:
                console.print(f"✨ Features: [cyan]{', '.join(config['features'])}[/cyan]")
            else:
                console.print(f"✨ Features: [yellow]Standard Django project[/yellow]")
                
            console.print(f"\n[bold]Approach:[/bold]")
            console.print("1. 🏗️  Create base project using Django's startproject")
            console.print("2. ⚡ Enhance with enterprise features and best practices")
            console.print("3. 🔧 Configure development environment and tools")
            
        else:
            print(f"\n🚀 Configuration Summary")
            print(f"Project: {config['project_name']}")
            print(f"Database: {config['database']}")
            print(f"Python: {config['python_version']}")
            print(f"Output: {config['output_dir']}")
            print(f"Features: {', '.join(config['features']) if config['features'] else 'Standard Django project'}")
            print(f"\nApproach: Django startproject + Enterprise enhancements")
    
    def _confirm_generation(self, args: argparse.Namespace, config: Dict) -> bool:
        """Confirm project generation with user"""
        if args.non_interactive:
            return True
            
        if QUESTIONARY_AVAILABLE and not args.simple_mode:
            confirm = questionary.confirm(
                "Proceed with project generation?",
                default=True
            ).ask()
            return confirm
        else:
            response = input("\nProceed with project generation? (Y/n) ").lower().strip()
            return response in ('', 'y', 'yes')
    
    def show_success_message(self, config: Dict):
        """Display success message with next steps"""
        project_path = Path(config['output_dir']) / config['project_name']
        manage_py_path = project_path / 'manage.py'
        
        if console and not config.get('simple_mode'):
            success_panel = Panel.fit(
                f"""
🎉 [bold green]Enterprise Django Project Generated Successfully![/bold green]

📁 [bold]Project Location:[/bold] [cyan]{project_path}[/cyan]

🚀 [bold]Next Steps:[/bold]

1. [yellow]Navigate to project directory[/yellow]
   cd {project_path}

2. [yellow]Set up virtual environment[/yellow]
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate    # Windows

3. [yellow]Install development dependencies[/yellow]
   pip install -r requirements/dev.txt

4. [yellow]Configure environment variables[/yellow]
   cp .env.example .env
   # Edit .env with your settings

5. [yellow]Run initial database setup[/yellow]
   python manage.py migrate

6. [yellow]Create superuser (optional)[/yellow]
   python manage.py createsuperuser

7. [yellow]Start development server[/yellow]
   python manage.py runserver

🔧 [bold]What was generated:[/bold]
• ✅ Django project using official startproject
• ✅ Modular settings architecture  
• ✅ { 'Enterprise security configurations' if 'security' in config['features'] else 'Standard security settings'}
• ✅ Development tools and pre-commit hooks
• ✅ {'Docker configuration' if 'docker' in config['features'] else ''}
• ✅ {'SRE monitoring foundation' if 'sre' in config['features'] else ''}

📚 [bold]Documentation:[/bold] 
   See [cyan]README.md[/cyan] for detailed instructions

💡 [bold]Tip:[/bold] Your project is ready to run immediately!
   {f"Try: [yellow]cd {project_path} && python manage.py runserver[/yellow]" if manage_py_path.exists() else ""}
                """.strip(),
                title="Project Ready! 🚀",
                border_style="green",
                padding=(1, 2)
            )
            console.print(success_panel)
        else:
            print(f"""
🎉 Enterprise Django Project Generated Successfully!

📁 Project Location: {project_path}

🚀 Next Steps:

1. cd {project_path}
2. python -m venv venv
3. source venv/bin/activate (Linux/Mac) OR venv\\Scripts\\activate (Windows)
4. pip install -r requirements/dev.txt
5. cp .env.example .env
6. python manage.py migrate
7. python manage.py runserver

📚 See README.md for detailed instructions

💡 Your project is ready to run immediately!
            """.strip())


def main():
    """Main entry point"""
    cli = EnterpriseCLI()
    cli.run()


if __name__ == "__main__":
    main()