"""
Lack of Cohesion of Methods (LCOM) metric implementation.
Based on CK metrics suite and research thresholds.
"""

import ast
from collections import defaultdict
from pathlib import Path
from typing import Any, Union, cast

from mfcqi.core.file_utils import get_python_files
from mfcqi.core.metric import Metric


class LackOfCohesionOfMethods(Metric):
    """Measures Lack of Cohesion of Methods (LCOM) using static analysis."""

    def extract(self, codebase: Path) -> float:
        """Extract average LCOM across all classes in the codebase."""
        if not codebase.exists() or not codebase.is_dir():
            return 0.0

        py_files = get_python_files(codebase)
        if not py_files:
            return 0.0

        class_lcom_scores = []

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding="utf-8")
                tree = ast.parse(content)

                # Get LCOM for each class in this file
                file_lcom = self._analyze_file_cohesion(tree)
                class_lcom_scores.extend(file_lcom)

            except (SyntaxError, UnicodeDecodeError, Exception):
                continue

        if not class_lcom_scores:
            return 0.0

        # Return average LCOM across all classes
        return sum(class_lcom_scores) / len(class_lcom_scores)

    def _analyze_file_cohesion(self, tree: ast.AST) -> list[float]:
        """Analyze cohesion for all classes in a file."""
        cohesion_scores = []

        # Find all class definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                lcom_score = self._calculate_class_lcom(node)
                cohesion_scores.append(lcom_score)

        return cohesion_scores

    def _calculate_class_lcom(self, class_node: ast.ClassDef) -> float:
        """Calculate LCOM for a single class using LCOM4 approach."""
        # Get all methods and instance variables
        methods = []
        instance_vars = set()

        # Find methods and collect instance variables they access
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("__"):
                # Skip magic methods for cohesion calculation
                method_vars = self._get_method_instance_vars(node)
                methods.append((node.name, method_vars))
                instance_vars.update(method_vars)

        if len(methods) <= 1:
            return 0.0  # Single method or no methods = perfect cohesion

        # Calculate LCOM4: number of connected components
        # Methods are connected if they share instance variables
        method_connections = self._build_method_connections(methods)
        connected_components = self._count_connected_components(method_connections)

        # LCOM4 = number of connected components
        # 1 = perfect cohesion, >1 = lack of cohesion
        return float(connected_components)

    def _get_method_instance_vars(self, method_node: ast.FunctionDef) -> set[str]:
        """Get instance variables accessed by a method."""
        instance_vars = set()

        for node in ast.walk(method_node):
            if (
                isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id == "self"
            ):
                # Look for self.variable_name patterns
                instance_vars.add(node.attr)

        return instance_vars

    def _build_method_connections(self, methods: list[tuple[str, set[str]]]) -> dict[str, set[str]]:
        """Build graph of method connections based on shared instance variables."""
        connections = defaultdict(set)

        for i, (method1, vars1) in enumerate(methods):
            for j, (method2, vars2) in enumerate(methods):
                if i != j and vars1 & vars2:  # Share at least one instance variable
                    connections[method1].add(method2)
                    connections[method2].add(method1)

        return dict(connections)

    def _count_connected_components(self, connections: dict[str, set[str]]) -> int:
        """Count connected components in method connection graph."""
        if not connections:
            return 1  # No connections means one component

        visited = set()
        components = 0

        def dfs(method: str) -> None:
            """Depth-first search to explore connected component."""
            if method in visited:
                return
            visited.add(method)
            for connected_method in connections.get(method, set()):
                dfs(connected_method)

        # Count components
        all_methods = set(connections.keys())
        for neighbor_set in connections.values():
            all_methods.update(neighbor_set)

        for method in all_methods:
            if method not in visited:
                dfs(method)
                components += 1

        return max(1, components)

    def normalize(self, value: Union[float, dict[str, Any]]) -> float:
        """Normalize LCOM to [0,1] range where lower LCOM is better.
        Based on research thresholds:
        - LCOM4 = 1: Perfect cohesion (1.0)
        - LCOM4 = 2-3: Good cohesion (0.7-0.9)
        - LCOM4 = 4-6: Moderate cohesion (0.4-0.7)
        - LCOM4 > 6: Poor cohesion (0.0-0.4)
        """
        value = cast("float", value)  # This metric only returns float from extract()
        if value <= 1:
            return 1.0  # Perfect cohesion
        elif value <= 3:
            # Good: 1-3 maps to 1.0-0.7
            return 1.0 - ((value - 1) / 2) * 0.3
        elif value <= 6:
            # Moderate: 3-6 maps to 0.7-0.4
            return 0.7 - ((value - 3) / 3) * 0.3
        else:
            # Poor: 6+ maps to 0.4-0.0
            return max(0.0, 0.4 - ((value - 6) / 6) * 0.4)

    def get_weight(self) -> float:
        """Return evidence-based weight for cohesion.

        Weight: 0.50 (reduced from 0.65 based on weak empirical evidence)
        Justification:
        - LCOM is conceptually useful as SRP indicator
        - BUT meta-analyses show < 50% success in fault prediction
        - Li & Henry (1993) claimed correlation but no r-value published
        - Weaker evidence than CBO (r=0.42) or RFC (r=0.48)
        - Meta-studies found "no positive impact on fault proneness"
        - Weight 0.50 reflects mixed empirical support
        - Optional metric (only applied to OO code)
        """
        return 0.50

    def get_name(self) -> str:
        """Return the name of this metric."""
        return "Lack of Cohesion of Methods"
