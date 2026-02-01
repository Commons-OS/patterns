---
id: pat_01kg5023xdfjhsd4s6982ysax8
page_url: https://commons-os.github.io/patterns/ai-governance-models/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/ai-governance-models.md
slug: ai-governance-models
title: AI Governance Models
aliases: [AI Ethics Frameworks, Responsible AI Frameworks, AI Control Frameworks]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: governance
  category: [framework, principle]
  era: [digital, cognitive]
  origin: [academic, corporate, governmental]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: ["pat_01kg5023xne3gs3g227jcvch6k", "pat_01kg5023x4easr02ymp7vsz81b", "pat_01kg5023y5fnhb2ej6755c58p1", "pat_01kg50240sfm8re6ep2sz2xmy5", "pat_01kg5023vwe00rptkqr3z6pkd9", "pat_01kg5023y4e708zavzfmvmx4yp", "pat_01kg50240fev1snyp2ytvn21xm", "pat_01kg50240rf3s9mqrqw0pp5mwn", "pat_01kg5023x3f8gtc1a31gws6jj3", "pat_01kg5023y4e708zavzcte3n4dd", "pat_01kg5023xmek8szp5z3c5dc977", "pat_01kg5023y8e9ssb52a5snc91pm", "pat_01kg5023xbed1bnd9kg5m8pqq0", "pat_01kg5023vhev9b6swdrszd75z9", "pat_01kg5023whehgsjwtbrb92n8n3"]
contributors: [higgerix, cloudsters]
sources:
  - https://www.ibm.com/think/topics/ai-governance
  - https://www.ai21.com/knowledge/ai-governance-frameworks/
  - https://www.computer.org/csdl/magazine/co/2024/09/10660604/1ZPP4D3zAvS
  - https://dualitytech.com/blog/ai-governance-framework/
  - https://www.informatica.com/resources/articles/ai-governance-explained.html
  - https://www.diligent.com/resources/blog/ai-governance
  - https://www.relyance.ai/blog/ai-governance-examples
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

AI Governance Models are structured frameworks of principles, policies, and practices that guide the responsible development, deployment, and management of artificial intelligence systems. The core problem these models address is the inherent risk associated with the increasing power and autonomy of AI. These risks include perpetuating and amplifying societal biases, a lack of transparency in decision-making that can make it impossible to scrutinize or contest outcomes, the potential for malicious misuse of the technology, and the fundamental challenge of ensuring accountability for AI-driven decisions. By establishing clear guidelines, oversight mechanisms, and lines of responsibility, AI governance aims to foster trust among users and the public, mitigate potential harm, and ensure that AI technologies are developed and used in a manner that is aligned with organizational values, societal norms, and legal and regulatory requirements. The value created by these models is a foundation for sustainable and ethical innovation, enabling organizations to confidently harness the transformative power of AI while managing its significant and often complex risks.

The origin of AI governance is not a single event but an evolution that has accelerated in recent years. Early discussions in the fields of computer ethics and robotics laid the conceptual groundwork, but for much of AI's history, governance was not a primary concern. The concept gained significant traction in the mid-2010s, driven by a convergence of factors. The machine learning revolution, particularly the success of deep learning, demonstrated AI's immense potential to transform industries and society. Simultaneously, a series of high-profile scandals and controversies, most notably the Cambridge Analytica affair, revealed AI's capacity for significant societal harm, including the manipulation of democratic processes [1]. This created a sense of urgency among policymakers, industry leaders, and the public. This period saw a proliferation of AI principles and frameworks from academic institutions, major technology companies like Google, IBM, and Microsoft, and multi-stakeholder organizations such as the Partnership on AI. Initially a reactive measure to address emerging harms, the practice of AI governance has since matured into a proactive and strategic necessity for any organization that is serious about leveraging AI responsibly and effectively.

### 2. Core Principles

AI Governance Models are built upon a set of core principles that have achieved broad consensus across industries, governments, and civil society. These principles serve as the normative foundation for the design, development, and deployment of ethical and responsible AI systems.

