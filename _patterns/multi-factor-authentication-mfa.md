---
id: pat_f0cc74661d0b489baee24d3c
page_url: https://commons-os.github.io/patterns/multi-factor-authentication-mfa/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/multi-factor-authentication-mfa.md
slug: multi-factor-authentication-mfa
title: Multi-Factor Authentication (MFA)
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
classification:
  universality: universal
  domain: security
  category:
  - pattern
  era:
  - cognitive
  origin:
  - commons-os
  status: draft
  commons_alignment: 4
  commons_domain:
  - business
  - security
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- manus-ai
- cloudsters
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

Multi-Factor Authentication (MFA) is a pattern for building resilient value creation systems.

**Problem:** Passwords alone are a weak form of authentication. They can be stolen, guessed, or cracked, and a single compromised password can give an attacker full access to a user's account and sensitive data. Relying solely on something the user *knows* is no longer sufficient.

**Context:** You are designing the authentication system for a value creation system. You need to provide a secure way for users to prove their identity and gain access to the system, protecting against unauthorized access even if their password is compromised.

### 2. Core Principles

**Require users to provide two or more independent verification factors to gain access to a resource.** This combines something the user knows (password) with something they *have* (a physical token or mobile device) or something they *are* (a biometric characteristic).

Common authentication factors include:
1.  **Knowledge Factor**: Something the user knows (e.g., password, PIN).
2.  **Possession Factor**: Something the user has (e.g., a mobile phone receiving a one-time password (OTP), a hardware security key like a YubiKey).
3.  **Inherence Factor**: Something the user is (e.g., fingerprint, facial recognition, voiceprint).

### 3. Rationale

MFA provides a critical layer of security on top of passwords. It:
- **Protects Against Credential Theft**: Even if an attacker steals a user's password, they cannot access the account without the second factor.
- **Significantly Increases Security**: According to Microsoft, MFA can block over 99.9% of account compromise attacks.
- **Provides Defense in Depth for Authentication**: Creates layered, redundant authentication controls.

### 4. Consequences

- **Positive**:
    - Dramatically reduces the risk of unauthorized account access.
    - Protects against common attacks like phishing, credential stuffing, and brute-force attacks.
    - Increases user confidence and trust in the system's security.
- **Negative**:
    - Can add a small amount of friction to the login process for users.
    - Requires users to have a second factor, which may be a challenge for some.
    - Can be more complex to implement and support (e.g., account recovery processes).

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Banking and Finance**: Nearly all online banking services require MFA for sensitive transactions.
- **Cloud Services**: Major cloud providers (AWS, Google, Microsoft) strongly recommend or require MFA for administrator accounts.
- **Social Media**: Platforms like Google, Facebook, and Twitter offer MFA to protect user accounts.

