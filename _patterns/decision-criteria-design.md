---
# ═══════════════════════════════════════════════════════════════════
# GROUP 1: CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════
id: pat_01khvcxdy2e5xa6kp3fwsctwkc
slug: decision-criteria-design
title: "Decision Criteria Design"
aliases: []
summary: >-
  Good decisions require good criteria, established before the options
  are evaluated — not reverse-engineered after the preferred answer is
  already clear. This pattern covers how to design decision criteria:
  identifying the dimensions that genuinely matter, weighting them
  appropriately, making them explicit before gathering information,
  and using them to prevent motivated reasoning from corrupting the
  evaluation.

# ═══════════════════════════════════════════════════════════════════
# GROUP 2: CONTEXTUAL TRANSLATION (The Navigator Engine)
# ═══════════════════════════════════════════════════════════════════
context_labels:
  corporate: "Strategic Decision-Making Process"
  government: "Public Policy Deliberation"
  activist: "Collective Decision Protocol"
  tech: "Product Decision Framework"

# ═══════════════════════════════════════════════════════════════════
# GROUP 3: ONTOLOGY & SEARCH OPTIMIZATION (The RAG Fuel)
# ═══════════════════════════════════════════════════════════════════
ontology:
  domain: decision-making
  cross_domains: []
  commons_domain:
    - life
  search_hints:
    primary_tension: "Decisiveness vs. Deliberation"
    vector_keywords: ["decision", "criteria", "design", "good", "decisions"]
  commons_assessment:
    stakeholder_architecture: 3.0
    value_creation: 3.5
    resilience: 3.0
    ownership: 4.0
    autonomy: 4.0
    composability: 3.0
    fractal_value: 4.0
    vitality: 3.5
    vitality_reasoning: >-
      This pattern sustains vitality by maintaining and renewing the
      system's existing health. 'Decision Criteria Design' contributes
      to ongoing functioning without necessarily generating new adaptive
      capacity. Watch for signs of rigidity if implementation becomes
      routinised.
    overall_score: 3.5

# ═══════════════════════════════════════════════════════════════════
# GROUP 4: LIFECYCLE & CONFIDENCE
# ═══════════════════════════════════════════════════════════════════
lifecycle:
  usage_stage: design
  adoption_stage: growth
  status: draft
  version: 0.1
  confidence: 1

# ═══════════════════════════════════════════════════════════════════
# GROUP 5: HARD RELATIONSHIPS (Human-Curated Graph)
# ═══════════════════════════════════════════════════════════════════
relationships:
  generalizes_from: []
  specializes_to:
    - slug: advance-directive-design
      weight: 0.82
    - slug: adventure-design-methodology
      weight: 0.71
  enables:
    - slug: acting-despite-irreducible-uncertainty
      weight: 0.85
    - slug: adaptive-facilitation
      weight: 0.72
  requires: []
  alternatives: []
  complementary:
    - slug: adaptive-strategy-under-uncertainty
      weight: 0.9
    - slug: adaptive-action-in-complex-systems
      weight: 0.85
    - slug: active-listening-depth
      weight: 0.75
    - slug: accountability-without-shame
      weight: 0.73
  tools: []
# ═══════════════════════════════════════════════════════════════════
# GROUP 6: GRAPH GARDEN (Machine-Written Graph)
# ═══════════════════════════════════════════════════════════════════
graph_garden:
  last_pruned: 2026-02-19
  entities:
    - id: decision-criteria
      type: concept
      label: "Decision Criteria"
      relevance: 1.0
    - id: ex-ante-design
      type: practice
      label: "Ex-Ante Criteria Design"
      relevance: 0.95
    - id: bias-prevention
      type: concept
      label: "Bias Prevention in Decision-Making"
      relevance: 0.85
    - id: weighting-systems
      type: tool
      label: "Criteria Weighting Systems"
      relevance: 0.9
    - id: values-alignment
      type: concept
      label: "Values Alignment"
      relevance: 0.8
    - id: dimensional-analysis
      type: practice
      label: "Multi-Dimensional Analysis"
      relevance: 0.85
    - id: sensemaking
      type: concept
      label: "Sensemaking and Analysis"
      relevance: 0.75
  communities:
    - id: decision-making-and-strategy
      label: "Decision-Making and Strategy"
      source: inferred
      confidence: 0.95
    - id: systems-thinking
      label: "Systems Thinking and Adaptive Action"
      source: inferred
      confidence: 0.8
    - id: values-and-meaning
      label: "Values, Meaning, and Life Design"
      source: inferred
      confidence: 0.75
  inferred_links:
    - target: adaptive-strategy-under-uncertainty
      type: complementary
      confidence: 0.9
      reason: "Both establish frameworks before implementation to avoid bias."
    - target: adaptive-action-in-complex-systems
      type: complementary
      confidence: 0.85
      reason: "Both require clear criteria for analysis and response phases."
    - target: acting-despite-irreducible-uncertainty
      type: enables
      confidence: 0.85
      reason: "Good criteria design enables decisive action despite uncertainty."
    - target: advance-directive-design
      type: specializes_to
      confidence: 0.82
      reason: "Applies decision criteria design to personal medical/financial decisions."
    - target: active-listening-depth
      type: complementary
      confidence: 0.75
      reason: "Listening for values and needs informs criteria identification."
    - target: accountability-without-shame
      type: complementary
      confidence: 0.73
      reason: "Clear criteria enable accountability measurement without judgment."
    - target: adaptive-facilitation
      type: enables
      confidence: 0.72
      reason: "Clear criteria help facilitators make real-time adaptation choices."
    - target: adventure-design-methodology
      type: specializes_to
      confidence: 0.71
      reason: "Uses decision criteria for clarity about risk, motivation, design."
