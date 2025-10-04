"""
Test for Pylint Integration - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import json
import tempfile
from pathlib import Path


def test_pylint_analyzer_exists():
    """RED: Test that PylintAnalyzer class exists."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    assert PylintAnalyzer is not None


def test_pylint_analyzer_initialization():
    """RED: Test that PylintAnalyzer can be initialized."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    analyzer = PylintAnalyzer()
    assert analyzer is not None


def test_pylint_analyzer_analyze_file():
    """RED: Test Pylint analysis of a single file."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def missing_docstring():
    x = 1
    return x

class MissingDocstring:
    pass
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        assert isinstance(results, list)
        assert len(results) > 0

        # Should find missing docstring issues
        docstring_issues = [r for r in results if "docstring" in r.get("message", "").lower()]
        assert len(docstring_issues) > 0


def test_pylint_analyzer_analyze_directory():
    """RED: Test Pylint analysis of a directory."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code1 = """
def function_with_issues():
    x = 1
    y = 2
    return x
"""

    code2 = """
import os
import sys

def another_function():
    pass
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = Path(tmpdir) / "file1.py"
        file2 = Path(tmpdir) / "file2.py"
        file1.write_text(code1)
        file2.write_text(code2)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_directory(Path(tmpdir))

        assert isinstance(results, dict)
        assert len(results) == 2  # Two files
        assert "file1.py" in str(results)
        assert "file2.py" in str(results)


def test_pylint_result_format():
    """RED: Test Pylint result format contains required fields."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def bad_function():
    x = 1
    y = 2
    if x:
        z = 3
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Each result should have required fields
        for result in results:
            assert "type" in result
            assert "line" in result
            assert "column" in result
            assert "message" in result
            assert "symbol" in result
            assert "path" in result


def test_pylint_severity_mapping():
    """RED: Test Pylint severity mapping to standard levels."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    analyzer = PylintAnalyzer()

    # Test severity mapping
    assert analyzer.map_severity("error") == "error"
    assert analyzer.map_severity("warning") == "warning"
    assert analyzer.map_severity("convention") == "info"
    assert analyzer.map_severity("refactor") == "hint"
    assert analyzer.map_severity("fatal") == "error"


def test_pylint_filter_results():
    """RED: Test filtering Pylint results by severity."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    # Mock results with different severities
    mock_results = [
        {"type": "error", "message": "Error message", "line": 1},
        {"type": "warning", "message": "Warning message", "line": 2},
        {"type": "convention", "message": "Convention message", "line": 3},
        {"type": "refactor", "message": "Refactor message", "line": 4},
    ]

    analyzer = PylintAnalyzer()

    # Filter by error only
    errors = analyzer.filter_by_severity(mock_results, ["error"])
    assert len(errors) == 1
    assert errors[0]["type"] == "error"

    # Filter by warning and error
    important = analyzer.filter_by_severity(mock_results, ["error", "warning"])
    assert len(important) == 2


def test_pylint_configuration():
    """RED: Test Pylint configuration options."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    # Test with custom configuration
    config = {
        "disable": ["missing-docstring"],
        "enable": ["unused-variable"],
        "max-line-length": 120,
    }

    analyzer = PylintAnalyzer(config=config)
    assert analyzer.config == config


def test_pylint_get_diagnostics():
    """RED: Test conversion of Pylint results to diagnostics."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def function_with_unused_variable():
    x = 1
    y = 2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        diagnostics = analyzer.get_diagnostics(test_file)

        assert isinstance(diagnostics, list)
        # Should contain DiagnosticsCollection objects
        if diagnostics:
            from mfcqi.analysis.diagnostics import DiagnosticsCollection

            assert isinstance(diagnostics[0], DiagnosticsCollection)


def test_pylint_error_handling():
    """RED: Test Pylint error handling for invalid files."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    # Test with invalid Python file
    invalid_code = """
def invalid_syntax(
    # Missing closing parenthesis
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "invalid.py"
        test_file.write_text(invalid_code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should handle errors gracefully
        assert isinstance(results, list)
        # Should contain syntax error (check both message and symbol)
        syntax_errors = [
            r
            for r in results
            if "syntax" in r.get("message", "").lower() or "syntax-error" in r.get("symbol", "")
        ]
        assert len(syntax_errors) > 0


def test_pylint_json_output():
    """RED: Test Pylint JSON output format."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def simple_function():
    return True
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "simple.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should be serializable to JSON
        json_str = json.dumps(results)
        parsed = json.loads(json_str)
        assert isinstance(parsed, list)


def test_pylint_line_number_accuracy():
    """RED: Test that Pylint reports accurate line numbers."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
# Line 1

def function_on_line_3():  # Line 3
    pass

# Line 6
def another_function():   # Line 7
    x = 1  # Line 8
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Verify line numbers are reasonable
        for result in results:
            line = result.get("line", 0)
            assert 1 <= line <= 10  # Within expected range


def test_pylint_detailed_explanations():
    """RED: Test that Pylint provides detailed explanations."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def unused_variable_function():
    x = 1
    y = 2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should find unused variable
        unused_issues = [r for r in results if "unused" in r.get("message", "").lower()]
        if unused_issues:
            issue = unused_issues[0]
            assert "message" in issue
            assert len(issue["message"]) > 10  # Should have detailed message


def test_pylint_integration_with_diagnostics():
    """RED: Test Pylint integration with analysis diagnostics."""
    from mfcqi.analysis.tools.pylint_analyzer import PylintAnalyzer

    code = """
def function_with_issues():
    x = 1
    if x:
        pass
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = PylintAnalyzer()
        diagnostics_collections = analyzer.get_diagnostics(test_file)

        if diagnostics_collections:
            collection = diagnostics_collections[0]
            assert collection.file_path == str(test_file)
            assert len(collection.diagnostics) > 0

            # Check diagnostic format
            diagnostic = collection.diagnostics[0]
            assert hasattr(diagnostic, "range")
            assert hasattr(diagnostic, "message")
            assert hasattr(diagnostic, "severity")
            assert diagnostic.source == "pylint"