1.  **Transparency and Explainability.** This foundational principle holds that AI systems should not be inscrutable "black boxes." Stakeholders, including users, regulators, and developers, should be able to understand how an AI system works and the rationale behind its decisions [2]. Transparency involves providing clear and accessible documentation about the data, algorithms, and models used in an AI system. Explainability (often abbreviated as XAI) refers to the methods and techniques used to make the internal workings of a complex AI model, such as a deep neural network, understandable to humans. Without a sufficient degree of transparency and explainability, it is impossible to build trust, debug systems effectively, or establish meaningful oversight.

2.  **Accountability.** There must be clear and well-defined lines of responsibility for the outcomes of AI systems. This principle ensures that if an AI system causes harm or makes a significant error, there is an identifiable individual, group, or entity that can be held responsible [4]. Accountability requires robust governance structures, clear roles and responsibilities for everyone involved in the AI lifecycle, and the ability to audit and trace the decision-making process of an AI system from its initial design to its ongoing operation. It is about ensuring that there is always a human in the loop who is ultimately answerable for the behavior of the system.

3.  **Fairness and Non-Discrimination.** AI systems should treat all individuals and groups equitably and avoid perpetuating or amplifying existing societal biases. This principle requires a proactive and ongoing effort to identify, measure, and mitigate bias in both the data used to train AI models and the algorithms themselves [5]. Fairness is a complex and multifaceted concept, and its assessment often involves examining the impact of AI systems on different demographic groups to ensure that outcomes are not systematically skewed to the disadvantage of any particular group. This is particularly critical in high-stakes applications such as hiring, lending, and criminal justice.

4.  **Safety and Security.** AI systems must be designed, built, and operated to be safe and secure throughout their entire lifecycle. This includes protecting them from adversarial attacks that could manipulate their behavior, ensuring that they operate reliably and predictably within their intended domain, and having safeguards in place to prevent unintended harm [4]. The principle of safety and security extends beyond technical robustness to include the consideration of the broader societal and environmental impacts of AI systems, ensuring that they do not pose a threat to human well-being or the planet.

5.  **Privacy.** AI systems must be designed and used in a way that respects the privacy of individuals and protects their personal data. This principle is closely tied to the broader field of data governance and requires that data is collected, used, stored, and shared in a manner that is compliant with privacy laws, such as the GDPR, and ethical norms [5]. It involves implementing privacy-enhancing techniques like data minimization (collecting only the data that is strictly necessary), anonymization, and secure data handling protocols to protect sensitive information from unauthorized access or misuse.

6.  **Human-Centricity and Oversight.** AI should be designed to augment and empower humans, not to replace them or operate without meaningful human control. This principle emphasizes that humans should always have the final say in decisions, especially in high-stakes situations where the consequences of an error could be severe [2]. Effective human oversight involves not just the ability for a human to intervene and override an AI-driven decision but also the capacity to understand and critically evaluate the recommendations made by AI systems. It is about ensuring that AI remains a tool in the service of human goals and values.

### 3. Key Practices

Operationalizing the core principles of AI governance requires a set of concrete practices that are embedded into the daily workflows and culture of an organization. These practices are the mechanisms that translate high-level principles into actionable steps and ensure that responsible AI is not just a slogan but a reality.

1.  **Establish a Cross-Functional AI Governance Committee.** This practice involves creating a dedicated, empowered body with representatives from a diverse range of departments, including legal, ethics, risk, compliance, data science, engineering, and business units. This committee is responsible for setting the organization's overall AI strategy, defining and updating AI policies, and overseeing their implementation and enforcement [6].

2.  **Develop and Maintain a Comprehensive AI Inventory.** Organizations should create and maintain a detailed and up-to-date inventory of all AI models and systems in use across the enterprise. This inventory should act as a single source of truth, and include metadata about each model's purpose, data sources, risk level, ownership, and development and deployment history [6].

3.  **Conduct Regular Risk and Impact Assessments.** Before deploying a new AI system, and periodically throughout its lifecycle, organizations should conduct thorough assessments to identify, analyze, and mitigate potential risks. This includes evaluating the potential for algorithmic bias, privacy violations, security vulnerabilities, and other ethical and societal harms [6].

4.  **Implement Robust Data Governance Practices.** Since AI systems are heavily reliant on data, strong data governance is a non-negotiable prerequisite for effective AI governance. This practice involves ensuring data quality, integrity, and provenance, as well as establishing and enforcing clear policies for data access, usage, and retention [4].

