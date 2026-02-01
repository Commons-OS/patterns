_# Pattern: Split Learning

## 1. Pattern Name and Number

**A108: Split Learning**

## 2. Problem

Federated Learning (P009) is a powerful privacy-preserving technique, but it requires clients (e.g., mobile devices) to have enough computational power to train a full AI model locally. For many resource-constrained devices, this is not feasible. Additionally, it requires significant communication and coordination between clients, which can be complex.

## 3. Context

You want to train a model on data that is distributed across multiple clients, but the clients are resource-constrained (e.g., simple IoT devices, older mobile phones) and cannot perform the full model training on their own. You need a way to split the computational load between the clients and a central server while still preserving the privacy of the raw data.

## 4. Solution

**Implement Split Learning (or SplitNN), a collaborative deep learning technique where the model is split into multiple sections.** A portion of the model is run on the client device, and the rest is run on a central server.

The process for a single client works as follows:
1.  **Client-Side Computation**: The client device runs the first few layers of the neural network on its local data. This produces an intermediate output called the "smashed data" or "activations."
2.  **Communication**: The client sends this small tensor of smashed data to the server. The raw data never leaves the device.
3.  **Server-Side Computation**: The server takes the smashed data and feeds it into the remaining layers of the model to produce the final output and calculate the loss.
4.  **Backpropagation**: The server computes the gradients and sends the gradients corresponding to the client-side layers back to the client. The client then updates its local model layers.

This process can be extended to multiple clients, who take turns training the model with the server.

## 5. Rationale

Split Learning offers a different trade-off between privacy, computation, and communication compared to Federated Learning. It:
- **Reduces Client-Side Computation**: The majority of the computational work is offloaded to the powerful central server, making it suitable for resource-constrained clients.
- **Preserves Raw Data Privacy**: The raw data never leaves the client device.
- **Simplifies Client-Side Logic**: The client only needs to manage a small part of the model.

## 6. Consequences

- **Positive**:
    - Enables collaborative learning with simple, low-power devices.
    - Provides a strong guarantee that raw data never leaves the client.
    - Can be faster than Federated Learning in some scenarios due to less client-side computation.
- **Negative**:
    - **Privacy of Smashed Data**: It may be possible for the server to reconstruct the original raw data from the intermediate "smashed data," especially for the layers close to the input. It does not offer the same level of formal privacy guarantee as techniques like Differential Privacy.
    - **Sequential Training**: In its basic form, clients train the model sequentially with the server, which can be slow.
    - **High Communication**: Requires frequent communication between the client and server for each training batch.

## 7. Known Uses

- **Healthcare**: Being explored as a way for hospitals with limited computational resources to collaborate on training models without sharing patient data.
- **IoT**: Suitable for training models on data from simple sensors and IoT devices.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of enabling AI on a wider range of devices while considering privacy.          |
| **2. Governance**       | 3           | A governance model for collaborative learning, but with weaker privacy guarantees than federated learning. |
| **3. Economy**          | 4           | Unlocks the value of data held on resource-constrained devices.                                       |
| **4. Technology**       | 4           | An important and practical technique in the privacy-preserving machine learning landscape.            |
| **5. Operations**       | 3           | Requires careful management of the client-server interaction.                                         |
| **6. Culture**          | 4           | Promotes a culture of finding practical solutions for privacy-preserving AI.                          |
| **7. Resilience**       | 3           | Builds resilience by enabling intelligence on edge devices.                                           |
| **Overall Score**       | **3.6**     | A valuable and practical pattern for collaborative learning with resource-constrained clients, but its privacy guarantees must be carefully evaluated. |
