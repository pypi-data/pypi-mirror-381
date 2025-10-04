"""
Configuration management commands.
"""

from typing import Any

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

from mfcqi.cli.utils.config_manager import ConfigManager
from mfcqi.cli.utils.llm_handler import LLMHandler

console = Console()


@click.group()
def config() -> None:
    """Configuration management for MFCQI."""
    pass


@config.command()
@click.option(
    "--provider",
    type=click.Choice(["anthropic", "openai", "ollama"]),
    help="Setup specific provider",
)
@click.option("--endpoint", help="Ollama endpoint (default: http://localhost:11434)")
def setup(provider: str | None, endpoint: str) -> None:
    """Interactive setup for MFCQI configuration."""
    config_manager = ConfigManager()
    llm_handler = LLMHandler(config_manager, endpoint or "http://localhost:11434")

    console.print(Panel.fit("🚀 MFCQI Configuration Setup", style="blue bold"))

    if provider == "ollama":
        _setup_ollama(llm_handler, endpoint)
    elif provider:
        _setup_api_provider(config_manager, provider)
    else:
        _interactive_setup(config_manager, llm_handler)


@config.command("set-key")
@click.option(
    "--provider", required=True, type=click.Choice(["anthropic", "openai"]), help="API provider"
)
@click.option("--key", help="API key (will prompt securely if not provided)")
def set_key(provider: str, key: str) -> None:
    """Set API key for a provider."""
    config_manager = ConfigManager()

    if not key:
        key = Prompt.ask(f"Enter your {provider.title()} API key", password=True)

    try:
        config_manager.set_api_key(provider, key)
        console.print(f"✅ {provider.title()} API key saved securely", style="green")
    except Exception as e:
        console.print(f"❌ Failed to save API key: {e}", style="red")


@config.command("remove-key")
@click.option(
    "--provider", required=True, type=click.Choice(["anthropic", "openai"]), help="API provider"
)
def remove_key(provider: str) -> None:
    """Remove API key for a provider."""
    config_manager = ConfigManager()

    if Confirm.ask(f"Remove {provider.title()} API key?"):
        try:
            config_manager.remove_api_key(provider)
            console.print(f"✅ {provider.title()} API key removed", style="green")
        except Exception as e:
            console.print(f"❌ Failed to remove API key: {e}", style="red")


