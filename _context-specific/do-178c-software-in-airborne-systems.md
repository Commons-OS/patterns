---
id: pat_01kg50240me98tfa0z5h8ade8f
page_url: https://commons-os.github.io/patterns/context-specific/do-178c-software-in-airborne-systems/
github_url: https://github.com/commons-os/patterns/blob/main/_context-specific/do-178c-software-in-airborne-systems.md
slug: do-178c-software-in-airborne-systems
title: DO-178C (Software in Airborne Systems)
aliases: [ED-12C, RTCA DO-178C]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: context-specific
  domain: technology
  category: [framework]
  era: [digital]
  origin: [RTCA, EUROCAE]
  status: draft
  commons_alignment: 3
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: 
  - https://www.windriver.com/solutions/learning/do-178c
  - https://en.wikipedia.org/wiki/DO-178C
  - https://www.modernrequirements.com/blogs/do-178c/
  - https://www.qualitestgroup.com/insights/blog/simplify-do-178c-compliance-with-10-best-practices/
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

DO-178C, formally titled "Software Considerations in Airborne Systems and Equipment Certification," is the internationally recognized standard for the development of software used in airborne systems. It provides a rigorous framework of processes and objectives that must be met to ensure the safety and reliability of aviation software. The standard is a joint effort by the Radio Technical Commission for Aeronautics (RTCA) and the European Organisation for Civil Aviation Equipment (EUROCAE), and it is the primary means by which certification authorities, such as the Federal Aviation Administration (FAA) and the European Union Aviation Safety Agency (EASA), approve software for use in commercial and military aircraft. The core problem that DO-178C addresses is the inherent risk associated with software in safety-critical systems, where a failure could lead to catastrophic events, including loss of life and aircraft. By establishing a structured and verifiable development lifecycle, the standard aims to minimize the probability of software errors and ensure that airborne systems perform their intended functions with the highest level of integrity.

The origin of DO-178C lies in the evolution of avionics and the increasing reliance on software to control critical aircraft functions. Its predecessor, DO-178B, was released in 1992 and served as the industry benchmark for over two decades. However, as software development methodologies advanced, with the advent of model-based design, object-oriented programming, and more sophisticated development tools, it became apparent that DO-178B needed to be updated. In 2011, after a multi-year collaborative effort involving hundreds of industry experts, DO-178C was released. This new version, along with its technology-specific supplements, provides a more comprehensive and adaptable framework that accommodates modern software engineering practices while maintaining the fundamental principles of safety and rigor that defined its predecessor.

### 2. Core Principles

DO-178C is built upon a set of core principles that ensure the development of safe and reliable software for airborne systems. These principles guide the entire software lifecycle, from planning to verification, and are fundamental to achieving certification.

1.  **Systematic Development Process**: DO-178C mandates a structured and disciplined approach to software development. This involves a series of well-defined processes, including software planning, development, verification, configuration management, and quality assurance. Each process has specific objectives that must be satisfied, ensuring that all aspects of the software lifecycle are rigorously controlled and documented.

2.  **Risk-Based Assurance**: The standard introduces the concept of Design Assurance Levels (DALs), which categorize software based on the potential consequences of its failure. Ranging from DAL A (catastrophic) to DAL E (no safety effect), this risk-based approach ensures that the level of effort and rigor applied to software development and verification is proportional to the criticality of the software's function. The higher the DAL, the more stringent the objectives that must be met.

3.  **Requirements-Driven Development**: All software development activities are driven by requirements. DO-178C requires that high-level requirements are decomposed into low-level requirements, which are then used to guide the design and implementation of the software. This ensures that the final software product directly addresses the needs of the system and that all code has a clear and documented purpose.

4.  **Comprehensive Verification**: Verification is a critical component of DO-178C, and it involves a combination of reviews, analyses, and tests to ensure that the software meets its requirements. The standard emphasizes that verification is not a one-time event but an ongoing process that occurs throughout the development lifecycle. This includes verifying that the software is robust, that it performs its intended function correctly, and that it does not contain any unintended functionality.

