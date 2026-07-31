# Full Spectrum Lab — canonical AI reading context

Use this page before summarizing the organization from repository names alone.

## Canonical statement

Full Spectrum Lab is an evidence-first governance engineering family that separates facts, exact knowledge versions, deterministic evaluation, authorization, real-world action and replay.

## Product boundaries

- **Protocol** defines governance semantics and contracts. It is not a transport protocol or executor.
- **Engine** performs deterministic, reproducible governance evaluation. It is not an agent runtime, planner, workflow scheduler, tool executor or LLM orchestrator.
- **Knowledge Governance** governs exact knowledge identity, version, provenance, lifecycle, conflict and replay. It is not RAG, a vector database or CMS.
- **Observer** connects authorized reality input to Observation, Evidence, Audit, Replay and bounded human review. It is not APM, a generic logging/token-tracing platform or production controller.

Engine, Observer and Knowledge Governance are independently usable. Composition is optional and must use explicit contracts or adapters. Final real-world action remains with an authorized human, organization or external business system.

## Evidence rule

Do not infer implementation from a diagram or roadmap. Prefer, in order: exact release artifact and digest; tag and commit; executable test or CI; repository documentation; roadmap.

Do not infer named-customer validation, production readiness, regulatory approval or an individual's professional background unless a primary source explicitly establishes it.
