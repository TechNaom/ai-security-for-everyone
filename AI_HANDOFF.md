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

## Current state (as of 2026-08-10, freshly scaffolded)

**Read `PROJECT_STATE.md` for the authoritative, up-to-date status.**

- Directory skeleton (with `.gitkeep` in every empty dir from the
  start — a bootstrap bug found in `ai-coding-agents-for-everyone`,
  avoided here by starting with the fix already in place),
  `docs/curriculum/CURRICULUM_MAP.md`, `docs/course-architecture.md`,
  `README.md`, this file, `PROJECT_STATE.md`, `LICENSE`/`LICENSE-CONTENT`.
- `templates/` and shared `assets/` copied from
  `ai-coding-agents-for-everyone` and rebranded
  (`window.AISFE_MODULES`, `window.AISFEProgress`,
  `aisfe-progress` localStorage key) — structure only, no content
  reused. Includes `templates/written-exam.template.html` from day
  one — that course had raw, unstyled `.md` exam files until a user-
  reported gap got fixed late; don't reintroduce that gap here.
- **CI (`.github/workflows/ci.yml`) and `scripts/local_check.sh`**
  copied from `ai-coding-agents-for-everyone` and already include: the
  `# CI: LONG_RUNNING_SERVER` / `# CI: NEEDS_LIVE_SERVER=` marker
  convention, `practice/solution.py` coverage (that course initially
  only ran `exercises/`+`project/` solutions and had to extend this
  after the fact — start with it already fixed), and the
  `shopt -s nullglob` fix for the structure-check job's chapter-audit
  loop (also found and fixed there after the first real CI run).
- **NOT YET pushed to GitHub.** No chapter content exists yet. No
  website (`index.html`) yet.

## Naming conventions

- Chapter folders: `chapters/chapter-NN-kebab-slug/`, matching the
  rest of the ecosystem.
- Repo name: `ai-security-for-everyone`, GitHub org `TechNaom`
  (planned, not yet created — confirm with the user before creating
  the public repo and pushing, same courtesy check used for
  `ai-coding-agents-for-everyone`).

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

Confirm with the user before creating the public GitHub repo
(`TechNaom/ai-security-for-everyone`) and pushing the scaffold. Once
confirmed: `git init`, `gh repo create ... --public --source=.
--remote=origin --push`, then verify CI Checks and Deploy GitHub Pages
both pass on the real GitHub Actions runners — don't consider the
scaffold done until both are confirmed green there, not just locally.

## Next task after that

Build Chapter 1 ("Threat Modeling LLM Systems: The OWASP Top 10 for
LLM Applications") as the reference chapter — Module 1 is fully
conceptual (no live-model dependency), a good place to start and
validate the template before Module 2 needs real model calls for
constructing/testing prompt injections. Verify Ollama's current model
recommendation and its actual behavior under injection/jailbreak
testing before writing Chapter 3's content — don't assume a technique
works against the installed model without testing it. Then continue
module by module per `docs/curriculum/CURRICULUM_MAP.md`, validating
each with a `quality-audits/chapter-0N-audit.md` before moving on.
Don't mass-generate ahead of validation.

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
