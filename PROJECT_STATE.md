# PROJECT_STATE.md — AI Security for Everyone

Last updated: 2026-08-12 (Chapter 10 / Module 4 complete)

## Course Objective

Teach learners (beginner → architect) to secure LLM-powered systems —
threat modeling, prompt injection/jailbreaking, data/model integrity,
securing RAG and agentic systems, red-teaming, and safe output
handling — following the TechNaom master course-building philosophy
(layered depth, story-first, production-grade, interview-ready,
original content only).

## Architecture Decisions

- **Course size: 13 chapters** (focused-topic sizing, matching every
  other course in the ecosystem).
- **Repo structure mirrors `ai-coding-agents-for-everyone`** (the most
  recent, most refined reference now): static site,
  `chapters/chapter-XX-slug/`, `docs/curriculum/`, `templates/`,
  `assessments/`, `quality-audits/`, `codebase/`. Shared front-end
  assets, templates (including `written-exam.template.html`, rendered
  as styled HTML from day one — not the raw-`.md` gap found and fixed
  in that course after user feedback), `.github/workflows/ci.yml`, and
  `scripts/local_check.sh` copied from `ai-coding-agents-for-everyone`
  and rebranded. `.gitkeep` files added to all empty directories from
  the start (a bootstrap bug — git doesn't track empty directories —
  was found and fixed there; starting with `.gitkeep` already in place
  here avoids rediscovering it).
- **Chapter file pattern**: uses `python-for-everyone`'s richer
  per-chapter structure (README.md in exercises/practice/project,
  `interview-questions.md`) from Chapter 1, not the thinner
  mcp-for-everyone-derived pattern — per
  [[feedback-course-structural-reference]], this is now the
  ecosystem's preferred going-forward pattern, not just a
  Chapter-7-onward exception like it was in the prior course.
- **Model/API policy**: inherits `ai-coding-agents-for-everyone`'s
  resolved policy directly, not re-litigated — `openai` Python package
  pointed at Ollama's local OpenAI-compatible endpoint by default, zero
  cost/API key, with a documented hosted-provider-swap option. See
  `docs/course-architecture.md` for the one addition specific to this
  course: the hosted-provider option is *more* relevant here since
  testing an attack against a production model's real safety training
  is itself a legitimate reason to reach for it.
- **Ethical framing (non-negotiable, see course-architecture.md)**:
  every attack technique pairs with a real, working defense; framed as
  defensive/educational throughout; no ready-to-use exploit content
  targeting a named real-world product.

## Completed

- [x] Step 1: Discovery (course vision, personas, prerequisites,
      outcomes, modules, chapters, projects, capstone, differentiators,
      cross-course links) — captured in conversation, confirmed by the
      user, summarized in `docs/curriculum/CURRICULUM_MAP.md`.
- [x] Cross-course overlap check: confirmed via `grep` against
      `mcp-for-everyone`, `ai-coding-agents-for-everyone`,
      `genai-for-everyone`, and `rag-for-everyone`'s own curriculum
      maps that this course's scope (deep LLM-specific security) does
      not duplicate any of them — each touches security at most one
      module/chapter/session wide; this course goes deep across a full
      13 chapters, explicitly building on (not repeating) each.
- [x] Step 2: Curriculum map (`docs/curriculum/CURRICULUM_MAP.md`).
- [x] Step 3: Repository architecture scaffolded — directories (with
      `.gitkeep` from the start), templates, shared assets (rebranded:
      `AISFE_MODULES`, `AISFEProgress`, `aisfe-progress`), CI (copied
      from `ai-coding-agents-for-everyone`, already includes the
      `practice/solution.py` coverage and marker-comment conventions
      that course had to add after the fact), README, this file,
      AI_HANDOFF.md, LICENSE/LICENSE-CONTENT.
- [x] Homepage (`index.html`) and roadmap (`docs/curriculum/index.html`)
      built as part of the initial scaffold, not deferred — the prior
      course shipped 8 chapters before anyone noticed there was no
      landing page; avoided that gap here from day one.
