# Client Profile — StateGuard Australia

> Single source of truth for client facts. Agents and prompts should read from this file rather than assuming. Keep it current; cite it in deliverables.

**Last updated:** 2026-06-11

---

## 1. Identity

| Field | Value |
|-------|-------|
| Business name | StateGuard Australia |
| Primary domain | https://stateguard.com.au |
| Industry | Integrated / electronic security services |
| Market | Australia (national) |
| ABN | 67 114 270 352 |
| Phone (canonical) | **1300 723 887** — any other number on-site is a bug |
| HQ email | info@stateguard.com.au |

> **Note:** A second domain, `proforcemonitoring.com.au`, exists on the same hosting account but is out of scope unless explicitly stated.

---

## 2. Brand Voice & Terminology

- **Tagline:** *Smart. Safe. Secure.*
- **Platform terms (use these):** Mission Talk, Assist App, NFC patrol verification, "7 Phases".
- **Retired voice:** the legacy "bespoke solution" phrasing is being phased out — do not use it.
- **Spelling:** **Australian English** throughout — centre, recognise, organise, defence, **licence** (noun), colour, etc.
- **Industry term accuracy:** use **"Grade A1"** (per ASIAL / AS/NZS 2201.2:2022), never "A1 Grade".

---

## 3. Services (high level)

StateGuard provides integrated security across monitoring, guarding, and electronic systems. Representative service clusters:

- **Grade A1 Monitoring** (alarm monitoring, CCTV monitoring, remote CCTV monitoring, CCTV installation, AI video analytics, duress/medical alarms)
- **Manned services** — security guards, mobile patrols, concierge, NOC operations
- **Electronic systems** — CCTV camera systems, access control, solar/pole cameras, AI video analytics
- **Industry verticals** — critical infrastructure, power stations, commercial real estate, education, and more

> Maintain the authoritative service list against the live site's Solutions / Services / Industries hubs.

---

## 4. Locations

**Physical offices (7)** — these carry LocalBusiness/Place schema on-site:

| City | Address |
|------|---------|
| Melbourne (HQ) | Brunswick VIC 3056 |
| Sydney | 44 Market St, Sydney NSW 2000 |
| Perth | 125 St Georges Tce, Perth WA 6000 |
| Hobart | 111 Macquarie St, Hobart TAS 7000 |
| Canberra | 2 Phillip Law St, Canberra ACT 2601 |
| Adelaide | 91 King William St, Adelaide SA 5000 |
| Brisbane | 32 Turbot St, Brisbane QLD 4000 |

**Service-area pages (no physical office)** — intentionally **without** LocalBusiness schema (fabricating an address would breach Google guidelines): melbourne-cbd, sydney-cbd, parramatta, north-sydney, western-sydney, geelong, gold-coast, pilbara, goldfields, security-services-darwin.

---

## 5. Technical Context (for audits)

- **CMS:** WordPress (WP core 7.0, PHP 8.2.x).
- **Theme:** bespoke custom theme `stateguard` (hand-coded PHP templates). **Not Elementor.**
- **Content storage:** ACF flexible-content/repeater meta. Homepage `post_content` is empty — everything renders from ACF. Internal links live in ACF URL subfields.
- **SEO/schema:** Yoast SEO Premium + Yoast Local SEO. Schema is **comprehensive** (Organization, WebSite+SearchAction, Service OfferCatalog, EducationalOccupationalCredential licences, FAQPage on homepage, LocalBusiness on capital-city pages, Breadcrumb). **Do not recommend adding schema that already exists** — duplicates get flagged.
- **Indexing:** robots.txt allows Google-Extended; blog_public=1; valid sitemap → AI-citation ready.
- **URL convention:** nested (`/about-us/...`, `/solutions/...`).
- **Interlinking:** Master Interlinking Tree implemented — every page carries a 3/6/9 link block, hub-and-spoke, zero orphans.
- **Environment caution:** no staging env; tight ~15GB disk. Do **not** enable the LiteSpeed Crawler (caused blank-page issues). This profile is read context for **audits/recommendations only — this project never edits the live site.**

---

## 6. Strategic Phase

The broader StateGuard initiative is two-phase: **(1) technical-SEO remediation** (largely complete) → **(2) a 53-page content launch** on the repaired foundation. This SEO-AI project supports phase 2 with keyword research, competitor analysis, GEO/AEO optimization, citation tracking, briefs, and a content calendar — all **recommendations only**.

---

## 7. Competitors

> TODO — populate after the first competitor-analysis pass. Track each in `data/competitors/` with domain, positioning, and overlap notes.

---

*Facts here are sourced from prior verified work on stateguard.com.au. Verify against the live site before asserting anything as current — this project does not have live access by default and makes recommendations only.*
