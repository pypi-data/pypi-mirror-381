"""Main CLI entry point for VulnGuard"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table
from rich.panel import Panel
from rich import box

from vulnguard import SecurityScanner
from vulnguard.models.issue import Severity

console = Console()


@click.group()
@click.version_option(version="0.0.2", prog_name="vulnguard")
def cli():
    """
    🛡️ VulnGuard - AI-Powered Code Security Scanner
    
    Detect security vulnerabilities in your code using Claude AI.
    """
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--api-key', envvar='CLAUDE_API_KEY', help='Claude API key')
@click.option('--model', '-m', default='claude-3-5-sonnet-20241022', 
              help='Claude model to use (e.g., claude-3-5-sonnet-20241022, claude-3-5-haiku-20241022)')
@click.option('--output', '-o', type=click.Path(), help='Output file path')
@click.option('--format', '-f', type=click.Choice(['json', 'text', 'table']), default='table', help='Output format')
@click.option('--severity', '-s', type=click.Choice(['critical', 'high', 'medium', 'low']), 
              help='Minimum severity to report')
@click.option('--no-save', is_flag=True, help='Do not save results to .vulnguard/')
@click.option('--quiet', '-q', is_flag=True, help='Minimal output')
def scan(path: str, api_key: Optional[str], model: str, output: Optional[str], format: str, 
         severity: Optional[str], no_save: bool, quiet: bool):
    """
    Scan a repository for security vulnerabilities.
    
    Examples:
    
        vulnguard scan .
        
        vulnguard scan /path/to/project --severity high
        
        vulnguard scan . --format json --output results.json
        
        vulnguard scan . --model claude-3-5-haiku-20241022  # Use faster/cheaper model
    """
    try:
        # Show banner unless quiet
        if not quiet:
            console.print(Panel.fit(
                "[bold cyan]🛡️  VulnGuard Security Scanner[/bold cyan]\n"
                "[dim]AI-Powered Vulnerability Detection[/dim]",
                border_style="cyan"
            ))
        
        # Run scan
        result = asyncio.run(_run_scan(path, api_key, model, not no_save, quiet))
        
        # Filter by severity if specified
        if severity:
            min_severity = Severity(severity)
            severity_order = ['info', 'low', 'medium', 'high', 'critical']
            min_index = severity_order.index(min_severity.value)
            result.issues = [
                issue for issue in result.issues 
                if severity_order.index(issue.severity.value) >= min_index
            ]
        
        # Output results
        if format == 'json':
            import json
            output_data = result.to_dict()
            if output:
                Path(output).write_text(json.dumps(output_data, indent=2))
                console.print(f"\n✅ Results saved to: {output}")
            else:
                console.print_json(data=output_data)
        
        elif format == 'table':
            _display_table_results(result, quiet)
        
        else:  # text
            _display_text_results(result)
        
        # Exit code based on findings
        if result.critical_count > 0:
            sys.exit(2)  # Critical issues found
        elif result.high_count > 0:
            sys.exit(1)  # High severity issues found
        else:
            sys.exit(0)  # Success
    
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Scan cancelled by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {e}", style="red")
        if not quiet:
            console.print("\n[dim]Run with --help for usage information[/dim]")
        sys.exit(1)


async def _run_scan(path: str, api_key: Optional[str], model: str, save_results: bool, quiet: bool):
    """Run the actual scan with progress indicator"""
    
    scanner = SecurityScanner(api_key=api_key, model=model)
    repo_path = Path(path).absolute()
    
    if not quiet:
        console.print(f"\n📁 Target: [cyan]{repo_path}[/cyan]")
        console.print()
    
    # Progress indicator
    if not quiet:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("[cyan]Analyzing code for vulnerabilities...", total=None)
            result = await scanner.scan(str(repo_path), save_results=save_results)
            progress.update(task, completed=True)
    else:
        result = await scanner.scan(str(repo_path), save_results=save_results)
    
    return result


def _display_table_results(result, quiet: bool):
    """Display results in a rich table format"""
    
    if not quiet:
        console.print()
        console.print("=" * 80)
        console.print("[bold]📊 Scan Results[/bold]")
        console.print("=" * 80)
    
    # Summary stats
    stats_table = Table(show_header=False, box=box.SIMPLE)
    stats_table.add_row("📁 Files scanned:", f"[cyan]{result.files_scanned}[/cyan]")
    stats_table.add_row("⏱️  Scan time:", f"[cyan]{result.scan_time_seconds}s[/cyan]")
    stats_table.add_row("🐛 Issues found:", f"[bold]{len(result.issues)}[/bold]")
    
    if result.issues:
        stats_table.add_row("   🔴 Critical:", f"[bold red]{result.critical_count}[/bold red]")
        stats_table.add_row("   🟠 High:", f"[bold yellow]{result.high_count}[/bold yellow]")
        stats_table.add_row("   🟡 Medium:", f"[bold]{result.medium_count}[/bold]")
        stats_table.add_row("   🟢 Low:", f"[dim]{result.low_count}[/dim]")
    
    console.print(stats_table)
    console.print()
    
    if result.issues:
        # Issues table
        issues_table = Table(
            title="🔍 Detected Vulnerabilities",
            box=box.ROUNDED,
            show_lines=True
        )
        issues_table.add_column("#", style="dim", width=3)
        issues_table.add_column("Severity", width=10)
        issues_table.add_column("Issue", style="bold")
        issues_table.add_column("Location", style="cyan")
        
        for idx, issue in enumerate(result.issues[:20], 1):
            # Color code severity
            severity_colors = {
                'critical': 'bold red',
                'high': 'bold yellow',
                'medium': 'yellow',
                'low': 'dim'
            }
            severity_style = severity_colors.get(issue.severity.value, 'white')
            
            issues_table.add_row(
                str(idx),
                f"[{severity_style}]{issue.severity.value.upper()}[/{severity_style}]",
                issue.title[:50],
                f"{issue.file_path}:{issue.line_number}"
            )
        
        console.print(issues_table)
        
        if len(result.issues) > 20:
            console.print(f"\n[dim]... and {len(result.issues) - 20} more issues[/dim]")
        
        console.print(f"\n💾 Full report: [cyan].vulnguard/scan_results.json[/cyan]")
    else:
        console.print("[bold green]✅ No security issues found![/bold green]")
    
    console.print()


def _display_text_results(result):
    """Display results in plain text format"""
    console.print(f"\nFiles scanned: {result.files_scanned}")
    console.print(f"Scan time: {result.scan_time_seconds}s")
    console.print(f"Issues found: {len(result.issues)}")
    
    if result.issues:
        console.print(f"  Critical: {result.critical_count}")
        console.print(f"  High: {result.high_count}")
        console.print(f"  Medium: {result.medium_count}")
        console.print(f"  Low: {result.low_count}")
        console.print()
        
        for idx, issue in enumerate(result.issues, 1):
            console.print(f"\n{idx}. [{issue.severity.value.upper()}] {issue.title}")
            console.print(f"   File: {issue.file_path}:{issue.line_number}")
            console.print(f"   {issue.description[:150]}...")


@cli.command()
@click.argument('report_path', type=click.Path(exists=True), 
                default='.vulnguard/scan_results.json')
def report(report_path: str):
    """
    Display a previously saved scan report.
    
    Examples:
    
        vulnguard report
        
        vulnguard report .vulnguard/scan_results.json
    """
    from vulnguard.reporters.json_reporter import JSONReporter
    
    try:
        console.print(f"\n📄 Loading report: [cyan]{report_path}[/cyan]\n")
        
        data = JSONReporter.load(report_path)
        
        # Create a mock result object for display
        from vulnguard.models.result import ScanResult
        from vulnguard.models.issue import SecurityIssue, Severity
        
        issues = [
            SecurityIssue(
                id=item['id'],
                severity=Severity(item['severity']),
                title=item['title'],
                description=item['description'],
                file_path=item['file_path'],
                line_number=item['line_number'],
                code_snippet=item.get('code_snippet', ''),
                recommendation=item.get('recommendation'),
                cwe_id=item.get('cwe_id')
            )
            for item in data.get('issues', [])
        ]
        
        result = ScanResult(
            repository_path=data['repository_path'],
            issues=issues,
            files_scanned=data['files_scanned'],
            scan_time_seconds=data['scan_time_seconds']
        )
        
        _display_table_results(result, quiet=False)
        
    except FileNotFoundError:
        console.print(f"[bold red]❌ Report not found:[/bold red] {report_path}")
        console.print("\n[dim]Run 'vulnguard scan' first to generate a report[/dim]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]❌ Error loading report:[/bold red] {e}")
        sys.exit(1)


@cli.command()
def init():
    """
    Initialize VulnGuard configuration in current directory.
    
    Creates a .vulnguard.yaml configuration file.
    """
    config_path = Path.cwd() / ".vulnguard.yaml"
    
    if config_path.exists():
        console.print(f"[yellow]⚠️  Configuration already exists:[/yellow] {config_path}")
        if not click.confirm("Overwrite?"):
            sys.exit(0)
    
    config_template = """# VulnGuard Configuration File

# Scan settings
scan:
  # File limit per scan (cost control)
  max_files: 20
  
  # File patterns to include
  include:
    - "**/*.py"
  
  # File patterns to exclude
  exclude:
    - "**/venv/**"
    - "**/__pycache__/**"
    - "**/node_modules/**"
    - "**/.git/**"
    - "**/tests/**"

# Severity threshold (critical, high, medium, low)
severity_threshold: medium

# Output settings
output:
  format: table  # json, table, text
  save_to_file: true
  output_dir: .vulnguard

# API settings
api:
  # Leave empty to use CLAUDE_API_KEY environment variable
  # api_key: "sk-ant-..."
  model: claude-3-5-sonnet-20241022
"""
    
    config_path.write_text(config_template)
    console.print(f"\n✅ Created configuration: [cyan]{config_path}[/cyan]")
    console.print("\n[dim]Edit this file to customize your scan settings[/dim]\n")


if __name__ == '__main__':
    cli()
