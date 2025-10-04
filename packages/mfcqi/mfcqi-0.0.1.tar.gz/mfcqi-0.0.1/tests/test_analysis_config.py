"""
Test for Analysis Configuration - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

from unittest.mock import patch

import pytest


def test_analysis_config_exists():
    """RED: Test that AnalysisConfig class exists."""
    from mfcqi.analysis.config import AnalysisConfig

    assert AnalysisConfig is not None


def test_analysis_config_initialization():
    """RED: Test that AnalysisConfig can be initialized."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig()
    assert config is not None


def test_analysis_config_default_model():
    """RED: Test default model configuration."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig()
    assert config.model == "claude-3-5-sonnet-20241022"


def test_analysis_config_custom_model():
    """RED: Test custom model configuration."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig(model="gpt-4o")
    assert config.model == "gpt-4o"


def test_analysis_config_from_env():
    """RED: Test configuration from environment variables."""
    from mfcqi.analysis.config import AnalysisConfig

    with patch.dict(
        "os.environ",
        {
            "CQI_LLM_MODEL": "gpt-4o-mini",
            "OPENAI_API_KEY": "test-key",
            "ANTHROPIC_API_KEY": "test-key",
        },
    ):
        config = AnalysisConfig()
        assert config.model == "gpt-4o-mini"
        assert config.openai_api_key == "test-key"
        assert config.anthropic_api_key == "test-key"


def test_api_key_loading():
    """RED: Test API key loading from environment."""
    from mfcqi.analysis.config import AnalysisConfig

    with patch.dict(
        "os.environ", {"OPENAI_API_KEY": "sk-test-openai", "ANTHROPIC_API_KEY": "sk-ant-test"}
    ):
        config = AnalysisConfig()
        assert config.openai_api_key == "sk-test-openai"
        assert config.anthropic_api_key == "sk-ant-test"


def test_temperature_configuration():
    """RED: Test temperature configuration."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig(temperature=0.5)
    assert config.temperature == 0.5

    # Test default
    default_config = AnalysisConfig()
    assert default_config.temperature == 0.1


def test_max_tokens_configuration():
    """RED: Test max tokens configuration."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig(max_tokens=2000)
    assert config.max_tokens == 2000

    # Test default (increased to 8000 to support more recommendations)
    default_config = AnalysisConfig()
    assert default_config.max_tokens == 8000


def test_timeout_configuration():
    """RED: Test timeout configuration."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig(timeout=120)
    assert config.timeout == 120

    # Test default
    default_config = AnalysisConfig()
    assert default_config.timeout == 60


def test_model_validation():
    """RED: Test model validation for supported models."""
    from mfcqi.analysis.config import AnalysisConfig

    # Valid models should work
    valid_models = ["claude-3-5-sonnet-20241022", "gpt-4o", "gpt-4o-mini"]

    for model in valid_models:
        config = AnalysisConfig(model=model)
        assert config.model == model


def test_model_fallback():
    """RED: Test model fallback for unsupported models."""
    from mfcqi.analysis.config import AnalysisConfig

    # Should fallback to default for unsupported models
    config = AnalysisConfig(model="unsupported-model")
    assert config.model == "claude-3-5-sonnet-20241022"  # Default fallback


def test_get_api_key_for_model():
    """RED: Test getting appropriate API key for model."""
    from mfcqi.analysis.config import AnalysisConfig

    with patch.dict(
        "os.environ", {"OPENAI_API_KEY": "openai-key", "ANTHROPIC_API_KEY": "anthropic-key"}
    ):
        config = AnalysisConfig()

        # Claude model should return Anthropic key
        claude_key = config.get_api_key_for_model("claude-3-5-sonnet-20241022")
        assert claude_key == "anthropic-key"

        # GPT model should return OpenAI key
        gpt_key = config.get_api_key_for_model("gpt-4o")
        assert gpt_key == "openai-key"


def test_validate_configuration():
    """RED: Test configuration validation."""
    from mfcqi.analysis.config import AnalysisConfig

    with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key", "ANTHROPIC_API_KEY": "test-key"}):
        config = AnalysisConfig()

        # Should not raise exception for valid config
        config.validate_config()

        # Should raise exception if no API key for selected model
        config.openai_api_key = None
        config.anthropic_api_key = None

        with pytest.raises(ValueError):
            config.validate_config()


def test_config_to_dict():
    """RED: Test configuration serialization to dict."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig(model="gpt-4o", temperature=0.3, max_tokens=1000)

    config_dict = config.to_dict()

    assert isinstance(config_dict, dict)
    assert config_dict["model"] == "gpt-4o"
    assert config_dict["temperature"] == 0.3
    assert config_dict["max_tokens"] == 1000


def test_config_from_dict():
    """RED: Test configuration creation from dict."""
    from mfcqi.analysis.config import AnalysisConfig

    config_dict = {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.2,
        "max_tokens": 2000,
        "timeout": 90,
    }

    config = AnalysisConfig.from_dict(config_dict)

    assert config.model == "claude-3-5-sonnet-20241022"
    assert config.temperature == 0.2
    assert config.max_tokens == 2000
    assert config.timeout == 90


def test_default_models_list():
    """RED: Test default models list."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig()
    models = config.get_supported_models()

    assert isinstance(models, list)
    assert "claude-3-5-sonnet-20241022" in models
    assert "gpt-4o" in models
    assert "gpt-4o-mini" in models


def test_model_priority():
    """RED: Test model priority selection."""
    from mfcqi.analysis.config import AnalysisConfig

    # Should select first available model based on API keys
    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test-key"}, clear=True):
        config = AnalysisConfig.from_environment()
        assert config.model.startswith("claude")

    with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}, clear=True):
        config = AnalysisConfig.from_environment()
        assert config.model.startswith("gpt")


def test_litellm_config():
    """RED: Test LiteLLM configuration generation."""
    from mfcqi.analysis.config import AnalysisConfig

    config = AnalysisConfig(model="gpt-4o", temperature=0.3)
    litellm_config = config.get_litellm_config()

    assert isinstance(litellm_config, dict)
    assert litellm_config["model"] == "gpt-4o"
    assert litellm_config["temperature"] == 0.3
    assert "messages" not in litellm_config  # Should not include messages
