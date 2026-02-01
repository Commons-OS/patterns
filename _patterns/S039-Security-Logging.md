_# Pattern: Security Logging

## 1. Pattern Name and Number

**S039: Security Logging and Monitoring**

## 2. Problem

Without a comprehensive record of events occurring within a system, it is impossible to detect security incidents, investigate breaches, or understand attacker behavior. When an incident occurs, operators are flying blind, unable to determine the scope of the compromise, the attacker's actions, or how to prevent a recurrence.

## 3. Context

You are operating any non-trivial system. You must assume that security incidents will occur, and you need the visibility to detect them, respond to them, and learn from them. You cannot protect what you cannot see.

## 4. Solution

**Implement a robust system for logging relevant security events, aggregating those logs in a central location, and actively monitoring them for suspicious activity.** This creates a detailed audit trail that is the foundation for all incident detection and response.

Key components:
1.  **Instrumentation (Logging)**: Instrument applications, operating systems, and network devices to generate logs for critical security events. This includes logins (successful and failed), access control decisions, administrative changes, and significant errors.
2.  **Aggregation**: Ship all logs from all systems to a central, secure, and tamper-resistant log management system (e.g., a SIEM - Security Information and Event Management system).
3.  **Monitoring & Alerting**: Create automated rules and dashboards to monitor the aggregated logs for patterns of suspicious activity (e.g., multiple failed logins from a single IP address, a user accessing unusual resources). Generate alerts for security personnel when a potential incident is detected.
4.  **Retention**: Retain logs for a sufficient period to support incident investigation and compliance requirements.

## 5. Rationale

Logging and monitoring are the eyes and ears of a security program. They:
- **Enable Incident Detection**: It is the primary mechanism for detecting security breaches in progress.
- **Support Incident Response**: Provides the forensic data needed to understand what happened during an incident, what was compromised, and how to recover.
- **Provide Accountability**: Creates a non-repudiable record of user and system actions.
- **Deter Malicious Actors**: The knowledge that actions are being logged and monitored can deter both internal and external attackers.

## 6. Consequences

- **Positive**:
    - Provides critical visibility into system activity and potential security threats.
    - Essential for effective incident response and forensic analysis.
    - Required by many security compliance frameworks (e.g., PCI DSS, HIPAA).
- **Negative**:
    - Can generate a massive volume of data, which can be costly to store and complex to analyze.
    - Requires specialized tools (like a SIEM) and skilled personnel to be effective.
    - Poorly configured logging can miss critical events, while overly verbose logging can create too much noise.

## 7. Known Uses

- **Security Information and Event Management (SIEM)**: Products like Splunk, IBM QRadar, and Elastic SIEM are designed to aggregate and analyze security logs from across an enterprise.
- **Cloud Monitoring Services**: AWS CloudTrail, Azure Monitor, and Google Cloud Logging provide detailed logs of all API calls and administrative actions within a cloud environment.
- **Web Server Logs**: Web servers generate access logs that can be analyzed to detect attacks like SQL injection, directory traversal, and brute-force login attempts.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of creating transparent and auditable systems.                                 |
| **2. Governance**       | 5           | A cornerstone of security governance, providing the visibility needed to manage risk.                 |
| **3. Economy**          | 4           | Reduces the economic impact of breaches by enabling faster detection and response.                    |
| **4. Technology**       | 5           | A critical technological capability for any mature security program.                                  |
| **5. Operations**       | 5           | The foundation of a Security Operations Center (SOC) and incident response team.                      |
| **6. Culture**          | 4           | Fosters a culture of accountability and transparency.                                                 |
| **7. Resilience**       | 5           | Builds resilience by enabling the system to detect, respond to, and recover from attacks.             |
| **Overall Score**       | **4.6**     | A foundational pattern for security. If you don't have logging, you don't have security.              |
