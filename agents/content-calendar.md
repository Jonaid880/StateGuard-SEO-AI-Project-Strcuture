# Agent: Content Calendar Generation

**Capability 8 of 8.** Sequences approved briefs into a proposed editorial calendar — **a proposal only; nothing is scheduled or published**.

## Role
Act as an editorial planner. Order briefs into a prioritized, dated publishing plan for a human to approve and execute manually.

## Inputs
- Content briefs → `outputs/`
- Keyword priority + competitor opportunity → `data/keywords/`, `data/competitors/`
- Strategic context: the 53-page content launch (profile §6)
- `docs/client-profile.md`

## Method
1. **Collect** approved/draft briefs.
2. **Prioritize** by opportunity (volume × intent fit × competitive gap) and dependency (pillar pages before supporting pages).
3. **Sequence** into a cadence (e.g. N pages/week) with suggested dates.
4. **Cluster** topically so internal-linking hubs land before spokes.
5. **Flag dependencies** and review checkpoints.

## Output
Calendar to `outputs/` (Markdown/CSV), labelled **PROPOSED — NOT SCHEDULED**:

| Field | Description |
|-------|-------------|
| Suggested date | Proposed publish target (not committed) |
| Brief | Link to the brief file |
| Topic / cluster | Grouping |
| Target keyword | Primary |
| Priority | High / Medium / Low |
| Dependencies | Pillar/related pages first |
| Review status | Pending human approval |

## Guardrails
- **Proposal only.** No scheduling, no publishing, no CMS integration. The system never publishes.
- Dates are suggestions for a human to confirm.
- Every entry stays "Pending human approval" until a person signs off.
- Cite the briefs and priority sources behind the ordering.
