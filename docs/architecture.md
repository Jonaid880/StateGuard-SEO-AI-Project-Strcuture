# Architecture

StateGuard SEO AI is a monorepo with two deployable pieces and a shared package.

```
┌─────────────────────┐        HTTP/JSON        ┌──────────────────────────┐
│  apps/web (Next.js) │ ──────────────────────► │ services/api (FastAPI)    │
│  - marketing page   │   NEXT_PUBLIC_API_URL   │  - /api/health            │
│  - dashboard        │ ◄────────────────────── │  - /api/content/generate  │
└─────────────────────┘                         │  - /api/analytics/{domain}│
                                                 └────────────┬─────────────┘
                                                              │
                          ┌───────────────────────────────────┼───────────────────────────┐
                          ▼                                   ▼                             ▼
                  integrations/llm.py              integrations/ahrefs.py        integrations/se_ranking.py
                  (Claude content gen)             (rankings, keywords)          (project rankings)
```

## Layers (backend)

| Layer | Responsibility |
|-------|----------------|
| `api/routes` | HTTP surface — thin controllers, validation via Pydantic |
| `services` | Business logic — content generation, analytics, audits |
| `integrations` | External API clients — Ahrefs, SE Ranking, LLM |
| `agents` | Multi-step / agentic workflows that compose services |
| `models` | Pydantic request/response schemas |
| `core` | Configuration and cross-cutting concerns |

## Design notes

- **Runs without credentials.** Every integration returns sample/placeholder
  data when its API key is missing, so the whole stack boots end-to-end for
  local development. Add keys in `.env` to switch to live data.
- **Frontend is presentation-only.** All SEO/AI logic lives in the FastAPI
  backend; the Next.js app calls it over HTTP via `src/lib/api.ts`.
- **LLM default.** Content generation defaults to the latest capable Claude
  model (see `integrations/llm.py`).
