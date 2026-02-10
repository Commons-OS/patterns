---
id: pat_047889ef253d45541de40d11
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/re-intermediation.md
slug: re-intermediation
title: Re-Intermediation
aliases:
- New Middlemen
- Platform Intermediation
- Digital Gatekeeping
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: context-dependent
  domain: platform
  category:
  - strategy
  era:
  - digital
  - cognitive
  origin:
  - platform-design
  - network-theory
  - software-engineering
  status: draft
  commons_alignment: 2
  commons_domain:
  - platform
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- higgerix
- cloudsters
sources:
- https://platformthinkinglabs.com/materials/the-reintermediation-of-markets/
- https://www.researchgate.net/publication/234759448_Reintermediation_Strategies_in_Business-to-Business_Electronic_Commerce
- https://www.tandfonline.com/doi/full/10.1080/13563467.2020.1766432
- https://www.fdic.gov/analysis/cfr/bank-research-conference/annual-18th/22-balyuk.pdf
- https://tomcheesewright.com/ideas/reintermediation
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
page_url: https://commons-os.github.io/patterns/re-intermediation/
---

### 1. Overview

Re-intermediation is the process by which new intermediaries emerge in a market, often facilitated by technology, to replace or augment existing ones. While the early internet was often hailed as a force for disintermediation, promising to connect producers and consumers directly, what has often transpired is a shift in who the intermediaries are and how they operate. These new intermediaries, frequently in the form of digital platforms, insert themselves between producers and consumers, creating new forms of value and, in many cases, new dependencies. This pattern is not merely about the re-introduction of a middleman; it is about the fundamental restructuring of value chains and the concentration of market power in the hands of those who control the new points of exchange. Understanding re-intermediation is crucial for anyone seeking to build or participate in the platform economy, as it highlights the strategic importance of controlling the "choke points" where value is created and exchanged. The re-intermediation phenomenon is a testament to the enduring economic logic of intermediation, which is to reduce transaction costs. However, the digital nature of the new intermediaries allows them to operate at a scale and with a level of sophistication that was previously unimaginable, leading to a host of new opportunities and challenges.

The significance of re-intermediation lies in its profound impact on market dynamics, competition, and the distribution of value. By aggregating demand and supply, standardizing interactions, and providing new services such as trust and reputation systems, new intermediaries can create significant efficiencies and unlock new market opportunities. However, this often comes at a cost. The new intermediaries can become powerful gatekeepers, extracting a significant share of the value created on their platforms and imposing their own rules and standards on participants. This can lead to a winner-take-all dynamic, where a single platform comes to dominate a particular market, stifling competition and innovation. The historical context of re-intermediation can be traced back to the rise of e-commerce in the late 1990s. While companies like Amazon and eBay initially appeared to be disintermediating traditional retail, they were, in fact, creating new, more powerful forms of intermediation. This trend has only accelerated with the rise of the mobile internet, social media, and the gig economy, with platforms like Uber, Airbnb, and Facebook becoming the new gatekeepers of their respective domains. The re-intermediation trend has also given rise to new business models, such as the "platform as a service" (PaaS) and "software as a service" (SaaS) models, which have further transformed the competitive landscape.

The historical origin of re-intermediation is deeply intertwined with the evolution of information and communication technologies. In the pre-digital era, intermediaries such as wholesalers, retailers, and brokers played a crucial role in overcoming the challenges of distance, information asymmetry, and transaction costs. The advent of the internet and e-commerce initially seemed to render these traditional intermediaries obsolete. However, as the digital landscape matured, it became clear that new forms of intermediation were emerging to address the unique challenges of the online world. These new intermediaries, often in the form of multi-sided platforms, were able to leverage the network effects, data, and algorithms of the digital realm to create new forms of value and capture a significant share of the market. The story of re-intermediation is therefore not simply a return to the past, but a story of the co-evolution of technology, business models, and market structures. This evolution is ongoing, with new technologies such as blockchain and artificial intelligence poised to once again reshape the landscape of intermediation.

### 2. Core Principles

1. **Aggregation and Standardization:** New intermediaries create value by aggregating a fragmented landscape of producers and consumers and standardizing the way they interact. This reduces search costs, increases market transparency, and enables more efficient matching of supply and demand. For example, a platform like Airbnb aggregates millions of individual property listings and standardizes the booking process, making it easy for travelers to find and book accommodation anywhere in the world. This principle is also evident in the world of content, where platforms like YouTube and Spotify aggregate vast libraries of user-generated and professionally produced content, and provide a standardized interface for discovery and consumption.

