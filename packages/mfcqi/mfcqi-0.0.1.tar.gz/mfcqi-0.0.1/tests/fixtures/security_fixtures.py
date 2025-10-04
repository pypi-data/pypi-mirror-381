"""
Security test fixtures for different paradigms and vulnerability levels.
"""

from pathlib import Path
from typing import Dict


def create_procedural_no_vulnerabilities(base_dir: Path) -> None:
    """Create procedural code with no security issues."""
    script = base_dir / "data_processor.py"
    script.write_text('''#!/usr/bin/env python3
"""Safe data processing script."""

import json
import hashlib
from typing import Any, Dict, List


def load_config(filename: str) -> Dict[str, Any]:
    """Safely load configuration from JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)


def hash_password(password: str, salt: str) -> str:
    """Securely hash a password with salt."""
    return hashlib.pbkdf2_hmac('sha256',
                              password.encode('utf-8'),
                              salt.encode('utf-8'),
                              100000)


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process data items safely."""
    results = []
    for item in data:
        if validate_item(item):
            results.append(transform_item(item))
    return results


def validate_item(item: Dict[str, Any]) -> bool:
    """Validate a data item."""
    required_fields = ['id', 'name', 'value']
    return all(field in item for field in required_fields)


def transform_item(item: Dict[str, Any]) -> Dict[str, Any]:
    """Transform a data item."""
    return {
        'id': item['id'],
        'display_name': item['name'].upper(),
        'processed_value': item['value'] * 2
    }


def main():
    """Main entry point."""
    config = load_config('config.json')
    data = config.get('data', [])
    results = process_data(data)

    with open('output.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Processed {len(results)} items")


if __name__ == '__main__':
    main()
''')


def create_procedural_high_vulnerabilities(base_dir: Path) -> None:
    """Create procedural code with many security issues."""
    script = base_dir / "vulnerable_script.py"
    script.write_text('''#!/usr/bin/env python3
"""Script with multiple security vulnerabilities."""

import os
import pickle
import subprocess
import sqlite3
import requests
from typing import Any

# B105: Hardcoded password
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"  # B105: Hardcoded API key


def execute_command(user_input: str) -> str:
    """B605, B602: Shell injection vulnerability."""
    # Dangerous: directly executing user input
    result = os.system(user_input)

    # Also dangerous: using shell=True
    output = subprocess.check_output(user_input, shell=True)
    return output.decode()


def load_user_data(filename: str) -> Any:
    """B301: Pickle deserialization vulnerability."""
    with open(filename, 'rb') as f:
        # Dangerous: unpickling untrusted data
        return pickle.load(f)


def query_database(user_id: str) -> list:
    """B608: SQL injection vulnerability."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Dangerous: string formatting in SQL
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)

    return cursor.fetchall()


def download_file(url: str) -> bytes:
    """B113: Request without timeout."""
    # Missing timeout can cause DoS
    response = requests.get(url)  # No timeout specified
    return response.content


def weak_random_token() -> str:
    """B311: Weak random number generator."""
    import random
    # Dangerous: predictable random for security
    return str(random.randint(1000, 9999))


def eval_math_expression(expr: str) -> Any:
    """B307: Use of eval - arbitrary code execution."""
    # Extremely dangerous: eval on user input
    return eval(expr)


def insecure_temp_file(data: str) -> None:
    """B108, B306: Insecure temp file creation."""
    import tempfile
    # Dangerous: predictable temp file
    temp = tempfile.mktemp()
    with open(temp, 'w') as f:
        f.write(data)


def use_md5_hash(data: str) -> str:
    """B303, B324: Use of insecure hash function."""
    import hashlib
    # Weak: MD5 is cryptographically broken
    return hashlib.md5(data.encode()).hexdigest()


# B103: Permissive file permissions
os.chmod('/tmp/important.txt', 0o777)

# B104: Binding to all interfaces
SERVER_HOST = '0.0.0.0'  # Dangerous: listens on all interfaces


def main():
    """Main with multiple vulnerabilities."""
    user_cmd = input("Enter command: ")
    execute_command(user_cmd)

    user_file = input("Enter pickle file: ")
    data = load_user_data(user_file)

    user_id = input("Enter user ID: ")
    users = query_database(user_id)

    print(f"Found {len(users)} users")
    print(f"Token: {weak_random_token()}")


if __name__ == '__main__':
    # B603: Subprocess without shell equals true
    subprocess.Popen(['ls', '-la'], shell=False)  # This one is actually OK
    main()
''')


