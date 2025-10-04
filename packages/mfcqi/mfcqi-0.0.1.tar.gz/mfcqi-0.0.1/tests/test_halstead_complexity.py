"""
Test for Halstead Complexity metric - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import tempfile
import textwrap
from pathlib import Path


def test_halstead_complexity_exists():
    """RED: Test that HalsteadComplexity class exists."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    assert HalsteadComplexity is not None


def test_halstead_complexity_is_metric():
    """RED: Test that HalsteadComplexity implements Metric interface."""
    from mfcqi.core.metric import Metric
    from mfcqi.metrics.complexity import HalsteadComplexity

    assert issubclass(HalsteadComplexity, Metric)


def test_halstead_simple_function():
    """Test Halstead metrics for simple function."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    code = textwrap.dedent("""
        def add(a, b):
            return a + b
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = HalsteadComplexity()
        result = metric.extract(Path(tmpdir))

        # Simple function should have low Halstead Volume
        # For add(a, b): return a + b, Volume is ~4.75
        assert 0 < result < 10.0


def test_halstead_complex_function():
    """Test Halstead metrics for complex function."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    code = textwrap.dedent("""
        def complex_logic(x, y, z):
            result = 0
            if x > 0 and y > 0:
                for i in range(x):
                    if i % 2 == 0:
                        result += i * y
                    else:
                        result -= i / z if z != 0 else 0
            elif x < 0 or y < 0:
                result = abs(x) + abs(y)
            return result * 2 if result > 100 else result / 2
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = HalsteadComplexity()
        result = metric.extract(Path(tmpdir))

        # Complex function should have higher Volume
        assert result > 100.0


def test_halstead_multiple_files():
    """RED: Test Halstead calculation across multiple files."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    file1 = textwrap.dedent("""
        def simple():
            return 1
    """)

    file2 = textwrap.dedent("""
        def moderate(x):
            if x > 0:
                return x * 2
            return x / 2
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "file1.py").write_text(file1)
        (Path(tmpdir) / "file2.py").write_text(file2)

        metric = HalsteadComplexity()
        result = metric.extract(Path(tmpdir))

        # Should return average Volume
        assert 0 < result < 20.0


def test_halstead_normalize():
    """Test normalization of Halstead values to [0,1] range with tanh-based function."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    metric = HalsteadComplexity()

    # Low Volume (0-100) should normalize to high quality (>0.9)
    # HV=50: 1.0 - tanh(50/2500) = 1.0 - tanh(0.02) ≈ 0.98
    assert metric.normalize(50.0) > 0.95

    # Medium Volume (300-500) should normalize to good quality with tanh
    # HV=400: 1.0 - tanh(400/2500) = 1.0 - tanh(0.16) ≈ 0.84
    assert 0.80 <= metric.normalize(400.0) <= 0.90

    # High Volume (900+) should normalize to lower quality
    # HV=950: 1.0 - tanh(950/2500) = 1.0 - tanh(0.38) ≈ 0.64
    assert metric.normalize(950.0) < 0.7

    # Very high volume (2000+) should be moderate
    # HV=2000: 1.0 - tanh(2000/2500) = 1.0 - tanh(0.8) ≈ 0.33
    assert 0.30 <= metric.normalize(2000.0) <= 0.40

    # All normalized values should be in [0,1]
    for volume in [10, 100, 300, 500, 700, 900, 1100, 2000, 5000]:
        normalized = metric.normalize(float(volume))
        assert 0.0 <= normalized <= 1.0


def test_halstead_name():
    """RED: Test that metric returns its name."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    metric = HalsteadComplexity()
    name = metric.get_name()

    assert name == "Halstead Volume"
    assert isinstance(name, str)


def test_halstead_empty_directory():
    """RED: Test Halstead with no Python files."""
    from mfcqi.metrics.complexity import HalsteadComplexity

    with tempfile.TemporaryDirectory() as tmpdir:
        metric = HalsteadComplexity()
        result = metric.extract(Path(tmpdir))

        # Should return a default value for empty projects
        assert result == 0.0  # Minimal volume as default
