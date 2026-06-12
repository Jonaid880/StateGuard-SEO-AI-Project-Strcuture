# Automation Controller

**Purpose:** Run StateGuard SEO agents on a fixed schedule, with every run reading Airtable first, recording its work, saving a markdown report, logging execution + failures, and updating Metrics Snapshots.
**Last updated:** 2026-06-11 · Owner: SEO Director

> ## ⛔ Hard automation boundary (encode in every run)
> A scheduled run may **read Airtable, update/create Airtable records, write markdown files, and append to Metrics Snapshots + Execution Logs**. It may **NEVER** publish to a live site, send an email/outreach, submit a form, create an account, or delete a record. Anything outward stops and is flagged for a human. *(This is the same boundary as [automation-capability-report.md](../outputs/director/automation-capability-report.md).)*

---

## 1. Schedule

| When (weekly, AEST/AEDT) | Agent / Job | Output |
|--------------------------|-------------|--------|
| **Monday** | Off-Page Director | `outputs/offpage-director/weekly/<date>.md` |
| **Tuesday** | Backlink Intelligence | `outputs/offpage/backlinks/<date>.md` |
| **Wednesday** | Competitor Intelligence | `outputs/competitor-analysis/<date>.md` |
| **Thursday** | Citation Intelligence | `outputs/offpage/citations/<date>.md` |
| **Friday** | **Weekly Executive Report** | `outputs/director/weekly/<date>.md` |
| **Monthly** (1st business day) | **Monthly SEO Report** | `outputs/director/monthly/<month>.md` |

Suggested time: **09:00 Australia/Melbourne** each run.

---

## 2. Per-run protocol (every job follows these 6 steps)
1. **Read Airtable first** — load the agent's tables + Knowledge Base (Rule 1 / Rule 0).
2. **Update Airtable** — create/update records per the agent's mandate (dedup; never delete).
3. **Save markdown report** — to the agent's `outputs/` folder (backup; Rule 6).
4. **Log execution** — append a row to **Execution Logs** (`tblbgkOGEb0GtSarA`): Date, Agent, Status=`Success`, Duration, Records Updated, Notes.
5. **Log failures** — on any error, append an Execution Logs row with Status=`Failed` (or `Partial`) and the error text in **Errors**; the wrapper logs a `Failed` row even if the agent process itself crashes.
6. **Update Metrics Snapshots** — append the run's relevant Airtable-rollup metrics as new dated rows (e.g. Links Won, Citations Live, Opportunities counts) — internal rollups only; external metrics stay human-captured.

---

## 3. Execution Logs table (created)
**`Execution Logs`** — `tblbgkOGEb0GtSarA`

| Field | Type | Use |
|-------|------|-----|
| Date | dateTime (primary, Australia/Melbourne) | run timestamp |
| Agent | single select | which agent/job ran |
| Status | single select | Success / Partial / Failed / Skipped |
| Duration | duration (h:mm:ss) | run time |
| Records Updated | number | Airtable records created/updated |
| Errors | long text | failure messages (empty on success) |
| Notes | long text | summary / output path |

> Append-only — never delete a log row (Rule 4). Build a "Failures" view (filter Status = Failed/Partial) for monitoring.

---

## 4. Controller orchestration (logic)

```
controller(today):
  job = schedule[today.weekday]          # Mon→Off-Page Director, … Fri→Weekly Report
  if today.is_first_business_day: job = "Monthly SEO Report"
  if not job: log(Skipped); return

  start = now()
  try:
    result = run_agent(job)               # headless Claude run, hard boundary enforced
    log_execution(date=start, agent=job, status="Success",
                  duration=now()-start, records=result.records_updated,
                  notes=result.report_path)
    update_metrics_snapshots(result.rollups)   # internal counts only
  except Error as e:
    log_execution(date=start, agent=job, status="Failed",
                  duration=now()-start, errors=str(e))
    alert_human(job, e)                    # email/Slack; do NOT retry destructively
```

