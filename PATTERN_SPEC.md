# Pattern Engine Specification

> **IMPORTANT**: This document is the authoritative source of truth for pattern format.
> **ALL contributors (human and AI) MUST read this before creating or modifying patterns.**

## Purpose

This specification ensures consistency across all patterns in the Commons OS Pattern Library. It defines the exact format, required fields, and validation rules that every pattern must follow.

---

## 1. File Location & Naming

### Location
All patterns MUST be stored in:
```
_patterns/
```

### Filename Format
```
{slug}.md
```

**Rules:**
- `slug`: Lowercase, hyphen-separated, human-readable identifier
- Extension: `.md` (Markdown)
- Slug MUST be unique across all patterns
- Slug SHOULD be descriptive enough to distinguish similar patterns

**Examples:**
```
sociocracy-original-gerard-endenburg.md
steward-ownership.md
zero-trust-architecture.md
privacy-by-design-cavoukian.md
```

**Slug Naming Guidelines:**
- Use the pattern's common name as the base
- Add originator name if multiple variants exist (e.g., `sociocracy-original-gerard-endenburg.md`)
- Add distinguishing context if needed (e.g., `privacy-by-design-cavoukian.md` vs `privacy-by-design-gdpr.md`)

**DO NOT USE:**
- Sequential numbers (e.g., `1024-`, `1025-`)
- Category prefixes (e.g., `P001-`, `S031-`, `IV001-`)
- UUIDs in filenames
- Uppercase letters

---

## 2. Pattern ID (TypeID)

Every pattern MUST have a unique `id` in TypeID format based on UUID7.

### Format
```
pat_{uuid7_base32}
```

### Generation
Use Python with the `uuid7` library:
```python
import uuid7

def generate_pattern_id():
    return f"pat_{uuid7.uuid7().hex[:26]}"
```

Or use the provided script:
```bash
python3 scripts/generate_typeid.py
```

**Example IDs:**
```
pat_01kg5023vveprts2at71w6e29g
pat_01kg502401ejststrxw4haba08
```

**Rules:**
- IDs are immutable once assigned
- IDs are globally unique across all patterns
- IDs are the primary identifier for cross-references between patterns
- The TypeID is the ONLY unique identifier — slugs are for human readability

---

## 3. YAML Frontmatter

Every pattern MUST begin with YAML frontmatter enclosed in `---` delimiters.

### Required Fields

```yaml
---
id: pat_{uuid7}                    # TypeID (required, immutable)
page_url: https://commons-os.github.io/patterns/{slug}/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/{slug}.md
slug: {slug}                       # Must match filename without .md
title: Pattern Title               # Human-readable title
aliases: [Alias 1, Alias 2]        # Alternative names (can be empty [])
version: 1.0                       # Semantic version
created: YYYY-MM-DDTHH:MM:SSZ      # ISO 8601 timestamp
modified: YYYY-MM-DDTHH:MM:SSZ     # ISO 8601 timestamp

tags:
  universality: universal|domain   # universal = applies everywhere, domain = specific context
  domain: governance|operations|finance|technology|culture|security|privacy|sovereignty|startup
  category: [framework|practice|principle|tool|structure|process|anti-pattern]
  era: [pre-industrial|industrial|cognitive]
  origin: [originator-name]        # Person or organization that created it
  status: draft|review|published
  commons_alignment: 1-5           # 1=low, 5=very high alignment with commons principles

commons_domain: business|security|startup|urban|ecology|life

# Pattern Relationships (use TypeIDs, can be empty [])
generalizes_from: []               # This pattern is a more general form of...
specializes_to: []                 # This pattern is specialized by...
enables: []                        # This pattern enables...
requires: []                       # This pattern requires...
related: []                        # Related patterns

# Metadata
contributors: [username1, username2]
sources: [https://source1.com, https://source2.com]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
```

### Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | TypeID in format `pat_{uuid7}` — the unique identifier |
| `page_url` | string | Yes | Public URL on GitHub Pages |
| `github_url` | string | Yes | Direct link to file on GitHub |
| `slug` | string | Yes | URL-friendly identifier, matches filename |
| `title` | string | Yes | Human-readable pattern name |
| `aliases` | array | Yes | Alternative names (can be empty) |
| `version` | string | Yes | Semantic version (e.g., 1.0, 1.1) |
| `created` | string | Yes | ISO 8601 creation timestamp |
| `modified` | string | Yes | ISO 8601 last modified timestamp |
| `tags.universality` | string | Yes | `universal` or `domain` |
| `tags.domain` | string | Yes | Primary domain category |
| `tags.category` | array | Yes | Pattern type(s) |
| `tags.era` | array | Yes | Historical era(s) of applicability |
| `tags.origin` | array | Yes | Creator(s) of the pattern |
| `tags.status` | string | Yes | `draft`, `review`, or `published` |
| `tags.commons_alignment` | integer | Yes | 1-5 score for commons alignment |
| `commons_domain` | string | Yes | High-level domain classification |
| `generalizes_from` | array | Yes | TypeIDs of parent patterns |
| `specializes_to` | array | Yes | TypeIDs of child patterns |
| `enables` | array | Yes | TypeIDs of enabled patterns |
| `requires` | array | Yes | TypeIDs of required patterns |
| `related` | array | Yes | TypeIDs of related patterns |
| `contributors` | array | Yes | GitHub usernames of contributors |
| `sources` | array | Yes | URLs of reference sources (quote URLs with special characters) |
| `license` | string | Yes | License identifier |
| `attribution` | string | Yes | Attribution statement |
| `repository` | string | Yes | Repository URL |