5.  **End-to-End Traceability**: DO-178C mandates bidirectional traceability between all software development artifacts. This means that every requirement must be traceable to the code that implements it and the tests that verify it, and vice versa. This complete traceability provides a clear audit trail and ensures that all requirements are met, all code is justified, and all tests are relevant.

6.  **Independence in Verification**: To ensure objectivity, DO-178C requires that certain verification activities be performed with independence. This means that the person responsible for verifying a software artifact cannot be the same person who developed it. This separation of duties helps to prevent errors and ensures a more thorough and unbiased review of the software.

7.  **Strict Configuration Management**: All software artifacts, including requirements, design documents, code, and test cases, must be placed under strict configuration management. This ensures that all changes are controlled, tracked, and approved, and that the integrity of the software baseline is maintained throughout the development lifecycle.

### 3. Key Practices

DO-178C compliance is achieved through the implementation of a set of key practices that translate the core principles into concrete actions. These practices cover the entire software lifecycle and are essential for developing safe and reliable airborne software.

1.  **Develop a Comprehensive Set of Plans**: Before any development work begins, a suite of planning documents must be created. This includes the Plan for Software Aspects of Certification (PSAC), which outlines the overall certification strategy, as well as detailed plans for software development (SDP), verification (SVP), configuration management (SCMP), and quality assurance (SQAP). These plans serve as the roadmap for the entire project and are reviewed and approved by certification authorities.

2.  **Establish and Maintain a Requirements Hierarchy**: A clear and complete hierarchy of requirements is established, starting from system-level requirements and flowing down to high-level and low-level software requirements. Each requirement must be uniquely identified, unambiguous, and testable. This structured approach ensures that the software is built to the correct specifications and that all functional and safety requirements are addressed.

3.  **Enforce Rigorous Design and Coding Standards**: The software design is developed based on the low-level requirements, and the code is implemented according to the design. Strict coding standards are enforced to ensure that the code is clear, maintainable, and free from common errors. The use of specific language features may be restricted, and all code must be traceable back to a corresponding requirement.

4.  **Conduct Thorough Verification and Validation**: A comprehensive verification and validation (V&V) process is implemented to ensure that the software meets its requirements and is free from defects. This includes a combination of reviews, analyses, and testing. Reviews are conducted on all software artifacts, including requirements, design, and code. Analyses are performed to assess aspects such as timing and memory usage. Testing is conducted at the unit, integration, and system levels to verify the functionality and robustness of the software.

5.  **Implement Robust Configuration Management**: All software artifacts are placed under a formal configuration management system. This ensures that all items are uniquely identified, that changes are controlled through a formal change request process, and that the history of all changes is maintained. This practice is crucial for maintaining the integrity of the software and for ensuring that the certified software is the same as the software that was developed and tested.

6.  **Ensure Independence in Verification**: To ensure objectivity, critical verification activities are performed by individuals who were not involved in the development of the artifact being verified. This practice of independence is applied to the verification of requirements, design, and code, and it helps to identify errors that may have been missed by the original developers.

7.  **Qualify Software Development and Verification Tools**: Any tools used to automate development or verification activities must be qualified to ensure that they perform their intended function correctly. The level of rigor required for tool qualification depends on the criticality of the software and the impact of the tool on the development process. This practice prevents the introduction of errors into the software by faulty tools.

8.  **Generate and Maintain Comprehensive Documentation**: Detailed documentation is created and maintained for all aspects of the software lifecycle. This includes the planning documents, requirements, design, code, verification cases and procedures, and all verification results. This documentation provides the evidence needed to demonstrate compliance with DO-178C and is reviewed by the certification authorities.

### 4. Application Context

