# Installation Guide

## Prerequisites

Before installing CodeQA, make sure you have:

1. Python 3.7 or higher installed
2. `pip` package manager
3. `cloc` command-line tool for counting lines of code

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
pip install codeqa
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