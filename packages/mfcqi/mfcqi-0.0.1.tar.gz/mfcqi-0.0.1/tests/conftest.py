"""
Global pytest configuration and fixtures.

This file is automatically loaded by pytest and provides fixtures
and configuration that apply to all tests.
"""

import os
import sys

# CRITICAL: Disable keyring BEFORE any imports of mfcqi modules
# This prevents macOS keychain access during parallel test execution
os.environ["MFCQI_DISABLE_KEYRING"] = "1"

# Also mock at module level before imports
from unittest.mock import MagicMock

sys.modules["keyring"] = MagicMock()
