---
id: pat_01kg5023zbftgswm71hgn15e2f
page_url: https://commons-os.github.io/patterns/large-scale-scrum-less/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/large-scale-scrum-less.md
slug: large-scale-scrum-less
title: Large-Scale Scrum (LeSS)
aliases: [LeSS]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: design
  category: [framework]
  era: [digital]
  origin: [agile-manifesto, craig-larman, bas-vodde]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: ["pat_01kg5023zwft8t7k63bfadqqwg"]
specializes_to: []
enables: []
requires: []
related: ["pat_01kg5023ydftgramg3qp7rjkam", "pat_01kg5023zwft8t7k635h086kyj", "pat_01kg5023ypf08rv1dagnb27bjj", "pat_01kg5023vwe00rptkqr3z6pkd9", "pat_01kg5023ypf08rv1dafrvtxwdr", "pat_01kg5023y7e50rxp3ew60jdasx", "pat_01kg5023ztenhrk74hc9a8qszj", "pat_01kg5023zwft8t7k639ctqfhce", "pat_01kg5023zwft8t7k63bfadqqwg", "pat_01kg50240wfjh98jqx34wdddnm", "pat_01kg5023xaemr9xsmd0fgaxe86", "pat_01kg5023yneg8rmv1200tvfn3g", "pat_01kg5023yneg8rmv122d6v7bg5", "pat_01kg5023xaemr9xsmcy13gf405", "pat_01kg5023xaemr9xsmcxd0eg8ek"]
contributors: [higgerix, cloudsters]
sources: 
  - https://less.works/
  - https://www.atlassian.com/agile/agile-at-scale/less
  - https://less.works/case-studies/john-deere
  - https://www.amazon.com/Large-Scale-Scrum-More-Addison-Wesley-Signature/dp/0321985710
  - https://www.amazon.com/Practices-Scaling-Lean-Agile-Development/dp/0321636406
  - https://www.mdpi.com/2227-9709/9/1/20
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Large-Scale Scrum (LeSS) is a framework for applying Scrum to multiple teams who work together on a single, complete product. It is not a separate, “new and improved” Scrum, but rather a way of scaling up the foundational principles of Scrum to a larger context. The core problem that LeSS addresses is the tendency for organizations to add excessive processes, roles, and artifacts as they grow, leading to increased complexity, slower delivery, and a disconnect from customer value. LeSS counteracts this by providing a minimalist framework that descales complexity by simplifying the organizational structure. The primary value of LeSS lies in its ability to help large organizations achieve the same benefits of agility that small Scrum teams enjoy: faster delivery, higher quality, increased adaptiveness, and a stronger focus on the customer. The origin of LeSS can be traced back to the experiences of Craig Larman and Bas Vodde, who, after years of consulting on large-scale Agile adoptions, distilled their observations and experiments into a set of principles and practices. They observed that many attempts to scale Scrum involved adding layers of management and coordination, which ultimately undermined the very agility they were trying to achieve. In response, they developed LeSS as a way to scale by *descaling*—removing organizational complexity to allow the simple power of Scrum to flourish, even with dozens or hundreds of developers. Their work, culminating in the books *Scaling Lean & Agile Development* and *Large-Scale Scrum: More with LeSS*, provides the foundation for the framework.


### 2. Core Principles

LeSS is built upon a set of ten core principles that guide its implementation and application. These principles are not rigid rules but rather a set of foundational ideas that help organizations to think and adapt their approach to scaling Scrum in a way that is consistent with the underlying values of Agile and Lean thinking.

1.  **Large-Scale Scrum is Scrum**: This is the most fundamental principle. LeSS is not a replacement for Scrum but an extension of it. It takes the core elements of single-team Scrum and applies them to a multi-team context without adding unnecessary complexity. The goal is to have multiple teams working as if they were one large Scrum team.

2.  **Empirical Process Control**: LeSS relies on the empirical pillars of transparency, inspection, and adaptation. Rather than following a prescriptive process, organizations are encouraged to experiment, learn, and adapt their practices based on evidence. This allows for a more context-sensitive and effective implementation.

