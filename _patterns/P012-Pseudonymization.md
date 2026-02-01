_# Pattern: Pseudonymization

## 1. Pattern Name and Number

**P012: Pseudonymization**

## 2. Problem

You need to process or share a dataset for secondary purposes, like analytics or research. While you want to protect the privacy of individuals, you also need to be able to link different records belonging to the same person over time. Simple anonymization (P004), which completely removes identifiers, breaks this ability to link records.

## 3. Context

You are processing personal data and need to reduce its privacy risk while retaining the ability to perform longitudinal analysis or link records from different sources that relate to the same individual. You need a middle ground between fully identifiable data and fully anonymized data.

## 4. Solution

**Apply Pseudonymization, the process of replacing direct identifiers (like name, email, or social security number) with a consistent but non-identifying pseudonym or token.** The key is that the same pseudonym is used for the same individual across different datasets or time points, allowing records to be linked without revealing the individual's real-world identity.

A critical aspect of pseudonymization is that the mapping between the real identifiers and the pseudonyms must be stored securely and separately, with highly restricted access. This mapping allows for re-identification if and only if it is absolutely necessary and authorized.

## 5. Rationale

Pseudonymization provides a practical balance between data utility and privacy. It:
- **Reduces Privacy Risk**: By removing direct identifiers from the main dataset, it significantly reduces the risk of a data breach exposing real-world identities.
- **Maintains Data Utility**: It allows for the linking of records, which is essential for many types of data analysis.
- **Is a Recommended Security Safeguard**: GDPR and other regulations explicitly recognize pseudonymization as a key security measure for protecting personal data.

## 6. Consequences

- **Positive**:
    - A strong safeguard that enables data processing for secondary purposes.
    - Reduces the scope of data protection obligations in some cases (pseudonymized data is still personal data under GDPR, but it is considered lower risk).
- **Negative**:
    - It is not full anonymization. The data can still be re-identified if the pseudonym-to-identifier mapping is compromised.
    - The security of the entire system depends on the secure storage and management of the mapping table.

## 7. Known Uses

- **Clinical Trials**: Patient data is often pseudonymized to allow researchers to analyze the data without knowing the patients' identities.
- **Web Analytics**: User IDs are often replaced with pseudonyms to track user behavior over time without storing personally identifiable information.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of enabling data analysis while respecting privacy.                            |
| **2. Governance**       | 4           | A key governance control for managing the privacy of data used for secondary purposes.                |
| **3. Economy**          | 4           | Unlocks the economic value of data for analytics and research.                                        |
| **4. Technology**       | 4           | A standard and well-understood data protection technique.                                             |
| **5. Operations**       | 4           | Requires operational discipline to ensure the secure management of the pseudonym mapping.             |
| **6. Culture**          | 4           | Promotes a culture of data protection by design.                                                      |
| **7. Resilience**       | 4           | Builds resilience against data breaches by reducing the impact of a compromise of the main dataset.   |
| **Overall Score**       | **4.0**     | A fundamental and widely used pattern for balancing data utility and privacy.                          |
