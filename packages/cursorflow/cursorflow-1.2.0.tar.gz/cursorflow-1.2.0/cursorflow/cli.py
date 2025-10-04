"""
Command Line Interface for Cursor Testing Agent

Universal CLI that works with any web framework.
Provides simple commands for testing components across different architectures.
"""

import click
import asyncio
import json
import os
from pathlib import Path
from typing import Dict
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

from .core.agent import TestAgent

console = Console()

@click.group()
@click.version_option(version="1.0.0")
def main():
    """Universal UI testing framework for any web technology"""
    pass

@main.command()
@click.argument('test_name', required=False, default='ui-test')
@click.option('--base-url', '-u', default='http://localhost:3000',
              help='Base URL for testing')
@click.option('--actions', '-a',
              help='JSON file with test actions, or inline JSON string')
@click.option('--logs', '-l', 
              type=click.Choice(['local', 'ssh', 'docker', 'systemd']),
              default='local',
              help='Log source type')
@click.option('--config', '-c', type=click.Path(exists=True),
              help='Configuration file path')
@click.option('--verbose', '-v', is_flag=True,
              help='Verbose output')
def test(test_name, base_url, actions, logs, config, verbose):
    """Test UI flows and interactions with real-time log monitoring"""
    
    if verbose:
        import logging
        logging.basicConfig(level=logging.INFO)
    
    # Parse actions
    test_actions = []
    if actions:
        try:
            # Check if it's a file path
            if actions.endswith('.json') and Path(actions).exists():
                with open(actions, 'r') as f:
                    test_actions = json.load(f)
                console.print(f"📋 Loaded actions from [cyan]{actions}[/cyan]")
            else:
                # Try to parse as inline JSON
                test_actions = json.loads(actions)
                console.print(f"📋 Using inline actions")
        except json.JSONDecodeError as e:
            console.print(f"[red]❌ Invalid JSON in actions: {e}[/red]")
            return
        except Exception as e:
            console.print(f"[red]❌ Failed to load actions: {e}[/red]")
            return
    else:
        # Default actions - just navigate and screenshot
        test_actions = [
            {"navigate": "/"},
            {"wait_for": "body"},
            {"screenshot": "baseline"}
        ]
        console.print(f"📋 Using default actions (navigate + screenshot)")
    
    # Load configuration
    agent_config = {}
    if config:
        with open(config, 'r') as f:
            agent_config = json.load(f)
    
    console.print(f"🎯 Testing [bold]{test_name}[/bold] at [blue]{base_url}[/blue]")
    
    # Initialize CursorFlow (framework-agnostic)
    try:
        from .core.cursorflow import CursorFlow
        flow = CursorFlow(
            base_url=base_url,
            log_config={'source': logs, 'paths': ['logs/app.log']},
            **agent_config
        )
    except Exception as e:
        console.print(f"[red]Error initializing CursorFlow: {e}[/red]")
        return
    
    # Execute test actions
    try:
        console.print(f"🚀 Executing {len(test_actions)} actions...")
        results = asyncio.run(flow.execute_and_collect(test_actions))
        
        console.print(f"✅ Test completed: {test_name}")
        console.print(f"📊 Browser events: {len(results.get('browser_events', []))}")
        console.print(f"📋 Server logs: {len(results.get('server_logs', []))}")
        console.print(f"📸 Screenshots: {len(results.get('artifacts', {}).get('screenshots', []))}")
        
        # Show correlations if found
        timeline = results.get('organized_timeline', [])
        if timeline:
            console.print(f"⏰ Timeline events: {len(timeline)}")
        
        # Save results to file for Cursor analysis
        output_file = f"{test_name.replace(' ', '_')}_test_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        console.print(f"💾 Full results saved to: [cyan]{output_file}[/cyan]")
        console.print(f"📁 Artifacts stored in: [cyan].cursorflow/artifacts/[/cyan]")
        
    except Exception as e:
        console.print(f"[red]❌ Test failed: {e}[/red]")
        if verbose:
            import traceback
            console.print(traceback.format_exc())
        raise

@main.command()
@click.option('--project-path', '-p', default='.',
              help='Project directory path')
@click.option('--environment', '-e', 
              type=click.Choice(['local', 'staging', 'production']),
              default='local',
              help='Target environment')
