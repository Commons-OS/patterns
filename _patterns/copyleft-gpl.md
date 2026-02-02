---
id: pat_82b24c1c14e64a949a0f78d4
title: "Copyleft (GPL)"
slug: copyleft-gpl
aliases: []
classification:
  universality: domain
  domain: startup
  category: [governance]
  era: [cognitive]
  origin: [startup-ecosystem]
  status: draft
  commons_alignment: 5
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
confidence_score: 0.7
sources: []
version: 1.0.0
last_updated: 2026-02-01
page_url: "https://commons-os.github.io/patterns/copyleft-gpl/"
github_url: "https://github.com/Commons-OS/patterns/blob/main/_patterns/copyleft-gpl.md"
created: 2026-02-01
modified: 2026-02-01
commons_domain: startup
contributors:
  - name: "Commons OS"
    role: author
license: "CC-BY-SA-4.0"
attribution: "Commons OS Pattern Library"
repository: "https://github.com/Commons-OS/patterns"
---

### 1. Overview

Copyleft is a legal and philosophical framework that leverages copyright law to ensure that a work and its derivatives remain free and open. The core purpose of copyleft is to grant users a set of freedoms—to use, study, modify, and share the work—while ensuring that these same freedoms are passed on to others who receive derivative versions. This is achieved through a licensing mechanism that requires any modified or extended versions of the work to be distributed under the same or compatible terms. The problem that copyleft addresses in the startup and business context is the threat of proprietary enclosure, where open-source code or other works are taken, modified, and then made proprietary, thus restricting the freedoms of subsequent users. By preventing this, copyleft fosters a collaborative ecosystem where knowledge and innovation can be shared and built upon by a community.

The concept of copyleft was pioneered by Richard Stallman in the mid-1980s as a cornerstone of the free software movement. Stallman's motivation stemmed from a direct experience with the consequences of proprietary software. After a company refused to share its improvements to a Lisp interpreter he had written, Stallman became determined to create a legal framework that would prevent such "software hoarding." This led to the creation of the GNU General Public License (GPL), the first and most well-known copyleft license. The term "copyleft" itself is a playful reversal of "copyright," a concept attributed to Don Hopkins. Copyleft is deeply aligned with commons-aligned value creation as it establishes a legal and ethical foundation for a digital commons. It ensures that the collective creations of a community remain a shared resource, preventing any single entity from privatizing the commons and extracting rent from it. This viral nature of copyleft licenses helps to grow the commons, as each new derivative work adds to the pool of freely available knowledge and tools.

### 2. Core Principles

1.  **The Four Essential Freedoms:** At the heart of copyleft are the four essential freedoms defined by the Free Software Foundation. These are the freedom to run the program for any purpose (freedom 0); the freedom to study how the program works and adapt it to your needs (freedom 1); the freedom to redistribute copies so you can help your neighbor (freedom 2); and the freedom to improve the program and release your improvements to the public, so that the whole community benefits (freedom 3). Access to the source code is a precondition for freedoms 1 and 3.

2.  **Reciprocity and Share-Alike:** Copyleft licenses are reciprocal in nature. They require that if you create a derivative work of a copyleft-licensed work, you must distribute your derivative work under the same or a compatible copyleft license. This "share-alike" provision is the key mechanism that ensures the continued freedom of the work and its derivatives, creating a virtuous cycle of sharing and collaboration.

3.  **Prevention of Proprietary Lock-in:** A fundamental principle of copyleft is to prevent the appropriation of free and open-source work into proprietary products. By requiring derivative works to be licensed under the same terms, copyleft ensures that the freedoms granted by the original author cannot be stripped away by downstream users. This protects the community from having its work enclosed and turned into a private asset.

4.  **Source Code Availability:** For software, copyleft licenses mandate that the source code must be made available alongside any distributed binaries. This is a practical and essential requirement for exercising the freedoms to study and modify the software. Without the source code, users would be unable to understand how the software works or make meaningful changes to it.

5.  **No Revocation of Rights:** Once a work is released under a copyleft license, the freedoms granted cannot be revoked. This provides a stable and predictable legal foundation for users and developers, who can be confident that their rights to use, modify, and share the work will not be taken away in the future.

### 3. Key Practices

