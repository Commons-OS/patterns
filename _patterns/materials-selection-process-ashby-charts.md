---
id: pat_01kg50240xe19r5fzqk2b4w2d7
page_url: https://commons-os.github.io/patterns/materials-selection-process-ashby-charts/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/materials-selection-process-ashby-charts.md
slug: materials-selection-process-ashby-charts
title: Materials Selection Process (Ashby Charts)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: implementation
  domain: operations
  category: [methodology]
  era: [industrial]
  origin: []
  status: draft
  commons_alignment: 2
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

## 1. Overview

The Materials Selection Process, particularly when enhanced by the use of Ashby charts, represents a systematic and visually intuitive methodology for optimizing the choice of materials in engineering design. Developed by Professor Michael F. Ashby of Cambridge University, this approach addresses the increasingly complex challenge of selecting the most suitable material from a vast and ever-growing range of options. The core of this process lies in translating design requirements into a set of material constraints and objectives, which are then used to screen and rank candidate materials. Ashby charts, which are scatter plots that map out the property space of materials, are the central tool in this process. They enable designers to simultaneously visualize and compare multiple material properties, facilitating the identification of optimal solutions that balance competing requirements such as performance, cost, and weight.

The fundamental premise of the Materials Selection Process is that the performance of a component is determined by a combination of its geometry, the material from which it is made, and the loads to which it is subjected. By decoupling these factors, it becomes possible to derive 'material indices' – quantitative measures of a material's suitability for a given application. These indices, which are combinations of material properties, can be plotted on Ashby charts to graphically identify the materials that offer the best performance. This visual approach not only simplifies the selection process but also fosters a deeper understanding of the trade-offs between different material properties and their impact on design performance. The process is not intended to provide a single definitive answer, but rather to narrow down the field of potential candidates to a manageable shortlist for more detailed evaluation.

## 2. Core Principles

The Materials Selection Process using Ashby charts is founded on a set of core principles that guide the designer from a statement of need to a well-reasoned choice of material. These principles provide a logical framework for navigating the complexities of material selection and ensure that the chosen material is not only technically sound but also aligned with the broader objectives of the design.

**1. Translation of Design Requirements:** The first principle is the translation of abstract design requirements into a concrete set of constraints and objectives. Constraints are firm limits that a material must meet to be considered, such as a maximum service temperature or a minimum fracture toughness. Objectives are quantities that the designer seeks to maximize or minimize, such as minimizing cost or maximizing strength-to-weight ratio. This step is crucial for framing the selection problem in a way that can be systematically addressed.

**2. Screening with Constraints:** Once the constraints are defined, they are used to screen the entire database of materials, eliminating those that do not meet the essential requirements. This is a non-negotiable filtering step that significantly reduces the number of candidate materials. For example, if a component must operate in a corrosive environment, all materials that are susceptible to corrosion would be screened out.

**3. Ranking with Objectives:** After screening, the remaining materials are ranked according to the defined objectives. This is where the concept of the 'material index' comes into play. By deriving a performance metric that combines the relevant material properties, it is possible to rank the candidates in order of their ability to meet the design objective. The material with the highest index value is, in principle, the best choice for the application.

**4. The Power of Visualization:** A central tenet of the Ashby method is the use of graphical charts to visualize material property space. By plotting one property against another on logarithmic scales, Ashby charts reveal the relationships between properties and allow for the rapid identification of materials with desirable combinations of attributes. The material indices can be plotted as lines on these charts, providing a clear visual guide to the optimal materials for a given application.

**5. Iterative Refinement:** The materials selection process is not a linear path but an iterative one. The initial selection may be refined as the design evolves and more detailed information becomes available. The insights gained from the Ashby charts can also inspire design modifications that take better advantage of the properties of a particular material. This iterative feedback loop between material selection and design is a key feature of the methodology.

## 3. Key Practices

The practical application of the Materials Selection Process involves a series of well-defined steps. These practices provide a structured workflow for designers to follow, ensuring a rigorous and comprehensive evaluation of material options.

