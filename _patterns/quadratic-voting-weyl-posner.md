---
id: pat_01kg5023w7f0htcqtrz67zjgdj
page_url: https://commons-os.github.io/patterns/quadratic-voting-weyl-posner/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/quadratic-voting-weyl-posner.md
slug: quadratic-voting-weyl-posner
title: Quadratic Voting
aliases:
- QV
version: 1.0
created: 2026-01-28 00:00:00+00:00
modified: 2026-01-28 00:00:00+00:00
classification:
  universality: domain
  domain: governance
  category: methodology
  era:
  - digital
  - cognitive
  origin:
  - academic
  - radicalxchange
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- higgerix
- cloudsters
sources:
- https://www.aeaweb.org/articles?id=10.1257/pandp.20181002
- https://chicagounbound.uchicago.edu/law_and_economics/643/
- https://econ.columbia.edu/wp-content/uploads/sites/32/2017/10/draft.8.25.2018.pdf
- https://www.radicalxchange.org/wiki/quadratic-voting/
- https://en.wikipedia.org/wiki/Quadratic_voting
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Quadratic Voting (QV) is a collective decision-making procedure that is designed to allow for a more nuanced expression of preferences than traditional one-person-one-vote systems. It addresses the issue of preference intensity by allowing participants to purchase votes on a given issue, with the cost of votes increasing quadratically. This means that the cost of casting *n* votes is *n*<sup>2</sup> vote credits. This mechanism allows individuals who feel strongly about a particular issue to have a greater say, while the increasing marginal cost of each additional vote prevents any single individual or small group from dominating the decision-making process. The core problem that Quadratic Voting seeks to solve is the "tyranny of the majority," a situation where a large group of individuals with weak preferences can consistently overrule a smaller group with strong preferences. By allowing for the expression of preference intensity, QV aims to produce outcomes that better reflect the overall welfare of the group.

The origin of Quadratic Voting can be traced back to the work of economists William Vickrey, Edward H. Clarke, and Theodore Groves on mechanism design, specifically the Vickrey-Clarke-Groves (VCG) mechanism. However, it was political scientist and Microsoft researcher E. Glen Weyl, along with his co-author Eric Posner, who fully developed and popularized the concept in their 2018 book, *Radical Markets: Uprooting Capitalism and Democracy for a Just Society*. They proposed QV as a way to reform voting systems in both the public and private sectors, arguing that it could lead to more efficient and equitable outcomes.

### 2. Core Principles

1.  **Expression of Preference Intensity:** Unlike traditional voting systems where each person gets a single vote of equal weight, Quadratic Voting allows individuals to express the intensity of their preferences. Voters can allocate more votes to issues they care deeply about, providing a richer and more nuanced signal of the collective will.

2.  **Equality of Voice Credits:** While voters can cast an unequal number of votes, every participant starts with an equal budget of "voice credits." This ensures a fundamental equality of potential influence, upholding the democratic principle of one-person-one-vote at the level of the credit allocation.

3.  **Increasing Marginal Cost:** The cost of each additional vote increases quadratically. This is the core mechanic that makes the system work. The first vote costs 1 credit, the second costs 3 additional credits (for a total of 4), the third costs 5 additional credits (for a total of 9), and so on. This increasing cost forces voters to be judicious in their allocation of credits, preventing them from easily concentrating all their power on a single issue and encouraging them to consider trade-offs.

4.  **Optimal Social Choice:** The theoretical foundation of Quadratic Voting is that it provides a mechanism for achieving a more socially optimal outcome. By aggregating not just the direction but also the intensity of preferences, QV aims to select the option that maximizes the total welfare of the group, as measured by the collective willingness to spend vote credits.

5.  **Mitigation of the Tyranny of the Majority:** A key goal of QV is to solve the problem of the tyranny of the majority, where a large group with mild preferences can consistently defeat a smaller group with intense preferences. QV empowers passionate minorities to have a greater influence on the issues that matter most to them, leading to more equitable and balanced outcomes.

### 3. Key Practices

1.  **Issuing Voice Credits:** Every participant in a Quadratic Voting process is given an equal budget of "voice credits." These credits are the currency used to purchase votes. The number of credits issued can be adjusted depending on the number of issues to be voted on and the desired level of engagement. For example, in a community budget decision with many competing projects, a larger number of credits might be issued to allow for more granular expression of preferences.

