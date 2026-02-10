---
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/cross-domain-single-sign-on.md
slug: cross-domain-single-sign-on
title: Cross-Domain Single Sign-On
aliases:
- Cross-Domain SSO
- CDSSO
version: "1.0"
created: "2026-02-10 00:00:00+00:00"
modified: "2026-02-10 00:00:00+00:00"
classification:
  universality: context-dependent
  domain: platform
  category:
  - integration
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 3
  commons_domain:
  - platform
generalizes_from: []
specializes_to: []
enables: []
requires: []
related:
- single-sign-on
- identity-federation
contributors:
- Manus AI
- cloudsters
sources:
- https://docs.pingidentity.com/web-agents/2025.11/user-guide/cdsso.html
- https://docs.oracle.com/cd/E19316-01/820-3746/gipjl/index.html
- https://www.ibm.com/docs/en/samfm/8.0.0.4?topic=solutions-cross-domain-single-sign
- https://aws.amazon.com/what-is/sso/
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Cross-Domain Single Sign-On (CDSSO) is an authentication pattern that enables a user to access multiple applications or services hosted on different internet domains after logging in only once [1]. It extends the concept of traditional Single Sign-On (SSO), which is typically restricted to a single domain, to create a seamless user experience across a distributed landscape of web properties. In today's internet, where organizations often manage a portfolio of services spread across various domains (e.g., `company.com`, `company.net`, `product.io`), CDSSO is crucial for providing unified and secure access. The historical origins of this pattern are tied to the growth of enterprise service portfolios and the need to integrate disparate systems without burdening users with multiple login prompts.

### 2. Core Principles

The implementation of Cross-Domain Single Sign-On is founded on several core principles that ensure its functionality and security:

| Principle | Description |
| :--- | :--- |
| **Centralized Authentication** | A single, trusted Identity Provider (IdP) is responsible for authenticating the user's credentials. This central authority issues an authentication assertion upon successful login. |
| **Trust Relationship** | A pre-established trust relationship must exist between the central IdP and all participating Service Providers (SPs) across the different domains. This is often configured through the exchange of security certificates or shared secrets. |
| **Token-Based Federation** | The user's identity and session information are propagated across domains using security tokens, such as SAML assertions, JWTs (JSON Web Tokens), or OpenID Connect ID Tokens. The token acts as a temporary passport for the user. |
| **Secure Token Exchange** | The mechanism for transferring the token between domains must be secure to prevent interception or tampering. This is typically achieved through browser redirects, back-channel communication, or by using an intermediary agent. |

### 3. Problem Statement

As organizations expand their digital footprint, they often deploy services and applications across multiple, distinct DNS domains. For example, a company might have its main website at `www.example.com`, its support portal at `support.example.net`, and a partner application at `partners.example.org`. Without a cross-domain authentication strategy, users are forced to maintain separate accounts and login sessions for each domain. This leads to a fragmented and frustrating user experience, increases the likelihood of password fatigue and weak password practices, and complicates identity and access management for administrators.

### 4. Solution

The Cross-Domain Single Sign-On pattern solves this problem by establishing a federated identity system. The solution involves a central Identity Provider (IdP) and multiple Service Providers (SPs) located in different domains. When a user attempts to access a resource on a participating SP, the following flow typically occurs:

1.  The SP, realizing the user is not authenticated, redirects the user's browser to the central IdP.
2.  The user provides their credentials (e.g., username and password) to the IdP. If the user already has an active session with the IdP, this step may be skipped.
3.  Upon successful authentication, the IdP generates a security token containing the user's identity information and session details.
4.  The IdP then redirects the user's browser back to the original SP, passing the security token along. This can be done via various mechanisms, such as an HTTP POST binding with the token in the request body.
5.  The SP receives the token, validates its authenticity by checking the IdP's signature, and establishes a local session for the user.
6.  When the user later navigates to another SP in a different domain, that SP will also redirect to the IdP. Since the user already has an active session, the IdP will immediately issue a new token for the second SP without requiring the user to log in again, thus achieving seamless cross-domain access [2].

