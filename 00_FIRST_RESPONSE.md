# TheoryForge — First Response (Section 19 deliverable)

> **What this document is.** The master prompt
> (`09_PROMPT_CLAUDE_PAPER_THEORYFORGE_ARXIV.md`, §19) requires that the *first*
> return **not** be implementation or drafted conclusions, but the eleven
> planning artifacts below, and that **the protocol and manifests be frozen
> before any open-frontier evaluation is run.** This file is that first
> response. Nothing here claims a mathematical discovery, reports an experiment,
> or promotes a claim. No code has been executed against the frontier.
>
> **Epistemic tagging.** Following the project's own rigor rules, factual
> statements about the existing codebases are tagged `[evidenced]` (read from
> the source files during the inventory), `[inferred]` (a defensible conclusion
> from evidence), or `[guessed]` (a hypothesis to be checked). Design proposals
> are unmarked but are proposals, not facts.
>
> **Status of every deliverable below:** `DRAFT / UNFROZEN`. Author of this
> response: Claude (Opus 4.8). Date: 2026-07-12.

---

## 0. Orientation: what TheoryForge is, and the gap it fills

TheoryForge is specified as **the Discovery Plane of the Bourbaki Engine**
(prompt §, and `Bourbaki/bourbaki-engine.tex` §4/§8). The surrounding ecosystem
already exists as follows `[evidenced]`:

| Component | Role | Maturity | What TheoryForge does with it |
|---|---|---|---|
| **Bourbaki Engine** (`/home/maxim/PycharmProjects/Bourbaki/`) | Governance architecture; defines Discovery Plane (propose-only) vs Trust Plane (sole promotion) | Paper + spec only, **no code**; Discovery Plane maturity code = **C (conceptual)** in `audits/CLAIM_LEDGER.md` | TheoryForge **is** the missing Discovery-Plane implementation |
| **MIRADOR** (`../mirador/`) | Typed/versioned Mathematical-Cell IR + event log + invalidation + transitions | Prototype **P**, working Python, 28 tests, `examples/affine_plank/` (13 cells / 55 events) | **Import** as the cell/serialize/hash/audit substrate |
| **ProofContext** (`../proof-context/`) | Dependency-aware retrieval → hashed **Evidence Bundle** | Eval **E**, working Python, 21 tests, 25-cell affine-plank corpus | **Import** as the ProofContext client; **two gaps must be built** (see B2) |
| **CongressBench** (`../congressbench/`) | Measures False-Theorem-Promotion-Rate of fresh-context review; defines reviewer contract | Planning + zero-cost StubReviewer harness, 14 tests, **no LLM runs** | **Conform to** its `Reviewer` ABC + `review.schema.json` |
| **Bang campaign** (`/home/maxim/PycharmProjects/bang-plank-euler-jacobi/`) | Main integrated case study | **Submission-ready** manuscript (AIMS Mathematics), 16 commits, 1 machine certificate | Corpus to **freeze**, rediscover, and extend |

**The central architectural fact** `[evidenced]`: authority is separated and
one-way. The Discovery Plane (TheoryForge) may only *propose* cells and edges;
only the Trust Plane / Congress may *promote*; MIRADOR enforces this in
`transitions.check_transition` (promotion requires `actor="congress"`,
independence level ≥ 3, no unresolved veto). **TheoryForge therefore has no
promotion authority by construction, not by policy.** Every acceptance criterion
in §18 that concerns authority is already structurally satisfied if TheoryForge
writes through MIRADOR.

---

## 1. Source inventory

Exact paths, verified during the inventory sweep. `[evidenced]` unless noted.

### 1.1 Bourbaki Engine — `/home/maxim/PycharmProjects/Bourbaki/`
- Paper (v2, current): `bourbaki-engine.tex` (+ `.pdf`, `bourbaki-engine-arxiv.tar.gz`); duplicate at `arxiv-submission/bourbaki-engine.tex`. v1 backups: `bourbaki-engine.pre-discovery.tex.bak`, `bourbaki-engine.pre-claimpromotion.tex.bak`.
- **v2 architecture spec (exists):** `spec/ARCHITECTURE_V2.md` (normative prose) + `schema/module-interfaces.json` (v2.0.0 machine-readable: planes, modules, object types, epistemic states, transition table, metric families).
- Audits: `audits/{SOURCE_INVENTORY,CLAIM_LEDGER,RELATED_WORK_MATRIX,RESPONSE_TO_CONGRESS,FINAL_ARXIV_CHECK}.md`, `audits/congress/reviews.md`. Changelog v1→v2: `SECTION_MAP_AND_CHANGELOG.md`. Reorientation briefs: `01_REORIENTACION_BOURBAKI_ENGINE_MILLENNIUM.md`, `02_…`, `07_…`.
- Status: paper + spec, **no executable code**. Git: 2 commits. MIT, Zenodo DOI `10.5281/zenodo.21328015`. Discovery Plane / formalization / scheduling = **specified, not built**.
- **Caveat:** `../ReadMe.txt` (145 KB) is unrelated (MT5/trading EA operations log). Do **not** cite it for TheoryForge.

