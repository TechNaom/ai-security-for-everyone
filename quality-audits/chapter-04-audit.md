# Chapter Quality Audit: Indirect Prompt Injection and Jailbreaking Techniques

## Summary

- Chapter: 4 — Indirect Prompt Injection and Jailbreaking Techniques (Module 2, Advanced)
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-11
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-03-audit.md` (structure
  only; no content reused). This is the **second chapter in this course with a
  live-model dependency** — see the dedicated "Live-Tested vs. Logical-Only
  Content Disclosure" section below, following exactly the disclosure
  discipline Chapter 3 established.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Northline Digest, an internal RAG-based wiki assistant) is built specifically to contrast against Chapter 3's Concierge example: the "attacker" (a contractor who edited a wiki page three weeks earlier) and the victim (an unrelated employee asking an unrelated question) never intersect. Explicitly recaps, rather than re-derives, GreenCart (Ch1) and Waypoint (Ch2) as already-seen indirect-injection instances before going deep. |
| Production depth | Pass | Goes beyond a definition-and-example treatment: a precise mechanism section extending Chapter 3's diagram to show decoupled attacker/victim timing, a five-channel delivery taxonomy (independent axis from Chapter 3's technique-family taxonomy, explicitly stated as such), a dedicated jailbreaking section precisely distinguishing it from injection with three technique categories beyond Chapter 3's DAN mention, and four defenses each extending Chapter 3's into the indirect/jailbreak context with explicit "what this stops / what it doesn't stop" splits. |
| Real-time framework accuracy | Pass | Every non-obvious factual claim was independently verified via live web search this session (not recalled from training-data memory): OWASP Top 10 for LLM Applications' (2025) indirect-injection definition; Zou et al.'s adversarial-suffix paper (arXiv:2307.15043); Wei, Haghtalab, and Steinhardt's "Jailbroken" paper naming competing objectives and mismatched generalization (arXiv:2307.02483); the documented "sandwich defense" pattern including its real, published limitation under adaptive attacks; and documented real-world multi-modal/OCR hidden-text injection patterns. See citations section below. |
| Architecture and diagrams | Pass | A dedicated ASCII diagram contrasts Chapter 3's direct-injection flow against this chapter's indirect flow, visually showing the decoupled attacker/victim timing that's this chapter's central claim. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — defense evaluation, defense-in-depth reasoning, bounded-consequence rule design, research citation matching, and a defense-layer completeness gate. Fresh scenario (ClearDesk Legal, a contract-review assistant) distinct from the lesson's Northline Digest. Automated scoring harness; `solution.py` verified to score a perfect 23/23 by direct execution; `starter.py` verified to report 0/23 cleanly. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson or exercises. Five drill fast classification across all five delivery channels; three are judgment calls (VaultAssist: whether injection defenses touch a directly-attempted jailbreak at all; StreamMod: prioritize between two unequal real risks; HelpDeskGenie: production-gear full mapping of channel + highest-leverage defense). Automated scoring harness; `solution.py` verified to score a perfect 9/9 by direct execution; `starter.py` verified to report 0/9 cleanly. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), each with strong answer, red flag, follow-up, and "what this proves" — verified present for all 8 by direct authoring and cross-check against `interview-questions.md`/`.html`. Question 8 is built around the adversarial-suffix research and its architectural implications; Question 6 tests whether a learner can catch an overclaimed "jailbreak-resistant" conclusion from an incomplete red-team test matrix. |
| Project implementation | Pass | A real, substantive hands-on lab (not the official Module 2 Level 2 project, which the curriculum map states ships after Chapter 5 — `project/index.html` states this distinction explicitly): a harness against Solstice Support (a new target distinct from the lesson's Northline Digest and the exercises' ClearDesk Legal) that constructs one indirect attempt per THREE delivery channels (RAG, tool output, web content) PLUS one direct jailbreak attempt (refusal suppression, no injected content), applies content-provenance tagging (Defense 1) and sandwich reinforcement (Defense 2), and deliberately demonstrates that neither defense touches the direct jailbreak row — both halves (pure judgment logic and graceful degradation) independently executed this session, see disclosure below. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (conflating "we defended against injection" with "we defended against jailbreaking" because both defenses shipped in the same effort), why that's wrong, why this matters before Chapter 5's defense-evaluation discipline, and a working definition of both indirect injection and jailbreaking carried forward. |
| Navigation/template consistency | Pass | lesson -> quiz -> exercises -> practice -> interview-questions -> project chain verified programmatically: every `href`/`src` across all 6 HTML files in this chapter folder resolves to a real file on disk (script-checked with a Python link-walker against the filesystem; 0 broken links out of every `href`/`src` scanned). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic, diagram-figure); no invented CSS, matching Chapters 1–3. |
| Public artifact readiness | Pass | No placeholder text (`local_check.sh`'s placeholder-text scan passed). All content original — no wording, examples, or structure reused from Chapters 1–3 or any sibling TechNaom repo. Every fictional system (Northline Digest, ClearDesk Legal, Solstice Support, and all practice-bank systems) is explicitly invented; no named real product is targeted by any example. Every jailbreak technique category is framed as documented mechanism, never as a working payload against a named real product, per this course's non-negotiable ethical framing. |

## Required Checks

- [x] Lesson opens with the simplest possible version of the indirect-delivery mechanism (Northline Digest's RAG-retrieved planted wiki note, decoupled from the victim's session by three weeks and an unrelated employee) rather than jargon, and explicitly builds on — not re-derives — Chapter 3's shared-token-stream mechanism and the already-seen GreenCart/Waypoint indirect-injection instances from Chapters 1–2.
- [x] Lesson includes a precise mechanism section explaining what changed (delivery channel, decoupled attacker/victim timing/identity) and what didn't (the underlying shared-token-stream vulnerability), with a supporting diagram contrasting direct vs. indirect flow.
- [x] Lesson includes a taxonomy of 4–5 real indirect-injection delivery channels, each with mechanism + example + why-it-works — five channels shipped (retrieved documents/RAG, tool/API output, web content, email/document content, multi-modal), exceeding the stated minimum, explicitly framed as a distinct axis from Chapter 3's technique-family taxonomy.
- [x] Lesson covers jailbreaking as a related but distinct concept: precisely defines the injection/jailbreak distinction, names real technique categories beyond Chapter 3's DAN mention (hypothetical/fictional framing at depth, competing-objectives exploitation, refusal-suppression patterns), and covers non-injection jailbreak mechanisms (adversarial suffixes) with an accurately-cited, independently-researched source.
- [x] Every technique is paired with a real, working defense: content provenance/tagging (operationalizing Chapter 2's Step 3 trust classification as a three-way technical control), sandwich/reinforcement prompting (with its real, documented limitation under adaptive attacks explicitly stated), output-based jailbreak/injection detection, and bounding the blast radius (explicitly argued as mattering MORE here, not just as much, since an indirect attacker may never interact with the victim's session at all).
- [x] No technique is presented as a ready-to-use exploit against a named real product — every scenario (Northline Digest, ClearDesk Legal, Solstice Support, and all practice-bank systems) is explicitly fictional; every jailbreak category and delivery-channel example is framed as mechanism, not a working payload against a real target.
- [x] Hands-on lab: a lesson section walks the harness structure (three delivery channels plus one direct jailbreak attempt) and honestly discloses the live-testing gap; the full harness ships in `project/`, constructing real multi-channel attempts against a real target with a working (though not live-verified this session) path to run against Ollama, and a fully live-verified graceful-degradation path.
- [x] Lesson includes a GenAI Builder Thought Process section and Points to Remember recap, matching Chapters 1–3's pattern.
- [x] Interview-questions callout box is present on `lesson.html` (linking to `interview-questions.html`) — verified present.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`) is present on `lesson.html`, `interview-questions.html`, and `project/index.html` (matching Chapters 1–3's convention) — verified present in all three files by direct grep.
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (5 present).
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 8 distinct fictional systems).
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves.
- [x] Project ships a real, substantive lab — a multi-channel harness with graceful degradation, defenses applied and re-tested, and a report that explicitly demonstrates the injection/jailbreak distinction — explicitly distinguished in its own text from Module 2's official Level 2 milestone project (ships after Chapter 5 per the curriculum map).
- [x] Chapter includes diagrams/visual-text architecture aids (the direct-vs-indirect flow diagram in Section 3).
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought).
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file (script-checked; 0 broken links).
- [x] Content is original — no wording, examples, or structure reused from Chapters 1–3 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted, per the ecosystem's structural-reference convention.
- [x] Every attack/vulnerability discussed is framed defensively: every taxonomy entry and jailbreak category in the lesson is paired with a defense in the same chapter; no example is presented as unsolved; no content targets a named real-world product; every scenario is stated as explicitly fictional; jailbreak technique descriptions describe mechanism only, never a working payload.
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 2, Advanced) matches the roadmap table exactly; indirect-injection and jailbreak framing matches Chapter 3's setup verbatim rather than introducing a conflicting definition.
- [x] `assets/chapters-data.js` updated: chapter-04 entry now has `path: "chapters/chapter-04-indirect-prompt-injection-and-jailbreaking-techniques/lesson.html"`. Module 2's `examPath` left `null`, per task instruction — Chapter 5 still needs to land before Module 2's exam gets built.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter (6 files: `exercises/starter.py`, `exercises/solution.py`, `practice/starter.py`, `practice/solution.py`, `project/starter.py`, `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed (not just compiled): `exercises/solution.py` scores 23/23, `exercises/starter.py` reports 0/23 cleanly (expected, TODOs unfilled by design); `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9 cleanly; `project/solution.py`'s `verify_tell_checks()` self-test scores 8/8 and its graceful-degradation path (openai not installed in this sandbox) exits 0 cleanly; `project/starter.py`'s self-test correctly reports 4/8 (the four "decline" synthetic cases pass by construction since the unfilled tell functions all return `False`; the four "succeeded" cases correctly fail, proving the self-test harness itself discriminates real logic from stubs) and also exits 0 cleanly.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output ended with "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a standalone Python link-walker script (not just `local_check.sh`'s chapter-path check) across all 6 HTML files in this chapter folder: 0 broken `href`/`src` targets.

## Live-Tested vs. Logical-Only Content Disclosure

This is the most important section of this audit, given this chapter's
subject matter and the environment constraint disclosed in the task.
Broken down precisely, claim by claim:

### The Ollama environment issue — re-confirmed this session, not assumed

At the start of this session, the local Ollama server's `/api/tags`
endpoint responded normally (`llama3.2:latest`, 3.2B parameters, confirmed
pulled and available). A direct, non-tool generation request against
`/api/chat` (via raw `curl`, not even the `openai` client layer) was
attempted with an 18-second timeout and returned `HTTP:000` after the full
timeout elapsed (`curl` exit code 28, timeout) — this exactly matches the
persistent, previously-disclosed, sandbox-wide pattern described in the
task and re-confirmed in Chapter 3's own build session, across at least
six sessions total now (five in `ai-coding-agents-for-everyone` plus
Chapter 3 of this repo). This chapter's own `project/solution.py` and
`project/starter.py` were also run directly this session (see below) and
both hit the `openai` package's own `ImportError` branch before even
reaching the network call, because the `openai` Python package is not
installed in this sandbox and could not be installed
(`ModuleNotFoundError` confirmed by direct `import openai` attempt; not
installed via `pip` since the network-level hang was already
independently confirmed via raw `curl` first, making a second,
package-mediated confirmation unnecessary — the same reasoning Chapter 3's
audit used).

### What WAS live-tested this session (real execution, real output observed)

- **`project/solution.py`'s `verify_tell_checks()` function** — executed
  directly, produced real console output, and every one of its 8
  synthetic self-test cases passed (4 "attempt succeeded" cases, 4 "the
  model correctly declined" cases, covering all three delivery-channel
  attempts plus the direct jailbreak attempt). This is the actual
  judgment logic of the harness — verified correct, independent of any
  live model call.
- **`project/solution.py`'s and `project/starter.py`'s graceful-
  degradation path** — both executed directly under a timeout, both hit
  the `openai` `ImportError` branch, both printed a clear message, and
  both exited with code 0 (confirmed via `echo "EXIT:$?"` after each
  run) — no hang, no traceback.
- **`exercises/solution.py`** (23/23) and **`practice/solution.py`**
  (9/9) — fully self-contained, no network dependency by design (pure
  classification/reasoning exercises), executed directly with real
  output matching every claim in this audit and in each `README.md`.
  `exercises/starter.py` (0/23) and `practice/starter.py` (0/9) were also
  executed directly, confirming clean, non-crashing behavior with TODOs
  unfilled.
- **Every internal link** across all 6 HTML files — checked with a
  standalone filesystem-walking script, not assumed from template
  convention.
- **`bash scripts/local_check.sh`** — executed directly from the repo
  root, all 6 checks passed.
- **Every research citation below** — verified via live web search this
  session against real, current sources (arXiv abstracts, OWASP
  documentation, and independent security-research writeups), not
  recalled from training-data memory.

### What is logical-only, NOT live-verified against a real model this session

- **Every delivery-channel example transcript in `lesson.html`'s
  Section 4** and **every jailbreak-category example in Section 5** —
  these describe well-established, publicly-documented mechanics of how
  retrieval, tool output, web-fetch, email, and multi-modal pipelines
  carry content into a model's context, and how hypothetical framing,
  competing-objectives exploitation, and refusal suppression interact
  with a model's trained safety behavior. They are framed in the lesson
  text itself as mechanism explanations, not as "output I personally
  observed this session" — no specific quoted model *response* anywhere
  in this chapter is presented as something actually generated by
  `llama3.2` this session, precisely because none was.
- **The general claim that smaller, lightly safety-tuned models are more
  susceptible across both injection and jailbreak technique families**
  (Section 7 of `lesson.html`) — stated as a documented pattern in the
  literature, explicitly not as a measured result against the specific
  installed model this session, matching Chapter 3's identical framing
  for the same underlying claim.
- **`project/solution.py`'s and `project/starter.py`'s live
  naive-vs-hardened report**, including the specific claim that the
  `jailbreak_direct` row behaves identically under both the naive and
  hardened defense modes — this code path was never reached this
  session, because the `openai` package's `ImportError` branch fired
  first (and, independently, the network-level hang was already
  confirmed via raw `curl`). This is the one genuine, load-bearing gap in
  this chapter's live verification, and it is disclosed explicitly in
  three places: this audit, `lesson.html`'s Hands-On Lab section, and
  `project/README.md`'s "An honest note on live verification" section —
  deliberately redundant, matching Chapter 3's practice, since this is
  the single claim in the chapter most at risk of being silently
  overclaimed.
- **The OWASP LLM01 category reference and the GreenCart/Waypoint
  cross-references** used to tie this chapter back to Chapters 1–3 —
  inherited from Chapters 1–3's already-verified framework claims (and,
  for OWASP's current indirect-injection definition specifically,
  independently re-verified this session — see citations below), not
  re-derived from scratch.

