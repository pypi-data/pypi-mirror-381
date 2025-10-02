"""Ensure SimulationRunner sends only the canonical TraitMix API header."""

from __future__ import annotations

from openai.types.chat import ChatCompletionMessageParam

from collinear.schemas.traitmix import TraitMixConfig
from collinear.simulate.runner import SimulationRunner


class CaptureRunner(SimulationRunner):
    """Capture headers from traitmix batch calls."""

    def __init__(self) -> None:
        """Initialize the capture runner."""
        super().__init__(
            assistant_model_url="https://example.test",
            assistant_model_api_key="k",
            assistant_model_name="gpt-test",
            collinear_api_key="traitmix-secret",
        )
        self.captured_headers: list[dict[str, str]] = []

    async def _call_batch_endpoint(
        self,
        payloads: list[dict[str, object]],
        *,
        headers: dict[str, str],
    ) -> list[str]:
        self.captured_headers.append(headers)
        return ["ok" for _ in payloads]

    async def _call_with_retry(
        self,
        _messages: list[ChatCompletionMessageParam],
        _system_prompt: str,
    ) -> str:
        return "assistant"


def test_traitmix_headers_use_api_key_only() -> None:
    """USER calls include only `API-Key` header (no `X-API-Key`)."""
    runner = CaptureRunner()

    cfg = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
    )

    runner.run(config=cfg, k=1, num_exchanges=1, batch_delay=0.0, progress=False)
    assert runner.captured_headers
    headers = runner.captured_headers[-1]
    assert headers == {"Content-Type": "application/json", "API-Key": "traitmix-secret"}
