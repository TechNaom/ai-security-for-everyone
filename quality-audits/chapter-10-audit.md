# Chapter Quality Audit: Securing Agentic Systems Against Adversarial Tool Output

## Summary

- Chapter: 10 — Securing Agentic Systems Against Adversarial Tool Output
  (Module 4, Advanced) — **completes Module 4** and ships the course's
  real, final **L3 Independent project**
- Reviewer: AI build agent (self-audit at time of authoring)
- Date: 2026-08-12
- Status: Ready for human review
- Note: `lesson.html` (836 lines) was written by a prior agent session
  interrupted mid-build by a rate limit. This session read it in full
  before doing anything else, confirmed it was complete, internally
  consistent, free of truncation and leftover TODOs, and contained both
  the interview-questions callout box and the footer GitHub link — and
  built on it as-is rather than rewriting it. All other required files
  (`quiz.html`, `interview-questions.html`/`.md`,
  `exercises/{index.html,starter.py,solution.py,README.md}`,
  `practice/{index.html,starter.py,solution.py,README.md}`,
  `project/{index.html,starter.py,solution.py,README.md}`) were written
  fresh this session, plus `assets/chapters-data.js`,
  `index.html`, `docs/curriculum/index.html`, and this audit.

## Framing decision: why this chapter organizes by round-trip moment, not pipeline stage or comparison table