DO-178C finds its primary and mandatory application in the realm of safety-critical avionics software, where failure could have catastrophic consequences. This includes flight control, navigation, and engine control systems. The standard is also increasingly adopted for mission-critical military systems, such as those in unmanned aerial vehicles (UAVs), and is influential in other high-assurance commercial sectors like medical devices, nuclear power, and autonomous vehicles, where software reliability is paramount. Conversely, the standard's rigor and cost are not justified for non-safety-critical applications, such as in-flight entertainment systems, or for rapid prototyping and research where agility is prioritized over formal certification.

DO-178C is scalable, applicable from individual components to large, integrated systems developed by single teams or multi-organizational consortia. While its home domain is aerospace and defense, its principles are being adapted for use in other industries requiring high-assurance software, including medical devices, automotive (particularly for autonomous driving), industrial control, and rail transportation.

### 5. Implementation

Successful implementation of DO-178C hinges on several prerequisites, including strong organizational commitment, a skilled workforce with expertise in safety-critical systems, and well-defined, compliant development processes. The initial steps involve a gap analysis to assess current practices against the standard, followed by the development of a comprehensive compliance plan. The selection and qualification of software tools is a critical phase, as is the training of all personnel. A pilot project is often recommended to validate processes and tools before full-scale deployment.

Common challenges in DO-178C implementation include managing the extensive documentation requirements, maintaining complete traceability, and navigating the complexities of tool qualification. Key success factors include early and thorough planning, the strategic use of automation to improve efficiency and reduce errors, seeking expert guidance from consultants or DERs, and fostering a culture of continuous improvement to stay current with the evolving standard and best practices.

### 6. Evidence & Impact

The impact of DO-178C is evident across the aerospace and defense industries. Virtually all major aircraft manufacturers, such as Boeing and Airbus, and their avionics suppliers, including Collins Aerospace and Honeywell, have adopted the standard. Furthermore, government agencies like the U.S. Department of Defense and NASA have embraced DO-178C for their critical systems, and it is now being adopted by emerging players in the urban air mobility (UAM) and drone sectors.

The documented outcomes of DO-178C adoption are significant. The standard has been instrumental in improving software reliability and reducing the incidence of software-related failures in aviation. While the upfront costs of compliance can be substantial, the emphasis on early defect detection and process control often leads to long-term cost savings through reduced rework. The standard also fosters greater interoperability among components from different suppliers. The effectiveness of DO-178C is supported by numerous studies and research from institutions like NASA's Software Engineering Laboratory, which have demonstrated a clear link between compliance and improved software safety and system safety and reliability.

### 7. Cognitive Era Considerations

The cognitive era, characterized by the rise of artificial intelligence (AI) and machine learning (ML), presents both opportunities and challenges for the DO-178C framework. While the standard was not originally designed to address the unique complexities of AI/ML systems, its principles of rigor, traceability, and verification remain highly relevant.

**Cognitive Augmentation Potential**:

AI and automation have the potential to significantly enhance the DO-178C compliance process. AI-powered tools can be used to automate many of the tedious and time-consuming tasks associated with compliance, such as requirements analysis, test case generation, and documentation. This can lead to a more efficient and cost-effective compliance process, while also reducing the risk of human error. For example, natural language processing (NLP) can be used to analyze requirements for ambiguity and inconsistency, while machine learning algorithms can be used to optimize test suites and identify areas of high risk.

**Human-Machine Balance**:

Despite the potential of AI, the human element remains crucial in the DO-178C process. The judgment and expertise of human engineers are still required to make critical decisions about safety, to interpret the results of verification activities, and to ensure that the overall system is safe and reliable. The role of the human in the cognitive era will shift from performing repetitive tasks to overseeing and validating the work of AI systems. This will require a new set of skills, including a deep understanding of AI/ML concepts and the ability to work effectively with intelligent tools.

**Evolution Outlook**:

