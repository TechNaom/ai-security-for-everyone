# Chapter 10 Exercises: Securing Agentic Systems Against Adversarial Tool Output

These exercises use a new scenario, deliberately different from the
lesson's Ferngate Logistics example: **Talbridge Health Network**, a
fictional regional healthcare provider whose Rounds Assistant helps
clinic schedulers manage patient appointments through two tools —
`check_lab_status(patient_id)` (read-only) and
`reschedule_priority_slot(patient_id, slot_id)` (side-effecting). You'll
classify scenarios by round-trip moment, compute a real permission-scope
risk score, judge honest claims versus overclaims, match defenses to
scenarios, match moments to their defense, critique flawed reports, and
match real research findings to their actual published source.

## Exercise standard

Eight tasks total. Five are marked production-gear — real permission-
risk-score computation, defense/scenario matching, critiquing flawed
reports, research citation matching, and written reasoning — not just
concept recall.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 27/27.

## The eight tasks

1. **Classify six scenarios by round-trip moment** — result arrival,
   context assembly, or action proposal.
2. **Production-gear.** Compute a real permission-scope risk score from
   four raw signals (credential scope match, whether a result can expand
   authority, whether the call is side-effecting, whether a human gate
   exists).
3. **Honest claim vs. overclaim** — four described defense claims.
4. **Production-gear.** Match defense to scenario — four scenarios, name
   the single best-fit defense from this chapter's six.
5. **Match moment to its defense** — map two of the three round-trip
   moments to the defense operating there most directly.
6. **Production-gear.** Critique four flawed-vs-sound report excerpts.
7. **Production-gear.** Research citation matching — OWASP's LLM06:2025,
   the OWASP GenAI Security Project's Top 10 for Agentic Applications,
   InjecAgent, or AgentDojo.
8. **Production-gear.** Written reasoning — why field-level provenance
   tagging alone doesn't stop anything.