- [x] Pushed to GitHub (`TechNaom/ai-security-for-everyone`, public),
      GitHub Pages enabled, CI Checks and Deploy GitHub Pages both
      verified green on real runners. One bootstrap bug found and
      fixed immediately: `quality-audits/.gitkeep` was missed in the
      initial `.gitkeep` pass despite being in the `mkdir` loop —
      caught by CI's `structure-check` job on the very first real run,
      same class of bug (git doesn't track empty directories) found in
      `ai-coding-agents-for-everyone`'s own first CI run.
- [x] **Chapter 1 built and live — reference chapter**: "Threat
      Modeling LLM Systems: The OWASP Top 10 for LLM Applications."
      Hook: GreenCart, a fictional grocery retailer whose LLM-powered
      return-triage assistant is exploited via indirect prompt
      injection through a customer-submitted text field, routing a
      fraudulent refund with no network boundary crossed. Covers the
      CURRENT OWASP Top 10 for LLM Applications (2025 edition, verified
      via research — correct category names/order/the real
      reordering from prior editions, not stale memory). Real depth on
      Prompt Injection (LLM01), Improper Output Handling (LLM05), and
      Excessive Agency (LLM06) — the three that set up the rest of the
      course — the other seven get real mechanism/example/check
      coverage. Closes with a genuine threat-modeling walkthrough (a
      real asset/category/likelihood-impact/mitigation table). Sets
      the course's non-negotiable ethical framing explicitly, in its
      own section, early. 8 exercises (4 production-gear), 8 practice
      scenarios, 8 interview questions across all 4 levels. Build was
      interrupted mid-session by an environment restart; resumed
      cleanly — prior partial work (lesson.html, quiz.html,
      interview-questions, exercises) was verified complete and kept,
      not redone.
- [x] **Chapter 2 built and live — completes Module 1**: "Mapping the
      Attack Surface of a Real LLM Feature." Teaches the systematic
      skill Chapter 1 only demonstrated once: a real, repeatable
      7-step attack-surface enumeration method (every tool, every
      context source including tool outputs, trust-classify each,
      cross-reference untrusted sources against side-effect tools,
      explicitly re-check tool outputs, run all 10 OWASP categories
      against the complete list, write the justified table). Applied
      to Waypoint, a fictional travel-booking trip-planner — a
      genuinely different shape from GreenCart (multi-turn, partner-
      data integration, payment path, six tools) — producing a 10-row
      threat model hitting every OWASP category. Names two real
      mistakes (under-scoping: a tool's OUTPUT re-enters context and
      was written by an external party, not the user; over-focusing:
      stopping after one Prompt Injection finding and missing a real
      Unbounded Consumption gap and a Supply Chain gap in the same
      system). Ships Module 1's real L1 project (AskHR, a fourth new
      scenario, validated structurally since the task is intentionally
      open-ended). 8 exercises (5 production-gear), 8 practice
      scenarios, 8 interview questions across all 4 levels.
      **Module 1 (Chapters 1-2) is now fully built and live.**
- [x] **Chapter 3 built and live — starts Module 2**: "Direct Prompt
      Injection." First chapter needing a real model; honestly
      disclosed a live-testing gap both in the audit AND directly in
      the lesson text itself (Ollama's generation endpoint hung past a
      20s timeout every attempt — the same persistent, disclosed
      sandbox-wide issue found across five prior sessions in
      `ai-coding-agents-for-everyone`). Every example transcript is
      framed as "representative of documented behavior," never as
      output observed this session. Covers the precise mechanism (no
      code-vs-data architectural separation; role weighting is trained,
      not guaranteed), a 5-family taxonomy (persona override/DAN,
      instruction override, fake authority, payload obfuscation,
      multi-turn escalation), and four real defenses each stating what
      it does/doesn't stop, including accurately-cited real provider
      research (OpenAI's Instruction Hierarchy paper, arXiv:2404.13208;
      Anthropic's XML-tag structuring and guardrails docs — both
      fetched live this session). Ships a real lab harness built to run
      for real once Ollama is reachable, with tested graceful
      degradation. 8 exercises (5 production-gear), 8 practice
      scenarios, 8 interview questions across all 4 levels. Also fixed
      a homepage inconsistency found on review: the "tested against
      real models" feature-card overclaimed relative to this chapter's
      own honest disclosure — softened to match actual practice.
