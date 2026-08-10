# AI Security for Everyone — Curriculum Map

LAST_REVIEWED: 2026-08-10

## Course Size

Focused emerging topic: 13 chapters, 4 projects (L1–L4), 1 capstone —
same sizing model as `mcp-for-everyone` and `ai-coding-agents-for-everyone`.

## Personas

- **AppSec engineer** — knows web/infra security, new to LLM-specific
  attack surface.
- **ML/AI engineer** — builds LLM features, has never done security
  work.
- **Red-teamer / pentester** — experienced in traditional pentesting,
  expanding into AI systems.
- **Engineering lead** — needs to threat-model an LLM feature or set
  team security standards for AI-assisted products.

## Prerequisites

- Comfortable with Python (`python-for-everyone` level).
- Soft prerequisite: `genai-for-everyone` (session 5.3, "Safety
  Fundamentals") for baseline vocabulary — this course goes deep where
  that course only introduced the concept.
- Soft prerequisite: `mcp-for-everyone` Module 5 (permission scoping,
  sandboxing, prompt injection via tool output) and
  `ai-coding-agents-for-everyone` Chapter 11 (agent sandboxing,
  permissions, destructive commands) — this course deepens both
  rather than re-teaching them. Link back, don't duplicate.

## Learning Outcomes

1. Threat-model an LLM-powered system using a structured framework
   (OWASP Top 10 for LLM Applications) rather than ad hoc worry.
2. Recognize, construct, and defend against direct and indirect prompt
   injection, including realistic jailbreak techniques.
3. Reason about data and model integrity: poisoning, extraction/theft,
   and supply-chain risk in models, weights, and dependencies.
4. Apply security thinking specifically to RAG pipelines and agentic
   systems, building on (not repeating) `rag-for-everyone` and
   `ai-coding-agents-for-everyone`.
5. Run a structured red-team exercise against an LLM system and
   produce a real findings report.
6. Handle LLM output safely — PII/sensitive-data leakage, and
   injection risks carried downstream (XSS/SSRF-style attacks via
   generated output).
7. Design and defend a security architecture for a full LLM system,
   with real trade-off reasoning (the capstone).

## Module Architecture

### Module 1 — Threat Modeling LLM Systems
**Purpose:** a structured way to think about LLM attack surface before
diving into any specific attack.
**Outcomes:** map an LLM system's attack surface; apply the OWASP Top
10 for LLM Applications as a working checklist, not trivia.
**Chapters:** 1, 2
**Labs:** threat-model a real, given LLM feature end to end
**Assessment:** concept + threat-modeling exercise

### Module 2 — Prompt Injection Deep Dive
**Purpose:** the single most consequential LLM-specific vulnerability
class, covered in real depth.
**Prerequisites:** Module 1
**Outcomes:** distinguish direct from indirect injection; construct
and defend against realistic jailbreak techniques; evaluate a defense
for what it actually stops vs. what it claims to stop.
**Chapters:** 3, 4, 5
**Labs:** build and then break a naive prompt-injection defense
**Assessment:** injection-construction + defense-evaluation exam

### Module 3 — Data & Model Integrity
**Purpose:** attacks on the model and its training/deployment pipeline,
not just its runtime inputs.
**Prerequisites:** Module 2
**Outcomes:** explain data poisoning and model extraction/theft
mechanically; assess supply-chain risk in model weights and
dependencies.
**Chapters:** 6, 7, 8
**Labs:** analyze a real (sanitized) supply-chain-risk scenario
**Assessment:** concept + risk-assessment exercise

### Module 4 — Securing RAG & Agentic Systems
**Purpose:** apply this course's depth to the two system shapes most
real LLM products actually take.
**Prerequisites:** Module 3
**Outcomes:** identify and mitigate injection risk carried through
retrieved documents; extend an agent's permission model against
adversarial tool output.
**Chapters:** 9, 10
**Labs:** find and fix an injection vector in a given RAG pipeline;
extend an agent's defenses against a malicious tool result
**Assessment:** applied security-review exercise

### Module 5 — Red-Teaming & Output Handling
**Purpose:** the practitioner half — running a real red-team exercise
and handling what an LLM outputs safely.
**Prerequisites:** Module 4
**Outcomes:** run a structured red-team methodology against a target
system; handle LLM output safely (PII leakage, downstream
injection risk in generated content).
**Chapters:** 11, 12
**Labs:** a full red-team exercise against a provided target, with a
real findings report
**Assessment:** red-team report graded against a rubric

### Module 6 — Capstone
**Purpose:** architect-level synthesis.
**Prerequisites:** Module 5
**Outcomes:** design and defend a security architecture for a
realistic LLM system, with real trade-off reasoning.
**Chapters:** 13
**Assessment:** capstone rubric (architecture challenge, Level 4)

## Chapter Roadmap

| # | Chapter | Module | Difficulty |
|---|---------|--------|------------|
| 1 | Threat Modeling LLM Systems: The OWASP Top 10 for LLM Applications | 1 | Beginner |
| 2 | Mapping the Attack Surface of a Real LLM Feature | 1 | Intermediate |
| 3 | Direct Prompt Injection | 2 | Intermediate |
| 4 | Indirect Prompt Injection and Jailbreaking Techniques | 2 | Advanced |
| 5 | Evaluating Prompt-Injection Defenses Honestly | 2 | Advanced |
| 6 | Data Poisoning | 3 | Advanced |
| 7 | Model Extraction and Theft | 3 | Advanced |
| 8 | Supply-Chain Risk: Weights, Dependencies, and Provenance | 3 | Advanced |
| 9 | Securing RAG Pipelines Against Injection | 4 | Advanced |
| 10 | Securing Agentic Systems Against Adversarial Tool Output | 4 | Advanced |
| 11 | Red-Teaming an LLM System: Methodology and Practice | 5 | Advanced |
| 12 | Handling LLM Output Safely: PII and Downstream Injection Risk | 5 | Advanced |
| 13 | Capstone: Security Architecture for a Real LLM System | 6 | Architect |

## Projects

- **L1 Guided** — Threat-model a real, given LLM feature end to end
  (ships after Ch. 2).
- **L2 Assisted** — Build and break a naive prompt-injection defense,
  partial scaffold (ships after Ch. 5).
- **L3 Independent** — Find and fix a real injection vector in a
  provided RAG pipeline or agent, no scaffold (ships after Ch. 10).
- **L4 Architecture Challenge** — Design a security architecture for a
  realistic LLM system, with a red-team report and full ADRs; business
  problem only (this is the capstone, Ch. 13).

## Cross-Course Links

- Builds on: `genai-for-everyone` (session 5.3 safety fundamentals),
  `mcp-for-everyone` (Module 5 security), `ai-coding-agents-for-everyone`
  (Chapter 11 agent security), `python-for-everyone` (baseline)
- Deepens (does not duplicate): `rag-for-everyone`'s context-injection
  and prompt-injection-safety material (Ch 19 and later chapters) —
  link back for RAG-pipeline specifics, this course adds the security
  practitioner's depth
- Feeds: future `AI Governance for Everyone` (compliance/regulatory
  framing, out of scope here — this course stays technical/red-team
  focused)
