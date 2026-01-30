---
id: pat_01kg5023xaemr9xsmd0fgaxe86
page_url: https://commons-os.github.io/patterns/domain/agile-unified-process-aup/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/agile-unified-process-aup.md
slug: agile-unified-process-aup
title: Agile Unified Process (AUP)
aliases: [AUP]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: 3
  domain: design
  category: [methodology]
  era: [digital]
  origin: [scott-ambler, rational-unified-process]
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: ["pat_01kg5023ydftgramg3qp7rjkam", "pat_01kg5023zwft8t7k635h086kyj", "pat_01kg5023ypf08rv1dagnb27bjj", "pat_01kg5023vwe00rptkqr3z6pkd9", "pat_01kg5023ypf08rv1dafrvtxwdr", "pat_01kg5023zbftgswm71hgn15e2f", "pat_01kg5023y7e50rxp3ew60jdasx", "pat_01kg5023ztenhrk74hc9a8qszj", "pat_01kg5023zwft8t7k639ctqfhce", "pat_01kg5023zwft8t7k63bfadqqwg", "pat_01kg50240wfjh98jqx34wdddnm", "pat_01kg5023yneg8rmv1200tvfn3g", "pat_01kg5023yneg8rmv122d6v7bg5", "pat_01kg5023xaemr9xsmcy13gf405", "pat_01kg5023xaemr9xsmcxd0eg8ek"]
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Agile Unified Process (AUP) is a simplified version of the Rational Unified Process (RUP) developed by Scott Ambler in 2005. It provides a straightforward and easy-to-understand approach for developing business application software using agile techniques while retaining the foundational principles of RUP. The primary problem that AUP addresses is the perceived complexity and ceremony of RUP, offering a more lightweight and agile alternative. AUP integrates agile practices such as test-driven development (TDD), agile modeling (AM), agile change management, and database refactoring to enhance productivity and responsiveness. The origin of AUP lies in the need to bridge the gap between the structured, formal approach of RUP and the more flexible, iterative nature of agile methodologies. Scott Ambler, a prominent figure in the agile community, created AUP to provide a practical and adaptable framework for software development teams who wanted the benefits of both approaches. While AUP was superseded by Disciplined Agile Delivery (DAD) in 2012, its principles and practices continue to influence modern software development methodologies.

### 2. Core Principles

The Agile Unified Process is founded on a set of core principles that guide its application and philosophy. These principles emphasize a pragmatic and people-centric approach to software development, blending the structure of the Unified Process with the flexibility of agile methods.

1.  **Your Staff Knows What They're Doing**: AUP trusts that development teams are composed of skilled individuals who can make decisions and manage their own work. It advocates for providing high-level guidance and support rather than prescriptive, detailed process documentation. This principle empowers teams to take ownership of their process and adapt it to their specific context.

2.  **Simplicity**: The AUP philosophy champions simplicity in both process and documentation. It aims to describe the development process concisely, focusing on essential activities and artifacts. By avoiding the exhaustive detail of more traditional methodologies, AUP reduces overhead and makes the process easier to understand and follow.

3.  **Agility**: AUP aligns with the values and principles of the Agile Manifesto. It promotes flexibility, adaptability, and responsiveness to change. This principle encourages teams to embrace changing requirements and to continuously adapt their plans and priorities based on feedback and new information.

4.  **Focus on High-Value Activities**: AUP directs teams to concentrate on activities that deliver the most value to stakeholders. It discourages spending time on non-essential tasks or creating documentation that does not serve a clear purpose. This focus on value ensures that the team's efforts are always aligned with the project's primary goals.

5.  **Tool Independence**: AUP does not prescribe any specific tools. It encourages teams to select and use the tools that are best suited for their needs and context. This principle promotes a practical approach to tool selection, favoring simple and effective tools over complex or mandated ones.

6.  **Iterative and Incremental Development**: AUP is an iterative and incremental process. Work is broken down into small, manageable iterations, and the system is developed and delivered in frequent increments. This approach allows for continuous feedback, risk mitigation, and the early delivery of value.

7.  **Collaboration and Communication**: AUP emphasizes close collaboration and communication among all team members and stakeholders. It promotes a transparent and inclusive development process where everyone is engaged and working towards a common goal. This principle is essential for building a shared understanding and for ensuring that the final product meets the needs of its users.

