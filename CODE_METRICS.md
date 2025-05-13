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

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 659 |
| Files | 3 |
| Comments | 258 |
| Linting Issues | 7 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:18 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_173634.json](metrics/metrics_20250513_173634.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 659 | 258 | 219 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | E (36) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (15) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| codeqa/metrics.py | 4 |
| codeqa/cli.py | 3 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 19.42 |
| codeqa/cli.py | A | 61.25 |
| codeqa/__init__.py | A | 100.00 |


#### Analysis
- Critical issues to address:
  - 7 linting issues
  - 18 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 659 |
| Files | 3 |
| Comments | 258 |
| Linting Issues | 7 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:18 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_173711.json](metrics/metrics_20250513_173711.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 659 | 258 | 219 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | E (36) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (15) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
| File | Issues |
|------|--------|
| codeqa/metrics.py | 4 |
| codeqa/cli.py | 3 |


#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 19.42 |
| codeqa/cli.py | A | 61.25 |
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
  - 7 linting issues
  - 18 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 641 |
| Files | 3 |
| Comments | 256 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:18 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191123.json](metrics/metrics_20250513_191123.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 641 | 256 | 215 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | E (36) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 20.42 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↓ 18 (2.7%) |
| Linting Issues | ↓ 7 (100.0%) |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 18 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 650 |
| Files | 3 |
| Comments | 257 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:18 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191244.json](metrics/metrics_20250513_191244.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 650 | 257 | 216 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | E (36) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (9) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 20.69 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 9 (1.4%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 18 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 641 |
| Files | 3 |
| Comments | 257 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:18 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191326.json](metrics/metrics_20250513_191326.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 641 | 257 | 216 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | E (36) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 20.47 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↓ 9 (1.4%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 18 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 627 |
| Files | 3 |
| Comments | 254 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:17 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191426.json](metrics/metrics_20250513_191426.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 627 | 254 | 213 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | E (40) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.51 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↓ 14 (2.2%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↓ 1 (5.6%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 17 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 631 |
| Files | 3 |
| Comments | 255 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:17 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191540.json](metrics/metrics_20250513_191540.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 631 | 255 | 214 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | F (41) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.27 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 4 (0.6%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 17 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 632 |
| Files | 3 |
| Comments | 258 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:17 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191634.json](metrics/metrics_20250513_191634.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 632 | 258 | 214 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | F (41) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.53 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 1 (0.2%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 17 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 638 |
| Files | 3 |
| Comments | 260 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:17 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191722.json](metrics/metrics_20250513_191722.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 638 | 260 | 215 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | F (42) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 21.28 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 6 (0.9%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 17 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 651 |
| Files | 3 |
| Comments | 266 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:17 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191801.json](metrics/metrics_20250513_191801.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 651 | 266 | 217 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | F (50) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 19.96 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 13 (2.0%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 17 high complexity functions
  - 0 files with low maintainability

### May 13, 2025

#### Summary

| Metric | Value | 
|--------|-------|
| Lines of Code | 663 |
| Files | 3 |
| Comments | 265 |
| Linting Issues | 0 |
| Cyclomatic Complexity | A:0 B:0 C:0 D:0 E:0 F:17 |
| Maintainability Index | A:3 B:0 C:0 |
| Detailed Report | [metrics_20250513_191829.json](metrics/metrics_20250513_191829.json) |

#### Code Statistics by Language
| Language | Files | Code | Comment | Blank |
|----------|-------|------|---------|-------|
| Python | 3 | 663 | 265 | 219 |


#### Top 10 Complex Files
| File | Grade | Complexity | Most Complex Function |
|------|-------|------------|----------------------|
| codeqa/metrics.py | A | 0 | N/A |
| codeqa/cli.py | A | 0 | N/A |


#### Top 10 Complex Functions/Methods
| File | Function | Grade | Complexity |
|------|----------|-------|------------|
| codeqa/metrics.py | F (46) | F | 0 |
| codeqa/metrics.py | D (21) | F | 0 |
| codeqa/metrics.py | C (16) | F | 0 |
| codeqa/metrics.py | C (12) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (10) | F | 0 |
| codeqa/metrics.py | B (8) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |
| codeqa/metrics.py | B (7) | F | 0 |


#### Top 10 Files with Linting Issues
No linting issues found.

#### Top 10 Files with Low Maintainability
| File | Grade | Score |
|------|-------|-------|
| codeqa/metrics.py | A | 20.35 |
| codeqa/cli.py | A | 61.43 |
| codeqa/__init__.py | A | 100.00 |


#### Trends Since Last Snapshot
| Metric | Change |
|--------|--------|
| Lines of Code | ↑ 12 (1.8%) |
| Linting Issues | ↑ 0 |
| Complex Functions | ↑ 0 (0.0%) |
| Low Maintainability | ↑ 0 |

#### Analysis
- Critical issues to address:
  - 0 linting issues
  - 17 high complexity functions
  - 0 files with low maintainability

