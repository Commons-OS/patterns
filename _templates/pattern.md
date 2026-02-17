--- 
# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
id: pat_{TYPEID}                       # REQUIRED. UUID7-based TypeID.
slug: {SLUG}                          # REQUIRED. Human-readable URL slug.
title: "{TITLE}"                       # REQUIRED. The official title of the pattern.
aliases: []                            # OPTIONAL. Alternative names for search expansion.
summary: >-                            # REQUIRED. For cards and search snippets (1-2 sentences).
  {A one-sentence summary of the pattern's core idea.}

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "{Corporate-friendly name}"
  government: "{Government-friendly name}"
  activist: "{Activist-friendly name}"
  tech: "{Tech-friendly name}"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & SEARCH OPTIMIZATION (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: {finance|governance|...}     # The primary domain this pattern belongs to.
  cross_domains: []                    # Other domains with strong connections.
  search_hints:
    primary_tension: "{Tension A} vs. {Tension B}"
    vector_keywords: []
  commons_assessment:
    stakeholder_architecture: 3        # 1-5. Who has voice and power?
    value_creation: 3                  # 1-5. Does it create shared value?
    resilience: 3                      # 1-5. Can it adapt and survive shocks?
    ownership: 3                       # 1-5. Is ownership distributed?
    autonomy: 3                        # 1-5. Does it enable self-governance?
    composability: 3                   # 1-5. Can it be combined with other patterns?
    fractal_value: 3                   # 1-5. Does value creation repeat at every scale?
    vitality: 3.0                      # NEW v7.1 — 0.0-5.0. Does it generate life?
    vitality_reasoning: >-             # NEW v7.1 — Concise explanation (1-3 sentences).
      {Reasoning for vitality score, including strengths and weaknesses.}
    overall_score: 3.0                 # Calculated average (now includes vitality).

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  usage_stage: design                  # {ideation|design|implementation|operation}
  adoption_stage: emerging             # {emerging|growth|mature}
  status: draft                        # {draft|revised|stable|deprecated}
  version: 1.0
  confidence: 2                        # {3|2|1} → ★★★|★★☆|★☆☆

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
  last_pruned: {YYYY-MM-DD}
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

> {A one-sentence summary of the pattern's core idea.}

> [!NOTE] Confidence Rating: ★★☆ (Medium)
> This rating reflects our confidence that this pattern is a good and correct
> solution to the stated problem. High (★★★) means it is a well-established,
> proven pattern. Medium (★★☆) means it is a promising but not yet fully proven
> solution. Low (★☆☆) means it is an emerging or experimental idea.

---

### Section 1: Context

*(100–200 words)*

{Describe the situation or environment in which the problem arises. Describe not just the structural situation but the living energy of the context — is this a system that is growing, stagnating, fragmenting, or decaying?}

---

### Section 2: Problem

*(100–200 words)*

> **The core conflict is {State the Primary Tension from the frontmatter}.**

{Describe the **forces** at play — the conflicting needs, constraints, and goals that make the problem difficult. What does it feel like to be caught between these forces?}

-   **Force 1:** {Description of the first conflicting need or constraint.}
-   **Force 2:** {Description of the second conflicting need or constraint.}
-   **Force 3:** {Description of the third conflicting need or constraint.}

---

### Section 3: Solution

*(200–400 words)*

> **Therefore, {State the core instruction of the solution in one bold sentence}.**

{Provide a detailed explanation. Describe the structure, participants, and collaborations involved. Explain the mechanism — how and why the solution resolves the forces described in Section 2. Include a diagram if it helps clarify the structure.}

---

### Section 4: Implementation

*(300–500 words)*

{Provide concrete, actionable steps for implementing the solution. This section should feel like a practical guide, not a theoretical treatise. Use code snippets, configuration examples, checklists, or step-by-step instructions. Frame the steps as acts of cultivation — tending, protecting, and growing the living system.}

---

### Section 5: Consequences

*(200–300 words)*

{Describe the trade-offs and implications of implementing this pattern. What new capacities for life does it create? What forms of decay does it make possible if not tended carefully? What are the known failure modes?}

---

### Section 6: Known Uses

*(200–300 words)*

{Provide at least two real-world examples of this pattern in action. Tell the stories of these living systems — don't just state facts. Link to the organizations or projects if possible.}

---

### Section 7: Cognitive Era

*(150–250 words)*

{How does this pattern change in the Cognitive Age? How does it interact with AI, autonomous agents, and distributed intelligence? Does it enable new forms of life and partnership? Does it create new vulnerabilities?}

---

### Section 8: Vitality

*(200–300 words)*

{This is the explicit diagnostic section. What does vitality look like in a system that uses this pattern? What are the signs of life? Conversely, what does decay look like? What are the warning signs that the pattern is being implemented in a way that stifles life? This section should provide a clear, actionable diagnostic for assessing the health of the pattern in practice.}
