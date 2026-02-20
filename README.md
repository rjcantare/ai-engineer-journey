# AI Engineer Journey

Building production-ready AI systems with deterministic architecture and controlled LLM boundaries.

---

## About

This repository documents my transition into becoming a Remote AI Engineer.

Focus: designing reliable AI systems — not just calling APIs.

Core areas:

* Python engineering
* OpenAI API integrations
* Deterministic system design
* Structured output enforcement
* Clean architecture & Git discipline

This is a build log of shipped systems.

---

## Repository Structure

```
ai-engineer-journey/
├── experiments/          # Prototypes
├── projects/             # Production-structured builds
│   ├── 01-ai-chat-cli/   # Financial Classifier (Shipped)
│   ├── 02-lead-qualifier-api/
│   ├── 03-pdf-extractor/
│   └── 04-rag-chatbot/
├── notes/
└── README.md
```

---

# 01 – OpenAI CLI Financial Classifier (Shipped)

A structured CLI tool integrating with the OpenAI API to classify financial stability.

### Key Engineering Highlights

* Strict JSON-only LLM contract
* Deterministic schema validation boundary
* Enum enforcement (HOT / WARM / COLD)
* Graceful failure handling
* Clean separation of concerns
* Environment-secured API keys
* Production-minded error handling

### Architecture

```
main.py                → CLI orchestration
openai_client.py       → API integration
prompt_templates.py    → Structured prompt builder
validate_classification() → Output validation boundary
```

Shifted from:

> “LLM decides.”

To:

> “LLM output validated and controlled inside deterministic system logic.”

---

## Engineering Principles

* Failure-path validation (not just success path)
* No premature abstraction
* No framework bloat
* Controlled scope per build
* Versioned, testable increments
* Real API usage (no mocks)

---

## Status

Day 1 — OpenAI integration
Day 2 — Deterministic validation boundary

System shipped and version-controlled.

---

## Roadmap

* Hybrid AI + deterministic decision engines
* Lead qualification systems
* Document intelligence tools
* RAG systems
* Production deployment workflows
* Drift monitoring & audit layers

---

## Author

Rainiel Jhon Cantare
AI Engineer in Transition — Philippines

---
