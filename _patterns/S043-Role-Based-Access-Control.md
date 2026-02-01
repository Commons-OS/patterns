_# Pattern: Role-Based Access Control (RBAC)

## 1. Pattern Name and Number

**S043: Role-Based Access Control (RBAC)**

## 2. Problem

Managing permissions for a large number of individual users is complex, error-prone, and does not scale. Granting permissions directly to users makes it difficult to have a clear overview of who has access to what, to enforce the principle of least privilege, and to update permissions when a user's job function changes. This often leads to users accumulating excessive permissions over time.

## 3. Context

You are designing an authorization system for an application or infrastructure with multiple users and a variety of resources. You need a scalable and manageable way to control who can access which resources and perform which actions.

## 4. Solution

**Implement Role-Based Access Control (RBAC), an access control model where permissions are assigned to roles, and users are then assigned to roles.** Instead of managing individual user permissions, you manage a smaller and more stable set of roles.

The model consists of three main components:
1.  **Permissions**: The ability to perform a specific action on a specific resource (e.g., "read" access to "file_X", "write" access to "database_Y").
2.  **Roles**: A collection of permissions that represents a specific job function or level of authority (e.g., "database_administrator", "marketing_analyst", "read_only_viewer").
3.  **Users**: Individuals who are assigned one or more roles.

A user's effective permissions are the sum of all permissions granted to all the roles they are assigned.

## 5. Rationale

RBAC provides a more structured and scalable approach to authorization. It:
- **Simplifies Administration**: Administrators manage a small number of roles instead of a large number of individual user permissions.
- **Enforces Least Privilege**: Roles can be designed to grant only the permissions necessary for a specific job function.
- **Improves Auditing**: It is much easier to review and audit role definitions and assignments than to audit the permissions of every single user.
- **Scales with the Organization**: When a new user joins, you simply assign them the appropriate role. When a user changes jobs, you just change their role assignment.

## 6. Consequences

- **Positive**:
    - A dramatic simplification of permission management.
    - A more secure and auditable authorization system.
    - A model that scales effectively as the number of users and resources grows.
- **Negative**:
    - Can be inflexible for very fine-grained access control needs, which might require a more attribute-based model (ABAC).
    - Requires a careful and well-planned design of the roles to be effective. Poorly designed roles can lead to "role explosion" or roles with excessive permissions.

## 7. Known Uses

- **Kubernetes**: Has a built-in RBAC API for controlling access to the Kubernetes API.
- **Cloud Platforms**: AWS IAM, Azure RBAC, and Google Cloud IAM all use RBAC as their primary authorization model.
- **Databases**: Most modern databases provide RBAC features for managing access to data.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of building secure and well-governed systems.                                  |
| **2. Governance**       | 5           | A fundamental pattern for scalable and auditable access governance.                                   |
| **3. Economy**          | 4           | Reduces the economic cost of security administration and compliance.                                  |
| **4. Technology**       | 5           | A standard, mature, and widely implemented authorization technology.                                  |
| **5. Operations**       | 4           | Simplifies security operations for user lifecycle management.                                         |
| **6. Culture**          | 4           | Fosters a culture of structured and intentional access management.                                    |
| **7. Resilience**       | 4           | Builds resilience by making it easier to enforce least privilege and prevent unauthorized access.     |
| **Overall Score**       | **4.3**     | A foundational and essential pattern for authorization in almost any non-trivial system.             |
