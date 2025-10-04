"""
Tests for Secrets Exposure metric using detect-secrets.
"""

import tempfile
from pathlib import Path


def test_metric_exists():
    """Test that SecretsExposureMetric class exists."""
    from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

    metric = SecretsExposureMetric()
    assert metric is not None
    assert metric.get_name() == "Secrets Exposure"


def test_no_secrets_perfect_score():
    """Test that codebase with no secrets scores 1.0."""
    from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

    metric = SecretsExposureMetric()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create clean Python file
        test_file = Path(tmpdir) / "clean.py"
        test_file.write_text('def foo():\n    return "hello"\n')

        raw_score = metric.extract(Path(tmpdir))
        normalized = metric.normalize(raw_score)
        assert raw_score == 0.0
        assert normalized == 1.0


def test_one_secret_severe_penalty():
    """Test that one exposed secret severely penalizes score."""
    from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

    metric = SecretsExposureMetric()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create file with private key (detected by PrivateKeyDetector)
        test_file = Path(tmpdir) / "config.py"
        test_file.write_text(
            '''
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF/IqWX9u1u7cKuwqHMX1YxGWNzO0
-----END RSA PRIVATE KEY-----"""
'''
        )

        raw_score = metric.extract(Path(tmpdir))
        normalized = metric.normalize(raw_score)

        # Should detect at least one secret
        assert raw_score >= 1.0
        # Score should be severely penalized
        assert normalized <= 0.3


def test_multiple_secrets_critical_failure():
    """Test that multiple secrets result in critical failure."""
    from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

    metric = SecretsExposureMetric()

    # Test normalization directly
    assert metric.normalize(0.0) == 1.0  # No secrets = perfect
    assert metric.normalize(1.0) == 0.3  # 1 secret = severe penalty
    assert metric.normalize(2.0) == 0.1  # 2 secrets = critical
    assert metric.normalize(3.0) == 0.1  # 3 secrets = critical
    assert metric.normalize(4.0) == 0.0  # 4+ secrets = complete failure


def test_test_files_excluded():
    """Test that secrets in test files are not counted."""
    from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

    metric = SecretsExposureMetric()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test file with private key (should be ignored)
        test_file = Path(tmpdir) / "test_config.py"
        test_file.write_text(
            '''PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF/IqWX9u1u7cKuwqHMX1YxGWNzO0
-----END RSA PRIVATE KEY-----"""
'''
        )

        # Create example file with private key (should be ignored)
        example_file = Path(tmpdir) / "config.example.py"
        example_file.write_text(
            '''PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF/IqWX9u1u7cKuwqHMX1YxGWNzO0
-----END RSA PRIVATE KEY-----"""
'''
        )

        raw_score = metric.extract(Path(tmpdir))
        normalized = metric.normalize(raw_score)

        # Should not count test/example files
        assert raw_score == 0.0
        assert normalized == 1.0


def test_metric_weight():
    """Test that weight is 0.85 based on research."""
    from mfcqi.metrics.secrets_exposure import SecretsExposureMetric

    metric = SecretsExposureMetric()
    assert metric.get_weight() == 0.85
