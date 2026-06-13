"""SE Ranking API integration (scaffold).

Returns sample data when no API key is configured. Replace `rankings` with real
SE Ranking API calls once credentials are in place.
"""

from app.core.config import get_settings

SE_RANKING_BASE_URL = "https://api.seranking.com"


class SERankingClient:
    def __init__(self) -> None:
        self._settings = get_settings()

    async def rankings(self, project_id: str) -> list[dict]:
        """Return current keyword rankings for a project."""
        if not self._settings.se_ranking_api_key:
            return [
                {"keyword": "seo audit tool", "position": 3},
                {"keyword": "backlink checker", "position": 9},
            ]

        import httpx

        headers = {"Authorization": f"Token {self._settings.se_ranking_api_key}"}
        async with httpx.AsyncClient(base_url=SE_RANKING_BASE_URL, headers=headers) as client:
            resp = await client.get(f"/projects/{project_id}/rankings")
            resp.raise_for_status()
            return resp.json()
