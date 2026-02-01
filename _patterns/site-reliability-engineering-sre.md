---
id: pat_01kg5023zzecsb265cgdd20fs7
page_url: https://commons-os.github.io/patterns/site-reliability-engineering-sre/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/site-reliability-engineering-sre.md
slug: site-reliability-engineering-sre
title: Site Reliability Engineering (SRE)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: design
  category: [practice, framework]
  era: [digital]
  origin: [Google]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: ["pat_01kg5023zseyh85cxgrhc3qpbm"]
specializes_to: ["pat_01kg5023x5fprarvy4w4fqephv", "pat_01kg5023zzecsb265cfpcw0gmn"]
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

## 1. Overview

Site Reliability Engineering (SRE) is a discipline that incorporates aspects of software engineering and applies them to infrastructure and operations problems. The main goals are to create scalable and highly reliable software systems. SRE is what you get when you treat operations as if it’s a software problem. The SRE mindset is to protect, provide for, and progress the software and systems with an ever-watchful eye on their availability, latency, performance, and capacity. SRE is a specific implementation of DevOps, which focuses on building reliable systems, whereas DevOps covers a broader scope of operations. [1] [2]

SRE originated at Google in 2003 when Ben Treynor Sloss was hired to lead a team of software engineers to run a production environment. This new team was tasked with making Google's large-scale sites more reliable, efficient, and scalable. The success of this team led to the growth of SRE within Google and its eventual adoption by the wider software industry. [3]

## 2. Core Principles

SRE is guided by a set of core principles that help to ensure the reliability and stability of large-scale systems. These principles are not a rigid set of rules, but rather a set of guidelines that can be adapted to the specific needs of each organization. [4]

### Embracing Risk

One of the most important principles of SRE is the idea of embracing risk. SREs understand that it is impossible to eliminate all risk from a system, and that trying to do so would be prohibitively expensive and time-consuming. Instead, SREs work to manage and mitigate risk, and to ensure that the system is able to withstand a certain level of failure. This is done through the use of error budgets, which are a tool for balancing the need for reliability with the need for innovation. [5]

### Service Level Objectives (SLOs)

Service Level Objectives (SLOs) are a key part of the SRE toolkit. SLOs are specific, measurable targets for reliability that are agreed upon by all stakeholders. They provide a clear and objective way to measure the performance of a system, and to determine whether it is meeting the needs of its users. SLOs are typically defined in terms of availability, latency, and error rate. [6]

### Eliminating Toil

Toil is the kind of work that is manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows. SREs are constantly looking for ways to eliminate toil, as it is a major source of inefficiency and human error. This is done through the use of automation, which is a core principle of SRE. [7]

### Monitoring

Monitoring is another essential principle of SRE. SREs use monitoring to gain insights into the health and performance of their systems. This information is used to detect and diagnose problems, to track the performance of the system over time, and to identify areas for improvement. SREs use a variety of monitoring tools, including white-box monitoring, which provides insights into the internal state of the system, and black-box monitoring, which tests the system from the outside, as a user would. [8]

### Automation

Automation is a core principle of SRE. SREs use automation to eliminate toil, to improve the reliability of their systems, and to make their work more efficient. Automation is used for a wide variety of tasks, including provisioning, configuration management, and release engineering. [9]

### Release Engineering

Release engineering is the process of building, testing, and deploying software. SREs are heavily involved in the release engineering process, as it is a major source of risk to the reliability of a system. SREs work to ensure that the release process is as automated and reliable as possible, and that it is able to be rolled back quickly in the event of a problem. [10]

### Simplicity

Simplicity is a key principle of SRE. SREs strive for simplicity in system design and operation, as it is a key factor in reliability. Complex systems are more difficult to understand, to debug, and to operate, and they are more likely to fail in unexpected ways. SREs work to reduce complexity wherever possible, and to ensure that the system is as simple as it can be. [11]

## 3. Key Practices

In addition to the core principles, there are a number of key practices that are common to most SRE teams. These practices help to put the principles of SRE into action, and to ensure that the system is as reliable as possible.

### On-Call and Incident Response

One of the most important practices of SRE is the on-call rotation. SREs are on-call to respond to incidents and to ensure that the system is always available. When an incident occurs, the on-call SRE is responsible for diagnosing the problem, mitigating the impact, and restoring service as quickly as possible. [12]

### Postmortems

After every incident, SREs conduct a postmortem to determine the root cause of the problem and to identify ways to prevent it from happening again. Postmortems are a key part of the SRE learning process, and they help to ensure that the system is constantly improving. Postmortems are blameless, and they focus on the technical and process-related causes of the incident, rather than on individual human error. [13]

