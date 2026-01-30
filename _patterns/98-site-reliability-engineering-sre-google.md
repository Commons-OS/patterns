---
id: pat_01kg5023x5fprarvy4w4fqephv
page_url: https://commons-os.github.io/patterns/98-site-reliability-engineering-sre-google/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/98-site-reliability-engineering-sre-google.md
slug: 98-site-reliability-engineering-sre-google
title: Site Reliability Engineering (SRE) - Google
aliases: [SRE]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: design
  category: practice
  era: digital
  origin: [google]
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: ["pat_01kg5023zzecsb265cgdd20fs7", "pat_01kg5023zseyh85cxgrhc3qpbm"]
specializes_to: ["pat_01kg5023zzecsb265cfpcw0gmn"]
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources:
  - "https://sre.google/"
  - "https://sre.google/sre-book/part-II-principles/"
  - "https://sre.google/sre-book/service-best-practices/"
  - "https://sre.google/workbook/slo-engineering-case-studies/"
  - "https://www.devopsinstitute.com/case-studies/"
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

## 1. Overview

Site Reliability Engineering (SRE) is a discipline that incorporates aspects of software engineering and applies them to infrastructure and operations problems. The main goals are to create scalable and highly reliable software systems. Coined by Benjamin Treynor Sloss at Google in 2003, SRE was born out of the need to have a more reliable and scalable way to manage Google's large-scale systems [1]. SRE teams are responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their services. SRE is what you get when you treat operations as a software problem. It's a model that moves away from the traditional separation of development and operations teams, instead promoting a model where both teams share ownership of the production environment. This shared ownership model is a key tenet of the DevOps movement, and SRE is often seen as a specific implementation of DevOps.

## 2. Core Principles

Site Reliability Engineering is built on a foundation of several core principles that guide its implementation and practice. These principles are not just theoretical concepts but are actively applied in the day-to-day work of SRE teams. A key principle is **embracing risk**, as SRE acknowledges that 100% reliability is an impossible goal. Instead, it manages reliability by defining a service's acceptable level of unreliability and using that as a budget. This "error budget" allows for a data-driven approach to balancing reliability work with the need to release new features. **Service Level Objectives (SLOs)** are another key component of SRE. They are specific, measurable targets for a service's reliability, such as uptime or latency. By setting and monitoring SLOs, SRE teams can objectively assess whether a service is meeting its reliability goals [2]. SRE also focuses on **eliminating toil**, which is the repetitive, manual, and automatable work that provides no enduring value. SRE aims to eliminate toil by automating as many tasks as possible. This frees up engineers to focus on more strategic work, such as improving system design and developing new features. **Monitoring** is another essential principle, as comprehensive monitoring provides the data needed to track SLOs, detect and diagnose problems, and understand system behavior. SRE teams use a variety of monitoring tools and techniques to gain deep insights into their services. **Automation** is a cornerstone of SRE. By automating operational tasks, SRE teams can improve efficiency, reduce human error, and scale their services more effectively. Automation is applied to a wide range of tasks, from provisioning infrastructure to deploying code. **Release engineering** is also a critical principle, as SRE places a strong emphasis on safe and reliable release engineering. This includes practices such as canary deployments, gradual rollouts, and automated testing to minimize the risk of introducing bugs into production. Finally, SRE strives for **simplicity** in system design and operation. Complex systems are harder to understand, debug, and maintain. By keeping systems as simple as possible, SRE teams can improve their reliability and reduce the likelihood of failures.

## 3. Key Practices

SRE is a practical discipline, and its success depends on the implementation of a set of key practices. These practices are designed to ensure that services are reliable, scalable, and efficient. One of the most important practices is the **on-call** rotation, where SRE teams respond to production incidents. The goal of on-call is not just to fix problems as they occur, but also to identify and address the root causes of those problems to prevent them from happening again. **Incident management** is another key practice, and SRE has a structured approach to incident management that emphasizes clear communication, collaboration, and a blameless postmortem culture. The goal is to learn from every incident and use that knowledge to improve the reliability of the system. **Postmortems** are a critical part of the SRE process. They are written documents that describe an incident, its impact, the actions taken to mitigate it, and the root cause. The goal of a postmortem is not to blame individuals, but to learn from the incident and prevent it from recurring. **Capacity planning** is another important practice, as SRE teams are responsible for capacity planning to ensure that their services can handle current and future demand. This involves forecasting traffic growth, load testing, and provisioning resources accordingly [3]. **Change management** is also a key practice, and SRE has a rigorous change management process to minimize the risk of introducing bugs into production. This includes practices such as code review, automated testing, and gradual rollouts. **Testing for reliability** is another important practice, and SRE teams use a variety of testing techniques to ensure the reliability of their services. This includes unit testing, integration testing, load testing, and chaos engineering. Finally, **observability** is a key practice, as SRE relies on observability to understand the behavior of complex systems. This includes monitoring, logging, and tracing to provide deep insights into system performance and health.

## 4. Application Context

SRE is most effectively applied in the context of large-scale, complex systems where reliability is a critical concern. It is particularly well-suited for organizations that are committed to a DevOps culture and are willing to invest in the engineering resources required to implement SRE practices. SRE is not a one-size-fits-all solution, and its application should be tailored to the specific needs of the organization and the services it provides. For example, a consumer-facing service with millions of users will have different reliability requirements than an internal service with a small number of users. SRE is also a good fit for organizations that are looking to move away from a traditional, reactive operations model to a more proactive, data-driven approach. By embracing the principles of SRE, organizations can improve the reliability of their services, increase the velocity of their development teams, and reduce the operational overhead of managing complex systems.

## 5. Implementation

