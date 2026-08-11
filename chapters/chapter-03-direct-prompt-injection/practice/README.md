# Chapter 3 Practice Bank: Direct Prompt Injection

Eight short, independent scenarios, each with its own fictional system —
none of them Meridian Notes (the lesson) or HelixCare Intake (the
exercises). The first five drill fast, accurate classification across
all five technique families from the lesson's taxonomy; the last three
test judgment about defenses.

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

1. **LibraLend** — role-play/persona override.
2. **QuickTax** — instruction override.
3. **TravelDesk** — context/scope confusion (fake authority).
4. **CodeReviewBot** — payload obfuscation (leetspeak substitution
   defeating a literal-string filter).
5. **WellnessCoach** — multi-turn/gradual escalation.
6. **(Judgment) BankAssist** — does a defense posture with structural
   separation and filtering, but no bounded consequence on its transfer
   tool, still have a real gap?
7. **(Judgment) StudyBuddy** — prioritize between a tool-free
   role-play risk and an uncapped-refund-tool instruction-override risk.
8. **(Production-gear) ConciergeDesk** — a combined attack: name both
   the opening technique family and the single highest-leverage defense
   layer that contains the damage even if the injection succeeds.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9.

Scenario 6 is deliberately built to show that structural separation and
filtering, while both real and worthwhile, are not sufficient on their
own — BankAssist's uncapped `transfer_funds` tool means a successful
injection (even a rare one that gets past both existing layers) still
converts directly into a real financial loss. That's this chapter's
Defense 3 (bounded consequence) made concrete: the correct answer is
that a real gap remains.
