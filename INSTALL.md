# Installation Guide

## Prerequisites

Before installing CodeQA, make sure you have:

1. Python 3.7 or higher installed
2. `pip` package manager
3. `cloc` command-line tool for counting lines of code

Note: setuptools will be installed automatically as a dependency if not already available.

## Installing cloc

### On macOS:
```bash
brew install cloc
```

### On Ubuntu/Debian:
```bash
sudo apt-get install cloc
```

### On Windows:
```bash
# Using Chocolatey
choco install cloc

# Or download directly from: https://github.com/AlDanial/cloc/releases/
```

## Installing CodeQA

### From PyPI

```bash
pip install code-metrics-tracker
```

### From Source

```bash
git clone https://github.com/AgileWorksZA/codeqa.git
cd codeqa
pip install -e .
```

## Verifying Installation

After installation, verify that CodeQA is working correctly:

```bash
codeqa --version
```

You should see the version number of CodeQA printed on the console.

## Initializing a Project

Navigate to your project directory and run:

```bash
codeqa init
```

This will create a basic configuration file (`codeqa.json`) and a CODE_METRICS.md file in your project.

## Updating Configuration

Edit the `codeqa.json` file to customize:

- `include_paths`: Directories to include in analysis
- `exclude_patterns`: Patterns to exclude from analysis

For example:

```json
{
  "include_paths": ["src", "lib", "tests"],
  "exclude_patterns": ["venv", "site-packages", "__pycache__", ".pyc", "node_modules"]
}
```

## Creating Your First Snapshot

After configuring, generate your first code quality snapshot:

```bash
codeqa snapshot
```

This will analyze your codebase and update the CODE_METRICS.md file.

## GitHub Actions Integration

To automate code quality tracking in your repository, add a workflow file at `.github/workflows/code-quality.yml`:

```yaml
name: Code Quality Metrics

on:
  push:
    branches: [ main ]

jobs:
  code-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install cloc
        run: sudo apt-get install -y cloc
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install code-metrics-tracker
      - name: Generate code quality snapshot
        run: codeqa snapshot --only-on-changes
      - name: Commit updated CODE_METRICS.md
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Update code quality metrics"
          file_pattern: CODE_METRICS.md generated/metrics/*
```

### ⚠️ Critical: Use Latest Action Versions

**Always use the latest versions of GitHub Actions** to avoid deprecation errors:

- ✅ `actions/checkout@v4` (not v3)
- ✅ `actions/setup-python@v5` (not v4) 
- ✅ `stefanzweifel/git-auto-commit-action@v5` (not v4)

**Deprecated versions will cause workflow failures** with messages like:
```
This request has been automatically failed because it uses a deprecated version of `actions/upload-artifact: v3`.
```

Using outdated action versions is the most common cause of GitHub Actions failures with CodeQA workflows.