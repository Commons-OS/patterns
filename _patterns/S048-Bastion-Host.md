_# Pattern: Bastion Host

## 1. Pattern Name and Number

**S048: Bastion Host**

## 2. Problem

To manage servers and other infrastructure in a private network, administrators need a way to connect to them from the outside world (e.g., from their corporate network or the internet). Exposing management ports like SSH or RDP directly to the internet for every server is extremely risky, as it creates a massive attack surface and makes the servers vulnerable to brute-force attacks and exploits.

## 3. Context

You have a private network (e.g., a VPC in the cloud) containing infrastructure that needs to be managed remotely. You need to provide secure administrative access to this infrastructure without exposing it directly to untrusted networks.

## 4. Solution

**Establish a Bastion Host (also known as a Jump Box or Jump Server), a single, hardened, and highly monitored server that acts as the sole entry point for administrative access to a private network.** Administrators first connect to the bastion host, and from there, they can "jump" to the other servers in the private network.

Key characteristics of a bastion host:
- **Hardened**: The bastion host itself should be stripped of all non-essential software and services and configured with the highest level of security.
- **Highly Monitored**: All activity on the bastion host should be extensively logged and monitored for any suspicious behavior (see S039: Security Logging).
- **Strict Access Control**: Access to the bastion host should be tightly controlled, using Multi-Factor Authentication (S036) and allowing connections only from specific, trusted IP addresses.
- **No Sensitive Data**: The bastion host should not store any sensitive data.

## 5. Rationale

A bastion host acts as a secure "choke point" for administrative traffic. It:
- **Reduces Attack Surface**: Instead of exposing every server to the internet, you only expose a single, hardened point of entry.
- **Centralizes Auditing and Control**: All administrative access goes through a single point, making it much easier to monitor and control.
- **Improves Security Posture**: Provides a simple and effective way to isolate your private network from the public internet.

## 6. Consequences

- **Positive**:
    - A dramatic reduction in the attack surface of your private network.
    - Centralized logging and auditing of all administrative access.
    - A simple and effective way to enforce strong authentication for administrative users.
- **Negative**:
    - The bastion host itself becomes a high-value target for attackers and a single point of failure for administrative access. It must be protected accordingly.
    - Can introduce an extra step for administrators, which can be a minor inconvenience.

## 7. Known Uses

- **Cloud Infrastructure**: Bastion hosts are a standard and recommended pattern for securely managing instances in a private VPC in AWS, Azure, and Google Cloud.
- **Corporate Networks**: Used to provide secure access for remote administrators or third-party vendors who need to manage internal systems.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 3           | A practical pattern for securing infrastructure.                                                      |
| **2. Governance**       | 4           | A strong governance control for managing administrative access.                                       |
| **3. Economy**          | 3           | Prevents economic loss from breaches caused by exposed management ports.                              |
| **4. Technology**       | 4           | A standard and well-understood security technology.                                                   |
| **5. Operations**       | 4           | A core operational security practice for network administration.                                      |
| **6. Culture**          | 3           | Fosters a culture of secure administrative access.                                                    |
| **7. Resilience**       | 4           | Builds resilience by protecting the internal network from direct attack.                              |
| **Overall Score**       | **3.6**     | A simple, effective, and essential pattern for securing administrative access to any private network. |
