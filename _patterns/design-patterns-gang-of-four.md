---
id: pat_01kg5023ycep88v76yxhd37x6q
page_url: https://commons-os.github.io/patterns/design-patterns-gang-of-four/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/design-patterns-gang-of-four.md
slug: design-patterns-gang-of-four
title: Design Patterns (Gang of Four)
aliases: []
version: 1.0
created: 2026-01-28T00:00:00Z
modified: 2026-01-28T00:00:00Z
tags:
  universality: domain
  domain: design
  category: [meta-pattern]
  era: [digital]
  origin: []
  status: draft
  commons_alignment: 3
commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []
contributors: [higgerix, cloudsters]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---

## 1. Overview

"Design Patterns: Elements of Reusable Object-Oriented Software" is a seminal book in the field of software engineering, authored by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, who are collectively known as the "Gang of Four" (GoF). Published in 1994, the book introduces 23 software design patterns that provide solutions to common problems in object-oriented software design. These patterns are not specific algorithms or code, but rather high-level descriptions of how to solve a recurring design problem in a particular context. The book is a cornerstone of object-oriented design and has had a profound impact on the way software is designed and built.

The patterns in the book are categorized into three main types: creational, structural, and behavioral. Creational patterns are concerned with the process of object creation, providing flexibility in how objects are instantiated. Structural patterns deal with the composition of classes and objects to form larger structures. Behavioral patterns focus on the interaction and communication between objects, promoting loose coupling and flexibility.

The book's primary goal is to help developers create more flexible, elegant, and reusable designs. By providing a common vocabulary and a set of proven solutions, the Gang of Four's work enables developers to communicate more effectively about design problems and to build more robust and maintainable software. The patterns are language-agnostic, although the examples in the book are primarily in C++ and Smalltalk. The principles and patterns described in the book, however, are applicable to a wide range of object-oriented programming languages and have been widely adopted in the software development community.

## 2. Core Principles

The Gang of Four's design patterns are built upon a set of fundamental principles of object-oriented design. These principles are not patterns themselves, but rather foundational concepts that guide the design of flexible and reusable software. Two of the most important principles emphasized in the book are:

*   **Program to an interface, not an implementation:** This principle suggests that we should depend on abstractions (interfaces or abstract classes) rather than concrete implementations. By programming to an interface, we decouple our code from specific implementations, making it easier to swap out different implementations in the future without affecting the client code. This promotes flexibility and reduces the impact of changes.

*   **Favor object composition over class inheritance:** While inheritance is a powerful mechanism for code reuse, the Gang of Four cautions against its overuse. They argue that inheritance can lead to tight coupling between parent and child classes, making the system more rigid and difficult to change. Object composition, on the other hand, allows for more flexible and dynamic relationships between objects. By composing objects, we can achieve greater flexibility and build more modular and maintainable systems.

In addition to these two core principles, the book categorizes the 23 design patterns into three distinct groups, each addressing a different aspect of software design:

*   **Creational Patterns:** These patterns abstract the instantiation process, making the system independent of how its objects are created. They provide mechanisms for creating objects in a controlled and flexible manner. The five creational patterns are: Abstract Factory, Builder, Factory Method, Prototype, and Singleton.

*   **Structural Patterns:** These patterns deal with the composition of classes and objects to form larger structures. They help in organizing classes and objects into larger structures, making the system more robust and easier to maintain. The seven structural patterns are: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, and Proxy.

*   **Behavioral Patterns:** These patterns are concerned with the algorithms and the assignment of responsibilities among objects. They describe how objects communicate and interact with each other to accomplish a task. The eleven behavioral patterns are: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, and Visitor.

## 3. Key Practices

The 23 design patterns presented by the Gang of Four are categorized into three types: creational, structural, and behavioral. Each pattern represents a proven solution to a recurring design problem, and understanding these patterns is a key practice for any object-oriented designer or developer.

### Creational Patterns

Creational patterns provide ways to create objects while hiding the creation logic, rather than instantiating objects directly using the `new` operator. This gives the program more flexibility in deciding which objects need to be created for a given use case.

*   **Abstract Factory:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
*   **Builder:** Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
*   **Factory Method:** Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
*   **Prototype:** Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.
*   **Singleton:** Ensures a class only has one instance, and provides a global point of access to it.

### Structural Patterns

Structural patterns explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.

*   **Adapter:** Allows objects with incompatible interfaces to collaborate.
*   **Bridge:** Decouples an abstraction from its implementation so that the two can vary independently.
*   **Composite:** Composes objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
*   **Decorator:** Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
*   **Facade:** Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
*   **Flyweight:** Uses sharing to support large numbers of fine-grained objects efficiently.
*   **Proxy:** Provides a surrogate or placeholder for another object to control access to it.

