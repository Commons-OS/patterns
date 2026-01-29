---
id: pat_01kg5023wwen09dwtf02v3xemt
page_url: https://commons-os.github.io/patterns/domain/85-rolling-forecasts/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/85-rolling-forecasts.md
slug: 85-rolling-forecasts
title: Rolling Forecasts
aliases: [Continuous Forecasting, Perpetual Forecasting]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: [practice]
  era: [digital]
  origin: [academic]
  status: draft
  commons_alignment: 3
generalizes_from: []
specializes_to: ["pat_01kg5023zve6sv1r0bt9fxtm1t"]
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview (150-300 words)

A rolling forecast is a dynamic financial planning and management tool that continuously updates and extends a company's financial projections over a set future time horizon, typically 12 to 18 months. Unlike traditional static annual budgets, which are prepared once a year and quickly become outdated, a rolling forecast is revised on a regular basis—usually monthly or quarterly. As one period of actual results is completed, it is dropped from the forecast, and a new future period is added to the end of the forecast horizon. This process ensures that the organization always has a current and forward-looking view of its expected financial performance.

The primary value of a rolling forecast is its ability to provide a more accurate and relevant basis for decision-making in a volatile and uncertain business environment. By constantly incorporating the latest market conditions, operational results, and business assumptions, it enables organizations to be more agile and responsive. This proactive approach to financial management helps businesses to identify and address potential opportunities and risks sooner, allocate resources more effectively, and improve the overall accuracy of their financial planning. The concept emerged from the need to overcome the limitations of static budgeting in dynamic industries, gaining prominence as businesses sought more adaptive planning methods in the latter half of the 20th century, with its adoption accelerating in the digital era.

### 2. Core Principles (3-7 principles, 200-400 words)

1.  **Continuous and Adaptive Planning**: Unlike static annual budgets, rolling forecasts are based on a principle of continuous planning. The forecast horizon (e.g., 12-18 months) is perpetually extended as time progresses. As each month or quarter of actual performance is recorded, a new forecast period is added to the end of the horizon. This ensures the plan is not a static document but a living, adaptive model that reflects the most current business realities and expectations, enabling greater organizational agility.

2.  **Driver-Based and Materiality-Focused**: Effective rolling forecasts are not built on detailed, line-item financial data alone. Instead, they are driven by key business and operational metrics that have the most significant impact on financial outcomes (e.g., sales volume, customer acquisition rates, production efficiency). This driver-based approach simplifies the forecasting process, makes it more understandable for non-finance stakeholders, and links financial projections directly to operational activities. The focus is on what is material to the business, avoiding unnecessary detail and focusing effort where it matters most.

3.  **Collaborative and Cross-Functional Ownership**: A rolling forecast is not solely a finance exercise. Its success depends on broad participation and ownership from across the organization. Sales, marketing, operations, and other departments must provide input for the key drivers and assumptions within their areas of expertise. This collaborative process breaks down silos, creates a shared understanding of the business, and fosters collective accountability for the forecast and the resulting performance.

4.  **Forward-Looking and Action-Oriented**: The primary purpose of a rolling forecast is not just to predict the future but to influence it. It is a proactive management tool designed to support decision-making. By regularly identifying potential performance gaps, risks, and opportunities, the forecast prompts timely management interventions and course corrections. The focus shifts from explaining past variances against an outdated budget to making informed decisions that shape future results.

5.  **Technology-Enabled Process**: While simple rolling forecasts can be managed in spreadsheets, their full potential is realized through modern planning and analytics platforms (EPM/CPM systems). Technology is a key enabler for integrating data from various sources, automating the forecasting process, modeling complex scenarios, and facilitating collaboration. The use of predictive analytics and AI can further enhance accuracy and provide deeper insights, transforming the forecast from a simple projection to a sophisticated predictive model.
### 3. Key Practices (5-10 practices, 300-600 words)

1.  **Define the Time Horizon and Frequency**: A critical first step is to determine the appropriate time horizon and update frequency for the forecast. This is not a one-size-fits-all decision. The horizon (e.g., 12, 18, or 24 months) should be long enough to cover the organization's business cycle and decision-making lead times. The frequency (e.g., monthly or quarterly) should be determined by the volatility of the business environment and the need for timely information. For example, a fast-moving tech company might use a monthly 18-month rolling forecast, while a more stable manufacturing firm might opt for a quarterly 24-month forecast.

