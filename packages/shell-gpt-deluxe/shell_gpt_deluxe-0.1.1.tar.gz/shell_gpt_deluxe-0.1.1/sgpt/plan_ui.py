"""
UI components for Plan-Execute mode.
Provides rich terminal formatting for plans, steps, and progress.
"""

from pathlib import Path
from typing import List

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table

from .cost_estimator import calculate_cost, format_cost
from .plan import Plan, Step, StepStatus, StepType


console = Console()


def display_plan_overview(plan: Plan, show_costs: bool = True) -> None:
    """
    Display a beautiful overview of the execution plan.

    Args:
        plan: The plan to display
        show_costs: Whether to show cost estimates
    """
    # Create table for steps
    table = Table(title="Execution Plan", show_header=True, header_style="bold cyan")
    table.add_column("#", style="dim", width=4)
    table.add_column("Status", width=8)
    table.add_column("Description", style="white")
    table.add_column("Type", style="yellow", width=12)

    if show_costs:
        table.add_column("Est. Cost", style="magenta", width=10)

    for i, step in enumerate(plan.steps, 1):
        status_symbol = {
            StepStatus.PENDING: "○",
            StepStatus.IN_PROGRESS: "●",
            StepStatus.COMPLETED: "✓",
            StepStatus.FAILED: "✗",
            StepStatus.SKIPPED: "⊘",
        }
        symbol = status_symbol.get(step.status, "○")

        status_color = {
            StepStatus.PENDING: "white",
            StepStatus.IN_PROGRESS: "yellow",
            StepStatus.COMPLETED: "green",
            StepStatus.FAILED: "red",
            StepStatus.SKIPPED: "dim",
        }
        color = status_color.get(step.status, "white")

        row = [
            str(i),
            f"[{color}]{symbol}[/{color}]",
            step.description,
            step.step_type.value,
        ]

        if show_costs:
            cost = calculate_cost(step.estimated_tokens, plan.model)
            row.append(format_cost(cost))

        table.add_row(*row)

    console.print()
    console.print(table)

    # Display summary
    if show_costs:
        console.print()
        console.print(
            f"[bold]Total Estimated Cost:[/bold] [magenta]{format_cost(plan.total_estimated_cost)}[/magenta] "
            f"([dim]{plan.total_estimated_tokens} tokens[/dim])"
        )
    console.print()


def display_step_detail(
    step: Step, step_number: int, total_steps: int, show_cost: bool = True
) -> None:
    """
    Display detailed information about a step.

    Args:
        step: The step to display
        step_number: Current step number
        total_steps: Total number of steps
        show_cost: Whether to show cost estimate
    """
    console.print()
    console.print("─" * 60)

    # Step header
    header_text = f"Step {step_number}/{total_steps}: {step.description}"
    console.print(f"[bold cyan]{header_text}[/bold cyan]")
    console.print("─" * 60)

    # Step details
    console.print(f"[yellow]Type:[/yellow] {step.step_type.value}")

    # Enhanced file status for CODE steps
    if step.step_type.value == "code" and step.output_file:
        file_exists = Path(step.output_file).exists()

        if file_exists:
            # File will be modified
            file_size = Path(step.output_file).stat().st_size
            size_str = f"{file_size} B" if file_size < 1024 else f"{file_size/1024:.1f} KB"
            console.print(f"[yellow]Action:[/yellow] [yellow]MODIFY[/yellow] existing file ⚠️")
            console.print(f"[yellow]Output file:[/yellow] {step.output_file} [dim](exists, {size_str})[/dim]")

            # Show a preview of changes
            try:
                old_content = Path(step.output_file).read_text(encoding='utf-8')
                new_content = step.command

                # Count changes
                old_lines = old_content.split('\n')
                new_lines = new_content.split('\n')

                # Simple diff count
                if len(new_lines) > len(old_lines):
                    diff = len(new_lines) - len(old_lines)
                    console.print(f"[dim]Changes: +{diff} lines added[/dim]")
                elif len(new_lines) < len(old_lines):
                    diff = len(old_lines) - len(new_lines)
                    console.print(f"[dim]Changes: -{diff} lines removed[/dim]")
                else:
                    console.print(f"[dim]Changes: ~{len(new_lines)} lines modified[/dim]")

                # Show first few new lines
                console.print("\n[yellow]Preview (first 5 lines of new content):[/yellow]")
                for i, line in enumerate(new_lines[:5], 1):
                    console.print(f"  [dim]{i:2}[/dim]  {line[:70]}")
                if len(new_lines) > 5:
                    console.print(f"  [dim]... ({len(new_lines) - 5} more lines)[/dim]")

            except Exception:
                pass  # If we can't read the file, skip the preview

        else:
            # New file will be created
            console.print(f"[yellow]Action:[/yellow] [green]CREATE[/green] new file ✨")
            console.print(f"[yellow]Output file:[/yellow] {step.output_file}")

            # Show preview of new file
            lines = step.command.split('\n')
            console.print(f"\n[yellow]Preview (first 10 lines):[/yellow]")
            for i, line in enumerate(lines[:10], 1):
                console.print(f"  [dim]{i:2}[/dim]  {line[:70]}")
            if len(lines) > 10:
                console.print(f"  [dim]... ({len(lines) - 10} more lines)[/dim]")

    # Command/code display
    console.print("\n[yellow]Command:[/yellow]")

    # Use syntax highlighting for code
    if step.step_type.value == "code":
        # Try to detect language from filename
        lang = "python"  # default
        if step.output_file:
            if step.output_file.endswith(".js"):
                lang = "javascript"
            elif step.output_file.endswith(".sh"):
                lang = "bash"
            elif step.output_file.endswith(".go"):
                lang = "go"
            elif step.output_file.endswith(".rs"):
                lang = "rust"

        syntax = Syntax(step.command, lang, theme="monokai", line_numbers=False)
        console.print(syntax)
    else:
        console.print(f"[green]{step.command}[/green]")

    # Cost estimate
    if show_cost:
        cost = calculate_cost(step.estimated_tokens, "gpt-4o")
        console.print(
            f"\n[magenta]Estimated: {step.estimated_tokens} tokens (~{format_cost(cost)})[/magenta]"
        )

    console.print("─" * 60)


