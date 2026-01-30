---
id: pat_01kg5023yvehgrw2tgchwaj9vp
page_url: https://commons-os.github.io/patterns/domain/futarchy-robin-hansons-prediction-market-governance/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/futarchy-robin-hansons-prediction-market-governance.md
slug: futarchy-robin-hansons-prediction-market-governance
title: Futarchy - Robin Hanson's Prediction Market Governance
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: governance
  category: [framework]
  era: [cognitive]
  origin: []
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: ["pat_01kg5023wbfw1azjwp3zgdr86p"]
specializes_to: []
enables: []
requires: []
related: ["pat_01kg5023xne3gs3g227jcvch6k", "pat_01kg5023x4easr02ymp7vsz81b", "pat_01kg5023y5fnhb2ej6755c58p1", "pat_01kg50240sfm8re6ep2sz2xmy5", "pat_01kg5023vwe00rptkqr3z6pkd9", "pat_01kg5023y4e708zavzfmvmx4yp", "pat_01kg50240fev1snyp2ytvn21xm", "pat_01kg50240rf3s9mqrqw0pp5mwn", "pat_01kg5023x3f8gtc1a31gws6jj3", "pat_01kg5023y4e708zavzcte3n4dd", "pat_01kg5023xmek8szp5z3c5dc977", "pat_01kg5023y8e9ssb52a5snc91pm", "pat_01kg5023xbed1bnd9kg5m8pqq0", "pat_01kg5023vhev9b6swdrszd75z9", "pat_01kg5023whehgsjwtbrb92n8n3"]
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

# 1. Overview

Futarchy is a governance model that utilizes prediction markets to make decisions. Proposed by economist Robin Hanson, its core principle is to "vote on values, but bet on beliefs." In a futarchy, a community or organization first defines its goals or values. Then, prediction markets are used to forecast the outcomes of different proposed actions or policies. The action predicted to best achieve the stated goals is then implemented. This approach aims to separate the subjective process of defining values from the objective process of determining the most effective way to achieve them, leveraging the collective intelligence of the market to make more informed decisions.

# 2. Core Principles

Futarchy's design is rooted in a few core principles aimed at enhancing decision-making by using prediction markets to aggregate information and encourage truth-seeking. These principles are designed to address some of the fundamental challenges of governance, such as information aggregation, incentive alignment, and the separation of powers.

**1. Vote on Values, Bet on Beliefs:** This is the central tenet of Futarchy, a principle that advocates for a clear separation between the expression of collective values and the formation of beliefs about how to best achieve those values. In this model, democratic processes, such as voting, are used to determine what a community or organization wants to achieve—its goals, its desired outcomes, its definition of success. This is the "vote on values" part of the equation. Once these values have been established and codified in a clear and measurable welfare metric, prediction markets are used to determine the most effective policies or actions to achieve those goals. This is the "bet on beliefs" part. This separation is crucial because it allows for a more rational and evidence-based approach to decision-making. It acknowledges that while values are subjective and best determined through democratic means, beliefs about cause and effect can be tested and refined through market mechanisms. By separating these two domains, Futarchy aims to reduce the influence of political ideology and partisan bickering on policy decisions, and instead focus on what actually works.

**2. Information Aggregation & Truthful Revelation:** A key challenge for any governance system is how to effectively aggregate the vast amount of dispersed information held by individuals within a community. Futarchy addresses this challenge by using prediction markets as its primary information aggregation mechanism. Prediction markets have been shown to be remarkably effective at pooling diverse and often conflicting pieces of information into a single, coherent forecast. By allowing individuals to bet on the outcomes of different policies, Futarchy creates a powerful incentive for those with relevant knowledge to participate in the decision-making process. This "put your money where your mouth is" approach encourages participants to be more honest and rigorous in their analysis, as accurate predictions are financially rewarded and inaccurate ones are penalized. This financial incentive for truthful revelation is a key advantage of Futarchy over traditional governance systems, where there are often strong incentives to misrepresent one's beliefs for political or personal gain. The result is a more accurate and reliable assessment of the likely consequences of different policy options.

**3. Separation of Powers & Conditional Markets:** Futarchy introduces a novel form of separation of powers, dividing the responsibilities of governance between elected representatives and the market. In a Futarchy-based system, elected representatives would be responsible for defining and managing a clear and measurable metric of collective welfare. This metric would serve as the objective function that the prediction markets would then seek to maximize. The market, in turn, would be responsible for selecting the policies that are most likely to increase the value of this metric. This separation of powers is designed to ensure that decisions are made in the best interests of the community as a whole, rather than being influenced by the narrow interests of a particular political faction or special interest group. The mechanism at the heart of this process is the use of conditional prediction markets. For each proposed policy, two conditional markets are created. One market predicts the value of the welfare metric if the policy is implemented, and the other predicts the value of the welfare metric if the policy is not implemented. The policy is then automatically adopted if the market predicts a higher welfare outcome with the policy than without it. This mechanism allows for a direct and transparent comparison of the expected outcomes of different policy options, providing a clear and objective basis for decision-making.

