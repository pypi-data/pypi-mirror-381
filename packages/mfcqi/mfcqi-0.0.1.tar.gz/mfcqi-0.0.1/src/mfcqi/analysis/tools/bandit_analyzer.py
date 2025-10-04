"""
Bandit analyzer integration for security analysis.
"""

from pathlib import Path
from typing import Any

try:
    from bandit.core import config as b_config
    from bandit.core import manager as b_manager

    BANDIT_AVAILABLE = True
except ImportError:
    BANDIT_AVAILABLE = False

from mfcqi.analysis.diagnostics import DiagnosticsCollection, DiagnosticSeverity, create_diagnostic
from mfcqi.core.file_utils import get_python_files


class BanditAnalyzer:
    """Bandit analyzer using bandit.core Python API (code-level integration)."""

    def __init__(self, config: dict[str, Any] | None = None):
        """Initialize Bandit analyzer with Python API."""
        if not BANDIT_AVAILABLE:
            raise ImportError("bandit is not installed. Install with: pip install bandit")

        self.config = config or {}

    def analyze_file(self, file_path: Path) -> list[dict[str, Any]]:
        """Analyze a single file using bandit.core Python API (NO subprocess)."""
        try:
            # Create Bandit config
            bandit_config = b_config.BanditConfig()

            # Build profile with test inclusions/exclusions
            profile = {
                "include": set(),  # Empty means include all
                "exclude": set(self.config.get("skip_tests", [])),
            }

            # Create Bandit manager with API
            mgr = b_manager.BanditManager(bandit_config, "file", profile=profile)

            # Discover and scan the file
            mgr.discover_files([str(file_path)], False)  # False = not recursive for single file
            mgr.run_tests()

            # Get results from API
            issues = mgr.get_issue_list()

            # Convert bandit.core Issue objects to our dict format
            results = []
            for issue in issues:
                results.append(
                    {
                        "line_number": issue.lineno,
                        "issue_confidence": issue.confidence,  # Already a string
                        "issue_severity": issue.severity,  # Already a string
                        "issue_text": issue.text,
                        "test_name": issue.test_id,
                        "filename": str(file_path),
                        "more_info": f"https://bandit.readthedocs.io/en/latest/plugins/{issue.test_id.lower()}.html",
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

    def map_severity(self, bandit_severity: str) -> str:
        """Map Bandit severity to standard levels."""
        severity_map = {"HIGH": "error", "MEDIUM": "warning", "LOW": "info"}
        return severity_map.get(bandit_severity, "warning")

    def filter_by_confidence(
        self, results: list[dict[str, Any]], confidence_levels: list[str]
    ) -> list[dict[str, Any]]:
        """Filter results by confidence levels."""
        return [r for r in results if r.get("issue_confidence") in confidence_levels]

    def get_diagnostics(self, file_path: Path) -> list[DiagnosticsCollection]:
        """Convert Bandit results to diagnostics."""
        results = self.analyze_file(file_path)

        if not results:
            return []

        diagnostics = []
        for result in results:
            severity_str = self.map_severity(result.get("issue_severity", "MEDIUM"))

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
                line=result.get("line_number", 1),
                character=0,  # Bandit doesn't provide column info
                message=result.get("issue_text", ""),
                severity=severity,
                code=result.get("test_name", ""),
            )

            # Override source to indicate this came from Bandit
            diagnostic.source = "bandit"

            diagnostics.append(diagnostic)

        if diagnostics:
            collection = DiagnosticsCollection(file_path=str(file_path), diagnostics=diagnostics)
            return [collection]

        return []
