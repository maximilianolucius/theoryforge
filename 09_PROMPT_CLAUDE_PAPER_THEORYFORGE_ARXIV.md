# Prompt para Claude Fable: paper arXiv de TheoryForge

## Identidad del proyecto

**Nombre:** TheoryForge

**Título recomendado:**

> **TheoryForge: Operator-Guided Autonomous Theory Formation in Mathematics**

**Subtítulo:**

> *From Theorem Proving to Definitions, Invariants, Reductions, and Research Programs*

**Tipo de trabajo:** autonomous mathematical discovery systems paper with benchmark and case studies.

**Categorías arXiv probables:** `cs.AI`, con cruces posibles en `cs.LO` y el dominio matemático del caso de estudio.

---

## Prompt maestro

You are Claude Fable 5 acting as principal investigator, mathematical discovery researcher, program-synthesis architect, formal-methods engineer, experimental designer, adversarial mathematician, and arXiv production lead.

Your mission is to create a complete paper, benchmark and reference implementation named **TheoryForge**.

TheoryForge is the Discovery Plane of the Bourbaki Engine. It must address a task broader than proving a supplied theorem:

> Given a governed mathematical corpus, an open research frontier, and explicit resource constraints, can an autonomous system construct useful new mathematical theory by synthesizing definitions, invariants, conjectures, reductions, counterexamples, barriers, and research programs whose value survives independent verification?

Read before designing the system:

1. the current Bourbaki Engine paper and its v2 architecture specification;
2. MIRADOR materials;
3. ProofContext materials;
4. CongressBench specification;
5. the complete Bang affine plank campaign;
6. primary sources on automated theorem proving, conjecture generation, program synthesis, FunSearch/AlphaEvolve-style discovery, symbolic mathematics, theory formation and scientific discovery agents.

Do not claim mathematical discovery merely because a model emits an unfamiliar statement. Novelty, truth, utility and nontriviality are separate evaluation axes.

Work under:

`theoryforge/`

## 1. Scientific distinction

Clearly distinguish:

- **proof search:** find a derivation of a fixed claim;
- **conjecture generation:** propose candidate statements;
- **program synthesis:** generate executable objects optimized by an evaluator;
- **theory formation:** create a network of definitions, claims, transformations and explanatory structure;
- **research-program formation:** decide which families of questions and representations deserve sustained effort.

TheoryForge targets the last two while using the first three as components.

## 2. Core research questions

1. Can explicit discovery operators outperform unconstrained “think harder” prompting?
2. Can a system synthesize definitions or invariants that compress and explain observed mathematical structure?
3. Can it identify minimal missing lemmas that unlock proof programs?
4. Can it discover useful barriers or `[NO_GO]` results rather than endlessly pursuing failed routes?
5. Does ProofContext improve discovery by retrieving assumptions, counterexamples and cross-domain analogies?
6. Does MIRADOR improve reuse and auditability of generated theory?
7. Does early formalization improve candidate quality or prematurely constrain exploration?
8. Which combinations of exploration, adversarial testing and formal verification yield the highest verified knowledge gain per unit cost?

## 3. Discovery outputs

TheoryForge must produce typed Mathematical Cells, including:

- new definition candidate;
- invariant;
- conjecture;
- equivalence candidate;
- reduction;
- construction;
- example;
- counterexample;
- extremal family;
- stability statement;
- classification proposal;
- bridge between domains;
- barrier or `[NO_GO]` claim;
- minimal missing lemma;
- proof blueprint;
- research program.

All outputs begin as `DRAFT`, `OPEN` or `EVIDENCE`. TheoryForge has no promotion authority.

## 4. Operator library

Implement and specify at least:

### `SPECIALIZE`

Restrict parameters, dimensions, symmetry or object classes to expose tractable structure.

### `GENERALIZE`

Identify which assumptions a proof or experiment actually uses and propose a broader object.

### `COUNTEREXAMPLE_FIRST`

Attack a claim before allocating proof effort.

### `NEGATE_AND_SEARCH`

Translate negation into model, SAT/SMT, combinatorial or computational search.

### `DUALIZE`

Construct a dual formulation and an explicit correspondence obligation.

### `CHANGE_REPRESENTATION`

Move among geometric, analytic, algebraic, combinatorial, probabilistic, logical or computational representations.

### `TRANSFER`

Import a pattern from another domain while generating a proof obligation for the transport.

### `MINIMAL_MISSING_LEMMA`

Given a proof blueprint with gaps, infer the weakest useful obligation that would close or materially advance the route.

### `EXTREMALIZE`

Search for equality cases, extremizers and rigid families.

### `STABILITY`

Ask what near-extremal objects must resemble.

### `BARRIER_SEARCH`

Attempt to prove that a method family cannot exceed a bound or cross a known obstruction.

