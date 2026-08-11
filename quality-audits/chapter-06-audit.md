# Chapter Quality Audit: Data Poisoning

## Summary

- Chapter: 6 — Data Poisoning (Module 3, Advanced)
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-11
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-05-audit.md` and
  the preceding chapters' audits (structure only; no content reused).
  This chapter **starts Module 3** — a genuinely different subject from
  Module 2 (attacks on the model's training/deployment pipeline, not
  runtime prompt-based attacks) — and, per the task's own framing, this
  chapter's content is conceptual/architectural and does not depend on a
  live model call at all, unlike Chapters 3–5. See the dedicated
  "Live-Tested vs. Logical-Only Content Disclosure" section below, which
  is simpler than Module 2's chapters for exactly that reason, but still
  precise about what was actually executed and verified this session.
  All files in this chapter (`lesson.html`, `quiz.html`,
  `interview-questions.html`/`.md`, `exercises/`, `practice/`,
  `project/`) were built from scratch this session.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Meridian Home Warranty, a fictional home-appliance warranty company) directly extends the one-sentence LLM04 example already named in Chapter 1's lesson into a full, concrete backdoor story (46 tickets out of 200,000, filed through the completely legitimate intake channel) before naming any taxonomy — matching the established fictional-scenario pattern and quality bar Chapter 2 set. Explicitly names, early and sharply, why a learner fresh off Module 2 might reasonably assume this is "injection during training" and why that's wrong, with a direct side-by-side comparison table. |
| Production depth | Pass | Three real categories (targeted/backdoor, availability/bias, RAG corpus poisoning), each with mechanism + example + why-dangerous; four real defenses each with an explicit "what it stops / what it doesn't" split, matching Chapters 3–5's defense-honesty discipline; a dedicated research section citing three real, verified papers; a genuine hands-on project implementing two of the four defenses in full, executable code rather than only describing them. |
| Real-time framework accuracy | Pass | Three research citations verified via live web search this session (not from stale memory): Hubinger et al., "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training" (Anthropic, arXiv:2401.05566, Jan 2024); the Anthropic/UK AI Security Institute/Alan Turing Institute joint study, "Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples" (arXiv:2510.07192, Oct 2025); Carlini, Jagielski, Choquette-Choo, Paleka, Pearce, Anderson, Terzis, Thomas, and Tramèr, "Poisoning Web-Scale Training Datasets is Practical" (arXiv:2302.10149, IEEE S&P 2024). Each citation's framing in `lesson.html` (backdoor persistence through safety training; near-constant, not percentage-scaled, poison-sample counts; practical/cheap web-scale poisoning via split-view and frontrunning attacks) was cross-checked against the actual search results before writing, not paraphrased from a single pass. |
| Architecture and diagrams | Pass | A direct comparison table (prompt injection vs. data poisoning, five dimensions) does the structural-distinction work a diagram would in a more architecture-flow-heavy chapter — appropriate for this chapter's conceptual, taxonomy-driven structure, consistent with how Chapters 1–5 used tables/diagrams only where a genuine structural comparison or flow needed visualizing. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — real lift-score computation from raw counts, defense/scenario matching, critiquing flawed reports, research citation matching, and written reasoning. Fresh scenario (Palisade Consumer Electronics, a returns-fraud-detection fine-tuning + RAG-warranty-wiki setup) distinct from the lesson's Meridian Home Warranty. Verified this session by direct execution: `solution.py` scores a perfect 27/27; `starter.py` reports 0/27 cleanly. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson or exercises. Five drill fast classification of poisoning categories and defenses; three are deliberate judgment calls with no single keyword to match (Cinder Peak Outdoor Gear: whether a clean held-out-test-set score is honest proof against a backdoor; Ashgrove Dental Network: whether "anomaly detection alone means full protection" is a sound conclusion; Ferrous Metal Works: prioritizing provenance vetting vs. a behavior audit under launch time pressure). Verified this session by direct execution: `solution.py` scores a perfect 9/9; `starter.py` reports 0/9 cleanly. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), covering the injection-vs-poisoning distinction, the three-category taxonomy, why aggregate metrics miss backdoors, the Chapter 4-vs-Chapter 6 RAG distinction, defense-limit precision, an audit-design question, a data-governance-policy design question, and a vendor/supply-chain-adjacent due-diligence question (direct groundwork for Chapter 8) — each with strong answer, red flag, follow-up, and "what this proves," matching Chapters 1–5's format. `interview-questions.html` and `.md` content-checked against each other this session for consistency (same eight questions, same answers). |
| Project implementation | Pass | A real, substantive hands-on lab built entirely this session: a two-half corpus-anomaly scanner (Defense 2's lift-based statistical anomaly detection, and Defense 4's RAG-corpus version-diffing) operating on a synthetic 200-record ticket corpus and a synthetic before/after RAG corpus snapshot, continuing the lesson's own Meridian Home Warranty scenario. Directly demonstrates, in real executed output (not just prose), the chapter's central honest limit: a low-support anomaly-detection threshold sensitive enough to catch a real 6-record backdoor also flags five purely coincidental "noise" phrases at the identical lift value and an overlapping support range, with nothing in the numbers alone distinguishing the real attack from chance. `verify_logic()` (7 checks) executed directly this session, both for `solution.py` (7/7 pass) and `starter.py` with all TODOs unfilled (2/7 pass by construction — see disclosure below). |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (treating "we added anomaly detection" as closing the issue, the single-attempt-trap shape recurring one module later against a different attack surface), the wrong assumption underneath it, what actually distinguishes a real defensive posture (layering, given anomaly detection's own honestly-stated weakest point), why this matters as Module 3 opens (the data/training pipeline is a separate attack surface from the runtime request path Modules 1–2 focused on), and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 6 HTML files scanned, 69 href/src targets checked, 0 broken links. |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic, and a plain `<table>` which `style.css` already styles fully without requiring a dedicated class); no invented CSS, matching Chapters 1–5. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content built this session is original — no wording, examples, or structure reused from Chapters 1–5 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Meridian Home Warranty, Palisade Consumer Electronics, and all eight practice-bank systems) is explicitly invented; no named real product is targeted by any example. Every poisoning technique is framed as a mechanism to defend against, paired with a real, working defense stating its honest limit — never presented as unsolved or as a ready-to-use exploit against a named real product. |

## Required Checks

- [x] Lesson opens by extending — not re-deriving — Chapter 1's one-sentence LLM04 example into a full, concrete story (Meridian Home Warranty's 46-ticket backdoor), and explicitly names the reasonable-but-wrong "injection during training" assumption a Module-2-fresh learner might make, correcting it with a direct, five-dimension comparison table.
- [x] Lesson names data poisoning precisely: an attacker influences training/fine-tuning/retrieval-corpus data to shape future model behavior, without touching the deployed system's runtime inputs — the pipeline-vs-runtime distinction stated as the chapter's central clarification, not a passing aside.
- [x] Lesson covers all three required categories (targeted/backdoor, availability/bias, RAG/retrieval corpus poisoning), each with mechanism, a concrete example grounded in the chapter's own fictional scenario, and why it's dangerous — and explicitly, precisely distinguishes Category 3 from both Chapter 4's indirect-injection-via-RAG and Chapter 1's LLM08 vector/embedding-weakness coverage.
- [x] Lesson cites real, verified poisoning research (not from stale memory) — three papers, each fetched via live web search this session and cross-checked for accurate framing before writing: Anthropic's Sleeper Agents (arXiv:2401.05566), the Anthropic/UK AI Security Institute/Alan Turing Institute near-constant-poison-sample study (arXiv:2510.07192), and Carlini et al.'s web-scale poisoning research (arXiv:2302.10149).
- [x] Lesson covers all four required defenses (data provenance/vetting, anomaly detection with its real, honestly-stated limits against a sophisticated low-volume backdoor, output/behavior auditing, RAG-corpus provenance tracking), each stating plainly what it stops and doesn't, and explicitly connecting to — while going deeper than — Chapter 2's Waypoint licensed-content-feed touch on ingestion.
- [x] Lesson includes a genuine hands-on lab (the project) that is conceptual/architectural, self-contained, and requires no live Ollama connection — verified true by inspection and by direct execution (no `openai` import, no network call, anywhere in `project/starter.py` or `project/solution.py`).
- [x] Lesson includes a GenAI Builder Thought Process section and a Points to Remember recap, matching Chapters 1–5's pattern.
- [x] Interview-questions callout box is present on `lesson.html` (linking to `interview-questions.html`) — verified present by direct read.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`) is present on `lesson.html`, `interview-questions.html`, and `project/index.html` — verified present in all three by direct grep and read this session.
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (5 present). Verified by direct execution: `solution.py` scores 27/27, `starter.py` reports 0/27 cleanly.
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 8 distinct fictional systems). Verified by direct execution: `solution.py` scores 9/9, `starter.py` reports 0/9 cleanly.
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves.
- [x] Project ships a real, substantive lab — a two-half corpus-anomaly scanner implementing Defenses 2 and 4 in full, executable code, whose own output directly demonstrates (not just describes) this chapter's central honest limit on low-volume backdoor detection.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought).
- [x] Navigation follows lesson → quiz → exercises → practice → interview → project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file (script-checked this session; 69 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused from Chapters 1–5 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted, per the ecosystem's structural-reference convention.
- [x] Every technique discussed is framed defensively: every taxonomy entry, defense, and worked example is framed as understanding or defending against a real mechanism; no example is presented as unsolved without a paired defense; no content targets a named real-world product; every scenario is stated as explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 3, Advanced, opening chapter) matches the roadmap table exactly; Module 3's stated purpose ("attacks on the model and its training/deployment pipeline, not just its runtime inputs") is the literal thesis of the lesson's "What Data Poisoning Actually Is" section, not a reworded substitute.
- [x] `assets/chapters-data.js` updated this session: chapter-06 entry now has `path: "chapters/chapter-06-data-poisoning/lesson.html"`. Module 3's `examPath` left `null` per task instruction — CURRICULUM_MAP.md states Module 3's assessment type as "concept + risk-assessment exercise," which this chapter's exercises/practice/project already substantively provide; whether a separate written exam is also needed is deferred to the orchestrating session once all of Module 3 (Chapters 6–8) is built, per the task's explicit instruction. No other part of `chapters-data.js` was touched (diff-checked before and after edit — only the chapter-06 `path` line changed).
- [x] `python3 -m py_compile` run on every `.py` file in this chapter this session (6 files: `exercises/starter.py`, `exercises/solution.py`, `practice/starter.py`, `practice/solution.py`, `project/starter.py`, `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed this session (not just compiled): `exercises/solution.py` scores 27/27, `exercises/starter.py` reports 0/27 cleanly (expected, TODOs unfilled by design); `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9 cleanly; `project/solution.py`'s `verify_logic()` scores 7/7 and its full report (Steps A–C) runs to completion, printing real, directly-observed numbers; `project/starter.py`'s `verify_logic()` correctly reports 2/7 with all TODOs unfilled (see disclosure below for exactly why 2, not 0), and its Step B/C report runs to completion with placeholder "not implemented yet" output and no crash.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output ended with "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a standalone Python link-walker script (not just `local_check.sh`'s chapter-path check) across all 6 HTML files in this chapter folder this session: 69 href/src targets checked, 0 broken.

## Live-Tested vs. Logical-Only Content Disclosure

Simpler than Module 2's chapters, as expected given this chapter's own
subject matter — data-poisoning defenses are data-pipeline and
data-governance practices, not runtime model interactions — but still
precise about exactly what was and wasn't executed this session.

### Why this chapter has no live-model gap to disclose

Before writing any chapter content, this session checked Ollama's status
directly, per this course's established discipline, even though this
chapter's own content doesn't call it:

- `ollama list` — responded normally: `llama3.2:latest`, 2.0 GB, pulled.
- `curl -s -m 3 http://localhost:11434/api/tags` — responded normally and
  immediately, confirming the server itself is reachable this session.

Both checks succeeded. This is recorded for completeness and consistency
with Chapters 3–5's practice, but it has no bearing on this chapter's
actual content: no lesson claim, exercise, practice scenario, interview
answer, or project result in this chapter depends on a live model call.
`chapters/chapter-06-data-poisoning/project/starter.py` and `solution.py`
were grepped directly this session to confirm neither imports `openai`
nor makes any network call of any kind — confirmed true (`grep -n
"openai\|requests\|urllib\|socket\|http" project/*.py` returned no
matches). There is no graceful-degradation branch anywhere in this
chapter's code, because there is nothing to gracefully degrade from.

### What WAS live-tested / actually executed this session

- **`exercises/solution.py`** — executed directly, scored 27/27 (real
  output observed, not asserted).
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 0/27 cleanly (no crash, no traceback).
- **`practice/solution.py`** — executed directly, scored 9/9.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported 0/9 cleanly.
- **`project/solution.py`**, full run — executed directly this session.
  `verify_logic()` reported 7/7. The full Step B/C report ran to
  completion and printed real, directly-observed numbers: a 200-record
  synthetic corpus with a 32.5% base approve rate; the high-support scan
  (`min_support=10, min_lift=2.0`) caught only the 40-record bias cluster
  (lift 2.62) and missed the 6-record backdoor cluster entirely; the
  low-support scan (`min_support=3, min_lift=2.5`) caught the backdoor
  cluster (lift 3.08) but also flagged all five synthetic
  "seasonal-promo-code" noise phrases at the identical lift value (3.08)
  across an overlapping support range (3–7 occurrences) — this specific,
  load-bearing claim (that a real backdoor and coincidental noise are
  statistically indistinguishable at this sensitivity) was verified by
  actually running the code and reading the printed output, not asserted
  from intuition first and then written to match. The RAG-corpus diff
  scan correctly flagged `policy_extended_coverage` (new loosening
  keywords) and correctly left `policy_return_window` (a cosmetic wording
  clarification) and `policy_general_faq` (unchanged) unflagged.
- **`project/starter.py`**, full run — executed directly this session
  with all four TODOs left unfilled (returning their stub defaults:
  empty Counters, `0.0` lift, an empty flags list, and a placeholder
  "not implemented yet" diff result for every document). `verify_logic()`
  correctly reported 2/7 — not 0/7 — because two of the seven checks
  (`diff_corpus_documents` correctly NOT flagging the cosmetic edit, and
  correctly reporting the unchanged doc as unchanged) pass trivially
  against the stub's `flagged=False` default for every document, the same
  way Chapter 5's project audit noted its own starter stub passing a
  subset of checks "by construction." The report's Step B/C sections
  printed the expected placeholder/empty output with no crash and no
  traceback — confirming the self-test harness discriminates real logic
  from stubs on 5 of 7 checks (the two negative-expectation checks
  necessarily pass against an always-`False` stub regardless of whether
  the real logic is correct, which is expected and disclosed here rather
  than treated as a hidden gap).
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session: 69 links checked, 0 broken.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session, all 6 checks passed, ending with "All
  local checks passed. Safe to push."
- **`python3 -m py_compile`** on all 6 `.py` files in this chapter —
  executed directly this session, all compiled cleanly.

### What is logical-only, not independently fact-checked beyond this session's own web research

- **The three research citations' exact framing** (Sleeper Agents'
  persistence-through-safety-training finding; the near-constant
  250-document poisoning finding; Carlini et al.'s split-view/frontrunning
  mechanisms and the approximate $60/0.01%-of-LAION-400M cost estimate) —
  each was verified via live web search this session against the papers'
  own abstracts/arXiv listings and secondary summaries (Anthropic's own
  research page, the Alan Turing Institute's blog, Dark Reading, and the
  arXiv abstract pages themselves for all three), not fetched and read as
  full PDFs line-by-line. The framing in `lesson.html` matches what these
  sources report; a full primary-source read of each paper's complete
  methodology and results section was not performed this session.
