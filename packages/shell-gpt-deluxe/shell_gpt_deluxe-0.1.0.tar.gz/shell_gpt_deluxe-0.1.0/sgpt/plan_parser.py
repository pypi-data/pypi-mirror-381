"""
Plan parser for converting LLM responses into Plan objects.
Handles various response formats (JSON, markdown, etc.)
"""

import json
import re
from typing import Optional

from .cost_estimator import MODEL_PRICING
from .plan import Plan, Step, StepType


def extract_json_from_response(response: str) -> str:
    """
    Extract JSON from various response formats.

    Args:
        response: Raw LLM response

    Returns:
        Cleaned JSON string
    """
    response = response.strip()

    # Remove markdown code blocks
    if "```json" in response:
        response = response.split("```json")[1].split("```")[0].strip()
    elif "```" in response:
        # Try to find JSON in any code block
        parts = response.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("{") or part.startswith("["):
                response = part
                break

    return response


def parse_step_type(type_str: str) -> StepType:
    """
    Parse step type string into StepType enum.

    Args:
        type_str: Type string from LLM

    Returns:
        StepType enum value
    """
    type_str = type_str.lower().strip()

    if type_str in ("code", "write", "create"):
        return StepType.CODE
    elif type_str in ("verification", "verify", "test", "check"):
        return StepType.VERIFICATION
    else:
        return StepType.SHELL


def parse_plan_from_json(
    response: str, goal: str, model: str
) -> Optional[Plan]:
    """
    Parse a JSON response into a Plan object.

    Args:
        response: JSON response from LLM
        goal: Original user goal
        model: Model being used

    Returns:
        Plan object or None if parsing failed
    """
    try:
        json_str = extract_json_from_response(response)
        data = json.loads(json_str)

        plan = Plan(goal=goal, model=model)

        steps_data = data.get("steps", [])
        if not steps_data:
            return None

        for step_data in steps_data:
            step_type = parse_step_type(step_data.get("type", "shell"))

            step = Step(
                description=step_data.get("description", ""),
                step_type=step_type,
                command=step_data.get("command", ""),
                output_file=step_data.get("output_file"),
                estimated_tokens=step_data.get("estimated_tokens", 100),
            )
            plan.add_step(step)

        # Update cost estimate
        cost_per_1k = MODEL_PRICING.get(model, MODEL_PRICING.get("gpt-4o", 0.0025))
        plan.update_cost_estimate(cost_per_1k)

        return plan

    except (json.JSONDecodeError, KeyError, ValueError):
        return None


def parse_plan_from_markdown(goal: str, model: str, response: str) -> Optional[Plan]:
    """
    Parse a markdown-formatted plan into a Plan object.
    Fallback parser for when LLM doesn't return JSON.

    Args:
        goal: Original user goal
        model: Model being used
        response: Markdown response from LLM

    Returns:
        Plan object or None if parsing failed
    """
    plan = Plan(goal=goal, model=model)

    # Look for numbered steps
    # Pattern: 1. Description: command
    pattern = r"(\d+)\.\s*([^:]+):\s*`?([^`\n]+)`?"
    matches = re.findall(pattern, response)

    if not matches:
        return None

    for _, description, command in matches:
        step = Step(
            description=description.strip(),
            step_type=StepType.SHELL,
            command=command.strip(),
            estimated_tokens=100,
        )
        plan.add_step(step)

    if plan.steps:
        cost_per_1k = MODEL_PRICING.get(model, MODEL_PRICING.get("gpt-4o", 0.0025))
        plan.update_cost_estimate(cost_per_1k)
        return plan

    return None


def create_fallback_plan(goal: str, model: str) -> Plan:
    """
    Create a simple fallback plan when parsing fails.

    Args:
        goal: Original user goal
        model: Model being used

    Returns:
        Simple single-step plan
    """
    plan = Plan(goal=goal, model=model)

    step = Step(
        description="Execute task directly",
        step_type=StepType.SHELL,
        command=goal,
        estimated_tokens=100,
    )
    plan.add_step(step)

    cost_per_1k = MODEL_PRICING.get(model, MODEL_PRICING.get("gpt-4o", 0.0025))
    plan.update_cost_estimate(cost_per_1k)

    return plan


def parse_plan(response: str, goal: str, model: str) -> Plan:
    """
    Parse LLM response into a Plan object.
    Tries multiple parsing strategies.

    Args:
        response: LLM response
        goal: Original user goal
        model: Model being used

    Returns:
        Parsed Plan object
    """
    # Try JSON parsing first
    plan = parse_plan_from_json(response, goal, model)
    if plan and plan.steps:
        return plan

    # Try markdown parsing
    plan = parse_plan_from_markdown(goal, model, response)
    if plan and plan.steps:
        return plan

    # Fallback to simple plan
    return create_fallback_plan(goal, model)