### 1.2 MIRADOR — `/home/maxim/PycharmProjects/VS/mirador/`
- Paper: `paper/mirador-typed-versioned-ir.{tex,pdf,bbl}`, `paper/references.bib`. DOI `10.5281/zenodo.21324524`.
- **Schemas (authoritative):** `schema/mathematical-cell.schema.json` (`schema_version="mirador-cell/1.0"`, draft 2020-12, `additionalProperties:false`; 20 object types, 11 epistemic states, 16 edge types); grammar `schema/mirador-ir.ebnf`.
- Package `src/mirador/` (v0.1.0, Python ≥3.11, dep `jsonschema`). Public API: `model.py` (`Cell, IR, Context, Edge, EnvBinding, Review, ObjectType, EpistemicState, EdgeType, JUSTIFICATION_EDGES`, all with `as_dict()`/`from_dict()`); `canonicalize.py` (`content_hash, version_hash, canonical_claim, classify_identity, Identity, probable_similarity`); `validate.py` (`validate_cell`); `dependency_graph.py` (`DependencyGraph`); `provenance.py` (`EventLog, Event, claim_card`); `transitions.py` (`apply_transition, check_transition, TRANSITIONS, Role, ROLES`); `invalidation.py` (`refute, revise_definition, reaudit`).
- Case study: `examples/affine_plank/` (`corpus.py`, `run_case_study.py`, `export.py`, `cells/*.json`, `event_log.json`, `summary.json`) — 13 cells, 55 events, chain valid, acyclic.
- Object types (20): CONCEPT, DEFINITION, CONSTRUCTION, STATEMENT, QUESTION, CONJECTURE, LEMMA, THEOREM, EXAMPLE, COUNTEREXAMPLE, REDUCTION, EQUIVALENCE, BARRIER, PROOF, REFUTATION, EXPERIMENT, CERTIFICATE, CHECKER, HEURISTIC, TRANSLATION.
- Epistemic states (11): DRAFT, OPEN, EVIDENCE, CANDIDATE, REFUTED, NO_GO, FORMALIZED, AUDITED, PROMOTED, SUSPECT, RETIRED.

### 1.3 ProofContext — `/home/maxim/PycharmProjects/VS/proof-context/`
- Paper: `paper/proofcontext-dependency-aware-retrieval.{tex,pdf}`. DOI `10.5281/zenodo.21325288`.
- **Schemas:** `schema/evidence-bundle.schema.json` (`proofcontext-bundle/1.0`; keys incl. `definitions, claims, dependency_paths, counterexamples, barriers, open_conflicts, compatibility_report, retrieval_warnings, provenance_manifest, bundle_hash`), `schema/problem-signature.schema.json`.
- Package `src/proofcontext/` (v0.1.0, deps `jsonschema,numpy,scikit-learn,scipy,sympy,networkx`; deterministic, no neural download). Client: `engine.py::ProofContext(graph, log).query(nl) -> QueryResult` with `.bundle`. Retrieval: 5 signals (BM25, LSA-dense, formula, formal, graph-diffusion), hard compatibility filters, `bundle/assemble.py::canonical_bundle_hash`.
- **Runtime dependency on MIRADOR** (deep, read-only); vendored copy at `vendor/mirador/`.
- Benchmark: `data/benchmark/mathscopebench.json`; module-interfaces reports near-miss served 0% vs 44–75% baselines, dependency-sufficiency 0.90–0.93 vs 0.40–0.43.

