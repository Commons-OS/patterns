---
id: pat_0e818ade26c24addaf9e0d72
page_url: https://commons-os.github.io/patterns/private-information-retrieval-pir/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/private-information-retrieval-pir.md
slug: private-information-retrieval-pir
title: Private Information Retrieval (PIR)
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
classification:
  universality: universal
  domain: privacy
  category:
  - pattern
  era:
  - cognitive
  origin:
  - commons-os
  status: draft
  commons_alignment: 4
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors:
- manus-ai
- cloudsters
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
### 1. Overview

Private Information Retrieval (PIR) is a pattern for building resilient value creation systems.

**Problem:** When you query a database, the server hosting the database learns what you are looking for. This can be a major privacy violation. For example, if you query a medical database for information about a specific disease, the server learns of your interest in that disease. If you query a patent database for a specific invention, the server learns about your company's research interests.

**Context:** You need to allow a client to retrieve an item from a database on a server without the server learning which item the client is retrieving. The database itself is public, but the client's query is private.

### 2. Core Principles

**Use a Private Information Retrieval (PIR) protocol. PIR is a cryptographic protocol that allows a user to retrieve an item from a server in possession of a database without revealing which item is retrieved.**

PIR protocols work by having the client send a query that is structured in such a way that it touches every single item in the database. The server processes this query and returns a response, also structured in a way that the client can decode to get the specific item they want. From the server's perspective, the query looks the same regardless of which item the client is interested in, because it has to read its entire database to answer it.

### 3. Rationale

PIR provides a strong, cryptographic guarantee of query privacy. It:
- **Protects Query Privacy**: Ensures that the server learns nothing about the client's interests.
- **Decouples Access from Interest**: Allows users to access public information without revealing their intentions.

### 4. Consequences

- **Positive**:
    - The strongest possible guarantee of query privacy.
    - Enables private access to public or semi-public databases.
- **Negative**:
    - **Extreme Performance Overhead**: The major drawback of PIR is that it requires the server to process its entire database for every single query. This makes it computationally infeasible for all but the smallest databases.
    - **High Communication Cost**: PIR protocols can also have high communication overhead.
    - **Complexity**: These are complex cryptographic protocols.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

PIR is mostly a subject of academic research, but it has some niche applications:
- **Password Breach Checking**: Some systems use PIR-like techniques to allow users to check if their password was in a data breach without revealing the password to the server.
- **Private Contact Discovery**: Used in some messaging apps to discover which of a user's contacts are also on the app, without revealing the user's entire contact list to the server.