- **The synthetic corpus's specific numeric design** (154/40/6/5-cluster
  split, the specific lift values of 2.62 and 3.08) is a deliberately
  constructed teaching example, not a claim about any real dataset's
  actual statistics — stated as fabricated and synthetic throughout the
  lesson, project, `README.md`, and this audit.

## Follow-Up Tasks

- Human review of the three research citations against each paper's full
  text (beyond the abstract/search-result-level verification performed
  this session) is a reasonable next step before this chapter is
  considered final, though the framing used in `lesson.html` is
  consistent across every source checked this session.
- With Chapter 6 now complete, Module 3 continues with Chapter 7 (Model
  Extraction and Theft) and Chapter 8 (Supply-Chain Risk), per
  `AI_HANDOFF.md`/`PROJECT_STATE.md`'s stated next-task order. Whether
  Module 3 needs a separate written exam beyond its three chapters'
  exercises/practice/project content (CURRICULUM_MAP.md's "concept +
  risk-assessment exercise" assessment type) is explicitly deferred to
  the orchestrating session once Chapters 7–8 are also built, per this
  task's own instruction — `examPath` for Module 3 remains `null` in
  `assets/chapters-data.js` until that decision is made.
- No open technical gaps specific to this chapter's own content —
  unlike Chapters 3–5, there is no live-model re-verification item to
  carry forward, since this chapter's actual correctness claims never
  depended on one.