3.  **Transparency**: True transparency is essential for empirical process control. In a LeSS context, this means having a single, shared Product Backlog, a common Definition of Done, and open communication channels. This transparency enables honest conversations about progress and impediments.

4.  **More with Less**: This principle embodies the minimalist spirit of LeSS. It advocates for achieving more value with less process, fewer roles, and less overhead. By simplifying the organizational structure, LeSS aims to increase ownership, purpose, and joy in work.

5.  **Whole Product Focus**: The entire effort in a LeSS implementation is directed towards delivering a single, integrated, and shippable product at the end of each Sprint. This principle ensures that all teams are aligned towards a common goal and that the focus remains on delivering value to the customer.

6.  **Customer-Centric**: The customer is the ultimate arbiter of value. LeSS emphasizes a deep understanding of customer needs and a relentless focus on delivering what the customer wants. This is achieved through short feedback loops, direct interaction with customers, and a shared understanding of the customer's perspective.

7.  **Continuous Improvement Towards Perfection**: LeSS organizations are never satisfied with the status quo. They are constantly seeking to improve their processes, practices, and product. This principle encourages a culture of humble and radical improvement, where teams are empowered to experiment and learn.

8.  **Systems Thinking**: LeSS encourages a holistic view of the organization and the development process. Instead of optimizing individual parts, the focus is on optimizing the whole system for value delivery. This means understanding the interactions between different parts of the system and avoiding local optimizations that can lead to global sub-optimization.

9.  **Lean Thinking**: LeSS incorporates many principles from Lean thinking, such as a focus on value, the elimination of waste, and respect for people. Managers in a LeSS organization are expected to be teachers and coaches who help their teams to apply Lean and systems thinking to their work.

10. **Queueing Theory**: LeSS applies insights from queueing theory to manage the flow of work. By understanding the negative impact of long queues, large batches, and high levels of work-in-progress, LeSS helps organizations to reduce cycle times and increase throughput.


### 3. Key Practices

LeSS is not just a set of principles; it also includes a set of key practices that provide a concrete starting point for implementation. These practices are designed to be as simple as possible while still providing the necessary structure for multiple teams to work together effectively.

1.  **LeSS and LeSS Huge Frameworks**: LeSS offers two distinct frameworks to cater to different scales of development. **LeSS** is designed for two to eight teams, providing a minimal set of adjustments to single-team Scrum. **LeSS Huge** is for organizations with more than eight teams and introduces an additional layer of structure in the form of Requirement Areas and Area Product Owners to manage the increased complexity.

2.  **One Product Backlog**: In LeSS, there is only one Product Backlog for the entire product, regardless of the number of teams. This ensures that all teams are working from a single source of truth and are aligned towards the same product vision. The Product Backlog is owned and managed by the Product Owner.

3.  **One Product Owner**: There is only one Product Owner for the entire product. This individual is responsible for the overall product vision, prioritizing the Product Backlog, and making the final decisions about what gets built. This single point of accountability is crucial for maintaining a coherent product strategy.

4.  **Area Product Owners (in LeSS Huge)**: In a LeSS Huge implementation, the Product Owner is supported by a team of Area Product Owners. Each Area Product Owner is responsible for a specific Requirement Area, which is a major area of customer concern. They work closely with the teams in their area and the overall Product Owner to ensure that the work being done is aligned with the product vision.

5.  **Cross-Functional, Feature Teams**: All teams in a LeSS implementation are cross-functional and are organized as feature teams. This means that each team has all the skills necessary to deliver a complete, end-to-end customer feature. There are no single-specialist teams, as this would create dependencies and handoffs.

6.  **One Common Sprint**: All teams work in the same Sprint, with the same start and end dates. This ensures that all teams are synchronized and that a potentially shippable product increment is produced at the end of each Sprint.

7.  **Sprint Planning Part 1 and 2**: Sprint Planning is divided into two parts. **Part 1** is a joint meeting where representatives from all teams meet with the Product Owner to select the items for the upcoming Sprint. **Part 2** is held by each team individually to plan their work for the Sprint.

