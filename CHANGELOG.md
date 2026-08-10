# Changelog

All notable changes to this course are logged here, newest first.

## 2026-08-10 — Repository scaffolded

- Discovery completed: course vision, 4 personas, prerequisites,
  learning outcomes, 6-module/13-chapter structure, project ladder
  (L1-L4), capstone shape, cross-course overlap check confirmed no
  duplication with `mcp-for-everyone`, `ai-coding-agents-for-everyone`,
  `genai-for-everyone`, or `rag-for-everyone`.
- `docs/curriculum/CURRICULUM_MAP.md` and `docs/course-architecture.md`
  written.
- Repository structure scaffolded from `ai-coding-agents-for-everyone`
  (structure only — no content reused): directories with `.gitkeep`
  from the start, shared `assets/` rebranded (`AISFE_MODULES`,
  `AISFEProgress`, `aisfe-progress`), `templates/` (including
  `written-exam.template.html` from day one), CI
  (`.github/workflows/ci.yml`, `scripts/local_check.sh`) already
  including the `practice/solution.py` coverage and `nullglob` fix that
  course needed to add after its own first real CI run.
- Model/API policy inherited directly from
  `ai-coding-agents-for-everyone`: `openai` client pointed at Ollama's
  local endpoint by default, documented hosted-provider-swap option.
- README.md, PROJECT_STATE.md, AI_HANDOFF.md, CONTRIBUTING.md,
  LICENSE/LICENSE-CONTENT written.
- No chapter content yet. Not yet pushed to GitHub — pending user
  confirmation to create the public repo.
