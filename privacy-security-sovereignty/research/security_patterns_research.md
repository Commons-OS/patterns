# Security Patterns Research Notes

## Source 1: NIST SP 800-207 Zero Trust Architecture

**Definition**: Zero Trust (ZT) is a cybersecurity paradigm that moves defenses from static, network-based perimeters to focus on users, assets, and resources.

### Core Zero Trust Principles:
1. **No Implicit Trust** - No trust granted based on network location or asset ownership
2. **Verify Explicitly** - Authentication and authorization are discrete functions before session establishment
3. **Protect Resources, Not Networks** - Focus on assets, services, workflows, not network segments
4. **Assume Breach** - Design assuming adversaries are already inside

### Zero Trust Architecture Components:
- Policy Engine (PE)
- Policy Administrator (PA)
- Policy Enforcement Point (PEP)
- Continuous Diagnostics and Mitigation (CDM)
- Industry Compliance
- Threat Intelligence
- Network and System Activity Logs
- Data Access Policies
- Enterprise PKI
- ID Management
- SIEM System

### ZTA Deployment Models:
1. **Device Agent/Gateway Model** - Agent on device communicates with gateway
2. **Enclave Gateway Model** - Gateway protects resource enclave
3. **Resource Portal Model** - Portal acts as PEP for user requests
4. **Device Application Sandboxing** - Apps run in isolated sandbox

## Source 2: Microsoft Azure Security Design Patterns
URL: https://learn.microsoft.com/en-us/azure/well-architected/security/design-patterns

### Key Security Patterns:
1. **Ambassador Pattern** - Offload security processing to a proxy
2. **Backends for Frontends** - Separate backend services for different clients
3. **Bulkhead Pattern** - Isolate elements to contain failures
4. **Gateway Aggregation** - Single gateway for multiple requests
5. **Gateway Offloading** - Offload shared functionality to gateway
6. **Gateway Routing** - Route requests to multiple services
7. **Sidecar Pattern** - Deploy helper components alongside main service
8. **Strangler Fig** - Incrementally migrate legacy system

## Source 3: SEI Secure Design Patterns (CMU)
URL: https://www.sei.cmu.edu/documents/813/2009_005_001_15110.pdf

### Categories of Secure Design Patterns:

#### Architectural-Level Patterns:
1. **Distrustful Decomposition** - Partition system into mutually distrustful components
2. **Privilege Separation** - Separate privileged operations from unprivileged
3. **Defer to Kernel** - Let OS handle security-critical operations

#### Design-Level Patterns:
4. **Secure Factory** - Encapsulate object creation with security checks
5. **Secure Strategy Factory** - Select security strategy at runtime
6. **Secure Builder Factory** - Build complex secure objects step by step
7. **Secure Chain of Responsibility** - Pass security requests along chain
8. **Secure State Machine** - Manage security state transitions
9. **Secure Visitor** - Separate security algorithm from object structure

#### Implementation-Level Patterns:
10. **Secure Logger** - Log security events safely
11. **Clear Sensitive Information** - Zero out sensitive data after use
12. **Secure Directory** - Protect directory structure
13. **Pathname Canonicalization** - Resolve paths to canonical form
14. **Input Validation** - Validate all input data

## Defense in Depth Patterns

**Definition**: Strategy using multiple, redundant defensive measures so if one fails, others remain.

### Defense in Depth Layers:
1. **Physical Security** - Physical access controls
2. **Network Security** - Firewalls, IDS/IPS, segmentation
3. **Host Security** - OS hardening, endpoint protection
4. **Application Security** - Secure coding, WAF
5. **Data Security** - Encryption, access controls, DLP
6. **Identity Security** - MFA, IAM, PAM
7. **Monitoring & Response** - SIEM, SOC, incident response

### Key Defense in Depth Patterns:
1. **Network Segmentation** - Divide network into security zones
2. **Microsegmentation** - Fine-grained segmentation at workload level
3. **DMZ Architecture** - Buffer zone between internal and external
4. **Air Gap** - Physical isolation of critical systems
5. **Defense in Breadth** - Multiple detection methods at each layer

## Security Patterns to Document (Initial List)

### Zero Trust Patterns:
1. Zero Trust Architecture
2. Continuous Verification
3. Least Privilege Access
4. Microsegmentation
5. Software-Defined Perimeter
6. Identity-Centric Security

### Access Control Patterns:
7. Role-Based Access Control (RBAC)
8. Attribute-Based Access Control (ABAC)
9. Policy-Based Access Control
10. Just-In-Time Access
11. Privileged Access Management
12. Multi-Factor Authentication

### Network Security Patterns:
13. Network Segmentation
14. DMZ Architecture
15. Bastion Host
16. Jump Server
17. Service Mesh Security
18. API Gateway Security

### Application Security Patterns:
19. Input Validation
20. Output Encoding
21. Parameterized Queries
22. Secure Session Management
23. Security Headers
24. Content Security Policy

### Cryptographic Patterns:
25. Encryption at Rest
26. Encryption in Transit
27. Key Management
28. Certificate Management
29. Hardware Security Modules
30. Secrets Management


## Software Supply Chain Security Patterns

### SBOM (Software Bill of Materials)
**Definition**: A comprehensive inventory of all software components, dependencies, and metadata in an application.

**Key SBOM Standards**:
- SPDX (Software Package Data Exchange)
- CycloneDX
- SWID Tags

**SBOM Use Cases**:
1. Vulnerability identification
2. License compliance
3. Component tracking
4. Incident response
5. Procurement decisions

### SLSA (Supply-chain Levels for Software Artifacts)
**Definition**: A security framework for ensuring the integrity of software artifacts throughout the supply chain.

**SLSA Levels**:
- Level 0: No guarantees
- Level 1: Documentation of build process
- Level 2: Tamper resistance of build service
- Level 3: Hardened builds
- Level 4: Two-person reviewed

### Secure SDLC Patterns

#### Requirements Phase:
1. Security Requirements Gathering
2. Threat Modeling
3. Risk Assessment
4. Abuse Case Development

#### Design Phase:
5. Secure Architecture Review
6. Attack Surface Analysis
7. Security Design Patterns Selection
8. Data Flow Diagrams

#### Development Phase:
9. Secure Coding Standards
10. Code Review
11. Static Application Security Testing (SAST)
12. Software Composition Analysis (SCA)

#### Testing Phase:
13. Dynamic Application Security Testing (DAST)
14. Interactive Application Security Testing (IAST)
15. Penetration Testing
16. Fuzz Testing

#### Deployment Phase:
17. Secure Configuration
18. Infrastructure as Code Security
19. Container Security Scanning
20. Runtime Application Self-Protection (RASP)

### Supply Chain Security Patterns to Document:

31. Software Bill of Materials (SBOM)
32. SLSA Framework Implementation
33. Dependency Pinning
34. Reproducible Builds
35. Code Signing
36. Binary Authorization
37. Artifact Registry Security
38. CI/CD Pipeline Security
39. Third-Party Code Review
40. Vendor Security Assessment
41. Open Source Governance
42. License Compliance Automation
