# Chapter 7 Project: A Query-Pattern Anomaly Scorer

A real, self-contained model-extraction defense tool: a scorer that
analyzes a synthetic 90-day log of API queries against ClauseFinder
(Halcyon Research's scenario from the lesson) and combines three
independent signals — volume vs. an account's own historical baseline,
clause-category coverage breadth, and input diversity — into one
composite risk score. This is Defense 1 ("rate limiting and query-pattern
anomaly detection"), actually implemented, including the honest limit its
own lesson section names in prose.

## The scenario

**Halcyon Research's ClauseFinder**, continuing the lesson's own example.
This project builds the piece of Defense 1 the lesson's lab section only
sketched the structure of: the actual scoring logic Halcyon's security
team would run over its own API access logs to triage which accounts
deserve a closer look. The full synthetic five-account, 90-day query log
is already written for you in `starter.py` — read it in full before you
start.

## What "done" looks like

Fill in the four parts of `starter.py`:

1. **`score_volume_vs_baseline()`** — score how far an account's query
   rate over the observed window sits above *its own* historical daily
   baseline, not a fleet-wide average.
2. **`score_category_coverage_breadth()`** — score how much of
   ClauseFinder's full clause-category space an account's queries touch.
3. **`score_input_diversity()`** — score how little an account repeats
   the same input clause.
4. **`combine_signals()` and `classify_risk()`** — combine the three
   signals into one composite score, and turn that score (plus a
   minimum-sample-size floor) into a risk band.

Then run:

```bash
python3 starter.py
```

## No live model dependency at all

Like Chapter 6's project, this one never imports `openai`, never calls
Ollama, and has no graceful-degradation branch to test, because there's
no live-model call anywhere in this file to degrade. Every function is
pure, deterministic Python operating on fabricated, clearly-labeled
synthetic account query logs. This matches this chapter's own subject:
query-pattern anomaly detection is an API-log-analysis practice, not a
runtime model interaction.

## An honest note on live verification

This chapter's content — like Chapter 6's — never depends on a live model
call, so there is no live-vs-logical-only gap to disclose for this
project's own code. For consistency with this course's established
discipline, this session still checked Ollama's status directly before
writing any chapter content:

- `ollama list` — responded normally, confirming `llama3.2:latest` is
  pulled.
- `curl -s -m 3 http://localhost:11434/api/tags` — responded normally
  and immediately.

Both checks succeeded this session, but neither is relevant to this
project's actual correctness claims — every number in this project's
report (the volume/coverage/diversity/composite scores, the risk-band
assignments) comes from deterministic code run directly against
fabricated data, and was actually executed this session. See
`quality-audits/chapter-07-audit.md` for the complete breakdown.

## What the finished report shows

Three report sections:

- **Step A** — the scorer's own logic self-test against small, synthetic
  cases (9 checks), independent of the full five-account log.
- **Step B** — all five synthetic accounts scored and ranked by
  composite risk score: `quicklex_bulk_account` (an obvious, unmissable
  high-volume sweep) lands at the top with a composite of 100.0 and a
  `high` band; `patient_broad_account` (a patient, well-paced campaign
  spread across the full 90 days) lands at 82.3, also `high`;
  `corp_legal_dept_alpha` (a genuinely legitimate corporate legal
  department running one real 200-page contract through the API in a
  short sprint) lands at 72.2 — also `high`; the two genuinely normal
  accounts (`assoc_hendricks`, `smallfirm_op_paralegal`) land around
  15-16, both `normal`.
- **Step C** — a direct side-by-side of the obvious campaign, the
  patient/paced campaign, and the legitimate power user, showing the
  patient campaign and the legitimate power user land only about 10
  points apart on the composite score and can land in the *same* risk
  band.

## Checking your work

Once you're satisfied with your own pass, compare it against
`solution.py` — a complete, worked reference. Both files' `verify_logic()`
scores 9/9 when correctly filled in.

```bash
python3 solution.py
```

Pay particular attention to Step C once your own implementation is
working: confirm for yourself that `patient_broad_account` and
`corp_legal_dept_alpha` really do land close together on the composite
score, both in the `high` band, despite one being a competitor's
carefully-paced distillation campaign and the other being Halcyon's own
best customer having a busy month. That's not a bug in the scorer — it's
the honest, observable proof of this chapter's central limit on Defense
1: broad category coverage and high input diversity look statistically
similar whether they come from a real long-form contract sprint or a
deliberately-paced extraction campaign designed to resemble one. This
score is a real, useful triage signal, not a verdict — a team still needs
human judgment, and the chapter's other three defenses, for the accounts
that land in the `watch` or `high` band.
