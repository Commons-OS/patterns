---
id: pat_37d0ce3c51419b0b34f64f37
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/multi-tenancy.md
slug: multi-tenancy
title: Multi-Tenancy
aliases:
- Shared Infrastructure
- SaaS Tenancy
- Application Multitenancy
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: context-dependent
  domain: platform
  category:
  - mechanism
  - strategy
  era:
  - digital
  origin:
  - software-engineering
  - cloud-computing
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
- higgerix
- cloudsters
sources:
- https://www.geeksforgeeks.org/system-design/multi-tenancy-architecture-system-design/
- https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models
- https://www.gooddata.com/blog/multi-tenant-architecture/
- https://www.cloudflare.com/learning/cloud/what-is-multitenancy/
- https://www.ibm.com/think/topics/multi-tenant
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
page_url: https://commons-os.github.io/patterns/multi-tenancy/
---

### 1. Overview

Multi-tenancy is a software architecture pattern in which a single instance of a software application serves multiple customers. Each customer is referred to as a tenant. Tenants may be given the ability to customize some parts of the application, such as the color of the user interface or business rules, but they cannot customize the application's code. In a multi-tenant architecture, multiple instances of an application operate in a shared environment. This is in contrast to a single-tenant architecture, where each customer has their own dedicated software instance and supporting infrastructure. The primary benefit of multi-tenancy is the cost savings that result from sharing resources, such as infrastructure, databases, and application instances. This model has become the standard for software-as-a-service (SaaS) offerings, as it allows providers to serve a large number of customers with a single, scalable infrastructure.

The importance of multi-tenancy lies in its ability to enable economies of scale in the delivery of software. By sharing resources, SaaS providers can significantly reduce their operational costs and pass those savings on to their customers. This has made sophisticated software accessible to a much broader range of businesses, including small and medium-sized enterprises that might not have been able to afford dedicated software instances. Furthermore, multi-tenancy simplifies the process of updating and maintaining software. Instead of having to update thousands of individual software instances, a SaaS provider can update a single application instance, and all tenants will instantly have access to the new features and bug fixes. This leads to a more consistent and reliable user experience for all customers.

The historical origins of multi-tenancy can be traced back to the mainframe era, where time-sharing systems allowed multiple users to share the resources of a single powerful computer. However, the modern concept of multi-tenancy emerged with the rise of the internet and the application service provider (ASP) model in the late 1990s. ASPs would host and manage third-party software applications and deliver them to customers over the internet. While the ASP model had its limitations, it laid the groundwork for the SaaS model that we know today. The advent of cloud computing, with its on-demand infrastructure and scalable services, has further accelerated the adoption of multi-tenancy, making it the dominant architecture for modern cloud-based applications. The evolution from mainframes to ASPs and finally to cloud-native SaaS represents a continuous drive towards greater efficiency, scalability, and cost-effectiveness in software delivery, with multi-tenancy as a core enabling pattern.

### 2. Core Principles

1.  **Resource Sharing:** At the heart of multi-tenancy is the principle of sharing resources among multiple tenants. This can include sharing infrastructure (servers, storage, networking), application instances, and databases. The goal is to maximize resource utilization and minimize costs. For example, instead of provisioning a separate server for each tenant, a multi-tenant application can run on a cluster of servers that are shared by all tenants. This allows for much higher server utilization and reduces the overall hardware cost. Similarly, sharing a database among multiple tenants can reduce licensing and maintenance costs.

2.  **Data Isolation:** While resources are shared, it is crucial to ensure that each tenant's data is securely isolated from other tenants. This is a fundamental requirement for privacy and security. Data isolation can be achieved at different levels, such as at the database, schema, or even table level, depending on the chosen tenancy model. For example, in a shared database model, each table would have a `tenant_id` column, and all queries would be filtered by the current tenant's ID to ensure that only the correct data is returned. In a separate schema model, each tenant has their own set of tables within the same database, providing a stronger level of isolation.

3.  **Scalability:** A multi-tenant architecture must be designed to scale horizontally to accommodate a growing number of tenants and users. This involves designing the application and infrastructure to be elastic, allowing resources to be added or removed dynamically based on demand. For example, a multi-tenant application might be deployed on a Kubernetes cluster, which can automatically scale the number of application pods up or down based on the current load. This ensures that the application can handle a large number of concurrent users without performance degradation.

