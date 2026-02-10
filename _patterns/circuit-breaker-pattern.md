---
id: pat_019c47f4fd7475e1b8ca972489
page_url: https://commons-os.github.io/patterns/circuit-breaker-pattern/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/circuit-breaker-pattern.md
slug: circuit-breaker-pattern
title: Circuit Breaker Pattern
aliases:
- Client-Side Resiliency Pattern
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
- https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
- https://martinfowler.com/bliki/CircuitBreaker.html
- https://www.geeksforgeeks.org/system-design/what-is-circuit-breaker-pattern-in-microservices/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Circuit Breaker pattern is a critical design pattern used in modern software architecture to enhance the resilience and stability of distributed systems. It is primarily used to handle faults that may arise when communicating with remote services or resources, especially in microservices architectures where applications are composed of multiple, independently deployable services. The pattern prevents an application from repeatedly trying to execute an operation that is likely to fail, thereby avoiding the consumption of critical resources and allowing the failing service time to recover. This approach is analogous to an electrical circuit breaker that trips to prevent damage to a circuit during an overload or short circuit [1]. The concept was first popularized by Michael Nygard in his book "Release It!" and has since become a fundamental pattern for building fault-tolerant systems [2].

### 2. Core Principles

The Circuit Breaker pattern is implemented as a state machine with three distinct states that govern the flow of requests to a protected service:

*   **Closed:** This is the normal operational state where requests from the consumer are passed through to the protected service. The circuit breaker maintains a count of recent failures, and if this count exceeds a predetermined threshold within a specific time period, the circuit breaker transitions to the "Open" state.

*   **Open:** In this state, the circuit breaker immediately rejects all incoming requests without attempting to contact the protected service. This prevents the application from wasting resources on an operation that is likely to fail and protects the failing service from being overwhelmed with requests. After a configured timeout period, the circuit breaker transitions to the "Half-Open" state.

*   **Half-Open:** In this state, the circuit breaker allows a limited number of test requests to pass through to the protected service. If these requests are successful, the circuit breaker transitions back to the "Closed" state, assuming that the service has recovered. If any of the test requests fail, the circuit breaker reverts to the "Open" state and the recovery timeout period begins again [3].

<br>

| State | Description | Request Handling |
| :--- | :--- | :--- |
| **Closed** | The service is assumed to be healthy. | Requests are passed through to the service. |
| **Open** | The service is assumed to be down. | Requests are immediately rejected. |
| **Half-Open** | The service may have recovered. | A limited number of test requests are allowed. |

<br>

### 3. Key Practices

In distributed systems, particularly those based on a microservices architecture, services often make synchronous calls to other services to fulfill requests. A failure in one service can cascade to other services that depend on it. For example, a service might be unresponsive or experiencing high latency. If a consumer repeatedly retries a request to an unresponsive service, it can lead to the exhaustion of critical system resources such as threads, memory, and network connections. This can cause the consumer application to slow down or even crash, leading to a cascading failure that can impact the entire system. This problem is exacerbated in complex systems with many interdependent services, where a single point of failure can have a widespread impact [4].

### 4. Implementation

The Circuit Breaker pattern provides a solution to this problem by acting as a proxy or intermediary between the service consumer and the provider. It monitors the health of the provider service and, upon detecting a high failure rate, "trips" or "opens" the circuit. When the circuit is open, all subsequent requests to the provider are immediately failed without being sent over the network. This allows the provider service time to recover from its failure without being overwhelmed by a flood of requests. After a configurable "cool-down" period, the circuit breaker enters a "half-open" state, where it allows a single request to pass through to the provider. If this request succeeds, the circuit breaker returns to the "closed" state, and normal operation resumes. If the request fails, the circuit breaker returns to the "open" state, and the cool-down period begins again.

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


While the Circuit Breaker pattern offers significant benefits in terms of resilience and fault tolerance, there are several trade-offs and considerations to keep in mind:

