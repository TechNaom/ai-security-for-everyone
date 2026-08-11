# Chapter 2 Exercises: Mapping the Attack Surface of a Real LLM Feature

These exercises use a second scenario, deliberately different from the
lesson's Waypoint trip-planning assistant: **ReviewMate**, a fictional
internal code-review assistant that reads pull requests, issues, and CI
logs, and can post comments and merge PRs, with four tools
(`read_pr_diff`, `read_linked_issue`, `get_ci_logs`, `post_comment`,
`merge_pr`). Applying the systematic method to a fresh scenario is the
point — recalling the lesson's answers by heart won't get you through
these.

## How to run

You'll need Python 3 installed. Check with:

```bash
python3 --version
```

Then run the starter file:

```bash
python3 starter.py
```

It prints a score report. Fill in each `# TODO`, re-run, and watch your
score climb toward the total.

## The eight tasks

1. **Map assets to OWASP categories** — assign the correct OWASP Top 10
   category ID to five ReviewMate attack-surface descriptions.
2. **Trust classification** — decide which context-window inputs are
   trusted (operator-authored) versus untrusted (attacker-influenceable).
3. **(Production-gear) Evaluate Excessive Agency fixes** — given four
   candidate fixes for the `merge_pr` tool, decide which ones actually
   reduce Excessive Agency risk versus which are unrelated
   reliability/UX changes.
4. **Likelihood/impact reasoning** — write a real, justified sentence
   (not "high" or "low" alone) for one asset's risk.
5. **(Production-gear) Output handling** — name the category and a
   concrete mitigation for ReviewMate's comments rendering as markdown
   with auto-loading images/links.
6. **(Production-gear) Unbounded consumption** — name the category and a
   concrete mitigation for uncapped, ReviewMate-triggered CI reruns.
7. **(Production-gear) System prompt leakage compliance check** — decide
   whether embedding the exact auto-merge safety criteria in the system
   prompt is a real problem, and name the fix.
8. **(Production-gear) Full-framework completeness check** — confirm all
   10 OWASP categories were at least considered while working through
   this chapter's exercises, the same completeness gate a real team runs
   before a threat model ships.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 31/31 when run.
Your own wording for the open-ended tasks (Exercises 4, 5, 6, 7) doesn't
need to match the reference text exactly — the checker looks for the
right category IDs and enough substance in your written justification,
not an exact string match.

Two rows in Exercise 1 (`pr_description_text` and `ci_log_output`) are
both mapped to LLM01 — this is deliberate. It's the exercises' version of
this chapter's Mistake 1 (under-scoping): the PR description is the
"obvious" untrusted field, and CI log output containing a dependency's
own console text is the one a first pass is likely to miss entirely.
