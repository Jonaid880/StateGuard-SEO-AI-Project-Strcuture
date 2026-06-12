# Prompt — AEO (Answer Engine Optimization)

**Agent:** [aeo-optimization](../agents/aeo-optimization.md) · **Output:** `../outputs/` + trends to `../data/reports/`

---

```
[Shared preamble — see prompts/README.md]

TASK: Recommend AEO improvements to win direct-answer surfaces (featured snippets, People Also Ask, voice) for {{query set / page, e.g. "concierge security questions"}}.

INPUTS: ../data/keywords/ (question + PAA queries), ../data/content/, ../data/competitors/ (snippet wins).

DO:
- Map real PAA/voice questions to pages (use the 6 audiences' likely questions).
- Recommend answer formatting: concise 40-60 word direct answer first, then depth; match pattern to query type (definition/steps/table/list).
- Recommend clear H2/H3 question structure with immediate answers.
- Schema: recommend FAQ/HowTo ONLY where it does not already exist (homepage already has FAQPage — client-profile §5; never duplicate).
- Note existing answer wins to defend.

OUTPUT: ../outputs/{{date}}-aeo-recommendations.md with columns:
Target query | Current answer owner | StateGuard page | Recommended format | Draft answer (40-60 words, for review) | Priority | Evidence

Australian English; factual accuracy per client profile. Recommendations only — nothing published.
```
