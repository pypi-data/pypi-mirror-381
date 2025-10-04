"""
Test for SmellAggregator - following strict TDD.
"""

from pathlib import Path


def test_smell_aggregator_exists():
    """RED: Test that SmellAggregator class exists."""
    from mfcqi.smell_detection.aggregator import SmellAggregator

    assert SmellAggregator is not None


def test_aggregator_accepts_detectors():
    """RED: Test that aggregator can be initialized with list of detectors."""
    from mfcqi.smell_detection.aggregator import SmellAggregator
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell

    class MockDetector(SmellDetector):
        @property
        def name(self) -> str:
            return "mock"

        def detect(self, codebase: Path) -> list[Smell]:
            return []

    aggregator = SmellAggregator(detectors=[MockDetector()])
    assert aggregator is not None


def test_aggregator_runs_all_detectors():
    """RED: Test that aggregator runs all configured detectors."""
    import tempfile

    from mfcqi.smell_detection.aggregator import SmellAggregator
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    class MockDetector1(SmellDetector):
        @property
        def name(self) -> str:
            return "mock1"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="S001",
                    name="Test Smell 1",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location="test1.py:1",
                    tool="mock1",
                    description="First smell",
                )
            ]

    class MockDetector2(SmellDetector):
        @property
        def name(self) -> str:
            return "mock2"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="S002",
                    name="Test Smell 2",
                    category=SmellCategory.IMPLEMENTATION,
                    severity=SmellSeverity.MEDIUM,
                    location="test2.py:10",
                    tool="mock2",
                    description="Second smell",
                )
            ]

    aggregator = SmellAggregator(detectors=[MockDetector1(), MockDetector2()])

    with tempfile.TemporaryDirectory() as tmpdir:
        smells = aggregator.detect_all(Path(tmpdir))

    # Should have smells from both detectors
    assert len(smells) == 2


def test_aggregator_deduplicates_same_smell():
    """RED: Test that aggregator removes duplicate smells from different tools."""
    import tempfile

    from mfcqi.smell_detection.aggregator import SmellAggregator
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    # Two detectors that find the same smell (same id + location)
    class Detector1(SmellDetector):
        @property
        def name(self) -> str:
            return "detector1"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="ASSERTION_ROULETTE",
                    name="Assertion Roulette",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location="tests/test_foo.py:42",
                    tool="detector1",
                    description="Multiple assertions without messages",
                )
            ]

    class Detector2(SmellDetector):
        @property
        def name(self) -> str:
            return "detector2"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="ASSERTION_ROULETTE",
                    name="Assertion Roulette",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.MEDIUM,  # Different severity
                    location="tests/test_foo.py:42",  # Same location
                    tool="detector2",
                    description="Too many assertions",
                )
            ]

    aggregator = SmellAggregator(detectors=[Detector1(), Detector2()])

    with tempfile.TemporaryDirectory() as tmpdir:
        smells = aggregator.detect_all(Path(tmpdir))

    # Should deduplicate to 1 smell
    assert len(smells) == 1


def test_aggregator_keeps_highest_severity_when_deduplicating():
    """RED: Test that when deduplicating, the smell with highest severity is kept."""
    import tempfile

    from mfcqi.smell_detection.aggregator import SmellAggregator
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    class Detector1(SmellDetector):
        @property
        def name(self) -> str:
            return "detector1"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="GOD_CLASS",
                    name="God Class",
                    category=SmellCategory.DESIGN,
                    severity=SmellSeverity.LOW,  # Lower severity
                    location="src/big.py:1",
                    tool="detector1",
                    description="Large class",
                )
            ]

    class Detector2(SmellDetector):
        @property
        def name(self) -> str:
            return "detector2"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="GOD_CLASS",
                    name="God Class",
                    category=SmellCategory.DESIGN,
                    severity=SmellSeverity.HIGH,  # Higher severity
                    location="src/big.py:1",
                    tool="detector2",
                    description="Very large class",
                )
            ]

    aggregator = SmellAggregator(detectors=[Detector1(), Detector2()])

    with tempfile.TemporaryDirectory() as tmpdir:
        smells = aggregator.detect_all(Path(tmpdir))

    assert len(smells) == 1
    # Should keep the HIGH severity one
    assert smells[0].severity == SmellSeverity.HIGH


def test_aggregator_counts_by_category():
    """RED: Test that aggregator can count smells by category."""
    import tempfile

    from mfcqi.smell_detection.aggregator import SmellAggregator
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    class MockDetector(SmellDetector):
        @property
        def name(self) -> str:
            return "mock"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="S1",
                    name="Test1",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location="t1.py:1",
                    tool="mock",
                    description="Test smell",
                ),
                Smell(
                    id="S2",
                    name="Test2",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location="t2.py:1",
                    tool="mock",
                    description="Another test smell",
                ),
                Smell(
                    id="S3",
                    name="Design1",
                    category=SmellCategory.DESIGN,
                    severity=SmellSeverity.HIGH,
                    location="d1.py:1",
                    tool="mock",
                    description="Design smell",
                ),
            ]

    aggregator = SmellAggregator(detectors=[MockDetector()])

    with tempfile.TemporaryDirectory() as tmpdir:
        counts = aggregator.count_by_category(Path(tmpdir))

    # Should have counts per category
    assert counts[SmellCategory.TEST] == 2
    assert counts[SmellCategory.DESIGN] == 1
    assert counts.get(SmellCategory.IMPLEMENTATION, 0) == 0
    assert counts.get(SmellCategory.ARCHITECTURAL, 0) == 0


def test_aggregator_calculates_weighted_counts():
    """RED: Test that aggregator can calculate severity-weighted counts."""
    import tempfile

    from mfcqi.smell_detection.aggregator import SmellAggregator
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    class MockDetector(SmellDetector):
        @property
        def name(self) -> str:
            return "mock"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="S1",
                    name="High Severity",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.HIGH,  # weight 3.0
                    location="t1.py:1",
                    tool="mock",
                    description="High",
                ),
                Smell(
                    id="S2",
                    name="Low Severity",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,  # weight 1.0
                    location="t2.py:1",
                    tool="mock",
                    description="Low",
                ),
            ]

    aggregator = SmellAggregator(detectors=[MockDetector()])

    with tempfile.TemporaryDirectory() as tmpdir:
        weighted = aggregator.weighted_count_by_category(Path(tmpdir))

    # TEST category should have: HIGH (3.0) + LOW (1.0) = 4.0
    assert weighted[SmellCategory.TEST] == 4.0