**1. Define the Function, Constraints, Objectives, and Free Variables:** The first step is to clearly articulate the design problem. This involves defining the function of the component, the constraints it must satisfy, the objectives to be optimized, and the free variables that the designer can manipulate (such as dimensions).

**2. Derive the Material Index:** Based on the objective function, a material index is derived. This is a mathematical expression that captures the relationship between the material properties that govern performance. For example, for a light and stiff tie-rod, the material index would be E/ρ (Young's modulus divided by density). For a light and stiff panel, the index would be E^(1/3)/ρ.

**3. Plot the Index on an Ashby Chart:** The derived material index is then plotted on the appropriate Ashby chart. Since the charts use logarithmic scales, the index equation is typically rearranged into a linear form. This allows the index to be represented as a straight line on the chart. By moving this line across the chart, it is possible to identify the materials that lie on or above the line, which represent the candidates with the highest performance index.

**4. Identify Candidate Materials:** The materials that are intersected by the selection line as it is moved to the optimal position on the chart are identified as the primary candidates. These materials offer the best combination of properties for the given application. The visual nature of this step allows for a rapid and intuitive comparison of different material classes.

**5. Investigate the Candidates in More Detail:** The shortlist of candidate materials generated from the Ashby charts is then subjected to a more detailed investigation. This may involve considering other factors that are not captured in the charts, such as cost, availability, manufacturability, and environmental impact. This final step often requires consulting supplier data sheets and other sources of detailed information.

## 4. Application Context

The Materials Selection Process using Ashby charts is a versatile methodology that can be applied across a wide range of engineering disciplines and at various stages of the design process. Its primary application is in the conceptual and embodiment design phases, where the choice of material has the most significant impact on the overall performance and cost of the product.

**Conceptual Design:** In the early stages of design, when the product concept is still being formulated, the Ashby method provides a powerful tool for exploring the feasibility of different design ideas. By quickly assessing the potential of various material classes, designers can make informed decisions about the most promising design directions to pursue. The charts can also stimulate creativity by revealing unconventional material choices that might not have been considered otherwise.

**Embodiment Design:** As the design progresses to the embodiment stage, where the overall layout and form of the components are being defined, the Materials Selection Process helps to refine the choice of material and to optimize the component's geometry. The material indices provide a quantitative basis for making trade-offs between competing design requirements, such as stiffness, strength, and weight.

**Redesign and Failure Analysis:** The methodology is also valuable in the context of redesigning existing products or analyzing component failures. By systematically evaluating the material choice against the design requirements, it is possible to identify opportunities for improvement or to pinpoint the root cause of a failure. For example, if a component is failing due to excessive deflection, an Ashby chart can be used to identify materials with a higher Young's modulus.

**Educational Tool:** Beyond its practical application in industry, the Materials Selection Process and Ashby charts are widely used as an educational tool in materials science and engineering curricula. The visual and intuitive nature of the charts makes them an effective way to teach students about the vast range of engineering materials and the relationships between their properties.

## 5. Implementation

Implementing the Materials Selection Process requires a systematic approach and access to reliable material property data. The following steps provide a detailed guide to implementing the process:

**1. Gather the Necessary Tools and Data:** The primary tool for this process is a comprehensive set of Ashby charts, which can be found in textbooks, online resources, or specialized software packages. The CES EduPack software, developed by Granta Design (now part of Ansys), is the most comprehensive tool for implementing the Ashby methodology, providing a vast database of material properties and interactive charting tools.

**2. Formulate the Design Problem:** As outlined in the Key Practices section, the first step is to clearly define the design problem in terms of function, constraints, objectives, and free variables. This is a critical step that requires a thorough understanding of the application and its performance requirements.

**3. Select the Appropriate Ashby Chart:** Based on the properties that are most relevant to the design problem, the appropriate Ashby chart is selected. For example, if the primary requirements are high stiffness and low weight, the Young's Modulus vs. Density chart would be the most relevant.

**4. Apply the Selection Criteria:** The constraints are applied to the chart to eliminate unsuitable materials. This can be done by drawing boxes or lines on the chart to define the acceptable range for each property. The material index is then plotted as a line on the chart, and this line is moved to identify the materials with the highest performance.

**5. Create a Shortlist of Candidates:** The materials that satisfy the constraints and rank highly according to the objective are compiled into a shortlist. This list should be small enough to allow for a more detailed evaluation of each candidate.

**6. Conduct a Detailed Evaluation:** The final step is to conduct a detailed evaluation of the shortlisted materials. This may involve considering additional factors such as:

*   **Cost and Availability:** The cost of the raw material and the availability of the material in the required form and quantity.
*   **Manufacturability:** The ease with which the material can be processed and shaped into the final component.
*   **Environmental Impact:** The life cycle environmental impact of the material, from extraction to disposal or recycling.
*   **Aesthetics and other Qualitative Factors:** The appearance, feel, and other subjective qualities of the material that may be important for the application.

This detailed evaluation will ultimately lead to the final choice of the most appropriate material for the design.

## 6. Evidence & Impact

The Materials Selection Process using Ashby charts has had a profound impact on the field of engineering design. Its adoption by both industry and academia is a testament to its effectiveness and utility. The evidence for its impact can be seen in the numerous products and applications where this methodology has been successfully applied.

One of the most significant impacts of the Ashby method is that it has made the process of material selection more rational and systematic. Prior to the development of this methodology, material selection was often based on intuition, experience, or trial and error. The Ashby method provides a structured framework that enables designers to make more informed and justifiable decisions. This has led to the development of products that are lighter, stronger, more efficient, and more cost-effective.

For example, in the aerospace industry, where weight is a critical design parameter, the Ashby method has been instrumental in the development of lightweight structures using advanced composite materials. By using Ashby charts to compare the specific stiffness and specific strength of different materials, designers have been able to identify the most promising candidates for reducing the weight of aircraft components.

In the automotive industry, the methodology has been used to select materials for a wide range of applications, from engine components to body panels. The need to improve fuel efficiency and reduce emissions has driven a strong focus on lightweighting, and the Ashby method has provided a valuable tool for achieving this goal.

The impact of the Ashby method is also evident in the field of materials science. The charts have provided a new way of visualizing and understanding the relationships between material properties, which has stimulated research into the development of new materials with novel combinations of attributes. The concept of 'material property space' has become a powerful paradigm for guiding the design of new materials.

## 7. Cognitive Era Considerations

The advent of the cognitive era, characterized by the increasing prevalence of artificial intelligence, machine learning, and big data, presents both opportunities and challenges for the Materials Selection Process. These new technologies have the potential to enhance the Ashby methodology in several ways.

**AI-Powered Material Discovery:** Machine learning algorithms can be trained on vast datasets of material properties to predict the properties of new, undiscovered materials. This could significantly expand the range of materials available to designers and accelerate the development of new materials with tailored properties. AI could also be used to identify novel material indices for complex, multi-objective design problems.

**Automated Selection and Optimization:** The process of screening and ranking materials could be automated using AI-powered software tools. These tools could take a set of design requirements as input and automatically generate a shortlist of optimal materials, along with a detailed analysis of their performance. This would free up designers to focus on the more creative aspects of the design process.

**Integration with Digital Twins:** The Materials Selection Process could be integrated with digital twin technology to create a more holistic and data-driven approach to design. A digital twin is a virtual representation of a physical product that is updated with real-time data from sensors. By integrating the Ashby methodology with a digital twin, it would be possible to monitor the performance of a material in service and to use this data to refine the selection process for future designs.

However, the cognitive era also presents challenges. The increasing complexity of materials and the vast amount of data available could make it more difficult for designers to make sense of the information and to make informed decisions. It will be important to develop new tools and interfaces that can help designers to navigate this complexity and to effectively leverage the power of AI and machine learning.

### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
The Materials Selection Process does not explicitly define Rights and Responsibilities for a broad set of stakeholders. Its primary users are designers and engineers, focusing on the technical requirements of a product. The inclusion of wider stakeholder interests, such as the environment or future generations, depends entirely on the designer choosing to translate those interests into specific, measurable material constraints and objectives.

**2. Value Creation Capability:**
The pattern is a powerful enabler of technical and economic value by optimizing material choice for performance and cost. While this can indirectly lead to social or ecological benefits (e.g., creating more efficient, safer, or longer-lasting products), it does not inherently capture non-monetary value streams. Its capability for collective value creation is limited unless explicitly guided to prioritize criteria beyond technical optimization.

**3. Resilience & Adaptability:**
The methodology promotes adaptability within the design process through its iterative nature, allowing for refinement as requirements change. It helps create resilient products by making robust, data-driven material choices. However, it is a tool for designing static objects rather than a framework for helping a socio-ecological system adapt to complexity and maintain coherence under stress.

**4. Ownership Architecture:**
The pattern is entirely silent on ownership. It is a technical decision-making tool that operates independently of any specific ownership or governance model. It treats materials as resources to be optimized, without defining Rights or Responsibilities associated with their use, stewardship, or end-of-life.

**5. Design for Autonomy:**
The process is highly systematic, data-driven, and based on clear rules, making it exceptionally well-suited for automation and integration with AI systems. As noted in the pattern's Cognitive Era Considerations, machine learning can enhance and automate the selection process. Its low coordination overhead makes it compatible with distributed or autonomous design systems.

**6. Composability & Interoperability:**
This pattern is highly modular and interoperable. It functions as a specialized module that can be easily integrated into larger product design, development, and lifecycle management workflows. It can be combined with other patterns like Life Cycle Assessment or Cost-Benefit Analysis to create more comprehensive decision-making systems.

**7. Fractal Value Creation:**
The core logic of the pattern—translating requirements, screening with constraints, and ranking with objectives—is fractal. This methodology can be applied at various scales, from selecting materials for a micro-scale electronic component to choosing structural materials for a large-scale infrastructure project, demonstrating its scalable value-creation logic.

**Overall Score: 2 (Partial Enabler)**

**Rationale:**
The Materials Selection Process is a powerful, systematic tool for technical optimization, but it has significant gaps in its alignment with the Commons OS v2.0 framework. It is a partial enabler because its focus is on optimizing resources for product performance, not on architecting collective value creation. While it is highly compatible with automation and can be adapted to include sustainability criteria, it lacks native support for stakeholder governance, holistic value definition, and distributed ownership.

**Opportunities for Improvement:**
- Integrate multi-stakeholder input mechanisms for defining selection constraints and objectives, moving beyond purely technical requirements.
- Develop standardized material indices that explicitly measure and rank social and ecological value creation, such as circularity, community impact, or knowledge-sharing potential.
- Combine the process with ownership patterns to link material selection decisions with long-term stewardship rights and responsibilities.

## 9. Resources & References

*   [1] Ashby, M. F. (2005). *Materials Selection in Mechanical Design* (3rd ed.). Elsevier-Butterworth Heinemann.
*   [2] Wikipedia. (n.d.). *Material selection*. Retrieved January 28, 2026, from https://en.wikipedia.org/wiki/Material_selection
*   [3] University of Cambridge. (n.d.). *Material Selection Charts*. Retrieved January 28, 2026, from https://www-materials.eng.cam.ac.uk/mpsite/interactive_charts/
*   [4] Proxom Engineering. (2020, October 15). *Material Selection Charts*. Retrieved January 28, 2026, from https://proxom.net/material-selection/
*   [5] Granta Design. (2009). *Material and Process Selection Charts*. Retrieved January 28, 2026, from https://www.researchgate.net/profile/Alain-Celzard/post/Looking_for_Material_with_High_Modulus_and_high_coefficient_of_thermal_expansion/attachment/59d6449379197b807799fd0e/AS%3A449286304473088%401484129610805/download/2_materials-charts-2009.pdf

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/implementation/materials-selection-process-ashby-charts/](https://commons-os.github.io/patterns/implementation/materials-selection-process-ashby-charts/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/materials-selection-process-ashby-charts.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_implementation/materials-selection-process-ashby-charts.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
