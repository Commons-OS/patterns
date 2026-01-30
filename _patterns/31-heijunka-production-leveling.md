---
id: pat_01kg5023w2eshb12c2rftpwzcd
page_url: https://commons-os.github.io/patterns/31-heijunka-production-leveling/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/31-heijunka-production-leveling.md
slug: 31-heijunka-production-leveling
title: Heijunka - Production Leveling
aliases: [Production Leveling, Production Smoothing]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: [practice]
  era: [industrial, digital]
  origin: [toyota, lean-manufacturing]
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: [https://www.isixsigma.com/lean-methodology/heijunka-the-art-of-leveling-production/, https://www.lean.org/lexicon-terms/heijunka/, https://www.azumuta.com/blog/heijunka-definition-techniques-and-example/, https://mag.toyota.co.uk/heijunka-toyota-production-system/, https://www.creativesafetysupply.com/articles/heijunka-production-leveling/]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Heijunka (平準化), a Japanese term for "leveling" or "smoothing," is a foundational principle of the Toyota Production System (TPS) designed to create stability in a production process by leveling the mix and volume of items produced over a specific period. The core problem Heijunka addresses is the unevenness (mura) and overburden (muri) that arise from fluctuating customer demand, which in turn create waste (muda). Instead of producing in large batches based on the volatile flow of customer orders, Heijunka enables a manufacturer to produce in smaller, more consistent increments, creating a predictable and rhythmic flow. This approach allows for better synchronization with customer demand, reduces the need for large inventories, shortens production lead times, and frees up capital. The origin of Heijunka is deeply rooted in post-war Japan, where Toyota, facing limited resources and capital, could not afford the large-batch, high-inventory model of Western mass production. Spearheaded by industrial engineer Taiichi Ohno, Toyota developed the TPS, with Heijunka as a cornerstone, to eliminate waste and improve efficiency. By producing a variety of models in small quantities on the same line, Toyota could respond to diverse customer needs without the crippling cost of large inventories, a revolutionary concept that has since become a benchmark for lean manufacturing worldwide.

### 2. Core Principles

1.  **Production Leveling by Volume**: This principle dictates that total production volume should be averaged out over a fixed period. Instead of chasing daily or weekly demand spikes, a company calculates the average demand and produces a consistent, level amount each day. For example, if weekly demand is 500 units, with orders of 200 on Monday and 50 on Friday, a traditional system would struggle with the initial surge and then have excess capacity. Under Heijunka, the company would produce a level 100 units per day, using a small buffer of finished goods to meet the initial Monday demand. This creates a predictable, manageable workload for employees and machines.

2.  **Production Leveling by Type (Mixed-Model Production)**: This principle addresses the variety of products demanded by customers. Rather than producing long runs of a single product before a lengthy changeover (e.g., AAAAABBBCC), Heijunka advocates for producing a mix of products in a recurring sequence (e.g., AABCABAABC). This frequent switching between models, made possible by rapid changeover techniques like Single-Minute Exchange of Die (SMED), allows the system to be highly responsive to the actual mix of customer orders. It reduces the risk of overproducing one item while being short on another, thus minimizing finished goods inventory and shortening lead times for all products.

3.  **Takt Time Pacing**: Takt time is the rhythm of production, synchronized with the rate of customer demand. It is calculated by dividing the available production time by the total customer demand for that period. Heijunka uses takt time as the heartbeat of the production line. Every process is designed to be completed within this time, ensuring that production is perfectly paced to meet demand without overproducing or falling behind. This creates a continuous and smooth flow of work throughout the value stream.

4.  **Pull System and Kanban**: Heijunka operates on a pull system, where downstream processes signal their needs to upstream processes. This is often visualized and managed using Kanban cards. A Kanban signal is triggered only when a customer order is received or a specific quantity of a product is consumed from a small, controlled inventory. This prevents the upstream overproduction that is common in traditional "push" systems, where production is based on forecasts rather than actual demand.

### 3. Key Practices

1.  **Heijunka Box (Leveling Box)**: This is a visual scheduling tool used to manage the leveled production of different product types. The box is a grid with horizontal rows for each product and vertical columns representing time intervals (e.g., hours or shifts). Kanban cards, representing individual units of production, are placed in the slots to create a visual schedule for the day. A worker takes a card from the current time slot, which tells them what to produce next. This simple, visual system makes the leveled schedule easy to understand and follow for everyone on the shop floor.

2.  **Single-Minute Exchange of Die (SMED)**: A critical enabler for leveling by type, SMED is a collection of techniques for dramatically reducing the time it takes to change a production line from one product to another. By minimizing changeover times, often to less than 10 minutes, the economic disincentive for frequent product switching is removed. This makes the small-batch, mixed-model production of Heijunka not only possible but also economically advantageous.

3.  **Standardized Work**: For production to flow smoothly at the prescribed takt time, every task must be clearly defined, documented, and performed consistently. Standardized work involves creating detailed instructions that specify the sequence of operations, the time allotted for each, and the expected quality outcome. This eliminates variation in how tasks are performed, which is essential for maintaining the rhythm and predictability required by Heijunka.

4.  **Buffer Management (Finished Goods and WIP)**: While Heijunka aims to minimize inventory, it strategically uses small, controlled buffers of inventory to absorb minor variations in demand and production. A small buffer of finished goods near shipping can help meet sudden demand spikes, while carefully placed buffers of Work-in-Progress (WIP) can decouple processes and prevent minor disruptions from halting the entire line. The key is that these buffers are intentionally sized and managed, not the result of uncontrolled overproduction.

5.  **ABC Production Analysis**: This is a method for categorizing products to help in designing the production schedule. Products are classified into A, B, and C categories based on their demand volume and value. 'A' items are high-volume, 'B' are medium-volume, and 'C' are low-volume. This analysis helps in determining the frequency of production for each item within the leveled schedule, ensuring that high-demand items are produced more frequently.

### 4. Application Context

-   **Best Used For**:
    -   Environments with multiple product variations and fluctuating customer demand.
    -   Manufacturing settings aiming to transition from a batch-and-queue system to a lean, continuous flow.
    -   Organizations seeking to reduce lead times, minimize inventory holding costs, and improve responsiveness.
    -   Processes where the cost of frequent changeovers can be significantly reduced through SMED.
    -   Service operations, such as call centers or software development, to level the inflow and processing of work requests.

-   **Not Suitable For**:
    -   True one-off, project-based production where each output is unique and demand is highly unpredictable.
    -   Processes with extremely long, unavoidable changeover times where the cost of frequent switching remains prohibitive.
    -   Environments where demand is naturally stable and consistent, as the primary benefit of leveling is reduced.

-   **Scale**: Heijunka is most commonly applied at the **Team**, **Department**, and **Organization** levels. While its principles can inform individual work, its true power is in coordinating multiple process steps across a value stream. It can also be extended to the **Multi-Organization/Ecosystem** level by synchronizing production schedules with suppliers and distributors.

-   **Domains**: While originating in the **automotive industry**, Heijunka is now widely applied across various manufacturing sectors, including **electronics, consumer goods, and industrial equipment**. Its principles have also been adapted for service industries such as **healthcare** (leveling patient appointments), **software development** (leveling the flow of features in an agile sprint), and **logistics** (smoothing the flow of goods through a distribution center).

### 5. Implementation

-   **Prerequisites**:
    -   **Management Commitment**: A deep understanding and commitment from leadership are essential, as implementing Heijunka is a significant cultural shift.
    -   **Process Stability**: Basic process stability and quality control (e.g., through 5S and standardized work) must be in place. Trying to level an unstable process will only amplify chaos.
    -   **Accurate Demand Data**: Reliable data on customer demand patterns is needed to calculate takt time and create the leveled schedule.
    -   **SMED Capability**: The ability to perform quick changeovers is a non-negotiable prerequisite for leveling by type.

-   **Getting Started**:
    1.  **Calculate Takt Time**: Determine the rate of customer demand and the available production time to establish the production rhythm.
    2.  **Develop a Leveled Schedule**: Analyze demand patterns for all products and create a mixed-model production sequence that levels the volume and mix over a defined period (e.g., a day or a week).
    3.  **Design the Heijunka Box**: Create a visual scheduling board (the Heijunka box) to display the leveled schedule and manage the flow of Kanban cards.
    4.  **Implement a Pull System**: Introduce Kanban signals to trigger production based on actual consumption, starting with a pilot area and then expanding.
    5.  **Continuously Improve (Kaizen)**: Regularly review the performance of the system, identify bottlenecks and sources of variation, and use Kaizen events to make incremental improvements.

-   **Common Challenges**:
    -   **Resistance to Change**: Employees and managers accustomed to batch production may resist the move to smaller batches and frequent changeovers.
    -   **Supplier Synchronization**: Suppliers may not be able to deliver in the small, frequent batches required by a leveled system.
    -   **Demand Volatility**: Highly erratic and unpredictable demand can be difficult to level effectively.
    -   **Ignoring Prerequisites**: Attempting to implement Heijunka without first establishing process stability and quick changeovers is a common cause of failure.

-   **Success Factors**:
    -   **Strong Leadership and Training**: Leaders must champion the change and provide thorough training to all employees.
    -   **Cross-Functional Collaboration**: Close collaboration between production, planning, and sales is needed to manage demand and capacity.
    -   **Patience and Persistence**: Heijunka is not a quick fix; it requires a long-term commitment to continuous improvement.
    -   **Visual Management**: Making the process visible through tools like the Heijunka box is crucial for engagement and adherence.

### 6. Evidence & Impact

-   **Notable Adopters**:
    -   **Toyota**: The originator and most famous example, using Heijunka as the foundation of its globally renowned production system.
    -   **Ford**: Has adopted lean principles, including production leveling, in many of its plants to compete with Toyota.
    -   **John Deere**: Uses production leveling to manage the complex manufacturing of its agricultural equipment.
    -   **FPZ**: An Italian manufacturer of blowers and fans that successfully implemented Heijunka, resulting in significant cost savings and efficiency gains.
    -   **Virginia Mason Medical Center**: A pioneer in applying lean principles to healthcare, using leveling techniques to smooth patient flow and reduce waiting times.

-   **Documented Outcomes**:
    -   **Reduced Lead Times**: By producing in smaller batches, the time from customer order to delivery is dramatically shortened.
    -   **Lower Inventory Costs**: Heijunka minimizes the need for large stocks of raw materials, WIP, and finished goods, freeing up capital.
    -   **Improved Productivity and Quality**: A stable, predictable production rhythm reduces overburden and stress on workers and equipment, leading to fewer errors and higher overall efficiency.
    -   **Increased Flexibility**: The ability to produce a mix of products allows companies to respond quickly to changes in customer preferences.
    -   **FPZ Case Study**: The Italian company FPZ reported savings of an estimated EUR 60,000 within the first three years of implementing lean, including Heijunka, by eliminating waste and streamlining operations [3].

-   **Research Support**:
    -   Numerous studies have validated the benefits of Heijunka. A 2013 simulation analysis published in the *IFAC Proceedings Volumes* demonstrated that a well-designed Heijunka system improves both throughput time and work-in-progress levels [1].
    -   Action research published in the *Journal of Industrial Engineering and Management* (2024) identified critical success factors for Heijunka implementation and confirmed its positive impact on operational performance [2].

### 7. Cognitive Era Considerations

-   **Cognitive Augmentation Potential**: In the cognitive era, AI and automation can significantly enhance Heijunka. Machine learning algorithms can analyze vast datasets of historical sales, market trends, and even social media sentiment to create far more accurate and dynamic demand forecasts. This allows for more precise calculation of takt time and more responsive leveling. AI-powered simulation tools can model and optimize different mixed-model production sequences in real-time, suggesting the most efficient schedule based on current conditions. IoT sensors on the production line can provide real-time data on machine status and performance, allowing AI systems to proactively adjust the schedule to account for potential disruptions.

-   **Human-Machine Balance**: While AI can optimize the schedule, the uniquely human aspects of Heijunka remain critical. The practice of Kaizen, or continuous improvement, relies on the creativity and problem-solving skills of front-line workers who observe the process and identify opportunities for improvement. The collaborative, team-based approach to problem-solving and the visual management aspects of the Heijunka box are designed for human interaction and engagement. The role of the human shifts from manual scheduling and data crunching to process oversight, exception handling, and driving a culture of improvement. Machines can generate the optimal plan, but humans are needed to implement it, adapt it, and improve it.

-   **Evolution Outlook**: The future of Heijunka lies in its integration with digital twin and cyber-physical systems. A digital twin of the entire production line could run simulations of the Heijunka schedule, identifying potential bottlenecks or resource conflicts before they occur in the physical world. This would allow for a level of proactive leveling and optimization that is impossible today. As supply chains become more interconnected and transparent through blockchain and other technologies, Heijunka could evolve from a single-factory system to a network-level production leveling system, synchronizing the flow of value across entire ecosystems in real-time.

### 8. Commons Alignment Assessment

1.  **Stakeholder Mapping**: Heijunka primarily focuses on the stakeholders within the immediate value stream: customers, employees, and suppliers. Its goal is to meet customer demand efficiently while creating a stable and less stressful work environment for employees. It also benefits suppliers by providing them with a more predictable and level demand pattern. However, it does not explicitly consider broader stakeholders such as the local community or the natural environment.

2.  **Value Creation**: The pattern excels at creating economic value for the firm (reduced costs, increased efficiency) and use value for the customer (shorter lead times, higher quality). It also creates value for employees by reducing overburden (muri) and creating a more predictable work environment. The value is primarily captured by the firm and the customer, with some benefits flowing to suppliers.

3.  **Value Preservation**: Heijunka is a highly adaptive system. By tying production directly to real-time customer demand (takt time) and enabling flexibility through mixed-model production, it ensures that the organization is always producing what is needed and can quickly pivot as customer preferences change. This inherent responsiveness is a powerful mechanism for preserving the relevance and value of the organization's output over time.

4.  **Shared Rights & Responsibilities**: Within the organization, Heijunka promotes a shared responsibility for maintaining the flow of production. It empowers front-line workers to manage their work through visual tools like the Kanban and Heijunka box. However, the ultimate control over the production schedule and the design of the system typically remains with management. The rights to the economic surplus generated are not explicitly shared beyond traditional wage and profit structures.

5.  **Systematic Design**: Heijunka is the epitome of systematic design. It is a highly structured, repeatable system for scheduling and controlling production. Practices like standardized work, takt time, and the Heijunka box are all designed to create a predictable and improvable system. The entire pattern is a process for designing and managing a production system for stability and efficiency.

6.  **Systems of Systems**: Heijunka is a core component of the larger Toyota Production System and is designed to integrate seamlessly with other lean patterns like Jidoka (autonomation), Kanban, and Kaizen. It acts as the pacemaker for the entire system, creating the stable foundation upon which other lean practices can be effectively built. Its effectiveness is magnified when it is part of this larger system of patterns.

7.  **Fractal Properties**: The core principle of leveling can be applied at multiple scales. An individual worker can level their own workload throughout the day. A team can level the flow of tasks in a project. A factory can level its production schedule. An entire supply chain can, in theory, level the flow of goods from raw materials to the final customer. The principles of balancing mix and volume to create a smooth flow are fractal in nature.

**Overall Score**: 3/5 (Transitional)

**Rationale**: Heijunka represents a significant step beyond traditional, extractive mass production. By creating a more stable and humane work environment and by focusing on waste reduction, it has positive social and environmental externalities. It fosters a sense of shared responsibility on the shop floor and creates a more collaborative relationship with suppliers. However, its primary focus remains on optimizing the efficiency and profitability of the individual firm. It does not inherently address broader commons concerns such as equitable distribution of value, community well-being, or environmental regeneration. It is a transitional pattern that moves away from purely extractive models but does not yet fully embrace a commons-centric logic. To improve its commons alignment, the pattern could be extended to explicitly include environmental metrics in its optimization, formalize value-sharing agreements with employees and suppliers, and engage the broader community in its operational planning.

### 9. Resources & References

-   **Essential Reading**:
    -   Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production*. Productivity Press. - The definitive book by the creator of the TPS, explaining the philosophy and principles behind it.
    -   Rother, M., & Shook, J. (2003). *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda*. Lean Enterprise Institute. - A practical guide to value stream mapping, a critical tool for identifying opportunities for Heijunka.
    -   Womack, J. P., & Jones, D. T. (2003). *Lean Thinking: Banish Waste and Create Wealth in Your Corporation*. Free Press. - A classic that introduced lean principles to a Western audience, with clear explanations of concepts like flow and pull.

-   **Organizations & Communities**:
    -   **Lean Enterprise Institute (LEI)**: A non-profit organization founded by James Womack, dedicated to advancing lean thinking through research, education, and events. (https://www.lean.org)
    -   **The Toyota Motor Corporation**: The source of the pattern, their official sites and publications offer deep insights into the Toyota Production System. (https://global.toyota/en/)

-   **Tools & Platforms**:
    -   **Kanban Boards (Physical or Digital)**: Tools like Trello, Jira, or even a simple whiteboard are essential for visualizing and managing the pull system that underpins Heijunka.
    -   **ERP/MES Systems**: Modern Enterprise Resource Planning and Manufacturing Execution Systems often have modules for lean scheduling and Heijunka, which can help in complex environments.

-   **References**:
    1.  Korytkowski, P., & Karkoszka, R. (2013). Multivariate simulation analysis of production leveling (Heijunka). *IFAC Proceedings Volumes, 46*(9), 850-855.
    2.  Alvarez, L., Avella, L., & Martinez, R. (2024). Impact and critical factors in Heijunka implementation an action research study. *Journal of Industrial Engineering and Management, 17*(1), 1-20.
    3.  Azumuta. (2024, January 2). *Heijunka: Definition, Techniques, and Example*. Azumuta Blog. Retrieved from https://www.azumuta.com/blog/heijunka-definition-techniques-and-example/
    4.  Friddle, J. R. (2024, October 14). Heijunka: The Art of Leveling Production. *iSixSigma*. Retrieved from https://www.isixsigma.com/lean-methodology/heijunka-the-art-of-leveling-production/
    5.  Lean Enterprise Institute. (n.d.). *Heijunka*. Lean Lexicon. Retrieved from https://www.lean.org/lexicon-terms/heijunka/

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/31-heijunka-production-leveling/](https://commons-os.github.io/patterns/domain/31-heijunka-production-leveling/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/31-heijunka-production-leveling.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/31-heijunka-production-leveling.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
