"""
Test for Analysis Diagnostics - following strict TDD.
This test MUST fail first because the code doesn't exist yet.
"""

import json


def test_diagnostic_model_exists():
    """RED: Test that Diagnostic model exists."""
    from mfcqi.analysis.diagnostics import Diagnostic

    assert Diagnostic is not None


def test_diagnostic_severity_enum_exists():
    """RED: Test that DiagnosticSeverity enum exists."""
    from mfcqi.analysis.diagnostics import DiagnosticSeverity

    assert DiagnosticSeverity is not None
    assert hasattr(DiagnosticSeverity, "ERROR")
    assert hasattr(DiagnosticSeverity, "WARNING")
    assert hasattr(DiagnosticSeverity, "INFORMATION")
    assert hasattr(DiagnosticSeverity, "HINT")


def test_position_model_exists():
    """RED: Test that Position model exists."""
    from mfcqi.analysis.diagnostics import Position

    assert Position is not None


def test_range_model_exists():
    """RED: Test that Range model exists."""
    from mfcqi.analysis.diagnostics import Range

    assert Range is not None


def test_position_creation():
    """RED: Test Position model creation with line and character."""
    from mfcqi.analysis.diagnostics import Position

    position = Position(line=10, character=5)

    assert position.line == 10
    assert position.character == 5


def test_range_creation():
    """RED: Test Range model creation with start and end positions."""
    from mfcqi.analysis.diagnostics import Position, Range

    start = Position(line=10, character=5)
    end = Position(line=10, character=15)
    range_obj = Range(start=start, end=end)

    assert range_obj.start == start
    assert range_obj.end == end


def test_diagnostic_creation_minimal():
    """RED: Test Diagnostic creation with minimal required fields."""
    from mfcqi.analysis.diagnostics import Diagnostic, DiagnosticSeverity, Position, Range

    start = Position(line=10, character=5)
    end = Position(line=10, character=15)
    range_obj = Range(start=start, end=end)

    diagnostic = Diagnostic(
        range=range_obj,
        message="High cyclomatic complexity detected",
        severity=DiagnosticSeverity.WARNING,
    )

    assert diagnostic.range == range_obj
    assert diagnostic.message == "High cyclomatic complexity detected"
    assert diagnostic.severity == DiagnosticSeverity.WARNING
    assert diagnostic.source == "mfcqi"  # Default value


def test_diagnostic_creation_full():
    """RED: Test Diagnostic creation with all fields."""
    from mfcqi.analysis.diagnostics import (
        Diagnostic,
        DiagnosticRelatedInformation,
        DiagnosticSeverity,
        Position,
        Range,
    )

    start = Position(line=10, character=5)
    end = Position(line=10, character=15)
    range_obj = Range(start=start, end=end)

    related = DiagnosticRelatedInformation(
        location_uri="file:///path/to/file.py",
        location_range=range_obj,
        message="Related complexity issue",
    )

    diagnostic = Diagnostic(
        range=range_obj,
        message="High cyclomatic complexity detected",
        severity=DiagnosticSeverity.WARNING,
        code="CC001",
        source="mfcqi",
        related_information=[related],
    )

    assert diagnostic.code == "CC001"
    assert len(diagnostic.related_information) == 1
    assert diagnostic.related_information[0] == related


def test_diagnostic_json_serialization():
    """RED: Test that Diagnostic can be serialized to JSON."""
    from mfcqi.analysis.diagnostics import Diagnostic, DiagnosticSeverity, Position, Range

    start = Position(line=10, character=5)
    end = Position(line=10, character=15)
    range_obj = Range(start=start, end=end)

    diagnostic = Diagnostic(
        range=range_obj,
        message="High cyclomatic complexity detected",
        severity=DiagnosticSeverity.WARNING,
        code="CC001",
    )

    # Should be able to convert to JSON
    json_str = diagnostic.model_dump_json()
    parsed = json.loads(json_str)

    assert parsed["message"] == "High cyclomatic complexity detected"
    assert parsed["severity"] == 2  # WARNING enum value
    assert parsed["code"] == "CC001"
    assert parsed["source"] == "mfcqi"


def test_diagnostic_related_information_exists():
    """RED: Test that DiagnosticRelatedInformation model exists."""
    from mfcqi.analysis.diagnostics import DiagnosticRelatedInformation

    assert DiagnosticRelatedInformation is not None


