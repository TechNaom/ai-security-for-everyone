# Chapter 13 Practice Bank: Capstone: Security Architecture for a Real LLM System

Eight short, independent scenarios, each with its own fictional
organization — none of them Cinderpeak Systems (the lesson) or Grantham
Municipal Services (the exercises). The first six drill fast, accurate
mapping of a described failure to the correct OWASP GenAI LLM Top 10
2026 category (across all ten, not just the two Chapter 12 used); the
last two test real architect-level judgment about ADR quality and
sandboxing trade-offs.

## The eight scenarios

1. **Fairmont Regional Airport Authority** — a public flight-status
   chatbot echoing a planted instruction from a passenger complaint
   field. Which OWASP 2026 category?
2. **Blackwood Actuarial Partners** — an actuarial-report generator
   restating a client's confidential loss-ratio figure in a
   firm-wide summary. Which category?
3. **Silvergate Credit Union** — a loan-assistant plugin, installed
   from an unvetted marketplace, later found bundling a data-
   exfiltration routine. Which category?
4. **Northaven Utilities Cooperative** — a fine-tuned outage-triage
   model that learned a backdoor trigger phrase from unreviewed
   historical tickets. Which category?
5. **Castlebridge Legal Tech** — a contract-review assistant granted
   standing authority to auto-file signed documents with no human
   checkpoint. Which category?
6. **Emberline Health Analytics** — a generated clinical-summary
   widget rendering raw, unescaped patient notes in a physician
   portal. Which category?
7. **Duskwater Insurance Group · Judgment** — is an ADR that names a
   decision and a rejected alternative, but states no real trade-off,
   a sound ADR?
8. **Fallowfield Robotics · Judgment, production-gear** — a first-party,
   already-schema-validated internal tool is proposed for full
   container sandboxing "to be extra safe." Is that the right call?

## Why this bank leans on judgment, not recall

Deciding whether an ADR is actually sound, or whether a sandboxing
proposal fits the threat model it's supposed to close, is a judgment
skill this course built specifically for its architect-level capstone —
there's no single keyword to pattern-match against for scenarios 7-8.
You have to reason about what's missing and what a given control
actually costs against what it actually buys.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 8/8.
