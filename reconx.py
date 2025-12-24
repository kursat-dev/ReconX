import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

from modules.subdomains import enumerate_subdomains
from modules.ports import scan_ports
from modules.tech import detect_tech
from utils.reporter import save_report

console = Console()

def main():
    parser = argparse.ArgumentParser(description="ReconX - Automated Web Reconnaissance Tool")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    parser.add_argument("-o", "--output", help="Output JSON file", default="report.json")
    args = parser.parse_args()

    target = args.domain
    results = {"target": target}

    console.print(Panel(f"[bold green]ReconX[/bold green] - Scanning [bold cyan]{target}[/bold cyan]", expand=False))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        
        # 1. Subdomain Enumeration
        task1 = progress.add_task(description="Enumerating subdomains...", total=None)
        subdomains = enumerate_subdomains(target)
        results["subdomains"] = subdomains
        progress.update(task1, completed=100)
        console.print(f"[+] Found {len(subdomains)} subdomains")

        # 2. Port Scanning
        task2 = progress.add_task(description="Scanning ports (Top Common)...", total=None)
        open_ports = scan_ports(target)
        results["open_ports"] = open_ports
        progress.update(task2, completed=100)
        console.print(f"[+] Open Ports: {', '.join(map(str, open_ports)) if open_ports else 'None found'}")

        # 3. Tech Stack Detection
        task3 = progress.add_task(description="Detecting tech stack...", total=None)
        tech_stack = detect_tech(target)
        results["tech_stack"] = tech_stack
        progress.update(task3, completed=100)
        console.print("[+] Tech Stack detected")
        
    # Display Tech Stack Table
    if tech_stack:
        table = Table(title="Technology Stack")
        table.add_column("Component", style="cyan")
        table.add_column("Value", style="magenta")
        for key, value in tech_stack.items():
            table.add_row(key, value)
        console.print(table)

    # Save Report
    save_report(results, args.output)
    console.print(f"[bold green]Done![/bold green] Report saved to [bold]{args.output}[/bold]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Scan interrupted by user.[/red]")
        sys.exit(0)