2.  **Identify and Model Key Business Drivers**: Instead of getting bogged down in detailed line-item forecasting, focus on the key operational and business drivers that have the most significant impact on financial performance. These drivers might include units sold, price per unit, customer churn rate, or website traffic. By creating a driver-based model, the forecast becomes more transparent, easier to understand for non-financial managers, and more directly linked to the operational levers of the business.

3.  **Establish a Clear and Efficient Process**: A well-defined and efficient process is essential for the successful implementation of a rolling forecast. This includes clearly defining roles and responsibilities, establishing a clear timeline for each forecast cycle, and automating data collection and consolidation as much as possible. The goal is to make the forecasting process as lightweight and value-added as possible, freeing up time for analysis and decision-making rather than data wrangling.

4.  **Promote Cross-Functional Collaboration**: A rolling forecast should be a collaborative effort, not a siloed finance activity. Involve key stakeholders from across the business—sales, marketing, operations, HR—in the forecasting process. Their input is crucial for developing realistic assumptions and creating a forecast that everyone understands and buys into. Regular forecast review meetings can facilitate this collaboration and ensure that the forecast is a shared tool for managing the business.

5.  **Integrate with Other Management Processes**: To maximize its value, the rolling forecast should be integrated with other key management processes, such as strategic planning, resource allocation, and performance management. The forecast should be a key input into these processes, providing a current and forward-looking view of the business to inform decisions. For example, the forecast can be used to identify the need for resource reallocation or to set more realistic performance targets.

6.  **Leverage Technology and Automation**: While it's possible to manage a rolling forecast in Excel, it can quickly become cumbersome and error-prone. Modern Enterprise Performance Management (EPM) or Corporate Performance Management (CPM) systems can automate many aspects of the rolling forecast process, from data integration and consolidation to scenario modeling and reporting. This not only improves efficiency and accuracy but also provides more powerful analytical capabilities.

7.  **Focus on Analysis and Action, Not Just Accuracy**: While forecast accuracy is important, the primary goal of a rolling forecast is to support better decision-making. Encourage a culture where the forecast is used as a tool for analysis, scenario planning, and proactive course correction. The focus should be on understanding the 

### 4. Application Context (200-300 words)

-   **Best Used For**:
    -   **Volatile and Dynamic Industries**: Companies in sectors like technology, retail, and fashion, where market conditions, consumer demand, and competitive landscapes change rapidly, benefit greatly from the agility that rolling forecasts provide.
    -   **Fast-Growing Businesses**: Startups and high-growth companies that are scaling quickly find that static annual budgets become obsolete almost immediately. Rolling forecasts provide a more realistic and current financial roadmap to manage growth and allocate resources effectively.
    -   **Project-Based Businesses**: Companies in industries like construction, consulting, and software development, where revenue and resource needs are tied to the lifecycle of specific projects, can use rolling forecasts to maintain a more accurate picture of future performance.
    -   **Turnaround and Restructuring Situations**: When a company is undergoing a significant transformation, a rolling forecast provides a crucial tool for managing cash flow, monitoring progress against turnaround plans, and making timely adjustments.

-   **Not Suitable For**:
    -   **Very Stable and Predictable Businesses**: For organizations in highly stable industries with predictable revenue and cost structures, the additional effort required for a rolling forecast may not yield significant benefits over a traditional static budget.
    -   **Extremely Small Businesses with Limited Resources**: Very small businesses with limited staff and resources may find the process of continuously updating a forecast to be too burdensome.

-   **Scale**: The principles of rolling forecasts can be applied at multiple scales, from a single **Team** or **Department** to an entire **Organization**. It is most commonly implemented at the **Organization** level, but can also be effective for managing large, multi-year projects or initiatives.

-   **Domains**: Rolling forecasts are widely used across a variety of industries, including **Technology**, **Retail**, **Manufacturing**, **Hospitality**, **Professional Services**, and **Healthcare**.

### 5. Implementation (400-600 words)

-   **Prerequisites**:
    -   **Executive Sponsorship and a Culture of Agility**: Successful implementation requires strong support from senior leadership and a willingness to move away from the traditional, static budgeting mindset. The organization must embrace a culture that values agility, collaboration, and data-driven decision-making.
    -   **Clear Objectives and Scope**: Before starting, it's crucial to define what the organization wants to achieve with a rolling forecast. Is the goal to improve forecast accuracy, enhance agility, or better align resources with strategic priorities? The initial scope should also be clearly defined, perhaps starting with a pilot program in a specific business unit or focusing on key financial metrics.
    -   **Defined Key Business Drivers**: The organization must identify the key operational and business drivers that have the most significant impact on financial performance. This requires a deep understanding of the business model and the key levers that drive value.

