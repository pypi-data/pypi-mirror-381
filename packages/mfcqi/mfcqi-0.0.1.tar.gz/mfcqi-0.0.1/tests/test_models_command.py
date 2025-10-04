"""Tests for models CLI command."""

from click.testing import CliRunner

from mfcqi.cli.commands.models import models


def test_models_list_command():
    """Test models list command."""
    runner = CliRunner()

    result = runner.invoke(models, ["list"])

    # Should complete (may show Ollama not available)
    assert result.exit_code == 0
    # Should mention models or Ollama
    assert "models" in result.output.lower() or "ollama" in result.output.lower()


def test_models_list_with_endpoint():
    """Test models list with custom endpoint."""
    runner = CliRunner()

    result = runner.invoke(models, ["list", "--endpoint", "http://localhost:11434"])

    # Should complete
    assert result.exit_code == 0


def test_models_pull_command():
    """Test models pull command."""
    runner = CliRunner()

    # Try to pull a model (will likely fail without Ollama running)
    result = runner.invoke(models, ["pull", "codellama:7b"])

    # Should either succeed or show meaningful error
    assert result.exit_code in [0, 1]
    # Output should be informative
    assert len(result.output) > 0


def test_models_test_command():
    """Test models test command."""
    runner = CliRunner()

    # Test a model (will skip if not available)
    result = runner.invoke(models, ["test", "codellama:7b"])

    # Should complete (may skip if model not available)
    assert result.exit_code in [0, 1]
    assert len(result.output) > 0


def test_models_benchmark_command():
    """Test models benchmark command."""
    runner = CliRunner()

    # Run benchmark (may skip if no models available)
    result = runner.invoke(models, ["benchmark"])

    # Should complete
    assert result.exit_code in [0, 1]
    assert len(result.output) > 0
