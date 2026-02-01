# AI-Specific Privacy, Security & Governance Patterns Research Notes

## Source 1: CSIRO Responsible AI Pattern Catalogue

**Definition**: Responsible AI is the practice of developing and using AI systems in a way that benefits individuals, groups, and wider society, while minimizing negative consequences.

### Pattern Categories:

#### Governance Patterns (Industry/Organization Level):
1. **RAI Law and Regulation** - Regulatory frameworks for AI
2. **RAI Maturity Model** - Assess organizational RAI capability
3. **RAI Certification** - Third-party certification of AI systems
4. **Regulatory Sandbox** - Safe space for AI experimentation
5. **Building Code** - Standards for AI system construction
6. **Independent Oversight** - External review mechanisms
7. **Trust Mark** - Visual indicator of RAI compliance
8. **RAI Standard** - Industry standards for responsible AI
9. **Leadership Commitment for RAI** - Executive sponsorship
10. **RAI Risk Committee** - Dedicated governance body
11. **Code for RAI** - Ethical guidelines and principles
12. **RAI Risk Assessment** - Systematic risk evaluation
13. **RAI Training** - Education and awareness programs
14. **Role-Level Accountability Contract** - Clear responsibilities
15. **RAI Bill of Materials** - Inventory of AI components
16. **Standardized Reporting** - Consistent disclosure formats

#### Process Patterns (Team Level):
17. **Customized Agile Process** - Agile adapted for RAI
18. **Tight Coupling of AI and Non-AI Development** - Integrated development
19. **Diverse Team** - Inclusive team composition
20. **Stakeholder Engagement** - Involve affected parties
21. **Continuous Documentation Using Templates** - Systematic documentation
22. **Verifiable Claim for AI System Artifacts** - Provable assertions
23. **Failure Mode and Effects Analysis (FMEA)** - Risk identification
24. **Fault Tree Analysis (FTA)** - Root cause analysis
25. **AI Suitability Assessment** - Evaluate AI appropriateness
26. **Verifiable RAI Requirement** - Testable requirements
27. **Lifecycle-Driven Data Requirement** - Data governance
28. **RAI User Story** - User-centric requirements
29. **Multi-Level Co-Architecting** - Coordinated design
30. **Envisioning Card** - Scenario planning tool
31. **RAI Design Modelling** - Design for responsibility
32. **System-Level RAI Simulation** - Test RAI properties

#### Product Patterns (System Level):
33. **XAI Interface** - Explainable AI user interface
34. **RAI Governance of APIs** - API-level controls
35. **RAI Governance via APIs** - Programmatic governance
36. **RAI Construction with Reuse** - Responsible component reuse
37. **RAI Acceptance Testing** - Validate RAI properties
38. **RAI Assessment for Test Cases** - Test case evaluation
39. **Continuous Deployment for RAI** - Safe deployment practices
40. **Extensible, Adaptive and Dynamic RAI Risk Assessment** - Runtime assessment
41. **Multi-Level Co-Versioning** - Coordinated versioning
42. **RAI Bill of Materials Registry** - Component tracking
43. **Verifiable RAI Credential** - Cryptographic attestation
44. **Co-Versioning Registry** - Version management
45. **Federated Learner** - Privacy-preserving training
46. **AI Mode Switcher** - Context-aware behavior
47. **Multi-Model Decision Maker** - Ensemble decisions
48. **Homogeneous Redundancy** - Fault tolerance
49. **Continuous RAI Validator** - Ongoing validation
50. **RAI Sandbox** - Safe testing environment
51. **RAI Knowledge Base** - Accumulated learnings
52. **RAI Digital Twin** - Simulation for testing
53. **Incentive Registry** - Reward mechanisms
54. **RAI Black Box** - Audit logging
55. **Global View Auditor** - System-wide monitoring
56. **Human-AI Interaction Patterns** - UX for AI
57. **Fairness Assessor** - Bias detection
58. **Discrimination Mitigator** - Bias correction
59. **Encrypted-Data-Based Trainer** - Privacy-preserving training
60. **Secure Aggregator** - Secure model aggregation
61. **Random Noise Data Generator** - Differential privacy
62. **Local Explainer** - Instance-level explanations
63. **Global Explainer** - Model-level explanations

## AI Privacy & Security Specific Patterns

### Model Privacy Patterns:
1. **Federated Learning** - Train without centralizing data
2. **Differential Privacy for ML** - Add noise to protect individuals
3. **Secure Multi-Party Computation for ML** - Joint computation without sharing
4. **Homomorphic Encryption for Inference** - Compute on encrypted data
5. **On-Device Inference** - Keep data on user device
6. **Model Distillation for Privacy** - Transfer knowledge without data
7. **Synthetic Data Generation** - Create privacy-safe training data

### Model Security Patterns:
8. **Model Watermarking** - Prove model ownership
9. **Adversarial Robustness** - Resist adversarial attacks
10. **Model Integrity Verification** - Detect tampering
11. **Secure Model Serving** - Protect deployed models
12. **Input Validation for ML** - Validate inference inputs
13. **Output Filtering** - Filter harmful outputs
14. **Rate Limiting for AI APIs** - Prevent abuse

