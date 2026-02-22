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
    You are a structured financial feature extraction engine.

    You MUST return ONLY valid JSON.
    Do NOT include explanations, markdown, code fences, or extra text.
    Do NOT include any keys other than those specified.

    Return strictly this JSON schema:

    {{
    "risk_score": number (0-100),
    "income_level": "low" | "medium" | "high",
    "dependency_load": "low" | "moderate" | "high",
    "savings_buffer": "low" | "moderate" | "high"
    }}

    Rules:
    - risk_score must be an integer between 0 and 100
    - Output must be valid JSON
    - No text before or after the JSON object

    Client Data:
    Monthly Income: ₱{monthly_income}
    Dependents: {dependents}
    Current Savings: ₱{current_savings}
    """

    return prompt.strip()
