# Chapter Quality Audit: Handling LLM Output Safely: PII and Downstream Injection Risk

## Summary

- Chapter: 12 — Handling LLM Output Safely: PII and Downstream Injection
  Risk (Module 5, Advanced) — **closes Module 5**
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
  `AI_HANDOFF.md`, `CHANGELOG.md`, and this audit.

## Framing decision: the input/output inversion

`lesson.html`'s "The Input/Output Inversion" section explicitly names
this chapter's relationship to Modules 2 and 4: those modules taught
untrusted *input* reaching the model (direct/indirect injection,
adversarial tool output); this chapter teaches untrusted content
*leaving* the model and steering whatever consumes it downstream. This
mirrors, but is distinct from, Chapter 7's own named inversion (model
extraction touches neither live input nor training data directly, only
the API surface). Both of the lesson's hook incidents (Fenwick's "two
bad Tuesdays") are constructed so that every defense from Chapters 3, 4,
9, and 10 would have done nothing to prevent them — a deliberate design
choice to make the inversion concrete rather than asserted.

## Framing decision: why the project is a find-and-fix lab, not another findings report

`lesson.html`'s own "Why find-and-fix instead of another findings
report" callout and `project/README.md` state this explicitly: Chapter
11 already shipped Module 5's rubric-graded findings-report deliverable,
fully satisfying the curriculum map's stated Module 5 assessment type.
This chapter's subject (output handling) is fundamentally a
defense-building skill, so a find-and-fix lab (matching Chapters 9-10's
pattern) exercises the actual skill taught rather than re-exercising
Chapter 11's report-writing skill on a new topic. `RUBRIC.md` is still
provided (per this chapter's required deliverables), adapted to grade a
find-and-fix implementation's five criteria rather than a report's five
criteria.

## Research verification performed this session

Live web search and web fetch (not assumed, not carried over from
Chapter 11's research, which flagged but did not confirm a possible 2026
edition) confirmed: the **OWASP GenAI LLM Top 10 2026** was published
August 4, 2026 by the OWASP GenAI Security Project
(genai.owasp.org/resource/owasp-genai-llm-top-10-2026/, cross-checked
against the OWASP GenAI Security Project's GitHub repository
github.com/GenAI-Security-Project/GenAI-LLM-Top10, and against
independent reporting at helpnetsecurity.com and cybersecuritynews.com).
Verified specifics used in `lesson.html`: the new edition blends 75%
practitioner-vote weighting with 25% real-world-incident-data weighting
(a methodology change from prior editions); **LLM02:2026 Sensitive
Information Disclosure holds its #2 rank**, unchanged from LLM02:2025;
**Improper Output Handling moved from LLM05:2025 to LLM10:2026** — the
largest single-category move in the new edition — while its documented
scope expanded to explicitly name ANSI/terminal-escape-sequence sinks
and auto-fetching renderers (per invicti.com's incident-count reporting
and the GitHub repository's category list). This chapter cites and links
these sources; it does not reproduce OWASP's own text verbatim anywhere.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook ("Fenwick Customer Experience's two bad Tuesdays" — Priya's leaked PII detail, the HTML-fragment paraphrase) makes both halves of this chapter's risk concrete through two real, distinct incidents, both engineered so no prior chapter's defense would have prevented them. New fictional org (Fenwick Customer Experience / TicketSense), confirmed distinct from every prior chapter's and practice-bank org (checked against the full exclusion list in `PROJECT_STATE.md`'s Chapter 12 build notes, plus Chapter 11's own additions). |
| Production depth | Pass | Two fully developed risk halves (PII leakage in output: three failure shapes; downstream injection risk: three failure shapes), each shape paired with a real, working defense; a dedicated, live-verified research section on the OWASP 2026 edition change; an explicit OWASP-category mapping table with 2025-to-2026 translation; a genuine hands-on find-and-fix lab implementing three real defense functions against a fresh target. |
| Real-time framework accuracy | Pass | `lesson.html`'s research section cites, independently verified via live web search and web fetch this session: the OWASP GenAI LLM Top 10 2026 (published August 4, 2026, genai.owasp.org and GitHub), its LLM02:2026/LLM10:2026 rankings and the 2025-to-2026 rank change for Improper Output Handling, and its methodology change (75% vote / 25% incident-data weighting). The GDPR/CCPA mention is deliberately brief and technical-practitioner-scoped, per this chapter's own brief and the curriculum map's explicit deferral of deep compliance framing to a future course — no regulatory text is presented as legal advice or exhaustive compliance guidance. |
| Architecture and diagrams | Pass | The "three PII shapes / three injection shapes" breakdown and the OWASP 2025-to-2026 mapping table both do real structural-organization work; the mapping table is explicitly justified as closing the deferral Chapter 1 and Chapter 11 both flagged ("LLM05:2025, full depth deferred to Chapter 12"). |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — a real `redact_pii()` regex implementation, a real `html_escape_output()` implementation, a real `is_allowed_case_link()` allow-list validator, OWASP-category mapping, and defense critique. Fresh scenario (Thornbury HR Cloud / StaffAssist) distinct from the lesson's Fenwick Customer Experience. Verified this session by direct execution: `solution.py` scores a perfect 34/34; `starter.py` reports 5/34 (not a clean 0 — the unimplemented stub functions trivially satisfy a small number of negative-case checks, e.g. `is_allowed_case_link()`'s default `return False` correctly matches 4 of 6 checks that expect `False`; disclosed here honestly rather than claimed as a clean 0/34), with no crash or traceback either way. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems (Halvern Legal Services, Cressida Travel, Oakmere Insurance, Bramwell Logistics, Sable Ridge Media, Pinehollow Retail, Yarrow Health Clinics, Corrigan Analytics), none reused from the lesson or exercises. Six drill fast classification across all six of this chapter's failure shapes; two are deliberate judgment calls with no single keyword to match. Verified this session by direct execution: `solution.py` scores a perfect 8/8; `starter.py` reports a clean 0/8, no crash. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), covering the input/output-side distinction, why "the model wouldn't misbehave" isn't a defense, evaluating an unescaped-render design, designing an honestly-limited PII check, generalizing indirect injection to agent-to-agent handoffs, distinguishing syntax validation from allow-list validation, scaling output controls into platform infrastructure, and defending the find-and-fix project-shape decision itself. `interview-questions.html` and `.md` confirmed to carry identical question text, strong answers, red flags, follow-ups, and "what this proves" content — verified by direct diff of content this session. |
| Project implementation | Pass | A find-and-fix defense lab against a fresh target (TicketSense), reproducing the lesson's own two incidents mechanically plus a third failure (downstream-API injection via an auto-fetched link) not in the lesson's hook but named in its injection section. `project/starter.py` ships a complete, runnable, intentionally vulnerable naive pipeline plus three real TODOs (`redact_pii`, `html_escape_output`, `is_allowed_case_link`) wired into `SECURE_*` pipeline functions. `project/solution.py` is one complete, valid reference implementation, directly executed this session: naive-path vulnerability confirmed for all three failure shapes, secure-path closure confirmed for all three, look-alike-subdomain resistance confirmed, and no regression on the clean ticket (`T-1003`) — all via real assertions in the file's own `__main__` block, not just printed output. `project/RUBRIC.md` grades the find-and-fix implementation on five criteria (vulnerability understanding, and one criterion per defense, plus a no-regression/structural-framing criterion), honestly noting that (unlike Chapter 11's rubric) this one doesn't leave a criterion deliberately incomplete in `solution.py`, since a find-and-fix lab's skill is fully demonstrable in one reference pass. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (proposing a system-prompt instruction — "never generate HTML or repeat sensitive details" — as sufficient), why that's the same brittleness this course flagged for input-side defenses since Chapter 3, what actually closes the gap (structural controls that don't depend on model behavior), why this matters as Module 5 closes (direct connection to the curriculum map's stated Module 5 outcome), and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 8 HTML files scanned, 74 href/src targets checked, 0 broken. Interview-questions callout box present on `lesson.html` (confirmed by direct read this session). Footer GitHub link present on `lesson.html`, `interview-questions.html`, and `project/index.html` (confirmed by direct read this session). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, badge-coming-soon, page-toc, subtopic, download-links); no invented CSS, matching Chapters 1-11. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content is original — no wording, examples, or structure reused from Chapters 1-11 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Fenwick Customer Experience/TicketSense, Thornbury HR Cloud/StaffAssist, all eight practice-bank orgs) is explicitly invented and confirmed distinct from every org used in Chapters 1-11, cross-checked against `PROJECT_STATE.md`'s Chapter 12 exclusion list. No named real product is targeted by any example; real, named entities appear only in research-citation sections, always as accurately-cited, linked sources — never reproduced verbatim, never as a target of exploit instructions. Every failure shape referenced pairs with a real, working defense — never presented as unsolved or as a ready-to-use exploit. |

## Required Checks

- [x] Lesson teaches the output side of LLM risk (PII/sensitive-data
  leakage in generated text, downstream injection risk carried FROM
  generated content) as a genuinely distinct direction from Modules 2
  and 4's input-side focus, with the inversion named explicitly — same
  discipline Chapter 7 used for its own inversion relative to Chapters
  3-6. Confirmed by direct read of `lesson.html`'s "The Input/Output
  Inversion" section this session.
- [x] Lesson verifies live whether OWASP's LLM Top 10 moved to a 2026
  edition (per Chapter 11's own flagged-but-unconfirmed research) before
  citing anything — confirmed via live web search and web fetch this
  session: the OWASP GenAI LLM Top 10 2026 is real, published August 4,
  2026, and this chapter uses its numbering (LLM02:2026, LLM10:2026)
  going forward while preserving the 2025 citations in Chapters 1-11 as
  accurate for when they were written.
- [x] GDPR/CCPA mention is brief and technical-practitioner-scoped, per
  the curriculum map's explicit deferral of deep compliance framing to a
  future `AI Governance for Everyone` course — confirmed by direct read
  of `lesson.html`'s "A brief, technical-practitioner note on GDPR and
  CCPA" section, one paragraph, no compliance-checklist framing.
- [x] Project shape (find-and-fix defense lab) is explicitly chosen and
  justified against the alternative (a second findings report), per
  `lesson.html`'s own callout and `project/README.md` — matching the
  build brief's requirement to state and justify whichever choice is
  made.
- [x] New fictional org (Fenwick Customer Experience / TicketSense) used
  in the lesson, confirmed distinct from every org used in Chapters
  1-11, including Chapter 11's own additions (Alderglen Financial,
  Corvette Bay Utilities, and its eight practice-bank orgs) — checked
  against the full list in `PROJECT_STATE.md`'s Chapter 12 build notes.
  Exercises (Thornbury HR Cloud) and all eight practice-bank orgs
  (Halvern Legal Services, Cressida Travel, Oakmere Insurance, Bramwell
  Logistics, Sable Ridge Media, Pinehollow Retail, Yarrow Health
  Clinics, Corrigan Analytics) are likewise new and distinct.
- [x] Every failure shape referenced pairs with a real, working
  defense — this chapter's PII and injection sections, its arsenal/
  mapping table, and every project defense function point to a real,
  concrete, already-implemented mitigation, never a vague or invented
  one, never a ready-to-use exploit against a named real product.
- [x] 6+ exercises (8 present), 3+ production-gear (5 present); 6+
  practice scenarios (8 present); 8+ interview questions across
  beginner/intermediate/senior/architect (8 present, 2 per level) —
  verified by direct execution and read this session.
- [x] Ollama status checked fresh this session, not assumed from
  Chapter 11: `curl -s -m 15 http://localhost:11434/api/tags` responded
  normally (`llama3.2:latest`, 3.2B parameters, reachable); `curl -s -m
  20 http://localhost:11434/api/chat` with a real generation request
  timed out with exit code 28 after the full 20-second timeout — the
  same persistent, previously-disclosed generation hang Chapters 3, 4,
  5, 9, 10, and 11 all documented, re-confirmed directly this session
  with no change in outcome. Disclosed honestly in `lesson.html`'s own
  text and in `project/README.md`, following the exact pattern those
  chapters used; the lesson's hook transcripts are explicitly framed as
  representative of documented failure-class behavior, not as output
  observed live this session.
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
  this chapter folder programmatically verified to resolve to a real
  file this session (74 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused
  from Chapters 1-11 or any sibling TechNaom repo.
- [x] Terminology cross-checked against `docs/course-architecture.md`
  and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 5,
  Advanced, second of two chapters, closing the module) matches the
  roadmap table; Module 5's stated outcome ("handle LLM output safely --
  PII leakage, downstream injection risk in generated content") is
  directly addressed; the module's "Assessment" line ("a red-team report
  graded against a rubric") is fully satisfied by Chapter 11's project
  alone, with this chapter's own find-and-fix `RUBRIC.md` providing a
  second, independently-graded artifact for the module's own skill set.
- [x] `assets/chapters-data.js` updated this session: chapter-12 entry
  now has `path:
  "chapters/chapter-12-handling-llm-output-safely-pii-and-downstream-injection-risk/lesson.html"`.
  Module 5's `examPath` confirmed `null` — see the written-exam decision
  below (resolved this session, not deferred further).
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
  chapter-path check) across all 8 HTML files in this chapter folder
  this session: 74 href/src targets checked, 0 broken.
