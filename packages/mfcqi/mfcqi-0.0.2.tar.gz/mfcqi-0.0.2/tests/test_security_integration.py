"""
Test integration of SecurityMetric with MFCQICalculator.
"""


def test_security_metric_standalone():
    """Test that security metric can be used standalone."""
    import tempfile
    from pathlib import Path

    from mfcqi.metrics.security import SecurityMetric

    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = Path(tmpdir)
        # Create vulnerable code
        test_file = test_dir / "app.py"
        test_file.write_text("""
import os

def execute(cmd):
    os.system(cmd)  # Security vulnerability

def safe_add(a, b):
    return a + b
""")

        # Use security metric directly
        metric = SecurityMetric()
        density = metric.extract(test_dir)
        score = metric.normalize(density)

        # Should detect vulnerability
        assert density > 0.0
        assert score < 1.0
        assert 0.0 <= score <= 1.0


def test_security_metric_in_mfcqi_calculator():
    """Test that SecurityMetric is included in MFCQI calculation."""
    import tempfile
    from pathlib import Path

    from mfcqi.calculator import MFCQICalculator

    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = Path(tmpdir)

        # Create code with security vulnerabilities
        test_file = test_dir / "vulnerable.py"
        test_file.write_text("""
import os
import pickle

def execute(cmd):
    os.system(cmd)  # B605: Command injection vulnerability

def load_data(data):
    return pickle.loads(data)  # B301: Deserialization vulnerability

password = "admin123"  # B105: Hardcoded password
""")

        # Create calculator
        calculator = MFCQICalculator()

        # Check that security is in core metrics
        assert "security" in calculator.core_metrics

        # Get detailed metrics
        detailed = calculator.get_detailed_metrics(test_dir)

        # Security metric should be calculated
        assert "security" in detailed
        security_score = detailed["security"]

        # Should detect vulnerabilities and have a lower score
        assert 0.0 <= security_score < 1.0
        assert security_score < 0.8  # Should be penalized for vulnerabilities

        # MFCQI score should include security
        mfcqi_score = calculator.calculate(test_dir)
        assert 0.0 <= mfcqi_score <= 1.0

        # MFCQI should be affected by poor security
        # Create same code without vulnerabilities
        safe_dir = Path(tmpdir) / "safe"
        safe_dir.mkdir()
        safe_file = safe_dir / "safe.py"
        safe_file.write_text("""
def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def process_data(data):
    return data.upper()
""")

        safe_score = calculator.calculate(safe_dir)
        safe_detailed = calculator.get_detailed_metrics(safe_dir)

        # Safe code should have better security score
        assert safe_detailed["security"] > security_score
        # And better overall MFCQI score (all else being similar)
        assert safe_score > mfcqi_score
