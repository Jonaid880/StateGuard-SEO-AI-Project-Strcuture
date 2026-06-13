"""LLM integration (Claude / Anthropic).

If no API key is configured, `complete` returns a deterministic placeholder so
the rest of the app runs without credentials during development.
"""

from app.core.config import get_settings

# Default to the latest capable Claude model for content generation.
DEFAULT_MODEL = "claude-opus-4-8"


class LLMClient:
    def __init__(self, model: str = DEFAULT_MODEL) -> None:
        self._settings = get_settings()
        self._model = model

    async def complete(self, prompt: str, max_tokens: int = 1024) -> str:
        """Return a completion for the prompt, or a placeholder if unconfigured."""
        api_key = self._settings.anthropic_api_key
        if not api_key:
            return (
                "[placeholder content] Configure ANTHROPIC_API_KEY to generate "
                f"real output. Prompt was: {prompt}"
            )

        # Lazy import so the dependency is only needed when a key is present.
        from anthropic import AsyncAnthropic

        client = AsyncAnthropic(api_key=api_key)
        message = await client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(block.text for block in message.content if block.type == "text")
