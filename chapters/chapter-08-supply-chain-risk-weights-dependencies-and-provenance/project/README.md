# Chapter 8 Project: A Provenance and Integrity Checker

A real, self-contained supply-chain defense tool: a checker that vets a
synthetic manifest of Solstice Diagnostics artifacts (the lesson's own
scenario) against checksum, safe-serialization-format, publisher-vetting,
and scan-result signals, combining them into one structured vetting
report. This is Defenses 1&ndash;3 ("provenance verification," "safe
model-loading practices," and "dependency scanning") actually
implemented, including the honest limit the lesson's own defense
sections name in prose.

## The scenario

**Solstice Diagnostics' TriageAssist**, continuing the lesson's own
example. This project builds the tool Solstice's security review should
have run *before* any of its three under-deadline decisions — the
unverified community adapter, the pickle-based loading path, the
unaudited third-party tool — ever reached production. The full synthetic
six-artifact manifest and as-found artifact set are already written for
you in `starter.py` — read it in full before you start.

## What "done" looks like

Fill in the four parts of `starter.py`:

1. **`checksum_matches()`** — confirm an artifact's as-found checksum
   matches the value independently recorded in the manifest at approval
   time.
2. **`format_is_safe()`** — confirm an artifact's serialization format is
   on the safe list, not a pickle-based format capable of arbitrary code
   execution on load.
3. **`publisher_is_vetted()`** — confirm an artifact's publisher is on
   the organization's vetted-source list.
4. **`vet_artifact()`** — combine the three checks above, plus a provided
   scan-clean flag, into one finding list and a BLOCK/APPROVE verdict.

Then run:

```bash
python3 starter.py
```

## No live model dependency at all

Like Chapters 6 and 7's projects, this one never imports `openai`, never
calls Ollama, and has no graceful-degradation branch to test, because
there's no live-model call anywhere in this file to degrade. Every
function is pure, deterministic Python operating on fabricated,
clearly-labeled synthetic artifact records. This matches this chapter's
own subject: provenance and integrity checking is an adoption-time,
offline practice, not a runtime model interaction.

## An honest note on live verification

This chapter's content — like Chapters 6 and 7's — never depends on a
live model call, so there is no live-vs-logical-only gap to disclose for
this project's own code. For consistency with this course's established
discipline, this session still checked Ollama's status directly before
writing any chapter content:

- `ollama list` — responded normally, confirming `llama3.2:latest` is
  pulled.
- `curl -s -m 3 http://localhost:11434/api/tags` — responded normally
  and immediately.

Both checks succeeded this session, but neither is relevant to this
project's actual correctness claims — every number and verdict in this
project's report (the per-artifact findings, the BLOCK/APPROVE verdicts,
the summary counts) comes from deterministic code run directly against
fabricated data, and was actually executed this session. See
`quality-audits/chapter-08-audit.md` for the complete breakdown.

## What the finished report shows

Three report sections:

- **Step A** — the checker's own logic self-test against small,
  synthetic cases (9 checks), independent of the full six-artifact set.
- **Step B** — all six synthetic artifacts vetted and reported:
  `base_model_v3` (fully clean) and `quiet_backdoor_candidate` (passes
  every mechanical check) both land at `APPROVE` with no findings;
  `triage_adapter_v1` is `BLOCK`ed for `CHECKSUM_MISMATCH`;
  `embedding_model_v2` for `UNSAFE_SERIALIZATION_FORMAT`;
  `framework_lib_core` for `UNVETTED_PUBLISHER`; `drug_interaction_client`
  for `SCAN_FLAGGED`.
- **Step C** — the honest hard case: `quiet_backdoor_candidate` passes
  every single check this tool can perform and is `APPROVE`d, with an
  explicit statement of exactly what that verdict does and doesn't
  prove.

## Checking your work

Once you're satisfied with your own pass, compare it against
`solution.py` — a complete, worked reference. Both files' `verify_logic()`
scores 9/9 when correctly filled in.

```bash
python3 solution.py
```

Pay particular attention to Step C once your own implementation is
working: confirm for yourself that `quiet_backdoor_candidate` really
does clear every check and land at `APPROVE` with zero findings. That's
not a bug in the checker — it's the honest, observable proof of this
chapter's central limit on Defenses 1&ndash;3: a checksum match, a safe
format, a vetted publisher, and a clean scan are all real, necessary
signals, and none of them, together or alone, can tell you whether an
artifact's actual learned weights contain a well-disguised backdoor. This
report is a real, useful gate, not a verdict on the deeper question — a
team still needs the organizational judgment layer (this chapter's
Defense 4, and Chapter 6's behavior-auditing defense) for exactly the
artifacts that clear every mechanical check this tool can run.