1.  **Choosing the Right License:** The first and most critical practice is selecting the appropriate copyleft license. The most common and strongest copyleft license is the GNU General Public License (GPL). For projects where you want to allow linking with non-GPL-compatible code, the GNU Lesser General Public License (LGPL) is a weaker but still effective copyleft license. The Affero General Public License (AGPL) is designed for web services and ensures that the source code is available to users of the service.

2.  **Clear Licensing and Copyright Notices:** Every source code file should include a clear copyright notice and a reference to the license under which it is distributed. This ensures that anyone who receives the code is aware of their rights and obligations. It is also good practice to include the full text of the license in a file named `LICENSE` or `COPYING` in the root of the project repository.

3.  **Maintaining a Contributor License Agreement (CLA):** For larger projects, it is common to require contributors to sign a Contributor License Agreement (CLA). A CLA clarifies the terms under which contributions are made and ensures that the project has the necessary rights to distribute the contributions under its chosen copyleft license. This can be particularly important for projects that may want to relicense the code in the future.

4.  **Tracking Dependencies and Their Licenses:** It is crucial to track the licenses of all dependencies that your project uses. If your project is licensed under a strong copyleft license like the GPL, you must ensure that all of your dependencies are compatible with the GPL. Using a dependency that is licensed under an incompatible license can create legal problems for your project.

5.  **Providing Source Code with Distributions:** When you distribute a binary or executable version of your copyleft-licensed software, you must also provide a way for users to obtain the corresponding source code. This can be done by including the source code with the binary distribution, or by providing a written offer to provide the source code on request.

6.  **Educating the Community:** A key practice for any copyleft project is to educate the community about the license and its implications. This includes explaining the rationale behind the choice of a copyleft license and providing clear guidance on how to comply with its terms. A well-informed community is more likely to respect the license and contribute to the project in a way that is consistent with its goals.

7.  **Enforcing the License:** While most people will respect the terms of a copyleft license, there may be instances where the license is violated. It is important to have a strategy for enforcing the license in such cases. This may involve contacting the violator and explaining the issue, or in more serious cases, taking legal action. The Free Software Foundation and other organizations can provide assistance with license enforcement.

### 4. Implementation

Implementing a copyleft strategy for a startup or business requires careful planning and execution. The first step is to choose the right copyleft license for your project. The GNU General Public License (GPL) is the most common and strongest copyleft license, and it is a good choice for projects where you want to ensure that all derivative works are also free and open-source. If you are developing a library that you want to be used by a wide range of applications, including proprietary ones, the GNU Lesser General Public License (LGPL) may be a better choice. Once you have chosen a license, you need to apply it to your code. This involves adding a copyright notice and a license header to each source file, and including the full text of the license in your project's repository. It is also important to track the licenses of all of your project's dependencies to ensure that they are compatible with your chosen license.

When distributing your copyleft-licensed software, you must make the source code available to users. This can be done by bundling the source code with the binary distribution, or by providing a written offer to provide the source code on request. For web-based services, the Affero General Public License (AGPL) requires that you make the source code available to users who interact with the service over a network. A key consideration for businesses is how to build a sustainable business model around copyleft-licensed software. One common approach is to offer paid support, consulting, or hosting services for the software. Another approach is to dual-license the software, offering it under a copyleft license for free, and under a commercial license for a fee to those who do not want to be bound by the copyleft terms.

Real-world examples of successful businesses built around copyleft-licensed software abound. Red Hat is a multi-billion dollar company that provides enterprise-grade Linux distributions and support services, all based on the GPL-licensed Linux kernel. WordPress, the world's most popular content management system, is also licensed under the GPL. The success of these companies demonstrates that it is possible to build a thriving business while still respecting the principles of free and open-source software. By carefully choosing a license, managing dependencies, and developing a sustainable business model, startups and businesses can leverage the power of copyleft to build innovative products and services while contributing to the digital commons.

### 5. 7 Pillars Assessment

