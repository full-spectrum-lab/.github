# Full Spectrum Lab

### 面向可审计 AI 与企业风险的本地优先观察和治理证据栈

[English](./README.md) · [简体中文](./README.zh-CN.md)

[查看 Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) · [运行 Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) · [查看工业案例](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) · [阅读 Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

**Protocol 定义治理契约，Engine 生成确定性分析与证据，Observer 将获得授权的本地事实连接到 Replay 与有边界的人工复核。**

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)

[![三层入口与三大核心组件](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/three-entry-three-core-components-zh-v10.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/three-entry-three-core-components.md)

## 选择入口

| 从哪里开始 | 回答什么问题 | 得到什么 |
|---|---|---|
| [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | 不替换业务系统，如何观察 AI 与企业风险？ | 本地证据、审计/回放和人工复核边界 |
| [工业案例](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) | 如何安全表达跨系统证据缺口？ | 带有禁止写回约束的合成设计 fixture |
| [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) | 治理计算能否复现？ | 确定性输出、fixture、报告和 CI |
| [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md) | 身份、能力、边界、证据和责任如何表达？ | Schema、样例与一致性检查 |

## 当前公开状态

| 项目 | 状态 | 准确含义 |
|---|---|---|
| Engine | [`v1.4.0` 稳定版](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.4.0) · [`v1.5.0` 预发布](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0) | v1.5 是企业试点候选；Engine 2.x 尚未启动。 |
| Observer | [`v0.2.0-alpha.2` 预发布](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.2.0-alpha.2) | 已验证 Engine v1.0/v1.5 兼容层；仍然只做观察。 |
| Observer 下一版本 | `v0.3.0-beta` — 研发中、尚未发布 | 本地单用户 Operator Console；规划不等于交付。 |
| Protocol | 早期公开草案 | 已公开 Schema 和一致性检查，不宣称最终标准。 |
| 工业 R04 | 设计完成 / fixture 已校验 | 合成案例、无具名客户、未经生产验证。 |

[机器可读版本事实源](https://github.com/full-spectrum-lab/.github/blob/main/status/public-status.json) · [证据状态词典](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)

## 十分钟验证

| 目标 | 入口 | 证据 |
|---|---|---|
| 运行确定性治理计算 | [Engine Quick Start](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start) | 本地产物与测试 |
| 生成 Protocol 对象链 | [Governance Chain CLI](https://github.com/full-spectrum-lab/full-spectrum-engine#governance-chain-cli-ten-minute-runnable) | 通过 Schema 校验的对象链与报告 |
| 查看有边界的工业场景 | [R04 拧紧证据缺口](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap) | 输入、主体、Profile、预期 Observation、Evidence 和复核边界 |
| 查看 Observer 已发布证据 | [Observer v0.2.0-alpha.2](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.2.0-alpha.2) | Release、门禁与兼容性证据 |

## 五个核心仓库

| 仓库 | 职责 |
|---|---|
| [full-spectrum-observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | 本地应用、Evidence Store、Audit/Replay 与操作流程 |
| [full-spectrum-engine](https://github.com/full-spectrum-lab/full-spectrum-engine) | 确定性治理运行时与治理链 CLI |
| [full-spectrum-protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) | 规范 Schema、技术说明和一致性规则 |
| [full-spectrum-enterprise-governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) | 企业/工业合成案例和人工复核模式 |
| [full-spectrum-commons](https://github.com/full-spectrum-lab/full-spectrum-commons) | 架构图、证据状态、研究稿和引用元数据 |

## 公开边界

- 本地优先、观察优先，不默认上传企业完整数据库；
- 当前公开 Observer 不执行最终业务或生产动作；
- 架构图、设计文档和 Wiki 不等于已交付能力；
- 除非有明确证据记录，公开案例均为合成或脱敏重构；
- 不宣称最终标准、监管批准或生产合规保证。

[研究](https://github.com/full-spectrum-lab/full-spectrum-commons/tree/main/research) · [引用](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/CITATION.cff) · [公开写作](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-writing-and-origins.md) · [官网](https://fullspectrumprotocol.com/)
