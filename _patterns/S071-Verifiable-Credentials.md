_# Pattern: Verifiable Credentials

## 1. Pattern Name and Number

**S071: Verifiable Credentials**

## 2. Problem

Traditional credentials, like a driver's license or a university degree, are physical documents that are difficult to verify online. Digital credentials, like a username and password, are just claims that are not backed by any proof. We need a way to represent and verify credentials in a way that is digitally native, secure, and trustworthy.

## 3. Context

You need a way for an entity (the **issuer**) to make a claim about another entity (the **subject**), and for a third entity (the **verifier**) to be able to cryptographically verify that claim. For example, a university (issuer) needs to issue a degree to a student (subject), and an employer (verifier) needs to be able to verify that the degree is authentic.

## 4. Solution

**Use Verifiable Credentials (VCs), a new W3C standard for digitally signed claims.** A Verifiable Credential is a set of claims made by an issuer about a subject, packaged in a tamper-evident and cryptographically verifiable data format.

The model involves three roles:
1.  **Issuer**: An entity that issues a credential (e.g., a university, a government, an employer).
2.  **Holder**: The subject of the credential, who holds it and can present it for verification (e.g., a student, a citizen, an employee).
3.  **Verifier**: An entity that needs to verify a credential (e.g., an employer, a website, a border agent).

The issuer creates a credential, cryptographically signs it with their private key, and gives it to the holder. The holder can then present the credential to a verifier. The verifier can check the digital signature on the credential to be sure that it was issued by the claimed issuer and that it has not been tampered with.

## 5. Rationale

Verifiable Credentials are a fundamental building block for a new, decentralized trust infrastructure for the internet. They are:
- **Tamper-Evident**: Any change to the credential will invalidate the digital signature.
- **Cryptographically Verifiable**: The verifier can be certain of the origin and integrity of the credential.
- **Decentralized**: They do not require the verifier to have a direct relationship with the issuer. The verification is done purely through cryptography.
- **Privacy-Preserving**: VCs can be used in combination with Zero-Knowledge Proofs to allow a holder to selectively disclose only the information that is necessary for a specific transaction (e.g., proving you are over 18 without revealing your date of birth).

## 6. Consequences

- **Positive**:
    - A secure, interoperable, and decentralized way to represent and verify claims.
    - A massive reduction in the friction and cost of identity verification.
- **Negative**:
    - **Ecosystem is still maturing**: The standards and technologies are still new.
    - **Key Management**: The security of the whole system relies on the secure management of the issuer's and holder's private keys.
    - **Revocation**: Managing the revocation of credentials in a decentralized way is a complex problem.

## 7. Known Uses

- **W3C Verifiable Credentials Data Model**: The core W3C standard.
- **Education**: Many universities are experimenting with issuing digital diplomas as Verifiable Credentials.
- **Healthcare**: Can be used for verifiable health records or vaccination certificates.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | A visionary technology that could create a new layer of trust for the internet.                       |
| **2. Governance**       | 5           | A decentralized governance model for trust and verification.                                          |
| **3. Economy**          | 5           | Could unlock a huge amount of economic value by reducing the friction of trusted interactions.        |
| **4. Technology**       | 4           | A cutting-edge technology that is rapidly maturing.                                                   |
| **5. Operations**       | 3           | The operational complexity, especially around key management and revocation, is still a challenge.    |
| **6. Culture**          | 5           | Represents a cultural shift towards a more trustworthy and verifiable digital world.                  |
| **7. Resilience**       | 5           | Builds strong resilience by decentralizing trust and verification.                                    |
| **Overall Score**       | **4.6**     | A foundational and transformative pattern for the future of digital trust and identity.                |
