_# Pattern: Right to Erasure

## 1. Pattern Name and Number

**P014: Right to Erasure ('Right to be Forgotten')**

## 2. Problem

Personal data is often kept by organizations indefinitely, even long after the original purpose for its collection has expired. This increases the risk of the data being breached, misused, or becoming inaccurate. Users have little control over their digital footprint and find it difficult to have their old, irrelevant, or sensitive data removed from systems.

## 3. Context

You are an organization that collects and processes personal data. You need to provide a mechanism for users to request the deletion of their data and to ensure that this deletion is carried out completely and securely, in compliance with legal obligations like the GDPR.

## 4. Solution

**Implement a robust process for handling Right to Erasure requests.** This involves both a user-facing interface and a comprehensive backend process.

1.  **Request Intake**: Provide a clear and accessible way for users to submit a deletion request (e.g., through their account settings or a dedicated privacy portal).
2.  **Identity Verification**: Securely verify the identity of the person making the request to prevent malicious or fraudulent deletions.
3.  **Request Validation**: Determine if the request is valid and if there are any legal grounds for retaining the data (e.g., for compliance with a legal obligation, for the establishment or defense of legal claims).
4.  **Data Deletion**: If the request is valid, permanently and securely delete the user's personal data from all systems, including production databases, logs, backups, and third-party services.
5.  **Confirmation**: Inform the user that their request has been completed.

This process must be well-documented and auditable.

## 5. Rationale

The Right to Erasure is a fundamental data protection right that gives individuals control over their personal information. Implementing this pattern:
- **Empowers Users**: Gives individuals agency over their digital footprint.
- **Reduces Risk**: Minimizes the amount of data your organization holds, thereby reducing the attack surface and the potential impact of a data breach (in line with Data Minimization, P001).
- **Ensures Compliance**: It is a legal requirement under GDPR (Article 17) and other data protection laws.
- **Builds Trust**: Demonstrates respect for user privacy and a commitment to responsible data stewardship.

## 6. Consequences

- **Positive**:
    - Increased user trust.
    - Compliance with fundamental data protection principles.
    - A reduced data footprint for the organization.
- **Negative**:
    - **Technical Complexity**: Completely and permanently deleting all instances of a user's data from complex, distributed systems (especially backups and logs) can be extremely challenging.
    - **Operational Burden**: Requires a well-defined and resourced operational process to handle requests in a timely manner.
    - **Potential for Abuse**: The process can be abused by malicious actors to harass others or to try to erase legitimate records.

## 7. Known Uses

- **All major online platforms** (e.g., Google, Facebook, Twitter) provide mechanisms for users to delete their accounts and associated data.
- It is a standard feature of any service that is compliant with GDPR.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of user empowerment and data agency.                                           |
| **2. Governance**       | 4           | A critical governance control for ensuring individual rights and data lifecycle management.           |
| **3. Economy**          | 3           | Can be costly to implement, but it is a necessary cost of doing business in a data-driven economy.    |
| **4. Technology**       | 3           | The technical implementation of complete data deletion can be very difficult.                         |
| **5. Operations**       | 3           | Requires a dedicated operational process.                                                             |
| **6. Culture**          | 5           | Fosters a culture that respects the user's right to control their own digital existence.              |
| **7. Resilience**       | 4           | Builds legal and social resilience by ensuring compliance and meeting user expectations.              |
| **Overall Score**       | **3.9**     | A fundamental user right and a complex but non-negotiable requirement for modern data governance.      |
