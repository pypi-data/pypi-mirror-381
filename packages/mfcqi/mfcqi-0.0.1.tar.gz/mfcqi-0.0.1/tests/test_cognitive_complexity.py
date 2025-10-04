"""Tests for Cognitive Complexity metric."""

import tempfile
import textwrap
from pathlib import Path

from mfcqi.metrics.cognitive import CognitiveComplexity


def test_cognitive_complexity_simple_function():
    """Test cognitive complexity on a simple function."""
    code = textwrap.dedent('''
        """Simple module."""
        def simple():
            """Simple function."""
            return 1
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "simple.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Simple function should have low complexity
        assert result["average"] == 0


def test_cognitive_complexity_with_nested_conditions():
    """Test cognitive complexity with nested conditions."""
    code = textwrap.dedent('''
        """Complex module."""
        def complex_function(a, b, c):
            """Function with nested conditions."""
            if a:
                if b:
                    if c:
                        return a + b + c
            return 0
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "complex.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Nested conditions increase cognitive complexity
        assert result["average"] > 0


def test_cognitive_complexity_nonexistent_path():
    """Test cognitive complexity with non-existent path."""
    metric = CognitiveComplexity()
    result = metric.extract(Path("/nonexistent/path"))

    # Non-existent path should return 0
    assert result["average"] == 0.0


def test_cognitive_complexity_empty_directory():
    """Test cognitive complexity with empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Empty directory should return 0
        assert result["average"] == 0.0


def test_cognitive_complexity_no_functions():
    """Test cognitive complexity with file containing no functions."""
    code = textwrap.dedent('''
        """Module with no functions."""
        CONSTANT = 42
        class EmptyClass:
            """Empty class."""
            pass
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "no_funcs.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # No functions should return 0
        assert result["average"] == 0.0


def test_cognitive_complexity_skips_test_files():
    """Test that cognitive complexity skips test files."""
    test_code = textwrap.dedent('''
        """Test module."""
        def test_something():
            """Complex test."""
            if True:
                if True:
                    if True:
                        return 1
    ''')

    prod_code = textwrap.dedent('''
        """Production code."""
        def simple():
            """Simple function."""
            return 1
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test directory
        test_dir = Path(tmpdir) / "test"
        test_dir.mkdir()
        (test_dir / "test_module.py").write_text(test_code)

        # Create production file
        (Path(tmpdir) / "prod.py").write_text(prod_code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Should only analyze prod file (complexity = 0)
        assert result["average"] == 0.0


def test_cognitive_complexity_handles_syntax_errors():
    """Test that cognitive complexity handles files with syntax errors."""
    bad_code = "def broken( syntax error"
    good_code = "def good(): return 1"

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "bad.py").write_text(bad_code)
        (Path(tmpdir) / "good.py").write_text(good_code)

        metric = CognitiveComplexity()
        # Should not raise exception, should skip bad file
        result = metric.extract(Path(tmpdir))

        # Should process good file
        assert result["average"] == 0.0


def test_cognitive_complexity_with_async_functions():
    """Test cognitive complexity with async functions."""
    code = textwrap.dedent('''
        """Async module."""
        async def async_function(x):
            """Async function with logic."""
            if x > 0:
                return x * 2
            return 0
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "async.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Should handle async functions
        assert result["average"] >= 0


def test_cognitive_complexity_normalize_excellent():
    """Test normalization for excellent complexity (<5)."""
    metric = CognitiveComplexity()

    # Test values < 5
    assert metric.normalize(0) == 1.0
    assert metric.normalize(2.5) > 0.9
    assert metric.normalize(5) > 0.8


def test_cognitive_complexity_normalize_good():
    """Test normalization for good complexity (5-10)."""
    metric = CognitiveComplexity()

    # Test values 5-10
    result_7 = metric.normalize(7)
    assert 0.7 <= result_7 <= 0.9

    result_10 = metric.normalize(10)
    assert 0.6 <= result_10 <= 0.8


def test_cognitive_complexity_normalize_fair():
    """Test normalization for fair complexity (10-15)."""
    metric = CognitiveComplexity()

    # Test values 10-15
    result_12 = metric.normalize(12)
    assert 0.4 <= result_12 <= 0.7

    result_15 = metric.normalize(15)
    assert 0.3 <= result_15 <= 0.5


def test_cognitive_complexity_normalize_poor():
    """Test normalization for poor complexity (15-25)."""
    metric = CognitiveComplexity()

    # Test values 15-25
    result_20 = metric.normalize(20)
    assert 0.2 <= result_20 <= 0.4

    result_25 = metric.normalize(25)
    assert 0.0 <= result_25 <= 0.3


def test_cognitive_complexity_normalize_very_poor():
    """Test normalization for very poor complexity (>25)."""
    metric = CognitiveComplexity()

    # Test values > 25
    result_30 = metric.normalize(30)
    assert 0.0 <= result_30 <= 0.2

    result_50 = metric.normalize(50)
    assert 0.0 <= result_50 <= 0.1

    result_100 = metric.normalize(100)
    assert result_100 == 0.0


def test_cognitive_complexity_recommendations_excellent():
    """Test recommendations for excellent complexity."""
    metric = CognitiveComplexity()

    recs = metric.get_recommendations(3.0)

    assert len(recs) > 0
    assert any("EXCELLENT" in rec for rec in recs)


def test_cognitive_complexity_recommendations_good():
    """Test recommendations for good complexity."""
    metric = CognitiveComplexity()

    recs = metric.get_recommendations(7.0)

    assert len(recs) > 0
    assert any("GOOD" in rec for rec in recs)


def test_cognitive_complexity_recommendations_moderate():
    """Test recommendations for moderate complexity."""
    metric = CognitiveComplexity()

    recs = metric.get_recommendations(12.0)

    assert len(recs) > 0
    assert any("MODERATE" in rec for rec in recs)
    # Should have specific recommendations
    assert len(recs) > 1


def test_cognitive_complexity_recommendations_high():
    """Test recommendations for high complexity."""
    metric = CognitiveComplexity()

    recs = metric.get_recommendations(18.0)

    assert len(recs) > 0
    assert any("HIGH" in rec for rec in recs)
    # Should have specific recommendations
    assert len(recs) > 1
    assert any("nested" in str(rec).lower() for rec in recs)


def test_cognitive_complexity_recommendations_critical():
    """Test recommendations for critical complexity."""
    metric = CognitiveComplexity()

    recs = metric.get_recommendations(30.0)

    assert len(recs) > 0
    assert any("CRITICAL" in rec for rec in recs)
    # Should have specific recommendations
    assert len(recs) > 1


def test_cognitive_complexity_get_name():
    """Test get_name method."""
    metric = CognitiveComplexity()
    assert metric.get_name() == "Cognitive Complexity"


def test_cognitive_complexity_get_weight():
    """Test get_weight method."""
    metric = CognitiveComplexity()
    weight = metric.get_weight()

    # Weight should be 0.75 based on documentation
    assert weight == 0.75


def test_cognitive_complexity_multiple_functions():
    """Test cognitive complexity with multiple functions."""
    code = textwrap.dedent('''
        """Module with multiple functions."""
        def simple1():
            """Simple function 1."""
            return 1

        def simple2():
            """Simple function 2."""
            return 2

        def complex(x, y):
            """Complex function."""
            if x:
                if y:
                    return x + y
            return 0
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "multi.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Should return average complexity
        assert result["average"] >= 0


def test_cognitive_complexity_with_loops():
    """Test cognitive complexity with loops."""
    code = textwrap.dedent('''
        """Module with loops."""
        def with_loop(items):
            """Function with a loop."""
            result = []
            for item in items:
                if item > 0:
                    result.append(item)
            return result
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "loops.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Loops increase cognitive complexity
        assert result["average"] > 0
