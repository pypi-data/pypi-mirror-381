"""
Plan-Execute Handler for breaking down and executing complex tasks step by step.
This handler orchestrates the entire plan-execute workflow with user approval.
"""

import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

import typer
from click.types import Choice
from prompt_toolkit import PromptSession

from ..config import cfg
from ..cost_estimator import MODEL_PRICING, calculate_cost, format_cost
from ..plan import Plan, Step, StepStatus, StepType
from ..plan_parser import parse_plan
from ..plan_ui import (
    display_approval_options,
    display_execution_summary,
    display_plan_overview,
    display_progress_header,
    display_step_detail,
    display_step_output,
)
from ..role import SystemRole
from ..utils import run_command
from .handler import Handler


class PlanExecuteHandler(Handler):
    """
    Handler for plan-execute mode.
    Generates a plan from user prompt, estimates costs, and executes step-by-step
    with user approval.
    """

    def __init__(
        self,
        role: SystemRole,
        markdown: bool,
        auto_approve: bool = False,
        show_costs: bool = True,
    ) -> None:
        super().__init__(role, markdown)
        self.auto_approve = auto_approve
        self.show_costs = show_costs
        self.session: PromptSession[str] = PromptSession()

    def make_messages(self, prompt: str) -> List[Dict[str, str]]:
        """Create messages for plan generation."""
        system_prompt = """You are a task planning and execution assistant.
Your job is to break down complex tasks into discrete, executable steps.

IMPORTANT: If the user provides existing code/files in their prompt (via stdin),
you can analyze it and create steps to modify or improve it. The user's prompt
may include file contents followed by instructions.

For each task, you must respond with a JSON object with this structure:
{
    "steps": [
        {
            "description": "Brief description of what this step does",
            "type": "shell|code|verification",
            "command": "The shell command OR code to execute",
            "output_file": "path/to/file.ext (only for code type, otherwise null)",
            "estimated_tokens": 100
        }
    ]
}

CRITICAL GUIDELINES FOR STEP TYPES:

1. **Use "code" type when:**
   - Creating/writing a new source code file (Python, JavaScript, HTML, etc.)
   - The "command" field contains the source code to write to the file
   - MUST specify "output_file" with the target filename
   - The code will be written to the file AS-IS

2. **Use "shell" type when:**
   - Running shell commands (ls, mkdir, pip install, npm install, etc.)
   - The "command" is a bash/shell command
   - Set "output_file" to null

3. **Use "verification" type when:**
   - Testing or verifying previous steps (python script.py, npm test, etc.)
   - Non-critical checks that can fail without stopping execution
   - Set "output_file" to null

Example for "create a hello.py file":
{
    "steps": [
        {
            "description": "Create hello.py with print statement",
            "type": "code",
            "command": "print('Hello, World!')",
            "output_file": "hello.py",
            "estimated_tokens": 50
        },
        {
            "description": "Run the Python script",
            "type": "verification",
            "command": "python hello.py",
            "output_file": null,
            "estimated_tokens": 50
        }
    ]
}

Example for "install flask":
{
    "steps": [
        {
            "description": "Install Flask using pip",
            "type": "shell",
            "command": "pip install flask",
            "output_file": null,
            "estimated_tokens": 50
        }
    ]
}

SPECIAL INSTRUCTIONS FOR GAME PROJECTS:

When creating games (pygame, tkinter, curses, etc.):
- Create complete, working games with proper game loops
- Include clear comments in code for better understanding
- For pygame/GUI games: Use syntax verification ONLY (python -m py_compile game.py)
  * Do NOT run interactive programs in verification steps - they will hang
- For text-based games: OK to verify by running with sample input
- Always create a requirements.txt if using external libraries (pygame, etc.)
- Structure: game code file → requirements.txt → pip install → syntax check verification
- Add helpful comments explaining game controls and how to play

Example for "create a snake game":
{
    "steps": [
        {
            "description": "Create snake_game.py with pygame",
            "type": "code",
            "command": "import pygame\\nimport random\\n\\n# Initialize pygame\\npygame.init()\\n\\n# Game constants\\nWIDTH, HEIGHT = 600, 400\\n...",
            "output_file": "snake_game.py",
            "estimated_tokens": 800
        },
        {
            "description": "Create requirements.txt",
            "type": "code",
            "command": "pygame>=2.5.0",
            "output_file": "requirements.txt",
            "estimated_tokens": 20
        },
        {
            "description": "Install pygame",
            "type": "shell",
            "command": "pip install -r requirements.txt",
            "output_file": null,
            "estimated_tokens": 50
        },
        {
            "description": "Verify syntax of snake_game.py",
            "type": "verification",
            "command": "python -m py_compile snake_game.py",
            "output_file": null,
            "estimated_tokens": 50
        }
    ]
}

Example when user provides existing code via stdin:
User input: "cat sample_code.py | sgpt --planexec 'fix the style issues'"
(stdin contains the code from sample_code.py)

{
    "steps": [
        {
            "description": "Overwrite sample_code.py with fixed formatting",
            "type": "code",
            "command": "def add(a, b):\\n    return a + b\\n\\ndef multiply(x, y):\\n    return x * y",
            "output_file": "sample_code.py",
            "estimated_tokens": 100
        },
        {
            "description": "Verify syntax of fixed code",
            "type": "verification",
            "command": "python -m py_compile sample_code.py",
            "output_file": null,
            "estimated_tokens": 50
        }
    ]
}

IMPORTANT: When code is provided via stdin with a recognizable filename (like "cat file.py | ..."):
- Extract the filename from the context
- Use that filename as the output_file to overwrite it
- If no filename is detectable, ask user or use a sensible default like "fixed_code.py"
- ONLY create requirements.txt and pip install steps if NEW dependencies are being added
- If modifying existing code without adding new imports, skip dependency steps
- Focus on the requested changes only

Example of improving existing code (no new dependencies):
User input: "cat snake_game.py | ... improve the visual design"
(stdin contains existing pygame code)

{
    "steps": [
        {
            "description": "Update snake_game.py with better colors and UI",
            "type": "code",
            "command": "import pygame\\n... (improved code with better colors) ...",
            "output_file": "snake_game.py",
            "estimated_tokens": 600
        },
        {
            "description": "Verify syntax",
            "type": "verification",
            "command": "python -m py_compile snake_game.py",
            "output_file": null,
            "estimated_tokens": 50
        }
    ]
}

Note: No requirements.txt or pip install since pygame was already being used.

Return ONLY the JSON object, no additional text."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
        return messages



    def get_user_approval(self, step: Step) -> str:
        """
        Get user approval for executing a step.

        Returns:
            'a' for approve, 'm' for modify, 's' for skip, 'q' for quit
        """
        if self.auto_approve:
            typer.secho("[Auto-approved]", fg="green")
            return "a"

        display_approval_options()
        option = typer.prompt(
            text="Choose action",
            type=Choice(("a", "m", "s", "q"), case_sensitive=False),
            default="a",
            show_choices=False,
            show_default=False,
        )
        return option.lower()

    def execute_step(self, step: Step) -> bool:
        """
        Execute a single step with improved error handling.

        Args:
            step: The step to execute

        Returns:
            True if successful, False otherwise
        """
        step.status = StepStatus.IN_PROGRESS

        try:
            if step.step_type == StepType.CODE:
                # Handle CODE type steps - execute code and optionally save to file
                if not step.output_file:
                    step.error = "No output file specified for code step"
                    step.status = StepStatus.FAILED
                    display_step_output(step, success=False)
                    return False

                output_path = Path(step.output_file)

                # Check if file already exists
                if output_path.exists():
                    overwrite = typer.confirm(
                        f"\n⚠ File {step.output_file} already exists. Overwrite?",
                        default=False,
                    )
                    if not overwrite:
                        step.status = StepStatus.SKIPPED
                        typer.secho("\n⊘ Step skipped (file exists).", fg="yellow")
                        return False

                # Create parent directories if needed
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Write the code to the target file
                output_path.write_text(step.command, encoding="utf-8")

                step.output = f"File written to {step.output_file} ({len(step.command)} bytes)"
                step.status = StepStatus.COMPLETED
                display_step_output(step, success=True)
                return True

            elif step.step_type == StepType.SHELL or step.step_type == StepType.VERIFICATION:
                # Check if this is an interactive program (verification only)
                if step.step_type == StepType.VERIFICATION and self.is_interactive_program(step.command):
                    typer.secho(
                        "\n⚠ Skipping interactive program verification (would hang)",
                        fg="yellow"
                    )
                    typer.secho(
                        f"💡 To run manually: {step.command}",
                        fg="cyan"
                    )
                    step.status = StepStatus.SKIPPED
                    step.output = "Skipped: Interactive program detected"
                    return True  # Non-critical, continue to next step

                # Check if required dependencies are available
                has_deps, dep_error = self.check_command_dependencies(step.command)
                if not has_deps:
                    typer.secho(f"\n⚠ Dependency missing: {dep_error}", fg="yellow")
                    skip = typer.confirm("Skip this step?", default=True)
                    if skip:
                        step.status = StepStatus.SKIPPED
                        step.error = dep_error
                        step.output = f"Skipped due to missing dependency: {dep_error}"
                        return False
                    # User chose not to skip, continue anyway (might fail)

                # Check for file redirection in shell commands (e.g., "echo 'x' > file.txt")
                # and warn if file exists
                if ">" in step.command and not ">>" in step.command:
                    # Extract potential filename
                    match = re.search(r'>\s*([^\s;&|]+)', step.command)
                    if match:
                        potential_file = match.group(1).strip().strip("'\"")
                        if Path(potential_file).exists():
                            overwrite = typer.confirm(
                                f"\n⚠ File {potential_file} already exists. Overwrite?",
                                default=False,
                            )
                            if not overwrite:
                                step.status = StepStatus.SKIPPED
                                typer.secho("\n⊘ Step skipped (file exists).", fg="yellow")
                                return False

                # Execute shell command
                typer.secho("\n[Executing...]", fg="white", dim=True)
                result = subprocess.run(
                    step.command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=120,  # Increased timeout for longer operations
                )
                step.output = result.stdout + result.stderr

                if result.returncode != 0:
                    step.error = f"Command failed with exit code {result.returncode}"
                    step.status = StepStatus.FAILED

                    # Verification steps can fail without being critical
                    if step.step_type == StepType.VERIFICATION:
                        typer.secho(
                            "\n⚠ Verification step failed (non-critical)", fg="yellow"
                        )
                    else:
                        display_step_output(step, success=False)
                    return False
                else:
                    step.status = StepStatus.COMPLETED
                    display_step_output(step, success=True)
                    return True

        except subprocess.TimeoutExpired:
            step.error = "Command timed out (120s limit)"
            step.status = StepStatus.FAILED
            display_step_output(step, success=False)
            return False
        except PermissionError as e:
            step.error = f"Permission denied: {e}"
            step.status = StepStatus.FAILED
            display_step_output(step, success=False)
            return False
        except Exception as e:
            step.error = str(e)
            step.status = StepStatus.FAILED
            display_step_output(step, success=False)
            return False

    def check_command_dependencies(self, command: str) -> tuple[bool, str]:
        """
        Check if required tools for a command are available.

        Args:
            command: The command to check

        Returns:
            Tuple of (has_dependencies, error_message)
        """
        command_lower = command.lower().strip()

        # Check for pip
        if command_lower.startswith("pip install") or command_lower.startswith("pip3 install"):
            result = subprocess.run("which pip", shell=True, capture_output=True)
            if result.returncode != 0:
                result = subprocess.run("which pip3", shell=True, capture_output=True)
                if result.returncode != 0:
                    return False, "pip not found. Install with: sudo apt install python3-pip"
            return True, ""

        # Check for python
        if command_lower.startswith("python ") or "python -" in command_lower:
            result = subprocess.run("which python", shell=True, capture_output=True)
            if result.returncode != 0:
                result = subprocess.run("which python3", shell=True, capture_output=True)
                if result.returncode != 0:
                    return False, "python not found. Install Python first."
            return True, ""

        # Check for npm
        if command_lower.startswith("npm "):
            result = subprocess.run("which npm", shell=True, capture_output=True)
            if result.returncode != 0:
                return False, "npm not found. Install Node.js first."
            return True, ""

        # Check for docker
        if command_lower.startswith("docker "):
            result = subprocess.run("which docker", shell=True, capture_output=True)
            if result.returncode != 0:
                return False, "docker not found. Install Docker first."
            return True, ""

        return True, ""

    def is_interactive_program(self, command: str) -> bool:
        """
        Check if a command runs an interactive program that would hang.

        Args:
            command: The command to check

        Returns:
            True if the command appears to run an interactive program
        """
        interactive_keywords = [
            "pygame",      # Pygame games
            "tkinter",     # GUI applications
            "curses",      # Terminal UI
            "input(",      # Python input() calls
            "raw_input(",  # Python 2 input
            "flask run",   # Flask dev server
            "django runserver",  # Django dev server
            "streamlit run",     # Streamlit apps
            "gradio",      # Gradio apps
            "game",        # Generic game keyword
            "interactive", # Explicitly interactive
            "gui",         # GUI programs
            "serve",       # Web servers
            "uvicorn",     # FastAPI server
        ]

        command_lower = command.lower()
        return any(keyword in command_lower for keyword in interactive_keywords)

    def modify_step(self, step: Step) -> None:
        """Allow user to modify a step's command."""
        typer.secho("\nEnter modified command (or press Enter to keep current):", fg="yellow")
        new_command = self.session.prompt("> ", default=step.command)
        if new_command and new_command != step.command:
            step.command = new_command
            typer.secho("✓ Command updated!", fg="green")

    def suggest_fix(
        self, step: Step, model: str, temperature: float, top_p: float
    ) -> Optional[str]:
        """
        Ask LLM to suggest a fix for a failed step.

        Args:
            step: The failed step
            model: Model to use
            temperature: Temperature setting
            top_p: Top-p setting

        Returns:
            Suggested fixed command or None
        """
        typer.secho("\n🤔 Asking LLM for a fix suggestion...", fg="yellow")

        fix_prompt = f"""The following command failed:
Command: {step.command}
Error: {step.error}
Output: {step.output[:500]}

Please suggest a fixed version of the command that might work.
Respond with ONLY the corrected command - no explanations, no markdown code blocks, no backticks.
Just the raw command that can be executed directly in a shell."""

        messages = [
            {"role": "system", "content": "You are a helpful assistant that fixes shell commands and code."},
            {"role": "user", "content": fix_prompt},
        ]

        try:
            # Use the base handler's get_completion without caching
            # We create a simple non-cached completion call
            from ..handlers.handler import use_litellm

            if use_litellm:
                import litellm  # type: ignore
                response = litellm.completion(
                    model=model,
                    temperature=temperature,
                    top_p=top_p,
                    messages=messages,
                    stream=True,
                )
            else:
                from openai import OpenAI
                client = OpenAI(
                    api_key=cfg.get("OPENAI_API_KEY"),
                    base_url=None if cfg.get("API_BASE_URL") == "default" else cfg.get("API_BASE_URL"),
                )
                response = client.chat.completions.create(
                    model=model,
                    temperature=temperature,
                    top_p=top_p,
                    messages=messages,
                    stream=True,
                )

            suggested_fix = ""
            for chunk in response:
                delta = chunk.choices[0].delta
                if use_litellm:
                    content = delta.get("content") or ""
                else:
                    content = delta.content or ""
                suggested_fix += content

            suggested_fix = suggested_fix.strip()

            # Clean up the suggested fix - remove markdown code blocks
            if suggested_fix.startswith("```"):
                # Remove ```bash or ```sh or ``` at start
                lines = suggested_fix.split("\n")
                # Remove first line if it's a code fence
                if lines[0].startswith("```"):
                    lines = lines[1:]
                # Remove last line if it's a code fence
                if lines and lines[-1].strip() == "```":
                    lines = lines[:-1]
                suggested_fix = "\n".join(lines).strip()

            # Remove any remaining backticks
            suggested_fix = suggested_fix.strip("`").strip()

            if suggested_fix and suggested_fix != step.command:
                typer.secho("\n💡 Suggested fix:", fg="green")
                typer.secho(suggested_fix, fg="cyan")
                return suggested_fix
            else:
                typer.secho("No fix suggestion available.", fg="yellow")
                return None

        except Exception as e:
            typer.secho(f"Could not get fix suggestion: {e}", fg="red")
            return None

    def handle(
        self,
        prompt: str,
        model: str,
        temperature: float,
        top_p: float,
        caching: bool,
        functions: Optional[List[Dict[str, str]]] = None,
        **kwargs: Any,
    ) -> str:
        """
        Main handler for plan-execute mode.

        Args:
            prompt: User's goal/task description
            model: Model to use
            temperature: Temperature for generation
            top_p: Top-p for generation
            caching: Whether to use caching
            functions: Function schemas (not used in plan-execute)
            **kwargs: Additional arguments

        Returns:
            Summary of execution
        """
        # Step 1: Generate plan
        typer.secho("\n🔄 Generating execution plan...\n", fg="cyan", bold=True)

        messages = self.make_messages(prompt.strip())
        generator = self.get_completion(
            model=model,
            temperature=temperature,
            top_p=top_p,
            messages=messages,
            functions=None,  # Disable functions for plan generation
            caching=caching,
        )

        # Collect full response
        response = ""
        for chunk in generator:
            response += chunk

        # Step 2: Parse plan
        plan = parse_plan(response, prompt, model)

        # Step 3: Display plan and get initial approval
        display_plan_overview(plan, show_costs=self.show_costs)

        if not self.auto_approve:
            typer.echo()  # Add blank line for clarity
            typer.secho("─" * 60, fg="cyan")
            proceed = typer.confirm(
                "Review the plan above. Proceed with execution?",
                default=True
            )
            typer.secho("─" * 60, fg="cyan")
            if not proceed:
                typer.secho("\n⚠ Execution cancelled by user.", fg="yellow")
                return "Execution cancelled by user."

        # Step 4: Execute steps
        display_progress_header()

        for i, step in enumerate(plan.steps, 1):
            display_step_detail(step, i, len(plan.steps), show_cost=self.show_costs)

            # Get approval
            approval = self.get_user_approval(step)

            if approval == "q":
                typer.secho("\n⚠ Execution cancelled by user.", fg="yellow")
                break
            elif approval == "s":
                step.status = StepStatus.SKIPPED
                typer.secho("\n⊘ Step skipped.", fg="yellow")
                continue
            elif approval == "m":
                self.modify_step(step)
                # Ask again after modification
                approval = self.get_user_approval(step)
                if approval != "a":
                    step.status = StepStatus.SKIPPED
                    typer.secho("\n⊘ Step skipped.", fg="yellow")
                    continue

            # Execute the step
            success = self.execute_step(step)

            if not success and step.step_type != StepType.VERIFICATION:
                # Verification steps can fail without stopping
                typer.secho("\nWhat would you like to do?", fg="cyan", bold=True)
                typer.echo("  [R]etry - Try the same command again")
                typer.echo("  [F]ix - Ask LLM to suggest a fix")
                typer.echo("  [M]odify - Manually edit the command")
                typer.echo("  [C]ontinue - Continue to next step")
                typer.echo("  [Q]uit - Stop execution")

                action = typer.prompt(
                    "Choose action",
                    type=Choice(("r", "f", "m", "c", "q"), case_sensitive=False),
                    default="f",
                    show_choices=False,
                )

                if action == "r":
                    # Retry same command
                    success = self.execute_step(step)
                    if not success:
                        typer.secho("\nStep failed again.", fg="red")
                        stop = typer.confirm(
                            "Stop execution?",
                            default=True,
                        )
                        if stop:
                            break
                elif action == "f":
                    # Get LLM fix suggestion
                    suggested_fix = self.suggest_fix(step, model, temperature, top_p)
                    if suggested_fix:
                        use_fix = typer.confirm(
                            "\nUse this suggested fix?", default=True
                        )
                        if use_fix:
                            step.command = suggested_fix
                            success = self.execute_step(step)
                            if not success:
                                typer.secho(
                                    "\nFix didn't work. Continuing to next step.",
                                    fg="yellow",
                                )
                elif action == "m":
                    # Manual modification
                    self.modify_step(step)
                    success = self.execute_step(step)
                    if not success:
                        typer.secho(
                            "\nModified command failed. Continuing to next step.",
                            fg="yellow",
                        )
                elif action == "c":
                    # Continue to next step
                    typer.secho("\nContinuing despite failure...", fg="yellow")
                    continue
                elif action == "q":
                    # Quit execution
                    typer.secho("\n⚠ Execution stopped by user.", fg="yellow")
                    break

        # Step 5: Display summary
        display_execution_summary(plan)

        return f"Plan execution completed. {plan.get_progress()}"
