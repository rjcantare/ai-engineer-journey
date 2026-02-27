# rag/retriever.py

import math
from rag.chunker import load_financial_knowledge
from rag.embedder import get_embedding


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot / (norm1 * norm2)


class FinancialRetriever:

    def __init__(self):
        self.text_chunks = load_financial_knowledge()
        self.embeddings = [
            get_embedding(chunk)
            for chunk in self.text_chunks
        ]

    def retrieve(self, query: str) -> tuple[str, float]:
        query_embedding = get_embedding(query)

        best_score = -1
        best_text = ""

        for text, vector in zip(self.text_chunks, self.embeddings):
            score = cosine_similarity(query_embedding, vector)

            if score > best_score:
                best_score = score
                best_text = text

        return best_text, best_score