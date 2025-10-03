from dapr_agents.types.llm import HFInferenceClientConfig
from dapr_agents.llm.base import LLMClientBase
from typing import Optional, Dict, Any, Union
from huggingface_hub import InferenceClient
from pydantic import Field, model_validator
import os
import logging

logger = logging.getLogger(__name__)


class HFHubInferenceClientBase(LLMClientBase):
    """
    Base class for managing Hugging Face Inference API clients.
    Handles client initialization, configuration, and shared logic.
    """

    model: Optional[str] = Field(
        default=None,
        description="Model ID on Hugging Face Hub or a URL to a deployed endpoint. If not set, a recommended model may be chosen by your wrapper.",
    )
    hf_provider: Optional[str] = Field(
        default="hf-inference",
        description="Inference provider to use. Defaults to automatic selection based on available providers. Ignored if a custom endpoint URL is provided.",
    )
    token: Optional[Union[str, bool]] = Field(
        default=None,
        description="Hugging Face access token for authentication. If None, uses the locally saved token. Set to False to skip sending a token. Mutually exclusive with api_key.",
    )
    api_key: Optional[Union[str, bool]] = Field(
        default=None, description="Alias for token. Use only one of token or api_key."
    )
    base_url: Optional[str] = Field(
        default=None,
        description="Custom endpoint URL for inference. Used for private deployments or TGI endpoints. Cannot be set if 'model' is a Hub ID.",
    )
    timeout: Optional[float] = Field(
        default=None,
        description="Maximum seconds to wait for a response. If None, waits indefinitely. Useful for slow model loading.",
    )
    headers: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        description="Extra HTTP headers to send with requests. Overrides defaults like authorization and user-agent.",
    )
    cookies: Optional[Dict[str, str]] = Field(
        default_factory=dict, description="Extra cookies to send with requests."
    )
    proxies: Optional[Any] = Field(
        default=None,
        description="Proxy settings for HTTP requests. Use standard requests format.",
    )
    bill_to: Optional[str] = Field(
        default=None,
        description="Billing account for requests. Only used for enterprise/organization billing.",
    )

    @model_validator(mode="before")
    def validate_and_initialize(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensures consistency for 'api_key' and 'token' fields before initialization.
        - Normalizes 'token' and 'api_key' to a single field.
        - Validates exclusivity of 'model' and 'base_url'.
        """
        token = values.get("token")
        api_key = values.get("api_key")
        model = values.get("model")
        base_url = values.get("base_url")

        # Ensure mutual exclusivity of `token` and `api_key`
        if token is not None and api_key is not None:
            raise ValueError(
                "Provide only one of 'api_key' or 'token'. They are aliases and cannot coexist."
            )

        # Normalize `token` to `api_key`
        if token is not None:
            values["api_key"] = token
            values.pop("token", None)  # Remove `token` for consistency

        # Use environment variable if `api_key` is not explicitly provided
        if api_key is None:
            api_key = os.environ.get("HUGGINGFACE_API_KEY")

        if api_key is None:
            raise ValueError(
                "API key is required. Set it explicitly or in the 'HUGGINGFACE_API_KEY' environment variable."
            )

        values["api_key"] = api_key

        # mutual‑exclusivity
        if model is not None and base_url is not None:
            raise ValueError("Cannot provide both 'model' and 'base_url'.")

        # require at least one
        if model is None and base_url is None:
            raise ValueError(
                "HF Inference needs either `model` or `base_url`. "
                "E.g. model='gpt2' or base_url='https://…/models/gpt2'."
            )

        # auto‑derive model from base_url
        if model is None:
            derived = base_url.rstrip("/").split("/")[-1]
            values["model"] = derived

        return values

    def model_post_init(self, __context: Any) -> None:
        """
        Initializes private attributes after validation.
        """
        self._provider = "huggingface"

        # Set up the private config and client attributes
        self._config = self.get_config()
        self._client = self.get_client()
        return super().model_post_init(__context)

    def get_config(self) -> HFInferenceClientConfig:
        """
        Returns the appropriate configuration for the Hugging Face Inference API.
        """
        return HFInferenceClientConfig(
            model=self.model,
            hf_provider=self.hf_provider,
            api_key=self.api_key,
            base_url=self.base_url,
            headers=self.headers,
            cookies=self.cookies,
            proxies=self.proxies,
            timeout=self.timeout,
        )

    def get_client(self) -> InferenceClient:
        """
        Initializes and returns the Hugging Face Inference client.
        """
        config: HFInferenceClientConfig = self.config
        return InferenceClient(
            model=config.model,
            provider=config.hf_provider,
            api_key=config.api_key,
            base_url=config.base_url,
            headers=config.headers,
            cookies=config.cookies,
            proxies=config.proxies,
            timeout=self.timeout,
        )

    @classmethod
    def from_config(
        cls, client_options: HFInferenceClientConfig, timeout: float = 1500
    ):
        """
        Initializes the HFHubInferenceClientBase using HFInferenceClientConfig.

        Args:
            client_options: The configuration options for the client.
            timeout: Timeout for requests (default is 1500 seconds).

        Returns:
            HFHubInferenceClientBase: The initialized client instance.
        """
        return cls(
            model=client_options.model,
            hf_provider=client_options.hf_provider,
            api_key=client_options.api_key,
            token=client_options.token,
            base_url=client_options.base_url,
            headers=client_options.headers,
            cookies=client_options.cookies,
            proxies=client_options.proxies,
            timeout=timeout,
        )

    @property
    def config(self) -> Dict[str, Any]:
        return self._config

    @property
    def client(self) -> InferenceClient:
        return self._client