5.  **Ensure Model Transparency and Comprehensive Documentation.** Every AI model should be accompanied by clear, comprehensive, and accessible documentation that explains its purpose, design, and limitations. This includes information about the training data, the algorithms used, the model's performance metrics, and any known weaknesses or biases [5].

6.  **Perform Regular Audits and Continuous Monitoring.** AI systems should be continuously monitored in production to detect performance degradation, model drift, and the emergence of bias. Regular audits should be conducted by internal or external parties to ensure ongoing compliance with governance policies and regulations [6].

7.  **Establish Clear Accountability and Ownership.** Every AI model and system should have a designated owner who is responsible for its performance, maintenance, and adherence to governance standards. This ensures that there is a clear point of contact for any issues that may arise and that someone is ultimately accountable for the model's impact [5].

8.  **Provide Ongoing Training and Education.** All employees, not just those directly involved in AI development, should receive training on the organization's AI ethics and governance policies. This helps to foster a culture of responsible AI and ensures that everyone in the organization understands their role in upholding these standards [6].

### 4. Application Context

AI Governance Models are applicable across a wide range of industries and at various organizational scales. However, their implementation is most critical in contexts where AI systems have a significant and direct impact on individuals, society, or the organization itself.

**Best Used For:**

*   **Highly Regulated Industries:** In sectors like finance, healthcare, and aviation, where strict regulatory compliance is mandatory, AI governance provides the necessary framework to ensure that AI systems adhere to legal and safety standards.
*   **High-Stakes Decision-Making:** When AI is used to make critical decisions that significantly affect people's lives, such as in credit scoring, hiring, insurance underwriting, or criminal justice, robust governance is essential to ensure fairness, accountability, and transparency.
*   **Large-Scale AI Deployments:** Organizations that deploy AI at scale across multiple departments and functions require a centralized governance model to ensure consistency, manage risks effectively, and align disparate AI initiatives with overall business objectives.
*   **Public Sector Applications:** Government agencies using AI for public services, such as social benefit distribution, infrastructure management, or law enforcement, have a special obligation to ensure public trust, equity, and accountability.
*   **Customer-Facing AI Systems:** For AI applications that interact directly with customers, such as chatbots, personalized recommendation engines, or dynamic pricing systems, governance is crucial for maintaining brand reputation, ensuring a positive and fair user experience, and protecting customer data.

**Not Suitable For:**

*   **Early-Stage Experimentation:** In the initial, exploratory phases of AI research and development, where the focus is on rapid prototyping and testing new ideas, a full-fledged, bureaucratic governance framework may be too burdensome and could stifle innovation.
*   **Low-Impact, Internal Tools:** For simple, internal AI tools with a limited and well-understood impact on business operations or individuals, a lightweight approach to governance may be more appropriate than a comprehensive, formal framework.

**Scale:**

AI Governance Models can and should be applied at all scales, from individual projects to entire ecosystems:

*   **Individual/Team:** At this level, governance may involve practices like peer code reviews, maintaining documentation standards, and adhering to team-level ethical guidelines and checklists.
*   **Department:** Departments may have their own specific AI policies and review processes that are tailored to their particular domain and risk profile.
*   **Organization:** A comprehensive, organization-wide AI governance framework, with a central committee and clear policies, is essential for managing AI risk and strategy at the enterprise level.
*   **Multi-Organization/Ecosystem:** In collaborative contexts, such as industry consortia, open-source projects, or public-private partnerships, shared governance models are needed to ensure interoperability, responsible data sharing, and collective accountability.

**Domains:**

AI governance is relevant in virtually every domain where AI is being adopted, including:

*   **Finance:** For algorithmic trading, fraud detection, credit risk assessment, and customer service.
*   **Healthcare:** For medical diagnosis, treatment planning, drug discovery, and hospital operations.
*   **Transportation:** For autonomous vehicles, traffic management systems, and logistics optimization.
*   **Retail:** For personalized marketing, supply chain management, dynamic pricing, and customer service.
*   **Government:** For public service delivery, policy simulation, national security, and law enforcement.
*   **Manufacturing:** For predictive maintenance, quality control, supply chain optimization, and robotics.

### 5. Implementation

