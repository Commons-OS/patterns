---
id: pat_01kg50240xe19r5fzqxd2rwsje
page_url: https://commons-os.github.io/patterns/nexus-framework/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/nexus-framework.md
slug: nexus-framework
title: Nexus Framework
aliases: [Nexus, Scaled Scrum]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: implementation
  domain: meta
  category: [framework]
  era: [digital]
  origin: [scrum.org]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
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

Nexus is a framework for scaling Scrum to multiple teams working on a single product. It provides a lightweight structure for coordinating the work of three to nine Scrum teams, enabling them to deliver an integrated and potentially releasable increment of product at least once per Sprint. The core problem Nexus solves is the complexity that arises when multiple teams collaborate on a single product, such as dependencies, integration issues, and communication overhead. By extending Scrum with a new role (the Nexus Integration Team), new events (the Nexus Sprint Planning, Nexus Daily Scrum, Nexus Sprint Review, and Nexus Sprint Retrospective), and new artifacts (the Nexus Sprint Backlog), Nexus provides a mechanism for managing these complexities and ensuring that all teams are aligned and working towards a common goal. The framework was created by Ken Schwaber, co-creator of Scrum, and was released by Scrum.org in 2015. It was developed in response to the growing need for a simple, yet effective way to scale Scrum without losing its fundamental principles and values.

### 2. Core Principles

1. **Transparency and Empiricism**: Nexus is built on the foundation of Scrum and its empirical process control. Transparency is crucial for success, and all teams must have visibility into each other's work, progress, and impediments. Decisions are made based on evidence, and the framework encourages continuous inspection and adaptation to optimize the development process.

2. **One Product, One Product Backlog**: A Nexus consists of multiple Scrum Teams working on a single product. To ensure alignment and a unified direction, there is only one Product Backlog for the entire Nexus. The Product Owner is responsible for managing and prioritizing this backlog to maximize the value of the product.

3. **Integrated Increment**: The ultimate goal of a Nexus is to deliver a potentially releasable, integrated increment of the product at least once per Sprint. All teams in the Nexus contribute to this single increment, and a shared Definition of Done is used to ensure that the integrated work is of high quality and can be considered complete.

4. **Nexus Integration Team**: To manage dependencies and ensure the successful integration of work from all teams, Nexus introduces the Nexus Integration Team (NIT). The NIT is a dedicated team responsible for coaching and guiding the Scrum Teams, facilitating cross-team collaboration, and resolving any integration issues that may arise. The NIT consists of the Product Owner, a Scrum Master, and one or more Nexus Integration Team members.

5. **Nexus Events**: Nexus extends Scrum's events to provide a formal structure for collaboration and communication between the teams. These events include the Nexus Sprint Planning, Nexus Daily Scrum, Nexus Sprint Review, and Nexus Sprint Retrospective. These events are designed to be lightweight and to supplement, not replace, the existing Scrum events.

### 3. Key Practices

1. **Nexus Integration Team (NIT)**: The NIT is a new role introduced in Nexus to ensure that a "Done" Integrated Increment is produced at least once a Sprint. It consists of the Product Owner, a Scrum Master, and appropriate members from the Scrum Teams. The NIT provides a focal point for integration, coaching teams on development practices and tools, and resolving cross-team dependencies.

2. **Cross-Team Refinement**: This is an ongoing activity to refine the Product Backlog to a state where dependencies are identified and minimized. It helps in forecasting which team will work on which items and ensures that the work is well understood before Sprint Planning.

3. **Nexus Sprint Planning**: This event coordinates the work of all Scrum Teams for the upcoming Sprint. Representatives from each team, along with the Product Owner, collaborate to select Product Backlog Items and form a Nexus Sprint Goal. Each team then creates its own Sprint Backlog, aligned with the overall Nexus Sprint Goal.

4. **Nexus Daily Scrum**: This is a daily event for appropriate representatives from each Scrum Team to inspect the current state of the Integrated Increment and to identify any integration issues or new dependencies. The insights from this meeting are then taken back to the individual team's Daily Scrum for detailed planning.

5. **Nexus Sprint Review**: This event replaces the individual team Sprint Reviews. The entire Nexus presents the single Integrated Increment to stakeholders, gathering feedback and adapting the Product Backlog accordingly.

6. **Nexus Sprint Retrospective**: This is a three-part event. First, representatives from each team meet to identify issues that impact the entire Nexus. Second, each team has its own Sprint Retrospective, which can be informed by the cross-team issues. Finally, the representatives meet again to discuss the outcomes of the team retrospectives and to create a plan for Nexus-level improvements.

7. **Nexus Sprint Backlog**: This is a new artifact that provides a consolidated view of the work being done by all teams in the Nexus for a single Sprint. It makes dependencies visible and helps in tracking progress towards the Nexus Sprint Goal.

