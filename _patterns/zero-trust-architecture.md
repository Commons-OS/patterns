---
id: pat_d2eb9d9c377a4469b89e3cc0
page_url: https://commons-os.github.io/patterns/zero-trust-architecture/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/zero-trust-architecture.md
slug: zero-trust-architecture
title: Zero Trust Architecture
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

Zero Trust Architecture is a pattern for building resilient value creation systems.

**Problem:** Traditional security models based on a trusted internal network and an untrusted external network are no longer effective. With the rise of remote work, cloud services, and sophisticated cyber-attacks, the network perimeter has dissolved, and assuming trust based on network location is a major security risk.

**Context:** You are designing or operating a value creation system with distributed users, devices, and resources. You need to provide secure access to resources regardless of their location, while protecting against both external and internal threats.

### 2. Core Principles

**Adopt a "never trust, always verify" approach to security.** A Zero Trust Architecture (ZTA) treats all network traffic as untrusted and requires strict identity verification for every person and device trying to access resources on a private network.

This involves:
- **Identity-Centric Security**: Security is centered around user and device identity, not network location.
- **Least Privilege Access**: Users and devices are granted the minimum level of access needed to perform their tasks.
- **Microsegmentation**: The network is broken down into small, isolated zones to limit the lateral movement of attackers.
- **Continuous Verification**: Authentication and authorization are re-evaluated continuously throughout a session.

### 3. Rationale

ZTA fundamentally changes the security paradigm from a location-centric to an identity-centric approach. This:
- **Reduces Attack Surface**: Eliminates the concept of a trusted internal network, reducing the attack surface.
- **Prevents Lateral Movement**: Microsegmentation contains breaches and prevents attackers from moving freely within the network.
- **Improves Visibility**: Continuous verification provides greater visibility into network traffic and user activity.
- **Enables Secure Remote Access**: Provides a secure way to access resources from any location.

### 4. Consequences

- **Positive**:
  - Significantly improved security posture.
  - Better protection against both external and internal threats.
  - Enables secure adoption of cloud and mobile technologies.
  - Increased visibility and control over network traffic.
- **Negative**:
  - Can be complex and costly to implement.
  - May introduce latency if not designed properly.
  - Requires a significant cultural shift in how security is perceived.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Google BeyondCorp**: Google's implementation of a zero-trust security model.
- **NIST SP 800-207**: The National Institute of Standards and Technology's framework for Zero Trust Architecture.
- **Microsoft Zero Trust**: Microsoft's framework and solutions for implementing zero trust.

