"""
OpenAI client wrapper for sending prompts and receiving responses.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


def get_openai_response(prompt: str) -> dict[str, object]:
    """
    Send a prompt to OpenAI and return the response text.

    Args:
        prompt (str): The formatted prompt string.

    Returns:
        str: The model's response content.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )

    usage = response.usage

    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    return {
    "content": response.choices[0].message.content,
    "usage": {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens
    }   
}
