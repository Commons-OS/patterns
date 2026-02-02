---
id: pat_01kg5023ytf2s8rdchqz3eqbg0
page_url: https://commons-os.github.io/patterns/functional-safety-iso-26262/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/functional-safety-iso-26262.md
slug: functional-safety-iso-26262
title: Functional Safety (ISO 26262)
aliases: []
version: 1.0
created: 2026-01-28 00:00:00+00:00
modified: 2026-01-28 00:00:00+00:00
classification:
  universality: domain
  domain: operations
  category:
  - framework
  era:
  - industrial
  - digital
  origin: []
  status: draft
  commons_alignment: 3
  commons_domain:
  - business
  - startup
  - security
generalizes_from: []
specializes_to: []
enables: []
requires: []
related:
- pat_01kg5023z4ejgvpxs00h779hk7
- pat_01kg5023x8evg9fk7ax23cbrbn
- pat_01kg5023wjfg8tqb1zqbg7dd8h
- pat_01kg5023xge89s6mx3nbjd0mgg
- pat_01kg5023vyfzhvteh04eykysqz
- pat_01kg5023zrexhr77rgbe4f62ew
- pat_01kg5023vjetsaajnc397n2n2m
- pat_01kg5023vyfzhvteh02a487gvh
- pat_01kg5023z8f6h9wk9sdad8sxxd
- pat_01kg5023x8evg9fk7as5cxmnwk
- pat_01kg5023z3f90bkx13t1xprvjz
- pat_01kg5023zcf99tjg7qgdbhqfkm
- pat_01kg5023zzecsb265cp79x0gvh
- pat_01kg5023ybeqhsr5sn20s4jgvn
- pat_01kg5023yaea8sqyn9hkqb477d
contributors:
- higgerix
- cloudsters
sources:
- https://www.synopsys.com/glossary/what-is-iso-26262.html
- https://www.ansys.com/simulation-topics/what-is-iso-26262
- https://www.perforce.com/blog/qac/what-is-iso-26262
- https://www.iso.org/standard/68385.html
- https://www.jamasoftware.com/blog/2019/12/03/the-importance-of-iso-26262-in-automotive-development/
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---




# 1. Overview

Functional Safety (ISO 26262) is an international standard that addresses the functional safety of electrical and electronic (E/E) systems in production road vehicles. Titled "Road vehicles – Functional safety", the standard is designed to ensure that automotive E/E systems operate safely and to mitigate the risks associated with their potential malfunctions. It provides a comprehensive framework and a set of guidelines for the entire lifecycle of these systems, from initial concept and design to production, operation, service, and decommissioning [1]. The primary goal of ISO 26262 is to minimize the likelihood of harm to people due to failures in the electronic systems of a vehicle. It is a risk-based safety standard, meaning it provides a structured approach to identifying, assessing, and mitigating hazards throughout the development process. The standard is derived from the more general functional safety standard, IEC 61508, but has been specifically adapted for the automotive industry [2].

# 2. Core Principles

The core principles of ISO 26262 are centered around a systematic and rigorous approach to achieving functional safety. These principles include:

*   **The Safety Lifecycle:** The standard defines a safety lifecycle that encompasses all phases of product development. This lifecycle includes management, development, production, operation, service, and decommissioning. By integrating safety-related activities throughout the entire lifecycle, the standard ensures that safety is not an afterthought but a fundamental aspect of the product from its inception to its retirement [1].

*   **Risk-Based Approach:** A cornerstone of ISO 26262 is its risk-based approach to safety. The standard requires a thorough analysis of potential hazards and an assessment of the associated risks. This is achieved through a process called Hazard Analysis and Risk Assessment (HARA), which helps to determine the necessary level of risk reduction for each identified hazard [3].

*   **Automotive Safety Integrity Levels (ASILs):** To classify the level of risk and to define the necessary safety requirements, ISO 26262 introduces the concept of Automotive Safety Integrity Levels (ASILs). ASILs are determined based on three factors: the severity of potential harm, the probability of exposure to a hazardous situation, and the controllability of the situation by the driver. There are four ASILs, from A (lowest risk) to D (highest risk), with each level requiring a different degree of rigor in the development and verification processes [4].

*   **Traceability:** The standard emphasizes the importance of traceability throughout the development process. This means that all safety requirements must be linked to their source, their implementation in the design, and their verification and validation. Traceability ensures that all safety requirements are addressed and provides a clear audit trail for compliance purposes.

# 3. Key Practices

ISO 26262 prescribes a set of key practices and methods to be applied during the development of safety-related E/E systems. These practices are designed to prevent, detect, and control failures. Some of the most important practices include:

*   **Hazard Analysis and Risk Assessment (HARA):** HARA is one of the first and most critical steps in the ISO 26262 process. It involves identifying potential hazards that could arise from the malfunctioning of an E/E system and assessing the associated risks. The results of the HARA are used to define the safety goals for the system and to determine the required ASIL for each safety goal [3].

