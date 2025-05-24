# Changelog

All notable changes to the Code Metrics Tracker project will be documented in this file.

## [0.1.9] - 2025-05-22

### Fixed
- Fixed cloc command failure when exclude patterns contain wildcards (e.g., `*.db`, `config/*.yaml`)
- Improved pattern handling in `build_cloc_exclude_args()` to correctly:
  - Convert `*.ext` patterns to `--exclude-ext=ext` 
  - Skip complex wildcard patterns that cloc doesn't support
  - Only pass simple directory names and paths to `--exclude-dir`

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