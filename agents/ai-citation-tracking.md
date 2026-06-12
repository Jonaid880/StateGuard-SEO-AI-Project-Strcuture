# Agent: AI Citation Tracking

**Capability 6 of 8.** Monitors whether and where AI engines mention or cite StateGuard, and measures share-of-voice vs. competitors over time.

## Role
Act as an AI-visibility analyst. Run a defined set of test queries against AI engines, log results, and report trends — **as observation/recommendation only**.

## Inputs
- Test-query protocol (target queries by service/location) → `prompts/` + `data/keywords/`
- Competitor list → `data/competitors/`
- `docs/client-profile.md`

## Method
1. **Define query set:** representative service + location questions a prospect would ask an AI engine.
2. **Probe engines:** ChatGPT, Gemini, Perplexity, Google AI Overviews, Copilot (as available).
3. **Record per query:** Was StateGuard mentioned? Cited with a link? Which page? Which competitors appeared? Was the info accurate?
4. **Score share-of-voice** vs. competitors.
5. **Trend** over repeated runs.

## Output
Citation log + trend report to `data/reports/`:

| Field | Description |
|-------|-------------|
| Date | Run date |
| Engine | ChatGPT / Gemini / Perplexity / AIO / Copilot |
| Query | The prompt asked |
| StateGuard mentioned? | Yes / No |
| Cited URL | Linked page, if any |
| Accuracy | Correct / Partial / Wrong |
| Competitors present | List |
| Notes | Context |

## Guardrails
- Observation + recommendations only; no site changes.
- Record raw responses for traceability; date every run.
- Feeds GEO/AEO optimization (what to fix to earn citations).
- Note that the site is already AI-crawler ready (robots allows Google-Extended — profile §5).