### 3. Key Practices

The Agile Unified Process is composed of seven key disciplines that represent the primary areas of activity within a software development project. These disciplines are the practical application of the AUP's principles, providing a framework for organizing and executing the work.

1.  **Model**: This practice involves understanding the business domain, the problem to be solved, and designing a viable solution. In AUP, modeling is done in an agile manner, creating models that are just good enough for the task at hand. This includes techniques like user stories, CRC cards, and high-level domain models. For example, a team might create a simple class diagram to explore the relationships between key business entities before starting to code.

2.  **Implementation**: This is the practice of transforming the models into executable code. AUP emphasizes a test-driven development (TDD) approach, where unit tests are written before the code is implemented. This ensures that the code is well-tested and meets the requirements. For instance, a developer would write a failing unit test for a new feature, then write the code to make the test pass, and finally refactor the code to improve its design.

3.  **Test**: Testing in AUP is a continuous activity that goes beyond unit testing. It includes various levels of testing, such as integration testing, system testing, and acceptance testing. The goal is to ensure the quality of the system and to verify that it meets the stakeholders' expectations. An example of this practice is the use of continuous integration (CI) to automatically build and test the system every time a change is committed.

4.  **Deployment**: This practice focuses on planning and executing the delivery of the system to its end-users. AUP distinguishes between development releases (to a staging environment) and production releases. The goal is to make the deployment process as smooth and reliable as possible. For example, a team might use automated deployment scripts to deploy the application to the production environment with a single command.

5.  **Configuration Management**: This practice involves managing all the artifacts of the project, including source code, documentation, and models. It includes version control, change management, and build management. The goal is to ensure the integrity and traceability of the project's assets. A common example is the use of a version control system like Git to manage changes to the source code.

6.  **Project Management**: This practice involves directing the project's activities, managing risks, and coordinating with stakeholders. In AUP, project management is done in an agile manner, with a focus on empowering the team and facilitating communication. For example, a project manager might use a Kanban board to visualize the workflow and to track the progress of tasks.

7.  **Environment**: This practice involves providing the necessary infrastructure, tools, and processes to support the development team. This includes setting up the development environment, configuring the CI/CD pipeline, and defining the coding standards. The goal is to create a productive and efficient work environment for the team.

### 4. Application Context

**Best Used For**:

*   **Small to medium-sized projects**: AUP is well-suited for projects with small to medium-sized teams where communication and collaboration are straightforward.
*   **Projects with unclear or evolving requirements**: The iterative and agile nature of AUP makes it ideal for projects where the requirements are not fully defined upfront and are expected to change over time.
*   **Business application development**: AUP is particularly effective for developing business applications that require a balance of structure and agility.
*   **Organizations transitioning from RUP to agile**: AUP can serve as a bridge for organizations that are familiar with RUP but want to adopt more agile practices.
*   **Teams that value both discipline and agility**: AUP provides a framework that combines the discipline of the Unified Process with the flexibility of agile development, making it a good choice for teams that want the best of both worlds.

**Not Suitable For**:

*   **Large, complex projects**: For very large and complex projects with distributed teams, the lightweight nature of AUP may not provide sufficient structure and coordination.
*   **Projects with fixed, well-defined requirements**: If the requirements are stable and unlikely to change, a more traditional, plan-driven methodology might be more efficient.
*   **Life-critical systems**: For systems where failure could have severe consequences, a more rigorous and formal methodology with comprehensive upfront design and verification is generally required.

**Scale**:

AUP is most effective at the **Team** and **Department** level. It can be applied to individual projects or to a portfolio of projects within a department. While some of the principles can be applied at an organizational level, AUP is not designed as a full-scale enterprise-level methodology.

**Domains**:

AUP has been applied in various domains, including:

*   **Finance**: For developing online banking applications and trading systems.
*   **Insurance**: For building policy management and claims processing systems.
*   **E-commerce**: For creating online retail platforms and customer relationship management (CRM) systems.
*   **Government**: For developing internal applications and citizen-facing services.

### 5. Implementation

**Prerequisites**:

