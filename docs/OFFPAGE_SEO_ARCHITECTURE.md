# Off-Page SEO Architecture

**Purpose:** A complete Off-Page SEO Operating System for StateGuard — backlinks, guest posts, outreach, digital PR, and citations — run by a coordinated set of agents on top of the StateGuard SEO Command Centre.

**Last updated:** 2026-06-11 · Owner: Off-Page Director (reports to [SEO Director](../agents/seo-director-agent.md))

---

## Mandatory rules (every off-page agent)

```
This agent must:
1. Read Airtable first
2. Update Airtable records
3. Avoid duplicate records
4. Save markdown backup
5. Use StateGuard SEO Command Centre as system of record
```

Plus the project guardrails and [AIRTABLE_INTEGRATION_RULES.md](../AIRTABLE_INTEGRATION_RULES.md) (incl. **Rule 0 — Knowledge Base first**):

- **Recommendations & preparation only.** Off-page work is **outward-facing** — the system **never sends an email, submits a form, posts a link, or contacts anyone**. It researches prospects, drafts outreach, and tracks status; **a human reviews and sends every outreach**.
- **Authority serves leads.** Prioritise links, mentions, and citations that build trust for the **money pages** (priority services + industries) and **AI citations** (GEO) — not vanity volume. Authority is the secondary goal in service of the primary goal: qualified leads.
- **Quality over quantity.** Relevant, Australian, reputable sources only. No link schemes, PBNs, paid-link manipulation, or spam. Never compromise the domain.
- **System of record:** base **StateGuard SEO Command Centre** (`appM7z8RfiM9nABQa`). Markdown is backup.

---

## Agent hierarchy

```
                         ┌─────────────────────────────┐
                         │     SEO DIRECTOR (main)      │  ← off-page rolls up here
                         └──────────────┬──────────────┘
                                        ▼
                         ┌─────────────────────────────┐
                         │     OFF-PAGE DIRECTOR        │  prioritise · assign · report
                         └──┬───────┬───────┬───────┬───┘
            ┌───────────────┘       │       │       └───────────────┐
            ▼               ▼       ▼       ▼                       ▼
   ┌───────────────┐ ┌────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
   │  Backlink     │ │ Guest Post │ │  Digital PR  │ │   Citation   │ │   Outreach   │
   │ Intelligence  │ │Intelligence│ │ Intelligence │ │ Intelligence │ │ Intelligence │
   └──────┬────────┘ └─────┬──────┘ └──────┬───────┘ └──────────────┘ └──────▲───────┘
          │                │               │                                  │
          └────────────────┴───────────────┴────────► prospects feed ─────────┘
                         (Backlink / Guest Post / Digital PR surface targets;
                          Outreach manages contact + status for all of them)
```

- **Backlink, Guest Post, Digital PR** are *discovery* agents — they surface prospects.
- **Outreach** is the *shared execution-prep* agent — it owns contact records, drafts, and status for prospects the other three surface.
- **Citation** is *self-contained* — directories/NAP don't need outreach sequences.
- **Off-Page Director** prioritises across all five and reports up to the main SEO Director.

---

## Airtable tables used

### Existing tables
| Table | ID | Off-page use |
|-------|----|--------------|
| Opportunities | `tblj8ImoiXXOjc2Xm` | Master backlog — off-page items use Category **Link Building** / **Local SEO** / **GEO**; Off-Page Director assigns + scores |
| Competitors | `tblmMvGA5EId7BzdP` | Backlink-gap source (their link profiles) |
| AI Visibility | `tblwxO8THa03tpWHz` | Digital PR / citations that influence AI answers |
| StateGuard Knowledge Base | `tbls1TV2f6wArnoxw` | Source of truth (licences, ASIAL, differentiators) for pitches/citations |
| Agent Performance / Agent Learning | `tbl2HLbCyxFTNRXz0` / `tblQcWkmokwfhzmLg` | Scorecards + self-improvement |

### Off-page tables (CREATED 2026-06-11)
| Table | ID | Owner agent | Holds |
|-------|----|-------------|-------|
| **Link Opportunities** | `tbls5HJYFizVeLIrt` | Backlink Intelligence | Prospect domains, type, authority, priority, anchor, status; **Target Page → Silo Map** |
| **Competitor Backlinks** | `tblUoMymdymyw3A9Z` | Backlink Intelligence | Competitor links, replicability, opportunity score; **Competitor → Competitors** |
| **Guest Post Pipeline** | `tblKNJ8lUadwMHbSB` | Guest Post Intelligence | Topic, anchor, brief/writing/publication status; **Target Page → Silo Map**, **Link Opportunity → Link Opportunities** |
| **Outreach Campaigns** | `tblmSEOLLWhCLSYn2` | Outreach Intelligence | Contact, stage, response, outcome; **Link Opportunity → Link Opportunities**. Drafts only — human sends |
| **Digital PR Opportunities** | `tblXWELOOfh0xMR8i` | Digital PR Intelligence | Angle, outlet, industry, priority, status; **Target Service → Silo Map** |
| **Citation Opportunities** | `tblvYbZDlBC9XFJ2l` | Citation Intelligence | Directory, authority, NAP/country, status; **Target Service → Silo Map** |

