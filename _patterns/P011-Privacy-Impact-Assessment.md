_# Pattern: Privacy Impact Assessment (PIA)

## 1. Pattern Name and Number

**P011: Privacy Impact Assessment (PIA)**

## 2. Problem

New projects, products, or features are often developed with a primary focus on functionality and business goals, while privacy considerations are overlooked or treated as an afterthought. This can lead to building systems that are not compliant with privacy regulations, that erode user trust, and that require costly re-engineering after the fact to fix privacy flaws.

## 3. Context

You are planning a new project or a significant change to an existing system that will involve the collection, use, or storage of personal data. You need a systematic process to identify and mitigate privacy risks *before* the project begins, rather than after it is built.

## 4. Solution

**Conduct a Privacy Impact Assessment (PIA), a systematic process for evaluating the potential effects of a project on individual privacy.** A PIA is a risk management tool that helps an organization make conscious and documented decisions about how to manage the privacy risks created by a new initiative.

The process typically involves:
1.  **Initiation**: Determine if a PIA is required for the project.
2.  **Data Flow Analysis**: Map out how personal data will be collected, used, stored, shared, and retained by the system.
3.  **Risk Identification**: Identify and assess potential privacy risks and their potential impact on individuals.
4.  **Mitigation**: Identify and evaluate solutions to mitigate the identified privacy risks. This often involves implementing other privacy patterns.
5.  **Reporting**: Document the entire process in a formal PIA report, which outlines the project, the risks, and the mitigation measures that will be taken.
6.  **Review and Approval**: The report is reviewed by stakeholders, including legal and privacy teams, before the project is approved.

## 5. Rationale

A PIA shifts privacy from being an afterthought to a core part of the design process. It:
- **Enables Privacy by Design**: It is the primary process for implementing Privacy by Design (P002).
- **Reduces Risk and Cost**: Identifies and addresses privacy issues early, when they are cheapest and easiest to fix.
- **Ensures Compliance**: It is a mandatory requirement under regulations like GDPR for many types of data processing.
- **Improves Decision Making**: Provides a structured framework for making informed decisions about data handling practices.

## 6. Consequences

- **Positive**:
    - Proactive identification and mitigation of privacy risks.
    - Reduced likelihood of costly redesigns and regulatory fines.
    - Increased trust from stakeholders and users.
- **Negative**:
    - Can be a bureaucratic and time-consuming process, especially for large projects.
    - Requires expertise in privacy principles and regulations to be effective.
    - The quality of the PIA depends on the accuracy and completeness of the information provided by the project team.

## 7. Known Uses

- **GDPR**: Article 35 of the GDPR mandates a Data Protection Impact Assessment (DPIA), a specific type of PIA, for processing that is likely to result in a high risk to the rights and freedoms of individuals.
- **Government Agencies**: Many governments around the world require PIAs for new government programs and systems that handle personal information.
- **Large Corporations**: Mature organizations have integrated the PIA process into their standard project management and system development lifecycle.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of building responsible and trustworthy systems from the outset.               |
| **2. Governance**       | 5           | A cornerstone of privacy governance and risk management.                                              |
| **3. Economy**          | 4           | Avoids the significant economic costs of non-compliance and post-deployment remediation.              |
| **4. Technology**       | 3           | Primarily a process pattern, but it drives the selection and implementation of privacy technologies.  |
| **5. Operations**       | 4           | Requires integrating a formal review process into project management and operations.                  |
| **6. Culture**          | 5           | Fosters a culture where privacy is a shared responsibility and a key design consideration.            |
| **7. Resilience**       | 4           | Builds regulatory and social resilience by ensuring systems are designed in a compliant and ethical way. |
| **Overall Score**       | **4.3**     | A fundamental governance pattern for any organization that regularly builds new products or systems.   |
