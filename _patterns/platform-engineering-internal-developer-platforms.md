---
id: pat_01kg5023znes88czf32w2emzxq
page_url: https://commons-os.github.io/patterns/platform-engineering-internal-developer-platforms/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/platform-engineering-internal-developer-platforms.md
slug: platform-engineering-internal-developer-platforms
title: Platform Engineering - Internal Developer Platforms
aliases: [Internal Developer Platform, IDP]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: design
  category: [practice]
  era: [digital]
  origin: [google, spotify, netflix]
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: ["pat_01kg5023vzfs093ryk8ek6spvb"]
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Platform engineering is the discipline of designing and building toolchains and workflows that enable self-service capabilities for software engineering organizations. It has emerged as a critical practice in the cloud-native era to manage the increasing complexity of software development and delivery. The primary output of platform engineering is an Internal Developer Platform (IDP), which is a curated set of tools and technologies that a platform team provides to their internal customers—the developers. The IDP is designed to reduce cognitive load on developers by providing a streamlined and automated path to production, often referred to as a "golden path." This allows developers to focus on writing code and delivering business value, rather than getting bogged down in the intricacies of infrastructure, security, and compliance.

The core problem that platform engineering solves is the friction and inefficiency that arises when developers are forced to become experts in a wide range of operational tasks. In many organizations, the promise of DevOps—"you build it, you run it"—has led to a situation where developers are overwhelmed with the complexity of modern toolchains. Platform engineering addresses this by creating a dedicated platform team that treats the internal platform as a product and the developers as customers. This product-centric approach ensures that the platform is designed to meet the needs of the developers and is continuously improved based on their feedback.

The origin of platform engineering can be traced back to the early 2010s, with companies like Google, Netflix, and Spotify pioneering the concept of internal platforms to support their rapidly growing engineering teams. These companies recognized that to scale their development efforts, they needed to provide their developers with a set of standardized tools and services that would abstract away the underlying infrastructure. This allowed their developers to move faster and with more autonomy, while still ensuring that the company's standards for security, reliability, and compliance were met. The success of these early pioneers has led to the widespread adoption of platform engineering as a best practice for modern software development organizations.


### 2. Core Principles

Platform engineering is guided by a set of core principles that are designed to maximize developer productivity, improve software quality, and accelerate the delivery of business value. These principles are the foundation upon which a successful Internal Developer Platform is built.

1.  **Developer Experience as a Product:** This is arguably the most important principle of platform engineering. It means treating the internal platform as a product and the developers as its customers. The platform team must adopt a product mindset, which involves understanding the needs of the developers, gathering feedback, and continuously iterating on the platform to improve the developer experience. This is in stark contrast to the traditional IT mindset, which often treats internal tools as a cost center and developers as a captive audience. By focusing on the developer experience, platform teams can create a platform that developers love to use, which in turn leads to higher productivity and morale.

2.  **Self-Service and Automation:** The goal of an IDP is to empower developers to self-serve their needs without having to file tickets or wait for another team to provision resources. This is achieved through a high degree of automation. The platform should automate as much of the software development lifecycle as possible, from provisioning infrastructure to deploying applications. This not only speeds up the development process but also reduces the risk of human error.

3.  **Golden Paths and Paved Roads:** An IDP should provide developers with "golden paths" or "paved roads" that make it easy for them to do the right thing. These are well-defined, supported, and documented ways of building, deploying, and running applications. Golden paths are not about restricting developers' choices, but about providing them with a set of sensible defaults and best practices that will help them to be successful. Developers should still have the freedom to deviate from the golden path if they have a good reason to do so, but the golden path should be the path of least resistance.

4.  **Security and Compliance by Design:** Security and compliance should be built into the platform from the ground up, not bolted on as an afterthought. The IDP should provide developers with a set of pre-approved, secure, and compliant components that they can use to build their applications. This helps to reduce the security and compliance burden on developers and ensures that all applications meet the organization's standards.

5.  **Observability and Feedback:** The platform should provide developers with the tools they need to understand the health and performance of their applications in production. This includes metrics, logs, and traces. The platform should also provide feedback to developers as early as possible in the development process. For example, the platform could provide feedback on code quality, security vulnerabilities, and compliance issues as soon as the code is committed.

6.  **Continuous Improvement:** An IDP is not a one-time project; it is a living product that must be continuously improved. The platform team should be constantly gathering feedback from developers, monitoring the usage of the platform, and looking for ways to make it better. This requires a culture of continuous learning and improvement.


