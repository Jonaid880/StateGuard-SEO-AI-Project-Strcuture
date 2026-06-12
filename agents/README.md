# Agents

One agent per capability. Each agent is a **research/analysis specialist** that reads inputs, produces a reviewer-ready deliverable, and stops. No agent publishes, edits a live site, or implements anything.

## Mandatory preamble — every agent prompt MUST start with this

```
This agent must:
1. Read Airtable first
2. Update Airtable records
3. Avoid duplicate records
4. Save markdown backup
5. Use StateGuard SEO Command Centre as system of record
```

This 5-point preamble opens every agent definition and every prompt that runs an agent. It is the operational form of [AIRTABLE_INTEGRATION_RULES.md](../AIRTABLE_INTEGRATION_RULES.md). Base of record: **StateGuard SEO Command Centre** — `appM7z8RfiM9nABQa`.

## Shared rules (apply to every agent)

1. **Never publish.** No writes to any live site, CMS, DNS, analytics, or hosting. Output is files only.
2. **Recommendations only.** Every deliverable is a proposal for human review.
3. **Read the client profile first.** `docs/client-profile.md` is the source of truth (brand voice, services, locations, AU English, "Grade A1", phone 1300 723 887).
4. **Cite sources.** Reference the dataset/audit/competitor file each finding came from.
5. **Respect existing technical state.** Don't recommend schema/interlinking that already exists (see profile §5).
6. **Australian English** in all copy and recommendations.
7. **Airtable is the system of record.** Follow [AIRTABLE_INTEGRATION_RULES.md](../AIRTABLE_INTEGRATION_RULES.md) (MANDATORY): search Airtable first, record every discovery, update status instead of duplicating, never delete, keep an audit trail. Markdown is backup; the **StateGuard SEO Command Centre** base (`appM7z8RfiM9nABQa`) is the truth.
8. **Knowledge Base first (content/keyword/GEO/brief agents).** Read the `StateGuard Knowledge Base` table (`tbls1TV2f6wArnoxw`) BEFORE generating recommendations — it is the operational source of truth (services, differentiators, licences, buyer pain points, GEO evidence, "do not duplicate" cautions). Prefer `Approved` records; never contradict them; add new durable facts back to it. See AIRTABLE_INTEGRATION_RULES.md → Rule 0.

## Roster

### Production agents (Airtable-integrated — build order)

These are the operational agents. Each opens with the mandatory preamble, reads/writes its Airtable table, and saves a markdown backup.

| # | File | Agent | Airtable table | Backup |
|---|------|-------|----------------|--------|
| 1 | [stateguard-keyword-intelligence-agent.md](stateguard-keyword-intelligence-agent.md) | Keyword Intelligence (SEO/AEO/GEO) | Keywords | `outputs/keywords/` |
| 2 | [competitor-intelligence-agent.md](competitor-intelligence-agent.md) | Competitor Intelligence | Competitors | `outputs/competitor-analysis/` |
| 3 | [content-brief-agent.md](content-brief-agent.md) | Content Brief | Content Calendar | `outputs/briefs/` |
| 4 | [technical-seo-agent.md](technical-seo-agent.md) | Technical SEO | Technical SEO Issues | `outputs/technical-seo/`, `data/audits/` |
| 5 | [geo-ai-citation-agent.md](geo-ai-citation-agent.md) | GEO / AI Citation | AI Visibility + Opportunities (GEO) | `outputs/geo-ai-citation/` |
| 6 | [seo-director-agent.md](seo-director-agent.md) | SEO Director (orchestrator) | Opportunities (master) + all tables | `outputs/director/` |
| 7 | [offpage-seo-director-agent.md](offpage-seo-director-agent.md) | Off-Page SEO Director (orchestrator) | 6 off-page tables + Opportunities | `outputs/offpage-director/` |

### Off-page intelligence agents (coordinated by the Off-Page SEO Director)
See [docs/OFFPAGE_SEO_ARCHITECTURE.md](../docs/OFFPAGE_SEO_ARCHITECTURE.md). Each opens with the 10-point off-page preamble (incl. never send / never create accounts / never delete).

| # | File | Agent | Airtable table(s) | Backup |
|---|------|-------|-------------------|--------|
| 8 | [backlink-intelligence-agent.md](backlink-intelligence-agent.md) | Backlink Intelligence | Link Opportunities, Competitor Backlinks | `outputs/offpage/backlinks/` |
| 9 | [guest-post-intelligence-agent.md](guest-post-intelligence-agent.md) | Guest Post Intelligence | Guest Post Pipeline | `outputs/offpage/guest-posts/` |
| 10 | [outreach-intelligence-agent.md](outreach-intelligence-agent.md) | Outreach Intelligence (drafts only) | Outreach Campaigns | `outputs/offpage/outreach/` |
| 11 | [digital-pr-intelligence-agent.md](digital-pr-intelligence-agent.md) | Digital PR Intelligence | Digital PR Opportunities | `outputs/offpage/digital-pr/` |
| 12 | [citation-intelligence-agent.md](citation-intelligence-agent.md) | Citation Intelligence | Citation Opportunities | `outputs/offpage/citations/` |

### Capability specs (reference — lighter definitions the production agents draw on)

| File | Capability |
|------|------------|
| [technical-seo-audit.md](technical-seo-audit.md) · [keyword-research.md](keyword-research.md) · [competitor-analysis.md](competitor-analysis.md) · [competitor-intelligence.md](competitor-intelligence.md) | audit / keyword / competitor specs |
| [geo-optimization.md](geo-optimization.md) · [aeo-optimization.md](aeo-optimization.md) · [ai-citation-tracking.md](ai-citation-tracking.md) | GEO / AEO / citation specs |
| [content-brief.md](content-brief.md) · [content-calendar.md](content-calendar.md) | content specs |

## Pipeline

```
                          ┌──────────────────── SEO DIRECTOR (6) ────────────────────┐
                          │  prioritizes Opportunities · coordinates · reports        │
                          └───────────────┬───────────────────────────┬──────────────┘
                                          ▼                           ▼
   keyword-intelligence (1) ─▶ competitor-intelligence (2) ─▶ content-brief (3) ─▶ [content calendar]
                                          │                           ▲
        technical-seo (4) ───────────────┘     geo / ai-citation (5) ─┘
                                                     (inform briefs)
        ↓ every stage records to Airtable, saves a backup, ends at the mandatory HUMAN REVIEW gate ↓
```