def auto_test(project_path, environment):
    """Auto-detect framework and run appropriate tests"""
    
    console.print("🔍 Auto-detecting project framework...")
    
    framework = TestAgent.detect_framework(project_path)
    console.print(f"Detected framework: [bold]{framework}[/bold]")
    
    # Load project configuration
    config_path = Path(project_path) / 'cursor-test-config.json'
    if config_path.exists():
        with open(config_path, 'r') as f:
            project_config = json.load(f)
    else:
        console.print("[yellow]No cursor-test-config.json found, using defaults[/yellow]")
        project_config = {}
    
    # Get environment config
    env_config = project_config.get('environments', {}).get(environment, {})
    base_url = env_config.get('base_url', 'http://localhost:3000')
    
    console.print(f"Testing [cyan]{environment}[/cyan] environment at [blue]{base_url}[/blue]")
    
    # Auto-detect components and run smoke tests
    asyncio.run(_run_auto_tests(framework, base_url, env_config))

async def _run_auto_tests(framework: str, base_url: str, config: Dict):
    """Run automatic tests based on detected framework"""
    
    try:
        agent = TestAgent(framework, base_url, **config)
        
        # Get available components
        components = agent.adapter.get_available_components()
        
        console.print(f"Found {len(components)} testable components")
        
        # Run smoke tests for all components
        results = await agent.run_smoke_tests(components)
        
        # Display summary
        display_smoke_test_summary(results)
        
    except Exception as e:
        console.print(f"[red]Auto-test failed: {e}[/red]")

@main.command()
@click.argument('project_path', default='.')
@click.option('--framework', '-f')
def install_rules(project_path, framework):
    """Install CursorFlow rules and configuration in a project"""
    
    console.print("🚀 Installing CursorFlow rules and configuration...")
    
    try:
        # Import and run the installation
        from .install_cursorflow_rules import install_cursorflow_rules
        success = install_cursorflow_rules(project_path)
        
        if success:
            console.print("[green]✅ CursorFlow rules installed successfully![/green]")
            console.print("\nNext steps:")
            console.print("1. Review cursorflow-config.json")
            console.print("2. Install dependencies: pip install cursorflow && playwright install chromium")
            console.print("3. Start testing: Use CursorFlow in Cursor!")
        else:
            console.print("[red]❌ Installation failed[/red]")
            
    except Exception as e:
        console.print(f"[red]Installation error: {e}[/red]")

@main.command()
@click.option('--force', is_flag=True, help='Force update even if no updates available')
@click.option('--project-dir', default='.', help='Project directory')
def update(force, project_dir):
    """Update CursorFlow package and rules"""
    
    console.print("🔄 Updating CursorFlow...")
    
    try:
        from .updater import update_cursorflow
        import asyncio
        
        success = asyncio.run(update_cursorflow(project_dir, force=force))
        
        if success:
            console.print("[green]✅ CursorFlow updated successfully![/green]")
        else:
            console.print("[red]❌ Update failed[/red]")
            
    except Exception as e:
        console.print(f"[red]Update error: {e}[/red]")

