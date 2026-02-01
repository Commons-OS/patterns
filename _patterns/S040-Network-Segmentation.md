_# Pattern: Network Segmentation

## 1. Pattern Name and Number

**S040: Network Segmentation**

## 2. Problem

A flat network, where all systems can communicate freely with each other, is a security nightmare. If a single, non-critical system is compromised (e.g., a development web server), an attacker can easily move laterally across the network to attack more critical systems, such as databases containing sensitive customer data. The entire network becomes a single, large attack surface.

## 3. Context

You are designing the network architecture for a value creation system that consists of multiple components with different levels of sensitivity and trust. You need to control the flow of traffic between these components to contain breaches and limit an attacker's ability to move laterally.

## 4. Solution

**Divide the network into smaller, isolated segments (or zones) and enforce strict access controls on all traffic flowing between them.** The goal is to create a "zero trust" network where communication is denied by default and only explicitly allowed if there is a legitimate business need.

Common segmentation strategies:
- **Perimeter Firewalls**: The traditional approach of creating a "trusted" internal network and an "untrusted" external network. This is no longer sufficient on its own.
- **VLANs (Virtual LANs)**: Segmenting the network at Layer 2 (the data link layer) to create broadcast domains.
- **Subnetting**: Segmenting the network at Layer 3 (the network layer) using IP address ranges.
- **Microsegmentation**: A modern, granular approach where security policies are applied to individual workloads (e.g., virtual machines, containers). This allows you to create a secure perimeter around every single application, effectively treating each one as its own isolated segment.

## 5. Rationale

Network segmentation is a core principle of a Defense in Depth (S032) strategy. It:
- **Contains Breaches**: Limits the "blast radius" of a security incident. If one segment is compromised, the others remain protected.
- **Reduces Attack Surface**: An attacker can only see and attack the systems within the segment they have compromised.
- **Improves Performance**: Can reduce network congestion by isolating traffic within a segment.
- **Enhances Monitoring**: Makes it easier to monitor traffic for suspicious activity as it crosses segment boundaries.

## 6. Consequences

- **Positive**:
    - Significantly improved security posture and resilience against lateral movement.
    - Better containment of security incidents.
    - Improved visibility and control over network traffic.
- **Negative**:
    - Can be complex to design and manage, especially in large and dynamic environments.
    - Requires careful planning of firewall rules and access control lists, which can be prone to error.
    - Microsegmentation, while powerful, requires sophisticated tools and a mature operations team.

## 7. Known Uses

- **PCI DSS**: The Payment Card Industry Data Security Standard requires strict network segmentation to isolate the Cardholder Data Environment (CDE) from the rest of the network.
- **Zero Trust Architecture**: Network segmentation is a foundational component of a Zero Trust security model (see S031).
- **Cloud VPCs (Virtual Private Clouds)**: Cloud providers allow users to create logically isolated sections of their cloud where they can launch resources in a virtual network that they define.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of building robust and compartmentalized systems.                              |
| **2. Governance**       | 5           | A fundamental governance control for managing internal network traffic and risk.                      |
| **3. Economy**          | 4           | Reduces the economic impact of a breach by containing its scope.                                      |
| **4. Technology**       | 5           | A fundamental networking and security technology.                                                     |
| **5. Operations**       | 3           | Can significantly increase operational complexity, especially for rule management.                    |
| **6. Culture**          | 4           | Fosters a culture of "zero trust" within the internal network.                                        |
| **7. Resilience**       | 5           | Directly builds resilience by containing the spread of security failures.                             |
| **Overall Score**       | **4.3**     | A foundational security pattern for any network of non-trivial size or complexity.                   |