*   **Failure Mode and Effects Analysis (FMEA):** FMEA is a systematic method for analyzing potential failure modes of a system and their effects on the system's operation. It is used to identify potential weaknesses in the design and to define measures to mitigate the effects of failures. FMEA can be applied at different levels, from the system level down to the component level.

*   **Fault Tree Analysis (FTA):** FTA is a top-down, deductive failure analysis in which a system's failure is traced back to its root causes. It is a powerful tool for identifying potential combinations of failures that could lead to a hazardous event. FTA is often used in conjunction with FMEA to provide a more comprehensive analysis of system safety.

*   **Software and Hardware Development Processes:** Part 6 of the standard is dedicated to product development at the software level, while Part 5 covers hardware development. These parts define specific requirements and recommendations for the design, implementation, and testing of software and hardware components to ensure their safety and reliability. This includes requirements for coding standards, software architecture, and hardware metrics [4].

*   **Verification and Validation:** ISO 26262 places a strong emphasis on verification and validation activities. Verification ensures that the system is being built correctly, while validation ensures that the correct system is being built. The standard requires a comprehensive verification and validation plan, including testing at the unit, integration, and system levels.


# 4. Application Context

ISO 26262 is applicable to all series production road vehicles, with the exception of mopeds. This includes passenger cars, trucks, buses, and motorcycles. The standard is relevant for any electrical and/or electronic system that has a safety-related function. As vehicles become increasingly complex and reliant on electronic systems for critical functions such as braking, steering, and advanced driver-assistance systems (ADAS), the importance and applicability of ISO 26262 continue to grow. The standard is intended to be applied in a variety of contexts, including:

*   **Original Equipment Manufacturers (OEMs):** Automotive OEMs are the primary users of ISO 26262. They are responsible for the overall safety of the vehicle and must ensure that all E/E systems comply with the standard.

*   **Suppliers:** Suppliers of automotive components, including hardware and software, are also required to comply with ISO 26262. They must provide evidence to the OEMs that their products have been developed in accordance with the standard.

*   **Development Tools:** The standard also has implications for the developers of software and hardware development tools. Part 8 of ISO 26262 provides guidance on the qualification of tools used in the development of safety-related systems. This ensures that the tools themselves do not introduce errors into the development process [4].

# 5. Implementation

Implementing ISO 26262 is a complex and multifaceted process that requires a strong commitment from the entire organization. The following are some of the key steps involved in implementing the standard:

1.  **Establish a Safety Culture:** A strong safety culture is the foundation for successful implementation of ISO 26262. This means that everyone in the organization, from top management to individual engineers, must be committed to safety and understand their role in the safety process.

2.  **Develop a Safety Plan:** A safety plan should be developed at the beginning of the project. This plan should define the safety goals for the system, the activities that will be performed to achieve those goals, and the resources that will be required.

3.  **Perform a Hazard Analysis and Risk Assessment (HARA):** As mentioned earlier, HARA is a critical step in the ISO 26262 process. It is used to identify potential hazards, assess the associated risks, and define the safety goals for the system.

4.  **Define the Functional and Technical Safety Concepts:** Based on the results of the HARA, the functional safety concept is developed. This concept describes how the system will achieve the safety goals. The technical safety concept then translates the functional safety concept into specific technical requirements for the hardware and software.

5.  **Develop Hardware and Software in Accordance with ASILs:** The development of hardware and software must be performed in accordance with the assigned ASILs. This includes using appropriate design methods, coding standards, and verification and validation techniques.

6.  **Perform Verification and Validation:** Verification and validation activities must be performed throughout the development process to ensure that the system meets the safety requirements. This includes testing at the unit, integration, and system levels.

7.  **Create a Safety Case:** A safety case is a documented argument that provides evidence that the system is acceptably safe. The safety case should include all of the artifacts produced during the development process, such as the safety plan, HARA, FMEA, and test results.

# 6. Evidence & Impact

The adoption of ISO 26262 has had a significant impact on the automotive industry. The standard has helped to improve the safety and reliability of automotive E/E systems and has reduced the number of accidents and injuries caused by system malfunctions. The evidence for the effectiveness of ISO 26262 can be seen in the following areas:

*   **Reduced Number of Recalls:** The implementation of ISO 26262 has led to a reduction in the number of vehicle recalls related to E/E system failures. This is because the standard helps to identify and mitigate potential problems early in the development process.

*   **Improved System Reliability:** The rigorous design, verification, and validation processes required by ISO 26262 have resulted in more reliable and robust E/E systems. This has led to a reduction in the number of system failures and an improvement in overall vehicle quality.

*   **Increased Consumer Confidence:** The adoption of ISO 26262 has helped to increase consumer confidence in the safety of modern vehicles. Consumers are more likely to purchase vehicles that have been developed in accordance with the standard.

*   **Harmonization of Safety Standards:** ISO 26262 has become the de facto global standard for automotive functional safety. This has helped to harmonize safety standards across the industry and has made it easier for OEMs and suppliers to develop and sell their products in different markets.


# 7. Cognitive Era Considerations

