# AI Security for Everyone

Free, interactive course on securing LLM-powered systems: threat
modeling, prompt injection and jailbreaking in depth, data/model
integrity, securing RAG and agentic systems, red-teaming, and safe
output handling — closing with a full security-architecture capstone.

🔗 **Repo:** <https://github.com/TechNaom/ai-security-for-everyone>
🔗 **Live UI:** <https://technaom.github.io/ai-security-for-everyone/>
*(GitHub Pages not yet enabled — no root `index.html` yet)*

This course follows the same philosophy as `ai-coding-agents-for-everyone`:

- Plain-language first, without hiding the real engineering.
- One chapter at a time, validated before scaling.
- No signup required to *read or run* the course. Hands-on chapters
  that need a real model run against a local, open-source model via
  [Ollama](https://ollama.com) by default — no API key, no account, no
  per-run cost — with a documented option to point the same code at a
  hosted provider instead, useful here specifically for testing an
  attack against a production-grade model's actual built-in defenses.
- Browser-first learning pages.
- Every attack demonstration is paired with a real, working defense —
  this is a defensive/educational security course, not an offense-only
  one, and no content ships as a ready-to-use exploit against a named
  real-world product.
- Hands-on code tested against a real, installed model before being
  written into a lesson.
- Interview-ready explanations.
- Strong architecture and trade-off thinking.

All examples, attack demonstrations, defenses, exercises, projects, and
thought-process journals in this course are original.

## What this is

`AI Security for Everyone` goes deep on LLM-specific security where
sibling TechNaom courses only went one module or chapter wide:
`mcp-for-everyone` covered MCP-specific permission/sandboxing,
`ai-coding-agents-for-everyone` covered agent-specific CI/permission
security. This course covers the OWASP Top 10 for LLM Applications,
prompt injection and jailbreaking in real depth, data poisoning, model
extraction, supply-chain risk, securing RAG and agentic systems
specifically, a real red-teaming methodology, and safe output handling
— closing with a capstone that designs a full security architecture
for a realistic LLM system.

## Model/API versions

Hands-on chapters that need a real model (constructing and testing
injections, evaluating defenses, red-teaming) use the plain **`openai`**
Python package (`pip install openai`) pointed, by default, at
**Ollama**'s local OpenAI-compatible endpoint — zero cost, zero API
key. A documented option points the exact same code at a hosted
provider (OpenAI, Anthropic, Gemini — all expose OpenAI-compatible
endpoints) for learners who want to test against a production model's
real safety training specifically. See `docs/course-architecture.md`
for the full policy and reasoning (inherited from
`ai-coding-agents-for-everyone`, not re-litigated here).

## Who this is for

- **AppSec engineers** who know web/infra security and are new to
  LLM-specific attack surface.
- **ML/AI engineers** who build LLM features and have never done
  security work.
- **Red-teamers / pentesters** expanding into AI systems.
- **Engineering leads** threat-modeling an LLM feature or setting team
  security standards.

## Learning path

See [`docs/curriculum/CURRICULUM_MAP.md`](docs/curriculum/CURRICULUM_MAP.md)
for the full module/chapter roadmap, learning outcomes, and project ladder.

## Repository structure

```text
ai-security-for-everyone/
  chapters/            per-chapter lessons, quizzes, labs, interview prep
  docs/curriculum/      curriculum map (source of truth) + styled roadmap
  docs/course-architecture.md
  templates/            reusable chapter/quiz/lab/project templates
  assessments/          quizzes, written exams, interview questions, ADR-style
                         architecture challenges
  quality-audits/       per-chapter quality gate checklists
  codebase/              starters, solutions, shared code, datasets
  assets/                shared site styling, sidebar, progress, quiz engine
  PROJECT_STATE.md       current build status (read this first)
  AI_HANDOFF.md          for any AI coding assistant picking this up cold
```

## How to start

This repo is under active construction. See `PROJECT_STATE.md` for
what's built and what's next.

## Projects

Four project levels, from guided to architecture-challenge — see the
curriculum map's Projects section.

## Capstone

Design and defend a full security architecture for a realistic LLM
system, with a red-team report and full ADRs, matching the same
ADR/architecture rigor as `ai-coding-agents-for-everyone`'s capstone.

## Contributing

Solo-maintained; not open to external PRs. See `CONTRIBUTING.md` if
you're forking this for your own use.

## License

Code is licensed under [MIT](LICENSE). Educational content (lessons,
diagrams, exercises, interview questions) is licensed under
[CC BY 4.0](LICENSE-CONTENT).
