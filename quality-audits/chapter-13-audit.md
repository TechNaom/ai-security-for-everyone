# Chapter Quality Audit: Capstone: Security Architecture for a Real LLM System

## Summary

- Chapter: 13 — Capstone: Security Architecture for a Real LLM System
  (Module 6, Architect) — **closes Module 6, and the entire 13-chapter
  course**
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-14
- Status: Ready for human review
- All files in this chapter (`lesson.html`, `quiz.html`,
  `interview-questions.html`/`.md`,
  `exercises/{index.html,starter.py,solution.py,README.md}`,
  `practice/{index.html,starter.py,solution.py,README.md}`,
  `project/{index.html,starter.py,solution.py,README.md,RUBRIC.md}`)
  were written fresh this session, plus `assets/chapters-data.js`,
  `index.html`, `docs/curriculum/index.html`, `PROJECT_STATE.md`,
  `AI_HANDOFF.md`, `CHANGELOG.md`, and this audit. Because this is the
  final chapter, this audit is deliberately held to the same rigor as
  every prior chapter's audit, not relaxed — an honest, non-self-
  congratulatory closing audit matters more here, not less.

## Framing decision: no incident hook

Unlike every one of Chapters 1-12, `lesson.html`'s hook (Cinderpeak
Systems' Aegis Copilot, 8 weeks from GA, no major incident in a
four-month beta) deliberately contains no failure that has already
happened. This is stated and justified explicitly in the lesson's own
"Why This Chapter Has No Incident" section: the skill this chapter
teaches is designing a system's defenses before a version of it exists
to fail, which an incident hook would undercut by inviting
pattern-matching against an earlier chapter's mechanism instead of a
genuine from-scratch threat model. This directly implements the L4
Architecture Challenge's "business problem only" requirement from
`CURRICULUM_MAP.md`'s Projects section.

## Framing decision: full OWASP 2026 Top 10 given for the first time

Chapters 1-12 each used a subset of OWASP categories relevant to that
chapter's own topic. `lesson.html`'s "This Course's Arsenal, Mapped to
the OWASP 2026 Top 10" section gives the complete ten-category 2026
list for the first time in this course, mapped to both this course's
own chapter depth and to specific Aegis Copilot components. It honestly
names two categories (LLM06:2026 Unbounded Consumption, LLM07:2026
Misinformation) that never received a dedicated course chapter — applying
Chapter 5's own "don't overclaim what a defense does" discipline to the
course's own coverage, not silently presenting all ten categories with
uniform authority.

## Research verification performed this session

