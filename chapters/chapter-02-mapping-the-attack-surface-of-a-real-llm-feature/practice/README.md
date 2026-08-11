# Chapter 2 Practice Bank: Mapping the Attack Surface of a Real LLM Feature

Eight short, independent scenarios, each with its own fictional system —
none of them Waypoint (the lesson) or ReviewMate (the exercises) again.
Each scenario is a few sentences and one judgment question. Several are
built specifically around this chapter's core lesson: a **tool's output**
re-entering context is just as real an injection channel as a
user-typed field, even when no user ever touched the malicious text.

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

1. **ClaimsBot** — a claims bot with a planted instruction in a
   user-typed claim description (the "obvious" injection case).
2. **MarketWatch** — a stock-research assistant where the injected
   instruction arrives through a *tool's* headline-fetching output, not
   any user-typed field at all — this chapter's core lesson, tested
   directly.
3. **DocSummarizer** — a contract summarizer whose output gets rendered
   as raw HTML.
4. **RecommendAI** — a model fine-tuned on unvetted, attacker-seeded
   training data (coordinated fake reviews).
5. **OpsChat** — an internal chatbot with no rate limit or output cap.
6. **(Judgment) VendorGate** — deciding whether a described plugin-vetting
   process already covers Supply Chain risk, or leaves a real gap.
7. **(Judgment) LegalAssist** — prioritizing between two real but
   unequal-impact issues when only one can be fixed before launch.
8. **(Production-gear) WarehouseBot** — a full two-category mapping where
   the planted instruction again arrives through a tool (a supplier's
   note), not a company-employee-typed field.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9 when run.
Scenarios 6 and 7 are genuine judgment calls, not keyword-matched free
text — there's a single correct answer, but reaching it requires
reasoning about the scenario, not recalling a category name. Scenarios 2
and 8 are deliberately similar in shape to each other (both are
tool-output injection) — if you get one right and the other wrong, go
back and reread this chapter's Mistake 1 before moving on.
