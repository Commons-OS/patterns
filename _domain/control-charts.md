---
id: pat_01kg5023y4e708zavza6kxdg76
page_url: https://commons-os.github.io/patterns/domain/control-charts/
github_url: https://github.com/commons-os/patterns/blob/main/_domain/control-charts.md
slug: control-charts
title: Control Charts
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: operations
  category: tool
  era: industrial
  origin: []
  status: draft
  commons_alignment: 1
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

# 1. Overview

Control charts, also known as Shewhart charts or process-behavior charts, are a fundamental tool for statistical process control (SPC). They are graphical representations of data collected from a process over time, used to determine whether a process is in a state of statistical control. A process is considered in control if the variation in its output is stable and predictable. The control chart was invented by Walter A. Shewhart at Bell Laboratories in the 1920s, and it remains one of the seven basic tools of quality, widely used across various industries to monitor and improve processes. [1] [2]

The primary purpose of a control chart is to distinguish between two types of process variation: common cause variation and special cause variation. Common cause variation is the inherent, natural variability of a process that is in a state of statistical control. Special cause variation, on the other hand, is due to assignable causes, which are events or circumstances that are not part of the normal process. By identifying and eliminating special causes of variation, a process can be brought into a state of statistical control, making its future performance predictable. [4]

# 2. Core Principles

The effective use of control charts is grounded in a few core principles that are essential for understanding and improving processes. These principles revolve around the nature of variation, the structure of the chart itself, and the statistical rules that govern its interpretation.

At the heart of statistical process control is the concept of **variation**. Every process exhibits variation; no two products or service outcomes are exactly alike. Shewhart identified two fundamental types of variation: **common cause** and **special cause**. Common cause variation is the random, inherent variability of a process that is operating in a stable and consistent manner. It is the "noise" within the system and can only be reduced by making fundamental changes to the process itself. Special cause variation, also known as assignable cause variation, comes from external, unpredictable events. These are the "signals" that indicate something has changed in the process, such as a machine malfunction, a new operator, or a different batch of raw materials. The primary goal of a control chart is to detect these special causes, allowing for their investigation and elimination, thereby bringing the process back into a state of statistical control where only common cause variation remains. [4] [6]

A control chart is a time-series graph with three key horizontal lines: a **center line (CL)**, an **upper control limit (UCL)**, and a **lower control limit (LCL)**. The center line represents the average or mean of the process data, providing a baseline for the process performance. The upper and lower control limits are placed at a calculated distance from the center line, typically at plus and minus three standard deviations (σ) of the process data. These limits define the range of expected variation for a stable process. Data points that fall within these limits are considered to be due to common cause variation, while points that fall outside the limits are signals of special cause variation. [1]

The statistical foundation of control charts is based on the **three-sigma (3σ) limits**. Shewhart chose three standard deviations as the optimal distance for the control limits to balance the risk of two types of errors: treating a common cause as a special cause (a false alarm) and treating a special cause as a common cause (missing a signal). For a normally distributed process, the 3σ limits ensure that approximately 99.73% of the data points will fall within the control limits if the process is stable. This makes it highly unlikely for a point to fall outside the limits purely by chance, thus providing a strong signal that a special cause is present. [8]

A process is considered to be **in a state of statistical control** when all the data points on its control chart fall within the control limits and do not exhibit any non-random patterns. An "out of control" process is indicated by one or more points falling outside the control limits or by the presence of specific patterns or runs in the data that suggest a non-random influence. These signals prompt an investigation to identify and address the special cause, leading to process improvement.

# 3. Key Practices

The practical application of control charts involves a set of key practices, from selecting the right type of chart for the data being analyzed to the systematic process of constructing and interpreting it. These practices ensure that the control chart serves as an effective tool for monitoring and improving process stability and capability.

Control charts are broadly categorized into two main types based on the kind of data they monitor: **variables data** and **attributes data**. Variables data are measurements on a continuous scale, such as length, weight, temperature, or time. For this type of data, charts are used in pairs to monitor both the central tendency and the variability of the process. The most common pairings are **X-bar and R charts**, which are ideal for smaller, consistent sample sizes, and **X-bar and s charts**, which are more suited for larger sample sizes. For individual measurements, **Individuals and Moving Range (I-MR) charts** are used.

Attributes data, in contrast, are discrete counts or proportions, such as the number of defective items or the count of errors. For this type of data, single charts are used. **P-charts** are used to monitor the proportion of non-conforming items in samples of varying sizes, while **np-charts** are used for the same purpose but require a constant sample size. **C-charts** are employed to monitor the number of defects in a unit of constant size, and **u-charts** are used when the sample size or area of opportunity for defects varies.

