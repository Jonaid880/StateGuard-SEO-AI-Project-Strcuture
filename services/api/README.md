# StateGuard API

FastAPI backend for the StateGuard SEO AI suite.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- API root: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

## Structure

```
app/
├── main.py            # FastAPI app factory + router wiring
├── core/config.py     # Settings loaded from environment
├── api/routes/        # HTTP endpoints (health, content, analytics)
├── services/          # Business logic (content, analytics, audit)
├── integrations/      # External APIs (Ahrefs, SE Ranking, LLM)
├── agents/            # Agentic SEO workflows
└── models/schemas.py  # Pydantic request/response models
```

Configure credentials in the repo-root `.env` (see `.env.example`).
