# Chapter 9 Practice Bank: Securing RAG Pipelines Against Injection

Eight short, independent scenarios, each with its own fictional system —
none of them Vesper Cloud / Vesper Assistant (the lesson) or Thornbury
Legal Research / CaseLens (the exercises). The first five drill fast,
accurate classification of pipeline stages and defenses; the last three
test real judgment: whether a claim is honestly limit-aware, and how to
prioritize a fix under launch time pressure.

## The eight scenarios

1. **Larkhollow Media** — a streaming platform's nightly job adds every
   new user review directly to its recommendation assistant's index,
   with no review step and no distinction from editorially-written show
   summaries. Which pipeline stage?
2. **Fennimore University** — an academic-advising bot's query about a
   "prerequisite override" retrieves a forum post from an anonymous
   student account purely because of keyword overlap, with no concept of
   who posted it. Which pipeline stage?
3. **Briarstone Bank** — a support bot's prompt-assembly code
   concatenates retrieved KB articles and forum posts directly into the
   prompt text with no delimiters. Which pipeline stage?
4. **Copperfield Realty** — a real-estate assistant recommends waiving a
   standard buyer-verification step based solely on wording found in a
   retrieved, unreviewed agent note. Which single defense would have
   stopped this most directly?
5. **Slate Peak Outdoors** — every chunk in a retail support bot's index
   is tagged at ingestion with its source and review status, queryable by
   every later stage. Which single defense is this?
6. **Ivywood Pharmacy Network · Judgment** — engineering claims content
   sanitization at ingestion means "no injected instruction can ever
   reach our model." Sound?
7. **Wrenfield Aviation · Judgment** — namespace-isolated indexes lead the
   team to conclude "any content retrieved from either one is fully
   vetted." Sound?
8. **Hollowbrook Nonprofit · Judgment, production-gear** — three weeks
   from launch, with zero query-sensitivity classification AND raw,
   untagged prompt concatenation, plus one already-accepted residual-risk
   gap. Which single fix has the higher expected impact, and which gap is
   the one being explicitly accepted for now?

## Why this bank leans on judgment, not recall

Deciding whether a RAG-defense claim is well-supported is a judgment
skill, not a lookup — a control that's technically in place (isolated
namespaces, an ingestion scanner) can still support a wrong or incomplete
conclusion if it doesn't account for what that specific control actually
rules out. Scenarios 6-8 are built so there's no single keyword to
pattern-match against; you have to reason about what a given control
actually covers, and at which of the three pipeline stages it operates.

## How to run these

Download `starter.py`, fill in every `# TODO`, then run `python3
starter.py` to see an automated score report. Compare against
`solution.py`, which scores a perfect 9/9.
