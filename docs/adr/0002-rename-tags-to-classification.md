# ADR-0002: Rename 'tags' to 'classification' in YAML Frontmatter

**Status:** Accepted

**Date:** 2026-02-02

**Deciders:** Commons OS maintainers

## Context

Pattern files use YAML frontmatter to store metadata. The original specification used a `tags` field with nested properties to classify patterns:

```yaml
tags:
  universality: domain
  domain: governance
  commons_alignment: 4
```

This structure was not rendering correctly in Jekyll templates. The template code `{{ page.tags.universality }}` was returning empty values, causing badges to display defaults instead of actual values.

After investigation, we discovered that **Jekyll reserves `tags` as a built-in frontmatter variable** for post tagging. When Jekyll encounters `tags:` with nested values, it attempts to parse it as an array of tag strings rather than as a nested object. This caused `page.tags.universality` to return nothing.

## Decision

Rename the `tags` field to `classification` in all pattern YAML frontmatter:

```yaml
classification:
  universality: domain
  domain: governance
  category: [framework]
  era: [industrial, cognitive]
  origin: [gerard-endenburg]
  status: draft
  commons_alignment: 4
```

All templates, scripts, and documentation were updated to use `classification` instead of `tags`.

## Consequences

### Positive

- **Jekyll compatibility**: `classification` is not a reserved word, so nested properties work correctly
- **Semantic clarity**: "Classification" better describes the purpose than generic "tags"
- **Template functionality restored**: Badges now display correctly on pattern pages

### Negative

- **Breaking change**: All 1,026 pattern files required updating
- **Script updates**: All Python scripts needed modification
- **Documentation updates**: PATTERN_SPEC.md and other docs needed revision

### Neutral

- The field structure remains the same, only the name changed
- No impact on TypeID, relationships, or other frontmatter fields

## Alternatives Considered

### Alternative 1: Use Top-Level Fields

Move each classification property to the top level of frontmatter:

```yaml
universality: domain
domain: governance
commons_alignment: 4
```

**Rejected because:**
- Clutters the frontmatter with many top-level fields
- Loses the logical grouping of classification-related properties
- Harder to distinguish classification from other metadata

### Alternative 2: Use 'metadata' as Field Name

Rename to `metadata` instead of `classification`.

**Rejected because:**
- Too generic; all frontmatter is metadata
- `classification` is more descriptive of the field's purpose

### Alternative 3: Prefix with Underscore

Use `_tags` to avoid Jekyll's reserved word handling.

**Rejected because:**
- Underscore prefix has special meaning in some contexts
- Less readable than a proper rename

## References

- Jekyll documentation on reserved frontmatter variables
- PATTERN_SPEC.md v1.2 for updated specification
- Commit that implemented this change across all patterns
