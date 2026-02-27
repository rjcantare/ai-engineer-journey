# test_rag.py

from rag.retriever import FinancialRetriever


def main():
    retriever = FinancialRetriever()

    while True:
        query = input("\nAsk a financial question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        result, score = retriever.retrieve(query)

        print("\n=== Retrieval Result ===")
        print(f"Similarity Score: {score:.4f}")
        print("Retrieved Chunk:")
        print(result)
        print("========================")


if __name__ == "__main__":
    main()