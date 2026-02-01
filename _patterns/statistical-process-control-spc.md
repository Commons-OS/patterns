---
id: pat_01kg50240zfdhtkt154ms1py31
page_url: https://commons-os.github.io/patterns/statistical-process-control-spc/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/statistical-process-control-spc.md
slug: statistical-process-control-spc
title: Statistical Process Control (SPC)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: implementation
  domain: operations
  category: [methodology, practice]
  era: [industrial, cognitive]
  origin: ["Walter Shewhart"]
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

Statistical Process Control (SPC) is a methodology that employs statistical techniques to monitor, control, and improve processes. It is a data-driven approach to quality management that enables organizations to shift from a reactive, detection-based approach to a proactive, prevention-based one. The core idea of SPC is to understand and reduce variation in a process, leading to more predictable and consistent outcomes. By analyzing data from a process in real-time, SPC can distinguish between natural, inherent variation (common cause) and variation that is the result of specific, identifiable events (special cause). This allows for timely intervention to correct problems before they result in non-conforming products or services.

The history of SPC dates back to the 1920s, when Walter A. Shewhart of Bell Labs developed the first control charts [1]. His work laid the foundation for a scientific approach to quality control. The methodology gained widespread use during World War II to ensure the quality of munitions and other critical products. After the war, its adoption in the United States waned, but it was enthusiastically embraced in Japan, where it became a cornerstone of the post-war quality revolution. In recent decades, SPC has seen a resurgence globally, particularly as an integral component of quality improvement initiatives like Six Sigma and Total Quality Management (TQM).

# 2. Core Principles

The effectiveness of Statistical Process Control is rooted in a set of fundamental principles that guide its application. These principles provide a framework for understanding and managing process variation.

At the heart of SPC is the **theory of variation**. This theory posits that variation is inherent in any process. Dr. W. Edwards Deming, a key figure in the quality movement, emphasized that understanding and properly reacting to this variation is crucial for effective management. SPC categorizes variation into two distinct types:

*   **Common Cause Variation:** This is the natural, random, and statistically predictable variation that is inherent in a process. It is the result of the combined effect of many small, unavoidable causes. A process that is only subject to common cause variation is said to be in a state of statistical control, or stable.
*   **Special Cause Variation:** This type of variation is caused by specific, identifiable events or circumstances that are not part of the process's normal operation. Examples include a machine malfunction, a new operator, or a bad batch of raw materials. Special cause variation is unpredictable and indicates that the process is out of statistical control, or unstable.

The primary goal of SPC is to identify and eliminate special cause variation to bring a process into a state of statistical control. Once a process is stable, its performance is predictable, and efforts can then be focused on reducing common cause variation to improve the process's capability.

Another core principle is the use of **data-driven decision making**. SPC replaces guesswork and intuition with objective analysis of process data. By collecting and analyzing data over time, SPC provides a clear picture of how a process is behaving. This allows for informed decisions about when to take action and when to leave a process alone, preventing the common mistake of over-adjusting a stable process, which can actually increase variation.

# 3. Key Practices

SPC employs a variety of tools and practices to monitor and control processes. The most well-known and widely used of these is the control chart.

**Control Charts** are graphical tools that display process data over time. A control chart has a center line (representing the process average), an upper control limit (UCL), and a lower control limit (LCL). These limits are calculated from the process data and represent the boundaries of common cause variation. Data points that fall within the control limits indicate that the process is in a state of statistical control. Data points that fall outside the control limits, or that exhibit non-random patterns, signal the presence of special cause variation, which requires investigation and corrective action.

There are many different types of control charts, each designed for a specific type of data:

*   **Control Charts for Variables Data:** These are used for measurable characteristics such as length, weight, or temperature.
    *   **X-bar and R charts:** Used to monitor the process average (X-bar) and process variation (R, the range) when data is collected in subgroups.
    *   **X-bar and s charts:** Similar to X-bar and R charts, but use the standard deviation (s) instead of the range to measure variation, which is more statistically efficient for larger subgroups.
    *   **Individuals and moving range (I-MR) charts:** Used when data is not collected in subgroups, but as individual measurements.