# 3. Key Practices

The implementation of Futarchy relies on several key practices to ensure its effectiveness and integrity.

**1. Defining a Clear and Measurable Welfare Metric:** A successful Futarchy requires a high-quality welfare metric that accurately reflects the community's values. This metric, which the prediction markets aim to maximize, should be defined through a democratic and inclusive process. It must be clear, transparent, and measurable, potentially combining economic, social, and environmental indicators.

**2. Establishing and Operating Prediction Markets:** The core of Futarchy involves carefully designed and operated prediction markets. This includes clear rules, sufficient liquidity for efficient price discovery, and measures to prevent manipulation. The markets should be open to all, with transparent results.

**3. Proposing, Evaluating, and Auditing Policies:** Any community member can propose a policy, which is then evaluated by conditional prediction markets. The policy is adopted if the market predicts a higher welfare outcome with its implementation. This decentralized approach is complemented by a robust auditing process to verify market results and monitor for manipulation, ensuring public confidence in the system's fairness and accuracy.

# 4. Application Context

Futarchy's principles can be applied in various contexts where complex decisions are needed, provided a clear and measurable objective function can be defined.

**1. Corporate Governance:** Futarchy can improve corporate decision-making by aligning shareholder, manager, and employee interests. A welfare metric based on long-term shareholder value (e.g., stock price, profitability) can be used to evaluate strategic decisions like market entry or product launches, fostering a more data-driven approach.

**2. Decentralized Autonomous Organizations (DAOs):** Futarchy is a promising governance model for DAOs, enabling decentralized and transparent decision-making. The welfare metric could be the value of the DAO's native token or user base growth, with prediction markets guiding decisions on new features or protocol changes.

**3. Public Policy and Government:** While full national implementation is challenging, Futarchy can be applied to specific public policy areas. For instance, a city could use it to allocate its infrastructure budget, with a welfare metric based on traffic congestion or public transit ridership, leading to more evidence-based urban planning.

**4. Non-Profit and Philanthropic Organizations:** Futarchy can enhance the effectiveness of non-profits by using a welfare metric based on social impact (e.g., lives saved, poverty reduction). Prediction markets can then guide resource allocation to the most effective programs, increasing accountability and impact.

# 5. Implementation

Implementing Futarchy is a complex process that requires careful planning. The following steps outline a general framework for implementation and highlight key challenges.

**1. Define the Welfare Metric:** The first step is to define a clear, measurable, and comprehensive welfare metric through a democratic and inclusive process. This metric should capture the community's values and be resistant to manipulation.

**2. Design and Develop the Platform:** This involves designing the prediction markets, including contract types and rules, and developing a secure, transparent, and user-friendly platform to host them. The platform should support policy proposals, trading, and performance tracking.

**3. Bootstrap Liquidity and Participation:** To ensure market efficiency, it's crucial to bootstrap liquidity and encourage participation. This can be achieved through incentives like subsidies or rewards for accurate predictions.

**4. Propose, Adjudicate, and Monitor:** A process for proposing, automatically adjudicating, and continuously monitoring policies is essential. The system should be iterative, allowing for adjustments to the welfare metric and market mechanisms over time.

### Challenges

Key challenges in implementing Futarchy include:

*   **Defining a comprehensive welfare metric.**
*   **Preventing market manipulation.**
*   **Ensuring sufficient market participation.**
*   **Solving the "Oracle Problem" for verifying outcomes.**
*   **Addressing ethical concerns about market-based decision-making.**

# 6. Evidence & Impact

While Futarchy has not been fully implemented, its core mechanism, prediction markets, has a strong track record of success in various contexts.

**1. Accuracy and Information Aggregation:** Extensive research has shown that prediction markets are often more accurate than traditional forecasting methods like polls and expert opinions [1, 2]. Their success lies in their ability to aggregate dispersed information by incentivizing participants to reveal their true beliefs, a phenomenon often referred to as the "wisdom of the crowd" [3].

**2. Real-World Applications and Impact:** Prediction markets have been applied in diverse areas, from political elections to corporate forecasting. The rise of blockchain technology has led to the development of decentralized prediction market platforms like Augur and Gnosis, which are particularly well-suited for use in DAOs. The use of prediction markets can lead to more objective and data-driven decision-making, helping to overcome biases and political pressures.