2.  **Designing the Ballot:** The ballot in a QV system presents a list of issues or proposals to be voted on. For each issue, voters can choose to cast votes in favor or against. The design of the ballot is crucial for ensuring clarity and preventing voter confusion. For instance, in the case of the Colorado Democratic Party's use of QV for platform creation, the ballot consisted of a series of proposed planks, and members could allocate their credits to the planks they most wanted to see included.

3.  **Casting Votes:** Voters allocate their voice credits to the issues on the ballot. The interface for casting votes typically shows the number of votes a certain number of credits will buy. For example, a voter might be shown a slider or a text box where they can input the number of credits they want to allocate to a particular issue, and the interface will dynamically update to show the corresponding number of votes. This provides immediate feedback to the voter and helps them make informed decisions about how to allocate their limited credits.

4.  **Tabulating the Results:** After the voting period has closed, the votes are tabulated. For each issue, the total number of votes in favor is compared to the total number of votes against. The option with the most votes wins. In some cases, the results may be used to rank a list of proposals, with the proposals receiving the most net positive votes being prioritized.

5.  **Ensuring Voter Anonymity and Preventing Collusion:** To ensure the integrity of the voting process, it is important to have mechanisms in place to prevent collusion and vote-buying. One common practice is to make individual votes anonymous, so that voters cannot prove to others how they voted. Another is to use a secure and verifiable identity system to prevent individuals from creating multiple accounts (a Sybil attack). In the context of blockchain-based QV systems, cryptographic techniques can be used to ensure both anonymity and verifiability.

6.  **Applying QV to Budgeting and Resource Allocation:** A key application of Quadratic Voting is in participatory budgeting and resource allocation. In this context, a community is presented with a list of proposed projects and a fixed budget. Community members use their voice credits to vote for the projects they want to see funded. The projects that receive the most votes are then funded until the budget is exhausted. This practice has been used by organizations like the Gitcoin community to fund open-source projects.

7.  **Utilizing QV for Polling and Market Research:** Quadratic Voting can be a powerful tool for gathering more accurate and nuanced data on public opinion than traditional polling methods. By forcing respondents to consider trade-offs and express the intensity of their preferences, QV can provide a more realistic picture of what a group truly wants. For example, a company could use QV to survey its customers about potential new product features, with the results providing a clear indication of which features are most desired.

### 4. Application Context

**Best Used For:**

*   **Participatory Budgeting:** Allowing community members to decide how a public budget should be allocated across a range of proposed projects.
*   **Corporate Governance:** Giving a voice to a wider range of stakeholders (e.g., employees, customers) in corporate decision-making, beyond just shareholders.
*   **Platform Governance:** Enabling users of a digital platform to have a say in its rules, features, and future development.
*   **Polling and Surveys:** Gathering more accurate and nuanced data on public opinion by forcing respondents to weigh their preferences.
*   **Prioritizing Features or Projects:** Helping teams or organizations decide which features to build or which projects to pursue based on the collective preference of the group.

**Not Suitable For:**

*   **Binary, High-Stakes Decisions:** In situations where there are only two options and the stakes are very high (e.g., a national election for a head of state), the potential for strategic voting and the complexity of the system may make it less suitable than traditional voting methods.
*   **Decisions Requiring Expert Knowledge:** For highly technical decisions that require specialized expertise, QV may not be the best approach, as it gives equal weight to the preferences of both informed and uninformed participants.
*   **Situations with Low Trust or High Potential for Collusion:** In environments where there is a high degree of distrust or a strong incentive for collusion, the integrity of the QV process can be compromised.

**Scale:**

Quadratic Voting can be applied at various scales, from small teams to large-scale ecosystems:

*   **Team:** A team can use QV to decide on project priorities or to allocate a small budget.
*   **Department:** A department can use QV to decide on its strategic direction or to allocate resources across different teams.
*   **Organization:** An entire organization can use QV for corporate governance, allowing employees to have a say in company policy.
*   **Multi-Organization/Ecosystem:** QV can be used to govern a network of organizations or a digital ecosystem, such as a blockchain community or a platform cooperative.

**Domains:**