8. **Integrated Increment**: This is the sum of all integrated work completed by a Nexus in a Sprint. It must be a "Done", usable, and potentially releasable increment that adheres to a single, shared Definition of Done.

9. **Definition of Done**: A single Definition of Done is agreed upon by all teams in the Nexus. This ensures that the integrated work is of a consistent quality and that everyone has a shared understanding of what it means for work to be complete.

### 4. Application Context

**Best Used For**:

*   **Scaling Scrum for multiple teams**: Nexus is ideal for organizations that are already using Scrum and need to scale their product development to between three and nine teams.
*   **Complex products with a single Product Backlog**: It is best suited for situations where multiple teams are working on a single product with a unified Product Backlog.
*   **Minimizing dependencies**: The framework is designed to identify and reduce cross-team dependencies, making it a good choice for projects where integration is a major challenge.
*   **Maintaining agility at scale**: Nexus provides a lightweight framework that allows organizations to scale without introducing excessive overhead or bureaucracy.

**Not Suitable For**:

*   **Single-team projects**: Nexus is designed for multi-team environments and would be overkill for a single Scrum team.
*   **Projects with more than nine teams**: The framework is not designed to scale beyond nine teams. For larger-scale projects, other frameworks like LeSS Huge or SAFe may be more appropriate.
*   **Organizations new to Scrum**: Nexus builds on a solid understanding of Scrum. Organizations that have not yet successfully implemented Scrum with a single team will likely struggle to implement Nexus.

**Scale**: Team/Department/Organization

**Domains**: Software development, IT, and other industries where complex products are developed by multiple teams.

### 5. Implementation

**Prerequisites**:

*   **Solid Scrum Foundation**: Before attempting to scale with Nexus, it is crucial to have a strong foundation in Scrum. The organization should have at least one, and preferably more, high-performing Scrum teams.
*   **A Clear Need to Scale**: Nexus should be adopted in response to a genuine need to scale product development, not just for the sake of scaling. The primary driver should be the complexity of the product and the need for multiple teams to work on it simultaneously.
*   **Leadership Buy-in**: Successful implementation of Nexus requires strong support from leadership. This includes providing the necessary resources, removing organizational impediments, and championing the change throughout the organization.

**Getting Started**:

1.  **Form the Nexus Integration Team (NIT)**: The first concrete step is to establish the NIT. This team will be accountable for the integration of all work done by the Scrum Teams in the Nexus.
2.  **Create a Single Product Backlog**: All teams in the Nexus work from a single Product Backlog. This ensures that everyone is aligned with the product vision and priorities.
3.  **Define a Shared Definition of Done**: A clear and agreed-upon Definition of Done is essential for ensuring that the integrated increment is of a consistent quality.
4.  **Start Small**: It is advisable to start with a small Nexus of three to four teams and then gradually scale up as the organization gains experience and confidence.
5.  **Educate and Train**: Ensure that all team members, as well as stakeholders, are trained in the Nexus framework and understand their roles and responsibilities.

**Common Challenges**:

*   **Resistance to Change**: As with any organizational change, there may be resistance from individuals and teams who are comfortable with the existing ways of working.
*   **Dependency Management**: Identifying and managing dependencies between teams can be a significant challenge, even with the structures provided by Nexus.
*   **Lack of Experienced Scrum Masters**: The success of Nexus depends heavily on the skills and experience of the Scrum Masters, both within the teams and in the NIT.
*   **Tooling and Infrastructure**: Inadequate tooling and infrastructure can make it difficult to maintain a single Product Backlog, track dependencies, and support continuous integration.

**Success Factors**:

*   **Strong Technical Practices**: Solid technical practices, such as continuous integration, automated testing, and a shared codebase, are essential for successful integration.
*   **Experienced Coaching**: An experienced Agile coach can provide invaluable guidance and support during the implementation of Nexus.
*   **A Culture of Collaboration**: Nexus requires a high degree of collaboration between teams. A culture that encourages and rewards collaboration is a key success factor.
*   **Patience and Persistence**: Implementing Nexus is a journey, not a destination. It requires patience, persistence, and a commitment to continuous improvement.

### 6. Evidence & Impact

**Notable Adopters**:

*   **KLM Royal Dutch Airlines**: Faced with challenges in scaling their Scrum implementation, KLM adopted a model called "Scrum Studio," which evolved from both Scrum and the Nexus Framework. This led to significant improvements in operational performance, innovation, and time to market.
*   **Cathay Pacific Airlines**: To launch their new Internet Booking Engine, Cathay Pacific transitioned from a hybrid waterfall/Scrum model to Nexus. This resulted in a 200% increase in the frequency of releasing increments and improved the quality of their product.
*   **Net Health**: This healthcare software company adopted Nexus to address challenges with silos, integration, and communication. As a result, they were able to have five Scrum teams delivering three integrated increments at the end of every sprint.
*   **A Security Software Product Company in India**: This company used Nexus to scale from a single Scrum team to six teams working on mobile applications, API development, and integration services. This led to more coordinated sprints and increments, minimized dependencies, and a faster time to market.
*   **A German HVAC Manufacturer**: This company used Nexus to redesign over 80 websites, resulting in the websites being delivered three months ahead of schedule.

