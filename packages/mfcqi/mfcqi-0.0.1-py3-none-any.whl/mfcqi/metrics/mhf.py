"""
Method Hiding Factor (MHF) metric implementation.

MHF = Number of private methods / Total number of methods

This metric measures encapsulation by calculating the ratio of
private methods to total methods in a class.
"""

import ast
from pathlib import Path
from typing import Any, Union, cast

from mfcqi.core.file_utils import get_python_files
from mfcqi.core.metric import Metric


class MHFVisitor(ast.NodeVisitor):
    """AST visitor to calculate MHF for each class."""

    def __init__(self) -> None:
        self.classes: dict[str, float] = {}  # class_name -> MHF value
        self.current_class: str | None = None
        self.current_class_total_methods = 0
        self.current_class_private_methods = 0

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Visit a class definition and calculate its MHF."""
        old_class = self.current_class
        old_total = self.current_class_total_methods
        old_private = self.current_class_private_methods

        self.current_class = node.name
        self.current_class_total_methods = 0
        self.current_class_private_methods = 0

        # Visit all child nodes
        self.generic_visit(node)

        # Calculate MHF for this class
        if self.current_class_total_methods > 0:
            mhf_value = self.current_class_private_methods / self.current_class_total_methods
        else:
            mhf_value = 0.0

        self.classes[self.current_class] = mhf_value

        # Restore previous context
        self.current_class = old_class
        self.current_class_total_methods = old_total
        self.current_class_private_methods = old_private

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Visit a function definition within a class."""
        if self.current_class is not None:
            # This is a method within a class
            self.current_class_total_methods += 1

            # Check if it's private (starts with _ but not __)
            # According to Python conventions:
            # - _method: protected/private
            # - __method__: magic/special methods (not counted as private)
            # - __method: name-mangled private
            if node.name.startswith("_") and not node.name.startswith("__"):
                self.current_class_private_methods += 1

        self.generic_visit(node)

    def get_max_mhf(self) -> float:
        """Return the maximum MHF value among all classes."""
        if not self.classes:
            return 0.0
        return float(max(self.classes.values()))


class MHFMetric(Metric):
    """Method Hiding Factor (MHF) metric."""

    def extract(self, codebase: Path) -> float:
        """Extract MHF value from codebase.

        Returns the maximum MHF value among all classes in the codebase.
        """
        if not codebase.exists() or not codebase.is_dir():
            return 0.0

        max_mhf = 0.0
        py_files = get_python_files(codebase)

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding="utf-8")
                mhf_value = self.extract_from_string(content)
                max_mhf = max(max_mhf, mhf_value)
            except (OSError, UnicodeDecodeError, SyntaxError):
                continue

        return float(max_mhf)

    def extract_from_string(self, code: str) -> float:
        """Extract MHF value from code string.

        MHF = Number of private methods / Total number of methods
        """
        try:
            tree = ast.parse(code)
            visitor = MHFVisitor()
            visitor.visit(tree)
            return visitor.get_max_mhf()
        except SyntaxError:
            return 0.0

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """Normalize MHF value to [0,1] range.
        MHF is already in [0,1] range, so no normalization needed.
        """
        value = cast("float", value)  # This metric only returns float from extract()
        return value

    def get_weight(self) -> float:
        """Return evidence-based weight for MHF metric.

        Based on research: MHF measures encapsulation quality.
        """
        return 0.55

    def get_name(self) -> str:
        """Return the name of this metric."""
        return "mhf"
