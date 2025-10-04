"""
Configuration management for LLM analysis.
"""

import os
from typing import Any

from pydantic import BaseModel


class AnalysisConfig(BaseModel):
    """Configuration for LLM analysis."""

    model: str = "claude-3-5-sonnet-20241022"
    temperature: float = 0.1
    max_tokens: int = 8000
    timeout: int = 60
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    def __init__(self, **kwargs: Any) -> None:
        """Initialize configuration with environment variables."""
        # Load from environment if not provided
        if "model" not in kwargs:
            kwargs["model"] = os.getenv("CQI_LLM_MODEL", "claude-3-5-sonnet-20241022")

        if "openai_api_key" not in kwargs:
            kwargs["openai_api_key"] = os.getenv("OPENAI_API_KEY")

        if "anthropic_api_key" not in kwargs:
            kwargs["anthropic_api_key"] = os.getenv("ANTHROPIC_API_KEY")

        # Validate model and fallback if needed
        supported_models = ["claude-3-5-sonnet-20241022", "gpt-4o", "gpt-4o-mini"]

        if kwargs["model"] not in supported_models:
            kwargs["model"] = "claude-3-5-sonnet-20241022"

        super().__init__(**kwargs)

    def get_api_key_for_model(self, model: str) -> str | None:
        """Get appropriate API key for the given model."""
        if model.startswith("claude"):
            return self.anthropic_api_key
        elif model.startswith("gpt"):
            return self.openai_api_key
        return None

    def validate_config(self) -> None:
        """Validate configuration."""
        api_key = self.get_api_key_for_model(self.model)
        if not api_key:
            raise ValueError(f"No API key found for model {self.model}")

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "timeout": self.timeout,
        }

    @classmethod
    def from_dict(cls, config_dict: dict[str, Any]) -> "AnalysisConfig":
        """Create configuration from dictionary."""
        return cls(**config_dict)

    def get_supported_models(self) -> list[str]:
        """Get list of supported models."""
        return ["claude-3-5-sonnet-20241022", "gpt-4o", "gpt-4o-mini"]

    @classmethod
    def from_environment(cls) -> "AnalysisConfig":
        """Create configuration from environment with model priority."""
        # Check available API keys and select appropriate model
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        openai_key = os.getenv("OPENAI_API_KEY")

        # Priority: Claude > GPT-4o > GPT-4o-mini
        if anthropic_key:
            model = "claude-3-5-sonnet-20241022"
        elif openai_key:
            model = "gpt-4o"
        else:
            model = "claude-3-5-sonnet-20241022"  # Default

        return cls(model=model)

    def get_litellm_config(self) -> dict[str, Any]:
        """Get configuration dictionary for LiteLLM."""
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "timeout": self.timeout,
        }