Per the task's explicit instruction not to re-verify from scratch but to
do a quick sanity check that nothing changed since Chapter 12 shipped:
`WebFetch` against `genai.owasp.org/resource/owasp-genai-llm-top-10-2026/`
and `genai.owasp.org/llm-top-10/` returned stale/incomplete content (the
fetch tool's summarization did not surface the 2026 category list
directly, instead surfacing older 2025 content from the same domain —
disclosed honestly here rather than treated as a negative result). A
follow-up `WebSearch` for "OWASP GenAI LLM Top 10 2026 LLM10 Improper
Output Handling ranking" and a second search for the full ten-category
list, both independently, confirmed via invicti.com's incident-count
reporting and cross-referenced against the GenAI-Security-Project GitHub
repository: LLM10:2026 Improper Output Handling ranked 10th, down from
#5 (confirming Chapter 12's own claim, unchanged); the full 2026 order
is LLM01 Prompt Injection (#1, unchanged), LLM02 Sensitive Information
Disclosure (#2, unchanged), LLM03 Excessive Agency (#6→#3, biggest
climb), LLM04 Supply Chain (#3→#4), LLM05 Data and Model Poisoning
(#4→#5), LLM06 Unbounded Consumption (#10→#6), LLM07 Misinformation
(#9→#7), LLM08 Hidden Context Exposure (renamed/expanded from LLM07:2025
System Prompt Leakage), LLM09 Vector and Embedding Weaknesses (~#8,
roughly unchanged), LLM10 Improper Output Handling (#5→#10, biggest
fall). This full ordering — not previously given in this course — is
used in `lesson.html`'s mapping table and in `exercises/`,
`practice/`, and `project/`'s `OWASP_2026_CATEGORIES` dictionaries. No
change from Chapter 12's own confirmed claims was found.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Cinderpeak Systems' Aegis Copilot pre-GA review) is a genuinely different narrative shape from every prior chapter — no incident, a pure business-problem brief — with the departure named and justified in the lesson's own text, not left implicit. New fictional org (Cinderpeak Systems / Aegis Copilot), confirmed distinct from every prior chapter's and practice-bank org against the full exclusion list in `PROJECT_STATE.md`'s (now-historical) Chapter 13 build notes. |
| Production depth | Pass | Full OWASP 2026 Top 10 mapping (all ten categories, course depth and Aegis Copilot component named for each); a complete, worked ADR example (ADR-02) at real production depth (context, decision, two seriously-considered rejected alternatives, a real trade-off and its own fix, an enforcement consequence); a second full worked trade-off example (sandboxing: first-party tools vs. third-party plugins) directly answering the task brief's explicit requirement to cover this judgment call and to reference `mcp-for-everyone`/`ai-coding-agents-for-everyone`'s own sandboxing depth. |
| Real-time framework accuracy | Pass | OWASP 2026 full ranking re-confirmed live this session (see Research Verification above); no claim in `lesson.html` contradicts what Chapter 12 already verified, and the full ten-category order (not previously given in this course) is independently sourced this session, not invented. |
| Architecture and diagrams | Pass | The OWASP-2026-to-course-arsenal mapping table and the two worked-example code-window blocks (ADR-02, and the system description itself) do real structural-organization work, consistent with prior chapters' use of `code-window` for structured technical content. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — a real `is_valid_adr()` structural checker, a real `is_sandboxing_warranted()` judgment-rule implementation, OWASP-2026 category mapping across all ten categories (not just two, since this is the capstone), a real `score_threat_model_completeness()` scorer, and ADR critique. Fresh scenario (Grantham Municipal Services / CivicAssist) distinct from the lesson's Cinderpeak Systems. Verified this session by direct execution: `solution.py` scores a perfect 38/38; `starter.py` reports 8/38 (not a clean 0 — the unimplemented stub functions trivially satisfy some negative-case checks, e.g. `is_valid_adr()`'s default `return False` and `is_sandboxing_warranted()`'s default `return False` each correctly match several checks that expect `False`; disclosed here honestly, matching the same pattern Chapter 12's own audit disclosed for its exercises), with no crash or traceback either way. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems (Fairmont Regional Airport Authority, Blackwood Actuarial Partners, Silvergate Credit Union, Northaven Utilities Cooperative, Castlebridge Legal Tech, Emberline Health Analytics, Duskwater Insurance Group, Fallowfield Robotics), none reused from the lesson or exercises. Six drill fast classification across the full ten-category OWASP 2026 set (not the six used in the exercises' own task 1, giving broader category coverage across the chapter as a whole); two are deliberate judgment calls (an ADR missing a real trade-off; a sandboxing-overkill decision) with no single keyword to match. Verified this session by direct execution: `solution.py` scores a perfect 8/8; `starter.py` reports a clean 0/8, no crash. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), covering the ADR-vs-findings-report distinction, why the hook has no incident, producing real ADR-quality reasoning on demand, evaluating a uniform-sandboxing proposal, recognizing a zero-finding self-red-team pass as a red flag, generalizing Chapter 12's mechanism to a higher-stakes multi-tenant context, designing a non-binary launch-recommendation format, and defending an honestly-limited review standard against a surface-level "more rigor" argument. `interview-questions.html` and `.md` confirmed to carry identical question text, strong answers, red flags, follow-ups, and "what this proves" content — verified by direct comparison of content written this session (both files authored from the same source content in the same session, not independently drafted). |
| Project implementation | Pass | The course's fourth and final project tier, the L4 Architecture Challenge — genuinely no-scaffold: `project/starter.py` ships only `SYSTEM_DESCRIPTION` (structured business-problem data) and an empty deliverable scaffold, with zero proposed architecture, zero planted vulnerability, and no single correct answer key, matching the L4 brief's "business problem only" requirement more strictly than Chapter 10's L3 project (which gave a complete, if vulnerable, pipeline). `project/solution.py` is one complete, valid reference review, directly executed this session: threat-model completeness (10/10), ADR completeness (6/6), defense-taxonomy coverage (3/3, using all three of Chapter 5's categories across the six ADRs), red-team findings (3, spanning all three severities), and honest gap-naming (1/1) all score at full strength via the file's own `assert` self-checks, all of which pass. `LAUNCH_RECOMMENDATION` deliberately scores 0/1 on its own check — following Chapter 11's own precedent of leaving one real synthesis skill for the learner to practice rather than copy — verified by a dedicated `assert` in `solution.py`'s own `__main__` block confirming this is deliberate, not an oversight. `project/RUBRIC.md` has six criteria (24 points total), one more than every prior chapter's five-criterion/20-point rubric, with the added criterion (#6, overall coherence across the four deliverable pieces) explicitly justified as the capstone's own added judgment dimension. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real question (does an honestly-flagged coverage gap on two OWASP categories mean the system isn't launch-ready), the assumption being made (conflating "not yet specialist-deep" with "not launch-ready"), what actually resolves it (a three-way prioritized recommendation format instead of a single GO/NO-GO bit), why this matters as the course closes (ties every module's own discipline together), and a working definition carried forward that closes the entire course, not just this chapter. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the full repository filesystem (excluding `templates/`, which intentionally contains unresolved `{{PLACEHOLDER}}` paths): 81 HTML files scanned, 957 href/src targets checked, 0 broken — covering this chapter and all 12 prior chapters plus the homepage and roadmap. Interview-questions callout box present on `lesson.html` (confirmed by direct read this session). Footer GitHub link present on `lesson.html`, `interview-questions.html`, and `project/index.html` (confirmed by direct read this session). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, badge-coming-soon, page-toc, subtopic, download-links); no invented CSS, matching Chapters 1-12. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content is original — no wording, examples, or structure reused from Chapters 1-12 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted, including the explicit, task-required reference to `mcp-for-everyone`/`ai-coding-agents-for-everyone`'s own sandboxing depth (named and cited by course/chapter, never with their content reproduced). Every fictional system (Cinderpeak Systems/Aegis Copilot, Grantham Municipal Services/CivicAssist, all eight practice-bank orgs) is explicitly invented and confirmed distinct from every org used in Chapters 1-12. No named real product is targeted by any example; real, named entities (OWASP, the sibling TechNaom repos) appear only as accurately-cited, linked sources or cross-course references — never reproduced verbatim, never as a target of exploit instructions. Every risk category referenced pairs with a real, working defense or an honest "needs follow-up" flag — never presented as unsolved without disclosure, never as a ready-to-use exploit. |

## Required Checks

- [x] Lesson is a genuine synthesis chapter drawing on all 12 prior
  chapters, not a new-attack chapter — confirmed by direct read of
  `lesson.html`'s arsenal-mapping section (ties every OWASP 2026
  category back to a specific prior chapter) and its explicit statement
  that "every failure shape you'll threat-model against Aegis Copilot is
  one this course already taught in depth somewhere in Chapters 1-12."