4.  **Performance Isolation:** It is important to prevent the activities of one tenant from negatively impacting the performance of other tenants. This is often referred to as the "noisy neighbor" problem. Mechanisms such as resource quotas, throttling, and load balancing are used to ensure fair resource allocation and consistent performance for all tenants. For example, a multi-tenant application might implement rate limiting to prevent any single tenant from making an excessive number of API requests. It might also use a load balancer to distribute traffic evenly across multiple application instances.

5.  **Customization:** While all tenants share the same core application, a multi-tenant architecture should allow for a degree of customization for each tenant. This can include customizing the user interface, workflows, and business rules. The key is to provide this flexibility without requiring changes to the underlying code. For example, a multi-tenant application might use a metadata-driven approach to customization, where each tenant's customizations are stored in a separate set of metadata that is used to render the user interface and execute business logic.

6.  **Operational Efficiency:** Multi-tenancy enables operational efficiency through centralized management and maintenance. Updates, patches, and new features can be rolled out to all tenants simultaneously, reducing the operational overhead associated with managing multiple individual software instances. For example, instead of having to manually update thousands of servers, a SaaS provider can use an automated deployment pipeline to update their entire multi-tenant environment in a matter of minutes. This allows for a much faster and more reliable release process.

7.  **Cost Efficiency:** By sharing resources and centralizing management, multi-tenancy significantly reduces the cost of delivering software. This cost efficiency is a key driver for the adoption of the SaaS model and has made powerful software more accessible to a wider range of businesses. The cost savings come from a variety of sources, including reduced hardware costs, lower energy consumption, and reduced operational overhead. These savings can be passed on to customers in the form of lower prices, making the software more competitive in the market.

### 3. Key Practices

1.  **Tenant-Aware Identity and Access Management:** Implement a robust identity and access management (IAM) system that is aware of tenants. This system should be able to authenticate users and enforce access control policies based on their tenant and role. For example, you could use a centralized identity provider like Okta or Azure Active Directory to manage user identities and then use a role-based access control (RBAC) system to define what each user is allowed to do within their tenant.

2.  **Tenant-Specific Routing:** Implement a mechanism to route incoming requests to the correct tenant. This can be based on a subdomain (e.g., `tenant1.myapp.com`), a URL path (e.g., `myapp.com/tenant1`), or a custom HTTP header (e.g., `X-Tenant-ID: tenant1`). The routing mechanism should be able to identify the tenant and direct the request to the appropriate application instance and database. For example, you could use a reverse proxy like Nginx or a cloud-native API gateway to handle tenant-specific routing.

3.  **Data Partitioning Strategy:** Choose a data partitioning strategy that balances the need for data isolation with the desire for cost efficiency. The three main strategies are separate databases, separate schemas, and a shared schema with a tenant ID column. The choice of strategy will depend on the specific requirements of the application. For example, if you have a small number of tenants with high data isolation requirements, you might choose to use separate databases. If you have a large number of tenants with lower data isolation requirements, you might choose to use a shared schema with a tenant ID column.

4.  **Automated Tenant Provisioning and Onboarding:** Automate the process of provisioning and onboarding new tenants. This should include creating the tenant's database or schema, configuring their settings, and creating their initial user accounts. Automation reduces the operational overhead and ensures a consistent onboarding experience. For example, you could create a self-service onboarding portal where new tenants can sign up and configure their account without any manual intervention from your team.

5.  **Centralized Monitoring and Logging:** Implement a centralized monitoring and logging system that can track the health and performance of the entire multi-tenant environment. This system should be able to filter logs and metrics by tenant, allowing for targeted troubleshooting and analysis. For example, you could use a tool like Datadog or New Relic to collect and analyze logs and metrics from all of your application instances and databases.

6.  **Progressive Deployment of Updates:** Implement a strategy for progressively deploying updates to tenants. This can involve rolling out updates to a small subset of tenants first, and then gradually expanding the rollout to all tenants. This approach minimizes the risk of introducing a bug that affects all customers simultaneously. For example, you could use a feature flagging system to enable new features for specific tenants before rolling them out to everyone.

7.  **Tenant-Specific Metering and Billing:** If you are charging tenants based on their usage, implement a system for metering their resource consumption and generating invoices. This system should be able to accurately track the usage of each tenant and apply the correct pricing model. For example, you could use a usage-based billing platform like Stripe or Chargebee to automate the entire billing process.

