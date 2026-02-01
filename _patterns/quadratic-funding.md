---
id: pat_01kg5023zrexhr77rg9vme60dd
page_url: https://commons-os.github.io/patterns/quadratic-funding/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/quadratic-funding.md
slug: quadratic-funding
title: Quadratic Funding
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: operations
  category: [framework, methodology]
  era: [digital]
  origin: ["A Flexible Design for Funding Public Goods"]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: ["https://arxiv.org/abs/1809.06421", "https://qf.gitcoin.co/", "https://www.wtfisqf.com/"]
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

## 1. Overview

Quadratic Funding (QF) is a novel and increasingly influential mechanism for funding public goods in a democratic and scalable manner. It presents a mathematical approach to crowdfunding that prioritizes the breadth of support over the depth of individual contributions. In essence, the number of contributors to a project matters more than the total amount of money contributed. This model aims to rectify the classic "free-rider problem" in public goods provision, where individuals can benefit from a resource without contributing to its creation or maintenance, leading to underfunding and a suboptimal provision of these goods. By amplifying the value of small donations from a large number of people, Quadratic Funding seeks to create a more equitable and efficient allocation of resources for projects that benefit a wide community.

The concept was formally introduced by Vitalik Buterin, Zoë Hitzig, and E. Glen Weyl in their 2018 paper, "A Flexible Design for Funding Public Goods." [1] The authors proposed QF as an extension of the principles of Quadratic Voting, applying them to the domain of public finance. The core of the mechanism is a matching fund that subsidizes public goods based on the number of individual contributions they receive. The matching amount for a given project is calculated as the square of the sum of the square roots of all individual contributions. This formula gives greater weight to a large number of small contributions than to a small number of large contributions, thereby reflecting the collective preference of the community more accurately.

Quadratic Funding has gained significant traction in the blockchain and open-source software communities, most notably through its implementation by Gitcoin, a platform that supports the development of open-source projects. [2] Gitcoin's grants program has demonstrated the potential of QF to mobilize communities and direct funding to a diverse range of projects that might otherwise struggle to secure financial support. The success of these initiatives has sparked a broader conversation about the potential for QF to be applied in other contexts, such as campaign finance, local infrastructure projects, and journalism. As a pattern, Quadratic Funding offers a powerful tool for fostering collective action and building more resilient and self-organizing ecosystems for public goods in the digital age.

## 2. Core Principles

Quadratic Funding is built upon a set of core principles that distinguish it from traditional funding mechanisms. These principles are designed to foster a more democratic, efficient, and community-driven approach to the allocation of resources for public goods. Understanding these principles is essential for appreciating the transformative potential of QF as an organizational pattern.

**1. Collective Preference Aggregation:** The primary principle of Quadratic Funding is to aggregate the preferences of a community in a way that reflects the intensity of their collective will. Unlike simple one-person-one-vote systems, which can be dominated by a simple majority, or market-based systems, which are skewed by wealth, QF provides a mechanism for a more nuanced expression of support. The quadratic nature of the matching formula ensures that a project with broad but shallow support can receive more funding than a project with narrow but deep support, aligning the allocation of resources with the collective good.

**2. Counteracting the Free-Rider Problem:** QF directly confronts the free-rider problem by creating a powerful incentive for individuals to contribute, no matter how small their contribution. The matching mechanism means that even a small donation can have a significant impact on the total funding a project receives, especially when many others are also contributing. This encourages participation and helps to overcome the rational apathy that often plagues collective action problems.

**3. Sybil Resistance and Identity Verification:** A critical principle for the successful implementation of Quadratic Funding is the ability to ensure that each contribution comes from a unique individual. This is known as Sybil resistance, and it is essential to prevent a single actor from creating multiple fake identities to artificially inflate the matching funds for a particular project. Various methods for identity verification have been proposed and implemented, ranging from social verification to more sophisticated digital identity solutions. The integrity of the QF mechanism depends on the robustness of these measures.

**4. Decentralization and Community Ownership:** Quadratic Funding is inherently a decentralized pattern. It distributes the power of funding decisions across a wide network of participants rather than concentrating it in the hands of a few central actors. This fosters a sense of community ownership and empowers individuals to have a direct say in the development of the public goods that they value. This decentralization also makes the funding ecosystem more resilient and less susceptible to capture by special interests.

**5. Scalability and Flexibility:** The QF model is designed to be both scalable and flexible. It can be applied to a wide range of public goods, from small-scale community projects to large-scale open-source software ecosystems. The mechanism can be adapted to different contexts by adjusting the size of the matching pool and the specific rules of the funding rounds. This adaptability makes QF a versatile tool for a variety of organizational settings.

