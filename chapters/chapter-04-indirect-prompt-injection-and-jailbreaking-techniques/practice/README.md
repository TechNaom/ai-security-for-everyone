# Chapter 4 Practice Bank: Indirect Prompt Injection and Jailbreaking Techniques

Eight short, independent scenarios, each with its own fictional system —
none of them Northline Digest (the lesson) or ClearDesk Legal (the
exercises). The first five drill fast, accurate classification across all
five delivery channels from the lesson's taxonomy; the last three test
judgment about the injection/jailbreak distinction and defenses.

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

1. **CampusWiki** — retrieved documents/RAG chunks.
2. **FreightTrack** — tool/API output.
3. **LumenDocs** — web content the model summarizes/browses.
4. **InboxPilot** — email/document content.
5. **ScanSafe** — multi-modal channel (OCR-readable, human-invisible text).
6. **(Judgment) VaultAssist** — does content-tagging and sandwich
   reinforcement, both fully applied against every indirect channel,
   address a directly-attempted jailbreak with no injection involved?
7. **(Judgment) StreamMod** — prioritize between an indirect-injection
   risk in a retrieved policy document and an uncapped, unbound
   moderation tool.
8. **(Production-gear) HelpDeskGenie** — a combined attack: name both the
   delivery channel and the single highest-leverage defense layer that
   contains the damage even if the injection succeeds.

## Checking your work

Both `starter.py` and `solution.py` include automated `score_scenario_*()`
functions — run either file directly to see a score report. `solution.py`
is the fully filled-in reference and scores a perfect 9/9.

Scenario 6 is deliberately built to show that content-tagging and sandwich
reinforcement, while both real defenses against indirect injection, do
nothing against a jailbreak attempted directly with no injected content
involved at all — that's this chapter's injection/jailbreak distinction
made concrete: the correct answer is that these two defenses do **not**
address this specific attempt, since a user honestly typing a
hypothetical-framing request to a plain, unmanipulated system prompt never
touches either defense at all.
