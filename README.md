# Code Metrics Tracker

[![PyPI Version](https://img.shields.io/pypi/v/code-metrics-tracker.svg)](https://pypi.org/project/code-metrics-tracker/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/code-metrics-tracker.svg)](https://pypi.org/project/code-metrics-tracker/)

A powerful code quality metrics tracking tool for Python projects that helps teams monitor and improve their codebase over time. Code Metrics Tracker leverages three specialized tools to provide comprehensive analysis:

- **cloc**: Counts lines of code, comments, and blank lines across programming languages
- **Ruff**: Identifies linting issues, code style violations, and potential bugs with fast performance
- **Radon**: Analyzes code complexity (cyclomatic complexity) and maintainability

The tracker generates detailed reports focusing on:

- **Lines of code statistics**: Track code volume and distribution by language
- **Linting issues**: Detect and monitor code style, potential bugs, and anti-patterns
- **Cyclomatic complexity**: Identify complex functions and methods that need refactoring
- **Maintainability index**: Measure how maintainable your code is over time

Results are stored in two complementary formats:
1. **JSON snapshots**: Detailed metrics data stored in versioned JSON files for programmatic analysis
2. **Markdown reports**: Human-readable CODE_METRICS.md file that tracks metrics over time with trend indicators

Perfect for teams that want to:
- Track code quality trends over time
- Identify problematic areas in the codebase
- Make data-driven refactoring decisions
- Establish quality standards with measurable metrics
- Integrate metrics tracking into CI/CD pipelines

## Installation

### Install from PyPI

```bash
pip install code-metrics-tracker
```

### Install Required Dependencies

The tool relies on three external tools that need to be installed separately:

#### 1. Install cloc

```bash
# macOS
brew install cloc

# Ubuntu/Debian
sudo apt-get install cloc

# Windows
choco install cloc
```

#### 2. Install Ruff and Radon

These are automatically installed as dependencies when you install code-metrics-tracker, but you can also install them directly:

```bash
pip install ruff radon
```

## Quick Start

1. Initialize code quality tracking in your project:

```bash
codeqa init
```

2. Create a code quality snapshot:

```bash
codeqa snapshot
```

3. View the generated CODE_METRICS.md file for detailed metrics.

## Features

- Track code quality metrics over time
- Generate formatted Markdown reports
- Compare snapshots to identify trends
- Highlight critical issues to address
- Configurable for different project structures

## Commands

- `codeqa init` - Initialize code quality tracking in your project
- `codeqa snapshot` - Create a new code quality snapshot
- `codeqa list` - List all available snapshots
- `codeqa compare` - Compare two snapshots to see trends
- `codeqa report` - Generate a standalone report from a snapshot

## Configuration

The tool uses a `codeqa.json` configuration file to determine which directories to analyze, focusing only on code maintained by your team.

Example configuration:

```json
{
  "include_paths": ["src", "tests"],
  "exclude_patterns": ["venv", "site-packages", "__pycache__", ".pyc"]
}
```

## GitHub Actions Integration

Add this to your GitHub Actions workflow to automatically track code quality metrics:

```yaml
name: Code Quality Metrics

on:
  push:
    branches: [ main ]

jobs:
  code-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install cloc
        run: sudo apt-get install -y cloc
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install code-metrics-tracker
      - name: Generate code quality snapshot
        run: codeqa snapshot
      - name: Commit updated CODE_METRICS.md
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "Update code quality metrics"
          file_pattern: CODE_METRICS.md generated/metrics/*
```

## Development Guide

### Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/AgileWorksZA/codeqa.git
cd codeqa
```

2. Install in development mode:
```bash
pip install -e .
```

3. Install development dependencies:
```bash
pip install build twine
```

### Creating a New Release

1. Update version numbers in both files:
   - `setup.py` - Update the `version` parameter
   - `codeqa/__init__.py` - Update the `__version__` variable

2. Update the README.md with any new features or changes

3. Build the package:
```bash
rm -rf dist/ build/ *.egg-info/
python -m build
```

4. Test the package locally:
```bash
pip install dist/*.whl
```

### Publishing to PyPI

1. Install publishing tools if you haven't already:
```bash
pip install twine
```

2. Create a `.pypirc` file in your home directory with your PyPI credentials:
```ini
[pypi]
username = your_username
password = your_password
```

3. Upload to PyPI:
```bash
python -m twine upload dist/*
```

4. Alternatively, use a token for authentication:
```bash
python -m twine upload --username __token__ --password your-pypi-token dist/*
```

5. Verify the package is available on PyPI:
https://pypi.org/project/code-metrics-tracker/

### Committing Changes to GitHub

1. Add and commit your changes:
```bash
git add .
git commit -m "Release version X.Y.Z with [brief description]"
```

2. Push to GitHub:
```bash
git push origin main
```

3. Create a GitHub release:
   - Go to the repository's Releases page
   - Click "Draft a new release"
   - Tag version: vX.Y.Z
   - Title: Version X.Y.Z
   - Description: Add release notes
   - Publish release

## License

MIT