_# Pattern: Differential Privacy for ML

## 1. Pattern Name and Number

**A102: Differential Privacy for ML**

## 2. Problem

Machine learning models are trained on large datasets, and they can inadvertently memorize and leak sensitive information from their training data. An attacker could potentially query a trained model and infer whether a specific individual's data was used in the training set, or even reconstruct parts of the training data itself. This is a major privacy risk, especially when training on sensitive data like medical records or financial information.

## 3. Context

You are training a machine learning model on a dataset that contains sensitive personal information. You need a strong, mathematically rigorous guarantee that the model will not leak information about any individual in the training data.

## 4. Solution

**Use Differential Privacy, a formal mathematical framework for quantifying the privacy leakage of an algorithm.** In the context of machine learning, this is typically achieved by injecting carefully calibrated random noise into the training process. A common technique is **Differentially Private Stochastic Gradient Descent (DP-SGD)**.

In DP-SGD, two main changes are made to the standard training process:
1.  **Gradient Clipping**: The gradient for each individual training example is clipped to a maximum norm. This limits the influence of any single data point on the model update.
2.  **Noise Injection**: Random noise (typically Gaussian noise) is added to the clipped gradients before they are aggregated and used to update the model.

The amount of noise added is controlled by a **privacy budget (epsilon, ε)**. A smaller epsilon provides a stronger privacy guarantee but also adds more noise, which can hurt the model's accuracy. This creates a direct and quantifiable trade-off between privacy and utility.

## 5. Rationale

Differential Privacy provides a strong, provable guarantee of privacy. It:
- **Is a Rigorous Definition**: It is a mathematical definition of privacy, not just a heuristic.
- **Protects Against a Wide Range of Attacks**: It protects against any attack that tries to infer information about individuals in the training data by observing the model's output.
- **Provides a Quantifiable Trade-off**: It allows you to explicitly reason about and tune the trade-off between privacy and accuracy.

## 6. Consequences

- **Positive**:
    - A strong, mathematically rigorous privacy guarantee for your machine learning model.
- **Negative**:
    - **Loss of Accuracy**: The noise added to the training process will almost always reduce the accuracy of the final model.
    - **Computationally Expensive**: Can add significant computational overhead to the training process.
    - **Hyperparameter Tuning**: Requires careful tuning of the privacy budget (epsilon) and other hyperparameters to find the right balance between privacy and utility.

## 7. Known Uses

- **Google**: Uses differentially private training for some of its AI models.
- **Apple**: Uses differential privacy to collect user data for analytics in a privacy-preserving way.
- **US Census Bureau**: Used differential privacy to protect the privacy of individuals in the 2020 Census data release.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 5           | A visionary technology for building truly privacy-preserving AI.                                      |
| **2. Governance**       | 5           | A powerful and provable governance control for managing data privacy risk in AI.                      |
| **3. Economy**          | 3           | The trade-off with accuracy can make it economically challenging to adopt in some use cases.          |
| **4. Technology**       | 4           | A cutting-edge technology that is the gold standard for privacy-preserving analytics and ML.          |
| **5. Operations**       | 3           | Adds significant complexity and computational cost to the model training process.                     |
| **6. Culture**          | 5           | Promotes a culture of rigorous, provable privacy engineering.                                         |
| **7. Resilience**       | 5           | Builds strong legal and social resilience by providing a provable guarantee of privacy.               |
| **Overall Score**       | **4.3**     | The gold standard for privacy-preserving machine learning, but it comes with a cost in terms of accuracy and complexity. |
