"""
Unit tests for LLMAnalysisEngine context building and formatting methods.

Tests the private methods that format tool outputs and build context for LLM prompts.
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest


# Helper function for API key detection
def has_api_key():
    """Check if any LLM API key is available."""
    return os.getenv("ANTHROPIC_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("OLLAMA_HOST")


# Test Group 1: _format_tool_output_for_metric() - All Branches


def test_format_tool_output_security_metric():
    """Test _format_tool_output_for_metric() with security/bandit data."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {
        "bandit_issues": [{"test_name": "B101"}, {"test_name": "B102"}, {"test_name": "B103"}]
    }

    result = engine._format_tool_output_for_metric("security", tool_outputs)

    assert "Found 3 security vulnerabilities via Bandit" in result


def test_format_tool_output_halstead_metric():
    """Test _format_tool_output_for_metric() with halstead volume data."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {"halstead_volume_raw": 2547.89}

    result = engine._format_tool_output_for_metric("halstead_volume", tool_outputs)

    assert "Halstead Volume: 2548" in result


def test_format_tool_output_cyclomatic_metric():
    """Test _format_tool_output_for_metric() with cyclomatic complexity data."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {"cyclomatic_complexity_raw": 8.73}

    result = engine._format_tool_output_for_metric("cyclomatic_complexity", tool_outputs)

    assert "Average Cyclomatic Complexity: 8.7" in result


def test_format_tool_output_unknown_metric():
    """Test _format_tool_output_for_metric() with unknown metric returns empty string."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {"some_data": 123}

    result = engine._format_tool_output_for_metric("unknown_metric", tool_outputs)

    assert result == ""


# Test Group 2: _format_tool_outputs() - Bandit Issues


def test_format_tool_outputs_with_bandit_issues():
    """Test _format_tool_outputs() with multiple bandit issues of varying severities."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {
        "bandit_issues": [
            {
                "test_name": "B201",
                "issue_text": "SQL injection risk",
                "filename": "db.py",
                "line_number": 42,
                "issue_severity": "HIGH",
            },
            {
                "test_name": "B101",
                "issue_text": "Use of assert",
                "filename": "test.py",
                "line_number": 10,
                "issue_severity": "LOW",
            },
            {
                "test_name": "B608",
                "issue_text": "SQL string formatting",
                "filename": "models.py",
                "line_number": 89,
                "issue_severity": "MEDIUM",
            },
            {
                "test_name": "B501",
                "issue_text": "Weak cryptography",
                "filename": "crypto.py",
                "line_number": 15,
                "issue_severity": "CRITICAL",
            },
        ]
    }

    result = engine._format_tool_outputs(tool_outputs)

    assert "bandit" in result
    bandit = result["bandit"]

    # Check summary
    assert bandit["summary"] == "Found 4 security issues"

    # Check severity counts
    assert bandit["critical_count"] == 1
    assert bandit["high_count"] == 1
    assert bandit["medium_count"] == 1
    assert bandit["low_count"] == 1

    # Check top issues sorted by severity
    assert len(bandit["top_issues"]) == 4
    # CRITICAL should be first
    assert bandit["top_issues"][0]["severity"] == "CRITICAL"
    assert bandit["top_issues"][0]["test_name"] == "B501"


def test_format_tool_outputs_empty_bandit():
    """Test _format_tool_outputs() with empty bandit_issues list."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {"bandit_issues": []}

    result = engine._format_tool_outputs(tool_outputs)

    assert "bandit" in result
    assert result["bandit"]["summary"] == "Found 0 security issues"
    assert result["bandit"]["critical_count"] == 0
    assert len(result["bandit"]["top_issues"]) == 0


# Test Group 3: _format_tool_outputs() - Complexity Data


def test_format_tool_outputs_with_complex_functions():
    """Test _format_tool_outputs() with complex_functions data."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {
        "complex_functions": [
            {"name": "process_data", "file": "processor.py", "complexity": 25},
            {"name": "validate_input", "file": "validator.py", "complexity": 18},
        ]
    }

    result = engine._format_tool_outputs(tool_outputs)

    assert "complexity" in result
    complexity = result["complexity"]

    # Should use the provided complex_functions data
    assert len(complexity["complex_functions"]) == 2
    assert complexity["complex_functions"][0]["name"] == "process_data"
    assert complexity["complex_functions"][0]["complexity"] == 25


def test_format_tool_outputs_with_high_cyclomatic():
    """Test _format_tool_outputs() with high cyclomatic_complexity_raw (>10)."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {"cyclomatic_complexity_raw": 15.7}

    result = engine._format_tool_outputs(tool_outputs)

    assert "complexity" in result
    complexity = result["complexity"]

    # Should create fallback entry for high complexity
    assert len(complexity["complex_functions"]) == 1
    assert complexity["complex_functions"][0]["name"] == "Multiple functions"
    assert complexity["complex_functions"][0]["complexity"] == 16  # rounded


def test_format_tool_outputs_with_high_halstead():
    """Test _format_tool_outputs() with high halstead_volume_raw (>1000)."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {"halstead_volume_raw": 3542.89}

    result = engine._format_tool_outputs(tool_outputs)

    assert "complexity" in result
    complexity = result["complexity"]

    # Should create entry for high volume files
    assert len(complexity["high_volume_files"]) == 1
    assert complexity["high_volume_files"][0]["path"] == "Various files"
    assert complexity["high_volume_files"][0]["volume"] == 3543  # rounded