Implementing an AI Governance Model is a significant strategic undertaking that requires careful planning, cross-functional collaboration, and a commitment to continuous improvement. It is not a one-time project that can be completed and then forgotten; rather, it is an ongoing process of embedding responsibility and oversight into the very fabric of the organization's AI activities.

**Prerequisites:**

*   **Executive Sponsorship:** Strong, visible, and consistent support from senior leadership is the single most important prerequisite for a successful AI governance program.
*   **Clear Business Objectives:** The AI governance strategy should not exist in a vacuum. It must be closely and explicitly aligned with the organization's overall business objectives, strategy, and risk appetite.
*   **Data Governance Maturity:** A solid foundation of data governance is a non-negotiable prerequisite for effective AI governance.
*   **AI Literacy:** A baseline level of AI literacy across the organization is necessary to foster a culture of responsible AI and to ensure that all stakeholders understand their roles and responsibilities.

**Getting Started:**

1.  **Establish a Governance Mandate:** The first formal step is to establish the mandate for the AI governance program, typically through a charter or policy document approved by the board or executive leadership.
2.  **Form a Governance Team:** Assemble a dedicated, cross-functional team with representatives from key stakeholder groups to develop and implement the governance framework.
3.  **Conduct a Baseline Assessment:** Conduct a thorough assessment of the organization's current state of AI adoption, maturity, and risk exposure.
4.  **Develop a Phased Roadmap:** Based on the baseline assessment, develop a phased and realistic roadmap for implementing the AI governance framework, prioritizing the highest-risk areas first.
5.  **Start with a Pilot Project:** Begin by applying the new governance framework to a single, high-impact pilot project to test and refine the framework in a real-world setting.

**Common Challenges:**

*   **Pace of Technological Change:** The rapid pace of innovation in AI can make it challenging to keep governance policies and practices up-to-date.
*   **Lack of Skilled Talent:** There is a shortage of professionals with the hybrid skills in data science, ethics, and law needed for effective AI governance.
*   **Organizational Silos:** AI governance requires collaboration across multiple departments, but organizational silos can make this difficult to achieve.
*   **Measuring ROI:** It can be challenging to quantify the return on investment (ROI) of AI governance, which can make it difficult to secure ongoing funding and resources.
*   **Resistance to Change:** As with any new initiative, there may be resistance to change from employees who are accustomed to the old way of doing things.

**Success Factors:**

*   **Integration with Existing Governance Structures:** AI governance should be integrated with the organization's existing governance, risk, and compliance (GRC) structures.
*   **Automation and Tooling:** Leveraging technology to automate aspects of AI governance can significantly improve efficiency and effectiveness.
*   **Continuous Learning and Adaptation:** AI governance is a dynamic process that must continuously adapt to new technologies, regulations, and business needs.
*   **Clear Communication and Training:** A clear communication plan and ongoing training are essential for ensuring that all stakeholders understand and are able to fulfill their governance responsibilities.
*   **Focus on Value Creation:** AI governance should be framed not just as a risk mitigation exercise but as a driver of business value.

### 6. Evidence & Impact

AI Governance Models are increasingly being adopted by organizations across various sectors, and the evidence of their impact is growing. While the field is still relatively new, there are numerous case studies and research findings that demonstrate the value of a structured approach to AI governance.

**Notable Adopters:**

*   **Google:** Google has a well-defined set of AI Principles and a dedicated Responsible AI organization that oversees their implementation.
*   **Microsoft:** Microsoft has established a comprehensive Responsible AI framework that is guided by six core principles.
*   **IBM:** IBM has a long-standing commitment to AI ethics, with a set of Principles for Trust and Transparency.
*   **Salesforce:** Salesforce has developed a set of Trusted AI Principles and a formal review process.
*   **Major Financial Institutions:** Many large banks and financial institutions have implemented AI governance frameworks to manage the risks associated with algorithmic trading, credit scoring, and fraud detection.

**Documented Outcomes:**

*   **Improved Risk Management:** Organizations with mature AI governance programs are better able to identify, assess, and mitigate the risks associated with AI [7].
*   **Enhanced Trust and Brand Reputation:** By demonstrating a commitment to responsible AI, organizations can build trust with their customers, employees, and other stakeholders [5].
*   **Increased Innovation and Competitiveness:** A clear and effective AI governance framework can actually accelerate innovation by providing developers with the guidance and confidence they need to build and deploy new AI systems responsibly [7].
*   **Reduced Bias and Improved Fairness:** By implementing practices like bias and fairness audits, organizations can reduce the risk of their AI systems perpetuating or amplifying societal biases [7].

