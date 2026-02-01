_# Pattern: Security as Code

## 1. Pattern Name and Number

**S059: Security as Code**

## 2. Problem

Security policies and configurations are often managed manually, through GUIs, or in documents. This approach is slow, error-prone, and does not scale. It creates a disconnect between the security team and the development team, and it makes it difficult to audit and enforce security policies consistently across a large and dynamic environment.

## 3. Context

You are operating in a modern, automated, and code-driven environment (e.g., using Infrastructure as Code, CI/CD). You need to manage your security policies in a way that is also automated, code-driven, and integrated into the developer workflow.

## 4. Solution

**Adopt the principle of Security as Code, which involves defining and managing your security policies and controls in a machine-readable, version-controlled format.** This means treating your security policies just like you treat your application code.

This can be applied to many different areas of security:
- **Infrastructure Security**: Using Infrastructure as Code security tools to scan for misconfigurations (see S051).
- **Policy Enforcement**: Using a policy engine like Open Policy Agent (OPA) to define and enforce security policies for your CI/CD pipeline, Kubernetes cluster, or APIs.
- **Security Scanning**: Defining the configuration for your security scanners (SAST, DAST, etc.) as code.
- **Incident Response**: Defining your incident response playbooks as code that can be automatically executed.

## 5. Rationale

Security as Code is the application of DevOps principles to security. It:
- **Automates Security**: Allows you to automate the enforcement and testing of your security policies.
- **Shifts Security Left**: Integrates security into the developer workflow, providing fast feedback and enabling developers to own security.
- **Provides a Single Source of Truth**: Your version-controlled code repository becomes the single source of truth for your security policies.
- **Is Auditable and Repeatable**: Makes it easy to audit your security policies and to apply them consistently across all your environments.

## 6. Consequences

- **Positive**:
    - A more automated, scalable, and auditable security program.
    - A better and more collaborative relationship between security and development teams (DevSecOps).
- **Negative**:
    - **Requires new skills**: Security professionals need to learn how to code and how to use modern development tools.
    - **Requires a cultural shift**: Requires a shift from a traditional, gatekeeper model of security to a more collaborative and enabling model.

## 7. Known Uses

- **Open Policy Agent (OPA)**: The de-facto standard for policy-as-code.
- **This is a core principle** of the entire DevSecOps movement.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | A visionary approach that redefines how security is done in a modern, automated world.                |
| **2. Governance**       | 5           | A powerful and scalable model for security governance.                                                |
| **3. Economy**          | 4           | Improves the efficiency and effectiveness of the security program.                                    |
| **4. Technology**       | 5           | A fundamental part of the modern DevOps and cloud-native technology stack.                            |
| **5. Operations**       | 4           | Transforms security operations from a manual, reactive function to an automated, proactive one.       |
| **6. Culture**          | 5           | The very definition of a DevSecOps culture.                                                           |
| **7. Resilience**       | 5           | Builds strong resilience by making security automated, repeatable, and consistent.                    |
| **Overall Score**       | **4.7**     | A foundational and transformative pattern that is at the heart of modern security engineering and security.     |
