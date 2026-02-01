_# Pattern: TEE-Based Inference

## 1. Pattern Name and Number

**A114: TEE-Based Inference**

## 2. Problem

When using a third-party cloud service to run AI inference on sensitive data (e.g., analyzing medical images, processing financial documents), the data is exposed to the cloud provider. Even if the data is encrypted in transit and at rest, it must be decrypted in memory for the AI model to process it. This creates a window of vulnerability where the cloud provider or an attacker who compromises the server could access the sensitive data.

## 3. Context

You need to use a cloud-based AI service for inference on highly sensitive data. You need the strongest possible technical guarantee that the data will remain confidential, even from the cloud provider itself, while it is being processed.

## 4. Solution

**Use a Trusted Execution Environment (TEE) to run the AI inference.** A TEE (also known as a secure enclave) is a secure area inside a main processor that is isolated from the rest of the system. It guarantees the confidentiality and integrity of the code and data that run within it.

The process works as follows:
1.  **Attestation**: The client first verifies that it is talking to a genuine TEE running the expected AI inference code. This is done through a cryptographic process called remote attestation.
2.  **Secure Channel**: The client establishes a secure, encrypted channel directly with the TEE.
3.  **Inference**: The client sends the encrypted sensitive data through the secure channel to the TEE. The TEE decrypts the data inside the enclave, runs the AI model on it, and encrypts the result.
4.  **Result**: The TEE sends the encrypted result back to the client. The data is never exposed in plaintext outside the isolated enclave.

## 5. Rationale

TEE-based inference provides a hardware-level guarantee of confidentiality for data in use. It:
- **Protects Data in Use**: Solves the final piece of the puzzle, protecting data not just at rest and in transit, but also during processing.
- **Provides Verifiable Security**: The remote attestation process provides a cryptographic proof that the environment is secure.
- **Enables Secure AI Outsourcing**: Allows organizations to use public cloud AI services for even their most sensitive data.

## 6. Consequences

- **Positive**:
    - One of the strongest forms of protection for data confidentiality in the cloud.
    - Enables new use cases for AI in highly regulated industries.
- **Negative**:
    - **Limited Availability**: TEEs are not available on all types of cloud instances, and support for specialized AI hardware (like GPUs) is still emerging.
    - **Performance Overhead**: There can be a performance overhead associated with running computations inside a TEE.
    - **Complexity**: The remote attestation and secure channel setup add complexity to the system.

## 7. Known Uses

- **Microsoft Azure Confidential Computing**: Azure offers confidential VMs that use AMD SEV-SNP technology to create TEEs.
- **Google Cloud Confidential Computing**: Google Cloud offers confidential VMs using AMD SEV.
- **Signal**: The Signal messaging app uses TEEs to privately manage its contact discovery process, so that Signal doesn't have to store a plaintext graph of its users' contacts.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of a world where data can be processed with absolute confidentiality.          |
| **2. Governance**       | 4           | A powerful technical control for enforcing data confidentiality policies.                             |
| **3. Economy**          | 4           | Unlocks new economic value by enabling secure AI on sensitive data.                                   |
| **4. Technology**       | 4           | A cutting-edge hardware-based security technology that is becoming more widely available.             |
| **5. Operations**       | 3           | Requires specialized infrastructure and adds operational complexity.                                  |
| **6. Culture**          | 4           | Promotes a culture of zero-trust, even for the cloud provider.                                        |
| **7. Resilience**       | 5           | Builds extremely strong resilience against data breaches at the cloud provider level.                 |
| **Overall Score**       | **4.1**     | A powerful and emerging pattern for achieving the highest level of data confidentiality in the cloud. |
