# Full Spectrum Lab

Created at: 2026-07-09 16:02 UTC+8

Last updated at: 2026-09-16 21:20 UTC+8

### Evidence-first governance engineering for AI and complex systems

[English](./README.md) · [简体中文](./README.zh-CN.md)

> Full Spectrum Lab separates **facts**, **exact knowledge versions**, **deterministic evaluation**, **authorization**, **real-world action**, and **replay**.

It is **not** an agent operating system, planner, workflow orchestrator, generic observability platform, RAG knowledge base, or automatic enforcement system. Final real-world action remains with an authorized human, organization, or external business system.

## First visit: a five-minute path

You do not need to understand every concept or read every repository in order. Start with the question you need to answer:

1. **What is Full Spectrum?** Read [Start from Your Question](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/start-from-your-question.md) and [Four Independent Engineering Tracks](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/four-independent-engineering-tracks.md).
2. **Can I run a reproducible example?** Open the [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine) and its [five-minute guide](https://github.com/full-spectrum-lab/full-spectrum-engine/blob/main/docs/getting-started-5min.md).
3. **Where are Evidence, Audit and Replay?** Open [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) and its [Releases](https://github.com/full-spectrum-lab/full-spectrum-observer/releases).
4. **Which exact knowledge version was used?** Open [Knowledge Governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) and its [Releases](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases).
5. **How are identity, permission and responsibility represented?** Open the [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md).
6. **How could this map to an enterprise problem?** Start with the synthetic cases in [Enterprise Governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance); a case is not evidence of customer deployment.

Always preserve this distinction:

```text
Concept != specification != schema != implementation != passing tests
        != fixed-scenario integration != general compatibility != real network != production readiness
```

Repository code, exact Releases, tests and Evidence define current capability. Diagrams and research explain relationships and origins; they do not independently prove implementation.

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)

[![Full Spectrum system map](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/product-views/full-spectrum-system-master-map-en-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

### Observer-centered architecture

[![Observer general system overview](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/observer-general-system-overview-zh-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/observer-general-system-overview-zh-v01.png)

This diagram presents the intended relationship between the Protocol network layer, the Engine subject/evaluation axis, the Knowledge Governance domain axis, the Observer reality/evidence node, and CASE / Pack / Adapter / Skill expansion. It is an architecture view, not proof that every depicted layer, adapter, network or workflow is implemented, integrated, runtime-verified or production-ready.

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

## One model across subjects, knowledge, relationships and domains

Full Spectrum is not limited to one industry or one type of system. Its reusable structure is:

```text
Engine / subject axis  deterministic evaluation across human → Agent/tool → team/system → organization → cross-organization network
Horizontal knowledge   domain material → exact version → Knowledge Pack → CASE / Skill
Protocol relationships who may act → capability → boundary → authorization → evidence → accountability
Domain extension       Core Contracts + Knowledge Pack + CASE + Adapter + Skill + Evidence
```

The Engine/subject axis applies reproducible evaluation across different kinds of subjects while preserving identity, authority and responsibility. The knowledge axis keeps domain knowledge exact and replayable across industries. Protocol connects relationships and boundaries. Observer makes each intersection observable, evidenced, auditable and reviewable. CASE, Pack, Adapter and Skill turn the same governance contracts into domain-specific solutions.

This is an architecture and expansion model—not a claim that a production-scale protocol network, every industry solution or a mature Skill ecosystem already exists. [Read the complete question-based model](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/start-from-your-question.md).

## From a local node to a governed network

Full Spectrum is not a loose toolkit of unrelated components. The tracks share governance invariants, versioned contracts, evidence semantics and responsibility boundaries. A single organization can run a local node and obtain value immediately; network value appears when multiple organizations exchange governed events, decisions and receipts without surrendering their own systems or authority.

```text
One organization       Observe facts → evaluate → Gate / review when supported → its own system acts
Multiple organizations  governed event → remote Gate → local action → disposition receipt
Mature composition      shared evidence + replay + bounded path comparison across the network
```

The network is built and operated by participating enterprises, organizations, public institutions or sovereign participants—not by Full Spectrum as a hosted SaaS network. Full Spectrum provides the method, contracts, node patterns and Engine/Observer capabilities for building it. Its intelligence is the accumulated, verifiable governance memory of participating organizations: exact knowledge, explicit relationships, evidence, decisions, receipts and replayable history. The current public ecosystem is building toward this model; it does not claim that a production-scale network already exists.

Availability is release-specific: architecture direction does not upgrade an unimplemented Gate or network capability to current product fact.

The second-generation direction is for participant-operated protocol nodes / Protocol Executors to invoke Engine and Observer for governance Gates and bounded optimization, while participants' own systems execute approved actions. Full Spectrum does not become the business executor or the owner of the participating network.

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
| Observer latest preview | [`v0.4.0-beta`](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.4.0-beta) | Windows x64 public pre-release; not stable; production-ready `NO`. |
| Observer maintenance line | [`v0.3.0-maintenance.6`](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-maintenance.6) | Validated maintenance candidate; `NOT_RELEASED / PRODUCTION_READY=NO`. |
| Knowledge Governance | [`v0.2.0-alpha` pre-release](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases/tag/v0.2.0-alpha) | Windows x64 candidate; 92/92 engineering tests; Linux/macOS not executed; production-ready `NO`. |
| Protocol | Early public draft | Public schemas and conformance checks; no final-standard claim. |
| Industrial case | Designed / fixture-validated | Synthetic, unnamed and not production validated. |

[Machine-readable status](https://github.com/full-spectrum-lab/.github/blob/main/status/public-status.json) · [AI context](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/AI_CONTEXT.md) · [Terminology](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/GLOSSARY.md) · [Evidence taxonomy](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)

## Verify, do not infer

Start with a repository's release page, exact tag, tests and attached evidence. Diagrams explain architecture; they do not prove implementation or production readiness.

- [Run Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start)
- [Inspect Observer v0.4.0-beta](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.4.0-beta)
- [Inspect the synthetic industrial case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap)
- [Read Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

Research and engineering stage. No production, regulatory, legal or customer-validation claim is implied.
