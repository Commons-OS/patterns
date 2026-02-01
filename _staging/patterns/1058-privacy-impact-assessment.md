---
id: pat_019c19b234d877f3a16a16eed6
page_url: https://commons-os.github.io/patterns/1058-privacy-impact-assessment/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/1058-privacy-impact-assessment.md
slug: 1058-privacy-impact-assessment
title: "Privacy Impact Assessment"
aliases: []
version: "1.0"
created: "2026-02-01T14:53:55Z"
modified: "2026-02-01T14:53:55Z"

tags:
  universality: universal
  domain: privacy
  category: [practice]
  era: [cognitive]
  origin: [Commons OS]
  status: draft
  commons_alignment: 3

commons_domain: security

generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []

contributors: [commons-os]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

A Privacy Risk Assessment (PRA) is a systematic process for identifying, analyzing, and mitigating privacy risks to individuals arising from the processing of their personal data. This pattern addresses the need for proactive management of privacy threats and vulnerabilities in systems and data flows, ensuring that the collection, use, and sharing of personally identifiable information (PII) comply with legal and ethical standards. By conducting a PRA, an organization gains a comprehensive understanding of its data processing activities and their privacy implications, enabling informed decision-making and the implementation of appropriate controls to protect individuals' privacy. This is crucial for building and maintaining trust with stakeholders and demonstrating responsible data stewardship.

The concept of privacy risk assessment has evolved with the development of data protection laws and the digitization of personal information. Early forms of privacy assessments emerged in the late 20th century, but the practice was formalized with regulatory frameworks like the GDPR, which mandates Data Protection Impact Assessments (DPIAs) for high-risk processing, and the NIST's Privacy Risk Assessment Methodology (PRAM). These frameworks have established a global standard for privacy risk management, emphasizing a proactive and preventative approach. For organizations and commons-based communities, adopting this pattern is essential for ensuring compliance, mitigating risks of data breaches and reputational damage, and fostering a culture of privacy. In commons, where shared resources and collaboration are key, a robust PRA process is critical for maintaining the integrity and sustainability of the community by ensuring that participants' personal data is handled with care and respect.

### 2. Core Principles

1.  **Proactive not Reactive; Preventative not Remedial:** This principle emphasizes anticipating and preventing privacy risks before they occur by embedding privacy considerations into the design of systems and processes from the outset.

2.  **Privacy as the Default Setting:** Systems and services should be designed to protect personal data automatically, with the most privacy-protective settings as the default and data sharing as opt-in.

3.  **Privacy Embedded into Design:** Privacy should be an integral component of the system's design and functionality, not an afterthought, with privacy controls integrated directly into the architecture.

4.  **Full Functionality – Positive-Sum, not Zero-Sum:** This principle seeks to accommodate all legitimate interests in a “win-win” manner, rejecting the false dichotomy between privacy and other interests like security or functionality.

5.  **End-to-End Security – Lifecycle Protection:** Strong security measures are essential for protecting privacy throughout the entire data lifecycle, from collection to destruction, safeguarding data against unauthorized access.

6.  **Visibility and Transparency – Keep it Open:** Organizations should be transparent about their data processing practices, providing clear information to individuals about how their data is used and allowing them to verify that it is handled appropriately.

### 3. Key Practices

1.  **Establish a Data Inventory:** Create a comprehensive inventory of all personal data the organization collects, processes, and stores, detailing the types of data, purposes of processing, data locations, and retention periods.

2.  **Map Data Flows:** Map the flow of personal data throughout the organization and with third parties to visualize the entire lifecycle of data and identify all points where data is handled.

3.  **Identify Privacy Threats and Vulnerabilities:** Systematically identify potential privacy threats and vulnerabilities through methods like threat modeling workshops, vulnerability scanning, and reviewing past incidents.

4.  **Assess Risk Likelihood and Impact:** For each identified threat, assess the likelihood of it occurring and the potential impact on individuals, using a risk matrix to score and prioritize risks.

5.  **Implement Risk Mitigation Measures:** Implement appropriate mitigation measures to reduce or eliminate the identified risks, such as technical controls, organizational policies, and employee training.

6.  **Document the Assessment Process and Findings:** Thoroughly document the entire PRA process, including the findings, risk levels, and mitigation measures, to serve as a record of due diligence and a baseline for future assessments.

7.  **Monitor and Review on an Ongoing Basis:** Continuously monitor the effectiveness of mitigation measures and review risk assessments regularly, especially when there are changes in data processing activities.

### 4. Implementation