### 3. Key Practices

To effectively implement platform engineering and build a successful Internal Developer Platform, organizations should adopt a set of key practices. These practices are the practical application of the core principles and are essential for creating a platform that delivers real value to developers and the business.

1.  **Establish a Dedicated Platform Team:** A dedicated platform team is essential for the success of any platform engineering initiative. This team is responsible for building, maintaining, and supporting the IDP. The team should be cross-functional, with a mix of skills in software engineering, infrastructure, security, and product management. The platform team should be treated as a product team, with a clear roadmap and a focus on delivering value to its customers—the developers.

2.  **Develop a Platform-as-a-Product Strategy:** The platform team should develop a clear strategy for the IDP, treating it as a product. This includes defining the vision, mission, and goals of the platform, as well as identifying the target audience and their needs. The strategy should also include a roadmap for the platform, outlining the features and capabilities that will be delivered over time. This product-centric approach helps to ensure that the platform is aligned with the needs of the business and that it delivers a positive return on investment.

3.  **Build a Thinnest Viable Platform (TVP):** Instead of trying to build a comprehensive platform from day one, organizations should start by building a "thinnest viable platform" (TVP). The TVP is the smallest possible version of the platform that delivers real value to developers. This approach allows the platform team to get feedback from developers early and often, and to iterate on the platform based on their needs. The TVP should focus on solving the most pressing problems for developers, such as automating the deployment process or providing self-service access to infrastructure.

4.  **Curate a Set of Supported Tools and Technologies:** The platform team should curate a set of supported tools and technologies that developers can use to build, deploy, and run their applications. This helps to reduce the cognitive load on developers and ensures that all applications are built using a consistent set of tools. The platform team should carefully evaluate and select the tools that are included in the platform, based on factors such as ease of use, reliability, and security.

5.  **Provide a Centralized Developer Portal:** A centralized developer portal is a key component of any IDP. The portal provides a single place for developers to access all of the tools, services, and documentation that they need to do their jobs. The portal should be designed to be user-friendly and intuitive, and it should provide a consistent experience across all of the tools and services that are included in the platform. Backstage, an open-source project from Spotify, is a popular choice for building developer portals.

6.  **Implement GitOps for Infrastructure and Application Management:** GitOps is a modern approach to managing infrastructure and applications that uses Git as the single source of truth. With GitOps, all changes to infrastructure and applications are made through pull requests to a Git repository. This provides a clear audit trail of all changes and makes it easy to roll back to a previous state if something goes wrong. GitOps is a key enabler of self-service and automation, and it is a best practice for any platform engineering initiative.

7.  **Foster a Culture of Collaboration and Feedback:** Platform engineering is not just about technology; it is also about culture. The platform team should foster a culture of collaboration and feedback, both within the team and with the broader engineering organization. The platform team should actively solicit feedback from developers and use it to improve the platform. The team should also be transparent about its roadmap and its progress, and it should celebrate its successes with the entire organization.


### 4. Application Context

Platform engineering and Internal Developer Platforms are most effective when applied in the right context. Understanding the scenarios where this pattern excels, where it is not a good fit, and the scale and domains where it is commonly applied is crucial for successful implementation.

**Best Used For:**

*   **Large and Growing Engineering Organizations:** As the number of developers and services grows, the complexity of managing the development and delivery process increases exponentially. Platform engineering provides a way to manage this complexity and to ensure that all teams are following a consistent set of standards and best practices.
*   **Cloud-Native Environments:** Organizations that are building and running applications in the cloud are well-suited for platform engineering. Cloud-native technologies, such as containers and microservices, introduce a new set of challenges that can be effectively addressed by an IDP.
*   **Organizations with a DevOps Culture:** Platform engineering is a natural evolution of DevOps. Organizations that have already embraced a DevOps culture, with its focus on collaboration, automation, and shared responsibility, will find it easier to adopt platform engineering.
*   **Complex and Regulated Industries:** In industries such as finance and healthcare, where security and compliance are paramount, platform engineering can help to ensure that all applications meet the required standards. An IDP can provide developers with a set of pre-approved, secure, and compliant components that they can use to build their applications.
*   **Organizations Seeking to Improve Developer Experience:**  For organizations that want to attract and retain top engineering talent, providing a world-class developer experience is essential. An IDP can significantly improve the developer experience by reducing friction, automating tedious tasks, and empowering developers to be more productive.