**3. Challenges and Limitations:** Despite their potential, prediction markets face challenges, including vulnerability to manipulation, the difficulty of applying them to long-term problems, and ethical concerns about their use in public policy. These issues must be addressed for large-scale implementation of Futarchy.

# 7. Cognitive Era Considerations

The Cognitive Era, with its advancements in AI, big data, and connectivity, offers both opportunities and challenges for Futarchy.

**1. AI-Powered Forecasting and Automated Governance:** AI can enhance prediction market accuracy by providing sophisticated forecasting models and augmenting the collective intelligence of the crowd. This can lead to new forms of automated governance where AI agents propose policies that are then evaluated by prediction markets and automatically implemented. However, this also raises questions about human oversight and unintended consequences.

**2. Big Data and Welfare Metrics:** Big data allows for the creation of more comprehensive and nuanced welfare metrics, incorporating a wide range of social, economic, and environmental indicators. This can lead to more effective Futarchy-based governance.

**3. New Risks and Challenges:** The use of AI in prediction markets introduces new risks, such as algorithmic collusion and manipulation. Additionally, the increasing reliance on technology could exacerbate the digital divide and information asymmetry, creating an unfair advantage for those with access to the latest technologies. Mitigating these risks is crucial for the successful implementation of Futarchy in the Cognitive Era.

# 8. Commons Alignment Assessment

This section assesses the alignment of Futarchy with the principles of a commons-based approach to governance. The assessment is based on seven key dimensions of commons alignment.

| Dimension | Alignment Score (1-5) | Rationale |
| :--- | :--- | :--- |
| **1. Openness & Inclusivity** | 4 | Futarchy is, in principle, open to anyone who wants to participate in the prediction markets. However, the need for financial resources to participate in the markets can be a barrier to entry for some, which limits its full inclusivity. |
| **2. Transparency** | 5 | The decision-making process in Futarchy is highly transparent. All proposed policies and the market's predictions about their likely outcomes are publicly visible. This allows for a high degree of scrutiny and accountability. |
| **3. Subsidiarity** | 3 | Futarchy can be adapted to different scales, from small communities to large nations. However, the reliance on a single, centralized welfare metric can be in tension with the principle of subsidiarity, which favors decision-making at the most local level possible. |
| **4. Peer-to-Peer Relationships** | 4 | Futarchy promotes peer-to-peer relationships by allowing anyone to propose policies and to participate in the prediction markets. This creates a more decentralized and bottom-up approach to governance, where ideas are judged on their merits rather than on the status of their proponents. |
| **5. Common Good Focus** | 3 | The focus of Futarchy is on maximizing a predefined welfare metric. While this metric is intended to represent the common good, there is a risk that it could be defined too narrowly or that it could be manipulated by special interests. The alignment with the common good is therefore highly dependent on the quality and integrity of the welfare metric. |
| **6. Fairness & Equity** | 2 | The use of prediction markets raises concerns about fairness and equity. Those with more financial resources may have a greater influence on the market, which could lead to outcomes that favor the wealthy. Addressing this issue is a key challenge for the implementation of Futarchy. |
| **7. Sustainability** | 3 | The long-term sustainability of a Futarchy-based system is uncertain. It depends on its ability to overcome the challenges of market manipulation, low participation, and the definition of a good welfare metric. If these challenges can be addressed, Futarchy has the potential to be a more sustainable form of governance than traditional models. |

**Overall Commons Alignment Score: 3**

# 9. Resources & References

[1] [Wikipedia: Prediction market](https://en.wikipedia.org/wiki/Prediction_market)

[2] [Corporate Prediction Markets: Evidence from Google, Ford, and Microsoft](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MS-TR-2008-11.pdf)

[3] [The Polymarket Effect: How Prediction Markets Are Beating The Experts](https://www.forbes.com/sites/jasonwingard/2025/11/19/the-polymarket-effect-how-prediction-markets-are-beating-the-experts/)

[4] [Futarchy: Vote Values, But Bet Beliefs](https://mason.gmu.edu/~rhanson/futarchy.html)

[5] [Shall We Vote on Values, But Bet on Beliefs?](https://mason.gmu.edu/~rhanson/futarchy2013.pdf)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/futarchy-robin-hansons-prediction-market-governance/](https://commons-os.github.io/patterns/domain/futarchy-robin-hansons-prediction-market-governance/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/futarchy-robin-hansons-prediction-market-governance.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/futarchy-robin-hansons-prediction-market-governance.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