### Behavioral Patterns

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects.

*   **Chain of Responsibility:** Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. The receiving objects are chained and the request is passed along the chain until an object handles it.
*   **Command:** Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
*   **Interpreter:** Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
*   **Iterator:** Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
*   **Mediator:** Defines an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
*   **Memento:** Without violating encapsulation, captures and externalizes an object's internal state so that the object can be restored to this state later.
*   **Observer:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
*   **State:** Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.
*   **Strategy:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
*   **Template Method:** Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
*   **Visitor:** Represents an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

## 4. Application Context

The design patterns presented by the Gang of Four are applicable in a wide variety of contexts within object-oriented software development. They are not tied to any specific programming language or domain, making them a versatile tool for software architects and developers. The patterns are most valuable in the design of large, complex systems where flexibility, reusability, and maintainability are critical concerns.

For example, creational patterns are particularly useful in situations where the exact type of object to be created is not known at compile time, or where the creation process is complex and needs to be decoupled from the client code. Structural patterns are essential for building complex object structures and for integrating disparate components into a cohesive system. Behavioral patterns are crucial for managing the interactions between objects, promoting loose coupling and making the system easier to understand and modify.

The Gang of Four's patterns are particularly relevant in the development of frameworks and libraries, where the goal is to provide a reusable and extensible set of components for other developers to use. They are also widely used in the design of graphical user interfaces (GUIs), where the separation of concerns between the model, view, and controller is a key design principle. In general, any software system that is expected to evolve and adapt over time can benefit from the application of these design patterns.

## 5. Implementation

Implementing the Gang of Four design patterns involves more than just copying and pasting code. It requires a deep understanding of the problem at hand and the context in which the pattern is to be applied. The patterns are not concrete solutions, but rather templates that can be adapted and customized to fit the specific needs of a project. The implementation of a design pattern typically involves the following steps:

1.  **Identify the problem:** The first step is to recognize that a recurring design problem exists. This requires experience and a good understanding of object-oriented design principles.
2.  **Select the appropriate pattern:** Once the problem is identified, the next step is to select the design pattern that best addresses the problem. This involves understanding the intent, motivation, and applicability of each pattern.
3.  **Adapt the pattern to the specific context:** The selected pattern needs to be adapted to the specific context of the project. This may involve renaming the classes and methods of the pattern to match the domain of the application, and it may also involve modifying the structure of the pattern to fit the specific requirements of the problem.
4.  **Implement the pattern in code:** The final step is to implement the pattern in the chosen programming language. This involves writing the code for the classes and interfaces that make up the pattern, and then integrating the pattern into the rest of the application.

It is important to remember that design patterns are not a silver bullet. They should be used judiciously and only when they provide a clear benefit. Overuse of design patterns can lead to overly complex and convoluted code that is difficult to understand and maintain. The goal is to use design patterns to create clean, simple, and elegant designs that are easy to understand and evolve over time.

## 6. Evidence & Impact

The impact of "Design Patterns: Elements of Reusable Object-Oriented Software" on the field of software engineering has been profound and long-lasting. Since its publication in 1994, the book has sold over 500,000 copies and has been translated into 13 languages, making it one of the most influential books in the history of computer science. The 23 design patterns presented in the book have become a fundamental part of the vocabulary of object-oriented designers and developers, and they are widely taught in university computer science programs and professional training courses.

The book's primary impact has been to provide a common language and a set of proven solutions for common design problems. This has enabled developers to communicate more effectively about design, and it has helped to raise the level of abstraction in software design. The patterns have been instrumental in the development of countless software systems, from small applications to large-scale enterprise systems. The influence of the Gang of Four's work can be seen in the design of many popular software frameworks and libraries, including the Java standard library, the C++ Standard Template Library (STL), and the Microsoft .NET Framework.

In 2005, the authors of the book were awarded the prestigious ACM SIGPLAN Programming Languages Achievement Award in recognition of the impact of their work on programming practice and programming language design. While the book has been criticized by some for promoting a 
pattern-heavy" approach to design that can lead to over-engineering, its overall impact on the software industry has been overwhelmingly positive. The book has helped to establish a culture of design excellence and has provided a foundation for the development of more robust, flexible, and maintainable software.

## 7. Cognitive Era Considerations

While the Gang of Four's design patterns were conceived in the digital era, their underlying principles of abstraction, composition, and loose coupling remain highly relevant in the cognitive era of artificial intelligence and machine learning. However, the application of these patterns in the context of AI-driven systems requires some reinterpretation and adaptation. The cognitive era is characterized by systems that can learn, adapt, and evolve, and the design patterns used to build these systems must reflect this new reality.