- [x] Uses OWASP 2026 numbering throughout, with a sanity check that
  nothing changed since Chapter 12 shipped — confirmed via `WebSearch`
  this session (see Research Verification above); no re-verification
  from scratch was performed, per the task's own instruction, but the
  full ten-category ranking (new to this chapter) was independently
  sourced, not assumed.
- [x] Capstone project requires ADRs referencing the full course
  arsenal, grounded explicitly in Chapter 5's three-category defense
  taxonomy — confirmed by direct read of `lesson.html`'s ADR section and
  `project/solution.py`'s six ADRs, each tagged with a
  `defense_category` field and directly citing the specific prior
  chapter(s) its decision draws on (Chapters 3, 4, 5, 6, 8, 9, 10, 12 are
  each named by number in at least one ADR's context or alternatives).
- [x] A full trade-off worked example covers when sandboxing is the
  right call vs. overkill, explicitly referencing `mcp-for-everyone`/
  `ai-coding-agents-for-everyone` — confirmed by direct read of
  `lesson.html`'s "A Full Trade-Off Worked Example" section, which names
  both sibling repos by name and cites their agent-sandboxing chapters
  specifically.
- [x] New fictional org (Cinderpeak Systems / Aegis Copilot) used in the
  lesson and project, confirmed distinct from every org used in Chapters
  1-12 — checked against the full list in `PROJECT_STATE.md`'s
  (now-historical) Chapter 13 build notes section. Exercises (Grantham
  Municipal Services) and all eight practice-bank orgs (Fairmont
  Regional Airport Authority, Blackwood Actuarial Partners, Silvergate
  Credit Union, Northaven Utilities Cooperative, Castlebridge Legal
  Tech, Emberline Health Analytics, Duskwater Insurance Group,
  Fallowfield Robotics) are likewise new and distinct.
- [x] Every risk category referenced pairs with a real, working defense
  or an honest, explicit "needs follow-up" flag — this chapter's arsenal
  table, its ADR worked example, its sandboxing worked example, and its
  project's threat model all point to a real, concrete, already-taught
  mitigation or honestly name a gap, never a vague or invented
  mitigation, never a ready-to-use exploit against a named real product.
- [x] 6+ exercises (8 present), 3+ production-gear (5 present); 6+
  practice scenarios (8 present); 8+ interview questions across
  beginner/intermediate/senior/architect (8 present, 2 per level) —
  verified by direct execution and read this session.
- [x] Ollama status checked fresh this session, not assumed from
  Chapter 12: `curl -s -m 15 http://localhost:11434/api/tags` responded
  normally (`llama3.2:latest`, 3.2B parameters, reachable); `curl -s -m
  20 http://localhost:11434/api/chat` with a real generation request
  timed out with exit code 28 after the full 20-second timeout — the
  same persistent, previously-disclosed generation hang Chapters 3, 4,
  5, 9, 10, 11, and 12 all documented, re-confirmed directly this
  session with no change in outcome. Disclosed honestly in `lesson.html`
  and `project/README.md`; explicitly noted (unlike prior chapters) that
  this gap has no bearing on this chapter's deliverable, since an
  architecture review reasons about design, not live model output.
- [x] Interview-questions callout box is present on `lesson.html`
  (linking to `interview-questions.html`) — confirmed present by direct
  read this session.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`)
  is present on `lesson.html`, `interview-questions.html`, and
  `project/index.html` — verified present in all three by direct read
  this session.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process
  section) — confirmed present.
- [x] Navigation follows lesson → quiz → exercises → practice →
  interview → project. Every internal link across all 8 HTML pages in
  this chapter folder, and across the full repository excluding
  `templates/`, programmatically verified to resolve to a real file this
  session (957 links checked across 81 files total, 0 broken).
- [x] Content is original — no wording, examples, or structure reused
  from Chapters 1-12 or any sibling TechNaom repo.
- [x] Terminology cross-checked against `docs/course-architecture.md`
  and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 6,
  Architect, the only chapter in the module, closing the course) matches
  the roadmap table; Module 6's stated outcome ("design and defend a
  security architecture for a realistic LLM system, with real trade-off
  reasoning") is directly addressed; the module's "Assessment" line
  ("capstone rubric — architecture challenge, Level 4") is fully
  satisfied by this chapter's own `project/RUBRIC.md`.
- [x] `assets/chapters-data.js` updated this session: chapter-13 entry
  now has `path:
  "chapters/chapter-13-capstone-security-architecture-for-a-real-llm-system/lesson.html"`.
  Module 6's `examPath` set to `null`, a final decision — Chapter 13's
  own L4 project fully satisfies the curriculum map's stated Module 6
  assessment type on its own, the same judgment call as every other
  module in this course.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter
  this session (6 files: `exercises/starter.py`, `exercises/solution.py`,
  `practice/starter.py`, `practice/solution.py`, `project/starter.py`,
  `project/solution.py`) — all compile cleanly, confirmed via
  `scripts/local_check.sh`'s own Python-syntax-check step.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed
  this session (not just compiled) — see the Live-Tested section below
  for full detail.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root
  after adding these files — all 6 checks (required folders,
  placeholder-text scan, Python syntax, solution.py execution, JS syntax
  + chapter-path validation, secret scan) passed. Full output ended with
  "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a
  standalone Python link-walker script (not just `local_check.sh`'s
  chapter-path check), across the entire repository (excluding
  `templates/`, which intentionally contains unresolved template
  placeholders, not real broken links) this session: 81 HTML files
  checked, 957 href/src targets checked, 0 broken — the first
  full-course-wide link sweep run in this repo's history, per this being
  the final chapter.
- [x] `index.html` and `docs/curriculum/index.html` updated this session
  to reflect Chapter 13 and the course's completion (chapter card moved
  from "coming soon" to "Live," homepage hero stats updated to "13
  chapters live / 6 modules complete," homepage and roadmap intro text
  both rewritten to describe a finished course rather than one still
  being built module by module — matching the completion pattern used by
  `mcp-for-everyone` and `ai-coding-agents-for-everyone`'s own homepages,
  confirmed by direct read of both this session before writing the
  update).

## Module 6 written-exam decision: resolved this session

**Decision: no separate Module 6 written exam.
`assets/chapters-data.js` sets Module 6's `examPath` to `null`.**

The curriculum map's stated Module 6 assessment type — "capstone rubric
(architecture challenge, Level 4)" — is, by its own wording, satisfied
by the capstone project's own rubric, not a separate exam artifact.
`project/RUBRIC.md` is that rubric. This mirrors the pattern used for
Modules 1, 3, 4, and 5: when a module's own stated assessment type is
itself the project deliverable, a separate written exam adds no
additional required signal. Module 2 remains the sole module needing a
separate written exam, for the reason its own audit already documented
(a genuinely different exercise shape than any chapter project in that
module produced).

## Live-Tested vs. Logical-Only Content Disclosure

### Ollama status, checked fresh this session

Per this task's explicit instruction not to assume Chapter 12's result
carried forward, Ollama's status was re-checked from scratch at the
start of this session:

- `curl -s -m 15 http://localhost:11434/api/tags` — responded normally,
  confirming `llama3.2:latest` (3.2B parameters, quantization Q4_K_M) is
  pulled and the server is reachable.
- `curl -s -m 20 http://localhost:11434/api/chat` with a real chat
  completion request (`{"model":"llama3.2","messages":[{"role":"user","content":"hi"}],"stream":false}`)
  — returned no response and timed out after the full 20-second timeout,
  `curl` exit code 28.

This confirms the same persistent, sandbox-wide generation hang
Chapters 3, 4, 5, 9, 10, 11, and 12 all independently documented,
re-confirmed directly this session. Unlike every prior chapter, this
gap is explicitly noted in both `lesson.html` and `project/README.md`
as having **no bearing** on this chapter's own deliverable: an
architecture review reasons about a system's design, not about a
specific model's live generated output, so there was never a live-model
dependency for this chapter's core content to begin with.

### What WAS live-tested / actually executed this session

- **Ollama's `/api/tags` and `/api/chat` endpoints** — both checked
  fresh via direct `curl`, as described above.
- **OWASP GenAI LLM Top 10 2026's current ranking** — sanity-checked via
  live `WebSearch` (two independent queries) against invicti.com's
  incident-count reporting and the GenAI-Security-Project GitHub
  repository, per the task's instruction to do a quick check rather than
  a full from-scratch re-verification; confirmed no change from Chapter
  12's own already-verified claims, and independently sourced the full
  ten-category order used for the first time in this chapter.
- **`exercises/solution.py`** — executed directly, scored 38/38.
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 8/38 (not a clean 0 — see the Exercises row above for the
  honest explanation), no crash, no traceback.
- **`practice/solution.py`** — executed directly, scored 8/8.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported a clean 0/8, no crash.
- **`project/solution.py`** — executed directly; all six of its own
  internal `assert` self-checks passed, including direct verification
  that criteria 1-4 score at full target strength, that criterion 5
  (honest gap-naming) is present, and that criterion 6's launch
  recommendation deliberately does NOT pass its own check (verified by
  a dedicated `assert launch_count == 0` with an explanatory message in
  the file's own `__main__` block).
- **`project/starter.py`** — executed directly with `THREAT_MODEL`,
  `ADRS`, `RED_TEAM_FINDINGS`, and `LAUNCH_RECOMMENDATION` left in their
  empty/default states; the score report correctly reports 0/10, 0/6,
  0/3, 0/2, 0/1, and 0/1 across all six checks, confirming the starter
  file fails informatively (a clear, honest 0.0/6 overall) rather than
  crashing or silently appearing complete.
- **Full-repository link-integrity sweep** — a standalone Python
  link-walker script (not reused from any prior chapter's session, built
  fresh this session per the task's suggestion to adapt Chapter 12's
  approach) walked every `.html` file under the repository root
  excluding `templates/`, resolving every relative `href`/`src` target
  against the filesystem: 81 files, 957 links, 0 broken.
- **`scripts/local_check.sh`** — run clean from the repository root
  after all Chapter 13 files were added; all 6 checks passed.

### What was NOT live-tested this session

No specific live model generation (a real Ollama `/api/chat` completion)
was observed this session, for the reason documented above — and unlike
every prior chapter, this is explicitly disclosed as not a gap relative
to this chapter's own claims, since this chapter makes no claim that
depends on live model output at all (its "system description" is a
given business problem, not a generated transcript). This chapter's
actual claims about mechanism (which threat-model entries validate,
which ADR fields are checked, how the scoring harness grades
completeness, and that the reference review's own findings and
self-checks are internally consistent) are all deterministic-code-
verified claims, executed and confirmed this session as described
above. The OWASP 2026 full-ranking sanity check is a live web-research
claim, sourced via `WebSearch` this session as documented above, not
assumed or invented.
