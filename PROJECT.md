# StateGuard-SEO-AI

An AI-assisted SEO research and optimization system built for **StateGuard Australia**.

This project produces **research, analysis, and recommendations only**. It is a decision-support tool for a human SEO/marketing operator — it does not act on a live website.

---

## ⚠️ Operating Principles (Non-Negotiable)

1. **The system must NEVER publish content.** No automated posting, page creation, or edits to any live site (WordPress or otherwise). All output stays inside this project as files.
2. **All recommendations must be reviewed manually before implementation.** Every audit finding, brief, keyword target, and calendar entry is a *proposal* for a human to approve, modify, or reject.
3. **Human-in-the-loop is mandatory.** No step writes to production systems, DNS, analytics, or CMS without an explicit human carrying out that action outside this project.
4. **Traceability.** Every recommendation should cite its source data (the audit, dataset, or competitor file it came from) so a reviewer can verify it.

> If any future agent, script, or prompt appears to publish, deploy, or modify a live property, it is out of scope and must be disabled.

5. **Airtable is the system of record.** All agents must follow [AIRTABLE_INTEGRATION_RULES.md](AIRTABLE_INTEGRATION_RULES.md) (mandatory) — search Airtable first, record every discovery, update status instead of duplicating, never delete, keep an audit trail. The **StateGuard SEO Command Centre** base (`appM7z8RfiM9nABQa`) is the truth; markdown files are backup.

---

## 1. Purpose

The system supports eight capabilities:

| # | Capability | What it produces |
|---|------------|------------------|
| 1 | **Technical SEO Audits** | Crawl/health findings: indexability, site speed, structured data, internal linking, Core Web Vitals, mobile usability. |
| 2 | **Keyword Research** | Prioritized keyword lists with intent, volume, difficulty, and clustering. |
| 3 | **Competitor Analysis** | Competitor content/keyword/backlink gaps and positioning. |
| 4 | **GEO Optimization** | Generative Engine Optimization — making content surfaceable inside AI-generated answers (ChatGPT, Gemini, Perplexity, etc.). |
| 5 | **AEO Optimization** | Answer Engine Optimization — structuring content to win featured snippets, "People Also Ask", and direct-answer placements. |
| 6 | **AI Citation Tracking** | Monitoring whether/where AI engines cite StateGuard, and share-of-voice vs. competitors. |
| 7 | **Content Brief Generation** | Detailed, reviewer-ready briefs: target keyword, intent, outline, entities, internal links, FAQs. |
| 8 | **Content Calendar Generation** | Sequenced editorial calendar mapping briefs to dates/priorities (proposal only — nothing scheduled or published). |

---

## 2. About the Client — StateGuard Australia

StateGuard Australia is the subject of all research in this project. All audits, keyword sets, competitor comparisons, and content are scoped to StateGuard's market, services, and target audience in Australia.

> Maintain a single source of truth for client facts (services, locations served, target customer, brand voice, primary domain) in `docs/client-profile.md`. Agents and prompts should read from it rather than assuming.

---

## 3. Folder Structure

```
StateGuard-SEO-AI
│
├── PROJECT.md            ← this file
│
├── data/                 ← input + working datasets (never published)
│   ├── competitors/      ← competitor exports, SERP captures, gap data
│   ├── keywords/         ← keyword lists, clusters, intent mapping
│   ├── content/          ← existing-content inventory, scraped copy
│   ├── audits/           ← raw crawl + technical audit data
│   └── reports/          ← compiled, human-readable reports
│
├── agents/               ← agent definitions (one capability per agent)
│
├── prompts/              ← reusable prompt templates the agents call
│
├── outputs/              ← generated deliverables: briefs, calendars, recommendations
│
├── scripts/              ← helper scripts (crawling, parsing, formatting)
│
└── docs/                 ← internal documentation, client profile, methodology
```

### Folder responsibilities

