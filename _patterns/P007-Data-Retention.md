_# Pattern: Data Retention

## 1. Pattern Name and Number

**P007: Data Retention**

## 2. Problem

Organizations often accumulate vast amounts of data over time, keeping it indefinitely "just in case." This practice, known as data hoarding, creates a massive and unnecessary liability. The more data you hold, the greater the risk and potential damage from a data breach, and the higher the cost of storage and management. Furthermore, keeping data longer than necessary can violate data protection regulations.

## 3. Context

You are operating a value creation system that collects and stores data, including personal information. You need a systematic policy and process for deciding how long to keep data and how to securely dispose of it once it is no longer needed.

## 4. Solution

**Establish and enforce a clear data retention policy that defines how long different types of data should be kept and includes a process for its secure deletion.** This policy should be based on a balance of legal requirements, business needs, and privacy principles.

Key steps include:
1.  **Data Classification**: Identify and classify the types of data you collect and the purposes for which it is used.
2.  **Define Retention Periods**: For each data class, define a specific retention period. This should be the minimum time required to fulfill the processing purpose and meet any legal or regulatory obligations (e.g., tax laws, industry regulations).
3.  **Secure Deletion**: Implement a process to automatically and securely delete or anonymize data once its retention period has expired. Deletion must be permanent and irrecoverable.
4.  **Documentation**: Document the retention policy, the rationale for the retention periods, and maintain a record of data disposal activities.

## 5. Rationale

A data retention policy is a critical component of data governance and privacy management. It:
- **Reduces Risk**: Minimizes the "blast radius" of a data breach by reducing the amount of data available to be stolen.
- **Ensures Compliance**: Adheres to the data minimization and storage limitation principles of regulations like GDPR.
- **Lowers Costs**: Reduces the costs associated with storing and managing unnecessary data.
- **Improves Data Quality**: Ensures that the data you hold is relevant, accurate, and up-to-date.

## 6. Consequences

- **Positive**:
    - Reduced risk, liability, and storage costs.
    - Improved compliance and data governance.
    - Increased trust from users who see that their data is not being hoarded indefinitely.
- **Negative**:
    - Requires a careful analysis of legal and business requirements to set appropriate retention periods.
    - Can be technically challenging to implement automated deletion across complex, distributed systems.
    - There is a risk of deleting data that is later found to be needed for unforeseen reasons (e.g., litigation).

## 7. Known Uses

- **Financial Services**: Banks are required by law to retain transaction records for a specific number of years for anti-fraud and anti-money laundering purposes.
- **Telecommunications**: Telecom companies have retention policies for call detail records, driven by both law enforcement requirements and business analytics needs.
- **Email Systems**: Many corporate email systems have automated policies to archive or delete emails after a certain period.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of being a responsible and efficient steward of data.                          |
| **2. Governance**       | 5           | A cornerstone of data governance, demonstrating control over the entire data lifecycle.               |
| **3. Economy**          | 4           | Directly reduces operational costs and the potential economic impact of a data breach.                |
| **4. Technology**       | 4           | Requires technological implementation of automated data lifecycle management and secure deletion.     |
| **5. Operations**       | 4           | Requires clear operational processes for policy enforcement, auditing, and handling exceptions.       |
| **6. Culture**          | 4           | Fosters a culture of data minimization, moving away from a "hoard everything" mentality.              |
| **7. Resilience**       | 5           | Builds resilience by minimizing the data footprint that needs to be protected and that can be lost.   |
| **Overall Score**       | **4.3**     | A fundamental and highly effective pattern for responsible data governance and risk management.        |