Quadratic Voting is being explored and applied in a variety of domains, including:

*   **Government and Public Sector:** For participatory budgeting, public consultations, and even in the legislative process.
*   **Technology and Software Development:** For governing open-source projects, prioritizing features, and making decisions in decentralized autonomous organizations (DAOs).
*   **Corporate and Organizational Governance:** As an alternative to traditional shareholder voting.
*   **Media and Journalism:** For allowing readers to have a say in the editorial direction of a publication.
*   **Urban Planning and Development:** For engaging residents in decisions about their local communities.

### 5. Implementation

**Prerequisites:**

*   **A Clearly Defined Electorate:** It is essential to have a clear and verifiable list of eligible voters. This is necessary to prevent Sybil attacks, where a single individual creates multiple accounts to gain a disproportionate amount of influence.
*   **A Well-Defined Set of Issues:** The issues to be voted on should be clearly defined and presented to the voters in an understandable way. Ambiguous or poorly worded proposals can lead to confusion and undermine the legitimacy of the results.
*   **A User-Friendly Voting Platform:** The platform used to conduct the vote should be easy to use and provide clear feedback to the voters. It should show them how many votes their credits will buy and how their allocation of credits will affect the outcome.
*   **A Communication Channel:** It is important to have a way to communicate with the voters before, during, and after the vote. This can be used to explain the rules of the process, answer questions, and announce the results.

**Getting Started:**

1.  **Define the Scope and Purpose of the Vote:** The first step is to be clear about what you are trying to achieve with the vote. Are you trying to allocate a budget, prioritize a list of projects, or gauge public opinion on a particular issue?
2.  **Choose a Voting Platform:** There are a number of platforms available for conducting Quadratic Votes, ranging from simple spreadsheets to sophisticated online tools. The choice of platform will depend on the scale and complexity of the vote.
3.  **Onboard and Educate the Voters:** It is important to make sure that the voters understand how Quadratic Voting works. This can be done through a combination of written materials, videos, and interactive tutorials.
4.  **Conduct the Vote:** Once the voters have been onboarded, the vote can be conducted. It is important to set a clear timeline for the voting period and to provide support to voters who may have questions or encounter technical difficulties.
5.  **Analyze and Communicate the Results:** After the voting period has closed, the results should be analyzed and communicated to the voters. This should include a clear explanation of which options won and how the votes were distributed.

**Common Challenges:**

*   **Voter Apathy and Fatigue:** As with any voting system, voter apathy can be a challenge. It is important to make the voting process as engaging and easy as possible to encourage participation.
*   **Collusion and Vote-Buying:** The potential for collusion and vote-buying is a significant concern in any voting system. While QV has some built-in protections against these behaviors, it is important to have additional mechanisms in place to prevent them, such as voter anonymity and a secure identity system.
*   **The 

### 6. Evidence & Impact

**Notable Adopters:**

*   **The Colorado Democratic Party:** Used QV to help decide its party platform. This was one of the first large-scale, real-world applications of the system in a political context.
*   **Gitcoin:** A platform for funding open-source projects, Gitcoin uses a variant of QV called Quadratic Funding (QF) to allocate matching funds to projects based on community contributions.
*   **The Taiwanese Government:** Has used QV in its vTaiwan process, an online platform for digital democracy, to solicit and prioritize public opinion on a range of policy issues.
*   **RadicalxChange:** The organization co-founded by Glen Weyl, uses QV for its own internal governance and to promote the adoption of the system more broadly.
*   **Various Blockchain Communities and DAOs:** A number of decentralized autonomous organizations (DAOs) and other blockchain-based communities have adopted QV for their governance processes.

**Documented Outcomes:**

*   **Increased Engagement and Participation:** In many cases, the use of QV has been shown to lead to higher levels of engagement and participation than traditional voting methods. The ability to express the intensity of one's preferences can be a powerful motivator for people to get involved.
*   **More Nuanced and Representative Outcomes:** QV has been shown to produce outcomes that are more nuanced and representative of the collective will than simple majority-rule voting. By giving more weight to the preferences of passionate minorities, QV can help to prevent the tyranny of the majority and lead to more equitable outcomes.
*   **Improved Legitimacy and Buy-in:** Because QV is a more expressive and participatory form of decision-making, it can lead to a greater sense of legitimacy and buy-in from the community. When people feel that their voices have been heard and that their preferences have been taken into account, they are more likely to accept and support the final decision.

