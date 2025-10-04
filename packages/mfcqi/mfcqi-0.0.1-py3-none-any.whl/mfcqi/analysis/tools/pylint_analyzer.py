"""
Pylint analyzer integration using pylint.lint.Run Python API.
"""

import io
import json
from pathlib import Path
from typing import Any

from pylint.lint import Run

from mfcqi.analysis.diagnostics import DiagnosticsCollection, DiagnosticSeverity, create_diagnostic
from mfcqi.core.file_utils import get_python_files


class PylintAnalyzer:
    """Pylint analyzer for detailed code quality analysis."""

    def __init__(self, config: dict[str, Any] | None = None):
        """Initialize Pylint analyzer."""
        self.config = config or {}

    def analyze_file(self, file_path: Path) -> list[dict[str, Any]]:
        """Analyze a single file using pylint.lint.Run Python API (NO subprocess)."""
        try:
            import sys

            # Build pylint args (like command-line args, but passed to API)
            args = [str(file_path), "--output-format=json2"]

            # Add configuration options
            if "disable" in self.config:
                disabled = ",".join(self.config["disable"])
                args.extend(["--disable", disabled])

            if "enable" in self.config:
                enabled = ",".join(self.config["enable"])
                args.extend(["--enable", enabled])

            if "max-line-length" in self.config:
                args.extend(["--max-line-length", str(self.config["max-line-length"])])

            # Create StringIO to capture output
            output = io.StringIO()

            # Save original stdout/stderr and redirect to capture output
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = output
            sys.stderr = io.StringIO()  # Suppress stderr

            try:
                # Run pylint with API (exit=False to prevent sys.exit)
                Run(args, exit=False)
            finally:
                # Restore stdout/stderr
                sys.stdout = old_stdout
                sys.stderr = old_stderr

            # Get results from captured output
            output.seek(0)
            output_data = output.read()

            if output_data:
                pylint_output = json.loads(output_data)
                pylint_results = pylint_output.get("messages", [])
            else:
                pylint_results = []

            # Convert to our format
            results = []
            for item in pylint_results:
                results.append(
                    {
                        "type": item.get("type", "unknown"),
                        "line": item.get("line", 1),
                        "column": item.get("column", 0),
                        "message": item.get("message", ""),
                        "symbol": item.get("symbol", ""),
                        "path": str(file_path),
                    }
                )

            return results

        except Exception:
            # Return empty list on error
            return []

    def analyze_directory(self, directory: Path) -> dict[str, list[dict[str, Any]]]:
        """Analyze all Python files in a directory."""
        results = {}

        # Find all Python files
        python_files = get_python_files(directory)

        for py_file in python_files:
            file_results = self.analyze_file(py_file)
            if file_results:
                results[py_file.name] = file_results

        return results

    def map_severity(self, pylint_type: str) -> str:
        """Map Pylint severity to standard levels."""
        severity_map = {
            "error": "error",
            "fatal": "error",
            "warning": "warning",
            "convention": "info",
            "refactor": "hint",
        }
        return severity_map.get(pylint_type, "warning")

    def filter_by_severity(
        self, results: list[dict[str, Any]], severities: list[str]
    ) -> list[dict[str, Any]]:
        """Filter results by severity levels."""
        return [r for r in results if r.get("type") in severities]

    def get_diagnostics(self, file_path: Path) -> list[DiagnosticsCollection]:
        """Convert Pylint results to diagnostics."""
        results = self.analyze_file(file_path)

        if not results:
            return []

        diagnostics = []
        for result in results:
            severity_str = self.map_severity(result.get("type", "warning"))

            # Map to DiagnosticSeverity
            severity_map = {
                "error": DiagnosticSeverity.ERROR,
                "warning": DiagnosticSeverity.WARNING,
                "info": DiagnosticSeverity.INFORMATION,
                "hint": DiagnosticSeverity.HINT,
            }
            severity = severity_map.get(severity_str, DiagnosticSeverity.WARNING)

            diagnostic = create_diagnostic(
                file_path=str(file_path),
                line=result.get("line", 1),
                character=result.get("column", 0),
                message=result.get("message", ""),
                severity=severity,
                code=result.get("symbol", ""),
            )

            # Override source to indicate this came from Pylint
            diagnostic.source = "pylint"

            diagnostics.append(diagnostic)

        if diagnostics:
            collection = DiagnosticsCollection(file_path=str(file_path), diagnostics=diagnostics)
            return [collection]

        return []
