"""Main entry point for MFCQI CLI when run as python -m mfcqi."""

import warnings

from mfcqi.cli.main import cli

# Suppress unhelpful warnings from dependencies
warnings.filterwarnings("ignore", category=SyntaxWarning, module="<unknown>")
warnings.filterwarnings("ignore", message="invalid escape sequence")

if __name__ == "__main__":
    cli()
