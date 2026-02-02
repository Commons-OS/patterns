# ADR-013: The Context Engine - A Living Semantic Graph

**Status**: Proposed  
**Date**: 2026-02-02  
**Authors**: Manus AI, Cloudsters  
**Supersedes**: None  
**Related**: ADR-012 (Multi-Value Classification Fields)

---

## 1. Context and Problem Statement

The Commons OS Pattern Library currently contains over 1,200 patterns, classified using a multi-value system for domains and categories (ADR-012). While functional for basic filtering, this architecture is fundamentally static. It treats patterns as isolated documents with simple tags, failing to capture the rich, dynamic web of relationships that exists between them.

The current system cannot answer crucial questions of **perspective**:

> "Which patterns are relevant for a startup founder in the idea stage?"

> "What are the historical precedents and potential tensions when applying Steward Ownership in a cooperative enterprise?"

> "Given that I've adopted Sociocracy, what complementary patterns should I consider, and which ones might create friction?"

This limitation prevents us from realizing the core vision of the project: a system that provides not just information, but **context** and **perspective**. The fundamental insight is that **context IS the network of relationships**. Putting something "in perspective" means understanding its position within a web of connections—to other patterns, to the user's situation, to historical precedents, and to potential futures.

Our current classification is a flat, descriptive schema. What we need is a deep, relational, and context-aware engine that treats the pattern library as a living, evolving semantic network.

---

## 2. Decision Drivers

### 2.1 Static vs. Living Knowledge

A static knowledge graph, built once and maintained occasionally, is insufficient for a domain as dynamic as organizational design. The system must learn and evolve. The concept of a **"Living Ontology"** is critical: an ontology that revises its own structure in response to persistent explanatory failures, not individual edge cases [1]. When the graph consistently fails to connect patterns that users find related, or when new patterns emerge that don't fit existing categories, the structure itself must adapt.

### 2.2 Hierarchy vs. Network (Rhizomatic Structure)

A rigid, hierarchical taxonomy cannot model the complex, non-linear connections between patterns. A **rhizomatic structure**, as described by Deleuze and Guattari, is required [2]:

- **Connection**: Any pattern can connect to any other
- **Heterogeneity**: Different types of nodes (patterns, personas, concepts) can connect
- **Multiplicity**: No single root or hierarchy; multiple valid perspectives
- **Asignifying rupture**: The graph can be broken and reconnect elsewhere
- **Cartography**: The system maps relationships rather than tracing fixed paths

This is not a "non-hierarchical taxonomy" (a contradiction in terms) but rather a **semantic network** or **graph ontology** where hierarchy is one possible view among many.

### 2.3 Knowledge vs. Context

A standard **Knowledge Graph** describes "what is"—entities and their semantic relationships. A **Context Graph** extends this to describe "how it works" by including operational metadata [3]:

| Aspect | Knowledge Graph | Context Graph |
|--------|-----------------|---------------|
| Focus | Static semantics ("what is") | Dynamic operations ("how it works") |
| Time | Snapshot relationships | Validity periods, transaction history |
| Memory | Documentation | Decision traces, precedent links |
| Optimization | Human-friendly definitions | AI-optimized, hallucination-resistant |
| Policies | External documentation | Queryable policy nodes |

The Context Engine must be a **Context Graph**, capturing not just what patterns exist, but how they've been used, by whom, with what outcomes, and under what constraints.

### 2.4 Generic vs. Persona-Driven Retrieval

Retrieval must be personalized. The system must understand **who is asking** and adapt its response accordingly. This is the emerging field of **PersonaRAG** [4]. A startup founder and an enterprise architect asking about "governance patterns" need fundamentally different responses, not just filtered results.

### 2.5 Scalability and Network Effects

As the library grows, the number of potential relationships grows exponentially. With 1,200 patterns, there are potentially 1.4 million pairwise relationships. The architecture must:

