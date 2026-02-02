# ADR-0005: Pattern Relationship Types

**Status:** Accepted

**Date:** 2026-01-15 (retrospective)

**Deciders:** Commons OS maintainers

## Context

Patterns do not exist in isolation. They relate to each other in meaningful ways: some are generalizations of others, some enable or require others, and some are simply related by topic. The Pattern Engine needed a vocabulary for expressing these relationships to build a navigable knowledge graph.

The challenge was to define relationship types that are semantically meaningful, consistently applicable, and useful for both human navigation and machine reasoning.

## Decision

The Pattern Engine uses **five relationship types** between patterns, each with clear semantics:

| Relationship | Direction | Meaning | Example |
|--------------|-----------|---------|---------|
| `generalizes_from` | A → B | A is a more general form of B | "Steward Ownership" generalizes from "Perpetual Purpose Trust" |
| `specializes_to` | A → B | A is a specialization of B | "Perpetual Purpose Trust" specializes to "Steward Ownership" |
| `enables` | A → B | A makes B possible or easier | "Zero Trust Architecture" enables "Secure Remote Access" |
| `requires` | A → B | A depends on B | "Secure Remote Access" requires "Zero Trust Architecture" |
| `related` | A ↔ B | A and B are topically related | "Sociocracy" is related to "Holacracy" |

These relationships are stored in the YAML frontmatter of each pattern and are used to build the knowledge graph (`graph.json`).

## Consequences

### Positive

The defined vocabulary enables consistent relationship mapping across all patterns. Contributors know exactly which relationship type to use for different connections.

The directional relationships (`generalizes_from`, `specializes_to`, `enables`, `requires`) support meaningful graph traversal. Users can navigate from general to specific patterns, or find patterns that enable a particular capability.

The `related` type provides flexibility for connections that don't fit the more specific types, preventing forced categorization.

### Negative

The relationship types require judgment to apply correctly. The distinction between `enables` and `requires` can be subtle, and different contributors might categorize the same relationship differently.

The current set may not capture all meaningful relationships. For example, there's no explicit "conflicts_with" or "supersedes" relationship, which might be useful in some cases.

Maintaining relationship accuracy at scale is challenging. As patterns are added and modified, relationships can become stale or incorrect.

### Neutral

The relationships are stored redundantly in both directions (e.g., if A generalizes_from B, then B should have specializes_to A). This redundancy aids navigation but requires careful maintenance to keep consistent.

## Alternatives Considered

### Alternative 1: Free-Form Tags Only

Use only free-form tags without structured relationships.

This approach was not chosen because tags don't capture the directionality and semantics of relationships. "Related to Sociocracy" is less informative than "generalizes from Sociocracy."

### Alternative 2: More Relationship Types

Define a larger vocabulary with more specific relationship types.

This approach was not chosen to keep the system simple and learnable. Five types provide enough expressiveness for most use cases without overwhelming contributors.

### Alternative 3: Ontology-Based Approach

Use a formal ontology language (OWL, RDF) for relationships.

This approach was not chosen because it adds complexity without proportional benefit for the current use case. The simple relationship vocabulary can be upgraded to a formal ontology later if needed.

## References

- ARCHITECTURE.md Section 3: Entity & Relationship Model
- PATTERN_SPEC.md Section 3.3: Relationships
- `graph.json` for the knowledge graph implementation
