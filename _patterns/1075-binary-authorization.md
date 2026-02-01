---
id: pat_29e9dbfe82d9450c9ba1d7d7
page_url: https://commons-os.github.io/patterns/1075-binary-authorization/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/1075-binary-authorization.md
slug: 1075-binary-authorization
title: Binary Authorization
aliases: []
version: 1.0
created: 2026-02-01T12:17:06Z
modified: 2026-02-01T12:17:06Z
tags:
  universality: universal
  domain: security
  category: [pattern]
  era: [cognitive]
  origin: [commons-os]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [manus-ai, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

Binary Authorization is a pattern for building resilient value creation systems.

**Problem:** In a complex CI/CD pipeline, there are many points where a malicious actor could compromise the build process to inject unauthorized code. For example, an attacker could compromise a developer's machine, the source code repository, or the build server itself. You need a final, strong guarantee that only code that has passed all the required security checks is allowed to be deployed into production.

**Context:** You are using a container-based workflow (e.g., with Kubernetes) and a CI/CD pipeline to build and deploy your applications. You need a strong, policy-based enforcement mechanism to ensure the integrity of the software that is deployed into your production environment.

### 2. Core Principles

**Implement Binary Authorization, a deploy-time security control that ensures only trusted container images are deployed.** It works by enforcing a policy that requires container images to be signed by trusted authorities before they can be deployed.

The process is as follows:
1.  **Code Signing**: As a container image passes through the CI/CD pipeline (e.g., after passing vulnerability scans, after being approved by QA), it is cryptographically signed by the relevant authority.
2.  **Policy Definition**: You define a policy that specifies which authorities (or "attestors") must have signed an image before it can be deployed.
3.  **Policy Enforcement**: A policy enforcer (e.g., an admission controller in Kubernetes) intercepts all deployment requests. It checks the signatures on the container image against the policy.
4.  **Deployment Decision**: If the image has all the required signatures, the deployment is allowed. If not, the deployment is blocked.

### 3. Rationale

Binary Authorization provides a powerful, last-line-of-defense for your software supply chain. It:
- **Provides a Strong Integrity Guarantee**: Ensures that only code that has passed all your required checks can run in production.
- **Is Policy-Driven**: Allows you to define and enforce your software supply chain policies as code.
- **Reduces the Risk of Unauthorized Code**: Protects against a wide range of attacks that aim to inject malicious code into the supply chain.

### 4. Consequences

- **Positive**:
    - A very strong guarantee of software supply chain integrity.
    - A clear and auditable enforcement of your deployment policies.
- **Negative**:
    - **Adds Complexity**: Requires a public key infrastructure (PKI) to manage the signing keys and a policy engine to manage the authorization policies.
    - **Can be difficult to set up**: Requires a mature CI/CD pipeline and a container orchestration platform like Kubernetes.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **Google Cloud Binary Authorization**: A managed service that brings binary authorization to Google Kubernetes Engine (GKE).
- **In-toto**: An open-source framework for defining and verifying the integrity of a software supply chain, which can be used to implement binary authorization.

