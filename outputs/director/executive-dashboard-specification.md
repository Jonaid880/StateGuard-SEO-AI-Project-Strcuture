# Executive Dashboard — Specification

**Base:** StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`) · **Date:** 2026-06-11
**Authors:** SEO Director + Off-Page SEO Director
**Purpose:** Define the metrics, data sources, and dashboard structure management needs to measure success — across SEO, competitors, authority, AI visibility, leads, implementation, and roadmap.

> Measurement principle (from the [Strategy](../../docs/STATEGUARD_SEO_STRATEGY.md)): **leads over traffic.** Every panel ladders up to the primary goal — qualified lead generation — with authority/rankings/AI as the means.

---

## 1. Diagnosis — why success can't be measured today

The Command Centre records **current state** well, but cannot show **growth**, because:

1. **No time-series anywhere.** Every table holds *current* values (Authority Score, Impact Score, Traffic, statuses). With single snapshots you can show a number, never a **trend**. Growth is unmeasurable without history.
2. **The primary goal — leads — is barely tracked.** "Lead Generated" exists only as a loose number on Content Calendar rows. There is **no central lead register, no source attribution, no lead type, no value, no conversion rate.** The thing the system exists to produce is the thing it measures least.
3. **No external performance data captured.** No organic traffic (GA4), no clicks/impressions/positions (GSC), no domain rating/referring-domains (Ahrefs/Semrush). The base plans the work but never ingests the results.
4. **No keyword rank tracking.** Keywords have a workflow Status but no position, search volume, difficulty, or ranking URL — so "ranking growth" can't be shown.
5. **No aggregate rollups.** AI mention rate, links won, % implementation, quarter completion — all *derivable* but none surfaced as a metric.
6. **No competitor time-series.** Competitors have one Authority Score + Last Reviewed; no trend, overlap, or share-of-voice history.

**Bottom line:** add a **time-series layer** and a **lead register**, capture **external data**, and surface **rollups** — then the 7 growth views become possible.

---

## 2. Missing metrics (by dashboard area)

| Area | Missing metric(s) |
|------|-------------------|
| SEO growth | Organic traffic, clicks/impressions, keyword positions (current + history), keywords in top 3/10, indexed money pages, avg position |
| Competitor growth | Competitor DR trend, referring-domains trend, keyword overlap/gap, share-of-voice over time |
| Authority growth | StateGuard DR/DA, total + new referring domains, links won (by type), citation/NAP consistency score |
| AI visibility growth | AI mention rate %, citation count, AI share-of-voice, accuracy — all over time |
| Lead generation growth | Central leads count, source attribution, lead type, conversion rate, pipeline value |
| Implementation progress | % opportunities complete, open vs fixed tech issues, content pipeline %, pages published vs planned |
| Roadmap progress | Quarter completion %, on-track vs at-risk, off-page milestone completion |

---

## 3. Recommended new Airtable tables (close the gaps)

### 3.1 ⭐ Metrics Snapshots (keystone — enables ALL growth charts)
A periodic, tall-format snapshot of every KPI value, so any metric can be charted over time.

| Field | Type | Notes |
|-------|------|-------|
| Snapshot Date | Date (primary as `Metric — Date` text or date) | weekly/monthly |
| Metric | Single select | e.g. Organic Traffic, Keywords Top 10, Referring Domains, AI Mention Rate, Leads, DR |
| Category | Single select | SEO / Competitor / Authority / AI Visibility / Leads / Implementation / Roadmap |
| Value | Number | the measurement |
| Target | Number | benchmark for that period |
| Entity | Single line text | "StateGuard" or a competitor name |
| Source | Single line text | GA4 / GSC / Ahrefs / Airtable rollup |
| Notes | Long text | context / audit trail |

> One row per metric per period. A few dozen rows/month powers every trend line on the dashboard.

### 3.2 ⭐ Leads (makes the PRIMARY goal measurable)
| Field | Type | Notes |
|-------|------|-------|
| Lead / Organisation | Single line text (primary) | |
| Date | Date | |
| Source | Single select | Organic Search / AI Search / Direct / Referral / Tender / Other |
| Landing Page | Link → Silo Map / Content Calendar | which page drove it |
| Service Interest | Link → Silo Map (service) | |
| Industry | Single select | the 9 verticals |
| Lead Type | Single select | Enquiry / Quote Request / Tender Invitation / Phone Call |
| Status | Single select | New / Qualified / Proposal / Won / Lost |
| Estimated Value | Currency | pipeline value |
| Notes | Long text | audit trail |

### 3.3 Rank Tracking (keyword positions over time)
| Field | Type | Notes |
|-------|------|-------|
| Keyword | Link → Keywords (primary display) | |
| Date | Date | |
| Position | Number | SERP position |
| Ranking URL | URL | which page ranks |
| Search Engine / Location | Single select | Google AU |
| SERP Features | Multi select | Snippet / PAA / Local pack / AI Overview |

> Alternative (lighter): add `Current Position`, `Previous Position`, `Search Volume`, `Difficulty`, `Ranking URL`, `Last Checked` fields to the existing **Keywords** table, and snapshot positions into Metrics Snapshots. Use Rank Tracking only if per-date history per keyword is needed.

### 3.4 Field additions to existing tables (no new table)
- **Keywords:** Current Position, Previous Position, Search Volume, Difficulty, Ranking URL, Last Checked.
- **Content Calendar:** Impressions, Clicks, Conversion Rate (it already has Traffic + Lead Generated).
- **Competitors:** Domain Rating, Referring Domains (snapshot the trend into Metrics Snapshots).
- **Citation Opportunities:** NAP Consistent (checkbox) for the consistency score.

---

## 4. Executive Dashboard design (Airtable Interface)

Build one **Interface → Dashboard** named **"Executive Dashboard"**, organised into 7 panels (or tabs). Most tiles read **Metrics Snapshots** (trend charts) or are **rollups** of existing tables.

```
┌──────────────────────────── EXECUTIVE DASHBOARD ────────────────────────────┐
│ [1 SEO GROWTH] [2 COMPETITOR] [3 AUTHORITY] [4 AI VISIBILITY]               │
│ [5 LEAD GENERATION ★ primary] [6 IMPLEMENTATION] [7 ROADMAP]                │
└──────────────────────────────────────────────────────────────────────────────┘
```

- **Number tiles** for current value + delta; **line charts** (from Metrics Snapshots) for growth; **bar/donut** for breakdowns; **grids** for the underlying records.
- Panel 5 (Leads) is the hero panel — placed top-centre.

---

## 5. KPI definitions

Each KPI: **Data source · Collection method · Update frequency · Target benchmark · Dashboard location.**
> Collection note: external metrics (traffic, rankings, DR) require a **human or connector** to pull from GA4/GSC/Ahrefs into **Metrics Snapshots** — the system has no live analytics access by default. Internal rollups (links won, AI mention rate, % complete, leads count) compute directly in Airtable.

### Panel 1 — SEO Growth
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| Organic traffic (users) | GA4 | Human/connector → Metrics Snapshots | Monthly | +15% MoM yr-1 (set baseline month 1) | SEO panel — line chart |
| Organic clicks & impressions | GSC | Export → Metrics Snapshots | Monthly | Clicks ↑ each month | SEO panel — line chart |
| Avg position (priority keywords) | GSC / rank tool | Snapshot → Rank Tracking | Weekly | Improving; top 10 by Q2 | SEO panel — line |
| Keywords in Top 3 / Top 10 | Rank tool / GSC | Rank Tracking rollup → Snapshot | Weekly | 5 priority service kw in Top 10 by Q2 | SEO panel — number + trend |
| Indexed money pages | GSC Coverage | Manual check → Snapshot | Monthly | 100% of priority pages indexed | SEO panel — number |

### Panel 2 — Competitor Growth
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| Competitor Domain Rating trend | Ahrefs/Semrush | Human → Competitors + Snapshots | Monthly | Close gap vs Wilson/MSS | Competitor panel — multi-line |
| Keyword overlap / gap count | Rank tool | Export → Snapshot | Monthly | Gap shrinking | Competitor panel — number |
| Share of Voice vs competitors | Rank tool / SERP | Snapshot | Monthly | StateGuard share ↑ | Competitor panel — stacked area |
| Competitor referring domains | Ahrefs | Human → Snapshot | Monthly | Track delta vs StateGuard | Competitor panel — bar |

### Panel 3 — Authority Growth
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| StateGuard Domain Rating/Authority | Ahrefs/Moz | Human → Snapshot | Monthly | +N points/quarter | Authority panel — line |
| Referring domains (total + new) | Ahrefs/GSC Links | Human → Snapshot; Link Opportunities (Won) rollup | Monthly | +8–12 relevant in 90 days | Authority panel — line + number |
| Links won by type | Link Opportunities | Airtable rollup (`Status = Won`) | Weekly | Quality-weighted growth | Authority panel — donut |
| Citations live + NAP consistency | Citation Opportunities | Rollup (`Live`) + NAP checkbox | Monthly | 100% NAP across 7 offices | Authority panel — gauge |

### Panel 4 — AI Visibility Growth
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| AI mention rate (% queries) | AI Visibility | Rollup (StateGuard Mentioned ÷ total) → Snapshot | Monthly | Rising from 0 baseline | AI panel — line |
| AI citation count (with link) | AI Visibility | Rollup of citation checkboxes | Monthly | ≥1 cited query in 90 days | AI panel — number |
| AI share-of-voice vs competitors | AI Visibility | Competitor Mentioned analysis → Snapshot | Monthly | StateGuard share ↑ | AI panel — stacked bar |
| Mention accuracy | AI Visibility | Manual rating → Snapshot | Monthly | Correct ≥ 90% | AI panel — number |

### Panel 5 — Lead Generation Growth ★ (primary)
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| Leads generated (count) | **Leads** table | Direct entry / form / CRM sync | Weekly | +growth MoM (baseline month 1) | Leads panel — big number + line |
| Leads by source | Leads | Rollup by Source | Monthly | Organic + AI share rising | Leads panel — donut |
| Lead type mix (enquiry/quote/tender) | Leads | Rollup by Lead Type | Monthly | Tender invitations rising | Leads panel — bar |
| Traffic → Lead conversion rate | GA4 + Leads | Computed (leads ÷ sessions) → Snapshot | Monthly | Improving each quarter | Leads panel — line |
| Estimated pipeline value | Leads | Sum of Estimated Value | Monthly | Growth | Leads panel — number |

### Panel 6 — Implementation Progress
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| Opportunities % complete | Opportunities | Rollup (Completed ÷ total) | Weekly | On-pace vs roadmap | Implementation panel — gauge |
| Open vs fixed technical issues | Technical SEO Issues | Rollup by Status | Weekly | 0 Critical/High open | Implementation panel — bar |
| Content pipeline status | Content Calendar | Rollup by Writing/Publish status | Weekly | Briefs → Published flowing | Implementation panel — funnel |
| Money pages published vs planned | Silo Map | Rollup (`Published` ÷ total) | Monthly | All priority pages live | Implementation panel — progress |

### Panel 7 — Roadmap Progress
| KPI | Data source | Collection method | Frequency | Target benchmark | Location |
|-----|-------------|-------------------|-----------|------------------|----------|
| Quarter completion % | Opportunities (`Roadmap Quarter` + Status) | Rollup per quarter | Monthly | Q-on-track | Roadmap panel — 4 gauges |
| On-track vs at-risk items | Opportunities | Status vs quarter vs date | Weekly | Minimise at-risk | Roadmap panel — bar |
| Off-page milestone completion | Off-page tables | Rollup (Won/Live/Landed) | Monthly | Month 1/2/3 plan hit | Roadmap panel — checklist |

---

## 6. Build sequence

1. **Create** the two keystone tables — **Metrics Snapshots** + **Leads** (highest impact; unlock 5 of 7 panels).
2. **Add** rank/volume fields to Keywords (or create Rank Tracking) + the Content Calendar/Competitors/Citation fields.
3. **Add rollup/formula fields** to existing tables for the internal KPIs (links won, % complete, AI mention rate, NAP score).
4. **Seed a baseline snapshot** (month 1) so growth has a zero point — without it, "growth" starts blank.
5. **Build the Interface** ("Executive Dashboard", 7 panels) — Interfaces are created in the Airtable UI (no API); tiles point at Metrics Snapshots + rollups.
6. **Assign collection owners** — a human/connector enters GA4/GSC/Ahrefs figures monthly; agents maintain the internal rollups + Leads + AI mention rate.

> **API note:** Airtable's API can create the **tables/fields** but **cannot create Interfaces/Dashboards or views** — those are built in the UI (this spec is the build sheet). Computed field types (rollup, formula referencing links) are partially API-creatable; some are quicker to add in-UI.

---

## 7. What this unlocks

With Metrics Snapshots + Leads in place and a baseline captured, management gets a single **Executive Dashboard** showing **growth** (not just state) across all 7 dimensions — and, critically, can finally answer the only question that matters for the primary goal: **"are we generating more qualified leads, and from which pages and channels?"**

> Recommended immediate action: approve and create **Metrics Snapshots** + **Leads**, then capture the **month-1 baseline** this week.
