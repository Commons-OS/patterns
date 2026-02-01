---
id: pat_fbfd5708ff3a48a889b99389
page_url: https://commons-os.github.io/patterns/access-control/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/access-control.md
slug: access-control
title: Access Control
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

Access Control is a pattern for building resilient value creation systems.

**Problem:** In any multi-user system, different users have different roles, responsibilities, and needs for accessing data. Granting universal access to all data for all users is a massive security and privacy risk. It allows unauthorized individuals to view, modify, or delete sensitive information, leading to data breaches, fraud, and operational chaos.

**Context:** You are designing a value creation system where multiple users or systems need to interact with a shared set of data and functions. You need a mechanism to ensure that users can only access the specific information and perform the specific actions that are necessary for their legitimate tasks.

### 2. Core Principles

**Implement a robust access control system that enforces policies over who can do what with which resources.** This involves authenticating the identity of a user (see S036: Multi-Factor Authentication) and then authorizing them based on a set of rules.

Common access control models include:
- **Role-Based Access Control (RBAC)**: Access rights are grouped by role (e.g., "administrator," "editor," "viewer"), and users are assigned to roles. This is the most common model for modern systems.
- **Attribute-Based Access Control (ABAC)**: Access is granted based on policies that combine attributes of the user (e.g., department, clearance), the resource (e.g., data classification), and the environment (e.g., time of day, location).
- **Discretionary Access Control (DAC)**: The owner of a resource can decide who gets to access it.
- **Mandatory Access Control (MAC)**: Access is determined by a central authority based on a security classification system.

### 3. Rationale

Access control is a fundamental pillar of security and privacy. It:
- **Enforces Least Privilege**: It is the primary mechanism for implementing the Principle of Least Privilege (S033), ensuring users only have the access they need.
- **Protects Confidentiality and Integrity**: Prevents unauthorized disclosure or modification of data.
- **Provides Accountability**: Creates a clear audit trail of who accessed what data and when.
- **Enables Segregation of Duties**: Prevents a single user from having enough power to commit fraud or cause catastrophic damage.

### 4. Consequences

- **Positive**:
    - Drastically reduces the risk of both internal and external data breaches.
    - Provides a clear and auditable record of data access.
    - Essential for compliance with almost all security and privacy regulations.
- **Negative**:
    - Can be complex to design, implement, and manage, especially in large organizations.
    - If poorly designed, it can create significant friction for users and hinder productivity.
    - Requires ongoing maintenance to keep roles and permissions up to date.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **File Systems**: Operating systems use access control lists (ACLs) to determine which users can read, write, or execute files.
- **Databases**: Database management systems use granular controls to manage access to specific tables, columns, and rows.
- **Cloud IAM**: All cloud platforms have sophisticated Identity and Access Management (IAM) systems to control access to cloud resources.

