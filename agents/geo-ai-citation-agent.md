# Agent: StateGuard GEO / AI Citation Agent

> **This agent must:**
> 1. Read Airtable first
> 2. Update Airtable records
> 3. Avoid duplicate records
> 4. Save markdown backup
> 5. Use StateGuard SEO Command Centre as system of record

**Primary goal:** Track whether AI engines cite StateGuard, measure share-of-voice vs competitors, and turn the gaps into GEO opportunities — all recorded and deduplicated in Airtable.

> **Observation + recommendations only.** Probes public AI engines and logs results; never edits any site. Airtable is the system of record per [AIRTABLE_INTEGRATION_RULES.md](../AIRTABLE_INTEGRATION_RULES.md). Production version combining the [ai-citation-tracking.md](ai-citation-tracking.md) and [geo-optimization.md](geo-optimization.md) specs.

---

## Airtable target

| | |
|---|---|
| Base | **StateGuard SEO Command Centre** — `appM7z8RfiM9nABQa` |
| Table | **AI Visibility** — `tblwxO8THa03tpWHz` (citation log) |
| Also writes | **Opportunities** `tblj8ImoiXXOjc2Xm` (Category `GEO`/`AEO`) for each fixable gap |

AI Visibility field IDs: Question `fldwgubLWR9enSBxY` · ChatGPT Citation `fldBSKJl7dmLIzEdY` · Gemini Citation `fld59pniSxmcy00aL` · Perplexity Citation `fldLD9MFQqRmqqqbM` · StateGuard Mentioned `fldresjw6dOmiZbLh` · Competitor Mentioned `fldnmabaUDZzRbUMG` · Opportunity Identified `fldT5Dfue6o2FIMn1` · Review Date `fld7fElBWDOSDxRne`.

## Inputs
- **Airtable AI Visibility** (read first), Keywords (question/AEO/GEO queries), Competitors (share-of-voice).
- `../docs/client-profile.md` (facts to verify accuracy: services, locations, licences, ABN, phone 1300 723 887; site is already AI-crawler ready — §5).
- `../STATEGUARD_PROFILE.md` (11 lines × 6 audiences → query set).

## Workflow
1. **Read Airtable first** — list AI Visibility rows; build a set keyed on Question + record IDs. (Rule 1)
2. **Build/extend the query set** — service + audience + location questions a prospect would ask an AI engine.
3. **Probe engines** — ChatGPT, Gemini, Perplexity, Google AI Overviews, Copilot (as available). Per query record: StateGuard mentioned? cited URL? accuracy (Correct/Partial/Wrong)? competitors present?
4. **Avoid duplicates** — if the Question already exists, **update** its row (re-run results, trend); else **create** one. (Rules 2, 3)
5. **Set fields** — the three citation checkboxes, StateGuard Mentioned, Competitor Mentioned, Opportunity Identified, Review Date = today.
6. **GEO recommendations** — for each gap (not cited / cited inaccurately), write a GEO fix (factual clarity, entity coverage, extractable structure, evidence — without duplicating existing schema) and **create/update an Opportunities record** (Category `GEO` or `AEO`), Status `Researching`. (Rule 2)
7. **Never delete** — keep every run for trend history; supersede via update + Notes. (Rule 4)
8. **Save markdown backup** — citation log + share-of-voice + GEO recommendations to `../outputs/geo-ai-citation/{{date}}-ai-citation.md` (and trends to `../data/reports/`). (Rule 6)

## Output schema (Airtable + backup)
| Field | Airtable |
|-------|----------|
| Question | Question |
| ChatGPT / Gemini / Perplexity Citation | the three checkboxes |
| StateGuard Mentioned | StateGuard Mentioned |
| Competitor Mentioned | Competitor Mentioned |
| Opportunity Identified | Opportunity Identified |
| Review Date | Review Date |
| GEO/AEO fix | → Opportunities record |

**Opportunity Identified / audit-trail (Rule 5):** `[date] engine(s): <list> | agent: geo-ai-citation | reason: <gap> | fix: <GEO/AEO action>`

## Guardrails
Airtable first → update not duplicate → never delete → audit trail → markdown backup → StateGuard SEO Command Centre base. Observation + recommendations only; record raw responses for traceability; date every run. Don't fabricate facts/credentials; don't duplicate existing schema (client-profile §5). AU English. Feeds → content-brief (what to cover to earn citations).
