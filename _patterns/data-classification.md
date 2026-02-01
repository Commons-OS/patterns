---
id: pat_784a1d1ab2674e72affb3f86
page_url: https://commons-os.github.io/patterns/data-classification/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/data-classification.md
slug: data-classification
title: Data Classification
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

Data Classification is a pattern for building resilient value creation systems.

**Problem:** Not all data is created equal. Some data is highly sensitive (e.g., financial records, health information), while other data is public (e.g., marketing materials). Treating all data with the same level of security is both inefficient and ineffective. It leads to over-protecting non-sensitive data, which is costly, and under-protecting critical data, which is dangerous.

**Context:** You are operating a value creation system that handles a variety of data with different levels of sensitivity and criticality. You need a systematic way to apply the appropriate level of security and privacy controls based on the nature of the data itself.

### 2. Core Principles

**Establish and enforce a data classification policy that categorizes data into different levels based on its sensitivity, criticality, and any legal or regulatory requirements.** This policy provides the foundation for applying risk-based controls.

A typical classification scheme might include:
- **Public**: Data that is freely available to the public. Its disclosure would cause no harm.
- **Internal**: Data that is for internal use by employees and authorized partners. Its unauthorized disclosure could cause minor harm.
- **Confidential**: Sensitive data that is intended for a limited audience. Its unauthorized disclosure could cause significant harm to the organization or its customers.
- **Restricted / Secret**: The most critical data, such as trade secrets, government classified information, or highly sensitive personal data. Its unauthorized disclosure could cause catastrophic harm.

Once the policy is defined, you must:
1.  **Discover and Classify**: Scan your systems to discover where sensitive data resides and apply the appropriate classification label (tag).
2.  **Enforce Controls**: Implement security controls based on the data's classification. For example, Restricted data might require encryption, strict access controls, and detailed logging, while Public data may require none of these.

### 3. Rationale

Data classification allows you to focus your security efforts where they are needed most. It:
- **Enables Risk-Based Security**: Allows you to apply security controls that are commensurate with the risk associated with the data.
- **Improves Efficiency**: Avoids the cost and complexity of applying the highest level of security to all data.
- **Enhances Compliance**: Helps demonstrate to regulators that you have a systematic approach to protecting sensitive data.
- **Informs Other Patterns**: It is a prerequisite for many other patterns, such as Data Retention (P007) and Data Sovereignty by Design (S061).

### 4. Consequences

- **Positive**:
    - A more efficient, effective, and risk-based security posture.
    - Clear guidance for employees on how to handle different types of data.
    - Simplified compliance and auditing.
- **Negative**:
    - Can be a major undertaking to discover and classify all data in a large, complex organization.
    - Requires ongoing effort to keep the classification up to date as new data is created.
    - Can be challenging to automate and enforce consistently across all systems.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Government Security**: Governments have long used classification systems (e.g., Top Secret, Secret, Confidential) to protect national security information.
- **Data Loss Prevention (DLP) Systems**: DLP tools use data classification to identify sensitive data and prevent it from being exfiltrated from the network.
- **Cloud Provider Tools**: Cloud providers offer tools like AWS Macie and Azure Information Protection to automatically discover, classify, and protect sensitive data.

