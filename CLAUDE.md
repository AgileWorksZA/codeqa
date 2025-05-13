# Code Metrics Tracker (codeqa)

## Project Overview

This tool tracks code quality metrics for Python projects, generating reports that highlight code quality trends over time.

- **Package name**: code-metrics-tracker
- **Current version**: 0.1.6
- **Repository**: https://github.com/AgileWorksZA/codeqa
- **PyPI**: https://pypi.org/project/code-metrics-tracker/

The tool uses three specialized analyzers:
1. **cloc**: Counts lines of code, comments, and blank lines
2. **Ruff**: Identifies linting issues and code style violations
3. **Radon**: Analyzes code complexity (cyclomatic complexity) and maintainability

## Key Files and Architecture

### Core Implementation

- `codeqa/__init__.py`: Version definition (`__version__ = "0.1.6"`)
- `codeqa/cli.py`: CLI command parser and entry point
- `codeqa/metrics.py`: Core implementation with all metrics functionality

### Templates

- `codeqa/templates/CODE_METRICS.md.template`: Template for the markdown report
- `codeqa/templates/codeqa.json.template`: Default configuration template
- `codeqa/templates/github-workflow.yml.template`: GitHub Actions integration

### Distribution and Setup

- `setup.py`: Package metadata, dependencies, and entry points
- `MANIFEST.in`: Ensures templates are included in distribution

## Development Workflow

### Local Development Setup

1. Clone repository: `git clone https://github.com/AgileWorksZA/codeqa.git`
2. Install in dev mode: `pip install -e .`
3. Install development dependencies: `pip install build twine`

### Creating a Release

1. Update versions in:
   - `setup.py` - `version="0.1.6"` parameter
   - `codeqa/__init__.py` - `__version__ = "0.1.6"` variable

2. Build the package:
   ```bash
   rm -rf dist/ build/ *.egg-info/
   python -m build
   ```

3. Local testing:
   ```bash
   pip install dist/*.whl
   ```

## Publishing to PyPI

**IMPORTANT**: Credentials for PyPI are stored in `~/.pypirc`. This file contains the authentication details needed for uploading to PyPI.

1. Ensure the PyPI credentials in `~/.pypirc` are correct
2. Upload to PyPI using one of these methods:
   ```bash
   # Using saved credentials in ~/.pypirc
   python -m twine upload dist/*
   
   # Or using token authentication
   python -m twine upload --username __token__ --password your-pypi-token dist/*
   ```

3. Verify the package is available: https://pypi.org/project/code-metrics-tracker/

## Command Overview

- `codeqa init`: Initialize project with config file and templates
- `codeqa snapshot`: Create a new metrics snapshot and update report
- `codeqa list`: List all available snapshots
- `codeqa compare`: Compare two snapshots to analyze trends
- `codeqa report`: Generate a standalone report from a snapshot

## Configuration

The tool uses a `codeqa.json` configuration file with:
- `include_paths`: Directories to include in analysis
- `exclude_patterns`: File patterns to exclude

Default configuration:
```json
{
  "include_paths": ["src", "tests"],
  "exclude_patterns": ["venv", "site-packages", "__pycache__", ".pyc"]
}
```

## Output Files

1. `CODE_METRICS.md`: Main report with historical metrics
2. `generated/metrics/metrics_YYYYMMDD_HHMMSS.json`: Snapshot data in JSON format

## Dependencies

- **Python**: 3.7+
- **External binary**: cloc (must be installed separately)
- **Python packages**:
  - ruff >= 0.0.254
  - radon >= 5.1.0