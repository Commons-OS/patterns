# ADR-0006: Staging to Patterns Promotion Workflow

**Status:** Accepted

**Date:** 2026-02-01 (retrospective)

**Deciders:** Commons OS maintainers

## Context

As the Pattern Engine grew to include contributions from multiple sources (human contributors, AI-generated content, bulk imports), quality control became essential. Patterns needed to be validated and enriched before becoming part of the canonical library. Without a gating mechanism, low-quality or inconsistent patterns could enter the main collection.

The challenge was to create a workflow that ensures quality without creating excessive friction for contributors.

## Decision

The Pattern Engine uses a **two-stage publishing workflow** with patterns moving from staging to canonical:

| Stage | Location | Purpose |
|-------|----------|---------|
| **Staging** | `_staging/patterns/` | New or modified patterns awaiting validation |
| **Canonical** | `_patterns/` | Validated, enriched patterns in the official library |

The workflow consists of three gates:

1. **Validation Gate**: Automated checks verify that patterns conform to PATTERN_SPEC.md (required fields, valid TypeID, correct format).

2. **Enrichment Gate**: AI-powered analysis suggests relationships, refines tags, and scores content quality. Results are posted as a report for human review.

3. **Promotion Gate**: Human reviewer approves the pattern and triggers promotion from staging to canonical.

GitHub Actions automate the validation and enrichment gates, while promotion requires manual approval.

## Consequences

### Positive

The staging area provides a safe space for work-in-progress patterns. Contributors can iterate on patterns without affecting the canonical library.

Automated validation catches format errors early, before human review. This reduces the burden on reviewers and ensures consistent quality.

The human-in-the-loop promotion step ensures that AI-generated content and bulk imports receive appropriate oversight before becoming canonical.

### Negative

The two-stage workflow adds friction for simple contributions. A contributor adding a single pattern must wait for validation, enrichment, and promotion rather than directly adding to the library.

The staging area can accumulate patterns that are never promoted, creating maintenance overhead. Periodic cleanup is needed to remove abandoned drafts.

The workflow depends on GitHub Actions, which can fail or have delays. Contributors may experience frustration if automation is slow or broken.

### Neutral

The workflow is designed for the current scale (1,000+ patterns). If the library grows significantly larger, the workflow may need adjustment to handle higher volume.

## Alternatives Considered

### Alternative 1: Direct Contribution to Canonical

Allow contributors to add patterns directly to `_patterns/` with post-hoc validation.

This approach was not chosen because it risks introducing low-quality patterns into the canonical library. Fixing problems after publication is harder than preventing them.

### Alternative 2: Branch-Based Workflow

Use Git branches instead of a staging directory, with patterns developed in feature branches.

This approach was not chosen because it adds Git complexity for contributors who may not be familiar with branching. The staging directory is simpler to understand and work with.

### Alternative 3: Full Automation Without Human Review

Automatically promote patterns that pass validation and enrichment.

This approach was not chosen because AI-generated content and bulk imports require human judgment. The human-in-the-loop step ensures contextual relevance and catches issues that automation might miss.

## References

- ARCHITECTURE.md Section 2: Core Architecture
- `.github/workflows/validate.yml` for validation automation
- `.github/workflows/enrich.yml` for enrichment automation
- `.github/workflows/promote.yml` for promotion workflow
