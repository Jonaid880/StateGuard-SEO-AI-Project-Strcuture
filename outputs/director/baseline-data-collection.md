# Baseline Data Collection Guide

**Objective:** Capture the **first real StateGuard SEO baseline** — every metric, where to find it, and where it lands in the Command Centre.
**Author:** SEO Director · **Date:** 2026-06-11
**Base:** StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`)

> **Integrity rules (non-negotiable):** Record **real numbers only** — never invent, estimate, or back-fill. A blank is honest; a guess corrupts the trend. Every capture is a **new dated row** in Metrics Snapshots (never overwrite a past snapshot — Rule 4). Cite the `Source` on every row. A pre-launch baseline of mostly zeros is the correct starting line.

## Destination tables (IDs)
- **Metrics Snapshots** `tbly27DXqeefAozPW` — primary destination (one dated row per metric per period).
- Leads `tbl9LtfBT57qJRu0V` · Competitors `tblmMvGA5EId7BzdP` · Citation Opportunities `tblvYbZDlBC9XFJ2l` · Technical SEO Issues `tblCGcz1Fl3Z2Uz6f` · *(Rank Tracking — proposed, optional).* 

**Each metric below lists:** Source · Exact Location · Screenshot Required · Frequency · Airtable Destination Table · Metric Snapshot Record Type *(the catalog Metric · Category · Entity · `Source` select value)*.

---

## 1. Google Search Console
*Property: stateguard.com.au. Use a clean calendar-month window for monthly pulls.*

| Metric | Exact Location | Screenshot | Frequency | Destination Table | Snapshot Record Type |
|--------|----------------|:----------:|-----------|-------------------|----------------------|
| Organic Clicks | Performance → Search results → **Total Clicks** | ✅ Yes (chart + total) | Monthly | Metrics Snapshots | Organic Clicks · SEO · StateGuard · *Google Search Console* |
| Organic Impressions | Performance → Search results → **Total Impressions** | ✅ Yes | Monthly | Metrics Snapshots | Organic Impressions · SEO · StateGuard · *Google Search Console* |
| Average Position (overall) | Performance → Search results → **Average Position** | ✅ Yes | Monthly | Metrics Snapshots | Average Position — Priority Keywords · SEO · StateGuard · *Google Search Console* |
| Average Position (priority KWs) | Performance → **Queries** tab → filter to the 14 priority keywords (regex) → Average Position | ✅ Yes | Monthly | Metrics Snapshots | Average Position — Priority Keywords · SEO · StateGuard *(note: filtered)* |
| Indexed Money Pages | Indexing → **Pages** → "Indexed" count; verify priority URLs via URL Inspection | ✅ Yes | Monthly | Metrics Snapshots | Indexed Money Pages · SEO · StateGuard · *Google Search Console* |
| Top queries / top pages *(context)* | Performance → **Queries** / **Pages** tabs → Export | ⬜ Optional (export CSV) | Monthly | Keywords / Rank Tracking *(backfill)* | — (feeds keyword positions, not a single row) |
| Coverage / indexing errors *(tech)* | Indexing → **Pages** → "Why pages aren't indexed" | ✅ Yes | Monthly | **Technical SEO Issues** | — (creates issue records, not a snapshot) |

---

## 2. GA4
*Property: StateGuard. Channel = Organic Search. Same window as GSC.*

| Metric | Exact Location | Screenshot | Frequency | Destination Table | Snapshot Record Type |
|--------|----------------|:----------:|-----------|-------------------|----------------------|
| Organic Traffic (Users) | Reports → Acquisition → **Traffic acquisition** → filter *Session default channel group = Organic Search* → Users | ✅ Yes | Monthly | Metrics Snapshots | Organic Traffic (Users) · SEO · StateGuard · *GA4* |
| Organic Sessions *(denominator)* | Same report → **Sessions** | ✅ Yes | Monthly | Metrics Snapshots | Organic Sessions · SEO · StateGuard · *GA4* *(supplementary — add row)* |
| Conversions / Key events (web) | Reports → Engagement → **Conversions** (form submit, click-to-call) → filter Organic | ✅ Yes | Monthly | **Leads** + Metrics Snapshots | feeds Leads (web enquiries) + Leads Generated count |
| Organic landing-page performance *(context)* | Reports → Engagement → **Landing page** → filter Organic | ⬜ Optional | Monthly | Content Calendar (Traffic) | — (per-page attribution) |

> Lead Conversion Rate % is computed later: **Leads ÷ Organic Sessions** (this report supplies the denominator).

---

## 3. Google Business Profile
*Capture per office (×7: Melbourne HQ, Sydney, Perth, Hobart, Canberra, Adelaide, Brisbane). Set `Entity` = "StateGuard — <City>"; also record a StateGuard total.*

| Metric | Exact Location | Screenshot | Frequency | Destination Table | Snapshot Record Type |
|--------|----------------|:----------:|-----------|-------------------|----------------------|
| Profile views/searches | GBP → **Performance** → "How people discovered you" (Searches/Views) | ✅ Yes (per office) | Monthly | Metrics Snapshots | GBP Profile Views · SEO · StateGuard — <City> · *Google Business Profile* *(add row)* |
| Calls | GBP → Performance → **Calls** | ✅ Yes | Monthly | **Leads** (Source = Google Business Profile) + Metrics Snapshots | GBP Calls · Leads · StateGuard — <City> *(add row)* |
| Website clicks | GBP → Performance → **Website clicks** | ✅ Yes | Monthly | Metrics Snapshots | GBP Website Clicks · SEO · StateGuard — <City> *(add row)* |
| Direction requests | GBP → Performance → **Directions** | ✅ Yes | Monthly | Metrics Snapshots | GBP Direction Requests · SEO · StateGuard — <City> *(add row)* |
| Reviews count + avg rating | GBP → **Reviews** | ✅ Yes | Monthly | Metrics Snapshots | GBP Reviews / GBP Avg Rating · Authority · StateGuard — <City> *(add rows)* |
| NAP + verification status | GBP → each profile → **Info** (name/address/phone vs canonical 1300 723 887) + Verified badge | ✅ Yes (per office) | Monthly | **Citation Opportunities** (GBP record) + Metrics Snapshots | NAP Consistency % · Authority · StateGuard · *Manual Entry* |

> GBP-specific metrics (Views/Calls/Clicks/Directions/Reviews) are **new catalog rows** — add them to Metrics Snapshots on first capture; only NAP Consistency % already exists as a placeholder.

---

## 4. Ahrefs / SE Ranking

### 4a. Ahrefs (authority + competitor links)
| Metric | Exact Location | Screenshot | Frequency | Destination Table | Snapshot Record Type |
|--------|----------------|:----------:|-----------|-------------------|----------------------|
| StateGuard Domain Rating | Site Explorer → `stateguard.com.au` → **Overview → DR** | ✅ Yes | Monthly | Metrics Snapshots | StateGuard Domain Rating · Authority · StateGuard · *Ahrefs* |
| Referring Domains — Total | Site Explorer → Overview → **Referring domains** | ✅ Yes | Monthly | Metrics Snapshots | Referring Domains — Total · Authority · StateGuard · *Ahrefs* |
| New Referring Domains | Site Explorer → **Referring domains** report → filter *New (30d)* | ✅ Yes | Monthly | Metrics Snapshots | New Referring Domains · Authority · StateGuard · *Ahrefs* |
| Organic keywords (count) *(context)* | Overview → **Organic keywords** | ⬜ Optional | Monthly | Metrics Snapshots | (supplementary) |
| Competitor Domain Rating | Site Explorer → each competitor (×8) → **DR** | ✅ Yes (per competitor) | Monthly | **Competitors** + Metrics Snapshots | Competitor Domain Rating · Competitor · *Entity = competitor name* · *Ahrefs* |
| Competitor Referring Domains | Site Explorer → each competitor → **Referring domains** | ✅ Yes | Monthly | **Competitors** + Metrics Snapshots | Competitor Referring Domains · Competitor · *Entity = competitor name* · *Ahrefs* |

### 4b. SE Ranking (rankings + share of voice)
| Metric | Exact Location | Screenshot | Frequency | Destination Table | Snapshot Record Type |
|--------|----------------|:----------:|-----------|-------------------|----------------------|
| Keyword positions (14 priority) | Rankings → **Keyword positions** (Google AU) | ✅ Yes | **Weekly** | Rank Tracking *(proposed)* / Keywords | feeds the three SEO counts below |
| Keywords in Top 3 | Rankings → filter **positions 1–3** → count | ✅ Yes | Weekly | Metrics Snapshots | Keywords in Top 3 · SEO · StateGuard · *SE Ranking* |
| Keywords in Top 10 | Rankings → filter **positions 1–10** → count | ✅ Yes | Weekly | Metrics Snapshots | Keywords in Top 10 · SEO · StateGuard · *SE Ranking* |
| Average Position (tracked set) | Rankings → **Average position** | ✅ Yes | Weekly | Metrics Snapshots | Average Position — Priority Keywords · SEO · StateGuard · *SE Ranking* |
| Share of Voice / Visibility | Overview → **Visibility / SoV** | ✅ Yes | Monthly | Metrics Snapshots | Share of Voice vs Competitors · Competitor · StateGuard · *SE Ranking* |
| Keyword Overlap / Gap | **Competitors** → keyword gap (vs the 8 tracked) | ✅ Yes | Monthly | Metrics Snapshots | Keyword Overlap / Gap Count · Competitor · StateGuard · *SE Ranking* |

---

## 5. Airtable Command Centre (internal rollups)
*No external tool — computed from the base today. Screenshot optional (a view/count for the report pack).*

| Metric | Exact Location (in base) | Screenshot | Frequency | Destination Table | Snapshot Record Type |
|--------|--------------------------|:----------:|-----------|-------------------|----------------------|
| Links Won | Link Opportunities → filter `Status = Won` → count | ⬜ Optional | Weekly | Metrics Snapshots | Links Won · Authority · StateGuard · *Airtable* |
| Citations Live | Citation Opportunities → `Status = Live` → count | ⬜ Optional | Weekly | Metrics Snapshots | Citations Live · Authority · StateGuard · *Airtable* |
| AI Mention Rate % | AI Visibility → `StateGuard Mentioned` ÷ total rows | ⬜ Optional | Monthly | Metrics Snapshots | AI Mention Rate % · AI Visibility · StateGuard · *Airtable* |
| AI Citation Count | AI Visibility → count of ticked ChatGPT/Gemini/Perplexity | ⬜ Optional | Monthly | Metrics Snapshots | AI Citation Count · AI Visibility · StateGuard · *Airtable* |
| Leads Generated (Count) | Leads → filter `Date` in period → count | ⬜ Optional | Weekly | Metrics Snapshots | Leads Generated (Count) · Leads · StateGuard · *Airtable* |
| Leads Won (Count) | Leads → `Lead Status = Won` → count | ⬜ Optional | Weekly | Metrics Snapshots | Leads Won (Count) · Leads · StateGuard · *Airtable* |
| Lead Pipeline Value | Leads → open leads → sum `Estimated Value` | ⬜ Optional | Weekly | Metrics Snapshots | Lead Pipeline Value · Leads · StateGuard · *Airtable* |
| Lead Conversion Rate % | Leads count ÷ GA4 Organic Sessions | ⬜ Optional | Monthly | Metrics Snapshots | Lead Conversion Rate % · Leads · StateGuard · *Manual Entry* |
| Opportunities Complete % | Opportunities → `Status = Completed` ÷ total | ⬜ Optional | Weekly | Metrics Snapshots | Opportunities Complete % · Implementation · StateGuard · *Airtable* |
| Open Technical Issues | Technical SEO Issues → `Status = Open/Investigating` → count | ⬜ Optional | Weekly | Metrics Snapshots | Open Technical Issues · Implementation · StateGuard · *Airtable* |
| Money Pages Published | Silo Map → `Status = Published` → count | ⬜ Optional | Monthly | Metrics Snapshots | Money Pages Published · Implementation · StateGuard · *Airtable* |
| Content Published (Count) | Content Calendar → `Publish Status = Published` → count | ⬜ Optional | Weekly | Metrics Snapshots | Content Published (Count) · Implementation · StateGuard · *Airtable* |
| Quarter Completion % | Opportunities → current `Roadmap Quarter` → Completed ÷ total | ⬜ Optional | Monthly | Metrics Snapshots | Quarter Completion % · Roadmap · StateGuard · *Airtable* |
| Off-Page Milestones Complete | Off-page tables → Won/Live/Landed vs plan | ⬜ Optional | Monthly | Metrics Snapshots | Off-Page Milestones Complete · Roadmap · StateGuard · *Airtable* |

---

## Capture order (first baseline — fastest first)
1. **Airtable rollups (Section 5)** — available now, no tool; honest internal baseline today.
2. **GSC + GA4 (Sections 1–2)** — free; organic traffic, clicks, impressions, positions, indexing.
3. **GBP (Section 3)** — per office; calls/clicks + NAP verification.
4. **Ahrefs + SE Ranking (Section 4)** — paid; authority, competitor, ranking metrics.

## Screenshot pack convention
Save each screenshot as `baseline/<source>/<metric>_<YYYY-MM-DD>.png` (e.g. `baseline/gsc/organic-clicks_2026-06-30.png`). Store alongside this guide for an auditable evidence trail; reference the filename in the snapshot row's `Notes`.

## How to record each snapshot
For every metric: add a **new row** in Metrics Snapshots → set `Date` (capture date), `Metric` (catalog name), `Category`, `Value` (the real number), `Target` (from the roadmap), `Entity` (StateGuard or competitor/office), `Source` (select), `Notes` (screenshot filename + any caveat). Keep the original placeholder rows as templates.

> **Owner:** assign one person/connector to run this monthly (weekly for the rollups). Once two dated periods exist, build the Executive Dashboard Interface per [executive-dashboard-specification.md](executive-dashboard-specification.md).
