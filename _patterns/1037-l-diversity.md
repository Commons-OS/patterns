---
id: pat_e38e0a256bf148a9aeb22616
page_url: https://commons-os.github.io/patterns/1037-l-diversity/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/1037-l-diversity.md
slug: 1037-l-diversity
title: L-Diversity
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

L-Diversity is a pattern for building resilient value creation systems.

**Problem:** K-Anonymity (P017) protects against re-identification by ensuring that each individual is part of a group of at least 'k' indistinguishable records. However, it is vulnerable to homogeneity attacks. If all 'k' individuals in a group share the same sensitive attribute (e.g., they all have the same disease), an attacker who knows that a person is in that group can infer their sensitive information, even without knowing their exact record.

**Context:** You have already applied K-Anonymity to a dataset, but you recognize that it is not sufficient to protect against attribute disclosure when the sensitive values within an equivalence class (a group of k-indistinguishable records) are not diverse.

### 2. Core Principles

**Apply L-Diversity, an extension of K-Anonymity that requires each equivalence class to have at least 'l' well-represented values for the sensitive attribute.** This ensures that even if an attacker can identify the equivalence class for an individual, they cannot infer the sensitive value with high confidence.

There are several interpretations of "well-represented":
- **Distinct L-Diversity**: Ensures there are at least 'l' distinct values for the sensitive attribute in each equivalence class.
- **Entropy L-Diversity**: Ensures that the distribution of sensitive values in each equivalence class has a certain amount of entropy, preventing one value from dominating.

Like K-Anonymity, L-Diversity is achieved through generalization and suppression of the quasi-identifiers.

### 3. Rationale

L-Diversity directly addresses the weaknesses of K-Anonymity. It:
- **Protects Against Homogeneity Attacks**: Prevents the inference of sensitive attributes by ensuring diversity within each equivalence class.
- **Provides a Stronger Privacy Guarantee**: Reduces the probability of correctly guessing an individual's sensitive attribute.
- **Builds on K-Anonymity**: It is a natural and necessary extension for any dataset where attribute disclosure is a concern.

### 4. Consequences

- **Positive**:
    - Provides a stronger privacy guarantee than K-Anonymity alone.
    - Protects against attribute disclosure attacks.
- **Negative**:
    - It is more difficult and costly to achieve than K-Anonymity, often requiring more data generalization or suppression, which further reduces data utility.
    - It is still vulnerable to some attacks, such as skewness attacks (if some sensitive values are much more common than others) and similarity attacks (if all the sensitive values in a group are semantically similar).
    - Can be complex to implement.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Healthcare Data Release**: Used in conjunction with K-Anonymity to protect patient privacy in datasets released for research.
- **Data Anonymization Tools**: Advanced data anonymization tools often provide options to enforce L-Diversity alongside K-Anonymity.

