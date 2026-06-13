# StateGuard SEO AI

An AI-powered SEO automation suite. StateGuard combines **SEO content generation**,
an **analytics dashboard**, and **automated audits/agents** into a single monorepo.

- **Frontend & dashboard** — Next.js (App Router, TypeScript, Tailwind CSS)
- **Backend & AI** — Python FastAPI service for content generation, analytics, and SEO agents
- **Integrations** — Ahrefs, SE Ranking, Google Search Console, and LLM providers (Claude)

---

## Monorepo layout

```
StateGuard-SEO-AI-Project-Strcuture/
├── apps/
│   └── web/                 # Next.js frontend + dashboard (TypeScript, Tailwind)
├── services/
│   └── api/                 # Python FastAPI backend (content, analytics, agents)
├── packages/
│   └── shared/              # Shared types/contracts between web and api
├── docs/                    # Architecture & getting-started docs
└── scripts/                 # Dev/ops helper scripts
```

See [`docs/architecture.md`](docs/architecture.md) for how the pieces fit together.

---

## Features

| Area | What it does |
|------|--------------|
| **Content generation** | AI-generated articles, meta titles/descriptions, and keyword-optimized copy |
| **Analytics dashboard** | Pull and visualize rankings, backlinks, and traffic from Ahrefs / SE Ranking / GSC |
| **SEO audits & agents** | Automated site audits, reporting, and agentic SEO workflows |

---

## Quick start

### Prerequisites

- **Node.js** 20+ and **npm** 10+
- **Python** 3.11+

### 1. Clone & configure

```bash
git clone https://github.com/Jonaid880/StateGuard-SEO-AI-Project-Strcuture.git
cd StateGuard-SEO-AI-Project-Strcuture
cp .env.example .env          # fill in your API keys
```

### 2. Frontend (Next.js)

```bash
cd apps/web
npm install
npm run dev                   # http://localhost:3000
```

### 3. Backend (FastAPI)

```bash
cd services/api
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload # http://localhost:8000  (docs at /docs)
```

The web app proxies API calls to the FastAPI service via `NEXT_PUBLIC_API_URL`
(defaults to `http://localhost:8000`).

---

## Environment variables

Copy `.env.example` to `.env` and fill in:

| Variable | Used by | Description |
|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | api | Claude API key for content generation & agents |
| `AHREFS_API_KEY` | api | Ahrefs API v3 token |
| `SE_RANKING_API_KEY` | api | SE Ranking API key |
| `NEXT_PUBLIC_API_URL` | web | Base URL of the FastAPI backend |

---

## Documentation

- [Getting started](docs/getting-started.md)
- [Architecture](docs/architecture.md)

## License

MIT — see [LICENSE](LICENSE).
