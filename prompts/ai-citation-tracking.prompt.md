# Prompt — AI Citation Tracking

**Agent:** [ai-citation-tracking](../agents/ai-citation-tracking.md) · **Output:** `../data/reports/` + Airtable "AI Visibility"

---

```
[Shared preamble — see prompts/README.md]

TASK: Probe AI engines for StateGuard visibility on a defined query set and log results.

QUERY SET: {{list, or "generate from the 11 service lines x 6 audiences x AU locations"}}.
Examples: "best security company Australia", "best healthcare security provider Australia",
"who provides mobile patrol services Australia", "security companies for government tenders Australia".

ENGINES: ChatGPT, Gemini, Perplexity, Google AI Overviews, Copilot (as available).

FOR EACH query x engine, record:
- StateGuard mentioned? (yes/no)
- Cited with a link? which page?
- Accuracy of any StateGuard info (Correct/Partial/Wrong)
- Which competitors appeared
- Opportunity identified (what would earn/improve the citation)

OUTPUT: ../data/reports/{{date}}-ai-citation-log.md with columns:
Date | Engine | Query | StateGuard mentioned? | Cited URL | Accuracy | Competitors present | Notes
Plus a share-of-voice summary vs competitors, and a trend note vs the previous run.

Record raw responses for traceability; date every run. Feeds GEO/AEO. Observation + recommendations only.
Mirror rows into the Airtable AI Visibility table when asked.
```