*   **Skilled and Empowered Team**: AUP relies on the expertise and autonomy of the development team. Team members should have a good understanding of software development principles and be empowered to make decisions about their work.
*   **Collaborative Culture**: A culture of open communication and collaboration is essential for the success of AUP. The team should be comfortable working together and sharing information freely.
*   **Basic Understanding of RUP and Agile**: While AUP is a simplified version of RUP, a basic understanding of the Unified Process and its phases (Inception, Elaboration, Construction, Transition) is helpful. Similarly, familiarity with agile principles and practices is crucial.
*   **Stakeholder Commitment**: The project's stakeholders must be committed to an iterative and incremental approach. They need to be available for regular feedback and be willing to accept that the requirements may evolve over time.

**Getting Started**:

1.  **Initial Modeling Workshop**: Begin with a workshop to create a high-level model of the system. This should involve the entire team and key stakeholders. The goal is to establish a shared understanding of the project's scope and objectives.
2.  **Set Up the Environment**: Establish the development and testing environments, including version control, continuous integration, and any other necessary tools. The environment should be automated as much as possible to support a rapid and iterative workflow.
3.  **Plan the First Iteration**: Identify a small set of high-priority features to be implemented in the first iteration. The plan should be flexible and adaptable, but it should provide a clear focus for the team's work.
4.  **Start Iterating**: Begin the first iteration, applying the AUP disciplines of modeling, implementation, and testing. Hold regular stand-up meetings to track progress and to address any impediments.
5.  **Gather Feedback and Adapt**: At the end of each iteration, hold a review and retrospective session. Gather feedback from stakeholders on the increment of software that has been delivered, and use this feedback to adapt the plan for the next iteration.

**Common Challenges**:

*   **Resistance to Change**: Teams that are accustomed to more traditional, plan-driven methodologies may resist the shift to a more agile approach. It is important to provide training and coaching to help them understand the benefits of AUP.
*   **Balancing Discipline and Agility**: Finding the right balance between the discipline of the Unified Process and the flexibility of agile development can be challenging. Teams may be tempted to either over-engineer the solution or to abandon discipline altogether.
*   **Lack of Stakeholder Involvement**: AUP requires active involvement from stakeholders. If stakeholders are not available for regular feedback, the project can quickly go off track.
*   **Inadequate Testing**: The emphasis on speed and agility can sometimes lead to a neglect of testing. It is crucial to maintain a strong focus on quality and to ensure that the system is thoroughly tested at all levels.

**Success Factors**:

*   **Strong Leadership Support**: The successful adoption of AUP requires strong support from leadership. Leaders need to champion the new approach and to provide the necessary resources and support for the team.
*   **Culture of Continuous Improvement**: AUP is not a one-size-fits-all solution. Teams should continuously reflect on their process and to adapt it to their specific needs and context.
*   **Focus on Delivering Value**: The ultimate measure of success for an AUP project is the delivery of value to the customer. The team should always be focused on this goal and should prioritize their work accordingly.
*   **Experienced Team Coach**: Having an experienced agile coach can be invaluable for a team that is new to AUP. A coach can provide guidance, support, and training to help the team navigate the challenges of adopting a new methodology.

### 6. Evidence & Impact

**Notable Adopters**:

While specific, large-scale, and publicly documented case studies of Agile Unified Process adoption are not as abundant as for more mainstream agile methodologies like Scrum or Kanban, AUP has been influential, particularly for organizations familiar with the Rational Unified Process (RUP). Notable adopters tend to be in the following categories:

*   **Financial services companies**: Banks and other financial institutions have used AUP to bring more agility to their development processes while maintaining a degree of the structure and documentation required for regulatory compliance.
*   **Insurance companies**: Similar to financial services, insurance companies have found AUP to be a good fit for developing complex policy and claims management systems in a more iterative and responsive manner.
*   **Government agencies**: Some government agencies have used AUP for internal software development projects, where the need for accountability and documentation is high, but there is also a desire to be more agile.
*   **Companies transitioning from RUP**: Many organizations that had invested in RUP saw AUP as a natural and low-risk way to start their agile journey.
*   **Small to medium-sized enterprises (SMEs)**: SMEs in various sectors have adopted AUP for its balance of simplicity and structure, which is well-suited to their size and resources.

**Documented Outcomes**:

The documented outcomes of AUP adoption are often qualitative and focus on the improvements in the development process itself. These include:

