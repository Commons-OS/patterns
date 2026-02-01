_# Pattern: L-Diversity

## 1. Pattern Name and Number

**P018: L-Diversity**

## 2. Problem

K-Anonymity (P017) protects against re-identification by ensuring that each individual is part of a group of at least 'k' indistinguishable records. However, it is vulnerable to homogeneity attacks. If all 'k' individuals in a group share the same sensitive attribute (e.g., they all have the same disease), an attacker who knows that a person is in that group can infer their sensitive information, even without knowing their exact record.

## 3. Context

You have already applied K-Anonymity to a dataset, but you recognize that it is not sufficient to protect against attribute disclosure when the sensitive values within an equivalence class (a group of k-indistinguishable records) are not diverse.

## 4. Solution

**Apply L-Diversity, an extension of K-Anonymity that requires each equivalence class to have at least 'l' well-represented values for the sensitive attribute.** This ensures that even if an attacker can identify the equivalence class for an individual, they cannot infer the sensitive value with high confidence.

There are several interpretations of "well-represented":
- **Distinct L-Diversity**: Ensures there are at least 'l' distinct values for the sensitive attribute in each equivalence class.
- **Entropy L-Diversity**: Ensures that the distribution of sensitive values in each equivalence class has a certain amount of entropy, preventing one value from dominating.

Like K-Anonymity, L-Diversity is achieved through generalization and suppression of the quasi-identifiers.

## 5. Rationale

L-Diversity directly addresses the weaknesses of K-Anonymity. It:
- **Protects Against Homogeneity Attacks**: Prevents the inference of sensitive attributes by ensuring diversity within each equivalence class.
- **Provides a Stronger Privacy Guarantee**: Reduces the probability of correctly guessing an individual's sensitive attribute.
- **Builds on K-Anonymity**: It is a natural and necessary extension for any dataset where attribute disclosure is a concern.

## 6. Consequences

- **Positive**:
    - Provides a stronger privacy guarantee than K-Anonymity alone.
    - Protects against attribute disclosure attacks.
- **Negative**:
    - It is more difficult and costly to achieve than K-Anonymity, often requiring more data generalization or suppression, which further reduces data utility.
    - It is still vulnerable to some attacks, such as skewness attacks (if some sensitive values are much more common than others) and similarity attacks (if all the sensitive values in a group are semantically similar).
    - Can be complex to implement.

## 7. Known Uses

- **Healthcare Data Release**: Used in conjunction with K-Anonymity to protect patient privacy in datasets released for research.
- **Data Anonymization Tools**: Advanced data anonymization tools often provide options to enforce L-Diversity alongside K-Anonymity.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of responsible data sharing.                                                   |
| **2. Governance**       | 4           | A more advanced governance model for managing attribute disclosure risk.                              |
| **3. Economy**          | 3           | Can reduce the economic value of the data due to the required information loss.                       |
| **4. Technology**       | 3           | A more complex data transformation technique than K-Anonymity.                                        |
| **5. Operations**       | 3           | Requires more sophisticated data analysis to implement effectively.                                   |
| **6. Culture**          | 4           | Promotes a deeper understanding of the subtleties of data privacy.                                    |
| **7. Resilience**       | 3           | Builds resilience against homogeneity attacks, but has its own vulnerabilities.                       |
| **Overall Score**       | **3.4**     | An important extension to K-Anonymity, but it highlights the inherent trade-off between privacy and data utility. |
