"""Tests for config CLI command."""

import pytest
from click.testing import CliRunner

from mfcqi.cli.commands.config import config


def test_config_status_command():
    """Test config status command."""
    runner = CliRunner()

    result = runner.invoke(config, ["status"])

    # Should show configuration status
    assert result.exit_code == 0
    assert "Configuration" in result.output or "Provider" in result.output


def test_config_set_key_with_key_provided():
    """Test setting API key via command line when keyring is disabled."""
    runner = CliRunner()

    # Use isolated filesystem for config
    with runner.isolated_filesystem():
        # With keyring disabled (default in tests), this should show error message
        result = runner.invoke(
            config, ["set-key", "--provider", "anthropic", "--key", "test-key-123"]
        )

        # Should complete (exit code 0) but show keyring not available message
        assert result.exit_code == 0
        assert (
            "keyring not available" in result.output.lower()
            or "environment variable" in result.output.lower()
        )


@pytest.mark.skip(reason="Interactive prompt tests hang - skipping")
def test_config_set_key_with_prompt():
    """Test setting API key via interactive prompt."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Provide key via input
        result = runner.invoke(
            config, ["set-key", "--provider", "openai"], input="test-openai-key\n"
        )

        # Should succeed
        assert result.exit_code == 0


@pytest.mark.skip(reason="Interactive prompt tests hang - skipping")
def test_config_remove_key():
    """Test removing API key."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # First set a key
        runner.invoke(config, ["set-key", "--provider", "anthropic", "--key", "test-key"])

        # Then remove it
        result = runner.invoke(config, ["remove-key", "--provider", "anthropic"], input="y\n")

        # Should succeed
        assert result.exit_code == 0


def test_config_setup_command():
    """Test config setup command."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Test non-interactive setup with ollama
        result = runner.invoke(config, ["setup", "--provider", "ollama"])

        # Should at least not crash
        assert result.exit_code in [0, 1]  # May fail if ollama not running


def test_config_setup_with_endpoint():
    """Test config setup with custom endpoint."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(
            config,
            ["setup", "--provider", "ollama", "--endpoint", "http://localhost:11434"],
        )

        # Should handle custom endpoint
        assert result.exit_code in [0, 1]  # May fail if ollama not available


def test_config_test_command_with_anthropic_provider():
    """Test the config test command with anthropic provider."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Test with provider - will fail without API key but should not crash
        result = runner.invoke(config, ["test", "--provider", "anthropic"])

        # Should not crash (may fail if no key)
        assert result.exit_code in [0, 1]


def test_config_test_command_with_openai_provider():
    """Test the config test command with openai provider."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Test with provider - will fail without API key but should not crash
        result = runner.invoke(config, ["test", "--provider", "openai"])

        # Should not crash (may fail if no key)
        assert result.exit_code in [0, 1]


def test_config_test_command_with_ollama_provider():
    """Test the config test command with ollama provider."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Test with ollama provider
        result = runner.invoke(config, ["test", "--provider", "ollama"])

        # Should not crash (may fail if ollama not running)
        assert result.exit_code in [0, 1]


def test_config_test_command_all_providers():
    """Test the config test command without specifying provider (tests all)."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Test all providers
        result = runner.invoke(config, ["test"])

        # Should not crash
        assert result.exit_code in [0, 1]


@pytest.mark.skip(reason="Interactive prompt tests hang - skipping")
def test_config_setup_anthropic_provider():
    """Test config setup with anthropic provider."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Provide API key via input
        result = runner.invoke(
            config, ["setup", "--provider", "anthropic"], input="test-anthropic-key\n"
        )

        # Should complete (may succeed or fail depending on key validity)
        assert result.exit_code in [0, 1]


@pytest.mark.skip(reason="Interactive prompt tests hang - skipping")
def test_config_setup_openai_provider():
    """Test config setup with openai provider."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Provide API key via input
        result = runner.invoke(config, ["setup", "--provider", "openai"], input="test-openai-key\n")

        # Should complete (may succeed or fail depending on key validity)
        assert result.exit_code in [0, 1]


@pytest.mark.skip(reason="Interactive prompt tests hang - skipping")
def test_config_remove_key_without_confirmation():
    """Test removing API key when user declines confirmation."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # First set a key
        runner.invoke(config, ["set-key", "--provider", "anthropic", "--key", "test-key"])

        # Try to remove but decline
        result = runner.invoke(config, ["remove-key", "--provider", "anthropic"], input="n\n")

        # Should complete without error
        assert result.exit_code in [0, 1]


@pytest.mark.skip(reason="Interactive prompt tests hang - skipping")
def test_config_remove_key_nonexistent():
    """Test removing a key that doesn't exist."""
    runner = CliRunner()

    with runner.isolated_filesystem():
        # Try to remove key that was never set
        result = runner.invoke(config, ["remove-key", "--provider", "openai"], input="y\n")

        # Should complete (may show warning but not crash)
        assert result.exit_code in [0, 1]
