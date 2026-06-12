# Submission Automation Layer — Implementation Report

**Author:** Off-Page SEO Director · **Date:** 2026-06-11
**Base:** StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`)
**Spec:** [docs/SUBMISSION_AUTOMATION_LAYER.md](../../docs/SUBMISSION_AUTOMATION_LAYER.md)

> **Hard boundary enforced:** automation stops at **`Ready For Submission`**. Automatic submission, publishing, account creation, and outreach sending are **NOT enabled** — a human performs every outward action.

---

## 1. Submission fields added (✅ 48 fields — 12 × 4 tables)
The common Submission field set was added to **Guest Post Pipeline** (`tblKNJ8lUadwMHbSB`), **Citation Opportunities** (`tblvYbZDlBC9XFJ2l`), **Digital PR Opportunities** (`tblXWELOOfh0xMR8i`), and **Link Opportunities** (`tbls5HJYFizVeLIrt`):

| Field | Type |
|-------|------|
| Submission Status | Single select — `Discovered`, `Qualified`, `Content Created`, `Ready For Submission`, `Submitted`, `Approved`, `Published`, `Rejected` |
| Submission URL | URL |
| Submission Method | Single select — Email / Web Form / Account-Portal / Postal-Manual |
| Contact Name | Single line text |
| Contact Email | Email |
| Required Content | Long text |
| Outreach Draft | Long text |
| Submission Package | Long text |
| Package Link | URL |
| Submission Owner | Single line text |
| Submitted Date | Date |
| Result Notes | Long text |

## 2. Views to create (⏳ manual — Airtable has no view-creation API)
Add these **5 views to each of the 4 tables** (filter on `Submission Status`). They are the human work queues + tracking:

| View | Filter |
|------|--------|
| **Ready For Submission** | `Submission Status` = Ready For Submission |
| **Submitted** | `Submission Status` = Submitted |
| **Approved** | `Submission Status` = Approved |
| **Published** | `Submission Status` = Published |
| **Rejected** | `Submission Status` = Rejected |

*(In each table: view list → ＋ Create → Grid → name it → set the filter. The "Ready For Submission" view is the primary human queue — show Submission URL, Method, Contact, Package Link, Submission Owner.)*

## 3. Output structure (✅ created)
```
outputs/offpage/submissions/
├── guest-posts/
├── citations/
├── pr/
└── directories/
```
Each opportunity's full package is saved here and linked from Airtable `Package Link`.

## 4. Off-page agents updated (✅ 6 files)
The Submission Automation Layer step was added to:
- [backlink-intelligence-agent.md](../../agents/backlink-intelligence-agent.md)
- [guest-post-intelligence-agent.md](../../agents/guest-post-intelligence-agent.md) — article is a **draft, never auto-published**
- [outreach-intelligence-agent.md](../../agents/outreach-intelligence-agent.md) — owns the `Outreach Draft` + Ready queue
- [digital-pr-intelligence-agent.md](../../agents/digital-pr-intelligence-agent.md) — stats **verified before pitch**
- [citation-intelligence-agent.md](../../agents/citation-intelligence-agent.md) — **human creates the account**
- [offpage-seo-director-agent.md](../../agents/offpage-seo-director-agent.md) — reports the Ready-For-Submission queue

Each agent now: finds the submission URL + public contact → generates `Required Content` → drafts `Outreach Draft` → assembles `Submission Package` (Airtable + file) → advances `Submission Status` **only up to `Ready For Submission`** → stops.

## 5. Off-Page Director reporting updated (✅)
Weekly/monthly reports now include a **Ready-For-Submission queue per type** (items awaiting human action). The Automation Controller advances items to Ready, logs to Execution Logs, and snapshots counts — never crossing the boundary.

## 6. Dashboard specification updated (✅)
[airtable-dashboard-build-guide.md](../director/airtable-dashboard-build-guide.md) Off-Page dashboard now includes:
- **KPI card:** Ready For Submission (count across the 4 tables).
- **Chart:** Submission pipeline funnel (X = `Submission Status`), orange `Ready For Submission` = the human queue.
- **Widget:** Ready-For-Submission queue grid (URL, Method, Contact, Package Link, Owner).

## 7. Status crosswalk (existing → Submission Status)
| Submission Status | Guest Post | Citation | Digital PR | Link Opp |
|-------------------|-----------|----------|-----------|----------|
| Discovered/Qualified | Brief Pending | Identified | Identified | Identified/Qualified |
| Content Created | Writing Draft/Review | (copy drafted) | Drafted | — |
| Ready For Submission | Writing Completed | (package ready) | (pitch ready) | Outreach |
| Submitted | — | Submitted | Pitched | (sent) |
| Published | Publication Published | Live | Landed | Won |
| Rejected | (declined) | Needs Fix | Passed | Rejected |

---

## What is explicitly NOT enabled
- ❌ Automatic **submission** (forms/portals) — human submits.
- ❌ Automatic **publishing** — guest articles are drafts; human publishes.
- ❌ Automatic **account creation** — human creates directory/portal accounts.
- ❌ Automatic **outreach sending** — drafts only; human sends.
- ✅ Everything **up to `Ready For Submission`** is automated.

## Operational from here
1. Build the 5 status views per table (≈4 clicks each) — start with **Ready For Submission**.
2. Agents now populate the submission fields + package on each run.
3. The human works the **Ready For Submission** queue: review → submit → set `Submitted`; then `Approved`/`Published`/`Rejected` get tracked.

> Implementation complete. Fields, folders, agents, Director reporting, and the dashboard spec are updated; the only manual remainder is the 5 status views (no view API). The Ready-For-Submission boundary is enforced everywhere.
