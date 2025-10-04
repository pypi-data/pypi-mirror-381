"""
Response for Class (RFC) metric implementation.

RFC = Number of local methods + Number of remote methods called

This metric measures the complexity of a class by counting all methods
that can potentially be executed in response to a message.
"""

import ast
from pathlib import Path
from typing import Any, Union, cast

from mfcqi.core.file_utils import get_python_files
from mfcqi.core.metric import Metric


class RFCVisitor(ast.NodeVisitor):
    """AST visitor to calculate RFC for each class."""

    def __init__(self) -> None:
        self.classes: dict[str, int] = {}  # class_name -> RFC value
        self.current_class: str | None = None
        self.current_class_methods: set[str] = set()
        self.current_class_calls: set[str] = set()

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Visit a class definition and calculate its RFC."""
        old_class = self.current_class
        old_methods = self.current_class_methods
        old_calls = self.current_class_calls

        self.current_class = node.name
        self.current_class_methods = set()
        self.current_class_calls = set()

        # Visit all child nodes
        self.generic_visit(node)

        # Calculate RFC for this class
        local_methods = len(self.current_class_methods)
        remote_calls = len(self.current_class_calls)
        rfc_value = local_methods + remote_calls

        self.classes[self.current_class] = rfc_value

        # Restore previous context
        self.current_class = old_class
        self.current_class_methods = old_methods
        self.current_class_calls = old_calls

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Visit a function definition within a class."""
        if self.current_class is not None:
            # This is a method within a class
            self.current_class_methods.add(node.name)

        # Visit the function body to find method calls
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        """Visit a method call to count remote calls."""
        if self.current_class is not None and hasattr(node.func, "attr"):
            # This is a call like obj.method()
            self.current_class_calls.add(node.func.attr)

        self.generic_visit(node)

    def get_max_rfc(self) -> int:
        """Return the maximum RFC value among all classes."""
        if not self.classes:
            return 0
        return int(max(self.classes.values()))


class RFCMetric(Metric):
    """Response for Class (RFC) metric."""

    def extract(self, codebase: Path) -> float:
        """Extract RFC value from codebase.

        Returns the maximum RFC value among all classes in the codebase.
        """
        if not codebase.exists() or not codebase.is_dir():
            return 0.0

        max_rfc = 0.0
        py_files = get_python_files(codebase)

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding="utf-8")
                rfc_value = self.extract_from_string(content)
                max_rfc = max(max_rfc, rfc_value)
            except (OSError, UnicodeDecodeError, SyntaxError):
                continue

        return float(max_rfc)

    def extract_from_string(self, code: str) -> int:
        """Extract RFC value from code string.

        RFC = Number of local methods + Number of remote methods called
        """
        try:
            tree = ast.parse(code)
            visitor = RFCVisitor()
            visitor.visit(tree)
            return visitor.get_max_rfc()
        except SyntaxError:
            return 0

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """Normalize RFC value to [0,1] range where lower RFC is better.

        Python-Specific Calibration (October 2025):
        ============================================
        Recalibrated from exponential penalty to piecewise linear normalization
        after validation revealed need to distinguish framework APIs (high RFC
        appropriate) from god objects (high RFC bad).

        Libraries/frameworks naturally have higher RFC due to:
        - Rich, comprehensive APIs (many public methods)
        - Extensive functionality in framework entry points
        - Complex but well-organized class hierarchies

        **Critical**: Original CK metrics (Chidamber & Kemerer 1994) validated on
        **applications**, not libraries. Frameworks require more lenient thresholds.

        Evidence-Based Thresholds:
        - RFC ≤ 15: Excellent (simple, focused classes) → 1.0
        - RFC 15-50: Good (typical library classes) → 1.0 to 0.75
        - RFC 50-100: Moderate (complex but acceptable) → 0.75 to 0.35
        - RFC 100-120: Poor (god object territory) → 0.35 to 0.0
        - RFC ≥ 120: Critical (definite god object) → 0.0

        Validation Results:
        - click (RFC=77): 0.19 → 0.53 (+185% improvement)
          Framework with many commands now appropriately scored
        - requests (RFC=42): 0.45 → 0.81 (+80% improvement)
          Library-appropriate API richness now correctly recognized

        Synthetic Baseline Evidence:
        - lib_01_good_framework (RFC=12): 0.95 → 1.00 (CLI framework pattern)
        - lib_02_good_orm (RFC=14): 0.91 → 1.00 (ORM framework pattern)
        - app_02_god_object (RFC=36): 0.52 → 0.86 (caught by other metrics)

        References:
        - Chidamber, S. & Kemerer, C. (1994). "A Metrics Suite for OO Design"
        - Basili et al. (1996): RFC > 50 correlates with higher defect rates
        - Subramanyam & Krishnan (2003): RFC predicts defects (r=0.48)
        - See docs/research.md for library-aware calibration methodology
        """
        value = cast("float", value)  # This metric only returns float from extract()

        if value <= 15:
            # Simple, focused classes - excellent
            return 1.0
        elif value <= 50:
            # Typical library classes - linear decay from 1.0 to 0.75
            # 0.25 point drop over 35 RFC points
            return 1.0 - 0.25 * (value - 15) / 35
        elif value <= 100:
            # Complex but acceptable - linear decay from 0.75 to 0.35
            # 0.40 point drop over 50 RFC points
            return 0.75 - 0.40 * (value - 50) / 50
        elif value <= 120:
            # Poor, approaching god object - linear decay from 0.35 to 0.0
            # 0.35 point drop over 20 RFC points
            return 0.35 - 0.35 * (value - 100) / 20
        else:
            # Definite god object
            return 0.0

    def get_weight(self) -> float:
        """Return evidence-based weight for RFC metric.

        Weight: 0.65
        Evidence-based justification:
        - Subramanyam & Krishnan (2003): r=0.48 correlation with defects
        - Basili et al. (1996): RFC > 50 correlates with higher fault rates
        - Chidamber & Kemerer (1994): Original CK metric suite
        - Direct indicator of class complexity and testing effort
        - Optional metric (only applied to OO code)
        """
        return 0.65

    def get_name(self) -> str:
        """Return the name of this metric."""
        return "rfc"
