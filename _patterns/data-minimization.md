---
id: pat_41981f664dc944aa9d7b6bc0
page_url: https://commons-os.github.io/patterns/data-minimization/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/data-minimization.md
slug: data-minimization
title: Data Minimization
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
classification:
  universality: universal
  domain: privacy
  category:
  - pattern
  era:
  - cognitive
  origin:
  - commons-os
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- manus-ai
- cloudsters
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

Data Minimization is a pattern for building resilient value creation systems.

**Problem:** Value creation systems often collect more personal data than necessary, increasing privacy risks, storage costs, and the potential for misuse. This over-collection expands the attack surface and creates a liability for the organization and its members.

**Context:** You are designing or operating a system that processes personal data to provide a service or create value. The data is essential for functionality, but every piece of data collected introduces privacy and security risks. You need to balance data utility with the principles of privacy and data protection.

### 2. Core Principles

**Collect only the data that is strictly necessary for the specific, defined purpose.** Implement a "default to no" policy for data collection. For every piece of data requested, there must be a clear and documented justification tied to a specific system function or user benefit.

This involves:
- **Purpose Limitation**: Clearly define and document the purpose for which data is collected.
- **Data Auditing**: Regularly review collected data and delete anything that is no longer necessary.
- **Just-in-Time Collection**: Collect data only when it is needed, not in advance.
- **Anonymization/Pseudonymization**: Where possible, use anonymized or pseudonymized data instead of personal data.

### 3. Rationale

By minimizing data collection, you reduce the system's privacy footprint. This:
- **Reduces Risk**: Less data means less risk of data breaches and misuse.
- **Builds Trust**: Demonstrates respect for user privacy, building trust with members.
- **Lowers Costs**: Reduces storage and data management costs.
- **Simplifies Compliance**: Eases compliance with data protection regulations like GDPR.

### 4. Consequences

- **Positive**:
  - Increased user trust and confidence.
  - Reduced security and privacy risks.
  - Lower data management costs.
  - Simplified regulatory compliance.
- **Negative**:
  - May limit the potential for future, unforeseen uses of data.
  - Requires more disciplined design and development processes.
  - Can be challenging to implement in legacy systems.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Signal**: The messaging app only stores the user's phone number and the date they last logged in.
- **Apple**: Apple's privacy-focused features, such as on-device processing and differential privacy, are examples of data minimization in practice.
- **DuckDuckGo**: The search engine does not store personal information or search history.

