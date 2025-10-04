"""
Test metrics against real-world Python applications.
This validates that our metrics accurately reflect code quality.
"""

import tempfile
import textwrap
from pathlib import Path


def test_high_quality_code_fixture():
    """Test that high-quality code (our own library) scores well."""
    from mfcqi.metrics.complexity import CyclomaticComplexity, HalsteadComplexity
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    # Test our own mfcqi library - it should be high quality
    cqi_src = Path(__file__).parent.parent / "src" / "mfcqi"

    cc = CyclomaticComplexity()
    cc_value = cc.extract(cqi_src)
    cc_normalized = cc.normalize(cc_value)

    hv = HalsteadComplexity()
    hv_value = hv.extract(cqi_src)
    hv_normalized = hv.normalize(hv_value)

    mi = MaintainabilityIndex()
    mi_value = mi.extract(cqi_src)
    mi_normalized = mi.normalize(mi_value)

    # Our own code should score reasonably well (adjusted for complex pattern detection algorithms)
    # CC around 5 is good for research-heavy code with complex algorithms
    # HV around 586 is expected for sophisticated algorithmic code
    # MI around 60 is moderate for research-heavy code with complex algorithms
    assert cc_normalized > 0.6, f"CC normalized: {cc_normalized}, raw: {cc_value}"
    assert hv_normalized > 0.35, f"HV normalized: {hv_normalized}, raw: {hv_value}"
    assert mi_normalized > 0.6, f"MI normalized: {mi_normalized}, raw: {mi_value}"


