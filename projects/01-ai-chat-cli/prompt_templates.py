"""
Prompt templates for financial risk classification.
"""


def build_classification_prompt(
    monthly_income: float,
    dependents: int,
    current_savings: float
) -> str:
    """
    Build a structured prompt for financial stability classification.

    Args:
        monthly_income (float): Monthly income in PHP.
        dependents (int): Number of financial dependents.
        current_savings (float): Current savings in PHP.

    Returns:
        str: Formatted prompt string.
    """
    prompt = f"""
You are a conservative financial risk classifier.

Classify the financial stability of this person.

Monthly Income: ₱{monthly_income}
Dependents: {dependents}
Current Savings: ₱{current_savings}

Rules:
- HOT = financially unstable / urgent protection needed
- WARM = moderate stability but risk exists
- COLD = financially stable and protected

Respond in this exact format:

Category: HOT | WARM | COLD
Reason: <exactly 2 sentences>
"""

    return prompt.strip()
