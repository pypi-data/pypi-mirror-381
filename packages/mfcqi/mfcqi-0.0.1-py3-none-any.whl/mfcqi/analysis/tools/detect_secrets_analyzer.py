"""
detect-secrets analyzer for finding secrets in code.

Uses detect_secrets Python API directly - NO subprocess.

detect_secrets provides these APIs:
- detect_secrets.core.scan.scan_file: Scan individual files
- detect_secrets.settings.get_settings: Get/configure global settings
- detect_secrets.settings.Settings.configure_plugins: Configure which detectors to use

NOTE: detect-secrets is an optional dependency. If not installed, this analyzer
will gracefully degrade and return empty results.
"""

from pathlib import Path
from typing import Any


class DetectSecretsAnalyzer:
    """Analyzer for detecting secrets (API keys, passwords, tokens) in code.

    Requires detect-secrets package to be installed. If not available, gracefully
    degrades and returns empty results.
    """

    def __init__(self, config: dict[str, Any] | None = None):
        """Initialize detect-secrets analyzer with optional configuration.

        Args:
            config: Optional configuration dict with 'plugins' key
        """
        self.config = config or {}
        self._available = False
        self.settings = None

        # Lazy import detect_secrets - don't crash if not installed
        try:
            from detect_secrets.settings import get_settings

            # Configure settings and plugins
            self.settings = get_settings()

            # Get plugins from config or use defaults
            plugins = self.config.get(
                "plugins",
                [
                    {"name": "AWSKeyDetector"},
                    {"name": "ArtifactoryDetector"},
                    {"name": "AzureStorageKeyDetector"},
                    {"name": "Base64HighEntropyString"},
                    {"name": "BasicAuthDetector"},
                    {"name": "CloudantDetector"},
                    {"name": "DiscordBotTokenDetector"},
                    {"name": "GitHubTokenDetector"},
                    {"name": "JwtTokenDetector"},
                    {"name": "MailchimpDetector"},
                    {"name": "NpmDetector"},
                    {"name": "PrivateKeyDetector"},
                    {"name": "SendGridDetector"},
                    {"name": "SlackDetector"},
                    {"name": "SoftlayerDetector"},
                    {"name": "SquareOAuthDetector"},
                    {"name": "StripeDetector"},
                    {"name": "TwilioKeyDetector"},
                ],
            )

            # Configure plugins
            self.settings.configure_plugins(plugins)
            self._available = True

        except ImportError:
            # detect-secrets not installed - graceful degradation
            pass

    def scan_file(self, file_path: Path) -> list[dict[str, Any]]:
        """
        Scan a single file for secrets using detect_secrets Python API.

        Args:
            file_path: Path to file to scan

        Returns:
            List of detected secrets with details.
            Returns empty list if detect-secrets not available.
        """
        # Check if detect-secrets is available
        if not self._available:
            return []

        try:
            # Lazy import for scan
            from detect_secrets.core import scan

            # Check file exists
            if not file_path.exists():
                return []

            # Scan using Python API (NO subprocess)
            secrets = list(scan.scan_file(str(file_path)))

            # Convert to our format
            results = []
            for secret in secrets:
                results.append(
                    {
                        "type": secret.type,
                        "line_number": secret.line_number,
                        "filename": str(file_path),
                        "secret_hash": secret.secret_hash,
                    }
                )

            return results

        except Exception:
            # Return empty list on error (graceful degradation)
            return []

    def scan_directory(self, directory: Path) -> dict[str, list[dict[str, Any]]]:
        """
        Scan all files in a directory for secrets.

        Args:
            directory: Directory to scan

        Returns:
            Dictionary mapping filenames to lists of secrets.
            Returns empty dict if detect-secrets not available.
        """
        # Check if detect-secrets is available
        if not self._available:
            return {}

        results = {}

        # Find all files (excluding common non-code files)
        for file_path in directory.rglob("*"):
            # Skip directories and common non-code files
            if file_path.is_dir():
                continue

            # Skip binary and non-text files
            if file_path.suffix in [".pyc", ".so", ".dll", ".exe", ".bin"]:
                continue

            # Scan the file
            file_secrets = self.scan_file(file_path)

            if file_secrets:
                results[str(file_path)] = file_secrets

        return results
