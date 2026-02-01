_# Pattern: Privacy-Preserving Record Linkage

## 1. Pattern Name and Number

**P030: Privacy-Preserving Record Linkage**

## 2. Problem

Two or more parties have datasets that contain information about the same individuals, but they cannot share the data with each other due to privacy regulations or commercial sensitivities. They need to link the records for the same individual across their datasets to perform a joint analysis, but they need to do so without revealing the identities of the individuals in their datasets.

## 3. Context

You are working with one or more other organizations to perform a data analysis project. You need to link your datasets together, but you are not allowed to share the raw data. For example, a hospital and a university may want to link patient health records with student academic records to study the impact of health on academic performance.

## 4. Solution

**Use Privacy-Preserving Record Linkage (PPRL), a set of techniques that allows two or more parties to identify records that correspond to the same individual in their respective datasets, without revealing any personally identifiable information (PII).**

A common approach is to use **cryptographic hashing**. The parties agree on a common set of identifiers (like name, date of birth, address) and a common cryptographic hash function. Each party then hashes the identifiers for each of their records and sends the resulting hashes to a trusted third party or to each other. The parties can then identify the matching records by comparing the hashes.

More advanced techniques use **Bloom filters** or **Secure Multi-Party Computation (P019)** to perform the linkage without a trusted third party and with even stronger privacy guarantees.

## 5. Rationale

PPRL enables valuable data linkage projects that would otherwise be impossible. It:
- **Protects Privacy**: Allows for data linkage without sharing PII.
- **Enables Collaboration**: Allows different organizations to collaborate on data analysis projects.
- **Unlocks New Insights**: Can lead to new and important insights that can only be gained by linking different datasets.

## 6. Consequences

- **Positive**:
    - The ability to perform data linkage in a privacy-preserving way.
    - A powerful enabler of collaborative research and data analysis.
- **Negative**:
    - **Accuracy**: There is often a trade-off between the accuracy of the linkage and the strength of the privacy guarantee. Some techniques can produce false positives (linking records that are not for the same person) or false negatives (failing to link records that are for the same person).
    - **Complexity**: These are advanced techniques that require specialized expertise.

## 7. Known Uses

- **Medical Research**: Used extensively to link patient records from different hospitals and research institutions.
- **Government**: Used by government agencies to link administrative datasets for statistical purposes.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of a data economy that is both collaborative and privacy-respecting.           |
| **2. Governance**       | 4           | A powerful governance control for managing the privacy risks of data linkage.                         |
| **3. Economy**          | 4           | Unlocks the economic value of linked data.                                                            |
| **4. Technology**       | 4           | A specialized but important area of privacy-enhancing technology.                                     |
| **5. Operations**       | 3           | The operational complexity is high.                                                                   |
| **6. Culture**          | 4           | Promotes a culture of collaborative, privacy-conscious data analysis.                                 |
| **7. Resilience**       | 4           | Builds legal and social resilience by enabling data linkage in a compliant and trustworthy way.       |
| **Overall Score**       | **3.9**     | A powerful and important pattern for any organization that needs to link sensitive datasets.           |