## 3. Key Practices

Implementing Quadratic Funding effectively requires a set of key practices that ensure the integrity, fairness, and efficiency of the process. These practices have been developed and refined through real-world applications of QF, particularly within the Gitcoin ecosystem. They provide a practical guide for organizations and communities looking to adopt this innovative funding model.

**1. Establishing a Matching Pool:** The first and most crucial practice is the establishment of a matching pool. This is the central fund that will be used to amplify the individual contributions. The size of the matching pool is a key determinant of the overall impact of the QF round. Matching pools can be funded by a variety of sources, including philanthropic organizations, corporate sponsors, or even a portion of a community's own treasury.

**2. Defining the Scope and Eligibility of Projects:** It is essential to clearly define the scope of the funding round and the eligibility criteria for projects that can participate. This ensures that the funding is directed towards projects that align with the goals of the community and the purpose of the matching fund. For example, a QF round might be focused on funding open-source software, scientific research, or local community initiatives.

**3. Implementing Robust Identity Verification:** As mentioned in the core principles, Sybil resistance is paramount. Implementing a robust system for identity verification is a critical practice. This can involve a variety of techniques, such as social verification through platforms like Twitter or GitHub, or more advanced methods like digital identity solutions that use cryptographic proofs. The goal is to make it as difficult as possible for a single individual to create multiple accounts and game the system.

**4. Running Time-Bound Funding Rounds:** QF is typically implemented in discrete, time-bound funding rounds. This creates a sense of urgency and encourages concentrated participation from the community. The duration of the funding round should be clearly communicated to all participants, and the results should be made transparent at the end of the round.

**5. Providing a User-Friendly Platform:** The success of a QF round depends on the participation of a large number of individuals. Therefore, it is essential to provide a user-friendly platform that makes it easy for people to discover projects, make contributions, and track the results. The platform should be intuitive, accessible, and transparent, providing clear information about the matching formula and the impact of each contribution.

**6. Fostering a Culture of Reciprocity and Collaboration:** Beyond the technical implementation, fostering a culture of reciprocity and collaboration is a key practice for the long-term success of Quadratic Funding. This involves encouraging projects to support each other, share information, and work together to build a stronger ecosystem. It also involves educating the community about the principles of QF and the importance of their participation.

**7. Continuous Improvement and Experimentation:** Quadratic Funding is still a relatively new and evolving mechanism. Therefore, a key practice is to embrace a spirit of continuous improvement and experimentation. This involves collecting data from each funding round, analyzing the results, and using the insights to refine the process for future rounds. It may also involve experimenting with different variations of the QF formula or different approaches to identity verification.

## 4. Application Context

Quadratic Funding is a versatile pattern that can be applied in a wide range of contexts where the provision of public goods is a challenge. Its ability to aggregate collective preferences and overcome the free-rider problem makes it a valuable tool for any community or organization that seeks to foster a more democratic and efficient allocation of resources. The following are some of the key application contexts where QF has been successfully implemented or has the potential to make a significant impact.

**Open-Source Software Development:** This is the context where Quadratic Funding has had its most prominent success to date. The development of open-source software is a classic public goods problem, as the software is freely available to everyone, but its creation and maintenance require significant resources. Gitcoin has demonstrated the power of QF to fund a wide range of open-source projects, from infrastructure and developer tools to decentralized applications. By allowing the community of users and developers to directly fund the projects they value, QF has created a more sustainable and vibrant ecosystem for open-source innovation.

**Scientific Research:** The funding of scientific research is another area where QF could have a transformative impact. Traditional funding mechanisms for science are often centralized and bureaucratic, with a small number of grant-making bodies making decisions about which research projects to support. QF could provide a more decentralized and democratic alternative, allowing the scientific community and the public to directly fund the research they believe is most important. This could lead to a more diverse and innovative research landscape, with funding directed towards a wider range of ideas and approaches.

**Journalism and Media:** The decline of traditional business models for journalism has created a crisis in the provision of high-quality, independent media. QF offers a potential solution by providing a mechanism for communities to directly fund the journalists and media outlets they trust. This could help to create a more sustainable and resilient media ecosystem, less reliant on advertising revenue and more accountable to the public it serves.

**Local and Urban Public Projects:** QF can also be applied at the local level to fund a variety of urban public projects, such as parks, community gardens, and public art. By allowing residents to directly contribute to the projects they want to see in their neighborhoods, QF can foster a greater sense of community ownership and engagement. It can also help to ensure that public resources are allocated in a way that reflects the actual needs and desires of the community.

