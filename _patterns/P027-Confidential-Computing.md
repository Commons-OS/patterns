_# Pattern: Confidential Computing

## 1. Pattern Name and Number

**P027: Confidential Computing**

## 2. Problem

Data is typically encrypted at rest (on disk) and in transit (over the network), but it must be decrypted in memory for processing. This "in-use" phase creates a window of vulnerability where the data is exposed to the cloud provider, system administrators, or attackers who have compromised the underlying infrastructure. Organizations are hesitant to process their most sensitive data in the cloud because they do not fully trust the cloud provider's infrastructure.

## 3. Context

You need to process highly sensitive data in a public cloud environment. You need the strongest possible technical guarantee that the data will remain confidential and integral, even from the cloud provider itself, while it is being processed.

## 4. Solution

**Use Confidential Computing, a hardware-based technology that isolates data and code in a protected, encrypted memory region called a Trusted Execution Environment (TEE) or secure enclave.** The TEE ensures that the data is encrypted in memory and cannot be accessed or modified by any other part of the system, including the host operating system, the hypervisor, or the cloud provider's administrators.

The key feature of Confidential Computing is **remote attestation**, a cryptographic process that allows a user to verify that they are communicating with a genuine TEE and that it is running the expected code before they send any sensitive data to it.

## 5. Rationale

Confidential Computing provides a hardware-enforced guarantee of confidentiality and integrity for data in use. It:
- **Protects Data in Use**: Completes the data protection triad of at-rest, in-transit, and in-use encryption.
- **Enables Zero-Trust for Cloud**: Allows you to use public cloud services without having to trust the cloud provider.
- **Unlocks New Use Cases**: Enables multi-party data sharing and collaboration on sensitive data, as different parties can pool their data in a secure enclave for joint analysis without revealing their raw data to each other.

## 6. Consequences

- **Positive**:
    - The strongest level of data protection currently available in the cloud.
    - A powerful enabler for secure multi-party collaboration.
- **Negative**:
    - **Limited Availability and Performance**: TEEs are not yet available on all CPU types, and there can be a performance overhead.
    - **Complexity**: The remote attestation process and the need to manage the secure enclave add complexity to the application architecture.
    - **Ecosystem is Maturing**: The tooling and programming models for Confidential Computing are still evolving.

## 7. Known Uses

- **Microsoft Azure Confidential Computing**: Offers confidential VMs and confidential containers.
- **Google Cloud Confidential Computing**: Offers confidential VMs.
- **Confidential Computing Consortium**: A Linux Foundation project with members including Google, Microsoft, Intel, and ARM, which is working to standardize the technology.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | A visionary technology that could fundamentally change the trust model of cloud computing.            |
| **2. Governance**       | 4           | A powerful technical control for enforcing data confidentiality policies.                             |
| **3. Economy**          | 4           | Unlocks new economic value by enabling secure collaboration on sensitive data.                        |
| **4. Technology**       | 4           | A cutting-edge hardware security technology that is becoming more widely available.                   |
| **5. Operations**       | 3           | Adds significant complexity to application deployment and operations.                                 |
| **6. Culture**          | 4           | Promotes a culture of zero-trust and verifiable security.                                             |
| **7. Resilience**       | 5           | Builds extremely strong resilience against data breaches at the infrastructure level.                 |
| **Overall Score**       | **4.1**     | A powerful and rapidly maturing pattern that is set to become a fundamental part of the cloud security landscape. |