**Research Support:**

*   A growing body of academic research supports the importance of AI governance.
*   Research from the World Economic Forum has highlighted the importance of a multi-stakeholder approach to AI governance.
*   Studies from institutions like the Berkman Klein Center at Harvard University and the AI Now Institute at New York University have been instrumental in shaping the discourse on AI ethics and governance.

### 7. Cognitive Era Considerations

As we move deeper into the cognitive era, where AI is not just a tool but a partner in cognitive tasks, the nature of AI Governance Models will need to evolve. The increasing autonomy and complexity of AI systems will require a more dynamic and adaptive approach to governance.

**Cognitive Augmentation Potential:**

AI and automation have the potential to significantly enhance AI governance itself. For example, AI-powered tools can be used to automate the process of monitoring AI systems for bias and performance degradation, providing real-time alerts to human overseers. AI can also be used to assist in the creation and maintenance of AI inventories, and to help organizations stay up-to-date with the rapidly changing regulatory landscape. In essence, we will use AI to govern AI.

**Human-Machine Balance:**

Despite the potential for automation, the human element will remain central to AI governance. While AI can automate many of the technical aspects of governance, humans will still be responsible for setting the ethical principles, making the final judgments in complex cases, and ensuring that AI systems are aligned with human values. The focus will shift from manual oversight of every decision to the design and management of the governance systems themselves. The uniquely human role will be to handle exceptions, adjudicate ethical dilemmas, and engage in stakeholder dialogue.

**Evolution Outlook:**

The AI governance models of the future will likely be more embedded, automated, and adaptive. We can expect to see the emergence of "Governance-as-Code," where governance policies are expressed in a machine-readable format and automatically enforced throughout the AI lifecycle. There will also be a greater emphasis on dynamic and continuous assurance, moving away from static, point-in-time audits to real-time monitoring and validation. Furthermore, as AI becomes more decentralized, with the rise of technologies like federated learning and blockchain, governance models will need to adapt to manage risk and ensure accountability in these new distributed environments.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
AI Governance Models define a broad spectrum of stakeholders, including developers, users, regulators, and the public, advocating for their inclusion through mechanisms like advisory boards. The framework distributes rights and responsibilities, assigning clear accountability for AI systems. However, its primary focus remains on human and organizational stakeholders, with less explicit consideration for the rights and roles of the environment or future generations within the governance architecture.

**2. Value Creation Capability:**
The pattern primarily enables value creation by mitigating risks and building trust, which fosters sustainable innovation and protects against social and economic harm. It creates social value through principles of fairness and accountability, and knowledge value through transparency and explainability requirements. However, the framework is often defensively postured, focusing more on preventing negative value (harm) than proactively architecting for positive collective value creation across social, ecological, and knowledge domains.

**3. Resilience & Adaptability:**
The pattern is explicitly designed for resilience and adaptability in the face of rapid technological change. Core practices like continuous monitoring, regular audits, and impact assessments allow systems to maintain coherence under stress and adapt to complexity. This focus on dynamic, ongoing assurance helps ensure that the value created by AI systems is resilient and can be sustained over time.

**4. Ownership Architecture:**
This pattern redefines ownership by emphasizing a distributed architecture of rights and responsibilities, moving beyond a purely proprietary view of technology. It establishes clear lines of accountability for AI models and their impacts, creating a culture of shared responsibility among developers, operators, and overseers. While it doesn't fully escape the paradigm of monetary equity, its focus on stewardship and accountability is a significant step toward a more commons-oriented ownership model.

**5. Design for Autonomy:**
AI Governance Models are inherently designed to be compatible with autonomous systems like AI and DAOs. The pattern promotes concepts like "Governance-as-Code" and automated monitoring, which are designed to manage complex, distributed systems with low coordination overhead. By providing a structured framework for oversight and accountability, it enables the responsible deployment of autonomous technologies.

