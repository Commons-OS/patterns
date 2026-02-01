_# Pattern: Private Information Retrieval

## 1. Pattern Name and Number

**P021: Private Information Retrieval (PIR)**

## 2. Problem

When you query a database, the server hosting the database learns what you are looking for. This can be a major privacy violation. For example, if you query a medical database for information about a specific disease, the server learns of your interest in that disease. If you query a patent database for a specific invention, the server learns about your company's research interests.

## 3. Context

You need to allow a client to retrieve an item from a database on a server without the server learning which item the client is retrieving. The database itself is public, but the client's query is private.

## 4. Solution

**Use a Private Information Retrieval (PIR) protocol. PIR is a cryptographic protocol that allows a user to retrieve an item from a server in possession of a database without revealing which item is retrieved.**

PIR protocols work by having the client send a query that is structured in such a way that it touches every single item in the database. The server processes this query and returns a response, also structured in a way that the client can decode to get the specific item they want. From the server's perspective, the query looks the same regardless of which item the client is interested in, because it has to read its entire database to answer it.

## 5. Rationale

PIR provides a strong, cryptographic guarantee of query privacy. It:
- **Protects Query Privacy**: Ensures that the server learns nothing about the client's interests.
- **Decouples Access from Interest**: Allows users to access public information without revealing their intentions.

## 6. Consequences

- **Positive**:
    - The strongest possible guarantee of query privacy.
    - Enables private access to public or semi-public databases.
- **Negative**:
    - **Extreme Performance Overhead**: The major drawback of PIR is that it requires the server to process its entire database for every single query. This makes it computationally infeasible for all but the smallest databases.
    - **High Communication Cost**: PIR protocols can also have high communication overhead.
    - **Complexity**: These are complex cryptographic protocols.

## 7. Known Uses

PIR is mostly a subject of academic research, but it has some niche applications:
- **Password Breach Checking**: Some systems use PIR-like techniques to allow users to check if their password was in a data breach without revealing the password to the server.
- **Private Contact Discovery**: Used in some messaging apps to discover which of a user's contacts are also on the app, without revealing the user's entire contact list to the server.

## 8. Commons OS Assessment

| Pillar                | Score (1-5) | Rationale                                                                                             |
| --------------------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| **1. Purpose & Vision**   | 4           | Aligns with the vision of a world where information can be accessed without surveillance.             |
| **2. Governance**       | 3           | A powerful but highly specialized technical governance control.                                       |
| **3. Economy**          | 2           | The high performance cost severely limits its economic viability for most applications.               |
| **4. Technology**       | 3           | A cutting-edge but still largely impractical cryptographic technology for general use.                |
| **5. Operations**       | 2           | Operationally infeasible for large databases.                                                         |
| **6. Culture**          | 4           | Promotes a strong culture of privacy and freedom of inquiry.                                          |
| **7. Resilience**       | 3           | Builds resilience against surveillance and inference attacks based on query patterns.                 |
| **Overall Score**       | **3.0**     | A theoretically powerful but currently impractical pattern for most real-world systems due to its performance cost. |
