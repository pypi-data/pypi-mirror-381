"""Helper functions for the analyze command."""

import json
from pathlib import Path
from typing import Any

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

from mfcqi.calculator import MFCQICalculator
from mfcqi.cli.utils.llm_handler import LLMHandler
from mfcqi.cli.utils.output import (
    format_analysis_output,
    format_json_output,
    format_sarif_output,
)

console = Console()


def calculate_metrics(
    path: Path,
    calculator: MFCQICalculator,
    need_tool_outputs: bool,
    silent: bool,
) -> tuple[dict[str, Any], dict[str, Any], float]:
    """Calculate metrics with optional tool outputs.

    Returns:
        Tuple of (detailed_metrics, tool_outputs, elapsed_time)
    """
    import time

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        console=console,
        disable=silent,
    ) as progress:
        task = progress.add_task("🔍 Analyzing codebase...", total=None)
        start_time = time.time()

        if need_tool_outputs:
            progress.update(
                task,
                description="📊 Calculating metrics...",
            )
            detailed_data = calculator.get_detailed_metrics_with_tool_outputs(path)
            detailed_metrics = detailed_data.get("metrics", {})
            detailed_metrics["mfcqi_score"] = detailed_data.get("mfcqi_score", 0.0)
            tool_outputs = detailed_data.get("tool_outputs", {})
        else:
            progress.update(task, description="📊 Calculating metrics...")
            detailed_metrics = calculator.get_detailed_metrics(path)
            tool_outputs = {}

        elapsed = time.time() - start_time
        cqi_score = detailed_metrics.get("mfcqi_score", 0.0)

        if not silent:
            progress.update(
                task,
                description=f"✅ Metrics calculated (MFCQI Score: {cqi_score:.2f}) in {elapsed:.1f}s",
            )

    return detailed_metrics, tool_outputs, elapsed


def get_llm_recommendations(
    path: str,
    detailed_metrics: dict[str, Any],
    tool_outputs: dict[str, Any],
    llm_handler: LLMHandler,
    model: str | None,
    provider: str | None,
    recommendations: int,
    silent: bool,
) -> dict[str, Any] | None:
    """Get LLM recommendations if available.

    Returns:
        Dictionary with recommendations or None
    """
    # Determine model to use
    selected_model = llm_handler.select_model(model, provider, silent)

    if not selected_model:
        if not silent:
            console.print("i  Analysis complete (metrics-only mode - no LLM configured)")
            console.print("💡 To get AI recommendations, run: mfcqi config setup")
        return None

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        disable=silent,
    ) as progress:
        task = progress.add_task("✨ Generating recommendations...", total=None)

        # Get LLM analysis
        llm_result = llm_handler.analyze_with_llm(
            path, detailed_metrics, selected_model, recommendations, tool_outputs
        )

        if llm_result:
            llm_result["model_used"] = selected_model
            if not silent:
                progress.update(task, description="✅ AI recommendations generated")

        return llm_result


def prepare_analysis_result(detailed_metrics: dict[str, Any]) -> dict[str, Any]:
    """Prepare the initial analysis result structure."""
    cqi_score = detailed_metrics.get("mfcqi_score", 0.0)

    return {
        "mfcqi_score": cqi_score,
        "metric_scores": {k: v for k, v in detailed_metrics.items() if k != "mfcqi_score"},
        "diagnostics": [],
        "recommendations": [],
        "model_used": "metrics-only",
    }


def output_results(
    analysis_result: dict[str, Any],
    output_format: str,
    output: Path | None,
    silent: bool,
) -> None:
    """Format and output analysis results."""
    # Format data
    from typing import Union

    from rich.panel import Panel

    output_data: Union[dict[str, Any], str, Panel]
    if output_format == "json":
        output_data = format_json_output(analysis_result)
    elif output_format == "sarif":
        output_data = format_sarif_output(analysis_result)
    else:
        output_data = format_analysis_output(analysis_result, output_format)

    # Write to file or console
    if output:
        if isinstance(output_data, (str, Panel)):
            output.write_text(str(output_data))
        else:
            output.write_text(json.dumps(output_data, indent=2))
        if not silent:
            console.print(f"📄 Report saved to: {output}")
    else:
        if output_format in ("json", "sarif") and isinstance(output_data, dict):
            click.echo(json.dumps(output_data, indent=2))
        else:
            console.print(output_data)


def check_minimum_score(cqi_score: float, min_score: float | None, silent: bool) -> bool:
    """Check if score meets minimum requirement."""
    if min_score is not None and cqi_score < min_score:
        if not silent:
            console.print(f"❌ MFCQI score {cqi_score:.2f} below minimum {min_score}", style="red")
        return False
    return True
