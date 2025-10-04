"""
Test for the core Metric interface - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

from abc import ABC
from pathlib import Path

import pytest


def test_metric_interface_exists():
    """RED: Test that the Metric abstract base class exists."""
    from mfcqi.core.metric import Metric

    assert issubclass(Metric, ABC)


def test_metric_has_required_methods():
    """RED: Test that Metric has the required abstract methods."""
    from mfcqi.core.metric import Metric

    # Check that required methods exist
    assert hasattr(Metric, "extract")
    assert hasattr(Metric, "normalize")
    assert hasattr(Metric, "get_weight")
    assert hasattr(Metric, "get_name")


def test_metric_extract_is_abstract():
    """RED: Test that extract method is abstract and requires implementation."""
    from mfcqi.core.metric import Metric

    class IncompleteMetric(Metric):
        pass

    # Should raise TypeError because extract is not implemented
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        IncompleteMetric()


def test_metric_extract_signature():
    """RED: Test that extract method has correct signature."""
    from mfcqi.core.metric import Metric

    class TestMetric(Metric):
        def extract(self, codebase: Path) -> float:
            return 0.5

        def normalize(self, value: float) -> float:
            return value

        def get_weight(self) -> float:
            return 1.0

        def get_name(self) -> str:
            return "test"

    metric = TestMetric()
    result = metric.extract(Path())
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


def test_metric_normalize_bounds():
    """RED: Test that normalize returns values in [0,1] range."""
    from mfcqi.core.metric import Metric

    class TestMetric(Metric):
        def extract(self, codebase: Path) -> float:
            return 100.0

        def normalize(self, value: float) -> float:
            return min(1.0, max(0.0, value / 100.0))

        def get_weight(self) -> float:
            return 1.0

        def get_name(self) -> str:
            return "test"

    metric = TestMetric()

    # Test normalization bounds
    assert metric.normalize(-10) == 0.0
    assert metric.normalize(50) == 0.5
    assert metric.normalize(150) == 1.0


def test_metric_calculate_template_method():
    """Test the calculate template method workflow."""
    import tempfile

    from mfcqi.core.metric import Metric

    class TestMetric(Metric):
        def extract(self, codebase: Path) -> float:
            return 100.0

        def normalize(self, value: float) -> float:
            return 0.8

        def get_weight(self) -> float:
            return 0.75

        def get_name(self) -> str:
            return "TestMetric"

    metric = TestMetric()

    with tempfile.TemporaryDirectory() as tmpdir:
        result = metric.calculate(Path(tmpdir))

        # Verify result structure
        assert "metric_name" in result
        assert result["metric_name"] == "TestMetric"
        assert result["raw_value"] == 100.0
        assert result["normalized_value"] == 0.8
        assert result["weight"] == 0.75
        assert result["weighted_value"] == 0.8 * 0.75


def test_metric_calculate_invalid_codebase():
    """Test calculate with invalid codebase path."""
    from mfcqi.core.metric import Metric

    class TestMetric(Metric):
        def extract(self, codebase: Path) -> float:
            return 50.0

        def normalize(self, value: float) -> float:
            return 0.5

        def get_weight(self) -> float:
            return 0.5

        def get_name(self) -> str:
            return "TestMetric"

    metric = TestMetric()
    result = metric.calculate(Path("/nonexistent/path"))

    # Should return error result
    assert "error" in result
    assert result["error"] == "Invalid codebase path"
    assert result["raw_value"] == 0.0
    assert result["normalized_value"] == 0.0


def test_metric_validate_codebase():
    """Test _validate_codebase method."""
    import tempfile

    from mfcqi.core.metric import Metric

    class TestMetric(Metric):
        def extract(self, codebase: Path) -> float:
            return 1.0

        def normalize(self, value: float) -> float:
            return 1.0

        def get_weight(self) -> float:
            return 1.0

        def get_name(self) -> str:
            return "Test"

    metric = TestMetric()

    # Valid directory
    with tempfile.TemporaryDirectory() as tmpdir:
        assert metric._validate_codebase(Path(tmpdir)) is True

    # Non-existent path
    assert metric._validate_codebase(Path("/nonexistent")) is False


def test_metric_hooks():
    """Test optional hook methods."""
    import tempfile

    from mfcqi.core.metric import Metric

    calls = []

    class TestMetric(Metric):
        def extract(self, codebase: Path) -> float:
            return 10.0

        def normalize(self, value: float) -> float:
            return 0.5

        def get_weight(self) -> float:
            return 0.6

        def get_name(self) -> str:
            return "TestHook"

        def _pre_process(self, codebase: Path) -> None:
            calls.append("pre")

        def _post_process_raw(self, raw_value: float) -> float:
            calls.append("post_raw")
            return raw_value * 2

        def _post_calculate(self, result: dict) -> None:
            calls.append("post_calc")

    metric = TestMetric()

    with tempfile.TemporaryDirectory() as tmpdir:
        result = metric.calculate(Path(tmpdir))

        # Verify hooks were called
        assert "pre" in calls
        assert "post_raw" in calls
        assert "post_calc" in calls

        # Verify post_process_raw modified the value
        assert result["processed_value"] == 20.0  # 10.0 * 2
