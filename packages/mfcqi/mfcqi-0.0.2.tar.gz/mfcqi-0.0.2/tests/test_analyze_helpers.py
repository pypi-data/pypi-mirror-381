"""Tests for analyze command helpers."""

import json
import tempfile
import textwrap
from pathlib import Path
from unittest.mock import MagicMock

from mfcqi.calculator import MFCQICalculator
from mfcqi.cli.commands.analyze_helpers import (
    calculate_metrics,
    check_minimum_score,
    get_llm_recommendations,
    output_results,
    prepare_analysis_result,
)
from mfcqi.cli.utils.config_manager import ConfigManager
from mfcqi.cli.utils.llm_handler import LLMHandler


def test_calculate_metrics_without_tool_outputs():
    """Test calculate_metrics without tool outputs."""
    code = textwrap.dedent('''
        """Test module."""
        def test():
            """Test function."""
            return 1
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        calculator = MFCQICalculator()
        detailed_metrics, tool_outputs, elapsed = calculate_metrics(
            Path(tmpdir), calculator, need_tool_outputs=False, silent=True
        )

        assert isinstance(detailed_metrics, dict)
        assert "mfcqi_score" in detailed_metrics
        assert tool_outputs == {}
        assert elapsed >= 0.0


def test_calculate_metrics_with_tool_outputs():
    """Test calculate_metrics with tool outputs."""
    code = textwrap.dedent('''
        """Test module."""
        def complex(a, b, c):
            """Complex function."""
            if a:
                if b:
                    if c:
                        if a > b:
                            return a * b * c
            return 0
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        calculator = MFCQICalculator()
        detailed_metrics, tool_outputs, elapsed = calculate_metrics(
            Path(tmpdir), calculator, need_tool_outputs=True, silent=True
        )

        assert isinstance(detailed_metrics, dict)
        assert "mfcqi_score" in detailed_metrics
        assert isinstance(tool_outputs, dict)
        assert elapsed >= 0.0


def test_get_llm_recommendations_no_model():
    """Test get_llm_recommendations when no model is configured."""
    from unittest.mock import patch

    with patch("mfcqi.cli.utils.config_manager.KEYRING_AVAILABLE", False):
        config_manager = ConfigManager()
        llm_handler = LLMHandler(config_manager, "http://localhost:99999")  # Invalid Ollama

    # Mock select_model to return None (no model available)
    llm_handler.select_model = MagicMock(return_value=None)

    detailed_metrics = {"mfcqi_score": 0.75}
    tool_outputs = {}

    result = get_llm_recommendations(
        "/test/path",
        detailed_metrics,
        tool_outputs,
        llm_handler,
        model=None,
        provider=None,
        recommendations=3,
        silent=True,
    )

    assert result is None


def test_get_llm_recommendations_with_model():
    """Test get_llm_recommendations with a model."""
    from unittest.mock import patch

    with patch("mfcqi.cli.utils.config_manager.KEYRING_AVAILABLE", False):
        config_manager = ConfigManager()
        llm_handler = LLMHandler(config_manager)

    # Mock the methods
    llm_handler.select_model = MagicMock(return_value="test-model")
    llm_handler.analyze_with_llm = MagicMock(
        return_value={"recommendations": ["Improve docs", "Reduce complexity"]}
    )

    detailed_metrics = {"mfcqi_score": 0.75}
    tool_outputs = {}

    result = get_llm_recommendations(
        "/test/path",
        detailed_metrics,
        tool_outputs,
        llm_handler,
        model="test-model",
        provider="test-provider",
        recommendations=3,
        silent=True,
    )

    assert result is not None
    assert result["model_used"] == "test-model"
    assert "recommendations" in result


def test_get_llm_recommendations_analysis_fails():
    """Test get_llm_recommendations when LLM analysis fails."""
    from unittest.mock import patch

    with patch("mfcqi.cli.utils.config_manager.KEYRING_AVAILABLE", False):
        config_manager = ConfigManager()
        llm_handler = LLMHandler(config_manager)

    # Mock select_model to return a model but analyze_with_llm returns None
    llm_handler.select_model = MagicMock(return_value="test-model")
    llm_handler.analyze_with_llm = MagicMock(return_value=None)

    detailed_metrics = {"mfcqi_score": 0.75}
    tool_outputs = {}

    result = get_llm_recommendations(
        "/test/path",
        detailed_metrics,
        tool_outputs,
        llm_handler,
        model="test-model",
        provider=None,
        recommendations=3,
        silent=True,
    )

    assert result is None


def test_prepare_analysis_result():
    """Test prepare_analysis_result creates correct structure."""
    detailed_metrics = {
        "mfcqi_score": 0.85,
        "cyclomatic_complexity": 0.90,
        "maintainability_index": 0.75,
        "documentation_coverage": 0.88,
    }

    result = prepare_analysis_result(detailed_metrics)

    assert result["mfcqi_score"] == 0.85
    assert "mfcqi_score" not in result["metric_scores"]
    assert result["metric_scores"]["cyclomatic_complexity"] == 0.90
    assert result["diagnostics"] == []
    assert result["recommendations"] == []
    assert result["model_used"] == "metrics-only"


def test_output_results_json_to_console():
    """Test output_results with JSON to console."""
    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {"cyclomatic_complexity": 0.80},
        "recommendations": ["Test recommendation"],
    }

    # Output to console (no file)
    output_results(analysis_result, output_format="json", output=None, silent=True)

    # Should not raise exceptions


def test_output_results_json_to_file():
    """Test output_results with JSON to file."""
    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {"cyclomatic_complexity": 0.80},
        "recommendations": ["Test recommendation"],
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = Path(tmpdir) / "output.json"

        output_results(analysis_result, output_format="json", output=output_file, silent=True)

        assert output_file.exists()
        data = json.loads(output_file.read_text())
        assert data["mfcqi_score"] == 0.75


def test_output_results_text_to_file():
    """Test output_results with text format to file."""
    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {"cyclomatic_complexity": 0.80},
        "recommendations": [],
        "model_used": "metrics-only",
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = Path(tmpdir) / "output.txt"

        output_results(analysis_result, output_format="text", output=output_file, silent=True)

        assert output_file.exists()
        content = output_file.read_text()
        assert len(content) > 0


def test_check_minimum_score_passes():
    """Test check_minimum_score when score meets minimum."""
    result = check_minimum_score(cqi_score=0.85, min_score=0.70, silent=True)
    assert result is True


def test_check_minimum_score_fails():
    """Test check_minimum_score when score below minimum."""
    result = check_minimum_score(cqi_score=0.65, min_score=0.70, silent=True)
    assert result is False


def test_check_minimum_score_no_minimum():
    """Test check_minimum_score when no minimum is set."""
    result = check_minimum_score(cqi_score=0.50, min_score=None, silent=True)
    assert result is True
