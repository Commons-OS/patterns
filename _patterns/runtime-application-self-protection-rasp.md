---
id: pat_c419f1ecbb9b4610ad69c175
page_url: https://commons-os.github.io/patterns/runtime-application-self-protection-rasp/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/runtime-application-self-protection-rasp.md
slug: runtime-application-self-protection-rasp
title: Runtime Application Self-Protection (RASP)
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
classification:
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
  commons_domain:
  - business
  - security
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

Runtime Application Self-Protection (RASP) is a pattern for building resilient value creation systems.

**Problem:** Traditional network and host-based security controls, like Web Application Firewalls (WAFs), have a limited understanding of the application they are protecting. They sit outside the application and try to identify attacks by inspecting network traffic. This makes them prone to false positives and false negatives, and they can be bypassed by sophisticated attackers. They don't have the context to understand what is a legitimate or a malicious action from the application's point of view.

**Context:** You are running a web application and need a more accurate and effective way to protect it from attacks in real-time. You need a security control that has deep visibility into the application's internal workings and can respond immediately to threats.

### 2. Core Principles

**Implement Runtime Application Self-Protection (RASP), a security technology that is built or linked into an application or application runtime, and is capable of controlling application execution and detecting and preventing real-time attacks.**

RASP works by instrumenting the application from the inside. It has full context of the application's code, data flow, and configuration. This allows it to identify and block attacks with much greater accuracy than a WAF.

RASP can be deployed in two modes:
- **Monitoring Mode**: It detects and logs attacks but does not block them.
- **Blocking Mode**: It actively blocks attacks as they happen.

### 3. Rationale

RASP provides a more modern and effective approach to application security. It:
- **Is Highly Accurate**: Because it has full application context, it can detect attacks with very few false positives.
- **Provides Real-Time Protection**: It can block attacks in real-time, before they can do any damage.
- **Is Easy to Deploy**: It is typically deployed as a simple library or agent that is added to the application, with no need for network re-architecture.

### 4. Consequences

- **Positive**:
    - A significant improvement in the accuracy and effectiveness of application security.
    - Real-time protection against a wide range of attacks.
- **Negative**:
    - **Performance Overhead**: It can add a small performance overhead to the application.
    - **Complexity**: It adds another component to the application stack that needs to be managed.
    - **Language Support**: RASP solutions are typically language-specific and may not be available for all programming languages.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **OWASP**: The Open Web Application Security Project has a lot of information on RASP.
- **Many commercial vendors** (like Imperva, Signal Sciences, and Contrast Security) offer RASP solutions.

