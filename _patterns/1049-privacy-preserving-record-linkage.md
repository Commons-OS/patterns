---
id: pat_e7bd862442ad4e88949fae20
page_url: https://commons-os.github.io/patterns/1049-privacy-preserving-record-linkage/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/1049-privacy-preserving-record-linkage.md
slug: 1049-privacy-preserving-record-linkage
title: Privacy-Preserving Record Linkage
aliases: []
version: 1.0
created: 2026-02-01T12:17:06Z
modified: 2026-02-01T12:17:06Z
tags:
  universality: universal
  domain: privacy
  category: [pattern]
  era: [cognitive]
  origin: [commons-os]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [manus-ai, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

Privacy-Preserving Record Linkage is a pattern for building resilient value creation systems.

**Problem:** Two or more parties have datasets that contain information about the same individuals, but they cannot share the data with each other due to privacy regulations or commercial sensitivities. They need to link the records for the same individual across their datasets to perform a joint analysis, but they need to do so without revealing the identities of the individuals in their datasets.

**Context:** You are working with one or more other organizations to perform a data analysis project. You need to link your datasets together, but you are not allowed to share the raw data. For example, a hospital and a university may want to link patient health records with student academic records to study the impact of health on academic performance.

### 2. Core Principles

**Use Privacy-Preserving Record Linkage (PPRL), a set of techniques that allows two or more parties to identify records that correspond to the same individual in their respective datasets, without revealing any personally identifiable information (PII).**

A common approach is to use **cryptographic hashing**. The parties agree on a common set of identifiers (like name, date of birth, address) and a common cryptographic hash function. Each party then hashes the identifiers for each of their records and sends the resulting hashes to a trusted third party or to each other. The parties can then identify the matching records by comparing the hashes.

More advanced techniques use **Bloom filters** or **Secure Multi-Party Computation (P019)** to perform the linkage without a trusted third party and with even stronger privacy guarantees.

### 3. Rationale

PPRL enables valuable data linkage projects that would otherwise be impossible. It:
- **Protects Privacy**: Allows for data linkage without sharing PII.
- **Enables Collaboration**: Allows different organizations to collaborate on data analysis projects.
- **Unlocks New Insights**: Can lead to new and important insights that can only be gained by linking different datasets.

### 4. Consequences

- **Positive**:
    - The ability to perform data linkage in a privacy-preserving way.
    - A powerful enabler of collaborative research and data analysis.
- **Negative**:
    - **Accuracy**: There is often a trade-off between the accuracy of the linkage and the strength of the privacy guarantee. Some techniques can produce false positives (linking records that are not for the same person) or false negatives (failing to link records that are for the same person).
    - **Complexity**: These are advanced techniques that require specialized expertise.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Medical Research**: Used extensively to link patient records from different hospitals and research institutions.
- **Government**: Used by government agencies to link administrative datasets for statistical purposes.