**Documented Outcomes**:

*   **Increased Frequency of Delivery**: As seen in the Cathay Pacific case study, Nexus can lead to a significant increase in the frequency of delivering integrated increments.
*   **Improved Quality**: The focus on an Integrated Increment and a shared Definition of Done helps to improve the quality of the product.
*   **Reduced Time to Market**: The German HVAC manufacturer's case study demonstrates that Nexus can help to reduce the time to market for new products and features.
*   **Enhanced Collaboration and Communication**: The case studies consistently highlight improved collaboration and communication between teams as a key benefit of Nexus.
*   **Better Dependency Management**: Nexus provides a structure for identifying and managing dependencies, which is a common challenge in scaled Agile environments.

**Research Support**:

While there is a growing body of case studies and anecdotal evidence supporting the effectiveness of Nexus, there is a need for more formal research on the framework. However, the existing evidence from organizations that have adopted Nexus suggests that it can be a valuable tool for scaling Scrum and improving product development outcomes.

### 7. Cognitive Era Considerations

**Cognitive Augmentation Potential**:

*   **AI-Powered Dependency Analysis**: AI and machine learning algorithms can be used to analyze the Product Backlog and identify potential dependencies between work items, even before they are explicitly flagged by the teams. This can help to reduce the overhead of Cross-Team Refinement and prevent integration issues from arising later in the development process.
*   **Automated Integration and Testing**: The Nexus Framework's emphasis on a single Integrated Increment makes it a prime candidate for automation. AI-powered tools can automate the process of integrating code from multiple teams, running regression tests, and even deploying the integrated increment to a staging environment. This can significantly reduce the manual effort required for integration and free up the Nexus Integration Team to focus on more strategic tasks.
*   **Intelligent Sprint Planning**: AI can assist in Nexus Sprint Planning by suggesting which teams are best suited to take on which Product Backlog Items, based on their past performance, skills, and capacity. This can help to create more realistic and achievable Sprint plans.

**Human-Machine Balance**:

*   **Facilitation and Coaching**: While AI can automate many of the mechanical aspects of Nexus, the role of the Scrum Master and the Nexus Integration Team in facilitating communication, coaching teams, and resolving conflicts will remain uniquely human. These roles will become even more important in a cognitive era, as they will need to guide the teams in effectively using AI-powered tools and interpreting their outputs.
*   **Product Ownership and Vision**: The Product Owner's role in defining the product vision, prioritizing the Product Backlog, and engaging with stakeholders will remain a fundamentally human endeavor. AI can provide data and insights to support these activities, but the ultimate decisions will still require human judgment and creativity.
*   **Complex Problem-Solving**: While AI can help to identify and manage dependencies, complex problem-solving that requires a deep understanding of the product, the technology, and the organizational context will still require human intervention.

**Evolution Outlook**:

*   **From Nexus to a 'Digital Nexus'**: As AI and automation become more integrated into the development process, the Nexus Framework may evolve into a 'Digital Nexus' where many of the coordination and integration activities are automated. This would allow the framework to scale to even larger numbers of teams and more complex products.
*   **The Rise of the 'AI-Augmented' Nexus Integration Team**: The Nexus Integration Team of the future may be a hybrid team of humans and AI agents, working together to ensure the smooth flow of work through the Nexus.
*   **A Greater Focus on Value Creation**: By automating many of the routine tasks associated with scaled Agile development, AI will free up teams to focus on what really matters: creating value for the customer. This could lead to a new wave of innovation and a re-imagining of what is possible with scaled Agile frameworks like Nexus.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
The Nexus Framework defines a clear stakeholder architecture centered on product development, including roles like the Product Owner, Scrum Teams, and the Nexus Integration Team. Responsibilities are explicitly assigned to ensure the delivery of an integrated product increment. However, the framework's stakeholder considerations are primarily internal to the development process and do not explicitly extend to broader stakeholders such as the environment, local communities, or future generations.

**2. Value Creation Capability:**
Nexus excels at enabling collective economic value creation by scaling Scrum to deliver complex products more effectively. It also generates knowledge value through its emphasis on cross-team collaboration and learning. The framework's focus on a single integrated increment fosters a sense of collective achievement and shared purpose, but it does not explicitly address the creation of social or ecological value.