8.  **Overall Retrospective**: In addition to the individual team retrospectives, LeSS introduces an Overall Retrospective. This is a meeting where representatives from all teams, the Product Owner, and the Scrum Masters come together to discuss and address system-level issues that are affecting the entire organization.

9.  **Product Backlog Refinement (PBR)**: PBR is a continuous process of clarifying and estimating items in the Product Backlog. In LeSS, this can be done in a variety of ways, including multi-team PBR sessions where several teams refine items together.

10. **Coordination and Integration**: LeSS emphasizes direct communication and collaboration between teams. Instead of relying on formal coordination roles or processes, teams are encouraged to talk to each other, share code, and use techniques like travelers (team members who temporarily join another team) to facilitate coordination.


### 4. Application Context

LeSS is a powerful framework, but it is not a one-size-fits-all solution. Understanding the context in which it is most likely to succeed is crucial for a successful adoption.

**Best Used For:**

*   **Large-scale product development:** LeSS is specifically designed for situations where multiple teams need to collaborate on a single product.
*   **Organizations committed to deep change:** LeSS is not a superficial process change; it requires a fundamental shift in organizational structure and culture.
*   **Environments where customer-centricity is a priority:** The framework's emphasis on a whole-product focus and direct customer feedback makes it ideal for organizations that want to be more responsive to customer needs.
*   **Companies seeking to simplify their organizational structure:** LeSS provides a blueprint for descaling complexity and removing unnecessary layers of management and bureaucracy.
*   **Situations where a long-term commitment to continuous improvement is possible:** LeSS is not a quick fix; it requires a sustained effort to learn, adapt, and improve over time.

**Not Suitable For:**

*   **Organizations that are not willing to change their structure:** If a company is resistant to breaking down functional silos and empowering teams, a LeSS adoption is unlikely to succeed.
*   **Project-centric organizations:** LeSS is designed for product development, not project management. It is not a good fit for organizations that are organized around temporary projects with fixed scopes and deadlines.

**Scale:**

LeSS is designed to be applicable across a range of scales, from a single department to an entire organization. The two frameworks, LeSS and LeSS Huge, provide a path for scaling from a few teams to dozens or even hundreds of teams. However, the emphasis is always on descaling complexity, so even at a large scale, the goal is to maintain a simple and flat organizational structure.

**Domains:**

LeSS has been successfully applied in a wide variety of industries, including finance, insurance, healthcare, telecommunications, and automotive. Any organization that is developing a large and complex product with multiple teams can potentially benefit from LeSS.


### 5. Implementation

Implementing LeSS is a significant undertaking that requires careful planning and a long-term commitment. It is not a process that can be rushed or implemented in a piecemeal fashion. The following provides a high-level overview of the key considerations for a LeSS adoption.

**Prerequisites:**

*   **A solid understanding of single-team Scrum:** Before attempting to scale Scrum, it is essential to have a solid foundation in the basics. The organization should have several teams that are successfully using Scrum and have a deep understanding of its principles and practices.
*   **Management support:** A LeSS adoption requires strong and visible support from management. Managers need to be willing to champion the change, remove organizational impediments, and empower the teams to self-organize.
*   **A willingness to experiment and learn:** LeSS is not a prescriptive framework. It provides a set of guiding principles and practices, but the specific implementation will vary depending on the context. The organization needs to be willing to experiment, learn from its mistakes, and adapt its approach over time.

**Getting Started:**

1.  **Educate the organization:** The first step is to educate everyone in the organization about LeSS, from senior management to the individual team members. This can be done through training, workshops, and coaching.
2.  **Define the product:** A clear and shared understanding of the product is essential. The organization needs to define the product in a way that is meaningful to both the business and the development teams.
3.  **Form the teams:** The next step is to form the cross-functional feature teams. This may require a significant reorganization of the existing structure.
4.  **Select the Product Owner:** A single Product Owner needs to be selected for the entire product. This individual should have a deep understanding of the business, the customers, and the market.
5.  **Start with a small number of teams:** It is generally recommended to start a LeSS adoption with a small number of teams (2-4) and then gradually scale up as the organization gains experience.

