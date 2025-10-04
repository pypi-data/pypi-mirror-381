"""Type Safety Metric - measures type annotation coverage and MyPy compliance."""

import ast
from pathlib import Path
from typing import Any, Union, cast

from mfcqi.core.file_utils import get_python_files
from mfcqi.core.metric import Metric


class TypeSafetyMetric(Metric):
    """Measures type annotation coverage in Python code."""

    def extract(self, codebase: Path) -> float:
        """Extract type safety score from codebase.

        Args:
            codebase: Path to analyze

        Returns:
            Type coverage score between 0.0 and 1.0
        """
        total_functions = 0
        typed_functions = 0

        for py_file in get_python_files(codebase):
            try:
                content = py_file.read_text(encoding="utf-8")
                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        total_functions += 1

                        # Check if function has return type annotation
                        has_return_type = node.returns is not None

                        # Check if all parameters have type annotations
                        all_params_typed = True
                        for arg in node.args.args:
                            if arg.annotation is None and arg.arg != "self" and arg.arg != "cls":
                                all_params_typed = False
                                break

                        # Function is considered typed if it has return type and all params typed
                        if has_return_type and all_params_typed:
                            typed_functions += 1

            except (SyntaxError, UnicodeDecodeError):
                # Skip files with syntax errors or encoding issues
                continue

        if total_functions == 0:
            return 0.0

        return typed_functions / total_functions

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """Normalize type coverage to quality score.
        Args:
            value: Raw type coverage (0.0 to 1.0)

        Returns:
            Normalized score between 0.0 and 1.0
        """
        value = cast("float", value)  # This metric only returns float from extract()
        return value

    def get_weight(self) -> float:
        """Return weight for type safety metric.

        Returns:
            Weight value for geometric mean calculation
        """
        return 0.12  # Similar to documentation coverage

    def get_name(self) -> str:
        """Return metric name.

        Returns:
            Name of this metric
        """
        return "type_safety"
