---
id: pat_01kg5023zwft8t7k63bfadqqwg
page_url: https://commons-os.github.io/patterns/domain/scrum/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/scrum.md
slug: scrum
title: Scrum
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: design
  category: framework
  era: digital
  origin: [agile-manifesto, hirotaka-takeuchi, ikujiro-nonaka]
  status: draft
  commons_alignment: 3
generalizes_from: []
specializes_to: ["pat_01kg5023zbftgswm71hgn15e2f", "pat_01kg5023zwft8t7k639ctqfhce"]
enables: []
requires: []
related: ["pat_01kg5023ydftgramg3qp7rjkam", "pat_01kg5023zwft8t7k635h086kyj", "pat_01kg5023ypf08rv1dagnb27bjj", "pat_01kg5023vwe00rptkqr3z6pkd9", "pat_01kg5023ypf08rv1dafrvtxwdr", "pat_01kg5023zbftgswm71hgn15e2f", "pat_01kg5023y7e50rxp3ew60jdasx", "pat_01kg5023ztenhrk74hc9a8qszj", "pat_01kg5023zwft8t7k639ctqfhce", "pat_01kg50240wfjh98jqx34wdddnm", "pat_01kg5023xaemr9xsmd0fgaxe86", "pat_01kg5023yneg8rmv1200tvfn3g", "pat_01kg5023yneg8rmv122d6v7bg5", "pat_01kg5023xaemr9xsmcy13gf405", "pat_01kg5023xaemr9xsmcxd0eg8ek"]
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview (150-300 words)

Scrum is an agile framework designed to help teams develop, deliver, and sustain complex products. It provides a lightweight yet powerful structure for managing work in iterative cycles called Sprints. The core idea of Scrum is to address complex adaptive problems, while productively and creatively delivering products of the highest possible value. It is not a methodology or a process, but a framework within which you can employ various processes and techniques. The framework is founded on empiricism, which asserts that knowledge comes from experience and making decisions based on what is known. 

The primary value of Scrum lies in its ability to create a feedback loop that allows for continuous improvement and adaptation. By working in short Sprints, teams can regularly inspect their work and adapt their plans based on new information. This iterative approach helps to manage risk, control the development process, and ensure that the final product meets the needs of the customers. 

The origin of Scrum can be traced back to a 1986 Harvard Business Review article by Hirotaka Takeuchi and Ikujiro Nonaka, titled "The New New Product Development Game." They described a new, holistic approach to product development that they compared to the game of rugby, where the team tries to go the distance as a unit, passing the ball back and forth. This idea was later formalized into the Scrum framework by Ken Schwaber and Jeff Sutherland in the early 1990s. They presented their first paper on Scrum at OOPSLA '95, and have continued to develop and refine the framework ever since, culminating in the Scrum Guide, which is the definitive guide to the framework.


### 2. Core Principles (3-7 principles, 200-400 words)

Scrum is based on a few core principles that are essential for its successful implementation. These principles provide the foundation for the framework's practices and events.

1.  **Empirical Process Control**: Scrum is founded on the principles of transparency, inspection, and adaptation. This empirical approach allows teams to manage the unpredictability of complex projects. 
    *   **Transparency**: All aspects of the process must be visible to those responsible for the outcome. This includes the product backlog, the sprint backlog, and the increment. Key stakeholders must have access to the same information to make informed decisions.
    *   **Inspection**: The various artifacts and the progress toward the Sprint Goal must be inspected frequently to detect undesirable variances. Inspection should not be so frequent that it gets in the way of the work, but it should be done diligently.
    *   **Adaptation**: If an inspector determines that one or more aspects of a process deviate outside acceptable limits, and that the resulting product will be unacceptable, the process or the material being processed must be adjusted. These adjustments must be made as soon as possible to minimize further deviation.

2.  **Self-Organization**: Scrum teams are self-organizing and cross-functional. They have the autonomy to decide how to best accomplish their work, rather than being directed by others outside the team. This encourages creativity, accountability, and ownership.

3.  **Collaboration**: Scrum emphasizes collaboration among all stakeholders, including the development team, the product owner, and the customers. This collaboration is essential for ensuring that the right product is built and that it meets the needs of the users.

4.  **Value-Based Prioritization**: The Product Owner is responsible for prioritizing the work in the product backlog based on its value to the business and the customer. This ensures that the team is always working on the most important features first.

