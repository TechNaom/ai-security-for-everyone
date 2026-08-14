# Chapter 13 Project: The L4 Architecture Challenge — Aegis Copilot Pre-GA Security Review

This is the course's fourth and final project tier, per
`CURRICULUM_MAP.md`'s Projects section: **"Design a security
architecture for a realistic LLM system, with a red-team report and
full ADRs; business problem only."** Unlike Chapters 9-12's find-and-fix
labs or Chapter 11's findings report against a provided vulnerable
target, there is no vulnerable pipeline shipped here to fix — you are
given a business problem and asked to design, justify, and defend a
security architecture from it.

## The business problem, the way a real internal request would read

> Cinderpeak Systems' Aegis Copilot — a multi-tenant AI workflow
> assistant — has run a nine-tenant beta for four months with no major
> incident. General availability is eight weeks out. Before opening
> registration to any company, design the security architecture Aegis
> Copilot should have had from day one. Produce: (1) a threat model
> covering all ten OWASP GenAI LLM Top 10 2026 categories against the
> system description below, honestly rating this team's actual
> confidence per category; (2) six Architecture Decision Records for
> the specific design points this review has already identified as
> needing one, each stating a real trade-off using the correct one of
> Chapter 5's three defense categories; (3) a red-team pass against your
> own finished design, using Chapter 11's methodology, with real
> findings — not zero; (4) a launch recommendation that separates
> must-fix, accepted-and-monitored, and needs-follow-up-review items.
> No specific vulnerability has been reported. Nothing here is a bug to
> find — it's a system to design well.

## The system

`starter.py`'s `SYSTEM_DESCRIPTION` encodes, as structured data, exactly
the Aegis Copilot architecture described in full in `lesson.html`'s
"The System" section: per-tenant workspaces, RAG ingestion, first-party
tools, a third-party plugin marketplace, per-tenant fine-tuning, and
three output surfaces (an internal HTML dashboard, a customer-facing
Markdown chat widget, and a cross-tenant weekly analytics digest email).

## What you actually do

1. Run `python3 starter.py` as-is first — it prints the business
   problem, the system description, and an empty deliverable scaffold
   (the threat model, ADR set, and red-team pass are not filled in
   yet), plus a score report showing how incomplete an empty submission
   is.
2. Fill in `THREAT_MODEL` — one entry per OWASP 2026 category (all ten
   keys in `OWASP_2026_CATEGORIES`), each with `applicable` (bool),
   `component` (which part of Aegis Copilot it concerns), and a real
   `rationale` string. For any category you can't confidently rate with
   real course-backed depth, say so honestly in the rationale (see
   `lesson.html`'s own worked example for LLM06 and LLM07) rather than
   writing a placeholder.
3. Fill in `ADRS` — one entry per topic named in `REQUIRED_ADR_TOPICS`
   (six total). Each ADR needs `title`, `context`, `decision`,
   `defense_category` (`"structural"`, `"detection"`, or
   `"consequence_bounding"`), `alternatives_considered` (a non-empty
   list), and `trade_offs` (a real, non-placeholder cost).
4. Fill in `RED_TEAM_FINDINGS` — at least one real, specific finding
   describing a residual gap your own ADRs leave open, each with a
   `severity` (`"blocking"`, `"accepted_risk"`, or
   `"needs_follow_up"`) and a `description`.
5. Fill in `LAUNCH_RECOMMENDATION` — a short string synthesizing the
   findings into a real recommendation, referencing at least one
   `"blocking"` or `"accepted_risk"` finding by name.
6. Run `python3 starter.py` again — the score report should reflect
   your completed deliverable. Grade your own finished submission
   against `RUBRIC.md`'s six criteria.

## How to run it

```bash
python3 --version
python3 starter.py       # business problem + system description + your in-progress deliverable
python3 solution.py      # one complete, valid reference architecture review
```

## No required live-model dependency

This project reasons about a system's *design*, not about a specific
model's live output — an architecture review doesn't depend on
observing one model's generation to be valid. Every function in both
`starter.py` and `solution.py` is pure, deterministic Python operating
on structured data (`SYSTEM_DESCRIPTION`, `THREAT_MODEL`, `ADRS`,
`RED_TEAM_FINDINGS`), with zero network dependency required. See
`lesson.html`'s honest disclosure on Ollama's status this session
(`/api/tags` OK, `/api/chat` hung again — the same persistent,
sandbox-wide issue Chapters 3, 4, 5, 9, 10, 11, and 12 all documented) —
it has no bearing on this project's deliverable.

## One criterion `solution.py` deliberately leaves for you

Following Chapter 11's own precedent (its reference solution
deliberately left the executive-summary-and-prioritization criterion
incomplete, since writing it from confirmed findings is the actual
Phase 5 skill being taught), `solution.py`'s `LAUNCH_RECOMMENDATION` is
left as a structural placeholder with real findings behind it, not a
finished executive recommendation. Writing your own, real, prioritized
launch recommendation from `solution.py`'s (or your own) findings is the
concrete synthesis skill this capstone's final criterion grades — not
something to copy from a reference file.
