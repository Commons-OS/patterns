---
id: pat_01kg5023wbfw1azjwp3zgdr86p
page_url: https://commons-os.github.io/patterns/futarchy-robin-hanson/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/futarchy-robin-hanson.md
slug: futarchy-robin-hanson
title: Futarchy
aliases:
- Decision Markets
- Prediction Markets Governance
version: 1.0
created: 2026-01-28 00:00:00+00:00
modified: 2026-01-28 00:00:00+00:00
classification:
  universality: domain
  domain: operations
  category:
  - framework
  era:
  - digital
  - cognitive
  origin:
  - academic
  status: draft
  commons_alignment: 4
  commons_domain:
  - business
  - startup
generalizes_from: []
specializes_to:
- pat_01kg5023yvehgrw2tgchwaj9vp
enables: []
requires: []
related: []
contributors:
- higgerix
- cloudsters
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Futarchy is a form of governance, originally proposed by economist Robin Hanson, that uses prediction markets to make decisions. The core idea is to separate the process of defining what we want (values) from the process of figuring out how to get it (beliefs). In a futarchy, elected officials or a similar democratic process would be responsible for defining a metric for national (or organizational) welfare. This metric would serve as the goal to be maximized. Prediction markets would then be used to bet on which proposed policies or actions are most likely to achieve that goal. The policy with the highest predicted positive impact on the welfare metric would be implemented.

This matters because traditional governance systems, including democracies, often struggle to aggregate information effectively and are susceptible to political biases and the influence of special interests. Futarchy aims to solve this by creating a system where decisions are based on the collective intelligence of the market, which is incentivized to be accurate. The origin of futarchy can be traced back to Robin Hanson's 1999 paper "Decision Markets" and was more formally introduced in his 2000 paper, "Futarchy: Vote Values, But Bet Beliefs." The idea has since gained traction in various domains, particularly within the blockchain and decentralized autonomous organization (DAO) communities, as a potential mechanism for more effective and decentralized governance.

### 2. Core Principles

1.  **Vote on Values, Bet on Beliefs:** This is the foundational principle of futarchy. It proposes a separation of concerns in governance. The determination of what a society or organization values (e.g., economic growth, environmental quality, social equity) is left to democratic processes. However, the beliefs about which policies will best achieve those values are determined by prediction markets. This principle aims to leverage the strengths of both democracy (for value alignment) and markets (for information aggregation).

2.  **Information Aggregation through Prediction Markets:** Futarchy is built on the premise that prediction markets are superior institutions for aggregating dispersed information. By allowing individuals to bet on the outcomes of policies, these markets can synthesize the knowledge and insights of a wide range of participants, including experts and those with specialized information. The resulting market prices are seen as the most accurate available forecasts of policy consequences.

3.  **Incentivized Accuracy:** The effectiveness of prediction markets in futarchy stems from the fact that participants are financially incentivized to be correct. To participate, one must "put their money where their mouth is." Those who make accurate predictions profit, while those who are wrong lose their stake. This mechanism encourages participants to be thoughtful and well-informed, and it tends to filter out noise and misinformation over time.

4.  **Ex-Post Welfare Measurement:** For futarchy to function, there must be a clearly defined and measurable metric of welfare that can be assessed after a policy has been implemented. This metric, which could be a composite of various indicators like GDP, happiness surveys, and environmental data, is determined through a democratic process. The ability to measure outcomes is crucial for settling bets and ensuring the accountability of the system.

5.  **Conditional Markets for Policy Selection:** The core mechanism for policy selection in futarchy involves the use of conditional prediction markets. For each proposed policy, two markets are created. One market predicts the value of the welfare metric if the policy is adopted, and the other predicts the value if the policy is not adopted. The policy is implemented only if the market predicts a higher welfare metric with the policy than without it.

### 3. Key Practices

1.  **Defining a Clear and Measurable Welfare Metric:** The first and most critical practice is to establish a clear, unambiguous, and measurable metric for welfare. This metric is the objective function that the prediction markets will try to maximize. The process of defining this metric should be democratic and inclusive, reflecting the values of the organization or society. Examples of welfare metrics could include a combination of GDP, leisure time, environmental quality, and public health indicators.

2.  **Proposing Policies:** Once the welfare metric is defined, any member of the community can propose policies or actions that they believe will improve it. These proposals must be specific and actionable, with a clear description of what will be done if the policy is implemented.

