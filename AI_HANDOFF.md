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

## Current state (as of 2026-08-12, Chapters 1-11 live, Module 5 started)

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

**Chapters 1-11 (Modules 1-5, partial) are done and live, plus the
Module 2 written exam.** Modules 1, 3, and 4 confirmed not needing a
separate written exam — satisfied by the chapters' own
exercises/project. Chapter 10 ("Securing Agentic Systems Against
Adversarial Tool Output," Module 4, Advanced) completed Module 4,
shipping the course's real, final L3 Independent project (extending
Chapter 9's Vesper Cloud corpus with a combined RAG-plus-tool-output
vector, genuinely no-scaffold). See `quality-audits/chapter-10-audit.md`
for full detail.

**Chapter 11 ("Red-Teaming an LLM System: Methodology and Practice,"
Module 5, Advanced) is built and live, starting Module 5.** It's a
process chapter, not a new-attack chapter — the third instance of the
"process chapter building on established mechanism" pattern (Chapter 2
on Chapter 1, Chapter 5 on Chapters 3-4) — teaching a five-phase
red-teaming methodology (scoping/rules of engagement, threat-model-
driven test-case design using Chapter 1's OWASP Top 10 as the
structuring device, systematic execution/documentation, severity/impact
classification, findings-report writing) that draws on Chapters 3-10's
own attack taxonomy as its arsenal, mapped explicitly to all ten OWASP
categories in the lesson's own table. Grounded in five real,
independently-verified sources: OWASP GenAI Security Project's GenAI Red
Teaming Guide (Jan 2025), NIST's Generative AI Profile (NIST-AI-600-1),
Microsoft's "Lessons from Red Teaming 100 Generative AI Products"
(arXiv:2501.07238), OpenAI's "Approach to External Red Teaming for AI
Models and Systems" (arXiv:2503.16431), and Anthropic's published
Frontier Red Team methodology. Hook is Alderglen Financial's Ledger
Copilot; the project is Module 5's own new deliverable shape — a
rubric-graded findings report (`project/RUBRIC.md`) against a fresh,
self-contained target (Ledger Copilot again, three planted
vulnerabilities mirroring Chapter 3/4/9/10's mechanisms), explicitly not
a byte-identical reuse of Chapter 9/10's Vesper Cloud pipeline, choice
justified in `project/README.md`. **Module 5 exam decision: explicitly
deferred to after Chapter 12 ships** — unlike every prior module,
Module 5's assessment type spans both chapters in the curriculum map's
own framing, and Chapter 12 covers a risk direction Chapter 11's project
doesn't exercise. Ollama checked fresh this session: `/api/tags` OK,
`/api/chat` timed out after a 20-second timeout (exit code 28) — same
persistent hang as Chapters 3, 4, 5, 9, 10. See
`quality-audits/chapter-11-audit.md` for the full detail.

## Next task after that

**Build Chapter 12 next: "Handling LLM Output Safely: PII and
Downstream Injection Risk," Module 5, Advanced — closes Module 5.** Full
curriculum-map text and a detailed build brief now live in
`PROJECT_STATE.md`'s "Next Recommended Task" section — read that section
in full before starting. Key points not to lose:

1. Chapter 12 covers the *output* side of LLM risk (what a model
   generates becoming a downstream attack vector) — the mirror image of
   everything Modules 2 and 4 covered (untrusted input reaching the
   model). Chapter 1 already flagged Improper Output Handling (LLM05)
   as "Chapter 12 builds a full chapter on exactly this," and Chapter
   11's own arsenal table restates that exact deferral — read both
   sections first, the same discipline Chapter 10 followed for Chapter 1
   and Chapter 8's own deferred material.
2. PII handling needs its own real, cited grounding — check current
   OWASP guidance (LLM02:2025 is the input-side entry; verify
   output-specific guidance), and check live whether OWASP has moved to
   a 2026 Top 10 edition (Chapter 11's own research turned up a
   reference to an "OWASP GenAI LLM Top 10 2026" resource — verify this
   directly before citing, since it may supersede the 2025 numbering
   Chapters 1-11 have used throughout). Keep any GDPR/CCPA regulatory
   mention brief and technical-practitioner-focused — this course
   defers deep compliance framing to a future `AI Governance for
   Everyone` course.
3. "Downstream injection risk in generated content" is the more novel
   half — a model's own output carrying an injection payload FROM the
   model's generation, not TO it, consumed by a downstream system
   (rendered webpage, another agent, a downstream API). Architecturally
   the mirror image of Modules 2 and 4's input-side risk — worth naming
   that inversion explicitly, the way Chapter 7 named its own "attacker
   touches neither the model nor its training data" inversion.
4. This chapter closes Module 5. Chapter 11 already shipped a rubric-
   graded findings-report project against Ledger Copilot; decide
   explicitly whether Chapter 12 needs its own separate findings-report
   deliverable (red-teaming the output side specifically) or a different
   project shape (e.g., a find-and-fix lab on output-handling defenses),
   and state the choice, the same way Chapter 11 justified its own
   fresh-target choice.
5. New fictional org, distinct from every org used across Chapters 1-11
   — the full updated list (including Alderglen Financial, Corvette Bay
   Utilities, and Chapter 11's eight practice-bank orgs) is in
   `PROJECT_STATE.md`'s Chapter 12 build notes.
6. Check Ollama status fresh at the start of that session — don't assume
   Chapter 11's hang carries forward.

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
