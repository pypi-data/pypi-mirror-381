"""
Tests for Quality Gates functionality.
"""

import tempfile
from pathlib import Path

import pytest


def test_quality_gate_config_class_exists():
    """RED: Test that QualityGateConfig class exists."""
    from mfcqi.quality_gates import QualityGateConfig

    assert QualityGateConfig is not None


def test_quality_gate_config_loads_from_file():
    """RED: Test loading quality gate config from YAML file."""
    from mfcqi.quality_gates import QualityGateConfig

    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = Path(tmpdir) / ".mfcqi.yaml"
        config_file.write_text(
            """
quality_gates:
  overall:
    mfcqi_score: 0.7
    security_score: 0.9
  metrics:
    cyclomatic_complexity: 0.8
"""
        )

        config = QualityGateConfig.from_file(config_file)
        assert config is not None
        assert config.overall_gates["mfcqi_score"] == 0.7
        assert config.overall_gates["security_score"] == 0.9
        assert config.metric_gates["cyclomatic_complexity"] == 0.8


def test_quality_gate_config_has_defaults():
    """RED: Test that config has sensible defaults when no file provided."""
    from mfcqi.quality_gates import QualityGateConfig

    config = QualityGateConfig.from_defaults()
    assert config is not None
    assert "mfcqi_score" in config.overall_gates
    assert config.overall_gates["mfcqi_score"] > 0


def test_quality_gate_evaluator_exists():
    """RED: Test that QualityGateEvaluator class exists."""
    from mfcqi.quality_gates import QualityGateEvaluator

    assert QualityGateEvaluator is not None


def test_quality_gate_evaluator_checks_overall_score():
    """RED: Test evaluating overall MFCQI score against threshold."""
    from mfcqi.quality_gates import QualityGateConfig, QualityGateEvaluator

    config = QualityGateConfig(overall_gates={"mfcqi_score": 0.7}, metric_gates={})

    analysis_result = {
        "mfcqi_score": 0.8,
        "metric_scores": {},
    }

    evaluator = QualityGateEvaluator(config)
    gate_result = evaluator.evaluate(analysis_result)

    assert gate_result.passed is True
    assert gate_result.overall_result is True


def test_quality_gate_evaluator_fails_low_score():
    """RED: Test that quality gate fails when score is below threshold."""
    from mfcqi.quality_gates import QualityGateConfig, QualityGateEvaluator

    config = QualityGateConfig(overall_gates={"mfcqi_score": 0.7}, metric_gates={})

    analysis_result = {
        "mfcqi_score": 0.5,  # Below threshold
        "metric_scores": {},
    }

    evaluator = QualityGateEvaluator(config)
    gate_result = evaluator.evaluate(analysis_result)

    assert gate_result.passed is False
    assert gate_result.overall_result is False


def test_quality_gate_evaluator_checks_individual_metrics():
    """RED: Test evaluating individual metrics against thresholds."""
    from mfcqi.quality_gates import QualityGateConfig, QualityGateEvaluator

    config = QualityGateConfig(
        overall_gates={},
        metric_gates={
            "cyclomatic_complexity": 0.8,
            "security": 0.9,
        },
    )

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.85,  # Pass
            "security": 0.95,  # Pass
        },
    }

    evaluator = QualityGateEvaluator(config)
    gate_result = evaluator.evaluate(analysis_result)

    assert gate_result.passed is True
    assert len(gate_result.metric_results) == 2


def test_quality_gate_evaluator_reports_failed_metrics():
    """RED: Test that failed metrics are reported in results."""
    from mfcqi.quality_gates import QualityGateConfig, QualityGateEvaluator

    config = QualityGateConfig(
        overall_gates={},
        metric_gates={
            "cyclomatic_complexity": 0.8,
            "security": 0.9,
        },
    )

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.6,  # Fail
            "security": 0.95,  # Pass
        },
    }

    evaluator = QualityGateEvaluator(config)
    gate_result = evaluator.evaluate(analysis_result)

    assert gate_result.passed is False
    failed_metrics = [r for r in gate_result.metric_results if not r["passed"]]
    assert len(failed_metrics) == 1
    assert failed_metrics[0]["metric"] == "cyclomatic_complexity"


