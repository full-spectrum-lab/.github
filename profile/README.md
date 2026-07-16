# Full Spectrum Lab

### Local-first observation and governance evidence for auditable AI and enterprise risk

[English](./README.md) · [简体中文](./README.zh-CN.md)

[Inspect Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) · [Run Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) · [Try a synthetic industrial case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) · [Read Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

Full Spectrum Lab builds an open, local-first Observer stack for auditable AI and enterprise risk. **Protocol defines the governance contract, Engine produces deterministic analysis and evidence, and Observer connects those capabilities to a bounded human-review workflow.**

| Start from | Question answered | Public entry |
| --- | --- | --- |
| **Enterprise** | How do we observe AI behavior, decisions and responsibility without replacing business systems? | [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) |
| **Industrial** | How do we detect cross-system risk while data remains inside the organization? | [Synthetic tightening-evidence case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) |
| **Protocol** | How are identity, capability, boundary, evidence and accountability represented? | [Protocol start](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md) |

[![Three entries and three core components](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/three-entry-three-core-components-zh-v10.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/three-entry-three-core-components.md)

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)
[![Engine v1.5.0](https://img.shields.io/badge/engine-v1.5.0-success)](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0)
[![Observer v0.2.0-alpha.2](https://img.shields.io/badge/observer-v0.2.0--alpha.2-orange)](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.2.0-alpha.2)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://github.com/full-spectrum-lab/full-spectrum-engine)
[![Local First](https://img.shields.io/badge/runtime-local--first-5b5bd6)](https://github.com/full-spectrum-lab/full-spectrum-engine#current-release-boundary)

[Evidence & Status](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md) · [Research](https://github.com/full-spectrum-lab/full-spectrum-commons/tree/main/research) · [Public Writing](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-writing-and-origins.md) · [Website](https://fullspectrumprotocol.com/index.html)

## Release truth

| Project | Public status | What it means |
| --- | --- | --- |
| Engine | [`v1.4.0` stable](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.4.0) · [`v1.5.0` preview](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0) | v1.5.0 is an enterprise-pilot candidate and remains a GitHub pre-release. |
| Observer | [`v0.2.0-alpha.2` pre-release](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.2.0-alpha.2) | Current public compatibility-adapter release; local-first and observer-only. |
| Observer next | `v0.3.0-beta` — in development, not released | Local single-user Operator Console; roadmap status is not a shipped capability. |
| Protocol | Early public draft | Schemas and conformance checks are available; no final-standard claim. |

**Documentation, implementation and release are separate states.** A roadmap entry does not become a public capability until code, tests, evidence and a Release are all present.

## About

Full Spectrum Lab hosts open-source work for governance beyond simple tool calling and agent connectivity.

The project focuses on the layer where AI actions become accountable: who acted, what capability was claimed, what risk was detected, what decision was made, what trace was preserved, and when human review must re-enter the loop.

The current public stack combines protocol schemas, runnable local engine code, an Observer application foundation, synthetic enterprise cases, diagrams, and cross-repository navigation. Public examples are not presented as production validation unless an explicit evidence record says so.

## Projects

### Protocol & Conformance

| Project | What it is | Start |
| --- | --- | --- |
| [full-spectrum-protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) | Source of truth for RFCs, schemas, Governance Events, I/O Contract, Cell Protocol, output envelopes, and conformance rules. | [START_HERE](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md) |
| [full-spectrum-commons](https://github.com/full-spectrum-lab/full-spectrum-commons) | Shared diagrams, glossary, visual index, public architecture maps, and cross-repository navigation. | [Visual Index](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md) |

### Runtime & Developer Tools

| Project | What it is | Start |
| --- | --- | --- |
| [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine) | Local-first runtime for RiskVector, Runestone, AuditTrace, reproducible simulation, and governance-chain CLI generation. | [Quick Start](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) |
| [full-spectrum-observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | Local-first Observer foundation kernel plus the v0.2 Engine v1.0/v1.5 Compatibility Adapter. v0.2.0-alpha.2 preserves version, Profile, UNKNOWN, reason-code, Replay and Audit semantics and remains observer-only. | [v0.2.0-alpha.2](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.2.0-alpha.2) |
| [Governance Chain CLI](https://github.com/full-spectrum-lab/full-spectrum-engine/tree/main/src/governance_chain) | Generates a protocol object chain from raw business input: Governance Event, Canonical Context, Cell Manifest, Output Envelope, Enterprise Writeback, and report. | [Example input](https://github.com/full-spectrum-lab/full-spectrum-engine/tree/main/examples/governance_chain) |

### Enterprise Governance Cases

| Project | What it is | Start |
| --- | --- | --- |
| [full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) | Synthetic enterprise and industrial governance cases, adapters, human-review workflow, report templates, and deployment guidance. | [Industrial case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) |
| [Ecommerce governance case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/ecommerce-knowledge-source-adapter-spec-v0.1.md) | Refund over-commitment and knowledge-source conflict examples for AI customer-service governance. | [Adapter spec](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/ecommerce-knowledge-source-adapter-spec-v0.1.md) |

## What Can I Use Today?

- Run a local governance engine example in `full-spectrum-engine`.
- Generate and validate an ecommerce governance-chain sample with the stdlib-only CLI.
- Read protocol schemas for Governance Event, Canonical Context, Cell Protocol, Output Envelope, and Enterprise Writeback.
- Inspect enterprise-facing customer-service governance examples.
- Use the visual index to understand the four-layer architecture.
- Inspect the released Observer v0.1 foundation kernel and the v0.2 Engine v1.0/v1.5 Compatibility Adapter; both remain local-first and observer-only.

## Start in 10 Minutes

| Goal | Start | Result |
| --- | --- | --- |
| Run the local observer engine | [Engine Quick Start](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) | Deterministic simulation and audit artifacts |
| Inspect the Observer application boundary | [Observer repository](https://github.com/full-spectrum-lab/full-spectrum-observer) | Source, architecture, tests and gated release evidence |
| Generate a governance object chain | [Governance Chain CLI](https://github.com/full-spectrum-lab/full-spectrum-engine#governance-chain-cli-ten-minute-runnable) | Schema-validated ecommerce objects and report |
| Validate protocol objects | [Protocol schema tools](https://github.com/full-spectrum-lab/full-spectrum-protocol/tree/main/tools) | Machine-readable conformance result |
| Inspect an enterprise case | [Ecommerce case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/ecommerce-knowledge-conflict) | Synthetic/desensitized review workflow |
| Understand the system | [Visual Index](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md) | Architecture and repository map |

## Open Capabilities

| Capability | Where it lives |
| --- | --- |
| Governance-chain generation and validation | `full-spectrum-engine` |
| Governance Event, I/O and audit schemas | `full-spectrum-protocol` |
| Local Observer Engine, RiskVector and Runestone | `full-spectrum-engine` |
| Observer application, evidence store and local operator workflow | `full-spectrum-observer` |
| Ecommerce governance and human-review cases | `full-spectrum-enterprise-governance` |
| Evidence status, diagrams and research index | `full-spectrum-commons` |

## Core Protocol Objects

| Object | Purpose | Link |
| --- | --- | --- |
| Identity Claim | Minimal declaration of who or what is acting. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/identity-claim.md) |
| Capability Declaration | Minimal declaration of what a subject can and cannot do. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/capability-declaration.md) |
| Governance Event | Minimal record for an AI-related action before risk interpretation. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/governance-event.md) |
| Canonical Context | Normalized context object used before governance decisions. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/canonical-context.md) |
| L1 Cell Protocol | Cell-level declaration for subject, capability, boundaries, and lifecycle. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/l1-cell-protocol.md) |
| Governance Output Envelope | Decision envelope emitted after governance interpretation. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/governance-output-envelope.md) |
| Enterprise Writeback | Enterprise-facing writeback object for review, routing, and action status. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/enterprise-writeback.md) |
| Audit Trace | Trace for review, escalation, decision, execution, or recovery. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/audit-trace.md) |

## Framework

Full Spectrum follows an observer-first adoption path:

1. Run the local Observer Engine on enterprise-controlled data.
2. Add an optional enterprise-local subject declaration.
3. Use stable I/O contracts and Profile-driven evaluation.
4. Add replay and audit hardening before controlled enterprise trials.
5. Consider certified identity or cross-node interoperability only when needed.

An organization does not need public DID, community membership, external certification, or a protocol network to use the first-generation observer. The observer produces analysis, warnings, reports, and audit records; it does not execute final enterprise actions.

> [Four-Layer Architecture](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/four-layer-architecture-v01.png) · [Why AI Needs a Relationship Protocol](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/protocol-system/why-ai-needs-relationship-protocol.png) · [Full Visual Index](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

## Research & Cases

- [WP-001: Governance Semantics and a Local-First Observer Engine](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/research/working-papers/wp-001-governance-semantics-and-local-observer-engine.md) — public working paper, not peer reviewed.
- [Evidence and Project Status](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md) — what is implemented, hypothesized, or not claimed.
- [Protocol Guide](https://fullspectrumprotocol.com/protocols/guide.html) — how the protocol objects fit together.
- [Technical Spec](https://fullspectrumprotocol.com/protocols/tech-spec.html) — engineering-facing description of the protocol stack.
- [FSHI Case Entry](https://fullspectrumprotocol.com/fshi-index.html) — AI customer-service quality inspection scenario.
- [Ecommerce governance case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/ecommerce-knowledge-source-adapter-spec-v0.1.md) — refund commitment and knowledge-source conflict examples.

## Public Writing & Origins

- [《开窗手册：全频谱、接口与静默封神》](https://read.douban.com/column/72712765/) — narrative origins and public-facing writing.
- [知乎专栏](https://www.zhihu.com/column/c_2008500556897998127) — Chinese essays on AI governance, civilization dynamics, and Full Spectrum.
- [Editorial status of legacy manuscripts](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/research/working-papers/legacy-manuscript-review.md) — why older manuscripts are not presented as peer-reviewed evidence.

These materials provide context and intellectual background. Normative specifications remain in `full-spectrum-protocol`; runnable claims remain tied to code and tests.

## Community

- [Open an issue](https://github.com/orgs/full-spectrum-lab/repositories) in the relevant repository with a narrow, reproducible question.
- [Propose a protocol change](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/CONTRIBUTING.md) with examples and schema impact.
- Contribute a counterexample that challenges a rule, Profile, example, or research claim.
- Add an enterprise case while keeping business claims separate from protocol guarantees.
- Read [Public Writing and Origins](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-writing-and-origins.md) for the Chinese public-reading path.

## Current Stage

Full Spectrum Lab is in early public build-out.

Already available:

- public repository split across protocol, engine, enterprise governance, and commons
- local-first Engine v1.5.0 enterprise-pilot candidate
- Observer v0.2.0-alpha.2 released as the Engine v1.0/v1.5 compatibility layer after 79 compatibility tests, independent negative reproduction and Foundation gate verification
- governance-chain CLI for reproducible ecommerce protocol objects
- protocol schemas and RFC scaffolding
- enterprise customer-service governance examples

Not claimed yet:

- no final standard status
- no production compliance guarantee
- no complete protocol-network implementation
- no claim that every enterprise package is production-ready

---

Built by Full Spectrum Lab for auditable human-AI and multi-agent governance.
