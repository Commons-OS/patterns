_# Pattern: Data Masking

## 1. Pattern Name and Number

**P023: Data Masking**

## 2. Problem

Developers, testers, and data analysts often need access to a realistic dataset to do their work. However, using real production data in non-production environments (like development, testing, or staging) creates a massive security and privacy risk. A copy of the production database is a high-value target for attackers, and exposing sensitive personal data to a large number of internal employees increases the risk of insider threats and accidental leaks.

## 3. Context

You need to provide a realistic and functional dataset for use in non-production environments. You need to protect the sensitive data in that dataset while preserving its realism and usability for development and testing.

## 4. Solution

**Use Data Masking (also known as data obfuscation) to create a copy of a production dataset where the sensitive data has been replaced with realistic but fake data.** Unlike anonymization, which just removes data, or synthetic data, which creates a whole new dataset, data masking works by selectively overwriting the sensitive fields in an existing dataset.

Common masking techniques include:
- **Substitution**: Replacing a value with a new one from a pre-defined dictionary (e.g., replacing all real names with a list of fake names).
- **Shuffling**: Randomly shuffling the values in a column (e.g., shuffling all the email addresses so they are no longer associated with the correct user).
- **Redaction**: Replacing characters with a generic character (e.g., `XXX-XX-1234`).
- **Encryption or Hashing**: Replacing a value with an encrypted or hashed version.

## 5. Rationale

Data masking provides a practical way to create high-quality test data. It:
- **Protects Sensitive Data**: Prevents sensitive production data from being exposed in less secure non-production environments.
- **Preserves Realism**: The structure, format, and statistical properties of the data remain largely intact, making it highly useful for development and testing.
- **Is a Mature Technology**: There are many commercial and open-source tools available for data masking.

## 6. Consequences

- **Positive**:
    - A significant reduction in the risk of data breaches from non-production environments.
    - The ability to provide high-quality, realistic data to development and testing teams.
- **Negative**:
    - **Can be complex to implement**: A good data masking strategy requires a careful understanding of the data model and the relationships between different data fields.
    - **May not preserve all statistical properties**: Some masking techniques can alter the statistical properties of the data, which could be an issue for some types of data analysis.

## 7. Known Uses

- **It is a standard practice** in most large organizations for creating test and development data.
- **Database vendors** (like Oracle and Microsoft) and specialized data masking companies (like Delphix and Informatica) offer sophisticated data masking tools.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 3           | A practical pattern for data protection in the development lifecycle.                                 |
| **2. Governance**       | 4           | A key governance control for managing the risk of non-production data.                                |
| **3. Economy**          | 4           | Prevents costly data breaches from development and testing environments.                              |
| **4. Technology**       | 4           | A mature and widely available data security technology.                                               |
| **5. Operations**       | 4           | A standard practice for database administration and DevOps teams.                                     |
| **6. Culture**          | 4           | Promotes a culture of data protection throughout the development lifecycle.                           |
| **7. Resilience**       | 4           | Builds resilience by reducing the attack surface of the organization.                                 |
| **Overall Score**       | **3.9**     | An essential and standard pattern for protecting sensitive data in non-production environments.        |
