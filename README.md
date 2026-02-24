# AI Engineer Journey

Building production-ready AI systems with deterministic architecture and controlled LLM boundaries.

---

## 📌 About

This repository documents my transition into becoming a **Remote AI Engineer**.

**Focus:** Designing reliable AI systems — not just calling APIs.

The goal is to treat LLMs as probabilistic components inside deterministic systems.

---

## 🧠 Core Areas

- Python engineering  
- OpenAI API integrations  
- Deterministic LLM control  
- Structured output enforcement  
- Hybrid AI + rule-based engines  
- Token cost awareness  
- Clean architecture & Git discipline  
- Unit testing for business logic  

This is a build log of shipped systems — not tutorials.

---

## 🗂 Repository Structure

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

````

---

# 🚀 01 – OpenAI CLI Financial Classifier (Shipped)

A structured CLI tool integrating with the OpenAI API to classify financial stability.

---

## 🏗 Architectural Evolution

### Version 1 — Direct LLM Classification

LLM returned:

```json
{ "category": "...", "reason": "..." }
````

**Risk:**
Business logic lived inside the prompt.

* No deterministic enforcement
* No boundary control
* No regression safety

---

### Version 2 — Hybrid Architecture (Current)

LLM now returns structured features only:

```json
{
  "risk_score": int (0–100),
  "income_level": "low | medium | high",
  "dependency_load": "low | moderate | high",
  "savings_buffer": "low | moderate | high"
}
```

Python enforces classification deterministically:

```
>= 70  → HOT
40–69  → WARM
< 40   → COLD
```

LLM does **not** control:

* Final decision
* Explanation logic
* Boundary conditions
* Business thresholds

This creates a controlled hybrid system.

---

## 🧩 Current Architecture

```
main.py              → CLI orchestration
openai_client.py     → API integration (deterministic, usage-aware)
prompt_templates.py  → Strict JSON feature extraction contract
validate_features()  → Schema enforcement boundary
classify_risk()      → Deterministic decision engine
generate_reason()    → Deterministic explanation builder
test_classifier.py   → Deterministic unit test safety net
```

---

## 🔍 Engineering Highlights

* Deterministic temperature control (`temperature=0.0`)
* Strict JSON-only LLM contract
* Schema validation boundary
* Hybrid AI + deterministic rule engine
* Transparent feature-based explanations
* Token usage monitoring
* Boundary testing (69 vs 70 threshold protection)
* Built-in `unittest` regression suite
* Clean Git commit discipline
* No framework bloat
* Controlled scope iteration

---

## 🧪 Deterministic Testing Layer (Day 5)

Added unit tests using Python’s built-in `unittest` framework.

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

This ensures:

* Business logic is regression-safe
* Boundary errors are caught immediately
* Deterministic layer remains stable
* Tests run locally with:

```
python -m unittest
```

No pytest.
No CI.
No architectural refactor.

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
* Day 5 — Deterministic unit tests for classifier + validation

System shipped and version-controlled.

---

## 🛣 Roadmap

* Enum value enforcement (schema tightening)
* Full deterministic scoring engine (LLM-free scoring path)
* Lead qualification API
* RAG systems
* Deployment workflows
* Monitoring & drift detection
* Audit logging layer

---

## 👤 Author

**Rainiel Jhon Cantare**
AI Engineer in Transition — Philippines

Building layered, controlled AI systems.