**Campaign Finance:** The influence of large donors in political campaigns is a major concern in many democracies. QF offers a potential solution by providing a system of public financing that amplifies the power of small-dollar donors. By matching small contributions with public funds, QF can reduce the reliance of candidates on large donors and special interests, and create a more level playing field for political competition.

## 5. Implementation

Implementing a Quadratic Funding mechanism involves a series of steps, from setting up the technical infrastructure to managing the social dynamics of the community. The following is a high-level overview of the implementation process, drawing on the best practices that have emerged from real-world applications of QF.

**1. Platform Development:** The first step is to develop or adopt a platform that can support the QF process. This platform should include features for project submission, user registration and identity verification, contribution processing, and the calculation and distribution of matching funds. The platform should be secure, transparent, and user-friendly, providing a seamless experience for both project creators and contributors.

**2. Securing the Matching Pool:** The next step is to secure the matching pool that will be used to amplify the individual contributions. As mentioned earlier, this can come from a variety of sources, such as philanthropic foundations, corporate sponsors, or a community-managed treasury. The size of the matching pool should be clearly communicated to the community, as it will determine the overall impact of the funding round.

**3. Establishing Governance and Rules:** It is essential to establish a clear set of rules and governance procedures for the QF round. This includes defining the eligibility criteria for projects, the duration of the funding round, and the process for resolving disputes. The governance model should be transparent and accountable, with clear lines of responsibility and decision-making authority.

**4. Onboarding Projects and Contributors:** Once the platform and rules are in place, the next step is to onboard projects and contributors. This involves promoting the funding round to the relevant communities, providing support to project creators, and educating contributors about the QF process. The goal is to attract a diverse range of high-quality projects and a large number of engaged contributors.

**5. Running the Funding Round:** The funding round itself is the core of the implementation process. During this period, contributors can make donations to the projects of their choice. The platform should provide real-time feedback on the matching funds, showing contributors the impact of their donations. This helps to create a dynamic and engaging experience, and encourages further participation.

**6. Distributing the Funds and Reporting the Results:** At the end of the funding round, the matching funds are calculated and distributed to the projects. It is essential to provide a transparent and detailed report of the results, showing the total amount of funding each project received, the number of contributors, and the distribution of the matching funds. This helps to build trust and accountability, and provides valuable data for future funding rounds.

**7. Iterating and Improving:** The final step is to iterate and improve the process based on the experience of the funding round. This involves collecting feedback from project creators and contributors, analyzing the data, and identifying areas for improvement. The goal is to create a learning loop that allows the QF mechanism to evolve and adapt over time.

## 6. Evidence & Impact

The most significant and well-documented evidence of the impact of Quadratic Funding comes from the Gitcoin Grants program. Since its inception, Gitcoin has used QF to distribute millions of dollars to thousands of open-source projects. These grants have had a profound impact on the Ethereum ecosystem and the broader open-source community, enabling the development of critical infrastructure, developer tools, and decentralized applications.

One of the key impacts of Gitcoin Grants has been the democratization of funding for open-source software. The program has enabled a long tail of projects to receive funding that they would have struggled to obtain through traditional means. This has led to a more diverse and vibrant ecosystem, with a wider range of ideas and approaches being explored.

Another important impact has been the fostering of a strong sense of community and collaboration. The QF process encourages projects to support each other and to engage with their users and contributors. This has helped to create a more positive and collaborative culture within the open-source community.

Beyond the world of open-source software, there is growing interest in the potential of QF to be applied in other contexts. The city of Boulder, Colorado, has experimented with using QF for participatory budgeting, and there are ongoing discussions about its potential for campaign finance reform. While these applications are still in their early stages, they demonstrate the growing recognition of QF as a powerful tool for collective decision-making.

The academic literature on Quadratic Funding is also growing. The original paper by Buterin, Hitzig, and Weyl has been widely cited, and there is a growing body of research exploring the theoretical properties of QF and its potential applications. This research is helping to build a more solid foundation for the continued development and adoption of this innovative funding mechanism.

## 7. Cognitive Era Considerations

As we move deeper into the Cognitive Era, an age characterized by the increasing importance of knowledge, information, and collective intelligence, the relevance of Quadratic Funding as an organizational pattern is likely to grow. The Cognitive Era presents a new set of challenges and opportunities for the provision of public goods, and QF is well-positioned to address them.

One of the key features of the Cognitive Era is the rise of decentralized networks and peer-to-peer collaboration. QF is a natural fit for this new paradigm, as it is an inherently decentralized mechanism that empowers communities to self-organize and fund the public goods they value. It provides a way to harness the collective intelligence of a network to make more informed and efficient funding decisions.

