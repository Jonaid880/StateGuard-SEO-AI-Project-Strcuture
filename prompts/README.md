# Prompts

Reusable, parameterized prompt templates the [agents](../agents) call. Each maps 1:1 to a capability agent.

## How to use

1. Pick the template for the task.
2. Replace every `{{placeholder}}` with real values (or a data file path).
3. Run it. The model reads `../docs/client-profile.md` and `../STATEGUARD_PROFILE.md` for client facts.
4. Output goes to the path named in the template — **as a recommendation for human review. Nothing is ever published.**

## Shared preamble (prepend to any prompt)

```
You are working on StateGuard-SEO-AI for StateGuard Australia.
Read ../docs/client-profile.md and ../STATEGUARD_PROFILE.md first (services, audiences, brand voice, AU English, "Grade A1", phone 1300 723 887).
Hard rules: recommendations only. Never publish, never edit any live site. Cite the source of every finding. Use Australian English.
```

## Templates

| File | Capability |
|------|-----------|
| [technical-seo-audit.prompt.md](technical-seo-audit.prompt.md) | Technical SEO audits |
| [keyword-research.prompt.md](keyword-research.prompt.md) | Keyword research |
| [competitor-intelligence.prompt.md](competitor-intelligence.prompt.md) | Competitor intelligence |
| [geo-optimization.prompt.md](geo-optimization.prompt.md) | GEO |
| [aeo-optimization.prompt.md](aeo-optimization.prompt.md) | AEO |
| [ai-citation-tracking.prompt.md](ai-citation-tracking.prompt.md) | AI citation tracking |
| [content-brief.prompt.md](content-brief.prompt.md) | Content brief generation |
| [content-calendar.prompt.md](content-calendar.prompt.md) | Content calendar generation |
