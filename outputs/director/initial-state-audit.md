# SEO Director Report — Initial State Audit

**Base:** StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`)
**Run by:** SEO Director Agent · **Date:** 2026-06-11
**Status:** Recommendations only — every item below awaits human review before implementation. Nothing published.

---

## 1. Executive Summary

The StateGuard SEO Command Centre has an **excellent framework but thin operational data**. All 7 core tables, relationships, the full 11-line keyword set, and a clean 2-hub silo are in place — but the "flesh" needed to drive leads is sparse: only 2 opportunities, 2 of ~53 content items, 4 competitors, and 3 AI-visibility questions, with no impact scores and two disconnected records.

This first Director pass **read the entire base, fixed structural gaps, and seeded a prioritized, lead-gen-weighted backlog** aligned to the new [SEO Strategy](../../docs/STATEGUARD_SEO_STRATEGY.md). Headline actions:

- Added the 3 missing **priority industries** (Education, Commercial Real Estate, Manufacturing) as keywords + opportunities.
- Built a **16-item Opportunities backlog** with Impact Scores, all mapped to the 5 priority services + 9 priority industries + GEO targets.
- Expanded **competitors 4 → 8** (added Securecorp, SECOM, Allied Universal/G4S, Glad Group as priority analysis targets).
- Expanded **AI-visibility questions 3 → 10** covering buyer/procurement GEO queries.
- Fixed **2 disconnected records** and stood up the **Agent Performance + Agent Learning** self-improvement loop.

**Strategic mandate applied:** lead generation over traffic. Money pages (services + industries) and tender/procurement visibility are weighted highest; pure informational volume is deprioritised.

---

## 2. Readiness Score

### **Current readiness: 4 / 10** (before this audit's records take effect: framework strong, data thin)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Framework & schema | 9/10 | 7 tables + relationships + silo + rules — excellent |
| Keyword coverage | 6/10 | 11 lines covered; 3 priority industries were missing (now added) |
| Opportunity backlog | 3/10 | only 2 opps, no impact scores (now 16, scored) |
| Competitor intel | 3/10 | 4 records, no major-player depth (now 8, 4 pending analysis) |
| Content pipeline | 2/10 | 2 of ~53 pages; briefs not written |
| AI visibility / GEO | 3/10 | 3 untested questions (now 10; citations unverified) |
| Technical readiness | 3/10 | 3 issues with no URLs; no crawl data yet |
| Data hygiene (links/audit trail) | 5/10 | 2 disconnected records (fixed); audit trails now added |

> **Post-audit readiness ≈ 6/10.** The backlog, strategy, competitor set, and GEO targets created today move the system from "scaffold" to "ready to execute." The path to 8+/10 runs through: a real technical crawl, the first written briefs, and live AI-citation probing.

---

## 3. Data Quality Findings

### Missing data
- **Impact Scores** were absent on all opportunities → set on all 16 priority items.
- **Keyword volume/difficulty** — no native fields (store in Notes or add fields; estimates must be cited).
- **Competitor depth** — Strengths/Weaknesses/Authority absent for the 4 new competitors (flagged *PENDING FULL ANALYSIS*).
- **Technical issues** — missing **Affected URL**, Date Identified, and Notes on all 3 → blocks verification (see §E).
- **Content Calendar** — only 2 items; no URL/Traffic/Lead data yet (expected pre-launch).
- **AI Visibility** — citation checkboxes unverified (require live probing by the GEO / AI Citation agent).

### Duplicate records
- **No exact duplicates.** Two acceptable near-overlaps (kept by design): Government has 2 keywords → 1 page (brand + tender intent); Construction has a commercial keyword + an audience variant. These are distinct queries, not duplicates.

### Disconnected records (fixed this run)
- **Opportunities → "Mobile Patrol Service Expansion"** had no keyword link → **linked** to *Mobile Patrol Services Australia* + Impact Score set.
- **Content Calendar → "Construction Site Security Checklist"** had no Primary Keyword → **linked** to *Construction Site Security*.
- **Silo Map** — all 13 pages are `Planned`, but several equivalents are **live on stateguard.com.au**. Flag: reconcile Silo `Status` with actually-published pages (a Director ↔ live-site sync task).

---

## 4. Audit Sections A–E

### A. Keyword Audit
- Reviewed all 21 existing keywords — 11 service/industry lines + 6 audiences + 4 informational. Clean clustering.
- **Missing service keywords:** none of the 5 priority services missing (all covered).
- **Missing industry keywords:** **Education, Commercial Real Estate, Manufacturing** — *created* as keywords + opportunities.
- **Created** 3 keyword records and 11 industry/service + 3 GEO opportunity records (see §7).

### B. Competitor Audit
- Reviewed 4 records (Wilson, MSS, Certis, SNP).
- **Missing major competitors** identified and *added* as priority analysis targets: **Securecorp, SECOM Australia, Allied Universal (G4S), Glad Group**.
- **Recommended priority for full analysis (in order):** 1) Securecorp, 2) Allied Universal/G4S (tenders/government), 3) SECOM (electronic/critical infra), 4) Glad Group (commercial real estate/concierge). Then deepen the 4 existing records (Strengths/Weaknesses/Authority).

### C. Content Audit
- Content Calendar holds only **2 of ~53** planned items; massive gap.
- **Highest-priority pages to brief first (lead-gen):** Security Guards, Government Security, Healthcare Security, Construction Security, Monitoring Services (Grade A1), Alarm Response — all now have Opportunities with Impact Scores and `Assigned To = Content Brief`.

### D. GEO Audit
- AI Visibility had **3 untested questions**; StateGuard not shown as cited.
- **Added 7 GEO tracking questions** (buyer/procurement framed) → 10 total.
- **Added 3 GEO Opportunities** (Best Security Company AU; Best Healthcare Provider AU; Government tender visibility), assigned to GEO / AI Citation.
- Next: the GEO / AI Citation agent must **probe engines live** and set the citation checkboxes + accuracy.

### E. Technical SEO Audit Preparation
A full technical audit **cannot run yet** — required inputs first:
1. **Crawl export** (Screaming Frog / Sitebulb) of stateguard.com.au — status codes, titles, H1s, canonicals, indexability.
2. **Core Web Vitals / PageSpeed** data for key templates (home, a service page, an industry page).
3. **Affected URLs** for the 3 existing issues (Missing H1, Broken Link, Missing FAQ Schema) — currently blank, so unverifiable.
4. **GSC** coverage + enhancement reports (indexing, schema, mobile).
5. **XML sitemap** snapshot for orphan/coverage cross-check.
> Note (client-profile §5): schema is already comprehensive via Yoast and interlinking is done — the audit must avoid re-flagging these. Do **not** enable the LiteSpeed Crawler.

---

## 5. Top 20 SEO Opportunities (lead-gen weighted)

Ranked by Impact Score. Items 1–16 are **live in Airtable** (Opportunities table); 17–20 are **recommended next** (not yet created — await go-ahead).

| # | Opportunity | Category | Priority | Impact | In Airtable |
|---|-------------|----------|----------|--------|-------------|
| 1 | Security Guards Service Page | Content | Critical | 95 | ✅ |
| 2 | Government Security Industry Page | Content | Critical | 90 | ✅ |
| 3 | Healthcare Security Industry Page | Content | High | 88 | ✅ (updated) |
| 4 | GEO: "Best Security Company Australia" citation | GEO | High | 88 | ✅ |
| 5 | Construction Security Industry Page | Content | High | 85 | ✅ |
| 6 | Monitoring Services Service Page (Grade A1) | Content | High | 84 | ✅ |
| 7 | Alarm Response Service Page | Content | High | 82 | ✅ |
| 8 | Mining Security Industry Page | Content | High | 80 | ✅ |
| 9 | GEO: "Best Healthcare Security Provider AU" citation | GEO | High | 80 | ✅ |
| 10 | Mobile Patrol Service Expansion | Keyword | Medium | 80 | ✅ (updated) |
| 11 | Critical Infrastructure Security Industry Page | Content | High | 78 | ✅ |
| 12 | Education Security Industry Page | Content | High | 76 | ✅ |
| 13 | Commercial Real Estate Security Industry Page | Content | High | 74 | ✅ |
| 14 | GEO: Government tender / procurement AI visibility | GEO | Medium | 72 | ✅ |
| 15 | Concierge Security Service Page | Content | Medium | 68 | ✅ |
| 16 | Manufacturing Security Industry Page | Content | Medium | 66 | ✅ |
| 17 | Capital-city location landing pages (7 offices) | Local SEO | High | ~75 | ▶ recommend |
| 18 | Enquiry/quote CRO on the 5 service pages | Conversion Rate Optimization | High | ~70 | ▶ recommend |
| 19 | AEO: cost/"how much" answer blocks → service pages | AEO | Medium | ~60 | ▶ recommend |
| 20 | Deepen 4 existing competitor profiles | (research) | Medium | ~55 | ▶ recommend |

## 6. Top 10 GEO Opportunities

| # | GEO query target | Tie-in | Tracked in AI Visibility |
|---|------------------|--------|--------------------------|
| 1 | Best Security Company Australia | brand authority | ✅ |
| 2 | Best Healthcare Security Provider Australia | Healthcare page + credentials | ✅ |
| 3 | Best alarm monitoring company Australia | Grade A1 differentiator | ✅ |
| 4 | Who provides government security services Australia | tenders/procurement | ✅ |
| 5 | Best mobile patrol company Australia | NFC patrol verification | ✅ |
| 6 | Security companies for construction sites Australia | builders audience | ✅ |
| 7 | Top security companies for healthcare facilities Australia | facility managers | ✅ |
| 8 | Security companies for mining sites Australia | remote-site capability | ✅ |
| 9 | Best concierge security provider Australia | property/facility managers | ✅ |
| 10 | Who provides mobile patrol services Australia | service intent | ✅ |

## 7. Top 10 Service Page Opportunities

| # | Service page | Priority | Impact | Opportunity in Airtable |
|---|--------------|----------|--------|--------------------------|
| 1 | Security Guards | Critical | 95 | ✅ |
| 2 | Monitoring Services (Grade A1) | High | 84 | ✅ |
| 3 | Alarm Response | High | 82 | ✅ |
| 4 | Mobile Patrols | Medium | 80 | ✅ |
| 5 | Concierge Security | Medium | 68 | ✅ |
| 6 | Event Security | Medium | ~64 | ▶ recommend |
| 7 | Security Guards — by city (Sydney/Melbourne/Perth…) | High | ~75 | ▶ recommend (Local SEO) |
| 8 | Mobile Patrols — by city | High | ~72 | ▶ recommend (Local SEO) |
| 9 | CCTV / Electronic Security service page | Medium | ~60 | ▶ recommend |
| 10 | Access Control service page | Medium | ~58 | ▶ recommend |

## 8. Top 10 Industry Page Opportunities

| # | Industry page | Priority | Impact | Opportunity in Airtable |
|---|---------------|----------|--------|--------------------------|
| 1 | Government | Critical | 90 | ✅ |
| 2 | Healthcare | High | 88 | ✅ |
| 3 | Construction | High | 85 | ✅ |
| 4 | Mining | High | 80 | ✅ |
| 5 | Critical Infrastructure | High | 78 | ✅ |
| 6 | Education | High | 76 | ✅ (new) |
| 7 | Commercial Real Estate | High | 74 | ✅ (new) |
| 8 | Manufacturing | Medium | 66 | ✅ (new) |
| 9 | Events | Medium | ~64 | ▶ recommend |
| 10 | Retail / Aviation (candidate expansion) | Low | ~50 | ▶ recommend |

---

## 9. Airtable Records Created (30)

| Table | Created | Items |
|-------|---------|-------|
| Keywords | 3 | Education Security Services · Commercial Real Estate Security · Manufacturing Security Services |
| Competitors | 4 | Securecorp · SECOM Australia · Allied Universal (G4S) · Glad Group |
| AI Visibility | 7 | the 7 buyer/procurement GEO questions (see §6) |
| Opportunities | 14 | 4 service pages + 7 industry pages + 3 GEO targets |
| Agent Performance | 1 | this Director run (Output Score 8, Business Value High) |
| Agent Learning | 1 | GEO generic-recommendations correction (lead-gen focus) |

## 10. Airtable Records Updated (3)

| Table | Record | Change |
|-------|--------|--------|
| Opportunities | Healthcare Security Industry Page | Impact Score 88, Assigned To, Target URL, Notes |
| Opportunities | Mobile Patrol Service Expansion | **linked keyword** (was disconnected), Impact 80, Target URL, Assigned To |
| Content Calendar | Construction Site Security Checklist | **linked Primary Keyword** (was disconnected) |

## 11. Recommended Next Actions (per agent)

1. **Technical SEO Agent** — gather the 5 required inputs in §E (crawl, CWV, GSC, sitemap, affected URLs); only then run the full audit. Backfill Affected URLs on the 3 open issues.
2. **Content Brief Agent** — write briefs for the top money pages in priority order: Security Guards → Government → Healthcare → Construction → Monitoring (Grade A1) → Alarm Response.
3. **Competitor Intelligence Agent** — run full analysis on the 4 new priority competitors; deepen the 4 existing profiles (Strengths/Weaknesses/Authority).
4. **GEO / AI Citation Agent** — probe the 10 AI-visibility questions live; set citation checkboxes + accuracy; convert confirmed gaps into GEO opportunities (apply the recorded learning: tie to lead generation, not generic tips).
5. **Keyword Intelligence Agent** — add city-level service keywords (Local SEO) for the 7 office cities; enrich volume/difficulty where data is available.
6. **SEO Director (next cycle)** — reconcile Silo `Status` vs the live site; convert recommended items #17–20 into Opportunities on approval; re-score readiness.

> **Human review gate:** approve/modify the backlog before any briefs are written or fixes implemented. The system never publishes.
