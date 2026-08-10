# AI Security for Everyone — Course Architecture

## Reference Pattern

Structural reference: `TechNaom/ai-coding-agents-for-everyone` (the
most recent, most refined pattern in the ecosystem — not
`mcp-for-everyone`, which it itself superseded). Reuse:

- Root `index.html` GitHub Pages entry point + `docs/curriculum/index.html`
  styled roadmap.
- Shared `assets/` (style.css, sidebar.js, progress.js, quiz-engine.js,
  home.js, chapters-data.js) — copied and rebranded, structure only.
- `chapters/chapter-XX-slug/` per-chapter folders using
  **`python-for-everyone`'s richer file pattern** (per
  [[feedback-course-structural-reference]]): `lesson.html`, `quiz.html`,
  `interview-questions.html` + `.md`, `exercises/{index.html,starter.py,
  solution.py,README.md}`, `practice/{index.html,starter.py,solution.py,
  README.md}`, `project/{index.html,starter.py,solution.py,README.md}`
  (+ `ai-paired.html` where a chapter's subject genuinely fits that
  pattern) — not the thinner mcp-for-everyone pattern.
- `templates/`, `assessments/` (including `templates/written-exam.template.html`
  rendered as styled HTML, not raw `.md` — a gap found and fixed in
  `ai-coding-agents-for-everyone` after user feedback; don't reintroduce
  it here), `quality-audits/`.
- `PROJECT_STATE.md`, `AI_HANDOFF.md` from day one.
- **CI**: `.github/workflows/ci.yml` and `scripts/local_check.sh`
  copied from `ai-coding-agents-for-everyone` and adapted — includes
  the `# CI: LONG_RUNNING_SERVER` / `# CI: NEEDS_LIVE_SERVER=` marker
  convention, the `practice/solution.py` coverage (a gap found and
  fixed there — start with it fixed here), and the `.gitkeep` /
  `nullglob` fixes for empty-directory bootstrapping (also found there
  — apply from the start, don't rediscover).

Do not reuse any sibling course's lesson content, examples, or project
stories. All security examples, attack demonstrations, and interview
answers must be original to this course.

## Production Depth Standard

Same bar as the rest of the ecosystem: 6+ exercises (3+ production-gear)
per chapter, 6+ practice scenarios, 8+ interview questions across all 4
levels, a tested project. Every code example — including attack
demonstrations and defenses — must be run against a real target before
being written into a lesson.

## Model/API Policy for Hands-On Security Labs

This course needs real model calls for several chapters (constructing
and testing prompt injections, evaluating a defense, running red-team
exercises). Follow `ai-coding-agents-for-everyone`'s resolved policy
exactly, don't re-litigate it: **fully local, open-source by default**
via the plain `openai` Python package pointed at **Ollama**'s local
OpenAI-compatible endpoint (`base_url="http://localhost:11434/v1"`),
zero API key, zero cost, for every learner. Include the same
documented, one-parameter "use a hosted provider instead" option
(OpenAI, Anthropic, Gemini all expose OpenAI-compatible endpoints) for
learners who want to test attacks against a production-grade model's
actual defenses specifically — this is arguably MORE relevant here
than in the agent-building course, since a hosted model's built-in
safety training is itself part of what a learner may want to probe.
State that testing against a hosted provider still costs real money
and requires a real account, same disclosure standard as before.

Verify the current Ollama model recommendation and its actual
behavior under injection/jailbreak testing before writing any chapter
that demonstrates an attack — do not assume a model's susceptibility
to a specific technique without testing it against the real, installed
model first. A claimed vulnerability that doesn't actually reproduce
against the model in use undermines the entire chapter's credibility.

## Security-Specific Ethical Framing (non-negotiable)

Every attack technique taught in this course must be paired with: (1)
a real, working defense or mitigation, never presented as unsolved,
(2) explicit framing as defensive/educational (this is a
security-research and defense-building course, not an offense-only
course), and (3) no content that would function as a ready-to-use
attack against a real production system without adaptation — examples
should demonstrate mechanism, not ship exploit payloads targeting any
specific named real-world product or service.

## Conversational Clarity Standard

Same as the rest of the ecosystem: explain like a helpful expert
beside the learner, story-first, senior-level trade-offs unpacked
patiently — including for attack techniques, where the "why does this
work" mechanism matters more than the payload itself.

## Builder Thought-Process Layer

Every chapter includes a visible reasoning section (problem framing,
options considered, chosen approach, validation, observed failure,
decision) — same pattern as the rest of the ecosystem, adapted to
security decisions (what's the actual threat model, what does this
defense really stop vs. claim to stop, what's the residual risk after
mitigation).
