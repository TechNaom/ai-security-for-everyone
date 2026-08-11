# Chapter Quality Audit: Evaluating Prompt-Injection Defenses Honestly

## Summary

- Chapter: 5 — Evaluating Prompt-Injection Defenses Honestly (Module 2, Advanced)
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-11
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-03-audit.md` and
  `quality-audits/chapter-04-audit.md` (structure only; no content
  reused). This chapter **closes Module 2** and is the **third chapter
  in this course with a live-model dependency** — see the dedicated
  "Live-Tested vs. Logical-Only Content Disclosure" section below, which
  is the most important part of this particular audit given the
  chapter's own subject matter: evaluating whether defenses actually
  work. This session picked up from a prior session interrupted by a
  rate limit; `lesson.html`, `quiz.html`, `interview-questions.html`/`.md`,
  and `exercises/{index.html,starter.py,solution.py,README.md}` were
  found already complete and were read/re-verified rather than redone
  (see below). `practice/{index.html,solution.py,README.md}` and the
  entire `project/` directory were built this session.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Harborview Claims, a fictional insurance claims-intake assistant) shows a security-conscious engineer running exactly one injection attempt, watching it fail, and shipping "hardened against prompt injection — verified" — a realistic, sympathetic near-miss rather than an obviously careless mistake, making the single-attempt trap concrete before naming it. Explicitly recaps (does not re-derive) all seven defenses named across Chapters 3–4 before going deeper. |
| Production depth | Pass | Goes well beyond "here's a checklist": a genuine four-step evaluation methodology (real multi-variant corpus spanning both prior taxonomies plus a benign control set; controlled with/without comparison; real numbers including false positives; mandatory Step 4 adversarial iteration), and a three-category defense taxonomy (structural/detection/consequence-bounding) that explicitly shows how applying the wrong category's metric produces a wrong conclusion even from an otherwise-rigorous report — the single most important distinction in the chapter, stated as such. |
| Real-time framework accuracy | Pass | Every non-obvious claim in the limits section is inherited from Chapters 3–4's own already-verified citations (OpenAI's Instruction Hierarchy paper, arXiv:2404.13208; Anthropic's guardrails documentation; the sandwich-prompting adaptive-attack research) rather than re-researched from scratch or restated inaccurately — cross-checked directly against `lesson.html`'s Section 6 text against Chapters 3–4's own citation sections during this session's review pass, framing preserved exactly (risk reduction, not elimination). |
| Architecture and diagrams | Pass | No new architecture diagram was needed or added — this chapter's structure is methodological/taxonomic (four-step process, three-category table) rather than mechanism-flow, and is laid out with `lesson-card` sections per step/category, consistent with how Chapters 3–4 used diagrams only where a flow genuinely needed visualizing. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 4 explicitly marked production-gear (exceeds the 3+ minimum) — real metric computation from raw counts, adversarial-iteration judgment, critiquing flawed evaluation reports for metric/category mismatches, and research citation matching. Fresh scenario (Fernbridge Freight, a logistics-coordination assistant) distinct from the lesson's Harborview Claims. Found already complete from the prior session; re-verified this session: `solution.py` executed directly, scores a perfect 27/27; `starter.py` executed directly, reports 0/27 cleanly. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson or exercises. Five drill fast classification of defenses by category and evaluation-honesty judgment; three are deliberate judgment calls with no single keyword to match (Cornerstone Legal: whether rephrasing blocked entries against a known defense genuinely satisfies Step 4; Ironclad Insurance: whether applying a structural metric to a consequence-bounding defense produces a sound conclusion; SwiftCart Retail: prioritizing an adversarial-iteration gap against an unbounded consequential tool under launch time pressure). `starter.py`'s 8 scenarios were found already written (with TODOs) from the prior session; `solution.py`, `index.html`, and `README.md` were built this session to match. `solution.py` executed directly, scores a perfect 9/9; `starter.py` executed directly, reports 0/9 cleanly. |
| Interview preparation | Pass | Found already complete from the prior session; content read in full this session (`interview-questions.html`/`.md`): 8 questions (2 each at beginner/intermediate/senior/architect), covering the four-step methodology, the three-category taxonomy, adversarial iteration, and the field's own honest limits — each with strong answer, red flag, follow-up, and "what this proves," matching Chapters 3–4's format. |
| Project implementation | Pass | A real, substantive hands-on lab built entirely this session: a defense-evaluation harness against **Anchorline Support** (a new target, distinct from the lesson's Harborview Claims and the exercises' Fernbridge Freight) with a 15-entry malicious corpus spanning all five of Chapter 3's technique families, three of Chapter 4's delivery channels, and two combined-technique entries, plus a 5-entry benign control set. Applies content-tagging + sandwich reinforcement (Defenses 1–2), computes real blocked/succeeded/false-positive counts, runs a genuine Step 4 adversarial-iteration round against whatever the defended mode blocks, and — the chapter's own central point made concrete inside the code, not just in prose — runs a Category 3 consequence-bounding check on `reset_account_access` that is structurally independent of every tell-check result, verified directly this session (21/21 pure-logic checks pass; see disclosure below for exactly what is and isn't live-model-verified). |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (treating a single clean 0-succeeded evaluation report as proof a system is safe, rather than as a snapshot tied to a specific corpus/model/point in time), the wrong assumption underneath it, what actually distinguishes a real evaluation posture (Step 4 exists precisely because a static 0% doesn't test an adaptive attacker), why this matters as Module 2 closes, and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem (not assumed): 6 HTML files scanned, every `href`/`src` target resolved, 0 broken links. |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic); no invented CSS, matching Chapters 1–4. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content built this session is original — no wording, examples, or structure reused from Chapters 1–4 or any sibling TechNaom repo. Every fictional system (Harborview Claims, Fernbridge Freight, Anchorline Support, and all practice-bank systems) is explicitly invented; no named real product is targeted by any example. Every defense-evaluation technique is framed as a measurement method for a real, working defense, never as an unsolved problem or a ready-to-use exploit against a named real product. |

## Required Checks

- [x] Lesson opens with a realistic near-miss (Harborview Claims' single-attempt "verified" claim) rather than jargon, and explicitly recaps — not re-derives — all seven defenses named across Chapters 3–4 before introducing the evaluation methodology.
- [x] Lesson names precisely why "we added a defense" isn't a stopping point: the single-attempt trap, and the subtler "tested several times but never adapted" trap, each grounded in Chapter 3's own combinatorial taxonomy and Chapter 4's own adaptive-attack citation.
- [x] Lesson builds a real, four-step evaluation methodology (corpus construction with multiple variants per family across both taxonomies plus a benign control set; controlled with/without comparison; real numbers including false positives; mandatory Step 4 adversarial iteration) — not a re-description of Chapters 3–4's defenses.
- [x] Lesson names a three-category defense taxonomy (structural / detection / consequence-bounding) with each category's genuinely different real evaluation question, and explicitly names the common mistake of applying one metric uniformly across all three.
- [x] Lesson includes an honest limits discussion citing Chapters 3–4's own already-verified provider research (OpenAI's Instruction Hierarchy paper, Anthropic's guardrails documentation, the sandwich-prompting adaptive-attack research), framed as the field's own stated position, not a course-specific caveat.
- [x] Lesson includes a worked evaluation example (the Anchorline Support hands-on-lab section) that walks the full methodology's structure against a real target, with an honest, explicit live-testing disclosure directly in the lesson text itself, not just the audit.
- [x] Lesson includes a GenAI Builder Thought Process section and a Points to Remember recap that also explicitly closes out Module 2, matching Chapters 1–4's pattern.
- [x] Interview-questions callout box is present on `lesson.html` (linking to `interview-questions.html`) — verified present.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`) is present on `lesson.html`, `interview-questions.html` (verified via prior-session content, re-checked this session), and `project/index.html` (added this session) — verified present in all three by direct read.
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (4 present). Verified by direct execution: `solution.py` scores 27/27, `starter.py` reports 0/27 cleanly.
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 8 distinct fictional systems). Verified by direct execution: `solution.py` scores 9/9, `starter.py` reports 0/9 cleanly.
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves — verified present by direct read of `interview-questions.html`/`.md` this session.
- [x] Project ships a real, substantive lab — a defense-evaluation harness with a real, multi-variant corpus, real blocked/succeeded/false-positive computation, a genuine Step 4 adversarial round, and a Category 3 consequence-bounding check that is structurally independent of the tell-check results — explicitly distinguished in its own text from Module 2's official Level 2 milestone project.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought).
- [x] Navigation follows lesson → quiz → exercises → practice → interview → project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file (script-checked this session; 0 broken links).
- [x] Content is original — no wording, examples, or structure reused from Chapters 1–4 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted, per the ecosystem's structural-reference convention.
- [x] Every technique discussed is framed defensively: every taxonomy entry, methodology step, and worked example is framed as measuring or applying a real, working defense; no example is presented as unsolved; no content targets a named real-world product; every scenario is stated as explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 2, Advanced, closing chapter) matches the roadmap table exactly; the "what a defense actually stops versus what it claims to stop" framing from the curriculum map is the literal thesis of the lesson's taxonomy section, not a reworded substitute.
- [x] `assets/chapters-data.js` updated this session: chapter-05 entry now has `path: "chapters/chapter-05-evaluating-prompt-injection-defenses-honestly/lesson.html"`. Module 2's `examPath` left `null` per task instruction — the module-2 written exam is a separate, not-yet-started task. No other part of the file was touched (diff-checked before and after edit).
- [x] `python3 -m py_compile` run on every `.py` file in this chapter this session (6 files: `exercises/starter.py`, `exercises/solution.py`, `practice/starter.py`, `practice/solution.py`, `project/starter.py`, `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed this session (not just compiled): `exercises/solution.py` scores 27/27, `exercises/starter.py` reports 0/27 cleanly (expected, TODOs unfilled by design); `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9 cleanly; `project/solution.py`'s `verify_logic()` self-test scores 21/21 and its graceful-degradation path (openai not installed in this sandbox) exits 0 cleanly; `project/starter.py`'s self-test correctly reports 3/21 (only the three "declined"/"helped normally" synthetic cases pass by construction since the unfilled stub functions all return `False`; every "succeeded" case and every consequence-bounding check correctly fails against the stubs, proving the self-test harness itself discriminates real logic from stubs) and also exits 0 cleanly.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output ended with "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a standalone Python link-walker script (not just `local_check.sh`'s chapter-path check) across all 6 HTML files in this chapter folder this session: 0 broken `href`/`src` targets.

## Live-Tested vs. Logical-Only Content Disclosure

This is the most important section of this audit, more so than in either
Chapter 3's or Chapter 4's audit, given this chapter's own subject
matter: a chapter whose entire thesis is "measure a defense's real
effectiveness, don't just describe it" would be self-undermining if its
own project's numbers were silently overclaimed. Broken down precisely,
claim by claim.

### The Ollama environment issue — re-confirmed this session with live attempts, not assumed from prior sessions

Before writing any of this chapter's project code, this session ran its
own independent live-verification attempts, per the task's explicit
instruction to try live verification briefly before falling back to the
disclosure pattern:

1. `curl -s -m 5 http://localhost:11434/api/tags` — responded normally
   and immediately: `{"models":[{"name":"llama3.2:latest", ...
   "parameter_size":"3.2B", ...}]}`. Confirms the model is pulled and
   the server process itself is up and responsive for non-generation
   endpoints.
2. `curl -s -m 12 -X POST http://localhost:11434/api/chat -H
   "Content-Type: application/json" -d '{"model":"llama3.2","messages":
   [{"role":"user","content":"Say OK"}],"stream":false}'` — timed the
   full 12-second timeout, `real 0m12.011s`, returned no response body,
   `curl` exit code 28 (operation timed out). This exactly matches the
   persistent, previously-disclosed, sandbox-wide pattern found across
   Chapters 3 and 4 of this course (and five prior sessions in
   `ai-coding-agents-for-everyone`), now independently re-confirmed a
   third time in this course specifically, with a fresh, short-timeout
   attempt rather than assumed from the prior two chapters' disclosures.
3. `python3 -c "import openai"` — raised `ModuleNotFoundError: No module
   named 'openai'`, confirming the `openai` Python package is not
   installed in this sandbox (also confirmed via `pip show openai`
   reporting "Package(s) not found"). This means `project/solution.py`
   and `project/starter.py` both hit the graceful-degradation path's
   `ImportError` branch before even attempting a network call — the raw
   `curl` timeout above was still run and disclosed independently,
   because it's the more fundamental confirmation (it rules out "maybe
   it would have worked if the package were installed") and because
   Chapters 3–4's own audits used the same reasoning.

### What WAS live-tested this session (real execution, real output observed)

- **`project/solution.py`'s `verify_logic()` function** — executed
  directly, produced real console output, and all 21 of its checks
  passed: 6 synthetic tell-check cases (one "succeeded" and one
  "declined"/"helped normally" case for each of the three tell
  functions) plus 15 consequence-bounding checks, one per malicious
  corpus entry, each confirming `consequence_bounding_check()` returns
  `True` (contained) using only `entry["target_user"]` and
  `SESSION_USER_ID` — no model text involved in this check at all,
  by construction.
- **`project/starter.py`'s `verify_logic()` function**, with every TODO
  still blank — executed directly, correctly reported 3/21: the three
  cases that pass by construction (the unfilled stub tell functions
  return `False`, matching the "declined"/"helped normally" expectation)
  passed; every "succeeded" case and every consequence-bounding check
  (which defaults to `False`, not the expected `True`, in the unfilled
  stub) correctly failed — confirming the self-test harness genuinely
  discriminates real logic from stubs rather than passing trivially.
- **Both scripts' graceful-degradation path** — both hit the `openai`
  `ImportError` branch, both printed a clear message ("The openai
  package isn't installed..."), both exited with code 0 (confirmed via
  `echo "exit:$?"` after each direct run) — no hang, no traceback, in
  either file.
- **`exercises/solution.py`** (27/27) and **`practice/solution.py`**
  (9/9) — fully self-contained, no network dependency by design (pure
  classification/reasoning exercises), executed directly this session
  with real output matching every claim in this audit and in each
  `README.md`. `exercises/starter.py` (0/27) and `practice/starter.py`
  (0/9) were also executed directly, confirming clean, non-crashing
  behavior with TODOs unfilled.
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session, not assumed from template convention: 0 broken links.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session, all 6 checks passed, ending with "All
  local checks passed. Safe to push."
- **`python3 -m py_compile`** on all 6 `.py` files in this chapter —
  executed directly this session, all compiled cleanly.

### What is logical-only, NOT live-verified against a real model this session

- **The real undefended-vs-defended block-rate and benign
  false-positive numbers** (`project/`'s Reports A and B) — the live
  code path (`build_report`/`run_corpus` calling
  `client.chat.completions.create(...)`) was never reached this session,
  because the `openai` package's `ImportError` branch fired first, and
  independently, the network-level generation hang was already
  confirmed via raw `curl`. The corpus itself, the tag/sandwich defense
  implementation, and the tell-check logic that WOULD process any real
  response are all verified correct (see above) — only the actual
  numbers a live model would produce were not observed.
- **The Step 4 adversarial-iteration round's real numbers**
  (`project/`'s Report C) — same reason. `adapt_for_recency()`'s
  transformation logic is grounded directly in Chapter 4's own cited
  sandwich-prompting adaptive-attack research (restating the malicious
  instruction as close as possible to generation time, targeting the
  defense's own recency-effect assumption), but no adapted entry was
  actually run against a live model this session, so no specific
  before/after adaptive-round success-rate number is claimed anywhere.
- **Report D's full-corpus consequence-bounding sweep as it would run
  inside `main()` against live model responses** — the pure-logic
  version of `consequence_bounding_check()` was verified directly (21/21
  above, exercising it against every corpus entry), but the specific
  end-to-end claim "the check holds even for the rows where a live
  model's tell fires" was not observed this session, because no live
  model call happened at all inside `main()`'s live branch. The lesson's
  own Section 7 text states this limitation explicitly rather than
  implying the full report was actually produced.
- **All worked-example numbers in `lesson.html`'s Section 7** (the
  hands-on lab walkthrough) — explicitly framed in the lesson text
  itself as "a representative, mechanism-grounded illustration of what
  the harness's methodology measures," never as "the actual result I
  observed this session," consistent with this chapter's own thesis
  applied reflexively to its own disclosure.
- **The general, field-level claim that structural defenses produce a
  real, non-trivial success-rate reduction while remaining vulnerable to
  adaptive iteration** (Section 6 of `lesson.html`) — this is Chapters
  3–4's own already-verified citation claim, carried forward and
  explicitly not re-presented as a number measured against the specific
  installed model this session.

### Research citations — inherited, not re-derived or restated inaccurately this session

This chapter does not introduce new external research citations beyond
what Chapters 3–4 already independently verified via live web search in
their own sessions (OpenAI's Instruction Hierarchy paper, arXiv:2404.13208;
Anthropic's guardrails documentation and agentic/browser-use
prompt-injection research; the sandwich-prompting adaptive-attack
research). This session's own contribution was cross-checking, not
re-researching: `lesson.html`'s Section 6 text was read side-by-side
against Chapters 3–4's own citation sections during this session's review
pass to confirm the framing (risk reduction, not elimination; partial
effectiveness, not a solved problem; very high adaptive-attack success
rates specifically once the defense is known) is preserved accurately
rather than drifted or overstated in the retelling — confirmed accurate.

## Follow-Up Tasks

- Re-run `project/solution.py` and `project/starter.py` against a real,
  responsive Ollama server (or a hosted-provider swap, per this course's
  documented Model/API policy) the moment this sandbox's known
  generation-hang issue is resolved, and update this audit's disclosure
  section with the real Reports A–D once observed — this is the one
  specific, named gap this chapter is carrying forward, matching
  Chapters 3–4's identical open item.
- Human review of whether Report D's consequence-bounding claim (blast
  radius stays contained even where the tell fires) actually holds once
  measured against real model responses — the harness's pure logic is
  verified correct and is structurally independent of the model's text
  by design, but the end-to-end claim as a whole hasn't been observed
  against a live model yet.
- With Chapter 5 now complete, Module 2 (Chapters 3–5) is fully built.
  Per `AI_HANDOFF.md`/`PROJECT_STATE.md`, the next task is Module 2's
  written exam (`assessments/written-exams/module-2-exam.html` + `.md`,
  using `templates/written-exam.template.html`) — the "injection-
  construction + defense-evaluation exam" per the curriculum map —
  explicitly not started this session per the task's own instruction.
  Once that exam exists, Module 2's `examPath` in
  `assets/chapters-data.js` should be updated from `null` to the real
  path (a separate task).
- After the Module 2 exam, Module 3 (Chapters 6–8: data poisoning, model
  extraction, supply chain) begins, continuing the same module-by-module
  build-then-validate discipline this and every prior chapter followed.