3.  **Creating Conditional Prediction Markets:** For each proposal, two conditional prediction markets are created. One market predicts the value of the welfare metric if the policy is implemented (the "pass" market), and the other predicts the value if the policy is not implemented (the "fail" market). These markets allow participants to bet on the outcomes of the policy.

4.  **Trading in the Prediction Markets:** Participants, or "traders," buy and sell shares in the conditional markets based on their beliefs about the likely impact of the proposed policy. This trading activity aggregates the collective intelligence of the market, and the prices in the two markets reflect the market's confidence in the policy's success or failure.

5.  **Implementing the Winning Policy:** After a predetermined trading period, the prices of the two markets are compared. If the price in the "pass" market is significantly higher than the price in the "fail" market, it indicates that the market believes the policy will have a positive impact on the welfare metric. In this case, the policy is automatically implemented.

6.  **Settling the Markets and Rewarding Traders:** Once the outcome of the policy is known (i.e., the welfare metric is measured at a future date), the prediction markets are settled. Traders who made correct predictions are rewarded, while those who made incorrect predictions lose their stake. This financial incentive encourages participants to be well-informed and to make accurate predictions.

7.  **Using Conditional Tokens (in DAOs):** In the context of DAOs and blockchain-based futarchy, conditional tokens are used to represent shares in the prediction markets. These tokens allow for the creation of decentralized and trustless prediction markets, where the rules of the market are enforced by smart contracts.

### 4. Application Context

-   **Best Used For**:
    -   **Corporate Governance:** Making strategic decisions in a company, such as whether to launch a new product, acquire another company, or change the company's a CEO.
    -   **Public Policy:** Deciding on government policies, such as tax rates, environmental regulations, or healthcare reforms.
    -   **DAO Governance:** Governing decentralized autonomous organizations, where it can be used to make decisions about protocol upgrades, treasury management, and other important issues.
    -   **Project Management:** Deciding on the best course of action for a complex project, such as which features to prioritize or which technical approach to take.
    -   **Non-Profit Organizations:** Making decisions about how to allocate resources to best achieve the organization's mission.

-   **Not Suitable For**:
    -   **Decisions Requiring Immediate Action:** The process of creating and settling prediction markets can take time, making it unsuitable for decisions that need to be made quickly.
    -   **Decisions with Unmeasurable Outcomes:** Futarchy requires a clear and measurable welfare metric. If the outcome of a decision cannot be measured, it is not possible to use futarchy.
    -   **Decisions with Strong Moral or Ethical Dimensions:** While futarchy can be used to make decisions about values, it is not well-suited for decisions that involve fundamental moral or ethical questions that cannot be easily quantified.

-   **Scale**: Individual/Team/Department/Organization/Multi-Organization/Ecosystem

-   **Domains**: Futarchy is a domain-agnostic pattern that can be applied in any industry or sector where there is a need to make complex decisions with uncertain outcomes. It is particularly well-suited for domains where there is a large amount of dispersed information that needs to be aggregated, such as in finance, technology, and public policy.

### 5. Implementation

-   **Prerequisites**:
    -   A clearly defined and measurable welfare metric.
    -   A community of participants who are willing to trade in the prediction markets.
    -   A platform for creating and settling prediction markets.
    -   A mechanism for implementing the winning policies.

-   **Getting Started**:
    1.  **Define the Welfare Metric:** The first step is to define the welfare metric that will be used to evaluate the success of policies. This should be done through a democratic and inclusive process.
    2.  **Create a Proposal:** Once the welfare metric is defined, anyone can create a proposal for a policy that they believe will improve it.
    3.  **Create the Prediction Markets:** For each proposal, two conditional prediction markets are created.
    4.  **Trade in the Markets:** Participants trade in the prediction markets based on their beliefs about the likely impact of the proposed policy.
    5.  **Implement the Winning Policy:** After a predetermined trading period, the policy with the highest predicted positive impact on the welfare metric is implemented.

-   **Common Challenges**:
    -   **Market Manipulation:** There is a risk that wealthy individuals or groups could try to manipulate the prediction markets to their own advantage.
    -   **Thin Markets:** If there are not enough participants in the prediction markets, the market prices may not be accurate.
    -   **Defining the Welfare Metric:** It can be challenging to define a welfare metric that accurately reflects the values of the community.
    -   **Goodhart's Law:** When a measure becomes a target, it ceases to be a good measure. There is a risk that people will try to game the welfare metric, rather than actually improving welfare.

