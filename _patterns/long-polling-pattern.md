---
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/long-polling-pattern.md
slug: long-polling-pattern
title: Long Polling Pattern
aliases:
- Comet
- Reverse AJAX
version: '1.0'
created: '2026-02-10 00:00:00+00:00'
modified: '2026-02-10 00:00:00+00:00'
classification:
  universality: domain
  domain: technology
  category:
  - practice
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 3
  commons_domain: &id001
  - business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- name: Manus AI
  role: author
- name: cloudsters
  role: author
sources:
- https://www.pubnub.com/guides/long-polling/
- https://javascript.info/long-polling
- https://ably.com/topic/long-polling
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
id: pat_019c47f4ff7f7da9ae2d9c7777
page_url: https://commons-os.github.io/patterns/long-polling-pattern/
commons_domain: *id001
---









### 1. Overview

Long Polling is a design pattern that enables a server to push information to a client in a way that emulates a persistent connection over HTTP. It is a variation of the traditional polling technique and is used to provide more responsive and efficient real-time communication between a client and a server. The pattern is particularly useful in web applications where the server needs to send updates to the client as soon as new data is available, without the client having to repeatedly request it.

The historical origins of long polling can be traced back to the early days of the web, when developers were looking for ways to overcome the limitations of the traditional request-response model of HTTP. The term "Comet" was coined in 2006 by Alex Russell in his blog post "Comet: Low Latency Data for the Browser" to describe a set of techniques, including long polling, that allow a web server to push data to a browser without the browser explicitly requesting it [1]. Long polling emerged as a popular and practical solution for building more dynamic and interactive web applications before the advent of more modern technologies like WebSockets and Server-Sent Events (SSE).

### 2. Core Principles

The Long Polling pattern is defined by a set of fundamental principles that govern its operation. These principles work together to create a communication channel that is more responsive than traditional polling methods while still relying on the standard HTTP protocol.

At its core, the pattern operates on the principle of a client-initiated, server-held connection. The process begins with the client sending a request to the server, just as it would in a normal HTTP interaction. However, instead of responding immediately, the server holds the request open for an extended period. The server will only send a response under two conditions: when new data becomes available for the client, or when a predefined timeout is reached. Upon receiving a response, the client immediately sends another request to the server, re-establishing the connection and ensuring that it is always ready to receive new data. This continuous cycle of request, hold, and response creates a persistent, or near real-time, communication channel between the client and the server.

### 3. Key Practices

In many modern applications, there is a need for the server to send updates to the client in real-time or near real-time. For example, in a chat application, new messages should appear on the user's screen as soon as they are sent. Similarly, in a live sports-scoring application, the scores should be updated instantly as the game progresses. The traditional request-response model of HTTP, where the client must initiate a request to receive data from the server, is not well-suited for these types of applications.

The most basic approach to solving this problem is to use **short polling**, where the client repeatedly sends requests to the server at a fixed interval (e.g., every few seconds) to check for new data. However, this approach has several significant drawbacks:

*   **High Latency:** There is an inherent delay between the time new data becomes available on the server and the time the client receives it. The average latency is half of the polling interval. To reduce latency, the polling interval must be shortened, which in turn exacerbates the other problems.
*   **High Network Overhead:** A large number of requests are sent to the server, many of which will be redundant if there is no new data. This creates unnecessary network traffic and consumes server resources.
*   **Scalability Issues:** As the number of clients increases, the server can become overwhelmed by the constant polling requests, leading to performance degradation and scalability challenges.

### 4. Implementation

The Long Polling pattern provides an elegant solution to the problem of real-time server-to-client communication by inverting the traditional request-response model. Instead of the client repeatedly asking the server for new data, the client makes a single request and the server holds that request open until it has something to send.

The process works as follows:

1.  **Client Request:** The client sends an HTTP request to the server, asking for any new data. This is similar to a normal HTTP request.
2.  **Server Holds Request:** The server receives the request but does not immediately send a response. Instead, it holds the request open and waits for new data to become available.
3.  **Data Becomes Available:** When new data is available for the client, the server sends a response containing the new data.
4.  **Client Receives Data and Re-requests:** The client receives the data and immediately sends another long poll request to the server. This ensures that the server is always ready to send new data to the client.
5.  **Timeout:** If no new data becomes available within a certain amount of time (a timeout), the server sends an empty response. The client then immediately sends another long poll request.

This process creates a persistent connection between the client and the server, allowing the server to push data to the client as soon as it becomes available. This significantly reduces the latency of data delivery and the number of requests sent to the server, making it a much more efficient solution than short polling.

### 5. 7 Pillars Assessment

| Pillar | Score (1-5) | Rationale |
|--------|-------------|-----------|
| Purpose | 3 | Serves a clear technical purpose in system design |
| Governance | 3 | Can be governed through standard engineering practices |
| Culture | 3 | Supports engineering culture of reliability and quality |
| Incentives | 3 | Aligns incentives toward system stability |
| Knowledge | 4 | Well-documented pattern with extensive community knowledge |
| Technology | 4 | Directly applicable to modern technology stacks |
| Resilience | 4 | Contributes to overall system resilience |
| **Overall** | **3.4** | **A valuable technical pattern that supports commons infrastructure** |


While the Long Polling pattern offers a significant improvement over traditional short polling, it is not without its own set of trade-offs and considerations. It is important to understand these factors when deciding whether to use long polling in a particular application.

