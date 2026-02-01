_# Pattern: Portable Data Formats

## 1. Pattern Name and Number

**S068: Portable Data Formats**

## 2. Problem

Data is often stored in proprietary, vendor-specific formats. When you want to move your data to a different application or service, you have to go through a complex, costly, and often lossy data conversion process. This creates vendor lock-in and makes it difficult to use your own data with the tools of your choice. Your data is trapped.

## 3. Context

You are designing a system that creates, stores, or processes data. You want to ensure that this data can be easily moved, shared, and used by other systems in the future, maximizing its value and ensuring your own freedom of choice.

## 4. Solution

**Adopt a policy of using Portable Data Formats, which are open, standardized, and widely supported, for all data storage and exchange.** Instead of using a proprietary binary format or a vendor-specific database schema, use formats like:

- **JSON (JavaScript Object Notation)**: For structured data.
- **CSV (Comma-Separated Values)**: For tabular data.
- **Parquet or ORC**: For columnar, analytical data.
- **XML (eXtensible Markup Language)**: For semi-structured data.
- **PDF/A**: For long-term archival of documents.

This principle should apply not just to data exports, but to the primary way data is stored and managed within the system whenever possible.

## 5. Rationale

Using portable data formats is a simple but powerful way to prevent data lock-in. It:
- **Ensures Interoperability**: Data can be easily read and understood by a wide range of different tools and applications.
- **Maximizes Data Value**: Allows data to be easily combined, analyzed, and used in new and innovative ways.
- **Future-Proofs Your Data**: Ensures that your data will remain accessible and usable for years to come, even as technologies change.
- **Supports Data Portability**: It is a technical prerequisite for implementing a Data Portability (P013) feature.

## 6. Consequences

- **Positive**:
    - Freedom from data lock-in.
    - Increased interoperability and data value.
    - A more resilient and future-proof data architecture.
- **Negative**:
    - **Performance**: Open formats may not always be as performant as highly optimized, proprietary binary formats for very specific use cases.
    - **Feature Support**: A proprietary format may have specific features that are not available in any open standard.

## 7. Known Uses

- **The entire modern web and API economy** is built on open data formats like JSON.
- **Data Warehousing and Big Data**: Columnar formats like Parquet and ORC are the industry standard for efficient analytical queries.
- **Government Open Data Initiatives**: Mandate the use of open, machine-readable formats for all published public data.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of a fluid and interoperable data ecosystem.                                   |
| **2. Governance**       | 4           | A key governance principle for data management and interoperability.                                  |
| **3. Economy**          | 5           | Maximizes the economic value of data by making it interoperable and preventing lock-in.               |
| **4. Technology**       | 5           | A fundamental principle of modern data architecture.                                                  |
| **5. Operations**       | 4           | Simplifies data integration and migration operations.                                                 |
| **6. Culture**          | 4           | Fosters a culture of openness and interoperability.                                                   |
| **7. Resilience**       | 5           | Builds strong resilience by ensuring that data is not tied to the fate of a single vendor or technology. |
| **Overall Score**       | **4.4**     | A simple, powerful, and foundational pattern for data sovereignty and interoperability.                |
