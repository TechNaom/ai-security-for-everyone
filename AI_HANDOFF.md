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

## Current state (as of 2026-08-11, Chapter 1 live)

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

Chapter 1 (reference chapter) is done and live. Build Chapter 2
("Mapping the Attack Surface of a Real LLM Feature," Module 1,
Intermediate) next — completes Module 1 and ships the real L1 project
("threat-model a real, given LLM feature end to end"; Chapter 1's own
project page is a short preview pointing here). Still conceptual, no
live-model dependency. Read Chapter 1 fully first — apply its exact
OWASP Top 10 framework to a new, different realistic feature (not
GreenCart again), going deeper on actually producing a threat-model
artifact than Chapter 1's walkthrough did.

## Next task after that

After Module 1, Module 2 (Chapters 3-5) begins needing a real model
for constructing/testing prompt injections — verify Ollama's current
model recommendation and its actual behavior under injection/jailbreak
testing before writing Chapter 3. Do not assume a technique works
against the installed model without testing it first — an untested
attack claim is actively misleading in a security course, more so than
in the agent-building course this repo's CI/docs were copied from.
Then continue module by module per `docs/curriculum/CURRICULUM_MAP.md`,
validating each with a `quality-audits/chapter-0N-audit.md` before
moving on. Don't mass-generate ahead of validation.

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
