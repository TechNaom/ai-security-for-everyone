# Chapter 1 Exercises: Threat Modeling LLM Systems (The OWASP Top 10 for LLM Applications)

These exercises use a second scenario, deliberately different from the
lesson's GreenCart/Aurora hook: **PolicyPilot**, a fictional internal HR
chatbot that answers policy questions and handles routine PTO requests
over Slack, with three tools (`lookup_employee`, `search_policy_docs`,
`update_pto_balance`). Applying the framework to a fresh scenario is the
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
   category ID to five PolicyPilot attack-surface descriptions.
2. **Trust classification** — decide which context-window inputs are
   trusted (operator-authored) versus untrusted (attacker-influenceable).
3. **(Production-gear) Evaluate Excessive Agency fixes** — given four
   candidate fixes for the PTO tool, decide which ones actually reduce
   Excessive Agency risk versus which are unrelated reliability/UX
   changes.
4. **Likelihood/impact reasoning** — write a real, justified sentence
   (not "high" or "low" alone) for one asset's risk.
5. **(Production-gear) Output handling** — name the category and a
   concrete mitigation for PolicyPilot rendering generated text directly
   into Slack markdown with no escaping.
6. **(Production-gear) Unbounded consumption** — name the category and a
   concrete mitigation for PolicyPilot having no rate limit or output cap.
7. **(Production-gear) System prompt leakage compliance check** — decide
   whether embedding a real approval threshold in the system prompt is a
   real problem, and name the fix.
8. **(Production-gear) Full-framework completeness check** — confirm all
   10 OWASP categories were at least considered while working through
   this chapter's exercises, the same completeness gate a real team runs
   before a threat model ships.

## Checking your work

Unlike Chapter 1 of `python-for-everyone`, this exercise set **does**
include an automated grader — `score_exercise_*()` functions built into
both `starter.py` and `solution.py`. Run either file directly to see a
score report. `solution.py` is the fully filled-in reference and scores a
perfect 31/31 when run. Your own wording for the open-ended tasks
(Exercises 4, 5, 6, 7) doesn't need to match the reference text exactly —
the checker looks for the right category IDs and enough substance in your
written justification, not an exact string match.
