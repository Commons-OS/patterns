---
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/two-phase-commit-pattern.md
slug: two-phase-commit-pattern
title: Two-Phase Commit Pattern
aliases:
- 2PC
- Two-Phase Transaction
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: domain
  domain: technology
  category:
  - practice
  - tool
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 2
  commons_domain: &id001
  - business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- name: Manus AI
  role: author
- name: cloudsters
  role: author
sources:
- https://en.wikipedia.org/wiki/Two-phase_commit_protocol
- https://martinfowler.com/articles/patterns-of-distributed-systems/two-phase-commit.html
- https://www.geeksforgeeks.org/dbms/two-phase-commit-protocol-distributed-transaction-management/
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
id: pat_019c47f501177174905fdf85a8
page_url: https://commons-os.github.io/patterns/two-phase-commit-pattern/
commons_domain: *id001
---









### 1. Overview

The Two-Phase Commit (2PC) pattern is a distributed algorithm that ensures atomicity for transactions across multiple participating services or databases. In a distributed system, a transaction may consist of several operations on different nodes. The 2PC pattern coordinates all the processes that participate in a distributed atomic transaction to either commit or abort the transaction. This ensures that all participating nodes are in a consistent state, either all completing the transaction or all rolling it back. Its historical origins are rooted in the need for reliable transaction processing in distributed database systems, dating back to the 1980s [1].

### 2. Core Principles

The Two-Phase Commit protocol is based on two main phases, orchestrated by a coordinator:

*   **Phase 1: Prepare Phase (or Voting Phase):** The coordinator sends a "prepare" message to all participating nodes, asking them if they are ready to commit the transaction. Each participant that is ready to commit responds with a "prepared" message after durably storing the transaction's changes. If a participant cannot commit, it responds with a "no" vote.

*   **Phase 2: Commit Phase (or Completion Phase):** If the coordinator receives a "prepared" message from all participants, it sends a "commit" message to all of them. The participants then make their changes permanent and release any locked resources. If any participant votes "no" or fails to respond, the coordinator sends an "abort" message to all participants, and they roll back their changes.

### 3. Key Practices

In distributed systems, maintaining data consistency across multiple nodes during a transaction is a significant challenge. A transaction might involve updating records in several different databases or services. If one of these updates fails, the entire transaction must be rolled back across all nodes to maintain a consistent state. Without a coordination mechanism, some nodes might commit their changes while others abort, leading to data inconsistency. This is often referred to as the "atomic commit problem" [2].

### 4. Implementation

The Two-Phase Commit pattern provides a solution to the atomic commit problem by introducing a coordinator that manages the transaction lifecycle across all participating nodes. The coordinator ensures that the transaction is atomic by guaranteeing that all participants agree on the final outcome before any changes are made permanent. The two-phase process ensures that no node will commit its changes until all nodes have agreed to do so, and if any node is unable to commit, all nodes will abort the transaction.

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


The Two-Phase Commit pattern has several trade-offs:

| Pros | Cons |
| --- | --- |
| **Atomicity:** Guarantees that a distributed transaction is all-or-nothing. | **Blocking:** Participants must lock resources while waiting for the coordinator's decision, which can reduce concurrency and performance. |
| **Consistency:** Ensures that all nodes in the system remain in a consistent state. | **Single Point of Failure:** The coordinator is a single point of failure. If it fails, the participants may be blocked indefinitely. |

### 6. When to Use

*   **Database Systems:** Many relational database systems, such as Oracle, PostgreSQL, and MySQL, implement 2PC for distributed transactions.
*   **Transaction Managers:** Java EE application servers with JTA (Java Transaction API) use a transaction manager that acts as a coordinator in a 2PC protocol.
*   **Messaging Systems:** Some messaging systems that support transactional messaging use 2PC to coordinate message sends and receives with database updates.

### 7. Anti-Patterns & Gotchas

In the cognitive era, where AI and machine learning models are often part of larger distributed systems, the Two-Phase Commit pattern can be applied to ensure the consistency of model updates and data processing pipelines. For example, in a federated learning scenario, 2PC could be used to coordinate the update of a global model with the updates from multiple local models. However, the blocking nature of 2PC could be a significant drawback in these scenarios, where long-running training jobs could hold locks for extended periods.

### 8. References

The Two-Phase Commit pattern has a mixed alignment with the Commons principles:

*   **Shared Resource:** The pattern is designed to manage shared resources (data) in a distributed environment, ensuring their consistency.
*   **Democratic Governance:** The voting mechanism in the prepare phase has some resemblance to democratic governance, as all participants have a say in the outcome of the transaction. However, the coordinator holds the ultimate authority.
*   **Equitable Access:** The blocking nature of 2PC can lead to inequitable access to resources, as some processes may be starved while waiting for a transaction to complete.
*   **Sustainability:** The overhead of the 2PC protocol, especially in terms of network communication and resource locking, can impact the overall efficiency and sustainability of the system.
*   **Community Benefit:** By ensuring data consistency, the 2PC pattern provides a benefit to the community of users who rely on the correctness of the distributed system.

### References

[1] Wikipedia. (n.d.). *Two-phase commit protocol*. Retrieved from https://en.wikipedia.org/wiki/Two-phase_commit_protocol

[2] Fowler, M. (n.d.). *Patterns of Distributed Systems: Two-Phase Commit*. Retrieved from https://martinfowler.com/articles/patterns-of-distributed-systems/two-phase-commit.html