### Testing for Reliability

SREs use a variety of testing techniques to ensure the reliability of their systems. These include unit testing, integration testing, and end-to-end testing. SREs also use a technique called chaos engineering, which involves intentionally injecting failures into the system to see how it responds. This helps to identify weaknesses in the system and to ensure that it is able to withstand a certain level of failure. [14]

### Capacity Planning

Capacity planning is the process of ensuring that the system has enough capacity to meet the needs of its users. SREs use a variety of techniques to forecast future demand and to ensure that the system is able to scale to meet that demand. This includes load testing, which is used to determine the maximum capacity of the system, and trend analysis, which is used to predict future growth. [15]

### Development

SREs are software engineers, and they spend a significant amount of their time writing code. This code is used to automate tasks, to build tools, and to improve the reliability of the system. SREs are also involved in the design and development of new features, and they work to ensure that these features are as reliable as possible. [16]

### Product

SREs work closely with product managers to ensure that the reliability of the system is taken into account when new features are being developed. SREs help to define the SLOs for new features, and they work to ensure that the system is able to meet those SLOs. SREs also work to ensure that the system is as user-friendly as possible, and that it provides a good user experience. [17]

## 4. Application Context

Site Reliability Engineering is most applicable in the context of large-scale, complex, and mission-critical systems. It is particularly well-suited for organizations that are running services that need to be highly available and that are constantly evolving. SRE is not a good fit for all organizations, and it is important to carefully consider the specific needs of your organization before adopting SRE. [18]

SRE is most effective when it is implemented as a partnership between the SRE team and the development teams. The SRE team is responsible for the reliability of the system, but they cannot do it alone. The development teams need to be on board with the principles of SRE, and they need to be willing to work with the SRE team to ensure that the system is as reliable as possible. [19]

SRE is also most effective when it is implemented in a culture of blamelessness. When an incident occurs, the focus should be on learning from the incident and on preventing it from happening again. It is important to create an environment where people feel safe to admit their mistakes and to learn from them. [20]

## 5. Implementation

Implementing SRE in an organization is a significant undertaking that requires a cultural shift and a commitment from all stakeholders. There are a number of different ways to implement SRE, and the best approach will depend on the specific needs of your organization. [21]

### Building an SRE Team

The first step in implementing SRE is to build an SRE team. This team should be made up of software engineers who have a strong understanding of both software development and operations. The team should be given the autonomy to make decisions about the reliability of the system, and they should be empowered to make changes to the system as needed. [22]

### Defining SLOs and Error Budgets

Once you have an SRE team in place, the next step is to define your SLOs and error budgets. This is a critical step, as it will provide a clear and objective way to measure the reliability of your system. The SLOs should be agreed upon by all stakeholders, and they should be regularly reviewed and updated as needed. [23]

### Adopting SRE Practices

Once you have your SLOs and error budgets in place, you can begin to adopt the other SRE practices, such as on-call and incident response, postmortems, and testing for reliability. It is important to adopt these practices gradually, and to ensure that they are well-understood by all stakeholders. [24]

### Fostering a Culture of Reliability

Finally, it is important to foster a culture of reliability throughout the organization. This means that everyone, from the CEO to the individual contributor, needs to be committed to the reliability of the system. It is important to create an environment where people feel safe to admit their mistakes and to learn from them. [25]

## 6. Evidence & Impact

The adoption of Site Reliability Engineering has had a significant impact on the software industry. It has been shown to improve the reliability and availability of large-scale systems, while also increasing the efficiency of the teams that operate them. [26]

One of the most well-known examples of the impact of SRE is Google. Google has been using SRE for over two decades, and it has been a key factor in the company's ability to scale its services to billions of users. Google's SRE teams are responsible for the reliability of all of the company's major services, including Search, Gmail, and YouTube. [27]

Another example of the impact of SRE is Netflix. Netflix adopted SRE in 2010, and it has been a key factor in the company's ability to scale its streaming service to over 200 million subscribers. Netflix's SRE teams are responsible for the reliability of the company's entire streaming infrastructure, from the data centers to the client applications. [28]

In addition to these large-scale examples, there are many other organizations that have successfully adopted SRE. These organizations have seen a number of benefits, including:

