---
id: pat_235f26a8b437483788a5b45c
page_url: https://commons-os.github.io/patterns/defense-in-depth/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/defense-in-depth.md
slug: defense-in-depth
title: Defense in Depth
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
tags:
  universality: universal
  domain: security
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

Defense in Depth is a pattern for building resilient value creation systems.

**Problem:** Relying on a single security control, such as a perimeter firewall, creates a single point of failure. If that one control is breached, the entire system is exposed, and attackers can move freely to access sensitive resources.

**Context:** You are designing the security architecture for a value creation system. You must assume that any single security control can and will eventually fail. You need a strategy that provides resilience against security failures and slows down attackers.

### 2. Core Principles

**Implement multiple, layered, and redundant security controls throughout the system.** The goal is to create a series of defensive barriers, so that if one layer fails, another is in place to thwart an attack. This approach is often compared to the layered defenses of a medieval castle.

Layers can include:
- **Physical Security**: Controls access to physical hardware.
- **Network Security**: Firewalls, Intrusion Detection/Prevention Systems (IDS/IPS), and network segmentation.
- **Host Security**: Hardening operating systems, endpoint protection, and anti-malware.
- **Application Security**: Secure coding practices, input validation, and Web Application Firewalls (WAFs).
- **Data Security**: Encryption at rest and in transit, data loss prevention (DLP), and access controls.
- **Identity and Access Management**: Strong authentication, MFA, and least privilege.
- **Monitoring and Response**: Security logging, SIEM, and a defined incident response plan.

### 3. Rationale

Defense in Depth creates a more resilient and robust security posture. It:
- **Eliminates Single Points of Failure**: A breach of one layer does not compromise the entire system.
- **Slows Down Attackers**: Forces attackers to bypass multiple controls, giving security teams more time to detect and respond.
- **Provides Redundancy**: If one control is misconfigured or fails, others can still provide protection.
- **Addresses a Wide Range of Threats**: Different layers are effective against different types of attacks.

### 4. Consequences

- **Positive**:
    - Significantly increased security resilience.
    - Better protection against sophisticated, multi-stage attacks.
    - Provides compensatory controls for weaknesses in other layers.
- **Negative**:
    - Can increase complexity and management overhead.
    - Can be more costly to implement due to the need for multiple security tools.
    - Requires careful planning to ensure layers are complementary and not redundant in a way that adds no value.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **PCI DSS (Payment Card Industry Data Security Standard)**: The standard requires multiple layers of security controls to protect cardholder data.
- **NIST Cybersecurity Framework**: The framework's "Protect" function emphasizes a layered security approach.
- **Military Strategy**: The concept originates from military strategy, where multiple lines of defense are used to protect a target.

