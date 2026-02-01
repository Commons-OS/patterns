---
id: pat_019c19b235107b7393e79957ea
page_url: https://commons-os.github.io/patterns/1095-slsa-framework/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/1095-slsa-framework.md
slug: 1095-slsa-framework
title: "SLSA Framework"
aliases: []
version: "1.0"
created: "2026-02-01T14:53:55Z"
modified: "2026-02-01T14:53:55Z"

tags:
  universality: universal
  domain: security
  category: [practice]
  era: [cognitive]
  origin: [Commons OS]
  status: draft
  commons_alignment: 3

commons_domain: security

generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []

contributors: [commons-os]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

The Supply-chain Levels for Software Artifacts (SLSA) is a security framework designed to protect the integrity of the software supply chain. It provides a checklist of standards and controls to prevent tampering, improve integrity, and secure software packages and infrastructure. The core problem SLSA addresses is the increasing risk of software supply chain attacks, where malicious actors inject vulnerabilities into software by compromising the development, build, or distribution processes. These attacks can have widespread consequences, affecting a vast number of users and organizations who depend on the compromised software.

The historical context for SLSA's creation is rooted in a series of high-profile supply chain attacks that highlighted the vulnerabilities in modern software development practices. Developed in response to these threats, SLSA was proposed by Google in collaboration with the Open Source Security Foundation (OpenSSF) in 2021. It is inspired by Google's internal best practices for ensuring the integrity of its own software production. The framework is designed to be a common language for discussing and improving supply chain security, providing a clear path for incremental adoption and improvement.

For organizations and commons-based projects, SLSA is critically important because it provides a structured approach to building trust and resilience in the software they produce and consume. By adopting SLSA, organizations can systematically reduce their exposure to supply chain threats, protect their users, and demonstrate a commitment to security. For the broader open-source ecosystem, SLSA offers a way to harden the shared infrastructure that so many depend on, fostering a more secure and trustworthy environment for collaboration and innovation.

### 2. Core Principles

1.  **Source Integrity**: This principle emphasizes that the source code used to create a software artifact must be verifiable and protected from unauthorized modifications. It involves using a version control system that maintains a detailed and immutable history of all changes, and implementing access controls to ensure that only authorized individuals can make changes to the codebase.

2.  **Build Integrity**: The build process itself must be secure and reproducible. This means that the build should be executed on a trusted and isolated platform, following a defined and scripted process. The goal is to ensure that the build process is not tampered with and that it consistently produces the same artifact from the same source code and dependencies.

3.  **Verifiable Provenance**: SLSA mandates the generation of provenance, which is authenticated metadata about how a software artifact was produced. This provenance includes details about the source code, dependencies, build process, and the tools used. It must be cryptographically signed to ensure its authenticity and integrity, allowing consumers to verify the artifact's origins and build process.

4.  **Common Language for Security**: SLSA establishes a common vocabulary and a set of four increasing levels of assurance (SLSA 1-4). This common language allows different organizations and projects to communicate clearly about their security posture and requirements, making it easier to assess the security of third-party software and to set consistent security goals across the industry.

5.  **Incremental and Adoptable**: The framework is designed to be adopted incrementally. The different SLSA levels provide a clear roadmap for organizations to gradually improve their supply chain security. This approach allows organizations to start with basic security measures and progressively move towards a more mature and resilient security posture without requiring a massive upfront investment.

### 3. Key Practices

1.  **Use Version Control**: All source code and configuration must be stored in a version control system (VCS) like Git. The VCS must maintain a complete and auditable history of all changes, which is essential for source integrity and for generating accurate provenance.

2.  **Automate Builds**: Builds should be fully automated using a CI/CD system. This eliminates the need for manual steps, which can be a source of errors and vulnerabilities. The build script should be version controlled alongside the source code.

3.  **Generate Provenance**: The build process must generate provenance that describes how the artifact was built. This provenance should be in a standard format, such as the in-toto attestation framework, and should be cryptographically signed by the build service.

4.  **Verify Provenance**: Consumers of an artifact should verify its provenance to ensure that it was built from the expected source code and by a trusted build process. This verification step is crucial for preventing the use of tampered or malicious artifacts.

5.  **Use Immutable Artifact References**: When referencing software artifacts, use immutable references that include a cryptographic hash (e.g., a Docker image digest). This ensures that you are always using the exact version of the artifact that you expect, and prevents attacks where a mutable tag is moved to point to a malicious artifact.

6.  **Isolate Build Environments**: Build environments should be ephemeral and isolated from each other. This prevents cross-contamination between builds and reduces the risk of a compromised build environment affecting other builds.

7.  **Harden Build Platforms**: The build platform itself must be hardened against attacks. This includes securing the build service's credentials, implementing access controls, and regularly auditing the platform for vulnerabilities.

### 4. Implementation

