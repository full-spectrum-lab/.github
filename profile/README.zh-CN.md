# Full Spectrum Lab

创建时间：2026-07-16 17:35 UTC+8

最后更新时间：2026-09-16 22:05 UTC+8

### 面向 AI 与复杂系统的证据优先治理工程体系

[English](./README.md) · [简体中文](./README.zh-CN.md)

> Full Spectrum Lab 用工程契约分离**事实、精确知识版本、确定性判断、授权、现实行动与事后回放**。

它不是 Agent 操作系统、任务规划器、工作流编排平台、通用可观测平台、RAG 知识库或自动处罚系统。现实行动始终由获得授权的人、组织或外部业务系统完成。

## 公共状态头

| 字段 | 当前值 |
|---|---|
| `ROLE` | 组织级公共入口和跨仓库导航 |
| `STATUS` | 当前有效的公共理解页面 |
| `CURRENT_CAPABILITY` | 五分钟入口、仓库边界、版本真相和证据导航 |
| `NOT_CLAIMED` | 运行时权限、协议权威、生产认证或自动代表项目发言 |
| `PRODUCTION_READY` | 本导航页不适用；各产品以具体 Release 为准，当前生态不宣称整体生产就绪 |
| `START_HERE` | [五分钟阅读路径](#第一次来到全频谱五分钟阅读路径) · [公共架构图](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-architecture-map.zh-CN.md) |

## 第一次来到全频谱：五分钟阅读路径

你不需要先理解全部概念，也不需要依次读完所有仓库。先选择你现在最想解决的问题：

1. **我想先知道全频谱是什么**：阅读[从你的问题开始](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/start-from-your-question.zh-CN.md)和[四条可独立使用的工程轨道](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/four-independent-engineering-tracks.md)。
2. **我想运行一个可复算示例**：进入 [Engine 中文说明](https://github.com/full-spectrum-lab/full-spectrum-engine/blob/main/README.zh-CN.md)和[五分钟入门](https://github.com/full-spectrum-lab/full-spectrum-engine/blob/main/docs/getting-started-5min.md)。
3. **我想查看证据、审计和回放**：进入 [Observer 中文说明](https://github.com/full-spectrum-lab/full-spectrum-observer/blob/main/README.zh-CN.md)和 [Observer Releases](https://github.com/full-spectrum-lab/full-spectrum-observer/releases)。
4. **我想确认使用了哪一份知识**：进入 [Knowledge Governance 中文入口](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/blob/master/README.zh-CN.md)和 [KG Releases](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases)。
5. **我想研究身份、权限和责任协议**：进入 [Protocol 中文说明](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/README.zh-CN.md)和 [Protocol 起点](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)。
6. **我想用于企业或行业问题**：从 [Enterprise Governance](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance) 的合成案例开始；案例不等于真实客户部署。

阅读时请始终区分：

```text
概念设想 ≠ 协议规范 ≠ Schema ≠ 代码实现 ≠ 测试通过
         ≠ 固定场景组合验证 ≠ 一般兼容 ≠ 真实网络 ≠ 生产就绪
```

公开能力以对应仓库的固定代码、Release、测试和 Evidence 为准。架构图和研究文章用于解释关系与来源，不能单独证明功能已经实现。

- [一张图理解公共架构](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/public-architecture-map.zh-CN.md)
- [常见误读与准确边界](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/MISINTERPRETATION_GUARD.zh-CN.md)
- [七条观察路径](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/research/civilization-systems-architecture/09_Full_Spectrum多尺度理解模型_七条观察路径.md)
- [陌生访客独立复核清单](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/external-visitor-review.zh-CN.md)

[![Engine CI](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-engine/actions/workflows/ci.yml)
[![Protocol Schemas](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-protocol/actions/workflows/schema-check.yml)
[![Observer CI](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml/badge.svg)](https://github.com/full-spectrum-lab/full-spectrum-observer/actions/workflows/foundation-gates.yml)

[![全频谱体系总图](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/product-views/full-spectrum-system-master-map-zh-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/visual-index.md)

### Observer 通用体系架构

[![Observer 通用体系总览](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/observer-general-system-overview-zh-v01.png?raw=1)](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/diagrams/architecture/observer-general-system-overview-zh-v01.png)

本图用于说明 Protocol 网络层、Engine 主体/判断纵轴、Knowledge Governance 知识横轴、Observer 现实与证据节点，以及 CASE / Pack / Adapter / Skill 扩展之间的目标关系。它是架构说明图，不代表当前版本已经实现图中全部层级、适配器、网络或流程，也不等于运行验证或生产就绪。

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

这个网络由参与的企业、组织、公共机构或国家级参与方自己建设和运营，不是由全频谱托管的 SaaS 网络。全频谱提供建网方法、契约、节点模式以及 Engine/Observer 能力。网络的“智能”来自参与组织累积的、可验证的治理记忆：精确知识、明确关系、证据、判断、回执和可回放历史。当前公开生态正在朝这个模型建设，不宣称生产级网络已经形成。

具体能力以各版本 Release Evidence 为准：架构方向不能把尚未实现的 Gate 或网络能力升级为当前产品事实。

第二代方向是由参与方运行协议节点 / Protocol Executor，调用 Engine 与 Observer 形成治理 Gate 和受约束优化；现实动作仍由参与方自己的系统执行。全频谱不成为业务执行器，也不拥有参与方组建的网络。

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
| Observer 最新预发布 | [`v0.4.0-beta`](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.4.0-beta) | Windows x64 公开预发布；不是稳定版；生产就绪：否。 |
| Observer 维护线 | [`v0.3.0-maintenance.6`](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.3.0-maintenance.6) | 已验证维护候选；`NOT_RELEASED / PRODUCTION_READY=NO`。 |
| Knowledge Governance | [`v0.2.0-alpha` 预发布](https://github.com/full-spectrum-lab/full-spectrum-knowledge-governance/releases/tag/v0.2.0-alpha) | Windows x64 技术候选；92/92 工程测试；Linux/macOS 未执行；生产就绪：否。 |
| Protocol | 早期公开草案 | 已公开 Schema 与一致性检查，不宣称最终标准。 |
| 工业案例 | 设计完成 / fixture 已验证 | 完全合成、无具名客户、未经生产验证。 |

[机器可读状态](https://github.com/full-spectrum-lab/.github/blob/main/status/public-status.json) · [AI 阅读上下文](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/AI_CONTEXT.md) · [术语表](https://github.com/full-spectrum-lab/.github/blob/main/ecosystem/GLOSSARY.md) · [证据状态词典](https://github.com/full-spectrum-lab/full-spectrum-commons/blob/main/docs/evidence-and-status.md)

## 请验证，不要猜测

公开事实以各仓库 Release、精确 Tag、测试和随附证据为准。架构图用于解释关系，不等于功能已实现或已经生产就绪。

- [运行 Engine](https://github.com/full-spectrum-lab/full-spectrum-engine#quick-start)
- [查看 Observer v0.4.0-beta](https://github.com/full-spectrum-lab/full-spectrum-observer/releases/tag/v0.4.0-beta)
- [查看合成工业案例](https://github.com/full-spectrum-lab/full-spectrum-enterprise-governance/tree/main/cases/industrial-tightening-evidence-gap)
- [阅读 Protocol](https://github.com/full-spectrum-lab/full-spectrum-protocol/blob/main/START_HERE.md)

当前处于研究与工程验证阶段，不构成生产、监管、法律或客户验证声明。
