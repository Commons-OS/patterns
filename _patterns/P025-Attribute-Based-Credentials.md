_# Pattern: Attribute-Based Credentials

## 1. Pattern Name and Number

**P025: Attribute-Based Credentials (ABCs)**

## 2. Problem

Traditional identity systems are all-or-nothing. To prove you are over 18, you show a driver's license, which reveals not just your age but also your name, address, and other sensitive information. This unnecessary disclosure of personal data creates privacy risks. Users lack the ability to selectively disclose only the information that is strictly necessary for a given interaction.

## 3. Context

You are designing an identity or access control system. You want to enable users to prove that they possess certain attributes (e.g., "is a student," "is a resident of New York," "has a valid subscription") without revealing their full identity or other, irrelevant attributes.

## 4. Solution

**Implement an Attribute-Based Credential (ABC) system, where identity is not a single, monolithic concept but a collection of distinct, verifiable attributes.** In an ABC system, a trusted issuer provides a user with a set of digitally signed credentials, each representing a single attribute. The user can then present one or more of these credentials to a verifier to prove that they possess the required attributes, without revealing any other information.

This is a core concept of Self-Sovereign Identity (SSI) (P064) and is often implemented using Verifiable Credentials (VCs) and Decentralized Identifiers (DIDs).

## 5. Rationale

ABCs enable a more granular and privacy-preserving approach to identity. They:
- **Support Selective Disclosure**: Allow users to share only the minimal amount of information required for a given transaction.
- **Enhance User Control**: Put the user in control of their own data, allowing them to decide what information to share and with whom.
- **Reduce Data Hoarding**: Verifiers don't need to collect and store large amounts of personal data; they only need to verify the required attributes at the time of the interaction.

## 6. Consequences

- **Positive**:
    - A massive improvement in user privacy and control.
    - Reduced risk and liability for verifiers, as they no longer need to store sensitive personal data.
    - A more flexible and composable approach to identity.
- **Negative**:
    - Requires a new infrastructure of issuers, holders (users), and verifiers, and a way to manage trust between them (e.g., a Trust Registry).
    - The user experience of managing a wallet of credentials can be complex.
    - The technology and standards are still maturing.

## 7. Known Uses

- **Verifiable Credentials (VCs)**: The W3C Verifiable Credentials standard is a technical implementation of the ABC concept.
- **Digital Identity Wallets**: Mobile apps that allow users to store and manage their digital credentials from various issuers.
- **Academic Credentials**: Universities can issue verifiable credentials for degrees and courses, allowing students to easily prove their educational qualifications to employers.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns perfectly with the vision of a user-centric, privacy-preserving digital identity.              |
| **2. Governance**       | 4           | A new governance model for identity based on decentralization and user control.                       |
| **3. Economy**          | 4           | Enables a more efficient and trustworthy digital economy by reducing friction in identity verification. |
| **4. Technology**       | 4           | A rapidly maturing technology based on open standards like VCs and DIDs.                              |
| **5. Operations**       | 3           | Requires the establishment and operation of a new ecosystem of issuers and verifiers.                 |
| **6. Culture**          | 5           | Represents a fundamental cultural shift from organization-centric to user-centric identity.           |
| **7. Resilience**       | 4           | Builds resilience by removing single points of failure in the identity system.                        |
| **Overall Score**       | **4.1**     | A foundational pattern for the future of digital identity.                                            |