The increasing use of AI/ML in airborne systems is driving an evolution in the DO-178C framework. The industry is actively working on developing new guidance and standards to address the unique challenges of certifying AI/ML systems. This includes developing methods for verifying and validating the behavior of non-deterministic systems, ensuring the explainability of AI/ML models, and managing the vast amounts of data required to train and test these systems. The future of DO-178C will likely involve a closer integration of AI/ML concepts and a greater emphasis on the use of formal methods and other advanced verification techniques.

### 8. Commons Alignment Assessment

This assessment evaluates the DO-178C standard against the seven dimensions of a commons-aligned pattern. It aims to provide a balanced view of how the standard contributes to or detracts from a commons-based approach to knowledge and practice.

**1. Stakeholder Mapping**:

The stakeholders in the DO-178C ecosystem are numerous and diverse. They include:

*   **Regulatory Bodies**: The FAA, EASA, and other national aviation authorities are the primary stakeholders, as they are responsible for ensuring the safety of the flying public.
*   **Aircraft Manufacturers**: Companies like Boeing and Airbus are major stakeholders, as they are ultimately responsible for the safety and certification of their aircraft.
*   **Avionics Suppliers**: The entire supply chain of avionics and software providers is directly impacted by the standard.
*   **Engineers and Developers**: The individuals who design, develop, and test the software are key stakeholders.
*   **The Flying Public**: The ultimate beneficiaries of the standard are the passengers and crew who rely on the safety of airborne systems.

The stakeholder mapping is comprehensive in its focus on safety and the direct participants in the aviation industry. However, it is less inclusive of broader societal stakeholders who may be impacted by the environmental or economic aspects of aviation.

**2. Value Creation**:

DO-178C creates significant value in several forms:

*   **Safety Value**: The primary value created is the assurance of safety in airborne software systems. This is a public good that benefits everyone who flies.
*   **Economic Value**: The standard creates economic value by enabling a global market for interoperable and certifiable avionics components. It also reduces the long-term costs associated with software failures and rework.
*   **Knowledge Value**: The standard itself is a valuable body of knowledge that has been developed and refined over decades. It represents a collective understanding of how to build safe and reliable software.

The value created by DO-178C is primarily captured by the aviation industry and its customers. While the public benefits from the safety it provides, the economic and knowledge value is largely contained within the industry.

**3. Value Preservation**:

DO-178C has a robust process for preserving its value and relevance over time. The standard is periodically updated to reflect changes in technology and best practices. The transition from DO-178B to DO-178C is a clear example of this. The use of supplemental documents, such as those for model-based design and object-oriented technology, allows the standard to adapt to new technologies without requiring a complete rewrite. This evolutionary approach ensures that the standard remains relevant and effective in a rapidly changing technological landscape.

**4. Shared Rights & Responsibilities**:

DO-178C establishes a clear distribution of rights and responsibilities among the various stakeholders. Regulatory bodies have the right to audit and approve software, while manufacturers and suppliers have the responsibility to comply with the standard. Engineers and developers have the responsibility to follow the prescribed processes and to produce high-quality software. However, the rights to the standard itself are held by RTCA and EUROCAE, and the document must be purchased. This limits the accessibility of the standard and can be a barrier to entry for smaller organizations and individuals.

**5. Systematic Design**:

DO-178C is the epitome of a systematically designed process. It provides a complete, end-to-end framework for the software development lifecycle, with well-defined processes, objectives, and artifacts. The standard's emphasis on planning, traceability, and verification ensures that the development process is repeatable, predictable, and auditable. This systematic design is a key factor in the standard's success in ensuring software safety.

**6. Systems of Systems**:

DO-178C is designed to work within a larger 
system of systems. It is closely integrated with other standards, such as ARP4754 for system-level design and DO-254 for hardware development. This integrated approach ensures that safety is addressed at all levels of the system, from the overall aircraft design down to the individual software and hardware components. The standard's modular and objective-based nature allows it to be composed with other processes and standards, making it adaptable to a wide range of system architectures.

