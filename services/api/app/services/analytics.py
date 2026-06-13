"""SEO analytics service.

Aggregates keyword/ranking data from external providers. The scaffold returns
sample data; wire up the Ahrefs / SE Ranking integrations to return live metrics.
"""

from app.integrations.ahrefs import AhrefsClient
from app.models.schemas import AnalyticsResponse, KeywordMetric


async def get_domain_overview(domain: str) -> AnalyticsResponse:
    """Return a keyword overview for a domain."""
    client = AhrefsClient()
    raw_keywords = await client.organic_keywords(domain)

    keywords = [
        KeywordMetric(
            keyword=row["keyword"],
            position=row["position"],
            volume=row["volume"],
            difficulty=row["difficulty"],
        )
        for row in raw_keywords
    ]

    return AnalyticsResponse(domain=domain, keywords=keywords)
