"""
Test for Code Duplication metric - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import tempfile
import textwrap
from pathlib import Path


def test_code_duplication_exists():
    """RED: Test that CodeDuplication class exists."""
    from mfcqi.metrics.duplication import CodeDuplication

    assert CodeDuplication is not None


def test_code_duplication_is_metric():
    """RED: Test that CodeDuplication implements Metric interface."""
    from mfcqi.core.metric import Metric
    from mfcqi.metrics.duplication import CodeDuplication

    assert issubclass(CodeDuplication, Metric)


def test_no_duplication():
    """RED: Test code with no duplication."""
    from mfcqi.metrics.duplication import CodeDuplication

    code = textwrap.dedent("""
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def multiply(a, b):
            return a * b
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = CodeDuplication()
        result = metric.extract(Path(tmpdir))

        # No duplication should return 0 or very low value
        assert result < 5.0


def test_obvious_duplication():
    """RED: Test code with obvious duplication."""
    from mfcqi.metrics.duplication import CodeDuplication

    code = textwrap.dedent("""
        def process_user_data(user):
            if user.age < 0:
                raise ValueError("Age cannot be negative")
            if user.age > 150:
                raise ValueError("Age cannot be greater than 150")

            user_info = {
                'name': user.name,
                'age': user.age,
                'email': user.email
            }

            return user_info

        def process_admin_data(admin):
            if admin.age < 0:
                raise ValueError("Age cannot be negative")
            if admin.age > 150:
                raise ValueError("Age cannot be greater than 150")

            admin_info = {
                'name': admin.name,
                'age': admin.age,
                'email': admin.email
            }

            return admin_info
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text(code)

        metric = CodeDuplication()
        result = metric.extract(Path(tmpdir))

        # Obvious duplication should return higher value
        assert result > 20.0


def test_duplication_across_files():
    """RED: Test duplication detection across multiple files."""
    from mfcqi.metrics.duplication import CodeDuplication

    file1 = textwrap.dedent("""
        def calculate_area(length, width):
            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive")
            return length * width
    """)

    file2 = textwrap.dedent("""
        def compute_area(length, width):
            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive")
            return length * width
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "file1.py").write_text(file1)
        (Path(tmpdir) / "file2.py").write_text(file2)

        metric = CodeDuplication()
        result = metric.extract(Path(tmpdir))

        # Should detect duplication across files
        assert result > 15.0


def test_duplication_normalize():
    """RED: Test normalization of duplication values to [0,1] range."""
    from mfcqi.metrics.duplication import CodeDuplication

    metric = CodeDuplication()

    # 0% duplication (best) should normalize to 1.0
    assert metric.normalize(0.0) == 1.0

    # Low duplication (5%) should normalize to high value (>0.8)
    assert metric.normalize(5.0) > 0.8

    # Medium duplication (15%) should normalize to medium value (~0.5)
    assert 0.4 <= metric.normalize(15.0) <= 0.6

    # High duplication (30%) should normalize to low value (<0.2)
    assert metric.normalize(30.0) < 0.2

    # All normalized values should be in [0,1]
    for duplication in [0, 5, 10, 15, 20, 30, 50]:
        normalized = metric.normalize(float(duplication))
        assert 0.0 <= normalized <= 1.0


def test_duplication_name():
    """RED: Test that metric returns its name."""
    from mfcqi.metrics.duplication import CodeDuplication

    metric = CodeDuplication()
    name = metric.get_name()

    assert name == "Code Duplication"
    assert isinstance(name, str)


def test_duplication_empty_directory():
    """RED: Test duplication with no Python files."""
    from mfcqi.metrics.duplication import CodeDuplication

    with tempfile.TemporaryDirectory() as tmpdir:
        metric = CodeDuplication()
        result = metric.extract(Path(tmpdir))

        # Should return 0% duplication for empty projects
        assert result == 0.0
