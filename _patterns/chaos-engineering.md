---
id: pat_01kg5023xsf58b5cjefwzpfedw
page_url: https://commons-os.github.io/patterns/chaos-engineering/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/chaos-engineering.md
slug: chaos-engineering
title: Chaos Engineering
aliases: [Resilience Engineering, Failure Injection Testing]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: design
  category: [practice]
  era: [digital]
  origin: [netflix]
  status: draft
  commons_alignment: 4
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

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
Chaos Engineering primarily defines responsibilities for the engineering and operations teams tasked with maintaining system stability. The rights of other stakeholders, such as end-users and customers, are implicitly protected by ensuring service availability. However, the pattern does not explicitly architect a broad set of rights and responsibilities for non-technical stakeholders like the environment or future generations.

**2. Value Creation Capability:**
The pattern directly enables the creation of **resilience value**, which is the capability of a system to continue delivering its core value proposition despite disruptions. This is a critical form of collective value creation, as it safeguards the benefits the system provides to all its stakeholders. It also generates significant **knowledge value** by revealing hidden dependencies and failure modes, enhancing the collective understanding of the system's complexity.

**3. Resilience & Adaptability:**
This is the core strength of Chaos Engineering. The entire practice is designed to help systems thrive on change and maintain coherence under stress by proactively exposing weaknesses. By deliberately injecting failures, it forces the system and the teams managing it to adapt and become more resilient, directly embodying the principles of adaptability and antifragility.

**4. Ownership Architecture:**
The pattern does not explicitly address ownership beyond the operational responsibility for system uptime. The focus is on the technical architecture and the responsibilities of the teams that build and operate it. It does not define ownership as a broader set of rights and responsibilities distributed among various stakeholders.

**5. Design for Autonomy:**
Chaos Engineering is highly compatible with and even essential for autonomous systems like AI, DAOs, and other distributed technologies. By building confidence in a system's ability to handle unexpected events, it provides the foundation of trust required for delegating control to autonomous agents. The emphasis on automating experiments also aligns with the goal of minimizing human coordination overhead.

**6. Composability & Interoperability:**
This pattern is highly composable and interoperable. It can be applied to virtually any software system and integrated with a wide range of other practices, such as continuous integration/continuous delivery (CI/CD), monitoring, and incident response. It acts as a modular capability that enhances the resilience of larger, composite value-creation systems.

**7. Fractal Value Creation:**
The logic of Chaos Engineering is fractal, meaning it can be applied at multiple scales. Experiments can be conducted on a single function, a microservice, a complete application, an entire infrastructure region, or even on human-organizational processes. This scalability allows the principle of resilience testing to be embedded throughout a system's architecture, from the smallest component to the whole.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
Chaos Engineering is a powerful enabler of resilient value creation, which is a core tenet of the Commons OS v2.0 framework. It provides a concrete practice for building systems that can adapt and thrive in complex, unpredictable environments. While it does not explicitly address all seven pillars, its profound impact on resilience, autonomy, and fractal value creation makes it a critical pattern for building modern commons.

**Opportunities for Improvement:**
- The pattern could be extended to consider a broader range of stakeholders beyond technical teams and end-users, including the environmental impact of system failures and recovery.
- Future iterations could explore how to apply Chaos Engineering principles to test the fairness and equity of value distribution within a system, not just its technical availability.
- The concept of 'blast radius' could be expanded to include social or economic impact, not just technical scope, when designing experiments.
