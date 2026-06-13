"""Content generation endpoints."""

from fastapi import APIRouter

from app.models.schemas import ContentRequest, GeneratedContent
from app.services.content_generation import generate_content

router = APIRouter(tags=["content"])


@router.post("/content/generate", response_model=GeneratedContent)
async def create_content(request: ContentRequest) -> GeneratedContent:
    """Generate SEO-optimized content for a topic and keyword set."""
    return await generate_content(request)
