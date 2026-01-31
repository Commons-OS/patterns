---
id: pat_01kg5023ztenhrk74ha5vzz8fs
page_url: https://commons-os.github.io/patterns/retroactive-public-goods-funding/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/retroactive-public-goods-funding.md
slug: retroactive-public-goods-funding
title: Retroactive Public Goods Funding
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: [framework, methodology]
  era: [digital]
  origin: ["Vitalik Buterin", "Optimism"]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: ["https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c", "https://unchainedcrypto.com/retroactive-public-goods-funding/", "https://gitcoin.co/blog/wtf-is-retro-funding", "https://gov.optimism.io/t/lessons-learned-from-two-years-of-retroactive-public-goods-funding/9239", "https://vitalik.eth.limo/general/2021/11/16/retro1.html"]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

# Retroactive Public Goods Funding

## 1. Overview

Retroactive Public Goods Funding (RetroPGF) is a novel approach to financing public goods that rewards projects based on the demonstrated impact they have already generated. Unlike traditional funding models that provide capital upfront based on proposals and predictions of future success, RetroPGF allocates funds retrospectively. This model is designed to address the inherent challenges of funding public goods, particularly in the digital realm, where contributions are often non-excludable and non-rivalrous, making it difficult to monetize them directly. By rewarding proven value, RetroPGF aims to create a more efficient and sustainable ecosystem for the development and maintenance of public goods, fostering innovation and long-term commitment from builders and contributors.

The core idea behind RetroPGF is that it is easier to reach a consensus on what has been useful in the past than to predict what will be useful in the future. This principle, articulated by Vitalik Buterin, underpins the entire mechanism. A designated body, often a decentralized autonomous organization (DAO) referred to as a "Results Oracle," is responsible for evaluating the impact of completed projects and distributing rewards accordingly. This process not only provides a financial return for valuable work but also creates a powerful incentive for individuals and organizations to invest their time, skills, and resources in creating public goods, knowing that their contributions may be rewarded later.

This pattern has gained significant traction within the Web3 and blockchain communities, with prominent ecosystems like Optimism, Gitcoin, and Filecoin pioneering its implementation. These early experiments have demonstrated the potential of RetroPGF to foster a vibrant and self-sustaining environment for public goods. By channeling protocol-generated revenue or community-donated funds into these retroactive rewards, a virtuous cycle is created: valuable public goods attract users and developers, which in turn generates more value for the ecosystem, a portion of which is then used to fund more public goods. This creates a powerful flywheel effect that drives continuous growth and innovation.

## 2. Core Principles

Retroactive Public Goods Funding is built on a set of core principles that differentiate it from traditional funding mechanisms and are designed to foster a more robust and equitable ecosystem for public goods. These principles guide the design and implementation of RetroPGF programs, ensuring that they remain aligned with their fundamental goal of rewarding demonstrated impact.

**Impact Equals Reward:** The most fundamental principle of RetroPGF is that funding should be proportional to the value a project has already created. This direct link between impact and reward is what drives the entire system. It shifts the focus from speculative promises to tangible results, ensuring that resources are allocated to projects that have proven their worth. This principle not only rewards past contributions but also creates a powerful incentive for future work, as builders can be confident that their efforts will be recognized and compensated if they deliver real value.

**It's Easier to Agree on What Was Useful Than What Will Be:** This principle, central to the philosophy of RetroPGF, acknowledges the inherent difficulty and uncertainty of predicting the future. By focusing on retrospective evaluation, RetroPGF leverages the collective wisdom of the community to assess the impact of completed projects. This approach is less susceptible to the biases and inaccuracies that can plague proactive funding decisions, leading to a more efficient and effective allocation of resources.

**Rewarding the Past to Build the Future:** RetroPGF is not just about rewarding past contributions; it is about creating a sustainable future for public goods. By providing a clear path to funding for successful projects, RetroPGF encourages long-term commitment and investment in the public goods ecosystem. This creates a virtuous cycle where the rewards from past successes fuel the development of future innovations, leading to a continuous process of growth and improvement.

