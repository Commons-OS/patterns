_# Pattern: Security Headers

## 1. Pattern Name and Number

**S044: Security Headers**

## 2. Problem

Web browsers have many built-in security features, but they are often disabled by default for backward compatibility. Without explicit instructions from the web server, browsers may be vulnerable to a wide range of common attacks, such as cross-site scripting (XSS), clickjacking, and protocol downgrade attacks. Relying on users to have a perfectly configured and up-to-date browser is not a reliable security strategy.

## 3. Context

You are developing a web application and need to protect your users from common client-side attacks. You want to leverage the built-in security capabilities of modern web browsers to harden your application's security posture.

## 4. Solution

**Configure your web server to send a set of HTTP Security Headers with every response.** These headers are instructions that tell the browser how to behave and what security policies to enforce for your site.

Key security headers include:
- **`Strict-Transport-Security` (HSTS)**: Forces the browser to communicate with your site only over HTTPS, preventing protocol downgrade attacks.
- **`Content-Security-Policy` (CSP)**: Provides fine-grained control over which resources (scripts, images, etc.) the browser is allowed to load, mitigating the risk of XSS attacks.
- **`X-Frame-Options`**: Prevents your site from being embedded in an `<iframe>` on other sites, which is the primary defense against clickjacking.
- **`X-Content-Type-Options`**: Prevents the browser from trying to guess the content type of a resource, which can help prevent certain types of XSS attacks.
- **`Referrer-Policy`**: Controls how much referrer information is sent with requests, which can help protect user privacy.

## 5. Rationale

Security headers are a simple, effective, and low-cost way to significantly improve the security of a web application. They:
- **Provide Defense in Depth**: Add an extra layer of client-side security to complement your server-side security controls.
- **Leverage Browser Security**: Take full advantage of the powerful security features built into modern browsers.
- **Are Easy to Implement**: In most cases, they can be enabled with a few lines of configuration on your web server or application gateway.

## 6. Consequences

- **Positive**:
    - A significant reduction in the risk of common client-side attacks.
    - A stronger security posture with minimal implementation effort.
- **Negative**:
    - **Can be complex to configure correctly**: A misconfigured `Content-Security-Policy` can break legitimate parts of your application.
    - **Not a silver bullet**: They are an important layer of defense, but they do not replace the need for secure server-side coding practices.

## 7. Known Uses

- **All major websites** (Google, Facebook, Twitter, etc.) use a strong set of security headers.
- **Security scanning tools** (like Qualys SSL Labs and Security Headers) check for the presence and correctness of these headers as a key indicator of a site's security posture.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 3           | A practical pattern for web security.                                                                 |
| **2. Governance**       | 4           | A key technical governance control for web application security.                                      |
| **3. Economy**          | 4           | A very low-cost way to prevent costly security incidents.                                             |
| **4. Technology**       | 5           | A standard and fundamental web security technology.                                                   |
| **5. Operations**       | 4           | A standard part of secure web server configuration and operations.                                    |
| **6. Culture**          | 3           | Promotes a culture of secure web development.                                                         |
| **7. Resilience**       | 4           | Builds resilience against a wide range of common client-side attacks.                                 |
| **Overall Score**       | **3.9**     | A simple, essential, and highly effective pattern for securing any web application.                    |
