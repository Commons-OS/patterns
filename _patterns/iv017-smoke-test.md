---
id: pat_91a6f5d00abf4297870fe137d5
page_url: https://commons-os.github.io/patterns/iv017-smoke-test/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/iv017-smoke-test.md
slug: iv017-smoke-test
title: "Smoke Test"
aliases: ["Fake Door Test", "Pre-order Validation"]
version: "1.0"
created: 2026-02-02T07:53:55Z
modified: 2026-02-02T07:53:55Z
classification:
  universality: domain
  domain: startup
  category: [validation]
  era: [digital]
  origin: ["Lean Startup"]
  status: published
  commons_alignment: 4
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

# IV017 - Smoke Test

## Overview

A smoke test is a validation technique used to gauge customer interest in a product or feature before it is fully developed. The core idea is to create a preliminary, often lightweight, representation of the product—such as a landing page, an advertisement, or a pre-order form—and measure how potential customers interact with it. This approach allows teams to gather real-world data on purchase intent and market demand with minimal investment of time and resources. The term "smoke test" is borrowed from the hardware and software industries, where it originally referred to a preliminary check to see if a new piece of equipment or code would "smoke" when turned on, indicating a fundamental problem. In the context of startups and product development, it serves a similar purpose: to quickly identify if a business idea has fundamental viability before committing to a full-scale build.

The primary goal of a smoke test is to move beyond speculation and gather empirical evidence of customer interest. Instead of relying on surveys or focus groups, which can be prone to hypothetical bias, a smoke test confronts potential customers with a call to action that mimics a real-world transaction, such as clicking a "buy now" button or signing up for a "coming soon" notification. The data collected from these interactions—conversion rates, click-through rates, and pre-order numbers—provide a much stronger signal of market demand. This allows entrepreneurs and product managers to make more informed decisions, pivot their ideas based on real feedback, and avoid the significant risk of building something nobody wants.

## Core Principles

1.  **Test Before You Build:** The foundational principle of a smoke test is to validate an idea with real users before investing significant resources in development. This "test-first" approach minimizes waste and reduces the risk of market failure.
2.  **Measure Actions, Not Opinions:** Smoke tests prioritize behavioral data over attitudinal data. Instead of asking people if they would use a product, it measures what they actually do when presented with the opportunity to acquire it.
3.  **Fake It ‘Til You Make It:** The technique often involves creating the *illusion* of a functional product. This might be a landing page for a product that doesn’t exist yet or a button for a feature that hasn’t been built. The goal is to simulate the user experience of the final product as closely as possible to elicit a genuine response.
4.  **Low-Fidelity and High-Speed:** A smoke test should be quick and cheap to implement. The emphasis is on learning and iteration, not on creating a polished or perfect artifact. The faster a team can get a smoke test in front of users, the faster they can learn and adapt.


## Key Practices

1.  **Landing Page MVP:** Create a single-page website that describes the product, its value proposition, and includes a call-to-action (CTA) for users to sign up, pre-order, or learn more. This is one of the most common forms of a smoke test.
2.  **Pre-order/Crowdfunding Campaign:** Launch a campaign on a platform like Kickstarter or Indiegogo, or even on your own site, to see if people are willing to pay for the product before it’s built. This is a strong form of validation as it involves a financial commitment from the customer.
3.  **A/B Testing:** Create multiple versions of your smoke test (e.g., different landing pages with different value propositions or pricing) to see which one performs better. This can help you refine your messaging and positioning.
4.  **Ad Campaign to a Fake Store:** Drive traffic from social media or search engine ads to a simple e-commerce page. The "buy" button might lead to a "coming soon" page or a simple form to collect email addresses. The conversion rate of the ad and the click-through rate on the "buy" button are key metrics.
5.  **The "404" Test:** Add a new link or button to your existing website that points to a new feature. When a user clicks on it, they are taken to a "feature coming soon" page or a simple 404 page. The number of clicks on the link is a measure of interest in the new feature.

## Implementation

Implementing a smoke test involves a series of steps, from defining the hypothesis to analyzing the results. Here’s a detailed guide:

**1. Define Your Hypothesis and Success Metrics:**

*   **Hypothesis:** Clearly state what you are trying to prove. For example: "We believe that there is enough demand for a subscription box for pet owners to justify building the service."
*   **Success Metrics:** Define what success looks like. This could be a certain number of email sign-ups, a specific conversion rate on a pre-order page, or a target return on ad spend (ROAS). For example: "If we can get 500 email sign-ups in two weeks with a marketing budget of $500, we will proceed with building the product."

**2. Choose Your Smoke Test Method:**

Select the most appropriate smoke test method based on your product, target audience, and resources. A simple landing page is a good starting point for many digital products, while a pre-order campaign might be more suitable for a physical product.

**3. Build the Smoke Test Artifact:**

