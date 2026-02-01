---
id: pat_01kg50240nfz989qp3d2bx6vvq
page_url: https://commons-os.github.io/patterns/iec-62304-medical-device-software/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/iec-62304-medical-device-software.md
slug: iec-62304-medical-device-software
title: IEC 62304 (Medical Device Software)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: context-specific
  domain: technology
  category: [framework, methodology]
  era: [digital]
  origin: ["International Electrotechnical Commission"]
  status: draft
  commons_alignment: 2
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

# IEC 62304 (Medical Device Software)

## 1. Overview

IEC 62304, titled "Medical device software – Software life cycle processes," is a seminal international standard that establishes a comprehensive framework for the entire lifecycle of medical device software. Its primary objective is to ensure the safety and effectiveness of software integral to the functioning of medical devices, a category that encompasses both software embedded within a physical medical device (SiMD) and standalone software that functions as a medical device in its own right (SaMD). The standard provides a risk-based framework that guides manufacturers in developing, maintaining, and managing software in a manner that prioritizes patient safety and meets regulatory requirements.

While IEC 62304 is not a quality management system (QMS) in itself, it is designed to be seamlessly integrated within a broader QMS framework, most commonly one that is compliant with ISO 13485, the international standard for medical device quality management systems. This integration ensures that the software development and maintenance processes are aligned with the overall quality objectives of the organization. The standard has achieved widespread international recognition and has been adopted as a national standard in numerous countries. Its harmonization with the regulatory requirements of major jurisdictions, including the United States (FDA) and the European Union, makes it an indispensable tool for medical device manufacturers seeking to gain market access in these regions.

## 2. Core Principles

The core principles of IEC 62304 are centered around a risk-based approach to software development and maintenance. The standard emphasizes the importance of a structured and documented process throughout the entire software lifecycle, from initial conception to final decommissioning. The key principles include a steadfast commitment to **risk management**, which is woven into every stage of the software lifecycle. This involves a continuous process of identifying, analyzing, and controlling risks associated with the software, a principle that is operationalized through a close synergy with ISO 14971, the international standard for risk management of medical devices. Another cornerstone of the standard is the **software safety classification**, a three-tiered system (Class A, B, and C) that categorizes software based on its potential to cause harm. This classification is a pivotal element of the standard, as it dictates the level of rigor and documentation required for the software development and maintenance processes. The standard also delineates a comprehensive set of **software development lifecycle processes**, which encompass planning, requirements analysis, design, implementation, testing, and release. A key strength of the standard is its flexibility in this regard, as it does not prescribe a specific software development model, thereby accommodating a wide range of methodologies, including agile and other modern approaches. The standard's purview extends beyond the initial development phase to encompass the entire lifecycle of the software, with a dedicated focus on **software maintenance**. This includes processes for managing changes, resolving problems, and ensuring the ongoing safety and effectiveness of the software after it has been released to the market. To ensure the integrity and traceability of the software and its associated documentation, the standard mandates a systematic approach to **configuration management**. This involves the implementation of processes for identifying, controlling, and tracking changes to the software and its components. Finally, the standard places a strong emphasis on **problem resolution**, requiring a formal process for reporting, investigating, and resolving software problems in a timely and effective manner.

## 3. Key Practices

IEC 62304 outlines a series of key practices that are essential for achieving compliance with the standard. These practices are designed to be adaptable to a variety of software development models, including agile and other modern methodologies. The standard mandates a structured approach to **software development planning**, which involves the creation of a comprehensive plan that defines the scope of the development effort, the chosen lifecycle model, and the specific tasks to be performed. A critical practice is **software requirements analysis**, which entails the meticulous definition and documentation of the software's functional and non-functional requirements, with a particular emphasis on safety and security. The standard also requires a two-tiered approach to design, with a high-level **software architectural design** that establishes the overall structure of the software and a more granular **software detailed design** that elaborates on the specific design of the software components. The implementation phase is governed by the practice of **software unit implementation and verification**, which involves the coding of the software units and the verification that they conform to the detailed design specifications. The standard also emphasizes the importance of a systematic approach to testing, with practices for **software integration and integration testing** to ensure that the software units work together as intended, and **software system testing** to verify that the complete software system meets all the specified requirements. Finally, the standard requires a controlled **software release** process to ensure that the software is released for use in a safe and effective manner.

## 4. Application Context

