---
id: pat_01kg5023ztenhrk74ha5vzz8fs
page_url: https://commons-os.github.io/patterns/domain/retroactive-public-goods-funding/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/retroactive-public-goods-funding.md
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
  commons_alignment: 3
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

## 8. Commons Alignment Assessment

This section assesses the alignment of the Retroactive Public Goods Funding pattern with the principles of a commons-based economy. The assessment is based on seven key dimensions of commons alignment, with a score from 1 to 5 for each dimension, where 1 represents low alignment and 5 represents high alignment.

**1. Openness and Accessibility (Score: 4/5):** RetroPGF programs are typically open to all members of a community, with a transparent application and evaluation process. The results of the funding rounds are made public, and the code and data associated with the program are often open-source. This high degree of openness and accessibility ensures that everyone has the opportunity to participate and that the process is accountable to the community.

**2. Community Governance (Score: 4/5):** RetroPGF is fundamentally a community-governed process. The evaluation of impact and the allocation of rewards are conducted by a decentralized body of community members, who are chosen for their expertise and alignment with the ecosystem's values. This decentralized approach to governance helps to ensure that funding decisions reflect the collective priorities of the community.

**3. Shared Resources (Score: 3/5):** The funding pool for a RetroPGF program is a shared resource that is used to support the creation of public goods. However, the resources themselves are not always managed as a commons. In many cases, the funding pool is controlled by a foundation or a core team, who then delegate the allocation of funds to the community. While the community has a say in how the funds are distributed, they do not always have full control over the management of the resource itself.

**4. Value Creation and Distribution (Score: 4/5):** RetroPGF is designed to reward the creation of value in a way that is fair and equitable. By rewarding projects based on their demonstrated impact, RetroPGF ensures that those who create the most value for the community receive the greatest rewards. This helps to create a more sustainable and equitable ecosystem for the development of public goods.

**5. Sustainability (Score: 3/5):** The sustainability of a RetroPGF program depends on the sustainability of its funding source. While some programs have secured long-term funding commitments, others are more dependent on short-term or volatile sources of revenue. To be truly sustainable, a RetroPGF program needs to have a reliable and long-term source of funding that can support the continuous creation of public goods.

**6. Non-Monetary Value (Score: 3/5):** While RetroPGF is primarily focused on the distribution of financial rewards, it also recognizes the importance of non-monetary value. The public recognition and validation that come with receiving a RetroPGF award can be a powerful motivator for builders and can help to build social capital and trust within the community. However, the primary focus remains on financial incentives.

**7. Contribution and Reciprocity (Score: 4/5):** RetroPGF is based on the principle of reciprocity, where those who contribute to the commons are rewarded for their contributions. This creates a strong incentive for individuals and organizations to contribute to the public good, knowing that their efforts will be recognized and rewarded. This helps to foster a culture of contribution and collaboration within the community.

**Overall Commons Alignment Score: 3/5**

## 9. Resources & References

[1] Buterin, V. (2021). *Retroactive Public Goods Funding*. Ethereum Optimism. [https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c](https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c)

[2] Unchained Crypto. (2024). *What Is Retroactive Public Goods Funding?*. [https://unchainedcrypto.com/retroactive-public-goods-funding/](https://unchainedcrypto.com/retroactive-public-goods-funding/)

[3] Gitcoin. (2025). *WTF is Retro Funding*. [https://gitcoin.co/blog/wtf-is-retro-funding](https://gitcoin.co/blog/wtf-is-retro-funding)

[4] Optimism Collective. (2024). *Lessons learned from two years of Retroactive Public Goods Funding*. [https://gov.optimism.io/t/lessons-learned-from-two-years-of-retroactive-public-goods-funding/9239](https://gov.optimism.io/t/lessons-learned-from-two-years-of-retroactive-public-goods-funding/9239)

[5] Buterin, V. (2021). *Review of Optimism retro funding round 1*. [https://vitalik.eth.limo/general/2021/11/16/retro1.html](https://vitalik.eth.limo/general/2021/11/16/retro1.html)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/retroactive-public-goods-funding/](https://commons-os.github.io/patterns/domain/retroactive-public-goods-funding/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/retroactive-public-goods-funding.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/retroactive-public-goods-funding.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
