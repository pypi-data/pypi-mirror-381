import asyncio
import copy
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, fields
from typing import Literal

from autogen_core.models import SystemMessage, UserMessage
from autogen_ext.models.openai import (
    AzureOpenAIChatCompletionClient,
    OpenAIChatCompletionClient,
)
from dynaconf import Dynaconf, DynaconfFormatError
from openai import OpenAI
from pydantic.networks import HttpUrl

from . import config as _config
from .azure_auth import AzureADTokenProvider
from .logging_utils import get_logger, trace  # noqa: F401

logger = get_logger(__name__)

ChatCompletionClient = AzureOpenAIChatCompletionClient | OpenAIChatCompletionClient


@dataclass
class ModelConfig:
    model_id: str
    model: str
    model_type: Literal["chat", "image", "embedding"]
    api_type: Literal["open_ai", "azure"]


@dataclass
class ModelConfigChatOpenAI(ModelConfig):
    api_key: str
    model_type: Literal["chat"]
    api_type: Literal["open_ai"]
    base_url: HttpUrl | None = None
    temperature: float | None = None
    reasoning_effort: Literal["low", "medium", "high"] | None = None
    reasoning: dict | None = None
    max_output_tokens: int | None = None
    model_info: dict | None = None
    _streaming_support: bool | None = True
    _tool_support: bool | None = True
    _json_support: bool | None = True
    _system_prompt_support: bool | None = True
    _temperature_support: bool | None = None
    _structured_output_support: bool | None = None
    _image_input_support: bool | None = False
    _reasoning_support: bool | None = False
    _max_output: int | None = None
    _max_context: int | None = None
    _cost_input: float | None = None
    _cost_output: float | None = None


@dataclass
class ModelConfigChatAzure(ModelConfig):
    api_key: str
    azure_deployment: str
    api_version: str
    azure_endpoint: HttpUrl
    model_type: Literal["chat"]
    api_type: Literal["azure"]
    temperature: float | None = None
    reasoning_effort: Literal["low", "medium", "high"] | None = None
    reasoning: dict | None = None
    max_output_tokens: int | None = None
    _streaming_support: bool | None = True
    _tool_support: bool | None = True
    _json_support: bool | None = True
    _system_prompt_support: bool | None = True
    _temperature_support: bool | None = True
    _structured_output_support: bool | None = None
    _image_input_support: bool | None = False
    _reasoning_support: bool | None = False
    _max_output: int | None = None
    _max_context: int | None = None
    _cost_input: float | None = None
    _cost_output: float | None = None


@dataclass
class ModelConfigImageOpenAI(ModelConfig):
    api_key: str
    size: str
    quality: str
    num_images: int
    model_type: Literal["image"]
    api_type: Literal["open_ai"]
    _cost_input: float | None = None
    _cost_output: float | None = None
    _temperature_support: bool | None = None
    _image_edit_support: bool | None = False
    _inpainting_support: bool | None = False
    _streaming_support: bool | None = False
    _tool_support: bool | None = False
    _system_prompt_support: bool | None = False


@dataclass
class ModelConfigImageAzure(ModelConfig):
    api_key: str
    azure_deployment: str
    api_version: str
    azure_endpoint: HttpUrl
    size: str
    quality: str
    num_images: int
    model_type: Literal["image"]
    api_type: Literal["azure"]
    _cost_input: float | None = None
    _cost_ouput: float | None = None
    _temperature_support: bool | None = None
    _image_edit_support: bool | None = False
    _inpainting_support: bool | None = False
    _streaming_support: bool | None = False
    _tool_support: bool | None = False
    _system_prompt_support: bool | None = False


@dataclass
class ModelConfigEmbeddingOpenAI(ModelConfig):
    model_type: Literal["embedding"]
    api_type: Literal["open_ai"]
    api_key: str
    _cost_input: float | None = None
    _cost_output: float | None = None
    _temperature_support: bool | None = False
    _streaming_support: bool | None = False
    _tool_support: bool | None = False
    _system_prompt_support: bool | None = False


@dataclass
class ModelConfigEmbeddingAzure(ModelConfig):
    model_type: Literal["embedding"]
    api_type: Literal["azure"]
    api_key: str
    azure_deployment: str
    api_version: str
    azure_endpoint: HttpUrl
    _cost_input: float | None = None
    _cost_output: float | None = None
    _temperature_support: bool | None = None
    _streaming_support: bool | None = False
    _tool_support: bool | None = False
    _system_prompt_support: bool | None = False


