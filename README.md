---

# AI Engineer Journey

Building production-ready AI systems with deterministic architecture and controlled LLM boundaries.

---

## About

This repository documents my transition into becoming a **Remote AI Engineer**.

Focus:
Designing reliable AI systems — not just calling APIs.

LLMs are treated as probabilistic components inside deterministic systems.

This repo is a build log of shipped systems — not tutorials.

---

# Week 1 — Deterministic Financial AI System

Built a structured financial risk classification system integrating OpenAI inside strict deterministic boundaries.

LLM is used for structured feature extraction — not decision-making.

---

## Architecture Evolution

### Phase 1 — Direct LLM Classification

LLM returned:

```json
{
  "category": "...",
  "reason": "..."
}
```

Problem:

* Business logic lived inside the prompt
* No deterministic enforcement
* No regression protection

---

### Phase 2 — Hybrid Deterministic Architecture (Current)

LLM now returns structured features only:

```json
{
  "risk_score": 0-100,
  "income_level": "low | medium | high",
  "dependency_load": "low | moderate | high",
  "savings_buffer": "low | moderate | high"
}
```

Classification enforced in Python:

```
risk_score >= 70  → HOT
risk_score 40–69  → WARM
risk_score < 40   → COLD
```

LLM does not control:

* Final decision
* Threshold logic
* Business rules
* Boundary conditions

Result: Controlled hybrid AI system.

---

## Engineering Foundations Established

* OpenAI API integration
* Strict JSON-only LLM contract
* Schema validation boundary
* Deterministic rule engine
* `temperature=0.0` extraction
* Token usage tracking
* Unit tests for boundary protection
* FastAPI transport layer
* Controlled HTTP failure mapping
* Linear Git rebase workflow

System shipped.
Version-controlled.
Deterministic core protected.

---

# Day 8 — Financial-Domain RAG Core (Retrieval Layer)

Implemented manual Retrieval-Augmented Generation mechanics.

No frameworks.
No vector database.
No persistence.

Understanding retrieval at the math layer first.

---

## Implementation Scope

```
01-ai-chat-cli/
├── rag/
│   ├── chunker.py
│   ├── embedder.py
│   ├── retriever.py
│   └── __init__.py
└── test_rag.py
```

---

## Retrieval Design

* Clean financial knowledge chunks (single concept each)
* OpenAI embeddings (`text-embedding-3-small`)
* In-memory vector store (Python list)
* Manual cosine similarity
* Top-1 retrieval
* Deterministic scoring

Embeddings computed once at initialization.
Query embedding computed per request.

---

## Example Behavior

Relevant query:

> “How much emergency fund should someone have?”

Similarity ≈ 0.66
Correct financial chunk retrieved.

Out-of-domain query:

> “What is cryptocurrency?”

Similarity ≈ 0.16
Weak semantic match detected.

Low similarity enables future threshold gating before LLM invocation.

Retriever returns:

```
(chunk, similarity_score)
```

Decision logic intentionally separated from retrieval logic.

---

## Engineering Principles Reinforced

* Separation of concerns
* Deterministic retrieval math
* Transparent similarity scoring
* Threshold-ready architecture
* No premature abstraction
* No framework dependency

---

## Current System State

✔ Deterministic financial classification engine
✔ Manual RAG retrieval layer
✔ Clean layered architecture
✔ Debuggable similarity scoring
✔ Ready for threshold integration
✔ Ready for LLM answer generation layer

---

## Repository Structure

```
ai-engineer-journey/
├── .github/
├── experiments/
├── projects/
│   ├── 01-ai-chat-cli/
│   ├── 02-lead-qualifier-api/
│   ├── 03-pdf-extractor/
│   └── 04-rag-chatbot/
├── notes/
└── README.md
```

---

## Engineering Philosophy

* LLMs interpret — code enforces
* Deterministic business rules first
* Validate before execute
* Auditability over cleverness
* Small controlled iterations
* No framework dependency without understanding mechanics

---

## Author

**Rainiel Jhon Cantare**
AI Engineer in Transition — Philippines

Building layered, controlled, production-aligned AI systems.

---