*   **Improved reliability and availability:** SRE has been shown to improve the reliability and availability of large-scale systems. This is due to a number of factors, including the use of SLOs, the focus on automation, and the practice of blameless postmortems. [29]
*   **Increased efficiency:** SRE has been shown to increase the efficiency of the teams that operate large-scale systems. This is due to a number of factors, including the focus on eliminating toil, the use of automation, and the practice of sharing knowledge. [30]
*   **Improved culture:** SRE has been shown to improve the culture of the organizations that adopt it. This is due to a number of factors, including the focus on blamelessness, the practice of sharing knowledge, and the emphasis on collaboration. [31]

## 7. Cognitive Era Considerations

The rise of the cognitive era, characterized by the increasing importance of data, machine learning, and artificial intelligence, presents both new challenges and opportunities for Site Reliability Engineering. SRE practices must evolve to manage the unique complexities of AI-powered systems, which are often non-deterministic and data-dependent. [32]

### AIOps

AIOps is the application of artificial intelligence to IT operations. AIOps tools can be used to automate many of the tasks that are traditionally performed by SREs, such as monitoring, incident response, and root cause analysis. AIOps can also be used to identify potential problems before they occur, and to provide recommendations for how to prevent them. [33]

### MLOps

MLOps is the application of DevOps principles to machine learning. MLOps is a critical part of the SRE toolkit in the cognitive era, as it helps to ensure that machine learning models are reliable, scalable, and maintainable. MLOps includes a number of practices, such as data validation, model testing, and model versioning. [34]

### Data Reliability Engineering

Data Reliability Engineering (DRE) is a new discipline that is emerging in the cognitive era. DRE is focused on ensuring the reliability of data pipelines and data products. DREs work to ensure that data is accurate, complete, and timely. They also work to ensure that data is available to the people who need it, when they need it. [35]

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
SRE primarily defines Rights and Responsibilities between software development and operations teams, with a focus on system reliability. Through Service Level Objectives (SLOs), it implicitly includes end-users as stakeholders whose experience is paramount. However, it does not explicitly architect for the Rights and Responsibilities of non-technical stakeholders like the environment or future generations.

**2. Value Creation Capability:**
The pattern excels at creating resilience and knowledge value. By treating operations as a software problem, SRE enables the collective capability to maintain highly reliable and scalable systems, which is a direct form of resilience value. The practice of blameless postmortems and a focus on automation fosters a culture of continuous learning and knowledge creation.

**3. Resilience & Adaptability:**
Resilience and adaptability are at the core of the SRE pattern. Practices like chaos engineering, error budgets, and automated, gradual rollouts are designed to help systems thrive on change and maintain coherence under stress. SRE helps systems adapt to complexity by providing a framework for managing risk and learning from failure.

**4. Ownership Architecture:**
SRE defines ownership as stewardship and responsibility for a service's reliability, rather than monetary equity. The use of error budgets empowers teams to 'own' the trade-offs between reliability and innovation for their service. This aligns with a broader definition of ownership based on Rights and Responsibilities.

**5. Design for Autonomy:**
The pattern is highly compatible with autonomous systems. Its emphasis on automation, monitoring, and clear SLOs provides a robust framework for managing the reliability of AI, DAOs, and other distributed systems. The low coordination overhead achieved through automation makes it well-suited for an autonomous future.

**6. Composability & Interoperability:**
SRE is a set of principles and practices, not a rigid standard, making it highly composable with other patterns like DevOps. It can be adapted to different organizational contexts and interoperates with a wide variety of tools and platforms. This allows it to be a building block in larger value-creation systems.

**7. Fractal Value Creation:**
The core logic of SRE—defining SLOs, managing error budgets, and automating operations—can be applied at multiple scales. This value-creation logic is fractal, applicable to a single microservice, a complex product, or even an entire organization's technical infrastructure.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
SRE is a powerful enabler of collective value creation, particularly in the digital realm. It provides a robust architecture for building resilient, adaptable, and scalable systems, which are foundational for any modern commons. While its stakeholder architecture is currently focused on technical and user stakeholders, its principles of shared responsibility, learning from failure, and managing complex systems are highly aligned with a commons-based approach.

**Opportunities for Improvement:**
- Explicitly include a wider range of stakeholders (e.g., social, ecological) in the definition of SLOs and error budgets.
- Develop practices for assessing and improving the social and ecological reliability of systems, in addition to technical reliability.
- Extend the concept of blameless postmortems to address not just technical failures, but also failures to meet broader social or ecological goals.

## 9. Resources & References

[1] Google. (n.d.). *Site Reliability Engineering*. Retrieved from https://sre.google/

[2] Wikipedia. (2023, October 26). *Site reliability engineering*. Retrieved from https://en.wikipedia.org/wiki/Site_reliability_engineering

