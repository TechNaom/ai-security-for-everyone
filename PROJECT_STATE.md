# PROJECT_STATE.md — AI Security for Everyone

Last updated: 2026-08-10

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

## Pending / Not Started

- [ ] Push to GitHub, verify CI/Pages green on real GitHub Actions
      runners (this is the immediate next step).
- [ ] `CONTRIBUTING.md`, `CHANGELOG.md` — not yet written, adapt from
      `ai-coding-agents-for-everyone`.
- [ ] Step 4: Build Chapter 1 ("Threat Modeling LLM Systems: The OWASP
      Top 10 for LLM Applications") as the reference chapter. This
      chapter is conceptual (no live-model dependency), so it does not
      block on the Ollama/model-policy question below.
- [ ] Step 5: Validate reference chapter, refine template if needed.
- [ ] Step 6: Build remaining 12 chapters module by module, validating
      after each module. Modules 1 is fully conceptual — good to build
      first. Module 2 onward (Chapter 3+) needs a real model for
      constructing/testing prompt injections — verify Ollama's current
      model recommendation and its actual behavior under
      injection/jailbreak testing before writing that content (do not
      assume a technique works against the installed model without
      testing it first).
- [ ] Step 7-8: Projects, assessments beyond per-chapter content.
- [ ] Step 9: Website — root `index.html`, styled roadmap, GitHub Pages
      deploy (`pages.yml` already staged, same as
      `ai-coding-agents-for-everyone`'s).
- [ ] Step 10: Capstone (Chapter 13).
- [ ] Step 12: Polish.

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

**Modules 1-2 (Chapters 1-5, plus the Module 1 threat-modeling
project and Module 2 written exam) are complete.** Next: Module 3 —
Chapter 6 ("Data Poisoning," Advanced), starting a 3-chapter module
(Chapters 6-8: Data Poisoning, Model Extraction and Theft, Supply-Chain
Risk) that per CURRICULUM_MAP.md is about attacks on the model and its
training/deployment pipeline, NOT runtime prompt-based attacks — a
genuinely different subject from Module 2, not a continuation of the
injection material. Chapter 1's OWASP coverage already briefly named
LLM04 (Data and Model Poisoning) and LLM03 (Supply Chain) — Chapter 6
should build on that brief mention, not re-derive OWASP from scratch.
This module is conceptual/architectural in nature (poisoning training
data, extracting model behavior/weights via API access, verifying
supply-chain provenance) — likely less dependent on live Ollama
generation than Module 2 was, though verify this as you scope Chapter
6's actual content; a genuine hands-on demonstration (e.g. actually
demonstrating a toy poisoning effect, or model extraction via repeated
API queries) would still need the same test-before-write discipline if
attempted. Read Chapter 1's LLM03/LLM04 coverage first for continuity.
Module 3's assessment type per CURRICULUM_MAP.md is "concept +
risk-assessment exercise" (not stated as needing a separate written
exam necessarily — check whether the exercises/project satisfy this,
similar to Module 1's judgment call, before assuming a written exam is
required).
