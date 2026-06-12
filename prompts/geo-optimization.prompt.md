# Prompt — GEO (Generative Engine Optimization)

**Agent:** [geo-optimization](../agents/geo-optimization.md) · **Output:** `../outputs/` + trends to `../data/reports/`

---

```
[Shared preamble — see prompts/README.md]

TASK: Recommend GEO improvements so generative engines (ChatGPT, Gemini, Perplexity, Google AI Overviews) retrieve and represent StateGuard accurately for {{topic/page set, e.g. "the Healthcare Security page" | "all service lines"}}.

INPUTS: ../data/content/ (content inventory), ../data/reports/ (citation findings), keyword/competitor outputs.

ASSESS & RECOMMEND on:
- Factual clarity — unambiguous, self-contained statements an LLM can lift (services, locations, licences, ABN, phone 1300 723 887).
- Entity coverage — consistent naming of StateGuard, services, "Grade A1" / ASIAL / licensing entities.
- Authority & evidence — credentials, certifications, data points, named sources.
- Machine-readable structure — headings, lists, tables, structured data (do NOT duplicate schema that already exists — client-profile §5).
- Freshness & cross-page consistency.

OUTPUT: ../outputs/{{date}}-geo-recommendations.md with columns:
Page/Topic | Issue (why an engine may misrepresent/skip it) | Recommendation (proposal) | Entities to reinforce | Priority | Evidence

Don't fabricate facts/credentials — verify against the client profile. Recommendations only.
```
