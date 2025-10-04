"""
Tests for Method Hiding Factor (MHF) metric.

MHF = Number of private methods / Total number of methods
Tests follow TDD methodology - write failing test first.
"""

from mfcqi.metrics.mhf import MHFMetric


class TestMHFMetric:
    """Test the MHF metric calculation."""

    def setup_method(self):
        """Set up test environment."""
        self.metric = MHFMetric()

    def test_mhf_class_with_only_public_methods(self):
        """Test MHF for class with only public methods."""
        code = """
class PublicClass:
    def public_method1(self):
        return 42

    def public_method2(self):
        return 24
"""
        result = self.metric.extract_from_string(code)
        # Expected: 0 private methods / 2 total methods = MHF of 0.0
        assert result == 0.0

    def test_mhf_class_with_mixed_methods(self):
        """Test MHF for class with both public and private methods."""
        code = """
class MixedClass:
    def public_method(self):
        return self._private_helper()

    def _private_helper(self):
        return 42

    def __dunder_method__(self):
        return "dunder"

    def another_public(self):
        return 24
"""
        result = self.metric.extract_from_string(code)
        # Expected: 1 private method (_private_helper) / 4 total methods = MHF of 0.25
        assert result == 0.25

    def test_mhf_class_with_only_private_methods(self):
        """Test MHF for class with only private methods."""
        code = """
class PrivateClass:
    def _helper1(self):
        return 1

    def _helper2(self):
        return 2

    def _internal_process(self):
        return self._helper1() + self._helper2()
"""
        result = self.metric.extract_from_string(code)
        # Expected: 3 private methods / 3 total methods = MHF of 1.0
        assert result == 1.0

    def test_mhf_nonexistent_path(self):
        """Test MHF with nonexistent path."""
        from pathlib import Path

        result = self.metric.extract(Path("/nonexistent/path"))
        assert result == 0.0

    def test_mhf_file_path_not_directory(self):
        """Test MHF with file path instead of directory."""
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

    def test_mhf_handles_syntax_errors(self):
        """Test MHF handles files with syntax errors gracefully."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            bad_file = Path(tmpdir) / "bad.py"
            bad_file.write_text("class Broken( syntax error")

            good_file = Path(tmpdir) / "good.py"
            good_file.write_text("class Good:\n    def _hidden(self): pass")

            result = self.metric.extract(Path(tmpdir))
            assert result >= 0.0

    def test_mhf_syntax_error_in_string(self):
        """Test MHF handles syntax error in extract_from_string."""
        code = "class Broken( syntax error"
        result = self.metric.extract_from_string(code)
        assert result == 0.0

    def test_mhf_normalize(self):
        """Test MHF normalize method."""
        result = self.metric.normalize(0.5)
        # Current implementation returns the value as-is
        assert result == 0.5

    def test_mhf_get_weight(self):
        """Test MHF get_weight method."""
        weight = self.metric.get_weight()
        assert weight == 0.55

    def test_mhf_empty_directory(self):
        """Test MHF with empty directory."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            result = self.metric.extract(Path(tmpdir))
            assert result == 0.0
