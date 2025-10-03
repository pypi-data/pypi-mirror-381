"""
Plan and Step data structures for Plan-Execute mode.
This module defines the core data structures for breaking down complex tasks
into executable steps with cost tracking and status management.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class StepStatus(Enum):
    """Status of a plan step."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class StepType(Enum):
    """Type of step to execute."""

    SHELL = "shell"  # Shell command
    CODE = "code"  # Code snippet to write to file
    VERIFICATION = "verification"  # Verification/test step


@dataclass
class Step:
    """
    Represents a single executable step in a plan.

    Attributes:
        description: Human-readable description of what this step does
        step_type: Type of step (shell, code, verification)
        command: The command or code to execute
        output_file: Optional file path to write code to (for CODE type)
        estimated_tokens: Estimated token count for this step
        status: Current status of the step
        output: Output from executing this step
        error: Error message if step failed
    """

    description: str
    step_type: StepType
    command: str
    output_file: Optional[str] = None
    estimated_tokens: int = 0
    status: StepStatus = StepStatus.PENDING
    output: str = ""
    error: str = ""

    def __str__(self) -> str:
        """String representation of the step."""
        status_symbol = {
            StepStatus.PENDING: "○",
            StepStatus.IN_PROGRESS: "●",
            StepStatus.COMPLETED: "✓",
            StepStatus.FAILED: "✗",
            StepStatus.SKIPPED: "⊘",
        }
        symbol = status_symbol.get(self.status, "○")
        return f"{symbol} {self.description}"


@dataclass
class Plan:
    """
    Represents a complete execution plan with multiple steps.

    Attributes:
        goal: The original user goal/prompt
        steps: List of steps to execute
        current_step_index: Index of the currently executing step
        total_estimated_tokens: Total estimated tokens for all steps
        total_estimated_cost: Estimated cost in USD
        model: The model being used for execution
    """

    goal: str
    steps: List[Step] = field(default_factory=list)
    current_step_index: int = 0
    total_estimated_tokens: int = 0
    total_estimated_cost: float = 0.0
    model: str = "gpt-4o"

    @property
    def is_complete(self) -> bool:
        """Check if all steps are completed or skipped."""
        return all(
            step.status in (StepStatus.COMPLETED, StepStatus.SKIPPED)
            for step in self.steps
        )

    @property
    def current_step(self) -> Optional[Step]:
        """Get the current step being executed."""
        if 0 <= self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]
        return None

    @property
    def failed_steps(self) -> List[Step]:
        """Get all failed steps."""
        return [step for step in self.steps if step.status == StepStatus.FAILED]

    @property
    def completed_steps(self) -> List[Step]:
        """Get all completed steps."""
        return [step for step in self.steps if step.status == StepStatus.COMPLETED]

    def next_step(self) -> Optional[Step]:
        """Move to next step and return it."""
        self.current_step_index += 1
        return self.current_step

    def add_step(self, step: Step) -> None:
        """Add a step to the plan."""
        self.steps.append(step)
        self.total_estimated_tokens += step.estimated_tokens

    def update_cost_estimate(self, cost_per_1k_tokens: float) -> None:
        """
        Update the total estimated cost based on token count.

        Args:
            cost_per_1k_tokens: Cost per 1000 tokens for the model
        """
        self.total_estimated_cost = (
            self.total_estimated_tokens / 1000
        ) * cost_per_1k_tokens

    def get_progress(self) -> str:
        """Get a progress string like '3/5 steps completed'."""
        completed = len(self.completed_steps)
        total = len(self.steps)
        return f"{completed}/{total} steps completed"

    def __str__(self) -> str:
        """String representation of the plan."""
        lines = [f"Goal: {self.goal}", ""]
        for i, step in enumerate(self.steps, 1):
            current_marker = "→ " if i - 1 == self.current_step_index else "  "
            lines.append(f"{current_marker}{i}. {step}")
        lines.append("")
        lines.append(self.get_progress())
        lines.append(
            f"Estimated cost: ${self.total_estimated_cost:.4f} ({self.total_estimated_tokens} tokens)"
        )
        return "\n".join(lines)