- [x] **Chapter 4 built and live**: "Indirect Prompt Injection and
      Jailbreaking Techniques." Keeps Chapter 3's mechanism unchanged,
      varies who supplies the tokens and when. Hook: Northline Digest,
      a fictional internal wiki assistant where a contractor's routine
      wiki edit plants an injection three weeks before an unrelated
      employee's unrelated question happens to retrieve it — attacker
      and victim decoupled in both time and identity. Explicitly builds
      on (doesn't re-introduce) Chapters 1-2's own indirect-injection
      instances. 5-channel delivery taxonomy (RAG documents, tool/API
      output, web content, email/documents, multi-modal hidden text)
      plus jailbreaking as a distinct concept, grounded in real cited
      research: OWASP LLM01:2025, Zou et al.'s adversarial-suffix paper
      (arXiv:2307.15043), Wei/Haghtalab/Steinhardt's competing-
      objectives framing (arXiv:2307.02483). Extends all four of
      Chapter 3's defenses to the indirect/jailbreak context. Same
      Ollama generation hang as Chapter 3, same honest-disclosure
      handling (in the lesson text itself, not just the audit). 8
      exercises (5 production-gear), 8 practice scenarios, 8 interview
      questions across all 4 levels.
- [x] **Chapter 5 built and live — completes Module 2**: "Evaluating
      Prompt-Injection Defenses Honestly." Turns Chapters 3-4's "what
      this stops / what it doesn't" habit into a real measurement
      methodology: a 4-step process (multi-variant corpus spanning both
      taxonomies + benign controls, controlled before/after comparison,
      real numbers including false positives, non-optional adversarial
      iteration). Central original contribution: a three-category
      defense taxonomy by what each type actually measures — structural
      (does the tell still fire), detection (a real false-positive/
      false-negative tradeoff), consequence-bounding (does blast radius
      stay contained, independent of whether injection succeeded) —
      and the real, common mistake of applying Category 1's metric to
      a Category 3 defense. Meta-honest disclosure: the chapter applies
      its own "don't overclaim" thesis to its own worked-example
      numbers, since Ollama hung again this session (re-confirmed via
      raw curl before writing). Build was interrupted mid-session by a
      rate limit; resumed cleanly with prior partial work verified and
      kept. 8 exercises (5 production-gear), 8 practice scenarios, 8
      interview questions across all 4 levels.
      **Module 2 (Chapters 3-5) is now fully built and live.**
- [x] **Module 2 written exam built**: `assessments/written-exams/module-2-exam.html`
      (+`.md` portable source) — a genuine "injection-construction +
      defense-evaluation exam" per CURRICULUM_MAP.md, not a general
      concept quiz. Part C asks the test-taker to actively construct
      plausible injection attempts against 3 scenarios (not just
      diagnose someone else's); Part D presents a fictional defense-
      evaluation report with 4 planted methodology flaws (narrow
      single-attempt-trap corpus, no benign control set, no adversarial
      -iteration round, Category 1 metric misapplied to a Category 3
      defense) with a full worked diagnosis key. 14 numbered items
      total. Registered in `chapters-data.js`.
- [x] **Chapter 6 built and live — starts Module 3, a genuinely new
      subject**: "Data Poisoning." Explicitly NOT "injection but during
      training" — draws a sharp, tabulated distinction from Modules
      1-2's runtime attack surface (pipeline-stage/persistent vs.
      runtime/one-session). Hook: Meridian Home Warranty, extending
      Chapter 1's one-sentence LLM04 example to full resolution (46
      unremarkable claims over 8 months teach a fine-tuned triage model
      a backdoor trigger phrase). Three categories (targeted/backdoor,
      availability/bias, RAG corpus poisoning — explicitly distinguished
      from Chapter 4's indirect-injection-via-RAG as a pipeline attack,
      not a runtime one), grounded in real current research (Hubinger
      et al.'s Sleeper Agents, arXiv:2401.05566; the Anthropic/UK
      AISI/Alan Turing Institute ~250-poisoned-documents finding,
      arXiv:2510.07192; Carlini et al.'s web-scale poisoning-cost
      research, arXiv:2302.10149). Four defenses, each honest about
      limits. Ships a self-contained (no live-model dependency)
      corpus-anomaly scanner project that honestly demonstrated its own
      documented limit during testing (a real backdoor and pure noise
      became statistically indistinguishable at low support). 8
      exercises (5 production-gear), 8 practice scenarios, 8 interview
      questions across all 4 levels.