**3. Resilience & Adaptability:**
Built on the empirical principles of Scrum, Nexus is designed for resilience and adaptability. The framework's events, such as the Nexus Daily Scrum and Nexus Sprint Retrospective, provide regular opportunities for inspection and adaptation, allowing the system to respond to change and maintain coherence under stress. This iterative approach helps the collective of teams to thrive on complexity and continuously improve its processes.

**4. Ownership Architecture:**
Ownership in Nexus is defined through clearly articulated responsibilities for the various roles and teams. The Product Owner 'owns' the Product Backlog, and the Nexus Integration Team 'owns' the integration of the work. This is a form of stewardship over different aspects of the value creation process. However, the concept of ownership is not explicitly defined in terms of a broader set of rights and responsibilities beyond the immediate context of product development.

**5. Design for Autonomy:**
Nexus is well-suited for a future of increased autonomy, as it provides a lightweight framework for coordinating the work of multiple autonomous teams. Its emphasis on transparency and self-organization makes it compatible with distributed systems and DAOs. The framework's design, which minimizes coordination overhead while maximizing alignment, is a key enabler for scaling autonomous collaboration.

**6. Composability & Interoperability:**
As an extension of Scrum, Nexus is inherently composable and can be integrated with other patterns and practices like DevOps and Lean UX to create more comprehensive value-creation systems. It is a 'system of systems' that allows for the combination of multiple Scrum teams into a larger, cohesive whole. This modularity enables organizations to adapt the framework to their specific context and needs.

**7. Fractal Value Creation:**
The core value-creating logic of Scrum—transparency, inspection, and adaptation—is replicated at all scales within the Nexus framework. The Nexus events are fractal versions of the team-level Scrum events, ensuring that the empirical process is applied to the coordination of the teams as well as the work of the teams themselves. This fractal design allows the value-creation logic to be applied consistently from the individual team to the entire Nexus.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
Nexus is a powerful enabler of collective value creation, providing a robust architecture for scaling agile development. It strongly aligns with the principles of resilience, adaptability, and composability. While its primary focus is on economic and knowledge value within the product development context, its core logic is highly compatible with a broader commons-based approach. The framework's main gap is its lack of explicit consideration for a wider set of stakeholders and forms of value.

**Opportunities for Improvement:**
- Integrate practices for mapping and engaging a broader range of stakeholders beyond the immediate product development process.
- Extend the definition of 'value' to explicitly include social and ecological metrics, alongside economic ones.
- Develop mechanisms for distributing rights and responsibilities more broadly among all stakeholders, not just the development teams and the Product Owner.

### 9. Resources & References

**Essential Reading**:

*   **The Nexus Framework for Scaling Scrum** by Kurt Bittner, Patricia Kong, and Dave West: This book provides a comprehensive guide to the Nexus Framework, with practical advice and real-world examples.
*   **The Nexus Guide**: The official guide to the Nexus Framework, maintained by Scrum.org. It provides a concise and definitive description of the framework.
*   **The Scrum Guide**: As Nexus is an extension of Scrum, a deep understanding of the Scrum Guide is essential.

**Organizations & Communities**:

*   **Scrum.org**: The home of Scrum and the Nexus Framework. Scrum.org provides a wealth of resources, including articles, case studies, and training courses.
*   **The Scrum.org Community Forums**: A great place to ask questions, share experiences, and connect with other Nexus practitioners.

**Tools & Platforms**:

*   **Jira with a Nexus plugin**: Atlassian's Jira is a popular tool for managing Agile projects, and there are several plugins available that can help you to implement Nexus.
*   **Kendis**: A tool that provides a visual platform for managing scaled Agile frameworks, including Nexus.
*   **Visual Paradigm**: Offers a Nexus Canvas tool to help visualize and manage work items within the Nexus framework.

**References**:

1.  Scrum.org. (2021). *The Nexus Guide*. https://www.scrum.org/resources/nexus-guide
2.  Scrum.org. (n.d.). *Big Companies that Scaled Scrum with the Nexus Framework part 1*. https://www.scrum.org/resources/big-companies-scaled-scrum-nexus-framework-part-1
3.  Kendis. (2019, February 1). *Nexus: Case Studies from KLM, Cathay Pacific & Net Health*. https://blog.kendis.io/nexus-framework-part-2/
4.  nimbleworx. (2024, May 6). *Implementing the Nexus Framework: A Guide to Scaling Scrum*. Medium. https://medium.com/@nimbleworx/implementing-the-nexus-framework-a-guide-to-scaling-scrum-85dfc4af6652
5.  StarAgile. (2023, August 17). *Nexus Framework: Future of Agile Management*. https://staragile.com/blog/nexus-framework

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/implementation/nexus-framework/](https://commons-os.github.io/patterns/implementation/nexus-framework/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/nexus-framework.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_implementation/nexus-framework.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
