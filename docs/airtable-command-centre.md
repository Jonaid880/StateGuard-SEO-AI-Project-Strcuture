# StateGuard SEO Command Centre — Airtable Reference

The SEO Operating System lives in Airtable. This file records its structure so the project has a source of truth.

**Built:** 2026-06-11
**Base (MAIN):** StateGuard SEO Command Centre — `appM7z8RfiM9nABQa`
**Open:** https://airtable.com/appM7z8RfiM9nABQa

> This is the **main base** for the SEO Operating System. It was originally the "StateGuard & ProForce" base (the only one shared with the Claude–Airtable integration); the user is renaming it to **StateGuard SEO Command Centre** in the Airtable UI (the API has no base-rename endpoint). The base ID `appM7z8RfiM9nABQa` is unchanged by the rename. It also still contains the pre-existing `Daily Update` (ProForce) table.

> **Planning & tracking only. No publishing automation. All recommendations are reviewed manually before implementation.**

---

## Tables (7)

| Table | ID | Primary field | Purpose |
|-------|----|---------------|---------|
| Opportunities | `tblj8ImoiXXOjc2Xm` | Opportunity Name | SEO opportunity backlog |
| Keywords | `tblIyRYsRBCFHwhv1` | Keyword | Keyword research & clustering |
| Competitors | `tblmMvGA5EId7BzdP` | Competitor Name | Competitor intelligence |
| Content Calendar | `tbl4n94v668Eehvfc` | Title | Editorial planning (proposed only) |
| AI Visibility | `tblwxO8THa03tpWHz` | Question | AI citation tracking |
| Technical SEO Issues | `tblCGcz1Fl3Z2Uz6f` | Issue Name | Technical issue tracker |
| Service & Industry Silo Map | `tblMZKYMUGOYH3UbX` | Page Name | Information-architecture silos |

## Relationships

- **Opportunities.Related Keyword** ↔ Keywords.**Opportunity**
- **Content Calendar.Primary Keyword** ↔ Keywords.**Content Calendar**
- **Service & Industry Silo Map.Target Keyword** ↔ Keywords.**Silo Pages**
- **Service & Industry Silo Map.Parent Page** ↔ **Child Pages** (self-link hierarchy)

## Computed ID fields (API can't create these — added manually)

Airtable's API can't create computed field types. Done in the UI:

- ✅ **Opportunities** — `Opportunity ID` (Autonumber) + `Date Created` (Created time).
- ✅ **Keywords** — `Keyword ID` (Autonumber).

Optional, for full ID parity, add an Autonumber field the same way (1 click each) to:
- **Competitors** → "Competitor ID" · **Content Calendar** → "Content ID" · **AI Visibility** → "Visibility ID" · **Technical SEO Issues** → "Issue ID" · **Service & Industry Silo Map** → "Page ID".

The descriptive name is each table's primary field (Airtable best practice), so nothing is blocked without these.

---

## Views to create (5)

Views can't be created via API — add each in ~4 clicks. In the table, click the view list → **+ Create** → **Grid**, name it, then set the filter/sort below.

| # | View name | Table | Filter | Sort |
|---|-----------|-------|--------|------|
| 1 | High Priority Opportunities | Opportunities | `Priority` is any of **Critical, High** | `Impact Score` ↓ |
| 2 | Published Content | Content Calendar | `Publish Status` is **Published** | `Traffic` ↓ |
| 3 | Open Technical Issues | Technical SEO Issues | `Status` is any of **Open, Investigating** | `Severity` ↓ |
| 4 | Competitor Reviews Due | Competitors | `Last Reviewed` is **on or before** "1 month ago" **OR** is **empty** | `Last Reviewed` ↑ |
| 5 | GEO Opportunities | Opportunities | `Category` is **GEO** | `Priority` ↓ |

> Tip: for #4, use the filter group with "Or" to combine the date and empty conditions.

---

## Dashboard-ready structure

Once the views exist, build an **Interface** (Airtable → Interfaces → Start building → Dashboard) with:

- **Number** elements: count of High Priority Opportunities; count of Open Technical Issues; sum of `Lead Generated` (Content Calendar); count of AI Visibility rows where `StateGuard Mentioned` is checked.
- **Grid/List** elements pointed at the 5 views above.
- **Chart**: Opportunities grouped by `Category` / `Status`; Content Calendar by `Publish Status`.

---

## Seeded data (2026-06-11)

Beyond the original samples, the base was populated from `STATEGUARD_PROFILE.md`:

- **Keywords — 21 records.** One primary commercial/transactional keyword per all **11 service lines**, plus 6 audience-intent keywords (one per buyer audience) and 4 informational/AEO keywords. Clustered (`Security Guards`, `Mining Security`, `Audience – Facility Managers`, `Informational – Pricing`, …) with target-page slugs.
- **Service & Industry Silo Map — 13 records.** Two hubs (**Security Services**, **Industries We Serve**) with all 11 lines as children: 6 Services (Security Guards, Mobile Patrols, Alarm Response, Concierge Security, Monitoring Services, Event Security) + 5 Industries (Healthcare, Mining, Construction, Critical Infrastructure, Government). Every leaf has `Parent Page` set and `Target Keyword` linked to its matching keyword.
- **Prompts** for all 8 capabilities live in `../prompts/` (templates the agents call).

---

## Guardrail

This base is a planning and tracking system. It contains recommendations and status only. Nothing here publishes to or edits any live site — implementation is always a manual, human-reviewed step performed outside Airtable.
