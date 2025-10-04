"""
Coupling Between Objects (CBO) metric implementation.
Based on CK metrics suite and research thresholds.
"""

import ast
from pathlib import Path
from typing import Any, Union, cast

from mfcqi.core.file_utils import get_python_files
from mfcqi.core.metric import Metric


class CouplingBetweenObjects(Metric):
    """Measures Coupling Between Objects (CBO) using static analysis."""

    def extract(self, codebase: Path) -> float:
        """Extract average CBO across all classes in the codebase."""
        if not codebase.exists() or not codebase.is_dir():
            return 0.0

        py_files = get_python_files(codebase)
        if not py_files:
            return 0.0

        class_coupling_scores = []

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding="utf-8")
                tree = ast.parse(content)

                # Get coupling for each class in this file
                file_coupling = self._analyze_file_coupling(tree, content)
                class_coupling_scores.extend(file_coupling)

            except (SyntaxError, UnicodeDecodeError, Exception):
                continue

        if not class_coupling_scores:
            return 0.0

        # Return average CBO across all classes
        return sum(class_coupling_scores) / len(class_coupling_scores)

    def _analyze_file_coupling(self, tree: ast.AST, content: str) -> list[float]:
        """Analyze coupling for all classes in a file."""
        coupling_scores = []

        # Find all class definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                cbo_score = self._calculate_class_coupling(node, tree, content)
                coupling_scores.append(cbo_score)

        return coupling_scores

    def _calculate_class_coupling(
        self, class_node: ast.ClassDef, tree: ast.AST, content: str
    ) -> float:
        """Calculate CBO for a single class."""
        coupled_classes = set()

        # Collect coupling from different sources
        coupled_classes.update(self._get_method_coupling(class_node))
        coupled_classes.update(self._get_annotation_coupling(class_node))
        coupled_classes.update(self._get_usage_coupling(class_node))
        coupled_classes.update(self._get_inheritance_coupling(class_node))

        # Filter out built-ins and self-references
        filtered_coupling = {
            cls
            for cls in coupled_classes
            if cls != class_node.name and self._is_meaningful_coupling(cls)
        }

        return float(len(filtered_coupling))

    def _get_method_coupling(self, class_node: ast.ClassDef) -> set[str]:
        """Get coupling from method signatures."""
        coupled = set()
        for node in ast.walk(class_node):
            if isinstance(node, ast.FunctionDef):
                # Check return annotation
                if node.returns:
                    type_name = self._extract_type_name(node.returns)
                    if type_name and self._is_external_type(type_name):
                        coupled.add(type_name)

                # Check parameter annotations
                for arg in node.args.args:
                    if arg.annotation:
                        type_name = self._extract_type_name(arg.annotation)
                        if type_name and self._is_external_type(type_name):
                            coupled.add(type_name)
        return coupled

    def _get_annotation_coupling(self, class_node: ast.ClassDef) -> set[str]:
        """Get coupling from variable annotations."""
        coupled = set()
        for node in ast.walk(class_node):
            if isinstance(node, ast.AnnAssign) and node.annotation:
                type_name = self._extract_type_name(node.annotation)
                if type_name and self._is_external_type(type_name):
                    coupled.add(type_name)
        return coupled

    def _get_usage_coupling(self, class_node: ast.ClassDef) -> set[str]:
        """Get coupling from attribute access and function calls."""
        coupled = set()
        for node in ast.walk(class_node):
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    coupled.add(node.value.id)
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    coupled.add(node.func.id)
                elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    coupled.add(node.func.value.id)
        return coupled

    def _get_inheritance_coupling(self, class_node: ast.ClassDef) -> set[str]:
        """Get coupling from base classes."""
        coupled = set()
        for base in class_node.bases:
            base_name = self._extract_type_name(base)
            if base_name and self._is_external_type(base_name):
                coupled.add(base_name)
        return coupled

    def _extract_type_name(self, annotation: ast.AST) -> str:
        """Extract type name from annotation node."""
        if isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Attribute):
            # Handle qualified names like typing.List
            return annotation.attr
        elif isinstance(annotation, ast.Subscript):
            # Handle generic types like List[str]
            return self._extract_type_name(annotation.value)
        return ""

    def _is_external_type(self, type_name: str) -> bool:
        """Check if type represents external coupling."""
        # Exclude built-in types
        builtin_types = {
            "int",
            "float",
            "str",
            "bool",
            "list",
            "dict",
            "set",
            "tuple",
            "None",
            "object",
            "type",
            "bytes",
            "bytearray",
        }
        return type_name not in builtin_types

    def _is_meaningful_coupling(self, class_name: str) -> bool:
        """Filter out noise to focus on meaningful coupling."""
        # Exclude very common/utility names that don't represent real coupling
        noise_names = {
            "self",
            "cls",
            "super",
            "len",
            "str",
            "int",
            "float",
            "bool",
            "list",
            "dict",
            "set",
            "tuple",
            "range",
            "enumerate",
            "zip",
            "print",
            "open",
            "file",
            "path",
            "os",
            "sys",
        }
        return class_name not in noise_names and len(class_name) > 1

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """Normalize CBO to [0,1] range where lower coupling is better.
        Based on research thresholds:
        - CBO <= 9: Good coupling (0.7-1.0)
        - CBO 10-20: Moderate coupling (0.4-0.7)
        - CBO > 20: High coupling (0.0-0.4)
        """
        value = cast("float", value)  # This metric only returns float from extract()
        if value <= 0:
            return 1.0  # No coupling = perfect
        elif value <= 9:
            # Excellent to good: 0-9 maps to 1.0-0.7
            return 1.0 - (value / 9) * 0.3
        elif value <= 20:
            # Moderate: 10-20 maps to 0.7-0.4
            return 0.7 - ((value - 9) / 11) * 0.3
        else:
            # Poor: 20+ maps to 0.4-0.0
            return max(0.0, 0.4 - ((value - 20) / 20) * 0.4)

    def get_weight(self) -> float:
        """Return evidence-based weight for coupling.

        Weight: 0.65 (reduced from 0.8)
        Justification:
        - CBO is a key Chidamber & Kemerer metric
        - High coupling correlates with maintenance difficulty
        - Studies show coupling as good indicator of maintainability
        - Less direct defect correlation than complexity metrics
        - Optional metric (only when coupling/cohesion check triggers)
        """
        return 0.65

    def get_name(self) -> str:
        """Return the name of this metric."""
        return "Coupling Between Objects"
