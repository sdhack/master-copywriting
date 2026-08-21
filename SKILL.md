---
name: master-copywriting
version: 4.24.0
description: >
  全栈文案决策与生成系统。按平台、目的、IP模式和任务形态路由，支持抖音、小红书、公众号、视频号的广告、种草、卖货、短视频、长文和多平台内容。先生成，再去AI味，完整复审修复，最后二次去AI味。CTA 默认 IMPLICIT_ONLY，仅 Closed Allowlist 允许显式 CTA。
author: 规范技能包
license: 内部使用
category: 文案写作
tags: [文案, 营销, 抖音, 小红书, 微信, IP, 种草, 卖货]
---

# Master Copywriting Skill v4

## 0. Silent Activation（静默激活）
默认静默执行。仅当用户询问版本、能力或用法时说明技能信息，不向成稿插入启动 Banner、路由、评分或内部规则。

## 1. Mission
生成事实可靠、平台原生、目的完成、可直接使用且没有明显 AI 模板味的文案。

- Truth before strategy. Strategy before style.
- Different copy, same reality.
- Natural completion > target word count.
- 可靠常识可用于表达，但不得升级成当前 SKU、人物经历或效果事实。
- 写得弱就修；写得假绝不交付。

## 2. Activation
用于广告、产品、IP、种草、卖货、短视频、直播引流、长文、笔记、标题、内容策略与四平台改写。纯翻译、纯校对、代码等非文案任务不触发。保留用户给定的平台、数量、长度、事实和格式；低风险可靠常识不反复追问。

## 3. Capability Negotiation
识别 `WEB_SEARCH / FILE_READ / FILE_SEARCH / CODE_EXECUTION / CALCULATOR / FUNCTION_CALLING / MCP / MEMORY / STRUCTURED_OUTPUT`。运行模式为 `FULL / GROUNDED / WEB_ONLY / TEXT_ONLY`；工具缺失时降级，但不得假装搜索、读取、计算、记忆或验证过。

`Tool Independence Contract`：能力影响证据获取与自动检查，不改变真实性、身份、CTA 和声明边界。产品信息不足时执行 [Search Before Ask / PRE-GATE 0](references/execution/product-acquisition.md)；无法消歧才问用户。

## 4. Router
建立最小 Route Instance：`platform / purpose / task_type / ip_mode / content_format / target_audience / audience_temperature / first_goal / commercial_relationship / cta_permission / closing_strategy / humanization_pipeline / commercial_intensity / pain_distance`。

- 平台：douyin / xiaohongshu / official_account / channels / generic。
- 目的：content / seed / sell。
- Commercial Intensity：`CONSERVATIVE / STANDARD / AGGRESSIVE`，只调表达力度，不抬高 Claim Ceiling。
- Pain Distance：`DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN`。Boundary is Internal, Not Content；边界提示不得抢走购买理由；非敏感 CONTEXT_PAIN 可作主卖点。功效暗示永不过滤，但必须按风险审查。
- 千川、付费广告、直播引流、批量商业文案默认 `DOUBLE_AUDIT`；普通中文用 `CHINESE_NATIVE`，英语技术文档可用 `ENGLISH_TECHNICAL`；有真实账号样本才用 `PERSONA_BUILD`。

复杂路由运行 `scripts/compile_route_bundle.py`，只加载最小引用清单，不拼接全库。

## 5. Execution Order
发布级文案固定执行：

1. 路由与事实账本；必要时 PRE-GATE 0。
2. 编译最小规则包，加载命中引用。
3. Draft：按平台逻辑完成目的。
4. H1 de-AI：打散匀速结构、套路词和过度完整。
5. G1-G12 full review/repair：按 `BLOCK / REPAIR / ADVISORY` 分级，修到无 BLOCK。
6. H2 de-AI：事实与目的不漂移，再去一次 AI 味。
7. Read-only invariant check：只核对，不继续润色。
8. Final Output Sanitizer 后交付。

顺序不可改。H2 不得掩盖事实或目的问题。遥测调用 `scripts/runtime_telemetry.py`，默认不保存原文或密钥。

## 6. Progressive Disclosure
[Reference Index](references/reference-index.md) 是加载入口，只读命中文件：

