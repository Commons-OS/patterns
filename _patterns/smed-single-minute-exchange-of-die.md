---
id: pat_01kg5023zzecsb265cx26t3kz3
page_url: https://commons-os.github.io/patterns/smed-single-minute-exchange-of-die/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/smed-single-minute-exchange-of-die.md
slug: smed-single-minute-exchange-of-die
title: SMED (Single-Minute Exchange of Die)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: [methodology, practice]
  era: [industrial, digital]
  origin: [Toyota]
  status: draft
  commons_alignment: 3
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

# SMED (Single-Minute Exchange of Die)

## 1. Overview

Single-Minute Exchange of Die (SMED) is a lean manufacturing methodology focused on dramatically reducing the time it takes to complete equipment changeovers. The term "single-minute" signifies the goal of reducing changeover times to the single digits (i.e., less than 10 minutes). The core idea is to convert as many changeover steps as possible to "external" activities, which can be performed while the equipment is still running, and to simplify and streamline the remaining "internal" steps, which must be done when the machine is stopped. This approach minimizes downtime, allows for smaller production lot sizes, and increases production flexibility. The concept was developed by Shigeo Shingo, a key contributor to the Toyota Production System (TPS), and has since become a widely adopted practice in various industries beyond manufacturing.

## 2. Core Principles

The SMED methodology is built upon a set of core principles that guide the reduction of changeover times. These principles provide a systematic framework for analyzing and improving setup processes, aiming to minimize downtime and maximize productivity.

### Differentiating Internal and External Setup

The most fundamental principle of SMED is the distinction between internal and external setup activities. **Internal setup** refers to tasks that can only be performed when the machine is stopped, such as removing an old die and mounting a new one. **External setup**, on the other hand, consists of tasks that can be completed while the machine is still in operation, such as fetching tools, preheating molds, or preparing the next set of materials. By identifying and separating these two types of activities, organizations can shift a significant portion of the setup work to be performed while the machine is still productive, thereby dramatically reducing the downtime required for the changeover.

### Converting Internal to External Setup

Once internal and external setup activities have been clearly distinguished, the next principle is to convert as many internal tasks as possible into external ones. This is the heart of the SMED process and offers the most significant opportunities for reducing changeover times. This conversion is achieved by meticulously planning and preparing for the changeover in advance. For example, instead of searching for tools and equipment during the changeover, they can be gathered and organized beforehand. Similarly, preheating dies or other components before the machine is stopped can eliminate a time-consuming internal activity. The goal is to perform all possible preparatory and concluding tasks while the machine is still running, leaving only the absolute essential tasks for the internal setup phase.

### Streamlining and Simplifying All Setup Activities

After converting internal activities to external ones, the next principle is to streamline and simplify all remaining setup tasks, both internal and external. This involves a detailed analysis of each step in the changeover process to identify and eliminate waste. Shigeo Shingo famously observed that "it's only the last turn of a bolt that tightens it—the rest is just movement." This highlights the importance of focusing on the value-adding aspects of each task and minimizing non-value-adding motions. Techniques for streamlining setup activities include using functional clamps and eliminating fasteners, implementing intermediate jigs to speed up positioning, and adopting parallel operations where multiple tasks can be performed simultaneously by different operators. The aim is to make every action more efficient and to reduce the time required for each step of the changeover process.

### Standardizing and Continuously Improving

The final core principle of SMED is to standardize the new, improved changeover procedure and to foster a culture of continuous improvement. Documenting the optimized process and creating standardized work instructions ensures that the improvements are sustained and that all operators perform the changeover in the most efficient way. This standardization also provides a baseline for future improvement efforts. SMED is not a one-time project but an ongoing process of refinement. By repeatedly applying the principles of observing, analyzing, and improving the changeover process, organizations can achieve progressively shorter setup times, driving further gains in productivity and flexibility.

## 3. Key Practices

To successfully implement SMED, several key practices are employed to systematically reduce changeover times. These practices provide a practical roadmap for analyzing, re-engineering, and optimizing setup processes.

### Separating Internal and External Setup

