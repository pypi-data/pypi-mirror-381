"""
Test for detect-secrets Python API Integration - Strict TDD.

detect-secrets HAS a Python API via:
- detect_secrets.core.scan.scan_file
- detect_secrets.settings.get_settings
- detect_secrets.settings.Settings.configure_plugins

Using these APIs directly - NO subprocess.

"""

import tempfile
from pathlib import Path


def test_detect_secrets_uses_python_api_not_subprocess():
    """
    RED: Test that DetectSecretsAnalyzer uses detect_secrets Python API, not subprocess.

    This test verifies we're using the HONEST code-level API integration.
    """
    import inspect

    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    analyzer = DetectSecretsAnalyzer()

    # Get the source code of scan_file method
    source = inspect.getsource(analyzer.scan_file)

    # MUST NOT use subprocess
    assert (
        "subprocess.run" not in source
        and "subprocess.call" not in source
        and "subprocess.Popen" not in source
    ), "DetectSecretsAnalyzer must NOT use subprocess module"

    # MUST use detect_secrets Python API
    assert "scan_file" in source or "detect_secrets" in source, (
        "DetectSecretsAnalyzer must use detect_secrets Python API"
    )


def test_detect_secrets_finds_aws_keys():
    """
    RED: Test that detect-secrets finds AWS access keys.
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    code_with_aws = """
# AWS credentials
aws_access_key = "AKIAIOSFODNN7EXAMPLE"
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "aws_secrets.py"
        test_file.write_text(code_with_aws)

        analyzer = DetectSecretsAnalyzer()
        results = analyzer.scan_file(test_file)

        # Should find AWS key
        assert isinstance(results, list)
        assert len(results) > 0, "Should detect AWS access key"

        # Check structure
        secret = results[0]
        assert "type" in secret
        assert "line_number" in secret
        assert "AWS" in secret["type"]


def test_detect_secrets_finds_private_keys():
    """
    RED: Test that detect-secrets finds private keys.
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    code_with_private_key = """
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890
-----END RSA PRIVATE KEY-----'''
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "private_key.py"
        test_file.write_text(code_with_private_key)

        analyzer = DetectSecretsAnalyzer()
        results = analyzer.scan_file(test_file)

        # Should find private key
        assert isinstance(results, list)
        assert len(results) > 0, "Should detect private key"

        secret = results[0]
        assert "Private" in secret["type"] or "RSA" in secret["type"]


def test_detect_secrets_clean_file():
    """
    RED: Test detect-secrets with clean code (no secrets).
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    clean_code = """
# This is clean code
def calculate(x, y):
    return x + y

api_key_placeholder = "YOUR_API_KEY_HERE"
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "clean.py"
        test_file.write_text(clean_code)

        analyzer = DetectSecretsAnalyzer()
        results = analyzer.scan_file(test_file)

        # Should return empty list or minimal false positives
        assert isinstance(results, list)


def test_detect_secrets_multiple_secrets_in_file():
    """
    RED: Test detecting multiple secrets in single file.
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    code_with_multiple = """
aws_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
"""

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "multiple.py"
        test_file.write_text(code_with_multiple)

        analyzer = DetectSecretsAnalyzer()
        results = analyzer.scan_file(test_file)

        # Should find multiple secrets
        assert len(results) >= 2, "Should find at least 2 secrets"


def test_detect_secrets_configurable_plugins():
    """
    RED: Test that plugins can be configured.
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    # Initialize with specific plugins
    config = {
        "plugins": [
            {"name": "AWSKeyDetector"},
            {"name": "PrivateKeyDetector"},
        ]
    }

    analyzer = DetectSecretsAnalyzer(config=config)

    # Should have configured plugins
    assert hasattr(analyzer, "settings") or hasattr(analyzer, "_settings")


def test_detect_secrets_scan_directory():
    """
    RED: Test scanning multiple files in a directory.
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files with secrets
        file1 = Path(tmpdir) / "file1.py"
        file1.write_text('aws_key = "AKIAIOSFODNN7EXAMPLE"')

        file2 = Path(tmpdir) / "file2.py"
        file2.write_text('api_key = "sk-1234567890abcdef"')

        analyzer = DetectSecretsAnalyzer()
        results = analyzer.scan_directory(Path(tmpdir))

        # Should return dict mapping files to secrets
        assert isinstance(results, dict)
        assert len(results) > 0, "Should find secrets in directory"


def test_detect_secrets_handles_binary_files():
    """
    RED: Test graceful handling of binary files.
    """
    from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a binary file
        bin_file = Path(tmpdir) / "binary.dat"
        bin_file.write_bytes(b"\\x00\\x01\\x02\\x03")

        analyzer = DetectSecretsAnalyzer()

        # Should not crash
        try:
            results = analyzer.scan_file(bin_file)
            assert isinstance(results, list)
        except Exception as e:
            # Acceptable to skip binary files
            assert "binary" in str(e).lower() or "decode" in str(e).lower()
