# Full Spectrum Lab

Open governance protocol and local-first runtime for auditable AI agent behavior, Governance Events, RiskVector, human review, and enterprise AI governance.

**[Website](https://fullspectrumprotocol.com/index.html)** · **[Quick Start](https://github.com/full-spectrum-lab/full-spectrum-engine)** · **[Visual Index](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)** · **[Protocol Guide](https://fullspectrumprotocol.com/protocols/guide.html)** · **[Architecture](https://fullspectrumprotocol.com/architecture.html)**

Full Spectrum Lab builds an open protocol stack for AI-era governance: schemas, adapters, local runtime, enterprise cases, audit traces, and human-review workflows.

## Projects

| Project | What it is | Start |
|---|---|---|
| **[full-spectrum-protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol)** | Source of truth for RFCs, schemas, Governance Events, I/O Contract, Cell Protocol and conformance rules. | [START_HERE](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md) |
| **[full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine)** | Local-first runtime for RiskVector, Runestone, AuditTrace, reports and reproducible simulation. | [Quick Start](https://github.com/full-spectrum-lab/full-spectrum-engine) |
| **[full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance)** | Enterprise AI customer-service governance cases, adapters, reports and human-review workflow. | [Try It Locally](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/try-it-locally.md) |
| **[full-spectrum-commons](https://github.com/full-spectrum-lab/full-spectrum-commons)** | Diagrams, ecosystem maps, glossary, public entry materials and cross-repo navigation. | [Visual Index](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md) |

## What can I use today?

- **[Run a local governance example](https://github.com/full-spectrum-lab/full-spectrum-engine)** — clone the engine and run a synthetic scenario in minutes.
- **[Validate a Governance Event](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/governance-event.md)** — read the minimal action record spec.
| Canonical Context | Normalized, governance-ready view the adapter produces from raw input (actor, action, authority, facts, unknowns, risk axes, privacy). | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/canonical-context.md) |
- **[Try an ecommerce AI customer-service case](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/cases/refund-overcommitment/README.md)** — refund over-commitment example.
- **[Inspect RiskVector / AuditTrace outputs](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/audit-trace.md)** — see the trace spec.
- **[View the four-layer architecture diagrams](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)** — start from the shared visual index.

## Core Specs

| Spec | Purpose | Link |
|---|---|---|
| Identity Claim | Minimal declaration of who or what is acting. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/identity-claim.md) |
| Capability Declaration | Minimal declaration of what a subject can and cannot do. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/capability-declaration.md) |
| Governance Event | Minimal record for an AI-related action before risk interpretation. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/governance-event.md) |
| Risk Alert | Minimal object for detected or suspected reviewable risk. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/risk-alert.md) |
| Audit Trace | Minimal trace for review, escalation, decision, execution, or recovery. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/audit-trace.md) |
| I/O Contract | Minimal mapping contract from business input/output to governance objects via a Business Adapter. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/io-contract.md) |
| L1 Cell Protocol | Subject access, identity tiering and certification domain before entering governance workflows. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/l1-cell-protocol.md) |
| Governance Output Envelope | Standard engine output object bundling result, risk vector, safety action, writeback, privacy, conformance. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/governance-output-envelope.md) |
| Enterprise Writeback | Enterprise-consumable decision object gating auto-reply, commitment and execution. | [spec](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/enterprise-writeback.md) |
| All specifications | Index of current protocol objects. | [specs/README](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/specs/README.md) |

These four specs are now available in `full-spectrum-protocol/specs`.

## Use Cases

- **[AI customer-service refund over-commitment](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/cases/refund-overcommitment/README.md)** — when the AI promises a refund it cannot authorize.
- **[Ecommerce knowledge-source conflict](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/cases/ecommerce-knowledge-conflict/README.md)** — conflicting product knowledge surfaces in replies.
- **[Human review workflow](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/try-it-locally.md)** — how human review re-enters the loop.
- **[Local trial case pack](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/local-trial-case-pack.md)** — run a desensitized case locally.

## Framework & Research

- **[Four-Layer Architecture](https://fullspectrumprotocol.com/architecture.html)** — the recursive governance stack.
- **[Protocol Guide](https://fullspectrumprotocol.com/protocols/guide.html)** — how the protocol fits together.
- **[Technical Spec](https://fullspectrumprotocol.com/protocols/tech-spec.html)** — engineering-facing details.
- **[FSHI case entry](https://fullspectrumprotocol.com/fshi-index.html)** — AI customer-service quality inspection use case.
- **[Protocol Outline & RFCs](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)** — start from START_HERE.

## Community

- **[Official site](https://fullspectrumprotocol.com/index.html)** — overview, architecture, protocol guide.
- **[Contributing](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/CONTRIBUTING.md)** — how to propose changes.
- **[Governance](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/GOVERNANCE.md)** — how decisions are made.

## Current Stage

Full Spectrum Lab is in early public build-out.

Current focus:

- protocol schemas and RFCs
- local-first engine preview
- enterprise AI customer-service examples
- conformance and testing guides

Not claimed yet:

- no final standard status
- no production compliance guarantee
- no complete protocol-network implementation
