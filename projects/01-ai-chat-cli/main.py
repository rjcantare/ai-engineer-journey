"""
CLI entry point for financial risk classification tool.
"""
import json
from prompt_templates import build_classification_prompt
from openai_client import get_openai_response


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

    raw_response = get_openai_response(prompt)

    try:
        parsed = json.loads(raw_response)

        category = parsed.get("category")
        reason = parsed.get("reason")

        if category not in ["HOT", "WARM", "COLD"]:
            raise ValueError("Invalid category value.")

        if not isinstance(reason, str) or len(reason.strip()) == 0:
            raise ValueError("Invalid reason value.")

    except (json.JSONDecodeError, ValueError, KeyError) as e:
        print("\n❌ Model returned invalid structured output.")
        print("Error:", str(e))
        return

    print("\n=== Classification Result ===")
    print(f"Category : {category}")
    print(f"Reason   : {reason}")
    print("=============================\n")   


if __name__ == "__main__":
    main()