Implementing a Privacy Risk Assessment (PRA) requires a structured approach. First, define the scope of the assessment, identifying the specific systems, processes, or projects to be evaluated. Assemble a dedicated team with representatives from legal, IT, and business units to lead the process. This team will conduct the data inventory and data flow mapping exercises, which are foundational to the entire PRA.

With a clear understanding of the data landscape, the team can proceed to the risk assessment phase. This involves brainstorming potential privacy threats and vulnerabilities, analyzing their likelihood and potential impact, and prioritizing them using a risk matrix. Based on this analysis, a risk mitigation plan is developed. Common tools and frameworks that can support this process include the NIST PRAM and ISO/IEC 29134:2017. Key considerations include ensuring objectivity, involving all relevant stakeholders, and communicating findings effectively.

To measure the success of the PRA implementation, organizations should track key metrics such as the number of mitigated risks, the reduction in the overall privacy risk score, and the number of privacy incidents. Ultimately, the success of a PRA is demonstrated by its ability to embed privacy considerations into the organization's culture and operations, leading to a more trustworthy and resilient approach to data management.

### 5. 7 Pillars Assessment
| Pillar | Score (1-5) | Rationale |
|---|---|---|
| Purpose | 4 | The purpose of a PRA is clear and vital: to systematically identify and mitigate privacy risks to individuals, which is fundamental to ethical data stewardship and building trust. |
| Governance | 5 | This pattern is a cornerstone of effective data governance, providing a structured framework for accountability and decision-making and operationalizing privacy principles. |
| Culture | 3 | The success of this pattern is heavily contingent on a supportive organizational culture; a culture that views privacy as a compliance hurdle will see diminished returns. |
| Incentives | 3 | The primary incentives are often extrinsic, such as avoiding fines, but there is a growing recognition of the positive incentive of enhanced customer trust and brand loyalty. |
| Knowledge | 4 | The PRA process is a powerful knowledge-generating activity, creating detailed data inventories and flow maps that deepen the organization's understanding of its data assets. |
| Technology | 4 | Technology is both the subject of the assessment and a key enabler of it; specialized software for data discovery and risk analysis makes the PRA process more efficient. |
| Resilience | 5 | By proactively identifying and addressing vulnerabilities, this pattern significantly enhances an organization's resilience to privacy-related incidents, moving it from a reactive to a preventative posture. |
| **Overall** | **4.0** | **This pattern is a critical component of modern data governance, though its ultimate effectiveness depends on cultural integration.** |

### 6. When to Use

*   When launching new products or services that process personal data.
*   When implementing new technologies like AI or IoT.
*   When undertaking major organizational changes such as mergers or acquisitions.
*   When there are changes to data processing activities.
*   To comply with legal and regulatory requirements like the GDPR.
*   As part of a regular review cycle to keep the privacy posture up-to-date.

### 7. Anti-Patterns & Gotchas

*   **Treating it as a one-time, check-the-box exercise:** Effective privacy management requires ongoing monitoring and regular reassessment.
*   **Scope that is too narrow or poorly defined:** Failing to properly define the scope can lead to significant blind spots.
*   **Lack of stakeholder engagement:** Conducting the assessment in a silo without involving key stakeholders will result in an incomplete picture of privacy risks.
*   **Focusing solely on compliance, not on actual harm:** The ultimate goal is to prevent harm to individuals, not just to meet technical compliance requirements.
*   **Failure to integrate findings into the development lifecycle:** The insights from the PRA must be acted upon and integrated into the organization's processes.
*   **Using generic, off-the-shelf assessments:** The assessment must be tailored to the specific context, data, and risks of the organization.

### 8. References

1.  **NIST Privacy Risk Assessment Methodology (PRAM).** National Institute of Standards and Technology. [https://csrc.nist.gov/projects/privacy-framework/pram](https://csrc.nist.gov/projects/privacy-framework/pram)
2.  **The 7 Foundational Principles of Privacy by Design.** Ann Cavoukian. [https://www.ipc.on.ca/wp-content/uploads/resources/7foundationalprinciples.pdf](https://www.ipc.on.ca/wp-content/uploads/resources/7foundationalprinciples.pdf)
3.  **ISO/IEC 29134:2017 Information technology — Security techniques — Guidelines for privacy impact assessment.** International Organization for Standardization. [https://www.iso.org/standard/62289.html](https://www.iso.org/standard/62289.html)
4.  **Data Protection Impact Assessments (DPIAs).** EU General Data Protection Regulation (GDPR), Article 35. [https://gdpr-info.eu/art-35-gdpr/](https://gdpr-info.eu/art-35-gdpr/)
5.  **LINDDUN Privacy Threat Modeling.** [https://linddun.org/](https://linddun.org/)
