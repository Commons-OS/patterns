_# Pattern: Multi-Factor Authentication

## 1. Pattern Name and Number

**S036: Multi-Factor Authentication (MFA)**

## 2. Problem

Passwords alone are a weak form of authentication. They can be stolen, guessed, or cracked, and a single compromised password can give an attacker full access to a user's account and sensitive data. Relying solely on something the user *knows* is no longer sufficient.

## 3. Context

You are designing the authentication system for a value creation system. You need to provide a secure way for users to prove their identity and gain access to the system, protecting against unauthorized access even if their password is compromised.

## 4. Solution

**Require users to provide two or more independent verification factors to gain access to a resource.** This combines something the user knows (password) with something they *have* (a physical token or mobile device) or something they *are* (a biometric characteristic).

Common authentication factors include:
1.  **Knowledge Factor**: Something the user knows (e.g., password, PIN).
2.  **Possession Factor**: Something the user has (e.g., a mobile phone receiving a one-time password (OTP), a hardware security key like a YubiKey).
3.  **Inherence Factor**: Something the user is (e.g., fingerprint, facial recognition, voiceprint).

## 5. Rationale

MFA provides a critical layer of security on top of passwords. It:
- **Protects Against Credential Theft**: Even if an attacker steals a user's password, they cannot access the account without the second factor.
- **Significantly Increases Security**: According to Microsoft, MFA can block over 99.9% of account compromise attacks.
- **Provides Defense in Depth for Authentication**: Creates layered, redundant authentication controls.

## 6. Consequences

- **Positive**:
    - Dramatically reduces the risk of unauthorized account access.
    - Protects against common attacks like phishing, credential stuffing, and brute-force attacks.
    - Increases user confidence and trust in the system's security.
- **Negative**:
    - Can add a small amount of friction to the login process for users.
    - Requires users to have a second factor, which may be a challenge for some.
    - Can be more complex to implement and support (e.g., account recovery processes).

## 7. Known Uses

- **Banking and Finance**: Nearly all online banking services require MFA for sensitive transactions.
- **Cloud Services**: Major cloud providers (AWS, Google, Microsoft) strongly recommend or require MFA for administrator accounts.
- **Social Media**: Platforms like Google, Facebook, and Twitter offer MFA to protect user accounts.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of creating secure and trustworthy systems.                                    |
| **2. Governance**       | 5           | A fundamental governance control for managing access risk.                                            |
| **3. Economy**          | 4           | Prevents significant economic loss from account takeovers and fraud.                                  |
| **4. Technology**       | 4           | A widely available and standardized technology.                                                       |
| **5. Operations**       | 4           | Requires operational processes for user enrollment and account recovery.                              |
| **6. Culture**          | 4           | Encourages a culture of security awareness among users.                                               |
| **7. Resilience**       | 5           | Creates strong resilience against a wide range of common cyberattacks.                                |
| **Overall Score**       | **4.3**     | A critical and highly effective security pattern that should be implemented for all user accounts.   |
