# Code Metrics Tracker Backlog

This document outlines planned improvements, fixes, and refactoring tasks for the Code Metrics Tracker project.

## Immediate Tasks

### 0. Refactor Parsing Implementation

- [x] **Refactor all tool output parsing to use proper JSON formats**
  - Convert radon CC parser to use JSON output properly
  - Convert cloc parser to use JSON output
  - Convert ruff parser to use JSON output
  - Priority: Critical
  - Effort: Medium
  - Completed in v0.1.4

- [x] **Create typed data structures for all metrics**
  - Define proper classes or TypedDict structures for each metric type
  - Ensure consistent data format throughout the application
  - Priority: High
  - Effort: Medium
  - Completed in v0.1.4

- [x] **Implement proper unit tests for parsing functions**
  - Create comprehensive tests for each parser
  - Ensure they handle edge cases properly
  - Priority: High
  - Effort: Medium
  - Completed in v0.1.4

- [x] **Remove workarounds and hacks**
  - Remove the function name mapping table in metrics.py
  - Replace regex-based parsers with direct JSON property access
  - Priority: High
  - Effort: Low
  - Completed in v0.1.4


### 1. Fix Linting Issues

- [ ] **Fix unused imports in cli.py**
  - Remove unused `os` import (F401)
  - Priority: High
  - Effort: Low

- [ ] **Fix unused variable in cli.py**
  - Address unused `list_parser` variable (F841)
  - Priority: High
  - Effort: Low

- [ ] **Fix f-string without placeholders in cli.py**
  - Replace `f"Snapshot added to CODE_METRICS.md"` with regular string (F541)
  - Priority: High
  - Effort: Low

- [ ] **Fix unused imports in metrics.py**
  - Remove unused `sys` import (F401)
  - Remove unused `pathlib.Path` import (F401)
  - Priority: High
  - Effort: Low

- [ ] **Fix f-strings without placeholders in metrics.py**
  - Replace f-strings without placeholders (line 913) with regular strings (F541)
  - Priority: High
  - Effort: Low

## Refactoring Tasks

### 1. Reduce Function Complexity

- [ ] **Refactor create_snapshot() function in metrics.py**
  - Break down into smaller, focused functions
  - Current complexity indicates this function is too large
  - Priority: Medium
  - Effort: High
  - Add tests before refactoring to ensure behavior is preserved

- [x] **Refactor JSON parsing in metrics.py**
  - Replace all string/regex parsing with proper JSON handling
  - Implement parse_radon_cc_json(), parse_ruff_json(), and parse_cloc_json() functions
  - Priority: High
  - Effort: Medium
  - Completed in v0.1.4

- [ ] **Refactor compare_snapshots() function in metrics.py**
  - Extract trend calculation logic into separate function
  - Priority: Medium
  - Effort: Medium
  - Add tests before refactoring

### 2. Improve Error Handling

- [ ] **Enhance error handling in CLI commands**
  - Add more descriptive error messages
  - Implement proper exception handling in the main function
  - Priority: Medium
  - Effort: Medium

- [ ] **Improve error handling in metrics processing**
  - Handle edge cases when tools return unexpected output
  - Priority: Medium
  - Effort: Medium

## Testing Tasks

- [ ] **Create unit tests for core functionality**
  - Set up pytest structure
  - Write tests for metrics calculation functions
  - Write tests for CLI commands
  - Priority: High
  - Effort: High

- [ ] **Create integration tests**
  - Test end-to-end workflow
  - Test with different project structures
  - Priority: Medium
  - Effort: High

- [ ] **Add test fixtures**
  - Create sample code for testing
  - Priority: Medium
  - Effort: Medium

## Feature Enhancements

- [ ] **Add customizable complexity thresholds**
  - Allow users to configure what constitutes high/medium/low complexity
  - Priority: Low
  - Effort: Medium

- [ ] **Add trend visualization**
  - Generate charts/graphs for metrics over time
  - Priority: Low
  - Effort: High

- [ ] **Add custom report templates**
  - Allow users to define their own report format
  - Priority: Low
  - Effort: High

- [ ] **Add support for more code quality tools**
  - Consider adding support for mypy, bandit, etc.
  - Priority: Low
  - Effort: High

## Documentation Improvements

- [ ] **Enhance function documentation**
  - Add detailed docstrings to all functions
  - Follow a consistent docstring format
  - Priority: Medium
  - Effort: Medium

- [ ] **Create API documentation**
  - Document the core API for programmatic usage
  - Priority: Low
  - Effort: Medium

- [ ] **Add tutorial documentation**
  - Create step-by-step examples for common workflows
  - Priority: Low
  - Effort: Medium

## Technical Debt Reduction

- [ ] **Modernize dependency handling**
  - Replace pkg_resources with importlib.resources
  - Priority: Medium
  - Effort: Low

- [ ] **Improve configuration file handling**
  - Use a more robust config parser
  - Priority: Low
  - Effort: Medium

## Implementation Notes

Before implementing any refactoring task:

1. Create unit tests that verify the current behavior
2. Document the expected inputs and outputs
3. Ensure tests pass after refactoring
4. Check that output formats remain backward compatible

For complex functions that need refactoring, consider:
- Breaking into smaller functions with single responsibilities
- Moving helper functions to separate modules if appropriate
- Using more descriptive variable names
- Adding assertions and input validation