The process of creating and using a control chart follows a systematic procedure:
1.  **Choose the appropriate control chart:** Select the chart type based on the data (variables or attributes) and the subgrouping strategy.
2.  **Determine the data collection plan:** Decide on the subgroup size, the frequency of sampling, and the overall period for data collection.
3.  **Collect the data:** Gather at least 20-25 subgroups of data to ensure that the calculated control limits are statistically reliable.
4.  **Calculate the center line and control limits:** Compute the average (for the center line) and the upper and lower control limits (typically at ±3 standard deviations) based on the collected data.
5.  **Construct the chart and plot the data:** Draw the center line and control limits on a graph and plot the data points in time order.
6.  **Interpret the chart:** Analyze the chart for any out-of-control signals. The most basic signal is a point falling outside the control limits. Other signals include non-random patterns, such as long runs of points on one side of the center line, or trends and cycles. These patterns suggest the presence of special cause variation, even if all points are within the control limits. [1]

# 4. Application Context

Control charts are a versatile tool with broad applicability across a wide range of industries and processes. While they originated in manufacturing, their use has expanded to any setting where a process can be measured and improved. The ability of control charts to provide real-time insights into process stability and performance makes them an invaluable asset for quality improvement, cost reduction, and operational efficiency.

In **manufacturing**, control charts are a cornerstone of quality control. They are used to monitor and control the dimensions of machined parts, the viscosity of chemical products, the fill volume of containers, and countless other critical-to-quality characteristics. By using control charts, manufacturers can detect and correct process shifts before a large number of defective products are made, leading to reduced scrap and rework, lower costs, and improved product consistency.

**Healthcare** is another sector where control charts have found extensive application. They are used to monitor a wide variety of processes, from patient wait times and medication errors to infection rates and surgical outcomes. For example, a hospital might use a p-chart to track the monthly percentage of patients who develop a post-operative infection, or an X-bar and R chart to monitor the time it takes to process lab results. By using control charts, healthcare providers can identify opportunities to improve patient safety, enhance the quality of care, and increase the efficiency of their operations. [10]

The **service industry** also benefits from the use of control charts. Banks can use them to monitor the time it takes to process a loan application, call centers can track the average handle time for customer inquiries, and logistics companies can monitor on-time delivery performance. In any service process, control charts can help to identify and eliminate sources of variation, leading to more consistent and predictable service delivery and higher levels of customer satisfaction.

Control charts are a key component of many structured quality improvement frameworks, most notably **Six Sigma** and **Total Quality Management (TQM)**. In Six Sigma, control charts are used in the "Control" phase of the DMAIC (Define, Measure, Analyze, Improve, Control) methodology to ensure that the gains from a process improvement project are sustained over time. In TQM, control charts are used as a tool for continuous improvement, empowering employees at all levels of an organization to monitor and improve the processes they work on.

# 5. Implementation

Successfully implementing control charts within an organization requires more than just an understanding of the statistical techniques. It involves a systematic approach that includes planning, training, and the establishment of a supportive organizational culture. A well-executed implementation can transform an organization's approach to quality, moving it from a reactive, inspection-based model to a proactive, prevention-based one.

The implementation of control charts follows a systematic progression. It begins with the identification of critical processes where the application of control charts will have the greatest impact on quality and performance. A cross-functional team, comprising process owners, operators, and quality experts, is then formed to guide the effort. Comprehensive training in SPC principles and control chart methodology is provided to all team members and operators. This is followed by the development of a detailed data collection plan, which specifies the process characteristics to be monitored, the measurement methods, and the sampling strategy. Once sufficient data is collected, the control charts are constructed and analyzed to assess process stability. If the process is found to be out of control, the team investigates and eliminates the special causes of variation. This iterative cycle of analysis and corrective action continues until the process is brought into a state of statistical control. Finally, a system for ongoing monitoring and continuous improvement is established to ensure that the gains are sustained over time.

Several factors are critical for the successful implementation of control charts. **Management commitment** is essential. Leaders must provide the resources, training, and time necessary for the implementation to succeed. They must also foster a culture that is focused on continuous improvement and that empowers employees to take ownership of quality.

**Software tools** can greatly simplify the creation and management of control charts. Many statistical software packages, as well as spreadsheet programs, have built-in functions for creating control charts. These tools can automate the calculations and graphing, making it easier for teams to focus on interpreting the charts and improving the process.