2. **Trust and Reputation as a Service:** In markets characterized by information asymmetry and risk, new intermediaries can play a crucial role in building trust and managing reputation. By providing mechanisms for reviews, ratings, and identity verification, they can reduce the uncertainty that often inhibits peer-to-peer transactions. This is a key function of platforms like Uber and eBay, where trust between strangers is essential for the functioning of the market. The importance of this principle is further underscored by the emergence of new trust-building technologies, such as blockchain-based identity systems and smart contracts.

3. **Data-Driven Value Creation:** Digital intermediaries are uniquely positioned to collect and analyze vast amounts of data about market participants and their interactions. This data can be used to create new forms of value, such as personalized recommendations, dynamic pricing, and targeted advertising. For example, Amazon uses its vast repository of customer data to provide personalized product recommendations, while Google uses its search data to deliver highly targeted advertising. This principle has become even more powerful with the advent of big data and machine learning, which allow platforms to extract ever more sophisticated insights from their data.

4. **Network Effects and Winner-Take-All Dynamics:** Many re-intermediated markets are characterized by strong network effects, where the value of the platform increases as more users join. This can create a virtuous cycle, where the leading platform attracts more users, which in turn makes it more attractive to even more users. This can lead to a winner-take-all dynamic, where a single platform comes to dominate the market, making it difficult for new entrants to compete. The power of network effects is evident in the dominance of platforms like Facebook in social networking and Google in search.

5. **Governance and Rule-Making:** New intermediaries are not just passive market-makers; they are also active rule-makers, setting the terms and conditions under which market participants can interact. This can include everything from pricing and payment policies to content moderation and dispute resolution. The governance of these platforms has become a major issue of public concern, as the decisions made by platform owners can have a significant impact on the lives and livelihoods of millions of people. The challenge of platform governance is to balance the competing interests of the platform owner, the users, and the wider public.

6. **Extraction and Exploitation:** While new intermediaries can create significant value, they can also be highly extractive, capturing a disproportionate share of the value created on their platforms. This can be achieved through a variety of mechanisms, such as high commission fees, data exploitation, and the algorithmic management of labor. The gig economy, in particular, has been criticized for its exploitative labor practices, with platforms like Uber and Deliveroo being accused of treating their workers as independent contractors in order to avoid providing them with the rights and protections of employees. This has led to a growing debate about the need for new forms of regulation to protect platform workers.

7. **Ecosystem Orchestration:** Successful intermediaries often evolve beyond simple marketplaces to become complex ecosystems of complementary products and services. By opening up their platforms to third-party developers and service providers, they can create a rich and diverse ecosystem that enhances the value of their core offering. This is a key strategy of companies like Apple and Google, whose mobile operating systems have become the foundation for a vast ecosystem of apps and services. The ability to orchestrate a successful ecosystem is a key source of competitive advantage in the platform economy.

### 3. Key Practices

1. **Identify and Address Market Frictions:** The first step in building a successful re-intermediation strategy is to identify a market that is characterized by significant frictions, such as high search costs, information asymmetry, or a lack of trust. The new intermediary must then develop a solution that addresses these frictions in a way that is superior to existing alternatives. This requires a deep understanding of the needs and pain points of both producers and consumers in the target market.

2. **Build a Critical Mass of Users:** Network effects are the lifeblood of most re-intermediated markets. It is therefore crucial to build a critical mass of users on both sides of the market as quickly as possible. This can be achieved through a variety of strategies, such as offering subsidies to early adopters, creating a compelling value proposition for both producers and consumers, and leveraging viral marketing techniques. The "chicken and egg" problem of attracting both supply and demand is a classic challenge for platform businesses, and requires a carefully crafted growth strategy.

3. **Develop a Robust Trust and Reputation System:** Trust is essential for the functioning of any market, but it is particularly important in peer-to-peer markets where participants are often strangers. It is therefore crucial to develop a robust trust and reputation system that includes features such as identity verification, reviews and ratings, and dispute resolution mechanisms. A well-designed trust system can be a powerful source of competitive advantage, as it can create a strong sense of community and loyalty among users.

4. **Leverage Data to Create Value:** Data is the new oil, and digital intermediaries are in a prime position to collect and refine it. It is therefore crucial to develop a data strategy that focuses on creating value for all market participants. This can include everything from personalized recommendations and dynamic pricing to fraud detection and market intelligence. However, it is also important to be mindful of the ethical implications of data collection and use, and to ensure that user privacy is protected.

5. **Design a Fair and Transparent Governance Model:** The governance of a platform is a critical factor in its long-term success. It is therefore crucial to design a governance model that is fair, transparent, and accountable to all market participants. This can include everything from clear and concise terms of service to a fair and impartial dispute resolution process. In some cases, it may also be appropriate to involve users in the governance of the platform, through mechanisms such as user councils or cooperative ownership structures.

