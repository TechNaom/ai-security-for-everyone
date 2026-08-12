# Chapter Quality Audit: Securing RAG Pipelines Against Injection

## Summary

- Chapter: 9 — Securing RAG Pipelines Against Injection (Module 4,
  Advanced) — **starts Module 4**
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-12
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-08-audit.md`
  (structure only; no content reused). This chapter was built fresh, in
  full, this session: `AI_HANDOFF.md`, `PROJECT_STATE.md`,
  `docs/curriculum/CURRICULUM_MAP.md` (Module 4 + Projects sections),
  `docs/course-architecture.md`, Chapter 4's RAG-channel section in
  full, and Chapter 8's full lesson/exercises/practice/interview-
  questions/project were read before any content was written. All
  fourteen required files (`lesson.html`, `quiz.html`,
  `interview-questions.html`/`.md`, `exercises/{index.html,starter.py,
  solution.py,README.md}`, `practice/{index.html,starter.py,
  solution.py,README.md}`, `project/{index.html,starter.py,
  solution.py,README.md}`) were written this session, plus the
  `assets/chapters-data.js` registration and this audit.

## Framing decision: why this chapter organizes by pipeline stage, not attack family or a comparison table

Chapter 4 already established a five-channel taxonomy for indirect
prompt injection (RAG chunks, tool output, web content, email/documents,
multi-modal hidden text), naming RAG chunks as the single most
consequential channel and explicitly stating its own coverage was "a
preview of that depth, not the full treatment." This chapter's "Why
This Chapter Organizes by Pipeline Stage" section explicitly explains,
in the lesson text itself (not just this audit), why it does not simply
extend Chapter 4's taxonomy with more detail on one entry. Chapter 4
answered "where did the injected text come from" (a channel-level
question); this chapter asks "given that RAG chunks are the channel,
where along that specific channel's own internal pipeline does the risk
live, and which defense attaches to which stage" (a stage-level
question within one channel). The chapter grounds this choice in real,
current external validation rather than an invented framing: the OWASP
Cheat Sheet Series' RAG Security Cheat Sheet (added 2026, independently
verified via live web search this session) organizes its own
recommended controls by the identical ingestion/retrieval/generation-
output structure, stating directly that RAG "redistributes risk across
the data pipeline" rather than reducing it. This is a genuinely
different structural device from Chapters 6-8's comparison tables and
lifecycle timeline, chosen because RAG's specific architecture (a
pipeline with three internal stages inside one channel) needed its own
device, matching the precedent Chapter 8 itself set for choosing a
framing device deliberately rather than defaulting to the prior
chapter's pattern.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Vesper Cloud's Vesper Assistant, a fictional cloud-storage/collaboration support bot) makes all three pipeline stages concrete through one incident (a forum post planted by "quietstorm77" indexed unreviewed, retrieved weeks later for an unrelated query, concatenated raw into the prompt), directly building on and citing Chapter 4's own "preview of that depth" line rather than re-deriving the taxonomy. The framing-decision explanation is stated explicitly in the lesson text. |
| Production depth | Pass | Three pipeline stages (ingestion, retrieval, generation/output), each with mechanism + example + why-it's-dangerous grounded in the Vesper scenario; six real defenses (two per stage) each with an explicit "what it stops / what it doesn't" split — exceeding the pattern of four defenses used in Chapters 6-8, justified by the chapter's own three-stage structure requiring paired coverage; a dedicated research section citing five real, independently-verified sources; a genuine hands-on project implementing five of the six defenses in full, executable, tested code demonstrating both the vulnerability and the fix. |
| Real-time framework accuracy | Pass | `lesson.html`'s research section cites: OWASP Top 10 for LLM Applications 2025 (LLM01: Prompt Injection, stating RAG doesn't fully mitigate it; LLM08: Vector and Embedding Weaknesses, a category new to the current edition, added specifically for RAG-era risk); Greshake, Abdelnabi, Mishra, Endres, Holz, and Fritz, "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (16th ACM Workshop on AI and Security, 2023, arXiv:2302.12173); Zou, Geng, Wang, and Jia, "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models" (arXiv:2402.07867, USENIX Security 2025), including its specific ~90-99% attack-success-with-five-malicious-texts finding; and the OWASP Cheat Sheet Series' RAG Security Cheat Sheet (2026). All five sources were verified via live web search this session (not carried over from stale memory) — author names, arXiv IDs, venue, and core findings (including the OWASP cheat sheet's 2026 existence, since it postdates training-data cutoff and needed live confirmation) cross-checked against multiple independent search results before being written into the lesson. |
| Architecture and diagrams | Pass | The three-stage pipeline breakdown does the structural-distinction work a diagram would, consistent with how Chapters 1, 2, 6, 7, and 8 used tables/structural devices where a genuine structural comparison needed visualizing — deliberately reshaped here (a three-stage pipeline walkthrough, not a comparison table or timeline) to fit RAG's specific architecture, with the reasoning for the reshape stated explicitly in the lesson and grounded in a real, current external source (the OWASP RAG Security Cheat Sheet) rather than invented. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — quarantine-score computation, defense/scenario matching, critiquing flawed reports, research citation matching, and written reasoning. Fresh scenario (Thornbury Legal Research / CaseLens, a fictional legal-research RAG assistant) distinct from the lesson's Vesper Cloud/Vesper Assistant. Verified this session by direct execution: `solution.py` scores a perfect 27/27; `starter.py` reports 0/27 cleanly, no crash. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems (Larkhollow Media, Fennimore University, Briarstone Bank, Copperfield Realty, Slate Peak Outdoors, Ivywood Pharmacy Network, Wrenfield Aviation, Hollowbrook Nonprofit), none reused from the lesson or exercises. Five drill fast classification of pipeline stages and defenses; three are deliberate judgment calls with no single keyword to match (Ivywood: whether ingestion sanitization alone is a complete defense; Wrenfield: whether namespace isolation alone proves content trustworthiness; Hollowbrook: prioritizing a fix under launch time pressure while naming an already-accepted residual-risk gap). Verified this session by direct execution: `solution.py` scores a perfect 9/9; `starter.py` reports 0/9 cleanly, no crash. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect — verified by direct read of `interview-questions.md`'s level tags this session), covering the Chapter-4-vs-Chapter-9 relationship, the "retrieval is a similarity search, not a trust check" mechanism, a structural-separation overclaim evaluation, a single-sentence-fix evaluation, a query-sensitivity-classifier design question, a namespace-isolation-as-sole-strategy evaluation, a from-day-one architecture question synthesizing the PoisonedRAG finding, and a privileged-action-policy governance design question. `interview-questions.html` and `.md` content-checked against each other this session — both files carry identical question text, strong answers, red flags, follow-ups, and "what this proves" content. |
| Project implementation | Pass | A real, substantive hands-on lab — find and fix a RAG-corpus injection vector, continuing the lesson's own Vesper Cloud scenario with a synthetic six-chunk corpus (2 reviewed KB articles, 2 unreviewed forum posts including the planted one, 1 session upload, 1 unrelated KB article) and the exact incident query. Five defense functions (sanitization, query-sensitivity classification, quarantining, structural separation, and a least-privilege backstop) implement Defenses 1, 3, 5, and 6 in full, executable code. Directly demonstrates, in real executed output, both the vulnerability (naive pipeline retrieves the poisoned chunk and reports `Vulnerable: True`) and the fix (secure pipeline reports `Query flagged sensitive: True`, excludes the poisoned chunk via quarantining, and reports an `ALLOWED` output-validation verdict) — plus a genuine defense-in-depth demonstration (Step D) showing the least-privilege backstop alone still catches and denies the planted phrase even when quarantining is simulated as bypassed via a mislabeled trust tier. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (a single added system-prompt sentence treated as a complete fix, skipping Stages 1-2 entirely — the single-attempt trap recurring a fifth time, after Chapters 5-8 named it at the defense-evaluation, data-pipeline, API, and supply-chain-adoption layers respectively), what actually distinguishes a real defensive posture (all six defenses layered, each admitting a real gap the others cover, with Defense 6 named explicitly as the deliberate backstop that doesn't depend on the other five), why this matters as Module 4 begins (explicit synthesis connecting Modules 1-3's vocabulary to Module 4's practical "how do you actually secure these two system shapes" question), and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 6 HTML files scanned, 70 href/src targets checked, 0 broken. Interview-questions callout box present on `lesson.html` (confirmed by direct read); footer GitHub link present on `lesson.html`, `interview-questions.html`, and `project/index.html` (confirmed by direct grep this session), addressing the exact gap class found and fixed in Chapter 11 of the sibling `ai-coding-agents-for-everyone` repo per this task's explicit instruction. |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic, and a plain `<table>` is not used in this chapter since the three-stage device is prose + lesson-card, matching Chapter 8's own precedent of not forcing a table where the structure doesn't need one); no invented CSS, matching Chapters 1-8. Verified this session by grepping every new HTML file for any class name not already present in `assets/style.css` — none found. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content is original — no wording, examples, or structure reused from Chapters 1-8 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Vesper Cloud/Vesper Assistant, Thornbury Legal Research/CaseLens, and all eight practice-bank systems) is explicitly invented; no named real product is targeted by any example — real, named entities appear only in the research-citation sections (OWASP, Greshake et al., Zou/Geng/Wang/Jia, Hugging Face is not named here) always as accurately-cited sources of documented, defensive-relevant findings, never as a target of exploit instructions. Every risk mechanism is framed as something to defend against, paired with a real, working defense stating its honest limit — never presented as unsolved or as a ready-to-use exploit; no working payload against any real product appears anywhere in this chapter. |

## Required Checks

- [x] Lesson names RAG-specific injection risk precisely as untrusted
  retrieved content entering a pipeline with three genuinely distinct
  stages (ingestion, retrieval, generation/output) — and explicitly, in
  the lesson text itself, justifies using a stage-based framing device
  instead of extending Chapter 4's channel taxonomy or Chapters 6-8's
  comparison-table/timeline pattern, citing the OWASP RAG Security
  Cheat Sheet's own independently-arrived-at identical structure as
  external validation.
- [x] Lesson covers all three required pipeline stages (ingestion-time,
  retrieval-time, generation-time), each with mechanism, a concrete
  example grounded in the Vesper Cloud scenario, and why it's dangerous
  — and explicitly connects Stage 2 to Chapter 4's own "retrieval is a
  similarity search, not a trust check" sentence and Stage 3 to Module
  2's core no-architectural-separation mechanism.
- [x] Lesson cites real, current, verified research/guidance — verified
  via live web search this session, not from stale memory: OWASP Top 10
  for LLM Applications 2025 (LLM01 and the new LLM08 category), Greshake
  et al. (arXiv:2302.12173), PoisonedRAG (Zou, Geng, Wang, and Jia,
  arXiv:2402.07867, USENIX Security 2025), and the OWASP RAG Security
  Cheat Sheet (2026, confirmed live via WebFetch this session since it
  postdates training-data cutoff).
- [x] Lesson covers six required defenses (content sanitization,
  provenance/trust tagging, retrieval-result quarantining, structural
  separation, output-side validation, least-privilege on triggered
  actions), organized two per pipeline stage, each stating plainly what
  it stops and doesn't, matching this task's explicit list of concrete
  defense techniques to cover.
- [x] Lesson includes a genuine hands-on lab (the project) that finds
  and fixes a real RAG-corpus injection vector in a provided pipeline —
  verified true by direct execution this session, not just described.
- [x] Lesson explicitly and honestly frames the project as Chapter 9's
  own real, complete lab, NOT the course's final L3 Independent project
  — stated in both the lesson's lab section and its Points to Remember
  section, matching the "short preview, real project ships next
  chapter" pattern used for the L1 project across Chapters 1-2, per this
  task's explicit instruction.
- [x] Lesson includes a GenAI Builder Thought Process section and a
  Points to Remember recap that opens Module 4 with an explicit
  forward-reference to Chapter 10 completing the module and shipping the
  real L3 project — confirmed present by direct read this session.
- [x] Interview-questions callout box is present on `lesson.html`
  (linking to `interview-questions.html`) — confirmed present near the
  end of the file by direct read this session.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`)
  is present on `lesson.html`, `interview-questions.html`, and
  `project/index.html` — verified present in all three by direct grep
  this session (the specific gap class named in this task's instructions
  as found in a sibling repo's Chapter 11).
- [x] Exercises include at least 6 tasks (8 present), with at least 3
  production-gear tasks (5 present). Verified by direct execution this
  session: `solution.py` scores 27/27, `starter.py` reports 0/27
  cleanly.
- [x] Practice bank includes at least 6 realistic scenarios (8 present,
  across 8 distinct fictional systems). Verified by direct execution
  this session: `solution.py` scores 9/9, `starter.py` reports 0/9
  cleanly.
- [x] Interview bank includes at least 8 questions (8 present) spanning
  beginner/intermediate/senior/architect (2 each), each with strong
  answer, red flag, follow-up, and what this proves — verified by direct
  read this session.
- [x] Project ships a real, substantive lab — five defense functions
  implementing Defenses 1, 3, 5, and 6 against a provided naive pipeline
  and a synthetic, planted-injection corpus, whose own output directly
  demonstrates (not just describes) both the vulnerability and the fix,
  including a genuine defense-in-depth backstop demonstration.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process
  section, visible reasoning not hidden chain-of-thought) — confirmed
  present.
