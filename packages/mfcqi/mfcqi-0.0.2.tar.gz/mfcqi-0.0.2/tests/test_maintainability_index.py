"""
Test for Maintainability Index metric - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import tempfile
import textwrap
from pathlib import Path


def test_maintainability_index_exists():
    """RED: Test that MaintainabilityIndex class exists."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    assert MaintainabilityIndex is not None


def test_maintainability_index_is_metric():
    """RED: Test that MaintainabilityIndex implements Metric interface."""
    from mfcqi.core.metric import Metric
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    assert issubclass(MaintainabilityIndex, Metric)


def test_maintainability_simple_code():
    """RED: Test MI for simple, maintainable code."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    code = textwrap.dedent("""
        def greet(name):
            \"\"\"Greet a person by name.\"\"\"
            return f"Hello, {name}!"
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = MaintainabilityIndex()
        result = metric.extract(Path(tmpdir))

        # Simple, documented function should have high MI (>70)
        assert result > 70.0


def test_maintainability_complex_code():
    """RED: Test MI for complex, unmaintainable code."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    code = textwrap.dedent("""
        def x(a, b, c, d, e):
            if a > 0:
                if b > 0:
                    if c > 0:
                        for i in range(d):
                            for j in range(e):
                                if i % 2 == 0:
                                    if j % 3 == 0:
                                        yield i * j
                                    else:
                                        yield i + j
                                else:
                                    if j % 5 == 0:
                                        yield i - j
                                    else:
                                        yield i / j if j != 0 else 0
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = MaintainabilityIndex()
        result = metric.extract(Path(tmpdir))

        # Complex, undocumented code should have lower MI (<60)
        assert result < 60.0


def test_maintainability_multiple_files():
    """RED: Test MI calculation across multiple files."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    file1 = textwrap.dedent("""
        def add(a, b):
            \"\"\"Add two numbers.\"\"\"
            return a + b
    """)

    file2 = textwrap.dedent("""
        def complex_calc(x, y, z):
            if x > 0 and y > 0:
                result = x * y / z if z != 0 else 0
                for i in range(int(result)):
                    if i % 2 == 0:
                        result += i
            else:
                result = abs(x - y)
            return result
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "file1.py").write_text(file1)
        (Path(tmpdir) / "file2.py").write_text(file2)

        metric = MaintainabilityIndex()
        result = metric.extract(Path(tmpdir))

        # Should return average MI
        assert 40.0 < result < 80.0


def test_maintainability_normalize():
    """Test normalization of MI values with library-adjusted thresholds (70/50/30/20)."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    metric = MaintainabilityIndex()

    # MI of 100 (best) should normalize to 1.0
    assert metric.normalize(100.0) == 1.0

    # MI of 70+ (excellent) should normalize to high value (0.85-1.0)
    assert metric.normalize(85.0) > 0.9

    # MI of 50 (good - library-appropriate) should normalize to ~0.70
    # With new thresholds: MI=50 is at start of "Good" range (50-70 → 0.70-0.85)
    assert 0.68 <= metric.normalize(50.0) <= 0.72

    # MI of 30 (moderate) should normalize to ~0.50
    assert 0.48 <= metric.normalize(30.0) <= 0.52

    # MI of 20 (poor threshold) should normalize to ~0.25
    assert 0.23 <= metric.normalize(20.0) <= 0.27

    # MI of 0 or negative should normalize to 0
    assert metric.normalize(0.0) == 0.0
    assert metric.normalize(-10.0) == 0.0

    # All normalized values should be in [0,1]
    for mi in [0, 20, 30, 40, 50, 60, 70, 80, 100, 120]:
        normalized = metric.normalize(float(mi))
        assert 0.0 <= normalized <= 1.0


def test_maintainability_name():
    """RED: Test that metric returns its name."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    metric = MaintainabilityIndex()
    name = metric.get_name()

    assert name == "Maintainability Index"
    assert isinstance(name, str)


def test_maintainability_empty_directory():
    """RED: Test MI with no Python files."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    with tempfile.TemporaryDirectory() as tmpdir:
        metric = MaintainabilityIndex()
        result = metric.extract(Path(tmpdir))

        # Should return a default value for empty projects
        # Using 100.0 as default (perfect maintainability for no code)
        assert result == 100.0


def test_maintainability_get_weight():
    """Test get_weight method."""
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    metric = MaintainabilityIndex()
    weight = metric.get_weight()

    # Should return 0.5 (reduced per research evidence)
    assert weight == 0.5
