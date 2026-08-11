# Chapter 6 Project: A Corpus-Anomaly Scanner

A real, self-contained data-poisoning defense tool with two halves: a
lift-based statistical anomaly scanner over a synthetic 200-record
fine-tuning corpus (Defense 2, actually implemented), and a version-diffing
scanner over a synthetic before/after RAG-corpus snapshot (Defense 4,
actually implemented). The scenario continues the lesson's own example:
**Meridian Home Warranty**, its claims-triage model, and its RAG-indexed
internal policy wiki.

## The scenario

Meridian fine-tunes a claims-triage model on historical support tickets
and separately runs a RAG-indexed internal policy wiki. This project
builds the security team's own tooling: a scanner that would run *before*
any fine-tuning run over the ticket corpus, and a diff-checker that runs
on *every update* to the indexed policy wiki before re-indexing. The full
scenario, the synthetic 200-record `build_synthetic_ticket_corpus()`, and
the `BEFORE_CORPUS`/`AFTER_CORPUS` RAG snapshot are in `starter.py` — read
them in full before you start.

## What "done" looks like

Fill in the four parts of `starter.py`:

1. **`count_phrase_occurrences()`** — count how often each candidate
   phrase appears overall, and how often it appears alongside each
   outcome label.
2. **`compute_lift()`** — compute how much more likely a target label is
   when a phrase is present, versus that label's overall base rate.
3. **`flag_rare_phrase_label_correlation()`** — combine Parts 1 and 2 into
   a real scan: flag any phrase whose support and lift both clear a
   threshold.
4. **`diff_corpus_documents()`** — diff a before/after RAG corpus
   snapshot and flag documents with a large change or a new
   policy-loosening keyword.

Then run:

```bash
python3 starter.py
```

## No live model dependency at all

Unlike Chapters 3–5's projects, this one never imports `openai`, never
calls Ollama, and has no graceful-degradation branch to test, because
there's no live-model call anywhere in this file to degrade. Every
function is pure, deterministic Python operating on fabricated,
clearly-labeled synthetic data. This matches this chapter's own subject:
data-poisoning defenses are data-pipeline practices, not runtime model
interactions.

## An honest note on live verification

This chapter's content — unlike Chapters 3–5 — never depends on a live
model call, so there is no live-vs-logical-only gap to disclose for this
project's own code. For consistency with this course's established
discipline, this session still checked Ollama's status directly before
writing any chapter content:

- `ollama list` — responded normally, confirming `llama3.2:latest` (2.0 GB)
  is pulled.
- `curl -s -m 3 http://localhost:11434/api/tags` — responded normally and
  immediately.

Both checks succeeded this session, but neither is relevant to this
project's actual correctness claims — every number in this project's
report (the lift scores, the support counts, the diff-flagging decisions)
comes from deterministic code run directly against fabricated data, and
was actually executed this session. See
`quality-audits/chapter-06-audit.md` for the complete breakdown.

## What the finished report shows

Three report sections:

- **Step A** — the scanner's own logic self-test against small, synthetic
  cases (7 checks), independent of the full 200-record corpus.
- **Step B** — the full corpus scanned twice: a high-support threshold
  (`min_support=10`) catches the 40-record bias cluster but misses the
  6-record backdoor entirely (support 6 < the 10-occurrence floor); a
  low-support threshold (`min_support=3`) catches the backdoor — but also
  flags five coincidental "noise" phrases that were never planted by
  anyone, yet score statistically identical to the real backdoor (same
  lift, overlapping support range). The report can't tell you, from the
  numbers alone, which flagged phrase is the real attack.
- **Step C** — the before/after RAG corpus diff: the policy-loosening
  edit to `policy_extended_coverage` gets flagged (new loosening
  keywords), the cosmetic wording clarification to `policy_return_window`
  does not, and the unchanged `policy_general_faq` is correctly reported
  as unchanged.

## Checking your work

Once you're satisfied with your own pass, compare it against
`solution.py` — a complete, worked reference. Both files' `verify_logic()`
scores 7/7 when correctly filled in.

```bash
python3 solution.py
```

Pay particular attention to the low-support scan in Step B once your own
implementation is working: confirm for yourself that the five
"seasonal-promo-code" noise phrases and the real
`extended-coverage rider EC-featherlight` backdoor phrase really do land
at the same lift value (about 3.08x) and an overlapping support range
(3–7 occurrences). That's not a bug in the scanner — it's the honest,
observable proof of this chapter's central limit on anomaly detection: a
low-volume, well-blended backdoor is genuinely, statistically
indistinguishable from ordinary chance correlation using this technique
alone, which is exactly why the lesson pairs it with output/behavior
auditing rather than treating it as sufficient by itself.
