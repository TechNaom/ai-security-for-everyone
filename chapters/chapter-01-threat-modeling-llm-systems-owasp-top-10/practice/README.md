# Chapter 1 Practice Bank: Threat Modeling LLM Systems (The OWASP Top 10 for LLM Applications)

Eight short, independent scenarios, each with its own fictional system —
none of them GreenCart/Aurora (the lesson) or PolicyPilot (the exercises)
again. Each scenario is a few sentences and one judgment question. The
point here is speed and accuracy across many different systems, not depth
on one — the way a real security review actually feels.

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

1. **TicketTriage** — an IT helpdesk bot with a planted instruction in a
   ticket description.
2. **SummarizeBot** — a PDF summarizer whose output gets rendered as raw
   HTML.
3. **CodeReviewBot** — a model fine-tuned on unvetted, attacker-seeded
   training data.
4. **QuickChat** — a public chatbot with no rate limit or output cap.
5. **(Judgment) PluginMarket** — deciding whether a described vetting
   process already covers Supply Chain risk, or leaves a real gap.
6. **(Judgment) ResearchAssistant** — prioritizing between two real but
   unequal-impact issues when only one can be fixed before launch.
7. **(Production-gear) InsightsRAG** — picking the one fix, among four
   candidates, that actually closes an access-control gap in a RAG
   pipeline.
8. **(Production-gear) FieldServiceBot** — a full two-category mapping:
   how a planted instruction got in, and why it caused real damage.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9 when run.
Scenarios 5 and 6 are genuine judgment calls, not keyword-matched free
text — there's a single correct answer, but reaching it requires reasoning
about the scenario, not recalling a category name.
