"""
Test for Ruff Integration - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import json
import tempfile
from pathlib import Path


def test_ruff_analyzer_exists():
    """RED: Test that RuffAnalyzer class exists."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    assert RuffAnalyzer is not None


def test_ruff_analyzer_initialization():
    """RED: Test that RuffAnalyzer can be initialized."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    analyzer = RuffAnalyzer()
    assert analyzer is not None


def test_ruff_analyzer_analyze_file():
    """RED: Test Ruff analysis of a single file."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    # Code with various style and quality issues
    problematic_code = """
import os,sys
import requests

def  function_with_issues():
    x=1+2
    y  =   3
    unused_var = 4
    print(f"Value: {x}")
    return x

class SomeClass:
    def __init__(self ):
        pass

    def unused_method(self):
        pass

def missing_return_annotation():
    return True
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "issues.py"
        test_file.write_text(problematic_code)

        analyzer = RuffAnalyzer()
        results = analyzer.analyze_file(test_file)

        assert isinstance(results, list)
        assert len(results) > 0

        # Should find various issues
        issues = [r for r in results if r.get("code")]
        assert len(issues) > 0


def test_ruff_analyzer_analyze_directory():
    """RED: Test Ruff analysis of a directory."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code1 = """
import os,sys

def bad_formatting():
    x=1+2
    return x
"""

    code2 = """
import json

def unused_import():
    return True
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = Path(tmpdir) / "file1.py"
        file2 = Path(tmpdir) / "file2.py"
        file1.write_text(code1)
        file2.write_text(code2)

        analyzer = RuffAnalyzer()
        results = analyzer.analyze_directory(Path(tmpdir))

        assert isinstance(results, dict)
        assert len(results) >= 1  # At least one file should have issues


def test_ruff_result_format():
    """RED: Test Ruff result format contains required fields."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = """
import os,sys

def bad_function():
    x=1+2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Each result should have required fields
        for result in results:
            assert "code" in result
            assert "line" in result
            assert "column" in result
            assert "message" in result
            assert "filename" in result


def test_ruff_rule_categories():
    """RED: Test Ruff rule categorization."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    analyzer = RuffAnalyzer()

    # Test rule category mapping
    assert analyzer.get_rule_category("E") == "style"  # pycodestyle errors
    assert analyzer.get_rule_category("W") == "style"  # pycodestyle warnings
    assert analyzer.get_rule_category("F") == "error"  # pyflakes
    assert analyzer.get_rule_category("C") == "complexity"  # mccabe
    assert analyzer.get_rule_category("B") == "bugprone"  # flake8-bugbear
    assert analyzer.get_rule_category("S") == "security"  # flake8-bandit


def test_ruff_severity_mapping():
    """RED: Test Ruff severity mapping to standard levels."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    analyzer = RuffAnalyzer()

    # Test severity mapping based on rule types
    assert analyzer.map_severity("F") == "error"  # Pyflakes errors
    assert analyzer.map_severity("E") == "warning"  # Style errors
    assert analyzer.map_severity("W") == "warning"  # Style warnings
    assert analyzer.map_severity("C") == "info"  # Complexity
    assert analyzer.map_severity("B") == "warning"  # Bug-prone patterns
    assert analyzer.map_severity("S") == "error"  # Security issues


def test_ruff_filter_by_category():
    """RED: Test filtering Ruff results by rule category."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    # Mock results with different rule types
    mock_results = [
        {"code": "E501", "message": "Line too long"},
        {"code": "F401", "message": "Imported but unused"},
        {"code": "W292", "message": "No newline at end of file"},
        {"code": "B902", "message": "Invalid first argument name"},
        {"code": "S101", "message": "Use of assert detected"},
    ]

    analyzer = RuffAnalyzer()

    # Filter by style issues only
    style_issues = analyzer.filter_by_category(mock_results, ["style"])
    style_codes = [r["code"][0] for r in style_issues]
    assert "E" in style_codes
    assert "W" in style_codes

    # Filter by errors only
    error_issues = analyzer.filter_by_category(mock_results, ["error"])
    error_codes = [r["code"][0] for r in error_issues]
    assert "F" in error_codes


def test_ruff_configuration():
    """RED: Test Ruff configuration options."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    # Test with custom configuration
    config = {
        "line_length": 120,
        "select": ["E", "F", "W"],
        "ignore": ["E501", "W503"],
        "exclude": ["migrations"],
    }

    analyzer = RuffAnalyzer(config=config)
    assert analyzer.config == config


