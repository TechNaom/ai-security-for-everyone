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

## Current state (as of 2026-08-12, Chapters 1-10 live, Module 4 complete)

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

**Chapters 1-10 (Modules 1-4) are done and live, plus the Module 2
written exam.** Module 3 confirmed not needing a separate written exam —
same judgment call as Module 1 (satisfied by the chapters' own
exercises/project). Chapter 9 ("Securing RAG Pipelines Against
Injection") went deep on Chapter 4's own "preview of that depth" line
for RAG chunks specifically, using a three-pipeline-stage framing
(ingestion/retrieval/generation-output) independently validated by
OWASP's own 2026 RAG Security Cheat Sheet's identical structure. Its
hook is Vesper Cloud's Vesper Assistant; its project is a real, complete
lab (find and fix the exact RAG-corpus injection vector from the
lesson's own incident) explicitly framed as NOT the final L3 project.
See `quality-audits/chapter-09-audit.md` for the full detail, including
the honest Ollama disclosure (`/api/tags` OK, `/api/chat` hung again,
curl exit code 28 — same persistent issue as Chapters 3-5).

**Chapter 10 ("Securing Agentic Systems Against Adversarial Tool
Output," Module 4, Advanced) is built and live, completing Module 4.**
Its `lesson.html` was written by a prior session interrupted mid-build
by a rate limit; the follow-up session read it in full first, confirmed
it was complete and internally consistent with no truncation or
leftover TODOs, and built the rest of the chapter on top of it rather
than rewriting it — worth knowing this pattern works if it happens
again (same lesson Chapter 1's own audit already recorded once). Chapter
10 organizes tool-call risk by three round-trip moments (result arrival,
context assembly, action proposal) — deliberately NOT a reuse of Chapter
9's pipeline-stage device, since a tool call's request/response shape is
genuinely different from a pipeline's. Hook is Ferngate Logistics'
Dispatch Copilot; the L3 project extends Chapter 9's own Vesper Cloud
corpus (confirmed byte-identical by direct diff) with a new tool call,
`check_partner_sync_diagnostic`, whose `diagnostic_note` field can carry
a planted instruction the same way a RAG chunk can — genuinely
no-scaffold (`starter.py` has zero `# TODO` markers). **Module 4 exam
decision: no separate written exam** — the L3 project itself satisfies
Module 4's "applied security-review exercise" assessment type, same
judgment call as Modules 1 and 3. See `quality-audits/chapter-10-audit.md`
for the full detail.

## Next task after that

**Build Module 5 next: Chapter 11 ("Red-Teaming an LLM System:
Methodology and Practice") and Chapter 12 ("Handling LLM Output Safely:
PII and Downstream Injection Risk").** Full curriculum-map text and a
detailed, chapter-by-chapter build brief (matching the level of detail
this file's Chapter 10 brief had) now live in `PROJECT_STATE.md`'s "Next
Recommended Task" section — read that section in full before starting.
Key points not to lose:

1. Module 5's own assessment type is a genuinely new deliverable shape
   for this course: "red-team report graded against a rubric," not a
   project/lab or a written exam like every module so far — decide
   explicitly how that reshapes Chapter 11's `project/` folder (and
   possibly needs a rubric document) before building it.
2. Chapter 11 is a methodology/process chapter (how to run a structured
   red-team exercise), not a re-teaching of attack techniques Modules
   2-4 already built in depth — same relationship Chapter 2 had to
   Chapter 1's threat-modeling depth, and Chapter 5 had to Chapters 3-4's
   injection-technique depth.
3. Chapter 12 covers the *output* side of LLM risk (what a model
   generates becoming a downstream attack vector) — the mirror image of
   everything Modules 2 and 4 covered (untrusted input reaching the
   model). Chapter 1 already flagged Improper Output Handling (LLM05)
   as "Chapter 12 builds a full chapter on exactly this" — read that
   section first, the same discipline Chapter 10 followed for Chapter 1
   and Chapter 8's own deferred material.
4. New fictional orgs for both chapters, distinct from every org used
   across Chapters 1-10 — the full list is in `PROJECT_STATE.md`'s
   Chapter 11 build notes.
5. Check Ollama status fresh at the start of that session — don't assume
   Chapters 9-10's hang carries forward; a red-teaming chapter is
   exactly the kind that would benefit most from testing this directly
   rather than assuming it's still broken.

Then Chapter 13 (capstone, Module 6). Continue module by module,
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
