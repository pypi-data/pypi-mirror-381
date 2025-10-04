"""
Tests for SARIF output format.
"""

import json
from pathlib import Path

from jsonschema import validate


def test_format_sarif_output_exists():
    """RED: Test that format_sarif_output function exists."""
    from mfcqi.cli.utils.output import format_sarif_output

    assert format_sarif_output is not None
    assert callable(format_sarif_output)


def test_format_sarif_output_returns_dict():
    """RED: Test that format_sarif_output returns a dictionary."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.8,
            "cognitive_complexity": 0.7,
        },
        "recommendations": ["Improve complexity"],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)
    assert isinstance(result, dict)


def test_sarif_output_has_required_fields():
    """RED: Test that SARIF output has all required SARIF 2.1.0 fields."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.8,
        },
        "recommendations": [],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    # SARIF 2.1.0 required fields
    assert "version" in result
    assert result["version"] == "2.1.0"
    assert "$schema" in result
    assert "runs" in result
    assert isinstance(result["runs"], list)
    assert len(result["runs"]) > 0


def test_sarif_output_tool_information():
    """RED: Test that SARIF output includes tool information."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {},
        "recommendations": [],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    run = result["runs"][0]
    assert "tool" in run
    assert "driver" in run["tool"]
    driver = run["tool"]["driver"]
    assert "name" in driver
    assert driver["name"] == "MFCQI"
    assert "informationUri" in driver


def test_sarif_output_includes_rules():
    """RED: Test that SARIF output includes rules for each metric."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.8,
            "cognitive_complexity": 0.7,
        },
        "recommendations": [],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    run = result["runs"][0]
    assert "tool" in run
    assert "driver" in run["tool"]
    driver = run["tool"]["driver"]
    assert "rules" in driver
    assert len(driver["rules"]) > 0

    # Check that rules are created for metrics
    rule_ids = [rule["id"] for rule in driver["rules"]]
    assert "cyclomatic_complexity" in rule_ids
    assert "cognitive_complexity" in rule_ids


def test_sarif_output_includes_results():
    """RED: Test that SARIF output includes results."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.8,
            "cognitive_complexity": 0.7,
        },
        "recommendations": [],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    run = result["runs"][0]
    assert "results" in run
    assert isinstance(run["results"], list)


def test_sarif_output_result_levels():
    """RED: Test that SARIF results have correct severity levels."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.5,  # Poor score
        "metric_scores": {
            "cyclomatic_complexity": 0.3,  # Poor
            "cognitive_complexity": 0.9,  # Excellent
        },
        "recommendations": [],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    run = result["runs"][0]
    results_list = run["results"]

    # Should have results for each metric
    assert len(results_list) >= 2

    # Check that levels are set correctly
    for result_item in results_list:
        assert "level" in result_item
        assert result_item["level"] in ["error", "warning", "note", "none"]


def test_sarif_output_with_recommendations():
    """RED: Test that SARIF output includes recommendations in results."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.8,
        },
        "recommendations": [
            "Reduce cyclomatic complexity",
            "Improve documentation",
        ],
        "model_used": "claude-3-sonnet",
    }

    result = format_sarif_output(analysis_result)

    run = result["runs"][0]
    results_list = run["results"]

    # Should include recommendations as results
    recommendation_messages = [r["message"]["text"] for r in results_list if "message" in r]
    assert len(recommendation_messages) > 0


def test_sarif_output_json_serializable():
    """RED: Test that SARIF output is JSON serializable."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {
            "cyclomatic_complexity": 0.8,
        },
        "recommendations": ["Test recommendation"],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    # Should be able to serialize to JSON without errors
    json_str = json.dumps(result, indent=2)
    assert isinstance(json_str, str)
    assert len(json_str) > 0

    # Should be able to deserialize back
    parsed = json.loads(json_str)
    assert parsed["version"] == "2.1.0"


def test_sarif_output_schema_url():
    """RED: Test that SARIF output has correct schema URL."""
    from mfcqi.cli.utils.output import format_sarif_output

    analysis_result = {
        "mfcqi_score": 0.75,
        "metric_scores": {},
        "recommendations": [],
        "model_used": "metrics-only",
    }

    result = format_sarif_output(analysis_result)

    assert "$schema" in result
    assert "sarif-schema-2.1.0" in result["$schema"] or "sarif/v2.1.0" in result["$schema"]


def test_sarif_output_validates_against_official_schema():
    """Test that SARIF output validates against official SARIF 2.1.0 JSON Schema."""
    from mfcqi.cli.utils.output import format_sarif_output

    # Load the official SARIF 2.1.0 schema
    schema_path = Path(__file__).parent / "schemas" / "sarif-schema-2.1.0.json"
    with open(schema_path) as f:
        sarif_schema = json.load(f)

    # Generate SARIF output
    analysis_result = {
        "mfcqi_score": 0.85,
        "metric_scores": {
            "cyclomatic_complexity": 0.9,
            "cognitive_complexity": 0.8,
            "maintainability_index": 0.85,
        },
        "recommendations": [
            "Excellent code quality",
            "Consider adding more tests",
        ],
        "model_used": "claude-3-5-sonnet",
    }

    sarif_output = format_sarif_output(analysis_result)

    # Validate against schema - will raise ValidationError if invalid
    validate(instance=sarif_output, schema=sarif_schema)
