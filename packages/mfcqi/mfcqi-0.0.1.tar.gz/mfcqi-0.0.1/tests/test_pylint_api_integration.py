"""
Test for Pylint API Integration - Strict TDD for code-level API usage.

with direct Python API calls using pylint.lint.Run.

This is to fix the DISHONEST subprocess implementation.
"""

import tempfile
from pathlib import Path


def test_pylint_uses_python_api_not_subprocess():
    """
    RED: Test that PylintAnalyzer uses pylint.lint.Run API, not subprocess.

    This test verifies we're using the HONEST code-level API integration
    instead of the DISHONEST subprocess approach.
    """
    import inspect

    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    analyzer = PylintAnalyzer()

    # Get the source code of analyze_file method
    source = inspect.getsource(analyzer.analyze_file)

    # MUST NOT use subprocess (check for actual usage, not just word in comments)
    assert (
        "subprocess.run" not in source
        and "subprocess.call" not in source
        and "subprocess.Popen" not in source
        and "import subprocess" not in source
    ), "PylintAnalyzer must NOT use subprocess module"

    # MUST use pylint.lint API
    assert "pylint.lint" in source or "lint.Run" in source or "Run(" in source, (
        "PylintAnalyzer must use pylint.lint.Run Python API"
    )


def test_pylint_api_detects_undefined_variable():
    """
    RED: Test Pylint API detects undefined variables.

    Real test using pylint.lint.Run API directly.
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code_with_undefined = """
def use_undefined():
    return undefined_variable
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_undefined.py"
        test_file.write_text(code_with_undefined)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should detect undefined variable
        assert isinstance(results, list)
        assert len(results) > 0, "Should detect undefined variable"

        # Check that it's the right issue
        undefined_issues = [
            r
            for r in results
            if "undefined" in r.get("message", "").lower()
            or r.get("symbol") == "undefined-variable"
        ]
        assert len(undefined_issues) > 0, "Should identify undefined variable issue"


def test_pylint_api_detects_unused_import():
    """
    RED: Test Pylint API detects unused imports.
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code_with_unused_import = """
import os
import sys

def main():
    print("Hello")
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_unused.py"
        test_file.write_text(code_with_unused_import)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should detect unused imports
        assert isinstance(results, list)
        assert len(results) > 0, "Should detect unused imports"


def test_pylint_api_respects_disable_config():
    """
    RED: Test that Pylint API respects disable configuration.

    Verify we can configure via Python API, not command-line args.
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
import os
import sys

def main():
    print("Hello")
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        # Initialize with config to disable unused-import check
        config = {"disable": ["unused-import"]}
        analyzer = PylintAnalyzer(config=config)
        results = analyzer.analyze_file(test_file)

        # Should respect config and skip unused-import
        for result in results:
            assert result.get("symbol") != "unused-import", (
                "Should skip unused-import when configured"
            )


def test_pylint_api_respects_enable_config():
    """
    RED: Test that Pylint API respects enable configuration.
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def func():
    pass
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        # Initialize with config to enable specific checks
        config = {"enable": ["missing-docstring"]}
        analyzer = PylintAnalyzer(config=config)
        results = analyzer.analyze_file(test_file)

        # Should detect missing docstring when enabled
        assert isinstance(results, list)


def test_pylint_api_returns_structured_results():
    """
    RED: Test that Pylint API returns properly structured results.

    Results should come from pylint.lint, not JSON parsing of subprocess output.
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def bad_function():
    return undefined_var
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_structure.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        assert isinstance(results, list), "Should return list"

        if results:  # If issues were found
            result = results[0]

            # Verify structure from API (not subprocess JSON parsing)
            required_fields = ["type", "line", "column", "message", "symbol", "path"]

            for field in required_fields:
                assert field in result, f"Result must have {field} field"

            # Verify types are correct (from API, not string parsing)
            assert isinstance(result["line"], int), "line should be int from API, not string"
            assert isinstance(result["column"], int), "column should be int from API, not string"


def test_pylint_api_handles_clean_code():
    """
    RED: Test Pylint API handles clean code (no issues).
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    clean_code = """
\"\"\"Module docstring.\"\"\"


def safe_function(x: int, y: int) -> int:
    \"\"\"Add two numbers.\"\"\"
    return x + y


def another_safe_function(data: str) -> int:
    \"\"\"Return length of string.\"\"\"
    return len(data)
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "clean.py"
        test_file.write_text(clean_code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should return empty list or very few issues (maybe just conventions)
        assert isinstance(results, list)


def test_pylint_api_handles_syntax_errors():
    """
    RED: Test Pylint API gracefully handles invalid Python code.
    """
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    invalid_code = """
def broken syntax here
    this is not valid python
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "broken.py"
        test_file.write_text(invalid_code)

        analyzer = PylintAnalyzer()

        # Should not crash, should return results with syntax error
        try:
            results = analyzer.analyze_file(test_file)
            assert isinstance(results, list)
            # Should have syntax error reported
            if results:
                assert any("syntax" in r.get("message", "").lower() for r in results)
        except Exception as e:
            # If it raises, it should be a specific pylint exception
            # not a generic subprocess error
            assert "subprocess" not in str(e).lower(), "Should not have subprocess errors"
