_# Pattern: Access Control

## 1. Pattern Name and Number

**P006: Access Control**

## 2. Problem

In any multi-user system, different users have different roles, responsibilities, and needs for accessing data. Granting universal access to all data for all users is a massive security and privacy risk. It allows unauthorized individuals to view, modify, or delete sensitive information, leading to data breaches, fraud, and operational chaos.

## 3. Context

You are designing a value creation system where multiple users or systems need to interact with a shared set of data and functions. You need a mechanism to ensure that users can only access the specific information and perform the specific actions that are necessary for their legitimate tasks.

## 4. Solution

**Implement a robust access control system that enforces policies over who can do what with which resources.** This involves authenticating the identity of a user (see S036: Multi-Factor Authentication) and then authorizing them based on a set of rules.

Common access control models include:
- **Role-Based Access Control (RBAC)**: Access rights are grouped by role (e.g., "administrator," "editor," "viewer"), and users are assigned to roles. This is the most common model for modern systems.
- **Attribute-Based Access Control (ABAC)**: Access is granted based on policies that combine attributes of the user (e.g., department, clearance), the resource (e.g., data classification), and the environment (e.g., time of day, location).
- **Discretionary Access Control (DAC)**: The owner of a resource can decide who gets to access it.
- **Mandatory Access Control (MAC)**: Access is determined by a central authority based on a security classification system.

## 5. Rationale

Access control is a fundamental pillar of security and privacy. It:
- **Enforces Least Privilege**: It is the primary mechanism for implementing the Principle of Least Privilege (S033), ensuring users only have the access they need.
- **Protects Confidentiality and Integrity**: Prevents unauthorized disclosure or modification of data.
- **Provides Accountability**: Creates a clear audit trail of who accessed what data and when.
- **Enables Segregation of Duties**: Prevents a single user from having enough power to commit fraud or cause catastrophic damage.

## 6. Consequences

- **Positive**:
    - Drastically reduces the risk of both internal and external data breaches.
    - Provides a clear and auditable record of data access.
    - Essential for compliance with almost all security and privacy regulations.
- **Negative**:
    - Can be complex to design, implement, and manage, especially in large organizations.
    - If poorly designed, it can create significant friction for users and hinder productivity.
    - Requires ongoing maintenance to keep roles and permissions up to date.

## 7. Known Uses

- **File Systems**: Operating systems use access control lists (ACLs) to determine which users can read, write, or execute files.
- **Databases**: Database management systems use granular controls to manage access to specific tables, columns, and rows.
- **Cloud IAM**: All cloud platforms have sophisticated Identity and Access Management (IAM) systems to control access to cloud resources.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of creating well-governed and secure systems.                                  |
| **2. Governance**       | 5           | The very definition of data and system governance.                                                    |
| **3. Economy**          | 4           | Prevents economic loss from internal fraud and external breaches.                                     |
| **4. Technology**       | 5           | A fundamental technological component of any secure, multi-user system.                               |
| **5. Operations**       | 4           | Requires disciplined operational processes for managing roles, permissions, and access requests.      |
| **6. Culture**          | 4           | Fosters a culture of responsibility and awareness around data access.                                 |
| **7. Resilience**       | 5           | Builds resilience by containing the impact of a compromised account to its authorized scope.          |
| **Overall Score**       | **4.4**     | A foundational and non-negotiable pattern for any system with more than one user.                    |
