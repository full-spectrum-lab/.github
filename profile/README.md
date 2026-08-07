# Full Spectrum Lab

### Evidence-first governance engineering for AI and complex systems

[English](./README.md) · [简体中文](./README.zh-CN.md)

> Full Spectrum Lab separates **facts**, **exact knowledge versions**, **deterministic evaluation**, **authorization**, **real-world action**, and **replay**.

It is **not** an agent operating system, planner, workflow orchestrator, generic observability platform, RAG knowledge base, or automatic enforcement system. Final real-world action remains with an authorized human, organization, or external business system.

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)

[![Full Spectrum system map](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/product-views/full-spectrum-system-master-map-en-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

## Start from your question

You do not need to understand the repository structure first. Start with the problem you need to make explainable, reproducible or governable.

| Your question | Start here |
|---|---|
| Why did the system reach this conclusion? | [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) |
| Can the evaluation be reproduced exactly? | [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine) |
| Which exact knowledge version was used? | [Knowledge Governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) |
| Who acted, under what capability and boundary? | [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) |
| How can this be applied to another domain? | CASE + Knowledge Pack + Adapter + Skill |
| I need the whole map first | [Question-based public entry](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/start-from-your-question.md) |

## Four independent engineering tracks

| Track | Responsibility | Explicit non-goal |
|---|---|---|
| [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) | Governance semantics and contracts for identity, capability, boundary, evidence and accountability | Not a transport protocol or executor |
| [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine) | Deterministic, reproducible governance evaluation and evidence generation | Not an agent runtime, planner or tool executor |
| [Knowledge Governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) | Exact knowledge identity, version, provenance, lifecycle, conflict and replay | Not RAG, a vector database or CMS |
| [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | Authorized reality input, Observation, Evidence, Audit, Replay and bounded human review | Not APM, generic logging or a production controller |

Engine, Observer and Knowledge Governance can be used independently. When composed, they meet through explicit contracts and adapters—not by turning one product into another.

Supporting repositories: [Enterprise Governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) provides synthetic cases and deployment patterns; [Commons](https://github.com/full-spectrum-lab/full-spectrum-commons) provides public maps, terminology and evidence navigation.

## Release truth

| Project | Public status | Meaning |
|---|---|---|
| Engine | [`v1.4.0` stable](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.4.0) · [`v1.5.0` pre-release](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0) | v1.5 is an enterprise-pilot candidate; Engine 2.x has not started. |
| Observer | [`v0.3.0-beta.1` pre-release](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-beta.1) | Windows x64 beta; evidence, audit/replay and bounded human review; production-ready `NO`. |
| Observer next | `v0.4.0-beta` — designed, not released | Frozen Observer requirements remain authoritative; downstream projects adapt to Observer. |
| Knowledge Governance | [`v0.1.0-alpha` pre-release](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases/tag/v0.1.0-alpha) | Windows x64 technical preview; production-ready `NO`; independently usable. |
| Protocol | Early public draft | Public schemas and conformance checks; no final-standard claim. |
| Industrial case | Designed / fixture-validated | Synthetic, unnamed and not production validated. |

[Machine-readable status](https://github.com/full-spectrum-lab/.github/blob/main/status/public-status.json) · [AI context](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/AI_CONTEXT.md) · [Terminology](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/GLOSSARY.md) · [Evidence taxonomy](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)

## Verify, do not infer

Start with a repository's release page, exact tag, tests and attached evidence. Diagrams explain architecture; they do not prove implementation or production readiness.

- [Run Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start)
- [Inspect Observer v0.3.0-beta.1](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-beta.1)
- [Inspect the synthetic industrial case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap)
- [Read Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

Research and engineering stage. No production, regulatory, legal or customer-validation claim is implied.
