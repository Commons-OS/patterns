_# Pattern: Chaos Engineering for Security

## 1. Pattern Name and Number

**S058: Chaos Engineering for Security**

## 2. Problem

We assume our security controls will work as expected, but we rarely test them under realistic failure conditions. When a real security incident happens, we often find that our monitoring, alerting, and response mechanisms do not work as we thought they would. This is a reactive and dangerous way to manage security.

## 3. Context

You are responsible for the security of a complex, distributed system. You need to be confident that your security controls are robust and that your team is prepared to respond to a real security incident.

## 4. Solution

**Apply the principles of Chaos Engineering to security by proactively and deliberately injecting security-related failures into your system to test its resilience.** This is not about breaking things randomly; it is about running controlled experiments to identify weaknesses in your security posture before an attacker does.

Examples of security chaos experiments include:
- **Simulating a compromised host**: What happens if an attacker gains control of one of your servers? Are your detection and response mechanisms triggered?
- **Simulating a secrets leak**: What happens if an API key or a password is leaked? Can you quickly revoke it and assess the damage?
- **Simulating a denial-of-service attack**: How does your system respond to a sudden spike in traffic?

## 5. Rationale

Chaos Engineering for Security is a proactive and empirical approach to security assurance. It:
- **Identifies Weaknesses Before Attackers Do**: Allows you to find and fix security weaknesses before they can be exploited.
- **Builds Confidence in Your Security Posture**: Gives you real-world evidence that your security controls work as expected.
- **Improves Your Incident Response Capabilities**: Provides realistic training for your incident response team.

## 6. Consequences

- **Positive**:
    - A more resilient and battle-tested security posture.
    - A more prepared and effective incident response team.
- **Negative**:
    - **Risk**: These are live experiments in a production or production-like environment. There is a risk that they could cause a real outage or security incident if not done carefully.
    - **Requires a Mature Culture**: Requires a high degree of trust and a blameless culture. You are deliberately breaking things to learn, not to assign blame.

## 7. Known Uses

- **Netflix**: The pioneers of Chaos Engineering, they have a mature practice for security chaos engineering.
- **Gremlin**: A commercial platform for chaos engineering that includes a library of security-specific experiments.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | A visionary, proactive approach to security assurance.                                                |
| **2. Governance**       | 4           | A powerful governance model for continuously validating security controls.                            |
| **3. Economy**          | 4           | Prevents costly security incidents by identifying weaknesses proactively.                             |
| **4. Technology**       | 4           | A cutting-edge practice that is at the intersection of security, DevOps, and resilience engineering.  |
| **5. Operations**       | 4           | A core practice for mature security and SRE teams.                                                    |
| **6. Culture**          | 5           | Fosters a culture of proactive, empirical, and blameless security.                                    |
| **7. Resilience**       | 5           | The very definition of building resilience by deliberately testing for failure.                       |
| **Overall Score**       | **4.3**     | A powerful and transformative pattern for any organization that is serious about building resilient and maintaining a resilient security posture. |