Another key feature of the Cognitive Era is the increasing importance of intangible public goods, such as open-source software, scientific knowledge, and creative content. These goods are often difficult to value and fund through traditional market mechanisms. QF provides a way to overcome this challenge by allowing communities to directly express their preferences and allocate resources accordingly.

Furthermore, the Cognitive Era is likely to see an increase in the demand for more participatory and democratic forms of governance. QF provides a powerful tool for participatory budgeting and other forms of collective decision-making. It allows communities to have a direct say in how public resources are allocated, fostering a greater sense of ownership and engagement.

However, the Cognitive Era also presents new challenges for the implementation of QF. The increasing sophistication of artificial intelligence and the potential for Sybil attacks to be automated at scale will require the development of more robust and sophisticated identity verification systems. The global and interconnected nature of the Cognitive Era will also require the development of new governance models for managing QF at a global scale.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
Quadratic Funding establishes a clear stakeholder architecture centered on contributors and project creators. Contributors are granted the Right to influence funding allocation through their donations, while creators have the Responsibility to deliver the proposed public good. The broader community is an implicit stakeholder, benefiting from the outcomes, though its Rights and Responsibilities are not explicitly defined within the mechanism itself.

**2. Value Creation Capability:**
The pattern excels at enabling collective value creation that extends far beyond direct economic output. By mathematically amplifying a broad base of support, it specifically channels resources towards projects with high social, ecological, and knowledge value that are typically underfunded by traditional markets. This directly enhances a system's capability to generate diverse forms of value.

**3. Resilience & Adaptability:**
QF enhances system resilience by diversifying its funding base, making it less fragile and susceptible to the whims of a few large funders. The mechanism is highly adaptable, as communities can continuously adjust their collective priorities in successive funding rounds. This allows the system to respond to change and maintain coherence by constantly re-aligning resource allocation with community-wide preferences.

**4. Ownership Architecture:**
The pattern re-frames ownership away from equity and towards stewardship of collective resources. While it doesn't define ownership of the resulting public goods, it establishes a form of collective ownership over the allocation process itself. The Right to participate is tied to the Responsibility of contribution, creating a system where stakeholdership is earned, not just purchased.

**5. Design for Autonomy:**
Quadratic Funding is exceptionally well-suited for autonomous systems, as demonstrated by its successful implementation in DAOs and other distributed networks. Its mathematical core allows for low-overhead coordination, enabling it to function as a semi-autonomous allocation engine. However, its full autonomy depends on robust, often automated, Sybil resistance mechanisms to ensure the integrity of contributions.

**6. Composability & Interoperability:**
This pattern is highly composable, designed to integrate seamlessly with other patterns to build more complex value-creation systems. It naturally interoperates with DAOs for treasury management, reputation systems for weighting contributions, and various governance frameworks for setting rules. QF can act as the economic engine within a larger, modular institutional stack.

**7. Fractal Value Creation:**
The core logic of Quadratic Funding is fractal, meaning it can be effectively applied at virtually any scale. The value-creation mechanism works equally well for a small local community funding a park, a digital ecosystem funding open-source code, or a nation-state implementing participatory budgeting. This scalability allows the pattern to create coherent value-creation systems from the micro to the macro level.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
Quadratic Funding is a powerful engine for collective value creation, strongly aligning with the core principles of a Commons. It provides a clear, scalable, and adaptable architecture for translating broad community preference into tangible support for public goods. Its primary function is to *enable* and *finance* value creation rather than being the complete value-creating system itself, which is why it is classified as a Value Creation Enabler.

**Opportunities for Improvement:**
- Integrate with reputation systems to give more weight to trusted contributors, enhancing Sybil resistance and rewarding long-term engagement.
- Develop clearer governance patterns for defining the scope of eligible projects and managing the matching pool to prevent capture.
- Explicitly define the Rights and Responsibilities of the commons being created (e.g., licensing, access, maintenance) as a condition of funding.

## 9. Resources & References

[1] Buterin, V., Hitzig, Z., & Weyl, E. G. (2018). A Flexible Design for Funding Public Goods. *arXiv preprint arXiv:1809.06421*. [https://arxiv.org/abs/1809.06421](https://arxiv.org/abs/1809.06421)

[2] Gitcoin. (n.d.). *WTF is Quadratic Funding?* Retrieved from [https://qf.gitcoin.co/](https://qf.gitcoin.co/)

[3] wtfisqf.com. (n.d.). *WTF is Quadratic Funding?* Retrieved from [https://www.wtfisqf.com/](https://www.wtfisqf.com/)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/quadratic-funding/](https://commons-os.github.io/patterns/domain/quadratic-funding/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/quadratic-funding.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/quadratic-funding.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