def test_format_tool_outputs_no_tool_data():
    """Test _format_tool_outputs() with empty tool_outputs dict."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    tool_outputs = {}

    result = engine._format_tool_outputs(tool_outputs)

    # Should return empty dict when no relevant data present
    assert result == {}


# Test Group 4: _build_context_with_real_data() - Integration


def test_build_context_with_critical_metrics():
    """Test _build_context_with_real_data() with metrics containing scores < 0.3."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    # Create temp codebase with a Python file
    with tempfile.TemporaryDirectory() as tmpdir:
        codebase_path = Path(tmpdir)
        (codebase_path / "test.py").write_text("def foo():\n    pass\n")

        metrics = {
            "mfcqi_score": 0.45,
            "security": 0.15,  # Critical (< 0.3)
            "halstead_volume": 0.25,  # Critical (< 0.3)
            "cyclomatic_complexity": 0.82,  # Not critical
        }

        tool_outputs = {
            "bandit_issues": [{"test_name": "B101"}],
            "halstead_volume_raw": 2000.0,
        }

        context = engine._build_context_with_real_data(codebase_path, metrics, tool_outputs)

        # Check critical_metrics are identified and sorted
        assert len(context["critical_metrics"]) == 2
        # Should be sorted by score (lowest first)
        assert context["critical_metrics"][0]["name"] == "security"
        assert context["critical_metrics"][0]["score"] == 0.15
        assert context["critical_metrics"][1]["name"] == "halstead_volume"
        assert context["critical_metrics"][1]["score"] == 0.25

        # Check tool output formatting was called
        assert "Found 1 security vulnerabilities" in context["critical_metrics"][0]["tool_output"]
        assert "Halstead Volume:" in context["critical_metrics"][1]["tool_output"]


def test_build_context_without_critical_metrics():
    """Test _build_context_with_real_data() with all metrics > 0.3."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    with tempfile.TemporaryDirectory() as tmpdir:
        codebase_path = Path(tmpdir)
        (codebase_path / "test.py").write_text("def foo():\n    pass\n")

        metrics = {
            "mfcqi_score": 0.85,
            "security": 0.90,
            "halstead_volume": 0.75,
            "cyclomatic_complexity": 0.82,
        }

        tool_outputs = {}

        context = engine._build_context_with_real_data(codebase_path, metrics, tool_outputs)

        # No critical metrics
        assert len(context["critical_metrics"]) == 0


def test_build_context_integrates_formatted_outputs():
    """Test _build_context_with_real_data() properly integrates formatted tool outputs."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    with tempfile.TemporaryDirectory() as tmpdir:
        codebase_path = Path(tmpdir)
        (codebase_path / "test.py").write_text("def foo():\n    pass\n")

        metrics = {"mfcqi_score": 0.75}

        tool_outputs = {
            "bandit_issues": [
                {
                    "test_name": "B201",
                    "issue_text": "SQL injection",
                    "filename": "db.py",
                    "line_number": 42,
                    "issue_severity": "HIGH",
                }
            ],
            "complex_functions": [{"name": "big_function", "file": "app.py", "complexity": 30}],
        }

        context = engine._build_context_with_real_data(codebase_path, metrics, tool_outputs)

        # Check that tool_outputs were formatted
        assert "tool_outputs" in context
        assert "bandit" in context["tool_outputs"]
        assert "complexity" in context["tool_outputs"]

        # Verify context structure
        assert "codebase_path" in context
        assert "total_files" in context
        assert "total_lines" in context
        assert "mfcqi_score" in context
        assert "metrics" in context


# Test Group 5: Error Handling


@pytest.mark.skipif(not has_api_key(), reason="No LLM API key available")
def test_analyze_with_cqi_data_exception_handling():
    """Test analyze_with_cqi_data() properly handles and re-raises exceptions."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    # Mock litellm.completion to raise exception
    with patch("litellm.completion", side_effect=Exception("LLM API error")):
        with tempfile.TemporaryDirectory() as tmpdir:
            codebase_path = Path(tmpdir)
            (codebase_path / "test.py").write_text("def foo():\n    pass\n")

            cqi_data = {"mfcqi_score": 0.75, "security": 0.80}

            # Should re-raise exception with context
            with pytest.raises(Exception) as exc_info:
                engine.analyze_with_cqi_data(str(codebase_path), cqi_data)

            assert "LLM analysis failed" in str(exc_info.value)
            assert "LLM API error" in str(exc_info.value)


@pytest.mark.skipif(not has_api_key(), reason="No LLM API key available")
@patch("litellm.completion")
def test_make_llm_request_exception_handling(mock_completion):
    """Test _make_llm_request() properly handles and wraps LiteLLM exceptions."""
    from mfcqi.analysis.engine import LLMAnalysisEngine

    engine = LLMAnalysisEngine()

    # Mock litellm to raise an exception
    mock_completion.side_effect = Exception("API rate limit exceeded")

    # Should wrap and re-raise exception
    with pytest.raises(Exception) as exc_info:
        engine._make_llm_request("Test prompt")

    assert "LLM request failed" in str(exc_info.value)
    assert "API rate limit exceeded" in str(exc_info.value)