# ═══════════════════════════════════════════════════════════════════
# GROUP 7: PROVENANCE
# ═══════════════════════════════════════════════════════════════════
contributors: ["higgerix", "cloudsters"]
sources:
  - "Decision Theory / Rational Choice"
license: CC-BY-SA-4.0
attribution: "commons.engineering by cloudsters, https://cloudsters.net"
---

Good decisions require good criteria, established before the options are evaluated — not reverse-engineered after the preferred answer is already clear.

> [!NOTE] Confidence Rating: ★★★ (Established)
> This pattern draws on Decision Theory / Rational Choice.

---

### Section 1: Context

Most organizations, movements, and teams make decisions in a state of ambiguity: the stakes are real, the information is incomplete, and the pressures to decide are immediate. In corporate strategy rooms, leaders face competing visions of market position without clear ways to weight shareholder value against employee resilience or ecosystem health. In government policy work, competing constituencies pull in opposite directions—efficiency, equity, sustainability—with no explicit common language for trade-offs. Activist collectives struggle between urgency and inclusion; tech teams between speed and durability. The system fragments because each stakeholder carries different unstated priorities into the room. When criteria are not designed upfront, the decision-making process becomes a proxy battle where hidden preferences shape what "seems obvious" after the fact. What looks like deliberation becomes motivated reasoning dressed up as rigor. The system grows brittle because nobody trusts the outcomes—they feel rigged, not reasoned.

---

### Section 2: Problem

> **The core conflict is Decisiveness vs. Deliberation.**

Speed demands closure: *We must decide now, or the opportunity passes.* Deliberation demands depth: *We must understand what truly matters before we choose.* 

When decisiveness dominates, criteria get skipped. Leaders rely on intuition, prior commitments, or the loudest voice. Decisions feel fast but lack legitimacy; stakeholders sense they were already made before the meeting began. When deliberation dominates without criteria, groups get lost in endless discussion. Every option spawns new dimensions to consider. Motivated reasoning creeps in—people unconsciously redefine what matters to justify their preferred outcome. The group fragments into camps, each using different (unstated) criteria to evaluate the same options. Decisions take months and still lack consent. What breaks is trust in the process itself. Stakeholders learn to game the system rather than engage it. In corporate contexts, this produces siloed strategies that don't hold when conditions shift. In government, it breeds policy incoherence and public distrust. In activist spaces, it corrodes solidarity. In tech, it leads to feature bloat and misaligned product direction.

---

### Section 3: Solution

> **Therefore, design and name your decision criteria explicitly—as a separate, prior act—before gathering options or evidence, and use those criteria as a public scaffold that prevents hidden preferences from steering the outcome.**

This pattern works by making the invisible visible. When criteria are designed first, three things shift. First, the conversation moves from *Which option do we prefer?* to *What actually matters here?* This is a change in the roots of the system. Second, all stakeholders must speak their values into a shared language before they can advocate for their preferred option. This doesn't eliminate conflict; it makes conflict legible and negotiable. Third, once criteria are public and weighted, the evaluation of options becomes less about rhetoric and more about evidence. A weak option cannot suddenly become strong because someone makes a better speech.

In Decision Theory terms, this follows the principle of **consequentialist evaluation**: decisions are sound if they're made through a sound process, applied consistently to the evidence. The criteria are the process. They act as a living membrane between the system's values and its choices—they translate what the community cares about into operational judgments.

The pattern also prevents **selection bias** and **motivated reasoning**. When criteria emerge *after* people have already formed preferences, those criteria are secretly shaped by the preferred conclusion. When criteria come first, they constrain what counts as relevant. This doesn't guarantee objectivity (values are always in play), but it channels decision-making toward coherence rather than self-deception.

