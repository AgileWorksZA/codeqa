# Code Metrics Tracker (codeqa)

## Project Overview

This tool tracks code quality metrics for Python projects, generating reports that highlight code quality trends over time.

- **Package name**: code-metrics-tracker
- **Current version**: 0.1.11
- **Repository**: https://github.com/AgileWorksZA/codeqa
- **PyPI**: https://pypi.org/project/code-metrics-tracker/

The tool uses three specialized analyzers:
1. **cloc**: Counts lines of code, comments, and blank lines
2. **Ruff**: Identifies linting issues and code style violations
3. **Radon**: Analyzes code complexity (cyclomatic complexity) and maintainability

## Key Files and Architecture

### Core Implementation

- `codeqa/__init__.py`: Version definition (`__version__ = "0.1.11"`)
- `codeqa/cli.py`: CLI command parser and entry point
- `codeqa/metrics.py`: Core implementation with all metrics functionality
- `codeqa/gitignore_parser.py`: NEW - Parses .gitignore files and converts patterns for codeqa
- `codeqa/pattern_translator.py`: NEW - Translates patterns between different tool formats

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
   - `setup.py` - `version="0.1.11"` parameter
   - `codeqa/__init__.py` - `__version__ = "0.1.11"` variable

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
  - `--from-gitignore`: Initialize exclude patterns from .gitignore file (NEW in 0.1.11)
  - `--all-gitignore-patterns`: Include all .gitignore patterns without filtering (NEW in 0.1.11)
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
  "exclude_patterns": ["migrations", ".coverage", "*.db", "*.log"]
}
```

Note: Many common patterns (like `.git`, `.venv`, `__pycache__`) are already excluded by the tools themselves, so the config only needs project-specific exclusions.

## New Feature: Initialize from .gitignore (v0.1.11)

### --from-gitignore Flag

The `--from-gitignore` option automatically reads your project's `.gitignore` file and configures exclude patterns to ensure consistency between what git ignores and what codeqa excludes from analysis.

```bash
# Initialize with patterns from .gitignore
codeqa init --from-gitignore

# Include ALL .gitignore patterns without filtering
codeqa init --from-gitignore --all-gitignore-patterns
```

### Pattern Filtering

By default, some .gitignore patterns are filtered out as they might contain code you want to analyze:
- IDE configuration files (`.idea/`, `.vscode/`)
- Environment files (`.env`, `.env.local`)
- Log files (`*.log`, `logs/`)
- OS-specific files (`.DS_Store`, `Thumbs.db`)
- Node.js dependencies (`node_modules/`)
- Git directory (`.git/`)

Use `--all-gitignore-patterns` to include these patterns anyway.

### Smart Project Detection

The tool detects your project type and suggests additional patterns:
- **Python projects**: Suggests `.coverage`, `htmlcov/`, `.pytest_cache/`, etc.
- **JavaScript projects**: Suggests `dist/`, `build/`, `.next/`, etc.
- **General projects**: Suggests common development artifacts

### Pattern Translation

The GitignoreParser and PatternTranslator work together to:
1. Parse .gitignore patterns using standard gitignore syntax
2. Filter questionable patterns (unless `--all-gitignore-patterns` is used)
3. Translate patterns to each tool's specific format:
   - **cloc**: Uses `--exclude-dir`, `--exclude-ext`, and `--not-match-d` with regex
   - **Ruff**: Uses glob patterns with `--exclude`
   - **Radon**: Uses `-i` for directories, `-e` for file patterns

### Implementation Details

Key components added in v0.1.11:
- `GitignoreParser.parse_gitignore()`: Reads and filters .gitignore patterns
- `GitignoreParser.suggest_additional_patterns()`: Suggests project-specific patterns
- `PatternTranslator.patterns_to_cloc_args()`: Converts patterns for cloc
- `PatternTranslator.patterns_to_ruff_globs()`: Converts patterns for ruff  
- `PatternTranslator.patterns_to_radon_args()`: Converts patterns for radon

### Bug Fixes in v0.1.11

- **Fixed cloc wildcard handling**: cloc now uses `--not-match-d` with regex for complex patterns instead of failing with "cannot specify directory paths" error
- **Improved pattern consistency**: All tools now handle the same exclude patterns correctly
- **Enhanced error handling**: Better validation and error messages for pattern translation

## Output Files

1. `CODE_METRICS.md`: Main report with historical metrics
2. `generated/metrics/metrics_YYYYMMDD_HHMMSS.json`: Snapshot data in JSON format

## Dependencies

- **Python**: 3.7+
- **External binary**: cloc (must be installed separately)
- **Python packages**:
  - ruff >= 0.0.254
  - radon >= 5.1.0

## Testing

The project includes comprehensive tests for the new functionality:
- `tests/test_gitignore_parser.py`: Tests for GitignoreParser functionality
- `tests/test_pattern_translator.py`: Tests for PatternTranslator functionality
- `tests/test_basic.py`: Core functionality tests
- `tests/test_parsing.py`: Metrics parsing tests

Run tests with:
```bash
python -m pytest tests/
```