# Getting started

## 1. Prerequisites

- Node.js 20+ and npm 10+
- Python 3.11+

## 2. Configure environment

```bash
cp .env.example .env
```

The stack runs without any keys (integrations fall back to sample data). Add
keys when you want live results:

- `ANTHROPIC_API_KEY` — real content generation
- `AHREFS_API_KEY` / `SE_RANKING_API_KEY` — live SEO metrics

## 3. Start the backend

```bash
cd services/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Verify: open http://localhost:8000/docs and hit `GET /api/health`.

## 4. Start the frontend

```bash
cd apps/web
npm install
npm run dev
```

Open http://localhost:3000 and click **Open dashboard**. The dashboard shows
"connected" once the backend is running.

## 5. Try the API

```bash
# Health
curl http://localhost:8000/api/health

# Generate content
curl -X POST http://localhost:8000/api/content/generate \
  -H "Content-Type: application/json" \
  -d '{"topic":"technical seo","keywords":["crawl budget","sitemaps"]}'

# Domain analytics
curl http://localhost:8000/api/analytics/example.com
```