| Pillar | Score (1-5) | Rationale |
|---|---|---|
| Purpose | 5 | The primary purpose of copyleft is to create a self-perpetuating commons of free and open knowledge, which is highly aligned with the goals of a commons-based economy. |
| Governance | 4 | Copyleft licenses provide a clear and legally robust governance framework for the software commons. However, the governance of the licenses themselves is centralized in organizations like the Free Software Foundation. |
| Culture | 5 | Copyleft has been instrumental in fostering a culture of collaboration, sharing, and reciprocity within the free and open-source software community. |
| Incentives | 4 | Copyleft provides strong incentives for contributing to the commons, as contributors know that their work will not be privatized. However, it can be challenging to build a business model around copyleft-licensed software. |
| Knowledge | 5 | Copyleft is all about the open and free sharing of knowledge, in the form of source code. It ensures that knowledge is not locked up in proprietary silos. |
| Technology | 5 | Copyleft is a technological innovation in the field of law and licensing. It uses the existing copyright system to create a new set of rules that are better suited to the digital age. |
| Resilience | 5 | The viral nature of copyleft licenses makes the commons more resilient. As more people use and contribute to copyleft-licensed projects, the commons grows and becomes more robust. |
| **Overall** | **4.9** | **Copyleft is a powerful tool for building and protecting the digital commons. It is highly aligned with the principles of a commons-based economy, and it has been instrumental in the success of the free and open-source software movement.** |

### 6. When to Use

*   **When you want to build a community around your project:** Copyleft licenses can help to foster a sense of community and shared ownership around a project. By ensuring that all contributions remain free and open, copyleft encourages people to contribute their time and skills to the project.
*   **When you want to prevent your work from being incorporated into proprietary products:** If you want to ensure that your work is not used to create closed-source products, a strong copyleft license like the GPL is the best choice.
*   **When you are building a platform or ecosystem:** Copyleft can be a powerful tool for building a platform or ecosystem. By requiring derivative works to be licensed under the same terms, copyleft can help to create a level playing field for all participants in the ecosystem.
*   **When you want to maximize the freedom of users:** The four essential freedoms at the heart of copyleft are designed to maximize the freedom of users. If your primary goal is to empower users, a copyleft license is a good choice.
*   **When you are building a business based on services or support:** Copyleft-licensed software can be a great foundation for a business that provides services or support. By giving the software away for free, you can build a large user base and then monetize your expertise by offering paid support, consulting, or hosting services.
*   **When you want to contribute to the digital commons:** By licensing your work under a copyleft license, you are making a contribution to the digital commons. You are sharing your work with the world in a way that ensures that it will always be free and open.

### 7. Anti-Patterns and Gotchas

*   **License Incompatibility:** One of the biggest gotchas with copyleft licenses is incompatibility. If you are not careful, you can end up in a situation where you cannot combine two pieces of code because their licenses are incompatible. For example, you cannot link a GPL-licensed library with a library that is licensed under a license that is not compatible with the GPL.
*   **Not Understanding the "Viral" Nature of Strong Copyleft:** A common mistake is to use a strong copyleft license like the GPL without fully understanding its implications. If you link your code to a GPL-licensed library, your code must also be licensed under the GPL. This can be a problem if you intended to release your code under a more permissive license or a proprietary license.
*   **Failing to Provide Source Code:** A clear violation of any copyleft license is to distribute a binary without also providing the source code. This is a common mistake made by companies that are new to open-source software. It is important to have a process in place to ensure that you are always in compliance with the source code availability requirements of the license.
*   **Using a Copyleft License for the Wrong Reasons:** Copyleft is a powerful tool, but it is not the right choice for every project. If your primary goal is to achieve the widest possible adoption of your code, a more permissive license like the MIT or Apache license may be a better choice. Using a copyleft license when a permissive license would be more appropriate can alienate potential users and contributors.
*   **Ignoring Community Norms:** Every open-source community has its own norms and expectations. When you are using a copyleft-licensed project, it is important to be aware of these norms and to act in a way that is respectful of the community. For example, some communities may have a strong preference for certain types of contributions, or they may have a particular way of handling license compliance issues.
*   **Dual-Licensing without a Clear Value Proposition:** While dual-licensing can be a viable business model, it can also be a source of confusion and frustration for the community. If you are going to dual-license your software, it is important to have a clear value proposition for the commercial license. Why would someone pay for a commercial license when they can get the software for free under a copyleft license?

### 8. References

1.  [What is Copyleft? - GNU Project - Free Software Foundation](https://www.gnu.org/licenses/copyleft.en.html)
2.  [Copyleft - Wikipedia](https://en.wikipedia.org/wiki/Copyleft)
3.  [All About Copyleft Licenses | FOSSA Blog](https://fossa.com/blog/all-about-copyleft-licenses/)
4.  [The Free Software Definition - GNU Project - Free Software Foundation](https://www.gnu.org/philosophy/free-sw.en.html)
5.  [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
