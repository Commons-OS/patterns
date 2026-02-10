---
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/sequential-convoy-pattern.md
slug: sequential-convoy-pattern
title: Sequential Convoy Pattern
aliases:
- Ordered Message Processing
- FIFO Message Groups
version: "1.0"
created: "2026-02-10 00:00:00+00:00"
modified: "2026-02-10 00:00:00+00:00"
classification:
  universality: context-dependent
  domain: platform
  category:
  - messaging
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 2
  commons_domain:
  - platform
generalizes_from: []
specializes_to: []
enables: []
requires: []
related:
- competing-consumers
- message-queue
contributors:
- Manus AI
- cloudsters
sources:
- https://learn.microsoft.com/en-us/azure/architecture/patterns/sequential-convoy
- https://www.willvelida.com/posts/sequential-convoy-pattern/
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

## 1. Overview

The Sequential Convoy pattern is a messaging pattern that ensures groups of related messages are processed in a first-in-first-out (FIFO) order, without blocking the processing of other, unrelated groups of messages. This pattern is particularly significant in distributed systems where horizontal scaling and parallel processing are common. While scaling out consumers of a message queue generally improves throughput, it can also lead to messages being processed out of their intended order. The Sequential Convoy pattern addresses this by introducing a mechanism to enforce ordering for specific subsets of messages, thereby maintaining data consistency and integrity for stateful operations.

The historical origins of this pattern are rooted in enterprise integration and message-oriented middleware. As systems became more distributed and asynchronous, the need to manage ordered sequences of events became critical. The term "convoy" aptly describes a group of messages traveling together in a specific sequence. The pattern has seen a resurgence in modern cloud-native architectures, where serverless functions and microservices often rely on message queues for communication and workflow orchestration. The ability to process messages in order at the level of a specific entity (like a customer order or a user session) while processing messages for other entities in parallel is a key enabler for building robust and scalable distributed applications.

## 2. Core Principles

The Sequential Convoy pattern is defined by a set of fundamental principles that ensure both ordered processing and scalability. These principles are essential for the correct implementation and functioning of the pattern.

| Principle | Description |
| :--- | :--- |
| **Categorization** | Incoming messages are grouped into distinct categories based on a shared identifier. This identifier, often referred to as a session ID or correlation ID, is what defines a "convoy" of related messages. For example, in an e-commerce system, all messages related to a specific order would share the same order ID as their category identifier. |
| **Sequential Processing within a Category** | All messages belonging to the same category must be processed in a strict first-in-first-out (FIFO) order. This ensures that operations are executed in the sequence they were intended, preserving the integrity of stateful processes. |
| **Parallel Processing between Categories** | While processing within a category is sequential, different categories can be processed concurrently by multiple consumers. This allows the system to scale horizontally, handling a high volume of messages as long as they are distributed across different categories. |
| **Exclusive Locking** | A consumer must be able to acquire an exclusive lock on a specific category. This lock prevents other consumers from processing messages from the same category simultaneously, thereby avoiding race conditions and ensuring that the sequential processing principle is upheld. |

## 3. Problem Statement

In modern distributed systems, message-driven architectures are a common approach for decoupling services and managing asynchronous workflows. A typical pattern used in these architectures is the [Competing Consumers pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers), where multiple consumers process messages from a single queue in parallel. This approach is highly effective for increasing throughput and improving the overall scalability of the system. [1]

However, this parallel processing model introduces a significant challenge: the loss of message order. When multiple consumers are independently pulling messages from a queue, there is no guarantee that the messages will be processed in the same order they were sent. For many business processes, the sequence of operations is critical. For instance, in an order management system, an `OrderCreated` event must be processed before an `OrderUpdated` event for the same order. If these events are processed out of order, it can lead to data inconsistencies, incorrect state transitions, and difficult-to-diagnose system errors.

The core problem, therefore, is how to **reconcile the need for scalable, parallel message processing with the requirement for strict ordering for related messages**. A naive solution of using a single consumer to process all messages sequentially would solve the ordering problem but would create a significant performance bottleneck, defeating the purpose of a distributed architecture. The Sequential Convoy pattern directly addresses this challenge by providing a mechanism to enforce order where it matters, without sacrificing the ability to process unrelated messages in parallel.

