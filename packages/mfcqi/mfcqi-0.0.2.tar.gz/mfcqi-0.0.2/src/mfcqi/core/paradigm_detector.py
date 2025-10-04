"""
Paradigm Detection for Python Code.

Detects whether Python code is object-oriented, procedural, or functional
to determine which metrics should be applied for quality assessment.
"""

import ast
import typing
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from mfcqi.core.file_utils import get_python_files


@dataclass
class ParadigmMetrics:
    """Metrics for determining code paradigm."""

    total_lines: int = 0
    total_classes: int = 0
    total_functions: int = 0
    class_methods: int = 0
    standalone_functions: int = 0
    inheritance_count: int = 0
    multiple_inheritance_count: int = 0
    private_methods: int = 0
    properties: int = 0
    composition_count: int = 0
    oo_imports: int = 0
    procedural_imports: int = 0


class ParadigmDetector:
    """Detects the primary programming paradigm of Python code."""

    # OO-indicating imports
    OO_IMPORTS: typing.ClassVar[set[str]] = {
        "abc",
        "dataclasses",
        "typing",
        "enum",
        "collections.abc",
        "typing_extensions",
        "attrs",
        "pydantic",
    }

    # Procedural/functional imports
    PROCEDURAL_IMPORTS: typing.ClassVar[set[str]] = {
        "functools",
        "itertools",
        "operator",
        "math",
        "statistics",
        "numpy",
        "scipy",
        "pandas",
        "sklearn",
        "matplotlib",
    }

    def __init__(self) -> None:
        self.metrics = ParadigmMetrics()

    def detect_paradigm(self, codebase_path: Path) -> dict[str, Any]:
        """
        Detect the primary paradigm of a Python codebase.

        Args:
            codebase_path: Path to the codebase to analyze

        Returns:
            Dictionary with paradigm classification and metrics
        """
        self.metrics = ParadigmMetrics()

        # Analyze all Python files
        py_files = get_python_files(codebase_path)
        if not py_files:
            return self._create_result("UNKNOWN", 0.0)

        for py_file in py_files:
            # Skip test files for paradigm detection
            if "test" in str(py_file).lower():
                continue

            try:
                content = py_file.read_text(encoding="utf-8")
                tree = ast.parse(content)
                self._analyze_file(tree, content)
            except (SyntaxError, UnicodeDecodeError):
                continue

        # Calculate OO score
        oo_score = self._calculate_oo_score()
        paradigm = self._classify_paradigm(oo_score)

        return self._create_result(paradigm, oo_score)

    def _analyze_file(self, tree: ast.AST, content: str) -> None:
        """Analyze a single Python file for paradigm indicators."""
        self.metrics.total_lines += len(content.splitlines())

        # Use visitor to collect metrics
        visitor = ParadigmVisitor()
        visitor.visit(tree)

        # Update metrics
        self.metrics.total_classes += visitor.classes
        self.metrics.total_functions += visitor.functions
        self.metrics.class_methods += visitor.class_methods
        self.metrics.standalone_functions += visitor.standalone_functions
        self.metrics.inheritance_count += visitor.inheritance_count
        self.metrics.multiple_inheritance_count += visitor.multiple_inheritance
        self.metrics.private_methods += visitor.private_methods
        self.metrics.properties += visitor.properties
        self.metrics.composition_count += visitor.composition_count
        self.metrics.oo_imports += visitor.oo_imports
        self.metrics.procedural_imports += visitor.procedural_imports

    def _calculate_oo_score(self) -> float:
        """Calculate object-oriented score from collected metrics."""
        if self.metrics.total_lines == 0:
            return 0.0

        # Prevent division by zero
        max(1, self.metrics.total_classes + self.metrics.total_functions)

        # Base OO indicators (0-1 scale)
        class_density = min(
            (self.metrics.total_classes / max(1, self.metrics.total_lines)) * 1000 / 5, 1.0
        )

        method_ratio = min(
            self.metrics.class_methods / max(1, self.metrics.standalone_functions), 1.0
        )

        inheritance_usage = min(
            self.metrics.inheritance_count / max(1, self.metrics.total_classes), 1.0
        )

        # Advanced OO features (bonus)
        encapsulation_score = min(
            self.metrics.private_methods / max(1, self.metrics.class_methods), 0.3
        )

        composition_score = min(
            self.metrics.composition_count / max(1, self.metrics.total_classes), 0.2
        )

        property_score = min(self.metrics.properties / max(1, self.metrics.class_methods), 0.2)

        # Import patterns
        import_score = 0.0
        if self.metrics.oo_imports > 0:
            import_score += 0.1
        if self.metrics.procedural_imports > self.metrics.oo_imports:
            import_score -= 0.1

        # Weighted composite score
        oo_score = (
            class_density * 0.3  # 30% - Class presence
            + method_ratio * 0.25  # 25% - Method vs function ratio
            + inheritance_usage * 0.2  # 20% - Inheritance usage
            + encapsulation_score  # Up to 30% - Encapsulation
            + composition_score  # Up to 20% - Composition
            + property_score  # Up to 20% - Properties
            + import_score  # ±10% - Import patterns
        )

        return max(0.0, min(1.0, oo_score))

    def _classify_paradigm(self, oo_score: float) -> str:
        """Classify paradigm based on OO score."""
        if oo_score >= 0.7:
            return "STRONG_OO"
        elif oo_score >= 0.4:
            return "MIXED_OO"
        elif oo_score >= 0.2:
            return "WEAK_OO"
        else:
            return "PROCEDURAL"

    def _create_result(self, paradigm: str, oo_score: float) -> dict[str, Any]:
        """Create the final result dictionary."""
        return {
            "paradigm": paradigm,
            "oo_score": oo_score,
            "metrics": {
                "total_lines": self.metrics.total_lines,
                "total_classes": self.metrics.total_classes,
                "total_functions": self.metrics.total_functions,
                "class_methods": self.metrics.class_methods,
                "standalone_functions": self.metrics.standalone_functions,
                "inheritance_count": self.metrics.inheritance_count,
                "private_methods": self.metrics.private_methods,
                "properties": self.metrics.properties,
            },
            "recommended_metrics": self._get_recommended_metrics(paradigm),
            "explanation": self._get_explanation(paradigm, oo_score),
        }

    def _get_recommended_metrics(self, paradigm: str) -> list[str]:
        """Get recommended metrics based on detected paradigm."""
        base_metrics = [
            "cyclomatic_complexity",
            "cognitive_complexity",
            "halstead_volume",
            "maintainability_index",
            "code_duplication",
            "documentation_coverage",
        ]

        paradigm_metrics = {
            "STRONG_OO": [
                *base_metrics,
                "rfc",
                "dit",
                "mhf",
                "coupling",
                "cohesion",
                "design_patterns",
            ],
            "MIXED_OO": [*base_metrics, "rfc", "coupling", "cohesion"],
            "WEAK_OO": [*base_metrics, "coupling"],
        }
        return paradigm_metrics.get(paradigm, base_metrics)

    def _get_explanation(self, paradigm: str, oo_score: float) -> str:
        """Get human-readable explanation of the paradigm classification."""
        explanations = {
            "STRONG_OO": f"Strong object-oriented design (score: {oo_score:.2f}). "
            f"Code heavily uses classes, inheritance, and OO patterns. "
            f"All OO metrics are applicable.",
            "MIXED_OO": f"Mixed object-oriented design (score: {oo_score:.2f}). "
            f"Code uses classes but also significant procedural elements. "
            f"Selected OO metrics are applicable.",
            "WEAK_OO": f"Weak object-oriented design (score: {oo_score:.2f}). "
            f"Code has some classes but is primarily procedural. "
            f"Basic OO metrics only.",
            "PROCEDURAL": f"Procedural/functional design (score: {oo_score:.2f}). "
            f"Code is primarily function-based. "
            f"OO-specific metrics not applicable.",
            "UNKNOWN": "Could not determine paradigm due to insufficient code.",
        }

        return explanations.get(paradigm, "Unknown paradigm classification.")


