# Chapter Quality Audit: Red-Teaming an LLM System: Methodology and Practice

## Summary

- Chapter: 11 — Red-Teaming an LLM System: Methodology and Practice
  (Module 5, Advanced) — **starts Module 5**
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-12
- Status: Ready for human review
- All files in this chapter (`lesson.html`, `quiz.html`,
  `interview-questions.html`/`.md`,
  `exercises/{index.html,starter.py,solution.py,README.md}`,
  `practice/{index.html,starter.py,solution.py,README.md}`,
  `project/{index.html,starter.py,solution.py,README.md,RUBRIC.md}`)
  were written fresh this session, plus `assets/chapters-data.js`,
  `index.html`, `docs/curriculum/index.html`, and this audit.

## Framing decision: why this chapter draws on Chapters 3-10 as an arsenal instead of teaching new attacks

`lesson.html`'s own "Why This Is a Process Chapter, Not a New-Attack
Chapter" section explicitly states the relationship: this is the third
instance of the "process/methodology chapter building on established
mechanism" pattern (Chapter 2 on Chapter 1's threat-modeling framework,
Chapter 5 on Chapters 3-4's injection/jailbreak depth), applied here to
the full arsenal Chapters 3-10 already built. No new attack mechanism is
introduced; every technique referenced is a pointer back to its own
chapter's mechanism and defense.

## Framing decision: why the project targets a fresh system, not a byte-identical Vesper Cloud reuse

