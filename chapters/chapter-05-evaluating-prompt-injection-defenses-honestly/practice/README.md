# Chapter 5 Practice Bank: Evaluating Prompt-Injection Defenses Honestly

Eight short, independent scenarios, each with its own fictional system —
none of them Harborview Claims (the lesson) or Fernbridge Freight (the
exercises). The first five drill fast, accurate classification of defenses
by category and evaluation practice by honesty; the last three test
judgment about adversarial iteration, metric/category mismatches, and
mapping a defense to its full evaluation profile.

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

1. **BrightPath Tutoring** — content-tagging of retrieved chunks: structural.
2. **Lockstep HR** — a hard, code-enforced ownership check and cap:
   consequence-bounding.
3. **TidalWave Marketing** — a clean corpus result shipped with no attacker
   model, no adversarial round, and no staleness caveat: not honest.
4. **Cornerstone Legal** — (judgment) rephrasing blocked entries specifically
   to defeat the defense that blocked them, then re-measuring: this *is*
   genuine Step 4 adversarial iteration.
5. **Havenlight Pharmacy** — output screening with human review: detection.
6. **(Judgment) Ironclad Insurance** — applying the structural "does the
   tell still fire" metric to a consequence-bounding defense and concluding
   it did nothing: an unsound, metric/category-mismatched conclusion.
7. **(Judgment) SwiftCart Retail** — under time pressure, an unbounded
   consequential tool is the higher-impact fix; a structural defense's
   adversarial-iteration gap is a real gap, but it doesn't leave a live
   system with zero protection the way an uncapped, unchecked tool call
   does.
8. **(Production-gear) NorthGate Utilities** — restating rules right before
   generation to counter the recency effect is sandwich/reinforcement
   prompting: structural, measured by "does the tell still fire."

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9.

Scenario 6 is this bank's concrete version of the lesson's Category 3
mistake: a bounded-consequence defense is never trying to stop the
injection's *text* from succeeding — it's trying to make a successful
injection harmless. Measuring it with Category 1's metric and concluding
"no benefit" is exactly the wrong-metric-for-the-right-defense mistake the
lesson names as the single most important distinction in this chapter.