The mechanism is social and cognitive at once. The act of naming criteria publicly creates accountability. It becomes harder to quietly shift priorities mid-evaluation. And because criteria are visible, a practitioner can revisit them later and ask: *Did we actually weight this the way we said we would?* This creates a feedback loop that tightens decision-making over time.

---

### Section 4: Implementation

**In Corporate Strategic Decisions:**
Establish a Decision Criteria Charter at the start of any strategic choice (market entry, M&A, product pivot). Name 5–7 dimensions that matter: financial return, talent impact, ecosystem dependency, strategic optionality, risk profile, alignment with mission. Have the executive team *weight* these dimensions explicitly using a simple numerical scale (0–5) or explicit ranking. Write these weights into a one-page document and circulate before any option is presented. When options arrive, evaluate each against the criteria using a structured rubric. Publish the scores. This shifts the decision from *the CEO prefers X* to *option X scores highest on criteria we all agreed to beforehand*.

**In Government Policy Deliberation:**
Create a Policy Evaluation Matrix early in the deliberation cycle, before stakeholder submissions begin. Name the criteria that matter: fiscal impact, equity (disaggregated by affected groups), implementation feasibility, alignment with existing statutes, democratic legitimacy, environmental consequence. Weight these criteria through a structured public consultation—not to manufacture false consensus, but to make disagreements about priorities visible and negotiable. Publish the matrix before evidence gathering. When policy briefs arrive, score them against the matrix. This prevents criteria from shifting to favor whichever stakeholder shows up with the best-written submission.

**In Activist Collective Decisions:**
Before any major decision (action strategy, resource allocation, structural change), run a Criteria Workshop where all voices get equal time to name what matters. You might surface: fidelity to our values, participation of most-impacted people, sustainability of our own volunteers, likelihood of win on the stated goal, growth of people-power. Resist the urge to reach consensus on weighting; instead, make it explicit that different members weight these differently. Document the range. When options come forward, evaluate them against the criteria map. This honors both urgency and inclusion—you can decide quickly without pretending everyone shares identical priorities.

**In Tech Product Decisions:**
Establish a Product Decision Framework at the start of each quarterly planning cycle or major feature decision. Name your criteria (user value, technical debt impact, business model fit, team learning opportunity, ecosystem coherence). Have product leadership and engineering leads weight these together, explicitly. Use this framework to evaluate feature proposals before they enter the sprint. This prevents the pattern where the loudest stakeholder's preference masquerades as a data-driven decision. When a high-scoring-on-all-dimensions feature is compared to a technically elegant but lower-user-value option, the criteria make that trade-off explicit rather than hidden.

**Across all contexts:**
- **Document criteria before gathering options.** Write them down. Circulate them. Ask: *Is anything missing?* Revise once, then lock them.
- **Make weights explicit.** If criteria A and B conflict, which wins? Say it. "We're weighting user safety at 5, launch speed at 2."
- **Use a structured evaluation tool.** A spreadsheet, rubric, or scoring matrix. Something that forces consistency.
- **Review the process after the decision.** Did we actually weight as stated? Did criteria shift mid-evaluation? What would we change next time?

---

### Section 5: Consequences

**What flourishes:**

Decisions become more durable because they're grounded in shared reasoning, not hidden authority. Stakeholders who lose a particular choice can see exactly why—the criteria were explicit, the scoring was transparent—and they're more likely to accept the outcome and implement it well. Teams develop institutional memory about what matters. Over time, criteria get refined based on which decisions actually held up well and which didn't. This creates a learning feedback loop. Motivation shifts from *gaming the process* to *solving the real problem*. Meetings move faster because the conversation is structured. Dissent becomes productive: *I weight ecosystem resilience higher than you do, so I want to revisit that criterion* is a clear, negotiable disagreement, not a veiled power struggle.

**What risks emerge:**

This pattern can calcify into ritual. Once criteria are designed, people follow them mechanically without asking whether they still fit the living context. If conditions shift dramatically, outdated criteria can lock an organization into obsolete choices. A high resilience score (3.0) warns us here: this pattern sustains but does not adapt. Groups can also use criteria as a way to dodge accountability—*We followed the process, so this outcome is legitimate*—when the criteria themselves were poorly designed or captured only dominant voices. There's also the risk of false precision: a scoring system can create the appearance of objectivity while masking value judgments that remain thoroughly contestable. If a team assigns numerical scores without acknowledging the interpretation work embedded in those scores, they create brittle decisions that feel rational but fail when reality doesn't match the model.

---

### Section 6: Known Uses

**NASA's Mission Selection Process (Space Agency, Government):**
NASA's decision framework for major mission proposals explicitly separates criteria design from option evaluation. The agency names criteria (scientific merit, technical feasibility, cost efficiency, alignment with strategic goals, international partnership potential) and weights them before proposals arrive. Proposal reviewers then score each mission against the published rubric. This process has been refined over decades and is documented in their mission selection guidelines. It allows NASA to compare missions as different as Mars rovers and space telescope arrays using a consistent logic. The criteria have shifted over time (reflecting changing priorities), but the discipline of designing them first has kept decisions coherent even through dramatic budget cycles and leadership changes.