**6. Composability & Interoperability:**
The pattern is highly composable and designed to integrate with existing organizational structures like GRC (Governance, Risk, and Compliance). It provides a modular framework of principles and practices that can be combined with other technical and social patterns to build larger, more complex value-creation systems. Its principles are widely adopted, fostering interoperability across different tools and platforms in the responsible AI ecosystem.

**7. Fractal Value Creation:**
The logic of AI governance can be applied fractally across multiple scales, from individual projects and teams to entire organizations and multi-stakeholder ecosystems. The pattern explicitly outlines how its principles and practices can be adapted to different levels, ensuring that the core logic of responsible value creation can be replicated and scaled. This allows for a coherent governance approach that functions consistently whether applied to a single algorithm or a global AI platform.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
AI Governance Models are a powerful enabler of collective value creation by establishing the necessary foundations of trust, safety, and accountability. The pattern strongly supports resilience, adaptability, and interoperability. However, it scores a 4 instead of a 5 because its focus is often more on mitigating downside risk for the deploying organization rather than proactively architecting for multi-stakeholder, positive-sum value creation. Its stakeholder considerations, while broad, do not yet fully incorporate non-human stakeholders like the environment in a meaningful way.

**Opportunities for Improvement:**
- Integrate ecological impact assessments as a core component of the governance framework to explicitly include the environment as a key stakeholder.
- Develop metrics and incentives that reward the proactive creation of positive social and ecological value, beyond simply mitigating risks.
- Strengthen mechanisms for community and public participation to ensure that the definition of "value" is collectively determined and not solely defined by the organization.

### 9. Resources & References

**Essential Reading:**

*   **"The Age of AI: And Our Human Future" by Henry A. Kissinger, Eric Schmidt, and Daniel Huttenlocher:** This book provides a high-level perspective on the societal implications of AI and the importance of developing a shared ethical framework.
*   **"Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy" by Cathy O'Neil:** A seminal work that highlights the dangers of algorithmic bias and the need for greater transparency and accountability in AI.
*   **NIST AI Risk Management Framework (AI RMF 1.0):** A practical and widely adopted framework for managing the risks associated with AI. It provides a structured approach to identifying, assessing, and mitigating AI risks.
*   **OECD AI Principles:** An influential set of intergovernmental principles that have been adopted by over 40 countries. They provide a high-level framework for the responsible stewardship of trustworthy AI.

**Organizations & Communities:**

*   **Partnership on AI (PAI):** A multi-stakeholder organization that brings together industry, academia, and civil society to advance the responsible development and use of AI.
*   **AI Now Institute:** A leading research institute at New York University that produces critical research on the social implications of AI.
*   **The Alan Turing Institute:** The UK's national institute for data science and artificial intelligence, which conducts research on AI ethics and governance.
*   **World Economic Forum's Centre for the Fourth Industrial Revolution:** An international organization that is working to shape the governance of emerging technologies, including AI.

**Tools & Platforms:**

*   **IBM AI Fairness 360:** An open-source toolkit that can help developers check for and mitigate bias in their machine learning models.
*   **Google's What-If Tool:** An interactive tool that allows developers to explore the performance of their models and test for fairness.
*   **Microsoft's Fairlearn:** An open-source toolkit that provides a range of fairness assessment and mitigation algorithms.

**References:**

[1] S. Chesterman, "The Evolution of AI Governance," in Computer, vol. 57, no. 09, pp. 80-92, 2024. [Online]. Available: https://www.computer.org/csdl/magazine/co/2024/09/10660604/1ZPP4D3zAvS

[2] "9 Key AI Governance Frameworks in 2025," AI21, [Online]. Available: https://www.ai21.com/knowledge/ai-governance-frameworks/

[3] "What is AI Governance?," IBM, [Online]. Available: https://www.ibm.com/think/topics/ai-governance

[4] "Principles of an AI Governance Framework," DualityTech, [Online]. Available: https://dualitytech.com/blog/ai-governance-framework/

[5] "AI Governance: Best Practices and Importance," Informatica, [Online]. Available: https://www.informatica.com/resources/articles/ai-governance-explained.html

[6] "AI governance: What it is, why it matters and how to implement it," Diligent, [Online]. Available: https://www.diligent.com/resources/blog/ai-governance

[7] "AI Governance Examples: Successes & Failures," Relyance AI, [Online]. Available: https://www.relyance.ai/blog/ai-governance-examples