**Common Challenges:**

*   **Resistance to change:** LeSS requires a significant change in mindset and behavior, and there is likely to be resistance from individuals and groups who are comfortable with the old way of working.
*   **Functional silos:** Breaking down functional silos and creating cross-functional teams can be a major challenge in many organizations.
*   **Lack of management support:** Without strong and consistent support from management, a LeSS adoption is unlikely to succeed.
*   **Difficulty in finding a single Product Owner:** Finding an individual with the skills, knowledge, and authority to be the Product Owner for a large product can be difficult.
*   **Coordination and communication overhead:** As the number of teams increases, so does the potential for coordination and communication overhead. LeSS provides a set of practices for managing this, but it is still a significant challenge.

**Success Factors:**

*   **A clear and compelling vision:** The organization needs to have a clear and compelling vision for why it is adopting LeSS and what it hopes to achieve.
*   **A dedicated and empowered Product Owner:** The success of a LeSS adoption depends heavily on the effectiveness of the Product Owner.
*   **A culture of trust and transparency:** LeSS requires a high degree of trust and transparency between all members of the organization.
*   **A focus on technical excellence:** Technical excellence is not optional in LeSS. The organization needs to invest in practices like continuous integration, test automation, and refactoring to ensure that it can deliver a high-quality product at scale.
*   **Patience and persistence:** A LeSS adoption is a long-term journey, not a short-term project. The organization needs to be patient and persistent in its efforts to learn and improve.


### 6. Evidence & Impact

While LeSS is a relatively new framework compared to some other scaling approaches, there is a growing body of evidence to support its effectiveness. The following provides a summary of some of the notable adopters, documented outcomes, and research support for LeSS.

**Notable Adopters:**

*   **John Deere:** The agricultural machinery giant used LeSS to overcome challenges with missed delivery dates and quality problems. The adoption of LeSS led to more reliable forecasting, improved quality, and a greater sense of ownership among the teams. [3]
*   **BMW:** The German automaker has used LeSS in various parts of its organization, including the development of its autonomous driving platform. The adoption of LeSS has helped BMW to improve its ability to innovate and respond to changing market demands.
*   **Ericsson:** The telecommunications company has used LeSS to develop its Media Gateway for Mobile Networks (M-MGw) product. The adoption of LeSS has enabled Ericsson to deliver a market-leading product in a highly competitive industry.
*   **Huawei:** The Chinese technology company has used LeSS to transform its product development process. The adoption of LeSS has helped Huawei to improve its ability to deliver complex products at scale.
*   **UBS:** The Swiss multinational investment bank has used LeSS to improve its software development process. The adoption of LeSS has helped UBS to increase its agility and responsiveness to customer needs.

**Documented Outcomes:**

*   **Improved delivery speed and predictability:** Many organizations that have adopted LeSS have reported a significant improvement in their ability to deliver software faster and more predictably.
*   **Increased quality:** The emphasis on technical excellence and a common Definition of Done in LeSS often leads to a significant improvement in product quality.
*   **Greater customer satisfaction:** The customer-centric focus of LeSS helps to ensure that the product being developed is aligned with customer needs, which often leads to higher levels of customer satisfaction.
*   **Improved employee morale and engagement:** The emphasis on empowerment, ownership, and purpose in LeSS can lead to a more engaged and motivated workforce.

**Research Support:**

While there is a need for more rigorous academic research on LeSS, there are a number of case studies and experience reports that provide evidence of its effectiveness. The official LeSS website (less.works) is a valuable resource for finding these case studies. Additionally, the books by Craig Larman and Bas Vodde provide a wealth of information and real-world examples of LeSS in action.


### 7. Cognitive Era Considerations

The transition into the Cognitive Era, characterized by the increasing prevalence of artificial intelligence and automation, presents both opportunities and challenges for frameworks like Large-Scale Scrum. The principles and practices of LeSS are well-suited to adapt to this new reality, but they will also need to evolve to fully leverage the potential of cognitive technologies.