### 4. Application Context

**Best Used For:**

*   **Software-as-a-Service (SaaS) applications:** This is the most common use case for multi-tenancy. SaaS applications that need to serve a large number of customers in a cost-effective manner are a natural fit for this architecture. Examples include Salesforce, Slack, and Dropbox.
*   **Platform-as-a-Service (PaaS) offerings:** PaaS providers like Heroku and AWS Elastic Beanstalk use multi-tenancy to provide a shared platform for developers to build and deploy their applications.
*   **Business-to-Business (B2B) applications:** B2B applications that are sold to multiple businesses can benefit from the cost savings and operational efficiency of multi-tenancy.
*   **Consumer applications with a large user base:** Consumer applications like social media platforms and online marketplaces can use multi-tenancy to serve millions of users in a scalable and cost-effective way.

**Not Suitable For:**

*   **Applications with highly sensitive data:** Applications that handle highly sensitive data, such as financial or medical records, may not be suitable for a multi-tenant architecture due to the risk of data breaches.
*   **Applications with extreme performance requirements:** Applications that have extreme performance requirements, such as high-frequency trading platforms, may not be suitable for a multi-tenant architecture due to the "noisy neighbor" problem.
*   **Applications that require deep customization:** Applications that require deep customization of the underlying code are not a good fit for multi-tenancy. In these cases, a single-tenant architecture is a better choice.

**Scale:**

Multi-tenancy is designed for scale. By sharing resources, a multi-tenant architecture can support a large number of tenants and users with a relatively small infrastructure footprint. The scalability of a multi-tenant architecture is determined by the scalability of its underlying components, such as the application servers, databases, and load balancers. With a well-designed architecture, a multi-tenant application can scale to support millions of users. For example, a multi-tenant application could be deployed on a global cloud provider like AWS or Azure, which would allow it to scale to meet the demands of a global user base.

**Domains:**

*   **Business Software:** CRM (Salesforce), ERP (NetSuite), HR (Workday), and other business software are often delivered as multi-tenant SaaS applications.
*   **Collaboration Tools:** Project management (Asana), team messaging (Slack), and video conferencing (Zoom) tools are typically multi-tenant.
*   **E-commerce Platforms:** Many e-commerce platforms (Shopify, BigCommerce) are multi-tenant, allowing multiple merchants to create their own online stores on a shared platform.
*   **Content Management Systems (CMS):** Multi-tenant CMS platforms (WordPress.com) allow multiple websites to be managed from a single instance of the CMS.
*   **Developer Tools:** Code hosting (GitHub), continuous integration (CircleCI), and error tracking (Sentry) tools are often multi-tenant.

### 5. Implementation

Implementing a multi-tenant architecture requires careful planning and consideration of several key factors. The first step is to choose a tenancy model that aligns with the specific requirements of the application. The three main models are:

*   **Isolated Tenancy:** Each tenant has their own dedicated application instance and database. This model provides the highest level of data isolation but is also the most expensive. This model is a good choice for applications that have a small number of high-value tenants who are willing to pay a premium for the extra security and performance.
*   **Shared Application, Separate Databases:** All tenants share the same application instance, but each tenant has their own dedicated database. This model provides a good balance of data isolation and cost efficiency. This model is a good choice for applications that have a moderate number of tenants and need to provide a good level of data isolation.
*   **Shared Everything:** All tenants share the same application instance and the same database. This model is the most cost-effective but also provides the lowest level of data isolation. This model is a good choice for applications that have a large number of tenants and can tolerate a lower level of data isolation.

Once a tenancy model has been chosen, the next step is to design the application and infrastructure to support it. This includes implementing a tenant-aware identity and access management system, a tenant-specific routing mechanism, and a data partitioning strategy. It is also important to automate the process of provisioning and onboarding new tenants, as well as the process of deploying updates. For example, you could use a combination of Terraform and Ansible to automate the entire infrastructure and application deployment process.

From an infrastructure perspective, a multi-tenant architecture should be designed to be scalable and resilient. This can be achieved by using cloud-based infrastructure and services, such as load balancers, auto-scaling groups, and managed databases. It is also important to implement a centralized monitoring and logging system to track the health and performance of the entire environment. For example, you could use a combination of Prometheus and Grafana to monitor the performance of your application and infrastructure in real-time.