`run_agent(job)` = invoke Claude Code headlessly with a prompt that loads the agent definition and runs it under the hard boundary. Example command:

```bash
claude -p "Act as the {AGENT}. Read agents/{file}.md and run it for StateGuard.
Follow AIRTABLE_INTEGRATION_RULES.md (Knowledge Base first, Airtable first, update-not-duplicate,
never delete, audit trail). Save the markdown report to {output_path}. Append an Execution Logs
row and the run's internal rollups to Metrics Snapshots. HARD BOUNDARY: never publish, send,
submit, create accounts, or delete — stop and flag for a human if any step would."
```

> **Prerequisite:** the markdown agents must be *runnable* — via the **Claude Code CLI** (`claude -p`, non-interactive) with a **scoped permission profile** (allow: Airtable MCP + file write under the project; deny: shell that could act outward), **or** built as **Claude Agent SDK** code. Provide secrets (`ANTHROPIC_API_KEY`, Airtable PAT) via the OS/secret store, **never in the repo**.

---

## 5. Implementation

### Option A — Windows Task Scheduler (local)
Save a runner (e.g. `scripts/run-agent.ps1`) that runs one agent and logs, then register one task per weekday + a monthly task.

`scripts/run-agent.ps1` (sketch):
```powershell
param([string]$Agent, [string]$File, [string]$Out)
$start = Get-Date
try {
  claude -p "Act as $Agent. Read agents/$File and run it... (full prompt, hard boundary)" |
    Out-File $Out -Encoding utf8
  $status = "Success"; $err = ""
} catch { $status = "Failed"; $err = $_.Exception.Message }
$dur = [int]((Get-Date) - $start).TotalSeconds
# Append to Execution Logs via Airtable API (PAT in $env:AIRTABLE_PAT)
Invoke-RestMethod -Method Post `
  -Uri "https://api.airtable.com/v0/appM7z8RfiM9nABQa/tblbgkOGEb0GtSarA" `
  -Headers @{ Authorization = "Bearer $env:AIRTABLE_PAT"; "Content-Type"="application/json" } `
  -Body (@{ records = @(@{ fields = @{
      Date = (Get-Date).ToString("s"); Agent = $Agent; Status = $status;
      Duration = $dur; Errors = $err; Notes = $Out } }) } | ConvertTo-Json -Depth 6)
