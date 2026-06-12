# Airtable Integration Rules

**Status:** MANDATORY for ALL current and future agents in StateGuard-SEO-AI.
**Last updated:** 2026-06-11

This project uses **Airtable as the primary system of record**. Markdown files in the project folders are a **backup**, not the source of truth. Every agent ([the 8 capability agents](agents/) and any future agent) must follow the eight rules below.

> These rules sit on top of the project's hard guardrails — **recommendations only, never publish, human review before implementation**. Airtable is a planning/tracking system; nothing here writes to any live site.

---

## The base — system of record

| | |
|---|---|
| **Base name** | **StateGuard SEO Command Centre** |
| **Base ID** | `appM7z8RfiM9nABQa` |
| **Open** | https://airtable.com/appM7z8RfiM9nABQa |

All agents must read from and write to **this base** (Rule 8). Do not invent a new base or keep data only in files.

### Tables (use the right one per discovery type)

| Table | ID | Holds |
|-------|----|-------|
| Opportunities | `tblj8ImoiXXOjc2Xm` | SEO opportunities (any category) |
| Keywords | `tblIyRYsRBCFHwhv1` | Keywords, clusters, intent |
| Competitors | `tblmMvGA5EId7BzdP` | Competitor records |
| Content Calendar | `tbl4n94v668Eehvfc` | Content plans / briefs |
| AI Visibility | `tblwxO8THa03tpWHz` | AI citation tracking |
| Technical SEO Issues | `tblCGcz1Fl3Z2Uz6f` | Technical issues |
| Service & Industry Silo Map | `tblMZKYMUGOYH3UbX` | Page IA / silos |
| **StateGuard Knowledge Base** | `tbls1TV2f6wArnoxw` | **Operational source of truth — read before recommending** |
| Agent Performance | `tbl2HLbCyxFTNRXz0` | Agent scorecards |
| Agent Learning | `tblQcWkmokwfhzmLg` | Recorded agent corrections |

---

## RULE 0 — KNOWLEDGE BASE FIRST (content/keyword/GEO agents)

**Before generating any content, keyword, GEO, or brief recommendation, agents MUST read the `StateGuard Knowledge Base` table** (`tbls1TV2f6wArnoxw`). It is the primary source of operational truth — services, differentiators (Mission Talk, Assist App, NFC patrol verification, Grade A1), licences, ABN, phone 1300 723 887, buyer pain points, procurement/tender requirements, GEO evidence, and "do not duplicate" cautions.