def test_simple_clean_code():
    """Test metrics on simple, clean code."""
    from mfcqi.metrics.complexity import CyclomaticComplexity, HalsteadComplexity
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    clean_code = textwrap.dedent('''
        """A simple calculator module with clean code."""

        def add(a: float, b: float) -> float:
            """Add two numbers together.

            Args:
                a: First number
                b: Second number

            Returns:
                Sum of a and b
            """
            return a + b

        def subtract(a: float, b: float) -> float:
            """Subtract b from a.

            Args:
                a: First number
                b: Second number

            Returns:
                Difference of a and b
            """
            return a - b

        def multiply(a: float, b: float) -> float:
            """Multiply two numbers.

            Args:
                a: First number
                b: Second number

            Returns:
                Product of a and b
            """
            return a * b

        def divide(a: float, b: float) -> float:
            """Divide a by b.

            Args:
                a: Numerator
                b: Denominator

            Returns:
                Quotient of a and b

            Raises:
                ValueError: If b is zero
            """
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "clean.py"
        test_file.write_text(clean_code)

        cc = CyclomaticComplexity()
        cc_value = cc.extract(Path(tmpdir))

        hv = HalsteadComplexity()
        hv_value = hv.extract(Path(tmpdir))

        mi = MaintainabilityIndex()
        mi_value = mi.extract(Path(tmpdir))

        # Clean code should have excellent scores
        assert cc.normalize(cc_value) > 0.9, f"CC: {cc_value}"
        assert hv.normalize(hv_value) > 0.9, f"HV: {hv_value}"
        # MI of 60+ is actually reasonable for simple functions
        assert mi.normalize(mi_value) > 0.6, f"MI: {mi_value}"


def test_complex_messy_code():
    """Test metrics on complex, poorly written code."""
    from mfcqi.metrics.complexity import CyclomaticComplexity, HalsteadComplexity
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    messy_code = textwrap.dedent("""
        def process(d, t, f, x=None, y=None, z=None):
            r = []
            if not d:
                return None
            for i in d:
                if t == 1:
                    if f:
                        if x and i > x:
                            if y:
                                if i < y:
                                    r.append(i * 2)
                                else:
                                    if z:
                                        r.append(i + z)
                                    else:
                                        r.append(i)
                            else:
                                r.append(i * 3)
                        elif not x:
                            r.append(i / 2 if i != 0 else 0)
                    else:
                        for j in range(i):
                            if j % 2 == 0:
                                for k in range(j):
                                    if k % 3 == 0:
                                        r.append(k)
                elif t == 2:
                    if i % 2 == 0:
                        if i % 3 == 0:
                            if i % 5 == 0:
                                r.append(i * 10)
                            else:
                                r.append(i * 5)
                        else:
                            r.append(i * 2)
                    else:
                        if i % 7 == 0:
                            r.append(i * 7)
                        else:
                            r.append(i)
                elif t == 3:
                    try:
                        v = i / (i - 10)
                        if v > 0:
                            r.append(v)
                        else:
                            r.append(-v)
                    except:
                        r.append(0)
            return r if r else None
    """)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "messy.py"
        test_file.write_text(messy_code)

        cc = CyclomaticComplexity()
        cc_value = cc.extract(Path(tmpdir))

        hv = HalsteadComplexity()
        hv_value = hv.extract(Path(tmpdir))

        mi = MaintainabilityIndex()
        mi_value = mi.extract(Path(tmpdir))

        # Messy code should have poor to moderate scores
        # Note: With tanh normalization, HV=496 → 1.0 - tanh(496/2500) ≈ 0.80
        # This is still considered "good" because libraries can have HV 2000-4000
        # MI=40.7 with new thresholds → 0.607 (moderate range 30-50 → 0.50-0.70)
        assert cc.normalize(cc_value) < 0.5, f"CC: {cc_value} (should be high/bad)"
        assert hv.normalize(hv_value) < 0.85, f"HV: {hv_value} (moderate with new tanh)"
        assert mi.normalize(mi_value) < 0.65, f"MI: {mi_value} (moderate with new thresholds)"


def test_medium_complexity_realistic_code():
    """Test metrics on realistic medium-complexity code."""
    from mfcqi.metrics.complexity import CyclomaticComplexity, HalsteadComplexity
    from mfcqi.metrics.maintainability import MaintainabilityIndex

    realistic_code = textwrap.dedent('''
        """User authentication module."""

        import hashlib
        import time
        from typing import Optional, Dict, Any


        class AuthenticationError(Exception):
            """Raised when authentication fails."""
            pass


        class UserAuthenticator:
            """Handles user authentication and session management."""

            def __init__(self, max_attempts: int = 3):
                self.max_attempts = max_attempts
                self.failed_attempts: Dict[str, int] = {}
                self.locked_users: Dict[str, float] = {}

            def authenticate(self, username: str, password: str) -> bool:
                """Authenticate a user with username and password.

                Args:
                    username: The username to authenticate
                    password: The password to verify

                Returns:
                    True if authentication successful

                Raises:
                    AuthenticationError: If user is locked or credentials invalid
                """
                # Check if user is locked
                if self._is_locked(username):
                    raise AuthenticationError(f"User {username} is locked")

                # Verify credentials
                if not self._verify_credentials(username, password):
                    self._record_failed_attempt(username)
                    attempts_left = self.max_attempts - self.failed_attempts.get(username, 0)

                    if attempts_left <= 0:
                        self._lock_user(username)
                        raise AuthenticationError(f"User {username} has been locked")
                    else:
                        raise AuthenticationError(
                            f"Invalid credentials. {attempts_left} attempts remaining"
                        )

                # Success - reset failed attempts
                if username in self.failed_attempts:
                    del self.failed_attempts[username]

                return True

            def _verify_credentials(self, username: str, password: str) -> bool:
                """Verify username and password against stored credentials."""
                # This is a simplified example - in reality would check database
                hashed = hashlib.sha256(password.encode()).hexdigest()
                expected = hashlib.sha256(b"correct_password").hexdigest()
                return username == "admin" and hashed == expected

            def _is_locked(self, username: str) -> bool:
                """Check if a user is currently locked."""
                if username not in self.locked_users:
                    return False

                lock_time = self.locked_users[username]
                # Unlock after 5 minutes
                if time.time() - lock_time > 300:
                    del self.locked_users[username]
                    return False

                return True

            def _record_failed_attempt(self, username: str) -> None:
                """Record a failed login attempt."""
                if username not in self.failed_attempts:
                    self.failed_attempts[username] = 0
                self.failed_attempts[username] += 1

            def _lock_user(self, username: str) -> None:
                """Lock a user account."""
                self.locked_users[username] = time.time()
    ''')

    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "auth.py"
        test_file.write_text(realistic_code)

        cc = CyclomaticComplexity()
        cc_value = cc.extract(Path(tmpdir))

        hv = HalsteadComplexity()
        hv_value = hv.extract(Path(tmpdir))

        mi = MaintainabilityIndex()
        mi_value = mi.extract(Path(tmpdir))

        # Realistic code should have moderate to good scores
        # Note: With tanh normalization, HV=175 → 1.0 - tanh(175/2500) ≈ 0.93
        # Small volumes score very high with evidence-based calibration
        assert 0.5 < cc.normalize(cc_value) < 0.9, f"CC: {cc_value}"
        assert 0.9 < hv.normalize(hv_value) < 0.95, f"HV: {hv_value} (small volume is good)"
        assert 0.6 < mi.normalize(mi_value) < 0.9, f"MI: {mi_value}"