`lesson.html`'s own "Three Moments in a Tool-Call Round Trip" section
explicitly explains why it does not reuse Chapter 9's three-pipeline-
stage device: a RAG pipeline is architecturally a pipeline with
ingestion/retrieval/generation stages, but a tool call is a
request/response round trip, repeated potentially many times per turn,
with its own three moments (result arrival, context assembly, action
proposal) where risk enters or a defense can act. This is a genuinely
different structural device chosen because a tool call's own shape
needed its own device, not a reuse of Chapter 9's for consistency's
sake — the same precedent Chapter 8 and Chapter 9 each set for choosing
a framing device deliberately.

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| Conversational clarity | Pass | Hook (Ferngate Logistics' Dispatch Copilot, a fictional freight/last-mile-delivery dispatch assistant) makes all three round-trip moments concrete through one incident (a partner carrier API's `delivery_notes` free-text field carrying a planted instruction, nearly triggering an unauthorized `issue_reship_credit` call). New fictional org, distinct from all prior chapters' (GreenCart, Waypoint, AskHR, Anchorline, Northline Digest, Meridian, Halcyon, Solstice, Coppervale, Vesper Cloud, Thornbury Legal, and Chapter 9's eight practice-bank orgs) — confirmed by direct read this session. |
| Production depth | Pass | Three round-trip moments (result arrival, context assembly, action proposal), each with mechanism + example + why-it's-dangerous grounded in the Ferngate scenario; six real defenses (two per moment) each with an explicit "what it stops / what it doesn't" split, matching Chapter 9's six-defense pattern; a dedicated research section citing four real, independently-verified sources; a genuine, no-scaffold hands-on project implementing a combined RAG-plus-tool-output fix in full, executable, tested code. |
| Real-time framework accuracy | Pass | `lesson.html`'s research section cites: OWASP Top 10 for LLM Applications 2025 (LLM06:2025, Excessive Agency); the OWASP GenAI Security Project's Top 10 for Agentic Applications (v1.0, December 9, 2025 — ASI02 Tool Misuse, ASI03 Identity & Privilege Abuse); Zhan, Ding, Xu, Tan, Xu, Kang, and He, "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents" (arXiv:2403.02691, ACL 2024 Findings), including its 24% base attack-success finding; and Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, and Tramèr, "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents" (arXiv:2406.13352), including its ~48% targeted attack-success finding. `lesson.html` states these were independently verified via live web search the prior session, including confirming the OWASP Agentic Applications Top 10's current existence, numbering, and publication date since it postdates training-data cutoff. |
| Architecture and diagrams | Pass | The three-moment round-trip breakdown does the structural-distinction work a diagram would, deliberately reshaped from Chapter 9's pipeline-stage device to fit a tool call's own request/response shape, with the reasoning stated explicitly in the lesson text. |
| Exercises | Pass | 8 tasks (exceeds the 6+ minimum), 5 explicitly marked production-gear (exceeds the 3+ minimum) — permission-risk-score computation, defense/scenario matching, critiquing flawed reports, research citation matching, and written reasoning. Fresh scenario (Talbridge Health Network / Rounds Assistant, a fictional healthcare-scheduling agent) distinct from the lesson's Ferngate Logistics. Verified this session by direct execution: `solution.py` scores a perfect 27/27; `starter.py` reports 0/27 cleanly, no crash. |
| Practice bank | Pass | 8 scenarios (exceeds the 6+ minimum) across 8 distinct fictional systems (Pemberton Insurance Group, Kestrel Robotics, Fairhaven School District, Journeywell Travel, Brightloom Retail, Oakstead Manufacturing, Silverline Broadcasting, Cascade Ridge Outfitters), none reused from the lesson or exercises. Five drill fast classification of round-trip moments and defenses; three are deliberate judgment calls with no single keyword to match. Verified this session by direct execution: `solution.py` scores a perfect 9/9; `starter.py` reports 0/9 cleanly, no crash. |
| Interview preparation | Pass | 8 questions (2 each at beginner/intermediate/senior/architect), covering the Chapter-1-vs-Chapter-10 relationship, the tool-result-fields-of-differing-trust mechanism, a tool-role-message-structure overclaim evaluation, a single-hardcoded-rule-fix evaluation, a provenance-tagging-scheme design question against a schema you don't control, a permission-scoping-as-sole-strategy evaluation, a from-day-one architecture question synthesizing InjecAgent's and AgentDojo's findings, and a human-in-the-loop confirmation-habituation design question. `interview-questions.html` and `.md` generated from the same source content this session — verified identical question text, strong answers, red flags, follow-ups, and "what this proves" content between both files. |
| Project implementation | Pass | The course's real, final L3 Independent project — genuinely no-scaffold: `project/starter.py` has zero `# TODO` markers and is a complete, runnable, vulnerable pipeline extending Chapter 9's own Vesper Cloud corpus with a new tool call (`check_partner_sync_diagnostic`) whose `diagnostic_note` field carries a planted instruction. Directly demonstrates, in real executed output, that for the incident account (`acct_7734`) both the RAG channel and the tool channel independently contribute a privileged-action phrase to the assembled prompt. `project/solution.py` is one complete, valid reference fix (not a scored answer key) combining Chapter 9's RAG defenses with this chapter's six tool-output defenses, including a combined output-side least-privilege backstop that inspects the fully-assembled prompt regardless of which channel a phrase came from — demonstrated by a simulated double-quarantine-bypass that still resolves `DENIED`. |
| GenAI Builder Thought Process layer | Pass | Dedicated section on `lesson.html`: names a specific real mistake (a single hardcoded dollar-cap rule on one tool treated as a complete fix, leaving Defenses 1-5 unimplemented — the single-attempt trap recurring again after five prior chapters named it at different layers), what actually distinguishes a real defensive posture (all six defenses layered, each admitting a real gap the others cover), why this matters as Module 4 closes (explicit synthesis connecting Chapter 9's RAG-shape answer to this chapter's agentic-shape answer), and a working definition carried forward. |
| Navigation/template consistency | Pass | lesson → quiz → exercises → practice → interview-questions → project chain verified this session with a standalone Python link-walker script against the filesystem: 6 HTML files scanned, 70 href/src targets checked, 0 broken. Interview-questions callout box present on `lesson.html` (confirmed by direct read this session, present near the end of the file). Footer GitHub link present on `lesson.html`, `interview-questions.html`, and `project/index.html` (confirmed by direct grep this session). |
| Accessibility/readability | Pass | Uses existing `style.css` classes only (hook, what-is, code-window, thinking-box, points-to-remember, lesson-card, task-card, badge-coming-soon, page-toc, subtopic, download-links); no invented CSS, matching Chapters 1-9. |
| Public artifact readiness | Pass | `local_check.sh`'s placeholder-text scan passed as part of the full run (see below). All content is original — no wording, examples, or structure reused from Chapters 1-9 or any sibling TechNaom repo; only their HTML/CSS class structure and file-pattern precedent were consulted. Every fictional system (Ferngate Logistics/Dispatch Copilot, Talbridge Health Network/Rounds Assistant, all eight practice-bank systems, and Vesper Cloud/Vesper Assistant reused deliberately from Chapter 9 for the project) is explicitly invented; no named real product is targeted by any example — real, named entities appear only in research-citation sections, always as accurately-cited sources of documented, defensive-relevant findings, never as a target of exploit instructions. Every risk mechanism is paired with a real, working defense stating its honest limit — never presented as unsolved or as a ready-to-use exploit. |