### `FORMALIZE_EARLY`

Compile definitions or intermediate claims early to reveal hidden assumptions.

### `SYNTHESIZE_DEFINITION`

Propose a concept that compresses repeated patterns, then test whether it improves theorem statements, proofs or retrieval.

For every operator define input types, preconditions, transformations, output state, validators, failure modes and cost accounting.

## 5. Architecture

Implement a closed but authority-separated loop:

```text
campaign constitution
    → ProofContext Evidence Bundle
    → frontier analysis
    → operator selection
    → candidate generation
    → exact experiments / counterexample search
    → formalization or certificate extraction
    → independent Congress
    → promoted result or structured failure
    → updated corpus and scheduler priors
```

Required modules:

- frontier mapper;
- operator policy;
- candidate generator;
- symbolic/computational laboratory;
- counterexample engine;
- proof planner;
- MIRADOR serializer;
- ProofContext client;
- Lean/formal backend adapter;
- CongressBench-compatible reviewer interface;
- research-program scheduler;
- immutable experiment and event logger.

## 6. Research-program scheduler

Manage a portfolio rather than a single chain of thought.

Track:

- program hypothesis;
- representation;
- target claims;
- known barriers;
- expected information gain;
- estimated cost;
- verification debt;
- novelty risk;
- dependencies;
- failed attempts;
- retreat conditions;
- minimum publishable outcome.

Reserve explicit budgets for exploitation, orthogonal exploration, counterexample search, formalization, barriers and reproduction.

The scheduler score allocates resources. It is not evidence of mathematical truth.

## 7. Evaluation ladder

TheoryForge requires several complementary evaluation worlds.

### Tier A — Synthetic mathematical worlds

Generate small formal universes with hidden rules, concepts and useful invariants. Evaluate whether TheoryForge recovers explanatory structure from examples and permitted queries.

Advantages: exact ground truth and contamination control.

Limitation: uncertain transfer to research mathematics.

### Tier B — Retrospective discoveries

Time-slice historical mathematical corpora before a known definition, lemma, classification or bridge appeared. Ask the system to reconstruct it.

Treat pretrained-model contamination as a major threat. Use substitution, renaming, representation scrambling and model-access controls where possible. Do not call this contamination-free.

### Tier C — Expert-authored unseen problems

External mathematicians provide unpublished or newly created research tasks, withheld insights and evaluation criteria.

### Tier D — Open mathematical frontier

Attack bounded open subproblems with external expert governance. Success includes a new lemma, counterexample, reduction, barrier or useful definition—not only full resolution.

## 8. TheoryBench

Create a benchmark provisionally named **TheoryBench**. Verify name availability before release.

Benchmark tasks should test:

- definition synthesis;
- invariant discovery;
- conjecture ranking;
- counterexample generation;
- minimal missing lemma extraction;
- representation change;
- cross-domain transfer;
- extremal-family recovery;
- stability conjecturing;
- barrier discovery;
- research-program selection.

Each task must specify:

- allowed corpus and tools;
- hidden ground truth where applicable;
- discovery budget;
- evaluation artifacts;
- novelty boundary;
- formal or expert checker;
- partial-credit criteria;
- contamination risk.

## 9. Evaluation dimensions

Do not reduce theory quality to theorem truth.

Measure:

### Correctness

- formal proof or certificate success;
- counterexample survival;
- assumption preservation;
- correspondence between informal and formal forms.

### Novelty

- retrieval-based collision search;
- source cutoff;
- independent literature audit;
- expert novelty judgment;
- distinction between globally new and new-to-system.

### Utility

- downstream proof success;
- number and importance of obligations closed;
- reuse across tasks;
- search-space reduction;
- barrier pruning;
- expert-rated usefulness.

### Theory compression

- facts explained by a new definition or invariant;
- reduction in description/proof length;
- dependency simplification;
- generalization without added exceptions.

### Robustness

- survival under counterexample search;
- representation perturbation;
- independent rederivation;
- formalization;
- reviewer-model changes.

### Efficiency

- verified knowledge gain per token, compute-hour and dollar;
- time to useful candidate;
- verification debt;
- failed-route value recovered.

## 10. Verified Knowledge Gain

Propose and validate a multidimensional result record rather than an opaque scalar.

At minimum report:

- promoted claims;
- refuted conjectures with reusable counterexamples;
- certified barriers;
- dependency edges added or removed;
- theory compression;
- external novelty status;
- cost and verification debt.

If a scalar utility is used for scheduling, preregister weights and never present it as objective mathematical value.

## 11. Baselines

Compare:

- direct single-model prompting;
- best-of-N sampling;
- tree/search prompting;
- proposer–critic agents;
- proof-only agents;
- executable program-search baselines;
- TheoryForge without operator library;
- TheoryForge without ProofContext;
- TheoryForge without counterexample-first policy;
- TheoryForge without early formalization;
- full TheoryForge.

