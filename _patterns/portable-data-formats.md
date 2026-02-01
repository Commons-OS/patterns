---
id: pat_f41e36e732ae4dfe93ff1aa4
page_url: https://commons-os.github.io/patterns/portable-data-formats/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/portable-data-formats.md
slug: portable-data-formats
title: Portable Data Formats
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
tags:
  universality: universal
  domain: sovereignty
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

Portable Data Formats is a pattern for building resilient value creation systems.

**Problem:** Data is often stored in proprietary, vendor-specific formats. When you want to move your data to a different application or service, you have to go through a complex, costly, and often lossy data conversion process. This creates vendor lock-in and makes it difficult to use your own data with the tools of your choice. Your data is trapped.

**Context:** You are designing a system that creates, stores, or processes data. You want to ensure that this data can be easily moved, shared, and used by other systems in the future, maximizing its value and ensuring your own freedom of choice.

### 2. Core Principles

**Adopt a policy of using Portable Data Formats, which are open, standardized, and widely supported, for all data storage and exchange.** Instead of using a proprietary binary format or a vendor-specific database schema, use formats like:

- **JSON (JavaScript Object Notation)**: For structured data.
- **CSV (Comma-Separated Values)**: For tabular data.
- **Parquet or ORC**: For columnar, analytical data.
- **XML (eXtensible Markup Language)**: For semi-structured data.
- **PDF/A**: For long-term archival of documents.

This principle should apply not just to data exports, but to the primary way data is stored and managed within the system whenever possible.

### 3. Rationale

Using portable data formats is a simple but powerful way to prevent data lock-in. It:
- **Ensures Interoperability**: Data can be easily read and understood by a wide range of different tools and applications.
- **Maximizes Data Value**: Allows data to be easily combined, analyzed, and used in new and innovative ways.
- **Future-Proofs Your Data**: Ensures that your data will remain accessible and usable for years to come, even as technologies change.
- **Supports Data Portability**: It is a technical prerequisite for implementing a Data Portability (P013) feature.

### 4. Consequences

- **Positive**:
    - Freedom from data lock-in.
    - Increased interoperability and data value.
    - A more resilient and future-proof data architecture.
- **Negative**:
    - **Performance**: Open formats may not always be as performant as highly optimized, proprietary binary formats for very specific use cases.
    - **Feature Support**: A proprietary format may have specific features that are not available in any open standard.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **The entire modern web and API economy** is built on open data formats like JSON.
- **Data Warehousing and Big Data**: Columnar formats like Parquet and ORC are the industry standard for efficient analytical queries.
- **Government Open Data Initiatives**: Mandate the use of open, machine-readable formats for all published public data.