*   **Control Charts for Attributes Data:** These are used for count data, such as the number of defects or non-conforming units.
    *   **p-charts:** Monitor the proportion of non-conforming units in a sample.
    *   **np-charts:** Monitor the number of non-conforming units in a sample of constant size.
    *   **c-charts:** Monitor the number of defects in a unit of constant size.
    *   **u-charts:** Monitor the number of defects per unit when the sample size varies.

In addition to control charts, SPC is often used in conjunction with other quality tools, famously collected by Dr. Kaoru Ishikawa as the **Seven Basic Tools of Quality** [1]:

1.  **Cause-and-effect diagram (Ishikawa or fishbone diagram):** Helps to identify, explore, and display the possible causes of a specific problem or condition.
2.  **Check sheet:** A simple, prepared form for collecting and analyzing data.
3.  **Control chart:** As described above.
4.  **Histogram:** A graph that shows the frequency distribution of a set of data.
5.  **Pareto chart:** A bar graph that shows which factors are the most significant, based on the 80/20 rule.
6.  **Scatter diagram:** A graph that displays the relationship between two variables.
7.  **Stratification:** A technique to separate data gathered from a variety of sources so that patterns can be seen.

# 4. Application Context

Statistical Process Control is a versatile methodology that can be applied in a wide variety of contexts where processes need to be monitored and controlled. While it originated in industrial manufacturing, its principles and tools have proven effective in numerous other sectors.

**Manufacturing:** This is the traditional and most common application area for SPC. It is used to monitor and control production processes, from the quality of raw materials to the final assembly of products. By using control charts, manufacturers can reduce scrap and rework, improve product consistency, and increase productivity. Industries such as automotive, aerospace, electronics, and pharmaceuticals rely heavily on SPC to meet stringent quality standards.

**Healthcare:** The healthcare industry has increasingly adopted SPC to improve patient safety and the quality of care. A systematic review of SPC applications in healthcare found its use in a wide range of settings and specialties [3]. It has been used to monitor surgical outcomes, reduce medication errors, control hospital-acquired infections, and improve patient satisfaction. For example, control charts can be used to track the time it takes to administer medication in an emergency room, helping to identify and address delays. Patients themselves can even use SPC principles to manage chronic conditions like asthma or diabetes by tracking key health indicators over time [3].

**Service Industries:** SPC is also applicable in service-oriented industries such as finance, logistics, and customer service. In a call center, for instance, SPC can be used to monitor call handling times, customer satisfaction scores, or first-call resolution rates. In logistics, it can be used to track on-time delivery performance or the accuracy of order fulfillment. The key is to identify the critical-to-quality characteristics of the service process and collect data to monitor their performance.

**Software Development:** In the realm of software engineering, SPC can be applied to monitor and control development processes. For example, it can be used to track the number of defects found during testing, the time it takes to resolve bugs, or the stability of a software build. This helps to improve software quality and the predictability of release schedules.

# 5. Implementation

Implementing Statistical Process Control effectively requires a systematic approach that goes beyond simply creating control charts. It involves a cultural shift towards data-driven decision making and continuous improvement. The following steps, adapted from a widely recognized implementation model [2], provide a roadmap for a successful SPC program.

**Step 1: Build a Foundation for Problem Solving**

The first and most critical step is to create an organizational environment that supports problem-solving and continuous improvement. This is often the most challenging part of the implementation. Key elements of this foundation include:

*   **Management Commitment:** Lasting success requires a deep commitment from top leadership. They must champion the SPC initiative and provide the necessary resources.
*   **Employee Involvement:** The people closest to the process are often the ones who understand it best. Engaging employees at all levels is essential for identifying and solving problems.
*   **Cooperative Culture:** SPC thrives in an environment of teamwork and collaboration, where managers and workers have a non-adversarial relationship focused on shared goals.
*   **Incentives and Recognition:** Providing recognition, rewards, and creating a sense of satisfaction for the people involved helps to secure the long-term commitment needed for success.

**Step 2: Identify Key Processes and Variables**

