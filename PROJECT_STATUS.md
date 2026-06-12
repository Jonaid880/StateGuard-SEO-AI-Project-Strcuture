# StateGuard SEO-AI — Project Status & Handoff

**Snapshot date:** 2026-06-11 · Use this to resume on any machine.

## What this is
An AI-assisted SEO operating system for **StateGuard Australia** — research, analysis, planning and tracking only. **Never publishes, never sends outreach, never creates accounts, never deletes.** Everything stops at human review / `Ready For Submission`.

## System of record — Airtable
- **Base:** StateGuard SEO Command Centre — `appM7z8RfiM9nABQa` — https://airtable.com/appM7z8RfiM9nABQa
- **Tables (IDs):** Opportunities `tblj8ImoiXXOjc2Xm` · Keywords `tblIyRYsRBCFHwhv1` · Competitors `tblmMvGA5EId7BzdP` · Content Calendar `tbl4n94v668Eehvfc` · AI Visibility `tblwxO8THa03tpWHz` · Technical SEO Issues `tblCGcz1Fl3Z2Uz6f` · Service & Industry Silo Map `tblMZKYMUGOYH3UbX` · Knowledge Base `tbls1TV2f6wArnoxw` · Agent Performance `tbl2HLbCyxFTNRXz0` · Agent Learning `tblQcWkmokwfhzmLg` · Leads `tbl9LtfBT57qJRu0V` · Metrics Snapshots `tbly27DXqeefAozPW` · Execution Logs `tblbgkOGEb0GtSarA` · Link Opportunities `tbls5HJYFizVeLIrt` · Competitor Backlinks `tblUoMymdymyw3A9Z` · Guest Post Pipeline `tblKNJ8lUadwMHbSB` · Outreach Campaigns `tblmSEOLLWhCLSYn2` · Digital PR Opportunities `tblXWELOOfh0xMR8i` · Citation Opportunities `tblvYbZDlBC9XFJ2l`

## What's built
- **Folders:** `data/ agents/ prompts/ outputs/ scripts/ docs/`
- **13 agents** (`agents/`): on-page (keyword, competitor, content-brief, technical, geo/ai-citation, **SEO Director**) + off-page (**Off-Page Director** + backlink, guest-post, outreach, digital-pr, citation). Each carries the mandatory preamble + Submission Layer.
- **8 prompt templates** (`prompts/`).
- **Governance/strategy docs** (`docs/` + root): PROJECT.md, STATEGUARD_PROFILE.md, AIRTABLE_INTEGRATION_RULES.md, client-profile, STATEGUARD_SEO_STRATEGY.md, OFFPAGE_SEO_ARCHITECTURE.md, AUTOMATION_CONTROLLER.md, SUBMISSION_AUTOMATION_LAYER.md, airtable-command-centre.md.
- **Reports** (`outputs/`): director audits, 12-month roadmap, dashboard specs, baseline guides + **real operational baseline**, automation report; off-page audit, Security Guards 30-day plan + PR strategy; **Security Guards content brief (94/100)**; **2 submission packages at Ready For Submission** (FMA guest post, ASIAL directory).

## Where we are
System fully built + populated; running in test mode. **Pending:** Airtable views + Interface dashboards (UI build); external baseline (traffic/rankings/DR/AI citations); activate automation. Connected SEO data MCPs (GSC / Ahrefs-style / SE-Ranking-style / AI brand-visibility) can now supply the external baseline.

## Resume on the OTHER PC (the always-on bot machine)
1. **Install Git**, then `git clone <your-private-repo-url>` (this repo).
2. **Install Claude Code** + sign in with the **same account**.
3. **Reconnect MCPs:** Airtable (→ base `appM7z8RfiM9nABQa`) + the SEO data tools.
4. **Open Claude Code in this folder** — the docs/agents/this file give full context (chat history doesn't transfer; it isn't needed).
5. **Automation:** set up Windows Task Scheduler per `docs/AUTOMATION_CONTROLLER.md` (Mon–Fri + monthly). All runs are read/record-only and stop at `Ready For Submission`.
6. **Keep in sync:** `git pull` before work, `git push` after, on either PC.

## Guardrails (always)
Recommendations/preparation only · never publish/send/create-accounts/delete · real data only (no invented metrics) · Airtable = source of record, markdown = backup · Knowledge Base first.

## Next actions
Pull the **real external baseline** (DR, referring domains, organic keywords/positions, AI citations) into Metrics Snapshots · build views + dashboards · next Q1 brief (Government, Impact 90) · activate scheduled automation.
