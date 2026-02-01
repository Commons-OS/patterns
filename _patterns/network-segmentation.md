---
id: pat_a93f34b7d2774335978d9b56
page_url: https://commons-os.github.io/patterns/network-segmentation/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/network-segmentation.md
slug: network-segmentation
title: Network Segmentation
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

Network Segmentation is a pattern for building resilient value creation systems.

**Problem:** A flat network, where all systems can communicate freely with each other, is a security nightmare. If a single, non-critical system is compromised (e.g., a development web server), an attacker can easily move laterally across the network to attack more critical systems, such as databases containing sensitive customer data. The entire network becomes a single, large attack surface.

**Context:** You are designing the network architecture for a value creation system that consists of multiple components with different levels of sensitivity and trust. You need to control the flow of traffic between these components to contain breaches and limit an attacker's ability to move laterally.

### 2. Core Principles

**Divide the network into smaller, isolated segments (or zones) and enforce strict access controls on all traffic flowing between them.** The goal is to create a "zero trust" network where communication is denied by default and only explicitly allowed if there is a legitimate business need.

Common segmentation strategies:
- **Perimeter Firewalls**: The traditional approach of creating a "trusted" internal network and an "untrusted" external network. This is no longer sufficient on its own.
- **VLANs (Virtual LANs)**: Segmenting the network at Layer 2 (the data link layer) to create broadcast domains.
- **Subnetting**: Segmenting the network at Layer 3 (the network layer) using IP address ranges.
- **Microsegmentation**: A modern, granular approach where security policies are applied to individual workloads (e.g., virtual machines, containers). This allows you to create a secure perimeter around every single application, effectively treating each one as its own isolated segment.

### 3. Rationale

Network segmentation is a core principle of a Defense in Depth (S032) strategy. It:
- **Contains Breaches**: Limits the "blast radius" of a security incident. If one segment is compromised, the others remain protected.
- **Reduces Attack Surface**: An attacker can only see and attack the systems within the segment they have compromised.
- **Improves Performance**: Can reduce network congestion by isolating traffic within a segment.
- **Enhances Monitoring**: Makes it easier to monitor traffic for suspicious activity as it crosses segment boundaries.

### 4. Consequences

- **Positive**:
    - Significantly improved security posture and resilience against lateral movement.
    - Better containment of security incidents.
    - Improved visibility and control over network traffic.
- **Negative**:
    - Can be complex to design and manage, especially in large and dynamic environments.
    - Requires careful planning of firewall rules and access control lists, which can be prone to error.
    - Microsegmentation, while powerful, requires sophisticated tools and a mature operations team.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **PCI DSS**: The Payment Card Industry Data Security Standard requires strict network segmentation to isolate the Cardholder Data Environment (CDE) from the rest of the network.
- **Zero Trust Architecture**: Network segmentation is a foundational component of a Zero Trust security model (see S031).
- **Cloud VPCs (Virtual Private Clouds)**: Cloud providers allow users to create logically isolated sections of their cloud where they can launch resources in a virtual network that they define.