*   **Increased team productivity**: By focusing on high-value activities and reducing unnecessary ceremony, AUP helps teams to become more productive.
*   **Improved software quality**: The emphasis on continuous testing and integration in AUP leads to higher-quality software with fewer defects.
*   **Greater responsiveness to change**: The iterative and agile nature of AUP allows teams to respond more effectively to changing requirements and customer feedback.
*   **Smoother transition to agile**: For organizations coming from a RUP background, AUP provides a smoother and less disruptive transition to agile practices.

**Research Support**:

While there are not many formal academic studies specifically on AUP, there is a significant body of research that supports the principles and practices that it incorporates. For example:

*   **Research on agile methods**: Numerous studies have demonstrated the benefits of agile methodologies in terms of productivity, quality, and customer satisfaction. AUP, as an agile methodology, is supported by this broader body of research.
*   **Research on the Unified Process**: The Unified Process itself is a well-researched and documented methodology. AUP builds on this solid foundation, and so it inherits some of its credibility.
*   **Scott Ambler's work**: Scott Ambler, the creator of AUP, has published extensively on agile and lean methodologies. His work provides a strong conceptual and practical foundation for AUP.

### 7. Cognitive Era Considerations

**Cognitive Augmentation Potential**:

*   **AI-Powered Modeling**: AI tools can assist in the modeling discipline by generating initial models from natural language descriptions, identifying potential inconsistencies in models, and suggesting alternative designs. This can accelerate the modeling process and improve the quality of the models.
*   **Intelligent Code Completion and Generation**: AI-powered code assistants can significantly enhance the implementation discipline by providing intelligent code completion, generating boilerplate code, and even suggesting entire functions or classes. This can free up developers to focus on more complex and creative aspects of their work.
*   **Automated Test Generation and Analysis**: AI can be used to automatically generate test cases, particularly for unit and integration testing. AI tools can also analyze test results to identify patterns and to predict potential areas of risk.
*   **Predictive Project Management**: AI can be used to analyze project data to identify potential risks and to predict project outcomes. This can help project managers to make more informed decisions and to take proactive measures to keep the project on track.

**Human-Machine Balance**:

While AI can augment many aspects of AUP, the human element remains crucial. The uniquely human aspects of AUP include:

*   **Strategic Decision-Making**: While AI can provide data and insights, the final decisions about the project's direction and priorities will still be made by humans.
*   **Creative Problem-Solving**: AI can assist in problem-solving, but the creative and innovative solutions will still come from human ingenuity.
*   **Collaboration and Communication**: The collaborative and communicative aspects of AUP are inherently human. AI can facilitate communication, but it cannot replace the trust and rapport that are built through human interaction.
*   **Ethical Considerations**: The ethical implications of the software being developed will always require human judgment and oversight.

**Evolution Outlook**:

In the cognitive era, AUP is likely to evolve in the following ways:

*   **Tighter Integration with AI Tools**: AUP will become more tightly integrated with AI-powered development tools. The AUP framework will provide guidance on how to effectively use these tools to enhance the development process.
*   **Greater Emphasis on Data-Driven Decision-Making**: With the help of AI, AUP will place a greater emphasis on data-driven decision-making. Project data will be continuously analyzed to provide insights and to guide the project's direction.
*   **Emergence of New Roles**: New roles may emerge in AUP teams, such as AI specialists who are responsible for developing and maintaining the AI-powered tools and infrastructure.

### 8. Commons Alignment Assessment

**1. Stakeholder Mapping**: AUP explicitly emphasizes collaboration and communication with stakeholders. The project management and modeling disciplines directly address the need to understand and engage with stakeholders. However, the extent of stakeholder mapping is not as comprehensive as in a true commons-based approach. The focus tends to be on the immediate stakeholders of the project (customers, users, developers) rather than the broader community or ecosystem.

**2. Value Creation**: AUP is focused on creating value for the customer. The principle of focusing on high-value activities ensures that the team is always working on what is most important to the customer. However, the definition of value is primarily economic. AUP does not explicitly consider other forms of value, such as social or environmental value.

**3. Value Preservation**: AUP's iterative and incremental approach helps to preserve value over time by allowing the system to evolve and adapt to changing needs. The emphasis on quality and testing also contributes to the long-term viability of the software. However, there is no explicit mechanism for ensuring that the value created is shared and stewarded by a community.

