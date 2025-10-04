"""
Aggregates and de-duplicates code smells from multiple detectors.

"""

from pathlib import Path

from mfcqi.smell_detection.detector_base import SmellDetector
from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity


class SmellAggregator:
    """Aggregates smells from multiple detectors and handles de-duplication.

    Based on code_smells.md recommendations:
    - Maintain shared smell taxonomy
    - De-duplicate when multiple tools report same smell
    - Keep highest severity when de-duplicating
    - Calculate weighted counts by category

    De-duplication Strategy:
        Two smells are considered duplicates if they have:
        - Same smell ID (e.g., "ASSERTION_ROULETTE")
        - Same location (file:line)

        When duplicates are found, keep the one with highest severity.

    Usage:
        detectors = [PytestSmellDetector(), PyExamineDetector()]
        aggregator = SmellAggregator(detectors)

        smells = aggregator.detect_all(codebase)
        counts = aggregator.count_by_category(codebase)
        weighted = aggregator.weighted_count_by_category(codebase)
    """

    def __init__(self, detectors: list[SmellDetector] | None = None):
        """Initialize aggregator with list of smell detectors.

        Args:
            detectors: List of SmellDetector instances to run
        """
        self.detectors = detectors or []

    def detect_all(self, codebase: Path) -> list[Smell]:
        """Run all detectors and return deduplicated list of smells.

        Args:
            codebase: Path to codebase root directory

        Returns:
            Deduplicated list of Smell objects
        """
        all_smells: list[Smell] = []

        # Run each detector and collect smells
        for detector in self.detectors:
            smells = detector.detect(codebase)
            all_smells.extend(smells)

        # Deduplicate smells
        deduplicated = self._deduplicate(all_smells)

        return deduplicated

    def count_by_category(self, codebase: Path) -> dict[SmellCategory, int]:
        """Count smells by category.

        Args:
            codebase: Path to codebase root directory

        Returns:
            Dictionary mapping SmellCategory to count
        """
        smells = self.detect_all(codebase)

        counts: dict[SmellCategory, int] = {}
        for smell in smells:
            counts[smell.category] = counts.get(smell.category, 0) + 1

        return counts

    def weighted_count_by_category(self, codebase: Path) -> dict[SmellCategory, float]:
        """Calculate severity-weighted counts by category.

        Uses severity_weight field from Smell objects:
        - HIGH: 3.0
        - MEDIUM: 2.0
        - LOW: 1.0

        Args:
            codebase: Path to codebase root directory

        Returns:
            Dictionary mapping SmellCategory to weighted count
        """
        smells = self.detect_all(codebase)

        weighted: dict[SmellCategory, float] = {}
        for smell in smells:
            weight = smell.severity_weight or 1.0
            weighted[smell.category] = weighted.get(smell.category, 0.0) + weight

        return weighted

    def _deduplicate(self, smells: list[Smell]) -> list[Smell]:
        """Deduplicate smells keeping highest severity.

        Two smells are duplicates if they have same id + location.

        Args:
            smells: List of potentially duplicate smells

        Returns:
            Deduplicated list with highest severity kept for each duplicate
        """
        if not smells:
            return []

        # Group smells by (id, location) tuple
        smell_groups: dict[tuple[str, str], list[Smell]] = {}

        for smell in smells:
            key = (smell.id, smell.location)
            if key not in smell_groups:
                smell_groups[key] = []
            smell_groups[key].append(smell)

        # For each group, keep the one with highest severity
        deduplicated: list[Smell] = []
        severity_order = {
            SmellSeverity.HIGH: 3,
            SmellSeverity.MEDIUM: 2,
            SmellSeverity.LOW: 1,
        }

        for group in smell_groups.values():
            if len(group) == 1:
                deduplicated.append(group[0])
            else:
                # Sort by severity (descending) and take first
                sorted_group = sorted(
                    group, key=lambda s: severity_order.get(s.severity, 0), reverse=True
                )
                deduplicated.append(sorted_group[0])

        return deduplicated
