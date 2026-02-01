_# Pattern: Input Validation

## 1. Pattern Name and Number

**S037: Input Validation**

## 2. Problem

Any data that enters a system from an external source is untrustworthy. Malicious actors can craft special inputs to exploit vulnerabilities in how the system processes that data. This can lead to a wide range of attacks, including SQL injection, Cross-Site Scripting (XSS), buffer overflows, and remote code execution, potentially compromising the entire system.

## 3. Context

You are building any component of a system that accepts input from an external source. This includes user input from web forms, API requests from other services, data from files, or messages from a queue. You must assume all such input is potentially malicious.

## 4. Solution

**Validate all input for correctness (syntax) and appropriateness (semantics) before it is processed.** The core principle is to "never trust user input."

Key validation strategies:
- **Allowlist Validation**: Define a strict set of allowed characters, patterns, or values (e.g., using a regular expression for a zip code `^[0-9]{5}$`). Reject any input that does not conform to the allowlist. This is the recommended approach.
- **Blocklist Validation**: Define a list of known malicious or dangerous characters (e.g., `<script>`, `--`). This is less secure, as attackers can often find ways to bypass the blocklist.
- **Type Checking**: Ensure the data is of the expected type (e.g., integer, boolean).
- **Length Checking**: Ensure the data is within an expected length range to prevent buffer overflows.
- **Canonicalization**: Convert the input into its simplest, standard form before validation to defeat encoding and obfuscation tricks.

## 5. Rationale

Input validation is one of the most fundamental and effective security controls. It:
- **Prevents a Wide Range of Attacks**: It is the primary defense against injection-style attacks, which consistently rank among the most common and dangerous vulnerabilities.
- **Improves System Stability**: Prevents malformed data from causing crashes or unexpected behavior.
- **Enforces Data Integrity**: Ensures that only valid data is stored and processed by the system.

## 6. Consequences

- **Positive**:
    - Dramatically reduces the system's attack surface.
    - Prevents many of the most common and critical web application vulnerabilities.
    - Increases the overall robustness and reliability of the system.
- **Negative**:
    - Can be complex to implement correctly, especially for complex data formats.
    - If validation rules are too strict, they can reject legitimate input, leading to a poor user experience.
    - Requires developers to be diligent and apply validation consistently at every trust boundary.

## 7. Known Uses

- **Web Application Firewalls (WAFs)**: WAFs automatically apply input validation rules to web traffic before it reaches the application.
- **API Gateways**: API gateways often perform validation on incoming API requests to ensure they conform to the defined schema.
- **Secure Coding Libraries**: Frameworks like OWASP ESAPI provide libraries for performing canonicalization and validation of user input.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of building robust and reliable systems.                                       |
| **2. Governance**       | 5           | A fundamental governance control for managing the risk of untrusted data.                             |
| **3. Economy**          | 4           | Prevents significant economic loss from data breaches caused by injection attacks.                    |
| **4. Technology**       | 5           | A fundamental technique in secure software engineering.                                               |
| **5. Operations**       | 4           | Requires operational discipline to ensure validation is applied consistently.                         |
| **6. Culture**          | 5           | Fosters a culture of "zero trust" towards external data.                                              |
| **7. Resilience**       | 5           | Provides strong resilience against a huge class of common attacks.                                    |
| **Overall Score**       | **4.6**     | An absolutely essential, first-line-of-defense security pattern for any software system.             |
