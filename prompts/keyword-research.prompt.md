# Prompt — Keyword Research

**Agent:** [keyword-research](../agents/keyword-research.md) · **Output:** `../data/keywords/`

---

```
[Shared preamble — see prompts/README.md]

TASK: Build a prioritized, intent-mapped keyword set for {{seed: e.g. "the Mining Security service line" | "all 11 service lines"}}.

INPUTS: seed terms from the 11 service lines and 6 audiences in STATEGUARD_PROFILE.md.
Optional data: {{path to GSC export / keyword-tool export}}.

METHOD:
1. Expand seeds across services (guarding, patrols, monitoring, CCTV, access control) and locations (7 office cities + service areas).
2. Enrich each: AU monthly volume, difficulty, SERP features (mark estimates clearly; cite any export).
3. Classify intent: Informational / Commercial / Transactional / Navigational.
4. Cluster by topic / target page; map to an existing hub or flag as a new-content opportunity.
5. Prioritize by relevance x opportunity (volume vs difficulty vs intent fit), weighted toward LEAD GENERATION (primary goal).

CONSTRAINTS: Australian English; correct terms ("Grade A1", "licence").

OUTPUT: CSV/Markdown to ../data/keywords/{{filename}} with columns:
Keyword | Cluster | Intent | Volume (AU) | Difficulty | SERP features | Priority (High/Med/Low) | Target page | Notes (source + rationale)

Mirror the high-priority rows into the Airtable Keywords table when asked. Recommendations only.
```