6. **Foster a Thriving Ecosystem:** A platform is only as strong as its ecosystem. It is therefore crucial to foster a thriving ecosystem of complementary products and services that enhance the value of the core offering. This can be achieved by providing open APIs, developer tools, and a marketplace for third-party apps and services. A successful ecosystem can create a powerful lock-in effect, making it difficult for users to switch to a competing platform.

7. **Continuously Innovate and Adapt:** The digital landscape is constantly evolving, and new intermediaries must be able to innovate and adapt in order to stay ahead of the competition. This requires a culture of experimentation, a willingness to take risks, and a deep understanding of the changing needs and expectations of market participants. The ability to pivot and embrace new technologies and business models is essential for long-term survival in the platform economy.

### 4. Application Context

**Best Used For:**

*   Markets with high fragmentation and information asymmetry, where a central platform can create value by connecting buyers and sellers.
*   Industries where trust and reputation are critical, and a platform can provide a mechanism for building and maintaining trust.
*   Situations where network effects can be leveraged to create a competitive advantage and a winner-take-all dynamic.
*   Contexts where data can be used to create new forms of value, such as personalized services and targeted advertising.

**Not Suitable For:**

*   Markets that are already highly efficient and transparent, with low transaction costs.
*   Industries where there are strong incumbents with significant market power and high barriers to entry.
*   Situations where it is difficult to build a critical mass of users on both sides of the market.

**Scale:**

The scale of re-intermediation can range from a small niche market to a global industry. At the micro-level, a new intermediary might emerge to serve a specific local community or a particular interest group. For example, a platform that connects local farmers with consumers in a specific city. At the macro-level, a platform like Amazon or Google can come to dominate a global market, with billions of users and a market capitalization in the trillions of dollars. The scalability of a re-intermediation strategy depends on a variety of factors, including the size of the target market, the strength of the network effects, and the ability of the platform to expand into new geographies and product categories. The most successful platforms are often those that are able to achieve global scale, as this allows them to benefit from the strongest network effects and economies of scale.

**Domains:**

*   E-commerce (e.g., Amazon, Alibaba, eBay)
*   Social Media (e.g., Facebook, Twitter, Instagram, TikTok)
*   Search (e.g., Google, Baidu, DuckDuckGo)
*   Gig Economy (e.g., Uber, Airbnb, Deliveroo, TaskRabbit)
*   Fintech (e.g., PayPal, Ant Financial, Stripe, Square)
*   Media and Entertainment (e.g., Netflix, Spotify, YouTube)
*   Education (e.g., Coursera, Udemy, edX)
*   Healthcare (e.g., Zocdoc, Teladoc)

### 5. Implementation

Implementing a re-intermediation strategy is a complex and challenging undertaking that requires a deep understanding of technology, business, and market dynamics. The first step is to identify a market that is ripe for disruption. This typically involves looking for markets that are characterized by high frictions, such as fragmented supply, information asymmetry, and a lack of trust. Once a suitable market has been identified, the next step is to develop a compelling value proposition for both producers and consumers. This should address the key pain points of the existing market and offer a solution that is significantly better than the alternatives. A useful tool for this is the value proposition canvas, which can help to ensure that the platform is creating real value for its users.

With a clear value proposition in hand, the next step is to build the platform. This will typically involve developing a sophisticated technology stack that can handle a large volume of transactions, manage a complex set of rules and interactions, and collect and analyze vast amounts of data. The platform should also be designed to be as user-friendly as possible, with a simple and intuitive interface that makes it easy for users to find what they are looking for and complete their transactions. The choice of technology stack will depend on the specific needs of the platform, but common choices include cloud-based infrastructure, microservices architecture, and a variety of open-source and proprietary software.

Once the platform is built, the next challenge is to build a critical mass of users. This is often the most difficult part of implementing a re-intermediation strategy, as it requires overcoming the "chicken and egg" problem of attracting both producers and consumers to a new and unproven platform. There are a variety of strategies that can be used to address this challenge, such as offering subsidies to early adopters, creating a compelling marketing campaign, and leveraging viral growth hacks. For example, Dropbox famously used a referral program to acquire millions of new users in its early days. It is also important to focus on a specific niche or vertical in the early stages, in order to build a strong community of early adopters before expanding to a broader market.

As the platform grows, it will be important to continuously innovate and adapt in order to stay ahead of the competition. This will involve adding new features and services, expanding into new markets, and responding to the changing needs and expectations of users. It will also be important to develop a robust governance model that can ensure the long-term health and sustainability of the platform. This may involve creating a set of community guidelines, establishing a dispute resolution process, and even giving users a say in the future direction of the platform. The ability to evolve and adapt is what separates the most successful platforms from the rest.