**Not Suitable For:**

*   **Small, Early-Stage Startups:** In the early stages of a startup, the focus is on speed and agility. The overhead of building and maintaining an IDP may not be justified. In these cases, a more lightweight approach to development and delivery is often more appropriate.
*   **Organizations with a Monolithic Architecture:** While platform engineering can be applied to monolithic architectures, it is most effective in organizations that have adopted a microservices-based architecture. The benefits of an IDP are more pronounced when there are a large number of services to manage.
*   **Organizations with a Strong Resistance to Change:** Platform engineering represents a significant change to the way that software is developed and delivered. Organizations with a strong resistance to change will find it difficult to adopt this new way of working.

**Scale:**

Platform engineering can be applied at various scales, but it is most commonly found at the **Department**, **Organization**, and **Multi-Organization** levels. While a single team can benefit from some of the principles of platform engineering, the full benefits of an IDP are realized when it is adopted across a larger group of developers.

**Domains:**

Platform engineering is applicable across a wide range of industries, but it is most commonly found in the following domains:

*   **Technology:**  Software and technology companies are the pioneers of platform engineering.
*   **Financial Services:** Banks, insurance companies, and other financial institutions are increasingly adopting platform engineering to improve their agility and to meet their regulatory requirements.
*   **E-commerce and Retail:** E-commerce and retail companies use platform engineering to manage the complexity of their online platforms and to deliver new features to their customers more quickly.
*   **Healthcare:** Healthcare organizations are using platform engineering to build secure and compliant applications that improve patient care.
*   **Media and Entertainment:** Media and entertainment companies use platform engineering to manage their content delivery pipelines and to provide a personalized experience to their users.


### 5. Implementation

Implementing platform engineering and building an Internal Developer Platform is a significant undertaking that requires careful planning and execution. This section provides a practical guide for organizations that are embarking on this journey.

**Prerequisites:**

*   **Executive Sponsorship:**  Platform engineering is a strategic initiative that requires strong support from executive leadership. The executive sponsors should understand the value of platform engineering and be willing to invest the necessary resources to make it successful.
*   **A Clear Vision and Strategy:** Before starting to build an IDP, it is essential to have a clear vision and strategy for what you want to achieve. This should include defining the goals of the platform, identifying the target audience, and outlining the key features and capabilities that will be delivered.
*   **A Dedicated Platform Team:** As mentioned earlier, a dedicated platform team is a prerequisite for success. This team should have the right mix of skills and experience, and it should be empowered to make decisions and to drive the platform forward.
*   **A DevOps Culture:** Platform engineering builds on the principles of DevOps. Organizations that have already embraced a DevOps culture will find it much easier to adopt platform engineering.
*   **A Willingness to Change:** Platform engineering represents a new way of working. Organizations must be willing to change their processes, their tools, and their culture to be successful.

**Getting Started:**

1.  **Start Small with a Thinnest Viable Platform (TVP):** Don't try to build a comprehensive platform from day one. Start with a TVP that solves a real problem for a small group of developers. This will allow you to get feedback early and often, and to iterate on the platform based on the needs of your users.
2.  **Identify a "Pioneer" Team:**  Identify a team of developers who are enthusiastic about the idea of platform engineering and who are willing to be early adopters of the platform. This team can provide valuable feedback and help to champion the platform to the rest of the organization.
3.  **Focus on the "Paved Road":**  When building your TVP, focus on creating a "paved road" for a single, well-defined use case. For example, you might focus on automating the deployment process for a specific type of application.
4.  **Measure and Communicate Your Success:**  It is important to measure the impact of your platform and to communicate your success to the rest of the organization. This will help to build momentum and to get buy-in from other teams.
5.  **Iterate and Grow:**  Once you have successfully launched your TVP, you can start to iterate and grow the platform based on the needs of your users. This might involve adding new features, supporting new use cases, or expanding the platform to other teams.

**Common Challenges:**

