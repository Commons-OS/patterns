_# Pattern: Open Standards Adoption

## 1. Pattern Name and Number

**S062: Open Standards Adoption**

## 2. Problem

Building systems on proprietary, closed technologies creates vendor lock-in. This makes it difficult, costly, or even impossible to switch to a different provider, integrate with other systems, or innovate beyond the vendor's roadmap. The value creation system becomes dependent on the vendor's pricing, strategy, and long-term viability, reducing its sovereignty and resilience.

## 3. Context

You are choosing the foundational technologies for a new value creation system, including communication protocols, data formats, and platform APIs. You need to make architectural choices that ensure long-term flexibility, interoperability, and freedom from vendor lock-in.

## 4. Solution

**Prioritize the use of open, consensus-driven, and widely adopted standards for all core components of the system.** An open standard is a specification that is publicly available, has been developed and is maintained via a collaborative and transparent process, and can be implemented by anyone.

Key areas for open standards:
- **Data Formats**: Use formats like JSON, XML, CSV, and Parquet instead of proprietary binary formats.
- **Communication Protocols**: Use standards like HTTP, TCP/IP, SMTP, and XMPP.
- **Identity**: Use standards like OpenID Connect (OIDC), SAML, and Verifiable Credentials (VCs).
- **APIs**: Design APIs based on open specifications like OpenAPI (formerly Swagger) and GraphQL.
- **Cloud**: Use standards like the Open Container Initiative (OCI) for containers and Kubernetes for orchestration.

## 5. Rationale

Adopting open standards is a strategic architectural decision that enhances sovereignty and resilience. It:
- **Prevents Vendor Lock-In**: Enables you to switch vendors or components with minimal disruption.
- **Promotes Interoperability**: Ensures that your system can easily communicate and exchange data with other systems, fostering a richer ecosystem.
- **Increases Longevity**: Open standards are more likely to be supported over the long term than a single vendor's proprietary technology.
- **Fosters Innovation**: Allows you to leverage a wider community of developers and tools, rather than being limited to a single vendor's ecosystem.

## 6. Consequences

- **Positive**:
    - Greater architectural flexibility and freedom.
    - Reduced costs and switching barriers.
    - Larger talent pool and wider community support.
    - Future-proofs the system against vendor obsolescence.
- **Negative**:
    - Open standards can sometimes lag behind the features of cutting-edge proprietary technologies.
    - Can sometimes be less opinionated, requiring more design and integration work.
    - "Open" can be a marketing term; it's important to verify that the standard is truly governed by a neutral, non-profit body (e.g., IETF, W3C, CNCF).

## 7. Known Uses

- **The Internet**: The entire internet is built on a foundation of open standards (TCP/IP, HTTP, DNS, etc.) governed by bodies like the IETF.
- **The World Wide Web**: Built on open standards like HTML, CSS, and JavaScript, governed by the W3C.
- **Cloud Native Computing Foundation (CNCF)**: A foundation that hosts and governs critical open standards for modern cloud computing, including Kubernetes and Prometheus.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of creating open, interoperable, and collaborative ecosystems.                 |
| **2. Governance**       | 5           | A key governance principle for avoiding technological dependencies and maintaining control.           |
| **3. Economy**          | 5           | Fosters a more competitive and innovative market, reducing costs and increasing value.                |
| **4. Technology**       | 5           | A fundamental principle for building sustainable and interoperable technology.                        |
| **5. Operations**       | 4           | Can simplify operations by leveraging a wider range of standard tools and expertise.                  |
| **6. Culture**          | 5           | Fosters a culture of collaboration, openness, and community contribution.                             |
| **7. Resilience**       | 5           | Builds resilience against vendor failure, price hikes, and strategic shifts.                          |
| **Overall Score**       | **4.9**     | A foundational pattern for building sovereign, resilient, and interoperable value creation systems.    |