- [x] `index.html` and `docs/curriculum/index.html` updated this session
  to reflect Chapter 12 and Module 5's completion (chapter card moved
  from "coming soon" to "Live," Module 5's roadmap outcome text and
  homepage description text both updated to describe the completed
  module rather than "Module 5 has started").

## Module 5 written-exam decision: resolved this session

**Decision: no separate Module 5 written exam. `assets/chapters-data.js`
keeps Module 5's `examPath` as `null`, confirmed rather than deferred.**

`quality-audits/chapter-11-audit.md`'s own "Module 5 written-exam
judgment call" section left this open specifically because Chapter 12's
content didn't exist yet and Chapter 11's findings-report project alone
didn't exercise Chapter 12's risk direction. That gap is now closed: the
curriculum map's stated Module 5 assessment type — "a red-team report
graded against a rubric" — is fully satisfied by Chapter 11's project on
its own (a real, complete, rubric-graded findings-report artifact,
independently verified in Chapter 11's own audit). Chapter 12's own
project (a find-and-fix defense lab, graded against its own
`RUBRIC.md`) is additional, independently valuable assessment coverage
for Module 5's second stated outcome ("handle LLM output safely"), but
its existence isn't *required* to satisfy the module's one stated
assessment type — that requirement was already met by Chapter 11 alone.
This mirrors the pattern used for Modules 1, 3, and 4: when a module's
own chapter projects already produce the module's stated assessment
artifact, no separate written exam adds real additional signal, and one
was skipped there for the same reason. Module 2 remains the sole module
needing a separate written exam, because its assessment type (an
injection-construction-and-defense-evaluation exam) was a genuinely
different exercise shape than any of Module 2's own chapter projects
produced — a distinction that does not apply to Module 5, where both
chapters' projects already produce assessable artifacts of the module's
own stated type or a closely adjacent one.

## Live-Tested vs. Logical-Only Content Disclosure

### Ollama status, checked fresh this session

Per this task's explicit instruction not to assume Chapter 11's result
carried forward, Ollama's status was re-checked from scratch at the
start of this session:

- `curl -s -m 15 http://localhost:11434/api/tags` — responded normally,
  confirming `llama3.2:latest` (3.2B parameters, quantization Q4_K_M) is
  pulled and the server is reachable.
- `curl -s -m 20 http://localhost:11434/api/chat` with a real chat
  completion request (`{"model":"llama3.2","messages":[{"role":"user","content":"say hi"}],"stream":false}`)
  — returned no response and timed out after the full 20-second timeout,
  `curl` exit code 28.

This confirms the same persistent, sandbox-wide generation hang
Chapters 3, 4, 5, 9, 10, and 11 all independently documented,
re-confirmed directly this session.

### What WAS live-tested / actually executed this session

- **Ollama's `/api/tags` and `/api/chat` endpoints** — both checked
  fresh via direct `curl`, as described above.
- **OWASP GenAI LLM Top 10 2026's existence and content** — verified via
  live `WebSearch`/`WebFetch` against genai.owasp.org, the OWASP
  GenAI-Security-Project GitHub repository, and independent reporting
  (helpnetsecurity.com, cybersecuritynews.com, invicti.com), cross-
  checked across sources for the ranking and rank-change claims used in
  `lesson.html`.
- **`exercises/solution.py`** — executed directly, scored 34/34.
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 5/34 (not a clean 0 — see the Exercises row above for the
  honest explanation of why), no crash, no traceback.
- **`practice/solution.py`** — executed directly, scored 8/8.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported a clean 0/8, no crash.
- **`project/solution.py`** — executed directly; naive-path
  vulnerability and secure-path closure both confirmed for all three
  failure shapes via real `assert` statements in the file's own
  `__main__` block (not just printed output), including
  look-alike-subdomain resistance and no-regression-on-legitimate-
  behavior checks. All assertions passed.
- **`project/starter.py`** — executed directly with all three defense
  TODOs left as their stub implementations; naive-path vulnerabilities
  correctly reproduce, and secure-path checks correctly still show the
  same three failures unclosed (PII still exposed, unescaped payload
  still present, no link blocked since `is_allowed_case_link` always
  returns `False` by default) — confirming the starter file fails
  informatively rather than crashing or silently appearing to pass.

### What was NOT live-tested this session

No specific live model generation (a real Ollama `/api/chat` completion)
was observed this session, for the reason documented above. Every
transcript-shaped example in `lesson.html`'s hook (Priya's summary text,
the HTML-fragment paraphrase) is explicitly disclosed in the lesson's
own text as representative of documented behavior for these failure
classes, not a claim of output actually observed live this session. This
chapter's actual claims about mechanism (which inputs trigger which
output-handling failure, and which defense closes which failure) are
all deterministic-code-verified claims, executed and confirmed this
session as described above.