**Decentralized and Community-Driven Evaluation:** To ensure fairness and transparency, the evaluation of impact in RetroPGF is typically conducted by a decentralized body of community members. These evaluators, often referred to as "badgeholders" or "citizens," are chosen for their expertise and alignment with the ecosystem's values. This decentralized approach to governance helps to mitigate the risk of capture and ensures that funding decisions reflect the collective priorities of the community.

## 3. Key Practices

Implementing a Retroactive Public Goods Funding program involves a set of key practices that have emerged from early experiments. These practices are designed to ensure that the process is fair, transparent, and effective in rewarding demonstrated impact. While the specific implementation details may vary between ecosystems, these core practices provide a general framework for how to run a successful RetroPGF program.

**Establishing a Funding Pool:** The first step in any RetroPGF program is to establish a pool of funds that will be used to reward impactful projects. This funding can come from a variety of sources, such as protocol-generated revenue (e.g., sequencer fees in the case of Optimism), donations from the community, or allocations from a foundation or treasury. The size of the funding pool will determine the total amount of rewards that can be distributed in a given round.

**Defining Impact Categories and Metrics:** To guide the evaluation process, it is important to define the categories of impact that will be rewarded and the metrics that will be used to assess that impact. Impact categories can be broad, such as "Infrastructure," "Tooling," and "Education," or more specific to the needs of the ecosystem. Metrics can be quantitative (e.g., number of users, transaction volume, GitHub commits) or qualitative (e.g., community feedback, expert testimonials). A combination of both is often used to provide a holistic view of a project's contribution.

**Application and Nomination Process:** Projects can be considered for RetroPGF rewards through an application or nomination process. This allows builders to showcase their work and provide evidence of their impact. The process should be open and accessible to all members of the community, ensuring that a wide range of projects have the opportunity to be considered. Some programs also allow for the nomination of projects by community members, which can help to surface valuable contributions that might otherwise be overlooked.

**Badgeholder-Based Evaluation:** The evaluation of impact is typically conducted by a group of trusted and knowledgeable community members known as "badgeholders" or "citizens." These individuals are responsible for reviewing applications, assessing the impact of each project, and voting on the allocation of rewards. The selection of badgeholders is a critical part of the process, as their expertise and integrity are essential for ensuring the fairness and legitimacy of the funding decisions. Badgeholders are often selected based on their past contributions to the ecosystem and their demonstrated understanding of its values and priorities.

**Transparent and Public Voting:** The voting process should be transparent and public, allowing the entire community to see how rewards are being allocated. This transparency helps to build trust in the process and provides valuable feedback to both builders and evaluators. Many RetroPGF programs use public platforms to display the votes of each badgeholder, along with their reasoning for their decisions. This open approach to governance is a key feature of the RetroPGF model and is essential for maintaining its legitimacy and accountability.

## 4. Application Context

Retroactive Public Goods Funding is particularly well-suited to certain contexts and environments, especially those where the value of contributions is difficult to measure upfront. The following are some of the key application contexts where RetroPGF has been successfully applied or has the potential to be highly effective.

**Web3 and Blockchain Ecosystems:** The most prominent and successful applications of RetroPGF to date have been within Web3 and blockchain ecosystems. These environments are characterized by a high degree of open-source development, a strong sense of community, and the presence of protocol-generated revenue streams that can be used to fund public goods. Ecosystems like Optimism, Gitcoin, and Solana have used RetroPGF to fund a wide range of projects, from core infrastructure and developer tooling to educational resources and community-building initiatives.

**Open-Source Software Development:** RetroPGF is a powerful tool for funding the development and maintenance of open-source software. Many open-source projects struggle to find sustainable funding models, as their work is freely available to everyone. RetroPGF provides a mechanism for rewarding the creators and maintainers of valuable open-source projects based on the impact they have already had. This can help to ensure the long-term sustainability of critical open-source infrastructure and encourage more developers to contribute to open-source projects.

