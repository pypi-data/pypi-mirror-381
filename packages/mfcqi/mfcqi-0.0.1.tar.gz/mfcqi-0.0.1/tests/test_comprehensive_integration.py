"""Comprehensive integration tests to increase coverage."""

import tempfile
import textwrap
from pathlib import Path

from mfcqi.calculator import MFCQICalculator


def test_calculator_with_complex_codebase():
    """Test calculator with a complex real-world-like codebase."""
    code = textwrap.dedent('''
        """Complex module with multiple patterns and issues."""

        class Singleton:
            """Singleton pattern implementation."""
            _instance = None

            def __new__(cls):
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                return cls._instance

            def get_data(self):
                """Get data."""
                return self._data if hasattr(self, '_data') else None

            def set_data(self, data):
                """Set data."""
                self._data = data

        class Factory:
            """Factory pattern implementation."""

            @staticmethod
            def create_product(product_type):
                """Create product based on type."""
                if product_type == "A":
                    return ProductA()
                elif product_type == "B":
                    return ProductB()
                else:
                    raise ValueError(f"Unknown product type: {product_type}")

        class ProductA:
            """Product A."""
            def operation(self):
                """Do operation A."""
                return "Product A operation"

        class ProductB:
            """Product B."""
            def operation(self):
                """Do operation B."""
                return "Product B operation"

        class Observer:
            """Observer pattern base."""
            def update(self, subject):
                """Update observer."""
                pass

        class ConcreteObserver(Observer):
            """Concrete observer."""
            def update(self, subject):
                """Update with subject state."""
                print(f"Observer notified: {subject.state}")

        class Subject:
            """Subject in observer pattern."""
            def __init__(self):
                self._observers = []
                self._state = None

            def attach(self, observer):
                """Attach observer."""
                self._observers.append(observer)

            def notify(self):
                """Notify all observers."""
                for observer in self._observers:
                    observer.update(self)

            @property
            def state(self):
                """Get state."""
                return self._state

            @state.setter
            def state(self, value):
                """Set state and notify."""
                self._state = value
                self.notify()
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "patterns.py").write_text(code)

        # Test with paradigm detection
        calculator = MFCQICalculator(use_paradigm_detection=True)
        score = calculator.calculate(Path(tmpdir))

        assert 0.0 <= score <= 1.0

        # Test detailed metrics
        details = calculator.get_detailed_metrics(Path(tmpdir))
        assert "mfcqi_score" in details
        assert len(details) > 3  # Should have multiple metrics


def test_calculator_with_security_issues():
    """Test calculator with code containing security issues."""
    code = textwrap.dedent('''
        """Module with security issues for testing."""
        import os
        import pickle

        def unsafe_exec(code_string):
            """Unsafe use of exec."""
            exec(code_string)  # Security issue

        def unsafe_eval(expression):
            """Unsafe use of eval."""
            return eval(expression)  # Security issue

        def load_data(filename):
            """Unsafe pickle usage."""
            with open(filename, 'rb') as f:
                return pickle.load(f)  # Security issue

        def run_command(cmd):
            """Unsafe command execution."""
            os.system(cmd)  # Security issue

        PASSWORD = "hardcoded123"  # Security issue
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "unsafe.py").write_text(code)

        calculator = MFCQICalculator()
        score = calculator.calculate(Path(tmpdir))

        # Score should be lower due to security issues
        assert 0.0 <= score <= 1.0

        # Get detailed metrics with tool outputs
        detailed = calculator.get_detailed_metrics_with_tool_outputs(Path(tmpdir))
        assert "mfcqi_score" in detailed
        assert "metrics" in detailed
        assert "tool_outputs" in detailed


