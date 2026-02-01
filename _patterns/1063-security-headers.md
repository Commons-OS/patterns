---
id: pat_00cac9f737b24d6688f941cd
page_url: https://commons-os.github.io/patterns/1063-security-headers/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/1063-security-headers.md
slug: 1063-security-headers
title: Security Headers
aliases: []
version: 1.0
created: 2026-02-01T12:17:06Z
modified: 2026-02-01T12:17:06Z
tags:
  universality: universal
  domain: security
  category: [pattern]
  era: [cognitive]
  origin: [commons-os]
  status: draft
  commons_alignment: 4
commons_domain: business
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
### 1. Overview

Security Headers is a pattern for building resilient value creation systems.

**Problem:** Web browsers have many built-in security features, but they are often disabled by default for backward compatibility. Without explicit instructions from the web server, browsers may be vulnerable to a wide range of common attacks, such as cross-site scripting (XSS), clickjacking, and protocol downgrade attacks. Relying on users to have a perfectly configured and up-to-date browser is not a reliable security strategy.

**Context:** You are developing a web application and need to protect your users from common client-side attacks. You want to leverage the built-in security capabilities of modern web browsers to harden your application's security posture.

### 2. Core Principles

**Configure your web server to send a set of HTTP Security Headers with every response.** These headers are instructions that tell the browser how to behave and what security policies to enforce for your site.

Key security headers include:
- **`Strict-Transport-Security` (HSTS)**: Forces the browser to communicate with your site only over HTTPS, preventing protocol downgrade attacks.
- **`Content-Security-Policy` (CSP)**: Provides fine-grained control over which resources (scripts, images, etc.) the browser is allowed to load, mitigating the risk of XSS attacks.
- **`X-Frame-Options`**: Prevents your site from being embedded in an `<iframe>` on other sites, which is the primary defense against clickjacking.
- **`X-Content-Type-Options`**: Prevents the browser from trying to guess the content type of a resource, which can help prevent certain types of XSS attacks.
- **`Referrer-Policy`**: Controls how much referrer information is sent with requests, which can help protect user privacy.

### 3. Rationale

Security headers are a simple, effective, and low-cost way to significantly improve the security of a web application. They:
- **Provide Defense in Depth**: Add an extra layer of client-side security to complement your server-side security controls.
- **Leverage Browser Security**: Take full advantage of the powerful security features built into modern browsers.
- **Are Easy to Implement**: In most cases, they can be enabled with a few lines of configuration on your web server or application gateway.

### 4. Consequences

- **Positive**:
    - A significant reduction in the risk of common client-side attacks.
    - A stronger security posture with minimal implementation effort.
- **Negative**:
    - **Can be complex to configure correctly**: A misconfigured `Content-Security-Policy` can break legitimate parts of your application.
    - **Not a silver bullet**: They are an important layer of defense, but they do not replace the need for secure server-side coding practices.

### 5. Application Context

**Best Used For:**
* Value creation systems requiring strong privacy and security foundations
* Organizations operating in regulated environments
* Systems handling sensitive data or requiring high trust

### 6. Known Uses

- **All major websites** (Google, Facebook, Twitter, etc.) use a strong set of security headers.
- **Security scanning tools** (like Qualys SSL Labs and Security Headers) check for the presence and correctness of these headers as a key indicator of a site's security posture.

