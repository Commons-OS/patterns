---
id: pat_01kg5023xsf58b5cjefwzpfedw
page_url: https://commons-os.github.io/patterns/domain/chaos-engineering/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/chaos-engineering.md
slug: chaos-engineering
title: Chaos Engineering
aliases: [Resilience Engineering, Failure Injection Testing]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: design
  category: [practice]
  era: [digital]
  origin: [netflix]
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: [https://www.ibm.com/think/topics/chaos-engineering, https://en.wikipedia.org/wiki/Chaos_engineering, https://www.gremlin.com/community/tutorials/chaos-engineering-the-history-principles-and-practice, https://steadybit.com/case-studies/, https://aws.amazon.com/blogs/publicsector/chaos-engineering-made-clear-generate-aws-fis-experiments-using-natural-language-through-amazon-bedrock/]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview (150-300 words)

Chaos Engineering is the discipline of experimenting on a software system in production to build confidence in its capability to withstand turbulent and unexpected conditions. It is a proactive approach to identifying systemic weaknesses by intentionally injecting controlled failures, such as server outages, network latency, or resource exhaustion. The goal is not to break the system, but to uncover hidden issues and vulnerabilities that could lead to major outages or customer-facing problems. By deliberately introducing and studying failures in a controlled environment, organizations can improve system resilience, reduce downtime, and enhance their understanding of complex distributed systems. This practice, pioneered by companies like Netflix, has become an essential component of modern software development and operations (SRE) for building highly reliable and fault-tolerant applications.

### 2. Core Principles (3-7 principles, 200-400 words)

Chaos Engineering is guided by a set of core principles that ensure experiments are conducted safely and effectively. These principles, first articulated by the pioneers of the practice, provide a framework for building confidence in system resilience.

A fundamental principle is to **build a hypothesis around steady-state behavior**. Before any failure injection, a clear, measurable understanding of the system's normal operational state is established. This baseline, which could be defined by metrics like requests per second or error rates, represents a healthy system. The core hypothesis of any chaos experiment is that the system will successfully maintain this steady state despite the introduced failure.

Experiments must **vary real-world events** to be effective. Chaos Engineering simulates a broad spectrum of failure scenarios, from server crashes and network latency to disk failures and entire datacenter outages. By systematically varying the types and magnitudes of these disruptive events, teams can uncover a more comprehensive range of potential vulnerabilities.

A central tenet of the practice is to **run experiments in production**. Although it may seem counterintuitive, this is essential because production environments are complex, dynamic, and impossible to fully replicate in staging or testing. Experimenting in the live environment provides the most accurate understanding of how a system will behave when confronted with real-world failures.

To maintain resilience over time, it is vital to **automate experiments to run continuously**. This ensures that the system is constantly being tested against a variety of failure scenarios, allowing teams to proactively identify and mitigate new weaknesses as they emerge.

Finally, a critical safety principle is to **minimize the blast radius** of any experiment. This involves limiting the potential impact on customers by starting with small, controlled experiments and gradually increasing their scope. For instance, an experiment might initially target a single server or a small cohort of users before being expanded to a larger portion of the system.

### 3. Key Practices (5-10 practices, 300-600 words)

Several key practices have emerged from the field of Chaos Engineering, enabling organizations to systematically improve the resilience of their systems.

One of the most effective practices is the **GameDay**, popularized by Amazon. These are planned events where teams collaboratively simulate failures in a controlled environment. The focus is not on assigning blame but on collective learning about how the system and the team respond to various failure scenarios. GameDays serve as an excellent method for training engineers, validating incident response procedures, and uncovering hidden dependencies within the system.

At the heart of Chaos Engineering is **fault injection**, the deliberate introduction of faults into a system. These faults can be injected at various levels, including the infrastructure (e.g., terminating a virtual machine), the network (e.g., introducing latency or packet loss), or the application (e.g., forcing an exception). The primary objective is to observe the system's behavior under duress and identify its weaknesses in handling such faults.

To achieve a state of continuous resilience, the automation of chaos experiments is paramount. **Automated Chaos Experiments** involve using a dedicated platform or tool to regularly and automatically inject faults and monitor the system's response. This ensures that the system is perpetually tested against a diverse range of failure scenarios, providing ongoing confidence in its resilience.

Effective **monitoring and alerting** are non-negotiable prerequisites for Chaos Engineering. Comprehensive visibility into the system's key metrics is required before, during, and after an experiment. This enables teams to accurately assess the impact of the experiment, promptly detect any adverse consequences, and execute a rollback if necessary.

A crucial safety measure is **limiting the blast radius** of an experiment. This is achieved by carefully controlling the scope of the experiment, starting with a small number of users or a single server, and incrementally expanding the scope as confidence in the system's resilience increases. A well-defined rollback plan is also essential to mitigate any unforeseen negative impacts.

Finally, Chaos Engineering serves as a powerful tool for **incident response training**. It is not solely about unearthing technical vulnerabilities; it is also about enhancing the team's ability to respond to incidents effectively. By simulating real-world failures, Chaos Engineering provides a safe and practical environment for engineers to hone their incident response skills, building the muscle memory required to resolve outages quickly and efficiently.

### 4. Application Context (200-300 words)

Chaos Engineering is most applicable and valuable in the context of complex, distributed systems where the potential for unpredictable failures is high. Modern cloud-native applications, microservices architectures, and large-scale online services are prime candidates for this practice. In such environments, it is practically impossible to anticipate all the ways in which the system can fail. The interdependencies between services, the dynamic nature of the infrastructure, and the sheer scale of these systems create a level of complexity that traditional testing methods cannot adequately address.

Organizations that rely on high availability and reliability to deliver their services, such as e-commerce platforms, financial institutions, and streaming media providers, have been early adopters of Chaos Engineering. For these companies, even a few minutes of downtime can result in significant financial losses and damage to their brand reputation. By proactively identifying and addressing weaknesses, Chaos Engineering helps these organizations to build more robust and resilient systems that can withstand the inevitable failures of a distributed environment.

However, the principles of Chaos Engineering are not limited to large-scale, web-based systems. The practice can also be applied to a wide range of other systems, including embedded systems, industrial control systems, and even organizational processes. Any system that is critical to the success of an organization and has the potential for unexpected failures can benefit from the principles of Chaos Engineering.

### 5. Implementation (400-600 words)

Implementing Chaos Engineering requires a systematic and disciplined approach. It is not about randomly causing chaos, but about conducting well-planned experiments to learn about the system's behavior. The following steps provide a general guide for implementing a Chaos Engineering practice.

First, it is essential to establish a strong foundation of monitoring and observability. Before you can start injecting failures, you need to have a clear understanding of your system's steady-state behavior. This involves identifying key business and system metrics, such as the number of transactions per second, the error rate, and the latency of critical services. These metrics will serve as the baseline for your experiments and will allow you to measure the impact of the failures you introduce.

Next, you should start by conducting small, manual experiments in a pre-production environment. This will allow you to get familiar with the process of Chaos Engineering and to build confidence in your ability to conduct experiments safely. A good starting point is to conduct a GameDay, where the team comes together to manually inject a simple failure, such as shutting down a non-critical service. The goal of this exercise is not to find a major flaw, but to learn about the process of conducting an experiment and to build the muscle memory for incident response.

Once you have gained some experience with manual experiments, you can start to automate the process. This involves using a Chaos Engineering tool or building your own platform to automatically inject failures into the system. There are a number of open-source and commercial tools available, such as Chaos Monkey, Gremlin, and Steadybit, that can help you to automate your experiments. When automating experiments, it is important to start with a small blast radius and to gradually increase the scope of the experiment as you gain confidence in the system's resilience.

Finally, it is crucial to have a clear process for analyzing the results of your experiments and for taking action on your findings. This involves not only identifying the technical weaknesses that were uncovered, but also understanding the organizational and process-related issues that may have contributed to them. The goal of Chaos Engineering is not just to find and fix bugs, but to continuously improve the resilience of the entire system, including the people and processes that support it.

### 6. Evidence & Impact (300-500 words)

The adoption of Chaos Engineering has had a significant and measurable impact on the reliability and resilience of software systems. Numerous case studies and industry reports have demonstrated the effectiveness of this practice in reducing downtime, improving system performance, and increasing organizational confidence.

One of the most well-known examples is Netflix, the pioneer of Chaos Engineering. By continuously injecting failures into their production environment, Netflix has been able to build a highly resilient streaming service that can withstand a wide range of failures, from the loss of a single server to the outage of an entire AWS region. This has resulted in a significant reduction in customer-facing outages and has helped Netflix to become one of the most reliable streaming services in the world.

Other companies have also reported significant benefits from adopting Chaos Engineering. For example, Salesforce, a leading provider of cloud-based software, used Chaos Engineering to improve the resilience of its platform and to achieve a 99.99% uptime. Similarly, ManoMano, a European e-commerce platform, used Chaos Engineering to identify and fix weaknesses in its system, leading to a significant reduction in incidents and an improvement in overall system reliability.

Beyond these specific examples, industry-wide studies have also shown the positive impact of Chaos Engineering. The "State of Chaos Engineering" report, published annually by Gremlin, has consistently found that organizations that practice Chaos Engineering experience fewer outages, have a lower mean time to resolution (MTTR), and are more confident in the resilience of their systems. The report also found that teams that regularly run chaos experiments are more likely to have a high level of availability, with many achieving 99.9% uptime or better.

In summary, the evidence is clear: Chaos Engineering is a powerful practice that can have a significant and positive impact on the reliability and resilience of software systems. By proactively identifying and addressing weaknesses, organizations can build more robust systems, reduce downtime, and ultimately deliver a better experience to their customers.

### 7. Cognitive Era Considerations (200-400 words)

The advent of the Cognitive Era, characterized by the widespread adoption of artificial intelligence (AI) and machine learning (ML), introduces new challenges and opportunities for Chaos Engineering. As systems become more intelligent and autonomous, their failure modes can become even more complex and unpredictable. AI-powered systems can exhibit emergent behaviors that are not explicitly programmed, making it difficult to anticipate all the ways in which they might fail.

In this context, Chaos Engineering becomes even more critical for ensuring the resilience of these systems. By injecting failures into AI-powered systems, we can gain a better understanding of how they behave under stress and identify potential weaknesses in their design. For example, we can use Chaos Engineering to test the resilience of an ML model to noisy or incomplete data, or to test the ability of an autonomous system to recover from a sensor failure.

Furthermore, AI and ML can also be used to enhance the practice of Chaos Engineering itself. For example, we can use ML to analyze the results of chaos experiments and to identify patterns that might indicate a potential weakness. We can also use AI to automatically generate new chaos experiments based on the system's current state and past failures. This can help us to more efficiently and effectively explore the space of possible failures and to build more resilient systems.

In the Cognitive Era, Chaos Engineering is not just about testing the resilience of individual components, but about understanding the systemic behavior of complex, intelligent systems. It is about building confidence in our ability to operate these systems safely and reliably, even in the face of unforeseen circumstances.

### 8. Commons Alignment Assessment (600-800 words)

Chaos Engineering, while primarily a technical practice, has significant implications for the development of a healthy and resilient digital commons. Its principles and practices can be seen as a form of collective learning and knowledge sharing, which are essential for building and maintaining shared resources.

From a commons perspective, Chaos Engineering can be viewed as a mechanism for building collective intelligence about the behavior of complex systems. By openly sharing the results of chaos experiments, organizations can help to create a shared understanding of common failure modes and best practices for building resilient systems. This knowledge can then be used by others to improve the resilience of their own systems, leading to a more robust and reliable digital infrastructure for everyone.

Furthermore, the practice of Chaos Engineering can help to foster a culture of collaboration and shared responsibility. When teams come together to conduct GameDays and other chaos experiments, they are not just testing the system, but also building social capital and trust. They are learning to work together to solve complex problems and to take collective ownership of the resilience of the system. This sense of shared ownership is a key characteristic of a healthy commons.

However, there are also potential tensions between the practice of Chaos Engineering and the principles of the commons. For example, if the knowledge gained from chaos experiments is not shared openly, it can create a competitive advantage for a single organization, rather than contributing to the collective good. Similarly, if chaos experiments are conducted in a way that harms users or disrupts the stability of the digital commons, they can have a negative impact on the shared resource.

To ensure that Chaos Engineering is aligned with the principles of the commons, it is important to adopt a set of best practices. First, organizations should be encouraged to share the results of their chaos experiments openly, for example, through blog posts, conference presentations, and open-source tools. Second, chaos experiments should be conducted in a responsible and ethical manner, with a focus on minimizing the potential harm to users and the broader digital ecosystem. Finally, the practice of Chaos Engineering should be seen as a form of collective stewardship, with the goal of improving the resilience of the digital commons for the benefit of all.

By embracing these principles, Chaos Engineering can become a powerful tool for building a more resilient and equitable digital world. It can help us to move from a world of isolated, proprietary systems to a world of interconnected, shared resources that are managed for the collective good.

### 9. Resources & References (200-400 words)

The following resources provide further information on the principles, practices, and tools of Chaos Engineering.

Several key books provide a solid foundation in Chaos Engineering. *Chaos Engineering: System Resiliency in Practice* by Casey Rosenthal and Nora Jones is a comprehensive guide to the discipline. For a historical perspective, *Chaos Monkeys: Obsolete Monkeys, Obsolete Data Centers* by Antonio Garcia Martinez offers a compelling narrative of the origins of the practice at Netflix.

A wealth of information is also available online. The [Principles of Chaos Engineering](https://principlesofchaos.org/) website provides a concise overview of the core tenets of the practice. For more in-depth articles and tutorials, the [Gremlin](https://www.gremlin.com/community/tutorials/chaos-engineering-the-history-principles-and-practice) and [IBM](https://www.ibm.com/think/topics/chaos-engineering) websites are excellent resources. The [Wikipedia](https://en.wikipedia.org/wiki/Chaos_engineering) article on Chaos Engineering offers a good starting point for research, and [Steadybit](https://steadybit.com/case-studies/) provides a collection of case studies.

A variety of tools are available to support the practice of Chaos Engineering. **Chaos Monkey**, the original tool from Netflix, is an open-source option for randomly terminating virtual machine instances. For more advanced capabilities, commercial platforms like **Gremlin** and **Steadybit** offer a wide range of attacks, user-friendly interfaces, and integrations with the development lifecycle. For those on the AWS platform, the **AWS Fault Injection Simulator** provides a managed service for injecting faults into AWS workloads.

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/chaos-engineering/](https://commons-os.github.io/patterns/domain/chaos-engineering/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/chaos-engineering.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/chaos-engineering.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