def create_oo_no_vulnerabilities(base_dir: Path) -> None:
    """Create OO code with no security issues."""
    app = base_dir / "secure_app.py"
    app.write_text('''"""Secure object-oriented application."""

import hashlib
import hmac
import json
import secrets
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class User:
    """User model with secure practices."""

    id: str
    username: str
    email: str
    _password_hash: Optional[str] = None

    def set_password(self, password: str) -> None:
        """Securely hash and store password."""
        salt = secrets.token_bytes(32)
        self._password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        ).hex()

    def verify_password(self, password: str) -> bool:
        """Securely verify password."""
        if not self._password_hash:
            return False
        # In real app, would extract salt from hash
        return hmac.compare_digest(
            self._password_hash,
            hashlib.sha256(password.encode()).hexdigest()
        )


class DataValidator:
    """Validates data with security in mind."""

    ALLOWED_FIELDS = {'name', 'email', 'age', 'country'}
    MAX_STRING_LENGTH = 1000

    @classmethod
    def validate_input(cls, data: Dict[str, Any]) -> bool:
        """Validate untrusted input data."""
        if not isinstance(data, dict):
            return False

        # Check for unexpected fields
        if not set(data.keys()).issubset(cls.ALLOWED_FIELDS):
            return False

        # Validate string lengths
        for key, value in data.items():
            if isinstance(value, str) and len(value) > cls.MAX_STRING_LENGTH:
                return False

        return True

    @classmethod
    def sanitize_string(cls, text: str) -> str:
        """Sanitize string for safe output."""
        # Remove control characters
        return ''.join(char for char in text if ord(char) >= 32)


class SecureStorage(ABC):
    """Abstract base for secure storage."""

    @abstractmethod
    def store(self, key: str, value: Any) -> None:
        """Store data securely."""
        pass

    @abstractmethod
    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve data securely."""
        pass


class JSONStorage(SecureStorage):
    """JSON-based secure storage implementation."""

    def __init__(self, filepath: str):
        """Initialize with filepath."""
        self.filepath = filepath
        self._data: Dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        """Load data from file safely."""
        try:
            with open(self.filepath, 'r') as f:
                self._data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._data = {}

    def store(self, key: str, value: Any) -> None:
        """Store data with validation."""
        if not isinstance(key, str) or len(key) > 100:
            raise ValueError("Invalid key")

        # Validate value is JSON-serializable
        try:
            json.dumps(value)
        except (TypeError, ValueError):
            raise ValueError("Value must be JSON-serializable")

        self._data[key] = value
        self._save()

    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve data safely."""
        return self._data.get(key)

    def _save(self) -> None:
        """Save data to file securely."""
        with open(self.filepath, 'w') as f:
            json.dump(self._data, f, indent=2)


class SecureApplication:
    """Main application class with security focus."""

    def __init__(self):
        """Initialize secure application."""
        self.storage = JSONStorage('data.json')
        self.validator = DataValidator()
        self.users: List[User] = []

    def create_user(self, username: str, email: str, password: str) -> User:
        """Create user with secure defaults."""
        # Generate cryptographically secure ID
        user_id = secrets.token_urlsafe(16)

        user = User(
            id=user_id,
            username=self.validator.sanitize_string(username),
            email=self.validator.sanitize_string(email)
        )
        user.set_password(password)

        self.users.append(user)
        return user

    def process_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process request with validation."""
        if not self.validator.validate_input(data):
            return {'error': 'Invalid input data'}

        # Safe processing
        result = {
            'status': 'success',
            'processed': True,
            'data': {k: v for k, v in data.items() if k in DataValidator.ALLOWED_FIELDS}
        }

        return result


def main():
    """Main entry point."""
    app = SecureApplication()

    # Create user securely
    user = app.create_user('john_doe', 'john@example.com', 'SecureP@ss123')

    # Process data securely
    result = app.process_request({'name': 'John', 'email': 'john@example.com'})

    print(f"User created: {user.username}")
    print(f"Processing result: {result}")


if __name__ == '__main__':
    main()
''')