Implementing SRE is a journey, not a destination. It requires a cultural shift and a commitment to continuous improvement. A good starting point is to **start small and iterate**. Instead of a large-scale rollout, begin with a single service or a small team and refine SRE practices over time. This allows for learning and adaptation. A crucial first step is to **define SLOs**, which are clear and measurable Service Level Objectives for your services. This provides a data-driven way to assess service reliability and make informed decisions about engineering investments. It is also important to **establish a blameless postmortem culture**. This is essential for learning from incidents and preventing them from recurring. When an incident occurs, the focus should be on understanding the root cause and identifying systemic issues, not on blaming individuals. **Automating everything** is another key aspect of SRE implementation. Start by automating repetitive, manual tasks to free up engineers for more strategic work. As the SRE practice matures, this can be extended to more advanced automation, such as automated incident response and self-healing systems. Building a **diverse team** is also important. SRE teams should be composed of individuals with a mix of software engineering and operations skills to ensure the right expertise to tackle a wide range of challenges. Finally, it is important to **choose the right tools**. A wide variety of tools are available to support SRE practices, from monitoring and alerting to incident management and automation. The key is to choose the tools that are the best fit for the organization and its specific needs.

## 6. Evidence & Impact

The impact of SRE can be seen in the improved reliability, scalability, and efficiency of the services that it is applied to. By embracing the principles of SRE, organizations can reduce the frequency and duration of outages, improve the user experience, and increase the velocity of their development teams. Several case studies provide evidence of the impact of SRE in the real world. For example, **Evernote**, the popular note-taking app, adopted SRE to improve the reliability of its service. By implementing SLOs and an error budget, Evernote was able to reduce the number of user-facing errors by 50% and improve the availability of its service to 99.99% [4]. **The Home Depot**, the largest home improvement retailer in the United States, also adopted SRE to improve the reliability of its e-commerce platform. By implementing SRE practices, The Home Depot was able to reduce the number of critical incidents by 70% and improve the availability of its platform to 99.99% [4]. **Standard Chartered Bank**, a multinational banking and financial services company, adopted SRE to improve the reliability of its core banking systems. By implementing SRE practices, Standard Chartered Bank was able to reduce the number of production incidents by 90% and improve the availability of its systems to 99.999% [5].

## 7. Cognitive Era Considerations

The cognitive era, characterized by the rise of artificial intelligence and machine learning, is having a profound impact on the field of Site Reliability Engineering. AI and ML are being used to automate and enhance many aspects of SRE, from monitoring and alerting to incident response and root cause analysis. For example, AI-powered monitoring tools can be used to detect anomalies and predict failures before they occur. Machine learning algorithms can be used to analyze large volumes of log data to identify the root cause of incidents more quickly and accurately. And AI-powered automation can be used to remediate incidents without human intervention. As AI and ML continue to mature, they will become increasingly integral to the practice of SRE. SRE teams that embrace these technologies will be better equipped to manage the complexity of modern systems and ensure the reliability of their services.

## 8. Commons Alignment Assessment

Site Reliability Engineering (SRE) demonstrates a significant alignment with the principles of the commons, particularly in its emphasis on shared resources, collaborative practices, and the open exchange of knowledge. While SRE originated within a corporate environment, its core tenets have been widely adopted and adapted by the broader technology community, fostering a sense of collective ownership and shared responsibility for the reliability of digital services. The SRE community thrives on the open sharing of best practices, tools, and lessons learned, which is evident in the extensive body of literature, open-source tools, and community forums dedicated to the discipline. This culture of open collaboration and knowledge sharing is a hallmark of a healthy commons. Furthermore, the SRE principle of blameless postmortems promotes a culture of transparency and collective learning, where failures are treated as opportunities for improvement rather than individual shortcomings. This aligns with the commons principle of shared governance and collective responsibility. The SRE model also encourages the development of shared, reusable tools and automation, which can be seen as a form of digital commons. By investing in shared infrastructure and automation, SRE teams can reduce duplicative effort and create a more efficient and sustainable operational environment for everyone. Overall, the SRE pattern embodies the spirit of the commons by promoting a culture of collaboration, knowledge sharing, and collective ownership of digital infrastructure.

## 9. Resources & References

For those interested in learning more about Site Reliability Engineering, there are a wealth of resources available. The foundational text on SRE is **"Site Reliability Engineering: How Google Runs Production Systems"** by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, which provides a detailed overview of the principles and practices of SRE at Google. Another valuable resource is **"The Site Reliability Workbook: Practical Ways to Implement SRE"** by Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, and Stephen Thorne, which provides practical advice and real-world examples of how to implement SRE. For a comprehensive guide to building secure and reliable systems, with a focus on the intersection of security and reliability, see **"Building Secure and Reliable Systems: Best Practices for Designing, Implementing, and Maintaining Systems"** by Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, and Adam Stubblefield. In addition to these books, there are several websites that provide valuable information on SRE. **sre.google** is the official website for Google SRE, and it contains a wealth of information on SRE, including articles, books, and videos. **The SRE Manifesto** provides a concise overview of the principles of SRE, as well as a curated list of resources. Finally, **SRE Weekly** is a weekly newsletter that curates the best articles, talks, and news about SRE.

[1]: https://sre.google/
[2]: https://sre.google/sre-book/part-II-principles/
[3]: https://sre.google/sre-book/service-best-practices/
[4]: https://sre.google/workbook/slo-engineering-case-studies/
[5]: https://www.devopsinstitute.com/case-studies/

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/98-site-reliability-engineering-sre-google/](https://commons-os.github.io/patterns/domain/98-site-reliability-engineering-sre-google/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/98-site-reliability-engineering-sre-google.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/98-site-reliability-engineering-sre-google.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