Finally, it is important to consider the security implications of multi-tenancy. Because multiple tenants are sharing the same resources, it is crucial to implement strong security measures to prevent data breaches and other security incidents. This includes encrypting data at rest and in transit, implementing network security controls, and regularly performing security audits. For example, you could use a web application firewall (WAF) to protect your application from common web-based attacks, and you could use a security information and event management (SIEM) system to collect and analyze security logs from all of your systems.

### 6. Evidence & Impact

The impact of multi-tenancy on the software industry has been profound. The rise of the SaaS model, which is enabled by multi-tenancy, has democratized access to sophisticated software, allowing businesses of all sizes to compete on a more level playing field. Companies like Salesforce, which was one of the pioneers of the SaaS model, have shown that it is possible to build a multi-billion dollar business by delivering software as a service. The success of Salesforce and other SaaS companies has inspired a whole new generation of entrepreneurs to build and launch their own SaaS products.

Real-world examples of multi-tenant architectures are abundant. In addition to Salesforce, other well-known examples include Google Workspace (formerly G Suite), Microsoft 365, and Slack. These applications are used by millions of people every day and are all built on multi-tenant architectures. The success of these companies is a testament to the power and scalability of the multi-tenant model. These companies have been able to achieve massive scale and profitability by leveraging the economies of scale that are inherent in a multi-tenant architecture.

The evidence for the benefits of multi-tenancy is clear. By sharing resources, SaaS providers can achieve significant cost savings, which they can then pass on to their customers. This has made software more affordable and accessible than ever before. Furthermore, multi-tenancy simplifies the process of updating and maintaining software, leading to a more consistent and reliable user experience. As the software industry continues to move towards the cloud, the importance of multi-tenancy is only going to grow. We can expect to see even more innovation in the area of multi-tenancy as new technologies and best practices emerge.

### 7. Cognitive Era Considerations

The cognitive era, with its focus on artificial intelligence (AI) and machine learning (ML), introduces new opportunities and challenges for multi-tenant architectures. On the one hand, AI and ML can be used to enhance multi-tenant applications in a variety of ways. For example, AI-powered features, such as personalized recommendations and intelligent search, can be delivered to all tenants in a cost-effective manner. Furthermore, ML can be used to optimize the performance and security of multi-tenant environments by detecting anomalies and predicting resource needs. For example, an ML model could be trained to predict when a tenant is about to experience a surge in traffic and then automatically scale up the resources for that tenant to prevent a performance degradation.

On the other hand, the cognitive era also introduces new challenges. For example, training and deploying ML models in a multi-tenant environment can be complex. It is important to ensure that the models are not biased by the data of any single tenant and that the predictions they make are accurate for all tenants. Furthermore, the use of AI and ML can raise new privacy and security concerns. It is crucial to ensure that the data used to train ML models is properly anonymized and that the models themselves are not vulnerable to attack. For example, an attacker could try to poison the training data for an ML model in order to cause it to make incorrect predictions. To mitigate this risk, it is important to implement strong data validation and security controls.

### 8. Commons Alignment Assessment

- **Shared Resource Potential:** High - Multi-tenancy is fundamentally about sharing resources, which aligns with the commons principle of managing shared resources for the benefit of all. By pooling resources, multi-tenancy can lead to a more efficient and sustainable use of computing infrastructure.

- **Democratic Governance:** Low - In a typical multi-tenant architecture, the governance of the platform is centralized in the hands of the provider. Tenants have limited say in how the platform is run or how it evolves. This can lead to a power imbalance between the provider and the tenants, and it can make it difficult for tenants to hold the provider accountable.

- **Equitable Access:** Medium - While multi-tenancy can make software more accessible by reducing its cost, access is still contingent on the ability to pay. Furthermore, the provider has the power to deny access to any tenant at any time. This can create a digital divide between those who can afford to pay for software and those who cannot.

- **Sustainability:** Medium - Multi-tenancy can contribute to environmental sustainability by reducing the overall energy consumption of data centers. However, the sustainability of the platform is ultimately dependent on the business model of the provider. If the provider is focused on maximizing profits, they may not be incentivized to invest in sustainable practices.

- **Community Benefit:** Medium - Multi-tenant platforms can create a sense of community among their users, but the primary beneficiary of the platform is the provider. The value created by the users is often captured by the provider in the form of data and revenue. This can lead to a situation where the users are creating value for the provider, but they are not sharing in the benefits.
