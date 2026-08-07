# Full Spectrum Lab

### 面向 AI 与复杂系统的证据优先治理工程体系

[English](./README.md) · [简体中文](./README.zh-CN.md)

> Full Spectrum Lab 用工程契约分离**事实、精确知识版本、确定性判断、授权、现实行动与事后回放**。

它不是 Agent 操作系统、任务规划器、工作流编排平台、通用可观测平台、RAG 知识库或自动处罚系统。现实行动始终由获得授权的人、组织或外部业务系统完成。

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)

[![全频谱体系总图](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/product-views/full-spectrum-system-master-map-zh-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

## 从你的问题开始

你不需要先读懂仓库结构。先从你希望被解释、复算或治理的真实问题进入。

| 你的问题 | 建议入口 |
|---|---|
| 系统为什么得出这个结论？ | [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) |
| 这个判断能否精确复算？ | [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine) |
| 当时究竟使用了哪个知识版本？ | [Knowledge Governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) |
| 谁以什么能力、在什么边界内行动？ | [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) |
| 怎样把它扩展到另一个行业？ | CASE + Knowledge Pack + Adapter + Skill |
| 我想先看完整体系 | [按问题组织的公共入口](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/start-from-your-question.zh-CN.md) |

## 一个贯穿主体、知识、关系与行业的模型

全频谱不局限于某个行业或某类系统。它可复用的结构是：

```text
Engine/主体纵轴 对人 → Agent/工具 → 团队/系统 → 组织 → 跨组织网络进行可复算判断
知识横轴      行业材料 → 精确版本 → Knowledge Pack → CASE / Skill
Protocol 网络 谁可以行动 → 能力 → 边界 → 授权 → 证据 → 责任
行业扩展      Core Contracts + Knowledge Pack + CASE + Adapter + Skill + Evidence
```

Engine/主体纵轴把可复算判断贯穿不同类型的主体，同时保持身份、授权和责任连续；知识横轴让不同行业的知识依据保持精确、可追溯、可回放；Protocol 连接主体间的关系与边界；Observer 让每个交叉点可观察、可留证、可审计、可复核；CASE、Pack、Adapter 和 Skill 把同一套治理合同扩展为行业方案。

这是架构与扩展模型，不代表生产级协议网络、所有行业方案或成熟 Skill 生态已经完成。[阅读完整的按问题组织模型](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/start-from-your-question.zh-CN.md)。

## 从单组织节点到治理网络

全频谱不是由彼此无关组件构成的松散工具箱。各条轨道共享治理不变量、版本化契约、证据语义和责任边界。单个组织可以先运行本地节点并获得价值；多个组织接入后，可以在不交出各自系统和行动权的前提下交换受治理的事件、判断和回执，形成网络价值。

```text
单个组织      Observe 事实 → 评估 → 在版本支持时 Gate / 复核 → 组织自己的系统执行
多个组织      治理事件 → 对方 Gate → 本地动作 → Disposition Receipt
成熟组合      共享证据 + 回放 + 受约束的跨网络候选路径比较
```

这个网络不是一个集中式自动大脑。它的“智能”来自各组织连接后累积的、可验证的治理记忆：精确知识、明确关系、证据、判断、回执和可回放历史。当前公开生态正在朝这个模型建设，不宣称生产级网络已经形成。

具体能力以各版本 Release Evidence 为准：架构方向不能把尚未实现的 Gate 或网络能力升级为当前产品事实。

## 四条可独立使用的工程轨道

| 轨道 | 职责 | 明确不做什么 |
|---|---|---|
| [Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol) | 身份、能力、边界、证据和责任等治理语义与契约 | 不是通信传输协议，也不执行行动 |
| [Engine](https://github.com/full-spectrum-lab/full-spectrum-engine) | 可复算的确定性治理判断与证据生成 | 不是 Agent Runtime、Planner 或工具执行器 |
| [Knowledge Governance](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance) | 精确知识身份、版本、来源、生命周期、冲突与回放 | 不是 RAG、向量数据库或 CMS |
| [Observer](https://github.com/full-spectrum-lab/full-spectrum-observer) | 授权现实输入、Observation、Evidence、Audit、Replay 与有边界的人工复核 | 不是 APM、通用日志平台或生产控制器 |

Engine、Observer 和 Knowledge Governance 均可独立使用。组合使用时通过显式契约和 Adapter 对接，不改变各自冻结的产品边界。

支撑仓库：[Enterprise Governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) 提供合成案例与部署模式；[Commons](https://github.com/full-spectrum-lab/full-spectrum-commons) 提供公共图谱、术语和证据导航。

## 当前公开状态

| 项目 | 状态 | 准确含义 |
|---|---|---|
| Engine | [`v1.4.0` 稳定版](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.4.0) · [`v1.5.0` 预发布](https://github.com/full-spectrum-lab/full-spectrum-engine/releases/tag/v1.5.0) | v1.5 为企业试点候选；Engine 2.x 尚未启动。 |
| Observer | [`v0.3.0-beta.1` 预发布](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-beta.1) | Windows x64 Beta；证据、审计/回放与受约束人工复核；生产就绪：否。 |
| Observer 下一版本 | `v0.4.0-beta` — 已设计、尚未发布 | Observer 冻结需求保持不变；下游项目适配 Observer。 |
| Knowledge Governance | [`v0.1.0-alpha` 预发布](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases/tag/v0.1.0-alpha) | Windows x64 技术预览；生产就绪：否；可独立使用。 |
| Protocol | 早期公开草案 | 已公开 Schema 与一致性检查，不宣称最终标准。 |
| 工业案例 | 设计完成 / fixture 已验证 | 完全合成、无具名客户、未经生产验证。 |

[机器可读状态](https://github.com/full-spectrum-lab/.github/blob/main/status/public-status.json) · [AI 阅读上下文](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/AI_CONTEXT.md) · [术语表](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/GLOSSARY.md) · [证据状态词典](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)

## 请验证，不要猜测

公开事实以各仓库 Release、精确 Tag、测试和随附证据为准。架构图用于解释关系，不等于功能已实现或已经生产就绪。

- [运行 Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start)
- [查看 Observer v0.3.0-beta.1](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-beta.1)
- [查看合成工业案例](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap)
- [阅读 Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

当前处于研究与工程验证阶段，不构成生产、监管、法律或客户验证声明。
