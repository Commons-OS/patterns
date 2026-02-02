# ADR-0004: 7 Pillars Commons Alignment Assessment Framework

**Status:** Accepted

**Date:** 2026-01-15 (retrospective)

**Deciders:** Commons OS maintainers

## Context

Patterns in the Commons OS library vary in how well they align with Commons values and principles. Some patterns are deeply rooted in commons-based thinking (like Sociocracy or Steward Ownership), while others are more neutral tools that could be applied in various contexts. Users needed a way to understand how "commons-aligned" each pattern is, and contributors needed guidance on how to evaluate patterns consistently.

The challenge was to create an assessment framework that is rigorous enough to be meaningful, yet simple enough to apply consistently across 1,000+ patterns.

## Decision

Every pattern includes a **7 Pillars Commons Alignment Assessment** that evaluates the pattern against seven dimensions of commons values. Each pillar is scored on a 1-5 scale with a brief justification.

The seven pillars are:

| Pillar | What It Measures |
|--------|------------------|
| **Shared Stewardship** | Does the pattern distribute ownership and responsibility broadly? |
| **Distributed Power** | Does the pattern prevent concentration of control? |
| **Regenerative Value** | Does the pattern create value that sustains and renews resources? |
| **Transparency** | Does the pattern promote openness and accountability? |
| **Participation** | Does the pattern enable meaningful stakeholder involvement? |
| **Resilience** | Does the pattern build adaptive capacity and robustness? |
| **Purpose Preservation** | Does the pattern protect long-term mission over short-term gains? |

The overall `commons_alignment` score (1-5) in the pattern's classification is derived from these individual pillar scores.

## Consequences

### Positive

The framework provides a consistent lens for evaluating all patterns. Contributors have clear criteria for assessment, and users can quickly understand a pattern's alignment with commons values.

The pillar-by-pillar breakdown adds nuance beyond a single score. A pattern might score high on Transparency but low on Distributed Power, which is useful information for practitioners.

The assessment section adds substantive content to each pattern, making the library more valuable as an educational resource about commons principles.

### Negative

The scoring is inherently subjective. Different evaluators might assign different scores to the same pattern, leading to inconsistencies across the library.

The 7 Pillars framework is specific to Commons OS and may not align with other commons frameworks or academic literature. This could create confusion for users familiar with other approaches.

Maintaining assessment quality at scale is challenging. With 1,000+ patterns, ensuring consistent and thoughtful assessments requires significant effort.

### Neutral

The framework assumes that "more commons-aligned" is better, which may not always be appropriate. Some patterns are valuable precisely because they are neutral tools applicable in many contexts.

## Alternatives Considered

### Alternative 1: Simple Binary Classification

Mark patterns as either "commons-aligned" or "general."

This approach was not chosen because it loses too much nuance. Many patterns have mixed characteristics that a binary classification cannot capture.

### Alternative 2: Single Numeric Score

Use only an overall 1-5 score without pillar breakdown.

This approach was not chosen because it doesn't provide enough information about why a pattern received its score. The pillar breakdown adds educational value and helps users understand the dimensions of commons alignment.

### Alternative 3: Adopt Existing Framework

Use an established commons assessment framework from academic literature.

This approach was not chosen because existing frameworks are often designed for different purposes (evaluating commons governance, not organizational patterns) and would require significant adaptation. The 7 Pillars framework was designed specifically for pattern evaluation.

## References

- PATTERN_SPEC.md Section 8: Commons Alignment Assessment
- Elinor Ostrom's work on commons governance (inspiration)
- Pattern content structure in all pattern files
