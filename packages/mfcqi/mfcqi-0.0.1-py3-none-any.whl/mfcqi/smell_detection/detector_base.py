"""
Base class for code smell detectors.

"""

from abc import ABC, abstractmethod
from pathlib import Path

from mfcqi.smell_detection.models import Smell


class SmellDetector(ABC):
    """Abstract base class for all smell detection tools.

    Each tool adapter (pytest-smell, PyExamine, Designite, etc.)
    should subclass this and implement the detect() method.

    The detector pattern allows:
    1. Uniform interface across different detection tools
    2. Easy addition of new detectors
    3. Consistent Smell output format
    4. Testable adapters

    Subclasses must implement:
    - detect(codebase): Run detection and return list of Smell objects
    - name: Property identifying the detector

    Example:
        class PytestSmellDetector(SmellDetector):
            @property
            def name(self) -> str:
                return "pytest-smell"

            def detect(self, codebase: Path) -> list[Smell]:
                # Run pytest-smell CLI
                # Parse output
                # Convert to Smell objects
                return smells
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of this detector for identification.

        Returns:
            str: Detector name (e.g., "pytest-smell", "pyexamine")
        """
        pass

    @abstractmethod
    def detect(self, codebase: Path) -> list[Smell]:
        """Detect code smells in the given codebase.

        Args:
            codebase: Path to the codebase root directory

        Returns:
            List of detected Smell objects

        Raises:
            FileNotFoundError: If codebase path doesn't exist
            RuntimeError: If detection tool fails to run
        """
        pass
