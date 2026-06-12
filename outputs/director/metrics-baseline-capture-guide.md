# Metrics Baseline — Capture Guide

**Table:** Metrics Snapshots (`tbly27DXqeefAozPW`) in StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`)
**Date:** 2026-06-11
**Status:** Structure only. 31 placeholder rows define the metric catalog — every `Value`, `Target`, and `Date` is **empty**. No values have been invented. This guide captures the **first real baseline**.

> Why a baseline matters: growth = today's value − a starting point. Until a dated baseline row exists for each metric, **no trend can be drawn**. Capture month-1 first; everything after is measured against it.

---

## How the table works
- **One row = one metric, one entity, one date.** The 31 placeholders are templates (no date/value).
- To record a baseline: **duplicate the placeholder row**, set `Date`, enter the real `Value`, set a `Target`, and keep `Category`/`Source`/`Entity`. Leave the original placeholder untouched as the template, **or** simply fill the placeholder's Date+Value for the first capture and duplicate-with-new-date each subsequent period.
- **Do not back-date or estimate.** If a number isn't available yet, leave the row blank and note why — a blank is honest; a guess corrupts the trend.

---

## Step 1 — Connect the data sources (one-time)
| Source | Gives you | Access needed |
|--------|-----------|---------------|
| **Google Search Console** | Clicks, impressions, average position, indexed pages | Verify stateguard.com.au property |
| **GA4** | Organic users/sessions, conversions | GA4 property + organic channel |
| **Ahrefs** (or Semrush) | Domain Rating, referring domains, competitor links | Paid account |
| **SE Ranking** | Keyword positions, share of voice, competitor overlap | Add the 14 priority keywords + 8 competitors |
| **Airtable** | Internal rollups (links won, leads, % complete) | Already in the base |
| **Manual Entry** | NAP %, AI share-of-voice, accuracy | Computed by the team |

## Step 2 — Capture the month-1 baseline (this week)
Record a dated row for each metric. Suggested order (fastest first):

**A. Airtable rollups (available now — no external tool):**
- Links Won, Citations Live, Leads Generated/Won/Pipeline Value, Opportunities Complete %, Open Technical Issues, Money Pages Published, Content Published, Quarter Completion %, Off-Page Milestones, AI Mention Rate %, AI Citation Count.
- Method: count/sum the relevant table today, enter as Value with today's Date, Source = Airtable. *(Today these are mostly 0 / small — that is the honest starting point, not an invented value.)*

**B. Google Search Console (free):**
- Organic Clicks, Organic Impressions, Average Position, Indexed Money Pages. Pull a clean 28-day or calendar-month window.

**C. GA4 (free):**
- Organic Traffic (Users). Same window as GSC.

**D. Ahrefs/Semrush + SE Ranking (paid):**
- StateGuard Domain Rating, Referring Domains (total/new), Competitor DR + Referring Domains (one row per competitor — set `Entity`), Keyword Overlap, Share of Voice, Keywords in Top 3/10.

**E. Manual (computed):**
- NAP Consistency %, AI Share of Voice, AI Mention Accuracy %, Lead Conversion Rate % (leads ÷ organic sessions).

## Step 3 — Set targets
For each baseline row, set a realistic `Target` for the next review period (monthly). Anchor targets to the [12-month roadmap](12-month-seo-roadmap.md) and [strategy](../../docs/STATEGUARD_SEO_STRATEGY.md) (leads > traffic). Don't set a target you can't tie to a planned action.

## Step 4 — Lock the cadence
| Frequency | Metrics |
|-----------|---------|
| **Weekly** | Airtable rollups (links won, leads, % complete, open issues), keyword positions |
| **Monthly** | GSC + GA4 + Ahrefs + SE Ranking pulls, AI visibility probe, NAP audit |

Each period: add **new dated rows** (never overwrite a past snapshot — Rule 4, never delete). The dashboard charts read across dates.

## Step 5 — Build the dashboard
Once ≥1 baseline + 1 follow-up period exist, build the **Executive Dashboard** Interface per the [specification](executive-dashboard-specification.md). Charts point at Metrics Snapshots (filtered by Category + Metric, plotted over Date).

---

## Owner & integrity rules
- **Owner:** assign a human (or connector) to enter A–E each period; agents maintain the Airtable-rollup rows.
- **Integrity:** never invent, estimate, or back-fill a value. Blank > fake. Cite the Source on every row. A baseline of mostly zeros is correct for a pre-launch program — it is the real starting line.

> Immediate next action: capture **Step 2A (Airtable rollups)** today — they need no external tools and give an honest internal baseline this afternoon.
