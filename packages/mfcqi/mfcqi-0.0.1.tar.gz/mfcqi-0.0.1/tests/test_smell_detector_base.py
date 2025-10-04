"""
Test for SmellDetector base class - following strict TDD.
"""

import tempfile
from pathlib import Path


def test_smell_detector_exists():
    """RED: Test that SmellDetector base class exists."""
    from mfcqi.smell_detection.detector_base import SmellDetector

    assert SmellDetector is not None


def test_smell_detector_is_abstract():
    """RED: Test that SmellDetector is an abstract base class."""
    from abc import ABC

    from mfcqi.smell_detection.detector_base import SmellDetector

    assert issubclass(SmellDetector, ABC)


def test_smell_detector_has_detect_method():
    """RED: Test that SmellDetector has abstract detect() method."""
    import inspect

    from mfcqi.smell_detection.detector_base import SmellDetector

    # Check that detect method exists
    assert hasattr(SmellDetector, "detect")

    # Check that it's abstract
    assert inspect.isabstract(SmellDetector)


def test_smell_detector_detect_signature():
    """RED: Test that detect() has correct signature: (codebase: Path) -> List[Smell]."""
    from typing import get_type_hints

    from mfcqi.smell_detection.detector_base import SmellDetector

    # Get type hints for detect method
    hints = get_type_hints(SmellDetector.detect)

    # Check parameter types
    assert "codebase" in hints
    assert hints["codebase"] == Path

    # Check return type is List[Smell]
    assert "return" in hints
    # Return type will be list[Smell] in Python 3.13


def test_smell_detector_cannot_be_instantiated():
    """RED: Test that SmellDetector cannot be instantiated directly."""
    from mfcqi.smell_detection.detector_base import SmellDetector

    # Should raise TypeError because it's abstract
    try:
        SmellDetector()
        raise AssertionError("Should not be able to instantiate abstract SmellDetector")
    except TypeError as e:
        assert "abstract" in str(e).lower()


def test_concrete_detector_subclass_works():
    """RED: Test that a concrete subclass of SmellDetector can be instantiated."""
    from mfcqi.smell_detection.detector_base import SmellDetector
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    # Create a concrete subclass for testing
    class TestDetector(SmellDetector):
        @property
        def name(self) -> str:
            return "test-detector"

        def detect(self, codebase: Path) -> list[Smell]:
            return [
                Smell(
                    id="TEST001",
                    name="Test Smell",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location="test.py:1",
                    tool="test-detector",
                    description="Test smell description",
                )
            ]

    # Should be able to instantiate
    detector = TestDetector()
    assert detector is not None

    # Should be able to call detect
    with tempfile.TemporaryDirectory() as tmpdir:
        smells = detector.detect(Path(tmpdir))
        assert len(smells) == 1
        assert smells[0].id == "TEST001"


def test_smell_detector_has_name_property():
    """RED: Test that SmellDetector has a name property for identification."""
    from mfcqi.smell_detection.detector_base import SmellDetector

    assert hasattr(SmellDetector, "name")
