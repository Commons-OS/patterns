---
id: pat_01kg50240vft1bjmxtcexfazdw
page_url: https://commons-os.github.io/patterns/implementation/delphi-method/
github_url: https://github.com/commons-os/patterns/blob/main/_implementation/delphi-method.md
slug: delphi-method
title: Delphi Method
aliases: [Delphi Technique, Estimate-Talk-Estimate]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: implementation
  domain: operations
  category: [methodology]
  era: [industrial]
  origin: [RAND Corporation]
  status: draft
  commons_alignment: 3
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

# 1. Overview

The Delphi method, also known as the Delphi technique, is a structured communication method, originally developed as a systematic, interactive forecasting method that relies on a panel of experts. The method is designed to achieve a convergence of opinion on a specific topic. The Delphi method is based on the principle that forecasts (or decisions) from a structured group of individuals are more accurate than those from unstructured groups. The experts answer questionnaires in two or more rounds. After each round, a facilitator provides an anonymized summary of the experts’ forecasts from the previous round as well as the reasons they provided for their judgments. Thus, experts are encouraged to revise their earlier answers in light of the replies of other members of their panel. It is believed that during this process the range of the answers will decrease and the group will converge towards the “correct” answer. Finally, the process is stopped after a predefined stopping criterion (e.g., number of rounds, achievement of consensus, stability of results), and the mean or median scores of the final rounds determine the results. The name "Delphi" derives from the Oracle of Delphi, a priestess at the Temple of Apollo in ancient Greece who was famous for her prophecies. The Delphi method was developed at the beginning of the Cold War by Olaf Helmer, Norman Dalkey, and Nicholas Rescher at the RAND Corporation to forecast the impact of technology on warfare. It has since been used in a wide range of fields, including business, government, education, and healthcare.


# 2. Core Principles

The Delphi method is founded on a set of core principles that differentiate it from other group decision-making techniques. These principles are designed to maximize the benefits of expert input while minimizing the pitfalls of group dynamics. The primary principles are anonymity, iteration with controlled feedback, and statistical group response.

**Anonymity:** Participants in a Delphi study remain anonymous to one another throughout the process. This is a crucial element that helps to prevent the influence of dominant personalities, authority figures, or group pressure on the opinions of the expert panel. Anonymity encourages participants to express their true opinions freely and to change their minds without fear of judgment. This allows the ideas to be evaluated on their merits, rather than on the reputation of the person who proposed them.

**Iteration with Controlled Feedback:** The Delphi process is iterative, typically involving multiple rounds of questionnaires. After each round, a facilitator provides a summary of the group's responses, including the range of opinions and the reasons for them. This controlled feedback allows the experts to consider the views of their peers and to revise their own opinions if they see fit. The iterative nature of the process allows for a gradual convergence of opinion as the experts learn from one another.

**Statistical Group Response:** The Delphi method relies on a statistical representation of the group's responses. Rather than seeking a simple majority vote, the method uses statistical measures such as the median or mean to represent the collective judgment of the expert panel. This approach ensures that the final outcome is a true reflection of the group's consensus, rather than the result of a few dominant voices. The use of statistical analysis also allows for a more nuanced understanding of the level of agreement or disagreement among the experts.


# 3. Key Practices

The successful implementation of the Delphi method relies on a set of key practices that guide the process from start to finish. These practices ensure the rigor and validity of the study's findings.

**Selection of Experts:** The quality of the output from a Delphi study is directly dependent on the expertise of the participants. Therefore, the careful selection of experts is a critical first step. Experts should be chosen based on their knowledge, experience, and ability to contribute to the topic under investigation. The panel should be diverse enough to represent a range of perspectives, but small enough to be manageable.

**The Role of the Facilitator:** The facilitator plays a central role in the Delphi process. They are responsible for managing the entire process, from selecting the experts to designing the questionnaires, analyzing the responses, and providing feedback to the panel. The facilitator must be neutral and objective, ensuring that their own biases do not influence the outcome of the study.