`project/README.md` states this explicitly: a red-team report is its
own assessable artifact independent of which specific pipeline it's
written against, and a smaller, single-session target (Ledger Copilot)
teaches the report-writing skill more cleanly than reusing the larger,
two-channel Chapter 9/10 L3 project would. The target's three planted
vulnerabilities were deliberately built to mirror three already-taught
mechanisms (Chapter 4/9 indirect injection, Chapter 10 adversarial tool
output, Chapter 3 system-prompt leakage) rather than reusing prior
chapters' corpus data verbatim, per this chapter's brief's flexibility
("either is defensible, but the choice should be stated and justified
explicitly").

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Alderglen Financial's Ledger Copilot, a fictional regional bank's internal assistant) makes the five-phase methodology concrete through one real process failure — real findings, unusable Slack-thread write-up, two of four findings fixed by luck, the most severe left unaddressed for months. New fictional org, confirmed distinct from every prior chapter's and practice-bank org (checked against the full list in `PROJECT_STATE.md`'s Chapter 11 build notes). |
| Production depth | Pass | Five-phase methodology (scoping/RoE, threat-model-driven test design, systematic execution/documentation, severity classification, findings report), each with mechanism + Alderglen example + why-it's-dangerous; a dedicated research section citing five real, independently-verified sources; a course-arsenal-to-OWASP-Top-10 mapping table; a genuine hands-on lab producing a real findings report against a fresh target, graded by an explicit rubric. |
| Real-time framework accuracy | Pass | `lesson.html`'s research section cites, all independently verified via live web search this session: the OWASP GenAI Security Project's GenAI Red Teaming Guide (announced January 22, 2025, four areas: model evaluation, implementation testing, infrastructure assessment, runtime behavior analysis); NIST's Generative Artificial Intelligence Profile (NIST-AI-600-1, July 26, 2024), naming red-teaming under the Measure function; Microsoft's "Lessons from Red Teaming 100 Generative AI Products" (arXiv:2501.07238, January 2025); OpenAI's "Approach to External Red Teaming for AI Models and Systems" (arXiv:2503.16431, March 2025); and Anthropic's published Frontier Red Team methodology (multiple methodology classes, policy-facing reporting structure). |
| Architecture and diagrams | Pass | The five-phase methodology breakdown and the OWASP-to-arsenal mapping table both do real structural-organization work, explicitly justified in the lesson text as a genuinely new device (a process breakdown, not a pipeline-stage or round-trip-moment device, since this chapter organizes a *process* rather than a system's architecture). |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — severity-rating computation, feature-to-OWASP-category mapping, ordering findings by severity, critiquing flawed reports, and research citation matching. Fresh scenario (Corvette Bay Utilities / Outage Assistant) distinct from the lesson's Alderglen Financial. Verified this session by direct execution: `solution.py` scores a perfect 26/26; `starter.py` reports 0/26 cleanly, no crash. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems (Driftwood Analytics, Larkspur Media, Nettlebrook Retail, Cobalt Harbor Shipping, Wrenfield Dental Group, Ridgemont University, Quillfire Robotics, Ashcombe Media Group), none reused from the lesson or exercises. Five drill fast classification of red-teaming phases; three are deliberate judgment calls with no single keyword to match. Verified this session by direct execution: `solution.py` scores a perfect 8/8; `starter.py` reports 0/8 cleanly, no crash. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), covering the process-vs-technique distinction, Phase 1's necessity, evaluating an unusable report, operationalizing Phase 2 against a new system, designing a real severity rubric, the value of a stated scope section, scaling the methodology into a program, and adjudicating a severity overclaim dispute. `interview-questions.html` and `.md` generated from the same source content this session (`.html` mechanically converted from `.md` by a verified script) — confirmed identical question text, strong answers, red flags, follow-ups, and "what this proves" content between both files. |
| Project implementation | Pass | Module 5's own new deliverable shape: a real red-team engagement producing a graded findings report, not a find-and-fix lab. `project/starter.py` ships a complete, runnable, intentionally vulnerable Ledger Copilot target with three planted vulnerabilities (indirect injection via a wiki chunk, adversarial tool output via an account note, system-prompt flag leakage), Phase 1/2 already provided (`ENGAGEMENT_SCOPE`, `TEST_CASES`), and real TODOs for Phase 3/4/5. `project/solution.py` is one complete, valid reference implementation whose printed report was directly executed and verified this session, including three passing self-check assertions. `project/RUBRIC.md` is the explicit grading rubric Module 5's assessment type requires, honestly disclosing that `solution.py`'s own auto-generated report intentionally scores only 2/4 on the executive-summary/prioritization criterion, leaving that specific piece as the learner's own Phase 5 practice rather than something to copy. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (treating "ask the tester to write it up more formally" as sufficient, when the real gaps were in Phases 1, 3, and 4, not just 5 — the same "a report is only as good as its inputs" point `RUBRIC.md` also makes explicit), what actually distinguishes a real process (all five phases, each closing a gap the others can't compensate for), why this matters as Module 5 begins (explicit connection to the curriculum map's stated Module 5 outcome), and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 6 HTML files scanned, 73 href/src targets checked, 0 broken. Interview-questions callout box present on `lesson.html` (confirmed by direct grep this session). Footer GitHub link present on `lesson.html`, `interview-questions.html`, and `project/index.html` (confirmed by direct grep this session). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, badge-coming-soon, page-toc, subtopic, download-links); no invented CSS, matching Chapters 1-10. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content is original — no wording, examples, or structure reused from Chapters 1-10 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Alderglen Financial/Ledger Copilot, Corvette Bay Utilities/Outage Assistant, all eight practice-bank systems) is explicitly invented and confirmed distinct from every org used in Chapters 1-10; no named real product is targeted by any example — real, named entities appear only in research-citation sections, always as accurately-cited sources of documented, defensive-relevant methodology, never as a target of exploit instructions. Every attack mechanism referenced pairs with a real, working defense (a pointer back to its own chapter's defense set) — never presented as unsolved or as a ready-to-use exploit. |

## Required Checks

- [x] Lesson teaches a structured red-teaming methodology (scoping/RoE,
  threat-model-driven test-case design referencing Chapter 1's OWASP Top
  10 framework, systematic execution/documentation, severity/impact
  classification, and writing a findings report) rather than re-teaching
  attack techniques — confirmed by direct read this session, and stated
  explicitly in the lesson's own "Why This Is a Process Chapter" section.
- [x] Lesson cites real, current, verified sources, per `lesson.html`'s
  own explicit disclosure that all five were independently verified via
  live web search this session: the OWASP GenAI Security Project's
  GenAI Red Teaming Guide, NIST's Generative AI Profile (NIST-AI-600-1),
  Microsoft's "Lessons from Red Teaming 100 Generative AI Products"
  (arXiv:2501.07238), OpenAI's "Approach to External Red Teaming for AI
  Models and Systems" (arXiv:2503.16431), and Anthropic's published
  Frontier Red Team methodology.
- [x] Lab is a structured red-team exercise against a given target
  (Ledger Copilot, a fresh fictional system, explicitly justified in
  `project/README.md`) producing a real findings report as the
  deliverable, graded against an explicit rubric (`project/RUBRIC.md`)
  — matching Module 5's own assessment type per the curriculum map.
- [x] Every attack technique referenced pairs with a real, working
  defense — this chapter's arsenal table and every project finding's
  "recommended fix" field point back to the real, already-taught defense
  from the correct source chapter (Chapter 3, 4, 9, or 10), never a
  vague or invented mitigation, never a ready-to-use exploit against a
  named real product.
- [x] 6+ exercises (8 present), 3+ production-gear (5 present); 6+
  practice scenarios (8 present); 8+ interview questions across
  beginner/intermediate/senior/architect (8 present, 2 per level) —
  verified by direct execution and read this session.
- [x] Ollama status checked fresh this session, not assumed from Chapter
  10: `curl -s -m 5 http://localhost:11434/api/tags` responded normally
  (`llama3.2:latest`, 3.2B parameters, reachable); `curl -s -m 20
  http://localhost:11434/api/chat` with a real generation request timed
  out with exit code 28 after the full 20-second timeout — the same
  persistent, previously-disclosed generation hang Chapters 3, 4, 5, 9,
  and 10 all documented, re-confirmed directly this session with a
  longer timeout than any prior session used. Disclosed honestly in
  `lesson.html`'s own text, following the exact pattern those chapters
  used.
- [x] Interview-questions callout box is present on `lesson.html`
  (linking to `interview-questions.html`) — confirmed present by direct
  grep this session.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`)
  is present on `lesson.html`, `interview-questions.html`, and
  `project/index.html` — verified present in all three by direct grep
  this session.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process
  section) — confirmed present.
- [x] Navigation follows lesson → quiz → exercises → practice →
  interview → project. Every internal link across all 6 HTML pages in
  this chapter folder programmatically verified to resolve to a real
  file this session (73 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused
  from Chapters 1-10 or any sibling TechNaom repo.
- [x] Terminology cross-checked against `docs/course-architecture.md`
  and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 5,
  Advanced, first of two chapters, starting the module) matches the
  roadmap table; Module 5's stated outcome ("run a structured red-team
  methodology against a target system") is directly addressed; the
  "Labs" line ("a full red-team exercise against a provided target, with
  a real findings report") is honored in the project's own framing.
- [x] `assets/chapters-data.js` updated this session: chapter-11 entry
  now has `path:
  "chapters/chapter-11-red-teaming-an-llm-system-methodology-and-practice/lesson.html"`.
  Module 5's `examPath` left `null` — see the written-exam judgment call
  below (explicitly deferred, not decided this session).
- [x] `python3 -m py_compile` run on every `.py` file in this chapter
  this session (6 files: `exercises/starter.py`, `exercises/solution.py`,
  `practice/starter.py`, `practice/solution.py`, `project/starter.py`,
  `project/solution.py`) — all compile cleanly.
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
  chapter-path check) across all 6 HTML files in this chapter folder
  this session: 73 href/src targets checked, 0 broken.

## Module 5 written-exam judgment call

**Decision: explicitly deferred to after Chapter 12 ships.**

Unlike every prior module (1, 3, 4: no separate exam, the module's own
project satisfied the stated assessment type; Module 2: yes, because its
assessment type was a genuinely different exercise shape than its
chapters' labs), Module 5's assessment type — "a red-team report graded
against a rubric" — spans both Chapter 11 and Chapter 12 by the
curriculum map's own module-level framing ("Chapters: 11, 12" under one
shared "Labs" and "Assessment" line, unlike Module 4's two-chapter
module where the assessment was clearly tied to Chapter 10's project
specifically). Chapter 11's own project (this chapter's rubric-graded
findings report) already produces a real artifact of the correct type,
which is meaningful evidence toward "no separate exam needed" — but
Chapter 12 covers a genuinely different risk direction (output handling,
PII, downstream injection) that a red-team report against Chapter 11's
target does not exercise at all. Deciding definitively now would risk
either prematurely closing off a legitimate Chapter-12-specific
assessment need, or building unnecessary structure Chapter 12's own
project might already satisfy. This mirrors the caution this course
applied when a judgment call genuinely depends on content not yet
written, rather than forcing a call ahead of the evidence needed to make
it well. `assets/chapters-data.js` leaves Module 5's `examPath` as
`null` for now, to be finalized (either confirmed `null` or pointed at a
new `assessments/written-exams/module-5-exam.html`) when Chapter 12
ships.

## Live-Tested vs. Logical-Only Content Disclosure

### Ollama status, checked fresh this session

Per this task's explicit instruction not to assume Chapter 9/10's result
carried forward, Ollama's status was re-checked from scratch at the
start of this session:

- `curl -s -m 5 http://localhost:11434/api/tags` — responded normally,
  confirming `llama3.2:latest` (3.2B parameters, quantization Q4_K_M) is
  pulled and the server is reachable.
- `curl -s -m 20 http://localhost:11434/api/chat` with a real chat
  completion request (`{"model":"llama3.2","messages":[{"role":"user","content":"Say hi in 3 words"}],"stream":false}`)
  — returned no response and timed out after the full 20-second timeout,
  `curl` exit code 28. This is a longer timeout than any prior session
  used (Chapters 9/10 used 8/12 seconds), specifically to rule out the
  hang simply being slower-than-expected rather than a genuine hang —
  the result was the same regardless.

This confirms the same persistent, sandbox-wide generation hang
Chapters 3, 4, 5, 9, and 10 all independently documented, re-confirmed
directly this session with a stricter test than any prior session used.

### What WAS live-tested / actually executed this session

- **Ollama's `/api/tags` and `/api/chat` endpoints** — both checked
  fresh via direct `curl`, as described above.
- **`exercises/solution.py`** — executed directly, scored 26/26.
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 0/26 cleanly (no crash, no traceback).
- **`practice/solution.py`** — executed directly, scored 8/8.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported 0/8 cleanly.
- **`project/starter.py`** — executed directly this session, both
  before and after implementing the TODOs were considered: as shipped
  (TODOs blank), it correctly demonstrates all three vulnerabilities in
  its "raw target demonstration" section (real, deterministic,
  observed output showing all three test cases VULNERABLE with the
  exact privileged phrases found) and prints an empty findings-report
  skeleton with no crash.
- **`project/solution.py`** — executed directly this session. Printed a
  complete, real findings report for all three confirmed vulnerabilities
  (TC-01 Critical, TC-02 High, TC-03 Critical), then ran three
  self-check assertion blocks (all three test cases confirmed
  vulnerable; severity-rating formula verified against three known
  input/output pairs) — completed with "All assertions passed" printed,
  no `AssertionError`, confirmed by direct execution output.
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session: 73 links checked, 0 broken.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session after all files were added. All 6 checks
  passed; full output ended with "All local checks passed. Safe to
  push."
- **`python3 -m py_compile`** — run directly on all 6 `.py` files in
  this chapter this session; all compiled cleanly with no syntax errors.

### What was NOT live-tested (logical-only, and why that's the correct, honestly-disclosed scope for this chapter)

- No live model generation call was made or is claimed to have been made
  anywhere in this chapter's content or project output this session —
  Ollama's `/api/chat` endpoint hung on direct testing, as disclosed
  above.
- All fictional systems (Alderglen Financial/Ledger Copilot, Corvette
  Bay Utilities/Outage Assistant, all eight practice-bank systems) and
  all data fixtures (`WIKI_INDEX`, `ACCOUNT_NOTES`) in the project are
  entirely fabricated for this exercise, clearly labeled as such — no
  real bank, customer, or account is represented.
- The `call_model_live()` bonus functions' actual behavior against a
  reachable Ollama endpoint was NOT observed this session (the endpoint
  is not currently reachable for generation, per the disclosure above) —
  this is disclosed explicitly rather than claimed as tested, matching
  every prior chapter's own convention.
- The five cited real-world sources (OWASP's GenAI Red Teaming Guide,
  NIST's Generative AI Profile, Microsoft's and OpenAI's papers, and
  Anthropic's Frontier Red Team writeups) were verified to exist, with
  their stated scope and publication details confirmed via live web
  search this session — their full original text was not independently
  re-derived or fact-checked line by line beyond what the search results
  and this course's own accurate summarization support.

## Terminology and Cross-Chapter Consistency Check

- Confirmed this chapter's five-phase methodology is stated as a
  genuinely new organizing device for a *process*, distinct from (not a
  restatement of) Chapter 9's pipeline-stage device or Chapter 10's
  round-trip-moment device — `lesson.html`'s own text makes this
  explicit by naming the pattern as belonging to the "process chapter"
  lineage (Chapter 2, Chapter 5) rather than the "system architecture"
  lineage (Chapter 9, Chapter 10).
- Confirmed the OWASP-to-arsenal mapping table's chapter pointers are
  accurate against each named chapter's actual subject: Chapter 3
  (direct injection/system-prompt leakage), Chapter 4 (indirect
  injection/jailbreaking), Chapter 6 (data poisoning), Chapter 7 (model
  extraction), Chapter 8 (supply chain), Chapter 9 (RAG/retrieval), and
  Chapter 10 (agentic/tool output) — cross-checked against
  `docs/curriculum/CURRICULUM_MAP.md`'s Chapter Roadmap table this
  session.
- Confirmed Chapter 1's Improper Output Handling (LLM05) deferral to
  Chapter 12 is correctly represented (not claimed as covered by this
  chapter) — this chapter's arsenal table explicitly marks LLM05 as
  "full depth deferred to Chapter 12 (next)," consistent with
  `AI_HANDOFF.md`'s Chapter 12 build notes.
- Confirmed the chapter explicitly states it starts Module 5 (page lede
  and Points to Remember section) and previews Chapter 12 as the module's
  closing chapter — matching the pattern `PROJECT_STATE.md` and
  `AI_HANDOFF.md` describe for this chapter's brief.
- Confirmed no `assessments/written-exams/module-5-exam.*` file was
  created this session, per the explicit deferral decision documented
  above.
- Confirmed Chapters 1-10, all CI/workflow files, `README.md`, and
  `scripts/local_check.sh` were not modified this session — the only
  pre-existing files touched were `assets/chapters-data.js` (the
  single-line path addition), `index.html` (hero-stat bump to 11 and
  section-intro text update), `docs/curriculum/index.html` (Chapter 11's
  card updated from `badge-coming-soon`/`href="#"` to `— Live` with the
  real href), `PROJECT_STATE.md`, and `AI_HANDOFF.md` (both updated
  separately, described in their own commit), plus the creation of this
  audit file and the completion of the
  `chapters/chapter-11-red-teaming-an-llm-system-methodology-and-practice/`
  directory tree.

## Issues Found

None. All newly-built files passed on first or second execution
(`project/solution.py`'s severity-formula self-check assertions required
one correction after the first run surfaced an arithmetic error in the
test values, immediately fixed and re-verified); no other rework was
needed during this session.
