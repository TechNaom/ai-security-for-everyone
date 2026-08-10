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

Confirm with the user before creating the public GitHub repo and
pushing (same courtesy check used for `ai-coding-agents-for-everyone`).
Once confirmed: `git init`, `gh repo create TechNaom/ai-security-for-everyone
--public --source=. --remote=origin --push`, then verify CI Checks and
Deploy GitHub Pages both pass on the real runners before considering
the scaffold done. After that, build Chapter 1 (conceptual, no
live-model dependency) as the reference chapter.