## 4. Solution

The Sequential Convoy pattern provides an elegant solution to the problem of ordered message processing in a scalable, distributed environment. The solution involves a combination of message categorization, queueing mechanisms, and consumer logic to ensure that related messages are processed sequentially while unrelated messages are processed in parallel.

The implementation of the pattern can be broken down into the following steps:

1.  **Message Categorization:** As messages are produced, they are assigned a category identifier. This identifier, often called a **session ID** or **group ID**, is a piece of metadata attached to the message. All messages that need to be processed in a specific order share the same session ID. For example, in an order processing system, the order ID would be the natural choice for the session ID.

2.  **Queueing and Session Awareness:** The message queueing system must support the concept of sessions or message groups. When a message with a session ID is sent to the queue, the broker ensures that it is associated with that session. Modern messaging systems like Azure Service Bus and Apache Kafka provide this functionality out of the box.

3.  **Consumer Locking and Processing:** Consumers are configured to lock and process messages on a per-session basis. When a consumer is ready to process a message, it requests a session from the queue. The message broker then provides the consumer with a session that has pending messages, along with an exclusive lock on that session. The consumer can then process all the messages within that session in a FIFO manner. Once all the messages in the session are processed, the consumer releases the lock, making the session available for other consumers if new messages arrive.

This approach is illustrated in the following diagram:

```
+----------+     +-----------------+     +-----------------------+     +-----------+
| Producer | --> |      Queue      | --> | Session-Aware Consumer| --> | Processed |
+----------+     | (with Sessions) |     | (Locks Session A)     |     | Message A1|
               +-----------------+     +-----------------------+     +-----------+
                                       |
                                       +-----------------------+     +-----------+
                                       | Session-Aware Consumer| --> | Processed |
                                       | (Locks Session B)     |     | Message B1|
                                       +-----------------------+     +-----------+
```

In this diagram, messages for different sessions (A and B) are sent to the same queue. However, the consumers are session-aware. One consumer locks and processes messages for Session A, while another consumer locks and processes messages for Session B. This allows for parallel processing of sessions, while maintaining strict order within each session.

## 5. Trade-offs and Considerations

While the Sequential Convoy pattern offers a powerful solution for ordered message processing, it's important to consider its trade-offs and potential challenges before implementing it. A thorough understanding of these factors will help in making informed architectural decisions.

| Aspect | Pros | Cons & Considerations |
| :--- | :--- | :--- |
| **Ordering and Consistency** | Guarantees FIFO processing for related messages, which is critical for maintaining data consistency in stateful applications. | The strict ordering requirement can limit the overall throughput of a single convoy. If one message in a convoy is slow to process, it will delay all subsequent messages in the same convoy. |
| **Scalability** | Allows for horizontal scaling by processing different convoys in parallel. This is a significant advantage over a single-threaded consumer model. | The degree of parallelism is limited by the number of active convoys. If the message load is not evenly distributed across convoys, some consumers may be idle while others are overloaded. This is often referred to as the "hot partition" problem. |
| **Complexity** | The pattern is relatively straightforward to understand and implement with modern messaging systems that provide built-in support for sessions or message groups. | The implementation can become more complex if the messaging system does not natively support sessions. In such cases, a custom solution for session management and locking would be required, which can be error-prone. |
| **Error Handling** | The pattern simplifies error handling for a sequence of related operations. If a message fails to process, it can be retried without affecting other convoys. | A failed message can block the processing of all subsequent messages in the same convoy. A robust dead-lettering and retry mechanism is essential to prevent a single failed message from halting an entire convoy indefinitely. |
| **Evolvability** | The pattern is extensible. New types of convoys can be added to the system without impacting existing ones. | Careful consideration must be given to how new message types are introduced into an existing convoy. Changes to the message contract or the processing logic must be backward-compatible to avoid breaking the sequential processing guarantee. |

