# Lighthouse Specification

> **IMPORTANT**: This document is the authoritative source of truth for Lighthouse format.
> **ALL contributors (human and AI) MUST read this before creating or modifying Lighthouses.**

## Purpose

Lighthouses are real-world implementations of Commons OS patterns. They are organizations, projects, or initiatives that demonstrate patterns in action. This specification ensures consistency across all Lighthouses in the Commons OS knowledge graph.

---

## 1. File Location & Naming

### Location
All Lighthouses MUST be stored in:
```
_lighthouses/
```

### Filename Format
```
{sequential_number}-{slug}.md
```

**Rules:**
- `sequential_number`: Integer, starting from 1, no leading zeros
- `slug`: Lowercase, hyphen-separated, human-readable (typically organization name)
- Extension: `.md` (Markdown)

**Examples:**
```
1-patagonia.md
2-mondragon-corporation.md
3-wikipedia.md
```

---

## 2. Lighthouse ID (TypeID)

Every Lighthouse MUST have a unique `id` in TypeID format based on UUID7.

### Format
```
lh_{uuid7_base32}
```

### Generation
Use Python with the provided script:
```bash
python3 scripts/generate_typeid.py --type lighthouse
```

**Example IDs:**
```
lh_01kg5023vveprts2at71w6e29g
lh_01kg502401ejststrxw4haba08
```

---

## 3. YAML Frontmatter

Every Lighthouse MUST begin with YAML frontmatter enclosed in `---` delimiters.

### Required Fields

```yaml
---
id: lh_{uuid7}                     # TypeID (required, immutable)
page_url: https://commons-os.github.io/lighthouses/{slug}/
github_url: https://github.com/commons-os/patterns/blob/main/_lighthouses/{filename}
slug: {sequential}-{slug}          # Must match filename without .md
title: Organization Name           # Official name
aliases: [Alias 1, Alias 2]        # Alternative names (can be empty [])
version: 1.0                       # Semantic version
created: YYYY-MM-DDTHH:MM:SSZ      # ISO 8601 timestamp
modified: YYYY-MM-DDTHH:MM:SSZ     # ISO 8601 timestamp

tags:
  industry: [technology|agriculture|finance|healthcare|education|manufacturing|retail|services|nonprofit|government]
  scale: [startup|small|medium|large|global]
  region: [north-america|south-america|europe|asia|africa|oceania|global]
  era: [pre-industrial|industrial|cognitive]
  status: draft|review|published|mature|deprecated
  commons_alignment: 1-5           # 1=low, 5=very high alignment with commons principles

location:
  city: City Name
  country: Country Name
  coordinates: [latitude, longitude]  # Optional

# Relationships
implements: []                     # Pattern TypeIDs this Lighthouse implements
inspired_by: []                    # Lighthouse TypeIDs that inspired this one
collaborates_with: []              # Lighthouse TypeIDs this one collaborates with
related: []                        # Related Lighthouse TypeIDs

# Metadata
website: https://example.com
founded: YYYY                      # Year founded
contributors: [username1, username2]
sources: [https://source1.com, https://source2.com]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
```

---

## 4. Content Structure

After the YAML frontmatter, the Lighthouse content MUST follow this structure:

```markdown
### 1. Overview

[2-3 paragraphs describing what the organization does, its mission, and why it's a Lighthouse]

### 2. Patterns in Action

[Describe which patterns this Lighthouse implements and how]

| Pattern | Implementation |
|---------|----------------|
| [Pattern Name](link) | How this pattern is applied |
| [Pattern Name](link) | How this pattern is applied |

### 3. Key Innovations

[Numbered list of specific innovations or practices that make this Lighthouse notable]

### 4. Impact & Outcomes

[Describe the measurable or observable impact of this Lighthouse]

### 5. 7 Pillars Assessment

| Pillar | Score (1-5) | Rationale |
|--------|-------------|-----------|
| Purpose | X | Why this score |
| Governance | X | Why this score |
| Culture | X | Why this score |
| Incentives | X | Why this score |
| Knowledge | X | Why this score |
| Technology | X | Why this score |
| Resilience | X | Why this score |
| **Overall** | **X.X** | **Summary** |

### 6. Lessons Learned

[What can other organizations learn from this Lighthouse?]

### 7. Challenges & Limitations

[What challenges has this Lighthouse faced? What are its limitations?]

### 8. References

[1] Source 1
[2] Source 2
```

---

## 5. Relationship Types

| Relationship | Direction | Description |
|--------------|-----------|-------------|
| `implements` | Lighthouse → Pattern | This Lighthouse implements these patterns |
| `inspired_by` | Lighthouse → Lighthouse | This Lighthouse was inspired by these others |
| `collaborates_with` | Lighthouse ↔ Lighthouse | These Lighthouses work together |
| `related` | Lighthouse ↔ Lighthouse | Related Lighthouses |

---

## 6. Validation Rules

Before committing any Lighthouse, verify:

### Automated Checks
- [ ] File is in `_lighthouses/` directory
- [ ] Filename matches `{number}-{slug}.md` format
- [ ] YAML frontmatter is valid
- [ ] All required fields are present
- [ ] `id` is in TypeID format (`lh_...`)
- [ ] `slug` matches filename
- [ ] All TypeID references in relationships are valid

### Manual Checks
- [ ] Content follows the 8-section structure
- [ ] 7 Pillars Assessment table is complete
- [ ] Pattern implementations are accurately described
- [ ] Sources are properly cited

---

## 7. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-01 | Initial specification |
