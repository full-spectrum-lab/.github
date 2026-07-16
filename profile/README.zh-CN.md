# Full Spectrum Lab

### 面向可审计 AI 行为的开放治理协议与本地优先运行时

[English](./README.md) · [简体中文](./README.zh-CN.md)

[运行 Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) · [查看 Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) · [阅读 Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md) · [运行企业案例](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/try-it-locally.md) · [浏览架构图](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

## 当前公开状态

| 项目 | 公开状态 | 准确含义 |
|---|---|---|
| Engine | [`v1.4.0` 正式版](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.4.0) · [`v1.5.0` 预览版](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0) | v1.5.0 是企业试点候选，在 GitHub 中仍标记为 pre-release。 |
| Observer | [`v0.2.0-alpha.2` 预发布](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.2.0-alpha.2) | 当前公开的 Engine v1.0/v1.5 兼容适配版本。 |
| Observer 下一版本 | `v0.3.0-beta` 正在研发，尚未发布 | 本地单用户 Operator Console；规划不等于已交付。 |
| Protocol | 早期公开草案 | 已提供 Schema 与一致性检查，不宣称最终标准地位。 |

文档、实现、测试和 Release 是四种不同状态。只有具备代码、测试、证据和正式 Release 的能力，才能作为公开交付能力对外声明。

## 仓库分工

| 仓库 | 作用 |
|---|---|
| [full-spectrum-protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) | RFC、Schema、Governance Event、I/O Contract、Cell Protocol 与一致性规则 |
| [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine) | 本地优先治理运行时、RiskVector、Runestone、AuditTrace 与治理链 CLI |
| [full-spectrum-observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | Observer 应用、Evidence Store、本地操作流程与 Engine 兼容适配 |
| [full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) | 企业治理案例、Adapter、人工复核与报告模板 |
| [full-spectrum-commons](https://github.com/full-spectrum-lab/full-spectrum-commons) | 架构图、术语、证据状态、研究稿与跨仓导航 |

## 十分钟入口

1. [运行 Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start)；
2. [生成并校验治理对象链](https://github.com/full-spectrum-lab/full-spectrum-engine#governance-chain-cli-ten-minute-runnable)；
3. [验证 Protocol Schema](https://github.com/full-spectrum-lab/full-spectrum-protocol/tree/main/tools)；
4. [查看 Observer 发布状态](https://github.com/full-spectrum-lab/full-spectrum-observer/releases)；
5. [运行电商治理案例](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/blob/main/docs/try-it-locally.md)。

## 研究与证据边界

- [Evidence and Project Status](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md) 区分已实现、假设与未声明能力；
- [WP-001](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/research/working-papers/wp-001-governance-semantics-and-local-observer-engine.md) 是公开工作论文，尚未同行评审；
- [Public Writing and Origins](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-writing-and-origins.md) 提供豆瓣、知乎与项目来源入口；
- [官方网站](https://fullspectrumprotocol.com/) 提供对外阅读入口。

第一代 Observer 可以在企业内部离线运行，不要求加入公共身份、认证或协议网络。它输出分析、预警、报告和审计记录，但不代表企业执行最终业务动作。

