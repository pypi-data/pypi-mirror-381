.PHONY: install format lint test test-all clean check-types check-deps coverage check help quality-check mfcqi-demo find-dead-code

# Multi-Factor Code Quality Index (MFCQI) Project Makefile

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED = \033[0;31m
BLUE = \033[0;34m
NC = \033[0m # No Color

help:
	@echo "$(BLUE)📏 Multi-Factor Code Quality Index (MFCQI) - Makefile Commands$(NC)"
	@echo ""
	@echo "$(GREEN)🧪 Testing:$(NC)"
	@echo "  make test           - Run quick tests (core functionality)"
	@echo "  make test-all       - Run all tests including slow SOTA detection"
	@echo "  make test-unit      - Run unit tests only"
	@echo "  make test-coverage  - Run tests with coverage report"
	@echo "  make coverage-html  - Generate HTML coverage report"
	@echo ""
	@echo "$(GREEN)🔧 Code Quality:$(NC)"
	@echo "  make format         - Format code with ruff"
	@echo "  make lint           - Run all linting checks"
	@echo "  make check-format   - Check code formatting"
	@echo "  make check-types    - Run mypy type checking"
	@echo "  make check-deps     - Check for dependency conflicts"
	@echo "  make find-dead-code - Find unused/dead code with Vulture"
	@echo "  make quality-check  - Run all quality checks (lint + types + tests)"
	@echo "  make check-all      - Run all checks and all tests (comprehensive)"
	@echo ""
	@echo "$(GREEN)📦 Setup:$(NC)"
	@echo "  make install        - Install dependencies with UV"
	@echo "  make develop        - Install development dependencies"
	@echo "  make clean          - Clean cache files and artifacts"
	@echo ""
	@echo "$(GREEN)🎯 MFCQI Specific:$(NC)"
	@echo "  make mfcqi            - Display MFCQI score for current codebase"
	@echo "  make mfcqi-demo       - Run MFCQI analysis on current codebase"
	@echo "  make mfcqi-detailed   - Show detailed metrics including OO metrics"
	@echo "  make mfcqi-benchmark  - Run pattern detection benchmarks"
	@echo "  make mfcqi-paradigm   - Test paradigm detection on examples"
	@echo "  make test-oo          - Run OO metrics tests (RFC, DIT, MHF)"
	@echo ""
	@echo "$(GREEN)🚀 Quick Start:$(NC)"
	@echo "  make install && make test-all && make quality-check"

install:
	@echo "$(BLUE)📦 Installing dependencies with UV...$(NC)"
	uv sync --all-extras

develop:
	@echo "$(BLUE)🔧 Installing development dependencies...$(NC)"
	uv sync --all-extras --dev
	uv add --dev pytest-cov pytest-xdist mypy ruff bandit

format:
	@echo "$(BLUE)🎨 Formatting code with ruff...$(NC)"
	uv run ruff format src/ tests/
	uv run ruff check --fix src/ tests/

check-format:
	@echo "$(BLUE)🔍 Checking code formatting...$(NC)"
	uv run ruff format --check src/ tests/
	@echo "$(GREEN)✅ Code formatting is correct$(NC)"

lint:
	@echo "$(BLUE)🔍 Running linting checks...$(NC)"
	@echo "$(YELLOW)→ Ruff linting...$(NC)"
	uv run ruff check src/ tests/
	@echo "$(YELLOW)→ Bandit security checks...$(NC)"
	uv run bandit -r src/ -f json -o bandit-report.json || true
	@echo "$(YELLOW)→ Pylint analysis...$(NC)"
	uv run pylint src/mfcqi/ --output-format=json > pylint-report.json || true
	@echo "$(GREEN)✅ Linting complete. Check reports for details.$(NC)"

check-types:
	@echo "$(BLUE)🔍 Running mypy type checking...$(NC)"
	uv run mypy --strict src/mfcqi/
	@echo "$(GREEN)✅ Type checking passed$(NC)"

find-dead-code:
	@echo "$(BLUE)🔍 Finding dead/unused code with Vulture...$(NC)"
	uv run vulture src/ --min-confidence 80 --sort-by-size

test:
	@echo "$(BLUE)🧪 Running all tests (API tests will auto-skip without keys)...$(NC)"
	uv run pytest tests/ -n auto -v --tb=short

test-core:
	@echo "$(BLUE)🧪 Running core tests only...$(NC)"
	uv run pytest tests/test_cyclomatic_complexity.py tests/test_maintainability_index.py tests/test_mfcqi_calculator.py -n auto -v --tb=short

test-unit:
	@echo "$(BLUE)🧪 Running unit tests...$(NC)"
	uv run pytest tests/ -n auto -v --tb=short -m "not slow and not integration"

test-all:
	@echo "$(BLUE)🧪 Running ALL tests...$(NC)"
	uv run pytest tests/ -v --tb=short

test-fast:
	@echo "$(BLUE)🧪 Running fast tests only...$(NC)"
	uv run pytest tests/ -n auto -v --tb=short -m "not slow" -x

test-oo:
	@echo "$(BLUE)🧪 Running Object-Oriented metrics tests...$(NC)"
	uv run pytest tests/test_rfc_metric.py tests/test_dit_metric.py tests/test_mhf_metric.py -v --tb=short
	@echo "$(GREEN)✅ OO metrics tests passed$(NC)"

test-coverage:
	@echo "$(BLUE)🧪 Running tests with coverage...$(NC)"
	uv run pytest tests/ -n auto --cov=src/mfcqi --cov-branch --cov-report=term-missing --cov-report=xml --cov-report=json --cov-report=html --cov-fail-under=80 -q
	@echo "$(GREEN)✅ Coverage report generated:$(NC)"
	@echo "  - coverage.xml (for Codecov)"
	@echo "  - coverage.json (for analysis)"
	@echo "  - htmlcov/index.html (open in browser)"

coverage-html:
	@echo "$(BLUE)📊 Generating HTML coverage report...$(NC)"
	uv run pytest tests/ -n auto --cov=src/mfcqi --cov-report=html -q
	@echo "$(GREEN)✅ HTML coverage report generated in htmlcov/$(NC)"
	@echo "$(BLUE)Open htmlcov/index.html in your browser$(NC)"

quality-check: check-format lint check-types test
	@echo "$(GREEN)🎉 All quality checks passed!$(NC)"

check-deps:
	@echo "$(BLUE)🔍 Checking for dependency conflicts...$(NC)"
	@python3 scripts/check_deps.py && echo "$(GREEN)✅ No dependency conflicts detected$(NC)" || (echo "$(RED)❌ Dependency conflicts found$(NC)" && exit 1)

check-all: check-format check-types check-deps test-all
	@echo "$(GREEN)🎉 All essential checks and tests passed!$(NC)"
	@echo "$(BLUE)📊 Calculating MFCQI score...$(NC)"
	@uv run python -c "from mfcqi.calculator import MFCQICalculator; from pathlib import Path; calc = MFCQICalculator(); result = calc.calculate(Path('src/mfcqi')); print(f'📈 MFCQI Score: {result:.2%}')" 2>/dev/null

check: quality-check

# MFCQI-specific targets
mfcqi:
	@echo "$(BLUE)📊 Calculating MFCQI score...$(NC)"
	@uv run python -c "from mfcqi.calculator import MFCQICalculator; from pathlib import Path; calc = MFCQICalculator(include_test_coverage=True); result = calc.calculate(Path('src/mfcqi')); print(f'MFCQI Score: {result:.2%}')" 2>/dev/null

mfcqi-demo:
	@echo "$(BLUE)📏 Running MFCQI analysis on current codebase...$(NC)"
	uv run python -c "from mfcqi.calculator import MFCQICalculator; from pathlib import Path; calc = MFCQICalculator(include_test_coverage=True); result = calc.calculate(Path('src/mfcqi')); print(f'📊 Current MFCQI Score: {result:.2%}')"

mfcqi-detailed:
	@echo "$(BLUE)📊 Detailed MFCQI analysis with OO metrics...$(NC)"
	@echo "$(BLUE)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)"
	@uv run python -c "from mfcqi.calculator import MFCQICalculator; from pathlib import Path; calc = MFCQICalculator(include_test_coverage=True, use_paradigm_detection=True); details = calc.get_detailed_metrics(Path('src/mfcqi')); print('Core Metrics:'); core = ['cyclomatic_complexity', 'cognitive_complexity', 'halstead_volume', 'maintainability_index', 'code_duplication', 'documentation_coverage']; [print(f'  {k:<25}: {details.get(k, 0):.3f}') for k in core]; print('\nOO Metrics (if applicable):'); oo = ['rfc', 'dit', 'mhf']; [print(f'  {k.upper():<25}: {details.get(k, 0):.3f}' if k in details else f'  {k.upper():<25}: N/A') for k in oo]; print(f'\n📈 Overall MFCQI Score: {details[\"mfcqi_score\"]:.3f} ({details[\"mfcqi_score\"]*100:.1f}%)')"
	@echo "$(BLUE)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(NC)"

mfcqi-paradigm:
	@echo "$(BLUE)🔍 Testing paradigm detection...$(NC)"
	@uv run python -c "from mfcqi.core.paradigm_detector import ParadigmDetector; from pathlib import Path; det = ParadigmDetector(); res = det.detect_paradigm(Path('src/mfcqi')); print(f'Paradigm: {res[\"paradigm\"]}'); print(f'OO Score: {res[\"oo_score\"]:.3f}'); print(f'Explanation: {res[\"explanation\"]}')"

mfcqi-benchmark:
	@echo "$(BLUE)🎯 Running pattern detection benchmarks...$(NC)"
	uv run python final_improved_analysis.py

mfcqi-validate:
	@echo "$(BLUE)✅ Validating SOTA pattern detection...$(NC)"
	uv run python test_sota_detection.py

mfcqi-debug:
	@echo "$(BLUE)🔍 Debugging pattern detection...$(NC)"
	uv run python debug_pattern_scoring.py

# Performance and profiling
profile-tests:
	@echo "$(BLUE)⏱️  Profiling test performance...$(NC)"
	uv run pytest tests/test_design_pattern_density.py --profile

profile-mfcqi:
	@echo "$(BLUE)⏱️  Profiling MFCQI calculation...$(NC)"
	uv run python -m cProfile -o cqi_profile.prof -c "from mfcqi.calculator import CQICalculator; from pathlib import Path; calc = CQICalculator(); calc.calculate(Path('src/mfcqi'))"
	@echo "$(GREEN)Profile saved to cqi_profile.prof$(NC)"

# Security and dependency checks
security-check:
	@echo "$(BLUE)🔒 Running security checks...$(NC)"
	uv run bandit -r src/ -f text
	uv run pip-audit || echo "$(YELLOW)⚠️  pip-audit not available, install with: uv add --dev pip-audit$(NC)"

deps-check:
	@echo "$(BLUE)📦 Checking dependencies...$(NC)"
	uv tree
	@echo "$(BLUE)Outdated packages:$(NC)"
	uv tree --outdated || echo "$(YELLOW)⚠️  No outdated packages or command not available$(NC)"

# Build and distribution
build:
	@echo "$(BLUE)🏗️  Building package...$(NC)"
	uv build

install-local:
	@echo "$(BLUE)📦 Installing package locally...$(NC)"
	uv pip install -e .

# Documentation
docs-serve:
	@echo "$(BLUE)📚 Starting documentation server...$(NC)"
	@echo "$(YELLOW)Documentation would be served here (not implemented yet)$(NC)"

# Database and external services (if needed)
setup-test-db:
	@echo "$(BLUE)🗄️  Setting up test database...$(NC)"
	@echo "$(YELLOW)No database setup needed for MFCQI$(NC)"

# CI/CD helpers
ci-test: install test-all quality-check
	@echo "$(GREEN)🚀 CI pipeline completed successfully$(NC)"

ci-quick: install test quality-check
	@echo "$(GREEN)⚡ Quick CI pipeline completed$(NC)"

# Cleanup
clean:
	@echo "$(BLUE)🧹 Cleaning up...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name ".DS_Store" -delete 2>/dev/null || true
	find . -type f -name "*.prof" -delete 2>/dev/null || true
	rm -f bandit-report.json pylint-report.json 2>/dev/null || true
	@echo "$(GREEN)✅ Cleanup complete$(NC)"

clean-all: clean
	@echo "$(BLUE)🧹 Deep cleaning...$(NC)"
	uv cache clean
	rm -rf .venv/ 2>/dev/null || true
	@echo "$(GREEN)✅ Deep cleanup complete$(NC)"

# Research and analysis
research-validate:
	@echo "$(BLUE)🔬 Validating research implementation...$(NC)"
	@echo "$(YELLOW)Running validation against known research benchmarks...$(NC)"
	uv run python verify_pattern_metrics.py

sota-accuracy:
	@echo "$(BLUE)🎯 Testing SOTA detection accuracy...$(NC)"
	uv run python -c "from mfcqi.pattern_detection.integrated_detector import IntegratedPatternDetector; print('🔍 SOTA detection loaded successfully'); detector = IntegratedPatternDetector(); print('✅ All detection methods initialized')"

# Git hooks and pre-commit
pre-commit: format lint test-fast
	@echo "$(GREEN)✅ Pre-commit checks passed$(NC)"

# Environment info
env-info:
	@echo "$(BLUE)🔍 Environment Information:$(NC)"
	@echo "Python version: $$(python --version)"
	@echo "UV version: $$(uv --version)"
	@echo "Platform: $$(uname -s -r)"
	@echo "Architecture: $$(uname -m)"
	@echo "Current directory: $$(pwd)"
	@echo "Virtual environment: $${VIRTUAL_ENV:-Not activated}"

# Default target
.DEFAULT_GOAL := help