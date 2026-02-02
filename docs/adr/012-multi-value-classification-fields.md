# 12. Use Multi-Value Arrays for Classification Fields

- **Status**: Accepted
- **Date**: 2026-02-02
- **Deciders**: Manus AI, Cloudsters

## Context and Problem Statement

The current `classification` frontmatter in patterns uses single string values for fields like `commons_domain` and `category`. This forces a pattern into a single, restrictive silo (e.g., a pattern is either `business` OR `startup`, but not both). This contradicts the core goal of the pattern library, which is to reveal connections and allow for cross-pollination of ideas. Many patterns, like "Lean Startup" or "Value Proposition Canvas," are equally relevant to both startups and established businesses. The current single-value implementation prevents flexible discovery and accurate representation of a pattern's applicability.

## Decision Drivers

- **Cross-Domain Relevance**: Many patterns are not confined to a single domain. A business innovating its processes uses startup patterns.
- **Discovery & Visualization**: Single-value fields prevent rich discovery queries (e.g., "find patterns in `business` AND `startup`") and limit the accuracy of knowledge graph visualizations.
- **Philosophical Alignment**: The goal is to connect ideas, not silo them. The data structure should reflect this.

## Considered Options

1. **Single String (Current)**: Keep the existing implementation. Simple, but fundamentally flawed and restrictive.
2. **Multi-Value Array**: Change fields to accept an array of strings. More complex, but correctly models the relationships.
3. **Separate Taxonomy Files**: Use a more complex taxonomy system (e.g., `tags.yml`). Overly complex for the current Jekyll setup.

## Decision Outcome

**Chosen Option**: Option 2, "Multi-Value Array". We will change key classification fields, specifically `commons_domain` and `category`, to accept an array of strings instead of a single string.

### Example

**Before (single value):**
```yaml
classification:
  commons_domain: startup
  category: growth
```

**After (multi-value array):**
```yaml
classification:
  commons_domain: [startup, business]
  category: [growth, product]
```

## Consequences

### Positive
- Enables more accurate and flexible pattern classification.
- Allows for powerful cross-domain queries.
- Improves the accuracy of knowledge graph visualizations by showing inter-domain connections.
- Aligns the implementation with the philosophical goal of the pattern library.

### Negative
- Requires a migration effort to update all 1,254 existing patterns.
- Requires updates to all scripts that parse or rely on these fields (`build_indexes.py`, `validate_pattern.py`, etc.).
- Jekyll templates and search functionality will need to be updated to handle array values.

## Implementation Plan

1. **ADR Creation**: This document.
2. **Update `PATTERN_SPEC.md`**: Reflect the change to array values.
3. **Migration Script**: Develop a script to:
    a. Convert the existing single value to a single-item array (e.g., `startup` -> `[startup]`)
    b. Apply rules to automatically add secondary domains (e.g., any pattern with "lean", "mvp", "canvas" gets both `business` and `startup` tags).
4. **Manual Review**: Manually review and augment the automated tagging.
5. **Script Updates**: Update all relevant scripts and templates to correctly read and process array values.
6. **Rebuild Indexes**: Regenerate `graph.json` and `search-index.json`.
