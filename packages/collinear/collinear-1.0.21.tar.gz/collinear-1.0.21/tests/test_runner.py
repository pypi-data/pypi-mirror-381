"""Tests exercising the conversation runner without network calls."""

from __future__ import annotations

import asyncio

import httpx
import pytest
from _pytest.monkeypatch import MonkeyPatch
from openai.types.chat import ChatCompletionMessageParam

import collinear.simulate.runner as runner_module
from collinear.schemas.traitmix import Role
from collinear.schemas.traitmix import SimulationResult
from collinear.schemas.traitmix import TraitMixCombination
from collinear.schemas.traitmix import TraitMixConfig
from collinear.simulate.runner import MAX_ALLOWED_CONCURRENCY
from collinear.simulate.runner import SimulationRunner


def test_run_builds_conversation_and_returns_results(monkeypatch: MonkeyPatch) -> None:
    """Monkeypatch turn generation to validate run() behavior without network."""

    async def fake_generate(
        _self: SimulationRunner,
        _combo: TraitMixCombination,
        _conversation: list[ChatCompletionMessageParam],
        role: Role,
    ) -> str:
        return {Role.USER: "u", Role.ASSISTANT: "a"}[role]

    monkeypatch.setattr(SimulationRunner, "_generate_turn", fake_generate)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
        tasks=["telecom"],
    )

    results = runner.run(
        config=config,
        k=1,
        num_exchanges=2,
        batch_delay=0.0,
        progress=False,
    )
    assert len(results) == 1
    res = results[0]

    assert [m["role"] for m in res.conv_prefix] == ["user", "assistant", "user"]
    assert res.response == "a"


def test_progress_updates_per_user_turn(monkeypatch: MonkeyPatch) -> None:
    """Progress bar receives one update per user turn when enabled."""
    updates: list[int] = []
    totals: list[int] = []
    closed: list[bool] = []

    class FakeBar:
        def __init__(
            self,
            total: int | None = None,
            desc: str | None = None,
            unit: str | None = None,
        ) -> None:
            if not isinstance(total, int):
                raise TypeError("expected integer total")
            totals.append(total)
            self.total = total
            self.n = 0
            self.desc = desc
            self.unit = unit

        def update(self, value: int) -> None:
            self.n += value
            updates.append(value)

        def refresh(self) -> None:
            pass

        def close(self) -> None:
            closed.append(True)

    def fake_tqdm(*, total: int, desc: str | None = None, unit: str | None = None) -> FakeBar:
        return FakeBar(total=total, desc=desc, unit=unit)

    monkeypatch.setattr(runner_module, "_PROGRESS_FACTORY", fake_tqdm)

    async def fake_generate(
        _self: SimulationRunner,
        _combo: TraitMixCombination,
        _conversation: list[ChatCompletionMessageParam],
        role: Role,
    ) -> str:
        return {Role.USER: "u", Role.ASSISTANT: "a"}[role]

    monkeypatch.setattr(SimulationRunner, "_generate_turn", fake_generate)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
        tasks=["telecom"],
    )

    results = runner.run(
        config=config,
        k=1,
        num_exchanges=2,
        batch_delay=0.0,
    )

    assert len(results) == 1
    assert totals == [2]
    assert updates == [1, 1]
    assert closed == [True]


def test_progress_adjusts_when_simulation_skipped(monkeypatch: MonkeyPatch) -> None:
    """Progress total shrinks when a simulation aborts early."""
    bars: list[FakeBar] = []
    updates: list[int] = []

    class FakeBar:
        def __init__(
            self,
            total: int | None = None,
            desc: str | None = None,
            unit: str | None = None,
        ) -> None:
            if not isinstance(total, int):
                raise TypeError("expected integer total")
            self.total = total
            self.n = 0
            self.desc = desc
            self.unit = unit
            bars.append(self)

        def update(self, value: int) -> None:
            self.n += value
            updates.append(value)

        def refresh(self) -> None:
            pass

        def close(self) -> None:
            pass

    def fake_tqdm(*, total: int, desc: str | None = None, unit: str | None = None) -> FakeBar:
        return FakeBar(total=total, desc=desc, unit=unit)

    monkeypatch.setattr(runner_module, "_PROGRESS_FACTORY", fake_tqdm)

    def failing_generate(
        _self: SimulationRunner,
        _combo: TraitMixCombination,
        _conversation: list[ChatCompletionMessageParam],
        role: Role,
    ) -> str:
        if role is Role.USER:
            raise SimulationRunner.InvalidTraitError("bad trait")
        return "a"

    monkeypatch.setattr(SimulationRunner, "_generate_turn", failing_generate)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
        tasks=["telecom"],
    )

    results = runner.run(
        config=config,
        k=1,
        num_exchanges=2,
        batch_delay=0.0,
    )

    assert results == []
    assert updates == [1]
    assert len(bars) == 1
    assert bars[0].total == 1