Implementing the SLSA framework is a journey of incremental improvement. A typical step-by-step approach starts with achieving SLSA Level 1 and progressively moving to higher levels. The first step is to automate the build process using a CI/CD system and to ensure that the build generates some level of provenance. Many modern CI/CD platforms, such as Google Cloud Build and GitHub Actions, have built-in support for generating basic provenance, making it relatively easy to achieve SLSA 1.

As an organization matures, it can move towards higher SLSA levels by implementing more stringent controls. To reach SLSA 2, the build process must be fully automated and the provenance must be authenticated. SLSA 3 requires the build platform to be hardened and the source and build processes to be more tightly controlled. Finally, SLSA 4, the highest level, requires a two-person review of all changes and a hermetic, reproducible build process. Key considerations during implementation include choosing the right tools, integrating them into existing workflows, and training developers on the new processes. It is also important to have a clear understanding of the threat model and to prioritize the implementation of controls that address the most significant risks.

Several tools and frameworks can help with the implementation of SLSA. The in-toto framework provides a standard for creating and verifying supply chain attestations. The Sigstore project offers tools for signing and verifying software artifacts. Many CI/CD platforms are also adding features to support SLSA, such as built-in provenance generation and verification. Success in implementing SLSA can be measured by the SLSA level achieved, the percentage of software artifacts that are built in compliance with SLSA, and a reduction in the number of supply chain-related security incidents.

### 5. 7 Pillars Assessment

| Pillar | Score (1-5) | Rationale |
|---|---|---|
| Purpose | 5 | The purpose of SLSA is exceptionally clear: to improve the security and integrity of the software supply chain. It directly addresses a well-defined and critical problem with a focused set of goals and a clear path to achievement. |
| Governance | 4 | SLSA is governed by the OpenSSF, a neutral and respected body in the open-source community. This provides a strong governance model that fosters collaboration and ensures the framework remains vendor-neutral and community-driven. |
| Culture | 3 | Adopting SLSA requires a cultural shift towards a security-first mindset in software development. This can be a challenge in organizations where speed of delivery is prioritized over security, and it requires a concerted effort to build awareness and provide training. |
| Incentives | 3 | The primary incentive for adopting SLSA is risk reduction, which can be difficult to quantify and may not be a strong enough motivator for all organizations. However, as supply chain attacks become more common, the incentive to adopt frameworks like SLSA is increasing. |
| Knowledge | 3 | Implementing SLSA requires specialized knowledge of supply chain security concepts and tools. While the framework is well-documented, there is a learning curve involved, and organizations may need to invest in training or hire experts to guide the implementation. |
| Technology | 4 | The technology to implement SLSA is rapidly evolving and improving. There are a growing number of open-source tools and commercial products that support SLSA, making it increasingly accessible to a wider range of organizations. |
| Resilience | 5 | SLSA is fundamentally about building resilience into the software supply chain. By implementing the controls and practices it recommends, organizations can significantly reduce their vulnerability to supply chain attacks and improve their ability to recover from them. |
| **Overall** | **3.9** | **SLSA is a well-designed and much-needed framework with a strong purpose and governance model, but its adoption requires a cultural shift and specialized knowledge.** |

### 6. When to Use

*   When developing or using software that is critical to your organization's operations.
*   When you are part of a regulated industry that has strict requirements for software security and integrity.
*   When you are developing open-source software that is widely used by the community.
*   When you need to provide strong security assurances to your customers or users.
*   When you want to reduce the risk of your software being compromised by a supply chain attack.
*   When you are looking for a structured and incremental approach to improving your software supply chain security.

### 7. Anti-Patterns & Gotchas

*   **SLSA-washing**: Claiming a higher SLSA level than is actually achieved. This can create a false sense of security and undermine the value of the framework.
*   **Tool-centric approach**: Focusing solely on implementing tools without understanding the underlying principles of supply chain security. This can lead to a fragmented and ineffective implementation.
*   **Ignoring the human element**: Failing to address the risk of insider threats or social engineering attacks. SLSA is a technical framework, but it needs to be complemented by strong security policies and training for personnel.
*   **Treating SLSA as a checklist**: Viewing SLSA as a one-time compliance exercise rather than an ongoing process of improvement. The threat landscape is constantly evolving, and so should your security practices.
*   **Boiling the ocean**: Trying to implement all of SLSA at once. The incremental nature of the framework is one of its key strengths, and organizations should take a phased approach to adoption.
*   **Lack of executive buy-in**: Without support from leadership, it can be difficult to secure the resources and make the cultural changes necessary to successfully implement SLSA.

### 8. References

1.  [SLSA Official Website](https://slsa.dev/)
2.  [Google Cloud Blog: Introducing SLSA](https://cloud.google.com/blog/products/application-development/google-introduces-slsa-framework)
3.  [SLSA GitHub Repository](https://github.com/slsa-framework/slsa)
4.  [Open Source Security Foundation (OpenSSF)](https://openssf.org/)
