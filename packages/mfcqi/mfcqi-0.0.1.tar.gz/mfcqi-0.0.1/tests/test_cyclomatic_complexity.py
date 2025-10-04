"""
Test for Cyclomatic Complexity metric - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import tempfile
import textwrap
from pathlib import Path


def test_cyclomatic_complexity_is_metric():
    """RED: Test that CyclomaticComplexity implements Metric interface."""
    from mfcqi.core.metric import Metric
    from mfcqi.metrics.complexity import CyclomaticComplexity

    assert issubclass(CyclomaticComplexity, Metric)


def test_cyclomatic_complexity_simple_function():
    """RED: Test CC for simple function with no branches."""
    from mfcqi.metrics.complexity import CyclomaticComplexity

    code = textwrap.dedent("""
        def add(a, b):
            return a + b
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = CyclomaticComplexity()
        result = metric.extract(Path(tmpdir))

        # Simple function has CC of 1 (no branches)
        assert result == 1.0


def test_cyclomatic_complexity_with_if():
    """RED: Test CC for function with single if statement."""
    from mfcqi.metrics.complexity import CyclomaticComplexity

    code = textwrap.dedent("""
        def check(x):
            if x > 0:
                return "positive"
            return "non-positive"
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = CyclomaticComplexity()
        result = metric.extract(Path(tmpdir))

        # Function with one if has CC of 2
        assert result == 2.0


def test_cyclomatic_complexity_multiple_files():
    """RED: Test CC calculation across multiple files."""
    from mfcqi.metrics.complexity import CyclomaticComplexity

    file1 = textwrap.dedent("""
        def func1():
            return 1
    """)

    file2 = textwrap.dedent("""
        def func2(x):
            if x:
                return True
            return False
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "file1.py").write_text(file1)
        (Path(tmpdir) / "file2.py").write_text(file2)

        metric = CyclomaticComplexity()
        result = metric.extract(Path(tmpdir))

        # Average CC: (1 + 2) / 2 = 1.5
        assert result == 1.5


def test_cyclomatic_complexity_normalize():
    """RED: Test normalization of CC values to [0,1] range."""
    from mfcqi.metrics.complexity import CyclomaticComplexity

    metric = CyclomaticComplexity()

    # CC of 1 (best) should normalize to 1.0
    assert metric.normalize(1.0) == 1.0

    # CC of 10 (threshold) should normalize to ~0.5
    assert 0.4 <= metric.normalize(10.0) <= 0.6

    # CC of 20+ (poor) should normalize close to 0
    assert metric.normalize(25.0) < 0.2

    # All normalized values should be in [0,1]
    for cc in [1, 5, 10, 15, 20, 30, 50]:
        normalized = metric.normalize(float(cc))
        assert 0.0 <= normalized <= 1.0


def test_cyclomatic_complexity_name():
    """RED: Test that metric returns its name."""
    from mfcqi.metrics.complexity import CyclomaticComplexity

    metric = CyclomaticComplexity()
    name = metric.get_name()

    assert name == "Cyclomatic Complexity"
    assert isinstance(name, str)
