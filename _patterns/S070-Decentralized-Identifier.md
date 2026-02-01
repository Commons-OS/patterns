_# Pattern: Decentralized Identifier (DID)

## 1. Pattern Name and Number

**S070: Decentralized Identifier (DID)**

## 2. Problem

Traditional digital identifiers, like email addresses or usernames, are issued and controlled by a central authority (e.g., Google, Facebook, your employer). This creates a dependency on that authority. If the authority decides to revoke your identifier, or if it goes out of business, you lose your digital identity. This centralized model is the root of vendor lock-in and a single point of control for digital identity.

## 3. Context

You need to create a digital identity for a user, organization, or thing that is globally unique, persistent, and not controlled by any single central authority. You need a foundation for a truly self-sovereign identity.

## 4. Solution

**Use a Decentralized Identifier (DID), a new type of globally unique identifier that is registered on a decentralized system (like a blockchain or other distributed ledger) and is under the full control of the identity owner.**

A DID is a simple text string that looks like this: `did:example:123456789abcdefghi`. The DID points to a **DID Document**, a JSON file that contains the public keys, service endpoints, and other metadata associated with the DID. The identity owner controls the DID Document and can update it at any time by using the private keys associated with the DID.

## 5. Rationale

DIDs are a fundamental building block for decentralized identity and digital sovereignty. They:
- **Enable Self-Sovereignty**: The identity owner creates, controls, and can even delete their own identifier without permission from any central authority.
- **Are Persistent**: A DID can last for the lifetime of the subject, unlike an email address or employee ID which can change.
- **Are Globally Resolvable**: Anyone in the world can look up the DID Document for a given DID to find its public keys and service endpoints.
- **Are Cryptographically Verifiable**: The link between the DID and the DID Document is secured with cryptography.

## 6. Consequences

- **Positive**:
    - A truly decentralized and self-sovereign foundation for digital identity.
    - Eliminates the dependency on centralized identity providers.
- **Negative**:
    - **Ecosystem is still maturing**: The standards and technologies around DIDs are still new and evolving.
    - **Key Management is Critical**: The user is fully responsible for the security of their private keys. If the keys are lost, the DID can be lost forever. This is a major usability challenge.
    - **Complexity**: The concepts of DIDs, DID Documents, and decentralized ledgers can be complex for developers and users to understand.

## 7. Known Uses

- **W3C DID Specification**: The core standard for DIDs is being developed by the World Wide Web Consortium (W3C).
- **Hyperledger Indy, DIF, Sovrin**: Major open-source projects and foundations that are building DID-based identity systems.
- **Microsoft Entra Verified ID**: Microsoft's decentralized identity solution is built on DIDs.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | A visionary technology that could fundamentally change the nature of digital identity.                |
| **2. Governance**       | 5           | A decentralized governance model for identity that puts the user in control.                          |
| **3. Economy**          | 4           | Could unlock a new economy of trusted, peer-to-peer interactions.                                     |
| **4. Technology**       | 4           | A cutting-edge technology that is rapidly maturing.                                                   |
| **5. Operations**       | 3           | The operational complexity, especially around key management, is still a major challenge.             |
| **6. Culture**          | 5           | Represents a major cultural shift towards user-centricity and self-sovereignty.                       |
| **7. Resilience**       | 5           | Builds extremely strong resilience by eliminating single points of failure and control.               |
| **Overall Score**       | **4.4**     | A foundational and transformative pattern for the future of digital identity and sovereignty.          |
