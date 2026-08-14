# AI_HANDOFF.md — AI Security for Everyone

Read this before touching anything in this repo. It's written so any AI
coding assistant can pick this up cold, with zero prior context, and
not redesign decisions that were already made.

## What this repository is

An open-source, free-to-read (and free-to-*run*) technical course
teaching LLM-specific security in depth — threat modeling, prompt
injection/jailbreaking, data/model integrity, securing RAG and agentic
systems, red-teaming, and safe output handling — part of the
**TechNaom "for Everyone"** course ecosystem. Follows the same
detailed master course-building prompt as every sibling course (ask
the maintainer for "the TechNaom master prompt" if you need the full
philosophy — it's not stored in this repo).

## Design philosophy (non-negotiable)

Same as the rest of the ecosystem: WHY → WHAT → HOW → BUILD → BREAK →
DEBUG → EVALUATE → SECURE → OPTIMIZE → SCALE → ARCHITECT progression;
layered depth for 4 personas; story-first; no shallow tutorials; 13
chapters, don't pad; all content original.

**Security-specific addition (non-negotiable)**: every attack
technique taught must be paired with a real, working defense — never
presented as unsolved. Framing throughout is defensive/educational,
not offense-only. No content ships as a ready-to-use exploit against
any named real-world product or service — demonstrate mechanism, not
payloads.

## Current state (as of 2026-08-14, all 13 chapters live — the course is complete)

**Read `PROJECT_STATE.md` for the authoritative, up-to-date status.**

- Directory skeleton (with `.gitkeep` in every empty dir — one was
  missed in the first pass, `quality-audits/.gitkeep`, and caught
  immediately by CI's `structure-check` job on the first real run;
  fixed in a follow-up commit), `docs/curriculum/CURRICULUM_MAP.md`,
  `docs/course-architecture.md`, `README.md`, this file,
  `PROJECT_STATE.md`, `LICENSE`/`LICENSE-CONTENT`, `CONTRIBUTING.md`,
  `CHANGELOG.md`.
- `templates/` and shared `assets/` copied from
  `ai-coding-agents-for-everyone` and rebranded
  (`window.AISFE_MODULES`, `window.AISFEProgress`,
  `aisfe-progress` localStorage key) — structure only, no content
  reused. Includes `templates/written-exam.template.html` from day one.
- **CI (`.github/workflows/ci.yml`) and `scripts/local_check.sh`**
  copied from `ai-coding-agents-for-everyone`, already including the
  `# CI: LONG_RUNNING_SERVER` / `# CI: NEEDS_LIVE_SERVER=` marker
  convention and `practice/solution.py` coverage.
- **Homepage (`index.html`) and roadmap
  (`docs/curriculum/index.html`) built from day one**, not deferred.
- **Pushed to GitHub** (`TechNaom/ai-security-for-everyone`, public),
  GitHub Pages enabled, both CI Checks and Deploy GitHub Pages verified
  green on real runners.
- **Chapter 1 ("Threat Modeling LLM Systems: The OWASP Top 10 for LLM
  Applications") is built and live** — the reference chapter. See
  `quality-audits/chapter-01-audit.md`. Its build was interrupted
  mid-session by an environment restart; resumed cleanly with prior
  partial work verified and kept, not redone — worth knowing this
  pattern works if it happens again.

## Naming conventions

- Chapter folders: `chapters/chapter-NN-kebab-slug/`, matching the
  rest of the ecosystem.
- Repo name: `ai-security-for-everyone`, GitHub org `TechNaom`,
  public, `main` branch — confirmed and created 2026-08-10.

## What NOT to change

- Don't restructure the repo layout without checking
  `docs/course-architecture.md` — mirrors `ai-coding-agents-for-everyone`
  deliberately.
- Don't assume any model's behavior under a specific injection/
  jailbreak technique without testing it against the real, installed
  model first — the same test-before-write discipline every sibling
  course has followed, applied here to attack demonstrations
  specifically: an untested claim that a technique works is worse than
  useless in a security course, it's actively misleading.
- Use `python-for-everyone`'s richer per-chapter file pattern
  (README.md in exercises/practice/project, `interview-questions.md`)
  from Chapter 1 onward — this course doesn't have the "Chapter 7
  onward" exception `ai-coding-agents-for-everyone` had, since that
  pattern is now the ecosystem default going forward.
- Every attack technique needs a real, working defense paired with it,
  framed as defensive/educational, with no ready-to-use exploit
  content targeting a named real product — this is a hard constraint,
  not a style preference.
- Don't hardcode a chapter-specific case into `ci.yml` — use the
  existing `# CI: LONG_RUNNING_SERVER` / `# CI: NEEDS_LIVE_SERVER=`
  markers, already wired in.
- Don't copy lesson content, examples, or project stories from any
  sibling TechNaom repo — structure/templates only.

## Current task

**The course is complete. All 13 chapters, all 6 modules, and all 4
project tiers are done and live.** Modules 1, 3, 4, 5, and 6 confirmed
not needing a separate written exam — each is fully satisfied by its own
chapters' exercises/projects (Module 2 is the sole exception, with a
dedicated written exam). Chapter 10 completed Module 4, shipping the L3
Independent project; Chapter 11 started Module 5 with a rubric-graded
findings-report project; Chapter 12 closed Module 5 with a find-and-fix
defense lab.

**Chapter 13 ("Capstone: Security Architecture for a Real LLM System,"
Module 6, Architect) is built and live, closing Module 6 and the entire
course.** A synthesis chapter, not a new-attack chapter — the L4
Architecture Challenge, the course's fourth and final project tier.
Deliberately breaks every prior chapter's incident-first hook pattern:
no incident, a pure business-problem brief (Cinderpeak Systems' Aegis
Copilot, a multi-tenant AI workflow platform 8 weeks from GA with no
major incident) — the skill taught is designing defenses before a
failure exists to diagnose. Gives the full OWASP GenAI LLM Top 10 2026
(all ten categories) for the first time in this course, re-verified live
this session that the ranking is unchanged since Chapter 12 shipped, and
honestly names two categories (LLM06 Unbounded Consumption, LLM07
Misinformation) this course never built a dedicated chapter for. Teaches
Architecture Decision Records tagged with Chapter 5's structural/
detection/consequence-bounding defense taxonomy, a full worked
sandboxing-tradeoff example (referencing `mcp-for-everyone` and
`ai-coding-agents-for-everyone`'s own agent-sandboxing depth), and
requires a self-directed red-team pass against the learner's own design
using Chapter 11's methodology. Ollama checked fresh this session:
`/api/tags` OK, `/api/chat` timed out after a 20-second timeout (exit
code 28) — same persistent hang as every chapter since Chapter 3,
disclosed honestly and noted as not load-bearing for a design-only
deliverable. Project (`project/RUBRIC.md`, six criteria, 24 points) has
one more criterion than every prior chapter's rubric, reflecting the
added judgment a Level 4 challenge requires; `project/solution.py`
deliberately leaves the launch-recommendation criterion incomplete,
following Chapter 11's own precedent. See
`quality-audits/chapter-13-audit.md` for the full detail.

## Next task after that

**There is no next chapter.** The course is finished. This session also
completed the course-wide final polish pass: a standalone link-walker
script checked all 81 real content HTML files (957 internal links, 0
broken), `scripts/local_check.sh` passed clean, and an OWASP-numbering
consistency check confirmed no chapter presents 2025 numbering as
currently authoritative. See `PROJECT_STATE.md`'s "Next Recommended
Task" section for the full, honest statement of what (if anything)
remains — as of this update, nothing required, only routine items
(pushing this session's commit, the next CI/Pages verification) and one
optional, out-of-scope item (whether sibling repos want to add
forward-links to this now-complete course, a cross-repo decision, not a
gap in this repo).

## Important architectural decisions (see PROJECT_STATE.md for full detail)

1. Model/API policy inherited directly from
   `ai-coding-agents-for-everyone`: `openai` package pointed at
   Ollama's local endpoint by default, zero cost/key, documented
   hosted-provider-swap option (more relevant here — testing against a
   production model's real safety training is a legitimate reason to
   use it).
2. 13 chapters, focused-topic sizing.
3. Static site, no backend, mirrors `ai-coding-agents-for-everyone`
   exactly.
4. Deliberately does NOT duplicate `mcp-for-everyone`'s Module 5 or
   `ai-coding-agents-for-everyone`'s Chapter 11 — links back to both,
   builds on top with LLM-specific depth those courses didn't cover.
5. Every attack pairs with a real defense; defensive/educational
   framing; no ready-to-use exploits against named real products —
   non-negotiable, not a style choice.
