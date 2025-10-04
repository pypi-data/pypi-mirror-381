"""
Data structures for code smell detection.

"""

from dataclasses import dataclass
from enum import Enum


class SmellCategory(Enum):
    """Categories of code smells based on code_smells.md recommendations.

    Three-layer architecture:
    - ARCHITECTURAL: High-level system structure issues
    - DESIGN: Class-level design problems
    - IMPLEMENTATION: Code-level issues
    - TEST: Test-specific smells

    References:
    - PyExamine (MSR 2025): Three-layer categorization
    - code_smells.md: Architectural (0.45), Implementation (0.35), Test (0.20) weights
    """

    ARCHITECTURAL = "architectural"
    DESIGN = "design"
    IMPLEMENTATION = "implementation"
    TEST = "test"


class SmellSeverity(Enum):
    """Severity levels for code smells.

    Used for weighted counting when aggregating smells.
    Higher severity smells have more impact on quality score.

    Typical weights:
    - HIGH: 3.0
    - MEDIUM: 2.0
    - LOW: 1.0
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class Smell:
    """Represents a detected code smell.

    This is the standard representation used across all smell detectors.
    Each tool adapter converts its output to this format.

    Attributes:
        id: Unique identifier for the smell type (e.g., "S001", "ASSERTION_ROULETTE")
        name: Human-readable name of the smell (e.g., "Assertion Roulette")
        category: The layer this smell belongs to (architectural/design/implementation/test)
        severity: Impact level (high/medium/low)
        location: File path and line number (e.g., "tests/test_foo.py:42")
        tool: Name of the tool that detected this smell (e.g., "pytest-smell")
        description: Detailed description of the smell instance
        severity_weight: Optional numeric weight for this severity (defaults based on severity)

    De-duplication:
        Two Smells are considered duplicates if they have the same id+location.
        When de-duplicating, keep the one with highest severity.
    """

    id: str
    name: str
    category: SmellCategory
    severity: SmellSeverity
    location: str
    tool: str
    description: str
    severity_weight: float | None = None

    def __post_init__(self) -> None:
        """Set default severity weight if not provided."""
        if self.severity_weight is None:
            # Default weights from code_smells.md recommendations
            weight_map = {
                SmellSeverity.HIGH: 3.0,
                SmellSeverity.MEDIUM: 2.0,
                SmellSeverity.LOW: 1.0,
            }
            self.severity_weight = weight_map.get(self.severity, 1.0)