*   **Internal Resistance to Change:** One of the biggest challenges in implementing platform engineering is overcoming internal resistance to change. Developers may be reluctant to give up their existing tools and workflows, and operations teams may be resistant to the idea of a self-service platform.
*   **Lack of Skills and Expertise:** Building and operating an IDP requires a specific set of skills and expertise. Many organizations lack the in-house talent to do this, and they may need to hire or train people to fill these roles.
*   **Choosing the Right Tools:** There are a bewildering array of tools available for building an IDP. Choosing the right tools can be a daunting task, and it is important to carefully evaluate the options before making a decision.
*   **Integrating with Existing Systems:** Most organizations have a complex landscape of existing systems. Integrating the IDP with these systems can be a major challenge.
*   **Measuring the ROI:**  It can be difficult to measure the return on investment (ROI) of a platform engineering initiative. This can make it difficult to get buy-in from executive leadership.

**Success Factors:**

*   **A Strong Product Mindset:** The platform team must have a strong product mindset, treating the platform as a product and the developers as customers.
*   **A Focus on Developer Experience:** The platform should be designed to provide a world-class developer experience.
*   **A Culture of Collaboration and Feedback:** The platform team should foster a culture of collaboration and feedback, both within the team and with the broader engineering organization.
*   **An Incremental and Iterative Approach:**  Start small with a TVP and then iterate and grow the platform based on the needs of your users.
*   **Strong Executive Sponsorship:**  Platform engineering is a strategic initiative that requires strong support from executive leadership.


### 6. Evidence & Impact

Platform engineering has moved beyond a theoretical concept to a proven practice with significant, measurable impact on business and technology outcomes. The adoption of Internal Developer Platforms (IDPs) by leading technology companies and the growing body of research on the topic provide compelling evidence of its effectiveness.

**Notable Adopters:**

Many of the world's leading technology companies have been pioneers in platform engineering, building sophisticated internal platforms to support their engineering teams. These companies have demonstrated the value of this approach at scale.

*   **Netflix:** Netflix is a well-known example of a company that has embraced platform engineering. Their internal platform, which includes tools like Spinnaker for continuous delivery, has been instrumental in their ability to innovate and to scale their streaming service to millions of users worldwide.
*   **Spotify:** Spotify's internal developer portal, Backstage, has become the de facto open-source standard for building IDPs. Backstage provides a unified interface for developers to access all of the tools, services, and documentation that they need to do their jobs. The success of Backstage has led to its adoption by many other companies.
*   **Google:** Google has a long history of building internal platforms to support its massive engineering organization. Their internal platform, which includes tools like Borg for container orchestration, has been a key enabler of their ability to build and to operate some of the largest and most complex systems in the world.
*   **Uber:** Uber has developed a number of internal platforms to support its ride-sharing and food delivery businesses. Their Michelangelo platform, for example, provides a complete machine learning workflow, from data management to model training and deployment.
*   **Shopify:** Shopify has built a powerful internal platform to support its e-commerce platform. Their platform provides a set of self-service tools and services that allow their merchants to build and to manage their online stores.

**Documented Outcomes:**

The adoption of platform engineering and IDPs has been shown to have a number of positive outcomes for organizations.

*   **Increased Developer Productivity:** By automating tedious tasks and providing a streamlined path to production, IDPs can significantly increase developer productivity. A study by the DevOps Research and Assessment (DORA) team found that elite performers, who are more likely to have adopted platform engineering, have 2.6 times more code deployments than low performers.
*   **Improved Software Quality:** IDPs can improve software quality by providing developers with a set of pre-approved, secure, and compliant components. This helps to reduce the risk of errors and vulnerabilities.
*   **Faster Time to Market:** By accelerating the development and delivery process, IDPs can help organizations to get new features and products to market faster. This can provide a significant competitive advantage.
*   **Reduced Operational Costs:** By automating infrastructure management and other operational tasks, IDPs can help to reduce operational costs.
*   **Improved Developer Experience and Retention:** A world-class developer experience is a key factor in attracting and retaining top engineering talent. IDPs can significantly improve the developer experience by reducing friction and empowering developers to be more productive.

**Research Support:**

A growing body of research supports the benefits of platform engineering. The State of DevOps Report, published annually by the DORA team, has consistently shown that organizations that adopt platform engineering practices are more likely to be high performers. The 2021 report, for example, found that organizations with internal platforms are 1.5 times more likely to be elite performers. Similarly, Gartner has predicted that by 2026, 80% of large software engineering organizations will have established platform engineering teams to provide reusable services, components, and tools for application delivery.


### 7. Cognitive Era Considerations

