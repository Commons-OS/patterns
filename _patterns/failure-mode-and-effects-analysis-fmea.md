---
id: pat_01kg5023yqf5racw9n8c613tza
page_url: https://commons-os.github.io/patterns/failure-mode-and-effects-analysis-fmea/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/failure-mode-and-effects-analysis-fmea.md
slug: failure-mode-and-effects-analysis-fmea
title: Failure Mode and Effects Analysis (FMEA)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: technology
  category: [methodology]
  era: [industrial]
  origin: []
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

# Failure Mode and Effects Analysis (FMEA)

## 1. Overview

Failure Mode and Effects Analysis (FMEA) is a systematic, proactive method for evaluating a process, product, or service to identify where and how it might fail and to assess the relative impact of different failures. The primary objective of FMEA is to identify potential failure modes, their causes, and their effects on the system's performance. This analysis allows for the prioritization of risks and the implementation of corrective actions to mitigate the most critical issues before they occur. FMEA is a foundational tool in risk management and quality control, widely used across various industries, including manufacturing, aerospace, healthcare, and software development.

The FMEA process is typically conducted by a cross-functional team of experts who have a deep understanding of the process, product, or service being analyzed. The team brainstorms potential failure modes, which are the ways in which a component, subsystem, or process could fail to perform its intended function. For each failure mode, the team identifies the potential effects of the failure, which are the consequences of the failure on the system, the user, or the environment. The team also investigates the potential causes of the failure, which are the design or process weaknesses that could lead to the failure mode.

Once the failure modes, effects, and causes have been identified, the team assesses the risk associated with each failure mode. This is typically done by assigning a numerical rating to three factors: the severity of the failure's effect, the likelihood of the failure's occurrence, and the probability of detecting the failure before it reaches the customer. These three ratings are then multiplied to calculate a Risk Priority Number (RPN). The RPN provides a quantitative measure of the risk associated with each failure mode, allowing the team to prioritize the most critical issues for corrective action.

FMEA is not a one-time analysis but a living document that should be updated throughout the lifecycle of the product, process, or service. As new information becomes available, the FMEA should be reviewed and revised to reflect the current understanding of the risks. This iterative process of analysis and improvement helps to ensure that the system remains reliable and safe over time.

## 2. Core Principles

FMEA is guided by a set of core principles that are essential for its effective implementation. These principles ensure that the analysis is comprehensive, systematic, and focused on proactive risk mitigation.

**Systematic Approach:** FMEA follows a structured and methodical process for identifying and analyzing potential failures. This systematic approach ensures that all aspects of the system are considered and that the analysis is conducted in a consistent and repeatable manner. The process typically involves a series of well-defined steps, from defining the scope of the analysis to implementing and monitoring corrective actions.

**Cross-Functional Collaboration:** FMEA is a team-based activity that brings together individuals with diverse expertise and perspectives. This cross-functional collaboration is crucial for a comprehensive analysis, as it ensures that all potential failure modes are identified and that the analysis is not biased by a single viewpoint. The team typically includes representatives from design, manufacturing, quality, and other relevant departments.

**Proactive Risk Management:** FMEA is a proactive tool that focuses on identifying and mitigating risks before they result in failures. By anticipating potential problems, organizations can take preventive actions to improve the design, process, or service and reduce the likelihood of costly and disruptive failures. This proactive approach is a key differentiator of FMEA from other quality control methods that focus on detecting failures after they have occurred.

**Quantitative Analysis:** FMEA uses a quantitative approach to assess and prioritize risks. The use of the Risk Priority Number (RPN) provides a numerical basis for decision-making, allowing the team to focus its resources on the most critical issues. This quantitative analysis helps to ensure that the corrective actions are targeted and effective.

**Continuous Improvement:** FMEA is not a static analysis but a dynamic process of continuous improvement. The FMEA document should be regularly reviewed and updated to reflect changes in the design, process, or operating conditions. This iterative process of analysis and improvement helps to ensure that the system remains reliable and safe over time.

**Documentation and Traceability:** A key principle of FMEA is the thorough documentation of the analysis process and its results. This documentation provides a record of the identified risks, the implemented corrective actions, and the rationale for the decisions made. This traceability is essential for accountability, knowledge sharing, and future reference.