---

## 4. Content Structure

After the YAML frontmatter, the pattern content MUST follow this structure:

```markdown
### 1. Overview

[2-3 paragraphs describing what the pattern is, the problem it solves, and its origin]

### 2. Core Principles

[Numbered list of the fundamental principles underlying the pattern]

### 3. Key Practices

[Numbered list of specific practices or methods used to implement the pattern]

### 4. Implementation

[Guidance on how to implement the pattern, including steps, considerations, and examples]

### 5. 7 Pillars Assessment

| Pillar | Score (1-5) | Rationale |
|--------|-------------|-----------|
| Purpose | X | [Why this score] |
| Governance | X | [Why this score] |
| Culture | X | [Why this score] |
| Incentives | X | [Why this score] |
| Knowledge | X | [Why this score] |
| Technology | X | [Why this score] |
| Resilience | X | [Why this score] |
| **Overall** | **X.X** | **[Summary]** |

### 6. When to Use

[Bullet points or paragraphs describing ideal contexts for this pattern]

### 7. Anti-Patterns & Gotchas

[Common mistakes, misapplications, or things to watch out for]

### 8. References

[Numbered list of sources with links]
```

---

## 5. Validation Rules

Before committing any pattern, verify:

### Automated Checks (run `scripts/validate_entity.py`)
- [ ] File is in `_patterns/` directory
- [ ] Filename matches `{slug}.md` format (no numbers, lowercase, hyphens)
- [ ] YAML frontmatter is valid and parseable
- [ ] All required fields are present
- [ ] `id` is in TypeID format (`pat_` prefix)
- [ ] `slug` matches filename without `.md`
- [ ] `commons_alignment` is between 1 and 5
- [ ] All TypeID references in relationships exist in `graph.json`

### Manual Checks
- [ ] Content follows the 8-section structure
- [ ] 7 Pillars Assessment table is complete with rationales
- [ ] Sources are properly cited
- [ ] No duplicate pattern (check by title, slug, and aliases)

---

## 6. Workflow for Adding Patterns

### Step 1: Generate TypeID
```bash
python3 scripts/generate_typeid.py
# Output: pat_01kg5024abcdef123456789
```

### Step 2: Create Slug
Choose a unique, descriptive slug:
- Check existing patterns: `ls _patterns/`
- Use pattern name + originator if needed for uniqueness

### Step 3: Create File from Template
```bash
cp _templates/pattern.md _patterns/{slug}.md
```

### Step 4: Fill in Content
- Replace all `{placeholders}` with actual values
- Complete all 8 content sections
- Fill in the 7 Pillars Assessment with rationales

### Step 5: Validate
```bash
python3 scripts/validate_entity.py _patterns/{slug}.md
```

### Step 6: Commit
```bash
git add _patterns/{slug}.md
git commit -m "Add pattern: {title}"
git push
```

---

## 7. Commons Alignment Scoring Guide

| Score | Label | Description |
|-------|-------|-------------|
| 5 | Very High | Fundamentally designed for collective value creation, stakeholder governance, long-term resilience |
| 4 | High | Strongly supports commons principles, minor trade-offs possible |
| 3 | Medium | Neutral tool, can be used for commons or extractive purposes depending on implementation |
| 2 | Low | Tends toward extraction, short-term thinking, or concentrated control |
| 1 | Very Low | Fundamentally extractive, undermines collective value creation |

---

## 8. Domain Categories

| Domain | Description | Examples |
|--------|-------------|----------|
| `governance` | Decision-making, authority, voting | Sociocracy, Steward Ownership |
| `operations` | Processes, workflows, execution | Lean, Kanban |
| `finance` | Funding, revenue, economics | Patient Capital, VC |
| `technology` | Technical systems, infrastructure | Zero Trust, API Security |
| `culture` | Values, norms, behaviors | Psychological Safety |
| `security` | Protection, resilience, risk | Defense in Depth |
| `privacy` | Data protection, consent | Data Minimization |
| `sovereignty` | Independence, self-determination | Self-Sovereign Identity |
| `startup` | Venture creation, scaling | Lean Startup, MVP |

---

## 9. Retrieval & Indexing

Patterns are stored as individual Markdown files, but retrieval is supported by generated indexes:

### graph.json
- Contains all pattern metadata and relationships
- Rebuilt automatically on each push to main
- Use for: finding patterns by TypeID, querying relationships

### embeddings.json
- Contains vector embeddings for semantic search
- Rebuilt automatically when patterns change
- Use for: "find patterns about X" queries

**Note:** These indexes are derived from the Markdown files. The files are the source of truth.

---

## 10. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-01 | Initial specification |
| 1.1 | 2026-02-01 | Removed sequential numbers from filename format; slug-only naming |

---

## 11. Questions?

If anything in this specification is unclear, open an issue at:
https://github.com/commons-os/patterns/issues
