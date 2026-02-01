_# Pattern: Runtime Application Self-Protection

## 1. Pattern Name and Number

**S057: Runtime Application Self-Protection (RASP)**

## 2. Problem

Traditional network and host-based security controls, like Web Application Firewalls (WAFs), have a limited understanding of the application they are protecting. They sit outside the application and try to identify attacks by inspecting network traffic. This makes them prone to false positives and false negatives, and they can be bypassed by sophisticated attackers. They don't have the context to understand what is a legitimate or a malicious action from the application's point of view.

## 3. Context

You are running a web application and need a more accurate and effective way to protect it from attacks in real-time. You need a security control that has deep visibility into the application's internal workings and can respond immediately to threats.

## 4. Solution

**Implement Runtime Application Self-Protection (RASP), a security technology that is built or linked into an application or application runtime, and is capable of controlling application execution and detecting and preventing real-time attacks.**

RASP works by instrumenting the application from the inside. It has full context of the application's code, data flow, and configuration. This allows it to identify and block attacks with much greater accuracy than a WAF.

RASP can be deployed in two modes:
- **Monitoring Mode**: It detects and logs attacks but does not block them.
- **Blocking Mode**: It actively blocks attacks as they happen.

## 5. Rationale

RASP provides a more modern and effective approach to application security. It:
- **Is Highly Accurate**: Because it has full application context, it can detect attacks with very few false positives.
- **Provides Real-Time Protection**: It can block attacks in real-time, before they can do any damage.
- **Is Easy to Deploy**: It is typically deployed as a simple library or agent that is added to the application, with no need for network re-architecture.

## 6. Consequences

- **Positive**:
    - A significant improvement in the accuracy and effectiveness of application security.
    - Real-time protection against a wide range of attacks.
- **Negative**:
    - **Performance Overhead**: It can add a small performance overhead to the application.
    - **Complexity**: It adds another component to the application stack that needs to be managed.
    - **Language Support**: RASP solutions are typically language-specific and may not be available for all programming languages.

## 7. Known Uses

- **OWASP**: The Open Web Application Security Project has a lot of information on RASP.
- **Many commercial vendors** (like Imperva, Signal Sciences, and Contrast Security) offer RASP solutions.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of a more intelligent and self-defending application security model.           |
| **2. Governance**       | 4           | A powerful, real-time governance control for application security.                                    |
| **3. Economy**          | 4           | Prevents costly data breaches and application downtime.                                               |
| **4. Technology**       | 4           | A modern and increasingly popular application security technology.                                    |
| **5. Operations**       | 3           | Adds complexity to the application stack.                                                             |
| **6. Culture**          | 4           | Promotes a culture of building security into the application itself.                                  |
| **7. Resilience**       | 5           | Builds strong resilience by enabling the application to defend itself against attacks in real-time.   |
| **Overall Score**       | **4.0**     | A powerful and modern pattern for real-time application security.                                      |
