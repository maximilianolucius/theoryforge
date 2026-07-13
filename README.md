# TheoryForge

**Operator-Guided Autonomous Theory Formation in Mathematics** — the *Discovery
Plane* of the Bourbaki Engine.

> **Status: PLANNING / UNFROZEN. No implementation, no experiments, no
> discoveries.** This repository currently contains the Section-19 first
> response required by the master prompt
> (`09_PROMPT_CLAUDE_PAPER_THEORYFORGE_ARXIV.md`) and a directory skeleton. It
> deliberately does **not** begin implementation or draft conclusions until the
> protocol and manifests are frozen and the blocking decisions are resolved.

## Read this first

- **[`00_FIRST_RESPONSE.md`](00_FIRST_RESPONSE.md)** — the master planning
  document: source inventory, related-work plan, task definition,
  discovery-operator API draft, TheoryBench design, contamination-control plan,
  baseline/ablation matrix, Bang corpus-freeze plan, verification/novelty
  protocol, staged schedule, and the blocking scientific decisions.

## Where TheoryForge sits

TheoryForge generates candidate mathematics; it **cannot promote it**. Authority
is separated and one-way (Bourbaki Engine, `spec/ARCHITECTURE_V2.md`):

```
corpus (frozen) → ProofContext Evidence Bundle → frontier analysis
  → operator selection → candidate generation → exact experiments / CE search
  → formalization / certificate → INDEPENDENT Congress → promoted | structured failure
  → updated corpus + scheduler priors
```

It builds on three existing sibling systems (reused, not reinvented):

| Sibling | Import / conform | Provides |
|---|---|---|
| `../mirador` | import `mirador` | Mathematical Cell IR, content-hash identity, event log, invalidation, transition authority |
| `../proof-context` | import `proofcontext` | dependency-aware retrieval → hashed Evidence Bundle |
| `../congressbench` | conform to `Reviewer` ABC + `review.schema.json` | independent fresh-context review contract |

Main integrated case study: the **Bang affine plank campaign**
(`../../bang-plank-euler-jacobi`) — a submission-ready manuscript with one
machine-verified certificate. See `case_studies/bang/`.

## Directory layout (per prompt §13)

`constitution/ schema/ operators/ retrieval/ generators/ experiments/
counterexamples/ formalization/ scheduler/ congress/ theorybench/
case_studies/bang/ results/ paper/ audits/ src/theoryforge/`

## License

MIT (consistent with the sibling projects). See `LICENSE`.
