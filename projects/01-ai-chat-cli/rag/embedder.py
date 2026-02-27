# rag/embedder.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_embedding(text: str) -> list[float]:
    """
    Convert text into embedding vector.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found.")

    client = OpenAI(api_key=api_key)

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding