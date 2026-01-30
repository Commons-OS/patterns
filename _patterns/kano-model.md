---
id: pat_01kg5023zae8rthxw6atqpeaf4
page_url: https://commons-os.github.io/patterns/kano-model/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/kano-model.md
slug: kano-model
title: Kano Model
aliases: [Kano analysis, Kano's model]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: methodology
  era: [industrial, digital]
  origin: [academic, noriaki-kano]
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

### 1. Overview

The Kano Model is a theory on product development and customer satisfaction developed by Professor Noriaki Kano in the 1980s. It provides a framework for prioritizing features based on their ability to satisfy customers. The model challenges the traditional belief that improving every feature leads to increased satisfaction, suggesting instead that features have different impacts on the customer experience. The core problem the Kano Model solves is the challenge of resource allocation in product development. By categorizing features into five distinct types, it helps teams focus their efforts on what truly matters to customers, thereby maximizing the impact of their work. The origin of the model can be traced back to Noriaki Kano's work as a professor of quality management at the Tokyo University of Science. He introduced the model in his 1984 paper "Attractive Quality and Must-be Quality," aiming to provide a more nuanced understanding of customer needs beyond the one-dimensional view that more is always better.

### 2. Core Principles

The Kano Model is built upon a set of principles that help to classify and understand customer preferences. These principles provide a multi-dimensional view of quality, moving beyond the traditional linear understanding of customer satisfaction.

1.  **Must-be Quality**: These are the basic expectations of a product or service. If these features are not present, customers will be extremely dissatisfied. However, their presence is taken for granted and does not significantly increase satisfaction. These are the "price of entry" for a product to be considered viable in the market. For example, a car must have functioning brakes. The presence of brakes doesn't delight the customer, but their absence would be a catastrophic failure.

2.  **One-dimensional Quality**: These attributes have a direct, linear relationship with customer satisfaction. The better the performance of these features, the higher the customer satisfaction, and vice-versa. These are the features that are typically discussed in customer feedback and are often the basis of competition between products. For instance, the fuel efficiency of a car is a one-dimensional quality; the more miles per gallon, the more satisfied the customer.

3.  **Attractive Quality**: These are the unexpected features that, when present, create a sense of delight and significantly boost customer satisfaction. However, their absence does not cause dissatisfaction because the customer was not expecting them in the first place. These are the "wow" factors that can differentiate a product from its competitors. An example would be the first car to feature a built-in GPS navigation system.

4.  **Indifferent Quality**: The presence or absence of these features has no impact on customer satisfaction. Customers are neutral towards them. Identifying these features is important as it allows companies to save resources by not investing in them. For example, the specific type of plastic used for a non-user-facing part of a car's engine would likely be an indifferent quality to the average customer.

5.  **Reverse Quality**: These are features that, when present, actually cause dissatisfaction. This highlights the fact that not all customers have the same preferences. What one customer segment finds attractive, another may find annoying. For example, a highly complex and feature-rich infotainment system in a car might be a reverse quality for a user who prefers simplicity and ease of use.

### 3. Key Practices

To effectively apply the Kano Model, a series of practices are employed to gather customer insights and translate them into actionable product decisions. These practices guide teams through the process of identifying, categorizing, and prioritizing features.

1.  **Survey Design and Administration**: The process begins with the creation of a specialized Kano questionnaire. For each feature, a pair of questions is formulated: a functional question about the customer's reaction to the feature's presence, and a dysfunctional question about their reaction to its absence. This survey is then administered to a representative sample of customers to gather data.

2.  **Data Analysis and Aggregation**: The collected responses are analyzed to classify each feature into one of the five Kano categories for each respondent. This is done using an evaluation table that maps the paired answers to a category. The results are then aggregated, typically by finding the mode for each feature, to determine its overall classification.

3.  **Visualization and Prioritization**: The aggregated data is often visualized on a grid to provide a clear overview of the feature categories. This visualization aids in the prioritization of the product backlog. The general strategy is to first address all "Must-be" features, then maximize "One-dimensional" features, and finally incorporate a selection of "Attractive" features to create delight.

4.  **Advanced Practices**: For deeper insights, the data can be segmented by customer demographics or behaviors to reveal different preferences among subgroups. The Kano Model can also be integrated with other frameworks like Quality Function Deployment (QFD). Finally, since customer expectations evolve, the Kano analysis should be repeated periodically to track changes and maintain product relevance.

### 4. Application Context

The Kano Model is a versatile framework that can be applied in a wide range of contexts to enhance product development and customer satisfaction. Its application is not limited to a specific industry or scale, making it a valuable tool for any organization that aims to better understand and meet the needs of its customers.

**Best Used For**:

*   **New Product Development**: When developing a new product, the Kano Model can help to identify the essential features that must be included, as well as the features that will differentiate the product in the market.
*   **Feature Prioritization**: For existing products, the Kano Model provides a structured approach to prioritizing the development of new features and the improvement of existing ones.
*   **Competitive Analysis**: By analyzing competitors' products through the lens of the Kano Model, companies can identify opportunities to gain a competitive advantage.
*   **Understanding Customer Segments**: The model can be used to understand the different needs and preferences of various customer segments, enabling more targeted product development and marketing.
*   **Roadmap Planning**: The insights from a Kano analysis can inform the product roadmap, ensuring that development efforts are aligned with customer value.

**Not Suitable For**:

*   **Radical Innovation**: While the Kano Model is excellent for understanding and prioritizing known customer needs, it is less effective for identifying needs that customers are not yet aware of. It is not a tool for generating radical, breakthrough innovations.
*   **Very Early-Stage Startups**: In the very early stages of a startup, when the product and target market are still highly uncertain, a full-blown Kano analysis may be premature. A more agile and iterative approach to product discovery may be more appropriate.

**Scale**:

The Kano Model can be applied at various scales, from individual features to entire products and services. It can be used by small teams, large departments, and even across entire organizations. The principles of the model are fractal, meaning they can be applied to different levels of granularity.

**Domains**:

The Kano Model has been successfully applied in a wide variety of domains, including:

*   **Software Development**: To prioritize features in software applications and websites.
*   **Manufacturing**: To design and improve physical products.
*   **Healthcare**: To understand and enhance the patient experience.
*   **Hospitality**: To improve the services offered by hotels and restaurants.
*   **Financial Services**: To develop new financial products and services that meet customer expectations.

### 5. Implementation

Successfully implementing the Kano Model requires careful planning and execution. It is a process of deep customer inquiry that, when done correctly, can yield powerful insights.

**Prerequisites & Getting Started**:

Before beginning, it is essential to have clear objectives, a defined list of features to evaluate, access to a representative customer sample, and the necessary resources for the analysis. The initial steps involve forming a cross-functional team, developing and pilot-testing the Kano questionnaire, and then administering the survey to collect responses. Once the data is collected, it is analyzed to categorize the features.

**Common Challenges & Success Factors**:

Common challenges in implementing the Kano Model include survey fatigue, misinterpretation of questions by respondents, sample bias, and analysis paralysis. To overcome these challenges and ensure success, it is important to have strong executive sponsorship, a customer-centric culture, and to integrate the Kano analysis into the product development process. Clear communication of the results is also a key success factor, as it helps to align the organization around a shared understanding of customer needs.

### 6. Evidence & Impact

The Kano Model has been widely adopted across various industries, demonstrating its effectiveness in guiding product development and enhancing customer satisfaction. While many companies do not publicly disclose their use of the model, its impact can be seen in the success of products that are well-aligned with customer needs.

**Notable Adopters**:

While specific company names are often not disclosed in case studies, the principles of the Kano model are evident in the product strategies of many successful companies. For example, the article from kano-surveys.com describes how a recipe website used the model to successfully redesign their platform. Another example from a Medium article shows how CarePay, a healthcare financing company, used the Kano model to improve their insurance product offerings. The model is also widely used in the software industry, with companies like Microsoft and Google implicitly applying its principles to prioritize features in their products.

**Documented Outcomes**:

The application of the Kano Model has led to a number of documented positive outcomes for businesses:

*   **Improved Customer Satisfaction**: By focusing on the features that matter most to customers, companies can create products that are more satisfying to use.
*   **Increased Market Share**: Products that are well-aligned with customer needs are more likely to succeed in the market and gain market share.
*   **Reduced Development Costs**: By avoiding the development of features that customers do not value, companies can save time and resources.
*   **Enhanced Customer Loyalty**: When customers are delighted by a product, they are more likely to become loyal customers and advocates for the brand.

**Research Support**:

The effectiveness of the Kano Model is supported by a body of academic research. Numerous studies have demonstrated the validity of the model and its usefulness in a variety of contexts. For example, a study published in the *Total Quality Management & Business Excellence* journal found that the Kano model is a valid and reliable tool for understanding customer needs in the airline industry. Another study in the *International Journal of Quality & Reliability Management* showed that the model can be effectively used to improve service quality in the healthcare sector. These studies, and many others like them, provide empirical evidence for the value of the Kano Model as a tool for product development and customer satisfaction.

### 7. Cognitive Era Considerations

The advent of the Cognitive Era, characterized by the widespread adoption of artificial intelligence and automation, presents both opportunities and challenges for the application of the Kano Model. As we move into this new era, the way we understand and apply the principles of the Kano Model is likely to evolve.

**Cognitive Augmentation Potential**:

AI and automation have the potential to significantly enhance the Kano Model in several ways. The entire process of conducting a Kano analysis, from generating the questionnaire to analyzing the results, can be automated. AI-powered tools can analyze vast amounts of unstructured customer feedback from sources like social media, online reviews, and customer support interactions to identify potential features for evaluation. This can help to ensure that the Kano analysis is comprehensive and that no important customer needs are overlooked. Furthermore, AI can be used to predict how the classification of features might change over time, allowing companies to be more proactive in their product development efforts.

**Human-Machine Balance**:

Despite the potential of AI, the Kano Model will continue to require a balance between human intelligence and machine automation. While AI can handle the heavy lifting of data analysis, human judgment will remain crucial for interpreting the results and making strategic decisions. The initial brainstorming of features to be tested, for example, often benefits from human creativity and a deep understanding of the product and its users. The final prioritization of features should not be left to algorithms alone. It should be a collaborative process where humans and machines work together, with humans making the final decisions based on a holistic understanding of the business context, market dynamics, and ethical considerations.

**Evolution Outlook**:

In the Cognitive Era, the Kano Model is likely to become more dynamic and real-time. Instead of being a periodic exercise, the Kano analysis could become a continuous process, with AI constantly monitoring customer feedback and updating the classification of features in real time. The model may also become more integrated with other AI-powered product management tools, creating a more holistic and data-driven approach to product development. The focus may shift from simply categorizing features to predicting the impact of different feature combinations on key business metrics, such as customer satisfaction, retention, and revenue. This will enable companies to make more informed and impactful product decisions.

### 8. Commons Alignment Assessment

The Kano Model, while primarily a tool for product development and customer satisfaction, can also be assessed for its alignment with the principles of a commons-based approach. This assessment examines how the model contributes to the creation and preservation of shared value, and how it distributes rights and responsibilities among stakeholders.

1.  **Stakeholder Mapping**: The Kano Model inherently focuses on one primary stakeholder: the customer. While this is a crucial stakeholder, a full commons approach would require a more comprehensive mapping of all stakeholders, including employees, suppliers, partners, and the wider community. The model, in its standard application, does not explicitly prompt for this broader stakeholder analysis. However, it could be adapted to include the perspectives of other stakeholders by conducting Kano analyses with these groups as well.

2.  **Value Creation**: The Kano Model is a powerful tool for creating value for customers by ensuring that products and services are designed to meet their needs and expectations. It helps to create a positive user experience and to build customer loyalty. However, the model's focus is primarily on use-value for the customer and exchange-value for the company. A commons approach would also consider the creation of social and environmental value.

3.  **Value Preservation**: The model's emphasis on tracking the evolution of customer preferences over time contributes to the preservation of value. By understanding how features move from being "Attractive" to "Must-be," companies can adapt their products to maintain their relevance and value in the market. This proactive approach to value preservation is a key strength of the model.

4.  **Shared Rights & Responsibilities**: The Kano Model does not directly address the distribution of rights and responsibilities. It is a tool for understanding customer preferences, not for governing a commons. However, by giving customers a voice in the product development process, it can be seen as a step towards a more participatory and democratic approach to design.

5.  **Systematic Design**: The Kano Model provides a systematic and data-driven approach to product development. It encourages a structured process of inquiry, analysis, and decision-making, which is a key element of systematic design. This systematic approach helps to ensure that product decisions are based on evidence rather than on assumptions or intuition.

6.  **Systems of Systems**: The Kano Model can be seen as a component of a larger system of product development and management. It can be integrated with other frameworks, such as Quality Function Deployment (QFD) and Agile methodologies, to create a more comprehensive and effective system of systems. This modularity and interoperability are key characteristics of a commons-based approach.

7.  **Fractal Properties**: The principles of the Kano Model are fractal, meaning they can be applied at different scales. The model can be used to evaluate individual features, entire products, or even the services of an entire organization. This scalability allows the model to be applied in a wide range of contexts and at different levels of granularity.

**Overall Score**: 3/5 (Transitional)

The Kano Model is a valuable tool that can contribute to a more commons-aligned approach to product development. Its focus on understanding and meeting customer needs is a key element of creating shared value. However, the model's primary focus on the customer and on economic value means that it falls short of a full commons approach. To be more aligned with the commons, the model would need to be expanded to include a broader range of stakeholders and a more holistic view of value creation. Nevertheless, the Kano Model can be seen as a transitional pattern that can help organizations to move towards a more participatory and customer-centric approach to design.

### 9. Resources & References

**Essential Reading**:

*   Kano, N., Seraku, N., Takahashi, F., & Tsuji, S. (1984). Attractive quality and must-be quality. *Journal of the Japanese Society for Quality Control*, *14*(2), 39-48.
*   Berger, C., Blauth, R., Boger, D., Bolster, C., Burchill, G., DuMouchel, W., ... & Walden, D. (1993). Kano's methods for understanding customer-defined quality. *Center for Quality of Management Journal*, *2*(4), 3-35.
*   Sauerwein, E., Bailom, F., Matzler, K., & Hinterhuber, H. H. (1996). The Kano model: How to delight your customers. *International Working Seminar on Production Economics*, *1*(4), 313-327.

**Organizations & Communities**:

*   **ASQ (American Society for Quality)**: A global community of people passionate about quality, who use the tools, their ideas and expertise to make our world work better. ASQ provides the quality community with training, professional certifications, and knowledge to a vast network of members of the global quality community.
*   **The CQI (Chartered Quality Institute)**: The chartered body for quality professionals. The CQI improves the performance of organizations by developing their capability in quality management.

**Tools & Platforms**:

*   **KanoSurveys.com**: A dedicated online tool for creating, administering, and analyzing Kano surveys.
*   **Qualtrics**: A leading experience management platform that can be used to create and distribute Kano questionnaires.
*   **SurveyMonkey**: A popular online survey tool that can be used to create Kano surveys, although the analysis may need to be done manually.

**References**:

[1] Wikipedia. (2023). *Kano model*. Retrieved from https://en.wikipedia.org/wiki/Kano_model

[2] Kano, N., Seraku, N., Takahashi, F., & Tsuji, S. (1984). Attractive quality and must-be quality. *Journal of the Japanese Society for Quality Control*, *14*(2), 39-48.

[3] KanoSurveys. (n.d.). *Kano model example*. Retrieved from https://www.kanosurveys.com/articles/kano-model-example

[4] Hörner, E. N. (2022). The ultimate guide to the Kano Model: value through the eyes of your customer. *Medium*. Retrieved from https://medium.com/carepay-stories/value-through-the-eyes-of-your-customer-the-kano-model-applied-f9fd653302a0

[5] TQM & Business Excellence. (2009). *The Kano model: A dynamic approach for classifying and prioritising requirements of airline travellers with three case studies on international airlines*. Retrieved from https://www.tandfonline.com/doi/abs/10.1080/14783360903181867

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/kano-model/](https://commons-os.github.io/patterns/domain/kano-model/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/kano-model.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/kano-model.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