### 5. Trade-offs and Considerations

**Pros:**
*   **Improved User Experience:** Users log in once to access multiple services, reducing friction and improving satisfaction.
*   **Centralized Security Management:** Authentication policies, password requirements, and multi-factor authentication (MFA) are managed in one place, strengthening overall security.
*   **Simplified Administration:** Reduces the overhead of managing user identities across multiple systems.

**Cons:**
*   **Single Point of Failure:** If the central IdP becomes unavailable, access to all federated applications is lost.
*   **Implementation Complexity:** Setting up the trust relationships and configuring the token exchange between the IdP and multiple SPs can be complex.
*   **Security Risk Concentration:** A compromise of the central IdP could potentially grant an attacker access to all connected systems.

### 6. Real-world Examples

*   **Google Accounts:** A user logged into Gmail (`mail.google.com`) is automatically authenticated when they visit YouTube (`youtube.com`) or Google Drive (`drive.google.com`). Google's account service acts as the central IdP for its vast ecosystem of services across different domains.
*   **Enterprise Identity Solutions:** Companies like Okta, Auth0 (now part of Okta), Ping Identity, and Microsoft (with Azure Active Directory) provide comprehensive CDSSO solutions that allow organizations to integrate their various cloud and on-premise applications, regardless of their domain.
*   **IBM Security Access Manager:** This platform provides a solution for managing user access and implementing single sign-on across different secure domains, as detailed in their documentation [3].

### 7. Cognitive Era Considerations

In the cognitive era, where AI and machine learning systems are increasingly prevalent, the Cross-Domain Single Sign-On pattern takes on new significance. AI-driven services are often distributed and specialized, running in different cloud environments or on-premise clusters. CDSSO is essential for creating a unified fabric that allows these services to securely interact and share data on behalf of a user. For example, a personalized AI assistant might need to access a user's data from a health service in one domain and a financial service in another. CDSSO provides the foundational identity layer to make such secure, cross-domain AI interactions possible, enabling federated learning and complex, personalized user journeys without compromising security.

### 8. Commons Alignment Assessment

| Commons Principle | Alignment Analysis |
| :--- | :--- |
| **Shared Resource** | The central Identity Provider (IdP) acts as a shared resource for authentication across multiple domains. However, it is often a proprietary system, which can limit its "common good" aspect unless based on open standards. |
| **Democratic Governance** | Governance is typically centralized and controlled by the organization that owns the IdP. There is little to no democratic participation from the end-users or the operators of the Service Providers. |
| **Equitable Access** | The pattern promotes equitable access by simplifying the login process for all users. By providing a single point of entry, it ensures that anyone with valid credentials can access all connected services without unnecessary barriers. |
| **Sustainability** | From a technical perspective, the pattern is sustainable as it is based on mature and widely adopted standards (SAML, OAuth, OIDC). However, reliance on a single vendor for the IdP can create lock-in and long-term cost concerns. |
| **Community Benefit** | The primary benefit is for the user community, which enjoys a more streamlined and secure experience. It also benefits the community of developers and administrators by simplifying identity management. |

### References

[1] Ping Identity. "Cross-domain single sign-on | Web Agents." [https://docs.pingidentity.com/web-agents/2025.11/user-guide/cdsso.html](https://docs.pingidentity.com/web-agents/2025.11/user-guide/cdsso.html)
[2] Oracle. "About Cross-Domain Single Sign-On." [https://docs.oracle.com/cd/E19316-01/820-3746/gipjl/index.html](https://docs.oracle.com/cd/E19316-01/820-3746/gipjl/index.html)
[3] IBM. "Cross-domain single signon." [https://www.ibm.com/docs/en/samfm/8.0.0.4?topic=solutions-cross-domain-single-sign](https://www.ibm.com/docs/en/samfm/8.0.0.4?topic=solutions-cross-domain-single-sign)
[4] Amazon Web Services. "What is SSO? - Single Sign-On Explained." [https://aws.amazon.com/what-is/sso/](https://aws.amazon.com/what-is/sso/)
