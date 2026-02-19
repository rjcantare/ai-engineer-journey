# AI Engineer Journey
Building production-ready AI systems, automations, and tools.

---

## About

This repository documents my transition into becoming a Remote AI Engineer.

Focus areas:

- Python engineering
- OpenAI API integrations
- AI automation systems
- Production-ready architecture
- Clean code & Git discipline
- Prompt engineering systems

This is not a tutorial repo.
This is a build log of shipped systems.

---

## Repository Structure
ai-engineer-journey/
│
├── experiments/ # Sandbox testing & quick prototypes
├── projects/ # Production-structured builds
│ ├── 01-ai-chat-cli/ # OpenAI CLI Financial Classifier (Completed)
│ ├── 02-lead-qualifier-api/
│ ├── 03-pdf-extractor/
│ └── 04-rag-chatbot/
│
├── notes/ # Technical notes & documentation
├── README.md
└── .gitignore


---

## Completed Builds

### 01 – OpenAI CLI Financial Classifier

**Description:**  
A structured CLI tool that integrates with the OpenAI API to classify financial stability.

**Features:**
- CLI input collection
- Structured prompt architecture
- OpenAI API integration
- Environment variable security (.env)
- Clean module separation
- Git-safe secret handling

**Architecture:**
main.py → CLI logic
openai_client.py → API integration layer
prompt_templates.py → Prompt builder
.env → Secret management


**Example Output:**
Status: ✅ Shipped

---

## Environment
- Python 3.11
- Git
- VS Code
- Windows

---

## Engineering Principles Applied
- Strict scope control
- Single-responsibility file separation
- No premature abstraction
- No framework overuse
- Secure credential handling
- Clean Git commits
- Real API usage (not mock)

---

## Current Status
Day 1 — First OpenAI API integration completed  
System shipped and versioned

---

## Roadmap Direction
This repository will progressively include:

- Lead qualification AI systems
- Automation pipelines
- Document intelligence tools
- RAG-based systems
- Production deployment workflows

Each project will follow:
- Clean architecture
- Clear separation of concerns
- Security best practices
- Commit discipline

---

## Author
Rainiel Jhon Cantare  
AI Engineer in Transition  
Philippines