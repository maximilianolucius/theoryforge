# Discovery Operator Library — API specification (DRAFT / UNFROZEN)

Companion to `00_FIRST_RESPONSE.md §4` and `schema/operator.schema.json`. Every
operator implements the common typed interface and emits candidate MIRADOR cells
in `{DRAFT, OPEN, EVIDENCE}` only — **never a promoted state**. Each candidate
carries `genealogy = {operator, parents, bundle_hash, model_version,
prompt_version, seed}`.

Legend for the summary table: **In** = MIRADOR input types · **Out** = emitted
type(s)/state · **Val** = key validator · **Fail** = characteristic failure mode
(what is emitted instead — never silence).

| Operator | Purpose | In | Out | Val | Fail → emit |
|---|---|---|---|---|---|
| `SPECIALIZE` | Restrict parameters/dims/symmetry to expose tractable structure | STATEMENT, CONJECTURE, DEFINITION | derived STATEMENT/EXAMPLE (OPEN) | specialization is a valid instance (`instance_of` edge type-checks) | trivial/empty instance → flagged, no cell |
| `GENERALIZE` | Identify which assumptions a proof actually uses; propose broader object | PROOF, THEOREM, EXPERIMENT | STATEMENT/CONJECTURE (DRAFT) + `generalizes` edge | dropped assumption is genuinely unused in the source proof | over-generalization refuted by a known counterexample → COUNTEREXAMPLE |
| `COUNTEREXAMPLE_FIRST` | Attack a claim before spending proof budget | CONJECTURE, STATEMENT | COUNTEREXAMPLE (EVIDENCE) or survived-search annotation | witness re-checked in **exact arithmetic** | search space too large → bounded-search BARRIER note |
| `NEGATE_AND_SEARCH` | Translate negation into model / SAT / SMT / combinatorial / computational search | STATEMENT, CONJECTURE | COUNTEREXAMPLE (EVIDENCE) or EXPERIMENT | solver certificate re-verified | solver timeout/unknown → EXPERIMENT with explicit incompleteness |
| `DUALIZE` | Construct a dual formulation + explicit correspondence obligation | STATEMENT, THEOREM | EQUIVALENCE/STATEMENT (DRAFT) + correspondence obligation | dual round-trips on a checked instance | correspondence unproven → obligation left OPEN, not asserted |
| `CHANGE_REPRESENTATION` | Move among geometric/analytic/algebraic/combinatorial/probabilistic/logical/computational forms | any claim/construction | TRANSLATION (DRAFT) + `translates` edge | representations agree on ≥1 checked instance | representation drops information → flagged as lossy |
| `TRANSFER` | Import a pattern from another domain + transport proof obligation | claim + retrieved analogue | STATEMENT/CONJECTURE (DRAFT) + transport obligation | analogue retrieved by ProofContext (see B2) | **blocked**: no cross-domain analogy retrieval yet (B2) |
| `MINIMAL_MISSING_LEMMA` | Infer the weakest obligation that closes/advances a gapped blueprint | PROOF blueprint (with gaps) | LEMMA (OPEN) + `requires` edge | assuming the lemma, remaining steps type-check | lemma ≡ theorem (no progress) → flagged |
| `EXTREMALIZE` | Search for equality cases, extremizers, rigid families | THEOREM (bound), EXAMPLE | EXTREMAL family / EXAMPLE (EVIDENCE) | extremizer attains the bound exactly | near-extremal only → EVIDENCE, not equality claim |
| `STABILITY` | Ask what near-extremal objects must resemble | extremal family | STABILITY STATEMENT (DRAFT) | perturbation stays within stated neighbourhood | instability found → COUNTEREXAMPLE to the stability claim |
| `BARRIER_SEARCH` | Prove a method family cannot exceed a bound / cross an obstruction | method + target bound | BARRIER / `[NO_GO]` (EVIDENCE) | obstruction instance is exact/certified | only heuristic → EVIDENCE, not NO_GO |
| `FORMALIZE_EARLY` | Compile definitions/claims early to reveal hidden assumptions | DEFINITION, STATEMENT | FORMALIZED refs + `correspondence_status` | backend accepts the declaration | hidden assumption surfaced → new precondition cell |
| `SYNTHESIZE_DEFINITION` | Propose a concept that compresses repeated patterns; test if it improves statements/proofs/retrieval | ≥2 EXAMPLE/EXPERIMENT/THEOREM | DEFINITION/CONCEPT (DRAFT) | IR type-check + non-collision (`content_hash`) | pure renaming → caught by collision search, scored as non-novel |

**Cross-cutting rules.**
- Output state ceiling is `EVIDENCE`; promotion happens only downstream (MIRADOR Congress gate).
- Cost is accounted per call (`tokens/compute_seconds/usd/tool_calls/wall_clock_s`) and written to the immutable event log.
- Exact arithmetic only for any numeric witness (project rigor rule; a numeric grid is never a proof).
- `TRANSFER` and `CHANGE_REPRESENTATION` depend on retrieval capabilities ProofContext does not yet expose — see blocking decision **B2**.

*Full per-operator preconditions, transform pseudocode, and cost tables are P2
deliverables (see `00_FIRST_RESPONSE.md §10`); this table is the frozen contract
surface they must satisfy.*
