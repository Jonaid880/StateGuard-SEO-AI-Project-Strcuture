# Automation Capability Report

**Author:** SEO Director · **Date:** 2026-06-11
**Scope:** StateGuard-SEO-AI project + StateGuard SEO Command Centre (`appM7z8RfiM9nABQa`)
**Question:** Can this system run automatically, how, and what is the *safest* architecture?

> **Governing principle:** automate **observation, analysis, and recording** only. **Never automate** publishing, sending outreach, creating accounts, or deleting — those stay human-gated (the project's existing guardrails). Automation must never weaken the review gate.

---

## Quick answers

| # | Question | Answer | Note |
|---|----------|--------|------|
| 1 | Can agents currently run automatically? | **No (not today)** | Agents are **markdown definitions**, executed by a Claude session when invoked. Nothing is scheduled yet. |
| 2 | What automation methods are available? | **Several** | Claude Code scheduled routines · Airtable Automations · Windows Task Scheduler · GitHub Actions · external orchestrators (Make/n8n) |
| 3 | Can scheduled jobs be created? | **Yes** | Via Claude Code routines (cloud cron), Windows Task Scheduler, or CI cron. |
| 4 | Can Airtable triggers be used? | **Yes (Airtable-internal only)** | Native Automations: trigger on record created/updated/condition → notify, update field, run script, call webhook. Cannot run our AI agents. |
| 5 | Can local scheduled tasks be used? | **Yes (with caveats)** | Windows Task Scheduler can run headless scripts/Claude Code — but needs the machine on + non-interactive runs. |
| 6 | Can GitHub Actions be used? | **Only after setup** | Project is **not a git repo** today; needs git init + push + runnable agent code (Agent SDK) + secrets. Higher effort/risk. |
| 7 | Can cron jobs be used? | **Yes, by platform** | No native cron on Windows. Use Task Scheduler (local), Claude routines (cloud), or CI cron (GitHub Actions). |

---

## Current State

- **The "agents" are specifications, not programs.** Each `agents/*.md` is a prompt/role definition. They produce output only when a human invokes them in a Claude Code session. There is **no autonomous runtime** — no agent wakes itself, polls, or runs on a clock today.
- **Airtable is reachable via MCP** during a session (read/write/update). Outside a session, nothing touches Airtable.
- **Environment:** Windows 11, local working dir `C:\Users\jonaid\Downloads\StateGuard-SEO-AI`, **not a git repository**, PowerShell + Bash available.
- **Scheduling capability exists but is unused:** Claude Code can create scheduled routines/tasks (cloud cron) — none are configured for this project yet.
- **Guardrails already enforce safety:** every agent is "recommendations/preparation only; never publish/never send." Automating the read/record half is therefore low-risk; the write-to-the-world half is already manual by design.

**Net:** the system is **session-driven** today. It is *automation-ready* (clear agent specs, a structured Airtable backend, markdown backups, status ladders) but nothing is actually scheduled.

---

## Automation Options (assessed)

| Method | What it can do here | Feasibility | Effort | Risk | Verdict |
|--------|---------------------|------------|--------|------|---------|
| **Claude Code scheduled routines** (cloud cron) | Run a chosen agent on a schedule → read base, analyse, write *recommendations* to Airtable + markdown, stop at the review gate | ✅ Native, available now | Low | **Low** (no outward actions) | **★ Core recommendation** |
| **Airtable Automations** (native triggers) | Internal reminders/digests: "competitor reviews due", "citations Needs Fix", "opportunities at-risk", weekly status email; field automation; webhooks | ✅ Available | Low | **Very low** (Airtable-internal) | **★ Use for reminders** |
| **Windows Task Scheduler** (local) | Run headless scripts / Claude Code CLI on a clock | ⚠️ Possible | Medium | Medium (machine must be on; local secrets) | Optional |
| **GitHub Actions** (CI cron) | Headless agent runs in the cloud on cron | ⚠️ Needs git repo + Agent-SDK code + secrets | High | Medium (secrets in CI; runnable code required) | Later, if scaling |
| **Native cron** | n/a on Windows | ❌ Not native | — | — | Use Task Scheduler / cloud cron instead |
| **External orchestrators** (Make / n8n / Zapier) | Connect Airtable ↔ APIs ↔ notifications on a schedule | ✅ Possible | Medium | Medium (3rd-party data access) | Optional for glue |
| **Claude Agent SDK** (custom code) | Turn the markdown agents into runnable programs for any scheduler | ✅ Possible | High | Medium | Foundation for GH Actions/Task Scheduler |

**Key constraint:** GitHub Actions / Task Scheduler / Agent SDK all require the agents to become **runnable code** (today they're markdown) and to hold **API secrets** (Anthropic + Airtable PAT). That's more surface area and more risk. Claude Code routines avoid both — they run the existing markdown agents in-session on a schedule.

---

## Recommended Architecture (safest)

A **two-tier, human-gated** design that automates only the safe half:

```
┌───────────────────────────── SAFE TO AUTOMATE ─────────────────────────────┐
│  TIER 0 — Airtable Automations (Airtable-internal)                          │
│    • Reminders: competitor reviews due · citations Needs Fix · at-risk opps │
│    • Weekly status digest email · field tidy-ups                            │
│    • NO AI, NO external action                                              │
│                                                                            │
│  TIER 1 — Claude Code Scheduled Routines (cloud cron)  ★ core              │
│    • Weekly: SEO Director read+report → outputs/director/                   │
│    • Weekly: Off-Page Director plan → outputs/offpage-director/             │
│    • Monthly: Metrics Snapshots rollup (Airtable-computed metrics)          │
│    • Monthly: GEO/AI-Citation probe log                                     │
│    → each WRITES RECOMMENDATIONS to Airtable + markdown, then STOPS         │
└────────────────────────────────────────────────────────────────────────────┘
                                   │  (every routine ends here)
                                   ▼
        ┌──────────────────── HUMAN REVIEW GATE (unchanged) ────────────────┐
        │  approve · publish · send outreach · create accounts · go live    │
        │  ✋ NEVER automated — always a person                              │
        └────────────────────────────────────────────────────────────────────┘
```

**Why this is safest:**
- It automates **read → analyse → record** (zero outward risk) and leaves **every outward/destructive action manual** — exactly matching the project guardrails.
- It uses **native capabilities** (Claude routines + Airtable Automations), so **no new secrets, no new code, no new third parties**.
- It's **reversible and observable** — routines write to Airtable (audit-trailed) + markdown backups; you can pause/delete a routine instantly.
- **Defer GitHub Actions / Task Scheduler / Agent SDK** until there's a proven need for headless scale — they add code + secrets + infra risk for little extra benefit right now.

**Hard automation boundary (encode in every routine):** a routine may *create/update Airtable records and write markdown*. It may **never** call a live CMS/site, send an email, submit a form, create an account, or delete a record. If a task needs any of those, it stops and flags for a human.

---

## Implementation Steps

### Phase 1 — Tier 0 reminders (today, zero risk)
1. In Airtable → **Automations**, add:
   - *Competitor reviews due:* when `Competitors.Last Reviewed` is >30 days (or empty) → send digest.
   - *Citations to fix:* when `Citation Opportunities.Status = Needs Fix` → notify.
   - *At-risk roadmap:* weekly summary of `Opportunities` by `Roadmap Quarter` + Status.
2. Add a **weekly status digest** automation (email/Slack) summarising open items.

### Phase 2 — Tier 1 scheduled agent routines (this week)
3. Create a **Claude Code scheduled routine** for the **weekly SEO Director read + report** (reads all tables, writes `outputs/director/weekly-<date>.md`, updates Opportunities priorities — recommendations only).
4. Add a **weekly Off-Page Director routine** → `outputs/offpage-director/weekly/`.
5. Add a **monthly Metrics Snapshots rollup** routine (computes the Airtable-internal metrics — links won, leads, % complete — and writes dated snapshot rows; external metrics still entered by a human per the baseline guide).
6. Each routine's prompt must restate the **hard automation boundary** (record-only; stop at the human gate).

### Phase 3 — verify & tune (ongoing)
7. Review the first few automated outputs; log quality to **Agent Performance**, corrections to **Agent Learning**.
8. Keep all approvals manual; confirm no routine ever attempts an outward action.

### Phase 4 — optional headless scale (only if needed, later)
9. If/when true headless runs are required: `git init` + push to GitHub, build the agents as **Agent SDK** code, store Anthropic + Airtable secrets in the CI vault, and run **GitHub Actions on a schedule** — still **read/analyse/record only**, with the same hard boundary. (Windows Task Scheduler is the local equivalent if cloud CI isn't wanted.)

---

## Recommendation
Adopt **Tier 0 (Airtable reminders) + Tier 1 (Claude Code scheduled routines)** now. It delivers real automation — weekly/monthly agent runs and reminders — **without new code, secrets, or third parties**, and it **cannot** breach the never-publish/never-send guardrails. Treat GitHub Actions/cron/Task Scheduler as a *later* option for scale, not a starting point.

> I can set up the first safe routine (e.g., the weekly SEO Director read+report) on request — it would run read-only/recommend-only and write to Airtable + `outputs/`.
