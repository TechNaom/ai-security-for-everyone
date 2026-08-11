# Chapter Quality Audit: Mapping the Attack Surface of a Real LLM Feature

## Summary

- Chapter: 2 — Mapping the Attack Surface of a Real LLM Feature (Module 1, Intermediate)
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-11
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-01-audit.md`
  (structure only; no content reused). This chapter also ships Module 1's
  real Level 1 (Guided) project, per `docs/curriculum/CURRICULUM_MAP.md`
  ("threat-model a real, given LLM feature end to end," ships after
  Ch. 2) — Chapter 1's `project/index.html` was an intentional preview
  page pointing here; this chapter builds the real deliverable.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook frames the real problem this chapter solves (being handed an undocumented system to audit, not a pre-mapped story); builds directly on Chapter 1's GreenCart/OWASP framework by name before introducing anything new. |
| Production depth | Pass | Goes beyond Chapter 1's single walkthrough: a seven-step, explicitly repeatable enumeration method (tool inventory, context-source inventory, trust classification, cross-reference, tool-output re-check, full-category cross-reference, table), applied step-by-step to Waypoint before the final table, plus two named, mechanism-explained common mistakes. |
| Real-time framework accuracy | Pass | Reuses Chapter 1's already-verified OWASP Top 10 for LLM Applications 2025-edition category names/IDs verbatim (LLM01–LLM10) — no new framework claims introduced that would need independent verification. |
| Architecture and diagrams | Pass | Waypoint's tool-inventory doc rendered as a `code-window`, functioning as the system diagram/description the task required; a full asset table (Section 5) makes the enumeration's output visually explicit before the threat-model table. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — access/permissions, risk evaluation, output-rendering safety, cost controls, compliance completeness gate. Fresh scenario (ReviewMate, an internal code-review assistant) distinct from the lesson's Waypoint and Chapter 1's GreenCart/PolicyPilot. Automated scoring harness; `solution.py` verified to score a perfect 31/31. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson, exercises, or Chapter 1. Two are pure judgment calls (VendorGate: is a described vetting process already sufficient; LegalAssist: which of two real risks to prioritize). Two scenarios (MarketWatch, WarehouseBot) are built specifically to test this chapter's core lesson — recognizing a tool's output, not just user input, as a Prompt Injection channel. Automated scoring harness; `solution.py` verified to score a perfect 9/9. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), each with strong answer, red flag, follow-up, and "what this proves" — verified present for all 8 by direct reading of `interview-questions.md`/`.html`. Questions are built around this chapter's specific content (the method's steps, the two named mistakes, Waypoint-specific category distinctions) rather than re-asking Chapter 1's questions. |
| Project implementation | Pass | Ships the real Module 1 Level 1 (Guided) project, per the curriculum map: a fourth, genuinely new scenario (AskHR, an internal HR chatbot with employee-record access) with no worked answer available while the learner works. `starter.py` is a structural validator (not a keyword-matched answer key) covering tool inventory, context-source/trust classification, and the full threat-model table, since the project is intentionally open-ended. `solution.py` is a complete worked reference, verified to cover all 10 OWASP categories and pass its own validator with zero issues. `project/README.md` and `project/index.html` both state clearly what "done" (a structural pass) does and does not certify. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: problem (finding one real vulnerability and stopping), assumption being made, what actually distinguishes a systematic pass, why this matters for the L1 project specifically, and a working definition of enumeration-completeness carried forward. |
| Navigation/template consistency | Pass | lesson -> quiz -> exercises -> practice -> interview-questions -> project chain verified programmatically: every `href`/`src` across all 6 HTML files in this chapter folder resolves to a real file on disk (script-checked with a Python link-walker against the filesystem, zero broken links). `../../index.html` and `../../docs/curriculum/index.html` links verified to resolve — this repo's root `index.html` and `docs/curriculum/index.html` already exist, so these are real resolutions, not expected-missing placeholders. |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic); no invented CSS, same as Chapter 1. |
| Public artifact readiness | Pass | No placeholder text (`local_check.sh`'s placeholder-text scan passed); all content is original — no wording, examples, or structure reused from Chapter 1 or any sibling TechNaom repo. |

## Required Checks

- [x] Lesson starts with a problem, not jargon (being handed a real, undocumented-beyond-a-tool-list LLM feature to audit, contrasted directly against how neatly Chapter 1's GreenCart hook was pre-mapped).
- [x] Lesson explicitly recaps (not re-derives) Chapter 1's OWASP Top 10 framework and trust-boundary concept, then introduces a new, different scenario (Waypoint, a trip-planning assistant with booking/payment tools — genuinely different in shape from GreenCart's return-triage batch job: multi-turn conversation, five tools, a RAG pipeline, a partner-data integration, a payment path).
- [x] Lesson includes a systematic, seven-step, explicitly repeatable method for attack-surface enumeration (tool inventory; context-source inventory; trust classification; cross-reference untrusted sources against tools with side effects; explicit re-check of tool outputs; full ten-category cross-reference; final table) — more procedural than Chapter 1's single walkthrough, as required.
- [x] Lesson includes two named common mistakes, each with a concrete Waypoint-specific example and a "why it happens" explanation: Mistake 1 (under-scoping — missing that a tool's own output re-enters context as untrusted data) and Mistake 2 (over-focusing on Prompt Injection and missing an equally real Unbounded Consumption/Supply Chain gap).
- [x] Lesson includes a full, worked threat model for Waypoint that is at least as thorough as Chapter 1's GreenCart table — Chapter 1's table has 5 rows across 4 categories; this chapter's table has 10 rows spanning all 10 OWASP categories, explicitly built via the systematic method rather than ad hoc.
- [x] Lesson includes a GenAI Builder Thought Process section and Points to Remember recap, matching Chapter 1's pattern.
- [x] Interview-questions callout box is present on `lesson.html` (linking to `interview-questions.html`) — verified present.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`) is present on `lesson.html` and `interview-questions.html` (the two pages carrying it in Chapter 1's own pattern) — verified present in both files by direct read, matching Chapter 1's convention (quiz/exercises/practice/project pages in Chapter 1 do not carry the footer GitHub link either; Chapter 2 matches this exactly).
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (5 present: tasks 3, 5, 6, 7, 8).
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 8 distinct fictional systems).
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves.
- [x] Project ships the real Module 1 Level 1 (Guided) deliverable: a fourth, genuinely new scenario (AskHR), a structural-validator starter scaffold appropriate to an open-ended threat-modeling task, a complete worked `solution.py` covering all 10 OWASP categories, and a `README.md` explaining the task and what "done" (a structural pass, not a content match) means.
- [x] Chapter includes diagrams/visual-text architecture aids (Waypoint's tool-inventory `code-window`, and the intermediate asset table in Section 5 making the enumeration's output explicit before risk analysis begins).
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought).
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file (script-checked; 0 broken links out of all `href`/`src` attributes scanned).
- [x] Content is original — no wording, examples, or structure reused from Chapter 1 or any sibling TechNaom repo; Chapter 1's own HTML/CSS class structure and file-pattern precedent were the only things consulted, per the ecosystem's structural-reference convention. Waypoint, ReviewMate, AskHR, and all eight practice-bank scenario systems (ClaimsBot, MarketWatch, DocSummarizer, RecommendAI, OpsChat, VendorGate, LegalAssist, WarehouseBot) are original and explicitly fictional.
- [x] Every attack/vulnerability discussed is framed defensively: every OWASP category finding in every table (lesson, exercises, practice, project) is paired with a concrete architectural mitigation; no example is presented as unsolved; no content targets a named real-world product — every scenario is stated as fictional (Waypoint Travel, ReviewMate, AskHR, and the eight practice-bank systems are all explicitly invented).
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: OWASP category names/IDs match Chapter 1 verbatim, "Level 1, Guided" project naming matches, and the chapter's position (Module 1, Intermediate, completes Module 1) matches the roadmap table exactly.
- [x] `assets/chapters-data.js` updated: chapter-02 entry now has `path: "chapters/chapter-02-mapping-the-attack-surface-of-a-real-llm-feature/lesson.html"`. Module 1's `examPath` left `null` — the curriculum map states Module 1's assessment type is "concept + threat-modeling exercise," which this chapter's exercises/practice bank and the real L1 project satisfy; no separate written-exam file exists or was called for. No other part of the file touched (Chapter 1's entry and all other modules/chapters left exactly as they were).
- [x] `python3 -m py_compile` run on every `.py` file in this chapter (6 files: `exercises/starter.py`, `exercises/solution.py`, `practice/starter.py`, `practice/solution.py`, `project/starter.py`, `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py` in this chapter actually executed: `exercises/solution.py` scores 31/31, `practice/solution.py` scores 9/9, `project/solution.py` passes its own structural validator with zero issues and reports coverage of all 10/10 OWASP categories. Both `starter.py` files (exercises, practice) were also run directly and confirmed to execute cleanly with a 0/N score report (expected, since their TODOs are unfilled by design) rather than crashing. `project/starter.py` was also run directly and confirmed to report its 5 expected structural gaps cleanly rather than crashing.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output ended with "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a standalone Python link-walker script (not just `local_check.sh`'s chapter-path check) across all 6 HTML files in this chapter folder: 0 broken `href`/`src` targets.

## Live-Tested vs. Logical-Only Content Disclosure

This chapter is fully conceptual (Module 1, no live-model dependency, per
`PROJECT_STATE.md` and `AI_HANDOFF.md`), the same as Chapter 1. Breaking
down what was and wasn't tested:

- **OWASP Top 10 for LLM Applications 2025 framework claims** (category
  names, IDs, order) — **inherited, not independently re-verified in this
  chapter's authoring session.** This chapter reuses Chapter 1's already
  live-checked category names/IDs verbatim and introduces no new claims
  about the framework's edition history, current ranking, or upstream
  source — it only applies the already-verified list to new scenarios.
  No new OWASP-framework research claim originates in this chapter.
- **Waypoint, ReviewMate, AskHR, and all practice-bank fictional
  systems** (ClaimsBot, MarketWatch, DocSummarizer, RecommendAI, OpsChat,
  VendorGate, LegalAssist, WarehouseBot) — **logical-only by design, not
  a live model claim.** These are original, fictional systems used to
  teach the systematic enumeration *method* and its application against
  the framework — mechanism and mitigation reasoning, not a claim that a
  specific installed model was tested against a specific attack string.
  That live-testing discipline is reserved for Chapter 3 onward (Module
  2, Prompt Injection Deep Dive), per `AI_HANDOFF.md`'s explicit gating
  on verifying Ollama's current model behavior first before any chapter
  demonstrates an attack against a real, installed model.
- **The seven-step attack-surface-mapping method itself** — **a
  process/methodology claim, not an empirical one.** It is presented as
  a repeatable procedure for security review work (analogous to a
  checklist or audit methodology), not as a claim about any model's
  behavior — it needs no live-model verification, the same way Chapter
  1's threat-modeling walkthrough format didn't.
- **All Python exercise/practice/project code** — **live-executed, not
  logical-only.** Every `solution.py` was run directly (not just
  `py_compile`-checked) and its printed output verified to match the
  claims in this audit (31/31, 9/9, 10/10-category coverage with zero
  validator issues) before this audit was written. Both `starter.py`
  files with scorable answers, and `project/starter.py`, were also run
  directly to confirm they execute cleanly and report the expected
  "incomplete" state rather than crashing.
- **All internal navigation links** — **live-checked, not logical-only:**
  verified twice — once via `scripts/local_check.sh`'s JS-driven
  chapter-path check, and once via a standalone Python filesystem-walking
  script scanning every `href`/`src` in all 6 HTML files directly — not
  assumed correct from template conventions.
- **No hosted-provider or Ollama API calls exist anywhere in this
  chapter's code** — correctly so, since Module 1 has no live-model
  dependency per the course's own architecture decision; nothing in this
  chapter needed to touch the model/API policy described in
  `docs/course-architecture.md`.

## Follow-Up Tasks

- Human review of Waypoint's threat-model table (10 rows, all 10
  categories) for whether the density reads as thorough-and-earned
  rather than padded — the chapter's own text explicitly acknowledges
  the systematic method, not extra cleverness, is what surfaced the less
  obvious rows; a reviewer should sanity-check that framing holds up.
- Human review of the AskHR project's validator thresholds
  (`MIN_TOOLS=4`, `MIN_CONTEXT_SOURCES=5`, `MIN_THREAT_ROWS=6`,
  `MIN_DISTINCT_CATEGORIES=6`, length-based substance checks) for whether
  they strike the right balance between "enforces real completeness" and
  "achievable by a learner working independently within the project's
  ~90-minute estimate" — these were set to be comfortably below what the
  reference solution achieves (4 tools, 6 sources, 10 rows, 10
  categories) so a strong-but-not-maximal learner submission still
  passes.
- With Module 1 now complete (Chapters 1–2), the next task per
  `AI_HANDOFF.md` is Module 2 (Chapter 3, Direct Prompt Injection) —
  gated on first verifying Ollama's current model recommendation and its
  actual behavior under injection/jailbreak testing, since Chapter 3 is
  the first chapter in this course with a live-model dependency.
- This audit's inherited OWASP 2025-edition claims should be re-verified
  at the source (`genai.owasp.org`) if either Chapter 1 or Chapter 2 is
  revised significantly after the framework itself is next updated
  upstream.
