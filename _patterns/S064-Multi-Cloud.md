_# Pattern: Multi-Cloud

## 1. Pattern Name and Number

**S064: Multi-Cloud**

## 2. Problem

Relying on a single cloud provider for all infrastructure needs creates a deep form of vendor lock-in and a single point of failure. A major outage, a significant price increase, or a change in the provider's strategic direction could have a devastating impact on the value creation system. This dependency fundamentally undermines the system's sovereignty and resilience.

## 3. Context

You are designing the infrastructure for a critical, large-scale value creation system. You have already decided to use public cloud infrastructure, but you need to mitigate the strategic risks associated with depending on a single provider like AWS, Azure, or Google Cloud.

## 4. Solution

**Intentionally design and operate your system to run across two or more public cloud providers.** This is a direct implementation of a Vendor Exit Strategy (S063) at the infrastructure level.

Common multi-cloud strategies:
- **Active-Active**: Run the full application stack simultaneously across multiple providers, distributing traffic between them. This provides the highest level of resilience but is also the most complex and costly.
- **Active-Passive**: Run the primary application on one provider and maintain a scaled-down, standby deployment on a second provider. In case of a failure, you can fail over to the passive environment.
- **Best-of-Breed**: Use different providers for different workloads based on their specific strengths. For example, use Google Cloud for its AI/ML services, AWS for its mature serverless offerings, and Azure for its enterprise integrations.
- **Cloud Bursting**: Run the primary workload on-premises or on one cloud and "burst" to a second cloud to handle peak traffic loads.

## 5. Rationale

A multi-cloud strategy is a powerful way to maintain technological sovereignty and resilience. It:
- **Avoids Vendor Lock-In**: Preserves the freedom to move workloads and negotiate favorable terms.
- **Increases Resilience**: Protects against a catastrophic, region-wide outage from a single provider.
- **Optimizes for Cost and Performance**: Allows you to choose the best and most cost-effective service for each specific workload.
- **Navigates Data Sovereignty**: Can be used to deploy workloads in specific regions or countries to meet data residency requirements (see S061: Data Sovereignty by Design).

## 6. Consequences

- **Positive**:
    - Maximum resilience and technological sovereignty.
    - Increased negotiating leverage with cloud providers.
    - Ability to optimize performance and cost by choosing the best service for the job.
- **Negative**:
    - **Significant Increase in Complexity**: You now have to manage multiple sets of APIs, security models, and networking environments.
    - **Increased Operational Overhead**: Your operations team needs expertise across multiple clouds.
    - **Data Transfer Costs**: Moving data between clouds can be expensive.
    - **Lowest Common Denominator Effect**: You may be forced to use only the services that are common to all your providers, preventing you from using the most advanced features of any single one.

## 7. Known Uses

- **Large Enterprises**: Many large financial institutions, e-commerce companies, and media giants use multi-cloud strategies to ensure uptime and avoid lock-in.
- **Cloud-Native Tooling**: The rise of Kubernetes and other CNCF projects has made multi-cloud strategies more feasible by providing a consistent abstraction layer across different providers.
- **Anthos and Azure Arc**: Google and Microsoft offer control planes that allow organizations to manage workloads across multiple clouds from a single interface.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of building highly resilient and sovereign systems.                            |
| **2. Governance**       | 5           | A powerful, albeit complex, governance strategy for managing infrastructure risk.                     |
| **3. Economy**          | 3           | Can be very expensive due to increased complexity and operational overhead.                           |
| **4. Technology**       | 4           | Relies on abstraction layers like Kubernetes to be feasible.                                          |
| **5. Operations**       | 2           | Dramatically increases operational complexity. This is not a pattern to be adopted lightly.             |
| **6. Culture**          | 3           | Requires a highly skilled and disciplined engineering culture.                                        |
| **7. Resilience**       | 5           | Provides the highest level of resilience against infrastructure-level failures.                       |
| **Overall Score**       | **3.7**     | A powerful but extremely complex and costly pattern. It should only be considered by large, mature organizations with a clear business case for the required investment in complexity. |