**Research Support:**

*   **"Quadratic Voting: How Mechanism Design Can Radicalize Democracy" by Steven P. Lalley and E. Glen Weyl:** This is the foundational paper that introduced the concept of QV and laid out its theoretical underpinnings. The paper argues that QV is the only voting system that is both efficient and democratic, in the sense that it maximizes social welfare while still giving every individual an equal say.
*   **"Quadratic Voting as Efficient Corporate Governance" by Eric A. Posner and E. Glen Weyl:** This paper applies the concept of QV to the context of corporate governance, arguing that it can be a more efficient and equitable way to make decisions in a firm than traditional shareholder voting.
*   **"Storable Votes and Quadratic Voting. An Experiment on Four California Propositions" by Alessandra Casella, Luis Sanchez, and Thomas Palfrey:** This experimental study compares QV to other voting systems and finds that it performs well in terms of both efficiency and preference revelation.

### 7. Cognitive Era Considerations

**Cognitive Augmentation Potential:**

*   **AI-Powered Proposal Generation and Analysis:** AI can be used to help communities generate and analyze proposals. For example, an AI could be used to identify areas of need within a community and to generate a range of potential solutions. It could also be used to analyze the potential impacts of different proposals, providing voters with more information on which to base their decisions.
*   **Personalized Voting Recommendations:** AI could be used to provide voters with personalized recommendations on how to allocate their vote credits. By analyzing a voter's past voting history and stated preferences, an AI could suggest a portfolio of votes that would be most likely to advance their interests.
*   **Automated Collusion Detection:** AI can be used to analyze voting patterns to detect and flag potential instances of collusion or vote-buying. This can help to ensure the integrity of the voting process and to prevent bad actors from gaming the system.

**Human-Machine Balance:**

While AI can be a powerful tool for augmenting the QV process, it is important to maintain a balance between human and machine intelligence. The ultimate decision of how to allocate one's vote credits should always rest with the individual voter. AI should be seen as a tool for providing information and recommendations, not for making decisions on behalf of voters. The uniquely human aspects of the process, such as deliberation, negotiation, and the formation of shared values, should be preserved and enhanced, not replaced by automation.

**Evolution Outlook:**

In the cognitive era, we can expect to see the continued evolution of Quadratic Voting and other forms of deliberative democracy. We may see the development of more sophisticated AI-powered tools for proposal generation, analysis, and recommendation. We may also see the integration of QV with other technologies, such as virtual and augmented reality, to create more immersive and engaging deliberative experiences. As our ability to collect and process large amounts of data increases, we may also see the development of new and more sophisticated ways of measuring and aggregating preferences, leading to even more efficient and equitable outcomes.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
Quadratic Voting (QV) defines stakeholder Rights through an equal allocation of "voice credits" to all participants, providing a baseline of potential influence. The Responsibility lies with each stakeholder to strategically allocate these credits to express the intensity of their preferences. However, the architecture's inclusiveness is entirely dependent on how the electorate is defined, as the pattern itself does not prescribe how to include non-human or future-generational stakeholders.

**2. Value Creation Capability:**
The pattern excels at enabling collective value creation by moving beyond simple majority rule to a more nuanced aggregation of preferences. This allows a community to identify and prioritize what it truly values, fostering better social outcomes and a stronger sense of shared purpose. The value created is primarily in the form of improved collective intelligence and more efficient resource allocation, which directly supports the creation of social and knowledge value.

**3. Resilience & Adaptability:**
QV enhances a system's resilience by providing a formal mechanism for minority voices with strong convictions to be heard, preventing the "tyranny of the majority." This allows the system to better register and adapt to important but non-obvious signals, increasing its capacity to maintain coherence and adapt to changing internal and external conditions.

**4. Ownership Architecture:**
The pattern re-frames ownership of a decision from a binary vote to a more granular stake represented by voice credits. This decouples decision-making power from monetary wealth, defining ownership as the right to influence outcomes and the responsibility to do so thoughtfully. While it doesn't present a complete ownership architecture, it provides a critical component for one by focusing on influence rather than equity.

