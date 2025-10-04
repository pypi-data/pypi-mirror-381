"""
Quality Gates implementation for MFCQI.
Allows projects to define minimum quality thresholds that must be met.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class QualityGateConfig:
    """Configuration for quality gates."""

    overall_gates: dict[str, float] = field(default_factory=dict)
    metric_gates: dict[str, float] = field(default_factory=dict)

    @classmethod
    def from_file(cls, config_path: Path) -> "QualityGateConfig":
        """Load quality gate configuration from YAML file."""
        with open(config_path) as f:
            config_data = yaml.safe_load(f)

        if not config_data or "quality_gates" not in config_data:
            raise ValueError("Configuration file must contain 'quality_gates' section")

        gates_config = config_data["quality_gates"]

        return cls(
            overall_gates=gates_config.get("overall", {}),
            metric_gates=gates_config.get("metrics", {}),
        )

    @classmethod
    def from_defaults(cls) -> "QualityGateConfig":
        """Create quality gate config with sensible defaults."""
        return cls(
            overall_gates={
                "mfcqi_score": 0.6,  # Minimum overall score
            },
            metric_gates={
                "security": 0.8,  # High bar for security
                "cyclomatic_complexity": 0.7,
                "cognitive_complexity": 0.7,
                "maintainability_index": 0.7,
            },
        )


@dataclass
class QualityGateResult:
    """Result of quality gate evaluation."""

    passed: bool
    overall_result: bool
    metric_results: list[dict[str, Any]] = field(default_factory=list)

    @property
    def failed_count(self) -> int:
        """Count of failed gates."""
        failed = sum(1 for r in self.metric_results if not r["passed"])
        if not self.overall_result:
            failed += 1
        return failed

    @property
    def passed_count(self) -> int:
        """Count of passed gates."""
        passed = sum(1 for r in self.metric_results if r["passed"])
        if self.overall_result:
            passed += 1
        return passed


class QualityGateEvaluator:
    """Evaluates analysis results against quality gate thresholds."""

    def __init__(self, config: QualityGateConfig):
        """Initialize evaluator with configuration."""
        self.config = config

    def evaluate(self, analysis_result: dict[str, Any]) -> QualityGateResult:
        """
        Evaluate analysis results against quality gates.

        Args:
            analysis_result: Dictionary containing mfcqi_score and metric_scores

        Returns:
            QualityGateResult with pass/fail details
        """
        mfcqi_score = analysis_result.get("mfcqi_score", 0.0)
        metric_scores = analysis_result.get("metric_scores", {})

        # Check overall MFCQI score
        overall_result = True
        if "mfcqi_score" in self.config.overall_gates:
            threshold = self.config.overall_gates["mfcqi_score"]
            overall_result = mfcqi_score >= threshold

        # Check other overall gates (like security_score)
        for gate_name, threshold in self.config.overall_gates.items():
            if gate_name == "mfcqi_score":
                continue
            if gate_name in metric_scores and metric_scores[gate_name] < threshold:
                overall_result = False

        # Check individual metric gates
        metric_results = []
        for metric_name, threshold in self.config.metric_gates.items():
            if metric_name in metric_scores:
                actual_value = metric_scores[metric_name]
                passed = actual_value >= threshold

                metric_results.append(
                    {
                        "metric": metric_name,
                        "threshold": threshold,
                        "actual": actual_value,
                        "passed": passed,
                    }
                )

        # Overall pass requires both overall gates and all metric gates to pass
        all_metrics_passed = all(r["passed"] for r in metric_results)
        overall_passed = overall_result and all_metrics_passed

        return QualityGateResult(
            passed=overall_passed,
            overall_result=overall_result,
            metric_results=metric_results,
        )


def find_quality_gate_config(project_path: Path) -> Path | None:
    """
    Find quality gate configuration file in project.

    Looks for .mfcqi.yaml or .mfcqi-gates.yaml in project root.

    Args:
        project_path: Path to project directory

    Returns:
        Path to config file if found, None otherwise
    """
    for config_name in [".mfcqi.yaml", ".mfcqi-gates.yaml"]:
        config_path = project_path / config_name
        if config_path.exists():
            return config_path

    return None