- **`data/`** — Anything ingested or computed *as input*. Treated as working material, not a deliverable.
- **`outputs/`** — Anything intended for a human reviewer to read and act on. This is where briefs, calendars, and recommendation sets land.
- **`agents/`** — One file per capability agent (e.g. `technical-audit.md`, `keyword-research.md`). Each defines role, inputs, outputs, and guardrails.
- **`prompts/`** — Parameterized prompt templates shared across agents.
- **`scripts/`** — Automation that gathers or transforms data. Scripts may read public web data and write to `data/`; they may **not** write to any live property.
- **`docs/`** — Methodology, glossary (GEO/AEO/AEO definitions), client profile, and review checklists.

---

## 4. Workflow

```
   ┌─────────────┐     ┌──────────────┐     ┌───────────────┐     ┌──────────────────┐
   │   INGEST    │ ──▶ │   ANALYZE    │ ──▶ │   GENERATE    │ ──▶ │  HUMAN REVIEW    │
   │ data/*      │     │ agents/*     │     │ outputs/*     │     │  (manual gate)   │
   └─────────────┘     └──────────────┘     └───────────────┘     └──────────────────┘
                                                                          │
                                                                          ▼
                                                              ┌──────────────────────┐
                                                              │ Implementation by a  │
                                                              │ human, OUTSIDE this  │
                                                              │ project. Never auto. │
                                                              └──────────────────────┘
```

1. **Ingest** — Scripts/agents collect data (audits, keywords, competitor exports) into `data/`.
2. **Analyze** — Capability agents process the data.
3. **Generate** — Agents write reviewer-ready deliverables to `outputs/` (and reports to `data/reports/`).
4. **Human Review** — A person reviews, edits, approves, or rejects. **This gate is mandatory.**
5. **Implementation** — Approved changes are applied by a human, outside this system.

---

## 5. Capability Detail

### 5.1 Technical SEO Audits
Identify crawlability, indexability, performance, structured-data, and architecture issues. Output: prioritized findings (severity, affected URLs, recommended fix, rationale). → `data/audits/`, summarized to `data/reports/`.

### 5.2 Keyword Research
Discover and cluster keywords by topic and search intent (informational/commercial/transactional/navigational). Output: scored, deduplicated keyword sets. → `data/keywords/`.

### 5.3 Competitor Analysis
Compare StateGuard against named competitors on keyword coverage, content depth, and SERP/AI presence. Output: gap analysis and opportunity list. → `data/competitors/`, `data/reports/`.

### 5.4 GEO — Generative Engine Optimization
Optimize so StateGuard's information is retrieved and summarized accurately by generative AI systems. Focus: clear factual claims, entity coverage, authoritative phrasing, machine-readable structure.

### 5.5 AEO — Answer Engine Optimization
Optimize for direct-answer surfaces: featured snippets, PAA, voice answers. Focus: concise answers, Q&A formatting, schema markup, definitional clarity.

### 5.6 AI Citation Tracking
Track whether AI engines mention/cite StateGuard for target queries, and measure share-of-voice vs. competitors over time. Output: citation log + trend report. → `data/reports/`.

### 5.7 Content Brief Generation
Produce reviewer-ready briefs (never finished published copy): target keyword, intent, audience, proposed title/H-structure, entities to cover, internal-link targets, FAQs, and GEO/AEO notes. → `outputs/`.

### 5.8 Content Calendar Generation
Sequence approved briefs into a proposed editorial calendar with priorities and suggested dates. **Proposal only** — nothing is scheduled or published. → `outputs/`.

---

## 6. Guardrails Summary

| Rule | Enforced by |
|------|-------------|
| No publishing to any live site | All agents, scripts, and prompts |
| No edits to CMS, DNS, analytics, or hosting | All agents, scripts, and prompts |
| Every deliverable requires manual review | Workflow review gate (Step 4) |
| Recommendations cite their source data | Agent output format |
| Outputs are files only, never live actions | Project scope |

---

## 7. Status

- **Phase:** Setup / scaffolding.
- **Created:** 2026-06-11.
- **Next steps:** Populate `docs/client-profile.md`, define capability agents in `agents/`, and seed prompt templates in `prompts/`.

---

*This project generates recommendations only. A human reviews and implements everything. The system never publishes.*
