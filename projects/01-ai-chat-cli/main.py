"""
CLI entry point for financial risk classification tool.
"""
import json
from prompt_templates import build_classification_prompt
from openai_client import get_openai_response

def validate_features(raw_response: str) -> dict:
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format.") from e

    required_keys = {
        "risk_score",
        "income_level",
        "dependency_load",
        "savings_buffer"
    }

    if set(parsed.keys()) != required_keys:
        raise ValueError("JSON does not match required schema.")

    if not isinstance(parsed["risk_score"], int):
        raise ValueError("risk_score must be integer.")

    if not 0 <= parsed["risk_score"] <= 100:
        raise ValueError("risk_score must be between 0 and 100.")

    return parsed

def classify_risk(risk_score: int) -> str:
    if risk_score >= 70:
        return "HOT"
    elif 40 <= risk_score <= 69:
        return "WARM"
    else:
        return "COLD"
    
def generate_reason(features: dict, category: str) -> str:
    return (
        f"{category} — "
        f"Risk score: {features['risk_score']}, "
        f"Income level: {features['income_level']}, "
        f"Dependency load: {features['dependency_load']}, "
        f"Savings buffer: {features['savings_buffer']}"
    )

def run_classification_pipeline(
    monthly_income: float,
    dependents: int,
    current_savings: float
) -> dict:
    """
    Orchestrates full classification pipeline and returns structured result.
    """

    # 1. Build prompt
    prompt = build_classification_prompt(
        monthly_income=monthly_income,
        dependents=dependents,
        current_savings=current_savings
    )

    # 2. Call LLM
    result = get_openai_response(prompt)
    raw_response = result["content"]

    # 3. Validate structured output
    features = validate_features(raw_response)

    # 4. Deterministic classification
    category = classify_risk(features["risk_score"])

    # 5. Return structured response
    return {
        "category": category,
        "risk_score": features["risk_score"],
        "income_level": features["income_level"],
        "dependency_load": features["dependency_load"],
        "savings_buffer": features["savings_buffer"]
    }

def main() -> None:
    """
    Collect user input, send to OpenAI, and print classification result.
    """
    try:
        monthly_income = float(input("Enter monthly income (PHP): "))
        dependents = int(input("Enter number of dependents: "))
        current_savings = float(input("Enter current savings (PHP): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    try:
        result = run_classification_pipeline(
            monthly_income,
            dependents,
            current_savings
    )
    except ValueError as e:
        print("\n❌ Model returned invalid structured output.")
        print("Error:", str(e))
        return

    print("\n=== Classification Result ===")
    print(f"Category : {result['category']}")
    print(f"Risk Score : {result['risk_score']}")
    print("=============================\n")

if __name__ == "__main__":
    main()