## Required Checks

- [x] Lesson names agentic tool-output risk precisely as adversarial
  content entering through a tool's returned result at one of three
  genuinely distinct round-trip moments (result arrival, context
  assembly, action proposal) — and explicitly, in the lesson text
  itself, justifies using a moment-based framing device instead of
  reusing Chapter 9's pipeline-stage device, since a tool call's own
  request/response shape is genuinely different from a pipeline's.
- [x] Lesson covers all three required round-trip moments, each with
  mechanism, a concrete example grounded in the Ferngate Logistics
  scenario, and why it's dangerous — and explicitly connects Moment 2 to
  Module 2's core no-architectural-separation mechanism and Moment 3 to
  Chapter 1's three Excessive Agency components.
- [x] Lesson cites real, current, verified research/guidance, per
  `lesson.html`'s own explicit disclosure that all four sources were
  independently verified via live web search the prior session: OWASP
  Top 10 for LLM Applications 2025 (LLM06:2025), the OWASP GenAI
  Security Project's Top 10 for Agentic Applications (v1.0, December
  2025), InjecAgent (arXiv:2403.02691, ACL 2024 Findings), and AgentDojo
  (arXiv:2406.13352).
- [x] Lesson covers six required defenses (schema/type validation,
  content sanitization, structural separation, field-level provenance
  tagging, permission/capability scoping, human-in-the-loop confirmation
  with a least-privilege backstop), organized two per round-trip moment,
  each stating plainly what it stops and doesn't.
- [x] Lesson includes and links to a genuine hands-on lab (the project)
  that finds and fixes a real combined RAG-plus-tool-output injection
  vector in a provided, no-scaffold pipeline — verified true by direct
  execution this session, not just described.
- [x] Lesson explicitly frames the project as the course's real, final
  L3 Independent project — stated in the lesson's lab section and its
  Points to Remember section, matching CURRICULUM_MAP.md's Projects
  section statement that the L3 project ships after Chapter 10.
- [x] Lesson includes a GenAI Builder Thought Process section and a
  Points to Remember recap that explicitly closes Module 4 and previews
  Module 5 (Chapters 11-12) — confirmed present by direct read this
  session.
- [x] Interview-questions callout box is present on `lesson.html`
  (linking to `interview-questions.html`) — confirmed present near the
  end of the file by direct read this session.
- [x] Footer GitHub link (`https://github.com/TechNaom/ai-security-for-everyone`)
  is present on `lesson.html`, `interview-questions.html`, and
  `project/index.html` — verified present in all three by direct read/
  grep this session.
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
- [x] Project ships a real, substantive, genuinely no-scaffold lab —
  `project/starter.py` has zero `# TODO` markers, is complete and
  runnable, and directly demonstrates the combined vulnerability in real
  executed output; `project/solution.py` is one complete, valid
  reference fix (not a fixed answer key) whose own executed output
  demonstrates the fix, including a defense-in-depth double-bypass
  demonstration.
- [x] Chapter includes a thinking journal (GenAI Builder Thought Process
  section) — confirmed present.
- [x] Navigation follows lesson → quiz → exercises → practice →
  interview → project. Every internal link across all 6 HTML pages in
  this chapter folder programmatically verified to resolve to a real
  file this session (70 links checked, 0 broken).
- [x] Content is original — no wording, examples, or structure reused
  from Chapters 1-9 or any sibling TechNaom repo, except the Vesper
  Cloud corpus data deliberately and explicitly reused/extended from
  Chapter 9's own project per this chapter's explicit brief.
- [x] Every attack mechanism discussed is framed defensively; no example
  is presented as unsolved without a paired defense; no content targets
  a named real-world product with exploit instructions; every scenario
  is stated as explicitly fictional.
- [x] Terminology cross-checked against `docs/course-architecture.md`
  and `docs/curriculum/CURRICULUM_MAP.md`: chapter position (Module 4,
  Advanced, second of two chapters, completing the module) matches the
  roadmap table; Module 4's stated outcome ("extend an agent's
  permission model against adversarial tool output") is directly
  addressed; the Projects section's statement that the L3 project ships
  after Chapter 10 is honored both in the lesson text and the project's
  own framing.
