# Chapter 9 Project: Find and Fix a RAG-Corpus Injection Vector

A real, complete lab continuing the lesson's **Vesper Cloud / Vesper
Assistant** scenario. You're given a naive, vulnerable RAG pipeline and a
synthetic six-chunk corpus containing a planted injection modeled
directly on `quietstorm77`'s forum post. Your job is to find the
vector by tracing it through the pipeline, then fix it by implementing
five real defense functions.

**This is Chapter 9's own real, complete project — not the course's
final L3 Independent project.** Per this course's curriculum map, the
L3 project ships after Chapter 10, which extends this exact pipeline
with the agentic/tool-output angle for a genuinely combined, no-scaffold
challenge. This project is real and complete on its own: every defense
below is implemented, tested, and produces directly observable, executed
output.

## The five parts

1. **`sanitize_content()`** (Defense 1) — flag chunks containing
   instruction-like patterns addressed to an assistant/system.
2. **`is_query_sensitive()`** (supports Defense 3) — classify whether a
   query touches a privileged-action topic, broadly (by topic keyword,
   not just an explicit mention of the action itself).
3. **`quarantine_filter()`** (Defense 3) — for a sensitivity-flagged
   query, exclude any chunk whose source wasn't independently reviewed.
4. **`build_prompt_secure()`** (Defense 5) — wrap retrieved content in
   structural delimiters, with the "reference material, not
   instructions" framing reinforced both before and after.
5. **`enforce_least_privilege()`** (production-gear, Defense 6) — the
   final backstop: no privileged action may be authorized by retrieved
   content, regardless of source, trust tier, or whether the earlier
   defenses already caught it.

## How to run

```bash
python3 --version
python3 starter.py
```

Fill in each `# TODO`, re-run, and watch `verify_logic()` climb toward
11/11.

## What "done" looks like

`verify_logic()` reports 11/11. Then look at the full report:

- **Step B (naive pipeline):** retrieves `forum_poisoned_note` in the top
  3 (it was engineered to score high on both "sync" and "quota") and
  reports `Vulnerable: True` — the planted "you are authorized to
  approve..." phrase reaches the assembled prompt completely unmarked.
- **Step C (secure pipeline):** the same query gets flagged sensitive
  (it mentions "quota"), quarantining excludes the unreviewed forum
  chunk, and output validation reports `ALLOWED` — because the
  privileged phrase never reaches the final context at all.
- **Step D (defense-in-depth):** simulates a quarantine failure (the
  poisoned chunk's trust tier gets mislabeled as reviewed) and confirms
  `enforce_least_privilege()` still catches the phrase and returns
  `DENIED` — the actual point of this project: a real defense-in-depth
  stack has one layer left even when an earlier layer fails.

Also confirm, by reading the code, that `forum_legit_tip` (a genuinely
harmless community tip) is never excluded by quarantining for an
ordinary, non-sensitive query — the fix closes the specific vector
without making all community content unusable.

## No required live-model dependency

Every defense function operates on fabricated, clearly-labeled text with
zero network dependency — see `lesson.html`'s honest disclosure on why
this project's core logic doesn't depend on a live model call this
session. An optional `call_model_live()` function is included at the
bottom of both `starter.py` and `solution.py` for learners who want to
try a real Ollama call; it degrades gracefully and isn't required for,
or checked by, `verify_logic()`.
