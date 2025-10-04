"""
Tests for Response for Class (RFC) metric.

RFC = Number of local methods + Number of remote methods called
Tests follow TDD methodology - write failing test first.
"""

from mfcqi.metrics.rfc import RFCMetric


class TestRFCMetric:
    """Test the RFC metric calculation."""

    def setup_method(self):
        """Set up test environment."""
        self.metric = RFCMetric()

    def test_rfc_simple_class_with_one_method(self):
        """Test RFC for class with single method, no external calls."""
        code = """
class SimpleClass:
    def method1(self):
        return 42
"""
        result = self.metric.extract_from_string(code)
        # Expected: 1 local method, 0 remote calls = RFC of 1
        assert result == 1

    def test_rfc_class_with_multiple_methods(self):
        """Test RFC for class with multiple methods, no external calls."""
        code = """
class MultiMethodClass:
    def method1(self):
        return 42

    def method2(self):
        return 24

    def method3(self):
        return 12
"""
        result = self.metric.extract_from_string(code)
        # Expected: 3 local methods, 0 remote calls = RFC of 3
        assert result == 3

    def test_rfc_class_with_remote_calls(self):
        """Test RFC for class with local methods and remote calls."""
        code = """
class ClassWithCalls:
    def __init__(self):
        self.helper = SomeHelper()

    def method1(self):
        return self.helper.calculate()

    def method2(self):
        result = self.helper.process()
        other_obj = OtherClass()
        return other_obj.finalize(result)
"""
        result = self.metric.extract_from_string(code)
        # Expected: 3 local methods (__init__, method1, method2)
        # + 3 remote calls (calculate, process, finalize) = RFC of 6
        assert result == 6

    def test_rfc_nonexistent_path(self):
        """Test RFC with nonexistent path."""
        from pathlib import Path

        result = self.metric.extract(Path("/nonexistent/path"))
        assert result == 0.0

    def test_rfc_file_path_not_directory(self):
        """Test RFC with file path instead of directory."""
        import tempfile
        from pathlib import Path

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(b"class Test:\n    def method(self): pass")

        try:
            result = self.metric.extract(tmp_path)
            assert result == 0.0
        finally:
            tmp_path.unlink()

    def test_rfc_handles_syntax_errors(self):
        """Test RFC handles files with syntax errors gracefully."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            bad_file = Path(tmpdir) / "bad.py"
            bad_file.write_text("class Broken( syntax error")

            good_file = Path(tmpdir) / "good.py"
            good_file.write_text("class Good:\n    def method(self): pass")

            result = self.metric.extract(Path(tmpdir))
            assert result >= 0.0

    def test_rfc_syntax_error_in_string(self):
        """Test RFC handles syntax error in extract_from_string."""
        code = "class Broken( syntax error"
        result = self.metric.extract_from_string(code)
        assert result == 0

    def test_rfc_normalize(self):
        """Test RFC normalize method with library-aware piecewise thresholds."""
        import pytest

        # RFC <= 15: Excellent (simple, focused classes)
        assert self.metric.normalize(5.0) == 1.0
        assert self.metric.normalize(10.0) == 1.0
        assert self.metric.normalize(15.0) == 1.0

        # RFC 30: Good (library-appropriate, ~0.89)
        # RFC=30: 1.0 - 0.25 * (30-15)/35 ≈ 0.893
        result_30 = self.metric.normalize(30.0)
        assert 0.88 < result_30 < 0.91

        # RFC 50: Library threshold (0.75)
        result_50 = self.metric.normalize(50.0)
        assert result_50 == pytest.approx(0.75, abs=0.01)

        # RFC 100: Complex but acceptable (0.35)
        result_100 = self.metric.normalize(100.0)
        assert result_100 == pytest.approx(0.35, abs=0.01)

        # RFC 120: God object threshold (0.0)
        assert self.metric.normalize(120.0) == pytest.approx(0.0, abs=0.01)

        # RFC > 120: Definite god object (0.0)
        assert self.metric.normalize(150.0) == 0.0

    def test_rfc_get_weight(self):
        """Test RFC get_weight method."""
        weight = self.metric.get_weight()
        assert weight == 0.65

    def test_rfc_empty_directory(self):
        """Test RFC with empty directory."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            result = self.metric.extract(Path(tmpdir))
            assert result == 0.0