- **Prefer `Approved` = true records** as established fact; treat unapproved as draft.
- **Never contradict** an Approved knowledge record; if new evidence conflicts, flag it (don't silently override) and record a new entry for human review.
- **Filter by `Category` / `Related Service` / `Related Industry`** to pull the relevant facts for the task.
- When an agent learns a new durable operational fact, **add it to the Knowledge Base** (Rule 2) so the whole system benefits.

> Knowledge Base First sits *before* Rule 1 for content work: know the truth, then check for existing records, then write.

---

## RULE 1 — AIRTABLE FIRST

**Before creating any recommendation, search Airtable for what already exists** and avoid duplicates. Check:

- Existing **Opportunities**
- Existing **Keywords**
- Existing **Competitor records**
- Existing **Content plans** (Content Calendar)
- Existing **Technical SEO issues**
- Existing **AI Visibility records**

**How:** use `search_records` / `list_records_for_table` on the relevant table(s). Match on the primary field (e.g. Keyword, Competitor Name, Issue Name) before writing. If a match exists, go to Rule 3 (update) instead of creating.

---

## RULE 2 — RECORD ALL DISCOVERIES

Whenever an agent discovers any of the following, it **must create or update an Airtable record** in the matching table:

| Discovery | Table |
|-----------|-------|
| New Keyword | Keywords |
| New Competitor | Competitors |
| New Opportunity | Opportunities |
| New Technical SEO Issue | Technical SEO Issues |
| New Content Idea | Content Calendar |
| New GEO Opportunity | Opportunities (Category = `GEO`) |

**No discovery may exist only in a markdown file.** Markdown is backup (Rule 6); Airtable is the record.

---

## RULE 3 — UPDATE STATUS (don't duplicate)

When something already exists, **update its status** rather than creating a new row. Typical progressions:

- **Opportunities:** Planned → Researching → Approved → In Progress → Implemented → Completed (or Rejected)
- **Keywords:** Research → Approved → Written → Published
- **Content Calendar:** Brief (Pending → Approved → Completed) · Writing (Not Started → Draft → Review → Completed) · Publish (Not Published → Published)
- **Technical SEO Issues:** Open → Investigating → Fixed → Verified

Example chain (as specified): `Research → Approved → In Progress → Implemented → Completed`.

**How:** use `update_records_for_table` with the existing record `id`. Never re-create.

---

## RULE 4 — NEVER DELETE DATA

**No Airtable record is ever deleted.** If something is wrong, obsolete, or rejected, **change its status** (e.g. Opportunities → `Rejected`) and explain in Notes. The history stays intact. Do not call any delete operation on this base.

---

## RULE 5 — AUDIT TRAIL

Every recommendation/record must carry an audit trail. Capture these four facts in the record's **Notes** (or dedicated fields where present):

1. **Date** — when the discovery/recommendation was made (use the table's Created-time field where it exists; otherwise write the date in Notes).
2. **Source** — where it came from (audit file, SERP capture, competitor URL, tool export, AI engine response).
3. **Agent Name** — which agent produced it (e.g. `keyword-research`, `competitor-intelligence`).
4. **Reason** — why it's recommended (the gap/opportunity it addresses).

**Suggested Notes format:**
```
[2026-06-11] source: outputs/competitor-analysis/wilsonsecurity.com.au.md | agent: competitor-intelligence | reason: gap — no Healthcare Security page; competitor ranks p1.
```

---

## RULE 6 — MARKDOWN BACKUP

Outputs are **still** saved to the project folders (`data/`, `outputs/`, `data/reports/`) as before — but their authoritative status lives in Airtable.

> **Airtable = System of Record. Markdown = Backup.**

Workflow: write the deliverable file **and** create/update the matching Airtable record(s), cross-referencing each (put the file path in the Airtable Source/Notes; note the record exists in the file).

---

## RULE 7 — IMPLEMENTATION TRACKING

When the **user confirms an implementation** (a fix shipped, a page published, a recommendation actioned off-system), the agent must **update the Airtable status** to reflect it:

- Opportunity → `Implemented` then `Completed`
- Technical SEO Issue → `Fixed` then `Verified` (set `Date Fixed`)
- Keyword → `Published` · Content Calendar Publish → `Published` (record Traffic / Lead Generated as they come in)

The system never performs the implementation — it only **tracks** what the human confirms.

---

## RULE 8 — STATEGUARD SEO COMMAND CENTRE

All agents must use the existing base **StateGuard SEO Command Centre** (`appM7z8RfiM9nABQa`) as the **primary workspace**. Do not create alternate bases or split the record across multiple bases. If access fails, stop and request that the base be shared with the integration — do not fall back to markdown-only.

---

## Quick agent checklist (every task)

1. **Search first** (Rule 1) — does it already exist?
2. If yes → **update status** (Rule 3); if no → **create record** (Rule 2).
3. Write the **audit trail**: Date · Source · Agent · Reason (Rule 5).
4. Save the **markdown backup** to the project folder and cross-reference (Rule 6).
5. **Never delete** — status only (Rule 4).
6. On confirmed implementation → **update status** (Rule 7).
7. Always in the **StateGuard SEO Command Centre** base (Rule 8).

---

*These rules are mandatory and override convenience. Airtable is the single source of truth; the system tracks and recommends — it never publishes, and a human reviews everything before implementation.*