### 1.4 CongressBench — `/home/maxim/PycharmProjects/VS/congressbench/`
- Master spec: `08_PROMPT_CLAUDE_PAPER_CONGRESSBENCH_ARXIV.md`. Paper: `paper/congressbench-fresh-context-review.{tex,pdf}`. Preregistration: `preregistration/PREREGISTRATION.md` (**DRAFT, unfrozen**).
- **Reviewer contract (the interface TheoryForge must satisfy):** `src/congressbench/reviewer.py::Reviewer(ABC)` with `review(item, bundle, condition, lens, seed) -> dict`; `REVIEW_SCHEMA_VERSION="congressbench-review/1.0"`; reference `StubReviewer` (synthetic, not evidence).
- **Schemas:** `schema/review.schema.json` (verdict ∈ {ACCEPT, REJECT, REPAIR, ABSTAIN}; 14 defect classes; `severity ∈ {fatal, material, cosmetic}`), `schema/item.schema.json` (stratum A/B/C, ground_truth DEFECTIVE/CORRECT, `representations{prose, mirador_cells, evidence_bundle, formal}`).
- Conditions C1–C6 (independence ladder): C1 self, C2 shared-history, C3 fresh-single, C4 fresh multi-lens Congress, C5 +MIRADOR cells & ProofContext bundle, C6 +formal checker. Isolation voids observations that leak out-of-condition context (`isolation.py`). Metric: FTPR (`scoring.py`).
- Bang defects: `src/congressbench/bang.py` (8 items, `gt_status=CONFIRMED`); Stratum-A mutators: `stratumA/mutators.py` (8 operators).
- Status: harness + 14 tests, **no LLM runs**. Blockers `audits/BLOCKING_DECISIONS.md`: **B5** (LLM budget/model families), **B6** (Lean4/mathlib not on PATH ⇒ Stratum-A items stay `gt_status=PENDING`).

### 1.5 Bang campaign — `/home/maxim/PycharmProjects/bang-plank-euler-jacobi/`
- **Live manuscript:** `drafts/affine-plank-triangle.tex` (172 KB) — *"Transport and tiling bounds for the affine plank problem on the triangle"*, 4 authors (Alraddadi, Lucius, Ahmad, Abdelfattah), MSC 52C17. AIMS submission: `drafts/aims-v1/affine-plank-triangle-aims-v1.{tex,pdf}` + `submission-source-aims-v1.zip`.
- **The one machine-assisted result:** `thm:sandwichbang` — `C^{111}_Δ(τ_0)=1` at `τ_0=(13/25,½,½)`. Certificate `c3_sandwich_certificate.txt` (12.06 MB, 812,651 leaves, SHA-256 `ead66ff2…`), independent checker `bb_certificate_check.py` (stdlib-only, prints `CERTIFICATE VALID`).
- Experiments: `experiments/` (68 exact-arithmetic Python scripts, `sympy`/`fractions`), curated arXiv bundle `drafts/ancillary/` (22 scripts + `README.md` script→theorem map). One Rust project `experiments/prop2_rust/` (not load-bearing).
- Notes (Spanish, primary record): `notes/01…61`. Audits: root `AUDITORIA_CLAUDE_30Jn.md`; `auditorias/00-ordenes-de-trabajo.md` + `auditorias/39…71`.
- Git: `main`, clean, 16 commits (2026-07-02 → 07-08); remote `github.com/maximilianolucius/bang-plank-affine-triangle`.
- **Two facts that change the plan** (see §6, §8):
  1. `[evidenced]` The campaign **pivoted away** from the Euler–Jacobi/BKK approach named in the folder and dossier; that line was refuted and archived in `drafts/obsolete/`. The live theory is transport-and-tiling. `drafts/hamilton-jacobi-*.tex` are **unrelated** work.
  2. `[evidenced]` The manuscript is **public** (GitHub + AIMS submission). This is a first-order contamination threat for any "rediscovery" claim (B3).

---

## 2. Related-work search plan

**Method** (mirrors the negative-novelty protocol used by the sibling projects, e.g. Bang `03-work-plan.md` T0.1): delegate the literature sweep to the `deep-research` skill, then build the §14 matrix; **make no firstness claim until the matrix and a collision-search protocol are complete** (prompt §14, §16).

**Families to sweep** (prompt §14) with seed anchors already surfaced `[evidenced]` by the name check:
- Automated theory formation / concept invention: **AM** (Lenat 1977), **HR** (Colton), "Learning Interestingness in Automated Mathematical Theory Formation" (arXiv **2511.14778**, 2025), agent-based cooperative theory formation.
- Automated conjecturing; inductive logic programming; symbolic concept discovery.
- Program-search discovery: **FunSearch**, **AlphaEvolve**, **AlphaGeometry** (auxiliary construction).
- Theorem proving / proof planning; QED, RMA, Aletheia, LEAP, Prover Agent.
- Scientific-discovery agents; definition & invariant synthesis; mathematical knowledge graphs & retrieval; formalization & proof-producing computation.

**Related-work matrix** (schema frozen here; cells to be filled by the sweep, not now):

