---
id: pat_019c19b235067714907bcdebad
page_url: https://commons-os.github.io/patterns/bastion-host/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/bastion-host.md
slug: bastion-host
title: Bastion Host
aliases: []
version: '1.0'
created: '2026-02-01T14:53:55Z'
modified: '2026-02-01T14:53:55Z'
tags:
  universality: universal
  domain: security
  category:
  - practice
  era:
  - cognitive
  origin:
  - Commons OS
  status: draft
  commons_alignment: 3
commons_domain: security
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- commons-os
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview
A bastion host, also known as a jump box or jump server, is a security-hardened computer that provides controlled access to a private network from an external, untrusted network such as the internet. The fundamental problem it solves is the need to expose a minimal attack surface while still allowing legitimate administrative access to internal resources. By channeling all incoming administrative traffic through a single, heavily fortified point, organizations can significantly reduce the risk of unauthorized access to their critical systems. The bastion host acts as a gateway, and it is designed to withstand direct attacks. It typically runs a minimal set of services, often just a single application like an SSH daemon or a proxy server, to limit its vulnerability.

The concept of a bastion host emerged in the early 1990s, with the term being popularized by security expert Marcus J. Ranum. In the early days of the internet, as organizations began connecting their internal networks to the global network, the need for a secure perimeter became paramount. Firewalls were the first line of defense, but they were not always sufficient to protect against all types of attacks. The bastion host was conceived as a critical strongpoint in the network's defense, a hardened server that could be placed in a demilitarized zone (DMZ) to provide an additional layer of security. For commons-based organizations, which often rely on distributed and collaborative infrastructure, the bastion host pattern is particularly relevant. It provides a mechanism for securing access to shared resources, ensuring that only authorized contributors can make changes, and creating a clear audit trail of all administrative actions. This helps to build trust and maintain the integrity of the commons.

### 2. Core Principles
1.  **Minimal Attack Surface:** The bastion host should be configured with the absolute minimum number of services, applications, and open ports necessary for its function. This principle dictates that any software or service not essential for the bastion's role as a secure gateway should be removed or disabled to reduce potential vulnerabilities.
2.  **Single Point of Entry:** All administrative access to the private network must be funneled through the bastion host. This simplifies monitoring, logging, and auditing of all administrative sessions, and it ensures that no unauthorized access paths to the internal network exist.
3.  **Strong Authentication and Authorization:** Access to the bastion host itself must be protected by strong authentication mechanisms, such as multi-factor authentication (MFA) and public-key cryptography. Furthermore, once authenticated, users should be granted only the minimum necessary privileges to perform their tasks, following the principle of least privilege.
4.  **Comprehensive Logging and Monitoring:** All activity on the bastion host, including login attempts, commands executed, and network traffic, must be logged and monitored in real-time. These logs should be shipped to a secure, centralized logging server to prevent tampering and to facilitate incident response.
5.  **Network Isolation:** The bastion host should be located in a segregated network segment, such as a DMZ, to isolate it from both the public internet and the internal private network. This prevents a compromise of the bastion host from immediately leading to a compromise of the entire internal network.
6.  **Immutability:** Treat the bastion host as an immutable component of the infrastructure. Instead of patching or updating a running bastion host, a new, updated instance should be deployed to replace the old one. This approach reduces configuration drift and ensures a consistent and predictable security posture.

### 3. Key Practices
1.  **Use a Hardened Operating System:** Start with a minimal, security-focused operating system image. Remove all unnecessary packages, libraries, and services. Regularly apply security patches and updates to the base image.
2.  **Enforce MFA and Key-Based Authentication:** Disable password-based authentication entirely and require all users to authenticate using SSH keys. Additionally, enforce the use of multi-factor authentication (MFA) to provide an extra layer of security against compromised keys.
3.  **Implement Strict Firewall Rules:** Configure firewall rules to only allow traffic on the necessary ports (e.g., port 22 for SSH) and from trusted IP addresses. All other traffic should be denied by default.
4.  **Centralize and Secure Logs:** Aggregate all logs from the bastion host to a remote, secure logging server. This ensures that logs are not tampered with and are available for analysis even if the bastion host is compromised.
5.  **Regularly Audit and Scan for Vulnerabilities:** Continuously monitor the bastion host for vulnerabilities using automated scanning tools. Regularly audit the bastion host's configuration to ensure it complies with security best practices.
6.  **Implement Session Recording:** Record all administrative sessions to the bastion host. This provides a detailed audit trail of all actions performed by administrators and can be invaluable for forensic analysis in the event of a security incident.
7.  **Automate Deployment and Configuration:** Use infrastructure-as-code tools like Terraform or Ansible to automate the deployment and configuration of the bastion host. This ensures that the bastion host is deployed in a consistent and repeatable manner, reducing the risk of human error.

