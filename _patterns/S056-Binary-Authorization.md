_# Pattern: Binary Authorization

## 1. Pattern Name and Number

**S056: Binary Authorization**

## 2. Problem

In a complex CI/CD pipeline, there are many points where a malicious actor could compromise the build process to inject unauthorized code. For example, an attacker could compromise a developer's machine, the source code repository, or the build server itself. You need a final, strong guarantee that only code that has passed all the required security checks is allowed to be deployed into production.

## 3. Context

You are using a container-based workflow (e.g., with Kubernetes) and a CI/CD pipeline to build and deploy your applications. You need a strong, policy-based enforcement mechanism to ensure the integrity of the software that is deployed into your production environment.

## 4. Solution

**Implement Binary Authorization, a deploy-time security control that ensures only trusted container images are deployed.** It works by enforcing a policy that requires container images to be signed by trusted authorities before they can be deployed.

The process is as follows:
1.  **Code Signing**: As a container image passes through the CI/CD pipeline (e.g., after passing vulnerability scans, after being approved by QA), it is cryptographically signed by the relevant authority.
2.  **Policy Definition**: You define a policy that specifies which authorities (or "attestors") must have signed an image before it can be deployed.
3.  **Policy Enforcement**: A policy enforcer (e.g., an admission controller in Kubernetes) intercepts all deployment requests. It checks the signatures on the container image against the policy.
4.  **Deployment Decision**: If the image has all the required signatures, the deployment is allowed. If not, the deployment is blocked.

## 5. Rationale

Binary Authorization provides a powerful, last-line-of-defense for your software supply chain. It:
- **Provides a Strong Integrity Guarantee**: Ensures that only code that has passed all your required checks can run in production.
- **Is Policy-Driven**: Allows you to define and enforce your software supply chain policies as code.
- **Reduces the Risk of Unauthorized Code**: Protects against a wide range of attacks that aim to inject malicious code into the supply chain.

## 6. Consequences

- **Positive**:
    - A very strong guarantee of software supply chain integrity.
    - A clear and auditable enforcement of your deployment policies.
- **Negative**:
    - **Adds Complexity**: Requires a public key infrastructure (PKI) to manage the signing keys and a policy engine to manage the authorization policies.
    - **Can be difficult to set up**: Requires a mature CI/CD pipeline and a container orchestration platform like Kubernetes.

## 7. Known Uses

- **Google Cloud Binary Authorization**: A managed service that brings binary authorization to Google Kubernetes Engine (GKE).
- **In-toto**: An open-source framework for defining and verifying the integrity of a software supply chain, which can be used to implement binary authorization.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of a secure and verifiable software supply chain.                              |
| **2. Governance**       | 5           | A powerful, policy-driven governance control for software deployment.                                 |
| **3. Economy**          | 4           | Prevents costly security incidents caused by the deployment of unauthorized code.                     |
| **4. Technology**       | 4           | A cutting-edge security technology for containerized environments.                                    |
| **5. Operations**       | 3           | Adds significant complexity to the CI/CD and Kubernetes operations.                                   |
| **6. Culture**          | 4           | Fosters a culture of strong security guarantees and policy-as-code.                                   |
| **7. Resilience**       | 5           | Builds extremely strong resilience against software supply chain attacks.                             |
| **Overall Score**       | **4.1**     | A powerful and increasingly important pattern for securing the software supply chain in a containerized world. |
