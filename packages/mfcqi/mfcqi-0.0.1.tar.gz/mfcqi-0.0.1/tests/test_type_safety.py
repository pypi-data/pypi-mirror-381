"""Test TypeSafetyMetric - following strict TDD."""

import tempfile
from pathlib import Path

from mfcqi.metrics.type_safety import TypeSafetyMetric


class TestTypeSafetyMetric:
    """Test type safety metric extraction and normalization."""

    def test_type_safety_metric_exists(self):
        """Test that TypeSafetyMetric class exists."""
        metric = TypeSafetyMetric()
        assert metric is not None

    def test_extract_from_fully_typed_code(self):
        """Test extraction from code with complete type annotations."""
        code = '''
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def greet(name: str) -> str:
    """Greet someone."""
    return f"Hello, {name}"

class Calculator:
    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        return x * y
'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "typed.py"
            test_file.write_text(code)

            metric = TypeSafetyMetric()
            result = metric.extract(tmp_path)

            # Expecting high score for fully typed code
            assert result > 0.9

    def test_extract_from_untyped_code(self):
        """Test extraction from code without type annotations."""
        code = '''
def add(a, b):
    """Add two numbers."""
    return a + b

def greet(name):
    """Greet someone."""
    return f"Hello, {name}"

class Calculator:
    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y
'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "untyped.py"
            test_file.write_text(code)

            metric = TypeSafetyMetric()
            result = metric.extract(tmp_path)

            # Expecting low score for untyped code
            assert result < 0.1

    def test_extract_from_partially_typed_code(self):
        """Test extraction from code with partial type annotations."""
        code = '''
def add(a: int, b: int) -> int:
    """Fully typed function."""
    return a + b

def greet(name):
    """Untyped function."""
    return f"Hello, {name}"

def process(data: list) -> None:
    """Partially typed - missing generic type."""
    for item in data:
        print(item)
'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "partial.py"
            test_file.write_text(code)

            metric = TypeSafetyMetric()
            result = metric.extract(tmp_path)

            # Expecting medium score for partially typed code
            assert 0.3 < result < 0.7

    def test_normalization_perfect_score(self):
        """Test normalization of perfect type coverage."""
        metric = TypeSafetyMetric()
        assert metric.normalize(1.0) == 1.0

    def test_normalization_zero_score(self):
        """Test normalization of no type coverage."""
        metric = TypeSafetyMetric()
        assert metric.normalize(0.0) == 0.0

    def test_normalization_partial_score(self):
        """Test normalization of partial type coverage."""
        metric = TypeSafetyMetric()
        normalized = metric.normalize(0.5)
        assert 0.4 < normalized < 0.6

    def test_empty_directory(self):
        """Test behavior with empty directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            metric = TypeSafetyMetric()
            result = metric.extract(tmp_path)
            assert result == 0.0

    def test_syntax_error_handling(self):
        """Test handling of files with syntax errors."""
        code = """
def broken(a: int -> int:  # Syntax error
    return a
"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "broken.py"
            test_file.write_text(code)

            metric = TypeSafetyMetric()
            result = metric.extract(tmp_path)
            # Should handle gracefully, return 0
            assert result == 0.0

    def test_class_methods_typing(self):
        """Test that class methods are properly evaluated for typing."""
        code = """
from typing import Optional, List

class TypedClass:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    @classmethod
    def from_list(cls, items: List[str]) -> "TypedClass":
        return cls(items[0])

    @staticmethod
    def validate(value: Optional[str]) -> bool:
        return value is not None

class UntypedClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            test_file = tmp_path / "classes.py"
            test_file.write_text(code)

            metric = TypeSafetyMetric()
            result = metric.extract(tmp_path)

            # 4 out of 6 methods are typed (TypedClass has all 4 typed, UntypedClass has 0 of 2)
            assert 0.6 < result < 0.7

    def test_get_weight(self):
        """Test get_weight method."""
        metric = TypeSafetyMetric()
        weight = metric.get_weight()

        # Should return 0.12 based on documentation
        assert weight == 0.12

    def test_get_name(self):
        """Test get_name method."""
        metric = TypeSafetyMetric()
        name = metric.get_name()

        # Should return "type_safety"
        assert name == "type_safety"
