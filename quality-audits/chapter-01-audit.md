# Chapter Quality Audit: Threat Modeling LLM Systems: The OWASP Top 10 for LLM Applications

## Summary

- Chapter: 1 — Threat Modeling LLM Systems: The OWASP Top 10 for LLM Applications (Module 1, Beginner)
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-11
- Status: Ready for human review
- Note: this is the first chapter audit ever written for this repo — no
  prior audit format existed here. This document's structure is adapted
  from `ai-coding-agents-for-everyone/quality-audits/chapter-01-audit.md`
  (structure only; no content reused) plus an added "Live-Tested vs.
  Logical-Only Content" section specific to this course's security
  framing requirements.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Story-first hook (GreenCart/Aurora return-fraud incident); mechanism explained in plain language before any framework vocabulary is introduced. |
| Production depth | Pass | Full walkthrough table maps concrete assets/data flows to OWASP categories with justified likelihood/impact reasoning and a specific architectural mitigation per row — not generic risk ratings. |
| Real-time framework accuracy | Pass | OWASP Top 10 for LLM Applications 2025 edition category names/IDs/order verified against `genai.owasp.org` (cited inline); reordering/new-categories claims (System Prompt Leakage, Vector and Embedding Weaknesses as new; Sensitive Info Disclosure moving to #2) stated as edition history, not asserted as tested behavior. |
| Architecture and diagrams | Pass | ASCII diagram contrasting a traditional web-app trust boundary with the LLM-system trust boundary the hook actually crossed. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 4 explicitly marked production-gear (access/permissions, risk evaluation, output-rendering safety, compliance completeness gate). Fresh scenario (PolicyPilot) distinct from the lesson's GreenCart/Aurora hook. Automated scoring harness; solution.py verified to score a perfect 31/31. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 6 distinct fictional systems, none reused from the lesson or exercises. Two are pure judgment calls (is a described process already sufficient; which of two real risks to prioritize) rather than keyword-matchable category recall. Automated scoring harness; solution.py verified to score a perfect 9/9. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), each with strong answer, red flag, follow-up, and "what this proves" — verified present for all 8 by direct grep of `interview-questions.md`. |
| Project implementation | Pass (scoped) | This chapter intentionally does not ship the L1 project — `CURRICULUM_MAP.md` states the L1 Guided project ("threat-model a real, given LLM feature end to end") ships after Chapter 2, which does not exist yet. `project/index.html` is a short, honest preview stating this and explaining what the real project will ask, matching the brevity/tone of `ai-coding-agents-for-everyone`'s Chapter 1 project preview page. `project/starter.py`/`solution.py`/`README.md` are minimal, honest placeholder scripts (no TODO scaffold, since there is nothing to build yet) that print the same preview message and execute cleanly. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: problem (vague "AI can be jailbroken" answers), assumption being made, what actually distinguishes a real threat model, why it matters before Chapter 2, and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson -> quiz -> exercises -> practice -> interview-questions -> project chain verified programmatically: every `href` across all 6 HTML files in this chapter folder resolves to a real file on disk (script-checked, zero broken links). `../../index.html` and `../../docs/curriculum/index.html` links verified to resolve to real files (both already exist in this repo, unlike some sibling courses at this build stage). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, diagram-figure); no invented CSS. |
| Public artifact readiness | Pass | No placeholder text (`local_check.sh`'s placeholder-text scan passed); all template `{{PLACEHOLDER}}` tokens replaced with original content. |

## Required Checks

- [x] Lesson starts with a problem, not jargon (GreenCart/Aurora return-fraud hook, full attacker-submitted payload shown as mechanism, not exploit-ready content against a real product).
- [x] Lesson includes: ethical framing section (why this course teaches attacks), a "what threat modeling means for an LLM system" conceptual section with a `what-is` box and ASCII trust-boundary diagram, all 10 OWASP Top 10:2025 categories covered (3 — Prompt Injection, Improper Output Handling, Excessive Agency — at real depth with "why this risk exists," "example," and "what real teams should check for" subsections; the other 7 with mechanism/example/check each), a full worked threat-model walkthrough table, a GenAI Builder Thought Process section, and Points to Remember.
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (4 present: tasks 3, 5, 6, 7).
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 6 distinct fictional systems).
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves.
- [x] Project includes a meaningful artifact appropriate to this chapter's position in the sequence: an honest, short preview of the L1 project and why it's gated until Chapter 2, per the curriculum map and explicit task instructions — not a premature/placeholder full project.
- [x] Chapter includes diagrams/visual-text architecture aids (ASCII trust-boundary diagram contrasting traditional vs. LLM-system threat modeling).
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought).
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file (script-checked with a Python link-walker against the filesystem; 0 broken links out of all `href` attributes scanned).
- [x] Content is original — no wording, examples, or structure reused from any sibling TechNaom repo; `ai-coding-agents-for-everyone` and `python-for-everyone` were consulted only for HTML/CSS class structure and file-pattern precedent, per the ecosystem's structural-reference convention.
- [x] Ethical framing constraint honored throughout: every OWASP category is presented with a defensive mechanism/mitigation, never as an unsolved problem; no ready-to-use exploit content targets a named real-world product (GreenCart, Aurora, PolicyPilot, TicketTriage, SummarizeBot, CodeReviewBot, QuickChat, PluginMarket, ResearchAssistant, InsightsRAG, FieldServiceBot are all explicitly fictional, stated as such in the lesson and exercise/practice text).
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: OWASP category names/IDs, module/chapter titles, "Level 1, Guided" project naming, and the "L1 project ships after Ch. 2" fact all match verbatim.
- [x] `assets/chapters-data.js` updated: chapter-01 entry now has `path: "chapters/chapter-01-threat-modeling-llm-systems-owasp-top-10/lesson.html"`. Module 1's `examPath` left `null` (no written exam exists yet). No other part of the file touched.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter (6 files: exercises/starter.py, exercises/solution.py, practice/starter.py, practice/solution.py, project/starter.py, project/solution.py) — all compile cleanly.
- [x] Every `solution.py` in this chapter actually executed: `exercises/solution.py` scores 31/31, `practice/solution.py` scores 9/9, `project/solution.py` prints its preview message cleanly with exit code 0.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output: "All local checks passed. Safe to push."

