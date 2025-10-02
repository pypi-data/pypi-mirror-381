"""Tests for k selection behavior in SimulationRunner.run.

Covers default k=None (all combos, deterministic order),
k >= total (all combos, deterministic order), and k < total
which should use random.sample to select a random subset.
"""

from __future__ import annotations

import random
from typing import cast

from _pytest.monkeypatch import MonkeyPatch
from openai.types.chat import ChatCompletionMessageParam

from collinear.schemas.traitmix import Role
from collinear.schemas.traitmix import TraitMixCombination
from collinear.schemas.traitmix import TraitMixConfig
from collinear.simulate.runner import SimulationRunner


async def _fake_generate(
    _self: SimulationRunner,
    _combo: TraitMixCombination,
    _conversation: list[ChatCompletionMessageParam],
    role: Role,
) -> str:
    return "u" if role is Role.USER else "a"


def _mk_runner(monkeypatch: MonkeyPatch) -> SimulationRunner:
    monkeypatch.setattr(SimulationRunner, "_generate_turn", _fake_generate)
    return SimulationRunner(
        assistant_model_url="https://example.test",
        assistant_model_api_key="k",
        assistant_model_name="gpt-test",
        collinear_api_key="demo-001",
    )


def _mk_config() -> TraitMixConfig:
    return TraitMixConfig(
        ages=["18-24", "25-34"],
        genders=["female"],
        occupations=["Employed"],
        intents=["billing", "cancel"],
        traits={"impatience": ["medium"], "skeptical": ["high"]},
        locations=["US"],
        languages=["English"],
        tasks=["telecom"],
    )


def _sig(c: TraitMixCombination) -> tuple[str, str, str, str, str, str]:
    assert c.trait is not None
    assert c.intensity is not None
    intensity = str(c.intensity)
    return (
        str(c.age),
        cast("str", c.gender),
        cast("str", c.occupation),
        cast("str", c.intent),
        c.trait,
        intensity,
    )


def test_k_none_runs_all_combinations_in_order(monkeypatch: MonkeyPatch) -> None:
    """Default k=None runs all combos in deterministic order."""
    runner = _mk_runner(monkeypatch)
    cfg = _mk_config()

    combos = cfg.combinations()
    results = runner.run(config=cfg, k=None, num_exchanges=1, batch_delay=0.0)

    assert len(results) == len(combos)
    expected = [_sig(c) for c in combos]
    got = [_sig(r.traitmix) for r in results if r.traitmix is not None]
    assert got == expected


def test_k_ge_total_runs_all_combinations_in_order(monkeypatch: MonkeyPatch) -> None:
    """K >= total returns all combos in deterministic order."""
    runner = _mk_runner(monkeypatch)
    cfg = _mk_config()
    combos = cfg.combinations()
    k = len(combos) + 5

    results = runner.run(config=cfg, k=k, num_exchanges=1, batch_delay=0.0)
    assert len(results) == len(combos)
    expected = [_sig(c) for c in combos]
    got = [_sig(r.traitmix) for r in results if r.traitmix is not None]
    assert got == expected


def test_k_lt_total_uses_random_sample(monkeypatch: MonkeyPatch) -> None:
    """K < total uses random.sample(pop, k)."""
    runner = _mk_runner(monkeypatch)
    cfg = _mk_config()
    combos = cfg.combinations()

    calls: list[tuple[list[TraitMixCombination], int]] = []

    def fake_sample(pop: list[TraitMixCombination], count: int) -> list[TraitMixCombination]:
        calls.append((pop, count))

        return pop[:count]

    monkeypatch.setattr(random, "sample", fake_sample)

    k = 3
    results = runner.run(config=cfg, k=k, num_exchanges=1, batch_delay=0.0)
    assert len(calls) == 1
    assert calls[0][1] == k
    assert calls[0][0] == combos
    assert len(results) == k
    got = [_sig(r.traitmix) for r in results if r.traitmix is not None]
    expected = [_sig(c) for c in combos[:k]]
    assert got == expected