**Questionnaire Design:** The questionnaires are the primary tool for collecting data in a Delphi study. They must be carefully designed to elicit the desired information from the experts. The questions should be clear, concise, and unambiguous. The first round questionnaire is often open-ended, allowing the experts to identify the key issues and concerns. Subsequent rounds are more structured, asking the experts to rate or rank the issues identified in the first round.

**The Iterative Process:** The iterative nature of the Delphi method is one of its defining features. The process of multiple rounds of questionnaires and feedback allows for a gradual refinement of the group's opinion. The number of rounds can vary depending on the topic and the level of consensus among the experts. The process is typically stopped when a predefined level of consensus is reached, or when the responses become stable.

**The Feedback Mechanism:** The feedback provided to the experts after each round is a critical component of the Delphi process. The feedback should be presented in a way that allows the experts to see the range of opinions and the reasons for them. This can include statistical summaries of the group's responses, as well as a qualitative summary of the comments and arguments. The feedback should be anonymous to prevent the influence of dominant personalities.

**The Final Report:** The final report of a Delphi study should provide a comprehensive summary of the process and the findings. It should include a description of the expert panel, the questionnaires used, the feedback provided, and the final consensus. The report should also include a discussion of the implications of the findings and any limitations of the study.


# 4. Application Context

The Delphi method is a versatile tool that can be applied in a wide range of contexts where expert opinion is needed to inform decision-making, forecasting, or policy development. Its structured approach makes it particularly useful in situations where there is a high degree of uncertainty or a lack of historical data. The method is also well-suited for complex problems that require a multidisciplinary approach.

**Forecasting:** The Delphi method was originally developed for forecasting, and it remains a widely used tool in this area. It is particularly useful for long-range forecasting, where historical data is of limited value. The method has been used to forecast trends in a variety of fields, including technology, business, and social change.

**Policy Making:** The Delphi method is increasingly being used in the policy-making process. It can be used to identify policy options, to assess the potential impacts of different policies, and to build consensus among stakeholders. The method is particularly useful in controversial policy areas, where it can help to depoliticize the debate and to focus on the evidence.

**Healthcare:** The Delphi method has been widely used in the healthcare sector. It has been used to develop clinical guidelines, to identify research priorities, and to assess the quality of care. The method is particularly useful in areas where there is a lack of evidence from randomized controlled trials.

**Business and Management:** The Delphi method is a valuable tool for business and management. It can be used for strategic planning, market research, and new product development. The method can help to identify emerging trends, to assess the potential of new technologies, and to build consensus among a management team.

**Education:** The Delphi method has been used in the field of education to identify future trends, to develop curriculum, and to set standards for student achievement. The method can help to ensure that the education system is responsive to the changing needs of society.


# 5. Implementation

Implementing a Delphi study requires careful planning and execution. The following steps provide a general guide to conducting a Delphi study, from the initial planning stages to the final report.

**Step 1: Define the Problem:** The first step in any Delphi study is to clearly define the problem or issue to be addressed. This includes defining the scope of the study, the specific questions to be answered, and the desired outcomes. A clear problem definition is essential for guiding the entire process and for ensuring that the results are relevant and useful.

**Step 2: Select the Experts:** As noted in the Key Practices section, the selection of experts is a critical step. The facilitator should identify and recruit a panel of experts with the appropriate knowledge and experience. The size of the panel can vary depending on the topic, but it is typically between 15 and 30 participants.

**Step 3: Develop the First Round Questionnaire:** The first round questionnaire is typically open-ended, designed to elicit a broad range of ideas and opinions from the expert panel. The questions should be carefully crafted to be clear, concise, and unbiased. The questionnaire should be pilot-tested before it is sent to the expert panel.

**Step 4: Administer the First Round Questionnaire:** The first round questionnaire is sent to the expert panel, along with instructions for completing it. The participants are typically given a few weeks to respond. The facilitator should monitor the response rate and send reminders as needed.

**Step 5: Analyze the First Round Responses:** The facilitator analyzes the responses from the first round questionnaire. The goal is to identify the key themes, ideas, and areas of agreement and disagreement. The facilitator then develops a structured questionnaire for the second round, based on the responses from the first round.

