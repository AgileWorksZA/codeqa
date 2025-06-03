# Changelog

All notable changes to the Code Metrics Tracker project will be documented in this file.

## [0.1.17] - 2025-06-03

### Changed
- **BREAKING**: Changed default behavior to only update CODE_METRICS.md when significant changes are detected
- Replaced `--only-on-changes` flag with `--force-update` flag for opposite behavior
- Now preserves CODE_METRICS.md unless there are meaningful metric changes or `--force-update` is used

## [0.1.16] - 2025-06-03

### Fixed
- Fixed CODE_METRICS.md updates - new snapshots now correctly appear at the top of Historical Snapshots section
- Added verbose feedback for successful file updates

## [0.1.15] - 2025-06-03

### Changed
- Reduced verbose output in production mode - detailed command output only shown with `--verbose` flag
- Added user-friendly progress messages for each analysis step
- Improved output clarity with emojis for verbose mode

## [0.1.14] - 2025-06-03

### Fixed
- Fixed cloc error "cannot specify directory paths" for patterns containing forward slashes
- Directory path patterns (like `data/simplepay/exports`) now correctly use regex instead of `--exclude-dir`

## [0.1.13] - 2025-06-03

### Fixed
- Fixed pkg_resources deprecation warning by using importlib.resources for Python 3.7+
- Improved compatibility with Python 3.13 and setuptools 81+

## [0.1.12] - 2025-06-03

### Added
- New `--force` flag for `codeqa init` to backup existing config and reinitialize
- Automatic stripping of inline comments from .gitignore patterns (e.g., `*.db # Database files` → `*.db`)

### Fixed
- Fixed issue where inline comments in .gitignore patterns would cause cloc errors
- Improved backup naming for multiple force initializations (adds incremental numbers)

## [0.1.11] - 2025-06-03

### Added
- New `--from-gitignore` flag for `codeqa init` to initialize exclude patterns from .gitignore
- New `--all-gitignore-patterns` flag to include all .gitignore patterns without filtering
- Pattern suggestions based on detected project type (Python, JavaScript, etc.)
- `GitignoreParser` class for parsing and converting .gitignore patterns
- `PatternTranslator` class for converting patterns between tool-specific formats

### Fixed
- Fixed cloc "cannot specify directory paths" error by using `--not-match-d` with regex for complex patterns
- Fixed cloc command failure when exclude patterns contain wildcards (e.g., `*.db`, `config/*.yaml`)
- Improved pattern handling for all tools (cloc, ruff, radon) to ensure consistent exclusions
- Fixed radon pattern handling to use `-i` for directories and `-e` for file patterns

## [0.1.6] - 2025-05-14

### Added
- Improved change detection in `--only-on-changes` flag
- Debug output showing which metrics changed between snapshots
- Clear messages when no changes are detected

### Fixed
- Fixed JSON field path references in snapshot comparison
- Corrected "_unchanged" suffix to JSON files when no changes detected

## [0.1.5] - 2025-05-14

### Fixed
- Fixed bug in Radon CC JSON parsing where string entries caused AttributeError

## [0.1.4] - 2023-05-14

### Added
- New `metrics_parsing.py` module with dedicated parsers for each tool
- TypedDict definitions for all metrics data structures
- Comprehensive test suite for parser functions
- `snapshot_manager.py` to reduce complexity in `metrics.py`

### Changed
- Refactored all tool output parsing to use JSON format:
  - Radon CC now properly uses JSON output with direct property access
  - Ruff now uses JSON output format for structured data
  - Cloc now uses JSON output for consistency
- Removed function name mapping workaround in favor of proper JSON parsing
- Refactored the create_snapshot function for better maintainability
- Improved documentation and type annotations

### Fixed
- Fixed cyclomatic complexity display for functions in reports
- Fixed handling of multi-word language names in cloc output
- Fixed compatibility with newer Radon versions

## [0.1.3] - 2023-04-30

### Added
- Comprehensive documentation and examples
- Detailed development guide to README

### Changed
- Updated project description in PyPI metadata

## [0.1.2] - 2023-04-15

### Added
- Enhanced project description in PyPI listing

## [0.1.1] - 2023-04-01

### Changed
- Renamed package to code-metrics-tracker for PyPI compatibility

## [0.1.0] - 2023-03-15

### Added
- Initial release with core functionality
- Support for cloc, ruff, and radon metrics
- Command-line interface with init, snapshot, list, compare, and report commands
- Markdown report generation
- JSON snapshot storage