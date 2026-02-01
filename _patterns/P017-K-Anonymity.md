_# Pattern: K-Anonymity

## 1. Pattern Name and Number

**P017: K-Anonymity**

## 2. Problem

Simply removing direct identifiers (like names and social security numbers) from a dataset is often not enough to protect individual privacy. An attacker can still re-identify individuals by linking the remaining quasi-identifiers (like zip code, birth date, and gender) with other publicly available datasets. For example, if only one person in a public voter registration list matches the zip code, birth date, and gender in your "anonymized" dataset, their identity is revealed.

## 3. Context

You want to release a dataset for research or public use that contains sensitive information. You have already removed direct identifiers, but you need to provide a stronger, more formal guarantee against re-identification attacks that use quasi-identifiers.

## 4. Solution

**Apply K-Anonymity, a technique that ensures each individual record in a dataset is indistinguishable from at least k-1 other records with respect to a set of quasi-identifiers.** This is achieved by generalizing or suppressing the data.

- **Generalization**: Replacing specific values with more general ones (e.g., replacing a specific birth date with just the birth year, or a specific zip code with a broader region).
- **Suppression**: Hiding certain values altogether (e.g., replacing a value with an asterisk).

The goal is to modify the dataset so that for any combination of quasi-identifier values, there are at least 'k' records that share that combination. This makes it impossible for an attacker to re-identify an individual with a probability greater than 1/k.

## 5. Rationale

K-Anonymity provides a formal, measurable guarantee against re-identification by linking. It:
- **Protects Against Linking Attacks**: It is specifically designed to thwart attempts to re-identify individuals by combining the dataset with other data sources.
- **Provides a Tunable Privacy Level**: The value of 'k' can be chosen to provide the desired level of privacy. A higher 'k' means stronger privacy but also more data distortion.
- **Is a Well-Understood Technique**: It is one of the earliest and most well-studied formal privacy models.

## 6. Consequences

- **Positive**:
    - Provides a much stronger privacy guarantee than simple de-identification.
    - Allows for the safe release of valuable datasets for research and analysis.
- **Negative**:
    - The process of generalization and suppression reduces the quality and utility of the data. There is a direct trade-off between the strength of privacy (k) and the usefulness of the data.
    - It does not protect against all types of privacy attacks. For example, if all 'k' individuals in a group have the same sensitive attribute (e.g., the same disease), an attacker still learns that information about everyone in the group (this is known as a homogeneity attack).
    - Can be complex to implement optimally.

## 7. Known Uses

- **Healthcare**: Used to anonymize patient data before it is released for clinical research.
- **Social Science**: Used by researchers to share survey data without revealing the identities of respondents.
- **Data Anonymization Tools**: Many data anonymization tools, such as ARX, provide features to achieve k-anonymity.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of enabling data sharing while protecting privacy.                             |
| **2. Governance**       | 4           | A formal governance model for managing re-identification risk in public datasets.                     |
| **3. Economy**          | 4           | Unlocks economic value by enabling the release of data for research and innovation.                   |
| **4. Technology**       | 3           | A well-understood but sometimes complex data transformation technique.                                |
| **5. Operations**       | 3           | Requires careful data analysis to apply generalization and suppression without destroying data utility. |
| **6. Culture**          | 4           | Promotes a culture of awareness around the risks of re-identification.                                |
| **7. Resilience**       | 3           | Builds resilience against linking attacks, but is vulnerable to other forms of privacy attacks.       |
| **Overall Score**       | **3.6**     | A classic and important pattern for data release, but it must be used with an understanding of its limitations. |
