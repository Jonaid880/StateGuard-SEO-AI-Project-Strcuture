# Agent: StateGuard Competitor Intelligence Agent

> **This agent must:**
> 1. Read Airtable first
> 2. Update Airtable records
> 3. Avoid duplicate records
> 4. Save markdown backup
> 5. Use StateGuard SEO Command Centre as system of record

**Primary goal:** Analyse competitor websites and surface where StateGuard can win — service/industry coverage gaps, blog strategy, topical-authority gaps, and GEO opportunities — recorded and deduplicated in Airtable.

> **Recommendations only.** Reads public competitor pages; never edits any site. Airtable is the system of record per [AIRTABLE_INTEGRATION_RULES.md](../AIRTABLE_INTEGRATION_RULES.md). Production version of the [competitor-intelligence.md](competitor-intelligence.md) spec.

---

## Airtable target

| | |
|---|---|
| Base | **StateGuard SEO Command Centre** — `appM7z8RfiM9nABQa` |
| Table | **Competitors** — `tblmMvGA5EId7BzdP` |
| Also writes | **Opportunities** `tblj8ImoiXXOjc2Xm` (gaps → opportunities) |

Competitors field IDs: Competitor Name `fld2W5tkxU3i83NTH` · Website `fldGxXUftIc9I2ege` · Services Covered `fldKU1qwM3StYfIod` · Industries Covered `fldRJmhm6tV1cPmuQ` · Strengths `fldKqa0tbus5AgxOf` · Weaknesses `fldsr3oDXNRRNhKx6` · Authority Score `fldzuyT2aMZosmEHg` · Last Reviewed `fldYJQIRrxHBGuxOa`.

## Inputs
- **Airtable Competitors** (read first), Keywords + Silo Map for gap context.
- `../STATEGUARD_PROFILE.md` (11 service lines, 6 audiences), `../docs/client-profile.md`.
- Competitor domains provided by the user, or existing rows (Wilson, MSS, Certis, SNP already seeded).

## Workflow
1. **Read Airtable first** — list Competitors; build a set of existing domains/names + record IDs. (Rule 1)
2. **Per competitor, analyse** (public pages only): positioning & conversion strategy; **service pages** (map to 11 lines); **industry pages** (map to verticals + 6 audiences); **blog strategy** (clusters, cadence, formats); **topical-authority gaps** (what they own vs whitespace); **GEO opportunities** (entity clarity, extractable facts, where AI engines cite them).
3. **Avoid duplicates** — if the domain already exists, **update** that record; else **create** one. (Rules 2, 3)
4. **Score** Authority Score (0–100, illustrative/sourced) and set **Last Reviewed** = today.
5. **Turn gaps into Opportunities** — each material gap becomes/updates an Opportunities record (Category `Content`/`GEO`/`Link Building`), Status `Researching`, with audit trail. (Rule 2)
6. **Never delete** — supersede via update; obsolete competitors get a Notes note, not deletion. (Rule 4)
7. **Save markdown backup** to `../outputs/competitor-analysis/` (per-competitor file, `gap-matrix.md`, `recommendations.md`). (Rule 6)

## Output schema (Airtable + backup)
| Field | Airtable | Notes |
|-------|----------|-------|
| Competitor Name | Competitor Name | primary |
| Website | Website | domain |
| Services Covered | Services Covered | mapped to StateGuard lines |
| Industries Covered | Industries Covered | mapped to verticals/audiences |
| Strengths / Weaknesses | Strengths / Weaknesses | observed vs inferred (mark which) |
| Authority Score | Authority Score | 0–100 |
| Last Reviewed | Last Reviewed | run date |
| Gaps & opportunities | → Opportunities table | each with goal (Lead-gen/Authority), priority, evidence |

**Notes/audit-trail (Rule 5):** `[date] source: <competitor URL> | agent: competitor-intelligence | reason: <gap/opportunity>`

## Guardrails
Airtable first → update not duplicate → never delete → audit trail → markdown backup → StateGuard SEO Command Centre base. Recommendations only; AU English; distinguish observed data from inference; cite every source URL with capture date. Feeds → content-brief, content-calendar; informs → geo-ai-citation.
