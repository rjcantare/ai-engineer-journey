# AI Engineer Journey

Building production-ready AI systems with deterministic architecture and controlled LLM boundaries.

---

## About

This repository documents my transition into becoming a Remote AI Engineer.

**Focus:** Designing reliable AI systems — not just calling APIs.

### Core Areas

* Python engineering
* OpenAI API integrations
* Deterministic LLM control
* Structured output enforcement
* Token cost awareness
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

---

## Key Engineering Highlights

* Explicit deterministic temperature control (`temperature=0.0`)
* Strict JSON-only LLM contract
* Deterministic schema validation boundary
* Enum enforcement (`HOT`, `WARM`, `COLD`)
* Token usage tracking (prompt / completion / total)
* Cost-awareness testing
* Graceful failure handling
* Clean separation of concerns
* Environment-secured API keys
* Production-minded Git workflow

---

## Architecture

```
main.py                    → CLI orchestration
openai_client.py           → API integration (deterministic + usage-aware)
prompt_templates.py        → Structured prompt builder
validate_classification()  → Output validation boundary
```

Shifted from:

> “LLM decides.”

To:

> “LLM output validated, constrained, and monitored inside deterministic system logic.”

---

## Engineering Principles

* Failure-path validation (not just success path)
* Deterministic entropy control
* Token visibility for cost awareness
* No premature abstraction
* No framework bloat
* Controlled scope per build
* Versioned, testable increments
* Real API usage (no mocks)
* Clean Git hygiene (rebase over force push)

---

## Status

* Day 1 — OpenAI integration
* Day 2 — Strict validation boundary
* Day 3 — Deterministic behavior + token usage monitoring

System shipped and version-controlled.

---

## Roadmap

* Versioned prompt contracts
* Hybrid AI + deterministic decision engines
* Lead qualification systems
* Document intelligence tools
* RAG systems
* Production deployment workflows
* Drift monitoring & audit layers

---

## Author

**Rainiel Jhon Cantare**
AI Engineer in Transition — Philippines

Building layered, controlled AI systems.
