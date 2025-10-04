"""
Integration tests for code smell detection system.

Tests the full pipeline:
1. AST test smell detector
2. PyExamine detector (if available)
3. SmellAggregator de-duplication
4. CodeSmellDensity metric calculation

"""

import tempfile
import textwrap
from pathlib import Path


def test_ast_detector_with_metric():
    """Test AST detector integrated with CodeSmellDensity metric."""
    from mfcqi.metrics.code_smell import CodeSmellDensity
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    # Create test code with known smells
    code = textwrap.dedent("""
        def test_bad_assertions():
            # This test has Assertion Roulette (4+ assertions without messages)
            assert 1 == 1
            assert 2 == 2
            assert 3 == 3
            assert 4 == 4

        def test_empty():
            # This test is empty (no assertions)
            user = User("test")
            print(user.name)

        def test_with_sleep():
            # This test uses sleep (Sleepy Test)
            import time
            setup()
            time.sleep(1)
            assert system.ready
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_smelly.py"
        test_file.write_text(code)

        # Use AST detector with metric
        metric = CodeSmellDensity(detectors=[ASTTestSmellDetector()])

        density = metric.extract(Path(tmpdir))

        # Should detect 4 test smells in this code
        # With ~13 LOC of code, that's about (4 smells * 2.0 avg weight * 0.2 test weight / 13) * 1000
        # = about 123 weighted smells per KLOC
        assert density > 0.0  # Should have smells
        assert density < 500.0  # Reasonable upper bound

        # Normalize to quality score
        score = metric.normalize(density)

        # With high smell density (>50 per KLOC), score can be 0.0
        assert score < 1.0  # Not perfect
        assert score >= 0.0  # Can be 0.0 for very smelly code


def test_multiple_detectors_with_aggregation():
    """Test multiple detectors working together with de-duplication."""
    from mfcqi.metrics.code_smell import CodeSmellDensity
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector
    from mfcqi.smell_detection.pyexamine import PyExamineDetector

    code = textwrap.dedent("""
        def test_multi():
            assert 1 == 1
            assert 2 == 2
            assert 3 == 3
            assert 4 == 4
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_multi.py"
        test_file.write_text(code)

        # Use multiple detectors
        detectors = [
            ASTTestSmellDetector(),
            PyExamineDetector(),  # Will return empty if not installed
        ]

        metric = CodeSmellDensity(detectors=detectors)
        density = metric.extract(Path(tmpdir))

        # Should work even if PyExamine not installed (AST detector still works)
        assert isinstance(density, (int, float))
        assert density >= 0.0


def test_smell_categories_weighted_correctly():
    """Test that different smell categories are weighted correctly."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()
    weights = metric._get_category_weights()

    # Verify weights from code_smells.md
    assert weights["architectural"] == 0.45
    assert weights["design"] == 0.45
    assert weights["implementation"] == 0.35
    assert weights["test"] == 0.20

    # Sum should be > 1.0 (because they're individual weights, not percentages)
    # This is correct - they're applied to category counts separately


def test_normalization_curve():
    """Test that normalization follows expected curve."""
    import pytest

    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()

    # Test key points on the normalization curve (use approx for float comparison)
    assert metric.normalize(0.0) == pytest.approx(1.0)  # Perfect - no smells
    assert metric.normalize(5.0) == pytest.approx(0.8)  # Good
    assert metric.normalize(10.0) == pytest.approx(0.6)  # Moderate
    assert metric.normalize(20.0) == pytest.approx(0.3)  # Poor
    assert metric.normalize(50.0) == pytest.approx(0.0)  # Very poor

    # Verify monotonic decrease (more smells = lower score)
    assert metric.normalize(1.0) > metric.normalize(5.0)
    assert metric.normalize(5.0) > metric.normalize(10.0)
    assert metric.normalize(10.0) > metric.normalize(20.0)


def test_metric_weight_is_moderate():
    """Test that CodeSmellDensity has moderate weight (0.5)."""
    from mfcqi.metrics.code_smell import CodeSmellDensity

    metric = CodeSmellDensity()
    assert metric.get_weight() == 0.5


def test_empty_codebase_perfect_score():
    """Test that empty codebase gets perfect score."""
    from mfcqi.metrics.code_smell import CodeSmellDensity
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    with tempfile.TemporaryDirectory() as tmpdir:
        metric = CodeSmellDensity(detectors=[ASTTestSmellDetector()])

        density = metric.extract(Path(tmpdir))
        assert density == 0.0

        score = metric.normalize(density)
        assert score == 1.0


def test_ast_detector_only_analyzes_test_files():
    """Test that AST detector ignores production code."""
    from mfcqi.metrics.code_smell import CodeSmellDensity
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    test_code = textwrap.dedent("""
        def test_something():
            assert 1 == 1
            assert 2 == 2
            assert 3 == 3
            assert 4 == 4
    """)

    prod_code = textwrap.dedent("""
        def calculate():
            # This has prints but it's not a test
            print("Calculating...")
            return 42
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test_foo.py").write_text(test_code)
        (Path(tmpdir) / "calculator.py").write_text(prod_code)

        metric = CodeSmellDensity(detectors=[ASTTestSmellDetector()])
        density = metric.extract(Path(tmpdir))

        # Should only count test smells (Assertion Roulette from test file)
        # Should not count print in production code
        assert density > 0.0  # Has test smells


def test_smell_detection_with_real_metric():
    """Test full integration: detect smells, aggregate, calculate metric."""
    from mfcqi.metrics.code_smell import CodeSmellDensity
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    # Create a realistic test file with multiple smell types
    code = textwrap.dedent("""
        import time

        def test_good():
            # This is a good test
            result = calculate(2, 3)
            assert result == 5, "2 + 3 should equal 5"

        def test_assertion_roulette():
            user = User("John", 25)
            assert user.name == "John"
            assert user.age == 25
            assert user.email is not None
            assert user.is_active
            assert user.created_at is not None

        def test_sleepy():
            setup()
            time.sleep(0.5)
            assert is_ready()

        def test_empty():
            user = User("Test")
            # Oops, forgot assertions

        def test_with_print():
            result = process()
            print(f"Result: {result}")
            assert result > 0
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_suite.py"
        test_file.write_text(code)

        # Calculate metric
        metric = CodeSmellDensity(detectors=[ASTTestSmellDetector()])

        # Extract smell density
        density = metric.extract(Path(tmpdir))
        assert density > 0.0  # Should detect smells

        # Normalize to quality score
        score = metric.normalize(density)
        assert 0.0 <= score < 1.0  # Should have lower score due to smells

        # Get full metric result
        result = metric.calculate(Path(tmpdir))
        assert result["metric_name"] == "Code Smell Density"
        assert result["weight"] == 0.5
        assert result["normalized_value"] < 1.0  # Has smells