def display_step_output(step: Step, success: bool) -> None:
    """
    Display the output from executing a step.

    Args:
        step: The step that was executed
        success: Whether execution was successful
    """
    if success:
        console.print(f"\n[bold green]✓ Step completed successfully![/bold green]")
        if step.output.strip():
            # Show more output for verification steps (they're more informative)
            from .plan import StepType
            if step.step_type == StepType.VERIFICATION:
                max_chars = 2000  # More output for tests
            else:
                max_chars = 1000

            output = step.output[:max_chars]
            if len(step.output) > max_chars:
                output += "\n... (output truncated)"

            console.print(f"\n[dim]Output:[/dim]")
            console.print(output)
    else:
        console.print(f"\n[bold red]✗ Step failed![/bold red]")
        if step.error:
            console.print(f"[red]Error: {step.error}[/red]")
        if step.output.strip():
            # Show more error output to help debugging
            output = step.output[:1500]
            if len(step.output) > 1500:
                output += "\n... (output truncated)"
            console.print(f"\n[dim]Output:[/dim]\n{output}")


def display_execution_summary(plan: Plan) -> None:
    """
    Display a summary after plan execution.

    Args:
        plan: The completed plan
    """
    console.print()
    console.print("=" * 60)
    console.print("[bold cyan]EXECUTION SUMMARY[/bold cyan]")
    console.print("=" * 60)

    # Create summary table
    table = Table(show_header=False, box=None)
    table.add_column("Metric", style="bold")
    table.add_column("Value")

    table.add_row("Total Steps", str(len(plan.steps)))
    table.add_row(
        "Completed", f"[green]{len(plan.completed_steps)}[/green]"
    )
    table.add_row("Failed", f"[red]{len(plan.failed_steps)}[/red]")
    table.add_row(
        "Skipped",
        f"[dim]{len([s for s in plan.steps if s.status == StepStatus.SKIPPED])}[/dim]",
    )

    console.print(table)
    console.print("=" * 60)
    console.print()

    # Show files created/modified
    created_files = [
        step.output_file
        for step in plan.completed_steps
        if step.output_file and step.step_type == StepType.CODE
    ]

    if created_files:
        console.print("[bold cyan]📁 Files Created/Modified:[/bold cyan]")
        for file_path in created_files:
            try:
                file_size = Path(file_path).stat().st_size
                size_str = f"{file_size} B" if file_size < 1024 else f"{file_size/1024:.1f} KB"

                # Determine file type
                if file_path.endswith('.py'):
                    file_type = "Python file"
                elif file_path.endswith('.js'):
                    file_type = "JavaScript file"
                elif file_path.endswith(('.txt', '.md')):
                    file_type = "Text file"
                elif file_path.endswith(('.yml', '.yaml')):
                    file_type = "YAML config"
                elif file_path == 'Dockerfile':
                    file_type = "Docker config"
                else:
                    file_type = "File"

                console.print(f"   • [green]{file_path}[/green] ({size_str}) - {file_type}")
            except FileNotFoundError:
                console.print(f"   • [green]{file_path}[/green]")
        console.print()

    # Show dependencies installed
    install_steps = [
        step for step in plan.completed_steps
        if step.step_type == StepType.SHELL and 'pip install' in step.command.lower()
    ]

    if install_steps:
        console.print("[bold cyan]📦 Dependencies Installed:[/bold cyan]")
        for step in install_steps:
            # Extract package names from pip install command
            if 'requirements.txt' in step.command:
                console.print("   • Installed from requirements.txt")
            else:
                # Try to extract package names
                parts = step.command.split()
                packages = [p for p in parts if not p.startswith('-') and p != 'pip' and p != 'install']
                for pkg in packages:
                    console.print(f"   • {pkg}")
        console.print()

    # Show test results
    verification_steps = [
        step for step in plan.completed_steps
        if step.step_type == StepType.VERIFICATION
    ]

    if verification_steps:
        console.print("[bold cyan]✅ Verification:[/bold cyan]")
        for step in verification_steps:
            console.print(f"   • {step.description} [green]✓[/green]")
        console.print()

    # Show what changed
    if plan.completed_steps:
        console.print("[bold cyan]💡 What Was Accomplished:[/bold cyan]")
        accomplishments = []

        # Analyze steps to generate accomplishments
        code_steps = [s for s in plan.completed_steps if s.step_type == StepType.CODE]
        shell_steps = [s for s in plan.completed_steps if s.step_type == StepType.SHELL]

        if code_steps:
            accomplishments.append(f"Created {len(code_steps)} file(s)")
        if install_steps:
            accomplishments.append("Installed project dependencies")
        if verification_steps:
            accomplishments.append("Verified code syntax and functionality")

        for item in accomplishments:
            console.print(f"   • {item}")
        console.print()

    # Show failed steps if any
    if plan.failed_steps:
        console.print("[bold red]❌ Failed Steps:[/bold red]")
        for step in plan.failed_steps:
            console.print(f"  • {step.description}")
            if step.error:
                console.print(f"    [dim]Error: {step.error}[/dim]")
        console.print()

    # Add "How to run" instructions if we created files
    if plan.completed_steps:
        python_files = [
            step.output_file
            for step in plan.completed_steps
            if step.output_file and step.output_file.endswith('.py')
        ]

        javascript_files = [
            step.output_file
            for step in plan.completed_steps
            if step.output_file and step.output_file.endswith('.js')
        ]

        if python_files or javascript_files:
            console.print("[bold cyan]🚀 How to run:[/bold cyan]")

            if python_files:
                # Check if it looks like a game or app
                main_file = python_files[0]  # Use first Python file as main
                console.print(f"  [green]python {main_file}[/green]")
                # Or python3
                console.print(f"  [dim]# or: python3 {main_file}[/dim]")

            if javascript_files:
                main_file = javascript_files[0]
                console.print(f"  [green]node {main_file}[/green]")

            console.print()