**Scientific Research and Academia:** The principles of RetroPGF can also be applied to the funding of scientific research and academic work. In these fields, the impact of research can often take years to become fully apparent. A retroactive funding model could be used to reward researchers whose work has had a significant and demonstrable impact on their field, as measured by citations, patents, or other indicators. This could help to incentivize more innovative and high-risk research, as researchers would be less dependent on securing upfront funding based on speculative proposals.

**Creative and Artistic Works:** RetroPGF can also be used to support the creation of creative and artistic works that are made freely available to the public. This could include everything from digital art and music to written works and educational content. By rewarding creators based on the impact and reach of their work, RetroPGF can provide a sustainable source of income for artists and creators who choose to make their work available as a public good.

## 5. Implementation

Implementing a Retroactive Public Goods Funding program requires careful planning and consideration of a number of key factors. The following is a step-by-step guide to implementing a RetroPGF program, drawing on the best practices and lessons learned from early experiments.

**1. Secure a Funding Source:** The first and most critical step is to secure a sustainable source of funding for the program. This could be a portion of protocol revenue, a dedicated community fund, or a commitment from a foundation or other organization. The size and predictability of the funding source will have a significant impact on the scale and sustainability of the program.

**2. Establish a Governance Framework:** A clear and transparent governance framework is essential for the success of any RetroPGF program. This includes defining the roles and responsibilities of the different participants, such as the program administrators, the badgeholders, and the community. The process for selecting and rotating badgeholders should be clearly defined, as should the rules and procedures for voting and allocating rewards.

**3. Define Impact and Evaluation Criteria:** The program should have a clear and well-defined set of criteria for what constitutes "impact" and how it will be evaluated. This includes identifying the key areas of contribution that the program aims to support and the specific metrics that will be used to measure impact in each of those areas. It is important to strike a balance between quantitative and qualitative metrics to ensure a holistic and nuanced assessment of each project's contribution.

**4. Develop an Application and Review Process:** A user-friendly and accessible application process is needed to allow projects to submit their work for consideration. The application should be designed to collect the information that badgeholders will need to evaluate the project's impact, including a description of the project, evidence of its use and adoption, and any relevant metrics or testimonials. The review process should be structured to ensure that each application is given a fair and thorough evaluation by the badgeholders.

**5. Conduct a Transparent Voting and Allocation Process:** The voting and allocation process should be conducted in a transparent and public manner. This includes publishing the votes of each badgeholder, along with their rationale for their decisions. The final allocation of rewards should be based on the collective judgment of the badgeholders, as expressed through their votes. There are various mechanisms that can be used to aggregate votes and determine the final allocation, such as a simple average, a median, or a more complex quadratic formula.

**6. Iterate and Improve:** A RetroPGF program should be viewed as an ongoing experiment that can be continuously improved over time. It is important to collect feedback from all participants, including builders, badgeholders, and the broader community, and to use that feedback to refine and improve the program. This iterative approach will help to ensure that the program remains effective and aligned with the evolving needs of the ecosystem.

## 6. Evidence & Impact

The effectiveness of Retroactive Public Goods Funding is best demonstrated through the real-world impact it has had on the ecosystems that have implemented it. The following examples and case studies provide evidence of how RetroPGF has been used to fund valuable public goods and the positive outcomes it has generated.

**Optimism:** As the pioneer of RetroPGF, Optimism has conducted multiple rounds of funding, distributing millions of dollars to projects that have contributed to its ecosystem. In its early rounds, Optimism focused on broad categories of impact, such as infrastructure, tooling, and education. This led to the funding of a wide range of projects, including:

*   **L2BEAT:** A research and analytics platform for Ethereum layer 2 solutions, which received significant funding for its role in providing critical data and insights to the community.
*   **Revoke.cash:** A tool that helps users manage their token approvals, enhancing the security of the ecosystem.
*   **CryptoZombies:** An interactive learning platform that teaches developers how to build on Ethereum and Optimism.

Lessons learned from these early rounds have led to a more refined approach, with a greater emphasis on expertise-based voting and a combination of metrics-based and subjective evaluation. This iterative approach to improving the RetroPGF process is a testament to the Optimism community's commitment to making it as effective as possible.