Many of the classic design patterns can be applied to the development of AI and machine learning systems. For example, the **Strategy pattern** can be used to encapsulate different machine learning algorithms, allowing a system to dynamically switch between algorithms based on the context or the data. The **Observer pattern** can be used to notify different components of an AI system when new data becomes available or when a model has been updated. The **Decorator pattern** can be used to add new functionalities to an AI model, such as explainability or bias detection, without modifying the core model itself.

Furthermore, the cognitive era is giving rise to new design patterns that are specific to the development of AI and machine learning systems. These patterns address challenges such as data management, model training and deployment, and the integration of AI components into larger systems. For example, patterns like the **Model-View-Controller (MVC) for ML systems** are emerging to provide a structured way to organize the different components of a machine learning application. As the field of AI continues to mature, we can expect to see the emergence of a new generation of design patterns that will provide a common language and a set of best practices for building intelligent systems.

## 8. Commons Alignment Assessment

The Gang of Four's Design Patterns, while originating from the world of proprietary software development, exhibit a surprising degree of alignment with the principles of a commons-based approach to creating and sharing knowledge. This alignment stems from the patterns' emphasis on reusability, modularity, and the creation of a shared vocabulary, all of which are essential for building and sustaining a knowledge commons.

**1. Shared Purpose & Values:** The Design Patterns themselves embody a shared purpose: to create a common language and a set of best practices for object-oriented design. This shared purpose fosters a sense of community among developers and promotes the creation of more robust and maintainable software. The values embedded in the patterns, such as flexibility, reusability, and elegance, are also consistent with the values of a commons-based approach.

**2. Collective Governance:** While the original set of 23 patterns was defined by the Gang of Four, the patterns have since been the subject of extensive discussion, debate, and refinement by the software development community. This ongoing dialogue and collective sense-making process can be seen as a form of informal collective governance, where the community collectively decides which patterns are most useful and how they should be applied.

**3. Fair & Equitable Distribution:** The Design Patterns are a form of knowledge that is freely available to anyone who wishes to learn and use them. The book itself is widely available, and there are countless free online resources that explain and illustrate the patterns. This open access to knowledge promotes a fair and equitable distribution of the benefits of good software design.

**4. Open & Transparent:** The patterns are, by their very nature, open and transparent. They are well-documented and their structure and intent are clearly explained. This transparency makes it easier for developers to understand and apply the patterns, and it also facilitates the process of peer review and collective improvement.

**5. Modular & Forkable:** The patterns are inherently modular, as they are designed to be combined and adapted to solve a wide variety of design problems. This modularity makes it easy to "fork" and adapt the patterns to new contexts and new programming languages. The history of design patterns is replete with examples of new patterns being created by adapting and extending the original Gang of Four patterns.

**6. Federated & Interoperable:** The Design Patterns promote interoperability by providing a common design vocabulary that can be used across different projects, teams, and organizations. This shared language makes it easier for different software components to interoperate, and it also facilitates the creation of federated systems that are composed of multiple, independently developed components.

**7. Polycentric & Decentralized:** The use of Design Patterns is a decentralized and polycentric practice. There is no central authority that dictates how the patterns should be used. Instead, the patterns are adopted and adapted by individual developers and teams based on their own needs and circumstances. This decentralized approach to design fosters innovation and creativity, and it allows the patterns to evolve and adapt over time.

Overall, the Gang of Four's Design Patterns provide a powerful example of how a set of well-defined, modular, and reusable knowledge artifacts can contribute to the creation of a vibrant and sustainable knowledge commons. While the patterns themselves are not a commons, they are a critical enabling technology for building and sharing knowledge in a collaborative and decentralized manner.

## 9. Resources & References

*   Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design patterns: elements of reusable object-oriented software*. Addison-Wesley.
*   [Wikipedia: Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
*   [DigitalOcean: Gang of 4 Design Patterns Explained](https://www.digitalocean.com/community/tutorials/gangs-of-four-gof-design-patterns)
*   [GeeksforGeeks: Gang of Four (GOF) Design Patterns](https://www.geeksforgeeks.org/gang-of-four-gof-design-patterns/)
*   [Martin Fowler: Gang of Four](https://martinfowler.com/bliki/GangOfFour.html)

---

## Navigation

- **Page URL**: [https://commons-os.github.io/patterns/domain/design-patterns-gang-of-four/](https://commons-os.github.io/patterns/domain/design-patterns-gang-of-four/)
- **Source**: [View on GitHub](https://github.com/commons-os/patterns/blob/main/_patterns/design-patterns-gang-of-four.md)
- **Edit**: [Edit this pattern](https://github.com/commons-os/patterns/edit/main/_domain/design-patterns-gang-of-four.md)

---

*Commons OS Pattern Library - Distributed by [cloudsters](https://cloudsters.net)*
