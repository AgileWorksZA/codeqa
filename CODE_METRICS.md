# Code Quality Metrics

This file tracks code quality metrics over time to help monitor and improve our codebase.

## Metrics Definitions

### Ruff Metrics

- **Issues Count**: Total number of linting issues detected by Ruff
- **Issues by Type**: Distribution of error types (unused imports, undefined names, etc.)

### Radon Complexity Metrics (CC)

- **A**: CC score 1-5 (low complexity)
- **B**: CC score 6-10 (moderate complexity)
- **C**: CC score 11-20 (high complexity)
- **D**: CC score 21-30 (very high complexity)
- **E**: CC score 31-40 (extremely high complexity)
- **F**: CC score 41+ (alarming complexity)

### Radon Maintainability Metrics (MI)

- **A**: MI score 20-100 (high maintainability)
- **B**: MI score 10-19 (medium maintainability)
- **C**: MI score 0-9 (low maintainability)

## Historical Snapshots

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,561 |
| Files | 9 |
| Comments | 637 |
| Linting Issues | 4 |
| Cyclomatic Complexity | A:11 B:3 C:9 D:0 E:0 F:41 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_000310.json](metrics/metrics_20250514_000310.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,561 | 637 | 518 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| tests/test_basic.py | B | 10 | TestCodeMetricsTracker.test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing.test_radon_cc_json_parsing |
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/snapshot_manager.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |
| codeqa/metrics_parsing.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| tests/test_basic.py | TestCodeMetricsTracker.test_snapshot | B | 10 |
| tests/test_basic.py | TestCodeMetricsTracker.test_init | B | 6 |
| tests/test_basic.py | TestCodeMetricsTracker.test_compare | B | 6 |
| tests/test_basic.py | TestCodeMetricsTracker.test_list | A | 5 |
| tests/test_basic.py | TestCodeMetricsTracker.test_report | A | 5 |
| tests/test_parsing.py | TestRadonParsing.test_radon_cc_json_parsing | A | 3 |
| tests/test_parsing.py | TestRadonParsing.setUp | A | 1 |
| tests/test_parsing.py | TestRuffParsing.setUp | A | 1 |
| tests/test_parsing.py | TestRuffParsing.test_ruff_json_parsing | A | 1 |
| tests/test_parsing.py | TestClocParsing.setUp | A | 1 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 22.24 |
| codeqa/snapshot_manager.py | A | 36.38 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 61.43 |
| codeqa/metrics_parsing.py | A | 64.16 |
| tests/test_parsing.py | A | 66.88 |
| codeqa/__init__.py | A | 100.00 |


#### Analysis
- Critical issues to address:
  - 4 linting issues
  - 50 high complexity functions
  - 0 files with low maintainability

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,604 |
| Files | 9 |
| Comments | 647 |
| Linting Issues | 4 |
| Cyclomatic Complexity | A:40 B:17 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_002745.json](metrics/metrics_20250514_002745.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,604 | 647 | 526 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 35 | create_snapshot |
| codeqa/cli.py | D | 23 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 35 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| codeqa/cli.py | main | D | 23 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |
| codeqa/metrics.py | list_snapshots | B | 10 |
| codeqa/snapshot_manager.py | list_snapshots | B | 10 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 22.24 |
| codeqa/snapshot_manager.py | A | 36.38 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 61.43 |
| codeqa/metrics_parsing.py | A | 63.60 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 43 (2.8%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↓ 42 (84.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 4 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,604 |
| Files | 9 |
| Comments | 647 |
| Linting Issues | 4 |
| Cyclomatic Complexity | A:40 B:17 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_003503.json](metrics/metrics_20250514_003503.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,604 | 647 | 526 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 35 | create_snapshot |
| codeqa/cli.py | D | 23 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 35 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| codeqa/cli.py | main | D | 23 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |
| codeqa/metrics.py | list_snapshots | B | 10 |
| codeqa/snapshot_manager.py | list_snapshots | B | 10 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 22.24 |
| codeqa/snapshot_manager.py | A | 36.38 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 61.43 |
| codeqa/metrics_parsing.py | A | 63.60 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 0 (0.0%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 4 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,604 |
| Files | 9 |
| Comments | 647 |
| Linting Issues | 4 |
| Cyclomatic Complexity | A:40 B:17 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250513_223623.json](metrics/metrics_20250513_223623.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,604 | 647 | 526 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 35 | create_snapshot |
| codeqa/cli.py | D | 23 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 35 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| codeqa/cli.py | main | D | 23 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | list_snapshots | B | 10 |
| codeqa/snapshot_manager.py | format_snapshot_markdown | B | 10 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 22.37 |
| codeqa/snapshot_manager.py | A | 36.61 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 61.43 |
| codeqa/metrics_parsing.py | A | 63.60 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 0 (0.0%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 4 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