| System | Fixed target | Generates conjectures | Synthesizes definitions | Changes representation | Finds counterexamples | Finds barriers | Formal verification | Novelty audit | Research-program memory |
|---|---|---|---|---|---|---|---|---|---|

**Search protocol:** (a) arXiv + Semantic Scholar citation trees of the anchors above; (b) keyword crosses `{theory formation, definition synthesis, invariant discovery, barrier} × {LLM, agent, autonomous}`; (c) for the Bang case study specifically, the campaign's own reference set in `bang…/notes/42-refs-papers-resumen.md` (Bakaev–Yehudayoff 2026, Ball 1991, Ambrus, Gardner 1988, Verreault survey). Output → `audits/RELATED_WORK_MATRIX.md`.

---

## 3. Precise theory-formation task definition

Distinguish (prompt §1) — TheoryForge targets (d)+(e) using (a)–(c) as components:
(a) **proof search** (derive a fixed claim); (b) **conjecture generation** (propose statements); (c) **program synthesis** (evaluator-optimized executable objects); (d) **theory formation** (a *network* of definitions/claims/transformations + explanatory structure); (e) **research-program formation** (which families deserve sustained effort).

**Formal task.** Given
- a **governed corpus** `C@v` — a set of MIRADOR cells at a frozen content-addressed version `v` (the freeze manifest, §8);
- a **frontier** `F ⊆ C@v` — the OPEN/QUESTION cells and their dependency neighbourhood;
- a **campaign constitution** `K` — exact conventions, allowed dependencies, certificate standard per claim class, novelty/attribution policy, stopping conditions, minimum deliverable (Bourbaki §5; instantiated per case study);
- a **resource budget** `B` — token/compute/dollar caps, split across the six reserves of §6 of the prompt (exploit, orthogonal-explore, counterexample, formalize, barrier, reproduce),

produce a set of **typed Mathematical Cells** `{o_i}` (§3 of the prompt: definition candidate, invariant, conjecture, equivalence, reduction, construction, example, counterexample, extremal family, stability statement, classification, bridge, barrier/`[NO_GO]`, minimal missing lemma, proof blueprint, research program), each
- created only in state `DRAFT`, `OPEN`, or `EVIDENCE` (**never promoted by TheoryForge**);
- carrying full **genealogy** (which operator, from which parent cells, under which Evidence Bundle hash, at which seed) and a **fixed information boundary** (the corpus version and model/prompt versions it was allowed to see).

**Objective (not a scalar of mathematical truth):** maximize **Verified Knowledge Gain** (§10) — promoted claims, refuted conjectures with reusable counterexamples, certified barriers, dependency edges added/removed, theory compression, external novelty status — **per unit cost**, where "promoted/certified/novel" are determined by the *independent* downstream machinery (Congress, checker, collision search), not by TheoryForge.

**Non-goals (structural):** TheoryForge does not decide truth, does not promote, and does not author its own reviews (author-barred-from-promotion is enforced by MIRADOR).

---

## 4. Discovery-operator API draft

**Common typed interface** (draft; to live in `operators/base.py`, machine schema `schema/operator.schema.json`):

```
Operator:
  name: str
  input_types:    set[ObjectType]         # MIRADOR object types it consumes
  preconditions:  Predicate(cell, bundle) # must hold on inputs + Evidence Bundle
  transform(inputs, bundle, budget) -> list[CandidateCell]
  output_state:   {DRAFT, OPEN, EVIDENCE} # never higher
  validators:     list[Validator]         # cheap self-checks before emission
  failure_modes:  list[FailureMode]       # each with a detectable signature
  cost:           CostRecord              # tokens/compute/$ + wall-clock, logged
```

Every emitted `CandidateCell` records `genealogy = {operator, parents[], bundle_hash, model_version, prompt_version, seed}` and is serialized through `mirador.Cell` so identity = `content_hash`.

**The 13 operators (prompt §4).** Full input/precondition/transform/output/validators/failure-modes/cost specs are staged in `operators/OPERATOR_API.md`; four representative full specs and a summary table follow.

*Representative full specs:*

