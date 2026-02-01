_# Pattern: Privacy by Default

## 1. Pattern Name and Number

**P022: Privacy by Default**

## 2. Problem

Many applications and services are configured with permissive, data-sharing settings out of the box. Users are expected to navigate complex settings menus to restrict the collection and sharing of their data. Most users never change the default settings, which means their data is often collected and used in ways they do not expect or want. The burden of privacy protection is placed on the user.

## 3. Context

You are designing a system, application, or service that processes personal data. You want to ensure that you are respecting user privacy from the very beginning and building a system that is trustworthy by design.

## 4. Solution

**Implement the principle of Privacy by Default, which means that the most privacy-protective settings are the default settings.** The system should be configured to collect only the minimum amount of personal data necessary for the service to function, and this data should not be shared or used for other purposes without the user actively choosing to opt-in.

This means:
- **Minimal Data Collection**: Do not collect any personal data that is not essential for the service.
- **No Pre-checked Boxes**: Consent for non-essential data processing or sharing must be an active, opt-in choice, not a pre-checked box.
- **Privacy-Protective Defaults**: Features like location tracking, ad personalization, and public visibility of profiles should be off by default.

## 5. Rationale

Privacy by Default shifts the burden of privacy protection from the user to the service provider. It:
- **Respects Users**: It treats user privacy as a fundamental right, not as a setting to be managed.
- **Builds Trust**: Demonstrates a commitment to privacy that can be a strong competitive differentiator.
- **Ensures Compliance**: It is a core requirement of GDPR (Article 25) and other modern data protection laws.
- **Protects the Majority**: Since most users do not change default settings, it ensures that the majority of users are protected.

## 6. Consequences

- **Positive**:
    - Increased user trust and a stronger brand reputation.
    - Compliance with a key principle of modern data protection law.
    - A more ethical and user-centric product.
- **Negative**:
    - May reduce the amount of data available for analytics and personalization, which could impact business models that rely on extensive data collection.
    - May require more user education to encourage them to opt-in to features that require more data.

## 7. Known Uses

- **GDPR**: Article 25, "Data protection by design and by default," makes this a legal requirement for any service processing the data of EU citizens.
- **Signal**: The messaging app is a prime example of a service built with privacy by default, with features like end-to-end encryption enabled for all conversations by default.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of a trustworthy and user-centric digital world.                               |
| **2. Governance**       | 5           | A fundamental principle of ethical and compliant data governance.                                     |
| **3. Economy**          | 3           | Can challenge data-hungry business models, but it is the foundation of a sustainable data economy.    |
| **4. Technology**       | 4           | Requires that privacy be a core consideration in the system's architecture and configuration.         |
| **5. Operations**       | 4           | Requires a conscious and deliberate approach to system configuration and feature design.              |
| **6. Culture**          | 5           | Fosters a culture that puts the user and their privacy first.                                         |
| **7. Resilience**       | 4           | Builds legal and social resilience by aligning with user expectations and regulatory requirements.    |
| **Overall Score**       | **4.3**     | A non-negotiable, foundational principle for any modern, trustworthy service.                          |
