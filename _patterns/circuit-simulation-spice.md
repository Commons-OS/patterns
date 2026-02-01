---
id: pat_01kg5023xted0bt7yxpv725xc5
page_url: https://commons-os.github.io/patterns/circuit-simulation-spice/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/circuit-simulation-spice.md
slug: circuit-simulation-spice
title: Circuit Simulation (SPICE)
aliases: [SPICE]
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
classification:
  universality: domain
  domain: design
  category: [tool, methodology]
  era: [digital]
  origin: [academic, uc-berkeley]
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: [https://en.wikipedia.org/wiki/SPICE, https://www.cadence.com/en_US/home/explore/spice-simulation.html, https://resources.altium.com/p/what-spice-simulation-electronics-design, https://developer.nvidia.com/blog/using-generative-ai-models-in-circuit-design/, https://silvaco.com/blog/spice-model-generation-by-machine-learning/]

license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Circuit Simulation (SPICE) is a foundational pattern in electronic engineering that utilizes software to simulate and analyze the behavior of electronic circuits. SPICE, an acronym for Simulation Program with Integrated Circuit Emphasis, provides a virtual environment where engineers can design, test, and verify circuit performance before committing to physical prototypes. This process is crucial for identifying design flaws, optimizing performance, and ensuring the reliability of electronic systems, ranging from simple analog circuits to complex integrated circuits (ICs). By modeling the interactions of various electronic components—such as transistors, resistors, and capacitors—SPICE enables a deep understanding of a circuit's electrical characteristics under diverse conditions. This predictive capability is indispensable in modern electronics, where the cost and complexity of manufacturing, particularly for ICs, demand a high degree of confidence in the design before production. The pattern's origins trace back to the University of California, Berkeley, where it was developed in the early 1970s, and it has since become an industry-standard tool, evolving into numerous commercial and open-source variants.


### 2. Core Principles

The effectiveness of SPICE as a circuit simulation tool is rooted in a set of core principles that have defined its development and application since its inception. These principles ensure that the simulation accurately reflects the real-world behavior of electronic circuits, providing engineers with a reliable platform for design and analysis.

**1. Nodal Analysis as the Foundation:** At its heart, SPICE employs nodal analysis to construct the system of equations that describe a circuit. This method simplifies the circuit into a collection of nodes and the voltages at these nodes relative to a reference (ground). By applying Kirchhoff's Current Law (KCL) at each node, a set of simultaneous equations is generated, representing the entire circuit's behavior. This approach is systematic and well-suited for computer-based analysis, forming the mathematical backbone of the simulation.

**2. Comprehensive Component Modeling:** The accuracy of a SPICE simulation is heavily dependent on the quality of the models used to represent the electronic components. SPICE utilizes a vast library of mathematical models for a wide range of devices, from basic passive components like resistors and capacitors to active devices like diodes, bipolar junction transistors (BJTs), and metal-oxide-semiconductor field-effect transistors (MOSFETs). These models capture the complex, often nonlinear, electrical characteristics of the components, allowing for a high-fidelity simulation of the circuit's performance.

**3. Numerical Solution of System Equations:** SPICE translates the circuit schematic and component models into a system of nonlinear differential algebraic equations. To solve these equations, which can be highly complex for large circuits, SPICE employs sophisticated numerical methods. Techniques such as the Newton-Raphson method are used to solve the nonlinear DC equations, while implicit integration methods, like the trapezoidal or Gear's method, are used for transient analysis. These numerical solvers are the engine of SPICE, enabling the calculation of circuit behavior over time or across a range of frequencies.

**4. Diverse Analysis Capabilities:** A key principle of SPICE is its ability to perform various types of analyses, offering a multifaceted view of circuit performance. The primary analysis types include:
    *   **DC Analysis:** Determines the DC operating point of the circuit.
    *   **AC Analysis:** Analyzes the circuit's linear response to small-signal AC inputs at various frequencies.
    *   **Transient Analysis:** Simulates the circuit's behavior over time in response to time-varying inputs.

These core principles collectively enable SPICE to be a powerful and versatile tool for circuit simulation, providing engineers with the insights needed to design and verify robust electronic systems.


### 3. Key Practices

Effective utilization of SPICE for circuit simulation involves a series of key practices that ensure accurate and meaningful results. These practices guide the engineer from the initial circuit concept to the final analysis, forming a systematic workflow for virtual prototyping and verification.

**1. Schematic Capture:** The process begins with the creation of a circuit schematic using a graphical editor. This visual representation of the circuit serves as the blueprint for the simulation. Modern electronic design automation (EDA) tools provide sophisticated schematic capture environments that allow engineers to place and connect components from extensive libraries.

**2. Netlist Generation:** Once the schematic is complete, it is converted into a text-based netlist. The netlist is a machine-readable description of the circuit, detailing the components, their connections (nodes), and their values. This is the primary input for the SPICE simulation engine.

**3. Component Model Selection:** The fidelity of the simulation is directly tied to the accuracy of the component models. Engineers must select appropriate models from the SPICE library that accurately represent the electrical behavior of the real-world components. For critical components, it may be necessary to use manufacturer-provided models or even create custom models.

**4. Analysis Type Selection and Configuration:** SPICE offers a variety of analysis types, and selecting the correct one is crucial for obtaining the desired information. The most common analyses include:
    *   **DC Operating Point Analysis:** To determine the DC voltages and currents in the circuit.
    *   **AC Sweep Analysis:** To analyze the circuit's frequency response.
    *   **Transient Analysis:** To observe the circuit's behavior over time.
Each analysis type requires specific configuration, such as setting the frequency range for an AC sweep or the time duration for a transient analysis.

**5. Simulation Execution:** With the netlist, models, and analysis settings in place, the SPICE simulation is executed. The simulation engine solves the complex system of equations that describe the circuit, generating a large amount of data representing the circuit's behavior.

**6. Post-Simulation Analysis and Visualization:** The raw data produced by the simulation is often extensive and difficult to interpret directly. Therefore, post-simulation analysis tools are used to process and visualize the results. This can include plotting voltages and currents, performing Fourier analysis, and calculating performance metrics.

**7. Design Iteration and Optimization:** The insights gained from the simulation results are used to refine and optimize the circuit design. This iterative process of simulation, analysis, and design modification is a cornerstone of using SPICE effectively. It allows engineers to explore the design space, identify and correct issues, and improve performance before building a physical prototype.


### 4. Application Context

The Circuit Simulation (SPICE) pattern is applicable across a wide spectrum of electronics design and engineering, serving as a critical tool for both educational and professional purposes. Its versatility allows it to be applied in various contexts where the behavior of electronic circuits must be understood, predicted, and verified.

**Integrated Circuit (IC) Design:** This is the original and most critical application context for SPICE. Given the high cost and complexity of IC fabrication, it is virtually impossible to breadboard or physically prototype an IC. SPICE simulation is the industry-standard method for verifying the functionality and performance of a design at the transistor level before committing to the expensive process of manufacturing. It allows designers to detect flaws, analyze timing, and assess power consumption with high accuracy.

**Printed Circuit Board (PCB) Level Design:** While discrete components on a PCB can be prototyped, SPICE simulation offers significant advantages. It enables the analysis of effects that are difficult to measure or replicate on a physical breadboard, such as parasitic capacitances and inductances that can significantly impact circuit performance at high frequencies. Furthermore, SPICE facilitates statistical analysis, like Monte Carlo simulations, to understand the impact of component tolerances on the circuit's overall behavior, a task that would be impractical to perform with physical prototypes.

**Analog and Mixed-Signal Circuits:** SPICE is exceptionally well-suited for the simulation of analog and mixed-signal circuits, where the continuous nature of the signals makes their behavior complex and often non-intuitive. It is an essential tool for designing filters, amplifiers, data converters, and phase-locked loops (PLLs).

**Power Electronics:** In the design of power supplies, DC-DC converters, and motor control circuits, SPICE is used to analyze efficiency, thermal behavior, and transient responses. The ability to simulate the switching behavior of power devices like MOSFETs and IGBTs is crucial for optimizing these designs.

**Educational Settings:** SPICE is a fundamental teaching tool in electrical engineering curricula. It provides students with a virtual laboratory where they can experiment with circuit designs, visualize electrical concepts, and gain an intuitive understanding of circuit theory without the need for expensive lab equipment.


### 5. Implementation

Implementing the Circuit Simulation (SPICE) pattern involves a structured workflow that leverages specialized software tools to move from a conceptual circuit design to a detailed performance analysis. The process is highly iterative, allowing for continuous refinement and optimization of the circuit before any hardware is built.

**1. Selecting a SPICE Simulator:** The first step is to choose a SPICE simulation tool. The landscape of SPICE simulators is diverse, catering to different needs and budgets:
    *   **Berkeley SPICE:** The original, open-source version from which all others are derived. While still available, it is primarily of historical and academic interest.
    *   **Commercial Simulators:** These are powerful, feature-rich tools integrated into comprehensive Electronic Design Automation (EDA) suites. Prominent examples include Cadence's PSpice and Spectre, Synopsys's HSPICE, and Altium Designer's integrated simulator. These tools offer extensive component libraries, advanced analysis capabilities, and professional support.
    *   **Free and Open-Source Simulators:** For students, hobbyists, and professionals on a budget, several high-quality free options are available. LTspice from Analog Devices and ngspice are popular choices that provide robust simulation capabilities.

**2. The Simulation Workflow:** Regardless of the specific tool used, the implementation of a SPICE simulation generally follows these steps:
    *   **Schematic Capture:** The circuit is drawn in a schematic editor. This involves placing components from a library and wiring them together to form the desired circuit topology.
    *   **Model Assignment:** Each component in the schematic must be associated with a SPICE model. These models, often provided by component manufacturers, contain the mathematical parameters that describe the device's electrical behavior. The accuracy of the simulation is critically dependent on the quality of these models.
    *   **Netlist Generation:** The schematic capture tool automatically translates the graphical representation of the circuit into a text-based netlist. This netlist is the input file for the SPICE engine, describing all the components and their interconnections.
    *   **Simulation Configuration:** The user defines the type of analysis to be performed (e.g., DC, AC, transient) and sets the relevant parameters. For a transient analysis, this would include the start and end times and the maximum time step. For an AC analysis, the frequency range and number of points would be specified.
    *   **Execution:** The SPICE engine reads the netlist and the component models, constructs the system of equations, and solves them numerically based on the configured analysis. This can be a computationally intensive process for large and complex circuits.
    *   **Post-Processing and Analysis:** The simulation results, typically voltages and currents at various points in the circuit, are then loaded into a waveform viewer. This tool allows the engineer to plot and analyze the data, measure performance characteristics, and gain insights into the circuit's behavior.

**3. Iterative Design and Refinement:** The results of the simulation are used to verify if the circuit meets its design specifications. If not, the engineer returns to the schematic, modifies the design, and re-runs the simulation. This iterative loop of simulation, analysis, and refinement is the core of the SPICE-based design process, enabling the optimization of the circuit for performance, cost, and reliability.


### 6. Evidence & Impact

The impact of the Circuit Simulation (SPICE) pattern on the electronics industry is profound and well-documented. Since its introduction, SPICE has fundamentally changed the way electronic circuits are designed, verified, and manufactured, leading to significant advancements in technology and a dramatic increase in the complexity and reliability of electronic devices.

**Evidence of Efficacy:**

The widespread adoption of SPICE by virtually every major company in the semiconductor and electronics industries is the most compelling evidence of its effectiveness. The fact that SPICE has remained the industry-standard for over four decades, despite the rapid pace of technological change, speaks to the robustness and enduring value of its core principles. The continuous development of commercial and open-source SPICE variants, each building upon the original Berkeley foundation, further demonstrates the vitality and relevance of this pattern.

**Impact on the Electronics Industry:**

*   **Reduced Design Costs and Time-to-Market:** By enabling engineers to thoroughly test and debug their designs in a virtual environment, SPICE significantly reduces the need for expensive and time-consuming physical prototypes. This leads to a shorter design cycle, allowing companies to bring new products to market faster and at a lower cost. The ability to identify and fix design flaws early in the process prevents costly revisions later in the manufacturing stage.

*   **Increased Circuit Complexity and Performance:** SPICE has been a key enabler of Moore's Law, which describes the exponential growth in the number of transistors on an integrated circuit. The ability to simulate and analyze the behavior of millions or even billions of transistors has allowed engineers to design increasingly complex and powerful microprocessors, memory chips, and other ICs. Without SPICE, the design of modern digital and analog systems would be intractable.

*   **Improved Design Reliability and Robustness:** SPICE allows engineers to analyze the performance of their circuits under a wide range of operating conditions, including variations in temperature, voltage, and component tolerances. This capability is crucial for designing robust and reliable products that will function correctly in the real world. Monte Carlo analysis, a feature available in many SPICE simulators, allows for a statistical analysis of the impact of component variations, ensuring that the design is resilient to manufacturing imperfections.

*   **Democratization of Electronics Design:** The availability of free and open-source SPICE simulators, such as LTspice and ngspice, has made powerful circuit simulation tools accessible to a broad audience, including students, hobbyists, and small businesses. This has fostered a culture of innovation and experimentation, allowing individuals and organizations with limited resources to design and develop sophisticated electronic systems.


### 7. Cognitive Era Considerations

The advent of the Cognitive Era, characterized by the widespread application of artificial intelligence (AI) and machine learning (ML), is beginning to reshape the landscape of electronic design automation, including the venerable Circuit Simulation (SPICE) pattern. While the core principles of SPICE remain as relevant as ever, AI and ML are introducing new capabilities and efficiencies that augment and accelerate the traditional simulation workflow.

**1. AI-Powered SPICE Model Generation:** One of the most significant impacts of AI is in the creation of SPICE models. Developing accurate models from measurement data has traditionally been a time-consuming and expert-driven process. Machine learning techniques, particularly neural networks, are now being used to automate this process. These ML-based tools can learn the complex relationships between physical parameters and electrical behavior, generating highly accurate SPICE models in a fraction of the time it would take a human expert.

**2. Generative Design and Optimization:** Generative AI is emerging as a powerful tool for exploring the design space and optimizing circuit performance. Instead of relying solely on the iterative refinement of a human-created design, engineers can now leverage AI algorithms to generate and evaluate thousands of design variations automatically. These algorithms can be trained to optimize for specific performance metrics, such as power consumption, area, or speed, leading to novel and highly efficient circuit topologies that a human designer might not have considered.

**3. Intelligent Simulation and Analysis:** AI is also being integrated into the simulation process itself. ML models can be used to predict the outcome of simulations, identify potential convergence issues, and even suggest modifications to the circuit to improve performance. This can significantly speed up the simulation process, especially for large and complex circuits where a full SPICE simulation can be computationally expensive.

**4. Automated Circuit Design:** The ultimate vision for AI in electronics design is the fully automated generation of circuits from high-level specifications. While this is still an active area of research, several startups and research groups are developing AI-powered tools that can take a set of requirements and automatically generate a complete schematic, select components, and even lay out the PCB. These tools leverage a combination of generative AI, knowledge graphs, and SPICE simulation to create functional and manufacturable designs.

In the Cognitive Era, the SPICE pattern is evolving from a purely analytical tool to a key component of a more intelligent and automated design ecosystem. The synergy between the rigorous physics-based simulation of SPICE and the data-driven learning capabilities of AI promises to unlock new levels of design productivity and innovation.


### 8. Commons Alignment Assessment (v2.0)

This assessment evaluates the pattern based on the Commons OS v2.0 framework, which focuses on the pattern's ability to enable resilient collective value creation.

**1. Stakeholder Architecture:**
The SPICE pattern primarily defines rights and responsibilities for its direct users, such as engineers and designers, by providing a standardized tool for circuit verification. Its open-source variants create a commons where the right to use, modify, and distribute the software is guaranteed, fostering a community of contributors and users. However, the framework does not explicitly extend rights to non-human stakeholders like the environment, nor does it inherently prescribe responsibilities for the long-term impact of the technologies it helps create.

**2. Value Creation Capability:**
The pattern is a powerful enabler of collective value creation, extending far beyond immediate economic output. By allowing for the design and verification of complex electronics, SPICE underpins the creation of vast knowledge, technological, and infrastructural value. This capability is foundational to modern society, enabling everything from communication systems to medical devices, thereby generating immense social and resilience value.

**3. Resilience & Adaptability:**
SPICE directly enhances the resilience and adaptability of electronic systems by allowing designers to simulate performance under a wide range of conditions and stresses. This virtual testing helps create robust hardware that can maintain coherence and function reliably in unpredictable real-world environments. The pattern itself has proven highly adaptable, evolving over decades and integrating new technologies like AI to meet the demands of increasing complexity.

**4. Ownership Architecture:**
The ownership architecture of SPICE is a tale of two models. The original public domain release and its open-source successors represent a form of knowledge commons, where ownership is defined by the right to use and contribute, not by monetary equity. This coexists with a commercial ecosystem where ownership is proprietary, yet still reliant on the interoperability of the open standard. This dual architecture has proven to be a resilient model for sustaining both innovation and access.

**5. Design for Autonomy:**
The pattern is exceptionally well-suited for autonomous systems. Its text-based netlist format and deterministic simulation engine make it highly compatible with AI-driven and generative design processes, which can automate the creation and optimization of circuits with minimal human coordination. As noted in the Cognitive Era Considerations, SPICE is becoming a key component in a more automated and intelligent design ecosystem.

**6. Composability & Interoperability:**
High composability and interoperability are core features of the SPICE pattern. Its standardized format allows it to serve as a foundational layer upon which countless other design tools and patterns are built. This enables seamless integration within larger electronic design automation (EDA) workflows and fosters a modular, interoperable ecosystem of specialized tools.

**7. Fractal Value Creation:**
The value-creation logic of circuit simulation is inherently fractal. The same fundamental principles of modeling and analysis can be applied at multiple scales, from the behavior of a single transistor, to a complex integrated circuit with billions of components, and even to the interaction of multiple electronic systems. This scalability allows the pattern to be a consistent value-creation engine across all levels of electronic design.

**Overall Score: 4 (Value Creation Enabler)**

**Rationale:**
Circuit Simulation (SPICE) is a quintessential Value Creation Enabler. While not a complete socio-economic architecture itself, it provides the critical infrastructure for resilient value creation in the technological commons. Its open-source roots created a powerful standard that enables massive innovation, knowledge sharing, and the development of the complex electronic systems that underpin modern society. The pattern's high interoperability, scalability, and growing synergy with AI make it a foundational tool for building the future.

**Opportunities for Improvement:**
- Explicitly integrate lifecycle assessment tools to help designers model the environmental impact and resource consumption of their circuits.
- Develop standardized models for failure modes and long-term degradation to better assess and design for multi-generational resilience.
- Create educational resources that frame the use of SPICE within a broader ethical context, encouraging designers to consider the stakeholder impacts of their creations.

The Circuit Simulation (SPICE) pattern exhibits a strong and multifaceted alignment with the principles of a commons-based economy. Its history, evolution, and impact on the electronics industry provide a compelling case study of how a shared resource, born in the academic commons, can foster innovation, democratize access to technology, and create a vibrant ecosystem of both commercial and non-commercial activity. This assessment explores the various dimensions of SPICE's commons alignment, from its open-source origins to its role as a foundational knowledge infrastructure.

**1. Open Source and Public Domain as a Foundational Principle:**

The most significant aspect of SPICE's commons alignment is its origin as a public domain software. Developed at the University of California, Berkeley, a public institution, SPICE was released in a way that ensured it would be a resource for all. This deliberate decision by its creators, particularly Donald Pederson's insistence on rewriting the proprietary CANCER program to remove restrictions, set the stage for SPICE to become a global standard. By making the source code available, the creators of SPICE established a knowledge commons that has been built upon for decades. This act of "commoning" the software has had a profound and lasting impact, preventing a single entity from monopolizing this critical technology and ensuring that it could be freely used, studied, modified, and distributed.

**2. Enabling a Diverse and Interoperable Ecosystem:**

The open nature of SPICE has given rise to a rich and diverse ecosystem of simulation tools. This ecosystem includes:

*   **Commercial Innovations:** Numerous companies have built powerful, proprietary EDA tools on top of the SPICE foundation. These commercial offerings, while not open source themselves, have benefited from the existence of a common, interoperable standard. The competition and innovation in the commercial EDA market have been fueled by the shared language and methodology that SPICE provides.
*   **Open-Source Continuations:** The original Berkeley SPICE has been forked and extended into several open-source projects, such as ngspice and Xyce. These projects continue the tradition of providing free and open access to high-quality simulation tools, ensuring that the commons continues to be nurtured and expanded.
*   **Community-Driven Development:** The open-source SPICE variants are often maintained and improved by a global community of volunteers. This collaborative model of development is a hallmark of a commons-based approach, where a shared resource is collectively managed and sustained by its users.

**3. Democratization of Access and Knowledge:**

SPICE has played a crucial role in democratizing access to electronics design. The availability of free and powerful SPICE simulators has lowered the barrier to entry for students, hobbyists, and small businesses, enabling them to learn, experiment, and innovate without the need for expensive software licenses. This has fostered a more inclusive and participatory culture in electronics, where a great idea can be pursued regardless of the designer's institutional affiliation or financial resources. Furthermore, the vast body of literature, tutorials, and online communities dedicated to SPICE constitutes a rich knowledge commons that supports learning and problem-solving.

**4. Fostering a Culture of Collaboration and Knowledge Sharing:**

The ubiquity of SPICE has created a common language and framework for circuit designers worldwide. This shared understanding facilitates collaboration and knowledge sharing across academic and industrial boundaries. When engineers from different organizations can all "speak SPICE," it becomes easier to share designs, debug problems, and build upon each other's work. The use of SPICE in academic research and its subsequent adoption by industry has created a virtuous cycle of knowledge transfer, with new models and techniques developed in academia often finding their way into commercial and open-source tools.

**5. A Foundation for Further Innovation:**

The SPICE pattern is not a static artifact; it is a living, evolving commons that continues to be a foundation for new innovations. The integration of AI and machine learning into the SPICE workflow is the latest chapter in this story. The open and extensible nature of the SPICE ecosystem allows for the seamless integration of these new technologies, further enhancing the power and accessibility of circuit simulation. The ability of the commons to adapt and incorporate new ideas is a testament to its resilience and long-term value.

In conclusion, the Circuit Simulation (SPICE) pattern is a powerful example of a technology commons that has delivered immense value to society. Its open-source origins, its role in fostering a diverse and interoperable ecosystem, its democratization of access to knowledge and tools, and its ability to serve as a foundation for ongoing innovation all point to a deep and enduring alignment with the principles of a commons-based economy. The story of SPICE is a powerful reminder that the most valuable resources are often those that are shared.


### 9. Resources & References

**Key SPICE Simulators:**

*   **[ngspice](http://ngspice.sourceforge.net/):** A popular and actively developed open-source SPICE simulator that is based on Berkeley SPICE 3f5. It is a great choice for both academic and professional use.
*   **[LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html):** A free, high-performance SPICE simulator from Analog Devices. It is widely used in the industry and is known for its fast simulation speeds and extensive library of models for Analog Devices components.
*   **[PSpice](https://www.pspice.com/):** A commercial SPICE simulator from Cadence Design Systems. It is a powerful and feature-rich tool that is tightly integrated with the OrCAD and Allegro design environments.
*   **[HSPICE](https://www.synopsys.com/implementation-and-signoff/ams-simulation/hspice.html):** A commercial SPICE simulator from Synopsys, widely regarded as the gold standard for accuracy in the semiconductor industry.

**Further Reading and Academic Papers:**

*   Nagel, L. W., and Pederson, D. O., "SPICE (Simulation Program with Integrated Circuit Emphasis)", Memorandum No. ERL-M382, University of California, Berkeley, Apr. 1973. (The original paper that introduced SPICE)
*   Nagel, L. W., "SPICE2: A Computer Program to Simulate Semiconductor Circuits," Memorandum No. ERL-M520, University of California, Berkeley, May 1975. (The paper describing the much-improved SPICE2)
*   Vladimirescu, A., "The SPICE Book," John Wiley & Sons, 1994. (A comprehensive book on SPICE and its use)

**Online Communities and Forums:**

*   **[All About Circuits Forum](https://forum.allaboutcircuits.com/):** A large and active online community for electronics enthusiasts and professionals, with a dedicated section for SPICE simulation.
*   **[EEVblog Forum](https://www.eevblog.com/forum/):** Another popular forum for electronics engineers, with frequent discussions and tutorials on SPICE and other EDA tools.