- **`COUNTEREXAMPLE_FIRST`** — in: CONJECTURE/STATEMENT. pre: claim is falsifiable + has a decidable/searchable model class. transform: compile negation to a search (grid/SAT/SMT/combinatorial) *before* any proof budget is spent. out: COUNTEREXAMPLE (EVIDENCE) or a "survived-search" annotation on the input (not a proof). validators: re-check the witness with exact arithmetic (never floats — Bang rigor rule). failure: search-space too large ⇒ emit a bounded-search barrier note, not silence. cost: search wall-clock + calls.
- **`SYNTHESIZE_DEFINITION`** — in: ≥2 EXAMPLE/EXPERIMENT/THEOREM cells sharing structure. pre: a repeated pattern retrievable via ProofContext. transform: propose a CONCEPT/DEFINITION that compresses the pattern; test whether it shortens statements/proofs or improves retrieval. out: DEFINITION (DRAFT). validators: definition type-checks in the IR grammar; does not collide (content_hash) with an existing definition unless intended. failure: definition is a renaming (caught by collision search, B3/§9) ⇒ REFUTED-as-novelty. cost: generation + a compression measurement.
- **`MINIMAL_MISSING_LEMMA`** — in: a PROOF blueprint with gaps. pre: gap is localized to ≥1 named obligation. transform: infer the *weakest* obligation that closes/advances the route. out: LEMMA (OPEN) + a `requires` edge to the blueprint. validators: assuming the lemma, the blueprint's remaining steps type-check. failure: proposed lemma is equivalent to the theorem (no progress) ⇒ flagged. cost: planner calls. *(Bang instance: the thin-plank lemma, §8.)*
- **`BARRIER_SEARCH`** — in: a method family + a target bound. pre: the method is formalizable as a bounded transformation. transform: attempt to prove the method cannot cross an obstruction. out: BARRIER / `[NO_GO]` (EVIDENCE). validators: the obstruction instance is exact/certified. failure: only heuristic obstruction found ⇒ EVIDENCE not NO_GO. cost: proof-attempt budget. *(Bang instance: the normalizer/chord-lemma obstruction, `prop:nogo`.)*

*Summary of the remaining operators:* `SPECIALIZE`, `GENERALIZE` (identify which assumptions a proof actually uses), `NEGATE_AND_SEARCH`, `DUALIZE` (+ correspondence obligation), `CHANGE_REPRESENTATION` (geometric↔analytic↔algebraic↔combinatorial↔probabilistic↔logical↔computational), `TRANSFER` (import a pattern from another domain + a transport proof obligation), `EXTREMALIZE` (equality cases / extremizers / rigid families), `STABILITY` (near-extremal structure), `FORMALIZE_EARLY` (compile early to expose hidden assumptions). Each gets the same seven-field spec in `operators/OPERATOR_API.md`.

**Note (blocking, B2):** `TRANSFER` and `CHANGE_REPRESENTATION` presuppose cross-domain analogy retrieval, which **ProofContext does not currently provide** `[evidenced]`. Either build it or descope these two operators for v1.

---

## 5. TheoryBench design

**Name check `[evidenced]` (prompt §8 requires it):** no exact "TheoryBench" was found, but the space is crowded with near-collisions — MathBench, UGMathBench, TPBench, GTBench, LemmaBench. **Recommendation:** treat the name as provisional and pick a less collision-prone name before release (candidate decision B-name). Reported, not decided here.

**Four evaluation worlds (prompt §7):**
- **Tier A — synthetic worlds:** small formal universes with hidden rules/concepts/invariants; exact ground truth, contamination-controllable. *Primary quantitative tier.*
- **Tier B — retrospective:** time-slice a corpus before a known definition/lemma/bridge; ask the system to reconstruct it. **Contamination is a first-order threat; never called contamination-free** (§6).
- **Tier C — expert-authored unseen:** external mathematicians supply withheld tasks + criteria.
- **Tier D — open frontier:** bounded open subproblems under external expert governance; success includes a new lemma/counterexample/reduction/barrier/definition, not only full resolution.

**Task families (prompt §8):** definition synthesis, invariant discovery, conjecture ranking, counterexample generation, minimal-missing-lemma extraction, representation change, cross-domain transfer, extremal-family recovery, stability conjecturing, barrier discovery, research-program selection.

**Per-task manifest (frozen schema; draft in `theorybench/task.schema.json`):**
`{task_id, tier, family, allowed_corpus@v, allowed_tools, hidden_ground_truth?, discovery_budget, evaluation_artifacts, novelty_boundary, checker (formal|expert), partial_credit_rubric, contamination_risk}`.

**Sealing:** Tier-C/D held-out tasks stay sealed until system freeze (§18); the sealed set is stored hashed, released by a manifest event.

---

## 6. Contamination-control plan

Threats (prompt §16): memorized discoveries, superficial renaming as novelty, false analogies, problem modification, reward hacking, evaluator overfitting, benchmark contamination, model monoculture.

