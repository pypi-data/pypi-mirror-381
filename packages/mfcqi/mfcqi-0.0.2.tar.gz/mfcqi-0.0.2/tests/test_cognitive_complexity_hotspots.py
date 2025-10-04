"""
Tests for Cognitive Complexity hotspot tracking - Strict TDD.

CognitiveComplexity to track individual function hotspots (CC > 15),
not just averages.

Per remediation plan: "Cognitive complexity only averages - Should track
method-level hotspots (>15)"
"""

import tempfile
import textwrap
from pathlib import Path


def test_cognitive_complexity_tracks_individual_functions():
    """
    RED: Test that cognitive complexity tracks individual function complexities.

    Current implementation only returns average. We need to track each function.
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    code = textwrap.dedent(
        """
        def simple_function():
            return 1

        def complex_function(x):
            if x > 0:
                if x > 10:
                    if x > 20:
                        if x > 30:
                            return x
            return 0
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Should return dict with average AND individual functions
        assert isinstance(result, dict), "Should return dict with detailed metrics"
        assert "average" in result, "Should include average complexity"
        assert "functions" in result, "Should include individual function data"
        assert isinstance(result["functions"], list), "Functions should be a list"


def test_cognitive_complexity_identifies_hotspots():
    """
    RED: Test that cognitive complexity identifies hotspots (CC > 15).

    Per SonarLint threshold, functions with CC > 15 are problematic.
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    # Create code with one high-complexity function (>15)
    code = textwrap.dedent(
        """
        def hotspot_function(a, b, c, d, e):
            # This function will have CC > 15 due to deep nesting
            if a:
                for i in range(10):
                    if b:
                        while c:
                            if d:
                                for j in range(5):
                                    if e:
                                        if a and b:
                                            if c or d:
                                                return 1
            return 0

        def simple_function():
            return 1
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Should identify hotspots
        assert "hotspots" in result, "Should track hotspots (CC > 15)"
        hotspots = result["hotspots"]
        assert isinstance(hotspots, list), "Hotspots should be a list"
        assert len(hotspots) > 0, "Should find at least one hotspot"

        # Hotspot should have details
        hotspot = hotspots[0]
        assert "function_name" in hotspot, "Should include function name"
        assert "complexity" in hotspot, "Should include complexity score"
        assert "line_number" in hotspot, "Should include line number"
        assert "file_path" in hotspot, "Should include file path"
        assert hotspot["complexity"] > 15, "Hotspot should have CC > 15"


def test_cognitive_complexity_hotspot_threshold_configurable():
    """
    RED: Test that hotspot threshold is configurable.

    Default is 15 per SonarLint, but should be configurable.
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    code = textwrap.dedent(
        """
        def moderate_function(x):
            if x:
                if x > 5:
                    if x > 10:
                        return x
            return 0
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        # Set lower threshold to catch this function
        metric = CognitiveComplexity(hotspot_threshold=5)
        result = metric.extract(Path(tmpdir))

        assert "hotspots" in result
        assert len(result["hotspots"]) > 0, "Should find hotspot with lower threshold"


def test_cognitive_complexity_no_hotspots_in_clean_code():
    """
    RED: Test that clean code has no hotspots.
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    code = textwrap.dedent(
        """
        def simple1():
            return 1

        def simple2(x):
            if x > 0:
                return x
            return 0

        def simple3(a, b):
            return a + b
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "clean.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        assert "hotspots" in result
        assert len(result["hotspots"]) == 0, "Clean code should have no hotspots"


def test_cognitive_complexity_sorts_hotspots_by_severity():
    """
    RED: Test that hotspots are sorted by complexity (worst first).
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    code = textwrap.dedent(
        """
        def moderate_hotspot(x):
            if x:
                if x > 5:
                    if x > 10:
                        if x > 15:
                            if x > 20:
                                return x
            return 0

        def severe_hotspot(a, b):
            if a:
                for i in range(10):
                    if b:
                        while a:
                            if b:
                                for j in range(5):
                                    if a and b:
                                        if a or b:
                                            if a != b:
                                                return 1
            return 0
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        hotspots = result["hotspots"]
        assert len(hotspots) >= 2, "Should find both hotspots"

        # Should be sorted by complexity descending
        for i in range(len(hotspots) - 1):
            assert hotspots[i]["complexity"] >= hotspots[i + 1]["complexity"], (
                "Hotspots should be sorted by complexity (worst first)"
            )


def test_cognitive_complexity_backward_compatible():
    """
    RED: Test that the metric is backward compatible.

    Existing code expects a float (average), but we're changing to dict.
    Need to handle both or provide migration path.
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    code = textwrap.dedent(
        """
        def simple():
            return 1
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Should still provide average as a number for backward compat
        assert "average" in result
        assert isinstance(result["average"], (int, float))


def test_cognitive_complexity_recommendations_mention_hotspots():
    """
    RED: Test that recommendations mention specific hotspot functions.

    Current recommendations are generic. Should mention actual problematic functions.
    """
    from mfcqi.metrics.cognitive import CognitiveComplexity

    code = textwrap.dedent(
        """
        def problematic_function(x):
            if x:
                if x > 5:
                    if x > 10:
                        if x > 15:
                            if x > 20:
                                if x > 25:
                                    return x
            return 0
        """
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        (Path(tmpdir) / "test.py").write_text(code)

        metric = CognitiveComplexity()
        result = metric.extract(Path(tmpdir))

        # Get recommendations based on the result
        recommendations = metric.get_recommendations(result)

        assert isinstance(recommendations, list)
        # Should mention the specific function name
        assert any("problematic_function" in rec for rec in recommendations), (
            "Recommendations should mention specific hotspot function names"
        )
