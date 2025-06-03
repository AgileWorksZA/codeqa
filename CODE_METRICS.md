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

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,645 |
| Files | 9 |
| Comments | 669 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:40 B:18 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_005630.json](metrics/metrics_20250514_005630.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,645 | 669 | 543 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
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
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.56 |
| codeqa/snapshot_manager.py | A | 36.00 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| codeqa/metrics_parsing.py | A | 63.60 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 41 (2.6%) |
| Linting Issues | ↑ 2 (50.0%) |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 6 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,645 |
| Files | 9 |
| Comments | 669 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:40 B:18 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_005640.json](metrics/metrics_20250514_005640.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,645 | 669 | 543 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
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
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.56 |
| codeqa/snapshot_manager.py | A | 36.00 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
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
  - 6 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,645 |
| Files | 9 |
| Comments | 669 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:40 B:18 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_005647.json](metrics/metrics_20250514_005647.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,645 | 669 | 543 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
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
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.56 |
| codeqa/snapshot_manager.py | A | 36.00 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
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
  - 6 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 14, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,647 |
| Files | 9 |
| Comments | 669 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:40 B:18 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250514_005728.json](metrics/metrics_20250514_005728.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,647 | 669 | 543 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/metrics_parsing.py | B | 10 | parse_radon_cc_json |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
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
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.56 |
| codeqa/snapshot_manager.py | A | 35.89 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| codeqa/metrics_parsing.py | A | 63.60 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 2 (0.1%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 6 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,489 |
| Files | 7 |
| Comments | 659 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:55 B:23 C:7 D:2 E:1 F:0 |
| Maintainability Index | A:6 B:1 C:0 |
| Detailed Report | [metrics_20250517_134858.json](metrics/metrics_20250517_134858.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 7 | 1,489 | 659 | 510 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 18.93 |
| codeqa/snapshot_manager.py | A | 35.89 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↓ 158 (9.6%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↑ 2 (25.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 6 linting issues
  - 10 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,489 |
| Files | 7 |
| Comments | 659 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:55 B:23 C:7 D:2 E:1 F:0 |
| Maintainability Index | A:6 B:1 C:0 |
| Detailed Report | [metrics_20250517_141500.json](metrics/metrics_20250517_141500.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 7 | 1,489 | 659 | 510 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 18.93 |
| codeqa/snapshot_manager.py | A | 35.89 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
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
  - 6 linting issues
  - 10 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 572 |
| Files | 4 |
| Comments | 171 |
| Linting Issues | 33 |
| Cyclomatic Complexity | A:32 B:6 C:2 D:0 E:0 F:0 |
| Maintainability Index | A:4 B:0 C:0 |
| Detailed Report | [metrics_20250517_141819.json](metrics/metrics_20250517_141819.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 4 | 572 | 171 | 147 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| tests/test_basic.py | B | 10 | test_snapshot |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| tests/test_basic.py | test_snapshot | B | 10 |
| tests/test_files/complex_sample.py | medium_complex_function | B | 9 |
| tests/test_files/linting_sample.py | complex_function | B | 8 |
| tests/test_basic.py | test_init | B | 6 |
| tests/test_basic.py | test_compare | B | 6 |
| tests/test_files/complex_sample.py | ComplexityTestClass | B | 6 |
| tests/test_basic.py | TestCodeMetricsTracker | A | 5 |
| tests/test_basic.py | test_list | A | 5 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_files/linting_sample.py | 23 |
| tests/test_files/complex_sample.py | 5 |
| tests/test_parsing.py | 4 |
| src | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| tests/test_files/complex_sample.py | A | 44.38 |
| tests/test_basic.py | A | 51.71 |
| tests/test_parsing.py | A | 63.65 |
| tests/test_files/linting_sample.py | A | 67.39 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↓ 917 (61.6%) |
| Linting Issues | ↑ 27 (450.0%) |
| Complex Functions | ↓ 8 (80.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 33 linting issues
  - 2 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,489 |
| Files | 7 |
| Comments | 659 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:55 B:23 C:7 D:2 E:1 F:0 |
| Maintainability Index | A:6 B:1 C:0 |
| Detailed Report | [metrics_20250517_141849.json](metrics/metrics_20250517_141849.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 7 | 1,489 | 659 | 510 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 18.93 |
| codeqa/snapshot_manager.py | A | 35.89 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 917 (160.3%) |
| Linting Issues | ↓ 27 (81.8%) |
| Complex Functions | ↑ 8 (400.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 6 linting issues
  - 10 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,681 |
| Files | 9 |
| Comments | 702 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:41 B:20 C:5 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250517_122259.json](metrics/metrics_20250517_122259.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 9 | 1,681 | 702 | 563 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
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
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 19.05 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 192 (12.9%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↓ 2 (20.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 6 linting issues
  - 8 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,489 |
| Files | 7 |
| Comments | 659 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:55 B:23 C:7 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250517_122543.json](metrics/metrics_20250517_122543.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 7 | 1,489 | 659 | 510 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 19.05 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
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
  - 6 linting issues
  - 10 high complexity functions
  - 0 files with low maintainability

### May 17, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,489 |
| Files | 7 |
| Comments | 659 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:55 B:23 C:7 D:2 E:1 F:0 |
| Maintainability Index | A:7 B:0 C:0 |
| Detailed Report | [metrics_20250517_131737.json](metrics/metrics_20250517_131737.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 7 | 1,489 | 659 | 510 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 19.05 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
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
  - 6 linting issues
  - 10 high complexity functions
  - 0 files with low maintainability

### May 24, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,491 |
| Files | 7 |
| Comments | 661 |
| Linting Issues | 6 |
| Cyclomatic Complexity | A:55 B:23 C:7 D:2 E:1 F:0 |
| Maintainability Index | A:6 B:1 C:0 |
| Detailed Report | [metrics_20250524_211857.json](metrics/metrics_20250524_211857.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 7 | 1,491 | 661 | 510 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 26 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 26 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |
| codeqa/metrics.py | get_formatted_trend | C | 12 |
| codeqa/snapshot_manager.py | get_formatted_trend | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 18.57 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 60.11 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/metrics_parsing.py | A | 65.30 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 2 (0.1%) |
| Linting Issues | ↑ 0 (0.0%) |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 6 linting issues
  - 10 high complexity functions
  - 0 files with low maintainability

### June 03, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,922 |
| Files | 11 |
| Comments | 930 |
| Linting Issues | 9 |
| Cyclomatic Complexity | A:79 B:26 C:10 D:2 E:1 F:0 |
| Maintainability Index | A:10 B:1 C:0 |
| Detailed Report | [metrics_20250603_130339.json](metrics/metrics_20250603_130339.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 11 | 1,922 | 930 | 683 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 28 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/gitignore_parser.py | C | 11 | filter_patterns |
| codeqa/pattern_translator.py | B | 10 | PatternTranslator |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 28 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | build_cloc_exclude_args | C | 18 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| codeqa/metrics.py | init_project | C | 15 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/gitignore_parser.py | 3 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 16.31 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 59.02 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/pattern_translator.py | A | 63.92 |
| codeqa/gitignore_parser.py | A | 64.99 |
| codeqa/metrics_parsing.py | A | 65.30 |
| tests/test_gitignore_parser.py | A | 73.74 |
| tests/test_pattern_translator.py | A | 77.90 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 433 (29.1%) |
| Linting Issues | ↑ 3 (50.0%) |
| Complex Functions | ↑ 3 (30.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 9 linting issues
  - 13 high complexity functions
  - 0 files with low maintainability

### June 03, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,922 |
| Files | 11 |
| Comments | 930 |
| Linting Issues | 9 |
| Cyclomatic Complexity | A:79 B:26 C:10 D:2 E:1 F:0 |
| Maintainability Index | A:10 B:1 C:0 |
| Detailed Report | [metrics_20250603_130519.json](metrics/metrics_20250603_130519.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 11 | 1,922 | 930 | 683 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 28 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/gitignore_parser.py | C | 11 | filter_patterns |
| codeqa/pattern_translator.py | B | 10 | PatternTranslator |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 28 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | build_cloc_exclude_args | C | 18 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| codeqa/metrics.py | init_project | C | 15 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/gitignore_parser.py | 3 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 16.31 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 59.02 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/pattern_translator.py | A | 63.92 |
| codeqa/gitignore_parser.py | A | 64.99 |
| codeqa/metrics_parsing.py | A | 65.30 |
| tests/test_gitignore_parser.py | A | 73.74 |
| tests/test_pattern_translator.py | A | 77.90 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 433 (29.1%) |
| Linting Issues | ↑ 3 (50.0%) |
| Complex Functions | ↑ 3 (30.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 9 linting issues
  - 13 high complexity functions
  - 0 files with low maintainability

### June 03, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 1,922 |
| Files | 11 |
| Comments | 930 |
| Linting Issues | 9 |
| Cyclomatic Complexity | A:79 B:26 C:10 D:2 E:1 F:0 |
| Maintainability Index | A:10 B:1 C:0 |
| Detailed Report | [metrics_20250603_143953.json](metrics/metrics_20250603_143953.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 11 | 1,922 | 930 | 683 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | E | 39 | create_snapshot |
| codeqa/cli.py | D | 28 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/gitignore_parser.py | C | 11 | filter_patterns |
| codeqa/pattern_translator.py | B | 10 | PatternTranslator |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_parsing.py | A | 3 | TestRadonParsing |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | E | 39 |
| codeqa/cli.py | main | D | 28 |
| codeqa/metrics.py | get_code_stats | D | 25 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | build_cloc_exclude_args | C | 18 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| codeqa/metrics.py | init_project | C | 15 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/gitignore_parser.py | 3 |
| codeqa/metrics.py | 1 |
| codeqa/snapshot_manager.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 16.31 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 51.71 |
| codeqa/cli.py | A | 59.02 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/pattern_translator.py | A | 63.92 |
| codeqa/gitignore_parser.py | A | 64.99 |
| codeqa/metrics_parsing.py | A | 65.30 |
| tests/test_gitignore_parser.py | A | 73.74 |
| tests/test_pattern_translator.py | A | 77.90 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 433 (29.1%) |
| Linting Issues | ↑ 3 (50.0%) |
| Complex Functions | ↑ 3 (30.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 9 linting issues
  - 13 high complexity functions
  - 0 files with low maintainability

### June 03, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 2,118 |
| Files | 13 |
| Comments | 981 |
| Linting Issues | 11 |
| Cyclomatic Complexity | A:87 B:27 C:9 D:3 E:0 F:1 |
| Maintainability Index | A:12 B:1 C:0 |
| Detailed Report | [metrics_20250603_180453.json](metrics/metrics_20250603_180453.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 13 | 2,118 | 981 | 732 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | F | 43 | create_snapshot |
| codeqa/cli.py | D | 30 | main |
| tests/test_files/complex_sample.py | C | 19 | very_complex_function |
| codeqa/snapshot_manager.py | C | 16 | compare_snapshots |
| codeqa/gitignore_parser.py | C | 11 | filter_patterns |
| codeqa/pattern_translator.py | B | 10 | PatternTranslator |
| tests/test_basic.py | B | 10 | test_snapshot |
| codeqa/metrics_parsing.py | B | 9 | parse_radon_cc_json |
| tests/test_files/linting_sample.py | B | 8 | complex_function |
| tests/test_gitignore_comments.py | A | 3 | TestGitignoreComments |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | create_snapshot | F | 43 |
| codeqa/cli.py | main | D | 30 |
| codeqa/metrics.py | get_code_stats | D | 26 |
| codeqa/metrics.py | init_project | D | 22 |
| tests/test_files/complex_sample.py | very_complex_function | C | 19 |
| codeqa/metrics.py | build_cloc_exclude_args | C | 16 |
| codeqa/metrics.py | compare_snapshots | C | 16 |
| codeqa/snapshot_manager.py | compare_snapshots | C | 16 |
| tests/test_files/complex_sample.py | complex_method | C | 14 |
| codeqa/metrics.py | parse_ruff_output | C | 12 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| tests/test_parsing.py | 4 |
| codeqa/gitignore_parser.py | 3 |
| codeqa/metrics.py | 2 |
| codeqa/snapshot_manager.py | 1 |
| tests/test_gitignore_comments.py | 1 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | B | 13.77 |
| codeqa/snapshot_manager.py | A | 36.11 |
| tests/test_basic.py | A | 52.02 |
| codeqa/cli.py | A | 57.95 |
| tests/test_parsing.py | A | 63.65 |
| codeqa/pattern_translator.py | A | 63.92 |
| codeqa/gitignore_parser.py | A | 64.40 |
| codeqa/metrics_parsing.py | A | 65.30 |
| tests/test_gitignore_parser.py | A | 73.74 |
| tests/test_pattern_translator.py | A | 77.90 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 629 (42.2%) |
| Linting Issues | ↑ 5 (83.3%) |
| Complex Functions | ↑ 3 (30.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 11 linting issues
  - 13 high complexity functions
  - 0 files with low maintainability

