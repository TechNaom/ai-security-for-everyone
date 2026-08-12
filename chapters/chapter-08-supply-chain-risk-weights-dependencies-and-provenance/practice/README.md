# Chapter 8 Practice Bank: Supply-Chain Risk: Weights, Dependencies, and Provenance

Eight short, independent scenarios, each with its own fictional system —
none of them Solstice Diagnostics / TriageAssist (the lesson) or
Coppervale Underwriting / RiskPilot (the exercises). The first five drill
fast, accurate classification of risk categories and defenses; the last
three test real judgment: whether a claim is honestly limit-aware,
whether a conclusion has a real defense/category mismatch, and how to
prioritize a fix under launch time pressure.

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

## The eight scenarios

1. **Windmere Logistics** — checking a new model's checksum against an
   independently recorded manifest value before production: provenance
   verification.
2. **Bellhaven Retail** — fine-tuning on top of an unvetted, community-
   published adapter chosen purely for benchmark score: compromised/
   backdoored weights.
3. **Farrow Veterinary Systems** — default pickle-based checkpoint
   loading, capable of executing arbitrary code from a tampered file:
   a vulnerable dependency in the ML toolchain.
4. **Oakstead Municipal** — connecting to a new MCP tool from an
   unvetted vendor: excessive trust in a third-party plugin/tool.
5. **Cardinal Peak Freight** — declaring "fully protected from any
   future supply-chain compromise" after pinning dependencies: not
   honest — pinning doesn't protect against a compromise of an
   already-trusted, already-pinned package's own build pipeline.
6. **(Judgment) Thistle & Vale Law** — claiming Safetensors adoption
   makes them "fully protected against a backdoored model": an unsound
   conclusion — safe loading removes code-execution-on-load risk, not
   the model's own learned, trigger-conditioned behavior.
7. **(Judgment) Brackenfield Analytics** — under time pressure, standing
   up an internal approval process is the higher-impact fix; with zero
   review of any kind, nothing else in this chapter's defenses ever gets
   applied consistently, which is a more fundamental gap than one
   specific file-format risk.
8. **(Production-gear) Ashgrove Biotech** — a SLSA-style signed-
   attestation framework verifying exactly how a model was built and
   from what source data: provenance verification, aimed primarily at
   compromised/backdoored weights.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9.

Scenario 6 is this bank's concrete version of the lesson's central
honest-limits point on Defense 2: safe model-loading practices are real,
useful, and remove a real class of risk, but neither format conversion
nor sandboxed loading says anything at all about whether the model's
actual learned weights contain a planted trigger — claiming a single
format change makes an entire risk category "fully protected against" is
exactly the overclaim this chapter's own defense sections warn against.