- [x] **Chapter 7 built and live**: "Model Extraction and Theft." A
      third distinct attack surface, extending Chapter 6's two-way
      pipeline-vs-runtime table into a three-way comparison: unlike
      Module 2 (manipulates one session) and Chapter 6 (poisons data
      before training), this chapter's attacker touches neither the
      target model nor its training data — only ordinary API queries,
      at volume, turning the model's output channel into a query
      oracle. Hook: Halcyon Research's ClauseFinder, hit by both a
      rival's query-based distillation campaign and a casual
      system-prompt extraction (tied to Chapter 1's LLM07). Three
      techniques (query-based distillation, training-data extraction/
      membership inference, system-prompt extraction) grounded in real
      cited research (Tramèr et al. arXiv:1609.02943, Krishna et al.
      arXiv:1910.12366, Carlini et al. arXiv:2012.07805 and
      arXiv:2311.17035). Four defenses including legal/ToS deterrence
      as a genuine non-technical control. Ships a self-contained
      query-pattern anomaly scorer that honestly demonstrated the same
      detection-defense false-positive tension Chapter 5 named (a
      legitimate power user scored only ~10 points below a real
      extraction campaign). 8 exercises (5 production-gear), 8 practice
      scenarios, 8 interview questions across all 4 levels.
- [x] **Chapter 8 built and live — completes Module 3**: "Supply-Chain
      Risk: Weights, Dependencies, and Provenance." Deliberately breaks
      Chapters 6-7's comparison-table pattern, with the reasoning
      stated directly in the lesson: supply-chain risk usually has no
      discrete attacker action against your system at all — it's a
      trust decision made at adoption time, upstream of everything
      else. Uses a lifecycle timeline instead (supply chain ->
      poisoning -> injection -> extraction). Hook: Solstice Diagnostics'
      TriageAssist, where three individually reasonable deadline-driven
      decisions (an unvetted community adapter, default pickle-based
      loading, an unvetted third-party vendor) each turn out to be live
      liabilities nobody attacked, just inherited. Three categories
      (compromised/backdoored weights, malicious/vulnerable ML-toolchain
      dependencies, excessive trust in third-party tools at adoption
      time), grounded in real current research (JFrog's 2024 pickle-
      backdoor disclosure, Sonatype's 2025 PickleScan bypass findings,
      Kellas et al.'s PickleBall paper — ACM CCS 2025, arXiv:2508.15987
      — Mend.io's 2024 PyPI typosquatting campaign, the December 2024
      ultralytics compromise, Safetensors, SLSA, Spoczynski et al.'s
      Atlas framework — arXiv:2502.19567). Four defenses. Ships a
      self-contained provenance/integrity checker project. 8 exercises
      (5 production-gear), 8 practice scenarios, 8 interview questions
      across all 4 levels. **Module 3 (Chapters 6-8) is now fully built
      and live.**
- [x] **Module 3 exam decision: no separate written exam** — Module
      3's assessment type ("concept + risk-assessment exercise")
      mirrors Module 1's phrasing exactly, and Module 1 didn't need a
      separate exam (its L1 project satisfied it). Chapters 6-8 already
      shipped substantial risk-assessment-style project tools (a
      corpus-anomaly scanner, a query-pattern scorer, a provenance
      checker) that collectively satisfy this assessment type. Same
      judgment call as Module 1, applied consistently.
- [x] **Chapter 9 built and live — starts Module 4**: "Securing RAG
      Pipelines Against Injection." Goes deep on Chapter 4's own
      "preview of that depth" line (RAG chunks as the single most
      consequential indirect-injection channel), organizing by three
      genuinely distinct pipeline stages instead of extending Chapter
      4's five-channel taxonomy or Chapters 6-8's comparison-table/
      timeline pattern — ingestion-time risk (what gets indexed, with
      what or no review), retrieval-time risk (a pure similarity search
      with no trust concept, the moment planted content activates), and
      generation/output-time risk (Module 2's no-architectural-
      separation mechanism reappearing inside RAG's own common naive
      prompt-assembly pattern). This framing is independently validated
      by real, current external guidance, not invented: the OWASP Cheat
      Sheet Series' RAG Security Cheat Sheet (added 2026, confirmed live
      via WebFetch this session) organizes its own recommended controls
      by the identical three-stage structure. Hook: Vesper Cloud's
      Vesper Assistant, a support RAG bot blending reviewed KB articles,
      an unreviewed public forum, and per-session uploads, where a forum
      post planted six weeks earlier is retrieved for an unrelated
      query and nearly causes a support agent to bypass identity
      verification and approve a quota override — caught by a second-
      reviewer check, not by the pipeline itself. Six real defenses, two
      per stage (content sanitization, provenance/trust tagging,
      retrieval-result quarantining, namespace isolation, structural
      separation, output-side least-privilege), grounded in real cited
      research: OWASP LLM01:2025 and the new LLM08:2025 (Vector and
      Embedding Weaknesses) category, Greshake et al.'s foundational
      indirect-injection paper (arXiv:2302.12173), and Zou, Geng, Wang,
      and Jia's PoisonedRAG (arXiv:2402.07867, USENIX Security 2025,
      ~90-99% attack success injecting as few as five malicious texts).
      Ollama's `/api/tags` responded normally this session but
      `/api/chat` hung again (curl exit code 28, re-confirmed directly),
      the same persistent issue Chapters 3-5 documented — this chapter's
      core mechanism and defense claims are demonstrated with
      deterministic, fully-executed code inspecting assembled prompt
      text directly, honestly disclosed in the lesson text itself as
      not a live-model-observed claim, following Chapter 5's exact
      disclosure pattern; an optional `call_model_live()` bonus function
      is included, not required for or checked by the project's
      scoring. Ships a real, complete RAG-specific lab (find and fix the
      exact injection vector from the lesson's own incident in a
      provided pipeline) — explicitly and repeatedly framed as NOT the
      course's final L3 Independent project, which ships after Chapter
      10 per CURRICULUM_MAP.md's Projects section, following the same
      "short preview, real project ships next chapter" pattern used for
      the L1 project across Chapters 1-2. 8 exercises (5
      production-gear), 8 practice scenarios, 8 interview questions
      across all 4 levels.
