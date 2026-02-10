
---
id: pat_8aaae1817c9062fd8cb0fa78
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/dark-patterns-in-platform-ux.md
slug: dark-patterns-in-platform-ux
title: Dark Patterns in Platform UX
aliases:
- Deceptive Design
- Manipulative UX
- Hostile Architecture
version: "1.0"
created: "2026-02-10 00:00:00+00:00"
modified: "2026-02-10 00:00:00+00:00"
classification:
  universality: context-dependent
  domain: platform
  category:
  - anti-pattern
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - behavioral-psychology
  - user-experience-design
  status: draft
  commons_alignment: 1
  commons_domain:
  - platform
  - social
  - business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related:
- privacy-by-design
- ethical-design
contributors:
- higgerix
- cloudsters
sources:
- https://www.nngroup.com/articles/deceptive-patterns/
- https://en.wikipedia.org/wiki/Dark_pattern
- https://www.deceptive.design/
- https://dl.acm.org/doi/10.1145/3411764.3445610
- https://www.ftc.gov/news-events/reports/bringing-dark-patterns-light
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

### 1. Overview

Dark Patterns in Platform UX are user interface design choices that manipulate users into taking actions they would not otherwise have taken, often benefiting the platform at the user's expense. These are not mistakes or poor design, but rather carefully crafted and intentional manipulations that exploit cognitive biases and human psychology. The term was coined by UX designer Harry Brignull in 2010 to name and shame these deceptive practices, which have since become a significant concern in the digital world. Dark patterns are a direct contradiction to the principles of user-centered design, which prioritizes user needs and goals. Instead, they prioritize business objectives, such as increasing sales, generating leads, or obtaining user data, often through unethical means. The prevalence of dark patterns has grown with the rise of the attention economy and the increasing competition for user engagement and revenue. This has led to a digital environment where users must be constantly on their guard against manipulation, and where trust in online platforms is eroding.

The significance of dark patterns lies in their potential to cause harm to users, ranging from financial losses and privacy violations to a general erosion of trust in digital platforms. They can trick users into making unintended purchases, signing up for recurring subscriptions without their explicit consent, or sharing more personal data than they are comfortable with. These deceptive practices can be particularly harmful to vulnerable users, such as the elderly, children, or those with low digital literacy. The widespread use of dark patterns has led to a growing backlash from users, regulators, and consumer advocacy groups, who are calling for greater transparency and accountability from tech companies. The study of dark patterns has become a critical area of research in human-computer interaction (HCI), law, and ethics, as academics and practitioners work to understand their impact and develop countermeasures. The fight against dark patterns is not just about protecting consumers, but also about preserving the integrity of the digital commons and ensuring that technology is used to empower, rather than exploit, individuals.

The historical context of dark patterns can be traced back to the early days of e-commerce, where deceptive practices were used to boost sales and gain a competitive edge. However, the rise of social media, mobile apps, and other digital platforms has created new opportunities for the use of dark patterns. The ability to collect and analyze vast amounts of user data has enabled platforms to personalize their deceptive tactics and target individual users with unprecedented precision. The A/B testing and other optimization techniques used to improve user experience can also be used to refine and perfect dark patterns, making them even more effective at manipulating user behavior. As a result, dark patterns have become a pervasive feature of the digital landscape, and their impact is likely to grow as technology becomes more integrated into our daily lives. The history of dark patterns is a cautionary tale about the potential for technology to be used for unethical purposes, and a reminder of the importance of ethical design and regulation.

### 2. Core Principles

1.  **Deception by Design:** The core of any dark pattern is the intentional deception of the user. This is not an accident or a design flaw, but a calculated decision to mislead or trick the user into taking an action that benefits the platform. This can be achieved through a variety of techniques, such as using misleading labels, hiding important information, or creating a false sense of urgency. The deception is often subtle, and may not be immediately apparent to the user. This is what makes dark patterns so insidious, and so effective.

2.  **Exploitation of Cognitive Biases:** Dark patterns are effective because they exploit known cognitive biases and heuristics that influence human decision-making. For example, they may use the scarcity bias to create a false sense of urgency, the social proof bias to create a false sense of popularity, or the default bias to trick users into accepting a particular option. By understanding and exploiting these biases, platforms can manipulate users into making decisions that they would not otherwise make. This is a form of psychological warfare, and it is being waged against users on a massive scale.

3.  **Asymmetry of Information:** Dark patterns thrive in situations where there is an asymmetry of information between the platform and the user. The platform has a deep understanding of user behavior and can use this knowledge to design manipulative interfaces, while the user is often unaware of the deceptive tactics being used against them. This information asymmetry gives the platform a significant advantage, and it is one of the key reasons why dark patterns are so difficult to combat.

4.  **Prioritization of Business Goals over User Needs:** Dark patterns are a clear indication that a platform is prioritizing its own business goals over the needs and interests of its users. This is a fundamental departure from the principles of user-centered design, which emphasizes empathy for the user and a commitment to creating a positive user experience. When a platform uses dark patterns, it is sending a clear message that it does not respect its users, and that it is willing to exploit them for its own gain.

