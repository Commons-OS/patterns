---
id: pat_01kg5023zae8rthxw686kx5x4k
page_url: https://commons-os.github.io/patterns/domain/kanban/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/kanban.md
slug: kanban
title: Kanban
aliases: [Kanban Method, Toyota Production System]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: [methodology, practice]
  era: [industrial, digital]
  origin: [toyota]
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: []
specializes_to: ["pat_01kg5023zae8rthxw6518chq43", "pat_01kg5023zae8rthxw66c5atdj6"]
enables: []
requires: []
related: ["pat_01kg5023z9e988phvxv2ywhcrd", "pat_01kg50240pfa89r4q24ctm0q0w", "pat_01kg502407eyh8wbym4fzzr7et", "pat_01kg5023vyfzhvteh04eykysqz", "pat_01kg5023x6ecsvs4r50r92ggad", "pat_01kg5023vmfk9bnr9pzvxb1j3z", "pat_01kg5023zcf99tjg7qba44c2j7", "pat_01kg5023zbftgswm71sjjf53xx", "pat_01kg5023wbfw1azjwp99gcgcrn", "pat_01kg5023zcf99tjg7qgdbhqfkm", "pat_01kg5023w1f29v6bdxpahq6a1m", "pat_01kg5023vdecr9aqhgpf1mh73v", "pat_01kg50240bf4ra2qcwx56j5qk8", "pat_01kg5023vke6gsrh5cyb1wbkte", "pat_01kg5023yweb8r88nxjsysr1hq"]
contributors: [higgerix, cloudsters]
sources: [https://www.atlassian.com/agile/kanban, https://asana.com/resources/what-is-kanban, https://businessmap.io/blog/kanban-examples, https://kanban.university/kanban-guide/, https://www.projectmanager.com/blog/kanban-history]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview (150-300 words)

Kanban is a visual management method for directing and improving work processes. Its name, Japanese for “signboard” or “billboard,” points to its core: making work visible. By using Kanban boards, teams can visualize their workflow, limit work-in-progress (WIP), and maximize efficiency. The primary problem Kanban solves is the reduction of waste and the improvement of flow in a process, leading to more predictable and faster delivery of value. It is not a software development lifecycle methodology or a project management framework, but a method to gradually improve whatever you are doing.

The origin of Kanban dates back to the late 1940s at Toyota, where industrial engineer Taiichi Ōno developed it as part of the Toyota Production System (TPS). The goal was to create a “just-in-time” (JIT) manufacturing process, where inventory levels were matched with actual consumption. This was achieved by using physical cards (kanbans) to signal the need for more materials, creating a pull system that reduced inventory and increased efficiency. In the early 2000s, David J. Anderson and other thought leaders adapted Kanban for knowledge work, particularly software development, where it has since become a popular approach within the Agile community.

### 2. Core Principles (3-7 principles, 200-400 words)

Kanban is founded on a set of core principles that guide its implementation and evolution. These principles are not rigid rules but rather a mindset that encourages continuous improvement and respect for the existing process.

1.  **Start with What You Do Now**: Kanban does not require a radical change to your current processes. It is designed to be applied directly to your existing workflow, allowing you to evolve it gradually. This principle lowers the barrier to adoption and reduces the resistance to change.

2.  **Agree to Pursue Incremental, Evolutionary Change**: Kanban promotes a culture of continuous, small, and incremental changes. This approach avoids the disruption of large-scale, revolutionary changes and allows teams to learn and adapt as they go. The goal is to evolve the process, not to replace it.

3.  **Respect the Current Process, Roles, Responsibilities & Titles**: Kanban recognizes that existing processes, roles, and responsibilities have value and should be respected. It does not prescribe a new set of roles or a rigid process. Instead, it provides a way to improve the existing system from within.

4.  **Encourage Acts of Leadership at All Levels**: In Kanban, leadership is not limited to managers or executives. Everyone is encouraged to take initiative and propose improvements. This principle empowers team members to take ownership of their work and contribute to the continuous improvement of the process.

### 3. Key Practices (5-10 practices, 300-600 words)

Kanban’s principles are put into action through a set of key practices. These practices provide a framework for implementing and using Kanban effectively.

1.  **Visualize the Workflow**: This is the most fundamental practice in Kanban. It involves creating a visual model of your workflow, typically using a Kanban board. The board is divided into columns that represent the different stages of your process (e.g., To Do, In Progress, Done). Work items are represented by cards that move from left to right across the board as they progress through the workflow. This visualization makes it easy to see the status of work, identify bottlenecks, and communicate progress.

2.  **Limit Work in Progress (WIP)**: Limiting WIP means setting a maximum number of work items that can be in each stage of the workflow at any given time. This practice is crucial for preventing bottlenecks, reducing context switching, and improving flow. By limiting WIP, you create a pull system where new work is only started when there is capacity available. This helps to ensure a smooth and predictable flow of work.

3.  **Manage Flow**: The goal of Kanban is to create a smooth and healthy flow of work. This means monitoring the movement of work items through the system and identifying and addressing any interruptions or delays. By managing flow, you can reduce lead times, increase predictability, and deliver value to customers more quickly. Key metrics for managing flow include cycle time (the time it takes to complete a work item) and throughput (the number of work items completed per unit of time).

4.  **Make Process Policies Explicit**: To ensure that everyone on the team has a shared understanding of how the process works, it is important to make your process policies explicit. This includes defining things like when a work item is ready to be pulled into the next stage, what the WIP limits are for each stage, and what the definition of “done” is. Explicit policies provide a clear and consistent framework for decision-making and help to reduce ambiguity and confusion.

5.  **Implement Feedback Loops**: Feedback loops are essential for continuous improvement. In Kanban, feedback loops can take many forms, including daily stand-up meetings, regular review meetings, and retrospective meetings. These meetings provide opportunities for the team to review their process, discuss what is working well and what is not, and identify opportunities for improvement.

6.  **Improve Collaboratively, Evolve Experimentally**: Kanban is a process of continuous improvement. It encourages teams to take a scientific approach to change, where they form a hypothesis, make a change, and then measure the results. This allows teams to learn and adapt as they go, and to evolve their process in a way that is tailored to their specific needs and context.

### 4. Application Context (200-300 words)

- **Best Used For**:
    - **Continuous delivery environments**: Where work is delivered in a continuous flow rather than in fixed iterations.
    - **Maintenance and support teams**: Where work is often unplanned and needs to be prioritized and addressed as it arises.
    - **Processes with unclear or evolving requirements**: Where flexibility and adaptability are key.
    - **Teams with a high degree of variability in their work**: Where a one-size-fits-all approach is not effective.
    - **Improving existing workflows**: Where the goal is to make gradual improvements to an existing process rather than starting from scratch.

- **Not Suitable For**:
    - **Projects with fixed deadlines and scope**: Where a more predictive approach like Waterfall may be more appropriate.
    - **Teams that require a high degree of ceremony and structure**: Where a more prescriptive framework like Scrum may be a better fit.

- **Scale**: Individual/Team/Department/Organization/Multi-Organization/Ecosystem

- **Domains**: While Kanban originated in manufacturing, it is now widely used in a variety of domains, including:
    - Software development
    - IT operations
    - Marketing
    - Human resources
    - Customer support
    - Personal productivity

### 5. Implementation (400-600 words)

Successfully implementing Kanban requires careful planning and a commitment to its core principles and practices. The journey begins with understanding the prerequisites, followed by a series of concrete steps to get started. It is also important to be aware of common challenges and the factors that contribute to success.

**Prerequisites**

Before implementing Kanban, it is essential to have a clear understanding of the existing workflow. This means identifying the different stages that work goes through, from start to finish. It is also important to have a team that is open to change and willing to experiment with new ways of working. While Kanban does not require specific roles, having a designated person to champion the implementation and guide the team can be beneficial. Finally, it is helpful to have a basic understanding of Kanban's principles and practices, as this will provide a solid foundation for the implementation.

**Getting Started**

1.  **Map Your Workflow**: The first step is to create a visual representation of your workflow. This can be done on a physical whiteboard or with a digital Kanban tool. The board should be divided into columns that represent the different stages of your process. This simple act of visualization is often a powerful catalyst for improvement.

2.  **Define Work Items**: Next, define the types of work that your team does and create a card for each work item. The cards should contain enough information to understand what the work is and who is responsible for it. This helps to make work tangible and trackable.

3.  **Establish a Pull System with WIP Limits**: Instead of pushing work into the system, Kanban uses a pull system where new work is only started when there is capacity available. To enable this, you need to set Work in Progress (WIP) limits for each stage of your workflow. This is a critical step that helps to prevent bottlenecks and improve flow.

4.  **Establish a Regular Cadence of Meetings**: To ensure that the process is working effectively and to identify opportunities for improvement, it is important to establish a regular cadence of meetings. This can include daily stand-up meetings to discuss progress and any impediments, as well as regular review and retrospective meetings to reflect on the process and identify areas for improvement.

**Common Challenges**

- **Resistance to Change**: One of the most common challenges is resistance to change. People are often comfortable with their existing ways of working and may be reluctant to adopt a new approach. To overcome this, it is important to communicate the benefits of Kanban and to involve the team in the implementation process.

- **Setting WIP Limits**: Setting the right WIP limits can be challenging. If the limits are too high, the system will not be effective at preventing bottlenecks. If they are too low, the system may be starved of work. It is often a process of trial and error to find the right balance.

- **Ignoring Blockers**: Blockers are issues that prevent work from moving forward. It is important to have a clear process for identifying and addressing blockers. If blockers are ignored, they can quickly bring the entire system to a halt.

**Success Factors**

- **Strong Leadership Support**: Having strong leadership support is crucial for a successful Kanban implementation. Leaders can help to champion the change, remove impediments, and provide the resources needed for success.

- **Team Buy-in**: It is essential to have the buy-in of the team. The team needs to understand the benefits of Kanban and be willing to participate in the process of continuous improvement.

- **Focus on Flow**: The ultimate goal of Kanban is to improve the flow of work. This means focusing on reducing lead times, increasing predictability, and delivering value to customers more quickly. By keeping the focus on flow, you can ensure that your Kanban implementation is delivering real business value.

### 6. Evidence & Impact (300-500 words)

Kanban's effectiveness is not just theoretical; it is backed by a growing body of evidence from a wide range of industries. From its origins in manufacturing to its widespread adoption in software development and beyond, Kanban has demonstrated its ability to improve efficiency, predictability, and customer satisfaction.

**Notable Adopters**

- **Toyota**: The birthplace of Kanban, Toyota continues to use it as a cornerstone of its world-renowned Toyota Production System.
- **Zara**: The fast-fashion retailer uses Kanban principles to manage its supply chain and quickly respond to changing customer demands.
- **Pixar**: The animation studio has used Kanban to manage the complex workflow of creating animated films, from storyboarding to final rendering.
- **Spotify**: The music streaming service has used a modified version of Kanban, known as the "Spotify Model," to scale its agile development practices across multiple teams.
- **Microsoft**: Microsoft has been a major proponent of Kanban for software development, with many teams using it to manage their workflows and improve their delivery of software updates.
- **Encoparts**: A distribution logistics company, implemented Kanban to improve the operational efficiency of its international purchasing division, resulting in a significant increase in flow efficiency.
- **ULMA Handling Systems**: An engineering company, used Kanban to manage complex, long-term projects, improving visibility and communication.
- **Schlenk**: A chemical manufacturer, used Kanban to achieve project agility and transparency, significantly reducing cycle times.

**Documented Outcomes**

The implementation of Kanban has led to a variety of documented outcomes, including:

- **Reduced Lead Times**: By limiting WIP and improving flow, Kanban helps to reduce the time it takes to deliver value to customers. For example, Schlenk reduced its cycle time from 110 days to 44 days.
- **Increased Predictability**: Kanban's focus on flow and metrics like cycle time and throughput helps to make delivery times more predictable. This allows teams to make more reliable commitments to their customers.
- **Improved Quality**: By reducing context switching and allowing team members to focus on one task at a time, Kanban can help to improve the quality of work.
- **Increased Customer Satisfaction**: By delivering value to customers more quickly and predictably, Kanban can help to increase customer satisfaction.
- **Improved Team Morale**: Kanban's emphasis on collaboration, empowerment, and continuous improvement can lead to improved team morale and engagement.

**Research Support**

While much of the evidence for Kanban's effectiveness comes from case studies and anecdotal reports, there is a growing body of academic research on the topic. A 2017 study published in the *Journal of Systems and Software* found that the use of WIP limits in Kanban was associated with a significant reduction in cycle time. Another study, published in the *Proceedings of the 18th International Conference on Agile Software Development*, found that Kanban was an effective tool for managing workflow and improving team collaboration.

### 7. Cognitive Era Considerations (200-400 words)

As we move into the cognitive era, characterized by the increasing use of artificial intelligence and automation, the Kanban method is poised to evolve and become even more powerful. The core principles of Kanban—visualizing work, limiting WIP, and managing flow—are well-suited to a world where human and machine intelligence are increasingly intertwined.

**Cognitive Augmentation Potential**

AI and automation can augment Kanban in several ways. For example, AI-powered tools can be used to automatically track work items, collect data on cycle time and throughput, and identify potential bottlenecks before they occur. This can free up team members from the manual work of data collection and analysis, allowing them to focus on more creative and strategic tasks. AI can also be used to optimize WIP limits and to suggest improvements to the workflow based on historical data.

**Human-Machine Balance**

While AI and automation can handle many of the routine tasks associated with Kanban, the human element remains crucial. The principles of respecting the current process, encouraging leadership at all levels, and improving collaboratively are all uniquely human endeavors. The role of the team will shift from doing the work to designing the work system, setting the strategic direction, and handling the complex and ambiguous tasks that require human intuition and creativity. The Kanban board will become a shared space where humans and machines collaborate to create value.

**Evolution Outlook**

In the cognitive era, we can expect to see the emergence of “intelligent” Kanban systems that are able to learn and adapt on their own. These systems will be able to automatically adjust WIP limits, re-route work around bottlenecks, and even suggest new process policies based on real-time data. The Kanban board will evolve from a static visualization of the workflow to a dynamic and interactive dashboard that provides real-time insights and recommendations. However, the fundamental principles of Kanban will remain as relevant as ever, providing a timeless framework for managing work in an increasingly complex and uncertain world.

### 8. Commons Alignment Assessment (600-800 words)

This assessment evaluates the Kanban method against the seven dimensions of a commons-aligned organization. Kanban, as a process improvement methodology, is not inherently commons-aligned, but it can be a powerful tool for building and managing a commons.

1.  **Stakeholder Mapping**: Kanban itself does not prescribe any specific stakeholder mapping. However, its emphasis on visualizing the entire workflow can help to make the different stakeholders and their roles more visible. A well-designed Kanban board can show who is responsible for each stage of the process, from the customer who requests the work to the team member who delivers it. This transparency can help to foster a sense of shared ownership and accountability. To improve its commons alignment, a Kanban implementation could explicitly map out all stakeholders, including those who are often overlooked, such as the community and the environment.

2.  **Value Creation**: Kanban is focused on creating value for the customer. It does this by improving the flow of work and reducing the time it takes to deliver value. However, the definition of “value” is often limited to the economic value created for the customer and the organization. A more commons-aligned approach would be to broaden the definition of value to include social and environmental value. For example, a Kanban board could be used to track the environmental impact of a project or the social benefits it creates.

3.  **Value Preservation**: Kanban’s focus on continuous improvement is a key mechanism for value preservation. By constantly seeking to improve the process, Kanban helps to ensure that the organization remains relevant and effective over time. The practice of implementing feedback loops is also crucial for value preservation, as it allows the organization to adapt to changing circumstances and to learn from its mistakes. To further enhance its value preservation capabilities, a Kanban implementation could incorporate metrics that track the long-term health of the system, such as team morale and technical debt.

4.  **Shared Rights & Responsibilities**: Kanban’s principle of encouraging leadership at all levels is a step towards a more equitable distribution of rights and responsibilities. By empowering team members to take initiative and to propose improvements, Kanban can help to break down traditional hierarchies and to create a more collaborative and democratic work environment. However, Kanban does not explicitly address the issue of ownership or governance. A more commons-aligned approach would be to combine Kanban with a governance model that gives stakeholders a real say in how the organization is run.

5.  **Systematic Design**: Kanban is a systematic approach to process improvement. It provides a set of principles and practices that can be used to design and manage a more effective workflow. The use of explicit policies and WIP limits helps to create a more predictable and stable system. However, the design of the system is often left to the team or the organization. A more commons-aligned approach would be to involve a wider range of stakeholders in the design of the system, to ensure that it is aligned with the needs of the commons.

6.  **Systems of Systems**: Kanban can be scaled to manage complex systems of systems. The concept of “flight levels” provides a way to connect the work of different teams and to align them with the strategic goals of the organization. This can be a powerful tool for managing a commons, which is often a complex system of interconnected parts. To be truly effective, however, a systems-of-systems approach to Kanban needs to be combined with a deep understanding of the dynamics of the system as a whole.

7.  **Fractal Properties**: The principles of Kanban are fractal in nature. They can be applied at any scale, from the individual to the organization. This means that a Kanban implementation can be started small and then gradually scaled up as the organization grows. This fractal property makes Kanban a very adaptable and resilient methodology, which is well-suited to the dynamic and ever-changing nature of a commons.

**Overall Score: 3/5 (Transitional)**

Kanban is a powerful tool for improving the efficiency and effectiveness of any organization. Its emphasis on transparency, continuous improvement, and empowerment can be a great asset for building and managing a commons. However, Kanban itself is not a complete solution. To be truly commons-aligned, it needs to be combined with a broader set of principles and practices that address the issues of ownership, governance, and value definition. Without these additional elements, Kanban can easily be co-opted by a traditional, extractive logic. Therefore, it is best seen as a transitional tool that can help organizations on their journey towards a more commons-oriented way of working.

### 9. Resources & References (200-400 words)

**Essential Reading**

-   **Kanban: Successful Evolutionary Change for Your Technology Business** by David J. Anderson. This is the foundational book on Kanban for knowledge work. It provides a comprehensive overview of the method, its principles, and its practices.
-   **The Official Guide to the Kanban Method** by Kanban University. This guide provides a concise and authoritative overview of the Kanban method. It is a great starting point for anyone who is new to Kanban.
-   **Kanban from the Inside** by Mike Burrows. This book provides a deeper dive into the principles and practices of Kanban. It is a great resource for anyone who wants to take their Kanban implementation to the next level.

**Organizations & Communities**

-   **Kanban University**: The leading organization for Kanban training and certification. It provides a wealth of resources, including articles, webinars, and case studies.
-   **Lean Kanban Inc.**: The company founded by David J. Anderson. It provides consulting, training, and coaching on Kanban.

**Tools & Platforms**

-   **Jira**: A popular project management tool that includes a powerful Kanban board feature.
-   **Asana**: A work management platform that provides a flexible and easy-to-use Kanban board.
-   **Trello**: A simple and intuitive Kanban tool that is great for personal productivity and small teams.
-   **Businessmap**: A powerful Kanban platform that is designed for enterprise-level implementations.

**References**

[1] Atlassian. (n.d.). *Kanban*. Atlassian. Retrieved January 28, 2026, from https://www.atlassian.com/agile/kanban

[2] Asana. (n.d.). *What Is Kanban? A Beginner’s Guide for Agile Teams*. Asana. Retrieved January 28, 2026, from https://asana.com/resources/what-is-kanban

[3] Businessmap. (2023, June 16). *6 Real-World Kanban Examples with Proven Results*. Businessmap. Retrieved January 28, 2026, from https://businessmap.io/blog/kanban-examples

[4] Kanban University. (n.d.). *The Official Guide to The Kanban Method*. Kanban University. Retrieved January 28, 2026, from https://kanban.university/kanban-guide/

[5] ProjectManager. (2024, April 25). *Kanban History: Origin & Expansion Across Industries*. ProjectManager. Retrieved January 28, 2026, from https://www.projectmanager.com/blog/kanban-history

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/kanban/](https://commons-os.github.io/patterns/domain/kanban/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/kanban.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/kanban.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
