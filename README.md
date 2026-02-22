# AI Engineer Journey

Building production-ready AI systems with deterministic architecture and controlled LLM boundaries.

---

## About

This repository documents my transition into becoming a Remote AI Engineer.

**Focus:** Designing reliable AI systems — not just calling APIs.

The goal is to treat LLMs as probabilistic components inside deterministic systems.

---

## Core Areas

* Python engineering
* OpenAI API integrations
* Deterministic LLM control
* Structured output enforcement
* Hybrid AI + rule-based engines
* Token cost awareness
* Clean architecture & Git discipline

This is a build log of shipped systems.

---

## Repository Structure

```
ai-engineer-journey/
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

# 01 – OpenAI CLI Financial Classifier (Shipped)

A structured CLI tool integrating with the OpenAI API to classify financial stability.

---

## Architectural Evolution

### Version 1 — Direct LLM Classification

LLM returned:

```
{ "category": "...", "reason": "..." }
```

Risk:
Business logic lived inside prompt.

---

### Version 2 — Hybrid Architecture (Current)

LLM now returns structured features only:

```
{
  "risk_score": int (0–100),
  "income_level": enum,
  "dependency_load": enum,
  "savings_buffer": enum
}
```

Python enforces classification deterministically:

```
>= 70 → HOT
40–69 → WARM
< 40 → COLD
```

LLM does not control:

* Final decision
* Explanation logic
* Boundary conditions

---

## Current Architecture

```
main.py              → CLI orchestration
openai_client.py     → API integration (deterministic, usage-aware)
prompt_templates.py  → Strict JSON feature extraction contract
validate_features()  → Schema enforcement boundary
classify_risk()      → Deterministic decision engine
generate_reason()    → Deterministic explanation builder
```

---

## Engineering Highlights

* Deterministic temperature control (`temperature=0.0`)
* Strict JSON-only LLM contract
* Schema validation boundary
* Hybrid AI + deterministic rule engine
* Transparent feature-based explanations
* Token usage monitoring
* Boundary testing (69 vs 70 threshold)
* Clean Git rebase workflow
* No framework bloat
* Controlled scope iteration

---

## Engineering Principles

* LLMs interpret — code enforces
* Business rules must be deterministic
* Validation before execution
* Boundary testing matters
* Auditability over cleverness
* No premature abstraction
* Production-aligned iteration

---

## Status

* Day 1 — OpenAI integration
* Day 2 — Strict JSON validation boundary
* Day 3 — Deterministic entropy control + token tracking
* Day 4 — Hybrid architecture refactor (LLM extraction + rule engine)

System shipped and version-controlled.

---

## Roadmap

* Unit tests for classifier boundary
* JSON schema enforcement
* Raw feature extraction scoring engine (full deterministic scoring)
* Lead qualification system
* RAG systems
* Deployment workflows
* Drift monitoring & audit layers

---

## Author

**Rainiel Jhon Cantare**
AI Engineer in Transition — Philippines

Building layered, controlled AI systems.
