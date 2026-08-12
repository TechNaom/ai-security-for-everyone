# Chapter 11 Practice Bank: Red-Teaming an LLM System: Methodology and Practice

Eight short, independent scenarios, each with its own fictional
system — none of them Alderglen Financial (the lesson) or Corvette Bay
Utilities (the exercises). The first five drill fast, accurate
classification of which of the five red-teaming phases a given event
belongs to; the last three test real judgment about what actually makes
a red-team engagement and its report valid and usable.

## The eight scenarios

1. **Driftwood Analytics** — signing a written scope document before
   testing begins. Which phase?
2. **Larkspur Media** — working through all ten OWASP categories against
   a real architecture before selecting techniques. Which phase?
3. **Nettlebrook Retail** — recording exact prompts, outputs, and
   timestamps immediately after each test. Which phase?
4. **Cobalt Harbor Shipping** — scoring a finding on likelihood and
   impact axes and combining them via a written rubric. Which phase?
5. **Wrenfield Dental Group** — delivering a structured document with an
   executive summary, scope, per-finding detail, and a prioritized
   remediation list. Which phase?
6. **Ridgemont University · Judgment** — does zero findings in an
   unscoped two-hour engagement prove the system is secure?
7. **Quillfire Robotics · Judgment** — is a comprehensive but unranked
   list of twelve findings just as actionable as a ranked one?
8. **Ashcombe Media Group · Judgment, production-gear** — three days
   before a board presentation, six findings have full reproduction
   steps but no severity ratings and no executive summary. Which single
   next step has the highest expected impact?

## Why this bank leans on judgment, not recall

Deciding whether a red-team engagement or its report is actually sound
is a judgment skill, not a lookup — a real, well-documented engagement
can still fail to produce organizational action if it skips one of the
five phases, and there's no single keyword to pattern-match against for
scenarios 6-8. You have to reason about which phase is missing and what
its absence actually costs.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 8/8.