# 6. Evidence & Impact

The impact of control charts on quality and performance improvement is well-documented across a multitude of industries. From their origins in manufacturing to their modern applications in healthcare and service industries, control charts have consistently demonstrated their effectiveness in reducing variation, improving quality, and lowering costs. The evidence for their impact can be found in numerous case studies and research publications that highlight the tangible benefits of this powerful statistical tool.

One of the most significant impacts of control charts is their ability to drive a fundamental shift in an organization's approach to quality. By providing a clear, visual method for distinguishing between common and special cause variation, control charts move quality control away from a reactive, inspection-based activity to a proactive, prevention-based one. This shift is exemplified in the work of W. Edwards Deming, who championed the use of control charts in post-war Japan. The widespread adoption of statistical process control, with the control chart as its centerpiece, was a key factor in the dramatic improvement of Japanese manufacturing quality and the country's rise as a global economic power. [9]

In the healthcare sector, the use of control charts has led to significant improvements in patient safety and the quality of care. For instance, a study published in the *Journal of the American Medical Association* demonstrated how control charts could be used to monitor and reduce surgical mortality rates. By tracking mortality rates over time and investigating special causes of variation, the participating hospitals were able to achieve a significant and sustained reduction in post-operative deaths. [10] Similarly, control charts have been used to reduce medication errors, decrease patient wait times, and lower the incidence of hospital-acquired infections, providing clear evidence of their positive impact on healthcare outcomes.

Numerous case studies from the manufacturing and service industries also attest to the power of control charts. A classic example is the experience of the Ford Motor Company in the 1980s. By implementing statistical process control and using control charts to monitor its manufacturing processes, Ford was able to dramatically improve the quality and reliability of its vehicles, leading to increased customer satisfaction and market share. In the service sector, companies have used control charts to improve the consistency of their service delivery, reduce customer complaints, and increase operational efficiency.

The measurable benefits of using control charts are substantial. Organizations that effectively implement control charts can expect to see a reduction in defects and rework, leading to lower costs and increased productivity. They can also achieve a greater understanding of their processes, enabling them to make data-driven decisions and focus their improvement efforts where they will have the greatest impact. Ultimately, the use of control charts leads to improved quality, increased customer satisfaction, and a stronger competitive position.

# 7. Cognitive Era Considerations

The advent of the Cognitive Era, characterized by the proliferation of big data, advanced analytics, and artificial intelligence, is transforming the landscape of statistical process control. While the fundamental principles of control charts remain as relevant as ever, these new technologies are opening up exciting possibilities for enhancing their capabilities and expanding their application. The integration of control charts with machine learning and AI is leading to more sophisticated, automated, and predictive forms of process monitoring and control.

In the era of **big data**, traditional manual methods of data collection and charting are often no longer feasible. Modern manufacturing and service processes are equipped with sensors and data acquisition systems that generate vast streams of data in real-time. This has led to the development of automated SPC systems that can monitor hundreds or even thousands of process variables simultaneously. These systems can automatically generate control charts, detect out-of-control signals, and even provide initial diagnostics to help engineers identify the root cause of a problem.

**Machine learning** algorithms are being integrated with control charts to create more intelligent and adaptive monitoring systems. For example, machine learning models can be used to build more accurate models of normal process behavior, leading to more sensitive and reliable control charts. They can also be used to identify complex, non-linear patterns in the data that may not be apparent on a traditional control chart. This can help to detect subtle process drifts and predict impending failures before they occur.

**Artificial intelligence (AI)** is further extending the capabilities of control charts by enabling more advanced forms of root cause analysis and process optimization. When an out-of-control signal is detected, an AI-powered system can analyze data from multiple sources to identify the most likely cause of the problem. These systems can also learn from past events to improve their diagnostic accuracy over time. Furthermore, AI can be used to optimize process parameters in real-time, automatically adjusting the process to keep it in a state of control and operating at peak performance.

The application of control charts is also expanding to new and more complex domains. In **IT operations**, control charts are being used to monitor the performance of computer networks, servers, and applications. They can help to detect anomalies, predict outages, and improve the reliability of IT services. In the realm of **social media**, control charts can be used to monitor sentiment and detect shifts in public opinion, providing valuable insights for marketing and brand management. As the digital transformation continues to reshape industries, the versatility of control charts will undoubtedly find even more novel applications.

# 8. Commons Alignment Assessment