### Research citations — independently researched this session, not recalled from memory

Per the task's explicit instruction to research real, current sources
rather than assume them, five live web searches were run this session:

1. **OWASP Top 10 for LLM Applications (2025), LLM01 — indirect prompt
   injection**: confirmed the current definition (malicious instructions
   hidden in external content an LLM later ingests, requiring no direct
   interaction between attacker and victim session) and its staged
   attack pattern (plant, store/retrieve, innocent trigger, context
   entry, behavior change) — matches this chapter's mechanism section
   framing exactly, and is quoted directly in the lesson's `what-is` box.
2. **Zou, Wang, Carlini, Nasr, Kolter, and Fredrikson, "Universal and
   Transferable Adversarial Attacks on Aligned Language Models"**
   (arXiv:2307.15043, 2023): confirmed the paper's core method
   (gradient/greedy-search-optimized adversarial suffixes) and its
   reported transfer to production systems (ChatGPT, Bard, Claude) at
   time of publication — cited in this chapter's jailbreaking section as
   documented mechanism, explicitly noted as patched-against-since-publication
   rather than a working current payload.
3. **Wei, Haghtalab, and Steinhardt, "Jailbroken: How Does LLM Safety
   Training Fail?"** (arXiv:2307.02483, 2023): confirmed the paper's two
   named failure modes — competing objectives and mismatched
   generalization — used directly in this chapter to ground the
   hypothetical-framing and competing-objectives jailbreak categories in
   real published research rather than an invented taxonomy.
