# Pattern Engine Agent Boot Procedure

> **Purpose**: Quick reference for AI agents working specifically on the Pattern Engine. For full system context, see [AGENT_BOOT.md](https://github.com/Commons-OS/commons-os.github.io/blob/main/AGENT_BOOT.md) in the main repository.

---

## Quick Start

### 1. Load Context (in order)

```
1. Read: docs/adr/README.md          # All Pattern Engine ADRs
2. Read: PATTERN_SPEC.md             # Pattern format specification
3. Read: ARCHITECTURE.md             # System architecture
4. Check: data/graph.json            # Current state (pattern count, relationships)
```

### 2. Key Rules

| Rule | Details |
|------|---------|
| **Filename format** | `{slug}.md` — no numbers, no prefixes |
| **Unique identifier** | TypeID in frontmatter (`id: pat_...`) |
| **Metadata field** | Use `classification:` not `tags:` (Jekyll reserved) |
| **Index generation** | Single script: `python3 scripts/build_indexes.py` |
| **Staging workflow** | New patterns → `_staging/patterns/` → validate → promote to `_patterns/` |

### 3. Before Making Changes

1. Check if an ADR exists for the area you're modifying
2. Run validation: `python3 scripts/validate_pattern.py <file>`
3. Rebuild indexes: `python3 scripts/build_indexes.py`
4. Test locally before pushing

---

## Current State

| Metric | Value |
|--------|-------|
| Patterns in `_patterns/` | 1,026 |
| Patterns in `_staging/` | 0 |
| Domains | 13 |
| Relationships | 3,300+ |

---

## ADR Summary

| ADR | Decision |
|-----|----------|
| 0001 | Slug-only filenames (no sequential numbers) |
| 0002 | Use `classification:` instead of `tags:` |
| 0003 | Single consolidated `build_indexes.py` script |
| 0004 | 7 Pillars Commons Alignment Assessment |
| 0005 | 5 relationship types (generalizes, specializes, enables, requires, related) |
| 0006 | Staging → Patterns promotion workflow |

---

## Common Commands

```bash
# Validate a pattern
python3 scripts/validate_pattern.py _patterns/steward-ownership.md

# Rebuild all indexes
python3 scripts/build_indexes.py

# Generate new TypeID
python3 scripts/generate_typeid.py

# Count patterns
ls _patterns/*.md | wc -l
```

---

## Pitfalls to Avoid

- **Don't use `tags:` in YAML** — Jekyll reserved, use `classification:`
- **Don't add Navigation section** — Template handles this
- **Don't hardcode counts** — Use Jekyll variables
- **Don't run deleted scripts** — Only `build_indexes.py` exists now

---

*Last updated: 2026-02-02*
