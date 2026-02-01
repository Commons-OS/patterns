---
id: pat_7721db0de1ba4208accd59e8
page_url: https://commons-os.github.io/patterns/privacy-by-default/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/privacy-by-default.md
slug: privacy-by-default
title: Privacy by Default
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
tags:
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

Privacy by Default is a pattern for building resilient value creation systems.

**Problem:** Many applications and services are configured with permissive, data-sharing settings out of the box. Users are expected to navigate complex settings menus to restrict the collection and sharing of their data. Most users never change the default settings, which means their data is often collected and used in ways they do not expect or want. The burden of privacy protection is placed on the user.

**Context:** You are designing a system, application, or service that processes personal data. You want to ensure that you are respecting user privacy from the very beginning and building a system that is trustworthy by design.

### 2. Core Principles

**Implement the principle of Privacy by Default, which means that the most privacy-protective settings are the default settings.** The system should be configured to collect only the minimum amount of personal data necessary for the service to function, and this data should not be shared or used for other purposes without the user actively choosing to opt-in.

This means:
- **Minimal Data Collection**: Do not collect any personal data that is not essential for the service.
- **No Pre-checked Boxes**: Consent for non-essential data processing or sharing must be an active, opt-in choice, not a pre-checked box.
- **Privacy-Protective Defaults**: Features like location tracking, ad personalization, and public visibility of profiles should be off by default.

### 3. Rationale

Privacy by Default shifts the burden of privacy protection from the user to the service provider. It:
- **Respects Users**: It treats user privacy as a fundamental right, not as a setting to be managed.
- **Builds Trust**: Demonstrates a commitment to privacy that can be a strong competitive differentiator.
- **Ensures Compliance**: It is a core requirement of GDPR (Article 25) and other modern data protection laws.
- **Protects the Majority**: Since most users do not change default settings, it ensures that the majority of users are protected.

### 4. Consequences

- **Positive**:
    - Increased user trust and a stronger brand reputation.
    - Compliance with a key principle of modern data protection law.
    - A more ethical and user-centric product.
- **Negative**:
    - May reduce the amount of data available for analytics and personalization, which could impact business models that rely on extensive data collection.
    - May require more user education to encourage them to opt-in to features that require more data.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **GDPR**: Article 25, "Data protection by design and by default," makes this a legal requirement for any service processing the data of EU citizens.
- **Signal**: The messaging app is a prime example of a service built with privacy by default, with features like end-to-end encryption enabled for all conversations by default.

