# Chapter 2 Project (Level 1, Guided): Threat-Model a Real LLM Feature End to End

This is Module 1's real Level 1 (Guided) project, per
`docs/curriculum/CURRICULUM_MAP.md`. You're handed **AskHR**, a fourth
fictional LLM feature — genuinely different from GreenCart (Chapter 1),
Waypoint (this chapter's lesson), and ReviewMate (this chapter's
exercises) — and asked to threat-model it end to end, with no worked
answer to check against as you go.

## The scenario

AskHR is an internal HR chatbot deployed in a company-wide Slack
workspace. It has four tools (`search_hr_policies`,
`get_employee_record`, `initiate_leave_request`,
`escalate_to_hr_specialist`), a mixed internal/third-party policy
retrieval pipeline, and both one-on-one and shared-channel conversation
sessions. The full scenario, including exact tool behavior, is described
in the docstring at the top of `starter.py` — read it in full before you
start.

## What "done" looks like

Fill in the three parts of `starter.py`:

1. **Tool inventory** (Step 1 of the lesson's method) — every tool, its
   real side effect, and its blast radius.
2. **Context-source inventory + trust classification** (Steps 2–3) —
   every source of text that reaches AskHR's context window, who
   controls it, and whether it re-enters context on later turns
   (including tool outputs — this is the lesson's core teaching point).
3. **The full threat-model table** (Steps 4–7) — real findings, each
   with an OWASP category, a justified likelihood/impact sentence (not
   a bare "high"/"low"), and an architectural mitigation. Aim to
   explicitly consider all 10 OWASP categories (Step 6's completeness
   discipline), even where some end up "not applicable, because...".

Then run:

```bash
python3 starter.py
```

This project is **open-ended** — there is no single fixed answer key, so
the validator checks *structural* completeness (enough tools and
sources enumerated, trust classified, at least one tool-output re-entry
flagged, enough distinct categories covered with real justified
reasoning and a real mitigation), not your exact wording against a
hidden key. A clean structural pass means your artifact has the right
shape; it doesn't certify that every individual finding is the single
best one.

## Checking your work

Once you're satisfied with your own pass, compare it against
`solution.py` — a complete, worked reference threat model covering all
10 OWASP categories, built with the same seven-step method. Differences
in wording or which specific finding you attached to which row are
normal and fine; differences in which *assets* you found at all are
worth revisiting against the lesson's Section 4 method, especially
Step 5 (tool outputs re-entering context) and Step 6 (the full
ten-category walk), since those are the two steps this chapter's
Mistakes 1 and 2 are built around.

```bash
python3 solution.py
```
