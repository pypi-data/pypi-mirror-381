"""
Smoke test for CLI imports without optional dependencies.

This test ensures the CLI can be imported even when optional dependencies
(pip-audit, detect-secrets) are not installed. The CLI should gracefully
degrade functionality rather than crash on import.

Regression Test for: ModuleNotFoundError when optional dependencies missing
"""

import sys
from unittest.mock import patch


class TestCLIImportSmoke:
    """Test CLI imports work without optional dependencies."""

    def test_cli_imports_without_pip_audit(self):
        """Test CLI can be imported when pip_audit is not installed."""
        # Simulate pip_audit not being installed
        with patch.dict(sys.modules, {"pip_audit": None}):
            # This import should NOT crash
            from mfcqi.cli.main import cli

            assert cli is not None

    def test_cli_imports_without_detect_secrets(self):
        """Test CLI can be imported when detect_secrets is not installed."""
        # Simulate detect_secrets not being installed
        with patch.dict(sys.modules, {"detect_secrets": None}):
            # This import should NOT crash
            from mfcqi.cli.main import cli

            assert cli is not None

    def test_cli_imports_without_any_optional_deps(self):
        """Test CLI can be imported when all optional dependencies are missing."""
        # Simulate all optional packages not installed
        with patch.dict(
            sys.modules,
            {
                "pip_audit": None,
                "detect_secrets": None,
            },
        ):
            # This import should NOT crash
            from mfcqi.cli.main import cli

            assert cli is not None

    def test_analyzers_gracefully_degrade_without_pip_audit(self):
        """Test pip_audit analyzer returns empty results when not available."""
        from pathlib import Path
        from unittest.mock import patch

        # Simulate pip_audit not installed
        with patch.dict(sys.modules, {"pip_audit": None}):
            # Force reimport to trigger ImportError path
            import importlib

            import mfcqi.analysis.tools.pip_audit_analyzer

            importlib.reload(mfcqi.analysis.tools.pip_audit_analyzer)

            from mfcqi.analysis.tools.pip_audit_analyzer import PipAuditAnalyzer

            analyzer = PipAuditAnalyzer()

            # Should return empty results, not crash
            result = analyzer.scan_requirements(Path("nonexistent.txt"))
            assert result == []

    def test_analyzers_gracefully_degrade_without_detect_secrets(self):
        """Test detect_secrets analyzer returns empty results when not available."""
        from pathlib import Path
        from unittest.mock import patch

        # Simulate detect_secrets not installed
        with patch.dict(sys.modules, {"detect_secrets": None}):
            # Force reimport to trigger ImportError path
            import importlib

            import mfcqi.analysis.tools.detect_secrets_analyzer

            importlib.reload(mfcqi.analysis.tools.detect_secrets_analyzer)

            from mfcqi.analysis.tools.detect_secrets_analyzer import (
                DetectSecretsAnalyzer,
            )

            analyzer = DetectSecretsAnalyzer()

            # Should return empty results, not crash
            result = analyzer.scan_file(Path("nonexistent.py"))
            assert result == []

    def test_metrics_work_without_optional_deps(self):
        """Test security metrics return safe defaults when analyzers unavailable."""
        from pathlib import Path
        from unittest.mock import patch

        # Simulate all optional deps not installed
        with patch.dict(
            sys.modules,
            {
                "pip_audit": None,
                "detect_secrets": None,
            },
        ):
            # Force reimport
            import importlib

            import mfcqi.analysis.tools.detect_secrets_analyzer
            import mfcqi.analysis.tools.pip_audit_analyzer

            importlib.reload(mfcqi.analysis.tools.pip_audit_analyzer)
            importlib.reload(mfcqi.analysis.tools.detect_secrets_analyzer)

            # Import metrics AFTER analyzers are reloaded
            import mfcqi.metrics.dependency_security
            import mfcqi.metrics.secrets_exposure

            importlib.reload(mfcqi.metrics.dependency_security)
            importlib.reload(mfcqi.metrics.secrets_exposure)

            # Create temp test directory
            import tempfile

            from mfcqi.metrics.dependency_security import DependencySecurityMetric
            from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

            temp_dir = Path(tempfile.mkdtemp())

            # Metrics should work and return safe defaults
            dep_metric = DependencySecurityMetric()
            secrets_metric = SecretsExposureMetric()

            # Should return 0.0 (no vulnerabilities/secrets found)
            # because analyzers gracefully return empty results
            assert dep_metric.extract(temp_dir) == 0.0
            assert secrets_metric.extract(temp_dir) == 0.0

            # Normalized should be 1.0 (perfect score when no issues)
            assert dep_metric.normalize(0.0) == 1.0
            assert secrets_metric.normalize(0.0) == 1.0

            # Clean up
            import shutil

            shutil.rmtree(temp_dir, ignore_errors=True)