- [x] **Chapter 10 built and live — completes Module 4**: "Securing
      Agentic Systems Against Adversarial Tool Output." `lesson.html`
      (836 lines) was written by a prior session interrupted mid-build
      by a rate limit; this session read it in full first, confirmed it
      was complete, internally consistent, free of truncation/leftover
      TODOs, and already had the interview-questions callout and footer
      GitHub link, and built the rest of the chapter on top of it rather
      than rewriting it. Completes what Chapter 1's Excessive Agency
      (LLM06) section and Chapter 8's Category 3 both explicitly
      deferred to "Module 4's future agentic-systems chapter": an
      agent's runtime defense against an already-connected tool's
      adversarial *result*, distinct from Chapter 8's adoption-time
      trust decision to connect the tool at all. Hook: Ferngate
      Logistics' Dispatch Copilot, where a partner carrier API's
      free-text `delivery_notes` field carries a planted instruction
      that nearly triggers an unauthorized `issue_reship_credit` call —
      caught only by a dispatcher's personal habit, not the
      architecture. Organizes tool-call risk by three round-trip moments
      (result arrival, context assembly, action proposal) — deliberately
      NOT a reuse of Chapter 9's pipeline-stage device, since a tool
      call's request/response shape is genuinely different from a
      pipeline's, with the reasoning stated explicitly in the lesson.
      Six real defenses (two per moment: schema/type validation and
      content sanitization at result arrival; structural separation and
      field-level provenance tagging at context assembly; permission/
      capability scoping and a human-in-the-loop least-privilege
      backstop with sandboxed, rate-limited execution at action
      proposal), grounded in real cited research independently verified
      via live web search the prior session: OWASP LLM06:2025 (Excessive
      Agency), the OWASP GenAI Security Project's Top 10 for Agentic
      Applications (v1.0, December 2025 — ASI02 Tool Misuse, ASI03
      Identity & Privilege Abuse), InjecAgent (arXiv:2403.02691, ACL 2024
      Findings, 24% base attack-success rate against ReAct-prompted
      GPT-4), and AgentDojo (arXiv:2406.13352, ~48% targeted
      attack-success rate against GPT-4o across 629 test cases). Ollama's
      `/api/tags` responded normally, `/api/chat` hung again (curl exit
      code 28), same persistent issue as Chapters 3-5 and 9, disclosed
      directly in the lesson text and re-confirmed in this chapter's own
      audit's exact wording (not re-tested this session, per the task's
      instruction to match the lesson's existing claim). Ships the
      course's real, final **L3 Independent project**
      (`chapters/chapter-10-.../project/`) — genuinely no-scaffold
      (`starter.py` has zero `# TODO` markers, a complete runnable
      vulnerable pipeline), extending Chapter 9's own Vesper Cloud
      corpus (confirmed identical by direct diff this session) with a
      new tool call, `check_partner_sync_diagnostic`, whose
      `diagnostic_note` field can carry a planted instruction the same
      way a RAG chunk can — a query that triggers both channels for the
      incident account gets two independent nudges toward the same
      unauthorized action, verified in real executed output.
      `solution.py` is one valid reference fix (not a scored answer key)
      combining Chapter 9's RAG defenses with this chapter's own six,
      including a combined least-privilege backstop that inspects the
      fully-assembled prompt regardless of which channel a phrase came
      from — demonstrated via a simulated double-quarantine-bypass that
      still resolves `DENIED`. 8 exercises (5 production-gear, new
      scenario: Talbridge Health Network/Rounds Assistant), 8 practice
      scenarios (8 new fictional orgs, none reused), 8 interview
      questions across all 4 levels. **Module 4 (Chapters 9-10) is now
      fully built and live.**
