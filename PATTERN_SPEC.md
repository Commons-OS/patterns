# Pattern Specification (v7.1)

**Date:** 17 February 2026
**Authors:** higgerix, cloudsters
**Status:** Definitive Specification (v7.1)
**Supersedes:** v1.3 (02 February 2026)

---

## 1. Purpose: A Language for Stewards

This specification defines the format for patterns in the Commons OS library. Its purpose is to provide a shared language for **Cognitive Systems Builders**—the intrapreneurs, entrepreneurs, and systems thinkers designing the resilient, living systems of the Cognitive Age.

Following this spec ensures that every pattern is not just a document, but a tool: a legible, repeatable, and machine-readable artifact that helps you make your systems thinking visible, influential, and effective.

---

## 2. The Core Principle: Write Once, Render Richly

The source of truth (the Markdown file) is optimized for the **author**, while the rendered web page is optimized for the **reader**. We achieve this by keeping the author-written body focused on the core narrative, and then programmatically injecting machine-readable data from the frontmatter into the page at build time.

-   **Author Focus:** Write the story (Context, Problem, Solution, etc.) in a clear, narrative flow that makes the reader feel the life of the system.
-   **Machine Focus:** Structure all graph data, metadata, and relationships in the YAML frontmatter.
-   **Build Process:** A build script reads the frontmatter and renders it as rich, human-readable components on the page (e.g., a visual score card for the Commons Alignment, a dynamic list of Related Patterns).

This eliminates content duplication, ensures data consistency, and keeps the authoring experience clean and focused.

---

## 3. The Definitive Frontmatter (v7.1)

The frontmatter is organized into 7 functional groups. The only change from v7 is the addition of `vitality` and `vitality_reasoning` to the existing `commons_assessment` block in Group 3.

```yaml
---
# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
id: pat_01h8x4e1gq7r9d1z2x3c4v5b6n
slug: transparent-ledger
title: "Transparent Ledger"
aliases: ["Open Book Management"]
summary: >-
  A pattern for establishing collective trust by making operational data
  and financial records accessible and auditable by all relevant stakeholders.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Open Book Management"
  government: "Public Account Auditing"
  activist: "Radical Transparency"
  tech: "Public Blockchain Ledger"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & SEARCH OPTIMIZATION (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: finance
  cross_domains: [governance, technology]
  search_hints:
    primary_tension: "Information Asymmetry vs. Collective Trust"
    vector_keywords: ["accountability", "ledger", "auditability", "commons", "transparency"]
  commons_assessment:
    stakeholder_architecture: 5
    value_creation: 4
    resilience: 5
    ownership: 5
    autonomy: 4
    composability: 3
    fractal_value: 5
    vitality: 4.5
    vitality_reasoning: >-
      Scores highly because it directly enables feedback loops and
      adaptation, which are the core mechanisms of any living system.
      Weakness: potential for rigid implementation that stifles local
      adaptation if governance is not sufficiently distributed.
    overall_score: 4.4

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  usage_stage: design
  adoption_stage: growth
  status: stable
  version: 1.2
  confidence: 3

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: HARD RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  generalizes_from: []
  specializes_to: []
  enables: []
  requires: []
  alternatives: []
  complementary: []
  tools: []

# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: 2026-02-17
  entities: []
  communities: []
  inferred_links: []

# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources: []
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
---
```

### Vitality Scoring Guidance

The `vitality` field assesses the pattern's capacity to generate life, wholeness, and adaptive capacity in the systems that adopt it. Use the following rubric:

| Score | Level | Meaning |
|:---|:---|:---|
| 4.5–5.0 | **Generative** | The pattern actively creates conditions for new life and adaptation to emerge. Systems using this pattern feel alive and evolving. |
| 3.5–4.4 | **Sustaining** | The pattern maintains and renews existing vitality. Systems using it are healthy but not necessarily generating new capacity. |
| 2.0–3.4 | **Functional** | The pattern works correctly but does not contribute to or may even dampen the system's aliveness. Risk of bureaucratic rigidity. |
| 0.0–1.9 | **Extractive** | The pattern actively depletes vitality. It may solve a narrow problem but at the cost of the system's overall health. |

---

## 4. The Definitive Body Structure (v7.1)

The body is the author's canvas. It contains **8 author-written sections**. The remaining sections (Commons Alignment, Related Patterns, References) are generated from the frontmatter at build time.

```markdown
> A one-sentence summary of the pattern's core idea.

> [!NOTE] Confidence Rating: ★★★ (High)
> This rating reflects our confidence that this pattern is a good and correct
> solution to the stated problem.

---

### Section 1: Context

*(100–200 words)*

Describes the situation or environment in which the problem arises. It should be a concise, narrative paragraph that helps the reader feel the living energy of the context — is this a system that is growing, stagnating, fragmenting, or decaying?

---

### Section 2: Problem

*(100–200 words)*

> **The core conflict is [State the Primary Tension from the frontmatter].**

After the bold problem statement, describe the **forces** at play. Forces are not abstract concepts; they are living tensions experienced by real people in real systems.

---

### Section 3: Solution

*(200–400 words)*

> **Therefore, [State the core instruction of the solution in one bold sentence].**

After the bold solution statement, provide a detailed explanation of the mechanism. Include a diagram if it helps clarify the structure.

---

### Section 4: Implementation

*(300–500 words)*

Provide concrete, actionable steps for implementing the solution. This section should feel like a practical guide, not a theoretical treatise. Frame the steps as acts of cultivation — tending, protecting, and growing the living system.

---

### Section 5: Consequences

*(200–300 words)*

Describe the trade-offs and implications. What new capacities for life does it create? What forms of decay does it make possible if not tended carefully?

---

### Section 6: Known Uses

*(200–300 words)*

Provide at least two real-world examples of this pattern in action. Tell the stories of these living systems — don't just state facts.

---

### Section 7: Cognitive Era

*(150–250 words)*

How does this pattern change in the Cognitive Age? How does it interact with AI, autonomous agents, and distributed intelligence?

---

### Section 8: Vitality

*(200–300 words)*

This is the explicit diagnostic section. What does vitality look like in a system that uses this pattern? What are the signs of life? Conversely, what does decay look like? This section should provide a clear, actionable diagnostic for assessing the health of the pattern in practice.
```

---

## 5. Workflow & Validation

1.  **Generate ID:** `python3 scripts/generate_typeid.py`
2.  **Create File:** `cp _templates/pattern.md _patterns/{slug}.md`
3.  **Fill Content:** Complete all YAML fields and the 8 body sections.
4.  **Validate:** `python3 scripts/validate_entity.py _patterns/{slug}.md`
5.  **Commit:** `git add _patterns/{slug}.md && git commit -m "Add pattern: {title}"`
