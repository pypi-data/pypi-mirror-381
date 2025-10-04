"""
Code Smell Detection module for MFCQI.

This module provides multi-layer code smell detection based on research-backed
methodologies from peer-reviewed literature.

Key References:
==============
- PyExamine (MSR 2025): 49 metrics across code/structural/architectural layers
- pytest-smell (2022): Pytest-specific test smell detection
- Designite/DPy: Architectural and design smells

Architecture:
============
Three-layer detection approach:
1. Architectural/Design smells (weight: 0.45)
2. Implementation/Code smells (weight: 0.35)
3. Test smells (weight: 0.20)

"""

from mfcqi.smell_detection.detector_base import SmellDetector
from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity

__all__ = ["Smell", "SmellCategory", "SmellDetector", "SmellSeverity"]