*   **Landing Page:** Use a simple website builder like Wix, Squarespace, or Instapage to create a professional-looking landing page. Include a clear value proposition, compelling visuals, and a prominent call-to-action.
*   **Ad Campaign:** Create targeted ads on platforms like Facebook, Instagram, or Google Ads. Your ad copy and visuals should be aligned with your landing page.
*   **Pre-order Page:** Set up a simple e-commerce page with a payment processor. Be transparent with customers that they are pre-ordering a product that is not yet available.

**4. Drive Traffic to Your Test:**

Use paid advertising, social media, email marketing, or content marketing to drive traffic to your smoke test. The goal is to get your test in front of a representative sample of your target audience.

**5. Measure and Analyze the Results:**

Use analytics tools like Google Analytics, VWO, or Hotjar to track your key metrics. Analyze the data to see if you have met your success criteria. Look for patterns in the data that can provide insights into your target audience and their needs.

**6. Make a Decision:**

Based on the results of your smoke test, you have three options:

*   **Green Light:** If you have met your success criteria, you can proceed with building the product with confidence.
*   **Yellow Light:** If the results are inconclusive, you may need to iterate on your idea and run another smoke test.
*   **Red Light:** If the results are poor, it’s a sign that your idea may not be viable. It’s better to pivot or abandon the idea at this stage than to invest more resources in a failing project.

## 7 Pillars Assessment

*   **Purpose:** {"score": 4, "rationale": "Smoke tests are highly aligned with the purpose pillar as they are a direct and effective method for validating that a product or service is solving a real-world problem that users are willing to pay for. By focusing on evidence of demand before building, it ensures that resources are directed towards creating genuine value."}
*   **Governance:** {"score": 3, "rationale": "While smoke tests themselves are a tool for validation and not a governance structure, they can contribute to a more decentralized and evidence-based decision-making process. By providing clear data on user interest, they empower teams to make decisions based on market feedback rather than hierarchical authority."}
*   **Culture:** {"score": 4, "rationale": "The use of smoke tests fosters a culture of experimentation, learning, and customer-centricity. It encourages teams to be lean, agile, and data-informed, and to embrace failure as a learning opportunity. This is a significant departure from traditional, risk-averse corporate cultures."}
*   **Incentives:** {"score": 3, "rationale": "Smoke tests can help align incentives by focusing the team on a common goal: achieving product-market fit. However, the incentives themselves are not inherent in the smoke test but rather in how the organization rewards the outcomes of the test. If the organization rewards learning and validated hypotheses, then the incentives are aligned."}
*   **Knowledge:** {"score": 4, "rationale": "Smoke tests are a powerful tool for generating knowledge about the market, customers, and the problem space. The data and insights generated from a smoke test are invaluable for informing product development, marketing, and business strategy. This knowledge is often tacit and difficult to acquire through other means."}
*   **Technology:** {"score": 3, "rationale": "The technology required to run a smoke test is typically simple and readily available (e.g., landing page builders, ad platforms). The focus is on using technology as a means to an end (i.e., learning) rather than on building complex or sophisticated technology for its own sake."}
*   **Resilience:** {"score": 4, "rationale": "By testing ideas early and cheaply, smoke tests increase the resilience of a startup or organization. They allow for rapid iteration and adaptation, and they reduce the risk of catastrophic failure by killing bad ideas before they consume significant resources."}

## When to Use

*   **Early-stage startups:** To validate a new business idea before building a product.
*   **New product or feature launches:** To gauge interest in a new offering before committing to a full-scale launch.
*   **Pivoting:** To test a new direction for an existing business.
*   **Prioritizing features:** To determine which features to build next based on user demand.
*   **Securing buy-in:** To convince stakeholders to invest in a new idea by providing evidence of market demand.

## Anti-Patterns

*   **Deceiving users:** While smoke tests involve a degree of "faking it," it’s important to be transparent with users as much as possible. For example, if you are collecting pre-orders, be clear that the product is not yet available.
*   **Not defining success metrics:** Without clear success metrics, it’s impossible to know if your smoke test was successful or not.
*   **Giving up too early:** A single failed smoke test doesn’t necessarily mean your idea is bad. It could be that your messaging was off, your target audience was wrong, or your test was poorly designed. Iterate and test again.
*   **Analysis paralysis:** Don’t get bogged down in the data. The goal of a smoke test is to make a quick go/no-go decision, not to write a PhD thesis.
*   **Ignoring qualitative feedback:** While quantitative data is important, don’t ignore the qualitative feedback you receive from users. This can provide valuable insights that you can’t get from the numbers alone.

## References

[1] [https://thegood.com/insights/smoke-testing/](https://thegood.com/insights/smoke-testing/)
[2] [https://www.bundl.com/articles/techniques-validating-purchase-intention-in-4-easy-steps-the-smoke-test](https://www.bundl.com/articles/techniques-validating-purchase-intention-in-4-easy-steps-the-smoke-test)
