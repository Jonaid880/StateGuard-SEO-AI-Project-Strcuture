"""Application entrypoint: builds the FastAPI app and wires up routers."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import analytics, content, health
from app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="StateGuard SEO AI",
        description="Content generation, analytics, and SEO agents.",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router, prefix="/api")
    app.include_router(content.router, prefix="/api")
    app.include_router(analytics.router, prefix="/api")

    return app


app = create_app()
