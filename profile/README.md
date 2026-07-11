# Full Spectrum Lab

### Open governance protocol and local-first runtime for auditable AI agent behavior

[Website](https://fullspectrumprotocol.com/index.html) · [Protocol Guide](https://fullspectrumprotocol.com/protocols/guide.html) · [Architecture](https://fullspectrumprotocol.com/architecture.html) · [Technical Spec](https://fullspectrumprotocol.com/protocols/tech-spec.html) · [FSHI Case](https://fullspectrumprotocol.com/fshi-index.html)

---

[![Full Spectrum governance overview](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/four-layer-architecture-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

## About

Full Spectrum Lab hosts open-source work for AI governance beyond simple tool calling and agent connectivity.

The project focuses on the layer where AI actions become accountable: who acted, what capability was claimed, what risk was detected, what decision was made, what trace was preserved, and when human review must re-enter the loop.

The current public stack combines protocol schemas, runnable local engine code, enterprise governance cases, diagrams, and cross-repository navigation.

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
| [Governance Chain CLI](https://github.com/full-spectrum-lab/full-spectrum-engine/tree/main/src/governance_chain) | Generates a protocol object chain from raw business input: Governance Event, Canonical Context, Cell Manifest, Output Envelope, Enterprise Writeback, and report. | [Example input](https://github.com/full-spectrum-lab/full-spectrum-engine/tree/main/examples/governance_chain) |

### Enterprise Governance Cases

| Project | What it is | Start |
| --- | --- | --- |
| [full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) | Enterprise AI customer-service governance cases, adapters, human-review workflow, report templates, and deployment guidance. | [Try It Locally](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/try-it-locally.md) |
| [Ecommerce governance case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/ecommerce-knowledge-source-adapter-spec-v0.1.md) | Refund over-commitment and knowledge-source conflict examples for AI customer-service governance. | [Adapter spec](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/ecommerce-knowledge-source-adapter-spec-v0.1.md) |

## What Can I Use Today?

- Run a local governance engine example in `full-spectrum-engine`.
- Generate and validate an ecommerce governance-chain sample with the stdlib-only CLI.
- Read protocol schemas for Governance Event, Canonical Context, Cell Protocol, Output Envelope, and Enterprise Writeback.
- Inspect enterprise-facing customer-service governance examples.
- Use the visual index to understand the four-layer architecture.

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

Full Spectrum is organized around a staged adoption path:

1. Local internal governance engine use
2. Cell-level declaration of identity, capability, boundary, and responsibility
3. Shared protocol objects for audit and interoperability
4. Cross-node compatibility and stronger conformance only when needed

This means an organization can start with one internal AI governance use case first. It does not need to join a full protocol network on day one.

> [Four-Layer Architecture](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/four-layer-architecture-v01.png) · [Why AI Needs a Relationship Protocol](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/protocol-system/why-ai-needs-relationship-protocol.png) · [Full Visual Index](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

## Research & Cases

- [Protocol Guide](https://fullspectrumprotocol.com/protocols/guide.html) — how the protocol objects fit together.
- [Technical Spec](https://fullspectrumprotocol.com/protocols/tech-spec.html) — engineering-facing description of the protocol stack.
- [FSHI Case Entry](https://fullspectrumprotocol.com/fshi-index.html) — AI customer-service quality inspection scenario.
- [Ecommerce governance case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/ecommerce-knowledge-source-adapter-spec-v0.1.md) — refund commitment and knowledge-source conflict examples.

## Community

- Contributions: start from the relevant repository and open an issue or pull request with a narrow change.
- Protocol changes: propose changes in `full-spectrum-protocol` with examples and schema impact.
- Engine changes: keep examples reproducible and tests deterministic.
- Enterprise cases: keep business claims separate from protocol guarantees.

## Current Stage

Full Spectrum Lab is in early public build-out.

Already available:

- public repository split across protocol, engine, enterprise governance, and commons
- local-first engine v1.0 baseline
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
