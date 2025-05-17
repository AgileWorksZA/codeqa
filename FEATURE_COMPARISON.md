# Feature Comparison Matrix

| Feature | codeqa | Wily | SonarQube | CodeClimate | Prospector | MegaLinter |
|---------|--------|------|-----------|-------------|------------|------------|
| **Core Functionality** |
| Lines of Code | ✅ (cloc) | ✅ | ✅ | ✅ | ❌ | ✅ |
| Linting Issues | ✅ (Ruff) | ❌ | ✅ | ✅ | ✅ | ✅ |
| Complexity Metrics | ✅ (Radon) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Historical Tracking | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Trend Analysis | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Deployment** |
| Local Execution | ✅ | ✅ | ⚠️ | ❌ | ✅ | ✅ |
| Cloud Service | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| Self-Hosted | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **Configuration** |
| Include/Exclude | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| Tool Selection | Fixed | Fixed | ✅ | ✅ | ✅ | ✅ |
| Custom Rules | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Integration** |
| Git Integration | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ |
| CI/CD Support | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GitHub Actions | ✅ | ❌ | ✅ | ✅ | ⚠️ | ✅ |
| **Reporting** |
| Markdown Reports | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| HTML Reports | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| JSON Export | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Dashboards | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| **Languages** |
| Python Support | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Multi-Language | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| **Maintenance** |
| Active Development | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Last Update | 2025 | 2020 | 2025 | 2025 | 2024 | 2025 |
| **Cost** |
| Free/Open Source | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ |
| Paid Tiers | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |

Legend:
- ✅ Full support
- ⚠️ Partial/Limited support  
- ❌ Not supported

## Key Differentiators

### codeqa Strengths:
1. **Lightweight local solution** with historical tracking
2. **Markdown-first reporting** ideal for git repos
3. **Simple configuration** without complexity overhead
4. **Active maintenance** unlike similar tool Wily

### codeqa Limitations:
1. **Python-only** support
2. **Fixed tool set** (cloc, Ruff, Radon)
3. **No enterprise features** (dashboards, team management)
4. **Basic visualizations** compared to cloud solutions

### Best Use Cases:

**Choose codeqa when:**
- You need local historical tracking
- Working on Python projects
- Want simple setup and maintenance
- Prefer markdown reports in git
- Need privacy/security for code

**Choose alternatives when:**
- Need multi-language support (SonarQube, MegaLinter)
- Want cloud dashboards (CodeClimate, Codacy)
- Require enterprise features (SonarQube)
- Only need one-time analysis (Prospector)

## Market Positioning

codeqa occupies a unique position as a "local-first historical code quality tracker" that bridges the gap between:
- Simple analyzers (Radon, flake8) that lack history
- Complex platforms (SonarQube) that require infrastructure
- Abandoned tools (Wily) with similar concepts