- Manage this complexity without becoming unwieldy
- Surface emergent insights from the network (patterns of patterns)
- Leverage network effects where value compounds with scale (Metcalfe's Law)

---

## 3. Considered Options

### Option 1: Extend the Current System

Continue adding more tags and categories to the existing YAML-based classification.

**Pros**: Simple to implement, backward compatible  
**Cons**: Does not solve the core problem of static, non-relational knowledge; will become increasingly unwieldy as complexity grows

### Option 2: Implement a Standard Knowledge Graph

Use a traditional graph database (e.g., Neo4j) with a fixed ontology.

**Pros**: Captures relationships, mature tooling available  
**Cons**: Remains static; lacks mechanisms for evolution and context-awareness; requires significant infrastructure

### Option 3: Build a Living Context Graph (The Context Engine)

Architect a new system that treats the pattern library as a dynamic, evolving semantic network, integrating concepts from Living Ontologies, Context Graphs, and Persona-based retrieval.

**Pros**: Addresses all decision drivers; creates foundation for AI-powered applications; enables true context-aware retrieval  
**Cons**: Significant R&D investment; introduces complexity; requires new tooling

---

## 4. Decision Outcome

We will formally launch a research and build initiative for the **Context Engine**, architected as a **Living Context Graph**. This is not a one-time build but an ongoing, core project that will evolve alongside the pattern library.

The `context-engine` repository will house the formal specification and core engine. The `patterns-repo` will serve as the first implementation and primary data source.

### 4.1 High-Level Architecture Principles

**Core Data Model**: The graph will consist of multiple node types and richly-typed, weighted edges.

#### The Commons Entity Abstraction

A key insight is that individuals, organizations, cities, ecosystems, and other entities are all **fractal representations of a value-creating commons**. Rather than creating rigid, separate node types for each, we introduce a unified **Commons Entity** abstraction:

> A Commons Entity is any value-creating system that can adopt patterns, exist at a particular scale, and participate in the graph as both consumer and contributor.

This fractal model recognizes that the same structural patterns appear at different scales—a startup team, a cooperative, a city, and an ecological region all face questions of governance, resource allocation, and collective action.

| Node Type | Description | Examples |
|-----------|-------------|----------|
| `Pattern` | A documented pattern in the library | Sociocracy, Steward Ownership |
| `CommonsEntity` | Any value-creating system at any scale | Individual, Startup, Cooperative, City, Ecosystem |
| `Concept` | An abstract idea or principle | Decentralization, Consent-based Decision Making |
| `Source` | A reference, book, or authority | Eric Ries, Frederic Laloux |
| `Domain` | A commons domain | Business, Startup, Security, City, Ecology, Life |

**Commons Entity Properties**:

| Property | Description | Examples |
|----------|-------------|----------|
| `scale` | The fractal level of the entity | individual, team, organization, network, city, region, ecosystem |
| `type` | The specific entity type | human, ai_agent, startup, cooperative, municipality, watershed |
| `context` | Current situation, goals, constraints | idea-stage, growth-phase, transition, regeneration |
| `pattern_adoption` | Patterns this entity has adopted | Links to Pattern nodes with adoption metadata |
| `relationships` | Connections to other entities | inspired_by, partnered_with, part_of, governs |

This abstraction enables powerful queries:
- *"Show me patterns adopted by entities similar to mine"* (Lighthouse discovery)
- *"What patterns work at my scale?"* (Scale-appropriate recommendations)
- *"How did this city apply patterns originally designed for organizations?"* (Cross-scale learning)

**Edge Properties**: Relationships are first-class citizens with rich metadata:

| Property | Description |
|----------|-------------|
| `type` | Relationship type (enables, requires, tensions_with, specializes, generalizes) |
| `weight` | Strength of relationship (0.0 to 1.0) |
| `confidence` | How certain we are about this relationship |
| `provenance` | Source of this relationship (human, AI, usage) |
| `temporal_context` | When this relationship is valid or was established |
| `decision_trace` | History of changes to this relationship |

**Evolution Mechanism**: The graph is a "living" entity. Evolution is governed by:

1. **Persistent Explanatory Failure**: When the graph consistently fails to explain user queries or connect related patterns, this signals a need for structural change
2. **Human Judgment**: Curators and community members propose and validate changes
3. **AI Assistance**: AI agents suggest relationships, identify gaps, and flag inconsistencies
4. **Usage Signals**: How users navigate the graph informs its evolution

**Query Layer**: The engine will expose a context-aware query API combining:

- **Graph Traversal**: For explicit relationship queries (e.g., Cypher)
- **Vector Search**: For semantic similarity (embeddings)
- **Persona Context**: User's position influences results
- **GraphRAG Integration**: Combining structured and semantic retrieval [5]

### 4.2 The Central Role of Commons Entities (Including Personas)

All Commons Entities—whether individuals, organizations, cities, or ecosystems—are **active participants** in the graph's creation, use, and evolution. The traditional concept of "persona" is subsumed into this broader abstraction.

**Human Entities**:
- Define their context (role, goals, constraints, history)
- Their position in the graph determines what's relevant
- Their feedback drives graph evolution
- Examples: Startup Founder (Idea Stage), Cooperative Developer, City Planner, Ecosystem Steward

**Digital Entities (AI Agents)**:
- Operate within the graph on behalf of humans or organizations
- Have defined capabilities and constraints
- Can propose relationships and flag inconsistencies
- Examples: Pattern Discovery Agent, Relationship Validator, Context Synthesizer

**Organizational Entities (Lighthouses)**:
- Real-world implementations of patterns
- Provide evidence of what works in practice
- Their pattern adoption history informs recommendations
- Examples: Buurtzorg, Mondragon, Patagonia, Amsterdam (city), Costa Rica (nation)

**Ecological & Regional Entities**:
- Watersheds, bioregions, urban ecosystems
- Apply patterns at landscape and systems scale
- Examples: Chesapeake Bay Program, Barcelona Superblocks, Mondragón Valley

**Entity as Graph Position**: Any entity's "context" is represented as a position or state within the graph—a set of activated nodes and weighted relationships that define what's relevant from their perspective. This enables the same query mechanisms to work across all scales.

### 4.3 The Commons OS Context

The Context Engine is not a generic knowledge management system. It is purpose-built for the **Commons OS** vision:

- **Multi-Domain**: Supports patterns across Business, Startup, Security, City, Ecology, and Life domains
- **Commons-Aligned**: Prioritizes patterns that support shared resources, collective governance, and regenerative practices
- **Open and Evolving**: The graph itself is a commons, openly accessible and community-maintained
- **AI-Ready**: Designed from the ground up to power AI agents and applications

---

## 5. Consequences

### Positive

- Transforms the pattern library from a static archive into a dynamic, intelligent system
- Enables highly relevant, context-aware retrieval and discovery
- Creates a powerful foundation for future AI agents and applications
- The value of the system will compound as the network grows (network effects)
- Positions Commons OS as a leader in knowledge management for organizational design

### Negative

- This is a significant, long-term R&D investment
- Introduces substantial complexity compared to the current file-based system
- Requires a new suite of tools for graph maintenance, visualization, and querying
- Risk of over-engineering if not carefully scoped

### Mitigations

- Start with a Minimum Viable Graph (MVG) focused on existing relationships
- Maintain backward compatibility with current file-based system
- Iterate based on real usage and feedback
- Document decisions thoroughly (ADRs) to enable course correction

---

## 6. Next Steps: Deep Research Phase

This ADR formally kicks off a **deep research project** to answer the following key questions before full implementation begins:

### 6.1 Schema Definition

- What is the definitive, extensible schema for patterns, personas, and their relationships?
- What are all the necessary node and edge types and their properties?
- How do we model the multi-domain nature of Commons OS?

### 6.2 Evolution Governance

- How do we manage the "living" aspect of the graph?
- What is the process for proposing, validating, and implementing changes to the graph structure?
- Who has authority: human curators, AI agents, community consensus?
- How do we prevent both stagnation and chaotic change?

### 6.3 Context Modeling

- How do we represent a user's "context" as a queryable position within the graph?
- What dimensions define a persona's context (role, goals, stage, constraints)?
- How do we handle context that changes over time?

### 6.4 Technical Stack

- What is the appropriate technology stack (graph database, vector store, query language)?
- How do we balance sophistication with operational simplicity?
- Can we achieve the vision with file-based storage, or is a database required?
- What visualization tools support exploration of the graph?

### 6.5 Implementation Roadmap

- What is the phased plan for migrating from our current system to the Context Engine?
- What is the Minimum Viable Graph (MVG)?
- How do we maintain backward compatibility during transition?

---

## 7. References

[1] Chen, J. (2025, December 22). *Living Ontology with judgment-driven evolution*. LinkedIn. Retrieved from https://www.linkedin.com/pulse/living-ontology-judgment-driven-evolution-jinchun-chen-frm-xqx0c

[2] Deleuze, G., & Guattari, F. (1987). *A Thousand Plateaus: Capitalism and Schizophrenia*. University of Minnesota Press.

[3] Winks, E. (2026, January 27). *Context Graph vs Knowledge Graph: Key Differences for AI*. Atlan. Retrieved from https://atlan.com/know/context-graph-vs-knowledge-graph/

[4] PersonaRAG: Enhancing Retrieval-Augmented Generation Systems with User-Centric Agents. (2024, July 12). *arXiv*. Retrieved from https://arxiv.org/abs/2407.09394

[5] Lorica, B., & Rao, P. (2024, May 30). *GraphRAG: Design Patterns, Challenges, Recommendations*. Gradient Flow. Retrieved from https://gradientflow.substack.com/p/graphrag-design-patterns-challenges

---

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **Context Engine** | The proposed system for managing the living semantic graph |
| **Context Graph** | A knowledge graph extended with operational metadata (lineage, decisions, temporal context) |
| **Living Ontology** | An ontology that evolves its structure based on persistent explanatory failures |
| **Rhizomatic Structure** | A non-hierarchical network where any point can connect to any other |
| **Commons Entity** | Any value-creating system (individual, organization, city, ecosystem) that can adopt patterns and participate in the graph |
| **Persona** | A specific type of Commons Entity representing a human user archetype |
| **GraphRAG** | Graph-based Retrieval Augmented Generation, combining knowledge graphs with LLMs |
| **MVG** | Minimum Viable Graph, the initial implementation scope |