def test_ruff_get_diagnostics():
    """RED: Test conversion of Ruff results to diagnostics."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = """
import os,sys

def problematic_function():
    x=1+2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()
        diagnostics = analyzer.get_diagnostics(test_file)

        assert isinstance(diagnostics, list)
        # Should contain DiagnosticsCollection objects
        if diagnostics:
            from mfcqi.analysis.diagnostics import DiagnosticsCollection

            assert isinstance(diagnostics[0], DiagnosticsCollection)


def test_ruff_rule_explanations():
    """RED: Test that Ruff provides rule explanations."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    analyzer = RuffAnalyzer()

    # Should be able to get explanation for common rules
    explanation = analyzer.get_rule_explanation("F401")
    assert isinstance(explanation, str)
    assert len(explanation) > 0

    # Should handle unknown rules gracefully
    unknown_explanation = analyzer.get_rule_explanation("UNKNOWN")
    assert isinstance(unknown_explanation, str)


def test_ruff_json_output():
    """RED: Test Ruff JSON output format."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = """
import os,sys

def test_function():
    x=1+2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should be serializable to JSON
        json_str = json.dumps(results)
        parsed = json.loads(json_str)
        assert isinstance(parsed, list)


def test_ruff_line_and_column_accuracy():
    """RED: Test that Ruff reports accurate line and column numbers."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = """
# Line 1
import os,sys  # Line 2 - should have import style issue

# Line 4
def function():  # Line 5
    x=1+2  # Line 6 - should have spacing issue
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Verify line and column numbers are reasonable
        for result in results:
            line = result.get("line", 0)
            column = result.get("column", 0)
            assert line >= 1
            assert column >= 0


def test_ruff_error_handling():
    """RED: Test Ruff error handling for invalid files."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    # Test with invalid Python file
    invalid_code = """
def invalid_syntax(
    # Missing closing parenthesis
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "invalid.py"
        test_file.write_text(invalid_code)

        analyzer = RuffAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should handle errors gracefully
        assert isinstance(results, list)
        # May contain syntax errors or be empty


def test_ruff_integration_with_diagnostics():
    """RED: Test Ruff integration with analysis diagnostics."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = """
import os,sys

def style_issues():
    x=1+2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()
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
            assert diagnostic.source == "ruff"


def test_ruff_fix_suggestions():
    """RED: Test that Ruff can provide fix suggestions."""
    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = """
import os,sys

def formatting_issues():
    x=1+2
    return x
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()

        # Should be able to get fix suggestions
        fixes = analyzer.get_fix_suggestions(test_file)
        assert isinstance(fixes, list)


def test_ruff_performance():
    """RED: Test that Ruff analysis is reasonably fast."""
    import time

    from mfcqi.analysis.tools.ruff_analyzer import RuffAnalyzer

    code = (
        """
    import os, sys
    import json, re

    def test_function():
        x = 1 + 2
        y = 3 + 4
        return x + y
    """
        * 10
    )  # Repeat to create larger file

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "large.py"
        test_file.write_text(code)

        analyzer = RuffAnalyzer()

        start_time = time.time()
        results = analyzer.analyze_file(test_file)
        end_time = time.time()

        # Should complete within reasonable time (2 seconds)
        assert (end_time - start_time) < 2.0
        assert isinstance(results, list)
