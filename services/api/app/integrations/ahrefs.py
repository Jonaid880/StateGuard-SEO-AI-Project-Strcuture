"""Ahrefs API v3 integration (scaffold).

Returns sample data when no API key is configured. Replace `organic_keywords`
with real Ahrefs Site Explorer calls once credentials are in place.
"""

from app.core.config import get_settings

AHREFS_BASE_URL = "https://api.ahrefs.com/v3"


class AhrefsClient:
    def __init__(self) -> None:
        self._settings = get_settings()

    async def organic_keywords(self, domain: str) -> list[dict]:
        """Return organic keywords for a domain."""
        if not self._settings.ahrefs_api_key:
            return _sample_keywords()

        # Lazy import keeps httpx optional at import time.
        import httpx

        headers = {"Authorization": f"Bearer {self._settings.ahrefs_api_key}"}
        params = {"target": domain, "mode": "subdomains"}
        async with httpx.AsyncClient(base_url=AHREFS_BASE_URL, headers=headers) as client:
            resp = await client.get("/site-explorer/organic-keywords", params=params)
            resp.raise_for_status()
            data = resp.json()
        return data.get("keywords", [])


def _sample_keywords() -> list[dict]:
    return [
        {"keyword": "seo automation", "position": 4, "volume": 2400, "difficulty": 38},
        {"keyword": "ai content generator", "position": 7, "volume": 8100, "difficulty": 52},
        {"keyword": "keyword research tool", "position": 12, "volume": 5400, "difficulty": 61},
    ]
