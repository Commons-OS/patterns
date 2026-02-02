---
id: pat_26e419c9b5c94622a48b5a3fe0
page_url: https://commons-os.github.io/patterns/solution-interviews/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/solution-interviews.md
slug: solution-interviews
title: "Solution Interviews"
aliases: ["The Mom Test for Solutions"]
version: "1.0"
created: 2026-02-02T07:53:55Z
modified: 2026-02-02T07:53:55Z
classification:
  universality: domain
  domain: startup
  category: [validation]
  era: [digital]
  origin: ["Rob Fitzpatrick"]
  status: published
  commons_alignment: 4.2
  commons_domain: [startup, business]
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [manus-ai, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

# Solution Interviews

## Overview

Solution Interviews are a customer research technique used to validate a proposed solution with potential customers. This pattern is a critical step in the lean startup methodology, occurring after a specific customer problem has been identified and validated. The primary goal of a Solution Interview is not to sell a product, but to learn whether a proposed solution resonates with the target audience and is something they would genuinely use and, potentially, pay for. It is a direct response to the risk of building a product that nobody wants, a common reason for startup failure. By engaging with customers early in the development process, entrepreneurs can gather crucial feedback, iterate on their ideas, and increase the likelihood of achieving product-market fit.

The principles behind effective Solution Interviews are heavily influenced by Rob Fitzpatrick's book, "The Mom Test" [1]. The book's central thesis is that founders should avoid asking biased questions that lead to misleading compliments and instead focus on the customer's life and their past behaviors. A well-executed Solution Interview feels more like a collaborative consultation than a sales pitch. It's about presenting a solution concept—often in the form of a prototype, mockup, or even a simple presentation—and then carefully observing the customer's reaction and asking insightful, open-ended questions to gauge their true interest and willingness to commit.

It is crucial to distinguish Solution Interviews from Problem Interviews. A Problem Interview focuses on understanding a customer's pains, needs, and current workflows *before* a solution is designed. Its purpose is to uncover and validate a problem worth solving. A Solution Interview, on the other hand, takes place once a potential solution has been conceived. It tests the hypothesis that this specific solution is the right one for the validated problem. Skipping the problem validation step and jumping straight to solution interviews is a common anti-pattern that often leads to solving non-existent problems.

## Core Principles

1.  **Focus on Past Behavior, Not Future Promises:** People are notoriously bad at predicting their own future behavior. A question like "Would you use this?" is likely to elicit a polite "yes," which is ultimately a vanity metric. Instead, focus on concrete examples from their past. Ask about how they currently solve the problem, what they've tried before, and what they've paid for. Past behavior is a much stronger indicator of future actions.

2.  **Show, Don't Just Tell:** Abstract ideas are hard to grasp and evaluate. A Solution Interview is most effective when you can present a tangible representation of your proposed solution. This doesn't need to be a fully functional product; a low-fidelity prototype, a series of mockups, a wireframe, or even a slide deck can be enough to make the solution concrete and elicit more specific, actionable feedback.

3.  **Listen More, Talk Less:** Your primary goal is to learn, not to pitch. After a brief introduction to the solution, the focus should shift to the customer. Let them react, ask questions, and express their thoughts freely. Avoid the temptation to defend your idea or over-explain its features. The most valuable insights often come from a customer's unprompted reactions and questions.

4.  **Seek Commitment, Not Compliments:** Compliments are worthless; commitment is the currency of validation. A genuine commitment is a signal that the customer sees real value in your solution. This commitment can take various forms, such as a pre-order, a letter of intent, a deposit, a time commitment for a pilot program, or even a reputational commitment like an introduction to other potential customers. The "ask" for commitment is a crucial part of the interview.

## Key Practices

1.  **Frame it as a Consultation:** Position the interview as a request for advice or expertise. People are often more open and honest when they feel they are helping you rather than being sold to. Phrases like, "I'm working on a new concept and I'd love to get your expert opinion on it," can set the right tone.

2.  **Ask Open-Ended "How," "What," and "Why" Questions:** Avoid yes/no questions. Instead, use open-ended questions that encourage detailed responses. For example, instead of "Do you like this feature?", ask "How would this feature fit into your current workflow?" or "What are your initial thoughts on this?"

3.  **Drill Down on Specifics:** When a customer makes a general statement, dig deeper to understand the underlying reasons. If they say, "This is interesting," follow up with, "What about it do you find interesting?" or "Can you give me an example of how you might use this?"

4.  **Observe Body Language and Emotional Reactions:** Non-verbal cues can be just as revealing as verbal feedback. Pay attention to their level of engagement, their facial expressions, and their overall demeanor. Does their face light up when they see the solution, or do they seem indifferent? These reactions can provide valuable clues about their true feelings.

## Implementation

Implementing Solution Interviews effectively requires a structured approach, from preparation to analysis.

1.  **Prerequisites:** Before conducting Solution Interviews, you must have two things: a **validated customer problem** and a **defined target audience**. You should have strong evidence from Problem Interviews or other research that you are addressing a real and significant pain point for a specific group of people.

2.  **Preparation:**
    *   **Create a Solution Artifact:** Develop a low-fidelity prototype, mockups, a presentation, or any other artifact that clearly communicates your proposed solution. The goal is to make the solution tangible enough for customers to react to.
    *   **Develop an Interview Script:** While you shouldn't follow a rigid script, it's helpful to have a list of key questions you want to ask. These questions should be open-ended and designed to test your core assumptions about the solution.
    *   **Define Your "Commitment Ask":** Decide what form of commitment you will ask for at the end of the interview if the feedback is positive. This could be a pre-order, a pilot program, an introduction, or another tangible sign of interest.

3.  **Execution:**
    *   **Introduction:** Start by setting the context. Remind them of the problem you discussed previously (if applicable) and explain that you are exploring a potential solution and would value their feedback.
    *   **Present the Solution:** Briefly present your solution artifact. Avoid a lengthy sales pitch; just provide enough information for them to understand the concept.
    *   **Listen and Observe:** This is the core of the interview. Let the customer react. Ask your open-ended questions and listen carefully to their responses. Pay attention to their non-verbal cues.
    *   **The Commitment Ask:** Towards the end of the interview, if the customer seems genuinely enthusiastic, make your "ask." Their response to this question is the ultimate test of validation.

4.  **Analysis:**
    *   **Synthesize Your Notes:** Immediately after each interview, review and synthesize your notes. Look for key quotes, insights, and patterns.
    *   **Identify Patterns:** After conducting several interviews, look for recurring themes and patterns in the feedback. Are customers consistently excited about a particular feature? Are they all confused by the same part of the user interface?
    *   **Make a "Go/No-Go" Decision:** Based on the patterns you've identified, decide whether to move forward with the solution, iterate on it based on the feedback, or pivot to a different solution altogether.

## 7 Pillars Assessment

*   **Purpose (Score: 5):** This pattern is deeply aligned with the purpose of building things that create value. By systematically de-risking ideas and focusing on solving real user problems, it ensures that time and resources are spent on creating products and services that are genuinely needed and wanted, which is the foundation of a healthy commons.
*   **Governance (Score: 3):** While the pattern itself does not prescribe a specific governance model, it inherently promotes a user-centric approach. By giving customers a voice in the development process, it lays the groundwork for more participatory and community-oriented governance structures. However, the ultimate decision-making power still rests with the entrepreneur or development team.
*   **Culture (Score: 4):** Solution Interviews foster a culture of humility, learning, and collaboration. It encourages founders to step out of their own echo chamber and engage directly with the people they aim to serve. This practice builds empathy and a deep understanding of user needs, which are essential cultural traits for any successful commons-based project.
*   **Incentives (Score: 3):** The primary incentive is for the creator: to gain validated learning and avoid wasting resources. For the customer, the incentive is the opportunity to influence the development of a product that could solve a significant problem for them. While not a direct economic incentive, this can be a powerful motivator for users who are passionate about the problem space.
*   **Knowledge (Score: 5):** The entire purpose of a Solution Interview is to generate knowledge and validate or invalidate hypotheses. It is a structured process for creating actionable insights from qualitative data. The knowledge gained is invaluable for making informed product decisions and is a core component of the "measure, learn, build" feedback loop.
*   **Technology (Score: 3):** The pattern is technology-agnostic and can be applied to the development of any product or service, whether it's a high-tech software application or a low-tech community service. The focus is on the human interaction and learning process, not the technology itself.
*   **Resilience (Score: 4):** By ensuring that solutions are validated before they are built, this pattern significantly increases the resilience of a project. It reduces the risk of market failure and helps to create a more sustainable and adaptable product or service that is closely aligned with user needs. This proactive approach to risk mitigation is a key factor in long-term resilience.

## When to Use

*   After you have strong evidence of a validated customer problem and a clearly defined target audience.
*   Before you invest significant time, money, and effort into building a high-fidelity product or a full-scale service.
*   When you have a specific solution hypothesis that you want to test with real users.
*   When you are deciding between multiple potential solutions and want to determine which one resonates most with your target market.

## Anti-Patterns

*   **Pitching Instead of Listening:** The interview turns into a sales pitch, with the founder dominating the conversation and trying to convince the customer of the solution's brilliance.
*   **Asking for Opinions, Not Facts:** Relying on hypothetical questions ("Would you use this?") and compliments ("That's a great idea!") as evidence of validation.
*   **Interviewing the Wrong People:** Talking to friends, family, or people who are not in your target customer segment, which leads to irrelevant and misleading feedback.
*   **Not Showing a Solution:** Trying to describe a solution in the abstract, which makes it difficult for customers to provide concrete feedback.
*   **Failing to Ask for Commitment:** Being afraid to ask for a tangible sign of commitment, which is the strongest form of validation.

## References

[1] Fitzpatrick, R. (2013). *The Mom Test: How to talk to customers & learn if your business is a good idea when everyone is lying to you*. CreateSpace Independent Publishing Platform.
[2] Durmonski, I. (2019). *The Mom Test by Rob Fitzpatrick [Actionable Summary]*. Durmonski.com. Retrieved from https://durmonski.com/book-summaries/the-mom-test/
[3] Pan, T. (2025). *The Mom Test: How to Conduct Effective User Research?*. TianPan.co. Retrieved from https://tianpan.co/blog/2025-04-29-the-mom-test
[4] Ranjan, R. (2024). *Problem Validation vs. Solution Validation vs. Product Validation - Understand the Difference*. ProductGrowth.blog. Retrieved from https://www.productgrowth.blog/p/problem-validation-vs-solution-validation
