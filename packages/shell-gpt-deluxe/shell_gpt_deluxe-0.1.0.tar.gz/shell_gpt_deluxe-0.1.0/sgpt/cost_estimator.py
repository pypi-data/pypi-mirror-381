"""
Cost estimation utilities for Plan-Execute mode.
Provides token counting and cost calculation for different models.
"""

from typing import Dict


# Model pricing per 1K tokens (input tokens, approximate as of 2024)
# These are estimates - update based on current OpenAI pricing
MODEL_PRICING: Dict[str, float] = {
    "gpt-4o": 0.0025,  # GPT-4o input pricing
    "gpt-4o-mini": 0.00015,
    "gpt-4": 0.03,
    "gpt-4-turbo": 0.01,
    "gpt-4-turbo-preview": 0.01,
    "gpt-3.5-turbo": 0.0005,
    "gpt-3.5-turbo-16k": 0.003,
}


def estimate_tokens(text: str) -> int:
    """
    Estimate token count for a given text.
    This is a rough approximation: ~4 characters per token for English text.

    For production use, consider using tiktoken library for accurate counts.

    Args:
        text: Text to estimate tokens for

    Returns:
        Estimated token count
    """
    # Rule of thumb: ~4 characters per token (conservative estimate)
    # This includes whitespace and punctuation
    char_count = len(text)
    estimated_tokens = max(1, char_count // 4)

    # Add some overhead for formatting and special tokens
    estimated_tokens = int(estimated_tokens * 1.1)

    return estimated_tokens


def estimate_command_tokens(command: str, step_type: str) -> int:
    """
    Estimate tokens for a command based on its type.

    Args:
        command: The command or code to execute
        step_type: Type of step (shell, code, verification)

    Returns:
        Estimated token count
    """
    base_tokens = estimate_tokens(command)

    # Code steps might have more tokens due to formatting
    if step_type == "code":
        return int(base_tokens * 1.2)

    return base_tokens


def calculate_cost(token_count: int, model: str) -> float:
    """
    Calculate cost for a given token count and model.

    Args:
        token_count: Number of tokens
        model: Model name

    Returns:
        Estimated cost in USD
    """
    # Get price per 1K tokens, default to gpt-4o pricing
    price_per_1k = MODEL_PRICING.get(model, MODEL_PRICING["gpt-4o"])

    # Calculate cost
    cost = (token_count / 1000) * price_per_1k

    return cost


def format_cost(cost: float) -> str:
    """
    Format cost for display.

    Args:
        cost: Cost in USD

    Returns:
        Formatted cost string
    """
    if cost < 0.0001:
        return "<$0.0001"
    elif cost < 0.01:
        return f"${cost:.4f}"
    elif cost < 1.0:
        return f"${cost:.3f}"
    else:
        return f"${cost:.2f}"


def get_model_info(model: str) -> Dict[str, any]:
    """
    Get information about a model.

    Args:
        model: Model name

    Returns:
        Dictionary with model information
    """
    price_per_1k = MODEL_PRICING.get(model, MODEL_PRICING["gpt-4o"])

    return {
        "name": model,
        "price_per_1k_tokens": price_per_1k,
        "price_formatted": format_cost(price_per_1k),
    }