-   **Success Factors**:
    -   A large and diverse community of participants in the prediction markets.
    -   A well-defined and robust welfare metric.
    -   A transparent and fair process for creating and settling the prediction markets.
    -   A strong commitment to implementing the winning policies.

### 6. Evidence & Impact

-   **Notable Adopters**:
    -   **Meta-DAO:** The first real-world application of futarchy, the Meta-DAO is a decentralized autonomous organization that uses prediction markets to make decisions about its governance and investments. It operates on the Solana blockchain.
    -   **GnosisDAO:** While not a pure futarchy, GnosisDAO has used prediction markets for some of its governance decisions.
    -   **Augur:** A decentralized prediction market platform that can be used to create futarchy-style prediction markets.
    -   **Zeitgeist:** A decentralized network for creating, trading, and resolving prediction markets, with a focus on futarchy.

-   **Documented Outcomes**:
    -   The Meta-DAO has successfully used futarchy to make a number of decisions, including a proposal to create a spot market for its native token, META. The market correctly predicted that the proposal would have a positive impact on the value of the token.
    -   In another example, a wealthy individual attempted to use their wealth to influence a proposal in the Meta-DAO, but the market ultimately rejected the proposal, demonstrating the resilience of futarchy to manipulation.

-   **Research Support**:
    -   **"Shall We Vote on Values, But Bet on Beliefs?" by Robin Hanson:** This paper provides the theoretical foundation for futarchy and argues that it is a more efficient and effective form of governance than traditional democracy.
    -   **"Decision Markets" by Robin Hanson:** This paper explores the use of prediction markets for making decisions in a variety of contexts, including corporate governance and public policy.

### 7. Cognitive Era Considerations

-   **Cognitive Augmentation Potential**: AI and automation can significantly enhance futarchy. AI agents could act as sophisticated traders in prediction markets, analyzing vast amounts of data to make more accurate predictions. Automation can streamline the process of creating and settling prediction markets, making the system more efficient and scalable. AI could also be used to help define and measure the welfare metric, by analyzing a wide range of data sources to identify the factors that are most important to human well-being.

-   **Human-Machine Balance**: While AI can play a powerful role in futarchy, humans will still have a critical role to play. Humans will be responsible for defining the values that are encoded in the welfare metric, and for overseeing the system to ensure that it is fair and transparent. Humans will also be needed to make decisions in cases where the prediction markets are unable to provide a clear answer, or where there are strong moral or ethical considerations.

-   **Evolution Outlook**: As AI and other cognitive technologies continue to develop, futarchy is likely to evolve as well. We may see the emergence of more sophisticated prediction markets, with AI agents playing an increasingly important role. We may also see the development of new ways of defining and measuring welfare, that take into account a wider range of human values. Ultimately, the goal is to create a system of governance that is both intelligent and humane, and that is able to make decisions that are in the best interests of all.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
Futarchy distributes Rights and Responsibilities by separating the definition of values (voting) from the execution of beliefs (betting). However, this architecture primarily empowers stakeholders with capital to participate in prediction markets, potentially marginalizing non-monetized stakeholders like the environment or future generations. Their inclusion depends entirely on their representation within the democratically chosen welfare metric, which is a significant structural dependency.

**2. Value Creation Capability:**
The pattern is explicitly designed to enhance collective value creation by optimizing decisions against a defined welfare metric. This metric can encompass social, ecological, and knowledge value, but the mechanism's focus is on aggregating information for economic efficiency. The system's capability to create holistic value is therefore contingent on the breadth and depth of the initial value metric defined by its stakeholders.

**3. Resilience & Adaptability:**
Futarchy is designed for adaptability, using prediction markets to dynamically select policies that are most likely to succeed in complex environments. The ability to update the core welfare metric allows the system to evolve its goals over time, maintaining coherence by tying all actions back to this shared objective. However, its resilience is vulnerable to market manipulation and low participation (thin markets), which can compromise the integrity of its decision-making process.

**4. Ownership Architecture:**
Ownership is implicitly defined through participation rights: the right to vote on values and the right to bet on beliefs. It does not fundamentally redefine ownership beyond a form of monetary and informational equity, as influence is directly tied to the capital and knowledge required to make successful predictions. The model does not explicitly architect for non-monetary forms of stakeholding or responsibility.

