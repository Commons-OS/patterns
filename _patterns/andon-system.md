---
id: pat_01kg5023xef1s9wh9a1qrpw7qf
page_url: https://commons-os.github.io/patterns/andon-system/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/andon-system.md
slug: andon-system
title: Andon System
aliases: [Andon Cord, Jidoka]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: operations
  category: [practice]
  era: [industrial, digital]
  origin: [toyota]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: ["pat_01kg5023w2eshb12c2m56q8825"]
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: [https://en.wikipedia.org/wiki/Andon_(manufacturing), https://www.planview.com/resources/guide/what-is-lean-manufacturing/andon-lean-manufacturing/, https://www.vorne.com/learn/key-concepts/andon/, https://www.l2l.com/guide/andon, https://www.rockwellautomation.com/en-us/company/news/case-studies/andon-solution-delivers-better-decision-making-at-toyota.html, https://signalo.us/andon/, https://www.amazon.com/Toyota-Production-System-Beyond-Large-Scale/dp/0915299143, https://www.amazon.com/Toyota-Way-Management-Principles-Manufacturer/dp/0071392319, https://www.lean.org/store/book/learning-to-see/]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

The Andon System is a powerful visual management tool that originated within the Toyota Production System (TPS) [1]. It serves as a real-time communication system on the factory floor, designed to alert operators and managers to problems as they occur. The term "Andon" (行灯) is Japanese for a traditional paper lantern, and in a manufacturing context, it typically takes the form of a light-based signal [2]. When a production issue arises—such as a quality defect, a tool malfunction, or a shortage of parts—an operator can activate the Andon signal, which is often a cord or button at their workstation. This action illuminates a light board, plays an audible alert, and immediately signals the need for assistance. The core idea is to stop production proactively so that the problem can be addressed immediately, preventing the issue from cascading down the line and leading to more significant waste. The Andon system is a cornerstone of Jidoka, or "autonomation" (automation with a human touch), one of the two pillars of the TPS, alongside Just-in-Time (JIT) [3]. Its value lies in its ability to foster a culture of quality, empower employees to take ownership of their work, and drive continuous improvement by making problems visible and forcing their resolution at the source.

### 2. Core Principles

The Andon system is built on a set of core principles that are deeply intertwined with the philosophy of Lean Manufacturing and the Toyota Production System. These principles are not merely technical guidelines but cultural tenets that empower individuals and drive organizational excellence.

1.  **Make Problems Visible.** The most fundamental principle of the Andon system is to bring immediate visibility to any abnormality in the production process. By using clear and easily understandable signals (lights, sounds), problems are externalized and made impossible to ignore. This transparency ensures that issues are not hidden or passed down the line, fostering an environment of honesty and accountability.

2.  **Stop the Line, Stop the Defects.** A core tenet of the Andon philosophy is to empower any operator to halt production the moment a problem is detected. This counterintuitive practice of stopping the entire line for a single issue is crucial for preventing the propagation of defects. It prioritizes quality over quantity, ensuring that issues are resolved at the source rather than being dealt with later, which is often more costly and time-consuming.

3.  **Immediate Response and Root Cause Analysis.** When an Andon is triggered, it is not just a signal for help but a call for immediate action. The system is designed to ensure that support staff (team leaders, maintenance, engineers) respond swiftly to diagnose and resolve the issue. The focus is not just on a quick fix but on understanding the root cause of the problem (a practice known as the "5 Whys") to prevent its recurrence.

4.  **Empower the Frontline.** The Andon system is a powerful tool for decentralizing authority and empowering the people closest to the work. It gives operators ownership of quality and the responsibility to act when they see a problem. This trust and empowerment lead to higher engagement, greater job satisfaction, and a more resilient and adaptive workforce.

5.  **Integrate Quality at the Source (Jidoka).** Andon is a key mechanism for implementing Jidoka, or "autonomation"—automation with a human touch. The principle is to build quality into the production process itself, rather than inspecting it in at the end. The Andon system provides the human touch, allowing for intelligent intervention when the automated process deviates from the standard.

6.  **Drive Continuous Improvement (Kaizen).** Every Andon signal represents an opportunity for improvement. By tracking and analyzing Andon calls, organizations can identify recurring problems, systemic weaknesses, and areas for process refinement. This data-driven approach to continuous improvement is at the heart of the Kaizen philosophy and is a key long-term benefit of the Andon system.

### 3. Key Practices

Successfully implementing an Andon system involves a set of concrete practices that translate its core principles into daily operations. These practices are designed to create a responsive, transparent, and continuously improving production environment.

| Practice | Description |
| :--- | :--- |
| **Simple and Accessible Signal Mechanisms** | At each workstation, there must be a straightforward and easily accessible way for an operator to signal a problem. The classic example is the 'Andon cord,' a physical rope that, when pulled, triggers the alert. Modern systems may use buttons, touch screens, or even automated triggers from machinery. The key is that the signal can be activated without delaying the operator's primary work. |
| **Multi-State Visual Displays** | The status of the production line should be visible at a glance to everyone in the area. This is typically achieved through a large, centrally located light board or individual light towers (Andon towers) at each station. These displays use a simple color-coded system: Green (Normal), Yellow/Amber (Assistance Needed), and Red (Production Stopped). |
| **Audible and Text-Based Alerts** | In addition to visual signals, Andon systems often incorporate audible alerts to draw attention to the issue. Modern digital Andon systems also send text messages, emails, or app notifications to specific individuals or groups. |
| **Defined Response Roles and Standard Work** | When an Andon is triggered, there must be a clear and immediate response. This requires defining roles and responsibilities for different types of alerts. Each response role should have a set of standardized work instructions for diagnosing and resolving the issue. |
| **Structured Problem-Solving at the Gemba** | The response to an Andon is not just about getting the line running again; it's about solving the problem permanently. This means going to the 'gemba' (the actual place where the work is done) to observe the problem firsthand and use a structured problem-solving methodology, such as the 5 Whys, to identify the root cause. |
| **Escalation Protocols and Time-Based Alerts** | If a problem cannot be resolved within a predefined time, there must be a clear escalation path. This ensures that problems do not linger and that the appropriate level of resources is applied. |
| **Data Logging and Analysis for Kaizen** | Every Andon event is a valuable piece of data. The system should log the time, location, type of problem, response time, and resolution for every alert. This data should be regularly analyzed to identify trends and drive continuous improvement. |
| **Integration with Production and Quality Systems** | Modern Andon systems are often integrated with other manufacturing systems, such as Manufacturing Execution Systems (MES) and Quality Management Systems (QMS), to allow for automated data collection and a more holistic view of the production process. |
| **Regular Training and Cultural Reinforcement** | The Andon system is as much a cultural tool as it is a technical one. Employees must be trained on the principles of Jidoka and the importance of quality at the source, and management must consistently reinforce a 'no-blame' culture. |

### 4. Application Context

The Andon system, while born in manufacturing, has proven to be a versatile pattern applicable in various contexts. Its effectiveness, however, depends on the nature of the work and the organizational environment.

-   **Best Used For**: Repetitive Production Environments, Quality-Critical Processes, Interdependent Workflows, Customer Service and Support, and Software Development (e.g., failed CI/CD builds).
-   **Not Suitable For**: Highly Creative or Unstructured Work, Continuous Flow Processes (where a full stop is impractical), and Low-Trust, Blame-Oriented Cultures.
-   **Scale**: The Andon pattern is fractal and can be applied at multiple scales, from an individual's work to an entire ecosystem.
-   **Domains**: While its roots are in **automotive manufacturing**, the Andon system's principles have been successfully applied in Electronics Manufacturing, Consumer Goods, Logistics and Warehousing, Healthcare, Software Engineering, and Food Service.

### 5. Implementation

Implementing an Andon system is a socio-technical endeavor that requires careful planning, cultural preparation, and a phased approach. It is not merely a matter of installing lights and cords; it is about rewiring an organization’s response to problems.

-   **Prerequisites**: Standardized Work, Management Commitment and a No-Blame Culture, Basic Problem-Solving Skills, and Defined Team Roles.
-   **Getting Started**: Start Small (pilot program), Define Triggers and Responses, Design the System, Train the Team, and Go Live and Support.
-   **Common Challenges**: Alarm Fatigue, Fear of Stopping the Line, Inadequate Response, and Failure to Address Root Causes.
-   **Success Factors**: Leadership as a Role Model, Employee Engagement, Integration with Daily Management, and Patience and Persistence.

### 6. Evidence & Impact

The effectiveness of the Andon system is backed by decades of application in some of the world's most successful companies and documented in numerous case studies and research papers. The impact is seen in improved quality, reduced downtime, and a more engaged workforce.

-   **Notable Adopters**: Toyota, Ford, Amazon, Boeing, Intel, and General Electric.
-   **Documented Outcomes**: Reduced Defects, Increased Production Uptime (a study by Signalo found a 43% reduction in downtime [6]), Faster Response Times (a Rockwell Automation case study at a Toyota plant showed improved decision-making [5]), and Improved Employee Morale and Engagement.
-   **Research Support**: Studies have shown the effectiveness of Andon in various contexts, including industrial processes, construction, and even in the sugar industry in Kenya, demonstrating its versatility.

### 7. Cognitive Era Considerations

The Andon system, a product of the industrial era, is being fundamentally transformed by the technologies of the cognitive era. The integration of Artificial Intelligence (AI), the Internet of Things (IoT), and advanced analytics is creating a new generation of "intelligent" Andon systems that are predictive, prescriptive, and more deeply integrated into the fabric of the organization.

-   **Cognitive Augmentation Potential**: Predictive Alerts, Automated Root Cause Analysis, and Intelligent Quality Control.
-   **Human-Machine Balance**: The human role shifts from signal to synthesis, focusing on complex problem-solving and ethical oversight.
-   **Evolution Outlook**: The Andon system is evolving from reactive to proactive, from local to global, and will be integrated with digital twins.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
The Andon system primarily defines Rights and Responsibilities for operators and managers within a production process. Operators are granted the Right and Responsibility to halt production upon identifying a defect, while managers are responsible for providing immediate support. This architecture is focused on internal human stakeholders, with limited explicit consideration for broader stakeholders like the environment, supply chain partners, or future generations.

**2. Value Creation Capability:**
The pattern excels at creating knowledge and resilience value. By making problems visible and forcing immediate root cause analysis, it builds a collective capability for continuous improvement (Kaizen). This focus on quality and process integrity creates a more robust and efficient system, which is a form of resilient value creation that goes beyond simple economic output.

**3. Resilience & Adaptability:**
Resilience is at the core of the Andon system. It provides a mechanism for a system to sense and respond to disruptions in real-time, maintaining coherence under stress. The practice of stopping the line to resolve issues, while seemingly counterproductive, is a key strategy for building long-term adaptability and preventing systemic failures.

**4. Ownership Architecture:**
The Andon system redefines ownership as distributed responsibility for quality. It empowers frontline workers by giving them the authority to stop the entire production line, framing ownership as a set of rights and responsibilities rather than just monetary equity. This fosters a culture of accountability and shared stewardship over the production process.

**5. Design for Autonomy:**
The pattern is highly compatible with autonomous systems and low-coordination-overhead designs. Its clear, simple signaling protocol can be easily integrated with AI for predictive alerts and with DAOs for decentralized quality control. The system's logic provides a clear framework for human-machine collaboration in complex, distributed environments.

**6. Composability & Interoperability:**
The Andon system is a highly composable pattern that serves as a building block for larger value-creation systems. It integrates seamlessly with other lean manufacturing patterns like Just-in-Time (JIT) and Kanban, and can be connected to digital systems like Manufacturing Execution Systems (MES) to create a more comprehensive operational architecture.

**7. Fractal Value Creation:**
The core logic of the Andon system—making problems visible and addressing them at the source—is fractal. It can be applied at the scale of an individual workstation, a team, a factory, or even an entire supply chain. This scalability allows the value-creation logic to be replicated across different levels of an organization or ecosystem.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
The Andon System is a powerful enabler of collective value creation, particularly in the domains of resilience, knowledge, and quality. It establishes a clear architecture of Rights and Responsibilities that empowers individuals and fosters a culture of shared ownership. While its traditional application is focused within a single organization, its principles are foundational for building more complex, resilient, and distributed value-creation systems.

**Opportunities for Improvement:**
- Broaden the stakeholder architecture to explicitly include external stakeholders, such as suppliers and customers, in the quality feedback loop.
- Integrate environmental and social metrics as triggers for Andon alerts, moving beyond production-related defects.
- Develop a cross-organizational Andon system to manage shared risks and opportunities in a multi-firm commons or ecosystem.

### 9. Resources & References

-   **Essential Reading**:
    -   Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production*. Productivity Press. [7]
    -   Liker, J. K. (2004). *The Toyota Way: 14 Management Principles from the World's Greatest Manufacturer*. McGraw-Hill. [8]
    -   Rother, M., & Shook, J. (2003). *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda*. Lean Enterprise Institute. [9]

-   **Organizations & Communities**:
    -   Lean Enterprise Institute (LEI)
    -   The Association for Manufacturing Excellence (AME)

-   **Tools & Platforms**:
    -   Versacall
    -   L2L (Leading2Lean)
    -   Shoplogix

-   **References**:
    1.  [Andon (manufacturing) - Wikipedia](https://en.wikipedia.org/wiki/Andon_(manufacturing))
    2.  [What is Andon in Lean Manufacturing? - Planview](https://www.planview.com/resources/guide/what-is-lean-manufacturing/andon-lean-manufacturing/)
    3.  [Andon: Definition and Benefits - Vorne Industries](https://www.vorne.com/learn/key-concepts/andon/)
    4.  [Andon in Lean Manufacturing Guide - L2L](https://www.l2l.com/guide/andon)
    5.  [Andon Solution Delivers Better Decision Making at Toyota - Rockwell Automation](https://www.rockwellautomation.com/en-us/company/news/case-studies/andon-solution-delivers-better-decision-making-at-toyota.html)
    6.  [Andon System for Manufacturing - Signalo](https://signalo.us/andon/)
    7.  Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production*. Productivity Press.
    8.  Liker, J. K. (2004). *The Toyota Way: 14 Management Principles from the World's Greatest Manufacturer*. McGraw-Hill.
    9.  Rother, M., & Shook, J. (2003). *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda*. Lean Enterprise Institute.
