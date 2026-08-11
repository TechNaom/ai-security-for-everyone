# Chapter 6 Practice Bank: Data Poisoning

Eight short, independent scenarios, each with its own fictional system —
none of them Meridian Home Warranty (the lesson) or Palisade Consumer
Electronics (the exercises). The first five drill fast, accurate
classification of poisoning categories and defenses; the last three test
judgment about honest claims, metric/category mismatches, and prioritizing
a fix under time pressure.

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

1. **GreenLeaf Nursery** — checking source authentication before use:
   provenance vetting.
2. **Solstice Bank** — 9 records out of 400,000 driving one narrow,
   triggered outcome: backdoor.
3. **Vantage Fleet Logistics** — a large, coordinated volume of subtly
   slanted contributions shifting overall behavior: availability/bias.
4. **Northfield University** — a standing wiki edit affecting every future
   retrieval on that topic: RAG corpus poisoning.
5. **Cinder Peak Outdoor Gear** — a clean held-out-test-set score presented
   as proof of no backdoor: not honest (the wrong evidence for the claim).
6. **(Judgment) Ashgrove Dental Network** — treating anomaly detection
   alone as "fully protected... including targeted backdoors": an unsound
   conclusion, since anomaly detection is honestly weakest against exactly
   the low-volume backdoors it claims to cover.
7. **(Judgment) Ferrous Metal Works** — under time pressure, closing a
   completely open, unvetted intake channel is the higher-impact fix; a
   missing behavior audit is a real gap, but an open door with zero
   provenance checking is the more fundamental exposure.
8. **(Production-gear) Skylark Freight Insurance** — versioned diffing
   with a review gate on RAG corpus updates is provenance tracking for RAG
   corpora, aimed primarily at catching RAG/retrieval corpus poisoning.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9.

Scenario 6 is this bank's concrete version of the lesson's central
honest-limits point: anomaly detection is real and useful, but it's
specifically weak against a low-volume, deliberately-blended backdoor —
claiming it provides full protection "including targeted backdoors" is
exactly the overclaim this chapter's Defense 2 section names directly.