**4. Shared Rights & Responsibilities**: AUP promotes shared responsibility within the development team. The principle of "Your Staff Knows What They're Doing" empowers the team to take ownership of their work. However, the rights and responsibilities are not explicitly shared with a broader community of stakeholders. The ownership of the software and the intellectual property rights are typically held by the organization that funded the development.

**5. Systematic Design**: AUP provides a systematic and disciplined approach to software development. The seven disciplines provide a clear framework for organizing and executing the work. The emphasis on modeling and architecture helps to ensure that the system is well-designed and maintainable. However, the design process is not as open or participatory as in a commons-based approach.

**6. Systems of Systems**: AUP can be used to develop systems that are part of a larger ecosystem. The emphasis on collaboration and communication can help to ensure that the system integrates well with other systems. However, AUP does not provide a framework for designing and governing a system of systems as a commons.

**7. Fractal Properties**: The principles of AUP can be applied at different scales, from a single team to a department. This gives AUP a degree of fractal properties. However, the methodology is not designed to be applied at the level of a multi-organizational ecosystem.

**Overall Score**: 3/5 (Transitional)

**Rationale**: AUP represents a significant step away from traditional, command-and-control methodologies towards a more collaborative and empowering approach to software development. It shares some of the values of a commons-based approach, such as collaboration, transparency, and shared responsibility within the team. However, it is still fundamentally a project-centric methodology that is focused on delivering value to a customer within the context of a single organization. It does not provide the mechanisms for creating and governing a software commons.

**Opportunities for Improvement**: To become more commons-aligned, AUP could be extended to include practices for: engaging a broader community of stakeholders; defining and measuring different forms of value; establishing a governance structure for sharing the rights and responsibilities of the software; and designing the software as part of a larger, interconnected ecosystem.

### 9. Resources & References

**Essential Reading**:

*   Ambler, S. W. (2002). *Agile Modeling: Effective Practices for Extreme Programming and the Unified Process*. John Wiley & Sons.
*   Ambler, S. W. (2005). *The Agile Unified Process*. Retrieved from [http://www.ambysoft.com/unifiedprocess/agileUP.html](http://www.ambysoft.com/unifiedprocess/agileUP.html)
*   Kruchten, P. (2003). *The Rational Unified Process: An Introduction*. Addison-Wesley Professional.

**Organizations & Communities**:

*   **Agile Alliance**: A non-profit organization that promotes the use of agile software development methodologies. ([https://www.agilealliance.org/](https://www.agilealliance.org/))
*   **Disciplined Agile Consortium**: The successor to AUP, the Disciplined Agile (DA) toolkit is a more comprehensive and scalable agile and lean framework. ([https://www.pmi.org/disciplined-agile](https://www.pmi.org/disciplined-agile))

**Tools & Platforms**:

AUP is tool-independent, but some commonly used tools include:

*   **Version Control**: Git, Subversion
*   **Continuous Integration**: Jenkins, CircleCI, Travis CI
*   **Project Management**: Jira, Trello, Kanban boards
*   **Modeling**: UML tools, whiteboards, CRC cards

**References**:

[1] Wikipedia. (2023). *Agile Unified Process*. Retrieved from [https://en.wikipedia.org/wiki/Agile_unified_process](https://en.wikipedia.org/wiki/Agile_unified_process)

[2] Agile Lone Star. (2022). *Agile Unified Process (AUP)*. Retrieved from [https://www.agilelonestar.com/knowledge-base/agile-unified-process](https://www.agilelonestar.com/knowledge-base/agile-unified-process)

[3] Ambler, S. W. (2001). *The Agile Unified Process (AUP)*. Retrieved from [https://www.researchgate.net/publication/267259668_The_Agile_Unified_Process_AUP](https://www.researchgate.net/publication/267259668_The_Agile_Unified_Process_AUP)

[4] Ambler, S. W. (2002). *Agile Modeling: Effective Practices for Extreme Programming and the Unified Process*. John Wiley & Sons.

[5] Kruchten, P. (2003). *The Rational Unified Process: An Introduction*. Addison-Wesley Professional.

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/agile-unified-process-aup/](https://commons-os.github.io/patterns/domain/agile-unified-process-aup/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/agile-unified-process-aup.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/agile-unified-process-aup.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
