"""MFCQI - Multi-Factor Code Quality Index."""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("mfcqi")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.1"  # fallback for development


def hello() -> str:
    return "Hello from mfcqi!"
