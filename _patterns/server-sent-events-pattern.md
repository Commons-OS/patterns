---
id: pat_019c47f5007f717e8fbe8e571c
page_url: https://commons-os.github.io/patterns/server-sent-events-pattern/
github_url: https://github.com/Commons-OS/patterns/blob/main/_patterns/server-sent-events-pattern.md
slug: server-sent-events-pattern
title: Server-Sent Events Pattern
aliases:
- SSE
- EventSource
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
  commons_alignment: 4
  commons_domain:
  - business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- manus-ai
- cloudsters
sources:
- https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
- https://engineering.surveysparrow.com/scaling-real-time-applications-with-server-sent-events-sse-abd91f70a5c9
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

The Server-Sent Events (SSE) pattern is a web technology that enables a server to push real-time updates to a web client over a single, long-lived HTTP connection. It provides a one-way communication channel from the server to the client, making it an efficient solution for applications that need to display live data streams, such as news feeds, stock tickers, and notifications. SSE is a W3C standard and is supported by all modern web browsers through the `EventSource` API [1].

### 2. Core Principles

The SSE pattern is based on a few core principles:

*   **HTTP-Based:** SSE operates over standard HTTP, which simplifies implementation and ensures compatibility with existing web infrastructure.
*   **Unidirectional:** Communication is one-way, from the server to the client. This makes SSE simpler and more lightweight than bidirectional alternatives like WebSockets.
*   **Text-Based:** The event stream is a simple, human-readable text format. Messages are separated by newlines, and each message can have fields for event type, data, and ID.
*   **Automatic Reconnection:** The browser automatically handles reconnection if the connection is lost, and the server can specify a reconnection timeout.

### 3. Key Practices

Many web applications need to display real-time information to users. Before SSE, developers relied on techniques like long-polling, which involves the client repeatedly sending requests to the server to check for new data. This approach is inefficient, as it creates a lot of unnecessary network traffic and can lead to high server load. A more efficient and scalable solution is needed to push real-time updates from the server to the client.

### 4. Implementation

The Server-Sent Events pattern provides a simple and efficient solution for pushing real-time updates from the server to the client. The client initiates a connection to the server using the `EventSource` API. The server then keeps the connection open and sends events to the client as they become available. The client can listen for these events and update the user interface accordingly. This approach eliminates the need for polling and provides a much more efficient and scalable solution for real-time web applications.

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


| Pros | Cons |
| --- | --- |
| Simple to implement | Unidirectional (server-to-client only) |
| Efficient for real-time updates | Limited number of connections per browser |
| Automatic reconnection | No support for binary data |
| Built-in error handling | |

### 6. When to Use

*   **Twitter:** Twitter uses SSE to push real-time updates to users' timelines.
*   **Facebook:** Facebook uses SSE to send real-time notifications to users.
*   **The New York Times:** The New York Times uses SSE to provide live news updates to its readers.
*   **Yahoo! Finance:** Yahoo! Finance uses SSE to provide real-time stock price updates.

### 7. Anti-Patterns & Gotchas

In the cognitive era, SSE can be used to stream real-time data from AI/ML models to clients. For example, an application could use SSE to provide live transcription of an audio stream, or to display real-time sentiment analysis of a social media feed. This enables the creation of a new class of intelligent applications that can react to events in real time.

### 8. References

The Server-Sent Events pattern aligns well with the principles of the Commons:

*   **Shared Resource:** SSE is an open standard, available for all to use.
*   **Democratic Governance:** The SSE standard is developed and maintained by the W3C, a community-driven organization.
*   **Equitable Access:** SSE is supported by all modern web browsers, ensuring that it is accessible to a wide range of users.
*   **Sustainability:** By reducing the need for polling, SSE can help to reduce network traffic and server load, leading to lower energy consumption.
*   **Community Benefit:** SSE enables the creation of a wide range of real-time applications that can benefit society, such as live news, emergency alerts, and collaborative tools.

### 8. References
[1] Mozilla Developer Network. (2025). Using server-sent events. Retrieved from https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[2] Sekar, M. (2025). Scaling Real-Time Applications with Server-Sent Events(SSE). Retrieved from https://engineering.surveysparrow.com/scaling-real-time-applications-with-server-sent-events-sse-abd91f70a5c9
