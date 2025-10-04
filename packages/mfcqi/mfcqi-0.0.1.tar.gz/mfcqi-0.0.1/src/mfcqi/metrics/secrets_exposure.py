"""
Secrets Exposure metric using detect-secrets for scanning exposed credentials.

Detects hardcoded secrets (API keys, passwords, tokens, private keys) in
source code using entropy-based and pattern-based detection.

Research Foundation:
    - OWASP Top 10 2021: A07 - Identification and Authentication Failures
    - GitGuardian 2024: 12.8M secrets leaked on GitHub (2024 alone)
    - GitHub Secret Scanning: 2.7M valid secrets prevented from being published
    - Verizon DBIR 2024: 15% of breaches involved use of stolen credentials

Secrets Sprawl Impact:
    - 90% of exposed secrets remain active >5 days after detection
    - Only 2.6% revoked within first hour of discovery
    - Average remediation time: 27 days (GitGuardian 2024)
    - Mean cost per exposed credential: $150 (Ponemon Institute 2023)
    - Credential stuffing: 3.4 billion attacks in Q1 2024 alone

Implementation:
    - Uses detect-secrets Python API with 18 detector plugins
    - Scans all text files for secrets patterns and high-entropy strings
    - Filters test files (test_*, *example*, fixtures) to reduce false positives
    - Severe penalty scoring: ANY secret is critical failure

References:
    [1] OWASP (2021). "A07:2021 - Identification and Authentication Failures"
    [2] GitGuardian (2024). "State of Secrets Sprawl Report 2024"
    [3] GitHub (2024). "Secret Scanning Annual Report"
    [4] Verizon (2024). "Data Breach Investigations Report"
    [5] Ponemon Institute (2023). "Cost of Credential Compromise"
"""

from pathlib import Path
from typing import Any, Union, cast

from mfcqi.analysis.tools.detect_secrets_analyzer import DetectSecretsAnalyzer
from mfcqi.core.metric import Metric


class SecretsExposureMetric(Metric):
    """Detects exposed secrets in source code using detect-secrets.

    Implements zero-tolerance approach to credential exposure. Even a single
    exposed secret represents critical security failure requiring immediate
    remediation.

    Normalization Strategy:
        - 0 secrets → 1.0 (perfect security)
        - 1 secret → 0.3 (severe penalty - 70% score reduction)
        - 2-3 secrets → 0.1 (critical penalty - 90% reduction)
        - 4+ secrets → 0.0 (complete failure - unacceptable)

    Rationale for Highest Weight (0.85):
        - Direct path to data breach (no exploit required)
        - Immediate access to production systems/data
        - Cannot be patched - must revoke and rotate
        - Permanent exposure in git history
        - Automated credential harvesting by bots (<5 min detection)
        - Single API key can compromise entire organization

    Detection Coverage:
        - AWS/Azure/GCP credentials
        - GitHub/GitLab tokens
        - Private keys (RSA, SSH, PGP)
        - Database connection strings
        - High-entropy strings (Base64)
        - API keys (Stripe, Twilio, SendGrid, etc.)
    """

    def extract(self, codebase: Path) -> float:
        """
        Count number of exposed secrets.

        Filters out test files and example configs to avoid false positives.

        Returns:
            Number of exposed secrets (0.0 = no secrets)
        """
        analyzer = DetectSecretsAnalyzer()

        # Scan entire codebase
        results = analyzer.scan_directory(codebase)

        # Filter out test files and example configs
        real_secrets_count = 0

        for filename, secrets in results.items():
            # Skip test files and examples
            if any(
                pattern in filename
                for pattern in ["test_", "example.", ".example", "fixture", "/tests/"]
            ):
                continue

            # Count secrets from this file
            real_secrets_count += len(secrets)

        return float(real_secrets_count)

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """
        Normalize secrets count to [0,1] range.

        Any secret = severe penalty. Multiple secrets = critical failure.

        Scoring:
        - 0 secrets: 1.0 (perfect)
        - 1 secret: 0.3 (severe penalty)
        - 2-3 secrets: 0.1 (critical penalty)
        - 4+ secrets: 0.0 (complete failure)

        Args:
            value: Number of secrets from extract()

        Returns:
            Normalized score where 1.0 = no secrets
        """
        value = cast("float", value)

        if value == 0:
            return 1.0
        elif value == 1:
            return 0.3  # Severe penalty for 1 secret
        elif value <= 3:
            return 0.1  # Critical penalty for 2-3 secrets
        else:
            return 0.0  # Complete failure for 4+ secrets

    def get_weight(self) -> float:
        """
        Return evidence-based weight for secrets exposure.

        Weight: 0.85

        Rationale: Exposed secrets lead directly to data breaches.
        Even one leaked API key can compromise entire systems.

        Evidence:
        - GitGuardian 2024: 39M secrets leaked on GitHub in 2024
        - 90% of exposed secrets remain active >5 days after notification
        - Only 2.6% of secrets revoked within first hour
        - Average time to remediate: 27 days

        References:
        [1] GitGuardian (2024). "State of Secrets Sprawl Report 2024"
        [2] OWASP (2021). "A07:2021 - Identification and Authentication Failures"
        """
        return 0.85

    def get_name(self) -> str:
        """Return the name of this metric."""
        return "Secrets Exposure"
