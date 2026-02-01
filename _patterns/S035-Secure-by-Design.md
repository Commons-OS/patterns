_# Pattern: Secure by Design

## 1. Pattern Name and Number

**S035: Secure by Design**

## 2. Problem

Security is often treated as a feature to be added on late in the development cycle, or as a reaction to vulnerabilities that have already been discovered. This "bolt-on" approach is costly, ineffective, and leaves systems perpetually vulnerable to attack.

## 3. Context

You are at the beginning of the design and development lifecycle for a new value creation system. You need to create a system that is fundamentally secure, rather than one that is simply patched to be secure after the fact.

## 4. Solution

**Integrate security into every phase of the system development lifecycle (SDLC), from initial conception to deployment and maintenance.** Security should be a core requirement, just like functionality or performance.

This involves:
- **Threat Modeling**: Proactively identify and mitigate potential security threats during the design phase.
- **Secure Coding Standards**: Follow established best practices for writing secure code to prevent common vulnerabilities (e.g., OWASP Top 10).
- **Security Testing**: Integrate static (SAST), dynamic (DAST), and interactive (IAST) security testing throughout the development process.
- **Secure Defaults**: Configure the system to be secure by default, requiring users to explicitly weaken security settings if necessary.
- **Security as Code**: Automate security controls and policies as part of the infrastructure and deployment pipeline.

## 5. Rationale

Building security in from the start is far more effective and efficient than trying to add it on later. This approach:
- **Reduces Vulnerabilities**: Proactively eliminates security flaws before they can be exploited.
- **Lowers Costs**: The cost of fixing a security vulnerability increases exponentially the later it is found in the development cycle.
- **Increases Trust**: Demonstrates a commitment to security that builds trust with users and partners.
- **Fosters a Security Culture**: Makes security a shared responsibility for the entire development team, not just a separate security team.

## 6. Consequences

- **Positive**:
    - A fundamentally more secure and resilient system.
    - Reduced development and maintenance costs over the long term.
    - Faster time-to-market for secure products.
    - Enhanced brand reputation and user trust.
- **Negative**:
    - Requires a significant cultural shift to integrate security into development processes.
    - May require developers to learn new skills and tools.
    - Can increase upfront development time and effort.

## 7. Known Uses

- **Microsoft Security Development Lifecycle (SDL)**: A comprehensive, company-wide process for building more secure software.
- **OWASP SAMM (Software Assurance Maturity Model)**: A framework for helping organizations formulate and implement a strategy for software security that is tailored to their specific business risks.
- **DevSecOps**: A cultural and technical movement that integrates security practices into the DevOps workflow.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of creating inherently trustworthy and high-quality systems.                   |
| **2. Governance**       | 5           | A core governance principle for managing software development risk.                                   |
| **3. Economy**          | 4           | Reduces the long-term economic cost of security vulnerabilities and breaches.                         |
| **4. Technology**       | 5           | A fundamental principle for modern software engineering and technology development.                   |
| **5. Operations**       | 5           | Integrates security into the core operational processes of software development (DevSecOps).          |
| **6. Culture**          | 5           | Drives a culture where security is everyone's responsibility.                                         |
| **7. Resilience**       | 5           | Creates systems that are resilient to attack by design, not by accident.                              |
| **Overall Score**       | **4.9**     | An absolutely essential, non-negotiable pattern for building any modern software or system.          |
