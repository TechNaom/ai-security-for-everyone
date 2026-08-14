# Changelog

All notable changes to this course are logged here, newest first.

## 2026-08-14 — Chapter 13 built, Module 6 complete: the course is finished

- Chapter 13 ("Capstone: Security Architecture for a Real LLM System,"
  Module 6, Architect) built and live — the final chapter, closing the
  course. All 13 chapters across all 6 modules are now live.
- Deliberately breaks every prior chapter's incident-first hook pattern:
  no incident, a pure business-problem brief (Cinderpeak Systems' Aegis
  Copilot, a multi-tenant AI workflow platform, 8 weeks from GA with no
  major incident) — the skill taught is designing defenses before a
  failure exists to diagnose, per the L4 Architecture Challenge's
  "business problem only" requirement.
- Full OWASP GenAI LLM Top 10 2026 (all ten categories, LLM01-LLM10)
  mapped to this course's arsenal for the first time — re-verified live
  this session that the ranking is unchanged since Chapter 12 shipped.
  Honestly names two categories (LLM06 Unbounded Consumption, LLM07
  Misinformation) this course never built a dedicated chapter for,
  applying Chapter 5's honest-limits discipline to the course's own
  coverage.
- Teaches Architecture Decision Records, requiring every ADR to be
  tagged with Chapter 5's structural/detection/consequence-bounding
  defense taxonomy and to state a real, honestly-priced trade-off — with
  a full worked example in `lesson.html`.
- Full worked trade-off example on when sandboxing (referencing
  `mcp-for-everyone` and `ai-coding-agents-for-everyone`'s own
  agent-sandboxing depth) is the right call versus overkill, comparing
  Aegis Copilot's first-party tools against its third-party plugin
  marketplace.
- Project is the course's fourth and final project tier, the **L4
  Architecture Challenge** (`project/RUBRIC.md`, six criteria, 24
  points): a threat model across all ten OWASP 2026 categories, six
  required ADRs, a self-directed red-team pass against the learner's own
  design (using Chapter 11's methodology), and a prioritized launch
  recommendation. `project/solution.py` deliberately leaves the launch-
  recommendation criterion incomplete, following Chapter 11's own
  precedent.
- 8 exercises (5 production-gear, new scenario: Grantham Municipal
  Services/CivicAssist), 8 practice scenarios (8 new fictional orgs), 8
  interview questions across all 4 levels, weighted toward
  senior/architect depth appropriate to the course's only Architect-tier
  chapter.
- Ollama checked fresh this session: `/api/tags` OK, `/api/chat` timed
  out after a 20-second timeout (exit code 28) — same persistent hang as
  every prior chapter since Chapter 3; disclosed honestly, and noted as
  not load-bearing for this chapter's deliverable (a design task, not a
  live-generation task).
- `index.html` and `docs/curriculum/index.html` updated to reflect the
  finished course (13/13 chapters live, 6/6 modules complete),
  matching the completion pattern used by `mcp-for-everyone` and
  `ai-coding-agents-for-everyone`.
- See `quality-audits/chapter-13-audit.md` for full detail.

## 2026-08-14 — Chapter 12 built, Module 5 complete

- Chapter 12 ("Handling LLM Output Safely: PII and Downstream Injection
  Risk," Module 5, Advanced) built and live, closing Module 5 — the
  *output* side of LLM risk (PII/sensitive-data leakage in generated
  text, downstream injection risk carried FROM generated content),
  explicitly the inversion of Modules 2 and 4's input-side focus.
- Verified live: the OWASP GenAI LLM Top 10 2026 shipped August 4, 2026
  (genai.owasp.org), confirming the edition Chapter 11's research had
  flagged but not confirmed. LLM02:2026 Sensitive Information Disclosure
  holds its #2 rank; Improper Output Handling moved from LLM05:2025 to
  LLM10:2026 with expanded scope. This course uses 2026 numbering from
  this chapter forward.
- New fictional org (Fenwick Customer Experience / TicketSense) and hook
  ("two bad Tuesdays": a PII leak into a cross-team export, and a
  paraphrased HTML-injection payload rendered unescaped in an internal
  dashboard).
- Project is a find-and-fix defense lab (`project/RUBRIC.md`,
  `project/starter.py`, `project/solution.py`) against TicketSense,
  implementing PII redaction, HTML output encoding, and allow-list URL
  validation — a deliberate departure from Chapter 11's findings-report
  shape, justified in `lesson.html` and `project/README.md`.
- 8 exercises (5 production-gear), 8 practice scenarios (8 new fictional
  orgs), 8 interview questions across all 4 levels.
- Module 5 written-exam decision resolved: no separate written exam —
  Chapter 11's project alone satisfies the curriculum map's stated
  Module 5 assessment type. `assets/chapters-data.js` Module 5
  `examPath` confirmed `null`.
- `index.html` and `docs/curriculum/index.html` updated to reflect
  Chapter 12 and Module 5's completion.
- See `quality-audits/chapter-12-audit.md` for full detail.

## 2026-08-10 — Repository scaffolded

- Discovery completed: course vision, 4 personas, prerequisites,
  learning outcomes, 6-module/13-chapter structure, project ladder
  (L1-L4), capstone shape, cross-course overlap check confirmed no
  duplication with `mcp-for-everyone`, `ai-coding-agents-for-everyone`,
  `genai-for-everyone`, or `rag-for-everyone`.
- `docs/curriculum/CURRICULUM_MAP.md` and `docs/course-architecture.md`
  written.
- Repository structure scaffolded from `ai-coding-agents-for-everyone`
  (structure only — no content reused): directories with `.gitkeep`
  from the start, shared `assets/` rebranded (`AISFE_MODULES`,
  `AISFEProgress`, `aisfe-progress`), `templates/` (including
  `written-exam.template.html` from day one), CI
  (`.github/workflows/ci.yml`, `scripts/local_check.sh`) already
  including the `practice/solution.py` coverage and `nullglob` fix that
  course needed to add after its own first real CI run.
- Model/API policy inherited directly from
  `ai-coding-agents-for-everyone`: `openai` client pointed at Ollama's
  local endpoint by default, documented hosted-provider-swap option.
- README.md, PROJECT_STATE.md, AI_HANDOFF.md, CONTRIBUTING.md,
  LICENSE/LICENSE-CONTENT written.
- No chapter content yet. Not yet pushed to GitHub — pending user
  confirmation to create the public repo.