**Step 6: Develop and Administer the Second Round Questionnaire:** The second round questionnaire is more structured than the first. It typically asks the experts to rate or rank the items identified in the first round. The questionnaire is sent to the expert panel, along with a summary of the results from the first round. The participants are asked to review the summary and to revise their original opinions if they see fit.

**Step 7: Analyze the Second Round Responses and Subsequent Rounds:** The facilitator analyzes the responses from the second round questionnaire. If a sufficient level of consensus has been reached, the process can be stopped. If not, the process is repeated with a third round questionnaire. The process of iteration and feedback continues until a predefined level of consensus is reached, or until the responses become stable.

**Step 8: Prepare the Final Report:** Once the Delphi study is complete, the facilitator prepares a final report. The report should provide a comprehensive summary of the process and the findings. It should include a description of the expert panel, the questionnaires used, the feedback provided, and the final consensus. The report should also include a discussion of the implications of the findings and any limitations of the study.


# 6. Evidence & Impact

The Delphi method has a long and successful track record of application in a wide range of fields. Its effectiveness is supported by a large body of evidence from both academic research and practical application. The method's impact can be seen in its influence on policy-making, its contribution to the development of best practices, and its role in fostering innovation.

**Evidence of Effectiveness:** The effectiveness of the Delphi method has been demonstrated in numerous studies. Research has shown that the method can produce more accurate forecasts than traditional forecasting techniques, such as trend extrapolation and unstructured group discussions. The method's success is attributed to its ability to harness the collective intelligence of a group of experts, while at the same time mitigating the negative effects of group dynamics. The iterative nature of the process, with its controlled feedback and anonymity, allows for a gradual convergence of opinion towards a more accurate and reliable consensus.

**Impact on Policy-Making:** The Delphi method has had a significant impact on policy-making at all levels of government. It has been used to inform policy decisions on a wide range of issues, from healthcare and environmental protection to national security and economic development. The method's ability to build consensus among a diverse group of stakeholders makes it a valuable tool for navigating complex and controversial policy debates. By providing a structured and transparent process for gathering expert opinion, the Delphi method can help to ensure that policy decisions are based on the best available evidence.

**Contribution to Best Practices:** The Delphi method has been instrumental in the development of best practices in a variety of professions. It has been used to develop clinical guidelines for doctors, to establish standards for educational testing, and to create best practice models for project management. The method's ability to synthesize the knowledge and experience of a group of experts makes it an ideal tool for identifying and codifying best practices. The resulting guidelines and standards can help to improve the quality and consistency of professional practice.

**Fostering Innovation:** The Delphi method can also be a powerful tool for fostering innovation. By bringing together a diverse group of experts, the method can help to generate new ideas and to identify emerging trends. The method's structured and iterative process can help to refine and develop these ideas into practical and actionable proposals. The Delphi method has been used to identify new product opportunities, to develop new business models, and to explore the potential of new technologies.


# 7. Cognitive Era Considerations

The Cognitive Era, characterized by the rise of artificial intelligence, big data, and advanced analytics, presents both challenges and opportunities for the Delphi method. While the core principles of the method remain relevant, its application is likely to be transformed by these new technologies. The integration of AI and big data into the Delphi process has the potential to enhance its accuracy, efficiency, and scope.

**AI-Powered Facilitation:** In the Cognitive Era, the role of the human facilitator in a Delphi study may be augmented or even replaced by AI-powered systems. These systems could automate many of the tasks of the facilitator, such as designing questionnaires, analyzing responses, and providing feedback to the expert panel. AI could also be used to identify and recruit experts, to personalize the experience for each participant, and to detect and mitigate bias in the responses.

**Big Data Integration:** The Delphi method has traditionally relied on the qualitative judgments of experts. In the Cognitive Era, these judgments can be supplemented with insights from big data. Experts could be provided with access to large datasets and advanced analytical tools to inform their opinions. This could help to improve the accuracy of their forecasts and to identify trends and patterns that would not be apparent from qualitative data alone.