**5. Design for Autonomy:**
Quadratic Voting is exceptionally well-suited for autonomous systems, as its mathematical foundation is easily implemented in code. It is already widely used in DAOs and other distributed systems for governance, demonstrating its compatibility with AI-driven environments. The potential for AI to augment the process, from proposal analysis to collusion detection, further highlights its low coordination overhead and suitability for autonomous design.

**6. Composability & Interoperability:**
This pattern is highly composable and can be integrated with a wide range of other governance and value-creation patterns. It can be combined with reputation systems, deliberative processes like polling, or funding mechanisms like in the case of Gitcoin's Quadratic Funding. This interoperability allows it to serve as a core decision-making module within larger, more complex systems of systems.

**7. Fractal Value Creation:**
The logic of QV is inherently fractal, as the core mechanism of allocating and spending voice credits can be applied effectively at any scale. The pattern can be used for decision-making within a small team, a large organization, or a global digital ecosystem. This scalability allows the same value-creation logic to be deployed across different levels of a system, creating coherent governance structures.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
Quadratic Voting is a powerful and well-defined mechanism that strongly enables resilient collective value creation. It provides a sophisticated tool for preference aggregation that is adaptable, scalable, and highly compatible with autonomous systems. It scores a 4 because while it is a critical *enabler* of a commons, it is not a complete *architecture* in itself; its effectiveness is contingent on a well-defined stakeholder map and ownership structure, which must be established by other patterns.

**Opportunities for Improvement:**
- Integrate with identity and reputation patterns to create more robust stakeholder architectures that are resistant to collusion and Sybil attacks.
- Combine with patterns for deliberative democracy to ensure that the preferences being expressed are well-informed and considered.
- Develop clear guidelines for defining the electorate to ensure that all relevant stakeholders, including non-human and future generations, are represented in the decision-making process.

### 9. Resources & References

**Essential Reading:**

*   Posner, E. A., & Weyl, E. G. (2018). *Radical Markets: Uprooting Capitalism and Democracy for a Just Society*. Princeton University Press. (This book provides a comprehensive and accessible introduction to Quadratic Voting and its potential applications.)
*   Lalley, S. P., & Weyl, E. G. (2018). Quadratic Voting: How Mechanism Design Can Radicalize Democracy. *AEA Papers and Proceedings*, *108*, 33–37. (The foundational academic paper on Quadratic Voting.)
*   Posner, E. A., & Weyl, E. G. (2013). *Quadratic Voting as Efficient Corporate Governance*. (Coase-Sandor Institute for Law & Economics Working Paper No. 643). (This paper explores the application of QV to corporate governance.)

**Organizations & Communities:**

*   **RadicalxChange:** A global movement for social change that promotes Quadratic Voting and other innovative social technologies. ([https://www.radicalxchange.org/](https://www.radicalxchange.org/))
*   **Gitcoin:** A platform that uses Quadratic Funding, a variant of QV, to fund open-source projects. ([https://gitcoin.co/](https://gitcoin.co/))

**Tools & Platforms:**

*   **RxC QV:** RadicalxChange’s in-house tool for running QV elections.
*   **Democracy Earth:** A non-profit organization that builds open-source, decentralized governance platforms, including implementations of QV.

**References:**

[1] Lalley, S. P., & Weyl, E. G. (2018). Quadratic Voting: How Mechanism Design Can Radicalize Democracy. *AEA Papers and Proceedings*, *108*, 33–37.

[2] Posner, E. A., & Weyl, E. G. (2013). *Quadratic Voting as Efficient Corporate Governance*. (Coase-Sandor Institute for Law & Economics Working Paper No. 643).

[3] Casella, A., Sanchez, L., & Palfrey, T. (2018). *Storable Votes and Quadratic Voting. An Experiment on Four California Propositions*.

[4] RadicalxChange. (n.d.). *Quadratic Voting*. Retrieved from [https://www.radicalxchange.org/wiki/quadratic-voting/](https://www.radicalxchange.org/wiki/quadratic-voting/)

[5] Wikipedia. (2023). *Quadratic voting*. Retrieved from [https://en.wikipedia.org/wiki/Quadratic_voting](https://en.wikipedia.org/wiki/Quadratic_voting)
