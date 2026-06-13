"""Content generation service.

Wraps the LLM integration to produce SEO-optimized content. This is a scaffold:
when no LLM key is configured it returns a deterministic placeholder so the API
runs end-to-end out of the box.
"""

from app.integrations.llm import LLMClient
from app.models.schemas import ContentRequest, GeneratedContent


async def generate_content(request: ContentRequest) -> GeneratedContent:
    """Generate a title, meta description, and body for the given request."""
    llm = LLMClient()

    prompt = (
        f"Write an SEO-optimized article about '{request.topic}'. "
        f"Tone: {request.tone.value}. "
        f"Target keywords: {', '.join(request.keywords) or 'none specified'}."
    )

    body = await llm.complete(prompt)

    keyword_hint = request.keywords[0] if request.keywords else request.topic
    return GeneratedContent(
        title=f"{request.topic.title()}: A Complete Guide",
        meta_description=(
            f"Everything you need to know about {keyword_hint}. "
            "Expert, up-to-date, and SEO-optimized."
        )[:160],
        body=body,
    )