5.  **Time-boxing**: All Scrum events are time-boxed, meaning they have a maximum duration. This ensures that a predefined amount of time is spent on each event and that the team does not waste time on unproductive activities.

6.  **Iterative Development**: Scrum is an iterative process, where work is done in short cycles called Sprints. This allows the team to deliver a potentially releasable increment of the product at the end of each Sprint, and to get feedback from stakeholders on a regular basis.


### 3. Key Practices (5-10 practices, 300-600 words)

Scrum is put into practice through a series of events, artifacts, and roles. These practices provide the structure for implementing the Scrum framework and its principles.

1.  **The Sprint**: A Sprint is a time-boxed event of one month or less during which a "Done," usable, and potentially releasable product Increment is created. Sprints have consistent lengths throughout a development effort. A new Sprint starts immediately after the conclusion of the previous Sprint.

2.  **Sprint Planning**: At the beginning of each Sprint, the Scrum Team holds a Sprint Planning meeting to decide what work will be done in the upcoming Sprint. The Product Owner presents the highest-priority items from the Product Backlog, and the Development Team selects the amount of work they believe they can accomplish during the Sprint. This work is then moved from the Product Backlog to the Sprint Backlog.

3.  **Daily Scrum**: The Daily Scrum is a 15-minute time-boxed event for the Development Team to synchronize activities and create a plan for the next 24 hours. This is done by inspecting the work since the last Daily Scrum and forecasting the work that could be done before the next one. The Daily Scrum is held at the same time and place each day to reduce complexity.

4.  **Sprint Review**: At the end of each Sprint, the Scrum Team and stakeholders hold a Sprint Review to inspect the Increment and adapt the Product Backlog if needed. During the Sprint Review, the Development Team demonstrates the work that it has "Done" and answers questions about the Increment. This is an informal meeting, not a status meeting, and the presentation of the Increment is intended to elicit feedback and foster collaboration.

5.  **Sprint Retrospective**: The Sprint Retrospective is an opportunity for the Scrum Team to inspect itself and create a plan for improvements to be enacted during the next Sprint. The retrospective occurs after the Sprint Review and prior to the next Sprint Planning. The purpose of the Sprint Retrospective is to: inspect how the last Sprint went with regards to people, relationships, process, and tools; identify and order the major items that went well and potential improvements; and create a plan for implementing improvements to the way the Scrum Team performs its work.

6.  **Product Backlog**: The Product Backlog is an ordered list of everything that is known to be needed in the product. It is the single source of requirements for any changes to be made to the product. The Product Owner is responsible for the Product Backlog, including its content, availability, and ordering.

7.  **Sprint Backlog**: The Sprint Backlog is the set of Product Backlog items selected for the Sprint, plus a plan for delivering the product Increment and realizing the Sprint Goal. The Sprint Backlog is a forecast by the Development Team about what functionality will be in the next Increment and the work needed to deliver that functionality into a "Done" Increment.

8.  **Increment**: The Increment is the sum of all the Product Backlog items completed during a Sprint and all previous Sprints. At the end of a Sprint, the new Increment must be "Done," which means it is in a usable condition and meets the Scrum Team’s definition of "Done."


### 4. Application Context (200-300 words)

Scrum is a versatile framework that can be applied in a wide variety of contexts, but it is most effective in certain situations and less so in others.

- **Best Used For**:
    - **Complex Projects**: Scrum is ideal for projects with a high degree of uncertainty and complexity, where the requirements are likely to change over time.
    - **Product Development**: It is particularly well-suited for the development of new products, where innovation and speed to market are critical.
    - **Cross-Functional Teams**: Scrum works best with small, cross-functional teams that have all the skills necessary to deliver a potentially releasable increment of the product.
    - **Customer-Centric Projects**: It is a good choice for projects where customer feedback is essential for success, as it provides regular opportunities for inspection and adaptation.
    - **Projects with unclear or evolving requirements**: The iterative nature of Scrum allows for flexibility and adaptation as the project progresses and requirements become clearer.

- **Not Suitable For**:
    - **Simple, predictable projects**: For projects with well-defined requirements and a low degree of uncertainty, a more traditional, plan-driven approach may be more efficient.
    - **Projects with a fixed scope and deadline**: While Scrum can be used in these situations, its flexibility may not be fully utilized, and a more rigid approach might be more appropriate.

