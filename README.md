# Master Copywriting v4.11.3

> 不是再给 AI 塞一堆文案模板，而是给它一套真正能做商业判断的文案操作系统。

**One Canonical Brain. Many Agent Bodies.**

Master Copywriting 是一个面向 AI Agent 的全栈文案决策与生成系统。它把产品事实、平台语境、商业目的、IP 身份、表达强度、转化路径与合规边界放进同一条可执行链路，让模型不只会“写得顺”，还知道该写什么、为什么这样写，以及什么绝不能编。

它适用于抖音、小红书、公众号、视频号及通用商业内容，可运行在 Codex、Claude、OpenAI、Gemini、GitHub Copilot 和任何能够读取 Markdown 的 Agent 中。

## 为什么它不只是 Prompt

普通提示词解决的是“这一次怎么写”。Master Copywriting 解决的是“面对不同平台、目的、产品和证据，系统应该如何稳定决策”。

- **先路由，再创作**：识别平台、目的、IP 模式、受众温度、产品事实充分度与商业强度。
- **先真相，再策略**：产品、数字、身份、外部事实和演示结果逐层过门，防止事实漂移。
- **卖点必须抵达购买理由**：把成分、参数、工艺翻译成真实场景中的利益、摩擦和选择理由。
- **强表达不等于乱承诺**：隐喻、剧情、反差、吐槽、情绪放大默认开放，主张上限始终由证据决定。
- **一次写作，多端运行**：Canonical Core 与 Agent Adapter 分离，同一套商业逻辑按宿主能力自动降级。
- **复杂性留在系统内部**：默认交付干净成稿，不把路由、评分、免责声明和内部标签甩给用户。

## 核心能力

### 1. Platform x Purpose x IP 路由

系统不是把同一篇稿子换几个平台词，而是重新理解每个平台上的用户问题：抖音争夺注意与即时决策，小红书建立判断标准，公众号承载完整认知，视频号强调可信与可转述。

### 2. Search Before Ask

当产品资料不足且宿主具备网络能力时，系统先识别 SKU、检索可信来源并建立 Product Ledger；只有检索失败或产品身份仍有歧义时，才向用户索取最少必要信息。

### 3. Claim Ceiling

每条主张都根据产品监管类别、授权宣称和证据等级确定表达上限。能强说的，不故意写弱；没有证据的，不靠谐音、暗语或剧情偷渡。

### 4. Pain Translation

从表层抱怨一路走到日常摩擦、情绪成本、理想进展与产品桥梁。系统区分 `DIRECT_PAIN`、`PARTIAL_PAIN` 和 `CONTEXT_PAIN`，让痛点更有画面，也让产品真的接得住。

### 5. Commercial Expression Freedom

支持 `CONSERVATIVE`、`STANDARD`、`AGGRESSIVE` 三档商业强度。普通食品、日用品和非宣称功效化妆品可以拥有更高的情绪密度与生活方式表达；保健食品、功效化妆品和医疗器械保持严格主张边界。

### 6. Conversion Recovery

一句高转化表达越过语义边界时，系统不会把它删成参数说明书，而是保留场景冲击和情绪强度，只替换越线的那一跳，从真实差异、便利性、感官、成本、身份与选择效率中重建购买理由。

### 7. Cross-Agent Portability

四种运行模式覆盖从高能力 Agent 到纯文本模型：

| Mode | 能力组合 | 运行方式 |
|---|---|---|
| `FULL` | Web + Files + Code + MCP + Memory + Structured Output | 完整检索、路由、验证与结构化执行 |
| `GROUNDED` | Files + Structured Output | 基于本地可信资料完整创作 |
| `WEB_ONLY` | Web + Structured Output | 在线检索并建立产品事实账本 |
| `TEXT_ONLY` | Markdown | 保留核心决策与硬门槛的轻量运行 |

## 架构

```text
SKILL.md                         Canonical Core / 路由 / 执行顺序 / Hard Gates
├── references/
│   ├── execution/              产品获取、主张权限、利益翻译、商业表达、痛点场景化
│   ├── modes/                  24 种平台 x 目的 x IP 模式
│   ├── angle/                  动态角度发现与自然深度
│   ├── craft/                  钩子、CTA、声音、公式与方法卡
│   ├── external/               外部情报与研究协议
│   └── quality/                反模板化、长度引擎与最终输出
├── adapters/                   Claude / OpenAI / Gemini / Copilot / Generic
├── schemas/                    产品、IP、路由、研究与内容指纹 Schema
├── scripts/                    验证、回归测试与打包工具
└── tests/                      激活、可移植性与行为回归测试
```

## 适用任务

- 抖音短视频口播、信息流广告与素人 IP 带货
- 小红书种草笔记、产品对比与选择标准内容
- 公众号长文、品牌内容与深度产品教育
- 视频号可信表达、熟人传播与直播承接内容
- 产品卖点提炼、参数转利益、痛点场景化
- 多版本创意、跨平台重构与内容批量规划
- 文案诊断、低转化改写与主张风险修复

## 快速开始

将仓库放入 Agent 的技能目录，让 Agent 完整读取 `SKILL.md`：

```text
~/.codex/skills/master-copywriting/
```

然后直接提出业务任务：

```text
使用 master-copywriting，写 5 篇抖音素人 IP 带货口播。
先检索并梳理产品卖点，每篇约 300 字，开头角度不要重复。
```

系统会自动完成任务路由、能力协商、按需加载 Reference、事实校验、商业表达、最终清理与交付。

其他 Agent 的接入方法见 [`adapters/`](adapters/)。

## 设计原则

```text
Truth before strategy.
Strategy before style.
Different copy, same reality.
Write badly -> rewrite.
Write falsely -> never output.
```

Master Copywriting 追求的不是“最安全的废话”，也不是“最刺激的虚话”，而是在事实允许的范围内，把购买理由推到最强。

## 质量保障

仓库包含行为回归、可移植性审计、事实校验和技能完整性验证脚本。修改核心规则后，可运行：

```bash
python scripts/validate_skill.py .
python scripts/run_regression.py
python scripts/run_behavioral_regression.py
```

## 版本

当前版本：**v4.11.3**

完整演进记录见 [`CHANGELOG.md`](CHANGELOG.md)，跨版本迁移说明见 [`MIGRATION.md`](MIGRATION.md)。

## License

本项目当前采用仓库内的 Internal Use License。未经明确书面许可，不得在组织外重新分发。详见 [`LICENSE`](LICENSE)。

---

**它不是替你写一句文案。它是在不同产品、平台和 Agent 之间，持续守住同一套商业判断。**

