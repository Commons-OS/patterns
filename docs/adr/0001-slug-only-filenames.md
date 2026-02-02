# ADR-0001: Slug-Only Filenames Without Sequential Numbers

**Status:** Accepted

**Date:** 2026-02-02

**Deciders:** Commons OS maintainers

**Supersedes:** Previous convention of `{number}-{slug}.md` format

## Context

Pattern files were originally named with a sequential number prefix followed by a slug, such as `1025-steward-ownership.md`. This convention was intended to provide human-readable ordering and quick identification.

However, this approach caused several problems:

1. **Numbering conflicts**: When multiple contributors added patterns simultaneously, they would assign the same numbers, creating merge conflicts and duplicate files.

2. **Redundancy with TypeID**: Each pattern already has a TypeID (`pat_01kg5023vve...`) as its unique identifier. The sequential number was redundant.

3. **Maintenance burden**: Renaming or reorganizing patterns required updating the number prefix, which added unnecessary complexity.

4. **No semantic value**: The numbers didn't convey meaningful information about the pattern's content or relationships.

## Decision

Pattern filenames use **slug-only format**: `{slug}.md`

Examples:
- `steward-ownership.md` (not `1025-steward-ownership.md`)
- `sociocracy-original-gerard-endenburg.md`
- `5s-methodology.md`

The slug must be:
- Lowercase
- Hyphen-separated words
- URL-safe (no special characters except hyphens)
- Unique within the patterns collection

The TypeID in the YAML frontmatter remains the authoritative unique identifier for all machine references and relationships.

## Consequences

### Positive

- **No numbering conflicts**: Contributors can add patterns without coordinating numbers
- **Simpler filenames**: Easier to read and type
- **Stable references**: Slugs are more stable than arbitrary numbers
- **Cleaner URLs**: Pattern URLs are more readable (`/patterns/steward-ownership/`)

### Negative

- **No visual ordering**: Files sort alphabetically, not by creation order
- **Migration required**: Existing files needed renaming (completed 2026-02-02)

### Neutral

- TypeID provides machine-readable ordering (UUIDv7 is time-sorted)
- The `graph.json` index provides alternative ways to browse patterns

## Alternatives Considered

### Alternative 1: Keep Sequential Numbers

Continue using `{number}-{slug}.md` format with a central registry to prevent conflicts.

**Rejected because:**
- Added complexity without proportional benefit
- Required coordination mechanism for number assignment
- Numbers were already causing conflicts

### Alternative 2: TypeID as Filename

Use the TypeID directly as the filename: `pat_01kg5023vve.md`

**Rejected because:**
- Not human-readable
- Difficult to navigate in file system
- Poor for URLs

## References

- System-wide ADR-0001: Use TypeID for Entity Identifiers
- PATTERN_SPEC.md Section 2: File Naming Convention