-   **Getting Started**:
    -   **Start Small and Iterate**: Don't try to boil the ocean. Start with a pilot program in a single business unit or with a limited set of metrics. This allows the organization to learn and refine the process before rolling it out more broadly.
    -   **Assemble a Cross-Functional Team**: The implementation team should include representatives from finance, as well as from key operational areas of the business. This ensures that the forecast is grounded in operational reality and has broad buy-in.
    -   **Select the Right Tools**: Evaluate whether the existing financial systems can support a rolling forecast or if a new solution is needed. Modern EPM/CPM platforms can provide the necessary capabilities for data integration, modeling, and collaboration.

-   **Common Challenges**:
    -   **Resistance to Change**: The move to a rolling forecast can be met with resistance from those who are comfortable with the traditional budgeting process. Overcoming this requires strong change management, clear communication of the benefits, and training and support for those involved in the new process.
    -   **Data Quality and Availability**: A rolling forecast is only as good as the data it's based on. Organizations may struggle with disparate data sources, inconsistent data definitions, and poor data quality. Addressing these data challenges is a critical prerequisite for success.
    -   **Lack of Automation**: A manual, spreadsheet-based rolling forecast process can be time-consuming and error-prone. Without the right technology to automate data collection, consolidation, and reporting, the process can become unsustainable.

-   **Success Factors**:
    -   **Strong Leadership Support**: As with any significant change initiative, strong and visible support from senior leadership is essential.
    -   **Clear Communication and Training**: It's important to clearly communicate the purpose and benefits of the rolling forecast and to provide adequate training to all those who will be involved in the process.
    -   **Focus on Continuous Improvement**: A rolling forecast is not a one-time project. It's a continuous process that should be regularly reviewed and refined to ensure it remains relevant and effective.
### 6. Evidence & Impact (300-500 words)

-   **Notable Adopters**:
    -   **Microsoft**: The technology giant famously abandoned the traditional annual budget in favor of a rolling forecast to increase its agility and responsiveness to the fast-changing tech landscape.
    -   **Danone**: The global food and beverage company has been on a journey to replace its traditional budgeting process with a rolling forecast to better manage its complex, global operations.
    -   **AGF**: The Canadian investment firm implemented an eight-quarter rolling forecast using Workday Adaptive Planning, which has enabled them to make more strategic, course-altering decisions much more quickly.
    -   **Southwest Airlines**: The airline uses a rolling forecast to manage its fuel costs and other key operational expenses in a volatile industry.
    -   **Unilever**: The consumer goods giant has used rolling forecasts to improve its demand planning and supply chain management.

-   **Documented Outcomes**:
    -   **Improved Forecast Accuracy**: Studies have shown that rolling forecasts can significantly improve forecast accuracy. For example, a study by the Aberdeen Group found that companies using rolling forecasts had a 14% higher accuracy in their revenue forecasts compared to those using static budgets.
    -   **Increased Agility and Responsiveness**: By providing a more current and forward-looking view of the business, rolling forecasts enable organizations to respond more quickly to changing market conditions. AGF, for example, cut several days out of its forecasting and reporting process every month, and a full week out of its annual budgeting practice.
    -   **Better Resource Allocation**: Rolling forecasts provide a more realistic basis for allocating resources, ensuring that they are directed to the areas of the business with the greatest potential.

-   **Research Support**:
    -   **Aberdeen Group**: The research firm has published numerous reports on the benefits of rolling forecasts, highlighting their impact on forecast accuracy, agility, and overall business performance.
    -   **FP&A Trends**: This organization provides a wealth of resources on rolling forecasts, including case studies, webinars, and articles that showcase the benefits and best practices of this approach.
    -   **Academic Research**: While much of the evidence for rolling forecasts comes from industry case studies and surveys, there is a growing body of academic research that supports the benefits of this approach. For example, a 2007 study by L. Tanlu found that companies that adopted rolling forecasts experienced a significant improvement in forecast accuracy.

### 7. Cognitive Era Considerations (200-400 words)