- **Scale**: Scrum can be applied at various scales, from a single team to a large, multi-team organization. However, scaling Scrum requires additional frameworks and practices, such as Scrum of Scrums, LeSS (Large-Scale Scrum), or SAFe (Scaled Agile Framework).

- **Domains**: Scrum is most commonly used in the software development industry, but it has also been successfully applied in a wide range of other domains, including:
    - Marketing and sales
    - Research and development
    - Customer support
    - Education
    - Government


### 5. Implementation (400-600 words)

Successfully implementing Scrum requires more than just following the rules. It requires a shift in mindset and a commitment to the framework's principles and values. Here are some guidelines for getting started with Scrum.

- **Prerequisites**:
    - **Management Buy-in**: Successful Scrum implementation requires strong support from management. This includes providing the necessary resources, removing organizational impediments, and empowering the team to self-organize.
    - **A Cross-Functional Team**: The team should have all the skills necessary to deliver a potentially releasable increment of the product. This may include developers, testers, designers, and other specialists.
    - **A Dedicated Product Owner**: The Product Owner is a critical role in Scrum, and it is important to have someone who is dedicated to the role and has the authority to make decisions about the product.
    - **A Trained Scrum Master**: The Scrum Master is the coach and facilitator for the team, and it is important to have someone who is well-trained in the Scrum framework and can guide the team through the process.

- **Getting Started**:
    1.  **Form the Team**: Assemble a cross-functional team of 5-9 people and ensure they have the necessary skills and resources.
    2.  **Create the Product Backlog**: The Product Owner works with stakeholders to create an initial Product Backlog, which is a prioritized list of all the features and requirements for the product.
    3.  **Hold the First Sprint Planning Meeting**: The team holds its first Sprint Planning meeting to select a set of items from the Product Backlog to work on during the first Sprint.
    4.  **Start the First Sprint**: The team begins working on the items in the Sprint Backlog, holding a Daily Scrum each day to coordinate their work.
    5.  **Hold the First Sprint Review and Retrospective**: At the end of the Sprint, the team holds a Sprint Review to demonstrate the work they have completed and a Sprint Retrospective to reflect on their process and identify areas for improvement.

- **Common Challenges**:
    - **Resistance to Change**: Scrum requires a significant change in mindset and culture, and it is common to encounter resistance from individuals and teams who are used to more traditional ways of working.
    - **Lack of a True Product Owner**: If the Product Owner is not empowered to make decisions or is not available to the team, it can lead to delays and confusion.
    - **An Ineffective Scrum Master**: A Scrum Master who is not effective in their role can fail to remove impediments and guide the team, leading to a dysfunctional team.
    - **Scope Creep**: It is important to protect the Sprint from scope creep, which is the tendency for the scope of a project to expand over time. The Product Owner is responsible for managing the Product Backlog and ensuring that the team is focused on the most valuable work.

- **Success Factors**:
    - **Strong Leadership**: Strong leadership from the Product Owner and Scrum Master is essential for success.
    - **Team Commitment**: The entire team must be committed to the Scrum framework and its principles.
    - **Continuous Improvement**: The team should always be looking for ways to improve its process and become more effective.
    - **A Supportive Environment**: The organization must provide a supportive environment for the team, including the necessary resources, training, and empowerment.


### 6. Evidence & Impact (300-500 words)

Scrum has been widely adopted across a variety of industries, and there is a growing body of evidence to support its effectiveness. Numerous case studies and research papers have documented the positive impact of Scrum on team productivity, product quality, and customer satisfaction.

- **Notable Adopters**:
    - **Microsoft**: Microsoft has been using Scrum for many years and has published numerous case studies on its experiences. They have found that Scrum has helped them to improve their ability to deliver complex products in a timely manner.
    - **Google**: Google uses Scrum in many of its product development teams. They have found that it helps them to innovate more quickly and to respond to changing market conditions.
    - **Amazon**: Amazon has used Scrum to develop and deliver a wide range of products and services, from its e-commerce platform to its cloud computing services.
    - **Spotify**: Spotify is well-known for its agile culture, which is heavily influenced by Scrum. They have developed their own unique approach to scaling agile, which is based on the principles of Scrum.
    - **ING**: The Dutch banking group ING has undergone a large-scale agile transformation, with Scrum as a key component. They have reported significant improvements in time to market and customer satisfaction.

