# Chapter Quality Audit: Direct Prompt Injection

## Summary

- Chapter: 3 — Direct Prompt Injection (Module 2, Intermediate) — starts Module 2
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-11
- Status: Ready for human review
- Note: structure adapted from `quality-audits/chapter-01-audit.md` and
  `chapter-02-audit.md` (structure only; no content reused). This is the
  **first chapter in this course with a live-model dependency** — see the
  dedicated "Live-Tested vs. Logical-Only Content Disclosure" section
  below, which is the single most important part of this audit given the
  model-access constraint disclosed in the task itself.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Meridian Notes / Concierge, a tool-free support widget) is the simplest possible version of the mechanism — no tools, no data round trip, just an attacker typing directly into a chat box — deliberately contrasted against Chapter 1's indirect GreenCart hook and Chapter 2's multi-tool Waypoint hook. Explicitly recaps, rather than re-derives, Chapter 1's direct-vs-indirect preview before going deep. |
| Production depth | Pass | Goes beyond a definition-and-example treatment: a precise mechanism section (token-stream framing, role-weighting-as-tendency-not-wall, a diagram contrasting traditional code/data separation against an LLM's single token stream), a five-family taxonomy each with mechanism + example + why-it-works, and four paired defenses each with an explicit "what this stops" / "what it doesn't stop" split rather than an unqualified claim. |
| Real-time framework accuracy | Pass | Provider-guidance claims (OpenAI's Instruction Hierarchy research, Anthropic's XML-tag structuring and guardrails documentation) were independently researched this session via web search against OpenAI's and Anthropic's own published sources (see citations below) — not recalled from training-data memory, and not overclaimed: both are cited as risk-reduction, explicitly not as solved-problem claims, matching each source's own stated framing. |
| Architecture and diagrams | Pass | A dedicated ASCII diagram contrasts a traditional program's code/data separation against an LLM's single shared token stream — the chapter's central mechanism claim made visual, not just asserted in prose. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — defense evaluation, defense-in-depth reasoning, bounded-consequence rule design, provider-guidance matching, and a defense-layer completeness gate. Fresh scenario (HelixCare Intake, a telehealth intake assistant) distinct from the lesson's Meridian Notes. Automated scoring harness; `solution.py` verified to score a perfect 24/24 by direct execution. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems, none reused from the lesson or exercises. Five drill fast classification across all five taxonomy families; three are judgment calls (BankAssist: does a defense posture with structural separation + filtering but no bounded consequence still have a real gap; StudyBuddy: prioritize between two unequal real risks; ConciergeDesk: production-gear full mapping of technique + highest-leverage defense). Automated scoring harness; `solution.py` verified to score a perfect 9/9 by direct execution. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), each with strong answer, red flag, follow-up, and "what this proves" — verified present for all 8 by direct reading of `interview-questions.md`/`.html`. Question 8 is specifically built around this chapter's own live-verification disclosure practice, testing whether a learner recognizes honest verification-status disclosure as a security-relevant practice in its own right, not a process footnote. |
| Project implementation | Pass | A real, substantive hands-on lab (not the official Module 2 Level 2 project, which the curriculum map states ships after Chapter 5 once defense evaluation is covered — `project/index.html` states this distinction explicitly): a red-team harness against Harbor Desk (a new, tool-free target distinct from the lesson's Meridian Notes and the exercises' HelixCare Intake) that constructs one attempt per taxonomy family, applies Defense 1 (structural separation) and Defense 2 (keyword pre-filter) and re-tests, and separates its judgment logic (`verify_tell_checks()`, pure, network-free, self-tested against synthetic labeled strings) from its live-model half (graceful degradation, `timeout=8.0`, exits 0 cleanly on any connect/timeout failure) — both halves independently executed this session, see disclosure below. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific over-narrow reading of Defense 3 (assuming "no tools" means "no real risk"), why that's wrong (brand/compliance/reputational stakes independent of tool access), why this matters for Chapter 4, and a working definition of direct injection carried forward. |
| Navigation/template consistency | Pass | lesson -> quiz -> exercises -> practice -> interview-questions -> project chain verified programmatically: every `href`/`src` across all 6 HTML files in this chapter folder resolves to a real file on disk (script-checked with a Python link-walker against the filesystem; 0 broken links out of every `href`/`src` scanned). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, scenario-card, badge-coming-soon, page-toc, subtopic, diagram-figure); no invented CSS, matching Chapters 1–2. |
| Public artifact readiness | Pass | No placeholder text (`local_check.sh`'s placeholder-text scan passed). All content original — no wording, examples, or structure reused from Chapters 1–2 or any sibling TechNaom repo. Every fictional system (Meridian Notes/Concierge, HelixCare Intake, Harbor Desk, and all practice-bank systems) is explicitly invented; no named real product is targeted by any example. |

## Required Checks

- [x] Lesson opens with the simplest possible version of the mechanism (a tool-free, single-turn direct injection against Concierge/Meridian Notes) rather than jargon, and explicitly builds on — not re-derives — Chapter 1's LLM01 direct-vs-indirect preview and trust-boundary framing.
- [x] Lesson includes a precise mechanism section: why an instruction-following model has no architectural equivalent of "code vs. data," why role-priority weighting is a trained tendency and not a hard wall, with a supporting diagram.
- [x] Lesson includes a taxonomy of at least 4–5 real direct-injection technique families, each with mechanism + example + why-it-works — five families shipped (role-play/persona override, instruction override, context/scope confusion, payload obfuscation, multi-turn/gradual escalation), exceeding the stated minimum.
- [x] Every technique is paired with a real, working defense: structural separation, input/output filtering with its real limits explicitly stated, "never let model judgment alone gate a consequential action" (tied explicitly back to Chapter 1's LLM06 Excessive Agency), and instruction-hierarchy/system-prompt hardening backed by real, cited, independently-researched current provider documentation (OpenAI, Anthropic).
- [x] No technique is presented as a ready-to-use exploit against a named real product — every scenario (Meridian Notes, HelixCare Intake, Harbor Desk, and all practice-bank systems) is explicitly fictional; every taxonomy example is framed as mechanism, not a working payload against a real target.
- [x] Hands-on lab: a lesson section walks the harness structure and honestly discloses the live-testing gap; the full harness ships in `project/`, constructing real injection attempts against a real target with a working (though not live-verified this session) path to run against Ollama, and a fully live-verified graceful-degradation path.
- [x] Lesson includes a GenAI Builder Thought Process section and Points to Remember recap, matching Chapters 1–2's pattern.
- [x] Interview-questions callout box is present on `lesson.html` (linking to `interview-questions.html`) — verified present.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`) is present on `lesson.html`, `interview-questions.html`, and `project/index.html` (matching Chapters 1–2's convention of carrying the footer link on these specific pages) — verified present in all three files by direct read.
- [x] Exercises include at least 6 tasks (8 present), with at least 3 production-gear tasks (5 present).
- [x] Practice bank includes at least 6 realistic scenarios (8 present, across 8 distinct fictional systems).
- [x] Interview bank includes at least 8 questions (8 present) spanning beginner/intermediate/senior/architect (2 each), each with strong answer, red flag, follow-up, and what this proves.
- [x] Project ships a real, substantive lab — a red-team harness with graceful degradation, a defense applied and re-tested, and a report — explicitly distinguished in its own text from Module 2's official Level 2 milestone project (ships after Chapter 5 per the curriculum map).
- [x] Chapter includes diagrams/visual-text architecture aids (the code-vs-data / shared-token-stream diagram in Section 3).
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process section, visible reasoning not hidden chain-of-thought).
- [x] Navigation follows lesson -> quiz -> exercises -> practice -> interview -> project. Every internal link across all 6 HTML pages in this chapter folder programmatically verified to resolve to a real file (script-checked; 0 broken links).
- [x] Content is original — no wording, examples, or structure reused from Chapters 1–2 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted, per the ecosystem's structural-reference convention.
- [x] Every attack/vulnerability discussed is framed defensively: every taxonomy entry in the lesson is paired with a defense in the same chapter; no example is presented as unsolved; no content targets a named real-world product; every scenario is stated as explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md` and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 2, Intermediate, starts Module 2) matches the roadmap table exactly; direct-vs-indirect framing matches Chapter 1's preview verbatim rather than introducing a conflicting definition.
- [x] `assets/chapters-data.js` updated: chapter-03 entry now has `path: "chapters/chapter-03-direct-prompt-injection/lesson.html"`. Module 2's `examPath` left `null`, per task instruction — the curriculum map's stated Module 2 assessment type ("injection-construction + defense-evaluation exam") suggests a real written exam once Chapters 3–5 are all complete, not yet; no other part of the file touched.
- [x] `python3 -m py_compile` run on every `.py` file in this chapter (6 files: `exercises/starter.py`, `exercises/solution.py`, `practice/starter.py`, `practice/solution.py`, `project/starter.py`, `project/solution.py`) — all compile cleanly.
- [x] Every `solution.py`/`starter.py` in this chapter actually executed (not just compiled): `exercises/solution.py` scores 24/24, `exercises/starter.py` reports 0/24 cleanly (expected, TODOs unfilled by design); `practice/solution.py` scores 9/9, `practice/starter.py` reports 0/9 cleanly; `project/solution.py`'s `verify_tell_checks()` self-test scores 10/10 and its graceful-degradation path (openai not installed in this sandbox) exits 0 with a clear message; `project/starter.py`'s self-test correctly reports 5/10 (the five "decline" synthetic cases pass by construction since the unfilled tell functions all return `False`; the five "succeeded" cases correctly fail, proving the self-test harness itself discriminates real logic from stubs) and also exits 0 cleanly.
- [x] `bash scripts/local_check.sh < /dev/null` run from the repo root after adding these files — all 6 checks (required folders, placeholder-text scan, Python syntax, solution.py execution, JS syntax + chapter-path validation, secret scan) passed. Full output ended with "All local checks passed. Safe to push."
- [x] Internal link resolution verified separately and explicitly with a standalone Python link-walker script (not just `local_check.sh`'s chapter-path check) across all 6 HTML files in this chapter folder: 0 broken `href`/`src` targets.

## Live-Tested vs. Logical-Only Content Disclosure

This is the most important section of this audit, given this chapter's
subject matter and the environment constraint disclosed in the task.
Broken down precisely, claim by claim:

### The Ollama environment issue — re-confirmed this session, not assumed

At the start of this session, the local Ollama server's `/api/tags`
endpoint responded normally (`llama3.2:latest`, 3.2B parameters,
confirmed pulled and available). A direct, non-tool generation request
against `/api/chat` (via raw `curl`, not even the `openai` client layer)
was attempted with a 20-second timeout and returned `HTTP:000` after the
full 20 seconds elapsed (`curl` exit code 28, timeout) — the server
accepted the connection but never returned a response. This exactly
matches the persistent, previously-disclosed, sandbox-wide pattern
described in the task ("server reachable, generation hangs
indefinitely") across at least five prior build sessions in the sibling
`ai-coding-agents-for-everyone` repo. A second attempt was not made
beyond this, per the task's own instruction not to burn excessive time
retrying a confirmed hang. **This chapter's `project/solution.py` and
`project/starter.py` were also run directly this session** (see below)
and both hit the `openai` package's own `ImportError` branch before
even reaching the network call, because the `openai` Python package is
not installed in this sandbox and could not be installed
(`pip install openai` failed under this environment's externally-managed
Python restriction, and a project-local venv was not created since the
network-level hang was already independently confirmed via raw `curl`
first, making a second, package-mediated confirmation unnecessary).

### What WAS live-tested this session (real execution, real output observed)

- **`project/solution.py`'s `verify_tell_checks()` function** — executed
  directly, produced real console output, and every one of its 10
  synthetic self-test cases passed (5 "injection succeeded" cases, 5
  "model correctly declined" cases). This is the actual judgment logic
  of the harness (does a given response text count as a successful
  injection) — verified correct, independent of any live model call.
- **`project/solution.py`'s and `project/starter.py`'s graceful-
  degradation path** — both executed directly under `timeout 20`, both
  hit the `openai` `ImportError` branch, both printed a clear message,
  and both exited with code 0 (confirmed via `echo "EXIT:$?"` after each
  run) — no hang, no traceback. This is the actual, tested behavior this
  chapter's text and README promise, not an assumed one.
- **`exercises/solution.py`** (24/24) and **`practice/solution.py`**
  (9/9) — fully self-contained, no network dependency by design (pure
  classification/reasoning exercises), executed directly with real
  output matching every claim in this audit and in each `README.md`.
- **Every internal link** across all 6 HTML files — checked with a
  standalone filesystem-walking script, not assumed from template
  convention.
- **`bash scripts/local_check.sh`** — executed directly from the repo
  root, all 6 checks passed.

### What is logical-only, NOT live-verified against a real model this session

- **Every taxonomy example transcript in `lesson.html`'s Section 4**
  (the five technique families) — these describe the well-established,
  publicly-documented mechanics of instruction-following models (how
  role-play framing, explicit override language, fake-authority
  formatting, encoding-based obfuscation, and multi-turn context-
  building each interact with a model's next-token prediction). They
  are framed in the lesson text itself as mechanism explanations, not
  as "output I personally observed this session" — no specific quoted
  model *response* is presented anywhere in this chapter as something
  actually generated by `llama3.2` this session, precisely because none
  was.
- **The specific claim that `llama3.2`'s 3B-parameter size makes it
  more susceptible to direct injection than larger, more heavily
  safety-tuned models** (Section 6 of `lesson.html`) — stated as a
  general, documented pattern in the literature on model size and
  safety-tuning robustness, explicitly NOT as a measured result against
  the specific installed model this session, and the lesson text says so
  directly ("a representative, mechanism-grounded expectation, not a
  claim about this specific installed model's measured behavior this
  session").
- **`project/solution.py`'s and `project/starter.py`'s live
  naive-vs-hardened report** (the actual comparison of how many of the
  five constructed attempts succeed against the naive system prompt
  versus the hardened one) — this code path was never reached this
  session, because the `openai` package's `ImportError` branch fired
  first (and, independently, the network-level hang was already
  confirmed via raw `curl`). This is the one genuine, load-bearing gap
  in this chapter's live verification, and it is disclosed explicitly in
  three places: this audit, `lesson.html`'s Hands-On Lab section, and
  `project/README.md`'s "An honest note on live verification" section —
  deliberately redundant, since this is the single claim in the chapter
  most at risk of being silently overclaimed.
- **The OWASP Top 10 category references** (LLM01, LLM06) used to tie
  this chapter back to Chapter 1 — inherited from Chapters 1–2's
  already-verified framework claims, not re-verified independently this
  session (no new claim about the framework's edition/ranking is made
  in this chapter).

### Provider-guidance citations — independently researched this session, not recalled from memory

Per the task's explicit instruction to research real, current provider
documentation rather than assume it, three live web searches were run
this session:

1. OpenAI's Instruction Hierarchy research — confirmed via
   `openai.com/index/the-instruction-hierarchy` and the underlying paper
   (Wallace et al., "The Instruction Hierarchy: Training LLMs to
   Prioritize Privileged Instructions," arXiv:2404.13208): system
   message, then developer message, then user message, with tool
   outputs/retrieved content/quoted text carrying no default authority
   unless explicitly elevated.
2. Anthropic's Claude documentation on structuring prompts —
   `platform.claude.com`'s "Use XML tags to structure your prompts" and
   "Mitigate jailbreaks and prompt injections" pages: XML-tag delimiting
   of untrusted content, treating tool-result content as inherently
   untrusted, input/output screening guidance.
3. Anthropic's published research on prompt-injection defenses in
   agentic/browser-use contexts — `anthropic.com/research/prompt-
   injection-defenses`: explicitly reports partial effectiveness (not
   elimination) and frames prompt injection as an active, ongoing
   research area.

All three are cited in `lesson.html`'s Defense 4 with accurate framing
(risk-reduction, not solved-problem) matching each source's own stated
position — verified by reading the search results directly, not
inferred from a general sense of "the providers probably do something
like this."

## Follow-Up Tasks

- Re-run `project/solution.py` and `project/starter.py` against a real,
  responsive Ollama server (or a hosted-provider swap, per this course's
  documented Model/API policy) the moment this sandbox's known
  generation-hang issue is resolved, and update this audit's disclosure
  section with the real naive-vs-hardened report once observed — this is
  the one specific, named gap this chapter is carrying forward.
- Human review of whether `llama3.2`'s specific susceptibility profile
  (once actually measurable) changes any of this chapter's example
  framing or its Defense 3 emphasis.
- With Chapter 3 now complete, the next task per `AI_HANDOFF.md` is
  Chapter 4 (Indirect Prompt Injection and Jailbreaking Techniques) —
  it should build on this chapter's mechanism section directly (the same
  underlying vulnerability, different delivery channel) rather than
  re-deriving it, per this chapter's own GenAI Builder Thought Process
  section.
- Once Chapters 3–5 are all complete, build Module 2's written exam
  (`examPath`, currently `null`) per the curriculum map's stated
  "injection-construction + defense-evaluation exam" assessment type —
  explicitly not started this session per the task's own instruction.
