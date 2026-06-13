"""Agentic SEO workflow (scaffold).

Orchestrates audit -> analytics -> content steps into a single recommendation
pass. Extend with tool-calling against the LLM client for autonomous workflows.
"""

from app.models.schemas import ContentRequest
from app.services.analytics import get_domain_overview
from app.services.content_generation import generate_content
from app.services.seo_audit import run_audit


async def run_seo_workflow(domain: str, topic: str) -> dict:
    """Run a simple end-to-end SEO pass and return combined results."""
    audit = await run_audit(f"https://{domain}")
    analytics = await get_domain_overview(domain)

    top_keywords = [k.keyword for k in analytics.keywords[:3]]
    content = await generate_content(
        ContentRequest(topic=topic, keywords=top_keywords)
    )

    return {
        "domain": domain,
        "audit_findings": [f.message for f in audit.findings],
        "top_keywords": top_keywords,
        "suggested_content": content.model_dump(),
    }