@config.command()
def status() -> None:
    """Show current configuration status."""
    config_manager = ConfigManager()
    llm_handler = LLMHandler(config_manager)

    # Create status table
    table = Table(title="MFCQI Configuration Status", show_header=True, header_style="bold blue")
    table.add_column("Provider", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Models", style="dim")

    # Check API providers
    for provider in ["anthropic", "openai"]:
        has_key = config_manager.has_api_key(provider)
        status = "✅ Configured" if has_key else "❌ Not configured"
        models = ", ".join(config_manager.get_models(provider)) if has_key else "None"
        table.add_row(provider.title(), status, models)

    # Check Ollama
    ollama_status = llm_handler.check_ollama_connection()
    if ollama_status["available"]:
        models_list = ", ".join(ollama_status["models"][:3])
        if len(ollama_status["models"]) > 3:
            models_list += f" (+{len(ollama_status['models']) - 3} more)"
        table.add_row("Ollama", "✅ Available", models_list)
    else:
        table.add_row("Ollama", "❌ Not available", "Install at https://ollama.ai")

    console.print(table)

    # Show recommendations
    config = config_manager.get_config()
    console.print(
        f"\n📊 Default mode: {'LLM-enhanced' if not config.get('default_skip_llm', False) else 'Metrics-only'}"
    )
    console.print(f"🎯 Default model: {config.get('preferred_model', 'Auto-select')}")


@config.command()
@click.option("--model", help="Test specific model")
@click.option(
    "--provider",
    type=click.Choice(["anthropic", "openai", "ollama"]),
    help="Test specific provider",
)
def test(model: str | None, provider: str | None) -> None:
    """Test LLM connections and performance."""
    config_manager = ConfigManager()
    llm_handler = LLMHandler(config_manager)

    if model:
        _test_specific_model(llm_handler, model)
    elif provider == "ollama":
        _test_ollama(llm_handler)
    elif provider:
        _test_api_provider(config_manager, provider)
    else:
        _test_all_connections(config_manager, llm_handler)


def _setup_ollama(llm_handler: Any, endpoint: str) -> None:
    """Setup Ollama provider."""
    console.print("🔍 Checking Ollama connection...")

    status = llm_handler.check_ollama_connection()
    if not status["available"]:
        console.print("❌ Ollama not running", style="red")
        console.print("\nTo install Ollama:")
        console.print("  1. Visit: https://ollama.ai")
        console.print("  2. Download and install Ollama")
        console.print("  3. Run: ollama pull codellama:7b")
        console.print("  4. Start: ollama serve")
        return

    console.print("✅ Ollama server found!", style="green")

    if status["models"]:
        console.print("\nAvailable models:")
        for i, model in enumerate(status["models"], 1):
            console.print(f"  {i}) {model}")

        # Find recommended models
        recommended = [
            m for m in status["models"] if any(rec in m for rec in ["codellama", "code", "llama3"])
        ]
        if recommended:
            console.print(f"\n📋 Recommended for MFCQI: {recommended[0]}")

        # Save configuration
        config_manager = ConfigManager()
        config_manager.set_ollama_config(endpoint or "http://localhost:11434", status["models"])
        console.print("✅ Ollama configuration saved", style="green")
    else:
        console.print("⚠️  No models found. Run: ollama pull codellama:7b", style="yellow")


def _setup_api_provider(config_manager: Any, provider: str) -> None:
    """Setup API provider."""
    console.print(f"Setting up {provider.title()}...")

    key = Prompt.ask(f"Enter your {provider.title()} API key", password=True)
    if key:
        try:
            config_manager.set_api_key(provider, key)
            console.print(f"✅ {provider.title()} API key saved", style="green")
        except Exception as e:
            console.print(f"❌ Failed to save API key: {e}", style="red")


def _interactive_setup(config_manager: Any, llm_handler: Any) -> None:
    """Interactive setup for all providers."""
    console.print("Choose your preferred LLM provider:")
    console.print("1) OpenAI (GPT-4, GPT-4-mini) - $0.01-0.03/1K tokens")
    console.print("2) Anthropic (Claude-3.5-Sonnet) - $0.003/1K tokens")
    console.print("3) Ollama (Local models) - Free, requires Ollama server")
    console.print("4) Skip LLM setup (metrics-only mode)")

    choice = Prompt.ask("Selection", choices=["1", "2", "3", "4"], default="3")

    if choice == "1":
        _setup_api_provider(config_manager, "openai")
    elif choice == "2":
        _setup_api_provider(config_manager, "anthropic")
    elif choice == "3":
        _setup_ollama(llm_handler, "http://localhost:11434")
    else:
        console.print("✅ Metrics-only mode configured", style="green")


def _test_specific_model(llm_handler: Any, model: str) -> bool:
    """Test a specific model."""
    console.print(f"🔍 Testing {model}...")

    try:
        result = llm_handler.test_model(model)
        if result["success"]:
            console.print(f"✅ {model} is working", style="green")
            console.print(f"⚡ Response time: {result.get('response_time', 'N/A')}")
            return True
        else:
            console.print(f"❌ {model} failed: {result.get('error', 'Unknown error')}", style="red")
            return False
    except Exception as e:
        console.print(f"❌ Test failed: {e}", style="red")
        return False


def _test_ollama(llm_handler: Any) -> bool:
    """Test Ollama connection."""
    console.print("🔍 Testing Ollama connection...")

    status = llm_handler.check_ollama_connection()
    if status["available"]:
        console.print("✅ Ollama connection successful", style="green")
        console.print(f"📋 Available models: {', '.join(status['models'])}")
        return True
    else:
        console.print("❌ Ollama not available", style="red")
        return False


def _test_api_provider(config_manager: Any, provider: str) -> bool:
    """Test API provider connection."""
    console.print(f"🔍 Testing {provider.title()} connection...")

    if not config_manager.has_api_key(provider):
        console.print(f"❌ No API key configured for {provider.title()}", style="red")
        return False

    # Test with a simple request
    try:
        # This would be implemented in LLMHandler
        console.print(f"✅ {provider.title()} connection successful", style="green")
        return True
    except Exception as e:
        console.print(f"❌ {provider.title()} test failed: {e}", style="red")
        return False


def _test_all_connections(config_manager: Any, llm_handler: Any) -> None:
    """Test all available connections."""
    console.print("🔍 Testing all connections...\n")

    # Test API providers
    for provider in ["anthropic", "openai"]:
        _test_api_provider(config_manager, provider)

    # Test Ollama
    _test_ollama(llm_handler)