- [x] **Module 4 exam decision: no separate written exam** — Module 4's
      assessment type ("applied security-review exercise") is satisfied
      almost verbatim by Chapter 10's own L3 project, which is framed
      explicitly as a real internal security-review request (see
      `project/README.md`), not a fill-in-the-blank exercise. Same
      judgment call as Modules 1 and 3: the module's own project already
      is the assessment type named in the curriculum map, so a separate
      written exam would be redundant. `assets/chapters-data.js` leaves
      Module 4's `examPath` as `null`, now a final decision (previously
      deferred/shared with Chapter 9).
- [x] **Chapter 11 built and live — starts Module 5**: "Red-Teaming an
      LLM System: Methodology and Practice." A process chapter, not a
      new-attack chapter — the third instance of the "process chapter
      building on established mechanism" pattern (after Chapter 2 on
      Chapter 1, Chapter 5 on Chapters 3-4), teaching a five-phase
      red-teaming methodology (scoping/rules of engagement,
      threat-model-driven test-case design using Chapter 1's OWASP Top
      10 as the structuring device, systematic execution and
      documentation, severity/impact classification, and writing a
      findings report) that draws on Chapters 3-10's own attack
      taxonomy as its working arsenal, mapped explicitly to all ten
      OWASP categories in the lesson's own table. Grounded in five real,
      independently-verified sources: OWASP GenAI Security Project's
      GenAI Red Teaming Guide (Jan 2025), NIST's Generative AI Profile
      (NIST-AI-600-1, July 2024), Microsoft's "Lessons from Red Teaming
      100 Generative AI Products" (arXiv:2501.07238), OpenAI's "Approach
      to External Red Teaming for AI Models and Systems"
      (arXiv:2503.16431), and Anthropic's published Frontier Red Team
      methodology. Hook is Alderglen Financial's Ledger Copilot; the
      project is Module 5's own new deliverable shape — a rubric-graded
      findings report (`project/RUBRIC.md`) against a fresh,
      self-contained target (Ledger Copilot again, with three planted
      vulnerabilities mirroring Chapter 3/4/9/10's mechanisms),
      explicitly not a byte-identical reuse of Chapter 9/10's Vesper
      Cloud pipeline, with the choice justified in `project/README.md`.
      8 exercises (5 production-gear, new scenario: Corvette Bay
      Utilities/Outage Assistant), 8 practice scenarios (8 new fictional
      orgs, none reused), 8 interview questions across all 4 levels.
      Ollama checked fresh this session: `/api/tags` OK, `/api/chat`
      timed out with a 20-second timeout (exit code 28) — same
      persistent hang as Chapters 3, 4, 5, 9, 10, disclosed honestly in
      `lesson.html`. See `quality-audits/chapter-11-audit.md` for full
      detail.
- [x] **Module 5 exam decision: explicitly deferred to after Chapter 12
      ships** — unlike every prior module, Module 5's assessment type
      ("a red-team report graded against a rubric") spans both Chapter
      11 and Chapter 12 in the curriculum map's own module-level
      framing, and Chapter 12 covers a genuinely different risk
      direction (output handling) that Chapter 11's own project doesn't
      exercise. `assets/chapters-data.js` leaves Module 5's `examPath`
      as `null` for now; final call (confirmed `null`, or a new
      `assessments/written-exams/module-5-exam.html`) to be made when
      Chapter 12 ships. See `quality-audits/chapter-11-audit.md`'s
      "Module 5 written-exam judgment call" section for full reasoning.

## Pending / Not Started

(Updated 2026-08-12 (Chapter 10 complete) — most items below from the
original scaffold plan are now done; keeping this section current
rather than stale.)

- [x] Push to GitHub, verify CI/Pages green — done since the initial
      scaffold, re-verified after every single chapter/doc push since.
- [x] `CONTRIBUTING.md`, `CHANGELOG.md` — written as part of the
      initial scaffold.
- [x] Reference chapter (Chapter 1) built and validated.
- [x] Website (root `index.html`, styled roadmap) — built as part of
      the initial scaffold, not deferred to a later step (a gap found
      late in `ai-coding-agents-for-everyone`'s build, avoided here).
- [x] Chapter 8 ("Supply-Chain Risk," Module 3) — completes Module 3.
- [x] Chapter 9 ("Securing RAG Pipelines Against Injection," Module 4) —
      starts Module 4.
- [x] Chapter 10 ("Securing Agentic Systems Against Adversarial Tool
      Output," Module 4) — completes Module 4, ships the L3 project.
- [x] Chapter 11 ("Red-Teaming an LLM System: Methodology and
      Practice," Module 5) — starts Module 5, ships the rubric-graded
      findings-report project. See "Next Recommended Task" below for
      the Chapter 12 brief.
- [ ] Chapter 12 (Module 5) — not yet built, closes Module 5.
- [ ] Chapter 13 (Module 6, capstone) — not yet built.
- [ ] Final polish pass once all 13 chapters exist.

## Known Issues

- None. All local checks (`scripts/local_check.sh`) pass as of Chapter
  10; CI and GitHub Pages verified green on real runners after every
  chapter push through Chapter 10.

## Open Decisions

- **License**: MIT (code) + CC BY 4.0 (content), matching the rest of
  the ecosystem — confirmed 2026-08-10, same pattern as every sibling
  course.
- **GitHub org/publish target**: `github.com/TechNaom/ai-security-for-everyone`,
  public, `main` branch, matching every sibling course's convention —
  not yet created on GitHub, pending confirmation before push.
- **Model recommendation for injection/jailbreak testing**: not yet
  verified against Ollama's current model library — do this at the
  start of Chapter 3 (the first chapter that needs a live model), same
  research discipline as every prior course's reference chapter.

## Design Standards

See `docs/course-architecture.md` for the full standard. Chapter
completion bar matches the rest of the ecosystem (6 exercises/6
practice scenarios/8 interview questions minimum, tested code before
writing).

## Next Recommended Task

**Chapter 11 ("Red-Teaming an LLM System: Methodology and Practice,"
Module 5, Advanced) is complete and live — Module 5 has started.** Next:
**Chapter 12 ("Handling LLM Output Safely: PII and Downstream Injection
Risk," Module 5, Advanced) — closes Module 5.**

### Module 5's full curriculum-map text (`docs/curriculum/CURRICULUM_MAP.md`)

> ### Module 5 — Red-Teaming & Output Handling
> **Purpose:** the practitioner half — running a real red-team exercise
> and handling what an LLM outputs safely.
> **Prerequisites:** Module 4
> **Outcomes:** run a structured red-team methodology against a target
> system; handle LLM output safely (PII leakage, downstream
> injection risk in generated content).
> **Chapters:** 11, 12
> **Labs:** a full red-team exercise against a provided target, with a
> real findings report
> **Assessment:** red-team report graded against a rubric

Chapter roadmap entry for Chapter 12: "Handling LLM Output Safely: PII
and Downstream Injection Risk," Module 5, Advanced. Description: "What
a model outputs can itself be an attack vector."

Cross-course links relevant to Module 5 (from CURRICULUM_MAP.md's
"Cross-Course Links" section): builds on `mcp-for-everyone` Module 5
(permission scoping, sandboxing, prompt injection via tool output) and
`ai-coding-agents-for-everyone` Chapter 11 (agent sandboxing,
permissions, destructive commands) as soft prerequisites — this course
deepens both rather than re-teaching them; link back, don't duplicate.

### What Chapter 11 already built (read before starting Chapter 12)

Chapter 11 is a process chapter, not a new-attack chapter — the third
instance of the "process chapter building on established mechanism"
pattern (Chapter 2 on Chapter 1, Chapter 5 on Chapters 3-4). It teaches
a five-phase red-teaming methodology (scoping/rules of engagement,
threat-model-driven test-case design using Chapter 1's OWASP Top 10 as
the structuring device, systematic execution/documentation,
severity/impact classification, findings-report writing), grounded in
five real, verified sources (OWASP's GenAI Red Teaming Guide, NIST's
Generative AI Profile, Microsoft's and OpenAI's red-teaming papers,
Anthropic's Frontier Red Team methodology), with an explicit table
mapping Chapters 3-10's own arsenal to all ten OWASP categories — LLM05
(Improper Output Handling) is explicitly marked in that table as
"named in Chapter 1, full depth deferred to Chapter 12 (next)," so
Chapter 12 is picking up a thread Chapter 11 deliberately left open, not
starting cold. Its hook and project target is **Alderglen Financial's
Ledger Copilot**; its project ships Module 5's new deliverable shape — a
rubric-graded findings report (`project/RUBRIC.md`) against a fresh
target with three planted vulnerabilities. Full detail in
`quality-audits/chapter-11-audit.md`.

**Module 5 exam decision: explicitly deferred, not yet decided.**
Module 5's assessment type spans both chapters per the curriculum map's
own module-level framing; Chapter 11's project produces a real artifact
of the right type but doesn't exercise Chapter 12's output-handling risk
direction at all. Decide this when Chapter 12 ships — see
`quality-audits/chapter-11-audit.md`'s "Module 5 written-exam judgment
call" section for the full reasoning already worked through.

### Chapter 12 build notes

1. **"Handling LLM output safely" is a genuinely different risk
   direction from everything Chapters 1-11 covered** — this course has
   so far focused almost entirely on untrusted *input* reaching the
   model (direct/indirect injection, RAG chunks, tool output, and now
   Chapter 11's red-teaming methodology for finding all of the above).
   Chapter 12 is about the *output* side: what the model generates
   becoming a downstream attack vector (e.g., generated content
   containing an unescaped payload that executes when rendered
   elsewhere, PII leakage in generated text, generated content that
   itself carries a planted instruction for whatever system consumes the
   model's output next). Chapter 1 already named Improper Output
   Handling (LLM05) as one of its three deep-dive categories and flagged
   it as "Chapter 12 builds a full chapter on exactly this," and Chapter
   11's own arsenal table restates that exact deferral — read both
   before writing Chapter 12, the same "read what an earlier chapter
   deferred to you" discipline Chapter 10 followed for Chapter 1/Chapter
   8.
2. PII handling needs its own real, cited grounding — check current
   OWASP guidance (LLM02:2025 Sensitive Information Disclosure is the
   input-side entry; verify whether there's output-specific guidance
   too, and check whether OWASP's LLM Top 10 has moved to a 2026 edition
   given Chapter 11's own research turned up an "OWASP GenAI LLM Top 10
   2026" resource — verify this live before citing, it may supersede the
   2025 numbering Chapters 1-11 have used throughout), and consider
   whether real regulatory framing (GDPR, CCPA) is worth a brief,
   appropriately-scoped mention — this course's curriculum map explicitly
   defers deep compliance/regulatory framing to a future `AI Governance
   for Everyone` course, so keep any regulatory mention brief and
   technical-practitioner-focused, not a compliance deep dive.
3. "Downstream injection risk in generated content" is the more novel
   half — a model's own output being consumed by another system (a
   rendered webpage, another agent, a downstream API) and carrying an
   injection payload FROM the model's generation, not TO it. This is
   architecturally the mirror image of everything Modules 2 and 4
   covered (untrusted input reaching the model) — worth naming that
   inversion explicitly in the lesson, the way Chapter 7 named its own
   "attacker touches neither the model nor its training data" inversion
   relative to Chapters 3-6.
4. This chapter closes Module 5. Chapter 11 already shipped a real
   rubric-graded findings-report project (against Alderglen Financial's
   Ledger Copilot); Chapter 12's own project should decide explicitly
   whether it needs its own separate findings-report-style deliverable
   (e.g., red-teaming the *output* side specifically, which Chapter 11's
   project didn't cover) or whether a different project shape (e.g., a
   find-and-fix lab on output-handling defenses, matching Chapters 9-10's
   pattern) better fits Chapter 12's own subject — state and justify
   whichever choice is made, the same way Chapter 11 justified its own
   fresh-target choice.
5. New fictional org, distinct from every org used across Chapters 1-11
   (see Chapter 11's own build notes for the Chapters 1-10 list, plus
   Chapter 11 adds: Alderglen Financial, Corvette Bay Utilities, and
   Chapter 11's eight practice-bank orgs — Driftwood Analytics, Larkspur
   Media, Nettlebrook Retail, Cobalt Harbor Shipping, Wrenfield Dental
   Group, Ridgemont University, Quillfire Robotics, Ashcombe Media
   Group).
6. Check Ollama status fresh at the start of that session (don't assume
   Chapter 11's `curl` result carries forward — it was `/api/tags` OK,
   `/api/chat` timed out after a 20-second timeout, exit code 28) and
   follow the same honest-disclosure discipline as every prior chapter
   that hit this if it's still hanging.

Then Chapter 13 (capstone, Module 6, architect-level, per
CURRICULUM_MAP.md: "design and defend a security architecture for a
realistic LLM system, with real trade-off reasoning," assessed by "a
capstone rubric — architecture challenge, Level 4"). Continue module by
module, validating each with a `quality-audits/chapter-0N-audit.md`
before moving on. Don't mass-generate ahead of validation.
