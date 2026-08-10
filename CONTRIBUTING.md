# Maintenance Guide (Solo-Maintained Project)

This repo is maintained solely by its owner — it is **not open to
external contributions**. Issues and pull requests from outside
contributors are not reviewed or merged. If you found this repo
useful, feel free to fork it for your own use per the license
(`LICENSE` for code, `LICENSE-CONTENT` for lesson content), but please
don't open issues or PRs here.

This doc is a working reference for how content gets added or updated,
so nothing drifts from the repo's conventions as it grows.

## The non-negotiable rule: test before you write

This rule is inherited from `mcp-for-everyone` and
`ai-coding-agents-for-everyone`, where it caught real, non-obvious
bugs repeatedly (see those repos' `PROJECT_STATE.md` files for the
full lists) — it applies here from day one. Every code example in
every chapter — including every attack demonstration and every
defense — must be installed and run against the real `openai` client
pointed at a real local Ollama server with a real model pulled (or
`mcp[cli]` for the agentic-systems chapter) before being written into
a lesson — never written from memory or copied from older tutorials.
**Do not relax this for any edit, however small it seems.** For a
security course specifically: an untested claim that an attack
technique works, or that a defense stops it, is worse than useless —
it's actively misleading in a course whose entire subject is knowing
what actually works. If you're adding or changing a code sample:

```bash
python3 -m venv /tmp/aisfe-test-env
/tmp/aisfe-test-env/bin/pip install openai "mcp[cli]"
# ollama pull <model>  -- see PROJECT_STATE.md for the current
# recommended model; requires a running local Ollama server
# (https://ollama.com), no API key or account needed.
# The openai client points at it via base_url="http://localhost:11434/v1".
/tmp/aisfe-test-env/bin/python your_new_example.py
```

Only write the example into the lesson once you've seen its real
output.

## The security-specific rule: every attack pairs with a real defense

Non-negotiable, checked on every chapter: any attack technique taught
must be paired with a real, working defense or mitigation shown in the
same chapter — never presented as unsolved. Framing is
defensive/educational throughout. No content ships as a ready-to-use
exploit against any named real-world product or service — demonstrate
mechanism (why the attack works, what the defense actually changes),
not a copy-pasteable payload aimed at a specific real target.

## Adding or updating a chapter

1. Follow `python-for-everyone`'s richer per-chapter file pattern from
   Chapter 1 (this course's default, not a later exception):
   `lesson.html`, `quiz.html`, `interview-questions.html` +
   `interview-questions.md`,
   `exercises/{index.html,starter.py,solution.py,README.md}`,
   `practice/{index.html,starter.py,solution.py,README.md}`,
   `project/{index.html,starter.py,solution.py,README.md}` (+
   `ai-paired.html` where a chapter's subject genuinely fits that
   pattern). Chapter 1 becomes the reference chapter once built.
2. Test every code sample per the rule above before writing it into
   the lesson — including verifying an attack actually reproduces
   against the real, installed model before claiming it does.
3. Wire the chapter into `assets/chapters-data.js` — give it a `path`
   only once its `lesson.html` actually exists (see that file's header
   comment for why a premature `path` breaks the site).
4. Update `docs/curriculum/index.html` (the styled roadmap) and the
   root `index.html`'s chapter count in `hero-stats`.
5. Write a quality audit at `quality-audits/chapter-0N-audit.md`
   following the format of existing audits, including a live-tested-
   vs-logical-only disclosure section.
6. Run the local checks below before pushing.

## Local checks before pushing

```bash
bash scripts/local_check.sh < /dev/null
```

Use `< /dev/null` if any chapter's code calls `input()` for a live
interactive demo (redirecting stdin from `/dev/null` matches real CI's
stdin-closed behavior — an open interactive shell will make `input()`
block for real instead of hitting `EOFError` the way it does in CI).
This runs the same checks CI runs: folder structure, placeholder-text
scan, Python syntax + actual execution of every `solution.py`
(exercises, practice, and project), JS syntax, chapter-path validation
against `chapters-data.js`, and a secret scan. If it fails, CI will
fail too — fix locally first.

## File naming convention

```
chapters/chapter-NN-kebab-slug/lesson.html
chapters/chapter-NN-kebab-slug/quiz.html
chapters/chapter-NN-kebab-slug/interview-questions.html
chapters/chapter-NN-kebab-slug/interview-questions.md
chapters/chapter-NN-kebab-slug/exercises/{index.html,starter.py,solution.py,README.md}
chapters/chapter-NN-kebab-slug/practice/{index.html,starter.py,solution.py,README.md}
chapters/chapter-NN-kebab-slug/project/{index.html,starter.py,solution.py,README.md}
assessments/written-exams/module-N-exam.html (+ .md as raw/portable source)
quality-audits/chapter-0N-audit.md
```

- Chapter numbers are two-digit, zero-padded: `chapter-01`,
  `chapter-02`, ... `chapter-13`.
- Slugs are lowercase, hyphenated, no special characters.

## Content standards

- **No placeholder text** in anything merged to `main` — no `[insert
  X]`, no Lorem ipsum. CI blocks these. (Bare `TODO 1:`, `TODO 2:` etc.
  inside `exercises/starter.py` and `project/starter.py` are
  intentional learner tasks, not placeholders — CI does not flag
  those.)
- **No API keys or secrets** committed anywhere, ever. CI scans for
  common secret patterns.
- **Cross-chapter Python imports** must use
  `importlib.util.spec_from_file_location`, never a `sys.path.insert`
  + `import solution` trick — multiple files across chapters share the
  name `solution.py`, and the naive approach breaks depending on
  invocation method.
- **Every file with a top-level `asyncio.run(main())`** must guard it
  with `if __name__ == "__main__":` — a bare top-level call crashes if
  the file is ever imported from inside a running event loop.
- **Long-running or live-server-dependent solution.py files** need a
  `# CI: LONG_RUNNING_SERVER` or `# CI: NEEDS_LIVE_SERVER=<path>`
  marker comment (see `ci.yml`'s comments) so CI knows not to treat a
  non-zero exit as a failure.
- **Chapters that call the model via Ollama** must check for a running
  local Ollama server (e.g. a connection error to `localhost:11434`)
  and skip/degrade gracefully with a clear message if it's absent,
  rather than crashing — CI runners don't have Ollama running or a
  model pulled, so this path is exercised on every CI run.
- **Written exams render as styled HTML**, not raw `.md` (the `.md`
  stays as a portable raw source) — use
  `templates/written-exam.template.html`.
- **Every chapter needs**: a hook grounded in a real problem, tested
  code (not illustrative pseudocode), a production scenario, common
  mistakes, a builder thought-process box, 6+ exercises (3+
  production-gear), 6+ practice scenarios, 8+ interview questions
  across all 4 levels, and a project — per
  `quality-audits/chapter-audit.template.md`.
