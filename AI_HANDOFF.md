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

## Current state (as of 2026-08-14, Chapters 1-12 live, Module 5 complete)

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

**Chapters 1-12 (Modules 1-5, all complete) are done and live, plus the
Module 2 written exam.** Modules 1, 3, 4, and now 5 confirmed not
needing a separate written exam — satisfied by the chapters' own
exercises/projects. Chapter 10 ("Securing Agentic Systems Against
Adversarial Tool Output," Module 4, Advanced) completed Module 4,
shipping the course's L3 Independent project. See
`quality-audits/chapter-10-audit.md` for full detail.

**Chapter 11 ("Red-Teaming an LLM System: Methodology and Practice,"
Module 5, Advanced) is built and live, starting Module 5.** A process
chapter teaching a five-phase red-teaming methodology, grounded in five
real, independently-verified sources (OWASP's GenAI Red Teaming Guide,
NIST's Generative AI Profile, Microsoft's and OpenAI's red-teaming
papers, Anthropic's Frontier Red Team methodology). Hook is Alderglen
Financial's Ledger Copilot; project ships a rubric-graded findings
report. See `quality-audits/chapter-11-audit.md` for full detail.

**Chapter 12 ("Handling LLM Output Safely: PII and Downstream Injection
Risk," Module 5, Advanced) is built and live, closing Module 5.** Covers
the *output* side of LLM risk (PII leakage in generated text,
downstream injection risk carried FROM generated content) — the
explicit inversion of Modules 2 and 4's input-side focus, named the way
Chapter 7 named its own inversion relative to Chapters 3-6. Verified
live this session: the **OWASP GenAI LLM Top 10 2026** shipped August 4,
2026, confirming the edition Chapter 11's research had flagged but not
confirmed — LLM02:2026 Sensitive Information Disclosure holds its #2
rank; Improper Output Handling moved from LLM05:2025 to **LLM10:2026**
(scope expanded). This chapter uses 2026 numbering going forward. A
brief, technical-practitioner-scoped GDPR/CCPA mention is included, per
the curriculum map's deferral of deep compliance framing to a future
course. Hook is Fenwick Customer Experience's TicketSense; the project
is a **find-and-fix defense lab** (not a second findings report),
explicitly justified since this chapter's skill is building output-side
controls and Chapter 11's project already satisfies Module 5's stated
assessment type. Ollama checked fresh this session: `/api/tags` OK,
`/api/chat` timed out after a 20-second timeout (exit code 28) — same
persistent hang as Chapters 3, 4, 5, 9, 10, 11. **Module 5 exam decision:
resolved, no separate written exam** — Chapter 11's project alone
satisfies the curriculum map's stated Module 5 assessment type, the same
judgment call as Modules 1, 3, and 4. See
`quality-audits/chapter-12-audit.md` for the full detail.

## Next task after that

**Build Chapter 13 next: "Capstone: Security Architecture for a Real LLM
System," Module 6, Architect — the final chapter, closing the course.**
Full curriculum-map text and a detailed build brief now live in
`PROJECT_STATE.md`'s "Next Recommended Task" section — read that section
in full before starting. Key points not to lose:

1. This is a synthesis chapter drawing on all 12 prior chapters, not a
   new-attack chapter — the L4 Architecture Challenge (per
   `CURRICULUM_MAP.md`'s Projects section: "design a security
   architecture for a realistic LLM system, with a red-team report and
   full ADRs; business problem only"). It should require learners to
   *use* Chapter 11's red-teaming methodology and Chapter 12's
   output-handling checklist as inputs, not re-teach either.
2. Use **OWASP 2026 numbering** throughout (LLM01:2026 through
   LLM10:2026) — Chapter 12 confirmed and adopted this edition; Chapter
   13 should follow suit, with a brief 2025-to-2026 mapping note if
   referencing Chapters 1-11's own citations.
3. Architect difficulty tier — the only chapter at that level. Should
   read as a genuine step up from every prior chapter's Advanced tier.
4. New fictional org, distinct from every org used across Chapters
   1-12 — the full updated list is in `PROJECT_STATE.md`'s Chapter 13
   build notes.
5. Check Ollama status fresh at the start of that session — don't assume
   Chapter 12's hang carries forward.
6. This is the last chapter — after validating it with
   `quality-audits/chapter-13-audit.md`, the remaining work is the
   course-wide final polish pass (link-integrity sweep, CI/Pages
   verification, a numbering-consistency check), not another chapter.

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