The cognitive era, characterized by the rise of artificial intelligence (AI), machine learning (ML), and autonomous systems, presents both new challenges and opportunities for functional safety in the automotive industry. While ISO 26262 provides a robust framework for the development of traditional E/E systems, its application to AI-driven systems requires careful consideration and adaptation. The following are some of the key considerations for functional safety in the cognitive era:

*   **Nondeterministic nature of AI/ML systems:** Unlike traditional software, which is deterministic and follows a predefined set of rules, AI and ML systems can be nondeterministic. Their behavior can be influenced by the data they are trained on and the environment they operate in. This makes it challenging to predict and verify their behavior in all possible situations. New methods and techniques are needed to validate the safety of these systems, such as simulation-based testing and formal verification of neural networks.

*   **The "black box" problem:** Many AI and ML models, such as deep neural networks, are often referred to as "black boxes" because it can be difficult to understand how they make their decisions. This lack of transparency makes it challenging to identify and mitigate potential safety risks. Techniques for explainable AI (XAI) are being developed to address this issue, but they are still in their early stages.

*   **The role of data:** The safety of AI and ML systems is highly dependent on the quality and completeness of the data they are trained on. Biased or incomplete data can lead to unsafe behavior. It is therefore essential to have a rigorous process for collecting, cleaning, and validating training data.

*   **Over-the-air (OTA) updates:** The ability to update vehicle software over the air presents new challenges for functional safety. It is essential to have a secure and reliable process for deploying OTA updates and for ensuring that the updated software is safe and does not introduce new hazards.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
ISO 26262 primarily defines responsibilities for Original Equipment Manufacturers (OEMs) and their suppliers, with the central stakeholder being the human user (driver, passenger, pedestrian) whose safety is the main concern. The rights of the public to safe vehicles are implicitly addressed by placing stringent responsibilities on manufacturers. However, the framework does not explicitly consider the environment, future generations, or non-human actors as stakeholders with defined rights and responsibilities, focusing narrowly on immediate human safety.

**2. Value Creation Capability:**
The primary value created by this pattern is safety and reliability, which can be understood as a form of resilience value. By preventing accidents and system malfunctions, it prevents the destruction of value (lives, property) and builds trust in complex technological systems. While this is a critical form of value, the pattern does not directly enable the creation of new, collective forms of value beyond risk mitigation, such as social, ecological, or knowledge value.

**3. Resilience & Adaptability:**
The core of ISO 26262 is to build resilience in automotive systems against technical failures. It provides a rigorous framework for identifying, assessing, and mitigating risks, helping systems maintain coherence under stress. However, the standard's highly structured and compliance-oriented nature can make it slow to adapt to rapidly evolving technologies like AI and autonomous systems, which are non-deterministic and challenge traditional verification and validation methods.

**4. Ownership Architecture:**
The pattern's concept of ownership is rooted in legal and industrial liability, focusing on who is responsible when a failure occurs. It does not engage with a broader concept of ownership as a set of rights and responsibilities for collective value creation. The framework is designed to assign and manage risk within a traditional supply chain, not to foster a sense of shared stewardship over the commons of mobility safety.

**5. Design for Autonomy:**
ISO 26262 was developed for conventional, deterministic electronic systems and faces significant challenges when applied to autonomous systems and AI. As noted in the pattern's "Cognitive Era Considerations," the non-deterministic nature of AI, the "black box" problem, and the reliance on data quality create gaps in the standard's ability to ensure safety. It is not inherently designed for the low-coordination, decentralized operation envisioned in many autonomous systems.

**6. Composability & Interoperability:**
The pattern is highly interoperable within the automotive industry, providing a common language and set of expectations for functional safety across a complex supply chain. It is designed to be composed with other engineering and quality management standards (e.g., Automotive SPICE). This allows it to be a foundational layer for building larger, safety-critical systems, ensuring that different components can be integrated with a consistent level of safety assurance.

**7. Fractal Value Creation:**
The logic of functional safety assessment can be applied fractally across different scales. The principles of hazard analysis, risk assessment, and ASIL determination can be used at the component level, the system level, the vehicle level, and could even be extended to the level of traffic management systems or smart city infrastructure. This scalability allows the core value-creation logic—ensuring safety—to be consistently applied throughout a complex system-of-systems.

**Overall Score: 3 (Transitional)**

**Rationale:**
ISO 26262 is a critical standard for ensuring safety in a world of increasingly complex automotive technology. It provides a robust framework for creating resilience value by preventing harm. However, its alignment with a commons-based approach is limited by its narrow stakeholder focus, its traditional view of ownership as liability, and its struggles to adapt to the non-deterministic nature of autonomous systems. It is a transitional pattern because while it is essential for safety today, it requires significant adaptation to become a true enabler of resilient, collective value creation in the cognitive era.

**Opportunities for Improvement:**
- Extend the stakeholder model to formally include the environment and data commons as entities with rights and protections.
- Develop extensions or companion standards (like ISO/PAS 21448 for SOTIF) that are better suited for the validation of AI/ML-based systems and autonomous behaviors.
- Integrate principles of shared data ownership and stewardship, especially for the vast amounts of data generated and used by modern vehicles to improve collective safety.
