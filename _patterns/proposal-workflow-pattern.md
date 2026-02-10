---
id: pat_proposal_workflow_pattern
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/proposal-workflow-pattern.md
slug: proposal-workflow-pattern
title: Proposal Workflow Pattern
aliases:
- RFC Pattern
- Decision Proposal Process
version: "1.0"
created: "2026-02-10 00:00:00+00:00"
modified: "2026-02-10 00:00:00+00:00"
classification:
  universality: context-dependent
  domain: platform
  category:
  - integration
  era:
  - digital
  - cognitive
  origin:
  - software-engineering
  - platform-design
  status: draft
  commons_alignment: 3
  commons_domain:
  - platform
generalizes_from: []
specializes_to: []
enables: []
requires: []
related:
- liquid-democracy-pattern
- polycentric-governance-pattern
contributors:
- Manus AI
- cloudsters
sources:
- https://commons.engineering
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
_**Pattern Name**_: Proposal Workflow Pattern

_**Use Case**_: When a user wants to create a proposal, get feedback, and then submit it for approval.

_**Description**_:

This pattern orchestrates a multi-step proposal process. It begins with the user drafting a proposal. Once the initial draft is ready, the system facilitates a feedback loop where stakeholders can review and provide comments. After incorporating feedback, the user can finalize the proposal and submit it for formal approval. The system then tracks the approval status and notifies the user of the outcome.

_**Workflow**_:

1.  **Draft Proposal**: The user creates the initial version of the proposal.
2.  **Feedback Loop**: The proposal is shared with designated reviewers for feedback.
3.  **Incorporate Feedback**: The user revises the proposal based on the feedback received.
4.  **Final Submission**: The user submits the finalized proposal for approval.
5.  **Approval Tracking**: The system monitors the approval process and provides status updates.
6.  **Notification**: The user is notified of the final approval or rejection.

_**Examples**_:

*   A project manager drafting a project proposal and sharing it with team leads for feedback before submitting it to the steering committee.
*   A sales team creating a sales proposal, getting it reviewed by legal and finance, and then sending it to the client.
*   A student writing a thesis proposal, getting feedback from their advisor, and then submitting it to the university for approval.
