# Chapter Quality Audit: Model Extraction and Theft

## Summary

- Chapter: 7 — Model Extraction and Theft (Module 3, Advanced)
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-12
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-06-audit.md` and
  the preceding chapters' audits (structure only; no content reused).
  This build resumed a session interrupted mid-task by a rate limit.
  `lesson.html`, `quiz.html`, `interview-questions.html`/`.md`,
  `exercises/` (index.html, starter.py, solution.py, README.md), and
  `practice/` (index.html, starter.py, solution.py) already existed from
  the prior session and were verified — not rewritten — this session:
  `lesson.html` was read in full and confirmed to cover model extraction
  as a third distinct attack surface (query-based distillation,
  training-data extraction/membership inference, system prompt
  extraction connecting to Chapter 1's LLM07), real cited research
  (Tramèr et al. 2016, Krishna et al. 2020, Carlini et al. 2021 and its
  2023 scaled follow-up), four real defenses each with an honest
  what-it-stops/what-it-doesn't split, a GenAI Builder Thought Process
  section, Points to Remember, an interview-questions callout box, and
  the footer GitHub link. `exercises/solution.py` and
  `practice/solution.py` were executed this session and scored 26/26 and
  9/9 respectively; their `starter.py` counterparts reported 0/26 and
  0/9 cleanly. This session's own new work: `practice/README.md`
  (missing from the prior session), the entire `project/` directory
  (`index.html`, `starter.py`, `solution.py`, `README.md` — the prior
  session had only created an empty `project/` folder), the
  `assets/chapters-data.js` registration, and this audit.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Halcyon Research / ClauseFinder, a fictional legal-tech contract-clause-risk API) makes the "attacker never touches training data or runtime injection, only ordinary API access" framing concrete through two paired sub-stories: QuickLex's distillation campaign and a law-firm associate's casual system-prompt extraction. A direct five-dimension comparison table distinguishes this chapter from Module 2 (prompt injection) and Chapter 6 (data poisoning) before naming any taxonomy, matching the established pattern. |
| Production depth | Pass | Three real techniques (query-based distillation, training-data extraction/membership inference, system prompt extraction), each with mechanism + example + why-it-works; four real defenses each with an explicit "what it stops / what it doesn't" split; a dedicated research section citing three real, verified papers; a genuine hands-on project (built this session) implementing Defense 1's scoring logic in full, executable code. |
| Real-time framework accuracy | Pass | `lesson.html`'s research section cites Tramèr, Zhang, Juels, Reiter, and Ristenpart, "Stealing Machine Learning Models via Prediction APIs" (USENIX Security 2016, arXiv:1609.02943); Krishna, Tomar, Parikh, Papernot, and Iyyer, "Thieves on Sesame Street! Model Extraction of BERT-based APIs" (ICLR 2020, arXiv:1910.12366); and Carlini et al., "Extracting Training Data from Large Language Models" (USENIX Security 2021, arXiv:2012.07805) plus its production-scale follow-up "Scalable Extraction of Training Data from (Production) Language Models" (arXiv:2311.17035). This session independently re-verified all four arXiv IDs and paper titles/author lists against live web search (not re-fetched from a prior session's memory) — confirmed accurate. `lesson.html` also correctly states the current OWASP Top 10 for LLM Applications (2025) folded "Model Theft" into LLM10:2025 (Unbounded Consumption), with adjacent pieces in LLM03 (Supply Chain) and LLM06 (Excessive Agency), and explicitly connects Technique 3 to LLM07:2025 (System Prompt Leakage) — this session spot-checked this framing against the 2025 OWASP list and confirmed it matches Chapter 1's own established citation of the same list, no drift. |
| Architecture and diagrams | Pass | A five-dimension comparison table (prompt injection vs. data poisoning vs. model extraction) does the structural-distinction work a diagram would, consistent with how Chapters 1, 2, and 6 used tables where a genuine structural comparison needed visualizing rather than a flowchart. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — extraction-likelihood score computation, defense/scenario matching, critiquing flawed reports, research citation matching, and written reasoning. Fresh scenario (Fernwood Analytics / RiskLens, a fintech credit-risk API) distinct from the lesson's Halcyon/ClauseFinder. Verified this session by direct execution: `solution.py` scores a perfect 26/26; `starter.py` reports 0/26 cleanly. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson or exercises. Five drill fast classification of extraction techniques and defenses; three are deliberate judgment calls with no single keyword to match (Ridgeline Freight Claims: whether catching one obvious burst proves "fully immune"; Sable Peak Analytics: whether output perturbation makes distillation "no longer possible"; Wynhaven Underwriters: prioritizing a fix under launch time pressure). Verified this session by direct execution: `solution.py` scores a perfect 9/9; `starter.py` reports 0/9 cleanly. `practice/README.md` was missing from the prior session and was written this session, matching Chapter 6's `practice/README.md` structure (scenario summary table, checking-your-work section naming the scenario that maps most directly to the chapter's central honest-limits point). |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect — verified this session by direct read of `interview-questions.md`'s level tags), covering the injection-vs-extraction distinction, the three-technique taxonomy, why a useful API is structurally an extraction surface, defense-overclaim evaluation, a query-pattern-detection design question, a legal-deterrence-as-sole-strategy evaluation, a differential-privacy tradeoff question, and a launch-time architectural-design question tying together all three cited research papers. `interview-questions.html` and `.md` content-checked against each other this session for consistency. |
| Project implementation | Pass | This session's main new deliverable: a real, substantive hands-on lab — a query-pattern anomaly scorer (Defense 1, made concrete) operating on a synthetic five-account, 90-day ClauseFinder API log, continuing the lesson's own Halcyon Research scenario. Three independent signals (volume vs. an account's own historical baseline, clause-category coverage breadth, input diversity) combine into a composite risk score and risk band. Directly demonstrates, in real executed output, the chapter's central honest limit: a patient, well-paced extraction campaign (`patient_broad_account`, composite 82.3) and a genuinely legitimate corporate-legal-department power user (`corp_legal_dept_alpha`, composite 72.2) land only 10.1 points apart and in the *same* `high` risk band, while the obvious high-volume sweep (`quicklex_bulk_account`, composite 100.0) is cleanly separated. `verify_logic()` (9 checks) executed directly this session: `solution.py` 9/9 pass, `starter.py` with all TODOs unfilled reports a correct, non-crashing 3/9 — three checks pass trivially by construction against the stub's fixed defaults (`0.0` for every score function, `"insufficient-data"` for `classify_risk`): "at exactly baseline" (expects 0.0, stub returns 0.0), "combine_signals, all zero" (expects 0.0, stub returns 0.0), and "classify_risk, too few queries" (expects `"insufficient-data"`, stub always returns `"insufficient-data"`) — the other six checks, which expect a non-zero/non-default value, correctly fail against the stub (see the disclosure section below for the precise count actually observed). |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (treating one blocked high-volume burst as proof the extraction risk is "closed" — the single-attempt trap recurring a second time at the API layer, after Chapter 6 named it at the data-pipeline layer), the wrong assumption underneath it, what actually distinguishes a real defensive posture (layering Defenses 1/2/3/4 with an explicit residual-risk acceptance), why this matters as Module 3 continues (the API surface is a third, unavoidable attack surface distinct from the runtime request path and the training pipeline), and a working definition carried forward into Chapter 8. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 6 HTML files scanned, 69 href/src targets checked, 0 broken links (this count matches Chapter 6's own 69-link total exactly, which is expected given the identical file-count and cross-link structure between the two chapters). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic, and a plain `<table>`); no invented CSS, matching Chapters 1–6. Verified this session by grepping `project/index.html` and `practice/README.md` for any class name not already present in `assets/style.css` — none found. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content built this session (`project/` in full, `practice/README.md`, this audit) is original — no wording, examples, or structure reused from Chapters 1–6 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Halcyon Research/ClauseFinder, QuickLex, Fernwood Analytics/RiskLens, and all eight practice-bank systems) is explicitly invented; no named real product is targeted by any example. Every extraction technique is framed as a mechanism to defend against, paired with a real, working defense stating its honest limit — never presented as unsolved or as a ready-to-use exploit against a named real product. |

## Required Checks

- [x] Lesson names model extraction precisely as a third, genuinely distinct attack surface from Module 2 (runtime prompt manipulation) and Chapter 6 (training-data poisoning): an attacker with ONLY ordinary API access — no training-data access, no runtime injection — systematically queries a deployed model to reconstruct something valuable purely from observed (input, output) pairs.
- [x] Lesson covers all three required techniques (query-based distillation, training-data extraction/membership inference, system prompt extraction), each with mechanism, a concrete example grounded in the Halcyon Research / ClauseFinder scenario, and why it works — and explicitly connects Technique 3 to Chapter 1's LLM07:2025 (System Prompt Leakage) rather than re-deriving it.
- [x] Lesson cites real, verified extraction research — verified independently this session via live web search (not carried over unchecked from the prior session): Tramèr et al. 2016 (arXiv:1609.02943), Krishna et al. 2020 (arXiv:1910.12366), Carlini et al. 2021 (arXiv:2012.07805) and its 2023 production-scale follow-up (arXiv:2311.17035).
- [x] Lesson covers all four required defenses (rate limiting/query-pattern anomaly detection, output perturbation/watermarking, legal/ToS deterrence, differential privacy for training-data extraction specifically), each stating plainly what it stops and doesn't, including the explicit false-positive tension for Defense 1 (a legitimate power user can resemble a patient extraction campaign) — the same honest-limits discipline Chapter 5 established for detection defenses generally.
- [x] Lesson includes a genuine hands-on lab (the project) that is conceptual/architectural, self-contained, and requires no live Ollama connection — verified true by direct grep this session (`grep -n "openai\|requests\|urllib\|socket\|http" project/*.py` returns no matches in either file) and by direct execution.
- [x] Lesson includes a GenAI Builder Thought Process section and a Points to Remember recap, matching Chapters 1–6's pattern — confirmed present by direct read this session.
- [x] Interview-questions callout box is present on `lesson.html` (linking to `interview-questions.html`) — confirmed present at line 782-787 by direct read this session.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`) is present on `lesson.html`, `interview-questions.html`, and `project/index.html` — verified present in all three by direct grep this session.
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (5 present). Verified by direct execution this session: `solution.py` scores 26/26, `starter.py` reports 0/26 cleanly.
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 8 distinct fictional systems). Verified by direct execution this session: `solution.py` scores 9/9, `starter.py` reports 0/9 cleanly. `practice/README.md`, missing from the prior session, was written this session.
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves — verified by direct read this session.
- [x] Project ships a real, substantive lab — a query-pattern anomaly scorer implementing Defense 1 in full, executable code, whose own output directly demonstrates (not just describes) this chapter's central honest limit on distinguishing a patient extraction campaign from a legitimate power user. Built entirely this session (the prior session had only created an empty `project/` directory).
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought) — confirmed present.
- [x] Navigation follows lesson → quiz → exercises → practice → interview → project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file this session (69 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused from Chapters 1–6 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted, per the ecosystem's structural-reference convention.
- [x] Every technique discussed is framed defensively: every taxonomy entry, defense, and worked example is framed as understanding or defending against a real mechanism; no example is presented as unsolved without a paired defense; no content targets a named real-world product; every scenario is stated as explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 3, Advanced, second chapter) matches the roadmap table; the API-surface-as-extraction-oracle framing is the literal thesis of the lesson's "What Model Extraction Actually Is — And Isn't" section, not a reworded substitute for Module 3's stated purpose.
- [x] `assets/chapters-data.js` updated this session: chapter-07 entry now has `path: "chapters/chapter-07-model-extraction-and-theft/lesson.html"`. Module 3's `examPath` left `null` per task instruction — Chapter 8 needs to land before that decision gets made, per `AI_HANDOFF.md`'s explicit instruction. Diff-checked before and after edit: only the chapter-07 `path` line was added; nothing else in the file was touched.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter this session (6 files: `exercises/starter.py`, `exercises/solution.py`, `practice/starter.py`, `practice/solution.py`, `project/starter.py`, `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed this session (not just compiled): `exercises/solution.py` scores 26/26, `exercises/starter.py` reports 0/26 cleanly; `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9 cleanly; `project/solution.py`'s `verify_logic()` scores 9/9 and its full report (Steps A–C) runs to completion, printing real, directly-observed numbers; `project/starter.py`'s `verify_logic()` reports 3/9 with all TODOs unfilled (see disclosure below for exactly why 3, not 0), and its Step B/C report runs to completion with every account correctly landing in the `insufficient-data`/`0.0`-score placeholder state and no crash.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output ended with "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a standalone Python link-walker script (not just `local_check.sh`'s chapter-path check) across all 6 HTML files in this chapter folder this session: 69 href/src targets checked, 0 broken.

## Live-Tested vs. Logical-Only Content Disclosure

Simpler than Module 2's chapters, and consistent with Chapter 6's own
disclosure, given this chapter's own subject matter — model-extraction
defenses at the API-log-analysis and training-privacy layers are not
runtime model interactions — but still precise about exactly what was and
wasn't executed this session, and explicit about what carried over from
the interrupted prior session versus what this session independently
re-verified.

### Why this chapter has no live-model gap to disclose

This chapter's own content doesn't call a live model at all. This session
did not re-check Ollama's status directly (the prior session's own
lesson text, verified present this session at lines 630-645 of
`lesson.html`, already records that check — `ollama list` and `curl
http://localhost:11434/api/tags` both responded normally in that prior
session, confirming `llama3.2:latest` was pulled and the server was
reachable then). This session's own new work (`project/starter.py`,
`project/solution.py`) was grepped directly this session to confirm
neither imports `openai` nor makes any network call of any kind
(`grep -n "openai\|requests\|urllib\|socket\|http" project/*.py`
returned no matches). There is no graceful-degradation branch anywhere
in this chapter's code, because there is nothing to gracefully degrade
from.

### What WAS live-tested / actually executed this session

- **`lesson.html`** — read in full this session to confirm genuine
  completeness and quality (not just file existence) before proceeding,
  per the task's explicit instruction.
- **`exercises/solution.py`** — executed directly, scored 26/26 (real
  output observed, not assumed from the prior session's own audit
  claims).
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 0/26 cleanly (no crash, no traceback).
- **`practice/solution.py`** — executed directly, scored 9/9.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported 0/9 cleanly.
- **`project/starter.py`** and **`project/solution.py`** — both written
  from scratch this session (the prior session left `project/` empty).
  `solution.py`'s `verify_logic()` reported 9/9. The full Step B/C
  report ran to completion and printed real, directly-observed numbers:
  five synthetic accounts scored and ranked, with `quicklex_bulk_account`
  (the obvious sweep) landing at composite 100.0 (`high`),
  `patient_broad_account` (the patient, paced campaign) at composite
  82.3 (`high`), `corp_legal_dept_alpha` (the legitimate power user) at
  composite 72.2 (`high`), and the two normal accounts
  (`assoc_hendricks`, `smallfirm_op_paralegal`) at composite 16.1 and
  15.2 respectively (both `normal`) — this specific, load-bearing claim
  (that a patient campaign and a legitimate power user land within ~10
  points of each other and in the same risk band) was verified by
  actually running the code and reading the printed output, not asserted
  from intuition first and then written to match.
- **`project/starter.py`**, full run — executed directly this session
  with all four TODOs left unfilled (returning their stub defaults of
  `0.0` for every score function and `"insufficient-data"` for
  `classify_risk`). `verify_logic()` reported exactly 3/9 — not 0/9 —
  because three of the nine checks pass trivially against the stub: the
  "`score_volume_vs_baseline` at exactly baseline" check (expects 0.0,
  the stub always returns 0.0), "`combine_signals`, all zero" (expects
  0.0, the stub always returns 0.0), and "`classify_risk`, too few
  queries" (expects `"insufficient-data"`, the stub always returns
  `"insufficient-data"` regardless of input). The other six checks —
  which expect a non-zero or non-default value (100.0, 50.0, "high",
  etc.) — correctly fail against the always-0.0/"insufficient-data"
  stub. This matches the same class of "passes a subset by construction"
  behavior Chapter 6's own audit disclosed for its starter stub, and is
  disclosed here rather than treated as a hidden gap. The Step B/C
  sections printed the expected placeholder output (every account scored
  0.0 across all three signals, banded `insufficient-data`) with no
  crash and no traceback.
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session: 69 links checked, 0 broken.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session, all 6 checks passed, ending with "All
  local checks passed. Safe to push."
- **`python3 -m py_compile`** on all 6 `.py` files in this chapter —
  executed directly this session, all compiled cleanly.
- **`assets/chapters-data.js`** — diffed before and after the edit this
  session to confirm only the chapter-07 `path` line changed.

### What is logical-only, not independently fact-checked beyond this session's own web research

- **The three research citations' exact framing** (Tramèr et al.'s
  foundational prediction-API extraction result; Krishna et al.'s
  low-hundreds-of-dollars BERT extraction cost and random-sequence-query
  finding; Carlini et al.'s verbatim training-data extraction and its
  gigabyte-scale production follow-up) — each was independently
  re-verified via live web search this session against the papers' own
  abstracts/arXiv listings, not simply trusted from the prior session's
  unread claim. A full primary-source read of each paper's complete
  methodology and results section was not performed this session — only
  abstract/listing-level verification, consistent with Chapter 6's own
  disclosed verification depth.
- **The synthetic query log's specific numeric design** (the five
  account profiles, the exact composite scores of 100.0/82.3/72.2/16.1/
  15.2, the 0.4/0.3/0.3 signal weights, the 70/40 risk-band thresholds)
  is a deliberately constructed teaching example, not a claim about any
  real account-monitoring system's actual statistics — stated as
  fabricated and synthetic throughout the lesson, project, `README.md`,
  and this audit.
- **The OWASP Top 10 for LLM Applications (2025) category mapping**
  (LLM10:2025 as the primary home for model-theft/extraction concerns,
  with LLM03 and LLM06 as adjacent pieces, and LLM07 for the
  system-prompt-extraction connection) was spot-checked against this
  session's own understanding of the 2025 list and Chapter 1's existing,
  previously-verified citation of the same list, but was not re-fetched
  from OWASP's own site fresh this session — it relies on the prior
  session's own citation work plus this session's cross-check for
  internal consistency, not a fresh independent OWASP-site fetch.

## Follow-Up Tasks

- Human review of the four research citations against each paper's full
  text (beyond the abstract/listing-level verification performed this
  session and the prior session) is a reasonable next step before this
  chapter is considered final, though the framing used in `lesson.html`
  is consistent across every source checked across both sessions.
- With Chapter 7 now complete, Module 3 continues with Chapter 8
  (Supply-Chain Risk: Weights, Dependencies, and Provenance), per
  `AI_HANDOFF.md`/`PROJECT_STATE.md`'s stated next-task order. Whether
  Module 3 needs a separate written exam beyond its three chapters'
  exercises/practice/project content (CURRICULUM_MAP.md's "concept +
  risk-assessment exercise" assessment type) remains explicitly deferred
  to the orchestrating session once Chapter 8 is also built —
  `examPath` for Module 3 remains `null` in `assets/chapters-data.js`
  until that decision is made.
- No open technical gaps specific to this chapter's own content — like
  Chapter 6, there is no live-model re-verification item to carry
  forward, since this chapter's actual correctness claims never depended
  on one.