4. **The documented "sandwich defense" pattern for prompt injection**:
   confirmed both its standard structure (restating trusted instructions
   after untrusted content) and its real, published limitation —
   adaptive-attack research reporting very high success rates against
   sandwich defenses specifically when an attacker knows the defense is
   in place — used to keep this chapter's Defense 2 framing honest
   (a real, worthwhile layer, explicitly not sufficient against a
   determined, adaptive attacker) rather than overclaiming it.
5. **Documented real-world multi-modal/OCR hidden-text injection
   patterns**: confirmed publicly-documented examples (white-text-on-white-background
   instructions in uploaded documents extracted by OCR pipelines,
   low-contrast/tiny-font text embedded in images for vision-capable
   models) from independent security-research writeups — used to ground
   this chapter's multi-modal delivery-channel section in real,
   documented patterns rather than a hypothetical mechanism.

All five are cited in `lesson.html` with accurate framing (documented
mechanism/research, not solved-problem or ready-to-use-exploit claims)
matching each source's own stated position — verified by reading the
search results directly, not inferred from general familiarity with the
topic.

## Follow-Up Tasks

- Re-run `project/solution.py` and `project/starter.py` against a real,
  responsive Ollama server (or a hosted-provider swap, per this course's
  documented Model/API policy) the moment this sandbox's known
  generation-hang issue is resolved, and update this audit's disclosure
  section with the real naive-vs-hardened report once observed — this is
  the one specific, named gap this chapter is carrying forward, matching
  Chapter 3's identical open item.
- Human review of whether the `jailbreak_direct` row's expected
  behavior (identical success/failure under both naive and hardened
  defense modes) actually holds once measured against a real model —
  the harness is built to reveal this either way, but it hasn't been
  observed yet.
- With Chapter 4 now complete, the next task per `AI_HANDOFF.md` /
  `PROJECT_STATE.md` is Chapter 5 (Evaluating Prompt-Injection Defenses
  Honestly) — it should build on this chapter's and Chapter 3's paired
  "what this stops / what it doesn't stop" defense framing directly,
  turning that pattern into its own explicit evaluation methodology.
- Once Chapters 3–5 are all complete, build Module 2's written exam
  (`examPath`, currently `null`) per the curriculum map's stated
  "injection-construction + defense-evaluation exam" assessment type —
  explicitly not started this session per the task's own instruction.
