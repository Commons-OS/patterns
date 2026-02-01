---
id: pat_01kg5023zae8rthxw686kx5x4k
page_url: https://commons-os.github.io/patterns/kanban/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/kanban.md
slug: kanban
title: Kanban
aliases: [Kanban Method, Toyota Production System]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: operations
  category: [methodology, practice]
  era: [industrial, digital]
  origin: [toyota]
  status: draft
  commons_alignment: 4
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

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
Kanban provides a framework for making work visible to all involved stakeholders, primarily the delivery team and the customer. Responsibilities are implicitly defined by the workflow stages, clarifying who does what and when. However, it does not inherently define rights or expand the stakeholder map to include non-obvious actors like the environment, the community, or future generations, requiring conscious adaptation to serve a broader commons.

**2. Value Creation Capability:**
The pattern is exceptionally strong at enabling the creation of economic and operational value by optimizing for speed and predictability. While its focus is on workflow efficiency, its flexible nature allows for the integration of other value dimensions, such as quality, knowledge, and team well-being, by making policies and goals explicit. It provides the "how" for value creation but requires the team to define "what" value to create, leaving the door open for social and ecological considerations.

**3. Resilience & Adaptability:**
Resilience and adaptability are at the core of the Kanban method. By promoting incremental, evolutionary change and continuous improvement through feedback loops, it helps systems thrive on complexity and maintain coherence under stress. The practice of limiting Work in Progress (WIP) is a key mechanism that builds resilience by preventing system overload and ensuring a sustainable pace.

**4. Ownership Architecture:**
Kanban does not define an ownership architecture in terms of equity or formal governance. Its contribution lies in fostering a sense of process ownership and shared responsibility among team members. The principle of "encouraging acts of leadership at all levels" distributes the responsibility for process improvement, but it does not address the ownership of the value or assets generated by the process.

**5. Design for Autonomy:**
Kanban is highly compatible with autonomous systems, both human and machine. Its pull-based system and low coordination overhead make it ideal for distributed teams, DAOs, and AI-augmented workflows. By making the process and its rules explicit, it creates a clear, low-friction environment where autonomous agents can effectively participate and contribute to the workflow.

**6. Composability & Interoperability:**
As a method rather than a rigid framework, Kanban is designed for high composability and interoperability. It can be layered onto virtually any existing process and combined with other patterns (like Scrum or GTD) to create more comprehensive value-creation systems. This "start with what you do now" principle makes it a versatile building block for larger, more complex organizational designs.

**7. Fractal Value Creation:**
The logic of visualizing work, limiting WIP, and managing flow is fundamentally fractal. These principles can be applied at any scale, from an individual's personal workflow to a team's project board, and all the way up to an organization's portfolio management system. This scalability allows the same core logic for resilient value creation to be replicated and adapted across different levels of a system.

**Overall Score: 4/5 (Value Creation Enabler)**

**Rationale:**
Kanban is a powerful enabler for resilient value creation due to its focus on flow, adaptability, and fractal scalability. It provides a robust operating system for managing work and improving processes. However, it does not by itself provide a complete value creation architecture, as it lacks native constructs for expanded stakeholder mapping and formal ownership rights, requiring deliberate integration with other patterns to become a fully-fledged commons.

**Opportunities for Improvement:**
- Explicitly integrate non-obvious stakeholders (e.g., environment, community) into the visual workflow and policies.
- Broaden the definition of "work items" and "value" to include non-economic contributions like knowledge creation or ecological regeneration.
- Combine Kanban with governance patterns that define shared ownership and decision-making rights over the value created.

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
