---
id: pat_34fe5b683f3c43dab01b0a7d
page_url: https://commons-os.github.io/patterns/decentralized-identifier-did/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/decentralized-identifier-did.md
slug: decentralized-identifier-did
title: Decentralized Identifier (DID)
aliases: []
version: 1.0
created: 2026-02-01 12:17:06+00:00
modified: 2026-02-01 12:17:06+00:00
classification:
  universality: universal
  domain: sovereignty
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

Decentralized Identifier (DID) is a pattern for building resilient value creation systems.

**Problem:** Traditional digital identifiers, like email addresses or usernames, are issued and controlled by a central authority (e.g., Google, Facebook, your employer). This creates a dependency on that authority. If the authority decides to revoke your identifier, or if it goes out of business, you lose your digital identity. This centralized model is the root of vendor lock-in and a single point of control for digital identity.

**Context:** You need to create a digital identity for a user, organization, or thing that is globally unique, persistent, and not controlled by any single central authority. You need a foundation for a truly self-sovereign identity.

### 2. Core Principles

**Use a Decentralized Identifier (DID), a new type of globally unique identifier that is registered on a decentralized system (like a blockchain or other distributed ledger) and is under the full control of the identity owner.**

A DID is a simple text string that looks like this: `did:example:123456789abcdefghi`. The DID points to a **DID Document**, a JSON file that contains the public keys, service endpoints, and other metadata associated with the DID. The identity owner controls the DID Document and can update it at any time by using the private keys associated with the DID.

### 3. Rationale

DIDs are a fundamental building block for decentralized identity and digital sovereignty. They:
- **Enable Self-Sovereignty**: The identity owner creates, controls, and can even delete their own identifier without permission from any central authority.
- **Are Persistent**: A DID can last for the lifetime of the subject, unlike an email address or employee ID which can change.
- **Are Globally Resolvable**: Anyone in the world can look up the DID Document for a given DID to find its public keys and service endpoints.
- **Are Cryptographically Verifiable**: The link between the DID and the DID Document is secured with cryptography.

### 4. Consequences

- **Positive**:
    - A truly decentralized and self-sovereign foundation for digital identity.
    - Eliminates the dependency on centralized identity providers.
- **Negative**:
    - **Ecosystem is still maturing**: The standards and technologies around DIDs are still new and evolving.
    - **Key Management is Critical**: The user is fully responsible for the security of their private keys. If the keys are lost, the DID can be lost forever. This is a major usability challenge.
    - **Complexity**: The concepts of DIDs, DID Documents, and decentralized ledgers can be complex for developers and users to understand.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **W3C DID Specification**: The core standard for DIDs is being developed by the World Wide Web Consortium (W3C).
- **Hyperledger Indy, DIF, Sovrin**: Major open-source projects and foundations that are building DID-based identity systems.
- **Microsoft Entra Verified ID**: Microsoft's decentralized identity solution is built on DIDs.