Use task-compatible baselines and fixed budgets. Do not compare benchmark numbers across incompatible settings.

## 12. Bang affine plank case study

Use Bang's affine plank problem as the main integrated case study.

Reconstruct and extend:

- transport-defect viewpoint;
- witness-measure characterization;
- tight configurations;
- three-median and `2F+1M` structures;
- one-plank-per-direction versus unrestricted constants;
- normalizer barriers;
- certificate-backed extremal searches;
- minimal missing lemmas for remaining routes.

Freeze the known campaign corpus before running discovery experiments. Clearly distinguish rediscovery from new output.

Any allegedly novel result must pass:

1. ProofContext collision search;
2. adversarial counterexample search;
3. formal/certificate verification where feasible;
4. fresh-context Congress;
5. external expert review.

## 13. Implementation

Create:

```text
theoryforge/
  README.md
  LICENSE
  pyproject.toml
  constitution/
  schema/
  operators/
  retrieval/
  generators/
  experiments/
  counterexamples/
  formalization/
  scheduler/
  congress/
  theorybench/
  case_studies/bang/
  results/
  paper/
  audits/
```

Preserve:

- immutable run manifests;
- model and prompt versions;
- Evidence Bundle hashes;
- tool calls and executable artifacts;
- exact random seeds;
- candidate genealogy;
- rejection and failure reasons;
- promotion records.

## 14. Related-work audit

Read primary sources on:

- automated conjecturing;
- automated theory formation;
- inductive logic programming;
- symbolic concept discovery;
- FunSearch and AlphaEvolve-style program evolution;
- theorem proving and proof planning;
- QED, RMA, Aletheia, LEAP and Prover Agent;
- AlphaGeometry-style auxiliary construction;
- scientific discovery agents;
- definition and invariant synthesis;
- mathematical knowledge graphs and retrieval;
- formalization and proof-producing computation.

Create:

| System | Fixed target | Generates conjectures | Synthesizes definitions | Changes representation | Finds counterexamples | Finds barriers | Formal verification | Novelty audit | Research-program memory |

Do not claim firstness before completing the matrix and search protocol.

## 15. Paper structure

1. Abstract
2. Introduction
3. From Theorem Proving to Theory Formation
4. Related Work
5. Task Definition and Output Ontology
6. Discovery Operators
7. TheoryForge Architecture
8. Research-Program Scheduling
9. TheoryBench
10. Experimental Protocol
11. Results and Ablations
12. Bang Affine Plank Case Study
13. Novelty, Verification and Promotion
14. Threats to Validity
15. Limitations and Research Agenda
16. Conclusion
17. Appendices

Produce arXiv-compatible LaTeX, verified bibliography, reproducible figures and tables, clean PDF and upload-ready source archive.

## 16. Threat model

Address:

- memorized discoveries;
- superficial renaming as novelty;
- false analogies;
- problem modification;
- reward hacking;
- evaluator overfitting;
- benchmark contamination;
- model monoculture;
- invalid transformation edges;
- computational evidence promoted as proof;
- formalization of a weaker claim;
- publication-priority errors;
- endless speculative branching;
- premature convergence;
- excessive verification debt;
- human expert selection bias.

## 17. Required deliverables

Return:

1. complete TheoryForge implementation;
2. discovery-operator specification;
3. TheoryBench dataset and manifest;
4. preregistered evaluation protocol;
5. baselines and ablations;
6. raw results;
7. candidate genealogies;
8. Bang case study;
9. novelty audits;
10. formal/certificate artifacts;
11. Congress reviews;
12. complete paper and PDF;
13. related-work matrix;
14. reproducibility report;
15. arXiv-ready archive.

## 18. Acceptance criteria

Do not declare completion unless:

- theory formation is distinguished from proof generation;
- outputs are represented as governed Mathematical Cells;
- TheoryForge has no promotion authority;
- every claimed discovery has a genealogy and fixed information boundary;
- novelty and correctness are evaluated separately;
- counterexample search precedes expensive proof promotion;
- baselines use comparable budgets;
- held-out tasks remain sealed until system freeze;
- negative and null results are reported;
- Bang rediscovery is not mislabeled as novelty;
- all reported results regenerate from raw artifacts;
- external expert judgment is identified rather than simulated.

## 19. First response required from Claude

Do not begin implementation or draft conclusions.

First return:

1. source inventory;
2. related-work search plan;
3. precise theory-formation task definition;
4. discovery-operator API draft;
5. TheoryBench design;
6. contamination-control plan;
7. baseline and ablation matrix;
8. Bang corpus-freeze plan;
9. verification and novelty protocol;
10. staged implementation schedule;
11. blocking scientific decisions.

Freeze the protocol and manifests before evaluating open-frontier performance.