**Gitcoin:** Gitcoin, a platform for funding public goods in the Ethereum ecosystem, has also embraced RetroPGF as a key part of its funding strategy. Gitcoin's implementation of RetroPGF, known as "Retro Funding," is designed to complement its popular Quadratic Funding rounds. While Quadratic Funding is used to support early-stage projects, Retro Funding is used to reward projects that have already demonstrated significant impact. This two-pronged approach creates a comprehensive funding pipeline that supports projects at every stage of their lifecycle.

**Filecoin:** The Filecoin ecosystem has also adopted RetroPGF to fund public goods that support its decentralized storage network. Filecoin's RetroPGF program has focused on rewarding contributions to core infrastructure, developer tooling, and community-building initiatives. By funding these essential public goods, Filecoin is helping to create a more robust and vibrant ecosystem for its users and developers.

**Impact on Builder Motivation and Retention:** One of the most significant impacts of RetroPGF has been on the motivation and retention of builders. By providing a clear path to funding for impactful work, RetroPGF has created a powerful incentive for developers and entrepreneurs to contribute to public goods ecosystems. This has helped to attract and retain top talent, leading to a higher quality and quantity of public goods being produced.

## 7. Cognitive Era Considerations

The transition to the Cognitive Era, characterized by the increasing importance of knowledge work, artificial intelligence, and decentralized collaboration, has significant implications for the funding of public goods. Retroactive Public Goods Funding is particularly well-suited to this new paradigm, as it provides a mechanism for rewarding the creation and dissemination of knowledge, which is a key public good in the Cognitive Era.

**Funding Knowledge Creation and Curation:** In the Cognitive Era, the ability to create, curate, and disseminate knowledge is more valuable than ever. RetroPGF can be used to fund a wide range of knowledge-based public goods, such as open-access research, educational materials, and curated datasets. By rewarding the creators and curators of high-quality knowledge, RetroPGF can help to accelerate the pace of innovation and ensure that valuable information is freely available to everyone.

**Aligning AI with the Public Good:** As artificial intelligence becomes more powerful and pervasive, it is essential to ensure that it is aligned with the public good. RetroPGF can be used to incentivize the development of AI systems that are designed to benefit society as a whole, rather than just a narrow set of stakeholders. For example, RetroPGF could be used to fund the development of open-source AI models, ethical AI frameworks, and AI-powered tools for social good.

**Decentralized and Collaborative Governance:** The Cognitive Era is also characterized by a shift towards more decentralized and collaborative forms of governance. RetroPGF is a natural fit for this new paradigm, as it is based on the principles of decentralized evaluation and community-driven decision-making. By empowering a diverse group of stakeholders to participate in the funding process, RetroPGF can help to ensure that funding decisions are aligned with the collective intelligence and values of the community.

**The Future of Work and Value Creation:** The rise of the Cognitive Era is also transforming the nature of work and value creation. As more and more work becomes knowledge-based and collaborative, traditional models of compensation and employment are becoming less relevant. RetroPGF offers a new model for rewarding value creation that is based on impact rather than on time or credentials. This could have profound implications for the future of work, as it provides a mechanism for individuals and teams to be rewarded for their contributions to public goods, regardless of their formal employment status.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
The pattern establishes a clear stakeholder architecture centered on value creation and assessment. It defines Rights for builders to have their impact evaluated and rewarded, and Responsibilities to deliver demonstrable value. It also outlines the Rights and Responsibilities of a decentralized body of evaluators (a "Results Oracle" or "badgeholders") tasked with assessing impact, creating a system of checks and balances between value creators and the community that funds them.

**2. Value Creation Capability:**
RetroPGF directly enables collective value creation beyond immediate economic output. By rewarding projects based on demonstrated impact, it incentivizes the production of non-monetizable public goods like open-source infrastructure, educational resources, and scientific knowledge. This focus on rewarding proven utility fosters a diverse ecosystem of value, including social, knowledge, and resilience value, which are critical for a thriving commons.

