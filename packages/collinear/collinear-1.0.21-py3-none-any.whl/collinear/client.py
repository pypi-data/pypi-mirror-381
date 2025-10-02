"""Main Client class for Collinear SDK."""

import logging

from collinear.assess.local import LocalGuardConfig
from collinear.assess.local import LocalSafetyAssessor
from collinear.schemas.assessment import AssessmentResponse
from collinear.schemas.traitmix import SimulationResult
from collinear.schemas.traitmix import TraitMixConfig
from collinear.schemas.traitmix import TraitMixConfigInput
from collinear.simulate.runner import SimulationRunner


class Client:
    """Main client for Collinear simulation."""

    def __init__(
        self,
        assistant_model_url: str,
        assistant_model_api_key: str,
        assistant_model_name: str,
        *,
        collinear_api_key: str,
        timeout: float = 30.0,
        max_retries: int = 3,
        rate_limit_retries: int = 6,
    ) -> None:
        """Initialize the Collinear client.

        Args:
            assistant_model_url: OpenAI-compatible endpoint URL for the assistant model.
            assistant_model_api_key: API key for the assistant model.
            assistant_model_name: Assistant model name to use (required).
            collinear_api_key: Collinear API key used to call the Collinear traitmix
                endpoint for generating USER turns.
            timeout: Request timeout in seconds.
            max_retries: Maximum number of retries for failed requests.
            rate_limit_retries: Maximum retries for rate limit errors (with exponential backoff).

        """
        if not assistant_model_name:
            raise ValueError("model_name is required")
        self.assistant_model_url = assistant_model_url
        self.assistant_model_api_key = assistant_model_api_key
        self.assistant_model_name = assistant_model_name
        if not collinear_api_key:
            raise ValueError("COLLINEAR_API_KEY is required")
        self.timeout = timeout
        self.max_retries = max_retries
        self.rate_limit_retries = rate_limit_retries
        self.logger = logging.getLogger("collinear")
        self._simulation_runner: SimulationRunner | None = None
        self._collinear_api_key = collinear_api_key

    @property
    def simulation_runner(self) -> SimulationRunner:
        """Lazy load simulation runner."""
        if self._simulation_runner is None:
            self._simulation_runner = SimulationRunner(
                assistant_model_url=self.assistant_model_url,
                assistant_model_api_key=self.assistant_model_api_key,
                assistant_model_name=self.assistant_model_name,
                collinear_api_key=self._collinear_api_key,
                timeout=self.timeout,
                max_retries=self.max_retries,
                rate_limit_retries=self.rate_limit_retries,
            )
        return self._simulation_runner

    def simulate(
        self,
        traitmix_config: TraitMixConfigInput,
        k: int | None = None,
        num_exchanges: int = 2,
        batch_delay: float = 0.1,
        *,
        traitmix_temperature: float | None = None,
        traitmix_max_tokens: int | None = None,
        traitmix_seed: int | None = None,
        assistant_max_tokens: int | None = None,
        assistant_seed: int | None = None,
        mix_traits: bool = False,
        progress: bool = True,
        max_concurrency: int = 1,
    ) -> list[SimulationResult]:
        """Run simulations with traitmixs against the model.

        Args:
            traitmix_config: Configuration dict with traitmixs, intents, traits.
                Expected keys:
                  - "ages": list[str] (age buckets such as "25-34")
                  - "genders": list[str]
                  - "occupations": list[str]
                  - "intents": list[str]
                  - "traits": dict[str, list[str]]  (trait -> levels in {"low","medium","high"})
                  - "languages": list[str]
                  - "locations": list[str]
                  - "task": str | "tasks": list[str]
            k: Optional number of simulation samples to generate. If ``None``,
                runs all available combinations.
            num_exchanges: Number of user-assistant exchanges (e.g., 2 = 2 user
                turns + 2 assistant turns)
            batch_delay: Delay between simulations to avoid rate limits
                (seconds)
            traitmix_temperature: Optional temperature for the traitmix generator (default 0.7).
            traitmix_max_tokens: Optional max tokens for the traitmix generator (default 256).
            traitmix_seed: Optional deterministic seed for the traitmix generator (-1 uses
                service-side randomness).
            assistant_max_tokens: Optional max tokens for the assistant model. If not set,
                the backend default is used.
            assistant_seed: Optional deterministic seed for the assistant model (if supported
                by your provider). If not set, no seed is sent.
            mix_traits: If True, mix traits pairwise (exactly 2 traits per traitmix).
                Requires at least two traits with levels. Defaults to False
                (single-trait behavior).
            progress: Whether to display a tqdm-style progress bar tracking traitmix
                API calls. Defaults to ``True``.
            max_concurrency: Maximum number of simultaneous traitmix requests. Defaults to ``1``
                which uses the ``/traitmix`` endpoint for individual requests. Values ``> 1`` are
                grouped into batches (up to 8) and routed to the ``/traitmix_batch`` endpoint.

        Returns:
            List of simulation results with conv_prefix and response

        Note:
            The SDK implements automatic retry with backoff logic to handle rate limits.
            If you're hitting rate limits frequently, increase the batch_delay parameter.

        """
        config = TraitMixConfig.from_input(traitmix_config)

        runner = self.simulation_runner
        return runner.run(
            config=config,
            k=k,
            num_exchanges=num_exchanges,
            batch_delay=batch_delay,
            traitmix_temperature=traitmix_temperature,
            traitmix_max_tokens=traitmix_max_tokens,
            traitmix_seed=traitmix_seed,
            assistant_max_tokens=assistant_max_tokens,
            assistant_seed=assistant_seed,
            mix_traits=mix_traits,
            progress=progress,
            max_concurrency=max_concurrency,
        )

    def assess(
        self,
        dataset: list[SimulationResult],
        *,
        judge_model_url: str | None = None,
        judge_model_api_key: str | None = None,
        judge_model_name: str | None = None,
        temperature: float = 0.0,
        max_tokens: int = 512,
    ) -> AssessmentResponse:
        """Assess simulated data locally using a user-provided model.

        This bypasses the Collinear platform entirely. It prompts an OpenAI-compatible
        model with a safety rubric and returns a compact ``AssessmentResponse``.

        Args:
            dataset: List of simulation results to assess.
            judge_model_url: Optional override for the judge's endpoint URL.
            judge_model_api_key: Optional override for the judge's API key.
            judge_model_name: Optional override for the judge model name.
            temperature: Sampling temperature for the judge.
            max_tokens: Max tokens for the judge completion.

        Returns:
            AssessmentResponse with scores and rationales per conversation.

        """
        if not dataset:
            raise ValueError("Dataset cannot be empty")

        cfg = LocalGuardConfig(
            api_url=judge_model_url or self.assistant_model_url,
            api_key=judge_model_api_key or self.assistant_model_api_key,
            model=judge_model_name or self.assistant_model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=self.timeout,
        )
        assessor = LocalSafetyAssessor(cfg)
        return assessor.score_dataset(dataset)