The first and most critical practice is to meticulously separate internal and external setup activities. This involves a detailed observation of the entire changeover process to identify which tasks absolutely require the machine to be stopped (internal) and which can be performed while the machine is still running (external). A common approach is to videotape the changeover and then analyze the footage with a cross-functional team of operators, engineers, and maintenance personnel. This collaborative analysis helps to create a comprehensive list of all setup elements, along with their durations. Once the list is compiled, each element is categorized as either internal or external. This simple act of separation often reveals that a significant portion of the changeover time is spent on tasks that could have been done while the machine was still in production.

### Converting Internal to External Setup

After separating internal and external activities, the next practice is to focus on converting as many internal tasks as possible into external ones. This is where the most substantial time savings are typically realized. The team brainstorms ways to modify the process, equipment, or procedures to allow tasks that were previously performed during downtime to be completed beforehand or afterward. Examples of this practice include:

This practice includes pre-checking and preparing tools and equipment in advance, preheating molds and dies to the required temperature before the changeover begins, and standardizing die heights and clamping points to minimize adjustments.

### Streamlining and Simplifying All Setup Activities

Once as many tasks as possible have been moved to the external setup phase, the focus shifts to streamlining and simplifying the remaining activities, both internal and external. The goal is to reduce the time and effort required for each step. This practice involves a range of techniques, including:

This practice involves a range of techniques, including using functional clamps and eliminating fasteners, implementing intermediate jigs, adopting parallel operations, eliminating adjustments, and mechanization where appropriate.

By systematically applying these key practices, organizations can achieve dramatic reductions in changeover times, leading to increased productivity, improved flexibility, and a more competitive manufacturing operation.

## 4. Application Context

While SMED originated in the manufacturing sector, specifically within the Toyota Production System, its principles and practices have proven to be highly adaptable and beneficial across a wide range of industries and operational contexts. The applicability of SMED extends far beyond the factory floor, offering significant value in any environment where there is a need to switch between different tasks, processes, or products efficiently.

### Manufacturing Industries

In its traditional application, SMED is a cornerstone of lean manufacturing. It is most impactful in environments with high product variety and a need for frequent changeovers. Industries such as automotive, consumer electronics, and fast-moving consumer goods (FMCG) have reaped enormous benefits from SMED by reducing downtime and enabling smaller batch sizes. This, in turn, allows for a more flexible and responsive production system, capable of meeting fluctuating customer demands without carrying large inventories. The principles of SMED are equally applicable in both discrete and process manufacturing, from stamping and molding operations to food processing and pharmaceuticals.

### Beyond Manufacturing

The power of SMED lies in its systematic approach to analyzing and improving any setup or changeover process. This has led to its successful application in a variety of non-manufacturing contexts:

In healthcare, SMED has been used to reduce operating room turnaround times. In software development, it has been applied to speed up software deployments. In service industries like airlines, it has been used to minimize aircraft turnaround time at the gate.

### When to Apply SMED

SMED is most beneficial in situations where:

SMED is most beneficial when changeover times are a significant source of downtime, when there is a desire to reduce lot sizes and inventory, when greater production flexibility is needed, or when there is a bottleneck in the production process.

In essence, SMED is a versatile and powerful methodology that can be applied in any situation where there is a need to improve the efficiency and effectiveness of a changeover or setup process. Its principles provide a universal framework for analyzing, simplifying, and streamlining any transition between tasks, making it a valuable tool for a wide range of organizations seeking to improve their operational performance.



## 6. Evidence & Impact

The implementation of SMED has a well-documented track record of delivering significant and measurable improvements in manufacturing performance. Numerous case studies and research papers have demonstrated the profound impact of this methodology on productivity, flexibility, cost, and quality. The evidence overwhelmingly supports the claim that SMED is a highly effective tool for achieving operational excellence.

### Quantifiable Improvements

The most direct and immediate impact of SMED is a dramatic reduction in changeover times. It is not uncommon for organizations to achieve reductions of 75% or more, with many case studies reporting reductions of over 90%. For example, a study in the automotive industry demonstrated a reduction in die changeover time from several hours to less than 15 minutes. These time savings translate directly into increased production capacity. With less downtime for changeovers, machines are available for production for a greater percentage of the time, leading to a significant increase in Overall Equipment Effectiveness (OEE).

### Enhanced Flexibility and Responsiveness

