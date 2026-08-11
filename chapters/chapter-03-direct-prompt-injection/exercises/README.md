# Chapter 3 Exercises: Direct Prompt Injection

These exercises use a new scenario, deliberately different from the
lesson's Meridian Notes / Concierge example: **HelixCare Intake**, a
fictional telehealth pre-visit intake assistant with one tool that has a
real side effect, `schedule_appointment(patient_id, slot)`. You'll
classify five real injection attempts by technique family, predict how a
naive keyword filter behaves against each, and design real defenses —
not just recall the lesson's taxonomy names.

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

1. **Classify technique families** — match five HelixCare Intake
   injection attempts to the correct family from this chapter's
   taxonomy.
2. **Predict keyword-filter behavior** — for the same five attempts,
   predict whether a naive filter blocking "ignore"/"disregard"/"override"
   would actually catch each one.
3. **(Production-gear) Evaluate candidate defenses** — decide which of
   four candidate fixes actually reduce direct-injection risk versus
   which are unrelated UX changes.
4. **(Production-gear) Defense-in-depth reasoning** — write a real,
   justified sentence about why keyword filtering alone isn't enough.
5. **(Production-gear) Bounded-consequence rule design** — design one
   concrete, code-enforced rule for `schedule_appointment`.
6. **Provider guidance matching** — match two defense descriptions to
   the real provider (OpenAI or Anthropic) whose documented guidance
   this chapter cites.
7. **Multi-turn escalation detection** — decide whether a transcript
   demonstrates gradual escalation or is a benign exchange.
8. **(Production-gear) Defense-layer completeness gate** — confirm all
   four of this chapter's defense layers were at least considered.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_exercise_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 24/24. Your own
wording for the open-ended tasks (Exercises 4 and 5) doesn't need to
match the reference text exactly — the checker looks for the right
substance (a named weakness, a named addition, a concrete code-enforced
rule), not an exact string match.

Exercise 2 is the exercises' concrete version of this chapter's Payload
Obfuscation lesson: three of the five attempts (the role-play, the
base64-encoded, and the multi-turn attempts) slip straight past the
naive filter, while only the two that use an explicit override/authority
word get caught — the same gap a real keyword blocklist has in
production.