> Built with relationships into the existing **Competitors** (`tblmMvGA5EId7BzdP`) and **Service & Industry Silo Map** (`tblMZKYMUGOYH3UbX`) tables, plus internal Link-Opportunity ↔ Guest Post / Outreach links. Autonumber IDs can be added manually (1 click) like the other tables. Off-page items may still be promoted to **Opportunities** rows tagged `Link Building`/`Local SEO` for the Director backlog.

#### Proposed schemas (summary)
- **Link Prospects:** Domain (primary) · Prospect Type (Resource page / Competitor backlink / Industry directory / Partner / Editorial) · Domain Authority (number) · Relevance (High/Med/Low) · Target Money Page (link→Opportunities/Silo) · Status (Identified → Qualified → Outreach → Won → Rejected) · Source · Notes
- **Guest Post Opportunities:** Publication (primary) · URL · Niche (Security/Facilities/Property/Construction/Government) · Domain Authority · Accepts Guest Posts (checkbox) · Guidelines URL · Proposed Topic · Status (Identified → Pitched → Accepted → Published → Declined) · Notes
- **Digital PR Opportunities:** Angle/Story (primary) · Outlet/Journalist · Type (Press release / Expert comment / Data study / Award / Commentary) · Deadline (date) · Relevance · Status (Identified → Drafted → Pitched → Landed → Passed) · Linked Money Page · Notes
- **Outreach Log:** Contact/Org (primary) · Email/Form (text — never auto-sent) · Linked Prospect (link→Link Prospects/Guest Post/Digital PR) · Sequence Stage (Draft → Ready for human → Sent → Replied → Won → Closed) · Draft Message · Owner (human) · Last Touch (date) · Notes
- **Citations / Directories:** Directory (primary) · URL · Category (General / Security industry / Local / Government supplier) · NAP Consistent (checkbox) · Status (Identified → Submitted → Live → Needs fix) · Office/Location · Notes

---

## The six agents

### 1. Off-Page Director Agent
- **Role:** Orchestrate off-page; prioritise the off-page backlog by authority value to money pages + AI citations; assign work to the 5 agents; report up to the main SEO Director.
- **Inputs:** all off-page tables, Opportunities (Link Building/Local SEO/GEO), Competitors, AI Visibility, Knowledge Base.
- **Outputs:** prioritised off-page backlog (Opportunities), weekly + monthly off-page reports → `outputs/offpage/`.
- **Airtable:** Opportunities (master) + reads all off-page tables.
- **Reports to:** main SEO Director.

### 2. Backlink Intelligence Agent
- **Role:** Analyse StateGuard's + competitors' backlink profiles; find link gaps and high-value, relevant prospects; flag toxic links for human review.
- **Inputs:** backlink exports (Ahrefs/Semrush/GSC links) provided by the user; Competitors table; Knowledge Base.
- **Outputs:** backlink gap analysis + qualified prospect list → **Link Prospects** table + `outputs/offpage/backlinks/`.
- **Airtable:** Link Prospects (write), Competitors (read).

### 3. Guest Post Intelligence Agent
- **Role:** Find guest-post opportunities on AU security, facilities, property, construction, and government-supplier publications; assess authority + relevance; propose topics tied to money pages; track pitch status.
- **Inputs:** target niches (from Strategy + Knowledge Base), publication research, editorial guidelines.
- **Outputs:** ranked guest-post opportunity list + proposed topics → **Guest Post Opportunities** table + `outputs/offpage/guest-posts/`.
- **Airtable:** Guest Post Opportunities (write), Knowledge Base (read for topic angles).

### 4. Outreach Intelligence Agent
- **Role:** Prepare and track outreach for prospects surfaced by Backlink/Guest Post/Digital PR. **Drafts** personalised messages and sequences; **never sends** — every message is queued "Ready for human".
- **Inputs:** prospects from the three discovery agents; Knowledge Base (accurate facts for personalisation).
- **Outputs:** outreach drafts + campaign status → **Outreach Log** table + `outputs/offpage/outreach/`.
- **Airtable:** Outreach Log (write); links to Link Prospects / Guest Post / Digital PR records.
- **Guardrail:** human sends; agent only prepares + tracks.

