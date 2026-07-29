# Full Spectrum Lab

### Local-first observation and governance evidence for auditable AI and enterprise risk

[English](./README.md) · [简体中文](./README.zh-CN.md)

[Inspect Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) · [Run Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) · [Try the industrial case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) · [Read Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

**Protocol defines governance contracts. Engine produces deterministic analysis and evidence. Observer connects authorized local facts to replay and bounded human review.**

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)

[![Three entries and three core components](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/three-entry-three-core-components-zh-v10.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/three-entry-three-core-components.md)

<details>
<summary><strong>Open the full system map</strong> — research-to-engineering context and product boundaries</summary>

[![Full Spectrum system master map](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/product-views/full-spectrum-system-master-map-en-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

The map is an orientation aid. Engine, Observer and Knowledge Governance are independently usable products; composition is optional and release truth remains repository-specific.
</details>

## Choose an entry

| Start from | Question | Result |
|---|---|---|
| [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | How can an organization observe AI and business risk without replacing its systems? | Local evidence, audit/replay and human-review boundary |
| [Industrial case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) | How can cross-system evidence gaps be represented safely? | Synthetic designed fixture with explicit no-writeback controls |
| [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) | Can the governance calculation be reproduced? | Deterministic output, fixtures, reports and CI |
| [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md) | How are identity, capability, boundary, evidence and accountability expressed? | Schemas, examples and conformance checks |
| [Knowledge Governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) | How can knowledge identity, version, lifecycle and evidence be governed locally? | Fixed knowledge governance core and deterministic evidence |

## Release truth

| Project | Public status | Meaning |
|---|---|---|
| Engine | [`v1.4.0` stable](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.4.0) · [`v1.5.0` pre-release](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0) | v1.5 is an Enterprise Pilot Candidate; Engine 2.x has not started. |
| Observer | [`v0.3.0-beta` pre-release](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-beta) | Verified Windows x64 Operator Console, local evidence, audit/replay and bounded human review; production-ready `NO`. |
| Observer next | `v0.4.0-beta` — designed, not released | Continues the frozen Observer product baseline; downstream projects adapt to it. |
| Protocol | Early public draft | Public schemas and conformance checks; no final-standard claim. |
| Knowledge Governance | [`v0.1.0-alpha` pre-release](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases/tag/v0.1.0-alpha) | Windows x64 verified; production-ready `NO`; no Observer/Engine dependency. |
| Industrial R04 | Designed / fixture-validated | Synthetic, no named customer, not production validated. |

[Machine-readable public status](https://github.com/full-spectrum-lab/.github/blob/main/status/public-status.json) · [Evidence taxonomy](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)

## Verify something in ten minutes

| Goal | Start | Evidence |
|---|---|---|
| Run deterministic governance | [Engine Quick Start](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) | Local artifacts and tests |
| Generate a protocol object chain | [Governance Chain CLI](https://github.com/full-spectrum-lab/full-spectrum-engine#governance-chain-cli-ten-minute-runnable) | Schema-validated object chain and report |
| Inspect a bounded industrial scenario | [R04 tightening evidence gap](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) | Input, subjects, profile, expected observation, evidence and review boundary |
| Check released Observer evidence | [Observer v0.3.0-beta](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-beta) | Package SHA, identity, manifest, self-verification and independent retest |

## Repositories

| Repository | Responsibility |
|---|---|
| [full-spectrum-observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | Local application, evidence store, audit/replay and operator workflow |
| [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine) | Deterministic governance runtime and governance-chain CLI |
| [full-spectrum-protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) | Normative schemas, specifications and conformance rules |
| [full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) | Synthetic enterprise/industrial cases and human-review patterns |
| [full-spectrum-commons](https://github.com/full-spectrum-lab/full-spectrum-commons) | Architecture maps, evidence status, research and citation metadata |
| [full-spectrum-knowledge-governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) | Independent local-first knowledge identity, lifecycle, resolution and evidence |

## Public boundary

- Local-first and observation-first; no default upload of enterprise databases.
- The public Observer line does not execute final business or production actions.
- A diagram, design or Wiki page is not a shipped capability.
- Public cases are synthetic or desensitized unless an explicit evidence record says otherwise.
- No final-standard, regulatory-approval or production-compliance claim.

[Research](https://github.com/full-spectrum-lab/full-spectrum-commons/tree/main/research) · [Citation](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/CITATION.cff) · [Public writing](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-writing-and-origins.md) · [Website](https://fullspectrumprotocol.com/)

Built for auditable human–AI and multi-agent governance.
