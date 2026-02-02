# Architecture Decision Records (ADRs) - Pattern Engine

This directory contains Architecture Decision Records specific to the Pattern Engine.

For **system-wide ADRs** that apply across all Commons OS engines, see: [commons-os.github.io/docs/adr](https://github.com/Commons-OS/commons-os.github.io/tree/main/docs/adr)

## Pattern Engine ADRs

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0001](0001-slug-only-filenames.md) | Slug-Only Filenames Without Sequential Numbers | Accepted | 2026-02-02 |
| [0002](0002-rename-tags-to-classification.md) | Rename 'tags' to 'classification' in YAML Frontmatter | Accepted | 2026-02-02 |
| [0003](0003-consolidated-index-generation.md) | Consolidated Index Generation Script | Accepted | 2026-02-02 |

## Creating a New ADR

1. Copy `template.md` to a new file: `NNNN-short-title.md`
2. Fill in all sections
3. Update this README with the new ADR
4. Submit a pull request

## For AI Agents

When starting a new session working on the Pattern Engine, read:

1. System-wide ADRs at `commons-os.github.io/docs/adr/`
2. Pattern-specific ADRs in this directory
3. `PATTERN_SPEC.md` for current pattern format
4. `ARCHITECTURE.md` for system overview
