---
id: pat_subdomain_based_tenant_routing
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/subdomain-based-tenant-routing.md
slug: subdomain-based-tenant-routing
title: Subdomain-Based Tenant Routing
aliases:
- Subdomain-based multi-tenancy
- Tenant routing by subdomain
version: "1.0"
created: "2026-02-10 00:00:00+00:00"
modified: "2026-02-10 00:00:00+00:00"
classification:
  universality: context-dependent
  domain: platform
  category:
  - scalability
  - integration
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 3
  commons_domain:
  - platform
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- Manus AI
- cloudsters
sources:
- https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/domain-names
- https://aws.amazon.com/blogs/networking-and-content-delivery/tenant-routing-strategies-for-saas-applications-on-aws/
- https://workos.com/blog/developers-guide-saas-multi-tenant-architecture
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

## 1. Overview

The Subdomain-Based Tenant Routing pattern is a widely adopted architectural approach for multi-tenant applications, particularly in the Software-as-a-Service (SaaS) domain. This pattern assigns a unique subdomain to each tenant, allowing for clear separation and routing of traffic at the domain name system (DNS) level. For instance, a tenant named "acme" would access the service via `acme.service.com`, while another tenant "globex" would use `globex.service.com`. This approach provides a distinct and branded experience for each tenant, while still allowing the provider to manage a single, unified application codebase and infrastructure. The historical origins of this pattern are closely tied to the rise of cloud computing and SaaS, where the need for scalable, isolated, and customizable multi-tenant architectures became paramount.

## 2. Core Principles

The Subdomain-Based Tenant Routing pattern is defined by a set of core principles that ensure its effective implementation:

| Principle | Description |
| :--- | :--- |
| **Tenant Identification via Subdomain** | The primary identifier for a tenant is the subdomain in the URL. This allows for immediate and unambiguous identification of the tenant for every incoming request. |
| **Centralized Routing Logic** | A centralized routing mechanism, often implemented in a reverse proxy, API gateway, or application middleware, is responsible for parsing the subdomain and directing the request to the appropriate tenant-specific resources. |
| **Tenant Isolation** | While the application itself is multi-tenant, the use of subdomains provides a logical separation of tenants. This can be extended to the data layer, where each tenant may have its own database schema or even a dedicated database instance. |
| **Scalability** | The pattern is inherently scalable, as new tenants can be onboarded by simply provisioning a new subdomain and updating the DNS records. The centralized routing logic can be scaled horizontally to handle increasing traffic. |

## 3. Problem Statement

In a multi-tenant application, a fundamental challenge is to correctly and efficiently route incoming requests to the appropriate tenant. Each tenant has its own set of users, data, and configurations, and it is critical to ensure that these are kept isolated from other tenants. A naive approach of using a single domain for all tenants and relying on user authentication to determine the tenant can lead to complex and error-prone application logic. It also fails to provide a branded and customized experience for each tenant, which is often a key requirement in SaaS applications.

## 4. Solution

The Subdomain-Based Tenant Routing pattern addresses this problem by leveraging the DNS to distinguish between tenants. When a user accesses their tenant-specific subdomain, the DNS resolves the domain to the IP address of the application's entry point, such as a load balancer or reverse proxy. This entry point then inspects the host header of the incoming HTTP request to extract the subdomain. The extracted subdomain is used as a key to look up the tenant's configuration, which may include database connection strings, theme information, and other tenant-specific settings. The request is then forwarded to the application server, which uses the tenant context to process the request and return the appropriate response. This approach simplifies the application logic, as the tenant context is established at the very beginning of the request lifecycle.

## 5. Trade-offs and Considerations

While the Subdomain-Based Tenant Routing pattern offers significant advantages, it also comes with its own set of trade-offs and considerations:

| Aspect | Pros | Cons |
| :--- | :--- | :--- |
| **Tenant Experience** | Provides a branded and professional experience for each tenant. | Requires tenants to manage their own DNS settings if they want to use a custom domain. |
| **Security** | Offers a clear and strong logical separation between tenants. | SSL certificate management can be complex, especially with a large number of tenants. Wildcard certificates can simplify this, but may not be suitable for all scenarios. |
| **Scalability** | Easily scalable by adding new subdomains for new tenants. | DNS propagation delays can impact the onboarding of new tenants. |
| **Development** | Simplifies application logic by providing a clear tenant context. | Requires careful handling of cross-tenant data access and ensuring that tenant data is not accidentally exposed. |

## 6. Real-world Examples

The Subdomain-Based Tenant Routing pattern is used by a vast number of successful SaaS companies, including:

*   **Slack:** Each workspace in Slack is accessed via a unique subdomain, such as `your-workspace.slack.com`.
*   **Atlassian:** Atlassian products like Jira and Confluence Cloud use subdomains to separate customer instances, for example, `your-company.atlassian.net`.
*   **Zendesk:** Zendesk customers access their support portal through a custom subdomain, like `your-company.zendesk.com`.
*   **Shopify:** Each Shopify store is given a unique subdomain, such as `your-store.myshopify.com`.

## 7. Cognitive Era Considerations

In the cognitive era, where AI and machine learning are becoming increasingly integrated into applications, the Subdomain-Based Tenant Routing pattern remains highly relevant. It can be used to provide tenant-specific AI models and services. For example, a multi-tenant e-commerce platform could use this pattern to offer personalized product recommendations to each tenant's customers, based on their unique data. The subdomain can be used to route requests to a tenant-specific machine learning model, ensuring that the recommendations are tailored to the tenant's product catalog and customer base. This allows for a high degree of personalization and customization, which is a key differentiator in the cognitive era.

## 8. Commons Alignment Assessment

The Subdomain-Based Tenant Routing pattern can be assessed against the five principles of the Commons:

| Principle | Assessment |
| :--- | :--- |
| **Shared Resource** | The core application and infrastructure are shared resources, which aligns with the principle of a shared resource. However, the tenant-specific data and configurations are not shared. |
| **Democratic Governance** | The governance of the platform is typically centralized and controlled by the service provider, which does not align with the principle of democratic governance. |
| **Equitable Access** | The pattern provides equitable access to the service for all tenants, as each tenant has its own dedicated subdomain and a consistent level of service. |
| **Sustainability** | The pattern can contribute to sustainability by allowing for efficient use of shared resources. However, the environmental impact of the underlying infrastructure should also be considered. |
| **Community Benefit** | The pattern can provide a community benefit by enabling the creation of a wide range of SaaS applications that serve a variety of needs. |

Overall, the Subdomain-Based Tenant Routing pattern has a mixed alignment with the principles of the Commons. While it promotes the efficient use of shared resources and provides equitable access, it does not inherently support democratic governance or community ownership.

### References

[1] Microsoft. (2025, July 3). *Domain Name Considerations in Multitenant Solutions*. Retrieved from https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/domain-names
[2] AWS. (2024, June 25). *Tenant routing strategies for SaaS applications on AWS*. Retrieved from https://aws.amazon.com/blogs/networking-and-content-delivery/tenant-routing-strategies-for-saas-applications-on-aws/
[3] WorkOS. (2025, December 3). *The developer's guide to SaaS multi-tenant architecture*. Retrieved from https://workos.com/blog/developers-guide-saas-multi-tenant-architecture
