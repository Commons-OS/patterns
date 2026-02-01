_# Pattern: Defense in Depth

## 1. Pattern Name and Number

**S032: Defense in Depth**

## 2. Problem

Relying on a single security control, such as a perimeter firewall, creates a single point of failure. If that one control is breached, the entire system is exposed, and attackers can move freely to access sensitive resources.

## 3. Context

You are designing the security architecture for a value creation system. You must assume that any single security control can and will eventually fail. You need a strategy that provides resilience against security failures and slows down attackers.

## 4. Solution

**Implement multiple, layered, and redundant security controls throughout the system.** The goal is to create a series of defensive barriers, so that if one layer fails, another is in place to thwart an attack. This approach is often compared to the layered defenses of a medieval castle.

Layers can include:
- **Physical Security**: Controls access to physical hardware.
- **Network Security**: Firewalls, Intrusion Detection/Prevention Systems (IDS/IPS), and network segmentation.
- **Host Security**: Hardening operating systems, endpoint protection, and anti-malware.
- **Application Security**: Secure coding practices, input validation, and Web Application Firewalls (WAFs).
- **Data Security**: Encryption at rest and in transit, data loss prevention (DLP), and access controls.
- **Identity and Access Management**: Strong authentication, MFA, and least privilege.
- **Monitoring and Response**: Security logging, SIEM, and a defined incident response plan.

## 5. Rationale

Defense in Depth creates a more resilient and robust security posture. It:
- **Eliminates Single Points of Failure**: A breach of one layer does not compromise the entire system.
- **Slows Down Attackers**: Forces attackers to bypass multiple controls, giving security teams more time to detect and respond.
- **Provides Redundancy**: If one control is misconfigured or fails, others can still provide protection.
- **Addresses a Wide Range of Threats**: Different layers are effective against different types of attacks.

## 6. Consequences

- **Positive**:
    - Significantly increased security resilience.
    - Better protection against sophisticated, multi-stage attacks.
    - Provides compensatory controls for weaknesses in other layers.
- **Negative**:
    - Can increase complexity and management overhead.
    - Can be more costly to implement due to the need for multiple security tools.
    - Requires careful planning to ensure layers are complementary and not redundant in a way that adds no value.

## 7. Known Uses

- **PCI DSS (Payment Card Industry Data Security Standard)**: The standard requires multiple layers of security controls to protect cardholder data.
- **NIST Cybersecurity Framework**: The framework's "Protect" function emphasizes a layered security approach.
- **Military Strategy**: The concept originates from military strategy, where multiple lines of defense are used to protect a target.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of creating robust and secure systems.                                         |
| **2. Governance**       | 5           | A fundamental principle of security governance and risk management.                                   |
| **3. Economy**          | 3           | Can be expensive, but the cost of a major breach is often far higher.                                   |
| **4. Technology**       | 5           | A core architectural principle that leverages a wide range of security technologies.                  |
| **5. Operations**       | 4           | Increases operational complexity but is essential for effective security operations.                  |
| **6. Culture**          | 4           | Promotes a culture of security awareness and layered thinking.                                        |
| **7. Resilience**       | 5           | The very definition of security resilience; the ability to withstand and recover from attacks.        |
| **Overall Score**       | **4.3**     | A foundational and non-negotiable pattern for securing any modern value creation system.             |
