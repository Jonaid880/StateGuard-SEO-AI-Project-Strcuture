# Prompt — Content Calendar Generation

**Agent:** [content-calendar](../agents/content-calendar.md) · **Output:** `../outputs/` + Airtable "Content Calendar"

---

```
[Shared preamble — see prompts/README.md]

TASK: Sequence approved/draft briefs into a PROPOSED editorial calendar. Nothing is scheduled or published.

INPUTS: ../outputs/ (briefs), ../data/keywords/ + ../data/competitors/ (priority/opportunity).
CONTEXT: the 53-page content launch (client-profile §6); pillar pages before supporting pages.
CADENCE: {{e.g. "3 pages/week starting {{start date}}"}}.

METHOD:
1. Collect briefs.
2. Prioritize by opportunity (volume x intent fit x competitive gap) and dependency.
3. Sequence into the cadence with SUGGESTED dates (not commitments).
4. Cluster topically so internal-linking hubs land before spokes.
5. Flag dependencies and review checkpoints.

OUTPUT: ../outputs/content-calendar.md (and/or CSV), headed "PROPOSED — NOT SCHEDULED", columns:
Suggested date | Brief | Topic/cluster | Target keyword | Priority | Dependencies | Review status (default "Pending human approval")

Proposal only — no scheduling, no publishing, no CMS integration. Every row stays "Pending human approval" until a person signs off.
Mirror into the Airtable Content Calendar table when asked.
```