class DallEAPIWrapper:
    def __init__(
        self,
        api_key: str | None = None,
        num_images: int = 1,
        size: str = "1024x1024",
        separator: str = "\n",
        model: str | None = "dall-e-2",
        quality: str | None = "standard",
        **kwargs,
    ):
        self.api_key = api_key
        self.num_images = num_images
        self.size = size
        self.separator = separator
        self.model = model
        self.quality = quality
        self.client = OpenAI(api_key=self.api_key)

    def run(self, query: str) -> str:
        try:
            response = self.client.images.generate(
                prompt=query,
                n=self.num_images,
                size=self.size,
                model=self.model,
                quality=self.quality,
                response_format="url",
            )
            image_urls = self.separator.join([item.url for item in response.data])
            return image_urls if image_urls else "No image was generated"
        except Exception as e:
            return f"Image Generation Error: {str(e)}"

    async def arun(self, query: str) -> str:
        try:
            response = await asyncio.to_thread(
                lambda: self.client.images.generate(
                    prompt=query,
                    n=self.num_images,
                    size=self.size,
                    model=self.model,
                    quality=self.quality,
                    response_format="url",
                )
            )
            image_urls = self.separator.join([item.url for item in response.data])
            return image_urls if image_urls else "No image was generated"
        except Exception as e:
            return f"Image Generation Error: {str(e)}"


