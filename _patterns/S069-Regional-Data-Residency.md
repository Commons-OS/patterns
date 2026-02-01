_# Pattern: Regional Data Residency

## 1. Pattern Name and Number

**S069: Regional Data Residency**

## 2. Problem

Many countries have data residency laws that require certain types of data, especially personal data or government data, to be stored and processed within the country's borders. Using a global cloud provider without careful configuration can result in data being moved between different geographic regions, violating these laws and creating legal and compliance risks.

## 3. Context

You are designing a system that will handle data from users in multiple countries, some of which have data residency requirements. You need to ensure that data from a specific country or region is stored and processed only within that region.

## 4. Solution

**Implement a Regional Data Residency architecture, where you deploy separate, isolated instances of your application stack in each geographic region that has a data residency requirement.**

This involves:
- **Regional Deployments**: Using a cloud provider that has data centers in the required regions, and deploying a full copy of your application and database in each one.
- **Geo-DNS**: Using a DNS service that can route users to the closest regional deployment based on their geographic location.
- **Data Partitioning**: Ensuring that data from users in a specific region is only ever stored in the database in that same region.
- **Strict Isolation**: Configuring your network and application to prevent data from being replicated or moved between regions unless it is explicitly allowed and legally permissible (e.g., after being anonymized).

## 5. Rationale

Regional Data Residency is a direct technical solution for meeting data residency laws. It:
- **Ensures Compliance**: Provides a clear and auditable way to demonstrate compliance with data residency requirements.
- **Reduces Latency**: Improves application performance by serving users from a data center that is geographically close to them.
- **Builds Trust**: Shows users and regulators that you are committed to respecting local laws and protecting their data.

## 6. Consequences

- **Positive**:
    - A clear path to compliance with data residency laws.
    - Improved performance for a global user base.
- **Negative**:
    - **Increased Complexity and Cost**: You have to manage multiple, independent deployments of your application, which significantly increases operational complexity and cost.
    - **Data Silos**: It can be more difficult to get a global, unified view of your data.
    - **Inconsistent User Experience**: If a user travels between regions, their data may not be available to them.

## 7. Known Uses

- **All major SaaS providers** (e.g., Salesforce, Workday) offer regional deployments to meet the data residency needs of their global customers.
- **Cloud providers** make this architecture possible by offering a global network of data center regions.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 3           | A practical pattern for meeting legal requirements.                                                   |
| **2. Governance**       | 4           | A key governance control for managing compliance with a complex web of national laws.                 |
| **3. Economy**          | 3           | A necessary cost of doing business globally, but it increases operational costs.                      |
| **4. Technology**       | 4           | A standard architectural pattern for global cloud applications.                                       |
| **5. Operations**       | 2           | Significantly increases operational complexity.                                                       |
| **6. Culture**          | 3           | Fosters a culture of awareness of the global legal landscape.                                         |
| **7. Resilience**       | 4           | Can build resilience by isolating the impact of a regional outage, but also adds complexity.          |
| **Overall Score**       | **3.3**     | A necessary but complex and costly pattern for any organization operating a global service.            |
