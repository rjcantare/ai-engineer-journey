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

    prompt = build_classification_prompt(
        monthly_income=monthly_income,
        dependents=dependents,
        current_savings=current_savings
    )

    result = get_openai_response(prompt)
    raw_response = result["content"]

    try:
        features = validate_features(raw_response)
    except ValueError as e:
        print("\n❌ Model returned invalid structured output.")
        print("Error:", str(e))
        return

    category = classify_risk(features["risk_score"])
    reason = generate_reason(features, category)

    print("\n=== Classification Result ===")
    print(f"Category : {category}")
    print(f"Reason   : {reason}")
    print("=============================\n")

    print("\n--- Token Usage ---")
    print(f"Prompt Tokens     : {result['usage']['prompt_tokens']}")
    print(f"Completion Tokens : {result['usage']['completion_tokens']}")
    print(f"Total Tokens      : {result['usage']['total_tokens']}")
    print("-------------------\n")


if __name__ == "__main__":
    main()