The application context of IEC 62304 is broad and encompassing, extending to all software that is intended for use in a medical device, irrespective of its safety classification. This includes both software that is an integral part of a physical medical device, often referred to as 'Software in a Medical Device' (SiMD), and standalone software that is itself considered a medical device, known as 'Software as a Medical Device' (SaMD). The standard is designed to be applied within the overarching framework of a quality management system (QMS), and it is most effective when it is integrated with a QMS that is compliant with ISO 13485, the international standard for medical device quality management systems. This integration ensures that the software development and maintenance processes are aligned with the organization's overall quality objectives. Furthermore, the standard is not intended to be a standalone document for risk management. Instead, it is designed to be used in close conjunction with the risk management process outlined in ISO 14971, the international standard for the application of risk management to medical devices. This symbiotic relationship between the three standards—IEC 62304, ISO 13485, and ISO 14971—creates a robust and comprehensive framework for the development of safe and effective medical device software.

## 5. Implementation

The implementation of IEC 62304 is a strategic undertaking that requires the seamless integration of its processes and requirements into the fabric of an organization's software development lifecycle. The journey towards compliance begins with a critical first step: the determination of the software's safety classification. This classification, which is based on the potential for the software to cause harm, is a pivotal decision that will dictate the level of rigor and documentation required throughout the development and maintenance processes. The implementation of the standard demands a disciplined and systematic approach to software engineering, with a relentless focus on documentation and traceability. Every decision, every action, and every outcome must be meticulously documented to create a clear and auditable trail. The standard also provides a framework for managing the use of 'Software of Unknown Provenance' (SOUP), which refers to software components that were not developed with the same level of rigor as the medical device software. The use of SOUP is not prohibited, but it is subject to a stringent set of requirements, including a thorough risk analysis and a compelling justification for its inclusion in the medical device software.

## 6. Evidence & Impact

The impact of IEC 62304 on the medical device industry has been profound and far-reaching. The standard has played a pivotal role in enhancing the safety and reliability of medical device software, providing a common language and a shared framework for manufacturers, regulators, and other stakeholders. The adoption of the standard has led to a more disciplined and systematic approach to software engineering, resulting in a tangible reduction in software-related adverse events. The standard's emphasis on risk management has been particularly impactful, forcing manufacturers to proactively identify and mitigate potential hazards throughout the software lifecycle. The infamous case of the Therac-25 radiation therapy machine, in which a series of software errors led to the deaths of several patients, stands as a stark and enduring reminder of the critical importance of a rigorous and systematic approach to medical device software development. The Therac-25 tragedy, which was caused by a combination of programming errors, inadequate testing, and a lack of a fail-safe design, was a watershed moment for the medical device industry, and it was a key catalyst for the development of standards such as IEC 62304. While the standard is not a panacea and cannot eliminate all software-related risks, its widespread adoption has undoubtedly made a significant contribution to the safety of medical devices and the protection of patients.

## 7. Cognitive Era Considerations

The advent of the cognitive era, characterized by the proliferation of artificial intelligence (AI) and machine learning (ML), presents both unprecedented opportunities and formidable challenges for the medical device industry. The integration of AI/ML algorithms into medical devices has the potential to revolutionize healthcare, enabling more accurate diagnoses, personalized treatments, and improved patient outcomes. However, the unique characteristics of these technologies also pose significant challenges to the established regulatory frameworks, including IEC 62304.

The non-deterministic and adaptive nature of many AI/ML algorithms, particularly those based on deep learning, makes it difficult to apply the traditional verification and validation methods that are the bedrock of IEC 62304. The “black box” problem, in which the internal workings of an algorithm are opaque even to its developers, makes it challenging to provide the level of transparency and traceability that is required by the standard. The ability of these algorithms to learn and adapt over time also raises new questions about how to ensure their ongoing safety and effectiveness. The traditional approach of “freezing” the software design after it has been validated is not always feasible or desirable for AI/ML-based medical devices, which may need to be continuously updated to maintain their performance.

The industry is actively engaged in a multifaceted effort to address these challenges. A key focus is the development of new guidance and standards that are specifically tailored to the unique characteristics of AI/ML-based medical software. The AAMI TIR45, which provides guidance on the use of agile practices in the development of medical device software, is a step in the right direction, but more specific guidance on AI/ML is needed. Other potential solutions that are being explored include the use of new testing and validation techniques, such as the use of large-scale clinical data sets to validate the performance of AI/ML algorithms, and the development of more robust post-market surveillance systems to monitor the performance of these devices after they have been deployed.

The application of IEC 62304 to AI/ML-based medical software is a rapidly evolving area that will require ongoing attention and adaptation from all stakeholders, including manufacturers, regulators, and healthcare providers. The ethical considerations of using AI/ML in medical devices, such as the potential for bias in the algorithms and the need to ensure that the benefits of these technologies are shared equitably, will also need to be carefully considered. As the cognitive era continues to unfold, the challenge will be to strike the right balance between fostering innovation and ensuring the safety and effectiveness of medical device software.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
IEC 62304 primarily defines the responsibilities of the medical device manufacturer, focusing on the processes required to ensure software safety and effectiveness. While this indirectly serves the interests of patients and healthcare providers by minimizing harm, it does not explicitly define a distributed architecture of Rights and Responsibilities for all stakeholders. The framework is producer-centric, positioning other stakeholders as passive recipients of the technology rather than active participants in its governance and value creation.

