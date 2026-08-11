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

**Chapter 3 is done.** Next: Chapter 4 ("Indirect Prompt Injection and
Jailbreaking Techniques," Module 2, Advanced). Read Chapter 3 fully
first — it explicitly set up this chapter ("Chapter 4 moves from direct
injection to indirect injection and jailbreaking carried through
untrusted content the model reads later — a genuinely different
delivery mechanism, but the exact same underlying vulnerability").
Build on Chapter 3's mechanism and defense-in-depth framing rather than
re-deriving it; this chapter's job is the delivery-mechanism half
(indirect) plus jailbreaking specifically (which Chapter 3's taxonomy
only touched via the DAN-pattern mention under persona override).
Before writing: check whether Ollama's generation endpoint is working
in this session (it wasn't for Chapter 3) — try a plain, short-timeout
completion first; if it still hangs, follow the exact honest-disclosure
pattern Chapter 3 established (disclose in the lesson text itself, not
just the audit; frame examples as "representative of documented
behavior"). Chapter 5 (evaluating defenses honestly) comes after, then
Module 2's exam.