-   **Cognitive Augmentation Potential**: The cognitive era, characterized by the rise of artificial intelligence (AI) and machine learning (ML), has the potential to significantly augment the rolling forecast process. AI-powered tools can automate the collection and integration of vast amounts of data from both internal and external sources, including market trends, competitor activities, and macroeconomic indicators. ML algorithms can identify complex patterns and correlations in this data that would be impossible for humans to detect, leading to more accurate and insightful forecasts. Predictive analytics can be used to generate baseline forecasts automatically, freeing up finance professionals to focus on more strategic, value-added activities like scenario planning and analysis.

-   **Human-Machine Balance**: While AI and automation can handle much of the heavy lifting in the rolling forecast process, the human element remains crucial. The role of the finance professional is shifting from a data cruncher to a strategic advisor. Humans are still needed to interpret the outputs of AI models, to apply business judgment and context, and to communicate the story behind the numbers to senior leadership. The most effective rolling forecast processes will be those that strike the right balance between human and machine, leveraging technology to augment human intelligence, not replace it.

-   **Evolution Outlook**: In the future, we can expect to see rolling forecasts become even more dynamic, continuous, and intelligent. The distinction between planning, forecasting, and reporting will likely blur as real-time data and AI-powered insights are integrated directly into the decision-making process. We may see the emergence of "live" financial models that are continuously updated and that can simulate the impact of decisions in real-time. This will enable organizations to become even more agile and proactive, navigating uncertainty with greater confidence and turning volatility into a competitive advantage.

### 8. Commons Alignment Assessment (600-800 words)

1.  **Stakeholder Mapping**: The rolling forecast pattern inherently promotes a more inclusive stakeholder map compared to traditional, top-down budgeting. Its effectiveness hinges on the active participation of various departments, including sales, marketing, operations, and human resources, in addition to the finance team and senior leadership. This cross-functional collaboration ensures that the forecast is grounded in the operational realities of the business. However, the scope of stakeholder engagement is typically limited to internal actors within the organization. The interests of external stakeholders, such as customers, suppliers, and the broader community, are generally not directly represented in the forecasting process, although their behavior is often a key input to the forecast (e.g., customer demand).

2.  **Value Creation**: The primary value created by a rolling forecast is enhanced organizational agility and improved decision-making. By providing a more accurate and timely view of the future, it enables the organization to respond more effectively to changing market conditions, allocate resources more efficiently, and improve its overall financial performance. The primary beneficiaries of this value are the organization's shareholders, who see improved returns, and its employees, who may benefit from a more stable and successful company. The value created for external stakeholders is indirect, for example, through more reliable product availability for customers or more predictable orders for suppliers.

3.  **Value Preservation**: The rolling forecast pattern is designed for value preservation through its continuous and adaptive nature. Unlike a static annual budget that quickly becomes outdated, a rolling forecast is constantly updated to reflect the latest information and business conditions. This ensures that it remains a relevant and valuable tool for decision-making over time. The use of driver-based models and technology platforms further enhances its resilience and adaptability.

4.  **Shared Rights & Responsibilities**: A rolling forecast promotes a greater sense of shared responsibility for the organization's financial performance. By involving a broader range of stakeholders in the forecasting process, it fosters a sense of collective ownership of the numbers. However, the rights to the forecast—the ability to approve it, modify it, and decide how it is used—are typically concentrated in the hands of senior leadership and the finance department. While operational managers have a responsibility to provide accurate inputs, they may not have the right to challenge the final forecast or the decisions that are based on it.

5.  **Systematic Design**: The rolling forecast pattern is enabled by a systematic design that includes a well-defined process, a clear set of roles and responsibilities, and a supporting technology infrastructure. The use of driver-based models provides a clear and logical structure for the forecast, while modern EPM/CPM platforms provide the tools for data integration, collaboration, and analysis. This systematic design is essential for ensuring the efficiency, accuracy, and sustainability of the rolling forecast process.

6.  **Systems of Systems**: A rolling forecast can be seen as a key component of a broader system of systems for organizational management. It integrates with and supports other key management processes, such as strategic planning, performance management, and risk management. For example, the rolling forecast can provide the financial context for strategic decisions, and it can be used to set more realistic and relevant performance targets. It can also be a key input into the risk management process, helping to identify and quantify potential financial risks.