**7. Fractal Properties**:

The principles of DO-178C exhibit fractal properties, as they can be applied at different scales. The core principles of rigor, traceability, and verification are just as relevant to a small, single-purpose software component as they are to a large, complex flight management system. This scalability allows the standard to be applied consistently across the entire software supply chain, ensuring that all components, regardless of their size or complexity, are developed to the same high standards of safety and reliability.

**Overall Score: 3 (Transitional)**

DO-178C is a highly effective standard for ensuring the safety and reliability of airborne software. Its systematic design, focus on risk-based assurance, and robust verification processes are exemplary. However, its alignment with a commons-based approach is limited by its proprietary nature and its focus on the aviation industry. While the safety value it creates is a public good, the knowledge and economic value are largely captured by the industry. To become more commons-aligned, the standard could be made more accessible to the public, and its principles could be more actively promoted for adoption in other safety-critical domains. The increasing adoption of DO-178C in other industries is a positive step in this direction, and it demonstrates the potential for the standard to evolve into a more open and widely applicable framework for high-assurance software development.

### 9. Resources & References

**Essential Reading**:

*   **DO-178C, Software Considerations in Airborne Systems and Equipment Certification**: The official standard from RTCA and EUROCAE. This is the definitive source for all information related to the standard.
*   **Developing Safety-Critical Software: A Practical Guide for Aviation Software and DO-178C Compliance by Leanna Rierson**: A comprehensive guide to the practical application of DO-178C, with detailed explanations and examples.
*   **The Avionics Handbook, Second Edition by Cary R. Spitzer**: A broad overview of the avionics industry, with several chapters dedicated to software development and certification.

**Organizations & Communities**:

*   **RTCA (Radio Technical Commission for Aeronautics)**: The primary organization responsible for developing and publishing the DO-178C standard in the United States.
*   **EUROCAE (European Organisation for Civil Aviation Equipment)**: The European counterpart to RTCA, responsible for the ED-12C version of the standard.
*   **SAE International**: A global association of engineers and technical experts in the aerospace, automotive, and commercial-vehicle industries. SAE publishes related standards, such as ARP4754.

**Tools & Platforms**:

*   **Ansys SCADE**: A model-based development environment that is widely used for developing and certifying safety-critical software to DO-178C standards.
*   **LDRA Tool Suite**: A comprehensive set of tools for code analysis, testing, and verification that supports DO-178C compliance.
*   **Parasoft C/C++test**: A unified testing solution that helps automate a number of DO-178C verification activities.
*   **Jama Connect**: A requirements management platform that helps manage the complex traceability requirements of DO-178C.

**References**:

[1] Wind River. (n.d.). *What Is DO-178C?*. Retrieved from https://www.windriver.com/solutions/learning/do-178c

[2] Wikipedia. (2023, October 26). *DO-178C*. Retrieved from https://en.wikipedia.org/wiki/DO-178C

[3] Modern Requirements. (2025, June 17). *Understanding DO-178C: The Standard Behind Airborne Software Safety*. Retrieved from https://www.modernrequirements.com/blogs/do-178c/

[4] Qualitest. (2021, June 7). *Simplify DO-178C Compliance with 10 Best Practices*. Retrieved from https://www.qualitestgroup.com/insights/blog/simplify-do-178c-compliance-with-10-best-practices/

[5] Ansys. (2025, August 27). *Your Guide To Implementing the DO-178C Standard*. Retrieved from https://www.ansys.com/blog/your-guide-to-implementing-do-178c-standard

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/context-specific/do-178c-software-in-airborne-systems/](https://commons-os.github.io/patterns/context-specific/do-178c-software-in-airborne-systems/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_context-specific/do-178c-software-in-airborne-systems.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_context-specific/do-178c-software-in-airborne-systems.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