def test_progress_adjustment_with_parallel_failures(monkeypatch: MonkeyPatch) -> None:
    """Verify progress total shrinks correctly when parallel tasks fail."""
    bars: list[FakeBar2] = []

    class FakeBar2:
        def __init__(
            self, total: int | None = None, desc: str | None = None, unit: str | None = None
        ) -> None:
            self.total = total or 0
            self.n = 0
            self.desc = desc
            self.unit = unit
            bars.append(self)

        def update(self, value: int) -> None:
            self.n += value

        def refresh(self) -> None:
            pass

        def close(self) -> None:
            pass

    monkeypatch.setattr(runner_module, "_PROGRESS_FACTORY", FakeBar2)

    async def partially_failing_build_conversation(
        self: SimulationRunner, combo: TraitMixCombination, _num_exchanges: int
    ) -> tuple[list[ChatCompletionMessageParam], str]:
        self._advance_progress(1)
        if "bad" in str(combo.traits):
            raise SimulationRunner.BuildConversationError(1, invalid_trait=True, trait="bad_trait")
        return [], "success"

    monkeypatch.setattr(
        SimulationRunner, "_build_conversation", partially_failing_build_conversation
    )

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"], "bad_trait": ["medium"]},
    )

    runner.run(config, k=2, num_exchanges=2, max_concurrency=2)

    assert len(bars) == 1
    assert bars[0].total == 2 * 2 - 1


def test_build_conversation_failed_carries_metadata(monkeypatch: MonkeyPatch) -> None:
    """Verify BuildConversationFailed carries user turn count and trait info."""
    caught_exceptions = []

    async def failing_build_conversation(
        self: SimulationRunner, _combo: TraitMixCombination, _num_exchanges: int
    ) -> tuple[list[ChatCompletionMessageParam], str]:
        self._advance_progress(1)
        raise SimulationRunner.BuildConversationError(1, invalid_trait=True, trait="bad_trait")

    monkeypatch.setattr(SimulationRunner, "_build_conversation", failing_build_conversation)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
    )

    async def capture_exceptions(
        self: SimulationRunner,
        samples: list[TraitMixCombination],
        num_exchanges: int,
        _batch_delay: float,
        _max_concurrency: int = 8,
    ) -> list[SimulationResult]:
        async def run_one(_i: int, combo: TraitMixCombination) -> None:
            try:
                await self._build_conversation(combo, num_exchanges)
            except SimulationRunner.BuildConversationError as e:
                caught_exceptions.append(e)

        await asyncio.gather(*(run_one(i, combo) for i, combo in enumerate(samples)))
        return []

    monkeypatch.setattr(SimulationRunner, "_execute_samples", capture_exceptions)
    runner.run(config, k=1, num_exchanges=2)

    assert len(caught_exceptions) == 1
    exc = caught_exceptions[0]
    assert exc.completed_user_turns == 1
    assert exc.invalid_trait is True
    assert exc.trait == "bad_trait"


def test_calculate_semaphore_limit() -> None:
    """Test semaphore limit calculation respects bounds."""
    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    near_min_request = 3
    moderate_request = 5
    above_max_request = 100

    assert runner.calculate_semaphore_limit(0) == 1
    assert runner.calculate_semaphore_limit(-5) == 1
    assert runner.calculate_semaphore_limit(near_min_request) == near_min_request
    assert runner.calculate_semaphore_limit(moderate_request) == moderate_request
    assert runner.calculate_semaphore_limit(MAX_ALLOWED_CONCURRENCY) == MAX_ALLOWED_CONCURRENCY
    assert runner.calculate_semaphore_limit(above_max_request) == MAX_ALLOWED_CONCURRENCY


def test_all_user_turns_hit_batch_endpoint(monkeypatch: MonkeyPatch) -> None:
    """Even single-turn conversations should use the batch traitmix endpoint."""
    called_payloads: list[tuple[str, object]] = []

    async def fake_request_traitmix(
        _self: SimulationRunner,
        url: str,
        _headers: dict[str, str],
        payload: object,
    ) -> tuple[httpx.Response | None, str | None]:
        called_payloads.append((url, payload))
        req = httpx.Request("POST", url)
        assert isinstance(payload, list)
        body: object = {"responses": ["mock-user" for _ in payload]}
        resp = httpx.Response(200, request=req, json=body)
        return resp, None

    async def fake_call_with_retry(
        _self: SimulationRunner, _messages: list[dict[str, object]], _system_prompt: str
    ) -> str:
        return "mock-assistant"

    monkeypatch.setattr(SimulationRunner, "_request_traitmix", fake_request_traitmix)
    monkeypatch.setattr(SimulationRunner, "_call_with_retry", fake_call_with_retry)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium"]},
    )

    asyncio.run(
        runner.run_async(
            config,
            k=1,
            num_exchanges=1,
            max_concurrency=1,
            batch_delay=0.0,
        )
    )

    assert called_payloads, "Expected traitmix request to be issued"
    assert all("steer_batch" in url for url, _ in called_payloads)
    assert all(isinstance(payload, list) and len(payload) == 1 for _, payload in called_payloads)