## Live-Tested vs. Logical-Only Content Disclosure

This chapter is fully conceptual (Module 1, no live-model dependency, per
`PROJECT_STATE.md` and `AI_HANDOFF.md`), so almost nothing in it makes a
claim about a specific model's runtime behavior under a specific attack —
the kind of claim that `course-architecture.md`'s "verify before writing"
rule is really aimed at. Breaking down what was and wasn't tested:

- **OWASP Top 10 for LLM Applications 2025 framework claims** (category
  names, IDs, order, which categories are new/reordered in the 2025
  edition vs. earlier editions) — **live-checked**, not logical-only:
  verified against the framework's own published source
  (`genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/`)
  during authoring, not recalled from training data or asserted from
  memory.
- **GreenCart/Aurora hook, walkthrough table, and all fictional-system
  scenarios in exercises/practice** (TicketTriage, SummarizeBot,
  CodeReviewBot, QuickChat, PluginMarket, ResearchAssistant, InsightsRAG,
  FieldServiceBot, PolicyPilot) — **logical-only by design, not a live
  model claim**. These are original, fictional systems used to teach the
  *mechanism* of each OWASP category (why the risk exists, given how
  LLMs actually work) and its mitigation. No claim is made or implied
  that a specific installed model was tested against a specific attack
  string in this chapter — that live-testing discipline is reserved for
  Chapter 3 onward (Module 2, Prompt Injection Deep Dive), which is
  explicitly gated on verifying Ollama's current model behavior first,
  per `AI_HANDOFF.md`'s "Current task" section. Chapter 1 deliberately
  stays at the level of "this is the mechanism and this is the
  architectural fix," not "here is a transcript proving model X does Y."
- **All Python exercise/practice/project code** — **live-executed**, not
  logical-only: every `solution.py` was run directly (not just
  `py_compile`-checked) and its printed score verified to match the
  claimed perfect score before this audit was written.
- **All internal navigation links** — **live-checked**, not
  logical-only: verified with a filesystem-walking script against the
  actual repo tree, not assumed correct from template conventions.
- **No hosted-provider or Ollama API calls exist anywhere in this
  chapter's code** — correctly so, since Module 1 has no live-model
  dependency per the course's own architecture decision; nothing in this
  chapter needed to touch the model/API policy described in
  `docs/course-architecture.md`.

## Follow-Up Tasks

- Human review of tone/pacing, and of whether GreenCart's incident
  severity (full-batch refund redirection) reads as plausible rather
  than exaggerated, before considering this chapter final.
- When Chapter 2 is built, revisit `project/index.html`'s description of
  the L1 project to make sure it still matches the real project spec
  exactly, and replace `project/starter.py`/`solution.py`/`README.md`
  with the real L1 project scaffold at that point.
- When Chapter 2 exists, consider adding a forward link from this
  chapter's "Points to Remember" (currently references Chapter 2 by name
  only, no link, since that page doesn't exist yet — adding a link now
  would 404).
- This audit's OWASP 2025-edition claims should be re-verified if this
  chapter is revised significantly after the framework itself is next
  updated upstream (OWASP has revised this list more than once already).