By making changeovers faster and more efficient, SMED enables the production of smaller lot sizes. This has a cascading effect on the entire production system, leading to a number of important benefits:

*   **Reduced Inventory:** Smaller lot sizes mean less work-in-process (WIP) and finished goods inventory. This reduces carrying costs, frees up valuable floor space, and minimizes the risk of obsolescence.
*   **Improved Responsiveness:** With the ability to switch quickly between different products, companies can be more responsive to changes in customer demand. This allows them to offer a wider variety of products and to fulfill orders more quickly, providing a significant competitive advantage.
*   **Smoother Production Flow:** Smaller lot sizes and more frequent changeovers lead to a more continuous and balanced production flow, reducing the bullwhip effect and creating a more stable and predictable manufacturing environment.

### Cost Reduction and Quality Improvement

The impact of SMED extends beyond time savings and flexibility. It also has a direct impact on cost and quality:

*   **Lower Manufacturing Costs:** Reduced downtime, lower inventory levels, and increased productivity all contribute to lower overall manufacturing costs.
*   **Improved Quality:** The standardized work procedures and elimination of adjustments that are central to SMED lead to a more consistent and repeatable setup process. This reduces the likelihood of errors and defects, resulting in a higher level of quality and less scrap and rework.
*   **Increased Safety:** By simplifying and streamlining the changeover process, SMED can also lead to a safer working environment. A well-organized and standardized process reduces the risk of accidents and injuries.

In conclusion, the evidence supporting the effectiveness of SMED is compelling. From dramatic reductions in changeover times to significant improvements in flexibility, cost, and quality, the impact of this methodology is both profound and far-reaching. For any organization looking to improve its manufacturing performance, SMED offers a proven and powerful solution.

## 7. Cognitive Era Considerations

In the Cognitive Era, characterized by the convergence of artificial intelligence, big data, and the Internet of Things (IoT), the principles of SMED are not only still relevant but are also being amplified and extended in new and powerful ways. The fundamental goal of reducing changeover time remains critical, but the tools and techniques available to achieve this goal have become significantly more sophisticated. Moreover, the very concept of a "changeover" is expanding beyond the physical realm of manufacturing to encompass digital processes and knowledge work.

### AI-Powered SMED

Artificial intelligence and machine learning are being used to enhance every stage of the SMED process:

*   **Automated Process Analysis:** AI-powered computer vision systems can automatically analyze video footage of changeovers, identifying and categorizing internal and external tasks with a level of detail and accuracy that would be difficult to achieve manually. This accelerates the initial analysis phase of SMED and provides a more granular understanding of the process.
*   **Predictive Maintenance:** IoT sensors on equipment can collect real-time data on machine health and performance. AI algorithms can analyze this data to predict when maintenance is required, allowing it to be scheduled as an external activity, rather than causing an unexpected breakdown and a lengthy, unplanned changeover.
*   **Optimized Scheduling:** AI can be used to optimize production schedules, taking into account not only customer demand but also the time and resources required for changeovers. This allows for a more dynamic and efficient allocation of resources, minimizing downtime and maximizing throughput.
*   **Augmented Reality Guidance:** Augmented reality (AR) can provide operators with real-time, interactive guidance during changeovers. Step-by-step instructions, diagrams, and videos can be overlaid on the operator's field of view, reducing the risk of errors and speeding up the process.

### SMED in the Digital Realm

The concept of a "changeover" is no longer limited to physical machines. In the Cognitive Era, we are increasingly dealing with digital "changeovers," such as:

*   **Software Deployments:** As mentioned earlier, the principles of SMED are being applied in DevOps to reduce the time it takes to deploy new software releases. This enables a continuous delivery pipeline, allowing for faster innovation and a more responsive development process.
*   **Data Model Changes:** In the world of big data, changing the structure of a data model or migrating data from one system to another can be a complex and time-consuming process. SMED principles can be used to streamline these "data changeovers," minimizing downtime and ensuring data integrity.
*   **AI Model Retraining:** As AI models are deployed in production, they need to be periodically retrained with new data to maintain their accuracy. The process of taking a model offline, retraining it, and deploying the new version is a type of changeover. SMED can be used to minimize the downtime of the AI application during this process.