class ModelManager:
    def __init__(
        self,
        settings_files: list[str] | None = None,
        settings_conf: Dynaconf | None = None,
    ):
        """Initialize the ModelManager with settings files or optional config.
        Args:
            settings_files (list[str], optional): List of paths to settings files.
            settings_conf (Dynaconf, optional): Dynaconf settings.
        """

        # ensure only one of settings_files or config is provided, or both are None
        if settings_files is not None and settings_conf is not None:
            raise ValueError(
                "You can only provide either settings_files or settings_conf, not both."
            )
        try:
            if settings_conf:
                # make deep copy of settings_conf to avoid modifying the original
                settings = copy.deepcopy(settings_conf)
            else:
                settings = _config.get_settings(settings_files=settings_files)

            self.model_configs = settings["models"].to_dict()
            self.config: dict[str, ModelConfig] = {}
        except AttributeError as e:
            missing_attr = str(e).split("'")[-2]
            error_message = (
                f"Missing required setting: '{missing_attr}'. "
                "Please add it to your settings file."
            )
            raise RuntimeError(error_message) from e
        except DynaconfFormatError as e:
            if "has no attribute" in str(e):
                missing_attr = str(e).split("'")[-2]
                error_message = (
                    f"Missing required setting: '{missing_attr}'. "
                    "Please add it to your settings or secrets file."
                )
                raise RuntimeError(error_message) from e
            else:
                raise RuntimeError(f"Dynaconf encountered an error: {e}") from e

        model_types = {
            "chat": {"open_ai": ModelConfigChatOpenAI, "azure": ModelConfigChatAzure},
            "image": {
                "open_ai": ModelConfigImageOpenAI,
                "azure": ModelConfigImageAzure,
            },
            "embedding": {
                "open_ai": ModelConfigEmbeddingOpenAI,
                "azure": ModelConfigEmbeddingAzure,
            },
        }

        """loop over all model configs in the TOML, for every model type and every
        model entry. For each model, determine the correct Python dataclass to
        instantiate (chat/image/embedding, openai/azure), and then creates an instance
        of that dataclass with all config values. Store each dataclass instance in
        the self.config dictionary, keyed by model_id, so later code like
        self.config[model_id] fetches the correct config object for that model.
        """
        for model_type in self.model_configs.keys():
            for model_id, model_config in self.model_configs[model_type].items():
                self.config[model_id] = model_types[model_type][
                    model_config["api_type"]
                ](model_id=model_id, model_type=model_type, **model_config)

        self.azure_token_provider = None
        # set the token provider if there is at least one azure model
        for azure_model in self.filter_models({"api_type": ["azure"]}):
            if self.config[azure_model].api_key == "provider":
                self.azure_token_provider = AzureADTokenProvider(
                    tenant_id=settings.get("azure_tenant_id"),
                    client_id=settings.get("azure_client_id"),
                    client_secret=settings.get("azure_client_id_secret"),
                )
                break

        self.default_chat_model = settings.defaults.chat_model
        self.default_image_model = settings.get("defaults.image_model", None)
        self.default_embedding_model = settings.get("defaults.embedding_model", None)
        self.default_chat_temperature = settings.defaults.chat_temperature
        # Mini model for internal utilities; fall back to chat model if unset
        self.default_mini_model = (
            settings.get("defaults.mini_model", None) or self.default_chat_model
        )

    def filter_models(self, filter_dict):
        return [
            key
            for key, value in self.config.items()
            if all(getattr(value, k) in v for k, v in filter_dict.items())
        ]

    def open_model(self, model_id: str, **kwargs) -> ChatCompletionClient:
        logger.debug(f"Opening model {model_id}")
        record = copy.deepcopy(self.config[model_id])
        model_kwargs = {
            **{
                field.name: getattr(record, field.name)
                for field in fields(record)
                if not field.name.startswith("_")
            },
            **kwargs,
        }
        model_kwargs.pop("api_type")
        model_kwargs.pop("model_type")

        if record.api_type == "azure" and model_kwargs["api_key"] == "provider":
            model_kwargs["azure_ad_token_provider"] = self.azure_token_provider
            model_kwargs.pop("api_key")

        if record.model_type == "chat":
            temp_support = getattr(record, "_temperature_support", True)
            if temp_support is False:
                # Model does not support temperature; ensure it's not passed
                model_kwargs.pop("temperature", None)
            elif temp_support is True:
                # Model supports temperature; default if unset or None
                if model_kwargs.get("temperature") is None:
                    model_kwargs["temperature"] = self.default_chat_temperature

            # Reasoning controls: prefer reasoning_effort; map legacy reasoning
            legacy_reasoning = model_kwargs.get("reasoning")
            if model_kwargs.get("reasoning_effort") is None and isinstance(
                legacy_reasoning, dict
            ):
                effort = legacy_reasoning.get("effort")
                if effort in ("low", "medium", "high"):
                    model_kwargs["reasoning_effort"] = effort
            # remove legacy field
            model_kwargs.pop("reasoning", None)

            # Enable reasoning when declared supported OR effort provided
            has_effort = model_kwargs.get("reasoning_effort") is not None
            reasoning_support = (
                getattr(record, "_reasoning_support", False) or has_effort
            )
            if reasoning_support:
                if model_kwargs.get("reasoning_effort") is None:
                    model_kwargs.pop("reasoning_effort", None)
                if model_kwargs.get("max_output_tokens") is None:
                    model_kwargs.pop("max_output_tokens", None)
            else:
                model_kwargs.pop("reasoning_effort", None)
                model_kwargs.pop("max_output_tokens", None)

            if record.api_type == "open_ai":
                return OpenAIChatCompletionClient(**model_kwargs)
            elif record.api_type == "azure":
                return AzureOpenAIChatCompletionClient(**model_kwargs)
        elif record.model_type == "image":
            return DallEAPIWrapper(**model_kwargs)

        raise ValueError("Invalid model_type")

    @staticmethod
    async def aask(question: str, model: str = None, system_prompt: str = None) -> str:
        """Asks a question to the model and returns the response."""
        mm = ModelManager()
        if model is None:
            model = mm.default_chat_model
        client = mm.open_model(model)
        if system_prompt:
            out = await client.create(
                [
                    SystemMessage(content=system_prompt),
                    UserMessage(content=question, source="user"),
                ]
            )
        else:
            out = await client.create([UserMessage(content=question, source="user")])
        return out.content

    @staticmethod
    def ask(question: str, model: str = None, system_prompt: str = None) -> str:
        """Asks a question to the model and returns the response."""
        return AsyncRunner.run_sync(ModelManager.aask(question, model, system_prompt))

    def get_streaming_support(self, model_id: str) -> bool:
        return self.config[model_id]._streaming_support

    def get_tool_support(self, model_id: str) -> bool:
        return self.config[model_id]._tool_support

    def get_system_prompt_support(self, model_id: str) -> bool:
        return self.config[model_id]._system_prompt_support

    def get_temperature_support(self, model_id: str) -> bool:
        return self.config[model_id]._temperature_support

    def get_structured_output_support(self, model_id: str) -> bool:
        return self.config[model_id]._structured_output_support

    def get_compatible_models(self, agent: str, agents: dict) -> list:
        filter = {"model_type": ["chat"]}
        if "tools" in agents[agent]:
            filter["_tool_support"] = [True]
        return self.filter_models(filter)

    @property
    def available_image_models(self) -> list:
        return self.filter_models({"model_type": ["image"]})

    @property
    def available_chat_models(self) -> list:
        return self.filter_models({"model_type": ["chat"]})

    @property
    def available_embedding_models(self) -> list:
        return self.filter_models({"model_type": ["embedding"]})


class AsyncRunner:
    _executor = None

    @classmethod
    def run_sync(cls, coro):
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(coro)
        else:
            if cls._executor is None:
                cls._executor = ThreadPoolExecutor()

            def runner():
                return asyncio.run(coro)

            return cls._executor.submit(runner).result()