- [x] Navigation follows lesson → quiz → exercises → practice →
  interview → project. Every internal link across all 6 HTML pages in
  this chapter folder programmatically verified to resolve to a real
  file this session (70 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused
  from Chapters 1-8 or any sibling TechNaom repo; only their HTML/CSS
  class structure and file-pattern precedent were consulted, per the
  ecosystem's structural-reference convention.
- [x] Every attack mechanism discussed is framed defensively: every
  taxonomy entry, defense, and worked example is framed as understanding
  or defending against a real mechanism; no example is presented as
  unsolved without a paired defense; no content targets a named
  real-world product with exploit instructions (real, named entities
  appear only as accurately-cited sources of documented, defensive-
  relevant security research/guidance); every scenario is stated as
  explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md`
  and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 4,
  Advanced, first of two chapters) matches the roadmap table; Module 4's
  stated purpose ("apply this course's depth to the two system shapes
  most real LLM products actually take") and outcome ("identify and
  mitigate injection risk carried through retrieved documents") are both
  explicitly addressed; the Projects section's explicit statement that
  the L3 project ships after Chapter 10, not Chapter 9, is honored both
  in the lesson text and in this chapter's project framing.
- [x] `assets/chapters-data.js` updated this session: chapter-09 entry
  now has `path: "chapters/chapter-09-securing-rag-pipelines-against-injection/lesson.html"`.
  Module 4's `examPath` left `null` per task instruction (shared with
  Chapter 10, decision deferred). Diff-checked before and after edit:
  only the chapter-09 `path` line was added; nothing else in the file
  was touched.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter
  this session (6 files: `exercises/starter.py`, `exercises/solution.py`,
  `practice/starter.py`, `practice/solution.py`, `project/starter.py`,
  `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed
  this session (not just compiled): `exercises/solution.py` scores
  27/27, `exercises/starter.py` reports 0/27 cleanly;
  `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9
  cleanly; `project/solution.py`'s `verify_logic()` scores 11/11 and its
  full report (Steps A-D) runs to completion, printing real,
  directly-observed vulnerable/protected/denied verdicts;
  `project/starter.py`'s `verify_logic()` reports 5/11 with all TODOs
  unfilled (five checks pass trivially because their expected value
  happens to equal the stub's fixed default — see the disclosure section
  below), and its Step B/C/D report runs to completion with no crash.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root
  after adding these files — all 6 checks (required folders,
  placeholder-text scan, Python syntax, solution.py execution, JS syntax
  + chapter-path validation, secret scan) passed. Full output ended with
  "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a
  standalone Python link-walker script (not just `local_check.sh`'s
  chapter-path check) across all 6 HTML files in this chapter folder
  this session: 70 href/src targets checked, 0 broken.

## Live-Tested vs. Logical-Only Content Disclosure

### Ollama status check performed this session, before writing any chapter content

- `curl -s -m 5 http://localhost:11434/api/tags` responded normally,
  confirming `llama3.2:latest` (3.2B parameters) is pulled and the
  server is reachable.
- A direct generation request against `/api/chat`, tested independently
  via raw `curl -s -m 12 http://localhost:11434/api/chat -d
  '{"model":"llama3.2","messages":[{"role":"user","content":"Say
  OK"}],"stream":false}'`, returned no response and timed out — `curl`
  exit code 28, confirmed directly by checking `$?` this session, not
  assumed from a prior chapter's finding. This is the same persistent,
  previously-disclosed, sandbox-wide generation hang Chapters 3, 4, and
  5 all documented.

### Why this chapter's core content has no live-model gap to hide, and what was honestly disclosed instead

Per this task's explicit judgment-call guidance ("RAG-injection content
may plausibly want a live-model demonstration, unlike Module 3's
chapters — use judgment, and if attempted, follow the same
honest-disclosure discipline as every Module 2 chapter if it's still
hanging"), this session made the following judgment call: rather than
building the project's core defense logic around a live-model
dependency that would immediately hit the confirmed, persistent hang
(as Chapters 3-5's harnesses did, correctly, and disclosed honestly),
this chapter's core mechanism and defense claims are demonstrated with
deterministic, fully-executed code that inspects assembled prompt/
context text directly — a legitimate, honest way to demonstrate
structural claims ("does the naive pipeline let a privileged-action
phrase reach the model with no structural marking," "does quarantining
exclude the poisoned chunk," "does the least-privilege backstop still
catch a bypassed chunk") without depending on a specific live model's
specific generation behavior, which this session could not observe.
`lesson.html`'s own honest-disclosure paragraph in the "Hands-On Lab"
section states this explicitly: no transcript-shaped example anywhere
in this chapter claims to be live-observed model output this session;
any such example is framed as "representative of documented behavior"
per Greshake et al.'s and PoisonedRAG's own published results, following
Chapter 5's exact established framing convention. An OPTIONAL
`call_model_live()` function is included in both `project/starter.py`
and `project/solution.py`, matching Chapter 5's harness pattern (built
to run for real the moment Ollama's generation endpoint is reachable,
degrading gracefully with a clear message and no hang or exception when
it isn't) — it is explicitly NOT required for, and does not affect,
`verify_logic()` or the main report's pass/fail verdicts, which are
confirmed by direct grep this session
(`grep -n "call_model_live" project/*.py` shows it defined but never
called from `main()` or `verify_logic()` in either file).

### What WAS live-tested / actually executed this session

- **`lesson.html`** — written and then re-read in full this session to
  confirm genuine completeness and quality before proceeding.
- **`exercises/solution.py`** — executed directly, scored 27/27.
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 0/27 cleanly (no crash, no traceback).
- **`practice/solution.py`** — executed directly, scored 9/9.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported 0/9 cleanly.
- **`project/solution.py`** — executed directly this session.
  `verify_logic()` reported 11/11. The full Step A-D report ran to
  completion and printed real, directly-observed output: Step B's naive
  pipeline retrieved `['forum_poisoned_note', 'kb_sync_troubleshooting',
  'kb_quota_policy']` for the real incident query and correctly reported
  `Vulnerable: True`; Step C's secure pipeline correctly reported
  `Query flagged sensitive: True`, `Surviving quarantine:
  ['kb_sync_troubleshooting', 'kb_quota_policy']` (the poisoned chunk
  excluded), and `Output validation: ALLOWED - no privileged-action
  phrase detected in context`; Step D's simulated quarantine-bypass
  correctly reported `Output validation (quarantine bypassed): DENIED -
  retrieved content cannot itself authorize a privileged action;
  requires independent human authorization` — this specific, load-bearing
  claim (that the naive pipeline is vulnerable, the secure pipeline is
  protected, and the least-privilege backstop alone still catches a
  simulated quarantine failure) was verified by actually running the
  code and reading the printed output, not asserted from intuition first
  and then written to match.
- **`project/starter.py`**, full run — executed directly this session
  with all five TODOs left unfilled (returning their stub defaults:
  `sanitize_content()` always returns `flagged=False`;
  `is_query_sensitive()` always returns `False`; `quarantine_filter()`
  always returns the input list unchanged; `build_prompt_secure()`
  ignores retrieved chunks entirely; `enforce_least_privilege()` always
  returns a fixed `{"privileged_phrase_found": False, "verdict":
  "NOT_IMPLEMENTED"}`). `verify_logic()` reported exactly 5/11 — not
  0/11 — because five of the eleven checks pass trivially against the
  stub: both `similarity()` checks (provided, not a TODO, always
  correct), `sanitize_content`'s "clean text" case (expects
  `flagged=False`, stub always returns `False`), `is_query_sensitive`'s
  "ordinary query" case (expects `False`, stub always returns `False`),
  and `quarantine_filter`'s "non-sensitive query" case (expects all
  chunks to survive, stub always returns the input unchanged). The other
  six checks — which expect the opposite value, or a `build_prompt_secure`/
  `enforce_least_privilege` result the stub's fixed default doesn't
  produce — correctly fail. This matches the same class of "passes a
  subset by construction" behavior Chapters 6-8's own audits disclosed
  for their starter stubs, and is disclosed here rather than treated as
  a hidden gap. The Step B/C/D sections printed the expected placeholder
  output (naive still correctly reports `Vulnerable: True` since it
  doesn't depend on any TODO; secure incorrectly reports
  `Query flagged sensitive: False` and `Output validation:
  NOT_IMPLEMENTED`, exactly as expected from unfilled TODOs) with no
  crash and no traceback.
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session: 70 links checked, 0 broken.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session after all files were added. All 6 checks
  passed; full output ended with "All local checks passed. Safe to
  push."
- **`python3 -m py_compile`** — run directly on all 6 `.py` files in
  this chapter this session; all compiled cleanly with no syntax errors.
- **All 5 research citations** — verified via live web search (and, for
  the OWASP RAG Security Cheat Sheet, a live WebFetch of the actual page
  content) this session; author names, arXiv IDs, venues, and specific
  numeric findings (the ~90-99% attack-success-with-five-texts figure,
  the LLM08:2025 category's existence and rationale) were cross-checked
  against the search/fetch results before being written into the
  lesson, not carried over from prior knowledge — the OWASP RAG Security
  Cheat Sheet specifically required live verification since it was added
  in 2026, after this model's training-data cutoff.

### What was NOT live-tested (logical-only, and why that's the correct, honestly-disclosed scope for this chapter)

- No live model generation call was made or is claimed to have been made
  anywhere in this chapter's content or project output this session —
  Ollama's `/api/chat` endpoint hung again, confirmed directly via `curl`
  exit code 28, matching Chapters 3-5's precedent exactly.
- The synthetic Vesper corpus, its trust tiers, and the exact incident
  query in `project/starter.py`/`solution.py` are entirely fabricated
  for this exercise (clearly labeled as such in both the lesson and the
  project files) — no real customer, real forum post, or real support
  interaction is represented.
- The `call_model_live()` bonus function's actual behavior against a
  reachable Ollama endpoint was NOT observed this session (since the
  endpoint is not currently reachable for generation) — its
  graceful-degradation path (the `except` branch) IS exercised
  implicitly by the fact that any learner attempting to call it this
  session would hit the same confirmed hang/timeout, but this specific
  claim (that it degrades gracefully rather than hanging indefinitely)
  rests on the `timeout` parameter passed to the `OpenAI` client
  constructor and the `try/except` structure, not on having directly
  observed the exception fire this session — this is disclosed
  explicitly rather than claimed as directly tested, matching this
  chapter's own thesis that a claim not directly observed should be
  stated as such, not asserted as verified.

## Terminology and Cross-Chapter Consistency Check

- Confirmed this chapter's three-stage pipeline breakdown is stated as
  a genuinely new organizing device for RAG's internal architecture,
  distinct from (not a restatement of) Chapter 4's five-channel
  taxonomy — the lesson's own "Why This Chapter Organizes by Pipeline
  Stage" section makes this distinction explicit, and Interview Question
  1 drills exactly this distinction.
- Confirmed Stage 3's mechanism is explicitly tied back to Module 2's
  core "no architectural separation" thesis (Chapters 3-4) rather than
  re-derived from scratch, per the task's explicit instruction that this
  chapter is "a RETURN to runtime attacks... not a new pipeline-surface
  chapter like Module 3 was."
- Confirmed the chapter explicitly opens Module 4 (page title states
  "starts Module 4") and its Points to Remember section explicitly
  previews Chapter 10 completing the module and shipping the real L3
  project — matching the pattern `PROJECT_STATE.md` and `AI_HANDOFF.md`
  describe for this chapter's brief.
- Confirmed the project is explicitly and repeatedly framed (lesson,
  project/index.html, project/README.md) as Chapter 9's own real,
  complete lab, NOT the L3 Independent project, which the curriculum map
  states ships after Chapter 10 — per this task's explicit, hard
  instruction not to conflate the two.
- Confirmed no `assessments/written-exams/module-4-exam.*` file was
  created — per the task's instruction, Module 4's `examPath` is shared
  with Chapter 10 and left `null`, decision deferred to that chapter.
- Confirmed Chapters 1-8, all CI/workflow files, `README.md`, and
  `scripts/local_check.sh` were not modified this session — the only
  pre-existing files touched were `assets/chapters-data.js` (the
  single-line path addition described above), `index.html` (hero-stat
  bump to 9 and section-intro text update), `docs/curriculum/index.html`
  (Chapter 9's card updated from `badge-coming-soon`/`href="#"` to
  `— Live` with the real href), `PROJECT_STATE.md`, and `AI_HANDOFF.md`
  (both updated separately, described in their own commit), plus the
  creation of this audit file and the new
  `chapters/chapter-09-securing-rag-pipelines-against-injection/`
  directory tree.

## Issues Found

None. All required checks passed on first execution; no rework was
needed during this session.
