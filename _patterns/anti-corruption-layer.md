---
id: pat_019c47f4fce37db2a16938101b
page_url: https://commons-os.github.io/patterns/anti-corruption-layer/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/anti-corruption-layer.md
slug: anti-corruption-layer
title: Anti-Corruption Layer
aliases:
- ACL
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: domain
  domain: platform
  category:
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
- https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer
- https://microservices.io/patterns/refactoring/anti-corruption-layer.html
- https://martinfowler.com/bliki/AntiCorruptionLayer.html
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Anti-Corruption Layer (ACL) is a design pattern used in software architecture to isolate a system from the complexities and potential "corruption" of external or legacy systems. It acts as a translation layer, mediating between the domain model of the core system and the data models or APIs of external systems. This pattern was first introduced by Eric Evans in his book, "Domain-Driven Design: Tackling Complexity in the Heart of Software" [1]. The primary significance of the ACL is to protect the integrity and consistency of the core domain model, allowing it to evolve independently without being constrained by the design decisions of other systems.

### 2. Core Principles

The Anti-Corruption Layer is defined by a set of core principles that guide its implementation and use:

*   **Isolation:** The ACL creates a distinct boundary between the core application and the external system, preventing direct dependencies.
*   **Translation:** It is responsible for translating data and commands between the two systems, which may have different semantic models.
*   **Facade:** The ACL can be implemented as a facade, presenting a simplified and consistent interface to the core application for interacting with the external system.
*   **Adapter:** It can also function as an adapter, converting the interface of the external system into an interface that the core application can understand.

### 3. Key Practices

When a modern application needs to integrate with a legacy system or a third-party service, it often faces challenges due to differing data models, APIs, and underlying technologies. The legacy system might have a convoluted data schema, or its API might be outdated and difficult to use. Forcing the modern application to conform to the legacy system's semantics can lead to a "corrupted" and overly complex design, hindering its maintainability and future development. This is particularly problematic during a gradual migration from a monolithic architecture to a microservices-based one, where new services must coexist and interact with the legacy monolith.

### 4. Implementation

The Anti-Corruption Layer pattern addresses this problem by introducing a mediating layer between the two systems. This layer is responsible for all communication and translation. When the core application needs to interact with the external system, it sends a request to the ACL using its own domain model. The ACL then translates this request into a format that the external system can understand and forwards it. Conversely, when the external system sends a response, the ACL translates it back into the core application's domain model before passing it on. This ensures that the core application remains "uncorrupted" by the external system's design.

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


While the Anti-Corruption Layer pattern offers significant benefits, it also introduces some trade-offs:

| Pros | Cons |
| --- | --- |
| Protects the core domain model from external influences. | Adds an extra layer of complexity to the system. |
| Allows the core application to evolve independently. | Can introduce latency due to the translation process. |
| Simplifies the interaction with complex or poorly designed external systems. | Requires additional development and maintenance effort. |

Considerations for implementing an ACL include its scalability, how it will be managed and monitored, and whether it should handle all communication or just a subset of features. In the context of a migration, it's also important to decide if the ACL is a temporary or permanent component of the architecture.

### 6. When to Use

A common real-world example of the Anti-Corruption Layer is in the context of migrating a monolithic e-commerce application to a microservices architecture. The monolith may have a large, complex database and a tightly coupled set of services. As new microservices are developed for features like order management or customer relationship management, they need to interact with the legacy monolith to access existing data. An ACL can be implemented to mediate between the new microservices and the monolith. For instance, a new "Order" microservice can communicate with the ACL using its own clean, modern data model, and the ACL will translate those communications to the legacy monolith's data model.

### 7. Anti-Patterns & Gotchas

In the cognitive era, where AI and machine learning models are increasingly integrated into applications, the Anti-Corruption Layer pattern remains highly relevant. AI/ML models often have their own specific data formats and APIs. An ACL can be used to isolate the core application from the complexities of these models, allowing for easier integration and the ability to swap out models without impacting the core application. For example, an application using a natural language processing (NLP) model for sentiment analysis could use an ACL to translate between its internal data structures and the input/output formats required by the NLP service.

### 8. References

The Anti-Corruption Layer pattern aligns with several of the Commons principles:

*   **Shared Resource:** The ACL itself can be a shared resource, providing a common interface for multiple services within a system to interact with an external system.
*   **Democratic Governance:** By isolating systems and promoting loose coupling, the ACL allows different teams to work on different parts of a system with greater autonomy.
*   **Equitable Access:** The ACL can provide a simplified and consistent interface to a complex legacy system, making it more accessible to new services and developers.
*   **Sustainability:** By protecting the core domain model, the ACL contributes to the long-term sustainability and maintainability of the application.
*   **Community Benefit:** In an open-source or collaborative environment, a well-designed ACL can benefit the entire community by making it easier to integrate with external systems.

Based on this assessment, the Anti-Corruption Layer pattern receives a Commons Alignment score of **3 out of 5**.

### References

[1] Evans, E. (2004). _Domain-Driven Design: Tackling Complexity in the Heart of Software_. Addison-Wesley Professional.
[2] Microsoft. (n.d.). _Anti-corruption Layer pattern_. Azure Architecture Center. Retrieved from https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer
[3] Richardson, C. (n.d.). _Pattern: Anti-corruption layer_. Microservices.io. Retrieved from https://microservices.io/patterns/refactoring/anti-corruption-layer.html