**Hybrid Approaches:** The Cognitive Era is likely to see the emergence of hybrid approaches that combine the Delphi method with other forecasting techniques, such as prediction markets and agent-based modeling. These hybrid approaches could leverage the strengths of each method to produce more accurate and robust forecasts. For example, the Delphi method could be used to generate the initial inputs for a prediction market, or to validate the results of an agent-based model.

**New Applications:** The Cognitive Era is also likely to open up new applications for the Delphi method. The method could be used to forecast the societal impacts of new technologies, to develop ethical guidelines for the use of AI, and to build consensus on how to address global challenges such as climate change and pandemics. The Delphi method's ability to bring together a diverse group of experts and to facilitate a structured and informed debate makes it an ideal tool for tackling these complex and multifaceted issues.

**Challenges and Risks:** The integration of AI and big data into the Delphi process also presents a number of challenges and risks. There is a risk that the use of AI could introduce new forms of bias into the process. There is also a risk that the reliance on big data could lead to a neglect of qualitative insights and expert judgment. It is therefore important to ensure that the integration of these new technologies is guided by a clear understanding of the strengths and weaknesses of the Delphi method, and by a commitment to its core principles of anonymity, iteration, and statistical group response.


# 8. Commons Alignment Assessment

The Commons Alignment Assessment evaluates the Delphi method's compatibility with the principles of a commons-based approach. The assessment considers seven key dimensions, each rated on a scale of 1 to 5, where 1 indicates low alignment and 5 indicates high alignment. The overall commons alignment score for the Delphi method is 3.

| Dimension | Assessment | Score |
|---|---|---|
| **Openness & Transparency** | The Delphi method can be implemented with a high degree of transparency, with the final report and the process itself being made public. However, the anonymity of the participants, while a core strength of the method, can also be seen as a lack of openness. | 3 |
| **Inclusivity & Diversity** | The method's effectiveness is highly dependent on the diversity of the expert panel. A well-designed Delphi study will be highly inclusive, seeking out a wide range of perspectives. However, the reliance on "experts" can also be a barrier to inclusivity, potentially excluding valuable knowledge from non-experts. | 3 |
| **Decentralization & Federation** | The Delphi method is a decentralized process, with the participants distributed geographically and working independently. However, the process is coordinated by a central facilitator, which introduces a degree of centralization. | 3 |
| **Subsidiarity & Autonomy** | The method respects the autonomy of the participants, allowing them to express their opinions freely and to change their minds without pressure. However, the structured nature of the process and the role of the facilitator can limit the autonomy of the participants to some extent. | 3 |
| **Trust & Reputation** | The anonymity of the process means that trust is placed in the method itself, rather than in the reputation of the participants. This can be a strength, as it allows ideas to be evaluated on their merits. However, it can also be a weakness, as it can be difficult to assess the credibility of the expert panel. | 3 |
| **Resource Efficiency & Sustainability** | The Delphi method can be a resource-efficient way to gather expert opinion, as it does not require face-to-face meetings. The use of online tools can further reduce the cost and environmental impact of the process. | 4 |
| **Governance & Accountability** | The Delphi method provides a structured and transparent process for decision-making, which can enhance accountability. The final report provides a clear record of the process and the findings, which can be used to hold decision-makers to account. | 3 |


# 9. Resources & References

1.  [Delphi method - Wikipedia](https://en.wikipedia.org/wiki/Delphi_method)
2.  [Delphi Method - RAND Corporation](https://www.rand.org/topics/delphi-method.html)
3.  [The Delphi Method: An Introduction](https://link.springer.com/chapter/10.1007/978-3-658-38862-1_1)
4.  [Utilizing and adapting the Delphi method for use in qualitative research](https://journals.sagepub.com/doi/abs/10.1177/1609406915621381)
5.  [A Practical Guide to Applying the Delphi Technique in Treatment Adaptation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8384080/)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/implementation/delphi-method/](https://commons-os.github.io/patterns/implementation/delphi-method/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_implementation/delphi-method.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_implementation/delphi-method.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
