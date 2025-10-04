"""
Integration test for SARIF output format.
Tests the full flow from CLI to SARIF output.
"""

import json
import tempfile
from pathlib import Path

from click.testing import CliRunner

from mfcqi.cli.main import cli


def test_sarif_output_format_cli():
    """Test that SARIF output can be generated via CLI."""
    # Create a simple test file
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "simple.py"
        test_file.write_text(
            """
def add(a, b):
    '''Add two numbers.'''
    return a + b
"""
        )

        # Run CLI with SARIF format
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "analyze",
                tmpdir,
                "--format",
                "sarif",
                "--metrics-only",
            ],
        )

        # Should succeed
        assert result.exit_code == 0

        # Output should be valid JSON
        output = result.output.strip()
        sarif_data = json.loads(output)

        # Verify SARIF structure
        assert sarif_data["version"] == "2.1.0"
        assert "$schema" in sarif_data
        assert "runs" in sarif_data
        assert len(sarif_data["runs"]) > 0

        # Verify tool information
        run = sarif_data["runs"][0]
        assert run["tool"]["driver"]["name"] == "MFCQI"

        # Verify results exist
        assert "results" in run
        assert len(run["results"]) > 0


def test_sarif_output_to_file():
    """Test that SARIF output can be written to a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "simple.py"
        test_file.write_text(
            """
def multiply(x, y):
    return x * y
"""
        )

        output_file = Path(tmpdir) / "output.sarif"

        # Run CLI with SARIF format and output file
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "analyze",
                tmpdir,
                "--format",
                "sarif",
                "--output",
                str(output_file),
                "--metrics-only",
            ],
        )

        # Should succeed
        assert result.exit_code == 0

        # Output file should exist
        assert output_file.exists()

        # File should contain valid SARIF
        sarif_content = output_file.read_text()
        sarif_data = json.loads(sarif_content)
        assert sarif_data["version"] == "2.1.0"


def test_sarif_includes_metric_rules():
    """Test that SARIF output includes rules for metrics."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "simple.py"
        test_file.write_text("def test(): pass")

        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["analyze", tmpdir, "--format", "sarif", "--metrics-only"],
        )

        sarif_data = json.loads(result.output.strip())
        rules = sarif_data["runs"][0]["tool"]["driver"]["rules"]

        # Should have rules for various metrics
        rule_ids = [rule["id"] for rule in rules]
        assert "mfcqi_score" in rule_ids
        assert len(rules) > 1  # Should have multiple metric rules
