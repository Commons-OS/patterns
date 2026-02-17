# Commons OS Pattern Library - Agent Boot Procedure

**Mission:** Our mission is to empower Commons Engineers by tending this living library of patterns.

> **READ THIS FIRST** when starting a new session to load context and avoid repeating past mistakes.

## Quick Stats (Updated: 2026-02-02)

| Metric | Value |
|--------|-------|
| Total Patterns | 1,282 |
| Multi-domain Patterns | 1,225 (95%) |
| Business Domain | 1,227 |
| Startup Domain | 1,176 |
| Security Domain | 721 |
| Relationships | 3,309 |
| ADRs | 12 |

## Key Architecture Decisions

### ADR-012: Multi-Value Classification (2026-02-02)
- `commons_domain` is now an **array**, not a string
- Patterns can belong to multiple domains: `[business, startup, security]`
- `category` is also an array for flexible tagging
- This enables cross-domain discovery and better visualization

### Critical Conventions
1. **Filename format**: `{slug}.md` (no numbers, no prefixes)
2. **YAML field**: Use `classification:` NOT `tags:` (Jekyll reserved)
3. **TypeID**: `pat_{uuid7}` format for unique identifiers
4. **Domain location**: Inside `classification:` block, as array

## File Locations

| Purpose | Path |
|---------|------|
| Patterns | `_patterns/*.md` |
| ADRs | `docs/adr/*.md` |
| Spec | `PATTERN_SPEC.md` (v1.3) |
| Index Builder | `scripts/build_indexes.py` (v3.0) |
| Graph Index | `data/graph.json` |
| Search Index | `search-index.json` |

## Startup Pattern Categories

| Category | Count | Examples |
|----------|-------|----------|
| Funding | 51 | Bootstrapping, VC, Patient Capital |
| Governance | 60 | Steward Ownership, B-Corp |
| Growth | 54 | PLG, Viral Loop, Community-Led |
| Team | 63 | Psychological Safety, OKRs |
| Validation | 15 | Customer Discovery, MVP variants |
| Product | 13 | Product-Market Fit, ICP, Positioning |

## Common Mistakes to Avoid

1. **DON'T** use `tags:` in YAML (Jekyll reserved keyword)
2. **DON'T** use numbered prefixes in filenames
3. **DON'T** treat `commons_domain` as a single string
4. **DON'T** forget to rebuild indexes after adding patterns
5. **DON'T** skip reading ADRs before making architecture changes

## Workflow for Adding Patterns

```bash
# 1. Generate TypeID
python3 scripts/generate_typeid.py

# 2. Create pattern file in _patterns/
# Use slug-only filename, multi-domain classification

# 3. Rebuild indexes
python3 scripts/build_indexes.py

# 4. Commit and push
git add -A && git commit -m "Add pattern: {title}" && git push
```

## Recent Changes Log

- **2026-02-02**: ADR-012 - Multi-domain classification implemented
- **2026-02-02**: Added 28 Idea/Validation + Product/Market patterns
- **2026-02-01**: ADR-001 to ADR-011 - Initial architecture decisions
- **2026-02-01**: Migrated to slug-only filenames
- **2026-02-01**: Renamed tags to classification