*   **Complexity:** Implementing a circuit breaker adds complexity to the application. Developers need to manage the state of the circuit breaker and configure its parameters, such as the failure threshold, reset timeout, and the number of test requests in the half-open state.

*   **Configuration:** The effectiveness of the circuit breaker is highly dependent on its configuration. If the failure threshold is too low, the circuit may trip unnecessarily, leading to false positives. If the reset timeout is too long, the application may not recover quickly enough from a transient failure.

*   **Fallback Mechanisms:** When the circuit is open, the application should have a fallback mechanism in place to handle the failed requests. This could involve returning a default response, retrieving data from a cache, or queuing the request for later processing.

*   **Monitoring and Logging:** It is essential to monitor the state of the circuit breaker and log its transitions. This information can be used to diagnose problems and fine-tune the configuration of the circuit breaker.

### 6. When to Use

The Circuit Breaker pattern is widely used in many real-world systems and is supported by numerous libraries and frameworks:

*   **Netflix Hystrix:** Hystrix is a popular open-source library developed by Netflix that provides a robust implementation of the Circuit Breaker pattern. It is widely used in the Netflix microservices architecture to improve resilience and fault tolerance.

*   **Polly:** Polly is a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner.

*   **Spring Cloud Circuit Breaker:** The Spring Cloud ecosystem provides a circuit breaker implementation that can be used with various underlying providers like Resilience4J, Sentinel, or Hystrix.

*   **Service Meshes:** Modern service mesh technologies like Istio and Linkerd provide built-in support for the Circuit Breaker pattern, allowing developers to configure and manage circuit breakers declaratively without modifying the application code.

### 7. Anti-Patterns & Gotchas

In the cognitive era, where AI and machine learning models are increasingly integrated into applications, the Circuit Breaker pattern remains highly relevant. The cognitive era introduces new challenges and opportunities for the Circuit Breaker pattern:

*   **Adaptive Circuit Breaking:** The parameters of the circuit breaker, such as the failure threshold and reset timeout, can be dynamically adjusted based on real-time monitoring and machine learning models. This allows the circuit breaker to adapt to changing conditions and make more intelligent decisions about when to trip and when to reset.

*   **Proactive Failure Detection:** Machine learning models can be used to predict potential failures before they occur. This information can be used to proactively trip the circuit breaker and prevent failures from impacting the application.

*   **Intelligent Fallbacks:** When the circuit is open, AI-powered fallback mechanisms can be used to provide more intelligent and context-aware responses. For example, a chatbot could use natural language generation to provide a more helpful and informative response to a user when a backend service is unavailable.

### 8. References

The Circuit Breaker pattern aligns well with the principles of the Commons, particularly in the context of building resilient and sustainable digital platforms:

*   **Shared Resource:** By preventing cascading failures, the Circuit Breaker pattern helps to protect shared resources and ensure their availability for all users.

*   **Sustainability:** The pattern contributes to the long-term sustainability of a system by preventing resource exhaustion and reducing the likelihood of catastrophic failures.

*   **Community Benefit:** By improving the overall resilience and reliability of a platform, the Circuit Breaker pattern benefits the entire community of users who depend on it.

*   **Democratic Governance:** The configuration and monitoring of circuit breakers can be managed in a transparent and collaborative manner, allowing for community input and oversight.

*   **Equitable Access:** By ensuring the stability of the platform, the Circuit Breaker pattern helps to provide equitable access to all users, regardless of their location or network conditions.

### 8. References
[1] Microsoft. (2025, March 21). *Circuit Breaker Pattern*. Azure Architecture Center. Retrieved from https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

[2] Fowler, M. (2014, March 6). *CircuitBreaker*. Retrieved from https://martinfowler.com/bliki/CircuitBreaker.html

[3] GeeksforGeeks. (2026, January 21). *Circuit Breaker Pattern in Microservices*. Retrieved from https://www.geeksforgeeks.org/system-design/what-is-circuit-breaker-pattern-in-microservices/

[4] AWS. (n.d.). *Circuit breaker pattern*. AWS Prescriptive Guidance. Retrieved from https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html
