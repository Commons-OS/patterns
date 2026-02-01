_# Pattern: Principle of Least Privilege

## 1. Pattern Name and Number

**S033: Principle of Least Privilege (PoLP)**

## 2. Problem

Granting users, applications, or systems excessive permissions beyond what is necessary for their function creates a significant security risk. If a privileged account is compromised, an attacker can gain broad access to sensitive data and critical systems, leading to catastrophic damage.

## 3. Context

You are designing the access control model for a value creation system. You need to define permissions for various actors (human users, service accounts, APIs) to ensure they can perform their legitimate tasks without having unnecessary or dangerous levels of access.

## 4. Solution

**Grant every module (user, process, program) the minimum privileges necessary to perform its function and no more.** This principle should be applied across all layers of the system.

Implementation involves:
- **Role-Based Access Control (RBAC)**: Define roles with specific sets of permissions and assign users to those roles.
- **Just-in-Time (JIT) Access**: Grant temporary, elevated privileges only when needed for a specific task and for a limited duration.
- **Fine-Grained Permissions**: Break down permissions into the smallest possible units to avoid granting broad access.
- **Regular Audits**: Periodically review user and system permissions to ensure they are still necessary and appropriate.
- **Separation of Duties**: Divide critical tasks among multiple users to prevent any single individual from having too much power.

## 5. Rationale

The Principle of Least Privilege is a cornerstone of modern security architecture. It:
- **Reduces Attack Surface**: Limits the potential damage that can be done if an account is compromised.
- **Prevents Lateral Movement**: Restricts an attacker's ability to move from a compromised, low-privilege system to more critical ones.
- **Minimizes Errors**: Reduces the likelihood of accidental misuse or misconfiguration by limiting what users and systems can do.
- **Improves Auditability**: Simplifies auditing and compliance by clearly defining who has access to what.

## 6. Consequences

- **Positive**:
    - Significantly reduces the risk and impact of security breaches.
    - Enhances system stability by preventing unintended changes.
    - Simplifies compliance with regulations that mandate access controls.
- **Negative**:
    - Can be complex to design and manage, especially in large, dynamic systems.
    - May create friction for users if they are constantly requesting access for legitimate tasks.
    - Requires careful planning to avoid hindering productivity.

## 7. Known Uses

- **Operating Systems**: Modern operating systems like Linux, Windows, and macOS use PoLP to separate user processes from the kernel and from each other.
- **Database Management Systems**: Granting users specific permissions (SELECT, INSERT, UPDATE, DELETE) on specific tables rather than full database access.
- **Cloud IAM (Identity and Access Management)**: Cloud providers like AWS, Azure, and GCP have sophisticated IAM systems built on the principle of least privilege.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of creating secure and well-governed systems.                                  |
| **2. Governance**       | 5           | A fundamental principle of access governance and risk management.                                     |
| **3. Economy**          | 4           | Reduces the economic impact of security incidents.                                                    |
| **4. Technology**       | 5           | A core concept in the design of secure technological systems and access control mechanisms.           |
| **5. Operations**       | 4           | Requires disciplined operational processes for managing permissions and access requests.              |
| **6. Culture**          | 4           | Fosters a culture of security awareness and responsibility.                                           |
| **7. Resilience**       | 5           | Directly enhances system resilience by containing the blast radius of security failures.              |
| **Overall Score**       | **4.4**     | A non-negotiable, foundational security pattern for any system involving multiple users or components. |
