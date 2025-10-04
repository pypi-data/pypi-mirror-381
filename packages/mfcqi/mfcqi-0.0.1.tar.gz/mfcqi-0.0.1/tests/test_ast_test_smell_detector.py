"""
Test for AST-based test smell detector - following strict TDD.

Detects common test smells using AST analysis without external tools.
"""

import tempfile
import textwrap
from pathlib import Path


def test_ast_test_smell_detector_exists():
    """RED: Test that ASTTestSmellDetector class exists."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    assert ASTTestSmellDetector is not None


def test_detector_is_smell_detector():
    """RED: Test that detector implements SmellDetector interface."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector
    from mfcqi.smell_detection.detector_base import SmellDetector

    assert issubclass(ASTTestSmellDetector, SmellDetector)


def test_detector_has_correct_name():
    """RED: Test that detector returns correct name."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    detector = ASTTestSmellDetector()
    assert detector.name == "ast-test-smells"


def test_detects_assertion_roulette():
    """RED: Test detection of multiple assertions without messages."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    code = textwrap.dedent("""
        def test_user_validation():
            user = User("John", 25)
            assert user.name == "John"
            assert user.age == 25
            assert user.is_valid()
            assert user.email is not None
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_user.py"
        test_file.write_text(code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # Should detect Assertion Roulette (4+ assertions without messages)
        roulette_smells = [s for s in smells if s.id == "ASSERTION_ROULETTE"]
        assert len(roulette_smells) > 0
        assert roulette_smells[0].location == "test_user.py:2"


def test_detects_empty_test():
    """RED: Test detection of tests with no assertions."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    code = textwrap.dedent("""
        def test_nothing():
            user = User("John", 25)
            print(f"Created user: {user}")
            # No assertions!
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_empty.py"
        test_file.write_text(code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # Should detect Empty Test
        empty_smells = [s for s in smells if s.id == "EMPTY_TEST"]
        assert len(empty_smells) == 1
        assert "test_nothing" in empty_smells[0].description


def test_detects_long_test():
    """RED: Test detection of overly long test functions."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    # Create a test with 60+ lines
    lines = ["def test_very_long():"]
    for i in range(60):
        lines.append(f"    x{i} = {i}")
    lines.append("    assert x0 == 0")

    code = "\n".join(lines)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_long.py"
        test_file.write_text(code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # Should detect Long Test
        long_smells = [s for s in smells if s.id == "LONG_TEST"]
        assert len(long_smells) == 1


def test_detects_sleepy_test():
    """RED: Test detection of tests with sleep() calls."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    code = textwrap.dedent("""
        import time

        def test_with_sleep():
            setup_system()
            time.sleep(2)  # Bad practice!
            assert system.is_ready()
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_sleepy.py"
        test_file.write_text(code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # Should detect Sleepy Test
        sleepy_smells = [s for s in smells if s.id == "SLEEPY_TEST"]
        assert len(sleepy_smells) == 1


def test_detects_redundant_print():
    """RED: Test detection of print statements in tests."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    code = textwrap.dedent("""
        def test_with_print():
            result = calculate(5, 10)
            print(f"Result: {result}")  # Should use logging
            assert result == 15
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_print.py"
        test_file.write_text(code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # Should detect Redundant Print
        print_smells = [s for s in smells if s.id == "REDUNDANT_PRINT"]
        assert len(print_smells) == 1


def test_ignores_non_test_files():
    """RED: Test that detector only analyzes test files."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    test_code = textwrap.dedent("""
        def test_something():
            assert True
    """)

    prod_code = textwrap.dedent("""
        def calculate(a, b):
            print("Debug")  # This is fine in production code
            return a + b
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_foo.py"
        test_file.write_text(test_code)

        prod_file = Path(tmpdir) / "calculator.py"
        prod_file.write_text(prod_code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # Should not detect print in production code
        locations = [s.location for s in smells]
        assert not any("calculator.py" in loc for loc in locations)


def test_empty_codebase_returns_no_smells():
    """RED: Test that empty codebase returns empty list."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector

    with tempfile.TemporaryDirectory() as tmpdir:
        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        assert smells == []


def test_all_smells_have_test_category():
    """RED: Test that all detected smells are categorized as TEST."""
    from mfcqi.smell_detection.ast_test_smells import ASTTestSmellDetector
    from mfcqi.smell_detection.models import SmellCategory

    code = textwrap.dedent("""
        def test_bad():
            assert 1 == 1
            assert 2 == 2
            assert 3 == 3
            assert 4 == 4
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_bad.py"
        test_file.write_text(code)

        detector = ASTTestSmellDetector()
        smells = detector.detect(Path(tmpdir))

        # All smells should be TEST category
        for smell in smells:
            assert smell.category == SmellCategory.TEST
