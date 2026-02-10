---
id: pat_019c47f500c67f2db5859b75ed
page_url: https://commons-os.github.io/patterns/strangler-fig-pattern/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/strangler-fig-pattern.md
slug: strangler-fig-pattern
title: Strangler Fig Pattern
aliases:
- Strangler Pattern
- Strangler Application
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: domain
  domain: platform
  category:
  - process
  - practice
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 3
  commons_domain:
  - platform
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- manus-ai
- cloudsters
sources:
- https://martinfowler.com/bliki/StranglerFigApplication.html
- https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Strangler Fig Pattern is an architectural pattern for incrementally migrating a legacy system by gradually replacing specific pieces of functionality with new applications and services. The term was coined by Martin Fowler, who was inspired by the strangler fig trees he saw in Australia. These trees grow by wrapping themselves around an existing tree, eventually replacing it entirely. In the same way, a new system is built around the legacy system, gradually taking over its functions until the legacy system can be decommissioned [1].

This pattern is a powerful strategy for managing the risk and complexity associated with modernizing large, monolithic systems. Instead of a high-risk "big bang" rewrite, the Strangler Fig Pattern offers a phased and controlled approach that allows the existing application to continue functioning during the modernization effort.

### 2. Core Principles

The Strangler Fig Pattern is defined by a set of core principles that guide its implementation:

| Principle | Description |
| :--- | :--- |
| **Incremental Replacement** | Functionality is moved from the legacy system to the new system in small, manageable increments. |
| **Coexistence** | The legacy and new systems coexist and operate in parallel during the migration process. |
| **Façade or Proxy** | An intermediary, often a façade or proxy, is used to intercept requests and route them to either the legacy system or the new system. |
| **Continuous Delivery** | The incremental nature of the pattern allows for the continuous delivery of new functionality and value to users. |

### 3. Key Practices

Many organizations rely on legacy systems that have become difficult to maintain and evolve. These systems are often monolithic, tightly coupled, and built on obsolete technologies. As business needs change and new technologies emerge, the pressure to modernize these systems grows. However, replacing a complex legacy system in a single operation (a "big bang" rewrite) is a high-risk, high-cost, and often-failed endeavor. The business cannot afford to freeze new feature development for the long period a rewrite would take, and the risk of failure is substantial.

### 4. Implementation

The Strangler Fig Pattern provides a solution to this problem by offering a gradual and controlled migration path. The solution involves three main steps:

1.  **Introduce a Façade:** A routing façade is placed in front of the legacy system. Initially, it simply passes all requests to the legacy system.
2.  **Implement New Functionality:** New functionality is built as separate services. The façade is then updated to route requests for this new functionality to the new services instead of the legacy system.
3.  **"Strangle" the Legacy System:** This process is repeated, with more and more functionality being moved to the new system. Over time, the legacy system is gradually "strangled" until it has no more functionality and can be safely decommissioned.

This approach allows the organization to modernize its systems incrementally, reducing risk and delivering value to users throughout the process.

### 5. 7 Pillars Assessment

| Pillar | Score (1-5) | Rationale |
|--------|-------------|-----------|
| Purpose | 3 | Serves a clear technical purpose in system design |
| Governance | 3 | Can be governed through standard engineering practices |
| Culture | 3 | Supports engineering culture of reliability and quality |
| Incentives | 3 | Aligns incentives toward system stability |
| Knowledge | 4 | Well-documented pattern with extensive community knowledge |
| Technology | 4 | Directly applicable to modern technology stacks |
| Resilience | 4 | Contributes to overall system resilience |
| **Overall** | **3.4** | **A valuable technical pattern that supports commons infrastructure** |


While the Strangler Fig Pattern offers significant advantages, it also has trade-offs and considerations that must be taken into account:

| Pros | Cons |
| :--- | :--- |
| Reduced risk compared to a "big bang" rewrite. | The migration process can be long and complex. |
| Continuous delivery of value to users. | The need for a transitional architecture adds complexity. |
| Allows for course correction during the migration. | The façade can become a bottleneck or a single point of failure. |
| Spreads the cost of modernization over time. | Managing data consistency between the legacy and new systems can be challenging. |

### 6. When to Use

The Strangler Fig Pattern is widely used in the industry for modernizing legacy systems. Some common examples include:

*   **Monolith to Microservices:** The pattern is a popular strategy for refactoring a monolithic application into a set of microservices. New functionality is built as microservices, and the façade routes requests to them, gradually strangling the monolith.
*   **Database Migration:** The pattern can be used to migrate from a legacy database to a new one. The new system can initially read from the legacy database and write to both, ensuring data consistency until the new database is ready to become the system of record [2].
*   **Cloud Migration:** When migrating an on-premises application to the cloud, the Strangler Fig Pattern can be used to move functionality to the cloud in a phased manner.

### 7. Anti-Patterns & Gotchas

In the cognitive era, the Strangler Fig Pattern remains highly relevant. It can be used to incrementally introduce AI/ML capabilities into legacy systems. For example, a legacy e-commerce application could use the pattern to add a new recommendation engine built as a separate AI-powered service. The façade would route product recommendation requests to the new service, while the rest of the application remains unchanged. This allows organizations to leverage the power of AI without having to rewrite their entire systems.

### 8. References

The Strangler Fig Pattern aligns with several of the Commons principles:

*   **Shared Resource:** The pattern promotes the creation of new, modular services that can be shared across the organization, rather than being locked within a monolithic application.
*   **Democratic Governance:** By breaking down a monolith into smaller services, the pattern can enable more decentralized and democratic governance of the system, with different teams taking ownership of different services.
*   **Equitable Access:** The pattern can improve equitable access by enabling the development of new, more accessible interfaces to legacy systems.
*   **Sustainability:** The pattern promotes the long-term sustainability of software systems by providing a path for their continuous evolution and modernization.
*   **Community Benefit:** By enabling the modernization of legacy systems, the pattern can help organizations to better serve their communities with more reliable, scalable, and feature-rich applications.

### 8. References
[1] Fowler, M. (2019). *Strangler Fig Application*. [https://martinfowler.com/bliki/StranglerFigApplication.html](https://martinfowler.com/bliki/StranglerFigApplication.html)
[2] Microsoft. (2023). *Strangler Fig Pattern*. [https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
