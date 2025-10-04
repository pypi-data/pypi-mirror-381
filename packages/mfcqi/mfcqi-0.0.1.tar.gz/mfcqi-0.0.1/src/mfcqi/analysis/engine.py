"""LLM analysis engine with Jinja2 templates and tool context."""

from pathlib import Path
from typing import Any

import litellm
from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel

from mfcqi.analysis.config import AnalysisConfig
from mfcqi.analysis.diagnostics import (
    DiagnosticsCollection,
)
from mfcqi.calculator import MFCQICalculator


class AnalysisResult(BaseModel):
    """Result from LLM analysis."""

    mfcqi_score: float
    metric_scores: dict[str, float]
    diagnostics: list[DiagnosticsCollection]
    recommendations: list[str]
    model_used: str


class LLMAnalysisEngine:
    """LLM analysis with context-aware recommendations."""

    def __init__(self, model: str | None = None, config: AnalysisConfig | None = None):
        """Initialize LLM analysis engine."""
        if config:
            self.config = config
        else:
            self.config = AnalysisConfig(model=model) if model else AnalysisConfig()

        self.model_name = self.config.model
        self.mfcqi_calculator = MFCQICalculator()

        # Set up Jinja2 templates with autoescape for security
        template_dir = Path(__file__).parent.parent / "templates"
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=True,  # Enable autoescape to prevent XSS vulnerabilities
        )
        self.main_template = self.env.get_template("code_quality_analysis.j2")
        self.fallback_template = self.env.get_template("fallback_recommendations.j2")

    def analyze_with_cqi_data(
        self,
        codebase_path: str,
        cqi_data: dict[str, Any],
        recommendation_count: int = 50,
        tool_outputs: dict[str, Any] | None = None,
    ) -> AnalysisResult:
        """Analyze with pre-calculated MFCQI data and REAL tool outputs."""
        try:
            self.config.validate_config()

            # Build context with REAL tool outputs
            context = self._build_context_with_real_data(
                Path(codebase_path), cqi_data, tool_outputs or {}
            )

            # Extract prioritized issues from tool outputs
            prioritized_issues = self._extract_prioritized_issues(
                tool_outputs or {}, recommendation_count, cqi_data
            )
            context["prioritized_issues"] = prioritized_issues
            context["recommendation_count"] = len(prioritized_issues)

            # Generate prompt from template
            prompt = self.main_template.render(**context)

            # Make LLM request
            llm_response = self._make_llm_request(prompt)

            # Parse recommendations
            recommendations = self._parse_recommendations(llm_response, len(prioritized_issues))

            return AnalysisResult(
                mfcqi_score=cqi_data.get("mfcqi_score", 0.0),
                metric_scores={k: v for k, v in cqi_data.items() if k != "mfcqi_score"},
                diagnostics=[],
                recommendations=recommendations,
                model_used=self.model_name,
            )
        except Exception as e:
            # No fallbacks - fail properly
            raise Exception(f"LLM analysis failed: {e}") from e

    def _build_context_with_real_data(
        self, codebase_path: Path, metrics: dict[str, Any], tool_outputs: dict[str, Any]
    ) -> dict[str, Any]:
        """Build context with REAL tool outputs, no fakes."""
        from mfcqi.core.file_utils import get_python_files

        py_files = get_python_files(codebase_path)
        total_lines = sum(len(f.read_text().splitlines()) for f in py_files if f.exists())

        # Categorize metrics by score
        critical_metrics = []
        for name, score in metrics.items():
            if name != "mfcqi_score" and isinstance(score, (int, float)) and score < 0.3:
                critical_metrics.append(
                    {
                        "name": name,
                        "score": score,
                        "tool_output": self._format_tool_output_for_metric(name, tool_outputs),
                    }
                )

        # Format real tool outputs for template
        formatted_tool_outputs = self._format_tool_outputs(tool_outputs)

        return {
            "codebase_path": str(codebase_path),
            "total_files": len(py_files),
            "total_lines": total_lines,
            "mfcqi_score": metrics.get("mfcqi_score", 0.0),
            "metrics": {k: v for k, v in metrics.items() if k != "mfcqi_score"},
            "critical_metrics": sorted(critical_metrics, key=lambda x: x["score"]),
            "tool_outputs": formatted_tool_outputs,
        }

    def _extract_prioritized_issues(
        self,
        tool_outputs: dict[str, Any],
        recommendation_count: int,
        metrics: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Extract and prioritize issues from tool outputs to generate N recommendations."""
        all_issues = []

        # Extract security issues from Bandit (HIGHEST priority)
        if "bandit_issues" in tool_outputs:
            for issue in tool_outputs["bandit_issues"]:
                # Map Bandit severity to our priority (always treat as HIGH for security)
                severity = issue.get("issue_severity", "MEDIUM")
                if severity in ["CRITICAL", "HIGH"]:
                    priority = 4
                    severity_tag = "HIGH"
                else:
                    priority = 3
                    severity_tag = "MEDIUM"

                all_issues.append(
                    {
                        "priority": priority,
                        "severity": severity_tag,
                        "type": "security",
                        "file": issue.get("filename", "unknown"),
                        "line": issue.get("line_number", 0),
                        "issue": issue.get("test_name", "unknown"),
                        "description": issue.get("issue_text", ""),
                    }
                )

        # Extract complexity issues (HIGH priority for complexity > 15)
        if "complex_functions" in tool_outputs:
            for func in tool_outputs["complex_functions"]:
                complexity = func.get("complexity", 0)
                if complexity > 15:
                    priority = 3
                    severity = "HIGH"
                elif complexity > 10:
                    priority = 2
                    severity = "MEDIUM"
                else:
                    priority = 1
                    severity = "LOW"

                all_issues.append(
                    {
                        "priority": priority,
                        "severity": severity,
                        "type": "complexity",
                        "file": func.get("file", "unknown"),
                        "line": func.get("line", 0),
                        "issue": f"High cyclomatic complexity in {func.get('name', 'unknown')}",
                        "description": f"Cyclomatic complexity: {complexity}",
                    }
                )

        # Add metric-based issues if we haven't reached the cap
        if metrics:
            for metric_name, score in metrics.items():
                if metric_name != "mfcqi_score" and isinstance(score, (int, float)) and score < 0.6:
                    priority = 2 if score < 0.4 else 1
                    all_issues.append(
                        {
                            "priority": priority,
                            "severity": "MEDIUM" if score < 0.4 else "LOW",
                            "type": "metric",
                            "file": "project-wide",
                            "line": 0,
                            "issue": f"Low {metric_name.replace('_', ' ')} score",
                            "description": f"{metric_name}: {score:.3f}",
                        }
                    )

        # Sort by priority (highest first) and take top N
        all_issues.sort(key=lambda x: x["priority"], reverse=True)
        return all_issues[:recommendation_count]

    def _format_tool_output_for_metric(self, metric_name: str, tool_outputs: dict[str, Any]) -> str:
        """Format tool output for a specific metric."""
        if metric_name == "security" and "bandit_issues" in tool_outputs:
            issues = tool_outputs["bandit_issues"]
            return f"Found {len(issues)} security vulnerabilities via Bandit"
        elif metric_name == "halstead_volume" and f"{metric_name}_raw" in tool_outputs:
            return f"Halstead Volume: {tool_outputs[f'{metric_name}_raw']:.0f}"
        elif metric_name == "cyclomatic_complexity" and f"{metric_name}_raw" in tool_outputs:
            return f"Average Cyclomatic Complexity: {tool_outputs[f'{metric_name}_raw']:.1f}"
        return ""

    def _format_tool_outputs(self, tool_outputs: dict[str, Any]) -> dict[str, Any]:
        """Format real tool outputs for template consumption."""
        formatted: dict[str, Any] = {}

        # Format Bandit issues if present
        if "bandit_issues" in tool_outputs:
            issues = tool_outputs["bandit_issues"]

            # Count by severity
            severity_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "CRITICAL": 0}
            for issue in issues:
                severity = issue.get("issue_severity", "LOW")
                severity_counts[severity] = severity_counts.get(severity, 0) + 1

            # Get top issues
            top_issues = sorted(
                issues,
                key=lambda x: {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(
                    x.get("issue_severity", "LOW"), 0
                ),
                reverse=True,
            )[:10]

            formatted["bandit"] = {
                "summary": f"Found {len(issues)} security issues",
                "critical_count": severity_counts["CRITICAL"],
                "high_count": severity_counts["HIGH"],
                "medium_count": severity_counts["MEDIUM"],
                "low_count": severity_counts["LOW"],
                "top_issues": [
                    {
                        "test_name": issue.get("test_name", "unknown"),
                        "issue_text": issue.get("issue_text", ""),
                        "filename": issue.get("filename", "unknown"),
                        "line_number": issue.get("line_number", 0),
                        "severity": issue.get("issue_severity", "UNKNOWN"),
                    }
                    for issue in top_issues
                ],
            }

        # Format complexity data if present
        if (
            "cyclomatic_complexity_raw" in tool_outputs
            or "halstead_volume_raw" in tool_outputs
            or "complex_functions" in tool_outputs
        ):
            complexity_data: dict[str, Any] = {"complex_functions": [], "high_volume_files": []}
            formatted["complexity"] = complexity_data

            # Use detailed function-level data if available
            if "complex_functions" in tool_outputs:
                complexity_data["complex_functions"] = tool_outputs["complex_functions"]
            elif "cyclomatic_complexity_raw" in tool_outputs:
                avg_cc = tool_outputs["cyclomatic_complexity_raw"]
                if avg_cc > 10:
                    functions_list = complexity_data["complex_functions"]
                    if isinstance(functions_list, list):
                        functions_list.append(
                            {
                                "name": "Multiple functions",
                                "file": "Various files",
                                "complexity": round(avg_cc),
                            }
                        )

            if "halstead_volume_raw" in tool_outputs:
                volume = tool_outputs["halstead_volume_raw"]
                if volume > 1000:
                    files_list = complexity_data["high_volume_files"]
                    if isinstance(files_list, list):
                        files_list.append({"path": "Various files", "volume": round(volume)})

        return formatted

    def _make_llm_request(self, prompt: str) -> str:
        """Make request to LLM."""
        try:
            litellm_config = self.config.get_litellm_config()
            response = litellm.completion(
                messages=[{"role": "user", "content": prompt}], **litellm_config
            )
            content = response.choices[0].message.content
            return content if isinstance(content, str) else str(content)
        except Exception as e:
            # NO FALLBACKS - let it fail properly
            raise Exception(f"LLM request failed: {e}") from e

    def _parse_recommendations(self, response: str, max_recommendations: int) -> list[str]:
        """Parse markdown-formatted LLM response into recommendations."""
        import re

        recommendations = []

        # Split by ## headings (since LLM doesn't use --- separators consistently)
        sections = re.split(r"\n(?=##\s*\[)", response)

        for section in sections:
            section = section.strip()
            if not section or not section.startswith("##"):
                continue

            # Extract heading with severity
            heading_match = re.search(r"^##\s*\[(\w+)\]\s*(.+)$", section, re.MULTILINE)
            if heading_match:
                severity = heading_match.group(1).upper()
                title = heading_match.group(2).strip()

                # Extract description
                desc_match = re.search(
                    r"\*\*Description:\*\*\s*(.+?)(?=\*\*|$)", section, re.DOTALL
                )
                description = desc_match.group(1).strip() if desc_match else ""

                # Build formatted recommendation
                if title and description:
                    # Truncate description to first sentence or 200 chars
                    if ". " in description:
                        description = description.split(". ")[0] + "."
                    elif len(description) > 200:
                        description = description[:200] + "..."

                    recommendations.append(f"[{severity}] {title}: {description}")

        # If no markdown format found, try to parse as plain text recommendations
        if not recommendations and response.strip():
            # Split by numbered list items
            lines = response.strip().split("\n")
            for line in lines:
                line = line.strip()
                # Match patterns like "1. ", "- ", "* ", etc.
                if re.match(r"^[\d\-\*•]\.\s", line):
                    # Remove the bullet/number
                    clean_line = re.sub(r"^[\d\-\*•]\.\s*", "", line)
                    # Check for severity markers
                    sev_match = re.match(r"^\[(\w+)\]\s*(.+)", clean_line)
                    if sev_match:
                        recommendations.append(clean_line)
                    else:
                        # Default to MEDIUM if no severity specified
                        recommendations.append(f"[MEDIUM] {clean_line}")

        return recommendations[:max_recommendations]