- **Documented Outcomes**:
    - **Increased Productivity**: Many organizations have reported significant increases in productivity after adopting Scrum. A study by the Standish Group found that agile projects are three times more likely to succeed than traditional projects.
    - **Improved Quality**: The iterative nature of Scrum and the focus on a "Done" increment at the end of each Sprint helps to improve the quality of the product. Early and frequent testing helps to identify and fix defects early in the development process.
    - **Faster Time to Market**: Scrum helps to reduce the time it takes to deliver a product to market by breaking down the work into small, manageable increments.
    - **Increased Customer Satisfaction**: The close collaboration between the development team and the customer helps to ensure that the final product meets the needs of the users.

- **Research Support**:
    - A 2022 study published in the journal *PeerJ Computer Science* found that applying Scrum ensured that defects were dealt with within reasonable timeframes and that early testing reduced code defects by 42%.
    - A 2023 study in the *ACM Transactions on Software Engineering and Methodology* developed and tested a comprehensive theoretical model of Scrum team effectiveness, identifying key factors that contribute to success.
    - Research from the University of Coimbra, Portugal, has shown that Scrum can be an effective tool for managing global software development projects, despite the challenges of working across different time zones and cultures.


### 7. Cognitive Era Considerations (200-400 words)

As we move into the cognitive era, characterized by the increasing use of artificial intelligence and automation, the Scrum framework is likely to evolve in significant ways. AI has the potential to augment the capabilities of Scrum teams and enhance the effectiveness of the framework.

- **Cognitive Augmentation Potential**:
    - **AI-Powered Analytics**: AI can be used to analyze the product backlog, identify dependencies and risks, and optimize the sprint backlog based on team capacity and historical data. This can help teams to make more informed decisions and to improve their planning and forecasting.
    - **Automated Testing and Deployment**: AI can be used to automate testing and deployment, which can help to reduce the time it takes to deliver a product to market and to improve the quality of the product.
    - **Intelligent Assistants**: AI-powered assistants can help Scrum Masters to facilitate meetings, track progress, and remove impediments. They can also provide real-time feedback to the team on their performance.

- **Human-Machine Balance**:
    - While AI can automate many of the tasks involved in Scrum, it is important to maintain a balance between human and machine. Humans will still be needed for tasks that require creativity, critical thinking, and emotional intelligence, such as setting the product vision, understanding customer needs, and collaborating with each other.
    - The role of the Scrum Master may evolve from a process coach to a human-machine interaction coach, helping the team to work effectively with AI-powered tools.

- **Evolution Outlook**:
    - The Scrum framework is likely to evolve to incorporate AI-powered tools and techniques. The Scrum events may be adapted to include AI-powered analysis and feedback, and new roles may emerge to manage the human-machine interface.
    - The focus of Scrum may shift from managing tasks to managing value creation, with AI helping to automate the more mundane aspects of the work and freeing up humans to focus on more creative and strategic activities.


### 8. Commons Alignment Assessment (600-800 words)

This section assesses the Scrum framework against the seven dimensions of the Commons Stack, a framework for designing and building commons-based P2P systems. The assessment provides a score from 1 to 5, where 1 is extractive and 5 is exemplary commons.

1.  **Stakeholder Mapping**: Scrum explicitly defines the roles of the Product Owner, Scrum Master, and Development Team. It also acknowledges the importance of other stakeholders, such as customers, users, and the sponsoring organization. However, the framework itself does not provide a systematic process for identifying and mapping all relevant stakeholders. The Product Owner is responsible for representing the interests of the stakeholders, but the process for how they do this is not prescribed. This can lead to a narrow focus on the needs of the most vocal or powerful stakeholders, while the needs of others are overlooked.

2.  **Value Creation**: Scrum is designed to create value for the customer by delivering a potentially releasable increment of the product at the end of each Sprint. The framework's focus on value-based prioritization ensures that the team is always working on the most important features first. However, the definition of "value" is often limited to the economic value for the sponsoring organization. The framework does not explicitly consider other types of value, such as social or environmental value.