def test_diagnostic_related_information_creation():
    """RED: Test DiagnosticRelatedInformation creation."""
    from mfcqi.analysis.diagnostics import DiagnosticRelatedInformation, Position, Range

    start = Position(line=5, character=0)
    end = Position(line=5, character=10)
    range_obj = Range(start=start, end=end)

    related = DiagnosticRelatedInformation(
        location_uri="file:///path/to/file.py",
        location_range=range_obj,
        message="Related complexity issue here",
    )

    assert related.location_uri == "file:///path/to/file.py"
    assert related.location_range == range_obj
    assert related.message == "Related complexity issue here"


def test_diagnostic_severity_values():
    """RED: Test DiagnosticSeverity enum values match LSP specification."""
    from mfcqi.analysis.diagnostics import DiagnosticSeverity

    # LSP specification values
    assert DiagnosticSeverity.ERROR.value == 1
    assert DiagnosticSeverity.WARNING.value == 2
    assert DiagnosticSeverity.INFORMATION.value == 3
    assert DiagnosticSeverity.HINT.value == 4


def test_create_diagnostic_helper_function():
    """RED: Test helper function to create diagnostics easily."""
    from mfcqi.analysis.diagnostics import DiagnosticSeverity, create_diagnostic

    diagnostic = create_diagnostic(
        file_path="test.py",
        line=15,
        character=4,
        end_line=15,
        end_character=20,
        message="Missing docstring",
        severity=DiagnosticSeverity.WARNING,
        code="DOC001",
    )

    assert diagnostic.range.start.line == 15
    assert diagnostic.range.start.character == 4
    assert diagnostic.range.end.line == 15
    assert diagnostic.range.end.character == 20
    assert diagnostic.message == "Missing docstring"
    assert diagnostic.severity == DiagnosticSeverity.WARNING
    assert diagnostic.code == "DOC001"


def test_create_diagnostic_helper_with_defaults():
    """RED: Test helper function with default values."""
    from mfcqi.analysis.diagnostics import DiagnosticSeverity, create_diagnostic

    diagnostic = create_diagnostic(file_path="test.py", line=10, message="Test message")

    assert diagnostic.range.start.line == 10
    assert diagnostic.range.start.character == 0  # Default
    assert diagnostic.range.end.line == 10
    assert diagnostic.range.end.character == 0  # Default
    assert diagnostic.message == "Test message"
    assert diagnostic.severity == DiagnosticSeverity.ERROR  # Default
    assert diagnostic.source == "mfcqi"


def test_diagnostics_collection_model():
    """RED: Test DiagnosticsCollection model for multiple diagnostics."""
    from mfcqi.analysis.diagnostics import (
        Diagnostic,
        DiagnosticsCollection,
        DiagnosticSeverity,
        Position,
        Range,
    )

    start = Position(line=10, character=5)
    end = Position(line=10, character=15)
    range_obj = Range(start=start, end=end)

    diagnostic1 = Diagnostic(range=range_obj, message="Issue 1", severity=DiagnosticSeverity.ERROR)

    diagnostic2 = Diagnostic(
        range=range_obj, message="Issue 2", severity=DiagnosticSeverity.WARNING
    )

    collection = DiagnosticsCollection(file_path="test.py", diagnostics=[diagnostic1, diagnostic2])

    assert collection.file_path == "test.py"
    assert len(collection.diagnostics) == 2
    assert collection.diagnostics[0] == diagnostic1
    assert collection.diagnostics[1] == diagnostic2


def test_diagnostics_collection_json_output():
    """RED: Test DiagnosticsCollection JSON serialization."""
    from mfcqi.analysis.diagnostics import (
        DiagnosticsCollection,
        DiagnosticSeverity,
        create_diagnostic,
    )

    diagnostic1 = create_diagnostic(
        "test.py", 5, message="Error 1", severity=DiagnosticSeverity.ERROR
    )
    diagnostic2 = create_diagnostic(
        "test.py", 10, message="Warning 1", severity=DiagnosticSeverity.WARNING
    )

    collection = DiagnosticsCollection(file_path="test.py", diagnostics=[diagnostic1, diagnostic2])

    json_str = collection.model_dump_json()
    parsed = json.loads(json_str)

    assert parsed["file_path"] == "test.py"
    assert len(parsed["diagnostics"]) == 2
    assert parsed["diagnostics"][0]["message"] == "Error 1"
    assert parsed["diagnostics"][1]["message"] == "Warning 1"