## 3. Key Practices

## 4. Application Context

## 5. Implementation

## 6. Evidence & Impact

## 7. Cognitive Era Considerations

## 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
FMEA implicitly defines responsibilities for the cross-functional team tasked with performing the analysis and implementing corrective actions. The rights of stakeholders (customers, users, the public) are protected by proactively preventing system failures that could cause harm or loss. However, it does not explicitly architect rights and responsibilities for a broad set of stakeholders like the environment or future generations, focusing primarily on the direct human and organizational users of a system.

**2. Value Creation Capability:**
The primary value created by FMEA is resilience and knowledge value. It enables the collective capability to preserve value by preventing its loss through failure, rather than directly creating new social or ecological value. By identifying systemic weaknesses, it generates a deep understanding of the system, which is a critical form of knowledge value that supports long-term viability.

**3. Resilience & Adaptability:**
This is a core strength of the FMEA pattern. The entire methodology is designed to enhance system resilience by anticipating and mitigating potential failures, thereby helping the system maintain coherence under stress. Because FMEA is a 'living document' meant to be updated as a system evolves, it provides a structured process for adaptation in the face of change.

**4. Ownership Architecture:**
FMEA does not address ownership architecture in the sense of defining rights and responsibilities over a shared resource. It is a risk management process, not an ownership model. It assigns responsibility for corrective actions to specific individuals or teams, but this is operational, not a form of equity or stewardship over a commons.

**5. Design for Autonomy:**
As a highly deliberative and human-centric process, FMEA has a high coordination overhead and is not inherently designed for autonomous systems. However, its outputs can be used to program and train autonomous systems, such as AI agents or DAOs, to detect and respond to the identified failure modes. The pattern is therefore compatible with and can inform the design of autonomous systems, even if it is not autonomous itself.

**6. Composability & Interoperability:**
FMEA is highly composable and interoperable. As a standardized methodology, it can be integrated with a wide range of other quality management, design, and operational patterns (e.g., Six Sigma, ISO 9001). Its modular nature allows it to be applied to individual components, which can then be composed to analyze the risks of a larger, more complex system.

**7. Fractal Value Creation:**
The logic of FMEA is inherently fractal, as the value-creation logic of identifying and mitigating failure can be applied at multiple scales. It is effective for analyzing a single software function, a complex physical product, a multi-step manufacturing process, or even an entire organization's service delivery workflow. This scalability allows the core principle of resilience through foresight to be embedded throughout a system's architecture.

**Overall Score: 3 (Transitional)**

**Rationale:**
FMEA is a powerful tool for creating resilience and knowledge value, which are essential for any commons. Its strengths in adaptability, composability, and fractal application make it a vital pattern. However, its primary focus is on preventing value loss rather than enabling new forms of collective value creation. It also lacks a native concept of stakeholder or ownership architecture beyond the immediate operational context. To become a true value creation enabler, it needs to be adapted to a broader definition of 'failure' that includes negative social and ecological externalities, not just technical or process faults.

**Opportunities for Improvement:**
- Integrate a broader stakeholder analysis into the FMEA process, explicitly considering impacts on the environment, community, and future generations when assessing the 'severity' of a failure.
- Expand the definition of 'failure mode' to include scenarios that degrade social, ecological, or knowledge value, not just technical non-performance.
- Develop a 'Commons FMEA' variant that uses the 7 Pillars as categories for brainstorming potential failures, linking risk mitigation directly to the health of the value creation architecture.

## 9. Resources & References

*   [https://asq.org/quality-resources/fmea](https://asq.org/quality-resources/fmea)
*   [https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis](https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis)
*   [https://quality-one.com/fmea/](https://quality-one.com/fmea/)
*   [https://www.scrut.io/post/guide-to-an-fmea-analysis](https://www.scrut.io/post/guide-to-an-fmea-analysis)
*   [https://fmea-training.com/10-steps-process-failure-mode-and-effects-analysis/](https://fmea-training.com/10-steps-process-failure-mode-and-effects-analysis/)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/failure-mode-and-effects-analysis-fmea/](https://commons-os.github.io/patterns/domain/failure-mode-and-effects-analysis-fmea/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/failure-mode-and-effects-analysis-fmea.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/failure-mode-and-effects-analysis-fmea.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