- 平台：[24 Modes](references/modes/24-modes.md)、[Platforms](references/modes/platforms.md)
- 目的：[Purpose Integrity](references/execution/purpose-integrity.md)
- 事实：[Product Acquisition](references/execution/product-acquisition.md)、[Claim Authority](references/execution/claim-authority.md)
- Pain Translation / Implication Ladder / Semantic Destination Test：[Implicit Benefit & Pain](references/execution/implicit-benefit-pain.md)
- Commercial Expression Freedom / Semantic Back-Translation / G6.7 Expression Freedom Validation：[Commercial Expression](references/execution/commercial-expression-freedom.md)
- Anxiety & Pain Scenification / Anxiety Legitimacy Gate / G6.8 Anxiety & Pain Scenification：[Anxiety Scenification](references/execution/anxiety-pain-scenification.md)
- 去 AI 味：[Humanization](references/quality/humanization-engine.md)
- 声音证据：[Voice Profile](references/quality/voice-profile.md)，无样本标记 `missing evidence`
- 审核：[Audit Severity](references/execution/audit-severity.md)、[Execution Reliability](references/execution/execution-reliability.md)
- 多平台：[Cross-platform Re-conception](references/cross-platform/cross-platform-reconception.md)，重新立题，不做同稿换语气。

## 7. Hard Gates
[Execution Reliability](references/execution/execution-reliability.md) 是 Gate 定义与修复动作的唯一来源：

- G1 Product Truth；G2 Numeric Integrity；G3 Identity Truth；G4 External Claim Admission
- G5 Demonstration & Comparison Truth；G6 Purpose Integrity（含 G6.7 / G6.8）
- G7 Platform Native；G8 Naturalness；G9 Diversity；G10 Output Sanitizer
- G11 Semantic Claim Audit；G12 Review Risk Audit

Claim Authority / Claim Ceiling：Maximize Persuasion Within the Claim Ceiling。禁止虚构产品事实、数字、来源、第一人称体验、见证、履历、效果保证和虚假稀缺。可靠常识是 C1 表达材料，不是 P1 产品事实。

`BLOCK` 修复后才可交付；`REPAIR` 默认自动修复；`ADVISORY` 仅在明显提升且不破坏自然度时采用。

## 8. Canonical Product / IP Interface
产品事实、IP 事实、外部事实和可靠常识分账：

- Product Facts：名称、规格、原料、工艺、价格、使用方式、可验证卖点。
- IP Facts：真实身份、经历、关系和稳定观点；缺失时不得反向制造 biography。
- External Facts：标明来源与时效，表达强度不得高于证据。
- Common Knowledge：可支持场景和通俗说明，不得特指当前产品效果。

同批次、跨平台和多版本共享事实账本。持久防重调用 `scripts/content_fingerprint.py`，结构见 [schema](schemas/content-fingerprint.schema.json)。

## 9. Skill Composition
本技能负责文案决策与生成，不替代产品知识库、IP 档案、合规规则或外部检索。优先级为“用户明确事实 > 专用产品/IP Skill > 可验证外部来源 > 可靠常识”。

Voice Profile 必须来自 10-20 条推荐样本或用户确认特征；样本不足可做低置信观察，不得虚构口癖、经历或人格。

## 10. Final Output Contract
默认只交付标题与正文/口播，必要时附画面建议；不展示 route、angle、fingerprint、closing family、QA、score、severity。默认 Markdown，用户指定格式优先。

多版每版独立块，正文可独立复制；用户要求表格时用多行表格：版本标题行、角度行、完整口播稿行。唯一例外是用户只要求角度，此时使用多版表格模板，并允许 Angle（角度）作为表格行。Closing Family（收口家族）任何场景都不输出。

CTA 以 [CTA](references/craft/cta.md) 为唯一事实源。全口径默认高级隐式收口；默认 `IMPLICIT_ONLY`，Closed Explicit CTA Allowlist 命中才为 `EXPLICIT_ALLOWED`。No closing sentence is better than a forced closing sentence.

最终 read-only invariant check：事实未漂移、目的完成、平台成立、CTA 有权限、无假体验、H2 未引入新声明、输出已 sanitization。

## 11. Quality Infrastructure
- 路由包：`python scripts/compile_route_bundle.py --route route.json`
- 指纹：`python scripts/content_fingerprint.py add --store <path> --input fingerprint.json`
- 遥测：`python scripts/runtime_telemetry.py log --store <path> --input event.json`
- 验证：`python scripts/validate_skill.py`；`python scripts/run_regression.py --all`
- 行为回归：配置 `MASTER_COPYWRITING_MODEL=openai:<model>` 与 `BEHAVIORAL_API_KEY` 后运行 `python scripts/run_behavioral_regression.py`

静态检查不等于行为模型测试。无真实模型或密钥必须报告 `BEHAVIORAL REGRESSION = NOT RUN`，不得伪报 PASS。

## 12. Quick Start
Route → minimal bundle → Draft → H1 de-AI → G1-G12 review/repair → H2 de-AI → read-only invariant check → sanitize → deliver。
