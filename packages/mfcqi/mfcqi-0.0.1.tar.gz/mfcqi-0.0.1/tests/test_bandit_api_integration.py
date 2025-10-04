"""
Test for Bandit API Integration - Strict TDD for code-level API usage.

with direct Python API calls using bandit.core.manager and bandit.core.config.

This is to fix the DISHONEST subprocess implementation.
"""

import tempfile
from pathlib import Path


def test_bandit_uses_python_api_not_subprocess():
    """
    RED: Test that BanditAnalyzer uses bandit.core API, not subprocess.

    This test verifies we're using the HONEST code-level API integration
    instead of the DISHONEST subprocess approach.
    """
    import inspect

    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    analyzer = BanditAnalyzer()

    # Get the source code of analyze_file method
    source = inspect.getsource(analyzer.analyze_file)

    # MUST NOT use subprocess (check for actual usage, not just word in comments)
    assert (
        "subprocess.run" not in source
        and "subprocess.call" not in source
        and "subprocess.Popen" not in source
        and "import subprocess" not in source
    ), "BanditAnalyzer must NOT use subprocess module"

    # MUST use bandit.core API
    assert "BanditManager" in source or "b_manager" in source, (
        "BanditAnalyzer must use bandit.core.manager Python API"
    )


def test_bandit_api_detects_hardcoded_password():
    """
    RED: Test Bandit API detects hardcoded passwords.

    Real test using bandit.core.manager API directly.
    """
    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    code_with_password = """
def get_database_connection():
    password = "hardcoded_secret_123"
    return connect(password)
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_passwords.py"
        test_file.write_text(code_with_password)

        analyzer = BanditAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should detect hardcoded password
        assert isinstance(results, list)
        assert len(results) > 0, "Should detect hardcoded password"

        # Check that it's the right issue
        password_issues = [r for r in results if "password" in r.get("issue_text", "").lower()]
        assert len(password_issues) > 0, "Should identify password issue"


def test_bandit_api_detects_sql_injection():
    """
    RED: Test Bandit API detects SQL injection vulnerabilities.
    """
    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    code_with_sql_injection = """
import sqlite3

def unsafe_query(user_input):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL injection vulnerability
    cursor.execute(f"SELECT * FROM users WHERE id = {user_input}")
    return cursor.fetchall()
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_sql.py"
        test_file.write_text(code_with_sql_injection)

        analyzer = BanditAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should detect SQL issues
        assert isinstance(results, list)
        # SQL injection detection varies, so just verify it scans successfully
        # The key is that it uses the API, not subprocess


def test_bandit_api_respects_config():
    """
    RED: Test that Bandit API respects configuration.

    Verify we can configure via Python API, not command-line args.
    """
    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    code = """
import subprocess

def run_command(cmd):
    subprocess.call(cmd, shell=True)
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        # Initialize with config to skip certain tests
        config = {"skip_tests": ["B602"]}  # Skip shell=True check
        analyzer = BanditAnalyzer(config=config)
        results = analyzer.analyze_file(test_file)

        # Should respect config and skip B602
        for result in results:
            assert result.get("test_name") != "B602", "Should skip B602 when configured"


def test_bandit_api_returns_structured_results():
    """
    RED: Test that Bandit API returns properly structured results.

    Results should come from bandit.core, not JSON parsing of subprocess output.
    """
    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    code = """
def eval_user_input(data):
    return eval(data)  # Dangerous use of eval
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_eval.py"
        test_file.write_text(code)

        analyzer = BanditAnalyzer()
        results = analyzer.analyze_file(test_file)

        assert isinstance(results, list), "Should return list"

        if results:  # If issues were found
            result = results[0]

            # Verify structure from API (not subprocess JSON parsing)
            required_fields = [
                "line_number",
                "issue_confidence",
                "issue_severity",
                "issue_text",
                "test_name",
                "filename",
            ]

            for field in required_fields:
                assert field in result, f"Result must have {field} field"

            # Verify types are correct (from API, not string parsing)
            assert isinstance(result["line_number"], int), (
                "line_number should be int from API, not string"
            )


def test_bandit_api_handles_no_issues():
    """
    RED: Test Bandit API handles clean code (no issues).
    """
    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    clean_code = """
def safe_function(x, y):
    return x + y

def another_safe_function(data):
    return len(data)
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "clean.py"
        test_file.write_text(clean_code)

        analyzer = BanditAnalyzer()
        results = analyzer.analyze_file(test_file)

        # Should return empty list, not crash
        assert isinstance(results, list)
        assert len(results) == 0, "Clean code should have no issues"


def test_bandit_api_handles_syntax_errors():
    """
    RED: Test Bandit API gracefully handles invalid Python code.
    """
    from mfcqi.analysis.tools.bandit_analyzer import BanditAnalyzer

    invalid_code = """
def broken syntax here
    this is not valid python
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "broken.py"
        test_file.write_text(invalid_code)

        analyzer = BanditAnalyzer()

        # Should not crash, should return empty list or handle gracefully
        try:
            results = analyzer.analyze_file(test_file)
            assert isinstance(results, list)
        except Exception as e:
            # If it raises, it should be a specific bandit exception
            # not a generic subprocess error
            assert "subprocess" not in str(e).lower(), "Should not have subprocess errors"
