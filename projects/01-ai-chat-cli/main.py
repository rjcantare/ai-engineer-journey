"""
CLI entry point for financial risk classification tool.
"""

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

    result = get_openai_response(prompt)

    print("\n--- Financial Classification Result ---")
    print(result)


if __name__ == "__main__":
    main()
