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

You MUST return ONLY valid JSON.
Do NOT include explanations, markdown, code fences, or extra text.
Do NOT include any keys other than those specified.

Return strictly this JSON schema:

{{
  "category": "HOT | WARM | COLD",
  "reason": "One concise sentence explaining the classification."
}}

Rules:
- category must be exactly one of: HOT, WARM, COLD
- reason must be exactly one sentence
- Output must be valid JSON
- No text before or after the JSON object

Classification Rules:
- HOT = financially unstable / urgent protection needed
- WARM = moderate stability but risk exists
- COLD = financially stable and protected

Client Data:
Monthly Income: ₱{monthly_income}
Dependents: {dependents}
Current Savings: ₱{current_savings}
"""

    return prompt.strip()
