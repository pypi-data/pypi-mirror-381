"""
Integration tests for all metrics - converted from validation scripts.
Tests that all metrics work correctly on the MFCQI codebase itself.
"""

from pathlib import Path

from mfcqi.calculator import MFCQICalculator
from mfcqi.metrics.cohesion import LackOfCohesionOfMethods
from mfcqi.metrics.complexity import CyclomaticComplexity, HalsteadComplexity
from mfcqi.metrics.coupling import CouplingBetweenObjects
from mfcqi.metrics.documentation import DocumentationCoverage
from mfcqi.metrics.duplication import CodeDuplication
from mfcqi.metrics.maintainability import MaintainabilityIndex


class TestMetricsAnalysis:
    """Test all metrics individually on the MFCQI codebase."""

    def setup_method(self):
        """Set up test fixtures."""
        self.codebase = Path(__file__).parent.parent / "src" / "mfcqi"
        self.metrics = {
            "cyclomatic_complexity": CyclomaticComplexity(),
            "halstead_volume": HalsteadComplexity(),
            "maintainability_index": MaintainabilityIndex(),
            "code_duplication": CodeDuplication(),
            "documentation_coverage": DocumentationCoverage(),
            "coupling": CouplingBetweenObjects(),
            "cohesion": LackOfCohesionOfMethods(),
        }

    def test_all_metrics_extract_successfully(self):
        """Test that all metrics can extract values from the codebase."""
        for name, metric in self.metrics.items():
            raw_value = metric.extract(self.codebase)
            assert raw_value is not None, f"{name} returned None"
            assert isinstance(raw_value, (int, float)), (
                f"{name} returned non-numeric value: {type(raw_value)}"
            )

    def test_all_metrics_normalize_correctly(self):
        """Test that all metrics normalize to [0,1] range."""
        for name, metric in self.metrics.items():
            raw_value = metric.extract(self.codebase)
            normalized = metric.normalize(raw_value)

            assert 0.0 <= normalized <= 1.0, f"{name} normalized to {normalized} (out of bounds)"
            assert isinstance(normalized, float), (
                f"{name} normalized to non-float: {type(normalized)}"
            )

    def test_cyclomatic_complexity_reasonable_values(self):
        """Test that cyclomatic complexity returns reasonable values."""
        metric = self.metrics["cyclomatic_complexity"]
        raw_value = metric.extract(self.codebase)

        # Average complexity should be relatively low for good code
        assert 1.0 <= raw_value <= 20.0, f"Unexpected cyclomatic complexity: {raw_value}"

    def test_halstead_volume_reasonable_values(self):
        """Test that Halstead volume returns reasonable values."""
        metric = self.metrics["halstead_volume"]
        raw_value = metric.extract(self.codebase)

        # Volume should be positive
        assert raw_value > 0, f"Halstead volume should be positive: {raw_value}"

    def test_maintainability_index_reasonable_values(self):
        """Test that maintainability index returns reasonable values."""
        metric = self.metrics["maintainability_index"]
        raw_value = metric.extract(self.codebase)

        # MI should be between 0 and 100
        assert 0 <= raw_value <= 100, f"Maintainability index out of range: {raw_value}"

    def test_code_duplication_reasonable_values(self):
        """Test that code duplication returns reasonable values."""
        metric = self.metrics["code_duplication"]
        raw_value = metric.extract(self.codebase)

        # Duplication percentage should be between 0 and 100
        assert 0 <= raw_value <= 100, f"Code duplication out of range: {raw_value}"

    def test_documentation_coverage_reasonable_values(self):
        """Test that documentation coverage returns reasonable values."""
        metric = self.metrics["documentation_coverage"]
        raw_value = metric.extract(self.codebase)

        # Coverage is returned as percentage (0-100)
        assert 0 <= raw_value <= 100, f"Documentation coverage out of range: {raw_value}"

    def test_coupling_metric(self):
        """Test coupling between objects metric."""
        metric = self.metrics["coupling"]
        raw_value = metric.extract(self.codebase)

        # CBO should be non-negative
        assert raw_value >= 0, f"Coupling should be non-negative: {raw_value}"

    def test_cohesion_metric(self):
        """Test lack of cohesion metric."""
        metric = self.metrics["cohesion"]
        raw_value = metric.extract(self.codebase)

        # LCOM should be non-negative
        assert raw_value >= 0, f"Cohesion should be non-negative: {raw_value}"


class TestMFCQICalculation:
    """Test the overall MFCQI calculation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.codebase = Path(__file__).parent.parent / "src" / "mfcqi"

    def test_mfcqi_calculation_basic(self):
        """Test basic MFCQI calculation."""
        calculator = MFCQICalculator()
        score = calculator.calculate(self.codebase)

        assert 0.0 <= score <= 1.0, f"MFCQI score out of bounds: {score}"
        assert score > 0.3, f"MFCQI score unexpectedly low: {score}"

    def test_mfcqi_detailed_metrics(self):
        """Test getting detailed metrics from calculator."""
        calculator = MFCQICalculator()
        score = calculator.calculate(self.codebase)

        # Just verify the score is valid and calculator has expected attributes
        assert 0.0 <= score <= 1.0, f"MFCQI score out of bounds: {score}"
        assert hasattr(calculator, "metrics"), "Calculator should have metrics attribute"

        # Verify the calculator has expected metrics
        expected_metrics = [
            "cyclomatic_complexity",
            "halstead_volume",
            "maintainability_index",
            "code_duplication",
            "documentation_coverage",
        ]

        for metric_name in expected_metrics:
            assert metric_name in calculator.metrics or metric_name in calculator.core_metrics, (
                f"Missing metric: {metric_name}"
            )


class TestMetricConsistency:
    """Test that metrics are consistent across multiple runs."""

    def setup_method(self):
        """Set up test fixtures."""
        self.codebase = Path(__file__).parent.parent / "src" / "mfcqi"

    def test_metrics_are_deterministic(self):
        """Test that metrics return the same values on multiple runs."""
        metrics = {
            "cyclomatic": CyclomaticComplexity(),
            "halstead": HalsteadComplexity(),
            "maintainability": MaintainabilityIndex(),
            "documentation": DocumentationCoverage(),
        }

        for name, metric in metrics.items():
            # Run extraction twice
            value1 = metric.extract(self.codebase)
            value2 = metric.extract(self.codebase)

            # For maintainability, use a small tolerance due to floating-point precision
            if name == "maintainability":
                assert abs(value1 - value2) < 0.1, (
                    f"{name} returned different values: {value1} vs {value2}"
                )
            else:
                assert value1 == value2, f"{name} returned different values: {value1} vs {value2}"

    def test_mfcqi_score_is_deterministic(self):
        """Test that MFCQI score is consistent across runs."""
        calculator = MFCQICalculator()

        score1 = calculator.calculate(self.codebase)
        score2 = calculator.calculate(self.codebase)

        assert abs(score1 - score2) < 0.001, f"MFCQI scores differ: {score1} vs {score2}"