def display_progress_header() -> None:
    """Display the execution started message."""
    console.print()
    console.print("[bold cyan]🚀 Starting execution...[/bold cyan]")
    console.print()


def get_approval_prompt() -> str:
    """
    Get user approval for a step.

    Returns:
        User's choice (a/m/s/q)
    """
    console.print()
    choice = typer.prompt(
        "[bold]Action[/bold]",
        type=str,
        default="a",
        show_default=False,
    )
    return choice.lower().strip()


def display_modification_prompt(current_command: str) -> str:
    """
    Prompt user to modify a command.

    Args:
        current_command: The current command text

    Returns:
        Modified command or original if unchanged
    """
    console.print("\n[yellow]Enter modified command (or press Enter to keep current):[/yellow]")
    console.print(f"[dim]Current: {current_command}[/dim]")

    # Use typer.prompt for simple modification
    new_command = typer.prompt(">", default=current_command, show_default=False)

    if new_command != current_command:
        console.print("[green]Command updated![/green]")

    return new_command


def display_approval_options() -> None:
    """Display the available approval options."""
    console.print("\n[bold]Options:[/bold]")
    console.print("  [green][A][/green]pprove - Execute this step")
    console.print("  [yellow][M][/yellow]odify - Edit the command")
    console.print("  [blue][S][/blue]kip - Skip this step")
    console.print("  [red][Q][/red]uit - Cancel execution")
