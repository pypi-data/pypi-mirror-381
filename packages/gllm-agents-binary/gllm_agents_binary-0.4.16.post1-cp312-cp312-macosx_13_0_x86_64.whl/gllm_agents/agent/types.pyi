from _typeshed import Incomplete
from a2a.types import AgentCard as AgentCard
from enum import StrEnum
from gllm_core.utils.retry import RetryConfig as RetryConfig
from pydantic import BaseModel
from typing import Any

class CredentialType(StrEnum):
    """Credential type enumeration for type safety and better developer experience.

    This enum defines the supported credential formats for language models:
    - API_KEY: String-based API keys (most common)
    - FILE: File paths to credential files (e.g., Google service account JSON)
    - DICT: Dictionary-based credentials (e.g., AWS Bedrock, LangChain)
    """
    API_KEY = 'api_key'
    FILE = 'file'
    DICT = 'dict'

class StreamMode(StrEnum):
    """LangGraph stream modes for astream operations.

    These modes control what data is included in the streaming output.
    """
    VALUES = 'values'
    CUSTOM = 'custom'

class HttpxClientOptions(BaseModel):
    """Options for the HTTP client.

    Args:
        timeout: The timeout for the HTTP client in seconds.
        trust_env: Whether to trust environment variables for proxy configuration.
        follow_redirects: Whether to automatically follow HTTP redirects.
    """
    timeout: float
    trust_env: bool
    follow_redirects: bool
    model_config: Incomplete
    class Config:
        """Pydantic v1 fallback config for HttpxClientOptions."""
        extra: str

class A2AClientConfig(BaseModel):
    """Configuration for A2A client.

    Args:
        discovery_urls: A list of base URLs to discover agents from using .well-known/agent.json.
        known_agents: A dictionary of known agents, keyed by AgentCard.name,
                      storing the parsed AgentCard objects. Can be pre-populated or
                      augmented by discovery.
        httpx_client_options: Options for the HTTP client.
    """
    discovery_urls: list[str] | None
    known_agents: dict[str, AgentCard]
    httpx_client_options: HttpxClientOptions | None

class BaseAgentConfig(BaseModel):
    """Base configuration for agent implementations.

    This class provides common configuration fields that all agent implementations
    can use. It serves as a foundation for more specific configuration classes.

    Args:
        tools: List of tools available to the agent.
        default_hyperparameters: Default hyperparameters for the language model.
    """
    tools: list[Any] | None
    default_hyperparameters: dict[str, Any] | None
    model_config: Incomplete
    class Config:
        """Pydantic v1 fallback config for BaseAgentConfig."""
        extra: str

class AgentConfig(BaseAgentConfig):
    '''Configuration for agent implementations with language model settings.

    This class extends BaseAgentConfig with language model specific configuration
    fields including provider, model name, API settings, and hyperparameters.

    Args:
        lm_name: The name of the language model to use.
        lm_hyperparameters: Hyperparameters for the language model.
        lm_provider: The provider of the language model (e.g., \'openai\', \'google\').
        lm_base_url: The base URL for the language model API.
        lm_api_key: The API key for the language model service (deprecated in favor of lm_credentials).
        lm_credentials: Enhanced credentials field supporting multiple formats with automatic type detection:

            Supported Formats:
            - str (API Key): "sk-proj-abc123..." → Auto-detected as API key
            - str (File Path): "/path/to/creds.json" → Auto-detected as file if exists
            - dict (Structured): {"access_key_id": "...", "secret_access_key": "..."} → Auto-detected as dict

            Provider Examples:
            - OpenAI: "sk-proj-abc123xyz"
            - Anthropic: "sk-ant-api03-abc123xyz"
            - Google Vertex AI: "/path/to/service-account.json"
            - AWS Bedrock: {"access_key_id": "AKIA...", "secret_access_key": "secret..."}
            - LangChain: {"api_key": "sk-123", "other_setting": "value"}

            Migration from lm_api_key:
            - Old: AgentConfig(lm_api_key="sk-123")
            - New: AgentConfig(lm_credentials="sk-123")  # Same behavior, auto-detected

        lm_retry_config: Retry configuration for the language model.
    '''
    lm_name: str | None
    lm_hyperparameters: dict[str, Any] | None
    lm_provider: str | None
    lm_base_url: str | None
    lm_api_key: str | None
    lm_credentials: str | dict[str, Any] | None
    lm_retry_config: RetryConfig | None

class LangflowAgentConfig(BaseAgentConfig):
    '''Configuration for Langflow agent implementations.

    This class extends BaseAgentConfig with Langflow-specific configuration
    fields for flow execution, API communication, and session management.

    Args:
        flow_id: The unique identifier of the Langflow flow to execute.
        base_url: The base URL of the Langflow API server. Defaults to environment variable
                 LANGFLOW_BASE_URL or "https://langflow.obrol.id".
        api_key: The API key for Langflow authentication. Supports credential auto-detection.
        httpx_client_options: HTTP client configuration options for httpx, including timeout.
    '''
    flow_id: str
    base_url: str | None
    api_key: str | None
    model_config: Incomplete
    class Config:
        """Pydantic v1 fallback config for LangflowAgentConfig."""
        extra: str