3.  **Value Preservation**: The iterative nature of Scrum helps to preserve the value of the product over time by allowing for continuous feedback and adaptation. The framework's focus on a "Done" increment at the end of each Sprint ensures that the product is always in a usable state. However, the framework does not provide any guidance on how to manage the long-term sustainability of the product, such as how to handle technical debt or how to ensure that the product remains relevant as the market changes.

4.  **Shared Rights & Responsibilities**: Scrum promotes shared rights and responsibilities within the Scrum Team. The team is self-organizing and has the autonomy to decide how to best accomplish its work. However, the distribution of rights and responsibilities between the Scrum Team and other stakeholders is not always clear. The Product Owner has the sole authority to make decisions about the product, which can lead to a concentration of power.

5.  **Systematic Design**: Scrum provides a systematic process for managing the development of complex products. The framework's events, artifacts, and roles provide a clear structure for the team to follow. However, the framework is not a complete methodology and must be supplemented with other practices and techniques. The success of Scrum depends on the team's ability to effectively implement the framework and to adapt it to their specific context.

6.  **Systems of Systems**: Scrum can be used in conjunction with other patterns and frameworks, such as Kanban, Lean, and XP (Extreme Programming). There are also several frameworks for scaling Scrum to large, multi-team organizations, such as Scrum of Scrums, LeSS (Large-Scale Scrum), and SAFe (Scaled Agile Framework). However, the integration of Scrum with other systems can be challenging and requires careful planning and coordination.

7.  **Fractal Properties**: The principles of Scrum, such as empiricism, self-organization, and collaboration, can be applied at different scales, from a single team to a large organization. However, scaling Scrum requires more than just replicating the framework at different levels. It requires a fundamental shift in the organization's culture and structure.

**Overall Score**: 3/5 (Transitional)

**Rationale**: Scrum is a powerful framework for managing complex projects, but it has some limitations from a commons perspective. The framework's focus on economic value, its lack of a systematic process for stakeholder mapping, and its potential for power concentration prevent it from being a fully commons-aligned pattern. However, the framework's emphasis on collaboration, self-organization, and continuous improvement provides a solid foundation for building more commons-oriented systems.

**Opportunities for Improvement**: To improve its commons alignment, the Scrum framework could be extended to include:

*   A more systematic process for identifying and mapping all relevant stakeholders.
*   A broader definition of value that includes social and environmental value.
*   Guidance on how to manage the long-term sustainability of the product.
*   A more distributed model of decision-making that empowers all stakeholders to participate in the governance of the product.


### 9. Resources & References (200-400 words)

- **Essential Reading**:
    - **The Scrum Guide**: The definitive guide to Scrum, written by its co-creators, Ken Schwaber and Jeff Sutherland. It is available for free on the Scrum.org website.
    - **"The New New Product Development Game"**: This 1986 Harvard Business Review article by Hirotaka Takeuchi and Ikujiro Nonaka is considered the origin of the ideas that became Scrum.
    - **"Scrum: The Art of Doing Twice the Work in Half the Time"**: A book by Jeff Sutherland that provides a comprehensive overview of the Scrum framework and its principles.
    - **"Agile Project Management with Scrum"**: A book by Ken Schwaber that provides a practical guide to implementing Scrum.

- **Organizations & Communities**:
    - **Scrum.org**: An organization founded by Ken Schwaber that provides Scrum training, certification, and resources.
    - **Scrum Alliance**: A non-profit organization that provides Scrum training, certification, and community support.

- **Tools & Platforms**:
    - **Jira**: A popular software development tool that provides support for Scrum and other agile frameworks.
    - **Trello**: A flexible and visual tool that can be used to manage Scrum projects.
    - **Asana**: A project management tool that can be adapted to support Scrum workflows.

- **References**:
    - Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
    - Takeuchi, H., & Nonaka, I. (1986). The New New Product Development Game. *Harvard Business Review*.
    - Sutherland, J. (2014). *Scrum: The Art of Doing Twice the Work in Half the Time*. Crown Business.
    - Schwaber, K. (2004). *Agile Project Management with Scrum*. Microsoft Press.
    - Alami, A. (2022). How Scrum adds value to achieving software quality?. *PeerJ Computer Science*, 8, e1041.
    - Verwijs, C. (2023). A Theory of Scrum Team Effectiveness. *ACM Transactions on Software Engineering and Methodology*, 32(4), 1-49.

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/scrum/](https://commons-os.github.io/patterns/domain/scrum/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/scrum.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/scrum.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
