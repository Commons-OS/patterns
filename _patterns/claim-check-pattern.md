---
id: pat_019c47f4fd7b7fdd9fec058378
page_url: https://commons-os.github.io/patterns/claim-check-pattern/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/claim-check-pattern.md
slug: claim-check-pattern
title: Claim-Check Pattern
aliases:
- Reference-Based Messaging
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
- https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check
- https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Claim-Check pattern is a design pattern used in messaging architectures to handle large messages efficiently. Instead of sending a large data payload directly through a messaging system, the pattern advocates for storing the payload in an external data store and sending a much smaller reference, or "claim check," within the message itself. The receiving component can then use this claim check to retrieve the full payload from the data store when needed. This approach prevents large messages from overwhelming the messaging infrastructure, which is typically optimized for high volumes of small messages [1].

The pattern's name is derived from the analogy of a luggage claim check at an airport. A traveler checks in their heavy luggage and receives a small ticket with a reference number. They can then travel lightly and use the ticket to reclaim their luggage at the destination. Similarly, in this pattern, the message travels lightly with just the claim check, and the heavy payload is retrieved only when required [2].

### 2. Core Principles

The Claim-Check pattern is defined by a few fundamental principles:

*   **Payload Separation:** The core principle is the decoupling of the large data payload from the primary message. The message bus is used for communication and coordination, not for data transfer.
*   **Externalized Storage:** The large payload is stored in a suitable external data store, such as a blob store, a distributed file system, or a database. This store is optimized for handling large data objects.
*   **Reference-Based Retrieval:** A unique identifier, the "claim check," is generated for the stored payload. This reference is included in the message and used by the consumer to fetch the data directly from the external store.
*   **On-Demand Access:** The consumer of the message retrieves the payload only when it needs to process it. This avoids unnecessary data transfer and processing for intermediate components in a message flow that may not need the full payload.

### 3. Key Practices

In distributed systems, particularly those built on messaging and event-driven architectures, components communicate by exchanging messages. However, messaging systems often have limitations on the size of messages they can handle. Sending messages that exceed these limits can lead to errors and failures. Furthermore, even if the messaging system can handle large messages, their transmission and storage can consume significant resources, leading to increased latency, reduced throughput, and higher operational costs. This can degrade the overall performance and scalability of the system [1].

### 4. Implementation

The solution provided by the Claim-Check pattern is to offload the large payload to an external data store. The process is as follows:

1.  The message producer, before sending a message, determines if the payload is large.
2.  If the payload is large, the producer stores it in an external data store (e.g., Amazon S3, Azure Blob Storage, or a database).
3.  The data store returns a unique key or reference for the stored object.
4.  The producer then creates a new, smaller message that contains this reference (the claim check) instead of the large payload.
5.  This smaller message is sent to the message bus.
6.  The message consumer receives the small message, extracts the claim check, and uses it to retrieve the full payload directly from the external data store.
7.  After processing, the consumer may be responsible for deleting the payload from the data store to manage storage costs and lifecycle.

This process ensures that the message bus only handles small, lightweight messages, preserving its performance and reliability.

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


While the Claim-Check pattern offers significant benefits, it also introduces certain trade-offs and considerations:

| Pros | Cons |
| :--- | :--- |
| **Improved Performance:** Prevents the message bus from becoming a bottleneck, improving throughput and latency. | **Increased Complexity:** Introduces an additional component (the data store) and more steps in the message processing logic. |
| **Scalability:** Allows the system to handle arbitrarily large messages, limited only by the capacity of the external data store. | **Data Management Overhead:** Requires a mechanism for managing the lifecycle of the stored payloads, including deletion after consumption to avoid orphaned data and unnecessary costs. |
| **Cost Efficiency:** Can reduce costs associated with message bus usage, as pricing is often based on message size and volume. | **Potential for Latency:** Adds an extra network hop to retrieve the payload, which can increase latency for the end-to-end process. |
| **Enhanced Security:** Sensitive data can be stored in a secure data store with fine-grained access control, rather than being transmitted through the message bus. | **Point of Failure:** The external data store becomes a critical component; if it is unavailable, consumers will not be able to process messages. |

### 6. When to Use

*   **E-commerce Order Processing:** In an e-commerce platform, an order might include large image files for customized products. Instead of embedding these images in the order message, the images are stored in a blob store, and the order message contains only the URLs (claim checks) to the images.
*   **Video Processing Pipelines:** A video upload service might use a messaging queue to trigger different processing steps (e.g., transcoding, thumbnail generation). The large video file is stored in a distributed file system, and the messages on the queue contain a reference to the video file.
*   **Azure Implementation:** Microsoft Azure provides several examples of implementing the Claim-Check pattern using services like Azure Service Bus for messaging, Azure Blob Storage for the data store, and Azure Event Grid to automate the generation of the claim check [1].

### 7. Anti-Patterns & Gotchas

In the cognitive era, with the rise of AI and machine learning, the Claim-Check pattern becomes even more relevant. AI/ML workloads often involve very large data payloads, such as:

*   **Machine Learning Models:** Trained models can be several gigabytes in size. When deploying models or passing them between services for inference, the Claim-Check pattern can be used to avoid clogging messaging systems.
*   **Large Datasets:** Training and batch inference processes often operate on large datasets. Messages that trigger these processes can use a claim check to refer to the dataset's location in a data lake or warehouse.
*   **Rich Media for Analysis:** AI services that analyze images, videos, or audio can use the Claim-Check pattern to handle the large media files. A message might trigger an analysis workflow, carrying a claim check that points to the media file in a cloud storage bucket.

By separating the large data artifacts from the control messages, the Claim-Check pattern enables the creation of scalable, resilient, and efficient AI/ML pipelines.

### 8. References

The Claim-Check pattern aligns with the principles of the Commons in several ways:

*   **Shared Resource:** The pattern promotes the efficient use of the message bus as a shared resource by preventing it from being monopolized by large messages. This ensures that the messaging system remains available and performant for all services that rely on it.
*   **Sustainability:** By optimizing resource utilization and potentially reducing operational costs, the pattern contributes to the long-term sustainability of the platform. The explicit need for data lifecycle management (deleting consumed payloads) also encourages sustainable practices.
*   **Equitable Access:** By keeping the shared messaging infrastructure healthy, the pattern ensures that all components, regardless of the size of the data they process, have equitable access to the communication backbone of the system.

However, the added complexity can be a barrier to smaller teams or less mature organizations. The governance of the external data store, including access control and data retention policies, becomes a critical aspect of ensuring the pattern is implemented in a way that is secure and beneficial to the community of users.

### References

[1] Microsoft. (n.d.). *Claim-Check pattern - Azure Architecture Center*. Retrieved February 10, 2026, from https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check

[2] Hohpe, G., & Woolf, B. (2003). *Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions*. Addison-Wesley Professional.
