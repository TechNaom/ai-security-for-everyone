# PROJECT_STATE.md — AI Security for Everyone

Last updated: 2026-08-12

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

## Pending / Not Started

(Updated 2026-08-12 — most items below from the original scaffold plan
are now done; keeping this section current rather than stale.)

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
      starts Module 4. See "Next Recommended Task" below for the
      Chapter 10 brief.
- [ ] Chapters 10-13 (rest of Module 4, Modules 5-6) — not yet built.
- [ ] Module 3's written exam (if warranted — pending the Module 3
      assessment-type judgment call, see "Next Recommended Task").
- [ ] Capstone (Chapter 13).
- [ ] Final polish pass once all 13 chapters exist.

## Known Issues

- None yet — repo is freshly scaffolded, no chapter content written,
  not yet pushed to GitHub.

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

**Chapter 9 ("Securing RAG Pipelines Against Injection," Module 4,
Advanced) is complete and live, starting Module 4.** Next: Chapter 10
("Securing Agentic Systems Against Adversarial Tool Output," Module 4,
Advanced) — completes Module 4 AND ships the course's real L3
Independent project ("find and fix a real injection vector in a
provided RAG pipeline or agent, no scaffold") per
`docs/curriculum/CURRICULUM_MAP.md`'s Projects section. This is the
one this course has been previewing since Chapter 9's own project was
explicitly framed as real-but-not-final.

**What Chapter 10 needs to do, concretely:**

1. Deepen what Chapter 1's Excessive Agency (LLM06) section and Module
   3's tool-trust material (Chapter 8's Category 3, specifically scoped
   away from runtime tool-output defenses at the time) only touched —
   an agent's runtime defenses against an adversarial tool *result*,
   distinct from Chapter 8's adoption-time trust decision to connect a
   tool in the first place. Chapter 8's lesson text itself already
   drew this exact line ("Module 4's future agentic-systems chapter
   will cover an agent's runtime defenses against an adversarial tool
   result... This category [Ch8's Category 3] is about the decision
   made before either of those defenses ever gets a chance to run") —
   read that section before writing Chapter 10 to avoid re-deriving or
   contradicting it.
2. **Build directly on Chapter 9's Vesper Cloud RAG lab, don't start a
   new pipeline from scratch.** Chapter 9's project (`chapters/
   chapter-09-securing-rag-pipelines-against-injection/project/`)
   ships a working, tested RAG pipeline (naive + six-defense-secured)
   for Vesper Assistant. Chapter 10's real L3 project should extend
   that exact pipeline with an agentic/tool-output angle — e.g., give
   Vesper Assistant a tool call (an account-lookup or ticket-update
   API) whose *returned result* can itself carry an adversarial
   instruction, the same way a retrieved RAG chunk can, and require the
   learner to find and fix an injection vector spanning BOTH channels
   (a poisoned retrieved chunk AND a poisoned tool result) with no
   scaffold — genuinely combining Chapter 9's RAG depth with Chapter
   10's own agentic depth, not just two separate labs bolted together.
3. Check Ollama status fresh at the start of that session (don't assume
   Chapter 9's `curl` result — it was `/api/tags` OK, `/api/chat` hung,
   exit code 28) and follow the same honest-disclosure discipline as
   every prior chapter that hit this if it's still hanging.
4. A new fictional org for Chapter 10's own lesson hook, distinct from
   every org already used across Chapters 1-9 (GreenCart, Waypoint,
   AskHR, Anchorline, Northline Digest, Meridian, Halcyon, Solstice,
   Coppervale, Vesper Cloud, Thornbury Legal, and the eight Chapter 9
   practice-bank orgs) — though the L3 project itself should stay on
   Vesper Cloud, per point 2 above, since it's explicitly extending
   Chapter 9's own lab.
5. After Chapter 10, decide whether Module 4 needs a separate written
   exam (`assessments/written-exams/module-4-exam.*`) or whether the
   L3 project satisfies the assessment type the way Chapters 1-2's and
   6-8's projects did for Modules 1 and 3 — Module 4's `examPath` is
   currently `null` in `assets/chapters-data.js`, left that way
   deliberately since it's shared between Chapters 9-10.

Then Module 5 (Chapters 11-12: red-teaming, output handling), then
Chapter 13 (capstone). Continue module by module, validating each with
a `quality-audits/chapter-0N-audit.md` before moving on. Don't
mass-generate ahead of validation.
