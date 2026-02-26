
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

## Core Engineering Focus

* Python backend engineering
* OpenAI API integrations
* Deterministic LLM control
* Structured JSON enforcement
* Hybrid AI + rule-based systems
* Token cost awareness
* Clean architecture & Git discipline
* Unit testing for business logic

---

## Repository Structure

```bash
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

# 01 – OpenAI Financial Risk Classifier (Shipped)

A structured financial classification system integrating OpenAI inside deterministic boundaries.

Originally built as a CLI tool.
Now exposed via a minimal FastAPI service.

---

## Architectural Evolution

### Version 1 — Direct LLM Classification

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

### Version 2 — Hybrid Deterministic Architecture (Current)

LLM now returns structured features only:

```json
{
  "risk_score": 0-100,
  "income_level": "low | medium | high",
  "dependency_load": "low | moderate | high",
  "savings_buffer": "low | moderate | high"
}
```

Classification is enforced in Python:

```
risk_score >= 70   → HOT
risk_score 40–69   → WARM
risk_score < 40    → COLD
```

LLM does not control:

* Final decision
* Thresholds
* Boundary conditions
* Business rules

Result: Controlled hybrid AI system.

---

## Service Layer (FastAPI)

### Endpoint

```
POST /classify
```

### Request

```json
{
  "income": 50000,
  "dependents": 2,
  "savings": 100000
}
```

### Response

```json
{
  "category": "WARM",
  "risk_score": 58,
  "income_level": "medium",
  "dependency_load": "moderate",
  "savings_buffer": "moderate"
}
```

### Execution Flow

```
api.py
  ↓
run_classification_pipeline()
  ↓
LLM feature extraction
  ↓
validate_features()
  ↓
classify_risk()
  ↓
Structured JSON response
```

The API layer is intentionally thin.

No business logic inside endpoint.
No middleware.
No authentication.
No overengineering.

Transport adapter only.

---

## System Components

```
main.py              → CLI + pipeline orchestration
api.py               → FastAPI transport boundary
openai_client.py     → OpenAI integration
prompt_templates.py  → Strict JSON contract
validate_features()  → Schema enforcement
classify_risk()      → Deterministic decision engine
generate_reason()    → Deterministic explanation builder
test_classifier.py   → Regression safety net
```

---

## Engineering Highlights

* `temperature=0.0` for deterministic extraction
* Strict JSON-only LLM contract
* Schema validation boundary
* Hybrid AI + rule engine design
* Token usage tracking
* Threshold boundary tests (69 vs 70)
* Built-in `unittest` suite
* Linear Git rebase workflow
* Controlled scope iteration

---

## Deterministic Testing Layer

Unit tests protect:

### Classifier Boundaries

* `>= 70` → HOT
* `70` → HOT
* `69` → WARM
* `40` → WARM
* `39` → COLD

### Validation Failures

* Missing key
* Extra key
* Non-integer `risk_score`
* Out-of-range `risk_score`

Run locally:

```bash
python test_classifier.py
```

No pytest.
No CI.
No framework bloat.

---

## API Failure Mapping (Production Hygiene)

Controlled HTTP semantics:

* `200` → Success
* `422` → Validation error
* `503` → OpenAI dependency failure
* `500` → Unexpected internal error

No stack traces leaked.
No provider details exposed.
Business logic untouched.

---

## Engineering Principles

* LLMs interpret — code enforces
* Deterministic business rules
* Validate before execute
* Boundaries must be tested
* Auditability over cleverness
* No premature abstraction
* Small controlled iterations

---

## Progress Log

* Day 1 — OpenAI integration
* Day 2 — Strict JSON validation boundary
* Day 3 — Deterministic entropy control + token tracking
* Day 4 — Hybrid architecture refactor
* Day 5 — Deterministic unit tests
* Day 6 — FastAPI service layer
* Day 7 — Controlled API error handling

System shipped.
Version-controlled.
Deterministic core protected.

---

## Roadmap

* Enum enforcement (schema tightening)
* Deterministic scoring fallback (LLM-free mode)
* Lead qualification API
* RAG systems
* Deployment workflows
* Monitoring & drift detection
* CI pipeline

---

## Author

**Rainiel Jhon Cantare**
AI Engineer in Transition — Philippines

Building layered, controlled, production-aligned AI systems.

---
