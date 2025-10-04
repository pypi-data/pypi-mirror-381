"""
AST-based test smell detector for Python tests.

Detects common test smells without requiring external tools:
- Assertion Roulette: Multiple assertions without messages
- Empty Test: No assertions in test
- Long Test: Test with too many lines
- Sleepy Test: Tests with sleep() calls
- Redundant Print: Print statements in tests

Based on test smell research:
- PyNose (JetBrains Research): Test smell taxonomy
- Pytest-smell paper (ISSTA 2022): Common test smells

"""

import ast
from pathlib import Path

from mfcqi.core.file_utils import get_python_files
from mfcqi.smell_detection.detector_base import SmellDetector
from mfcqi.smell_detection.models import Smell, SmellCategory, SmellSeverity


class ASTTestSmellDetector(SmellDetector):
    """Detects test smells using AST analysis.

    This is a built-in detector that doesn't require external tools.
    Analyzes Python test files to find common anti-patterns.

    Detected Smells:
    ================
    1. ASSERTION_ROULETTE: 4+ assertions without descriptive messages
    2. EMPTY_TEST: Test function with no assertions
    3. LONG_TEST: Test function with 50+ lines
    4. SLEEPY_TEST: Test with time.sleep() calls
    5. REDUNDANT_PRINT: Print statements in test code

    Only analyzes files matching test patterns:
    - test_*.py
    - *_test.py
    """

    @property
    def name(self) -> str:
        """Return detector name."""
        return "ast-test-smells"

    def detect(self, codebase: Path) -> list[Smell]:
        """Detect test smells in Python test files.

        Args:
            codebase: Path to codebase root

        Returns:
            List of detected Smell objects
        """
        smells: list[Smell] = []

        # Get all Python files
        py_files = get_python_files(codebase)

        for py_file in py_files:
            # Only analyze test files
            if not self._is_test_file(py_file):
                continue

            try:
                content = py_file.read_text(encoding="utf-8")
                tree = ast.parse(content, filename=str(py_file))

                # Analyze each test function
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and self._is_test_function(node):
                        file_smells = self._analyze_test_function(node, py_file, codebase)
                        smells.extend(file_smells)

            except (SyntaxError, UnicodeDecodeError):
                continue

        return smells

    def _is_test_file(self, file_path: Path) -> bool:
        """Check if file is a test file."""
        name = file_path.name
        return name.startswith("test_") or name.endswith("_test.py")

    def _is_test_function(self, node: ast.FunctionDef) -> bool:
        """Check if function is a test function."""
        return node.name.startswith("test_")

    def _analyze_test_function(
        self, node: ast.FunctionDef, file_path: Path, codebase: Path
    ) -> list[Smell]:
        """Analyze a single test function for smells."""
        smells: list[Smell] = []

        # Get relative path for location
        try:
            relative_path = file_path.relative_to(codebase)
        except ValueError:
            relative_path = file_path

        location = f"{relative_path}:{node.lineno}"

        # Check for Assertion Roulette (4+ assertions without messages)
        assert_count = self._count_assertions(node)
        assert_with_msg_count = self._count_assertions_with_messages(node)

        if assert_count >= 4 and assert_with_msg_count < assert_count // 2:
            smells.append(
                Smell(
                    id="ASSERTION_ROULETTE",
                    name="Assertion Roulette",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.MEDIUM,
                    location=location,
                    tool=self.name,
                    description=f"Test '{node.name}' has {assert_count} assertions, "
                    f"most without descriptive messages. Makes failures hard to diagnose.",
                )
            )

        # Check for Empty Test (no assertions)
        if assert_count == 0:
            smells.append(
                Smell(
                    id="EMPTY_TEST",
                    name="Empty Test",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.HIGH,
                    location=location,
                    tool=self.name,
                    description=f"Test '{node.name}' has no assertions. Tests should verify behavior.",
                )
            )

        # Check for Long Test (50+ lines)
        test_lines = self._count_function_lines(node)
        if test_lines >= 50:
            smells.append(
                Smell(
                    id="LONG_TEST",
                    name="Long Test",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.MEDIUM,
                    location=location,
                    tool=self.name,
                    description=f"Test '{node.name}' is {test_lines} lines long. "
                    f"Consider breaking into smaller, focused tests.",
                )
            )

        # Check for Sleepy Test (sleep calls)
        if self._has_sleep_call(node):
            smells.append(
                Smell(
                    id="SLEEPY_TEST",
                    name="Sleepy Test",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.HIGH,
                    location=location,
                    tool=self.name,
                    description=f"Test '{node.name}' uses time.sleep(). "
                    f"Use proper synchronization or mocking instead.",
                )
            )

        # Check for Redundant Print
        if self._has_print_call(node):
            smells.append(
                Smell(
                    id="REDUNDANT_PRINT",
                    name="Redundant Print",
                    category=SmellCategory.TEST,
                    severity=SmellSeverity.LOW,
                    location=location,
                    tool=self.name,
                    description=f"Test '{node.name}' contains print statements. "
                    f"Use logging or pytest output capturing instead.",
                )
            )

        return smells

    def _count_assertions(self, node: ast.FunctionDef) -> int:
        """Count number of assert statements in function."""
        count = 0
        for child in ast.walk(node):
            if isinstance(child, ast.Assert):
                count += 1
        return count

    def _count_assertions_with_messages(self, node: ast.FunctionDef) -> int:
        """Count assertions with descriptive messages."""
        count = 0
        for child in ast.walk(node):
            if isinstance(child, ast.Assert) and child.msg is not None:
                count += 1
        return count

    def _count_function_lines(self, node: ast.FunctionDef) -> int:
        """Count lines in function (end line - start line)."""
        if hasattr(node, "end_lineno") and node.end_lineno:
            return node.end_lineno - node.lineno + 1
        return 0

    def _has_sleep_call(self, node: ast.FunctionDef) -> bool:
        """Check if function contains time.sleep() calls."""
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                # Check for time.sleep()
                if isinstance(child.func, ast.Attribute):
                    if child.func.attr == "sleep":
                        return True
                # Check for sleep() if time imported as 'from time import sleep'
                elif isinstance(child.func, ast.Name) and child.func.id == "sleep":
                    return True
        return False

    def _has_print_call(self, node: ast.FunctionDef) -> bool:
        """Check if function contains print() calls."""
        for child in ast.walk(node):
            if (
                isinstance(child, ast.Call)
                and isinstance(child.func, ast.Name)
                and child.func.id == "print"
            ):
                return True
        return False
