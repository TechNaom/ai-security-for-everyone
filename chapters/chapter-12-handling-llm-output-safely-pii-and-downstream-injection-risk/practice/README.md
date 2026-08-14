# Chapter 12 Practice Bank: Handling LLM Output Safely: PII and Downstream Injection Risk

Eight short, independent scenarios, each with its own fictional
organization — none of them Fenwick Customer Experience (the lesson) or
Thornbury HR Cloud (the exercises). The first six drill fast, accurate
classification of which of this chapter's six failure shapes a given
event belongs to; the last two test real judgment about what actually
makes an output-handling defense sufficient.

## The eight scenarios

1. **Halvern Legal Services** — a confidential settlement figure
   reaching a wider-audience billing dashboard. Which failure shape?
2. **Cressida Travel** — a different traveler's itinerary detail
   bleeding into an unrelated reply. Which failure shape?
3. **Oakmere Insurance** — an unprompted bank routing number in a reply
   to a narrow question. Which failure shape?
4. **Bramwell Logistics** — an unescaped, script-bearing shipment note
   rendered as raw HTML. Which failure shape?
5. **Sable Ridge Media** — one model's generated output feeding
   unlabeled into a second model's instruction context. Which failure
   shape?
6. **Pinehollow Retail** — an auto-fetched generated link pointing at an
   internal admin endpoint. Which failure shape?
7. **Yarrow Health Clinics · Judgment** — is a system-prompt instruction
   alone, with no output-side scanner or scoping, a sufficient PII
   defense?
8. **Corrigan Analytics · Judgment, production-gear** — a PII scanner and
   HTML escaping are already in place, but no allow-list check exists,
   and an auto-fetch feature ships next week. Which single next step has
   the highest expected impact?

## Why this bank leans on judgment, not recall

Deciding whether an output-handling defense is actually sufficient is a
judgment skill, not a lookup — a system with some real controls in place
can still have one specific, actively exploitable gap, and there's no
single keyword to pattern-match against for scenarios 7-8. You have to
reason about which control is missing and what its absence actually
costs given what's shipping next.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 8/8.