The cognitive era, characterized by the increasing prevalence of artificial intelligence and machine learning, is poised to have a profound impact on platform engineering. As AI becomes more sophisticated, it will augment the capabilities of both platform engineers and developers, leading to a new generation of intelligent and autonomous Internal Developer Platforms.

**Cognitive Augmentation Potential:**

AI has the potential to augment platform engineering in a number of ways:

*   **AI-Powered Developer Assistants:** AI-powered assistants, integrated into the developer's IDE, can provide intelligent code completion, suggest best practices, and identify potential bugs and security vulnerabilities in real time. This can significantly improve developer productivity and code quality.
*   **Intelligent Infrastructure Optimization:** AI can be used to analyze infrastructure usage patterns and to automatically optimize resource allocation. This can lead to significant cost savings and improved performance.
*   **Proactive Security and Compliance:** AI-powered security tools can continuously monitor the platform for threats and vulnerabilities, and can automatically remediate issues as they are discovered. This can help to improve the security and compliance posture of the organization.
*   **Autonomous Operations:** AI can be used to automate many of the operational tasks that are currently performed by platform engineers, such as monitoring, alerting, and incident response. This can free up platform engineers to focus on more strategic initiatives.
*   **Personalized Developer Experiences:** AI can be used to personalize the developer experience, providing each developer with a set of tools and services that are tailored to their specific needs and preferences.

**Human-Machine Balance:**

While AI will automate many tasks, it will not replace the need for human platform engineers. The role of the platform engineer will evolve to focus on higher-level tasks that require creativity, critical thinking, and strategic decision-making. These tasks include:

*   **Designing and Evolving the Platform Architecture:** Platform engineers will be responsible for designing the overall architecture of the platform and for ensuring that it is able to meet the future needs of the organization.
*   **Curating and Integrating AI-Powered Tools:** Platform engineers will need to carefully evaluate and select the AI-powered tools that are included in the platform, and to ensure that they are well-integrated with the rest of the platform.
*   **Governing the Use of AI:** Platform engineers will be responsible for establishing policies and procedures for the responsible use of AI on the platform. This includes ensuring that AI is used in a fair, transparent, and ethical manner.
*   **Fostering a Culture of Learning and Experimentation:** Platform engineers will need to foster a culture of learning and experimentation, encouraging developers to explore new ways of using AI to improve their productivity and to create innovative new products and services.

**Evolution Outlook:**

In the cognitive era, the Internal Developer Platform will evolve from a passive set of tools and services to an active and intelligent partner for developers. The IDP will be able to anticipate the needs of developers, to provide them with proactive guidance and support, and to continuously learn and improve based on their feedback. This will lead to a new level of synergy between humans and machines, and will enable organizations to build and to operate software at a scale and a level of sophistication that is unimaginable today.


### 8. Commons Alignment Assessment

This section assesses the alignment of the Platform Engineering pattern with the seven dimensions of the Commons OS framework. The assessment provides a score for each dimension, as well as an overall score and a rationale for the assessment.

**1. Stakeholder Mapping:**

The Platform Engineering pattern demonstrates a strong understanding of its internal stakeholders. It explicitly identifies developers as the primary customers of the Internal Developer Platform (IDP) and emphasizes the importance of understanding their needs and providing them with a positive experience. The pattern also recognizes the roles of platform engineers, operations teams, security teams, and compliance teams. However, the connection to external stakeholders, such as end-users and the broader community, is less direct. While the pattern leads to better outcomes for end-users, it does not explicitly include them in the feedback loop.

*   **Score: 4/5**

**2. Value Creation:**

The pattern creates significant value for a wide range of stakeholders. For developers, it reduces cognitive load, increases productivity, and improves the overall developer experience. For the organization, it leads to faster time to market, improved software quality, reduced operational costs, and better security and compliance. For end-users, it results in higher quality products and services. The value created is primarily instrumental, focused on improving the efficiency and effectiveness of the software development process.

*   **Score: 4/5**

**3. Value Preservation:**

The pattern has a strong focus on value preservation. The concept of the IDP as a living product that is continuously improved ensures that it remains relevant over time. The platform team is responsible for keeping the platform up-to-date with the latest technologies and for adapting it to the changing needs of the organization. This product mindset is a key factor in the long-term sustainability of the pattern.

*   **Score: 4/5**

**4. Shared Rights & Responsibilities:**