def test_concurrency_above_one_uses_batch(monkeypatch: MonkeyPatch) -> None:
    """Verify concurrency > 1 routes to /steer_batch endpoint."""
    called_urls: list[tuple[str, object]] = []

    async def fake_request_traitmix(
        _self: SimulationRunner,
        url: str,
        _headers: dict[str, str],
        payload: object,
    ) -> tuple[httpx.Response | None, str | None]:
        called_urls.append((url, payload))
        req = httpx.Request("POST", url)
        assert isinstance(payload, list)
        body: object = {"responses": ["mock-user" for _ in payload]}
        resp = httpx.Response(200, request=req, json=body)
        return resp, None

    async def fake_call_with_retry(
        _self: SimulationRunner, _messages: list[dict[str, object]], _system_prompt: str
    ) -> str:
        return "mock-assistant"

    monkeypatch.setattr(SimulationRunner, "_request_traitmix", fake_request_traitmix)
    monkeypatch.setattr(SimulationRunner, "_call_with_retry", fake_call_with_retry)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        ages=["18-24", "25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing"],
        traits={"impatience": ["medium", "high"]},
    )

    asyncio.run(
        runner.run_async(
            config,
            k=2,
            num_exchanges=1,
            max_concurrency=2,
            batch_delay=0.0,
        )
    )

    assert called_urls, "Expected traitmix request to be issued"
    assert all("steer_batch" in url for url, _ in called_urls)
    assert all(isinstance(payload, list) for _, payload in called_urls)


def test_concurrent_run_preserves_result_order(monkeypatch: MonkeyPatch) -> None:
    """Results stay aligned with configured sample order under concurrency."""

    async def fake_build_conversation(
        _self: SimulationRunner,
        combo: TraitMixCombination,
        num_exchanges: int,
    ) -> tuple[list[ChatCompletionMessageParam], str]:
        level_label_value = combo.intensity if combo.intensity is not None else "medium"
        if isinstance(level_label_value, int):
            mapping = {0: "low", 1: "medium", 2: "high"}
            level_label = mapping[level_label_value]
        else:
            level_label = level_label_value
        order = {"low": 0, "medium": 1, "high": 2}
        level = order[level_label]

        await asyncio.sleep(0.01 * (2 - level))
        messages: list[ChatCompletionMessageParam] = []
        total_turns = num_exchanges * 2
        for turn in range(1, total_turns + 1):
            if turn % 2 == 1:
                messages.append(
                    {
                        "role": Role.USER.value,
                        "content": f"user-{level_label}-{turn}",
                    }
                )
            else:
                if turn == total_turns:
                    content = f"assistant-{level_label}-final"
                else:
                    content = f"assistant-{level_label}-{turn}"
                messages.append(
                    {
                        "role": Role.ASSISTANT.value,
                        "content": content,
                    }
                )
        final_response = str(messages[-1]["content"])
        return messages, final_response

    monkeypatch.setattr(SimulationRunner, "_build_conversation", fake_build_conversation)

    runner = SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="test-key",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )

    config = TraitMixConfig(
        traits={"patience": ["low", "medium", "high"]},
    )

    results = runner.run(
        config=config,
        num_exchanges=2,
        batch_delay=0.0,
        progress=False,
        max_concurrency=3,
    )

    intensities: list[str] = []
    for res in results:
        assert res.traitmix is not None
        intensity_value = res.traitmix.intensity
        assert intensity_value is not None
        intensities.append(str(intensity_value))
    assert intensities == ["low", "medium", "high"]

    responses = [res.response for res in results]
    assert responses == [
        "assistant-low-final",
        "assistant-medium-final",
        "assistant-high-final",
    ]


def test_batch_endpoint_raises_on_empty_response() -> None:
    """Empty traitmix responses trigger an explicit error."""

    class EmptyBatchRunner(SimulationRunner):
        def __init__(self) -> None:
            super().__init__(
                assistant_model_url="https://example.test",
                assistant_model_api_key="test-key",
                assistant_model_name="gpt-test",
                collinear_api_key="demo-001",
            )

        async def _call_batch_endpoint(
            self,
            payloads: list[dict[str, object]],
            *,
            headers: dict[str, str],
        ) -> list[str]:
            _ = payloads
            _ = headers
            return [""]

        async def _call_with_retry(
            self,
            _messages: list[ChatCompletionMessageParam],
            _system_prompt: str,
        ) -> str:
            return "assistant"

        async def invoke_trait_dict(
            self,
            *,
            trait_dict: dict[str, int | str],
            combo: TraitMixCombination,
        ) -> str:
            return await super()._call_collinear_traitmix_api_trait_dict(
                trait_dict=trait_dict,
                combo=combo,
                conversation=[],
            )

    runner = EmptyBatchRunner()

    with pytest.raises(SimulationRunner.EmptyTraitMixResponseError):
        asyncio.run(
            runner.invoke_trait_dict(
                trait_dict={"impatience": "medium"},
                combo=TraitMixCombination(
                    age=None,
                    gender=None,
                    occupation=None,
                    intent=None,
                    traits={"impatience": "medium"},
                    location=None,
                    language=None,
                    task=None,
                ),
            )
        )
