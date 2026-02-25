# AI Engineer Journey

Building production-ready AI systems with deterministic architecture and controlled LLM boundaries.

---

## 📌 About

This repository documents my transition into becoming a **Remote AI Engineer**.

**Focus:** Designing reliable AI systems — not just calling APIs.

The goal is to treat LLMs as probabilistic components inside deterministic systems.

---

## 🧠 Core Areas

* Python engineering
* OpenAI API integrations
* Deterministic LLM control
* Structured output enforcement
* Hybrid AI + rule-based engines
* Token cost awareness
* Clean architecture & Git discipline
* Unit testing for business logic

This is a build log of shipped systems — not tutorials.

---

## 🗂 Repository Structure

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

# 🚀 01 – OpenAI Financial Risk Classifier (Shipped)

A structured financial classification system integrating the OpenAI API within deterministic boundaries.

Initially built as a CLI tool.
Now exposed as a minimal FastAPI service.

---

## 🏗 Architectural Evolution

---

### Version 1 — Direct LLM Classification

LLM returned:

```json
{
  "category": "...",
  "reason": "..."
}
```

**Risk:**
Business logic lived inside the prompt.

* No deterministic enforcement
* No boundary control
* No regression safety

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

Python enforces classification deterministically:

```text
risk_score >= 70   → HOT
risk_score 40–69   → WARM
risk_score < 40    → COLD
```

LLM does **not** control:

* Final decision
* Explanation logic
* Boundary conditions
* Business thresholds

This creates a controlled hybrid AI system.

---

## 🌐 Version 3 — Service Layer (Day 6)

The CLI system is now wrapped with a minimal FastAPI service.

### Endpoint

```http
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

### API Architecture

```text
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

* No business logic inside endpoint
* No database
* No middleware
* No authentication
* No async refactor
* No overengineering

Just a transport adapter.

---

## 🧩 Current System Components

```text
main.py              → CLI + pipeline orchestration
api.py               → FastAPI transport layer
openai_client.py     → OpenAI API integration (usage-aware)
prompt_templates.py  → Strict JSON feature extraction contract
validate_features()  → Schema enforcement boundary
classify_risk()      → Deterministic decision engine
generate_reason()    → Deterministic explanation builder
test_classifier.py   → Deterministic regression safety net
```

---

## 🔍 Engineering Highlights

* Deterministic temperature control (`temperature=0.0`)
* Strict JSON-only LLM contract
* Schema validation boundary
* Hybrid AI + deterministic rule engine
* Transparent feature-based reasoning
* Token usage monitoring
* Threshold protection testing (69 vs 70)
* Built-in `unittest` regression suite
* Clean Git commit discipline
* Linear rebase workflow
* No framework bloat
* Controlled scope iteration

---

## 🧪 Deterministic Testing Layer (Day 5)

Unit tests implemented using Python’s built-in `unittest`.

### Protected Logic

**Classifier Boundary Tests**

* `risk_score >= 70` → HOT
* `risk_score == 70` → HOT
* `risk_score == 69` → WARM
* `risk_score == 40` → WARM
* `risk_score == 39` → COLD

**Validation Failure Tests**

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
No architectural drift.

Strict scope discipline.

---

## 📐 Engineering Principles

* LLMs interpret — code enforces
* Business rules must be deterministic
* Validation before execution
* Boundary testing matters
* Auditability over cleverness
* No premature abstraction
* Production-aligned iteration
* Small controlled improvements

---

## 📅 Progress Log

* Day 1 — OpenAI integration
* Day 2 — Strict JSON validation boundary
* Day 3 — Deterministic entropy control + token tracking
* Day 4 — Hybrid architecture refactor (LLM extraction + rule engine)
* Day 5 — Deterministic unit tests (classifier + validation)
* Day 6 — FastAPI service layer (CLI → API transition)

System shipped.
Version-controlled.
Deterministic core protected.

---

## 🛣 Roadmap

* Enum value enforcement (schema tightening)
* Fully deterministic scoring engine (LLM-free fallback path)
* Lead qualification API
* RAG systems
* Deployment workflows
* Monitoring & drift detection
* Audit logging layer
* Production CI pipeline

---

## 👤 Author

**Rainiel Jhon Cantare**
AI Engineer in Transition — Philippines

Building layered, controlled, production-aligned AI systems.

---