@main.command()
@click.option('--project-dir', default='.', help='Project directory')
def check_updates(project_dir):
    """Check for available updates"""
    
    try:
        from .updater import check_updates
        import asyncio
        
        result = asyncio.run(check_updates(project_dir))
        
        if "error" in result:
            console.print(f"[red]Error checking updates: {result['error']}[/red]")
            return
        
        # Display update information
        table = Table(title="CursorFlow Update Status")
        table.add_column("Component", style="cyan")
        table.add_column("Current", style="yellow")
        table.add_column("Latest", style="green")
        table.add_column("Status", style="bold")
        
        # Package status
        pkg_status = "🔄 Update Available" if result.get("version_update_available") else "✅ Current"
        table.add_row(
            "Package",
            result.get("current_version", "unknown"),
            result.get("latest_version", "unknown"),
            pkg_status
        )
        
        # Rules status
        rules_status = "🔄 Update Available" if result.get("rules_update_available") else "✅ Current"
        table.add_row(
            "Rules",
            result.get("current_rules_version", "unknown"),
            result.get("latest_rules_version", "unknown"),
            rules_status
        )
        
        # Dependencies status
        deps_status = "✅ Current" if result.get("dependencies_current") else "⚠️  Needs Update"
        table.add_row("Dependencies", "-", "-", deps_status)
        
        console.print(table)
        
        # Show update commands if needed
        if result.get("version_update_available") or result.get("rules_update_available"):
            console.print("\n💡 Run [bold]cursorflow update[/bold] to install updates")
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.option('--project-dir', default='.', help='Project directory')
def install_deps(project_dir):
    """Install or update CursorFlow dependencies"""
    
    console.print("🔧 Installing CursorFlow dependencies...")
    
    try:
        from .updater import install_dependencies
        import asyncio
        
        success = asyncio.run(install_dependencies(project_dir))
        
        if success:
            console.print("[green]✅ Dependencies installed successfully![/green]")
        else:
            console.print("[red]❌ Dependency installation failed[/red]")
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
@click.argument('project_path')
# Framework detection removed - CursorFlow is framework-agnostic
def init(project_path):
    """Initialize cursor testing for a project"""
    
    project_dir = Path(project_path)
    
    # Create configuration file (framework-agnostic)
    config_template = {
        'environments': {
            'local': {
                'base_url': 'http://localhost:3000',
                'logs': 'local',
                'log_paths': {
                    'app': 'logs/app.log'
                }
            },
            'staging': {
                'base_url': 'https://staging.example.com',
                'logs': 'ssh',
                'ssh_config': {
                    'hostname': 'staging-server',
                    'username': 'deploy'
                },
                'log_paths': {
                    'app_error': '/var/log/app/error.log'
                }
            }
        }
    }
    
    # Universal configuration works for any web application
    
    # Save configuration
    config_path = project_dir / 'cursor-test-config.json'
    with open(config_path, 'w') as f:
        json.dump(config_template, f, indent=2)
    
    console.print(f"[green]Initialized cursor testing for project[/green]")
    console.print(f"Configuration saved to: {config_path}")
    console.print("\nNext steps:")
    console.print("1. Edit cursor-test-config.json with your specific settings")
    console.print("2. Run: cursor-test auto-test")

def display_test_results(results: Dict):
    """Display test results in rich format"""
    
    # Summary table
    table = Table(title="Test Results Summary")
    table.add_column("Component", style="cyan")
    table.add_column("Framework", style="magenta")
    table.add_column("Success", style="green")
    table.add_column("Errors", style="red")
    table.add_column("Warnings", style="yellow")
    
    summary = results.get('correlations', {}).get('summary', {})
    
    table.add_row(
        results.get('component', 'unknown'),
        results.get('framework', 'unknown'),
        "✅" if results.get('success', False) else "❌",
        str(summary.get('error_count', 0)),
        str(summary.get('warning_count', 0))
    )
    
    console.print(table)
    
    # Critical issues
    critical_issues = results.get('correlations', {}).get('critical_issues', [])
    if critical_issues:
        console.print(f"\n[red bold]🚨 {len(critical_issues)} Critical Issues Found:[/red bold]")
        for i, issue in enumerate(critical_issues[:3], 1):
            browser_event = issue['browser_event']
            server_logs = issue['server_logs']
            console.print(f"  {i}. {browser_event.get('action', 'Unknown action')} → {len(server_logs)} server errors")
    
    # Recommendations
    recommendations = results.get('correlations', {}).get('recommendations', [])
    if recommendations:
        console.print(f"\n[blue bold]💡 Recommendations:[/blue bold]")
        for rec in recommendations[:3]:
            console.print(f"  • {rec.get('title', 'Unknown recommendation')}")

def display_smoke_test_summary(results: Dict):
    """Display smoke test results for multiple components"""
    
    table = Table(title="Smoke Test Results")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="bold")
    table.add_column("Errors", style="red")
    table.add_column("Duration", style="blue")
    
    for component_name, result in results.items():
        if result.get('success', False):
            status = "[green]✅ PASS[/green]"
        else:
            status = "[red]❌ FAIL[/red]"
            
        error_count = len(result.get('correlations', {}).get('critical_issues', []))
        duration = f"{result.get('duration', 0):.1f}s"
        
        table.add_row(component_name, status, str(error_count), duration)
    
    console.print(table)

if __name__ == '__main__':
    main()
