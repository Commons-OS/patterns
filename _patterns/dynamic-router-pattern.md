---
id: pat_019c47f4fe4c79899431e5bc78
page_url: https://commons-os.github.io/patterns/dynamic-router-pattern/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/dynamic-router-pattern.md
slug: dynamic-router-pattern
title: Dynamic Router Pattern
aliases:
- Dynamic Routing
- Adaptive Routing
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: domain
  domain: technology
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
  - business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- manus-ai
- cloudsters
sources:
- https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html
- https://docs.redhat.com/en/documentation/red_hat_jboss_fuse/6.2/html/apache_camel_development_guide/dynamicrouter
- https://en.wikipedia.org/wiki/Dynamic_routing
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Dynamic Router is a messaging pattern that enables the routing of messages to different destinations based on a set of rules that can be changed at runtime. This pattern is particularly useful in distributed systems where the number of destinations can change over time, and where it is not desirable to have to reconfigure the router every time a destination is added or removed [1].

The concept of dynamic routing has its roots in computer networking, where it is used to describe the capability of a network to 'route around' damage, such as loss of a node or a connection between nodes, as long as other path choices are available [3]. In the context of enterprise integration, the Dynamic Router pattern allows for a similar level of flexibility and resilience, by enabling the routing logic to be updated dynamically.

### 2. Core Principles

The Dynamic Router pattern is based on the following core principles:

*   **Runtime Configuration:** The routing rules can be updated at runtime, without having to stop or restart the router.
*   **Self-Configuration:** Destinations can register and deregister themselves with the router, by sending special configuration messages to a control channel.
*   **Rule-Based Routing:** The routing logic is based on a set of rules that are evaluated for each incoming message. The rules determine which destination the message should be sent to.

### 3. Key Practices

In a distributed system, it is often necessary to route messages to a set of destinations that can change over time. For example, new services may be added, or existing services may be removed or updated. In such a dynamic environment, it can be difficult to maintain the routing logic, especially if the router has to be manually reconfigured every time a destination changes. This can lead to a system that is brittle and difficult to maintain.

### 4. Implementation

The Dynamic Router pattern provides a solution to this problem by allowing the routing logic to be updated dynamically. The router has a control channel that allows destinations to register and deregister themselves. When a destination registers itself, it provides a set of rules that specify the conditions under which it can handle a message. These rules are stored in a rule base.

When a message arrives, the router evaluates the rules in the rule base and routes the message to the destination whose rules are fulfilled. This allows for efficient, predictive routing without the maintenance dependency of the router on each potential recipient [1].

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


### Pros

*   **Flexibility:** The routing logic can be updated at runtime, without having to stop or restart the router.
*   **Scalability:** New destinations can be added without having to reconfigure the router.
*   **Resilience:** The router can 'route around' failed destinations, as long as other path choices are available.

### Cons

*   **Increased Complexity:** The implementation of a Dynamic Router can be more complex than that of a static router.
*   **Performance Overhead:** The evaluation of the routing rules can introduce a performance overhead.

### 6. When to Use

*   **Apache Camel:** Apache Camel provides an implementation of the Dynamic Router pattern, which allows the routing slip to be computed on-the-fly [2].
*   **Spring Integration:** Spring Integration also provides support for dynamic routing, allowing for the configuration of routers to be changed dynamically without bringing down the system.

### 7. Anti-Patterns & Gotchas

In the age of AI/ML, the Dynamic Router pattern can be used to route requests to different models based on the input data. For example, a Dynamic Router could be used to route a request to a specific machine learning model based on the language of the input text, or the type of image.

This can be particularly useful in scenarios where there are multiple models that can handle a request, and where the best model to use depends on the specific characteristics of the input data. By using a Dynamic Router, it is possible to create a system that can automatically select the best model for each request, without having to manually configure the routing logic.

### 8. References

*   **Shared Resource:** The Dynamic Router can be seen as a shared resource that is used by multiple services in a distributed system. By providing a centralized routing service, the Dynamic Router can help to reduce the duplication of routing logic across services.
*   **Democratic Governance:** The control channel of the Dynamic Router allows for a form of democratic governance, where destinations can register and deregister themselves. This allows for a more decentralized and flexible system, where the routing logic is not controlled by a single entity.
*   **Equitable Access:** The Dynamic Router provides equitable access to the routing service, as any service can register itself as a destination, as long as it can handle the messages that are sent to it.
*   **Sustainability:** The Dynamic Router can help to improve the sustainability of a system, by making it more resilient to failures. By being able to 'route around' failed destinations, the Dynamic Router can help to ensure that the system remains available, even in the event of a partial failure.
*   **Community Benefit:** The Dynamic Router can provide a benefit to the community, by making it easier to build and maintain distributed systems. By providing a flexible and resilient routing service, the Dynamic Router can help to reduce the complexity of building and managing distributed systems.

### 8. References
[1] [Enterprise Integration Patterns: Dynamic Router](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html)
[2] [Apache Camel Development Guide: Dynamic Router](https://docs.redhat.com/en/documentation/red_hat_jboss_fuse/6.2/html/apache_camel_development_guide/dynamicrouter)
[3] [Wikipedia: Dynamic routing](https://en.wikipedia.org/wiki/Dynamic_routing)
