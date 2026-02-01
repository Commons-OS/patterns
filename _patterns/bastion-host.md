---
id: pat_468f73ebe0fa4c65bae22dfa
page_url: https://commons-os.github.io/patterns/bastion-host/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/bastion-host.md
slug: bastion-host
title: Bastion Host
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

Bastion Host is a pattern for building resilient value creation systems.

**Problem:** To manage servers and other infrastructure in a private network, administrators need a way to connect to them from the outside world (e.g., from their corporate network or the internet). Exposing management ports like SSH or RDP directly to the internet for every server is extremely risky, as it creates a massive attack surface and makes the servers vulnerable to brute-force attacks and exploits.

**Context:** You have a private network (e.g., a VPC in the cloud) containing infrastructure that needs to be managed remotely. You need to provide secure administrative access to this infrastructure without exposing it directly to untrusted networks.

### 2. Core Principles

**Establish a Bastion Host (also known as a Jump Box or Jump Server), a single, hardened, and highly monitored server that acts as the sole entry point for administrative access to a private network.** Administrators first connect to the bastion host, and from there, they can "jump" to the other servers in the private network.

Key characteristics of a bastion host:
- **Hardened**: The bastion host itself should be stripped of all non-essential software and services and configured with the highest level of security.
- **Highly Monitored**: All activity on the bastion host should be extensively logged and monitored for any suspicious behavior (see S039: Security Logging).
- **Strict Access Control**: Access to the bastion host should be tightly controlled, using Multi-Factor Authentication (S036) and allowing connections only from specific, trusted IP addresses.
- **No Sensitive Data**: The bastion host should not store any sensitive data.

### 3. Rationale

A bastion host acts as a secure "choke point" for administrative traffic. It:
- **Reduces Attack Surface**: Instead of exposing every server to the internet, you only expose a single, hardened point of entry.
- **Centralizes Auditing and Control**: All administrative access goes through a single point, making it much easier to monitor and control.
- **Improves Security Posture**: Provides a simple and effective way to isolate your private network from the public internet.

### 4. Consequences

- **Positive**:
    - A dramatic reduction in the attack surface of your private network.
    - Centralized logging and auditing of all administrative access.
    - A simple and effective way to enforce strong authentication for administrative users.
- **Negative**:
    - The bastion host itself becomes a high-value target for attackers and a single point of failure for administrative access. It must be protected accordingly.
    - Can introduce an extra step for administrators, which can be a minor inconvenience.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Cloud Infrastructure**: Bastion hosts are a standard and recommended pattern for securely managing instances in a private VPC in AWS, Azure, and Google Cloud.
- **Corporate Networks**: Used to provide secure access for remote administrators or third-party vendors who need to manage internal systems.