The pattern establishes a clear division of responsibilities between the platform team and the development teams. The platform team is responsible for the platform, and the development teams are responsible for their applications. This separation of concerns is a key strength of the pattern. However, the rights of the different stakeholders are not as clearly defined. While developers have the right to a good developer experience, their ability to influence the direction of the platform may be limited.

*   **Score: 3/5**

**5. Systematic Design:**

The pattern is highly systematic. It relies on a set of well-defined processes, tools, and architectures to create a streamlined and automated software development lifecycle. The concepts of "golden paths" and "paved roads" are a testament to the systematic nature of the pattern. The use of GitOps for infrastructure and application management further enhances the systematic design of the pattern.

*   **Score: 5/5**

**6. Systems of Systems:**

The pattern is designed to be a system of systems. It integrates a wide range of tools and technologies into a cohesive and effective platform. It also composes well with other patterns, such as DevOps, microservices, and agile development. The IDP acts as a unifying layer that brings together all of the different parts of the software development ecosystem.

*   **Score: 5/5**

**7. Fractal Properties:**

The principles of platform engineering are fractal, meaning that they can be applied at different scales. An organization can start with a small, focused platform for a single team and then gradually expand it to serve the entire organization. The concept of the "thinnest viable platform" is a practical application of this fractal property.

*   **Score: 5/5**

**Overall Score: 4/5 (Commons-Aligned)**

Platform engineering is a highly effective pattern for improving the efficiency and effectiveness of software development in large and complex organizations. It is well-aligned with the principles of the Commons OS framework, particularly in its systematic design, its ability to compose with other patterns, and its fractal properties. The main opportunity for improvement is to strengthen the connection to external stakeholders and to more clearly define the rights of all stakeholders.


### 9. Resources & References

This section provides a curated list of resources for those who want to learn more about platform engineering and Internal Developer Platforms.

**Essential Reading:**

*   **"Team Topologies: Organizing Business and Technology Teams for Fast Flow" by Matthew Skelton and Manuel Pais:** This book provides a foundational understanding of how to organize teams for modern software development. It introduces the concept of a "platform team" as one of the four fundamental team types, which is a core concept in platform engineering.
*   **"The State of DevOps Report" by the DevOps Research and Assessment (DORA) team:** This annual report provides data-driven insights into the practices that lead to high performance in software development. The report consistently shows a strong correlation between the use of internal platforms and elite performance.
*   **Platformengineering.org:** This website is a hub for the platform engineering community, with a wealth of articles, blog posts, and other resources on the topic.

**Organizations & Communities:**

*   **The Cloud Native Computing Foundation (CNCF):** The CNCF is the home of many of the key technologies that are used to build internal platforms, such as Kubernetes and Prometheus. The CNCF also has a number of working groups and special interest groups that are focused on platform engineering.
*   **The Platform Engineering Community:** This is a global community of platform engineers who share best practices and learn from each other. The community has a Slack channel, a newsletter, and a number of local meetup groups.

**Tools & Platforms:**

*   **Backstage:** An open-source platform for building developer portals, created by Spotify and now a CNCF project.
*   **Kubernetes:** An open-source container orchestration platform that is the foundation for many internal platforms.
*   **Terraform:** An open-source infrastructure as code tool that is used to automate the provisioning of infrastructure.
*   **GitLab and GitHub:** These platforms provide a complete DevOps lifecycle, including source code management, CI/CD, and package management.

**References:**

[1] platformengineering.org. (n.d.). *What is platform engineering?* Retrieved from https://platformengineering.org/blog/what-is-platform-engineering

[2] Microsoft. (2025, October 23). *What is Platform Engineering?* Microsoft Learn. Retrieved from https://learn.microsoft.com/en-us/platform-engineering/what-is-platform-engineering

[3] Microsoft. (2025, October 20). *Case studies: Three platform engineering implementations*. Microsoft Learn. Retrieved from https://learn.microsoft.com/en-us/platform-engineering/case-study

[4] Gartner. (2023). *Gartner Predicts 80% of Software Engineering Organizations Will Establish Platform Teams by 2026*. Gartner.

[5] DevOps Research and Assessment (DORA). (2021). *State of DevOps Report*. Google Cloud.

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/platform-engineering-internal-developer-platforms/](https://commons-os.github.io/patterns/domain/platform-engineering-internal-developer-platforms/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/platform-engineering-internal-developer-platforms.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/platform-engineering-internal-developer-platforms.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