**Structural controls:**
1. **Fixed information boundary per cell** — genealogy records exactly which corpus version + model/prompt version produced each candidate; nothing outside `C@v` is admissible input.
2. **Novelty ≠ correctness** — evaluated on separate axes (§9); "new-to-system" and "globally new" are distinct labels and never merged.
3. **Collision search before novelty is asserted** — content-hash + `classify_identity` + `probable_similarity` over the corpus (must be built, B2/§9), plus a human primary-source audit (§14). Renaming is caught as `REPRESENTATIONAL` identity, not novelty.
4. **Model-access controls & substitution** for Tier B: rename symbols, scramble representations, substitute constants where the mathematics permits; run reviewers from ≥2 model families to break monoculture (B5).

**Bang-specific contamination (acute) `[evidenced]`:** the Bang manuscript is public (GitHub + AIMS submission) and plausibly within or adjacent to pretraining data. Therefore:
- Bang Tier-B "rediscovery" **cannot be reported as contamination-free**, and any rediscovered result is labeled **rediscovery**, never novelty (§18).
- Genuine novelty for the Bang case study can only be claimed for the **open** subproblems (§8: `prob:covconst` non-concurrent non-facet triples; the thin-plank lemma; `prob:suff` on `Δ^{d≥3}`) and only after the full §9 gauntlet + external expert review.
- **Contamination-controls to freeze inside the corpus, flagged:** `notes/09-fibonacci-bootstrap.md` is an unretracted but mathematically **unsound** artifact `[evidenced]`; notes 05–21 are early refuted "victory" drafts; `paper-ready/00-INDEX.ms` asserts a since-corrected claim (triangle ⇒ planar via Ambrus). These are frozen **with a poison flag** so a rediscovery run that "confirms" them is scored as a failure, not a success.

---

## 7. Baseline and ablation matrix

Fixed budget `B`, task-compatible only; no cross-setting number comparison (prompt §11).

**Baselines:** direct single-model prompting · best-of-N sampling · tree/search prompting · proposer–critic agents · proof-only agents · executable program-search (FunSearch-style).

**Ablations of TheoryForge:** − operator library · − ProofContext · − counterexample-first policy · − early formalization · **full TheoryForge**.

| Arm | Operators | ProofContext | CE-first | Early-formalize | Scheduler |
|---|---|---|---|---|---|
| direct prompt | – | – | – | – | – |
| best-of-N | – | – | – | – | – |
| tree/search | – | – | – | – | – |
| proposer–critic | – | – | – | – | – |
| proof-only | – | – | – | – | – |
| program-search | – | – | – | – | – |
| TF − operators | – | ✓ | ✓ | ✓ | ✓ |
| TF − ProofContext | ✓ | – | ✓ | ✓ | ✓ |
| TF − CE-first | ✓ | ✓ | – | ✓ | ✓ |
| TF − early-formalize | ✓ | ✓ | ✓ | – | ✓ |
| **full TF** | ✓ | ✓ | ✓ | ✓ | ✓ |

Reported per TheoryBench task family; metric = Verified Knowledge Gain per unit cost (§9/§10).

---

## 8. Bang corpus-freeze plan

**Freeze mechanism:** git tag `bang-freeze-v0` on `bang-plank-affine-triangle@<commit>` + a SHA-256 **manifest** of the exact frozen file set, stored at `case_studies/bang/CORPUS_FREEZE.manifest.json` and hash-pinned in a MIRADOR freeze event. A draft manifest is generated alongside this response (`case_studies/bang/`); the file **boundary itself is a decision (B-freeze)** because of the poison-flagged items.

**Include (the knowledge record):**
- `00-research-dossier.md`, `03-work-plan.md`, `README.md`, `pinasco-outreach-draft-y-research.md`, `instrucciones-modificaciones-paper-aims.md`;
- `drafts/affine-plank-triangle.tex` + `drafts/aims-v1/*` + `drafts/entregas/*` + `drafts/BUILD.md` + `drafts/M1-working-notes.md`;
- `drafts/ancillary/*` (22 scripts + README map) and `experiments/*.py`;
- the certificate `c3_sandwich_certificate.txt` + checker `bb_certificate_check.py` + emitter `c3_balanced_bb.py`;
- `notes/01…61` (+ `lit-todo.md`, `method-abstraction.md`); `AUDITORIA_CLAUDE_30Jn.md`; `auditorias/*`.

**Exclude:** `drafts/obsolete/*` (abandoned Euler–Jacobi approach — the manuscript says do not cite) and `drafts/hamilton-jacobi-*.tex` (unrelated); `refs/*` (copyright-excluded PDFs — record bibliographic identity only).