**Cognitive Augmentation Potential:**

AI and automation can significantly enhance the effectiveness of LeSS in several ways. For instance, AI-powered tools can assist the Product Owner in refining the Product Backlog by analyzing vast amounts of data to identify customer trends, predict market shifts, and even suggest potential features. The principle of technical excellence can be bolstered by AI-driven test automation, continuous integration, and deployment pipelines, which can help to ensure the delivery of high-quality software at scale. Furthermore, AI can analyze communication patterns within and between teams, providing valuable insights into collaboration, identifying potential bottlenecks, and suggesting improvements to the overall system.

**Human-Machine Balance:**

Despite the potential of AI, the human element will remain central to the success of LeSS. The role of the Product Owner, which requires strategic thinking, empathy, and a deep understanding of human needs, is unlikely to be fully automated. Similarly, the Scrum Master role, with its focus on coaching, mentoring, and facilitating human interaction, will remain a uniquely human endeavor. While AI can provide data and insights, it is the teams themselves who must use this information to collaborate, solve problems, and make decisions. The future of LeSS in the Cognitive Era will be about finding the right balance between leveraging the power of AI and nurturing the creativity, ingenuity, and collaborative spirit of the people doing the work.

**Evolution Outlook:**

As cognitive technologies mature, the LeSS framework will likely evolve to incorporate them more deeply into its practices. The emphasis on systems thinking will become even more critical as organizations become more complex and interconnected, and AI will provide new tools for understanding and optimizing these systems. The principle of continuous improvement will be amplified by the ability of AI to provide real-time feedback and insights, enabling organizations to learn and adapt more quickly than ever before. The future of LeSS will be one of human-machine collaboration, where the framework provides the structure and the principles, and AI provides the tools and the intelligence to help organizations thrive in the Cognitive Era.


### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
LeSS defines Rights and Responsibilities primarily between the development teams and the customer, who is represented by the Product Owner. The framework grants teams the Right to self-organize and the Responsibility to deliver a product increment, while the Product Owner has the Right to direct the product's vision and the Responsibility to maximize its value. However, it does not explicitly define an architecture for engaging with broader stakeholders such as the environment, local communities, or future generations, focusing instead on the direct participants in product development.

**2. Value Creation Capability:**
LeSS is highly effective at creating economic and knowledge value. It enables the collective capability of multiple teams to deliver complex products efficiently, while its principles of continuous improvement and transparency foster a culture of learning and knowledge sharing. The framework's intense focus on a single "whole product" for a customer, however, leaves the creation of social, ecological, or resilience value as an implicit, rather than an explicit, goal.

**3. Resilience & Adaptability:**
Resilience and adaptability are core strengths of the LeSS framework. By building upon Scrum's empirical process control (transparency, inspection, adaptation) and promoting systems thinking, it helps organizations thrive on change and manage complexity. The "More with Less" principle aims to descale organizational bureaucracy, creating a more robust and less fragile system that can maintain coherence under the stress of large-scale development.

**4. Ownership Architecture:**
LeSS defines ownership primarily as stewardship and responsibility rather than monetary equity. The Product Owner "owns" the product vision and backlog, signifying their ultimate responsibility for the product's success on behalf of the customer. The teams, in turn, have ownership over their internal processes and the quality of their work. This architecture fosters a sense of shared responsibility for the product as a whole.

**5. Design for Autonomy:**
The framework is explicitly designed to increase autonomy, organizing work around self-managing, cross-functional feature teams to minimize coordination overhead. This decentralized structure and its reliance on clear, simple rules make it highly compatible with distributed systems and potentially adaptable for collaboration with AI agents or DAOs. The emphasis on direct communication over complex processes further supports a low-overhead, autonomous operational model.

**6. Composability & Interoperability:**
LeSS is designed to be a specific application of Scrum and is highly composable with other Agile and Lean patterns, such as Continuous Integration, Test-Driven Development, and Communities of Practice. It provides a clear, bounded system for product development that can interoperate with other organizational functions like marketing, sales, and support through the central role of the Product Owner. Its minimalist nature allows it to be combined with other patterns to build larger, more comprehensive value-creation systems.

