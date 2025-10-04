"""Integration tests for TypeSafetyMetric in MFCQI calculator."""

import tempfile
from pathlib import Path

from mfcqi.calculator import MFCQICalculator


class TestTypeSafetyIntegration:
    """Test TypeSafetyMetric integration with calculator."""

    def test_calculator_without_type_safety(self):
        """Test that calculator works without type safety metric by default."""
        code = """
def add(a: int, b: int) -> int:
    return a + b
"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "test.py"
            test_file.write_text(code)

            calculator = MFCQICalculator()
            score = calculator.calculate(tmp_path)

            # Score should be calculated without type safety
            assert 0.0 <= score <= 1.0

    def test_calculator_with_type_safety(self):
        """Test that calculator includes type safety when enabled."""
        fully_typed = '''
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y
'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "typed.py"
            test_file.write_text(fully_typed)

            calculator = MFCQICalculator(include_type_safety=True)
            detailed = calculator.get_detailed_metrics(tmp_path)

            # Type safety should be included in metrics
            assert "type_safety" in detailed
            assert detailed["type_safety"] > 0.9  # Fully typed code

    def test_type_safety_affects_overall_score(self):
        """Test that type safety impacts the overall MFCQI score."""
        untyped = '''
def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(x, y):
    """Multiply two numbers."""
    return x * y
'''
        typed = '''
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y
'''

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)

            # Test untyped code
            test_file = tmp_path / "code.py"
            test_file.write_text(untyped)

            calculator_with_types = MFCQICalculator(include_type_safety=True)
            untyped_score = calculator_with_types.calculate(tmp_path)

            # Test typed code
            test_file.write_text(typed)
            typed_score = calculator_with_types.calculate(tmp_path)

            # Typed code should have higher score
            assert typed_score > untyped_score

    def test_type_safety_in_detailed_metrics(self):
        """Test that type safety appears correctly in detailed metrics."""
        mixed_code = '''
def typed_func(x: int) -> int:
    """Fully typed function."""
    return x * 2

def untyped_func(x):
    """Untyped function."""
    return x * 2

class MyClass:
    def typed_method(self, a: str) -> str:
        """Typed method."""
        return a.upper()

    def untyped_method(self, a):
        """Untyped method."""
        return a.lower()
'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "mixed.py"
            test_file.write_text(mixed_code)

            calculator = MFCQICalculator(include_type_safety=True)
            detailed = calculator.get_detailed_metrics(tmp_path)

            # Check type safety is included and has reasonable value
            assert "type_safety" in detailed
            assert 0.4 < detailed["type_safety"] < 0.6  # 50% typed

    def test_type_safety_disabled_by_default(self):
        """Test that type safety is not included by default."""
        code = """
def func(x: int) -> int:
    return x * 2
"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "test.py"
            test_file.write_text(code)

            # Default calculator without explicit type_safety flag
            calculator = MFCQICalculator()
            calculator.get_detailed_metrics(tmp_path)

            # Type safety should NOT be in the core metrics used for MFCQI
            # (might be in optional metrics for display but not in calculation)
            metrics_used = calculator.metrics
            assert "type_safety" not in metrics_used