**5. Design for Autonomy:**
Futarchy is exceptionally well-suited for autonomous systems, making it highly compatible with DAOs and AI agents. Its low coordination overhead, where decisions are automatically triggered by market outcomes, makes it a powerful tool for decentralized governance. AI agents can act as sophisticated participants in the prediction markets, potentially increasing the system's overall accuracy and efficiency.

**6. Composability & Interoperability:**
This pattern is highly modular and can be combined with other governance patterns to create more sophisticated systems. For instance, the value-setting process can be managed by a different pattern like Sociocracy, while Futarchy handles the policy execution. This composability allows it to serve as a core decision-making engine within a larger, multi-pattern governance framework.

**7. Fractal Value Creation:**
The core logic of separating values from beliefs and using markets to predict outcomes can be applied at multiple scales. A small team can use it for project management, a corporation for strategic planning, or a digital commons for protocol governance. This fractal nature makes it a versatile pattern for value creation across different levels of social organization.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
Futarchy is a powerful enabler of collective value creation due to its robust mechanism for information aggregation and decentralized decision-making. Its high degree of autonomy, composability, and fractal applicability make it a cornerstone pattern for cognitive-era governance. However, its reliance on capital for participation and the challenge of defining a truly comprehensive welfare metric prevent it from being a complete Value Creation Architecture out-of-the-box. It strongly enables value creation but requires conscious design to ensure equitable stakeholder representation and holistic goals.

**Opportunities for Improvement:**
- Integrate non-monetary staking mechanisms, such as reputation or proof-of-contribution, to broaden stakeholder participation beyond capital holders.
- Develop more robust and inclusive methods for defining the welfare metric, such as combining it with deliberative processes or quadratic voting to better represent minority interests.
- Implement safeguards against market manipulation, such as subsidies for contrarian bets or dynamic market-making algorithms, to enhance the resilience of the decision-making process.

### 9. Resources & References

-   **Essential Reading**:
    -   Hanson, R. (2000). *Futarchy: Vote Values, But Bet Beliefs*. [https://mason.gmu.edu/~rhanson/futarchy.html](https://mason.gmu.edu/~rhanson/futarchy.html)
    -   Hanson, R. (2013). Shall We Vote on Values, But Bet on Beliefs?. *Journal of Political Philosophy*, *21*(2), 151-178. [https://mason.gmu.edu/~rhanson/futarchy2013.pdf](https://mason.gmu.edu/~rhanson/futarchy2013.pdf)
    -   Buterin, V. (2014). *An Introduction to Futarchy*. Ethereum Blog. [https://blog.ethereum.org/2014/08/21/introduction-futarchy](https://blog.ethereum.org/2014/08/21/introduction-futarchy)

-   **Organizations & Communities**:
    -   **Meta-DAO:** The first real-world application of futarchy. [https://themetadao.org/](https://themetadao.org/)
    -   **GnosisDAO:** A DAO that has used prediction markets for governance. [https://gnosis.io/](https://gnosis.io/)
    -   **Zeitgeist:** A decentralized network for prediction markets. [https://zeitgeist.pm/](https://zeitgeist.pm/)

-   **Tools & Platforms**:
    -   **Augur:** A decentralized prediction market platform. [https://augur.net/](https://augur.net/)

-   **References**:
    1.  Hanson, R. (2000). *Futarchy: Vote Values, But Bet Beliefs*. Retrieved from [https://mason.gmu.edu/~rhanson/futarchy.html](https://mason.gmu.edu/~rhanson/futarchy.html)
    2.  Hanson, R. (2013). Shall We Vote on Values, But Bet on Beliefs?. *Journal of Political Philosophy*, *21*(2), 151-178. Retrieved from [https://mason.gmu.edu/~rhanson/futarchy2013.pdf](https://mason.gmu.edu/~rhanson/futarchy2013.pdf)
    3.  Wikipedia. (2025). *Futarchy*. Retrieved from [https://en.wikipedia.org/wiki/Futarchy](https://en.wikipedia.org/wiki/Futarchy)
    4.  Helius. (2024). *Futarchy and Governance: Prediction Markets Meet DAOs on Solana*. Retrieved from [https://www.helius.dev/blog/futarchy-and-governance-prediction-markets-meet-daos-on-solana](https://www.helius.dev/blog/futarchy-and-governance-prediction-markets-meet-daos-on-solana)
    5.  Buterin, V. (2014). *An Introduction to Futarchy*. Ethereum Blog. Retrieved from [https://blog.ethereum.org/2014/08/21/introduction-futarchy](https://blog.ethereum.org/2014/08/21/introduction-futarchy)