**Poison-flag inside the freeze** (contamination controls, §6): `notes/09-fibonacci-bootstrap.md` (unsound), notes 05–21 (refuted), `paper-ready/00-INDEX.ms` (since-corrected Ambrus claim).

**Rediscovery vs novelty labeling** (prompt §12/§18):
- **Rediscovery targets** (frozen, then hidden from the system's boundary): `thm:median`, `thm:wper`, `thm:tight`, `thm:char`, transport-defect `def:defect`, the normalizer obstruction `prop:nogo`, the certificate-backed `thm:sandwichbang`.
- **Novelty targets** (genuinely open): `prob:covconst` (non-concurrent, non-facet triples), the **thin-plank lemma** (flagship missing lemma), `prob:suff` on `Δ^{d≥3}`, `prob:defect` (exact `sup_u D_Δ(u) ∈ [3/2,2]`).

**Naming discrepancy (B4) `[evidenced]`:** the prompt (§12) lists a **`2F+1M`** structure to reconstruct; **no such object exists in the corpus under any spelling.** The closest are `thm:3plus1` ("three facets + one plank") and `notes/25` ("3 facet planks + 1 tilted"). This must be clarified with the PI before it is set as a rediscovery target — I will not invent a `2F+1M` theorem.

Every allegedly novel Bang result must pass the five-stage gauntlet of §9.

---

## 9. Verification and novelty protocol

**The five-stage promotion gauntlet (prompt §12), counterexample-first:**
1. **ProofContext collision search** — content_hash + `classify_identity` + `probable_similarity` over `C@v` and (for global novelty) the literature audit. *Must be built (B2): ProofContext exposes the MIRADOR primitives but no collision-search client call `[evidenced]`.*
2. **Adversarial counterexample search** — runs *before* expensive proof effort (§18); exact arithmetic only.
3. **Formal / certificate verification where feasible** — see backend decision B1: default tier = **exact-rational / symbolic certificate + independent stdlib checker** (the Bang standard: certificate + checker, where the checker, not the search, is the authority — `bang…/auditorias/64`). Lean 4 is the named proof-assistant backend but **is not installed** (B6); treat proof-assistant formalization as optional/gated, not assumed.
4. **Fresh-context Congress** — a `Reviewer`-conforming interface (CongressBench `review.schema.json`, condition ≥ C4) run by ≥2 model families (B5); ACCEPT decided by the veto adjudicator, **not** by TheoryForge.
5. **External expert review** — identified, not simulated (§18). For Bang: the four manuscript authors + the Pinasco outreach thread.

**Evaluation dimensions (prompt §9), each measured concretely:**
- **Correctness:** certificate/checker pass · counterexample survival · assumption preservation · informal↔formal correspondence status (MIRADOR `correspondence_status`, never auto-inferred).
- **Novelty:** collision search · source cutoff · literature audit · expert judgment · global-new vs new-to-system.
- **Utility:** downstream proof success · obligations closed · reuse across tasks · search-space reduction · barrier pruning · expert-rated usefulness.
- **Theory compression:** facts explained by a new definition/invariant · description/proof-length reduction · dependency simplification.
- **Robustness:** survival under counterexample search · representation perturbation · independent rederivation · reviewer-model change.
- **Efficiency:** verified knowledge gain per token/compute-hour/dollar · time-to-useful-candidate · verification debt · failed-route value recovered.

**Verified Knowledge Gain (prompt §10):** a multidimensional record (promoted claims, refuted-with-reusable-counterexample, certified barriers, dependency edges ±, compression, external novelty, cost, verification debt) — **not an opaque scalar.** Any scalar used for scheduling has **preregistered weights** and is never presented as objective mathematical value.

---

## 10. Staged implementation schedule (gated)

Modeled on the Bang campaign's gated style (`03-work-plan.md`, gates that permit a publishable fallback). Each phase ends in a gate; no phase claims results.

- **P0 — Freeze & preregister.** Freeze Bang corpus (§8), freeze this protocol + TheoryBench manifests + baseline matrix + VKG weights. *Gate G0:* manifests hash-pinned, blocking decisions (§11) resolved or explicitly deferred. **← required before any open-frontier run.**
- **P1 — Substrate integration.** `mirador` serializer adapter, `proofcontext` client adapter, CongressBench `Reviewer` adapter; immutable run manifests + event logger. *G1:* a candidate cell round-trips DRAFT→(review)→ACCEPT/REJECT through real MIRADOR + a real reviewer on a toy item.
- **P2 — Operator library.** Implement the 13 operators against the §4 interface + validators + cost accounting. *G2:* each operator has a passing typed unit test and a failure-mode test.
- **P3 — Symbolic lab + counterexample engine.** Exact-arithmetic experiment runners + `NEGATE_AND_SEARCH`/`COUNTEREXAMPLE_FIRST`. *G3:* reproduces one known Bang counterexample/negative check exactly.
- **P4 — Research-program scheduler.** Portfolio with the six budget reserves (§6 of prompt); score is a resource heuristic, preregistered, never evidence. *G4:* deterministic replay of a scheduling decision from the log.
- **P5 — TheoryBench Tier A.** Synthetic worlds + checkers; run baselines + ablations. *G5:* full-TF ≥ best baseline on ≥1 family at fixed budget, or an honest null reported.
- **P6 — Bang rediscovery (Tier B).** Rediscovery targets only (§8), contamination caveats attached; poison-flagged items scored as failures if "confirmed." *G6:* rediscovery vs novelty cleanly separated in the log.
- **P7 — Ablations & robustness.** Full matrix (§7) + robustness perturbations. *G7:* every reported number regenerates from raw artifacts.
- **P8 — Open frontier (Tier D), gated.** Only after G0–G7 and external expert governance is in place; bounded Bang open subproblem (§8). *G8:* any output (even a barrier/null) passes the §9 gauntlet.
- **P9 — Paper & arXiv archive.** Structure per prompt §15; reproducibility report; §14 matrix complete before any firstness claim.

---

## 11. Blocking scientific decisions

These require a human PI decision before P0 closes. I state each with a recommendation but do **not** decide them.

- **B1 — Formal backend.** Lean 4 is named but not installed (CongressBench B6) `[evidenced]`. *Recommend:* adopt exact-rational/symbolic certificate + independent checker as the default "formal" tier (matches the only machine-verified Bang result); make Lean optional and gated. Decision needed: install Lean, or ratify the certificate standard?
- **B2 — ProofContext gaps.** No cross-domain **analogy/transfer retrieval** and no **collision-search client** exist `[evidenced]`. These block `TRANSFER`/`CHANGE_REPRESENTATION` (§4) and gauntlet stage 1 (§9). *Recommend:* build a thin collision-search wrapper over MIRADOR (`content_hash`/`classify_identity`/`probable_similarity`) for v1; **descope RQ5 cross-domain analogy** to a stated limitation for v1.
- **B3 — Bang contamination.** The manuscript is public `[evidenced]`; Tier-B rediscovery cannot be contamination-free. *Recommend:* keep Bang as an integrated *illustrative* case (rediscovery labeled as such) and make **Tier A synthetic worlds the primary quantitative evidence**; claim Bang novelty only on open subproblems after the full gauntlet.
- **B4 — `2F+1M` target.** No such object exists in the corpus `[evidenced]`; closest is `thm:3plus1`. *Needs PI clarification* before it is set as a rediscovery target.
- **B5 — LLM budget & model families.** Reviewer independence and anti-monoculture need ≥2 model families; empirical Congress runs have a real dollar cost (CongressBench B5 open). *Decision:* budget + which model families.
- **B6 — Frontier target & external expert (Tier D).** Which bounded open subproblem (`prob:covconst` / thin-plank lemma / `prob:suff`), and **who** is the identified external expert (manuscript authors? Pinasco?). Required by §18 (expert judgment identified, not simulated).
- **B7 — Congress composition for evaluation.** `StubReviewer` is explicitly not evidence `[evidenced]`; a real evaluative Congress needs LLM reviewers + a human expert. *Decision:* composition and independence level per TheoryBench tier.
- **B8 — VKG scalar.** Whether to use a scalar utility for scheduling at all; if yes, its **preregistered weights** (prompt §10). *Recommend:* multidimensional record for reporting; a preregistered scalar only for scheduler resource allocation.
- **B-name — benchmark name.** "TheoryBench" collides closely with existing benchmarks `[evidenced]`; pick a distinct name before release.

---

## Freeze checklist (prompt §19 final line)

Before evaluating open-frontier performance, freeze and hash-pin: **(1)** this protocol; **(2)** the Bang corpus manifest (§8); **(3)** the TheoryBench task manifests + sealed set; **(4)** the baseline/ablation matrix (§7); **(5)** the VKG weights (§10). Freeze is recorded as a MIRADOR event; open-frontier runs (P8) are inadmissible until the freeze event exists and B1–B7 are resolved or explicitly deferred.