- [x] `assets/chapters-data.js` updated this session: chapter-10 entry
  now has `path:
  "chapters/chapter-10-securing-agentic-systems-against-adversarial-tool-output/lesson.html"`.
  Module 4's `examPath` left `null` — see the written-exam judgment call
  below.
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
  this session: 70 href/src targets checked, 0 broken.

## Module 4 written-exam judgment call

**Decision: no separate Module 4 written exam. The L3 Independent
project satisfies the module's assessment type.**

CURRICULUM_MAP.md states Module 4's assessment as "applied
security-review exercise." Chapter 10's own project *is* an applied
security-review exercise, stated almost verbatim: a provided, genuinely
vulnerable pipeline, no scaffold, framed exactly the way a real internal
security-review request would read (see `project/README.md`'s "brief"
section), requiring the learner to trace two independent vectors and
produce a working fix — a closer match to "applied security-review
exercise" than a written exam would be. This mirrors the exact judgment
call already made for Module 1 (satisfied by Chapters 1-2's L1 project)
and Module 3 (satisfied by Chapters 6-8's risk-assessment-style project
tools) — both used the reasoning "the module's own project/lab already
is the assessment type named in the curriculum map, so a separate
written exam would be redundant, not additive." Module 2 got a written
exam because its assessment type ("injection-construction and
defense-evaluation exam") is a genuinely different exercise shape than
what Chapters 3-5's labs produced. Module 4's shape does not have that
gap: `assets/chapters-data.js` leaves Module 4's `examPath` as `null`,
now a final decision rather than deferred.

## Live-Tested vs. Logical-Only Content Disclosure

### Ollama status, as already documented in `lesson.html`

This chapter's `lesson.html` (written by a prior session) states its own
honest disclosure directly in the "L3 Independent Project" section:
`curl -s -m 8 http://localhost:11434/api/tags` responded normally,
confirming `llama3.2:latest` (3.2B parameters) is pulled and the server
is reachable; a direct generation request against `/api/chat`, tested
independently via raw `curl` with a 12-second timeout, returned no
response and timed out (`curl` exit code 28) — the same persistent,
previously-disclosed, sandbox-wide generation hang Chapters 3, 4, 5, and
9 all documented. This session did not re-run that `curl` check, per
this task's explicit instruction not to re-test a result the lesson
already documents — this audit reproduces `lesson.html`'s own exact
wording rather than re-verifying it, since the instruction was to match
the audit to what the lesson actually claims, not to re-test.

`lesson.html` states explicitly, in its own text, that its mechanism
claims (how a tool call's round trip assembles context, how each defense
structurally changes what reaches the model or what's allowed to
execute) are accurate, testable, deterministic-code-verified claims —
every defense function in the project is real, executed code whose
behavior was actually observed. It also states explicitly that no claim
is made that a specific live model was observed generating a specific
compliant-versus-refusing response this session; any transcript-shaped
example is framed as "representative of documented behavior" per
InjecAgent's and AgentDojo's own published results.

### What WAS live-tested / actually executed this session

- **`lesson.html`** — read in full this session (all 836 lines) before
  any other work began, to confirm genuine completeness, internal
  consistency, and absence of truncation or leftover TODOs, per this
  task's explicit first instruction.
- **`exercises/solution.py`** — executed directly, scored 27/27.
- **`exercises/starter.py`** — executed directly with all TODOs blank,
  reported 0/27 cleanly (no crash, no traceback).
- **`practice/solution.py`** — executed directly, scored 9/9.
- **`practice/starter.py`** — executed directly with all TODOs blank,
  reported 0/9 cleanly.
- **`project/starter.py`** — executed directly this session. Reproduces
  the combined vulnerability with real, directly-observed output: for
  `acct_9142` (ordinary account), the RAG channel alone contributes a
  privileged phrase (`Vulnerable: True`); for `acct_7734` (the incident
  account), BOTH the RAG channel and the tool channel independently
  contribute a privileged phrase, printed explicitly as
  `>>> BOTH channels independently pushed toward the same unauthorized
  action.`
- **`project/solution.py`** — executed directly this session. Both
  `acct_9142` and `acct_7734` resolve `ALLOWED` through the defended
  pipeline; a simulated double-quarantine-bypass (both the RAG chunk's
  trust tier mislabeled AND the tool-note quarantine forced off)
  resolves `DENIED` through the combined least-privilege backstop alone.
  All three `assert` statements at the end of `main()` passed, confirmed
  by the script completing with no `AssertionError` and printing "All
  assertions passed."
- **Every internal link** across all 6 HTML files in this chapter —
  checked with a standalone filesystem-walking Python script this
  session: 70 links checked, 0 broken.
- **`bash scripts/local_check.sh < /dev/null`** — executed directly from
  the repo root this session after all files were added. All 6 checks
  passed; full output ended with "All local checks passed. Safe to
  push."
- **`python3 -m py_compile`** — run directly on all 6 `.py` files in
  this chapter this session; all compiled cleanly with no syntax errors.

### What was NOT live-tested (logical-only, and why that's the correct, honestly-disclosed scope for this chapter)

- No live model generation call was made or is claimed to have been made
  anywhere in this chapter's content or project output this session —
  Ollama's `/api/chat` endpoint's hang, as already documented directly
  in `lesson.html` from the prior session, was not re-tested this
  session per this task's explicit instruction to read and match the
  lesson's exact existing wording rather than re-test.
- The synthetic Vesper corpus, `PARTNER_API_RESPONSES` fixture, and both
  demo accounts (`acct_9142`, `acct_7734`) in `project/starter.py`/
  `solution.py` are entirely fabricated for this exercise (clearly
  labeled as such) — no real customer, partner API, or support
  interaction is represented.
- The `call_model_live()` bonus functions' actual behavior against a
  reachable Ollama endpoint was NOT observed this session (the endpoint
  is not currently reachable for generation, per the lesson's own
  disclosure) — this is disclosed explicitly rather than claimed as
  tested, matching every prior chapter's own convention.

## Terminology and Cross-Chapter Consistency Check

- Confirmed this chapter's three-moment round-trip breakdown is stated
  as a genuinely new organizing device for a tool call's own
  request/response shape, distinct from (not a restatement of) Chapter
  9's three-pipeline-stage device — `lesson.html`'s own "Three Moments"
  section makes this distinction explicit.
- Confirmed the chapter draws the exact boundary Chapter 8's Category 3
  already stated in its own text (adoption-time trust decision to
  connect a tool vs. this chapter's runtime defense against an
  already-connected tool's adversarial result) rather than re-deriving
  or contradicting it — verified by direct comparison of `lesson.html`'s
  quoted Chapter 8 text against Chapter 8's own `lesson.html` this
  session.
- Confirmed the project genuinely extends Chapter 9's own Vesper Cloud
  pipeline (identical corpus, identical chunk ids, identical planted
  forum post) rather than starting a new scenario from scratch, per this
  task's explicit instruction — verified by direct diff of the CORPUS
  data structure between `chapter-09/project/starter.py` and
  `chapter-10/project/starter.py` this session: identical.
- Confirmed the chapter explicitly states it completes Module 4 (page
  title, lede, and Points to Remember section) and previews Module 5
  (Chapters 11-12) — matching the pattern `PROJECT_STATE.md` and
  `AI_HANDOFF.md` describe for this chapter's brief.
- Confirmed the L3 project's own README and lesson text state explicitly
  it is the course's real, final L3 Independent project — no conflation
  with Chapter 9's own real-but-not-final project.
- Confirmed no `assessments/written-exams/module-4-exam.*` file was
  created, per this session's judgment call (documented above) that the
  L3 project satisfies Module 4's assessment type.
- Confirmed Chapters 1-9, all CI/workflow files, `README.md`, and
  `scripts/local_check.sh` were not modified this session — the only
  pre-existing files touched were `assets/chapters-data.js` (the
  single-line path addition), `index.html` (hero-stat bump to 10 and
  section-intro text update), `docs/curriculum/index.html` (Chapter 10's
  card updated from `badge-coming-soon`/`href="#"` to `— Live` with the
  real href), `PROJECT_STATE.md`, and `AI_HANDOFF.md` (both updated
  separately, described in their own commit), plus the creation of this
  audit file and the completion of the
  `chapters/chapter-10-securing-agentic-systems-against-adversarial-tool-output/`
  directory tree.

## Issues Found

None. `lesson.html` from the prior interrupted session was read in full,
confirmed complete and internally consistent, and used as-is. All
newly-built files passed on first execution; no rework was needed during
this session.
