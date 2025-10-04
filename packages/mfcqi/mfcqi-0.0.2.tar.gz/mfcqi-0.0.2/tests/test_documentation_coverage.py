"""
Test for Documentation Coverage metric - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import tempfile
import textwrap
from pathlib import Path


def test_documentation_coverage_exists():
    """RED: Test that DocumentationCoverage class exists."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    assert DocumentationCoverage is not None


def test_documentation_coverage_is_metric():
    """RED: Test that DocumentationCoverage implements Metric interface."""
    from mfcqi.core.metric import Metric
    from mfcqi.metrics.documentation import DocumentationCoverage

    assert issubclass(DocumentationCoverage, Metric)


def test_no_documentation():
    """RED: Test coverage when no docstrings are present."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    code = textwrap.dedent("""
        def add(a, b):
            return a + b

        def multiply(a, b):
            return a * b

        class Calculator:
            def divide(self, a, b):
                return a / b
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "undocumented.py"
        test_file.write_text(code)

        metric = DocumentationCoverage()
        result = metric.extract(Path(tmpdir))

        # No documentation = 0% coverage
        assert result == 0.0


def test_full_documentation():
    """RED: Test coverage when all functions/classes have docstrings."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    code = textwrap.dedent('''
        """Module for mathematical operations."""

        def add(a, b):
            """Add two numbers together.

            Args:
                a: First number
                b: Second number

            Returns:
                Sum of a and b
            """
            return a + b

        def multiply(a, b):
            """Multiply two numbers.

            Args:
                a: First number
                b: Second number

            Returns:
                Product of a and b
            """
            return a * b

        class Calculator:
            """A simple calculator class."""

            def divide(self, a, b):
                """Divide two numbers.

                Args:
                    a: Numerator
                    b: Denominator

                Returns:
                    Quotient of a and b
                """
                return a / b
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "documented.py"
        test_file.write_text(code)

        metric = DocumentationCoverage()
        result = metric.extract(Path(tmpdir))

        # Full documentation should give high coverage
        assert result > 90.0


def test_partial_documentation():
    """RED: Test coverage with partial documentation."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    code = textwrap.dedent('''
        """Module for data processing."""

        def process_data(data):
            """Process input data and return results."""
            return [x * 2 for x in data]

        def format_data(data):
            # No docstring here
            return ", ".join(map(str, data))

        class DataProcessor:
            """Handles data processing operations."""

            def transform(self, data):
                # No docstring here
                return [x + 1 for x in data]

            def validate(self, data):
                """Validate input data."""
                return all(isinstance(x, (int, float)) for x in data)
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "partial.py"
        test_file.write_text(code)

        metric = DocumentationCoverage()
        result = metric.extract(Path(tmpdir))

        # Partial documentation should give moderate coverage
        assert 40.0 < result < 80.0


def test_private_functions_ignored():
    """RED: Test that private functions are not counted in documentation coverage."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    code = textwrap.dedent('''
        def public_function():
            """This is documented."""
            return "public"

        def _private_function():
            # Private functions don't need docs
            return "private"

        def __dunder_function__():
            # Dunder functions don't need docs
            return "dunder"

        class MyClass:
            """Documented class."""

            def public_method(self):
                """Documented public method."""
                return "public"

            def _private_method(self):
                # Private method, no doc needed
                return "private"
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "mixed.py"
        test_file.write_text(code)

        metric = DocumentationCoverage()
        result = metric.extract(Path(tmpdir))

        # Should only count public functions/methods and class + module
        # 3 documented out of 4 items (missing module docstring) = 75%
        assert 70.0 <= result <= 80.0


def test_multiple_files():
    """RED: Test documentation coverage across multiple files."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    file1 = textwrap.dedent('''
        """Well documented module."""

        def documented_func():
            """This function is documented."""
            return True
    ''')

    file2 = textwrap.dedent("""
        def undocumented_func():
            return False

        class UndocumentedClass:
            def method(self):
                return None
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "documented.py").write_text(file1)
        (Path(tmpdir) / "undocumented.py").write_text(file2)

        metric = DocumentationCoverage()
        result = metric.extract(Path(tmpdir))

        # Should return average across all files
        # 1 documented out of 4 total items = 25%
        assert 20.0 < result < 35.0


def test_documentation_normalize():
    """RED: Test normalization of documentation values to [0,1] range."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    metric = DocumentationCoverage()

    # 100% documentation (best) should normalize to 1.0
    assert metric.normalize(100.0) == 1.0

    # 80% documentation (good) should normalize to high value (>=0.8)
    assert metric.normalize(80.0) >= 0.8

    # 50% documentation (moderate) should normalize to ~0.5
    assert 0.4 <= metric.normalize(50.0) <= 0.6

    # 20% documentation (poor) should normalize to low value (<0.3)
    assert metric.normalize(20.0) < 0.3

    # 0% documentation (worst) should normalize to 0.0
    assert metric.normalize(0.0) == 0.0

    # All normalized values should be in [0,1]
    for coverage in [0, 20, 40, 60, 80, 100]:
        normalized = metric.normalize(float(coverage))
        assert 0.0 <= normalized <= 1.0


def test_documentation_name():
    """RED: Test that metric returns its name."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    metric = DocumentationCoverage()
    name = metric.get_name()

    assert name == "Documentation Coverage"
    assert isinstance(name, str)


def test_documentation_empty_directory():
    """RED: Test documentation coverage with no Python files."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    with tempfile.TemporaryDirectory() as tmpdir:
        metric = DocumentationCoverage()
        result = metric.extract(Path(tmpdir))

        # Should return 0% coverage for empty projects
        assert result == 0.0


def test_documentation_get_weight():
    """Test get_weight method."""
    from mfcqi.metrics.documentation import DocumentationCoverage

    metric = DocumentationCoverage()
    weight = metric.get_weight()

    # Should return 0.4
    assert weight == 0.4