class ParadigmVisitor(ast.NodeVisitor):
    """AST visitor to collect paradigm-related metrics."""

    def __init__(self) -> None:
        self.classes = 0
        self.functions = 0
        self.class_methods = 0
        self.standalone_functions = 0
        self.inheritance_count = 0
        self.multiple_inheritance = 0
        self.private_methods = 0
        self.properties = 0
        self.composition_count = 0
        self.oo_imports = 0
        self.procedural_imports = 0

        self._in_class = False
        self._current_class: ast.ClassDef | None = None

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        """Visit class definition."""
        self.classes += 1

        # Check inheritance
        if node.bases:
            self.inheritance_count += 1
            if len(node.bases) > 1:
                self.multiple_inheritance += 1

        # Analyze class body
        old_in_class = self._in_class
        old_current_class = self._current_class
        self._in_class = True
        self._current_class = node

        # Check for composition (class attributes that are other classes)
        for item in node.body:
            if isinstance(item, ast.Assign):
                # Simple heuristic: attribute assignment that might be composition
                self.composition_count += 1

        self.generic_visit(node)

        self._in_class = old_in_class
        self._current_class = old_current_class

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Visit function definition."""
        self.functions += 1

        if self._in_class:
            self.class_methods += 1

            # Check for private methods (Python convention)
            if node.name.startswith("_") and not node.name.startswith("__"):
                self.private_methods += 1

            # Check for properties
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == "property":
                    self.properties += 1
        else:
            self.standalone_functions += 1

        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        """Visit import statement."""
        for alias in node.names:
            if alias.name in ParadigmDetector.OO_IMPORTS:
                self.oo_imports += 1
            elif alias.name in ParadigmDetector.PROCEDURAL_IMPORTS:
                self.procedural_imports += 1

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Visit from-import statement."""
        if node.module:
            if node.module in ParadigmDetector.OO_IMPORTS:
                self.oo_imports += 1
            elif node.module in ParadigmDetector.PROCEDURAL_IMPORTS:
                self.procedural_imports += 1