In the Cognitive Era, the ability to change and adapt quickly is more important than ever. SMED, with its focus on reducing changeover times and increasing flexibility, is a critical enabler of this agility. By embracing the new tools and technologies of the Cognitive Era, organizations can take the principles of SMED to a whole new level, achieving unprecedented levels of efficiency, responsiveness, and competitiveness.

## 8. Commons Alignment Assessment

The Commons Alignment Assessment evaluates how well the SMED pattern aligns with the principles of a commons-based approach. This assessment considers seven key dimensions, providing a holistic view of the pattern's potential to contribute to a more collaborative, equitable, and sustainable world.

| Dimension | Assessment |
| :--- | :--- |
| **1. Openness & Transparency** | SMED promotes transparency by making the changeover process visible and understandable to all involved. The practice of videotaping and analyzing the process encourages open communication and a shared understanding of the challenges and opportunities for improvement. The knowledge gained through SMED implementation is typically shared openly within the organization to foster a culture of continuous learning. |
| **2. Decentralization & Federation** | While SMED is often implemented within a hierarchical organization, it empowers frontline workers by giving them the knowledge and tools to improve their own work processes. The team-based approach to SMED encourages decentralized decision-making, as the people closest to the work are best equipped to identify and implement improvements. |
| **3. Community & Collaboration** | Collaboration is at the heart of SMED. The methodology relies on cross-functional teams of operators, engineers, and managers working together to analyze and improve the changeover process. This collaborative approach breaks down silos between departments and fosters a sense of shared ownership and collective responsibility. |
| **4. Resource Efficiency & Sustainability** | SMED is highly aligned with the principles of resource efficiency and sustainability. By reducing downtime, SMED increases the productive capacity of existing equipment, reducing the need for additional capital investment. The ability to produce in smaller batches also reduces waste from overproduction and obsolescence. Furthermore, a more efficient manufacturing process consumes less energy and resources. |
| **5. Fairness & Equity** | SMED can contribute to a more fair and equitable workplace by empowering workers and valuing their knowledge and expertise. By involving operators in the improvement process, SMED recognizes their contribution and gives them a greater sense of agency. The simplification of tasks can also make the work less physically demanding and more accessible to a wider range of people. |
| **6. Individual & Collective Well-being** | By creating a more efficient, less stressful, and safer work environment, SMED can contribute to the well-being of individuals. The collaborative nature of the process can also enhance a sense of community and shared purpose. At a collective level, the increased productivity and competitiveness that result from SMED can contribute to economic stability and prosperity. |
| **7. Resilience & Adaptability** | SMED is a key enabler of organizational resilience and adaptability. In a rapidly changing world, the ability to switch quickly and efficiently between different products or tasks is a critical competitive advantage. SMED provides the flexibility needed to respond to fluctuating customer demands, supply chain disruptions, and other unforeseen events. |

## 9. Resources & References

### Key Literature

*   Shingo, S. (1985). *A Revolution in Manufacturing: The SMED System*. Productivity Press.
*   Shingo, S. (1989). *A Study of the Toyota Production System*. Productivity Press.

### Online Resources

*   [Lean Production - SMED](https://www.leanproduction.com/smed/)
*   [Wikipedia - Single-Minute Exchange of Die](https://en.wikipedia.org/wiki/Single-minute_exchange_of_die)
*   [Kaizen.com - Reduce changeover time and boost efficiency](https://kaizen.com/insights/smed-reduce-changeover-boost-efficiency/)

### References

[1] Shingo, S. (1985). *A Revolution in Manufacturing: The SMED System*. Productivity Press.

[2] Taylor, F. W. (1911). *Shop Management*. Harper & Brothers.

[3] Arnold, H. L., & Faurote, F. L. (1915). *Ford Methods and the Ford Shops*. The Engineering Magazine Company.

[4] "The History of Quick Change Over (SMED) | AllAboutLean.com". (2014, March 2). Retrieved from https://www.allaboutlean.com/smed-history/

[5] Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production*. Productivity Press.

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/smed-single-minute-exchange-of-die/](https://commons-os.github.io/patterns/domain/smed-single-minute-exchange-of-die/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/smed-single-minute-exchange-of-die.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/smed-single-minute-exchange-of-die.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
