# Baseline Capture Worksheet — GSC · GA4 · SE Ranking/Ahrefs

**Purpose:** Fill the `Your Value` column from the three external sources, then hand this back — the SEO Director will write each value into **Metrics Snapshots** (`tbly27DXqeefAozPW`) as the first dated baseline.
**Capture date:** ____-__-__  (use one consistent month/window for all)
**Rule:** real numbers only. Leave blank if unavailable — never guess.

> Covers the three external sources you named. (Google Business Profile + Airtable internal rollups are captured separately — say the word and I'll do the Airtable rollups now, no tools needed.)

---

## 1. Google Search Console  *(property: stateguard.com.au · window: last full calendar month)*

| # | Metric | Where to read it | Your Value |
|---|--------|------------------|:----------:|
| 1 | Organic Clicks | Performance → Search results → **Total Clicks** | |
| 2 | Organic Impressions | Performance → Search results → **Total Impressions** | |
| 3 | Average Position (overall) | Performance → **Average Position** | |
| 4 | Average Position (priority KWs) | Performance → Queries → filter to the 14 priority keywords | |
| 5 | Indexed Money Pages | Indexing → Pages → **Indexed** count | |

## 2. GA4  *(property: StateGuard · channel: Organic Search · same window)*

| # | Metric | Where to read it | Your Value |
|---|--------|------------------|:----------:|
| 6 | Organic Traffic (Users) | Acquisition → Traffic acquisition → filter *Organic Search* → **Users** | |
| 7 | Organic Sessions | same report → **Sessions** | |
| 8 | Web Conversions (enquiries) | Engagement → Conversions → filter Organic *(if configured)* | |

## 3. SE Ranking *(or Ahrefs)*  *(Google AU · 14 priority keywords · 8 tracked competitors)*

### StateGuard authority + rankings
| # | Metric | Where to read it | Your Value |
|---|--------|------------------|:----------:|
| 9 | Domain Rating / Trust | Ahrefs Overview → **DR** *(or SE Ranking domain trust)* | |
| 10 | Referring Domains — Total | Ahrefs Overview → **Referring domains** | |
| 11 | New Referring Domains (30d) | Ahrefs Referring domains → filter *New* | |
| 12 | Keywords in Top 3 | SE Ranking → positions 1–3 → count | |
| 13 | Keywords in Top 10 | SE Ranking → positions 1–10 → count | |
| 14 | Average Position (tracked set) | SE Ranking → **Average position** | |
| 15 | Share of Voice / Visibility | SE Ranking → Overview → **Visibility/SoV** | |
| 16 | Keyword Overlap / Gap | SE Ranking → Competitors → keyword gap count | |

### Competitors (one row each — DR + Referring Domains)
| # | Competitor | Domain Rating | Referring Domains |
|---|------------|:-------------:|:-----------------:|
| 17 | Wilson Security | | |
| 18 | MSS Security | | |
| 19 | Certis Security Australia | | |
| 20 | SNP Security | | |
| 21 | Securecorp | | |
| 22 | SECOM Australia | | |
| 23 | Allied Universal (G4S) | | |
| 24 | Glad Group | | |

---

## When you've filled it
Paste the filled worksheet (or the source screenshots) back. I will then, for each metric:
- create a **new dated row** in Metrics Snapshots with `Date`, `Value`, `Category`, `Entity`, `Source`;
- mirror Competitor DR/RDs into the **Competitors** table;
- leave the placeholder catalog rows intact;
- never overwrite a prior snapshot.

> Quick win available now: I can record the **Airtable internal rollups** (links won, leads, opportunities %, etc.) as real baseline rows immediately — they're computed from the base and need no external tool. Just say "do the Airtable rollups."