def create_oo_moderate_vulnerabilities(base_dir: Path) -> None:
    """Create OO code with moderate security issues."""
    app = base_dir / "webapp.py"
    app.write_text('''"""Web application with some security issues."""

import hashlib
import pickle
import random
import sqlite3
from typing import Any, Dict, List, Optional


class User:
    """User class with some security issues."""

    # B105: Hardcoded salt (should be random per user)
    SALT = "mysalt123"

    def __init__(self, username: str, password: str):
        """Initialize user."""
        self.username = username
        # B303: MD5 is weak for password hashing
        self.password_hash = hashlib.md5(
            (password + self.SALT).encode()
        ).hexdigest()

        # B311: Using random instead of secrets
        self.session_token = str(random.randint(100000, 999999))

    def check_password(self, password: str) -> bool:
        """Check password (weak implementation)."""
        test_hash = hashlib.md5(
            (password + self.SALT).encode()
        ).hexdigest()
        # B105: String comparison may be vulnerable to timing attacks
        return test_hash == self.password_hash


class Database:
    """Database class with SQL injection risks."""

    def __init__(self, db_path: str):
        """Initialize database connection."""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        """B608: SQL injection vulnerability."""
        query = f"SELECT * FROM users WHERE username = '{username}'"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def save_data(self, data: Any) -> None:
        """B301: Pickle serialization (security risk)."""
        serialized = pickle.dumps(data)
        self.cursor.execute(
            "INSERT INTO data (content) VALUES (?)",
            (serialized,)
        )

    def load_data(self, data_id: int) -> Any:
        """B301: Pickle deserialization vulnerability."""
        self.cursor.execute(
            "SELECT content FROM data WHERE id = ?",
            (data_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return pickle.loads(row[0])
        return None


class SessionManager:
    """Session management with security issues."""

    def __init__(self):
        """Initialize session manager."""
        self.sessions: Dict[str, User] = {}
        # B311: Weak random for session IDs
        self.random = random.Random()

    def create_session(self, user: User) -> str:
        """Create session with weak token."""
        # B311: Predictable session ID
        session_id = str(self.random.randint(1000000, 9999999))
        self.sessions[session_id] = user
        return session_id

    def validate_session(self, session_id: str) -> Optional[User]:
        """Validate session (no expiration)."""
        # Security issue: No session expiration
        return self.sessions.get(session_id)


class FileHandler:
    """File handler with some security issues."""

    @staticmethod
    def save_upload(filename: str, content: bytes) -> None:
        """Save uploaded file (path traversal risk)."""
        # B108: Potential path traversal
        path = f"/uploads/{filename}"
        with open(path, 'wb') as f:
            f.write(content)

    @staticmethod
    def execute_script(script_name: str) -> str:
        """B605: Command injection risk."""
        import os
        # Dangerous: constructing shell command
        command = f"python scripts/{script_name}"
        return os.popen(command).read()


class Application:
    """Main application with mixed security."""

    # B105: Hardcoded configuration
    SECRET_KEY = "my_secret_key_123"
    DEBUG = True  # B105: Debug enabled in production

    def __init__(self):
        """Initialize application."""
        self.db = Database('app.db')
        self.sessions = SessionManager()
        self.users: List[User] = []

    def authenticate(self, username: str, password: str) -> Optional[str]:
        """Authenticate user (with SQL injection risk)."""
        user_data = self.db.get_user(username)

        if user_data:
            user = User(username, password)
            if user.check_password(password):
                return self.sessions.create_session(user)

        return None

    def process_data(self, data: Any) -> None:
        """Process and store data (with pickle risk)."""
        self.db.save_data(data)


def main():
    """Main entry point."""
    app = Application()

    # Authenticate user
    session = app.authenticate("admin", "password123")

    if session:
        print(f"Session created: {session}")

        # Process potentially dangerous data
        user_data = {"name": "admin", "role": "superuser"}
        app.process_data(user_data)


if __name__ == '__main__':
    main()
''')


def create_test_fixtures(base_dir: Path) -> Dict[str, Path]:
    """Create all test fixtures and return paths."""
    fixtures = {}

    # Procedural fixtures
    proc_safe = base_dir / "procedural_safe"
    proc_safe.mkdir(exist_ok=True)
    create_procedural_no_vulnerabilities(proc_safe)
    fixtures['procedural_safe'] = proc_safe

    proc_vulnerable = base_dir / "procedural_vulnerable"
    proc_vulnerable.mkdir(exist_ok=True)
    create_procedural_high_vulnerabilities(proc_vulnerable)
    fixtures['procedural_vulnerable'] = proc_vulnerable

    # OO fixtures
    oo_safe = base_dir / "oo_safe"
    oo_safe.mkdir(exist_ok=True)
    create_oo_no_vulnerabilities(oo_safe)
    fixtures['oo_safe'] = oo_safe

    oo_moderate = base_dir / "oo_moderate"
    oo_moderate.mkdir(exist_ok=True)
    create_oo_moderate_vulnerabilities(oo_moderate)
    fixtures['oo_moderate'] = oo_moderate

    return fixtures


__all__ = ['create_test_fixtures']