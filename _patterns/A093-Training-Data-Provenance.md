_# Pattern: Training Data Provenance

## 1. Pattern Name and Number

**A093: Training Data Provenance**

## 2. Problem

An AI model is a direct reflection of the data it was trained on. If the training data is biased, inaccurate, poisoned, or has licensing issues, the resulting model will be flawed, untrustworthy, and could create significant legal and ethical risks. Without a clear record of where the training data came from and how it was processed, it is impossible to debug model behavior, audit for bias, or ensure legal compliance.

## 3. Context

You are developing an AI model for a value creation system. You need to ensure the integrity, quality, and legality of the data used to train the model, and you must be able to demonstrate this to auditors, regulators, and users.

## 4. Solution

**Maintain a detailed, immutable record of the origin, lineage, and transformation history of all data used to train an AI model.** This is often referred to as data provenance or data lineage.

Key information to track for training data provenance:
- **Data Source**: Where did the data originate? (e.g., a specific public dataset, an internal database, a third-party provider).
- **Licensing and Rights**: What are the legal terms of use for the data? Are there any restrictions on its use for training commercial models?
- **Version Control**: Just like code, data changes over time. Use a data version control system (e.g., DVC) to track every version of the dataset used for training.
- **Transformation History**: Log every preprocessing step applied to the data (e.g., cleaning, normalization, feature engineering), including the code used to perform the transformation.
- **Data Hash**: Compute a cryptographic hash of the final training dataset to ensure its integrity and detect any tampering.

## 5. Rationale

Training data provenance is a prerequisite for trustworthy AI. It:
- **Enables Reproducibility**: Allows you to perfectly recreate the dataset used to train any given model version.
- **Facilitates Debugging**: When a model behaves unexpectedly, you can trace its behavior back to the specific data points that may have caused the issue.
- **Supports Auditing and Compliance**: Provides the evidence needed to demonstrate compliance with data protection regulations and to audit for issues like bias.
- **Manages Legal Risk**: Ensures that you have the legal right to use the data for training, avoiding copyright and licensing disputes.

## 6. Consequences

- **Positive**:
    - Greatly increased trust, transparency, and accountability of AI models.
    - Essential for debugging and understanding model behavior.
    - Reduces legal and compliance risks.
- **Negative**:
    - Requires specialized tools for data versioning and lineage tracking.
    - Adds process and overhead to the data preparation workflow.
    - Can be challenging to implement for complex data pipelines involving many sources and transformations.

## 7. Known Uses

- **Data Version Control (DVC)**: An open-source tool that brings version control to data science projects, allowing you to version datasets and models.
- **Pachyderm**: A data science platform built on Kubernetes that provides data versioning and lineage for complex pipelines.
- **MLflow**: The MLflow platform tracks the dataset version used for each model training run.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | Aligns with the vision of creating transparent, accountable, and trustworthy AI systems.              |
| **2. Governance**       | 5           | A cornerstone of data and AI governance.                                                              |
| **3. Economy**          | 4           | Reduces the significant economic risk of deploying biased, illegal, or unreliable models.             |
| **4. Technology**       | 4           | Relies on specific technologies for data versioning and lineage tracking.                             |
| **5. Operations**       | 4           | Requires integrating data provenance tracking into the MLOps workflow.                                |
| **6. Culture**          | 5           | Fosters a culture where data quality and integrity are treated as first-class citizens.               |
| **7. Resilience**       | 4           | Builds resilience by allowing you to trace and mitigate issues originating from the training data.    |
| **Overall Score**       | **4.4**     | A foundational pattern for building trustworthy and governable AI.                                     |
