"""File utilities for MFCQI - filtering and path management."""

from pathlib import Path

# Directories to exclude from analysis
EXCLUDED_DIRS = {
    ".venv",
    "venv",
    "env",
    ".env",
    "__pycache__",
    ".pytest_cache",
    ".tox",
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    "build",
    "dist",
    ".eggs",
    "*.egg-info",
    ".mypy_cache",
    ".ruff_cache",
    ".coverage",
    "htmlcov",
    "site-packages",
    ".hypothesis",
    ".nox",
}


def get_python_files(codebase: Path, exclude_tests: bool = False) -> list[Path]:
    """Get all Python files in codebase, excluding common non-project directories.

    Args:
        codebase: Root directory to search
        exclude_tests: If True, also exclude test files

    Returns:
        List of Python file paths that should be analyzed
    """
    py_files = []

    for py_file in codebase.rglob("*.py"):
        # Check if any parent directory should be excluded
        should_exclude = False
        for part in py_file.parts:
            if part in EXCLUDED_DIRS or part.startswith("."):
                should_exclude = True
                break

        if should_exclude:
            continue

        # Optionally exclude test files
        if exclude_tests and ("test" in py_file.stem.lower() or "tests" in str(py_file.parent)):
            continue

        py_files.append(py_file)

    # Sort for deterministic ordering
    return sorted(py_files)


def should_analyze_file(file_path: Path) -> bool:
    """Check if a file should be analyzed based on exclusion rules.

    Args:
        file_path: Path to check

    Returns:
        True if file should be analyzed, False if it should be skipped
    """
    return all(not (part in EXCLUDED_DIRS or part.startswith(".")) for part in file_path.parts)
