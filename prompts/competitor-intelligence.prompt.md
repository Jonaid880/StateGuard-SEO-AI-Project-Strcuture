# Prompt — Competitor Intelligence

**Agent:** [competitor-intelligence](../agents/competitor-intelligence.md) · **Output:** `../outputs/competitor-analysis/`

---

```
[Shared preamble — see prompts/README.md]

TASK: Run a full competitor intelligence pass on {{competitor domain(s), e.g. wilsonsecurity.com.au, msssecurity.com.au}}.
Read public pages only. Never edit any site.

For EACH competitor, deconstruct:
1. Overview — positioning, geographic coverage, conversion strategy (CTAs/forms/phone), visible tech signals.
2. Service pages — inventory; map each to StateGuard's 11 service lines; note depth + CTA strength.
3. Industry/vertical pages — inventory; map to StateGuard's verticals + 6 audiences; flag pages StateGuard lacks.
4. Blog strategy — clusters, cadence/recency, formats, standout/ranking topics.
5. Topical authority gaps — topics they own that StateGuard misses, AND whitespace no one covers well.
6. GEO opportunities — entity clarity, extractable facts, structured data, credentials; queries where an AI engine would cite them and what StateGuard needs to be cited instead.

Then synthesize across all competitors:
7. Recommendations for StateGuard — each tied to evidence + a goal (Lead generation / Authority), prioritized.

OUTPUT — all inside ../outputs/competitor-analysis/:
- <competitor-domain>.md  (sections 1-6, with source URLs + capture date)
- gap-matrix.md           (StateGuard vs all competitors: service/industry/topic/GEO coverage)
- recommendations.md      (ID | Type | Recommendation | Rationale | Supports goal | Priority | Effort | Evidence)
- README.md               (competitor set + run date)

Distinguish observed data from inference. Cite every source URL. Recommendations only.
Mirror key competitors into the Airtable Competitors table when asked.
```
