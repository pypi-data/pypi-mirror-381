"""
Ruff analyzer integration for modern fast linting.
"""

import json
import subprocess
from pathlib import Path
from typing import Any

from mfcqi.analysis.diagnostics import DiagnosticsCollection, DiagnosticSeverity, create_diagnostic
from mfcqi.core.file_utils import get_python_files


class RuffAnalyzer:
    """Ruff analyzer for modern, fast Python linting with 800+ rules."""

    def __init__(self, config: dict[str, Any] | None = None):
        """Initialize Ruff analyzer."""
        self.config = config or {}

    def analyze_file(self, file_path: Path) -> list[dict[str, Any]]:
        """Analyze a single file with Ruff."""
        try:
            # Build ruff command
            cmd = ["ruff", "check", "--output-format=json", str(file_path)]

            # Add configuration options
            if "select" in self.config:
                selected = ",".join(self.config["select"])
                cmd.extend(["--select", selected])

            if "ignore" in self.config:
                ignored = ",".join(self.config["ignore"])
                cmd.extend(["--ignore", ignored])

            if "line_length" in self.config:
                cmd.extend(["--line-length", str(self.config["line_length"])])

            # Run ruff
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            # Parse JSON output - Ruff may exit with non-zero but still provide JSON
            if result.stdout:
                try:
                    ruff_results = json.loads(result.stdout)
                except json.JSONDecodeError:
                    ruff_results = []
            else:
                ruff_results = []

            # Convert to our format
            results = []
            for item in ruff_results:
                results.append(
                    {
                        "code": item.get("code", ""),
                        "line": item.get("location", {}).get("row", 1),
                        "column": item.get("location", {}).get("column", 0),
                        "message": item.get("message", ""),
                        "filename": item.get("filename", str(file_path)),
                        "fix": item.get("fix"),
                        "url": item.get("url", ""),
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

    def get_rule_category(self, rule_code: str) -> str:
        """Get category for a rule code."""
        if not rule_code:
            return "unknown"

        first_char = rule_code[0]
        category_map = {
            "E": "style",  # pycodestyle errors
            "W": "style",  # pycodestyle warnings
            "F": "error",  # pyflakes
            "C": "complexity",  # mccabe
            "B": "bugprone",  # flake8-bugbear
            "S": "security",  # flake8-bandit
            "I": "import",  # isort
            "N": "naming",  # pep8-naming
            "D": "docstring",  # pydocstyle
            "U": "upgrade",  # pyupgrade
            "A": "builtin",  # flake8-builtins
            "T": "print",  # flake8-print
        }
        return category_map.get(first_char, "other")

    def map_severity(self, rule_code: str) -> str:
        """Map rule code to severity level."""
        if not rule_code:
            return "warning"

        first_char = rule_code[0]
        severity_map = {
            "F": "error",  # Pyflakes errors are serious
            "E": "warning",  # Style errors
            "W": "warning",  # Style warnings
            "C": "info",  # Complexity
            "B": "warning",  # Bug-prone patterns
            "S": "error",  # Security issues
            "I": "info",  # Import order
            "N": "info",  # Naming conventions
            "D": "info",  # Docstring issues
            "U": "info",  # Upgrade suggestions
            "A": "warning",  # Built-in shadowing
            "T": "warning",  # Print statements
        }
        return severity_map.get(first_char, "warning")

    def filter_by_category(
        self, results: list[dict[str, Any]], categories: list[str]
    ) -> list[dict[str, Any]]:
        """Filter results by rule categories."""
        filtered = []
        for result in results:
            rule_code = result.get("code", "")
            category = self.get_rule_category(rule_code)
            if category in categories:
                filtered.append(result)
        return filtered

    def get_rule_explanation(self, rule_code: str) -> str:
        """Get explanation for a rule code."""
        # Common rule explanations
        explanations = {
            "F401": "Imported module/name is not used",
            "E501": "Line too long",
            "W292": "No newline at end of file",
            "E302": "Expected 2 blank lines, found fewer",
            "E303": "Too many blank lines",
            "F841": "Local variable is assigned but never used",
            "B902": "Invalid first argument for method",
            "S101": "Use of assert detected (security risk)",
            "I001": "Import block is un-sorted or un-formatted",
            "N806": "Variable name should be lowercase",
        }

        return explanations.get(rule_code, f"Rule {rule_code}: See Ruff documentation for details")

    def get_diagnostics(self, file_path: Path) -> list[DiagnosticsCollection]:
        """Convert Ruff results to diagnostics."""
        results = self.analyze_file(file_path)

        if not results:
            return []

        diagnostics = []
        for result in results:
            rule_code = result.get("code", "")
            severity_str = self.map_severity(rule_code)

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
                code=rule_code,
            )

            # Override source to indicate this came from Ruff
            diagnostic.source = "ruff"

            diagnostics.append(diagnostic)

        if diagnostics:
            collection = DiagnosticsCollection(file_path=str(file_path), diagnostics=diagnostics)
            return [collection]

        return []

    def get_fix_suggestions(self, file_path: Path) -> list[dict[str, Any]]:
        """Get fix suggestions from Ruff."""
        results = self.analyze_file(file_path)

        fixes = []
        for result in results:
            if result.get("fix"):
                fixes.append(
                    {
                        "rule": result.get("code", ""),
                        "message": result.get("message", ""),
                        "fix": result.get("fix"),
                        "line": result.get("line", 1),
                    }
                )

        return fixes
