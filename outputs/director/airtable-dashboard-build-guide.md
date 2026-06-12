# Airtable Dashboard Build Guide

**Base:** StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`) · **Date:** 2026-06-11
**Goal:** Build 5 Interface dashboards — Executive, SEO, Competitor, Off-Page, Lead.

> **Why this is a guide, not an automation:** Airtable **Interfaces, dashboards, and views cannot be created via the API** — they're built in the Airtable UI. This is the step-by-step build sheet. Operational KPIs (Leads, Opportunities, Link Opportunities counts) work **immediately**; trend charts need **Metrics Snapshots** populated with a baseline first (see [baseline-data-collection.md](baseline-data-collection.md)).

## Tables used
Metrics Snapshots `tbly27DXqeefAozPW` · Leads `tbl9LtfBT57qJRu0V` · Opportunities `tblj8ImoiXXOjc2Xm` · Keywords `tblIyRYsRBCFHwhv1` · Competitors `tblmMvGA5EId7BzdP` · AI Visibility `tblwxO8THa03tpWHz` · Link Opportunities `tbls5HJYFizVeLIrt`.

---

## Part A — One-time setup

### A1. Create supporting views first (in each base table)
Interface elements read from a table/view, so create these views (Grid unless noted):

| Table | View | Filter / Sort |
|-------|------|---------------|
| Metrics Snapshots | SEO / Competitor / Authority / AI Visibility / Leads (5 views) | filter `Category` = that value; sort `Date` ↑ |
| Metrics Snapshots | Latest by Metric | sort `Date` ↓ (for "current value" KPI cards) |
| Leads | Open Pipeline | `Lead Status` is any of New, Qualified, Proposal Sent |
| Leads | Won | `Lead Status` = Won |
| Leads | This Period | `Date` is within this month |
| Opportunities | By Quarter | group `Roadmap Quarter`; sort `Impact Score` ↓ |
| Opportunities | High Priority | `Priority` is any of Critical, High |
| Keywords | Priority Keywords | `Priority` = High; sort `Cluster` |
| Competitors | All (sort Authority ↓) | sort `Authority Score` ↓ |
| Link Opportunities | High-Priority Prospects | `Priority` = High; sort `Authority Score` ↓ |
| Link Opportunities | Won | `Status` = Won |
| AI Visibility | Mentioned | `StateGuard Mentioned` = checked |

### A2. Create the Interface app
1. Airtable → left rail → **Interfaces** → **Start building** (or **＋ New interface**).
2. Choose **Dashboard** layout → name it **"StateGuard SEO — Dashboards"**.
3. You'll add **5 pages** (one per dashboard): top bar → **＋ Add page** → **Dashboard** → name it. Repeat for all 5.
4. Set page-level access (share with the team as Viewer/Editor) when done.

### A3. How to add each element (applies everywhere)
- **KPI card** → **＋ Add element → Number** → pick **Source table/view** → **Summary** (Count / Sum of <field> / Percent) → optional **Filter** → optional **comparison vs previous**.
- **Chart** → **＋ Add element → Chart** → **Source** → **Chart type** (bar/line/donut) → **X-axis** (group-by field) → **Y-axis** (Count / Sum / Average) → optional **series/colour** by a field.
- **Widget (records)** → **＋ Add element → Grid / List** → pick the **view** → choose visible fields.
- **Filter control** → **＋ Add element → Filter** (or page-level **Filters** in the top bar) → choose the field (e.g. Date, Source) so viewers can slice the whole page.
- **Layout** → drag to resize/position; put KPI cards in a top row, charts in the middle, grids at the bottom.

> **Metrics Snapshots caveat:** it's tall (one row per metric per period). For a **trend chart**: Source = Metrics Snapshots, filter `Metric` = X, chart = **Line**, X-axis = `Date`, Y-axis = **Sum of Value** (one row/date so sum = the value). For a **current-value KPI card**: source the **"Latest by Metric"** view, filter `Metric` = X, summary = **Sum of Value**, and rely on the date-desc sort (or just read the latest snapshot row).

---

## Part B — The 5 dashboards

### 1. Executive Dashboard
*Audience: leadership. One screen: are we winning leads and on-plan?*

**KPI Cards (top row):**
| Card | Source | Summary |
|------|--------|---------|
| Leads (this period) | Leads · This Period | Count |
| Pipeline Value | Leads · Open Pipeline | Sum of Estimated Value |
| Leads Won | Leads · Won | Count |
| Opportunities Complete % | Opportunities | Percent where Status = Completed |
| AI Mention Rate | AI Visibility | Percent where StateGuard Mentioned = checked |

**Charts:**
- **Leads by Source** — Leads · Donut · X = Lead Source · Y = Count.
- **Leads over time** — Leads · Line · X = Date (by month) · Y = Count.
- **Roadmap progress** — Opportunities · Stacked Bar · X = Roadmap Quarter · colour = Status.
- **Organic Traffic trend** — Metrics Snapshots (SEO view, Metric = Organic Traffic) · Line · X = Date · Y = Value. *(after baseline)*

**Widgets:** Top Opportunities grid (Opportunities · High Priority, fields: Name, Category, Impact Score, Status, Roadmap Quarter).
**Filters:** Date range; Roadmap Quarter.
**Layout:** 5 KPI cards across top → 2×2 chart grid → opportunities grid full-width bottom.

### 2. SEO Dashboard
*Audience: SEO lead. Organic growth + keyword/page health.*

**KPI Cards:** Organic Traffic (latest) · Organic Clicks (latest) · Keywords in Top 10 (latest) · Average Position (latest) · Indexed Money Pages (latest) — all from Metrics Snapshots "Latest by Metric"; plus **Keywords total** (Keywords · Count).

**Charts:**
- **Organic Traffic over time** — Metrics Snapshots (SEO) · Line · X = Date · Y = Value (Metric = Organic Traffic).
- **Clicks vs Impressions** — Metrics Snapshots (SEO) · Line · two metrics as series.
- **Keywords by Status** — Keywords · Bar · X = Status · Y = Count.
- **Keywords by Cluster** — Keywords · Bar · X = Cluster · Y = Count.
- **Keywords by Search Intent** — Keywords · Donut · X = Search Intent.

**Widgets:** Priority Keywords grid (Keywords · Priority Keywords); SEO/Content/Technical opportunities grid (Opportunities filtered Category = Content / Technical SEO).
**Filters:** Cluster; Search Intent; Priority; (Metrics) Category = SEO.
**Layout:** KPI row → traffic trend (wide) → keyword breakdown charts (3 across) → grids.

### 3. Competitor Dashboard
*Audience: strategy. Where competitors lead and where the gaps are.*

**KPI Cards:** Competitors tracked (Competitors · Count) · Avg Competitor Authority (Competitors · Average of Authority Score) · StateGuard DR (Metrics Snapshots latest) · Share of Voice (Metrics Snapshots latest).

**Charts:**
- **Competitor Authority Score** — Competitors · Bar · X = Competitor Name · Y = Authority Score.
- **Competitor DR trend** — Metrics Snapshots (Competitor) · Line · X = Date · Y = Value · series = Entity.
- **Replicable backlink gaps** — Competitor Backlinks · Bar · X = Replicable · Y = Count (or by Status).
- **AI competitor mentions** — AI Visibility · Bar · X = Competitor Mentioned · Y = Count.

**Widgets:** Competitors grid (Name, Website, Authority, Last Reviewed, Industries); Competitor Backlinks grid (Targeted, high Opportunity Score).
**Filters:** Industry; Replicable; Status; Last Reviewed (reviews due).
**Layout:** KPI row → authority bar + DR trend → gaps chart + competitors grid.

### 4. Off-Page Dashboard
*Audience: Off-Page Director. Authority pipeline + wins.*

**KPI Cards:** Links Won (Link Opportunities · Won · Count) · Prospects in pipeline (Link Opportunities · Count where Status = Identified/Qualified/Outreach) · Citations Live (Citation Opportunities · Count where Status = Live) · Referring Domains (Metrics Snapshots latest) · Domain Rating (Metrics Snapshots latest) · **Ready For Submission** (count across Guest Post / Citation / Digital PR / Link tables where `Submission Status` = Ready For Submission — the human work queue).

**Charts:**
- **Link pipeline by Status** — Link Opportunities · Bar (funnel-style) · X = Status · Y = Count.
- **Opportunity Type mix** — Link Opportunities · Donut · X = Opportunity Type.
- **Prospects by Priority** — Link Opportunities · Bar · X = Priority.
- **Referring Domains trend** — Metrics Snapshots (Authority) · Line · X = Date · Y = Value.
- **Digital PR by Status** — Digital PR Opportunities · Bar · X = Status.
- **Submission pipeline (funnel)** — any submission table · Bar · X = `Submission Status` (Discovered → Qualified → Content Created → **Ready For Submission** → Submitted → Approved → Published) · Y = Count. The orange **Ready For Submission** stage is the human queue; nothing crosses to Submitted without a person.

**Widgets:** High-Priority Prospects grid (Link Opportunities · High-Priority Prospects); Outreach Campaigns grid (Stage); Citation NAP grid (Citation Opportunities, Status); **Ready-For-Submission queue grid** (filter `Submission Status` = Ready For Submission, fields: Submission URL, Submission Method, Contact, Package Link, Submission Owner).
**Filters:** Opportunity Type; Priority; Status; Country = Australia.
**Layout:** KPI row → pipeline bar + type donut → trend + PR chart → prospect/outreach grids.

### 5. Lead Dashboard ★ (primary goal)
*Audience: leadership + sales. The money view.*

**KPI Cards:** Total Leads (Leads · Count) · Leads Won (Leads · Won · Count) · **Win Rate %** (Leads · Percent where Status = Won) · Pipeline Value (Leads · Open Pipeline · Sum Estimated Value) · Won Value (Leads · Won · Sum Actual Value) · Conversion Rate (Metrics Snapshots latest).

**Charts:**
- **Leads by Source** — Leads · Donut · X = Lead Source.
- **Leads by Service** — Leads · Bar · X = Service · Y = Count.
- **Leads by Industry** — Leads · Bar · X = Industry.
- **Lead status funnel** — Leads · Bar · X = Lead Status (New→Qualified→Proposal→Won/Lost).
- **Leads by Type** — Leads · Donut · X = Lead Type.
- **Leads over time** — Leads · Line · X = Date (month).
- **Pipeline value by Service** — Leads · Bar · X = Service · Y = Sum of Estimated Value.

**Widgets:** Recent Leads grid (Lead ID, Date, Source, Service, Industry, Status, Estimated Value, Landing Page); Won Leads grid (Actual Value).
**Filters:** Lead Source; Service; Industry; Lead Status; Date range.
**Layout:** 6 KPI cards top → source/service/industry charts → status funnel + value-by-service → leads grid bottom.

---

## Part C — Build order & tips

1. **Build views first** (Part A1) — elements depend on them.
2. **Start with the Lead + Off-Page + Competitor dashboards** — they read operational tables and work **today** (no baseline needed).
3. **Add Metrics-Snapshots trend charts after the first baseline** is captured; until then those tiles read empty (honest).
4. **Use page-level filters** (Date range, Roadmap Quarter) so one control updates every element on the page.
5. **Colour consistently** — map Status/Priority colours to the field colours already set in the base.
6. **Share** each dashboard as **Viewer** for leadership, **Editor** for the SEO team.
7. **Refresh cadence:** operational KPIs update live; Metrics-Snapshots charts update when new dated rows are added (weekly/monthly per the baseline guide).

> Result: a 5-page Interface where leadership sees leads + roadmap at a glance, and each team gets a focused operational view — all reading the single source of truth, with the never-publish/never-send guardrails untouched (dashboards are read-only views of the base).