Once the foundation is in place, the next step is to identify the critical processes and variables that have the most significant impact on quality and performance. This involves using problem-solving tools like brainstorming, Pareto charts, and cause-and-effect diagrams to prioritize areas for improvement. This ensures that SPC efforts are focused where they can make the biggest difference.

**Step 3: Bring Processes into Statistical Control**

With key variables identified, the next phase is to use control charts to monitor the process and bring it into a state of statistical control. This involves:

1.  **Choosing the right control chart:** Select the appropriate chart based on the type of data being collected (variables or attributes).
2.  **Collecting data:** Gather data from the process in a systematic way.
3.  **Calculating control limits:** Use the collected data to calculate the center line and control limits.
4.  **Plotting the data and interpreting the chart:** Plot the data points on the chart and look for signs of special cause variation (points outside the limits, non-random patterns). When special causes are identified, investigate the root cause and take corrective action to prevent recurrence.

**Step 4: Measure Process Capability**

After a process has been brought into a state of statistical control, the next question is whether it is capable of meeting the customer's requirements or specifications. This is assessed by comparing the natural variation of the process (the control limits) to the specification limits. Process capability indices, such as Cp and Cpk, are used to quantify this relationship. A capable process is one where the natural variation is well within the specification limits.

**Step 5: Plan for Process Improvement**

If a process is not capable of meeting requirements, a plan for improvement is needed. This may involve fundamental changes to the process, such as new equipment, different materials, or improved methods. The Plan-Do-Study-Act (PDSA) cycle is a useful framework for managing these improvement efforts. After changes are made, the process is monitored again using control charts to verify the effectiveness of the improvements.

**Step 6: Foster Continuous Improvement**

SPC is not a one-time project; it is a commitment to ongoing, continuous improvement. Once one process is brought under control and made capable, the organization moves on to the next priority area. The cycle of monitoring, controlling, and improving becomes an integral part of the organization's culture.

# 6. Evidence & Impact

The impact of Statistical Process Control on quality and productivity is well-documented across various industries. The methodology's ability to reduce variation and provide insights into process performance leads to tangible benefits.

One of the most significant impacts of SPC is the **reduction of defects and waste**. By identifying and addressing special cause variation, organizations can prevent the production of non-conforming products. This leads to lower scrap and rework costs, as well as a reduction in warranty claims. A case study in a manufacturing firm demonstrated that the use of SPC resulted in significant cost savings by improving quality and reducing waste [4].

SPC also leads to **improved product quality and consistency**. By bringing processes into a state of statistical control, organizations can ensure that their products consistently meet customer expectations. This not only enhances customer satisfaction but also strengthens brand reputation. The focus on reducing variation leads to more uniform products and a more predictable process output.

In the healthcare sector, SPC has been shown to have a profound impact on patient safety and the quality of care. A systematic review of 57 studies found that SPC was applied in a wide range of clinical settings, leading to improvements in processes and patient outcomes [3]. For example, it has been used to reduce medication errors, decrease the incidence of hospital-acquired infections, and improve the timeliness of critical medical procedures. The review also highlighted that SPC can empower patients to manage their own chronic conditions, such as asthma and diabetes, by tracking their health data over time, thus giving the tool a therapeutic dimension [3].

Furthermore, the implementation of SPC can have a positive impact on organizational culture. It fosters a data-driven approach to problem-solving and promotes a culture of continuous improvement. By involving employees at all levels in the monitoring and improvement of processes, SPC can increase engagement and create a shared sense of ownership for quality.

# 7. Cognitive Era Considerations

As we move into the cognitive era, characterized by big data, artificial intelligence (AI), and machine learning (ML), the principles and practices of Statistical Process Control are evolving. The integration of these new technologies is enhancing the power and applicability of SPC, allowing for more sophisticated and automated process monitoring and control.

The sheer volume, velocity, and variety of data generated in modern industrial and business processes present both a challenge and an opportunity for SPC. Traditional manual methods of data collection and charting are often inadequate for handling big data. AI and ML algorithms can be used to automate the process of data analysis, identifying complex patterns and correlations that would be impossible to detect with conventional methods. This allows for a more comprehensive and real-time understanding of process behavior.