7.  **Fractal Properties**: The principles of rolling forecasts exhibit fractal properties, as they can be applied at different scales throughout an organization. A single department can use a rolling forecast to manage its own budget and resources, while the organization as a whole can use a consolidated rolling forecast to manage its overall financial performance. The core principles of continuous planning, driver-based modeling, and cross-functional collaboration are relevant and applicable at all of these scales.

**Overall Score**: 3/5 (Transitional)

**Rationale**: The rolling forecast pattern represents a significant step away from the extractive and hierarchical nature of traditional budgeting. It promotes greater collaboration, agility, and data-driven decision-making, which are all hallmarks of a more commons-aligned approach to organizational management. However, the pattern is still primarily focused on optimizing the financial performance of the individual organization, and it does not yet fully embrace the broader principles of the commons, such as multi-stakeholder governance and the creation of shared value for all stakeholders. To become more commons-aligned, the pattern could be extended to include a more explicit consideration of the interests of external stakeholders and a greater emphasis on the creation of social and environmental value in addition to financial value.

### 9. Resources & References (200-400 words)

-   **Essential Reading**:
    -   *Future Ready: How to Master Business Forecasting* by Steve Morlidge and Steve Player. This book provides a comprehensive guide to the principles and practices of modern business forecasting, with a strong emphasis on the benefits of rolling forecasts.
    -   *Implementing Beyond Budgeting: Unlocking the Performance Potential* by Bjarte Bogsnes. While not exclusively about rolling forecasts, this book provides a powerful critique of traditional budgeting and a compelling vision for a more agile and adaptive approach to performance management, in which rolling forecasts play a key role.
    -   *The CFO as Business Integrator: The Essential Role of the 21st-Century CFO* by the American Institute of CPAs (AICPA). This report highlights the changing role of the CFO and the importance of tools like rolling forecasts in enabling finance to become a more strategic partner to the business.

-   **Organizations & Communities**:
    -   **FP&A Trends Group**: A leading online resource for finance professionals, offering a wealth of articles, webinars, and case studies on rolling forecasts and other modern FP&A topics.
    -   **Association for Financial Professionals (AFP)**: A professional association for finance professionals that provides a range of resources and events on topics related to financial planning and analysis, including rolling forecasts.

-   **Tools & Platforms**:
    -   **Anaplan**: A cloud-based platform for connected planning that is widely used for implementing rolling forecasts and other advanced planning processes.
    -   **Workday Adaptive Planning**: A leading cloud-based corporate performance management (CPM) solution that provides a comprehensive suite of tools for budgeting, forecasting, and reporting.
    -   **Cube**: A financial planning and analysis (FP&A) platform that helps companies to automate and streamline their budgeting and forecasting processes.

-   **References**:
    -   Aberdeen Group. (n.d.). *The ROI of Rolling Forecasts*. Retrieved from https://www.aberdeenessentials.com/cfo-essentials/the-roi-of-rolling-forecasts/
    -   Anaplan. (n.d.). *8 steps to implementing rolling forecasts*. Retrieved from https://www.anaplan.com/blog/8-steps-implementing-rolling-forecasts/
    -   Bogsnes, B. (2009). *Implementing Beyond Budgeting: Unlocking the Performance Potential*. John Wiley & Sons.
    -   Cube. (2024, November 27). *Rolling forecasts: Definition, how to make one, and when to use them*. Retrieved from https://www.cubesoftware.com/blog/rolling-forecast
    -   FP&A Trends. (n.d.). *Danone's Journey from Budget to Rolling Forecast & Beyond*. Retrieved from https://fpa-trends.com/tv-series/danones-journey-budget-rolling-forecast-beyond
    -   Morlidge, S., & Player, S. (2010). *Future Ready: How to Master Business Forecasting*. John Wiley & Sons.
    -   Tanlu, L. (2007). *Does the adoption of rolling forecasts improve planning? An empirical investigation of the consequences of rolling forecasts*. SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1004125
    -   Wall Street Prep. (2024, February 20). *Rolling Forecast Guide | FP&A Best Practices Tutorial*. Retrieved from https://www.wallstreetprep.com/knowledge/rolling-forecast-best-practices-guide-fpa-professionals/
    -   Workday. (n.d.). *What Is a Rolling Forecast?*. Retrieved from https://www.workday.com/en-ca/topics/fpa/rolling-forecast.html

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/85-rolling-forecasts/](https://commons-os.github.io/patterns/domain/85-rolling-forecasts/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/85-rolling-forecasts.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/85-rolling-forecasts.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