**2. Value Creation Capability:**
The pattern's core focus is on creating safety and reliability, which are crucial forms of resilience value in the healthcare domain. By providing a framework for regulatory compliance, it enables economic value creation for manufacturers. However, its scope of value creation is narrow, primarily centered on mitigating risks and preventing negative outcomes rather than proactively fostering a wider spectrum of collective value, such as social, ecological, or knowledge value beyond process documentation.

**3. Resilience & Adaptability:**
The standard promotes system resilience by mandating rigorous risk management, change control, and problem resolution processes. This structured approach helps maintain software coherence and safety under stress. However, as noted in the pattern's "Cognitive Era Considerations," its rigid, process-heavy nature presents challenges for adapting to rapidly evolving, non-deterministic technologies like AI and machine learning, potentially hindering innovation and adaptability.

**4. Ownership Architecture:**
Ownership within the IEC 62304 framework is implicitly tied to the manufacturer, who holds the responsibility for the software's safety and maintenance. It does not conceptualize ownership as a distributed set of Rights and Responsibilities shared among various stakeholders. The model is one of proprietary control, not of a shared resource managed for collective benefit.

**5. Design for Autonomy:**
While the standard can be applied to software in distributed systems, its high coordination overhead and extensive documentation requirements are not inherently aligned with the principles of low-friction autonomy. The challenges in applying this process-oriented standard to adaptive and non-deterministic AI/ML systems highlight a significant gap. It is not designed for a world of autonomous agents or decentralized autonomous organizations (DAOs).

**6. Composability & Interoperability:**
The pattern demonstrates strong composability and interoperability by design. It is explicitly intended to integrate with other key standards like ISO 13485 (Quality Management) and ISO 14971 (Risk Management). Its framework for managing 'Software of Unknown Provenance' (SOUP) also provides a clear mechanism for composing systems from third-party components, enabling the construction of larger, more complex value-creation systems.

**7. Fractal Value Creation:**
The risk-based, process-driven logic of IEC 62304 can be applied at multiple scales. The principles of safety classification, requirements analysis, and verification can be implemented from the level of a single software unit up to a complex, integrated system of systems. This allows the core value-creation logic of ensuring safety and reliability to be replicated fractally throughout a product's architecture.

**Overall Score: 2 (Partial Enabler)**

**Rationale:**
IEC 62304 is a critical standard that provides a partial framework for value creation by focusing intensely on safety and risk mitigation, which are forms of resilience value. However, it is fundamentally a legacy, producer-centric pattern that falls short of a true Commons architecture. Its major gaps in stakeholder participation, distributed ownership, and adaptability to autonomous systems limit its alignment with the v2.0 framework, making it a partial enabler that requires significant adaptation for a commons-based approach.

**Opportunities for Improvement:**
- Evolve the stakeholder model to formally include the Rights and Responsibilities of patients, clinicians, and healthcare systems in the governance of medical software.
- Expand the framework to support the lifecycle of adaptive, AI/ML-driven systems, fostering innovation while ensuring safety through new validation and monitoring paradigms.
- Introduce concepts of data and knowledge commons, enabling the collective use of health data for public good while protecting patient privacy and ownership.

## 9. Resources & References

[1] IEC 62304:2006, Medical device software – Software life cycle processes. International Electrotechnical Commission.

[2] Wikipedia. IEC 62304. [https://en.wikipedia.org/wiki/IEC_62304](https://en.wikipedia.org/wiki/IEC_62304)

[3] Kaestner, C. (2024). An illustrated guide to medical device software development and IEC 62304. Medical Device HQ. [https://medicaldevicehq.com/articles/the-illustrated-guide-to-medical-device-software-development-and-iec-62304/](https://medicaldevicehq.com/articles/the-illustrated-guide-to-medical-device-software-development-and-iec-62304/)

[4] Pavlović, A. (2025). Ultimate guide to the IEC 62304 standard. Qualio. [https://www.qualio.com/blog/iec-62304](https://www.qualio.com/blog/iec-62304)

[5] Ketryx. (2024). A Comprehensive Guide to IEC 62304: Navigating the Standard for Medical Device Software. [https://www.ketryx.com/blog/a-comprehensive-guide-to-iec-62304-navigating-the-standard-for-medical-device-software](https://www.ketryx.com/blog/a-comprehensive-guide-to-iec-62304-navigating-the-standard-for-medical-device-software)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/context-specific/iec-62304-medical-device-software/](https://commons-os.github.io/patterns/context-specific/iec-62304-medical-device-software/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/iec-62304-medical-device-software.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_context-specific/iec-62304-medical-device-software.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
