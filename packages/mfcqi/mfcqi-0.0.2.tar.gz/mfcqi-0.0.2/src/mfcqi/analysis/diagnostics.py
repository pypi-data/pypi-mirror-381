"""
Diagnostic models for MFCQI analysis - LSP compatible format.
"""

from enum import IntEnum

from pydantic import BaseModel


class DiagnosticSeverity(IntEnum):
    """LSP DiagnosticSeverity enum values."""

    ERROR = 1
    WARNING = 2
    INFORMATION = 3
    HINT = 4


class Position(BaseModel):
    """LSP Position model."""

    line: int
    character: int


class Range(BaseModel):
    """LSP Range model."""

    start: Position
    end: Position


class DiagnosticRelatedInformation(BaseModel):
    """LSP DiagnosticRelatedInformation model."""

    location_uri: str
    location_range: Range
    message: str


class Diagnostic(BaseModel):
    """LSP Diagnostic model."""

    range: Range
    message: str
    severity: DiagnosticSeverity
    code: str | None = None
    source: str = "mfcqi"
    related_information: list[DiagnosticRelatedInformation] | None = None


class DiagnosticsCollection(BaseModel):
    """Collection of diagnostics for a single file."""

    file_path: str
    diagnostics: list[Diagnostic]


def create_diagnostic(
    file_path: str,
    line: int,
    message: str,
    character: int = 0,
    end_line: int | None = None,
    end_character: int | None = None,
    severity: DiagnosticSeverity = DiagnosticSeverity.ERROR,
    code: str | None = None,
) -> Diagnostic:
    """Helper function to create diagnostics easily."""
    if end_line is None:
        end_line = line
    if end_character is None:
        end_character = character

    start = Position(line=line, character=character)
    end = Position(line=end_line, character=end_character)
    range_obj = Range(start=start, end=end)

    return Diagnostic(range=range_obj, message=message, severity=severity, code=code)