### 5. Digital PR Intelligence Agent
- **Role:** Identify PR angles, data-story ideas, expert-comment opportunities (HARO-style), industry awards, and journalists/outlets in AU security/facilities/government; tie each to authority + AI-citation goals.
- **Inputs:** Knowledge Base (StateGuard facts, differentiators, licences), AI Visibility (citation gaps), industry news.
- **Outputs:** PR opportunity pipeline + draft angles → **Digital PR Opportunities** table + `outputs/offpage/digital-pr/`.
- **Airtable:** Digital PR Opportunities (write), AI Visibility + Knowledge Base (read).

### 6. Citation Intelligence Agent
- **Role:** Manage local citations and directory listings; audit NAP (name/address/phone) consistency across the 7 offices; find security-industry + government-supplier directories; track claimed/verified status.
- **Inputs:** the 7 verified offices + canonical phone **1300 723 887** (Knowledge Base); directory research.
- **Outputs:** citation/NAP audit + submission tracker → **Citations / Directories** table + `outputs/offpage/citations/`.
- **Airtable:** Citations / Directories (write), Knowledge Base (read for authoritative NAP).

---

## Reporting structure

```
Each intelligence agent ─► writes records to its table + markdown backup in outputs/offpage/<agent>/
                          │
Off-Page Director ────────┴─► weekly off-page report  → outputs/offpage/weekly/<date>.md
                            └─► monthly off-page report → outputs/offpage/monthly/<month>.md
                                 │
                                 └─► rolls into the main SEO Director report (outputs/director/)
```

- **Backups:** `outputs/offpage/` with one sub-folder per agent (`backlinks/`, `guest-posts/`, `outreach/`, `digital-pr/`, `citations/`) plus `weekly/` and `monthly/`.
- **Audit trail** on every record: Date · Source · Agent · Reason (Rule 5).
- **Status, never delete** (Rule 4): rejected prospects → a closing status with a reason, not deletion.

---

## Weekly workflow

| Day | Agent | Action |
|-----|-------|--------|
| Mon | Off-Page Director | Read base; review last week's status; set this week's off-page priorities (money-page + AI-citation weighted) |
| Tue | Backlink + Guest Post | Discover & qualify new prospects → write to tables (dedup first) |
| Wed | Digital PR | Scan for angles/queries/awards; draft 1–2 PR angles |
| Thu | Outreach | Prepare/personalise drafts for qualified prospects → "Ready for human"; **human reviews & sends** |
| Fri | Citation | Audit/advance directory + NAP tasks; verify any newly-live citations |
| Fri | Off-Page Director | Compile **weekly off-page report**; advance/clean statuses; flag items for human review |

> Throughout: every agent reads Airtable first, avoids duplicates, updates status (not new rows), and saves its backup. No message is ever sent by the system.

## Monthly workflow

| Week | Focus |
|------|-------|
| Week 1 | **Backlink profile review** — StateGuard vs the 8 competitors; refresh gap analysis; toxic-link check (flag for human disavow decision) |
| Week 2 | **Guest post + Digital PR pipeline** — secure/advance placements; convert landed coverage into authority evidence (add to Knowledge Base) |
| Week 3 | **Citation + NAP audit** — full consistency sweep across 7 offices + directories; fix-list for human action |
| Week 4 | **Off-Page Director monthly report** — wins (links/mentions/citations), authority trend, AI-citation movement, share-of-voice vs competitors, next-month plan → rolls into main SEO Director cycle |

### Monthly KPIs (authority in service of leads)
- New **relevant** referring domains won (quality-weighted, not raw count)
- Guest posts / PR placements landed → linking to money pages
- Citation/NAP consistency score across 7 offices
- Movement in **AI citations** + share-of-voice vs Wilson/MSS/Certis/SNP/Securecorp/SECOM/Allied Universal/Glad
- Authority lift correlated to money-page rankings + enquiries

> **Traffic from links is not the KPI.** The KPI is authority that lifts money-page rankings, wins AI citations, and supports tender credibility — i.e. leads.

---

## Setup checklist (to activate this system)

1. **Approve & create** the 5 proposed off-page tables (or run off-page via Opportunities `Link Building`/`Local SEO` tags in the interim).
2. **Author the 6 agent definitions** in `agents/` (mirroring the on-page production agents, each opening with the mandatory preamble).
3. **Create** `outputs/offpage/` sub-folders.
4. **Provide data:** backlink export (StateGuard + competitors) to seed the Backlink agent; directory list to seed Citations.
5. **Off-Page Director** runs its first audit, seeds the backlog, and reports up to the main SEO Director.

> Everything here is recommendations + preparation. A human reviews and performs all outward actions (sending outreach, submitting listings, disavowing links). The system never contacts anyone and never publishes.