5.  **Erosion of Trust:** The use of dark patterns can have a corrosive effect on user trust. When users realize that they have been deceived or manipulated, they are likely to lose trust in the platform and may be less willing to engage with it in the future. This can have long-term consequences for the platform's reputation and brand image. In the long run, the use of dark patterns is a losing strategy, as it will ultimately drive users away.

6.  **Obstruction and Friction:** Many dark patterns work by creating obstruction and friction for users who want to take actions that are not in the platform's interest. For example, it may be easy to sign up for a service but difficult to cancel it, or it may be easy to share personal data but difficult to delete it. This is a form of user-hostile design, and it is a clear indication that the platform is not on the user's side.

7.  **Lack of Transparency and Control:** Dark patterns often involve a lack of transparency and control for the user. Important information may be hidden or obscured, and users may not be given clear choices or the ability to easily change their settings. This can leave users feeling powerless and frustrated. The lack of transparency and control is a key feature of dark patterns, and it is one of the reasons why they are so harmful.

### 3. Key Practices

1.  **Bait and Switch:** This practice involves advertising a free or low-cost product or service that is not actually available or is only available in limited quantities. When the user tries to access the advertised product, they are presented with a more expensive or lower-quality alternative. A well-known example is the "free" tax filing software that is advertised by companies like Intuit, which is often not actually free for most users. This is a classic example of a dark pattern, and it is one of the most common.

2.  **Confirmshaming:** This practice uses guilt or shame to pressure users into taking a particular action. For example, a website might use a pop-up to ask for the user's email address, and the option to decline might be worded in a way that makes the user feel bad, such as "No thanks, I don't like saving money." This is a form of emotional manipulation, and it is a particularly insidious type of dark pattern.

3.  **Disguised Ads:** This practice involves designing advertisements to look like regular content, such as news articles or user-generated posts. This can trick users into clicking on the ads, which can generate revenue for the platform. This is a common practice on social media platforms and news websites, and it is a major source of revenue for many of these companies.

4.  **Forced Continuity:** This practice involves automatically renewing a subscription or service without the user's explicit consent. This can be achieved by making it difficult to cancel the service or by not providing clear information about the renewal terms. This is a common practice for streaming services and other subscription-based businesses, and it is a major source of frustration for many users.

5.  **Friend Spam:** This practice involves asking for the user's email or social media permissions under the pretense of a different purpose, and then using those permissions to send spam to the user's contacts. This is a common practice for social media platforms and mobile games, and it is a major violation of user privacy.

6.  **Hidden Costs:** This practice involves adding unexpected fees or charges to the user's bill at the end of the checkout process. This can be achieved by not displaying the full price of the product or service upfront, or by using pre-selected options that add extra costs. This is a common practice for airlines and other travel companies, and it is a major source of frustration for many users.

7.  **Roach Motel:** This practice makes it easy for the user to get into a situation but difficult for them to get out of it. For example, it may be easy to sign up for a service but difficult to cancel it. This is a common practice for subscription-based services and social media platforms, and it is a major source of frustration for many users.

### 4. Application Context

**Best Used For:**

*   Maximizing short-term profits at the expense of user trust.
*   Increasing user engagement and retention through manipulative means.
*   Acquiring user data without their full knowledge or consent.
*   Driving users towards specific actions that benefit the platform.

**Not Suitable For:**

*   Building long-term relationships with users based on trust and transparency.
*   Creating a positive and ethical user experience.
*   Complying with data protection regulations such as the GDPR.

**Scale:**

Dark patterns can be implemented at any scale, from a single button on a website to a complex system of manipulative interfaces across an entire platform. They can be used by small businesses and large corporations alike, and their impact can range from minor annoyances to significant financial and privacy harms. The scalability of dark patterns is one of the reasons why they are so pervasive and difficult to regulate. The ease with which dark patterns can be deployed and tested has led to their widespread adoption, and has created a digital environment where users are constantly at risk of being manipulated.

**Domains:**

Dark patterns can be found in a wide range of industry domains, including:

*   E-commerce
*   Social media
*   Mobile apps
*   Financial services
*   Travel
*   News and media

### 5. Implementation

Implementing dark patterns is a process that involves a deep understanding of user psychology and a willingness to prioritize business goals over user needs. The first step is to identify the desired user behavior that will benefit the platform, such as making a purchase, signing up for a subscription, or sharing personal data. Once the desired behavior has been identified, the next step is to design a user interface that will manipulate the user into taking that action. This can be achieved through a variety of techniques, such as using misleading labels, hiding important information, or creating a false sense of urgency. The design process is often data-driven, with platforms using A/B testing and other methods to determine which dark patterns are most effective.