[3] Sloss, B. T. (2014, November 19). *Keys to SRE*. Google Cloud Blog. Retrieved from https://cloud.google.com/blog/products/gcp/keys-to-sre

[4] Treynor, B., et al. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media.

[5] Jones, C., et al. (2018). *The Site Reliability Workbook: Practical Ways to Implement SRE*. O'Reilly Media.

[6] Google. (n.d.). *Service Level Objectives*. Retrieved from https://sre.google/sre-book/service-level-objectives/

[7] Google. (n.d.). *Eliminating Toil*. Retrieved from https://sre.google/sre-book/eliminating-toil/

[8] Google. (n.d.). *Monitoring Distributed Systems*. Retrieved from https://sre.google/sre-book/monitoring-distributed-systems/

[9] Google. (n.d.). *Automation at Google*. Retrieved from https://sre.google/sre-book/automation-at-google/

[10] Google. (n.d.). *Release Engineering*. Retrieved from https://sre.google/sre-book/release-engineering/

[11] Google. (n.d.). *Simplicity*. Retrieved from https://sre.google/sre-book/simplicity/

[12] Google. (n.d.). *Being On-Call*. Retrieved from https://sre.google/sre-book/being-on-call/

[13] Google. (n.d.). *Postmortem Culture: Learning from Failure*. Retrieved from https://sre.google/sre-book/postmortem-culture/

[14] Basiri, A., et al. (2016). *Chaos Engineering*. O'Reilly Media.

[15] Google. (n.d.). *Capacity Planning*. Retrieved from https://sre.google/sre-book/capacity-planning/

[16] Google. (n.d.). *Software Engineering in SRE*. Retrieved from https://sre.google/sre-book/software-engineering-in-sre/

[17] Google. (n.d.). *Product Reliability*. Retrieved from https://sre.google/sre-book/product-reliability/

[18] Beyer, B., et al. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly Media.

[19] Jones, C., et al. (2018). *The Site Reliability Workbook: Practical Ways to Implement SRE*. O'Reilly Media.

[20] Google. (n.d.). *Postmortem Culture: Learning from Failure*. Retrieved from https://sre.google/sre-book/postmortem-culture/

[21] Jones, C., et al. (2018). *The Site Reliability Workbook: Practical Ways to Implement SRE*. O'Reilly Media.

[22] Google. (n.d.). *Building Secure and Reliable Systems*. Retrieved from https://sre.google/sre-book/building-secure-and-reliable-systems/

[23] Google. (n.d.). *Service Level Objectives*. Retrieved from https://sre.google/sre-book/service-level-objectives/

[24] Jones, C., et al. (2018). *The Site Reliability Workbook: Practical Ways to Implement SRE*. O'Reilly Media.

[25] Google. (n.d.). *Postmortem Culture: Learning from Failure*. Retrieved from https://sre.google/sre-book/postmortem-culture/

[26] Dynatrace. (2021, June 3). *What is SRE? Site reliability engineering explained*. Retrieved from https://www.dynatrace.com/news/blog/what-is-site-reliability-engineering/

[27] Google. (n.d.). *Site Reliability Engineering*. Retrieved from https://sre.google/

[28] Netflix Technology Blog. (2016, August 19). *The Netflix Simian Army*. Retrieved from https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116

[29] Amazon Web Services. (n.d.). *What is Site Reliability Engineering?*. Retrieved from https://aws.amazon.com/what-is/sre/

[30] Nautilus Technologies. (2020, August 12). *Benefits of Site Reliability Engineering (SRE)*. Medium. Retrieved from https://medium.com/@Nautilus_Technologies/benefits-of-site-reliability-engineering-sre-b47c016120db

[31] Relout. (n.d.). *4 Key Benefits of Implementing Site Reliability Engineering (SRE) in Your Organization*. Retrieved from https://relout.cloud/article/4-key-benefits-of-implementing-site-reliability-engineering-sre-in-your-organization/

[32] HashiCorp. (2021, September 21). *The Future of SRE in a Cognitive Era*. Retrieved from https://www.hashicorp.com/blog/the-future-of-sre-in-a-cognitive-era

[33] Moogsoft. (n.d.). *What is AIOps?*. Retrieved from https://www.moogsoft.com/what-is-aiops

[34] Google Cloud. (n.d.). *What is MLOps?*. Retrieved from https://cloud.google.com/mlops

[35] Barr, D. (2021, October 26). *What is Data Reliability Engineering?*. Monte Carlo. Retrieved from https://www.montecarlodata.com/what-is-data-reliability-engineering/
