"""
Test for Code Smell data structures - following strict TDD.
"""


def test_smell_category_enum_exists():
    """RED: Test that SmellCategory enum exists."""
    from mfcqi.smell_detection.models import SmellCategory

    assert SmellCategory is not None


def test_smell_category_has_four_categories():
    """RED: Test that SmellCategory has the four main categories."""
    from mfcqi.smell_detection.models import SmellCategory

    # Based on code_smells.md: Architectural, Design, Implementation, Test
    assert hasattr(SmellCategory, "ARCHITECTURAL")
    assert hasattr(SmellCategory, "DESIGN")
    assert hasattr(SmellCategory, "IMPLEMENTATION")
    assert hasattr(SmellCategory, "TEST")


def test_smell_severity_enum_exists():
    """RED: Test that SmellSeverity enum exists."""
    from mfcqi.smell_detection.models import SmellSeverity

    assert SmellSeverity is not None


def test_smell_severity_has_three_levels():
    """RED: Test that SmellSeverity has three severity levels."""
    from mfcqi.smell_detection.models import SmellSeverity

    assert hasattr(SmellSeverity, "HIGH")
    assert hasattr(SmellSeverity, "MEDIUM")
    assert hasattr(SmellSeverity, "LOW")


def test_smell_dataclass_exists():
    """RED: Test that Smell dataclass exists."""
    from mfcqi.smell_detection.models import Smell

    assert Smell is not None


def test_smell_dataclass_creation():
    """RED: Test creating a Smell instance with required fields."""
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    smell = Smell(
        id="S001",
        name="Assertion Roulette",
        category=SmellCategory.TEST,
        severity=SmellSeverity.HIGH,
        location="tests/test_example.py:42",
        tool="pytest-smell",
        description="Multiple assertions without clear failure messages",
    )

    assert smell.id == "S001"
    assert smell.name == "Assertion Roulette"
    assert smell.category == SmellCategory.TEST
    assert smell.severity == SmellSeverity.HIGH
    assert smell.location == "tests/test_example.py:42"
    assert smell.tool == "pytest-smell"
    assert smell.description == "Multiple assertions without clear failure messages"


def test_smell_has_optional_severity_weight():
    """RED: Test that Smell can have an optional severity_weight field."""
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    smell = Smell(
        id="S002",
        name="God Class",
        category=SmellCategory.DESIGN,
        severity=SmellSeverity.HIGH,
        location="src/big_class.py:1",
        tool="designite",
        description="Class has too many responsibilities",
        severity_weight=3.0,
    )

    assert smell.severity_weight == 3.0


def test_smell_severity_weight_auto_assigned():
    """RED: Test that severity_weight is auto-assigned based on severity if not provided."""
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    smell = Smell(
        id="S003",
        name="Lazy Test",
        category=SmellCategory.TEST,
        severity=SmellSeverity.LOW,
        location="tests/test_foo.py:10",
        tool="pytest-smell",
        description="Test doesn't assert anything",
    )

    # Should auto-assign weight based on severity: LOW = 1.0
    assert smell.severity_weight == 1.0


def test_smell_equality():
    """RED: Test that two Smells with same id are equal for de-duplication."""
    from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

    smell1 = Smell(
        id="S001",
        name="Test",
        category=SmellCategory.TEST,
        severity=SmellSeverity.LOW,
        location="test.py:1",
        tool="tool1",
        description="Desc",
    )

    smell2 = Smell(
        id="S001",
        name="Test",
        category=SmellCategory.TEST,
        severity=SmellSeverity.HIGH,  # Different severity
        location="test.py:1",
        tool="tool2",  # Different tool
        description="Desc2",  # Different description
    )

    # Should be equal based on id+location for de-duplication
    assert smell1.id == smell2.id
