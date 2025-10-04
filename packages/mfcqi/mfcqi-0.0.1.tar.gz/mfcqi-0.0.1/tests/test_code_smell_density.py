"""
Test for CodeSmellDensity metric - following strict TDD.
"""

import tempfile
import textwrap
from pathlib import Path


def test_code_smell_density_exists():
    """RED: Test that CodeSmellDensity class exists."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    assert CodeSmellDensity is not None


def test_code_smell_density_is_metric():
    """RED: Test that CodeSmellDensity implements Metric interface."""
    from mfcqi.core.metric import Metric
    from mfcqi.metrics.code_smell import CodeSmellDensity

    assert issubclass(CodeSmellDensity, Metric)


def test_no_smells_returns_perfect_score():
    """RED: Test codebase with no smells returns 1.0 (perfect)."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    # Create simple codebase with no smells
    code = textwrap.dedent("""
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "simple.py"
        test_file.write_text(code)

        metric = CodeSmellDensity()
        result = metric.extract(Path(tmpdir))

        # No smells = perfect score
        assert result == 0.0  # extract returns smell count, normalize converts to score


def test_extract_counts_smells():
    """RED: Test that extract() returns total weighted smell count per KLOC."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    # We'll need to mock detectors for this test
    # For now, just test that extract returns a numeric value
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text("def foo(): pass\n" * 100)  # 100 LOC

        metric = CodeSmellDensity()
        result = metric.extract(Path(tmpdir))

        # Should return a number
        assert isinstance(result, (int, float))
        assert result >= 0.0


def test_normalize_converts_to_quality_score():
    """RED: Test that normalize() converts smell count to quality score [0,1]."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()

    # 0 smells = perfect score (1.0)
    assert metric.normalize(0.0) == 1.0

    # High smell count = low score
    high_smell_score = metric.normalize(100.0)
    assert 0.0 <= high_smell_score <= 0.5

    # Moderate smell count = moderate score
    medium_smell_score = metric.normalize(10.0)
    assert 0.3 <= medium_smell_score <= 0.8

    # Low smell count = high score
    low_smell_score = metric.normalize(2.0)
    assert 0.7 <= low_smell_score < 1.0


def test_three_layer_weighting():
    """RED: Test that different smell categories have correct weights."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()

    # Weights from code_smells.md:
    # - Architectural/Design: 0.45
    # - Implementation: 0.35
    # - Test: 0.20
    weights = metric._get_category_weights()

    assert weights["architectural"] == 0.45
    assert weights["design"] == 0.45  # Design grouped with architectural
    assert weights["implementation"] == 0.35
    assert weights["test"] == 0.20


def test_metric_has_correct_name():
    """RED: Test that metric returns correct name."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()
    assert metric.get_name() == "Code Smell Density"


def test_metric_has_moderate_weight():
    """RED: Test that metric has moderate weight (0.5)."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()
    assert metric.get_weight() == 0.5


def test_smell_count_normalized_per_kloc():
    """RED: Test that smell counts are normalized per 1000 lines of code."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()

    # For a codebase with 500 LOC and 5 smells:
    # Should normalize to: (5 / 500) * 1000 = 10 smells per KLOC
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create file with ~500 lines
        code = "\n".join([f"def func{i}(): pass" for i in range(250)])
        test_file = Path(tmpdir) / "big.py"
        test_file.write_text(code)

        # Mock some smells - we'll integrate real detectors later
        result = metric.extract(Path(tmpdir))

        # For now, just check it returns reasonable value
        assert isinstance(result, (int, float))


def test_can_configure_detectors():
    """RED: Test that metric can be initialized with custom detectors."""
    from mfcqi.metrics.code_smell import CodeSmellDensity
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    class MockDetector(SmellDetector):
        @property
        def name(self) -> str:
            return "mock"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="MOCK001",
                    name="Mock Smell",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location="test.py:1",
                    tool="mock",
                    description="Mock smell for testing",
                )
            ]

    metric = CodeSmellDensity(detectors=[MockDetector()])
    assert metric is not None

    # Should be able to detect smells using custom detector
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text("def foo(): pass")

        result = metric.extract(Path(tmpdir))
        # Should have found the mock smell
        assert result > 0.0
