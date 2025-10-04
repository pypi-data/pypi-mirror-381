"""
Documentation Coverage metric implementation.
"""

import ast
from pathlib import Path
from typing import Any, Union, cast

from mfcqi.core.file_utils import get_python_files
from mfcqi.core.metric import Metric


class DocumentationCoverage(Metric):
    """Measures Documentation Coverage using AST analysis."""

    def extract(self, codebase: Path) -> float:
        """Extract documentation coverage percentage from Python files."""
        py_files = get_python_files(codebase)

        if not py_files:
            return 0.0  # No files = 0% coverage

        total_documentable = 0
        total_documented = 0

        for py_file in py_files:
            try:
                content = py_file.read_text()
                tree = ast.parse(content)
                file_stats = self._analyze_file_documentation(tree)
                total_documentable += file_stats["documentable"]
                total_documented += file_stats["documented"]
            except (SyntaxError, UnicodeDecodeError):
                continue

        if total_documentable == 0:
            return 0.0

        return (total_documented / total_documentable) * 100.0

    def _analyze_file_documentation(self, tree: ast.Module) -> dict[str, int]:
        """Analyze documentation in a single file."""
        documentable = 0
        documented = 0

        # Check module-level docstring
        documentable += 1  # Every module should have a docstring
        if self._has_docstring(tree):
            documented += 1

        # Count functions and classes
        for node in ast.walk(tree):
            if self._is_public_definition(node):
                documentable += 1
                if self._has_docstring(node):
                    documented += 1

        return {"documentable": documentable, "documented": documented}

    def _is_public_definition(self, node: ast.AST) -> bool:
        """Check if node is a public function or class definition."""
        return (
            isinstance(node, (ast.FunctionDef, ast.ClassDef))
            and hasattr(node, "name")
            and not node.name.startswith("_")
        )

    def _has_docstring(self, node: ast.AST) -> bool:
        """Check if node has a docstring."""
        if not hasattr(node, "body") or not node.body:
            return False

        first_statement = node.body[0]
        return (
            isinstance(first_statement, ast.Expr)
            and isinstance(first_statement.value, ast.Constant)
            and isinstance(first_statement.value.value, str)
        )

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """Normalize documentation coverage to [0,1] range where higher is better.
        Based on documentation standards:
        - 100% documentation: Perfect (1.0)
        - 80% documentation: Good (0.8)
        - 60% documentation: Moderate (0.6)
        - 40% documentation: Poor (0.4)
        - 0% documentation: Worst (0.0)
        """
        value = cast("float", value)  # This metric only returns float from extract()
        if value <= 0:
            return 0.0
        elif value >= 100:
            return 1.0
        else:
            # Linear normalization since documentation coverage is well-scaled
            return value / 100.0

    def get_weight(self) -> float:
        """Return evidence-based weight for documentation coverage.

        Based on empirical research and practical experience:
        - Documentation critical for maintainability and knowledge transfer
        - Reduces onboarding time and improves team productivity
        - While not directly correlated with defects, essential for long-term quality
        - Weight of 0.4 balances its importance with direct quality metrics
        """
        return 0.4

    def get_name(self) -> str:
        """Return the name of this metric."""
        return "Documentation Coverage"