### Training Data Governance Patterns:
15. **Training Data Provenance** - Track data origins
16. **Data Lineage** - Document data transformations
17. **Consent Management for Training Data** - Manage permissions
18. **Data Retention Policies** - Define data lifecycle
19. **Right to Erasure for Training Data** - Remove data on request
20. **Bias Audit for Training Data** - Detect data bias

### Model Governance Patterns:
21. **Model Registry** - Catalog all models
22. **Model Versioning** - Track model changes
23. **Model Approval Workflow** - Gate deployment
24. **Model Monitoring** - Track production performance
25. **Model Drift Detection** - Detect degradation
26. **Model Rollback** - Revert to previous versions
27. **A/B Testing for Models** - Compare model versions
28. **Shadow Deployment** - Test in production safely

### Explainability Patterns:
29. **LIME (Local Interpretable Model-agnostic Explanations)**
30. **SHAP (SHapley Additive exPlanations)**
31. **Attention Visualization** - Show model focus
32. **Feature Importance** - Rank input features
33. **Counterfactual Explanations** - Show what-if scenarios
34. **Decision Boundary Visualization** - Show classification logic

## EU AI Act Compliance Patterns

### Risk Classification:
- Unacceptable Risk (Prohibited)
- High Risk (Strict requirements)
- Limited Risk (Transparency obligations)
- Minimal Risk (No specific requirements)

### High-Risk AI Compliance Patterns:
1. **Risk Management System** - Continuous risk management
2. **Data Governance** - Quality and representativeness
3. **Technical Documentation** - Comprehensive documentation
4. **Record Keeping** - Automatic logging
5. **Transparency** - Clear information to users
6. **Human Oversight** - Human-in-the-loop
7. **Accuracy, Robustness, Cybersecurity** - Technical requirements
8. **Conformity Assessment** - Pre-market evaluation

## AI-Specific Patterns to Document (Initial List)

### Privacy Patterns:
1. Federated Learning
2. Differential Privacy for ML
3. On-Device Inference
4. Synthetic Data Generation
5. Model Distillation for Privacy
6. Secure Aggregation
7. Split Learning

### Security Patterns:
8. Adversarial Robustness
9. Model Watermarking
10. Secure Model Serving
11. Input Validation for ML
12. Output Filtering
13. Model Integrity Verification
14. AI Supply Chain Security

### Governance Patterns:
15. Model Registry
16. Training Data Provenance
17. Model Approval Workflow
18. Bias Audit
19. Explainability Interface
20. Human-in-the-Loop
21. Model Monitoring
22. AI Bill of Materials


## On-Device AI and Edge AI Privacy Patterns

### On-Device AI Benefits for Privacy:
- Data stays on user device
- No network transmission of sensitive data
- Reduced attack surface
- User control over data
- Compliance with data localization requirements

### On-Device AI Patterns:
1. **Local Model Inference** - Run inference entirely on device
2. **Model Quantization** - Reduce model size for device deployment
3. **Model Pruning** - Remove unnecessary parameters
4. **Knowledge Distillation** - Train smaller models from larger ones
5. **Split Inference** - Split model between device and cloud
6. **Cached Inference** - Cache common inference results
7. **Lazy Loading** - Load model components on demand

### Edge AI Architecture Patterns:
8. **Edge-Cloud Hybrid** - Combine edge and cloud processing
9. **Hierarchical Edge** - Multiple edge tiers
10. **Federated Edge** - Coordinate across edge nodes
11. **Edge Aggregation** - Aggregate data at edge before cloud
12. **Edge Gateway** - Central edge processing point
13. **Mesh Edge** - Peer-to-peer edge communication

### Private Inference Patterns:
14. **Trusted Execution Environment (TEE) Inference** - Use hardware enclaves
15. **Homomorphic Encryption Inference** - Compute on encrypted data
16. **Secure Multi-Party Computation Inference** - Distributed computation
17. **Garbled Circuits for Inference** - Cryptographic protocol
18. **Oblivious Inference** - Hide access patterns
19. **Differential Privacy Inference** - Add noise to outputs

### Model Privacy Protection Patterns:
20. **Model Obfuscation** - Hide model architecture
21. **Model Encryption** - Encrypt model weights
22. **Watermarking** - Embed ownership proof
23. **Fingerprinting** - Unique model identification
24. **Access Control for Models** - Restrict model access

## Additional AI Patterns to Document:

### Edge/On-Device Patterns:
23. On-Device Inference Architecture
24. Edge AI Gateway
25. Model Compression Pipeline
26. Split Learning
27. Hierarchical Federated Learning
28. Edge Model Update

### Private Inference Patterns:
29. TEE-Based Inference
30. Homomorphic ML Inference
31. Secure Two-Party Inference
32. Oblivious Neural Network
33. Private Information Retrieval for ML