def test_quality_gate_result_provides_details():
    """RED: Test that gate result provides detailed pass/fail information."""
    from mfcqi.quality_gates import QualityGateConfig, QualityGateEvaluator

    config = QualityGateConfig(
        overall_gates={"mfcqi_score": 0.7},
        metric_gates={"security": 0.9},
    )

    analysis_result = {
        "mfcqi_score": 0.8,
        "metric_scores": {"security": 0.85},
    }

    evaluator = QualityGateEvaluator(config)
    gate_result = evaluator.evaluate(analysis_result)

    # Should provide details about each gate check
    assert hasattr(gate_result, "overall_result")
    assert hasattr(gate_result, "metric_results")
    assert hasattr(gate_result, "passed")
    assert hasattr(gate_result, "failed_count")
    assert hasattr(gate_result, "passed_count")


def test_quality_gate_cli_flag_exists():
    """RED: Test that --quality-gate CLI flag exists."""
    from click.testing import CliRunner

    from mfcqi.cli.main import cli

    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--help"])

    assert "--quality-gate" in result.output


def test_quality_gate_cli_exits_with_failure():
    """RED: Test that CLI exits with code 1 when quality gate fails."""
    from click.testing import CliRunner

    from mfcqi.cli.main import cli

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create poor quality code
        test_file = Path(tmpdir) / "bad.py"
        test_file.write_text(
            """
def complex(a, b, c, d, e):
    if a:
        if b:
            if c:
                for i in range(d):
                    for j in range(e):
                        if i % 2:
                            if j % 3:
                                return i * j
"""
        )

        # Create strict quality gate config
        config_file = Path(tmpdir) / ".mfcqi.yaml"
        config_file.write_text(
            """
quality_gates:
  overall:
    mfcqi_score: 0.9  # Very strict
"""
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "analyze",
                tmpdir,
                "--quality-gate",
                "--metrics-only",
            ],
        )

        # Should fail (exit code 1)
        assert result.exit_code == 1


def test_quality_gate_cli_exits_with_success():
    """RED: Test that CLI exits with code 0 when quality gate passes."""
    from click.testing import CliRunner

    from mfcqi.cli.main import cli

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create good quality code
        test_file = Path(tmpdir) / "good.py"
        test_file.write_text(
            """
def add(a, b):
    '''Add two numbers.'''
    return a + b

def multiply(x, y):
    '''Multiply two numbers.'''
    return x * y
"""
        )

        # Create lenient quality gate config
        config_file = Path(tmpdir) / ".mfcqi.yaml"
        config_file.write_text(
            """
quality_gates:
  overall:
    mfcqi_score: 0.5  # Lenient
"""
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "analyze",
                tmpdir,
                "--quality-gate",
                "--metrics-only",
            ],
        )

        # Should pass (exit code 0)
        assert result.exit_code == 0


def test_quality_gate_output_shows_results():
    """RED: Test that quality gate results are displayed to user."""
    from click.testing import CliRunner

    from mfcqi.cli.main import cli

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "code.py"
        test_file.write_text("def test(): pass")

        config_file = Path(tmpdir) / ".mfcqi.yaml"
        config_file.write_text(
            """
quality_gates:
  overall:
    mfcqi_score: 0.7
"""
        )

        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "analyze",
                tmpdir,
                "--quality-gate",
                "--metrics-only",
            ],
        )

        # Output should mention quality gates
        output = result.output.lower()
        assert "quality gate" in output or "gate" in output


def test_quality_gate_finds_config_in_project_root():
    """RED: Test that quality gate automatically finds .mfcqi.yaml in project."""
    from mfcqi.quality_gates import find_quality_gate_config

    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = Path(tmpdir) / ".mfcqi.yaml"
        config_file.write_text(
            """
quality_gates:
  overall:
    mfcqi_score: 0.8
"""
        )

        found_config = find_quality_gate_config(Path(tmpdir))
        assert found_config is not None
        assert found_config == config_file


def test_quality_gate_config_validates_yaml_structure():
    """RED: Test that invalid YAML structure raises validation error."""
    from mfcqi.quality_gates import QualityGateConfig

    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = Path(tmpdir) / ".mfcqi.yaml"
        config_file.write_text(
            """
invalid_structure:
  random_key: value
"""
        )

        with pytest.raises(ValueError, match="quality_gates"):
            QualityGateConfig.from_file(config_file)
