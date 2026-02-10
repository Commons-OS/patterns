---
id: pat_019c47f4fd367bbfbc2d5f75c4
page_url: https://commons-os.github.io/patterns/bloom-filter-pattern/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/bloom-filter-pattern.md
slug: bloom-filter-pattern
title: Bloom Filter Pattern
aliases:
- Bloom Filter
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: domain
  domain: technology
  category:
  - tool
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
- https://en.wikipedia.org/wiki/Bloom_filter
- https://www.geeksforgeeks.org/system-design/bloom-filters-in-system-design/
- https://systemdesign.one/bloom-filters-explained/
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Bloom Filter pattern is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. It was conceived by Burton Howard Bloom in 1970. The trade-off for its efficiency is that it is probabilistic: it may return a false positive (indicating an element is in the set when it is not), but it will never return a false negative (indicating an element is not in the set when it is). This characteristic makes it particularly useful in scenarios where memory is a concern and a small rate of false positives is acceptable.

### 2. Core Principles

The core principles of the Bloom Filter pattern are:

*   **Probabilistic Set Representation:** A Bloom filter represents a set of elements in a probabilistic manner. It uses a bit array and a set of hash functions to do this.
*   **No False Negatives:** If the filter indicates that an element is not in the set, it is definitively not in the set.
*   **Potential for False Positives:** If the filter indicates that an element is in the set, it may or may not be. The probability of false positives can be controlled by the size of the bit array and the number of hash functions used.
*   **Space Efficiency:** Bloom filters are highly space-efficient compared to other data structures that perform the same task, such as hash tables.

### 3. Key Practices

In many large-scale systems, there is a need to check for the existence of an element in a large set. For example, a web browser might want to check if a URL is malicious, or a database might want to avoid expensive disk lookups for non-existent keys. Storing the entire set in memory can be infeasible due to memory constraints. A naive approach of storing all elements in a hash set would consume a large amount of memory, especially for large sets.

### 4. Implementation

The Bloom Filter pattern provides a space-efficient solution to this problem. It uses a bit array of a fixed size and a set of hash functions. When an element is added to the set, it is hashed by each of the hash functions, and the bits at the corresponding indices in the bit array are set to 1. To check if an element is in the set, it is hashed by the same hash functions, and the bits at the corresponding indices are checked. If all the bits are 1, the element is considered to be in the set. If any of the bits are 0, the element is definitively not in the set.

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


| Pros | Cons |
| --- | --- |
| Space-efficient | False positives are possible |
| Fast membership testing | Cannot delete elements |
| No false negatives | The size of the bit array and the number of hash functions must be chosen carefully to balance the false positive rate and memory usage |

### 6. When to Use

*   **Google Chrome:** Uses a Bloom filter to identify malicious URLs.
*   **Apache Cassandra:** Uses Bloom filters to reduce disk lookups for non-existent rows.
*   **Medium:** Uses Bloom filters to prevent recommending articles that a user has already read.
*   **Content Delivery Networks (CDNs):** Use Bloom filters to avoid caching one-hit wonders.

### 7. Anti-Patterns & Gotchas

In the cognitive era, Bloom filters can be used in various AI/ML applications. For example, they can be used to build more efficient recommendation systems by filtering out items that a user has already seen or interacted with. They can also be used in natural language processing to quickly check for the presence of words in a large vocabulary.

### 8. References

| Commons Principle | Assessment |
| --- | --- |
| Shared Resource | The Bloom Filter pattern can be considered a shared resource in the sense that it is a well-known and widely used data structure that can be used by anyone to build more efficient systems. |
| Democratic Governance | The pattern is not directly related to governance. |
| Equitable Access | The pattern is accessible to everyone and can be implemented in any programming language. |
| Sustainability | The pattern promotes sustainability by reducing memory usage and disk I/O, which can lead to energy savings. |
| Community Benefit | The pattern benefits the community by enabling the development of more efficient and scalable systems. |

### References

1.  Bloom, B. H. (1970). Space/time trade-offs in hash coding with allowable errors. Communications of the ACM, 13(7), 422-426.
2.  [https://en.wikipedia.org/wiki/Bloom_filter](https://en.wikipedia.org/wiki/Bloom_filter)
3.  [https://www.geeksforgeeks.org/system-design/bloom-filters-in-system-design/](https://www.geeksforgeeks.org/system-design/bloom-filters-in-system-design/)
