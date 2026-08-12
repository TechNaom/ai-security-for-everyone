# Chapter 10 Practice Bank: Securing Agentic Systems Against Adversarial Tool Output

Eight short, independent scenarios, each with its own fictional system —
none of them Ferngate Logistics (the lesson) or Talbridge Health Network
(the exercises). The first five drill fast, accurate classification of
round-trip moments and defenses; the last three test real judgment:
whether a claim is honestly limit-aware, and how to prioritize a fix
under launch time pressure.

## The eight scenarios

1. **Pemberton Insurance Group** — a claims-lookup tool returns a JSON
   response mixing a structured, system-set status enum with a free-text
   field an external contracted adjuster submitted, containing a planted
   instruction, with nothing distinguishing the two by the time the
   response reaches the model. Which round-trip moment?
2. **Kestrel Robotics** — a fleet-dispatch agent's tool-call result is
   correctly placed inside a proper tool-role message, but nothing in
   the message content reinforces that the field is data, not an
   instruction. Which round-trip moment?
3. **Fairhaven School District** — an agent proposes waiving a required
   parent-notification step, unprompted, based solely on wording found
   in a tool's returned free-text field. Which round-trip moment?
4. **Journeywell Travel** — the credential behind a read-only
   cancel-status-lookup tool can also authorize a card charge, even
   though the tool itself only exposes a status check. Which single
   defense would have stopped this most directly?
5. **Brightloom Retail** — every field in a retail-support agent's tool
   responses is tagged at result-arrival time with whether it's
   system-generated or vendor-submitted. Which single defense is this?
6. **Oakstead Manufacturing · Judgment** — engineering claims schema
   validation alone means "no malicious content can ever reach our model
   through a tool call." Sound?
7. **Silverline Broadcasting · Judgment** — narrowly scoped tool
   credentials lead the team to conclude "a manipulated tool result can
   never cause real harm." Sound?
8. **Cascade Ridge Outfitters · Judgment, production-gear** — three
   weeks from launch, with zero content sanitization AND zero
   structural framing on tool results, plus one already-accepted
   residual-risk gap. Which single fix has the higher expected impact,
   and which gap is the one being explicitly accepted for now?

## Why this bank leans on judgment, not recall

Deciding whether an agentic-defense claim is well-supported is a
judgment skill, not a lookup — a control that's technically in place
(scoped credentials, a schema validator) can still support a wrong or
incomplete conclusion if it doesn't account for what that specific
control actually rules out. Scenarios 6–8 are built so there's no single
keyword to pattern-match against; you have to reason about what a given
control actually covers, and at which of the three round-trip moments it
operates.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 9/9.
