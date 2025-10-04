"""
Integration tests for ParadigmDetector.

Tests the paradigm detection system with various code examples
to ensure proper classification of OO vs procedural Python code.
"""

import tempfile
from pathlib import Path

import pytest

from mfcqi.core.paradigm_detector import ParadigmDetector


class TestParadigmDetector:
    """Test the ParadigmDetector with various code examples."""

    def setup_method(self):
        """Set up test environment."""
        self.detector = ParadigmDetector()

    def _create_test_codebase(self, files_content: dict) -> Path:
        """Create a temporary codebase with given files."""
        temp_dir = Path(tempfile.mkdtemp())

        for filename, content in files_content.items():
            file_path = temp_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)

        return temp_dir

    def test_strong_oo_codebase(self):
        """Test detection of strong OO codebase (Django-style)."""
        files = {
            "models.py": '''
from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass

class BaseModel(ABC):
    """Abstract base model."""

    def __init__(self, id: Optional[int] = None):
        self._id = id

    @property
    def id(self) -> Optional[int]:
        return self._id

    @abstractmethod
    def save(self) -> None:
        pass

@dataclass
class User(BaseModel):
    """User model with inheritance and composition."""

    name: str
    email: str
    profile: 'UserProfile'

    def save(self) -> None:
        self._validate()
        self._persist()

    def _validate(self) -> None:
        if '@' not in self.email:
            raise ValueError("Invalid email")

    def _persist(self) -> None:
        # Save to database
        pass

class UserProfile:
    """User profile with encapsulation."""

    def __init__(self, bio: str):
        self._bio = bio
        self._settings = UserSettings()

    @property
    def bio(self) -> str:
        return self._bio

    def update_bio(self, new_bio: str) -> None:
        self._bio = new_bio

class UserSettings:
    """Nested class for composition."""

    def __init__(self):
        self._theme = "light"
''',
            "services.py": '''
from typing import List
from .models import User

class UserService:
    """Service class following dependency injection."""

    def __init__(self, repository: 'UserRepository'):
        self._repository = repository

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        user.save()
        return user

    def get_all_users(self) -> List[User]:
        return self._repository.find_all()

class UserRepository:
    """Repository pattern implementation."""

    def find_all(self) -> List[User]:
        # Database query
        return []
''',
        }

        codebase_path = self._create_test_codebase(files)
        result = self.detector.detect_paradigm(codebase_path)

        assert result["paradigm"] == "STRONG_OO"
        assert result["oo_score"] >= 0.7
        assert "rfc" in result["recommended_metrics"]
        assert "dit" in result["recommended_metrics"]
        assert "mhf" in result["recommended_metrics"]

    def test_procedural_codebase(self):
        """Test detection of procedural codebase (data science style)."""
        files = {
            "analysis.py": '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def load_dataset(filename: str) -> pd.DataFrame:
    """Load data from CSV file."""
    return pd.read_csv(filename)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset."""
    # Remove missing values
    df = df.dropna()

    # Normalize numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()

    return df

def calculate_statistics(data: pd.Series) -> dict:
    """Calculate basic statistics."""
    return {
        'mean': data.mean(),
        'std': data.std(),
        'median': data.median(),
        'min': data.min(),
        'max': data.max()
    }

def generate_report(df: pd.DataFrame) -> dict:
    """Generate statistical report."""
    report = {}

    for column in df.select_dtypes(include=[np.number]).columns:
        report[column] = calculate_statistics(df[column])

    return report

def plot_distributions(df: pd.DataFrame, output_dir: Path) -> None:
    """Create distribution plots."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        plt.figure(figsize=(8, 6))
        plt.hist(df[col], bins=30, alpha=0.7)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

        output_file = output_dir / f'{col}_distribution.png'
        plt.savefig(output_file)
        plt.close()

def main():
    """Main analysis pipeline."""
    # Load and process data
    df = load_dataset('data.csv')
    df_clean = clean_data(df)

    # Generate report
    stats_report = generate_report(df_clean)

    # Create visualizations
    output_dir = Path('plots')
    output_dir.mkdir(exist_ok=True)
    plot_distributions(df_clean, output_dir)

    print("Analysis complete!")

if __name__ == "__main__":
    main()
''',
            "utils.py": '''
import json
from pathlib import Path
from typing import Any, Dict

def save_json(data: Dict[str, Any], filename: str) -> None:
    """Save data to JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filename: str) -> Dict[str, Any]:
    """Load data from JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def validate_file_exists(filepath: str) -> bool:
    """Check if file exists."""
    return Path(filepath).exists()
''',
        }

        codebase_path = self._create_test_codebase(files)
        result = self.detector.detect_paradigm(codebase_path)

        assert result["paradigm"] == "PROCEDURAL"
        assert result["oo_score"] < 0.2
        assert "rfc" not in result["recommended_metrics"]
        assert "dit" not in result["recommended_metrics"]

    def test_mixed_oo_codebase(self):
        """Test detection of mixed OO codebase (Flask-style)."""
        files = {
            "app.py": '''
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Global configuration
DATABASE_URL = "sqlite:///app.db"
DEBUG_MODE = True

def create_app():
    """Application factory."""
    app.config['DEBUG'] = DEBUG_MODE
    return app

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    users = fetch_all_users()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    """Create new user."""
    data = request.get_json()
    user_id = save_user(data)
    return jsonify({'id': user_id}), 201

def fetch_all_users():
    """Fetch users from database."""
    # Database query logic
    return [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'}
    ]

def save_user(user_data):
    """Save user to database."""
    # Database save logic
    return 123

class UserValidator:
    """Simple validator class."""

    @staticmethod
    def validate_email(email):
        return '@' in email

    @staticmethod
    def validate_name(name):
        return len(name) > 0

if __name__ == '__main__':
    app.run(debug=True)
''',
            "config.py": '''
import os
from dataclasses import dataclass

@dataclass
class Config:
    """Configuration dataclass."""
    database_url: str
    debug: bool = False
    secret_key: str = "dev-key"

def get_config():
    """Get configuration based on environment."""
    return Config(
        database_url=os.getenv('DATABASE_URL', 'sqlite:///default.db'),
        debug=os.getenv('DEBUG', 'False').lower() == 'true',
        secret_key=os.getenv('SECRET_KEY', 'dev-key')
    )
''',
        }

        codebase_path = self._create_test_codebase(files)
        result = self.detector.detect_paradigm(codebase_path)

        assert result["paradigm"] in ["MIXED_OO", "WEAK_OO"]
        assert 0.2 <= result["oo_score"] < 0.7
        # Should have some OO metrics but not all
        recommended = result["recommended_metrics"]
        assert "rfc" in recommended or "coupling" in recommended

    def test_functional_style_codebase(self):
        """Test detection of functional-style codebase."""
        files = {
            "functional.py": '''
from functools import reduce, partial
from itertools import chain, groupby
from operator import add, mul
from typing import List, Callable, Iterator

def compose(*functions):
    """Compose multiple functions."""
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def curry(func):
    """Curry a function."""
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return partial(func, *args, **kwargs)
    return curried

@curry
def multiply_add(x, y, z):
    """Multiply first two, add third."""
    return x * y + z

def map_reduce_filter(data: List[int]) -> int:
    """Functional data processing pipeline."""
    return reduce(
        add,
        map(
            lambda x: x ** 2,
            filter(lambda x: x % 2 == 0, data)
        ),
        0
    )

def group_and_sum(data: List[tuple]) -> dict:
    """Group data and sum values."""
    grouped = groupby(sorted(data), key=lambda x: x[0])
    return {
        key: sum(item[1] for item in group)
        for key, group in grouped
    }

def pipeline(*functions):
    """Create a data processing pipeline."""
    def process(data):
        return reduce(lambda result, func: func(result), functions, data)
    return process

# Pure functions for data transformation
square = lambda x: x ** 2
double = lambda x: x * 2
is_even = lambda x: x % 2 == 0

def main():
    """Main functional processing."""
    data = list(range(1, 11))

    # Functional pipeline
    process = pipeline(
        partial(filter, is_even),
        partial(map, square),
        partial(map, double),
        list
    )

    result = process(data)
    print(f"Processed data: {result}")

if __name__ == "__main__":
    main()
'''
        }

        codebase_path = self._create_test_codebase(files)
        result = self.detector.detect_paradigm(codebase_path)

        assert result["paradigm"] == "PROCEDURAL"
        assert result["oo_score"] < 0.2

    def test_empty_codebase(self):
        """Test detection with empty codebase."""
        files = {}

        codebase_path = self._create_test_codebase(files)
        result = self.detector.detect_paradigm(codebase_path)

        assert result["paradigm"] == "UNKNOWN"
        assert result["oo_score"] == 0.0

    def test_weak_oo_codebase(self):
        """Test detection of weak OO codebase (simple classes)."""
        files = {
            "simple.py": '''
def process_data(filename):
    """Process data from file."""
    with open(filename) as f:
        lines = f.readlines()

    data = [line.strip().split(',') for line in lines]
    return data

class DataPoint:
    """Simple data container."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

def analyze_points(points):
    """Analyze list of data points."""
    total_distance = sum(point.distance_from_origin() for point in points)
    return total_distance / len(points)

def main():
    data = process_data('input.csv')
    points = [DataPoint(float(row[0]), float(row[1])) for row in data]
    avg_distance = analyze_points(points)
    print(f"Average distance: {avg_distance}")
'''
        }

        codebase_path = self._create_test_codebase(files)
        result = self.detector.detect_paradigm(codebase_path)

        # Could be MIXED_OO, WEAK_OO, or PROCEDURAL depending on exact scoring
        assert result["paradigm"] in ["MIXED_OO", "WEAK_OO", "PROCEDURAL"]
        assert result["oo_score"] < 0.7  # Not strong OO

    def test_metrics_selection_consistency(self):
        """Test that metric selection is consistent with paradigm classification."""
        test_cases = [
            ("STRONG_OO", ["rfc", "dit", "mhf", "coupling", "cohesion"]),
            ("MIXED_OO", ["rfc", "coupling", "cohesion"]),
            ("WEAK_OO", ["coupling"]),
            ("PROCEDURAL", []),
        ]

        for paradigm, expected_oo_metrics in test_cases:
            recommended = self.detector._get_recommended_metrics(paradigm)

            # Check that expected OO metrics are present/absent
            for metric in expected_oo_metrics:
                assert metric in recommended, f"{metric} should be in {paradigm} recommendations"

            # All paradigms should have base metrics
            base_metrics = [
                "cyclomatic_complexity",
                "cognitive_complexity",
                "maintainability_index",
            ]
            for metric in base_metrics:
                assert metric in recommended, f"{metric} should always be recommended"

    def test_scoring_boundary_conditions(self):
        """Test scoring at boundary conditions."""
        # Test minimum possible metrics
        self.detector.metrics.total_lines = 1
        self.detector.metrics.total_classes = 0
        self.detector.metrics.total_functions = 1
        score = self.detector._calculate_oo_score()
        assert 0.0 <= score <= 1.0

        # Test maximum OO indicators
        self.detector.metrics.total_lines = 100
        self.detector.metrics.total_classes = 10
        self.detector.metrics.class_methods = 50
        self.detector.metrics.standalone_functions = 1
        self.detector.metrics.inheritance_count = 5
        self.detector.metrics.private_methods = 25
        self.detector.metrics.properties = 10
        score = self.detector._calculate_oo_score()
        assert 0.0 <= score <= 1.0

    def teardown_method(self):
        """Clean up after tests."""
        # Temporary directories are automatically cleaned up
        pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