### 6. Evidence & Impact

The impact of re-intermediation on the economy and society has been profound and far-reaching. On the one hand, it has led to significant gains in efficiency and convenience, with platforms like Amazon and Uber making it easier and cheaper than ever before to buy goods and services. It has also created new opportunities for entrepreneurship and innovation, with millions of people around the world now earning a living as producers on digital platforms. For example, the rise of the app economy, enabled by Apple's App Store and Google's Play Store, has created a whole new industry of software development and created jobs for millions of people.

On the other hand, re-intermediation has also been associated with a number of negative consequences, including the concentration of market power, the erosion of labor rights, and the spread of misinformation. The winner-take-all dynamics of many re-intermediated markets have led to the emergence of a small number of dominant platforms that are able to extract a significant share of the value created on their platforms. This has raised concerns about the impact on competition, innovation, and consumer welfare. For example, the dominance of Google in the search market has led to accusations of anti-competitive behavior, while the dominance of Facebook in the social media market has raised concerns about the spread of fake news and the manipulation of public opinion.

The gig economy, in particular, has been the subject of intense debate and controversy. While platforms like Uber and Deliveroo have created new opportunities for flexible work, they have also been criticized for their exploitative labor practices. By classifying their workers as independent contractors, these platforms are able to avoid providing them with the rights and protections of employees, such as a minimum wage, paid sick leave, and collective bargaining rights. This has led to a growing movement of "platform cooperativism," which seeks to build alternative platforms that are owned and controlled by their workers. Examples of platform cooperatives include Stocksy United, a stock photography cooperative, and Fairmondo, a cooperative online marketplace.

### 7. Cognitive Era Considerations

The rise of artificial intelligence and machine learning is likely to have a profound impact on the future of re-intermediation. On the one hand, AI has the potential to make intermediaries even more powerful and efficient. For example, AI-powered recommendation engines can help users to discover new products and services, while AI-powered chatbots can provide instant customer support. AI can also be used to optimize pricing, detect fraud, and personalize the user experience. This is likely to further entrench the position of the dominant platforms, as they are the ones with the most data to train their AI models.

The development of decentralized technologies, such as blockchain, could also have a significant impact on the future of re-intermediation. By enabling peer-to-peer transactions without the need for a trusted intermediary, blockchain has the potential to create a more decentralized and democratic economy. For example, a decentralized ride-sharing platform could allow drivers and riders to connect directly, without the need for a central company like Uber to take a cut of the fare. However, it is still early days for these technologies, and it remains to be seen whether they will be able to overcome the significant technical, social, and regulatory challenges that they currently face. The future of intermediation is likely to be a complex interplay between the centralizing forces of AI and the decentralizing forces of blockchain.

### 8. Commons Alignment Assessment

- **Shared Resource Potential:** Low - Re-intermediation, in its current form, is generally not aligned with the principles of a shared resource. The platforms that facilitate re-intermediation are typically privately owned and controlled, and the value that is created on these platforms is often extracted for the benefit of a small number of shareholders. The data that is collected on these platforms is also typically treated as a private asset, rather than a shared resource.

- **Democratic Governance:** Low - The governance of most re-intermediated platforms is highly centralized and undemocratic. The rules and policies of the platform are typically set by the platform owner, with little or no input from the users who create the value on the platform. This can lead to a sense of powerlessness and disenfranchisement among users, and can make it difficult to hold the platform accountable for its actions.

- **Equitable Access:** Medium - Re-intermediated platforms can provide more equitable access to markets for some producers and consumers. For example, a small artisan in a developing country can now sell their products to a global audience through a platform like Etsy. However, access to these platforms is often contingent on having access to a smartphone, a bank account, and a reliable internet connection, which can exclude many people in the developing world. Furthermore, the algorithms that are used to rank and recommend products and services on these platforms can be biased, which can further disadvantage certain groups.

- **Sustainability:** Low - The business models of many re-intermediated platforms are based on a logic of endless growth and extraction, which is not sustainable in the long run. The gig economy, in particular, has been criticized for its negative impact on the environment, with the increased use of cars for ride-sharing and food delivery contributing to traffic congestion and air pollution. Furthermore, the constant pressure to grow and innovate can lead to a culture of burnout and exploitation among platform workers.

- **Community Benefit:** Low - While re-intermediated platforms can provide some benefits to communities, such as increased convenience and new economic opportunities, these benefits are often outweighed by the negative consequences, such as the erosion of local businesses, the casualization of labor, and the extraction of value from local communities. For example, the rise of Airbnb has been linked to rising housing costs and the displacement of long-term residents in many cities. A more commons-aligned approach to re-intermediation would seek to balance the interests of the platform with the needs of the community.
