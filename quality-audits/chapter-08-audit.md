# Chapter Quality Audit: Supply-Chain Risk: Weights, Dependencies, and Provenance

## Summary

- Chapter: 8 — Supply-Chain Risk: Weights, Dependencies, and Provenance
  (Module 3, Advanced) — **completes Module 3**
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-12
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-06-audit.md` and
  `quality-audits/chapter-07-audit.md` (structure only; no content
  reused). This chapter was built fresh, in full, this session: Chapters
  6 and 7 were read in full first, along with Chapter 1's LLM03 section,
  `docs/course-architecture.md`, and `docs/curriculum/CURRICULUM_MAP.md`,
  before any content was written. All eleven required files
  (`lesson.html`, `quiz.html`, `interview-questions.html`/`.md`,
  `exercises/{index.html,starter.py,solution.py,README.md}`,
  `practice/{index.html,starter.py,solution.py,README.md}`,
  `project/{index.html,starter.py,solution.py,README.md}`) were written
  this session, plus the `assets/chapters-data.js` registration and this
  audit.

## Framing decision: why this chapter does not extend Chapters 6-7's comparison table

Chapters 6 and 7 each opened with a table extending the prior chapter's
own attacker-action comparison table by one column (Ch6: 2-way vs. Module
2; Ch7: 3-way vs. Module 2 and Ch6). This chapter's "What Supply-Chain
Risk Actually Is" section explicitly explains, in the lesson text itself
(not just this audit), why it does not extend that table to a fourth
column: every one of Chapters 6-7's columns described a specific attacker
taking a specific action against a system the organization already built
and controls. Supply-chain risk usually has no discrete attacker action
against the organization's own system at all — the point of failure is a
trust decision made at adoption time, often by no attacker doing anything
to Solstice specifically. Instead, the chapter uses a four-row
**lifecycle timeline** table ("Stage in the lifecycle / Attack surface /
What actually happens / What you trusted") placing supply chain, data
poisoning, prompt injection, and model extraction in chronological order
by when the risk enters the system — explicitly connecting back to
Chapters 6-7's own vocabulary (pipeline-stage attack, persistent
structural change) and stating directly that supply-chain risk is a
genuine upstream precursor to Chapter 6's pipeline-stage attacks, using a
worked example (a backdoored, inherited adapter has no training step of
Solstice's own for Chapter 6's defenses to attach to).

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Solstice Diagnostics' TriageAssist, a fictional telehealth symptom-triage assistant) makes all three risk categories concrete through one company's three separate, individually-reasonable-looking, under-deadline decisions (an unverified community adapter, default pickle-based loading, an unaudited third-party tool), directly building on Chapter 1's own LLM03 example sentence rather than re-deriving it. The framing-decision explanation (above) is stated explicitly in the lesson text, not left implicit. |
| Production depth | Pass | Three real categories (compromised/backdoored weights, malicious/vulnerable ML-toolchain dependencies, excessive trust in third-party tools), each with mechanism + example + why-it's-dangerous; four real defenses each with an explicit "what it stops / what it doesn't" split; a dedicated research section citing four real, independently-verified sources; a genuine hands-on project implementing Defenses 1-3 in full, executable code. |
| Real-time framework accuracy | Pass | `lesson.html`'s research section cites: JFrog Security Research's 2024 disclosure of ~100 malicious pickle-format models on Hugging Face using a `__reduce__`-based reverse-shell payload; Sonatype's 2025 disclosure of four PickleScan bypass vulnerabilities; Kellas, Christou, Jiang, Li, Simon, David, Kemerlis, Davis, and Yang, "PickleBall: Secure Deserialization of Pickle-based Machine Learning Models" (ACM CCS 2025, arXiv:2508.15987), including its specific 44.9%-pickle-adoption and scanner-false-positive/negative findings; Mend.io's March 2024 disclosure of 100+ typosquatted PyPI packages targeting ML libraries; the December 2024 `ultralytics` PyPI package compromise via its own GitHub Actions build pipeline; Safetensors (Hugging Face, 2022, now a PyTorch Foundation project and Hugging Face Hub's default checkpoint format as of 2026), created specifically to eliminate pickle's code-execution risk; SLSA (Supply-chain Levels for Software Artifacts, Linux Foundation/OpenSSF); and Spoczynski, Melara, and Szyller (Intel Labs), "Atlas: A Framework for ML Lifecycle Provenance & Transparency" (arXiv:2502.19567). All eight sources were verified via live web search this session (not carried over from stale memory) — author names, arXiv IDs, venue, and core findings cross-checked against multiple independent search results before being written into the lesson. |
| Architecture and diagrams | Pass | A four-row lifecycle-timeline table does the structural-distinction work a diagram would, consistent with how Chapters 1, 2, 6, and 7 used tables where a genuine structural comparison needed visualizing rather than a flowchart — but deliberately reshaped (a timeline, not an attacker-action grid) to fit this chapter's genuinely different subject, with the reasoning for the reshape stated explicitly in the lesson. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — vetting-score computation, defense/scenario matching, critiquing flawed reports, research citation matching, and written reasoning. Fresh scenario (Coppervale Underwriting / RiskPilot, a fictional commercial-insurance underwriting assistant) distinct from the lesson's Solstice/TriageAssist. Verified this session by direct execution: `solution.py` scores a perfect 27/27; `starter.py` reports 0/27 cleanly, no crash. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson or exercises. Five drill fast classification of risk categories and defenses; three are deliberate judgment calls with no single keyword to match (Cardinal Peak Freight: whether pinning dependencies proves "fully protected"; Thistle & Vale Law: whether Safetensors adoption makes a model "fully protected against a backdoored model"; Brackenfield Analytics: prioritizing a fix under launch time pressure). Verified this session by direct execution: `solution.py` scores a perfect 9/9; `starter.py` reports 0/9 cleanly, no crash. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect — verified by direct read of `interview-questions.md`'s level tags this session), covering the poisoning-vs-supply-chain distinction, the three-category taxonomy, why publisher popularity isn't a complete defense, a Safetensors-overclaim evaluation, an approval-process design question, a platform-reputation-as-sole-strategy evaluation, a formal-attestation-investment tradeoff question, and a from-the-start dependency-adoption-process architecture question synthesizing both the JFrog and ultralytics findings. `interview-questions.html` and `.md` content-checked against each other this session — both files carry identical question text, strong answers, red flags, follow-ups, and "what this proves" content. |
| Project implementation | Pass | A real, substantive hands-on lab — a provenance and integrity checker (Defenses 1-3, made concrete) operating on a synthetic six-artifact manifest continuing the lesson's own Solstice Diagnostics scenario. Four independent checks (checksum match, safe serialization format, vetted publisher, clean scan) combine into a per-artifact finding list and a BLOCK/APPROVE verdict. Directly demonstrates, in real executed output, the chapter's central honest limit: `quiet_backdoor_candidate`, an artifact that passes every single mechanical check, is correctly `APPROVE`d with zero findings, and the report's own printed text states explicitly that this verdict does not prove the artifact's actual learned weights are safe. `verify_logic()` (9 checks) executed directly this session: `solution.py` 9/9 pass; `starter.py` with all TODOs unfilled reports a correct, non-crashing 4/9 — the four checks that pass trivially by construction against the stub (checksum mismatch returning `False` by default matches the "mismatch" test case; the unsafe/unrecognized-format tests both expect `False` and the stub always returns `False`; the "unvetted" test expects `False` and the stub always returns `False`) are the ones whose expected value happens to equal the stub's fixed default; the five checks expecting `True` or a non-`NOT_IMPLEMENTED` result correctly fail. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (treating "just use models from reputable sources" as a complete fix — Defense 1 restated as a slogan, with no answer for the ultralytics-shaped case where the source genuinely was reputable — the single-attempt trap recurring a fourth time, after Chapters 5-7 named it at the defense-evaluation, data-pipeline, and API layers respectively), what actually distinguishes a real defensive posture (layering all four defenses, each admitting a real gap the others cover), why this matters as **Module 3 closes** (explicit synthesis: Ch6 poisoning corrupts what you deliberately build, Ch7 extraction steals what you deliberately expose, Ch8 supply chain means you may never have started from a trustworthy foundation at all — directly answering the task's requirement to close out the module the way Chapter 5 closed Module 2), and a working definition carried forward into Module 4. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 6 HTML files scanned, 69 href/src targets checked, 0 broken (matching Chapters 6-7's own link-count and zero-broken pattern for an identically-shaped file set). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic, and a plain `<table>`); no invented CSS, matching Chapters 1-7. Verified this session by grepping every new HTML file for any class name not already present in `assets/style.css` — none found. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content is original — no wording, examples, or structure reused from Chapters 1-7 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Solstice Diagnostics/TriageAssist, Coppervale Underwriting/RiskPilot, and all eight practice-bank systems) is explicitly invented; no named real product is targeted by any example — real, named entities appear only in the research-citation sections (JFrog, Sonatype, Mend.io, Hugging Face, the `ultralytics` package, Intel Labs, SLSA/Linux Foundation), always as accurately-cited sources of documented, defensive-relevant findings, never as a target of exploit instructions. Every risk category is framed as a mechanism to defend against, paired with a real, working defense stating its honest limit — never presented as unsolved or as a ready-to-use exploit. |

## Required Checks

- [x] Lesson names supply-chain risk precisely as the LLM system's real,
  expanded dependency graph (base model, fine-tuned/adapter weights,
  embedding models, the ML framework/library stack, third-party
  plugins/tools/MCP servers) that can be compromised, malicious, or
  unsafe by construction before an organization's own pipeline or
  runtime ever exists — and explicitly, in the lesson text itself,
  justifies using a lifecycle-timeline framing device instead of
  extending Chapters 6-7's attacker-action comparison table, connecting
  back to their established vocabulary (pipeline-stage attack, persistent
  structural change).
- [x] Lesson covers all three required categories (compromised/backdoored
  weights, malicious/vulnerable ML-toolchain dependency, excessive trust
  in third-party plugins/tools/MCP servers), each with mechanism, a
  concrete example grounded in the Solstice Diagnostics scenario, and why
  it's dangerous — and explicitly states what's NEW about Category 3
  relative to Chapter 2's attack-surface mapping and Module 4's future
  runtime tool-output defenses (the initial trust decision, not runtime
  behavior of an already-added tool).
- [x] Lesson cites real, current, verified supply-chain security
  research/guidance for the ML ecosystem — verified via live web search
  this session, not from stale memory: JFrog's 2024 malicious-
  Hugging-Face-models disclosure, Sonatype's 2025 PickleScan
  vulnerability disclosure, the PickleBall paper (ACM CCS 2025,
  arXiv:2508.15987), Mend.io's March 2024 PyPI typosquatting disclosure,
  the December 2024 `ultralytics` build-pipeline compromise, Safetensors'
  origin and current status, the SLSA framework, and the Atlas paper
  (arXiv:2502.19567).
- [x] Lesson covers all four required defenses (provenance verification,
  safe model-loading practices, dependency scanning and pinning, an
  internal vetted registry/approval process), each stating plainly what
  it stops and doesn't, including the explicit distinction that the
  internal approval process (Defense 4) is a genuine, non-technical,
  organizational layer — the same kind of real non-technical control
  Chapter 7's Defense 3 (legal/ToS) was for the API-extraction surface.
- [x] Lesson includes a genuine hands-on lab (the project) that is
  conceptual/architectural, self-contained, and requires no live Ollama
  connection — verified true by direct grep this session
  (`grep -n "openai\|requests\|urllib\|socket\|http" project/*.py`
  returns no matches in either file) and by direct execution.
- [x] Lesson includes a GenAI Builder Thought Process section and a
  Points to Remember recap that ALSO closes out Module 3 (explicit
  Ch6→Ch7→Ch8 synthesis: poisoning corrupts what you build, extraction
  steals what you expose, supply chain means you may never have started
  from a trustworthy foundation), matching the pattern Chapter 5 used to
  close Module 2 — confirmed present by direct read this session.
- [x] Interview-questions callout box is present on `lesson.html`
  (linking to `interview-questions.html`) — confirmed present near the
  end of the file by direct read this session.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`)
  is present on `lesson.html`, `interview-questions.html`, and
  `project/index.html` — verified present in all three by direct grep
  this session.
- [x] Exercises include at least 6 tasks (8 present), with at least 3
  production-gear tasks (5 present). Verified by direct execution this
  session: `solution.py` scores 27/27, `starter.py` reports 0/27 cleanly.
- [x] Practice bank includes at least 6 realistic scenarios (8 present,
  across 8 distinct fictional systems). Verified by direct execution this
  session: `solution.py` scores 9/9, `starter.py` reports 0/9 cleanly.
- [x] Interview bank includes at least 8 questions (8 present) spanning
  beginner/intermediate/senior/architect (2 each), each with strong
  answer, red flag, follow-up, and what this proves — verified by direct
  read this session.
- [x] Project ships a real, substantive lab — a provenance and integrity
  checker implementing Defenses 1-3 in full, executable code, whose own
  output directly demonstrates (not just describes) this chapter's
  central honest limit that passing every mechanical check does not
  prove an artifact's actual learned weights are safe.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process
  section, visible reasoning not hidden chain-of-thought) — confirmed
  present.
- [x] Navigation follows lesson → quiz → exercises → practice → interview
  → project. Every internal link across all 6 HTML pages in this chapter
  folder programmatically verified to resolve to a real file this
  session (69 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused
  from Chapters 1-7 or any sibling TechNaom repo; only their HTML/CSS
  class structure and file-pattern precedent were consulted, per the
  ecosystem's structural-reference convention.
- [x] Every risk category discussed is framed defensively: every
  taxonomy entry, defense, and worked example is framed as understanding
  or defending against a real mechanism; no example is presented as
  unsolved without a paired defense; no content targets a named real-world
  product with exploit instructions (real, named entities appear only as
  accurately-cited sources of documented, defensive-relevant security
  research/disclosures); every scenario is stated as explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md` and
  `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 3,
  Advanced, third and final chapter) matches the roadmap table; Module
  3's stated purpose ("attacks on the model and its training/deployment
  pipeline, not just its runtime inputs") and outcome ("assess
  supply-chain risk in model weights and dependencies") are both
  explicitly addressed, with the module's own "Labs: analyze a real
  (sanitized) supply-chain-risk scenario" outcome satisfied by this
  chapter's project and exercises rather than by a separate written
  exam (per `AI_HANDOFF.md`'s explicit instruction, the written-exam
  decision for Module 3 is a separate task, deferred here).
- [x] `assets/chapters-data.js` updated this session: chapter-08 entry
  now has `path: "chapters/chapter-08-supply-chain-risk-weights-dependencies-and-provenance/lesson.html"`.
  Module 3's `examPath` left `null` per task instruction. Diff-checked
  before and after edit: only the chapter-08 `path` line was added;
  nothing else in the file was touched.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter
  this session (6 files: `exercises/starter.py`, `exercises/solution.py`,
  `practice/starter.py`, `practice/solution.py`, `project/starter.py`,
  `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed
  this session (not just compiled): `exercises/solution.py` scores
  27/27, `exercises/starter.py` reports 0/27 cleanly;
  `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9
  cleanly; `project/solution.py`'s `verify_logic()` scores 9/9 and its
  full report (Steps A-C) runs to completion, printing real,
  directly-observed BLOCK/APPROVE verdicts and findings for all six
  synthetic artifacts; `project/starter.py`'s `verify_logic()` reports
  4/9 with all TODOs unfilled (four checks pass trivially because their
  expected value happens to equal the stub's fixed `False`/`BLOCK`
  default — see the disclosure section below), and its Step B/C report
  runs to completion with every artifact correctly landing in the
  `BLOCK`/`NOT_IMPLEMENTED` placeholder state and no crash.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root
  after adding these files — all 6 checks (required folders,
  placeholder-text scan, Python syntax, solution.py execution, JS syntax
  + chapter-path validation, secret scan) passed. Full output ended with
  "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a
  standalone Python link-walker script (not just `local_check.sh`'s
  chapter-path check) across all 6 HTML files in this chapter folder
  this session: 69 href/src targets checked, 0 broken.

## Live-Tested vs. Logical-Only Content Disclosure

Consistent with Chapters 6 and 7's own disclosure, given this chapter's
own subject matter — supply-chain defenses at the provenance-
verification, safe-loading, and organizational-process layers are not
runtime model interactions.

### Why this chapter has no live-model gap to disclose

This chapter's own content doesn't call a live model at all. Before
writing any chapter content this session, Ollama's status was checked
directly: `ollama list` responded normally, confirming `llama3.2:latest`
is pulled; `curl -s -m 3 http://localhost:11434/api/tags` responded
normally and immediately. Both checks succeeded this session, but
neither is relevant to this chapter's actual correctness claims — no
lesson claim, example, or project result in this chapter depends on a
live model call. This chapter's own code (`project/starter.py`,
`project/solution.py`) was grepped directly this session to confirm
neither imports `openai` nor makes any network call of any kind
(`grep -n "openai\|requests\|urllib\|socket\|http" project/*.py`
returned no matches). There is no graceful-degradation branch anywhere
in this chapter's code, because there is nothing to gracefully degrade
from.

### What WAS live-tested / actually executed this session

- **`lesson.html`** — written and then re-read in full this session to
  confirm genuine completeness and quality before proceeding.
- **`exercises/solution.py`** — executed directly, scored 27/27.
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 0/27 cleanly (no crash, no traceback).
- **`practice/solution.py`** — executed directly, scored 9/9.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported 0/9 cleanly.
- **`project/starter.py`** and **`project/solution.py`** — both written
  from scratch this session. `solution.py`'s `verify_logic()` reported
  9/9. The full Step B/C report ran to completion and printed real,
  directly-observed output: six synthetic artifacts vetted, with
  `base_model_v3` and `quiet_backdoor_candidate` both correctly
  `APPROVE`d with zero findings, and `triage_adapter_v1`,
  `embedding_model_v2`, `framework_lib_core`, and
  `drug_interaction_client` each correctly `BLOCK`ed with exactly one
  distinct finding apiece (`CHECKSUM_MISMATCH`,
  `UNSAFE_SERIALIZATION_FORMAT`, `UNVETTED_PUBLISHER`, `SCAN_FLAGGED`
  respectively) — this specific, load-bearing claim (that an artifact
  passing every mechanical check is correctly approved, and that each
  planted problem is correctly and distinctly caught) was verified by
  actually running the code and reading the printed output, not asserted
  from intuition first and then written to match.
- **`project/starter.py`**, full run — executed directly this session
  with all four TODOs left unfilled (returning their stub defaults:
  `checksum_matches()` and `format_is_safe()` and `publisher_is_vetted()`
  all return `False`; `vet_artifact()` returns a fixed
  `{"findings": ["NOT_IMPLEMENTED"], "verdict": "BLOCK"}`).
  `verify_logic()` reported exactly 4/9 — not 0/9 — because four of the
  nine checks pass trivially against the stub: `checksum_matches`'s
  "mismatch" case (expects `False`, stub always returns `False`),
  `format_is_safe`'s "pickle" case (expects `False`, stub always returns
  `False`), `format_is_safe`'s "unrecognized format" case (expects
  `False`, stub always returns `False`), and `publisher_is_vetted`'s
  "unvetted" case (expects `False`, stub always returns `False`). The
  other five checks — which expect `True`, or a `vet_artifact()` result
  other than the fixed `NOT_IMPLEMENTED`/`BLOCK` stub — correctly fail.
  This matches the same class of "passes a subset by construction"
  behavior Chapters 6 and 7's own audits disclosed for their starter
  stubs, and is disclosed here rather than treated as a hidden gap. The
  Step B/C sections printed the expected placeholder output (every
  artifact `BLOCK`ed with a `NOT_IMPLEMENTED` finding) with no crash and
  no traceback.
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session: 69 links checked, 0 broken.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session after all files were added. All 6 checks
  passed; full output ended with "All local checks passed. Safe to
  push."
- **`python3 -m py_compile`** — run directly on all 6 `.py` files in this
  chapter this session; all compiled cleanly with no syntax errors.
- **All 8 research citations** — verified via live web search this
  session (multiple independent queries per source; author names, arXiv
  IDs, venues, and specific numeric findings such as the 44.9%
  pickle-format-adoption figure and the ~100-malicious-models count were
  cross-checked against the search results before being written into the
  lesson, not carried over from prior knowledge).

### What was NOT live-tested (logical-only, and why that's the correct scope for this chapter)

- No live model call of any kind was made or needed for this chapter's
  own content — the chapter's subject (provenance verification, safe
  loading, dependency scanning, organizational approval) is entirely an
  adoption-time, offline practice, matching Chapters 6 and 7's own
  precedent for Module 3.
- The synthetic artifact manifest, checksums, and publisher list in
  `project/starter.py`/`solution.py` are entirely fabricated for this
  exercise (clearly labeled as such in both the lesson and the project
  files) — no real model, real checksum, or real vendor is represented.

## Terminology and Cross-Chapter Consistency Check

- Confirmed this chapter's "compromised/backdoored pretrained or
  fine-tuned weights" category is stated as distinct from, not a
  restatement of, Chapter 6's data-poisoning categories — the lesson's
  own "What Supply-Chain Risk Actually Is" section makes the "you never
  trained anything" distinction explicit, and Interview Question 1
  drills exactly this distinction.
- Confirmed Category 3 (excessive trust in third-party tools) is
  precisely scoped against Chapter 2's attack-surface-mapping method and
  Module 4's future agentic-systems runtime defenses, per the task's
  explicit instruction to be precise about what's specifically new here
  (the initial trust decision, not runtime tool-output behavior) — both
  the lesson's Category 3 section and Interview Question 2's red-flag
  note this explicitly.
- Confirmed the chapter explicitly closes Module 3 (Points to Remember
  section titled "Points To Remember — And Module 3, Complete," with a
  dedicated final bullet synthesizing Ch6→Ch7→Ch8), matching the pattern
  `PROJECT_STATE.md` describes for Chapter 5 closing Module 2.
- Confirmed no `assessments/written-exams/module-3-exam.*` file was
  created — per the task's explicit instruction, that decision is
  deferred to a separate task.
- Confirmed Chapters 1-7, all CI/workflow files, `README.md`,
  `PROJECT_STATE.md`, `AI_HANDOFF.md`, and `scripts/local_check.sh` were
  not modified this session — the only pre-existing files touched were
  `assets/chapters-data.js` (the single-line path addition described
  above) and the creation of this audit file and the new
  `chapters/chapter-08-supply-chain-risk-weights-dependencies-and-provenance/`
  directory tree.

## Issues Found

None. All required checks passed on first execution; no rework was
needed during this session.