**3. Resilience & Adaptability:**
The core principle, "it is easier to agree on what was useful than to predict what will be," makes the system inherently resilient and adaptable. Instead of speculating on future needs, the pattern allocates resources based on proven, historical value, allowing the system to adapt to emergent needs and thrive on complexity. This retrospective approach ensures that the funding mechanism remains coherent and effective even as the ecosystem evolves under stress.

**4. Ownership Architecture:**
The pattern reframes ownership away from direct equity in an asset and towards a right to be rewarded for creating value. While it doesn't define ownership of the public goods themselves (which remain open), it establishes a form of "impact ownership." Contributors have a legitimate claim on rewards based on the value their work has generated, defining a new kind of stakeholding based on contribution rather than capital investment.

**5. Design for Autonomy:**
RetroPGF is explicitly designed for and has found its greatest success within autonomous, distributed systems like DAOs. The reliance on a decentralized "Results Oracle" for evaluation and its application within blockchain ecosystems demonstrates high compatibility with AI and other autonomous agents. The process minimizes upfront coordination overhead, as it focuses on evaluating finished work rather than managing ongoing projects.

**6. Composability & Interoperability:**
This pattern is highly composable, designed to integrate with other economic and governance patterns. It can be layered on top of any system that generates collective revenue (e.g., protocol fees, DAO treasuries) to create a public goods funding engine. As shown by its use with Quadratic Funding, it can be combined with other funding mechanisms to create a more comprehensive and life-cycle-aware capital allocation system.

**7. Fractal Value Creation:**
The logic of rewarding demonstrated impact can be applied at multiple scales, making it fractal. A large-scale ecosystem can use it to fund major infrastructure, while a small DAO or sub-community can apply the same principle to reward local contributions. This scalability allows the core value-creation logic to be deployed across different levels of a larger system, from macro to micro.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
RetroPGF is a powerful enabler of collective value creation that is highly aligned with the principles of a resilient, adaptive commons. It establishes a clear architecture for rewarding demonstrated impact, fostering the production of public goods that are often neglected by traditional market economies. Its design for autonomy and composability makes it a foundational component for modern, decentralized ecosystems.

**Opportunities for Improvement:**
- The model's effectiveness is highly dependent on the integrity and wisdom of the "Results Oracle." Developing robust, transparent, and capture-resistant evaluation mechanisms is critical for long-term success.
- Explicitly defining the Rights and Responsibilities of the funding source (e.g., the protocol or DAO treasury) would strengthen the stakeholder architecture.
- Further exploration is needed on how to measure and reward non-obvious or long-tail value, as the model may favor impact that is easily quantifiable.

## 9. Resources & References

[1] Buterin, V. (2021). *Retroactive Public Goods Funding*. Ethereum Optimism. [https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c](https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c)

[2] Unchained Crypto. (2024). *What Is Retroactive Public Goods Funding?*. [https://unchainedcrypto.com/retroactive-public-goods-funding/](https://unchainedcrypto.com/retroactive-public-goods-funding/)

[3] Gitcoin. (2025). *WTF is Retro Funding*. [https://gitcoin.co/blog/wtf-is-retro-funding](https://gitcoin.co/blog/wtf-is-retro-funding)

[4] Optimism Collective. (2024). *Lessons learned from two years of Retroactive Public Goods Funding*. [https://gov.optimism.io/t/lessons-learned-from-two-years-of-retroactive-public-goods-funding/9239](https://gov.optimism.io/t/lessons-learned-from-two-years-of-retroactive-public-goods-funding/9239)

[5] Buterin, V. (2021). *Review of Optimism retro funding round 1*. [https://vitalik.eth.limo/general/2021/11/16/retro1.html](https://vitalik.eth.limo/general/2021/11/16/retro1.html)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/retroactive-public-goods-funding/](https://commons-os.github.io/patterns/domain/retroactive-public-goods-funding/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/retroactive-public-goods-funding.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/retroactive-public-goods-funding.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