**The UK's National Institute for Health and Care Excellence (NICE) (Government, Policy):**
NICE uses explicit decision criteria to evaluate whether new medicines and medical technologies should be funded through the National Health Service. Before any appraisal begins, NICE publishes its criteria: clinical effectiveness, cost-effectiveness (typically measured via quality-adjusted life years), and equity considerations. These criteria are weighted and open to public consultation. When pharmaceutical companies submit evidence for a new drug, NICE evaluates it against these criteria using a structured process. Because criteria are public and stable, decisions are predictable and defensible even when they reject expensive new treatments. This has become the gold standard for health technology assessment globally. The pattern's power here is that it prevents each new drug from triggering a fresh argument about what counts as a good outcome.

**Participatory Budgeting in São Paulo (Activist/Government Hybrid):**
When São Paulo's participatory budgeting process scaled beyond neighborhood-level decisions, organizers faced the problem that different districts wanted to prioritize different kinds of spending. Rather than letting each neighborhood define its own criteria, the process created a citywide criteria framework: accessibility for people with disabilities, environmental sustainability, economic inclusion, alignment with existing infrastructure plans. These were weighted through citywide deliberation, then applied locally. This allowed São Paulo to allocate resources equitably across neighborhoods while respecting local priorities. The criteria acted as a commons language, making it possible to compare a community center in the south zone with a transit improvement in the north and allocate resources coherently. When criteria shifted (after a change in city administration), the process was transparent about the change, and different stakeholder groups could see exactly what had changed and organize around it.

---

### Section 7: Cognitive Era

In an age of AI and distributed intelligence, this pattern transforms but remains vital. AI can now generate options faster than humans can evaluate them, and it can surface optimization possibilities we wouldn't have considered. But this creates a new urgency around criteria design: *if we don't specify what we care about, the algorithm will optimize for something we didn't mean to ask for*.

The tech translation shifts here: Product Decision Frameworks must now explicitly address what an AI system should do when criteria conflict (the human team can hold tension; the algorithm cannot). Teams building recommendation systems, content moderation tools, or autonomous systems discover that vague criteria—"maximize engagement," "flag harmful content"—produce catastrophic unintended consequences. Tight, explicit criteria design becomes a safety mechanism.

Distributed decision-making also changes the pattern. If decisions are made across a network of teams or even by algorithmic systems, criteria become the *protocol*—the shared language that coordinates action without requiring centralized authority. A decentralized autonomous organization (DAO) cannot rely on a single executive to interpret judgment calls; it must encode criteria so thoroughly that the system can operate without constant human override.

The risk is that explicit criteria, once encoded into code or embedded in an AI system, become much harder to revise. A spreadsheet-based criteria framework can shift in the next meeting; a production algorithm carrying embedded criteria takes much longer to change. This tilts the pattern toward rigidity. The new leverage is to build **criteria versioning** into systems from the start—treating criteria as living parameters, not fixed rules, that can be audited and updated as conditions evolve.

---

### Section 8: Vitality

**Signs of life:**

- Decisions that were controversial in the moment are revisited six months later and people acknowledge they were the right calls. This means criteria were real, not theater.
- A new person joining the team can understand *why* past decisions were made by reading the criteria and evaluation, without requiring oral history from veterans.
- In moments of conflict, stakeholders disagree about *which criteria matter most*, not about whether criteria exist or what they were. The debate is legible.
- After a decision that didn't work out, the group asks *Did our criteria miss something?* rather than *Did we choose the wrong option?* This reflects a learning orientation to the system itself.

**Signs of decay:**

- Criteria are written into a binder and never looked at again. People refer to them only when someone challenges a decision, treating them as a legal defense rather than a living logic.
- Criteria shift mid-evaluation without acknowledgment. "We decided to weight market speed more heavily" happens in whispers, not in a revision of the public framework.
- A team starts scoring options against criteria but then picks a different option anyway, citing reasons that weren't in the criteria. The criteria become decoration.
- People express fatigue about the process itself: *This takes forever; we should just decide faster.* Criteria design has become burden rather than clarity.

**When to replant:**

Restart the criteria design process when the external context has fundamentally shifted (new competitive pressure, regulatory change, major personnel turnover) or when you notice that recent decisions don't align with what your community said it cared about. Don't wait for failure; refresh criteria annually, or whenever the organization articulates a new mission or values shift. The act of redesigning criteria together is itself a vitality practice—it reconnects the team to what they actually care about, beyond the momentum of prior choices.