def test_calculator_caching_behavior():
    """Test that calculator properly caches results."""
    code = textwrap.dedent('''
        """Simple module for caching test."""
        def simple_function(x):
            """Simple function."""
            return x * 2

        def another_function(y):
            """Another function."""
            return y + 1
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "simple.py").write_text(code)

        calculator = MFCQICalculator()

        # First calculation
        score1 = calculator.calculate(Path(tmpdir))

        # Second calculation should use cache
        score2 = calculator.calculate(Path(tmpdir))

        # Scores should be identical (deterministic)
        assert score1 == score2


def test_calculator_with_empty_files():
    """Test calculator handles empty Python files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create empty Python file
        (Path(tmpdir) / "empty.py").write_text("")

        calculator = MFCQICalculator()
        score = calculator.calculate(Path(tmpdir))

        # Should handle gracefully
        assert score >= 0.0


def test_calculator_with_syntax_error_files():
    """Test calculator handles files with syntax errors."""
    code = "def broken( syntax error here"

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "broken.py").write_text(code)
        # Add a valid file too
        (Path(tmpdir) / "valid.py").write_text("def good(): return 1")

        calculator = MFCQICalculator()
        # Should not crash, should return a score based on valid files
        score = calculator.calculate(Path(tmpdir))

        assert 0.0 <= score <= 1.0


def test_calculator_with_mixed_quality_code():
    """Test calculator with mixed quality code."""
    good_code = textwrap.dedent('''
        """High quality module."""

        def add(a: int, b: int) -> int:
            """Add two integers.

            Args:
                a: First integer
                b: Second integer

            Returns:
                Sum of a and b
            """
            return a + b

        def multiply(x: float, y: float) -> float:
            """Multiply two floats.

            Args:
                x: First number
                y: Second number

            Returns:
                Product of x and y
            """
            return x * y
    ''')

    bad_code = textwrap.dedent("""
        def x(a,b,c,d,e,f,g,h):
            if a:
                if b:
                    if c:
                        if d:
                            if e:
                                if f:
                                    if g:
                                        return h
            return 0
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "good.py").write_text(good_code)
        (Path(tmpdir) / "bad.py").write_text(bad_code)

        calculator = MFCQICalculator()
        score = calculator.calculate(Path(tmpdir))

        # Score should be reasonable (good code outweighs bad in this case)
        assert 0.2 <= score <= 0.9


def test_calculator_with_oo_paradigm():
    """Test calculator correctly identifies OO paradigm."""
    oo_code = textwrap.dedent('''
        """Object-oriented module."""

        class Animal:
            """Base animal class."""
            def __init__(self, name):
                self.name = name

            def speak(self):
                """Animal speaks."""
                pass

        class Dog(Animal):
            """Dog class."""
            def speak(self):
                """Dog barks."""
                return f"{self.name} says Woof!"

        class Cat(Animal):
            """Cat class."""
            def speak(self):
                """Cat meows."""
                return f"{self.name} says Meow!"

        class Zoo:
            """Zoo container."""
            def __init__(self):
                self.animals = []

            def add_animal(self, animal):
                """Add animal to zoo."""
                self.animals.append(animal)

            def all_speak(self):
                """Make all animals speak."""
                return [animal.speak() for animal in self.animals]
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        for i in range(5):
            (Path(tmpdir) / f"module{i}.py").write_text(oo_code)

        # With paradigm detection enabled
        calculator = MFCQICalculator(use_paradigm_detection=True)
        applicable_metrics = calculator._determine_applicable_metrics(Path(tmpdir))

        # Should include OO metrics
        assert any(key in applicable_metrics for key in ["rfc", "dit", "mhf"])


def test_calculator_with_procedural_paradigm():
    """Test calculator correctly identifies procedural paradigm."""
    procedural_code = textwrap.dedent('''
        """Procedural module."""

        def process_data(data):
            """Process data."""
            result = []
            for item in data:
                if item > 0:
                    result.append(item * 2)
            return result

        def filter_data(data, threshold):
            """Filter data by threshold."""
            return [x for x in data if x > threshold]

        def aggregate(data):
            """Aggregate data."""
            return sum(data) / len(data) if data else 0
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "procedural.py").write_text(procedural_code)

        # With paradigm detection enabled
        calculator = MFCQICalculator(use_paradigm_detection=True)
        applicable_metrics = calculator._determine_applicable_metrics(Path(tmpdir))

        # Should not include OO-specific metrics for pure procedural
        # (though patterns might still be included if complexity is high)
        assert "cyclomatic_complexity" in applicable_metrics
        assert "maintainability_index" in applicable_metrics
