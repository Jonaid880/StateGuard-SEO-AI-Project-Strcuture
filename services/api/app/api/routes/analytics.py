"""SEO analytics endpoints."""

from fastapi import APIRouter

from app.models.schemas import AnalyticsResponse
from app.services.analytics import get_domain_overview

router = APIRouter(tags=["analytics"])


@router.get("/analytics/{domain}", response_model=AnalyticsResponse)
async def domain_overview(domain: str) -> AnalyticsResponse:
    """Return a keyword/ranking overview for a domain."""
    return await get_domain_overview(domain)