The Control Charts pattern, while originating in the industrial, proprietary context of manufacturing, exhibits a surprising degree of alignment with the principles of a commons-based approach to organizing and creating value. Its emphasis on transparency, shared understanding, and collective problem-solving resonates with the core tenets of the commons. This assessment explores the alignment of the Control Charts pattern with the seven dimensions of a commons.

**Openness & Transparency:** Control charts are fundamentally a tool for transparency. By making process performance visible to all stakeholders, they create a shared understanding of the current state of the process and provide a common basis for decision-making. The visual nature of the control chart makes it accessible to a wide audience, from shop-floor operators to senior managers, breaking down information silos and fostering a culture of openness.

**Equitable Distribution:** While the direct outputs of a process may be privately owned, the knowledge and improvements generated through the use of control charts can be more equitably distributed. When operators are empowered to use control charts to improve their own work, they gain valuable skills and a greater sense of ownership and agency. The resulting improvements in quality and efficiency can also lead to broader societal benefits, such as safer products and a cleaner environment.

**Decentralized & Polycentric:** Control charts are a highly decentralized tool. They can be applied at any level of an organization, from individual workstations to entire value streams. This allows for a polycentric approach to quality improvement, where control and decision-making are distributed throughout the system. Teams can monitor and improve their own processes without the need for centralized command and control, leading to greater agility and resilience.

**Community & Collaboration:** Control charts are a powerful catalyst for collaboration. When a process goes out of control, the chart provides a clear signal that brings the team together to investigate the cause and implement a solution. This collaborative problem-solving process strengthens relationships and builds a sense of community. The shared language and framework provided by control charts facilitate communication and cooperation across different functions and departments.

**Sustainability & Resilience:** By promoting process stability and reducing waste, control charts contribute to the long-term sustainability of an organization and its surrounding ecosystem. A stable process is a more efficient process, consuming fewer resources and generating less pollution. The ability of control charts to detect and diagnose problems also enhances the resilience of a system, enabling it to better withstand and adapt to unexpected disruptions.

**Pluralistic & Inclusive:** The principles of statistical process control are universally applicable, but the specific implementation of control charts can and should be adapted to the local context. The choice of which process characteristics to monitor, the design of the data collection plan, and the interpretation of the charts should all be informed by the knowledge and experience of the people who do the work. This allows for a pluralistic and inclusive approach to quality improvement that respects the diversity of different settings and cultures.

**Purpose-driven & Value-aligned:** The ultimate purpose of control charts is to improve the quality of products and services, which in turn enhances the well-being of customers and society as a whole. By focusing on the reduction of variation and the elimination of waste, control charts align with the core values of craftsmanship, excellence, and respect for people. They provide a practical means for organizations to live out their commitment to creating value for all stakeholders.

# 9. Resources & References

## Further Reading

*   Wheeler, D. J. (2000). *Understanding Variation: The Key to Managing Chaos*. SPC Press.
*   Deming, W. E. (2000). *Out of the Crisis*. The MIT Press.
*   Montgomery, D. C. (2019). *Introduction to Statistical Quality Control*. Wiley.

## References

[1] ASQ. (n.d.). *Control Chart*. Retrieved from https://asq.org/quality-resources/control-chart

[2] Wikipedia. (2023, October 27). *Control chart*. Retrieved from https://en.wikipedia.org/wiki/Control_chart

[3] The W. Edwards Deming Institute. (2023). *A Beginner's Guide to Control Charts*. Retrieved from https://deming.org/a-beginners-guide-to-control-charts/

[4] JMP. (n.d.). *Understanding Control Charts*. Retrieved from https://www.jmp.com/en/statistics-knowledge-portal/quality-and-reliability-methods/control-charts

[5] NIST/SEMATECH. (n.d.). *e-Handbook of Statistical Methods*. Retrieved from https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm

[6] MoreSteam. (2025). *Control Charts: The Key Tool for Process Improvement*. Retrieved from https://www.moresteam.com/resources/blogs/control-charts-for-process-improvement

[7] iSixSigma. (2025). *A Guide to Control Charts*. Retrieved from https://www.isixsigma.com/control-charts/a-guide-to-control-charts/

[8] Wheeler, D. J. (2000). *Understanding Variation: The Key to Managing Chaos*. SPC Press.

[9] Deming, W. E. (2000). *Out of the Crisis*. The MIT Press.

[10] Benneyan, J. C. (1998). Statistical quality control methods in infection control and hospital epidemiology, Part I: Introduction and basic theory. *Infection Control & Hospital Epidemiology*, 19(3), 194-214.

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/control-charts/](https://commons-os.github.io/patterns/domain/control-charts/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_domain/control-charts.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/control-charts.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