A key area where AI is transforming SPC is in **pattern recognition on control charts**. Machine learning models, such as neural networks and support vector machines, can be trained to automatically recognize non-random patterns (e.g., trends, cycles, shifts) that indicate the presence of special cause variation. This automates a task that traditionally required a trained human analyst, leading to faster and more consistent diagnosis of process issues.

Furthermore, the integration of AI and SPC is leading to the development of more **flexible and robust control charting techniques**. One research paper proposes a new type of control chart, the "class-chart," which uses AI classifiers to monitor processes with multiple categorical and latent variables [4]. This approach is more adaptable to complex processes where traditional SPC assumptions may not hold. It also has the ability to make future predictions, moving SPC from a purely monitoring tool to a proactive control system.

In the context of the Internet of Things (IoT), where sensors are embedded in machines and products, SPC can be used to monitor vast networks of interconnected devices in real-time. AI-powered SPC systems can analyze the streams of data from these sensors to predict equipment failures, optimize maintenance schedules, and improve overall operational efficiency.

# 8. Commons Alignment Assessment

(Note: The official 7 dimensions of the Commons OS Alignment Assessment were not available at the time of writing. The following is a proposed assessment based on general principles of the commons and open-source projects. The score is a preliminary estimate.)

**Overall Score: 1/5**

Statistical Process Control, in its traditional application, has a low alignment with the principles of the commons. It is primarily a methodology used within individual organizations to improve their internal processes and gain a competitive advantage. However, there are aspects of SPC that have the potential for greater commons alignment, particularly in the context of open-source implementations and the sharing of best practices.

| Dimension | Score (1-5) | Rationale |
| :--- | :--- | :--- |
| **1. Openness & Transparency** | 2 | The principles of SPC are well-documented and publicly available. However, the implementation of SPC within an organization is often proprietary, and the data and results are typically not shared openly. |
| **2. Community Governance** | 1 | SPC is a methodology, not a community-governed project. Its application is determined by the management of the organization using it. There is no formal community governance structure. |
| **3. Shared Resources** | 2 | While there are many books, articles, and training materials available on SPC, the actual implementation and the knowledge gained from it are often siloed within individual organizations. There is no central repository of shared SPC resources or case studies in a commons-based model. |
| **4. Equitable Access** | 3 | The basic tools and knowledge of SPC are widely accessible. However, the cost of training, software, and implementation can be a barrier for smaller organizations and individuals. |
| **5. Sustainability** | 1 | The sustainability of SPC within an organization depends on its continued commitment and resources. There is no broader community or ecosystem to ensure its long-term sustainability as a commons. |
| **6. Interoperability** | 2 | SPC data and software are often not interoperable between different systems. There is a lack of open standards for SPC data exchange. |
| **7. Contribution to the Commons** | 1 | In its typical application, SPC is used for private gain and does not directly contribute to a shared knowledge commons. The benefits are primarily captured by the organization implementing it. |

# 9. Resources & References

[1] ASQ. (n.d.). *What is Statistical Process Control? SPC Quality Tools*. Retrieved from https://asq.org/quality-resources/statistical-process-control

[2] DataMyte. (2021, December 18). *How To Implement Statistical Quality Control (SPC) in 6 Steps*. Retrieved from https://datamyte.com/knowledge-base/how-to-implement-statistical-quality-control-spc-in-6-steps/

[3] Thor, J., Lundberg, J., Ask, J., Olsson, J., Carli, C., Härenstam, K. P., & Brommels, M. (2007). Application of statistical process control in healthcare improvement: systematic review. *Quality and Safety in Health Care*, *16*(5), 387–399. https://doi.org/10.1136/qshc.2006.022194

[4] Boaventura, L. L., Ferreira, P. H., & Fiaccone, R. L. (2022). On flexible Statistical Process Control with Artificial Intelligence: Classification control charts. *Expert Systems with Applications*, *194*, 116492. https://doi.org/10.1016/j.eswa.2021.116492

[5] ASQ. (n.d.). *History of Quality*. Retrieved from https://asq.org/quality-resources/history-of-quality