| **Pros** | **Cons** |
| :--- | :--- |
| **Low Latency:** Long polling provides near real-time communication, as the server can push data to the client as soon as it becomes available. | **Resource Intensive:** Holding a large number of open connections can be resource-intensive for the server, especially as the number of clients grows. |
| **Reduced Network Overhead:** Compared to short polling, long polling significantly reduces the number of requests sent to the server, as the client only sends a new request after receiving a response. | **Complexity:** Implementing long polling can be more complex than short polling, as it requires careful management of connections, timeouts, and error handling. |
| **Wide Compatibility:** Long polling is based on standard HTTP and is supported by virtually all web browsers and servers, making it a highly compatible solution. | **Scalability Challenges:** While more scalable than short polling, long polling can still present scalability challenges in very large-scale applications with a massive number of concurrent clients. |
| **Firewall and Proxy Friendly:** Since long polling uses standard HTTP requests, it is generally not blocked by firewalls and proxies, which can sometimes be an issue with other real-time technologies like WebSockets. | **No Guaranteed Delivery:** Like any HTTP-based communication, there is no inherent guarantee of message delivery. Additional logic may be required to ensure that messages are not lost. |

### 6. When to Use

The Long Polling pattern has been widely used in a variety of real-world applications, particularly in the years before WebSockets became a mainstream technology. Even today, it remains a viable option in certain scenarios, especially when simplicity and compatibility are key requirements.

One of the most well-known examples of long polling is its use in early versions of **Facebook's notification and messaging systems**. When a user received a new notification or message, the server would push the update to the user's browser using long polling, providing a near real-time experience. While Facebook has since transitioned to more modern technologies, its use of long polling was a testament to the pattern's effectiveness in a large-scale social media application.

Other common examples of long polling in action include:

*   **Real-time Chat Applications:** Many simple chat applications have been built using long polling to deliver messages between users in real-time.
*   **Live Commenting Systems:** Systems that allow users to comment on a live event, such as a blog post or a news article, often use long polling to display new comments as they are posted.
*   **Online Collaboration Tools:** Some online collaboration tools use long polling to synchronize changes between multiple users who are working on the same document or project.

### 7. Anti-Patterns & Gotchas

In the Cognitive Era, characterized by the rise of artificial intelligence (AI) and machine learning (ML), the need for real-time data exchange between clients and intelligent services is more critical than ever. While more advanced protocols like WebSockets and gRPC are often favored for high-throughput streaming applications, the Long Polling pattern still holds relevance in specific AI/ML scenarios.

One key application is in managing interactions with long-running, asynchronous AI tasks. For example, a user might submit a request for a complex data analysis or a generative AI model to create an image. These tasks can take a significant amount of time to complete. Long polling provides a simple and effective mechanism for the client to wait for the result. The client initiates a long poll request, and the server holds it until the AI model has finished its processing and then returns the final result. This avoids the complexity of setting up a full-fledged streaming protocol for what might be a one-off or infrequent interaction.

Furthermore, long polling can be used in simple conversational AI and chatbot applications. When a user sends a message, the client can use long polling to wait for the bot's response. This is often sufficient for text-based conversations where the latency requirements are not as stringent as in, for example, real-time voice or video analysis.

However, for applications that require a continuous stream of data to or from an AI model, such as real-time object detection in a video feed or continuous sensor data analysis, long polling is generally not the most suitable choice. The overhead of establishing a new HTTP request for each data packet can become a significant bottleneck and lead to performance issues. In these high-throughput, low-latency scenarios, the persistent, bidirectional connections offered by WebSockets or the high-performance RPC framework of gRPC are far more efficient and scalable.

### 8. References

The Long Polling pattern, when viewed through the lens of the Commons principles, presents a mixed but generally positive alignment. Its primary contribution to the commons is as a widely understood and accessible technique for improving the user experience of web applications.

From the perspective of a **Shared Resource**, the pattern itself is a piece of shared knowledge within the software engineering community. It is not a tangible resource that can be depleted, but rather a technique that can be freely used and adapted by anyone. In this sense, it is a valuable part of the intellectual commons of software design.

In terms of **Equitable Access**, the pattern is highly accessible. It relies on the ubiquitous HTTP protocol, which is supported by all web browsers and servers. This means that developers do not need specialized software or hardware to implement long polling, making it an equitable choice for a wide range of projects and teams.

When it comes to **Sustainability**, the picture is more nuanced. Compared to the less efficient short polling method, long polling is a more sustainable choice as it reduces unnecessary network traffic and server load. However, when compared to more modern technologies like WebSockets, long polling is less sustainable in large-scale applications due to its higher resource consumption on the server. Therefore, its sustainability is context-dependent.

The pattern has a clear **Community Benefit** by enabling the creation of more responsive and interactive applications. This leads to a better user experience, which is a direct benefit to the community of users of those applications. The simplicity of the pattern also benefits the developer community by providing a straightforward way to implement real-time features without the complexity of more advanced protocols.

Finally, the principle of **Democratic Governance** is not directly applicable to the Long Polling pattern itself, as it is a technical pattern rather than a community or an organization. However, the fact that it is an open and well-documented pattern means that there are no barriers to its use or adaptation, which is in the spirit of democratic and open principles.

### 8. References
[1] A. Russell, "Comet: Low Latency Data for the Browser," *Alex Russell's Blog*, 2006. [Online]. Available: https://alex.russo.org/2006/03/comet-low-latency-data-for-the-browser/