```

Register the schedule (run as your user; machine must be on at run time):
```powershell
$act = { param($a,$f,$o) New-ScheduledTaskAction -Execute "powershell.exe" `
  -Argument "-File C:\Users\jonaid\Downloads\StateGuard-SEO-AI\scripts\run-agent.ps1 -Agent '$a' -File '$f' -Out '$o'" }

Register-ScheduledTask -TaskName "SG Off-Page Director" -Action (& $act "Off-Page Director" "offpage-seo-director-agent.md" "outputs\offpage-director\weekly\$(Get-Date -f yyyy-MM-dd).md") `
  -Trigger (New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9am)
# repeat: Tuesday=Backlink, Wednesday=Competitor, Thursday=Citation, Friday=Weekly Report
Register-ScheduledTask -TaskName "SG Monthly SEO Report" -Action (& $act "Monthly SEO Report" "seo-director-agent.md" "outputs\director\monthly\$(Get-Date -f yyyy-MM).md") `
  -Trigger (New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9am)   # gate to 1st week in the script
```
- **Secrets:** set `ANTHROPIC_API_KEY` + `AIRTABLE_PAT` as **user environment variables** (not in the script).
- **Pros:** no cloud, secrets stay local, instant disable (`Disable-ScheduledTask`). **Cons:** machine must be on; less auditable.

### Option B — GitHub Actions (cloud cron)
Requires: `git init` + push to a **private** repo + runnable agents (Agent SDK or CLI) + secrets in **GitHub Encrypted Secrets**.

`.github/workflows/seo-automation.yml`:
```yaml
name: StateGuard SEO Automation
on:
  schedule:
    - cron: '0 23 * * 0'   # Mon 09:00 AEST  (UTC = AEST-10; adjust for AEDT)
    - cron: '0 23 * * 1'   # Tue
    - cron: '0 23 * * 2'   # Wed
    - cron: '0 23 * * 3'   # Thu
    - cron: '0 23 * * 4'   # Fri (weekly report)
    - cron: '0 23 1 * *'   # Monthly
  workflow_dispatch: {}     # manual run button
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: node scripts/run-agent.js        # maps weekday → agent, enforces hard boundary
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          AIRTABLE_PAT: ${{ secrets.AIRTABLE_PAT }}
      - run: |                                 # commit the markdown reports back
          git config user.name "seo-bot"; git add outputs/; git commit -m "automated run" || true; git push
```
- **Cron is UTC** — convert from Melbourne (AEST = UTC+10, AEDT = UTC+11); the example uses 23:00 UTC ≈ 09:00 AEST.
- **Pros:** cloud reliability (machine-independent), managed secrets, full run history, one-click disable. **Cons:** secrets in CI, repo + runnable code required, must keep repo private.

### Option C — Cron (Linux / macOS / WSL)
No native cron on Windows — use **WSL** or a Linux/macOS host. `crontab -e`:
```cron
# m h dom mon dow   (server TZ; set CRON_TZ or use UTC)
CRON_TZ=Australia/Melbourne
0 9 * * 1  ~/stateguard/scripts/run-agent.sh "Off-Page Director" offpage-seo-director-agent.md
0 9 * * 2  ~/stateguard/scripts/run-agent.sh "Backlink Intelligence" backlink-intelligence-agent.md
0 9 * * 3  ~/stateguard/scripts/run-agent.sh "Competitor Intelligence" competitor-intelligence-agent.md
0 9 * * 4  ~/stateguard/scripts/run-agent.sh "Citation Intelligence" citation-intelligence-agent.md
0 9 * * 5  ~/stateguard/scripts/run-agent.sh "Weekly Executive Report" seo-director-agent.md
0 9 1 * *  ~/stateguard/scripts/run-agent.sh "Monthly SEO Report" seo-director-agent.md
```
- `run-agent.sh` mirrors the PowerShell runner (run `claude -p`, then POST an Execution Logs row). Secrets via the shell profile / a secret manager.
- **Pros:** simple, standard. **Cons:** needs a Linux/WSL host that's always on; secrets local.

---

## 6. Recommended safest option

**Overall safest = native Claude Code scheduled routines** (no secrets, no new code, no third party) — reaffirmed from the [automation capability report](../outputs/director/automation-capability-report.md). Use that first if available.

**Among the three requested schedulers**, ranked by safety for *this* project (on-prem, single-operator, human-gated, never-outward):

| Option | Secret exposure | New attack surface | Reliability | Kill switch | Verdict |
|--------|-----------------|--------------------|-------------|-------------|---------|
| **Windows Task Scheduler** | Local only | Minimal (no cloud, no repo) | Med (machine must be on) | Instant | **★ Safest for this setup** |
| GitHub Actions (private) | CI secret store | Repo + CI | High (cloud) | Instant | Best when you need cloud reliability |
| Cron (WSL/Linux) | Local | Needs always-on host | Med | Instant | Only if on Linux/WSL |

**Recommendation:** start with **Windows Task Scheduler** — it keeps the Anthropic + Airtable secrets **on your machine**, adds **no cloud/repo surface**, and can be disabled in one command. Move to **GitHub Actions (private repo)** only when you need machine-independent reliability; at that point store secrets in GitHub Encrypted Secrets and keep the repo private. **In every option, enforce the hard boundary and a scoped permission profile** so a run can never act outward — that, not the scheduler choice, is what keeps automation safe.

> **Status:** this controller is documented and the Execution Logs table is created. **No schedule has been activated** — activation (building the runnable agent + registering a task) is a human step, by design.