## 6. Real-world Examples

The Sequential Convoy pattern is used in a variety of real-world scenarios where ordered processing of related messages is a critical requirement. Here are a few examples:

*   **E-commerce Order Processing:** As mentioned earlier, this is a classic use case for the Sequential Convoy pattern. All events related to a customer's order, such as `OrderPlaced`, `PaymentProcessed`, `OrderShipped`, and `OrderDelivered`, must be processed in the correct sequence. Using the order ID as the session ID ensures that all events for a single order are processed by the same consumer in a FIFO manner, while orders from different customers can be processed in parallel.

*   **Financial Transactions:** In financial systems, the order of transactions is paramount. For example, a series of debits and credits to a bank account must be processed in the exact order they occurred to ensure the final balance is correct. The account number can be used as the session ID to create a convoy for all transactions related to a specific account.

*   **User Session Management:** In a web application, all events generated by a user within a single session (e.g., `Login`, `AddToCart`, `Checkout`, `Logout`) might need to be processed sequentially to maintain a consistent view of the user's state. The user's session ID can be used to group these events into a convoy.

*   **IoT Data Ingestion:** In an IoT scenario, a single device might send a stream of sensor readings that need to be processed in order to detect trends or anomalies. The device ID can be used as the session ID to ensure that all readings from a specific device are processed sequentially.

## 7. Cognitive Era Considerations

In the cognitive era, where AI and machine learning are becoming increasingly prevalent, the Sequential Convoy pattern remains highly relevant and can be adapted to support new use cases. The ability to process sequential data in order is fundamental to many machine learning tasks, such as natural language processing (NLP) and time-series analysis.

For example, in an NLP pipeline, a document might be broken down into a sequence of sentences or paragraphs that need to be processed in order to understand the context and meaning of the text. The document ID could be used as the session ID to ensure that the parts of the document are processed sequentially by a series of NLP models (e.g., for sentiment analysis, entity extraction, and summarization).

Furthermore, the Sequential Convoy pattern can be used to manage the state of conversational AI agents. Each conversation with a user can be treated as a convoy, with the conversation ID as the session ID. This ensures that all messages in a conversation are processed in order, allowing the AI agent to maintain a coherent and context-aware dialogue with the user.

## 8. Commons Alignment Assessment

The Sequential Convoy pattern can be assessed against the five principles of the Commons to understand its potential for contributing to a shared, open, and equitable digital ecosystem.

*   **Shared Resource:** The pattern itself is a shared resource in the form of a design pattern that can be freely used and adapted by the software development community. The underlying messaging infrastructure can also be a shared resource, such as a multi-tenant message broker.

*   **Democratic Governance:** The governance of the pattern is largely decentralized, with its evolution being driven by the collective experience of the developer community. However, the implementation of the pattern within a specific organization will be subject to the governance policies of that organization.

*   **Equitable Access:** The pattern is accessible to any developer or organization that has access to the necessary messaging technologies. Many open-source and commercial messaging systems support the features required to implement this pattern, making it widely accessible.

*   **Sustainability:** The pattern contributes to the sustainability of software systems by providing a robust and scalable solution for ordered message processing. This can lead to more resilient and maintainable systems, reducing the long-term costs of software development and maintenance.

*   **Community Benefit:** The pattern provides a significant benefit to the developer community by offering a standardized solution to a common problem. This can help to improve the quality and reliability of software systems, which in turn benefits the end-users of those systems.

Overall, the Sequential Convoy pattern aligns well with the principles of the Commons, particularly in its role as a shared and accessible resource that contributes to the sustainability and community benefit of the software ecosystem.

### References

[1] Microsoft. (n.d.). *Sequential Convoy pattern*. Azure Architecture Center. Retrieved February 10, 2026, from https://learn.microsoft.com/en-us/azure/architecture/patterns/sequential-convoy

[2] Velida, W. (2024, January 26). *The Sequential Convoy Pattern*. Will Velida. Retrieved February 10, 2026, from https://www.willvelida.com/posts/sequential-convoy-pattern/
