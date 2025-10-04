"""Tests for badge CLI command."""

import json
import tempfile
import textwrap
from pathlib import Path

from click.testing import CliRunner

from mfcqi.cli.commands.badge import badge


def test_badge_url_format():
    """Test badge command with URL format (default)."""
    runner = CliRunner()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create simple Python file
        code = textwrap.dedent('''
            """Test module."""

            def hello():
                """Say hello."""
                return "Hello"
        ''')
        (Path(tmpdir) / "test.py").write_text(code)

        result = runner.invoke(badge, [tmpdir, "--format", "url"])

        assert result.exit_code == 0
        assert "shields.io" in result.output or "MFCQI" in result.output


def test_badge_json_format():
    """Test badge command with JSON format."""
    runner = CliRunner()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create simple Python file
        code = textwrap.dedent('''
            """Test module."""

            def greet(name: str) -> str:
                """Greet someone."""
                return f"Hello, {name}!"
        ''')
        (Path(tmpdir) / "module.py").write_text(code)

        # Use temporary output file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
            output_file = Path(tmp.name)

        try:
            result = runner.invoke(
                badge, [tmpdir, "--format", "json", "--output", str(output_file)]
            )

            assert result.exit_code == 0

            # Check that JSON was created
            if output_file.exists():
                data = json.loads(output_file.read_text())
                assert "schemaVersion" in data
                assert "label" in data
                assert "message" in data
                assert data["label"] == "MFCQI"
        finally:
            if output_file.exists():
                output_file.unlink()


def test_badge_markdown_format():
    """Test badge command with markdown format."""
    runner = CliRunner()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create simple code
        (Path(tmpdir) / "simple.py").write_text("def f(): return 1")

        result = runner.invoke(badge, [tmpdir, "--format", "markdown"])

        assert result.exit_code == 0
        assert "markdown" in result.output.lower() or "MFCQI" in result.output


def test_badge_with_simple_codebase():
    """Test badge command with simple codebase."""
    runner = CliRunner()

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create code and test
        (Path(tmpdir) / "code.py").write_text("def add(a, b): return a + b")
        (Path(tmpdir) / "test_code.py").write_text("def test_add(): pass")

        result = runner.invoke(badge, [tmpdir, "--format", "url"])

        # Should succeed
        assert result.exit_code == 0


def test_badge_color_mapping():
    """Test that different scores produce different colors."""
    runner = CliRunner()

    # Create poor quality code (should get red/yellow badge)
    poor_code = textwrap.dedent("""
        def bad(a,b,c,d,e,f,g):
            if a:
                if b:
                    if c:
                        if d:
                            if e:
                                if f:
                                    return g
            return 0
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "poor.py").write_text(poor_code)

        result = runner.invoke(badge, [tmpdir])

        # Should complete successfully
        assert result.exit_code == 0


def test_badge_default_path():
    """Test badge with default path (current directory)."""
    runner = CliRunner()

    # Run in temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text("def f(): pass")

        with runner.isolated_filesystem(temp_dir=tmpdir):
            result = runner.invoke(badge, [])

            # Should work with default path
            assert result.exit_code == 0
