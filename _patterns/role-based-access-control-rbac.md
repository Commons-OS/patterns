---
id: pat_7bd8c70bf4d74bb980598eff
page_url: https://commons-os.github.io/patterns/role-based-access-control-rbac/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/role-based-access-control-rbac.md
slug: role-based-access-control-rbac
title: Role-Based Access Control (RBAC)
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

Role-Based Access Control (RBAC) is a pattern for building resilient value creation systems.

**Problem:** Managing permissions for a large number of individual users is complex, error-prone, and does not scale. Granting permissions directly to users makes it difficult to have a clear overview of who has access to what, to enforce the principle of least privilege, and to update permissions when a user's job function changes. This often leads to users accumulating excessive permissions over time.

**Context:** You are designing an authorization system for an application or infrastructure with multiple users and a variety of resources. You need a scalable and manageable way to control who can access which resources and perform which actions.

### 2. Core Principles

**Implement Role-Based Access Control (RBAC), an access control model where permissions are assigned to roles, and users are then assigned to roles.** Instead of managing individual user permissions, you manage a smaller and more stable set of roles.

The model consists of three main components:
1.  **Permissions**: The ability to perform a specific action on a specific resource (e.g., "read" access to "file_X", "write" access to "database_Y").
2.  **Roles**: A collection of permissions that represents a specific job function or level of authority (e.g., "database_administrator", "marketing_analyst", "read_only_viewer").
3.  **Users**: Individuals who are assigned one or more roles.

A user's effective permissions are the sum of all permissions granted to all the roles they are assigned.

### 3. Rationale

RBAC provides a more structured and scalable approach to authorization. It:
- **Simplifies Administration**: Administrators manage a small number of roles instead of a large number of individual user permissions.
- **Enforces Least Privilege**: Roles can be designed to grant only the permissions necessary for a specific job function.
- **Improves Auditing**: It is much easier to review and audit role definitions and assignments than to audit the permissions of every single user.
- **Scales with the Organization**: When a new user joins, you simply assign them the appropriate role. When a user changes jobs, you just change their role assignment.

### 4. Consequences

- **Positive**:
    - A dramatic simplification of permission management.
    - A more secure and auditable authorization system.
    - A model that scales effectively as the number of users and resources grows.
- **Negative**:
    - Can be inflexible for very fine-grained access control needs, which might require a more attribute-based model (ABAC).
    - Requires a careful and well-planned design of the roles to be effective. Poorly designed roles can lead to "role explosion" or roles with excessive permissions.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Kubernetes**: Has a built-in RBAC API for controlling access to the Kubernetes API.
- **Cloud Platforms**: AWS IAM, Azure RBAC, and Google Cloud IAM all use RBAC as their primary authorization model.
- **Databases**: Most modern databases provide RBAC features for managing access to data.

