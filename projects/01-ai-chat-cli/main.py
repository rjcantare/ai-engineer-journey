"""
CLI entry point for financial risk classification tool.
"""
import json
from unittest import result
from prompt_templates import build_classification_prompt
from openai_client import get_openai_response

def validate_classification(raw_response: str) -> tuple[str, str]:
    """
    Validate and extract classification result from raw JSON string.
    
    Returns:
        tuple[str, str]: (category, reason)
    
    Raises:
        ValueError: If JSON is invalid or schema is incorrect.
    """
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format.") from e

    if not isinstance(parsed, dict):
        raise ValueError("Response is not a JSON object.")

    # Ensure only expected keys exist
    expected_keys = {"category", "reason"}
    if set(parsed.keys()) != expected_keys:
        raise ValueError("JSON does not match required schema.")

    category = parsed.get("category")
    reason = parsed.get("reason")

    if category not in ["HOT", "WARM", "COLD"]:
        raise ValueError("Invalid category value.")

    if not isinstance(reason, str) or len(reason.strip()) == 0:
        raise ValueError("Invalid reason value.")

    return category, reason

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
        category, reason = validate_classification(raw_response)
    except ValueError as e:
        print("\n❌ Model returned invalid structured output.")
        print("Error:", str(e))
        return

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