**7. Fractal Value Creation:**
The value-creation logic of LeSS exhibits fractal properties. The core Scrum pattern of a team working from a backlog in Sprints is the foundational unit. LeSS scales this by treating multiple teams as a single, larger team, and LeSS Huge extends this again with the introduction of Requirement Areas. This demonstrates that the underlying principles of empirical process control and whole-product focus can be applied at multiple scales.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
LeSS is a powerful framework for enabling collective value creation in the context of large-scale product development. Its emphasis on systems thinking, adaptability, and decentralized autonomy strongly aligns with the core tenets of a resilient system. While it excels at creating economic and knowledge value, it scores a 4 instead of a 5 because its stakeholder architecture is narrowly focused on the customer and development organization, lacking explicit mechanisms to account for broader social or ecological value creation.

**Opportunities for Improvement:**
- Broaden the Stakeholder Architecture by introducing practices to identify and engage with non-obvious stakeholders, such as the environment or community, and incorporate their needs into the product vision.
- Explicitly expand the definition of "value" beyond the product-market fit to include metrics for social, ecological, and resilience value, encouraging the Product Owner to consider these dimensions during prioritization.
- Integrate a "Commons Stewardship" role or responsibility, perhaps as an extension of the Scrum Master or management function, to focus on the long-term health and viability of the entire value-creation ecosystem, not just the product itself.


### 9. Resources & References

**Essential Reading:**

*   **Larman, C., & Vodde, B. (2016). *Large-Scale Scrum: More with LeSS*. Addison-Wesley Professional.** This is the definitive guide to LeSS, written by the creators of the framework. It provides a comprehensive overview of the principles, practices, and rules of LeSS.
*   **Larman, C., & Vodde, B. (2010). *Scaling Lean & Agile Development: Thinking and Organizational Tools for Large-Scale Scrum*. Addison-Wesley Professional.** This book provides the foundational thinking behind LeSS, including a deep dive into systems thinking, lean development, and queueing theory.
*   **Larman, C., & Vodde, B. (2010). *Practices for Scaling Lean & Agile Development*. Addison-Wesley Professional.** This book is the predecessor to *Large-Scale Scrum* and provides a wealth of practical advice and experiments for scaling agile development.

**Organizations & Communities:**

*   **The LeSS Company:** The official organization behind LeSS. Their website (less.works) is the primary source of information on the framework, including case studies, articles, and a directory of certified trainers and coaches.
*   **Scrum.org and Scrum Alliance:** While not specifically focused on LeSS, these organizations provide a wealth of information and resources on Scrum in general, which is the foundation of LeSS.

**Tools & Platforms:**

LeSS is a framework, not a tool. However, there are a number of tools that can be used to support a LeSS implementation, such as Jira, Trello, and other agile project management tools. The key is to use tools that are flexible and can be adapted to the specific needs of the organization.

**References:**

[1] LeSS.works. (n.d.). *Large Scale Scrum (LeSS)*. Retrieved from https://less.works/

[2] Atlassian. (n.d.). *The Large-Scale Scrum (LeSS) framework*. Retrieved from https://www.atlassian.com/agile/agile-at-scale/less

[3] LeSS.works. (n.d.). *John Deere Case Study*. Retrieved from https://less.works/case-studies/john-deere

[4] Larman, C., & Vodde, B. (2016). *Large-Scale Scrum: More with LeSS*. Addison-Wesley Professional.

[5] Larman, C., & Vodde, B. (2010). *Practices for Scaling Lean & Agile Development*. Addison-Wesley Professional.

[6] Adoption of Large-Scale Scrum Practices through the Use of Management 3.0. (2022). *Journal of Software Engineering and Applications*, *9*(1), 20. https://doi.org/10.3390/jsea9010020

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/large-scale-scrum-less/](https://commons-os.github.io/patterns/domain/large-scale-scrum-less/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/large-scale-scrum-less.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/large-scale-scrum-less.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
