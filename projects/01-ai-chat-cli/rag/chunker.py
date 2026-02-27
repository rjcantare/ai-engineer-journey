# rag/chunker.py

def load_financial_knowledge() -> list[str]:
    """
    Returns small, clean financial knowledge chunks.
    Each chunk should represent one clear idea.
    """

    return [
        (
            "An emergency fund should typically cover 3 to 6 months "
            "of essential living expenses. This fund protects against "
            "unexpected events like job loss, medical emergencies, "
            "or urgent repairs."
        ),
        (
            "Term insurance provides life coverage for a fixed period, "
            "such as 10, 20, or 30 years. It does not accumulate cash value "
            "and is generally more affordable than permanent life insurance."
        ),
        (
            "Whole life insurance provides lifetime coverage and includes "
            "a cash value component that grows over time. Premiums are "
            "typically higher than term insurance."
        ),
        (
            "Income replacement planning often recommends coverage equal "
            "to 10 to 15 times annual income. The goal is to ensure "
            "dependents can maintain their lifestyle if income stops."
        ),
        (
            "Risk management involves identifying potential financial risks "
            "and reducing them through strategies such as insurance, "
            "diversification, and maintaining adequate savings."
        )
    ]