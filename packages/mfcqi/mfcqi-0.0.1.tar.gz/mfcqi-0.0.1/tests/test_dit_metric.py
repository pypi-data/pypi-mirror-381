"""
Tests for Depth of Inheritance Tree (DIT) metric.

DIT = Maximum inheritance path from class to root
Tests follow TDD methodology - write failing test first.
"""

from mfcqi.metrics.dit import DITMetric


class TestDITMetric:
    """Test the DIT metric calculation."""

    def setup_method(self):
        """Set up test environment."""
        self.metric = DITMetric()

    def test_dit_class_with_no_inheritance(self):
        """Test DIT for class with no inheritance."""
        code = """
class SimpleClass:
    def method1(self):
        return 42
"""
        result = self.metric.extract_from_string(code)
        # Expected: No inheritance = DIT of 0
        assert result == 0

    def test_dit_class_with_single_inheritance(self):
        """Test DIT for class with single level inheritance."""
        code = """
class BaseClass:
    def base_method(self):
        return "base"

class ChildClass(BaseClass):
    def child_method(self):
        return "child"
"""
        result = self.metric.extract_from_string(code)
        # Expected: ChildClass inherits from BaseClass = DIT of 1
        assert result == 1

    def test_dit_class_with_multiple_inheritance_levels(self):
        """Test DIT for class with multiple inheritance levels."""
        code = """
class GrandParent:
    def grandparent_method(self):
        return "grandparent"

class Parent(GrandParent):
    def parent_method(self):
        return "parent"

class Child(Parent):
    def child_method(self):
        return "child"

class GreatGrandChild(Child):
    def great_grandchild_method(self):
        return "great_grandchild"
"""
        result = self.metric.extract_from_string(code)
        # Expected: GreatGrandChild -> Child -> Parent -> GrandParent = DIT of 3
        assert result == 3

    def test_dit_nonexistent_path(self):
        """Test DIT with nonexistent path."""
        from pathlib import Path

        result = self.metric.extract(Path("/nonexistent/path"))
        # Nonexistent path should return 0
        assert result == 0.0

    def test_dit_file_path_not_directory(self):
        """Test DIT with file path instead of directory."""
        import tempfile
        from pathlib import Path

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(b"class Test: pass")

        try:
            result = self.metric.extract(tmp_path)
            # File path (not directory) should return 0
            assert result == 0.0
        finally:
            tmp_path.unlink()

    def test_dit_handles_syntax_errors(self):
        """Test that DIT handles files with syntax errors gracefully."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create file with syntax error
            bad_file = Path(tmpdir) / "bad.py"
            bad_file.write_text("class Broken( syntax error")

            # Create valid file
            good_file = Path(tmpdir) / "good.py"
            good_file.write_text("class Base: pass\nclass Child(Base): pass")

            result = self.metric.extract(Path(tmpdir))
            # Should process good file and skip bad file
            assert result == 1.0

    def test_dit_handles_unicode_errors(self):
        """Test that DIT handles files with unicode decode errors."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create file with invalid UTF-8
            bad_file = Path(tmpdir) / "bad.py"
            bad_file.write_bytes(b"\xff\xfe class Test: pass")

            # Create valid file
            good_file = Path(tmpdir) / "good.py"
            good_file.write_text("class Good: pass")

            result = self.metric.extract(Path(tmpdir))
            # Should handle gracefully
            assert result >= 0.0

    def test_dit_syntax_error_in_string(self):
        """Test DIT handles syntax error in extract_from_string."""
        code = "class Broken( syntax error"
        result = self.metric.extract_from_string(code)
        # Should return 0 for syntax error
        assert result == 0

    def test_dit_normalize(self):
        """Test DIT normalize method with Python multi-paradigm research-backed thresholds."""
        import pytest

        # DIT = 0-3: Excellent for Python (procedural/shallow OO)
        assert self.metric.normalize(0.0) == pytest.approx(1.0)
        assert self.metric.normalize(1.0) == pytest.approx(1.0)
        assert self.metric.normalize(2.0) == pytest.approx(1.0)
        assert self.metric.normalize(3.0) == pytest.approx(1.0)

        # DIT = 4-6: Framework-appropriate (linear decay)
        # DIT = 4: 0.9 (frameworks commonly have DIT=4)
        assert self.metric.normalize(4.0) == pytest.approx(0.9, abs=0.01)
        # DIT = 5: 0.8
        assert self.metric.normalize(5.0) == pytest.approx(0.8, abs=0.01)
        # DIT = 6: 0.7
        assert self.metric.normalize(6.0) == pytest.approx(0.7, abs=0.01)

        # DIT = 7-10: Getting deep (decay continues)
        # DIT = 10: 0.4
        assert self.metric.normalize(10.0) == pytest.approx(0.4, abs=0.01)

        # DIT >= 15: Very deep (0.0)
        assert self.metric.normalize(15.0) == pytest.approx(0.0, abs=0.01)
        assert self.metric.normalize(20.0) == pytest.approx(0.0, abs=0.01)

    def test_dit_get_weight(self):
        """Test DIT get_weight method."""
        weight = self.metric.get_weight()
        # Should return 0.6 based on documentation
        assert weight == 0.6

    def test_dit_empty_directory(self):
        """Test DIT with empty directory."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            result = self.metric.extract(Path(tmpdir))
            # Empty directory should return 0
            assert result == 0.0