### 4. Implementation
A successful implementation of a bastion host begins with careful planning and design. The first step is to select a minimal and secure operating system and to create a hardened base image. This image should be regularly updated with the latest security patches. Next, the network architecture needs to be designed, including the placement of the bastion host in a DMZ and the configuration of firewall rules and security groups to strictly control traffic. Infrastructure-as-code tools should be used to define and provision the bastion host and its surrounding network infrastructure. This ensures that the deployment is automated, repeatable, and version-controlled.

Once the bastion host is deployed, the focus shifts to access control and monitoring. User accounts should be provisioned with the principle of least privilege, and access should be granted using a combination of SSH keys and multi-factor authentication. A centralized logging and monitoring solution should be implemented to collect and analyze logs from the bastion host in real-time. Session recording should also be enabled to provide a complete audit trail of all administrative activities. Common tools used for implementing bastion hosts include OpenSSH for secure remote access, Terraform for infrastructure provisioning, Ansible for configuration management, and tools like `auditd` and the ELK stack for logging and monitoring.

Success can be measured by a combination of security and operational metrics. From a security perspective, success means that there are no unauthorized access attempts to the internal network, and that all administrative access is logged and audited. This can be verified through regular penetration testing and security audits. From an operational perspective, success means that legitimate users can access the resources they need without undue friction, and that the bastion host is highly available and performant. Key metrics to track include the number of failed login attempts, the time to detect and respond to security incidents, and the uptime of the bastion host.

### 5. 7 Pillars Assessment
| Pillar | Score (1-5) | Rationale |
|---|---|---|
| Purpose | 5 | The Bastion Host pattern has a very clear and well-defined purpose: to provide a secure, single point of access to a private network. This clarity of purpose makes it a highly effective security control when implemented correctly. |
| Governance | 4 | Effective governance of a bastion host requires strict access control policies, regular audits, and clear lines of responsibility. While the pattern itself encourages good governance, its effectiveness is ultimately dependent on the organization's commitment to enforcing these policies. |
| Culture | 3 | A security-conscious culture is essential for the successful implementation of a bastion host. If developers and administrators are not trained on the importance of secure access practices, they may be tempted to bypass the bastion host or to use weak credentials, undermining its effectiveness. |
| Incentives | 3 | The primary incentive for using a bastion host is risk reduction. However, it can sometimes be perceived as an obstacle to productivity, creating a disincentive for its use. It is important to streamline the user experience of the bastion host to minimize this friction. |
| Knowledge | 4 | Implementing and managing a bastion host requires specialized knowledge of network security, operating system hardening, and access control. While there is a wealth of information available on this topic, it is important to ensure that the team responsible for the bastion host has the necessary expertise. |
| Technology | 5 | The technology required to implement a bastion host is mature, widely available, and well-understood. Open-source tools like OpenSSH and a variety of commercial solutions provide a robust foundation for building a secure bastion host. |
| Resilience | 4 | A bastion host can be a single point of failure if not designed for high availability. However, by deploying multiple bastion hosts in a load-balanced configuration, it is possible to create a highly resilient and fault-tolerant access solution. |
| **Overall** | **4.0** | **The Bastion Host is a powerful and well-established security pattern, but its effectiveness depends on a holistic approach that includes strong governance, a security-aware culture, and a resilient technical implementation.** |

### 6. When to Use
*   When you need to provide remote administrative access to servers in a private network.
*   When you want to centralize and control all administrative access to your infrastructure.
*   When you need to create a detailed audit trail of all administrative actions.
*   When you are operating in a regulated environment that requires strict access controls.
*   When you want to reduce the attack surface of your private network.
*   When you need to provide secure access to a distributed and collaborative infrastructure.

### 7. Anti-Patterns & Gotchas
*   **Shared Credentials:** Allowing multiple users to share the same credentials to access the bastion host. This makes it impossible to attribute actions to a specific individual.
*   **Weak Authentication:** Using weak passwords or not enforcing multi-factor authentication. This makes the bastion host vulnerable to brute-force attacks.
*   **Lack of Logging and Monitoring:** Failing to log and monitor all activity on the bastion host. This makes it difficult to detect and respond to security incidents.
*   **Permissive Firewall Rules:** Configuring overly permissive firewall rules that allow unnecessary traffic to and from the bastion host. This increases the attack surface of the bastion host.
*   **Not Hardening the Host:** Failing to properly harden the bastion host by removing unnecessary services and applications. This leaves the bastion host vulnerable to attack.
*   **Single Point of Failure:** Deploying a single bastion host without a high-availability plan. This can lead to a complete loss of administrative access if the bastion host fails.

### 8. References
1.  [Bastion host - Wikipedia](https://en.wikipedia.org/wiki/Bastion_host)
2.  [14 Best Practices to Secure SSH Bastion Host - Teleport](https://goteleport.com/blog/security-hardening-ssh-bastion-best-practices/)
3.  [What Is a Bastion Host? Types, Use Cases, and Safety Measures - Heimdal Security](https://heimdalsecurity.com/blog/bastion-host/)