The design of a dark pattern is often an iterative process that involves A/B testing and other optimization techniques to refine and perfect the manipulative interface. The goal is to create a design that is as effective as possible at tricking the user into taking the desired action, while also being subtle enough to avoid detection. This can be a difficult balance to strike, as a design that is too obviously manipulative may be counterproductive and may lead to a backlash from users. The use of A/B testing to optimize dark patterns is a particularly insidious practice, as it allows platforms to fine-tune their manipulative techniques and to maximize their effectiveness.

The implementation of dark patterns is often a collaborative effort that involves designers, developers, and product managers. The designer is responsible for creating the manipulative interface, the developer is responsible for implementing it, and the product manager is responsible for setting the business goals and measuring the results. This collaborative approach can make it difficult to assign responsibility for the use of dark patterns, as each individual may feel that they are just doing their job. The normalization of dark patterns within the tech industry is a major problem, and it is one of the reasons why they are so pervasive.

The use of dark patterns is often justified by the argument that they are necessary to achieve business goals and to compete in the marketplace. However, this argument ignores the ethical implications of manipulating users and the long-term damage that can be done to user trust. In the long run, the use of dark patterns is likely to be counterproductive, as it can lead to a loss of users and a damaged reputation. The short-term gains that can be achieved through the use of dark patterns are not worth the long-term costs.

### 6. Evidence & Impact

The impact of dark patterns on users can be significant, ranging from minor annoyances to serious financial and privacy harms. For example, a user who is tricked into signing up for a recurring subscription may end up paying for a service that they do not want or need. A user who is tricked into sharing their personal data may be at risk of identity theft or other forms of fraud. The impact of dark patterns can be particularly severe for vulnerable users, such as the elderly, children, or those with low digital literacy. The cumulative effect of dark patterns can be a significant drain on users' time, money, and mental energy.

There is a growing body of evidence that demonstrates the prevalence and impact of dark patterns. For example, a study by researchers at Princeton and the University of Chicago found that dark patterns are widespread on e-commerce websites, and that they can have a significant impact on user behavior. The study found that dark patterns can increase sales by as much as 10%, and that they can be particularly effective at tricking users into making unintended purchases. Another study by the Norwegian Consumer Council found that many popular apps use dark patterns to trick users into sharing their personal data. These studies provide empirical evidence of the harm that dark patterns can cause, and they highlight the need for greater regulation and enforcement.

The use of dark patterns has also led to a number of high-profile lawsuits and regulatory actions. For example, the US Federal Trade Commission (FTC) has taken action against a number of companies for using dark patterns, including Amazon and LinkedIn. The FTC has also issued a report on dark patterns, which provides guidance to businesses on how to avoid using them. In Europe, the General Data Protection Regulation (GDPR) includes provisions that are designed to protect users from dark patterns, such as the requirement for clear and unambiguous consent for the processing of personal data. These regulatory actions are a positive step, but more needs to be done to combat the use of dark patterns.

### 7. Cognitive Era Considerations

The rise of artificial intelligence (AI) and machine learning (ML) is likely to have a significant impact on the use of dark patterns. On the one hand, AI and ML could be used to create more sophisticated and effective dark patterns that are personalized to individual users. For example, an AI-powered dark pattern could learn a user's cognitive biases and preferences, and then use this information to design a manipulative interface that is tailored to that user. This could make dark patterns even more difficult to detect and resist. The use of AI to personalize dark patterns is a major threat to user autonomy, and it is a development that needs to be closely monitored.

On the other hand, AI and ML could also be used to detect and combat dark patterns. For example, an AI-powered tool could be used to scan websites and apps for dark patterns, and to alert users to their presence. An AI-powered tool could also be used to automatically block dark patterns, or to provide users with alternative interfaces that are free from manipulation. The development of these tools could help to level the playing field between platforms and users, and to create a more transparent and ethical digital environment. The use of AI to combat dark patterns is a promising area of research, and it is one that could have a significant impact on the future of the internet.

### 8. Commons Alignment Assessment

- **Shared Resource Potential:** Low - Dark patterns are designed to extract value from users, not to create a shared resource. They are a form of enclosure that privatizes user data and attention for the benefit of the platform. They are a zero-sum game, where the platform's gain is the user's loss.
- **Democratic Governance:** Low - Dark patterns are the antithesis of democratic governance. They are a form of manipulation that undermines user autonomy and control. They are a top-down approach to design that does not involve users in the decision-making process. They are a form of digital authoritarianism.
- **Equitable Access:** Low - Dark patterns can be particularly harmful to vulnerable users, which can exacerbate existing inequalities. They are a form of discrimination that can deny users equitable access to information and services. They are a barrier to digital inclusion.
- **Sustainability:** Low - The use of dark patterns is not a sustainable practice. It can lead to a loss of user trust and a damaged reputation, which can have long-term consequences for the platform. It is a short-term approach to business that is not in the long-term interests of the platform or its users. It is a race to the bottom.
- **Community Benefit:** Low - Dark patterns do not benefit the community. They are a form of exploitation that can harm users and erode trust in the digital environment. They are a net negative for society. They are a threat to the health of the digital commons.
