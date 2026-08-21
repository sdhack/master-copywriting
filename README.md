# Master Copywriting Skill

> v4.24.0 · 跨 Agent 的事实约束、平台路由与自然化文案生成系统

[![Version](https://img.shields.io/badge/version-4.24.0-2563eb?style=flat-square)](CHANGELOG.md)
[![Platforms](https://img.shields.io/badge/platforms-Douyin%20%7C%20XHS%20%7C%20OA%20%7C%20Channels-0f766e?style=flat-square)](SKILL.md)
[![Static validation](https://img.shields.io/badge/static%20validation-0%20errors-16a34a?style=flat-square)](scripts/validate_skill.py)
[![License](https://img.shields.io/badge/license-internal-6b7280?style=flat-square)](LICENSE)

Master Copywriting 不是一组万能模板，而是一层可组合的文案决策系统：先判断平台、目的、事实和 CTA 权限，再生成平台原生内容；生成后经过两次去 AI 味、G1-G12 审计和只读不变量核验。

## 能解决什么

- 抖音、小红书、公众号、视频号的内容、种草、卖货和跨平台改写
- 短视频口播、直播引流、笔记、长文、标题和多版本文案
- 产品事实、IP 事实、外部事实与可靠常识的分账使用
- 账号声音画像：只从真实样本提取，不凭空编造人设
- 内容指纹防重复、最小规则包加载和隐私友好的运行遥测

## 核心流程

```text
Route
  ↓
Minimal route bundle
  ↓
Draft
  ↓
H1 de-AI
  ↓
G1-G12 review / repair
  ↓
H2 de-AI
  ↓
Read-only invariant check
  ↓
Sanitize → deliver
```

流程顺序是发布级约束。H2 只能改善表达，不能掩盖事实、目的或平台问题；最终只读核验失败时，回到对应修复阶段，而不是在核验阶段偷偷改稿。

## 设计原则

| 原则 | 实际行为 |
| --- | --- |
| 事实优先 | 不虚构 SKU、数字、来源、履历、体验、见证或效果保证 |
| 平台原生 | 四个平台重新立题，不做同稿换语气 |
| 常识可用 | 可靠常识可帮助表达场景，但不能升级成当前产品事实 |
| CTA 有权限 | 默认 `IMPLICIT_ONLY`；只有 Closed Explicit CTA Allowlist 命中才允许显式 CTA |
| 自然完成 | 自然停笔优先于硬塞收口、万能金句或固定模板 |
| 可降级 | 工具缺失时减少证据能力，不假装搜索、读取、计算或记忆 |

## 审计等级

- `BLOCK`：事实、身份、证据、权限或不变量失败，修复前不得交付
- `REPAIR`：目的、平台、自然度、信息顺序或商业路径问题，默认自动修复
- `ADVISORY`：可选的节奏和措辞优化，不影响可交付性

G1-G12 的定义位于 [execution-reliability.md](references/execution/execution-reliability.md)，等级处置位于 [audit-severity.md](references/execution/audit-severity.md)。

## 目录结构

```text
SKILL.md                         # 精简入口：路由、不变量、加载地图
references/                      # 按需读取的单一事实来源
  modes/                         # 平台与 24 种任务模式
  execution/                    # 事实、声明、目的、CTA、审计与执行可靠性
  quality/                      # 去 AI 味、输出、合规、声音画像
  cross-platform/               # 跨平台重新立题
  craft/                        # 钩子、公式、示例与表达素材
adapters/                       # Agent 能力映射，不改规范规则
schemas/                        # 产品、IP、路由、研究和内容指纹接口
scripts/                        # 验证、回归、编译、指纹和遥测工具
tests/                          # 静态、可移植性和行为回归材料
```

## 快速使用

直接把 `SKILL.md` 加载到支持 Markdown 的 Agent。复杂任务再按 [reference-index.md](references/reference-index.md) 读取命中的引用文件，不要默认加载全库。

### 编译最小路由包

```bash
python scripts/compile_route_bundle.py --route route.json
```

示例 `route.json`：

```json
{
  "platform": "douyin",
  "purpose": "sell",
  "task_type": "short_video",
  "ip_mode": "standard",
  "humanization_pipeline": "DOUBLE_AUDIT"
}
```

### 内容指纹

```bash
python scripts/content_fingerprint.py add \
  --store .master-copywriting/fingerprints.jsonl \
  --input fingerprint.json
python scripts/content_fingerprint.py check \
  --store .master-copywriting/fingerprints.jsonl \
  --input fingerprint.json
```

指纹默认只保存结构化字段，不保存原文。相似度是确定性的 token/Jaccard 检查，不能替代人工或模型判断。

### 运行遥测

```bash
python scripts/runtime_telemetry.py log \
  --store .master-copywriting/telemetry.jsonl \
  --input event.json
python scripts/runtime_telemetry.py summary \
  --store .master-copywriting/telemetry.jsonl
```

遥测记录阶段耗时、引用数量、编辑比例、审核数量、修复循环和最终不变量状态；默认过滤原文和密钥。

## 验证与证据边界

```bash
python scripts/validate_skill.py
python scripts/run_regression.py --all
python scripts/run_behavioral_regression.py
```

当前静态契约回归结果：`107 pass / 0 fail / 1 skip`。行为回归没有配置真实模型时会明确显示 `BEHAVIORAL REGRESSION = NOT RUN`，不会把静态检查冒充模型证据。配置真实 OpenAI-compatible 模型后：

```bash
set MASTER_COPYWRITING_MODEL=openai:<model>
set BEHAVIORAL_API_KEY=<key>
python scripts/run_behavioral_regression.py
```

密钥只通过环境变量提供，不要写入 route、fixture、README 或提交历史。

## 适配器

- [generic](adapters/generic.md)：仅 Markdown 的最低能力基线
- [claude](adapters/claude.md)、[openai](adapters/openai.md)、[gemini](adapters/gemini.md)、[copilot](adapters/copilot.md)：工具能力映射
- [limited-agent](adapters/limited-agent.md)：受限环境下的安全降级

适配器只说明能力，不重定义事实、目的、CTA 或硬门禁。

## 版本与治理

- 入口版本：`4.24.0`
- 变更记录：[CHANGELOG.md](CHANGELOG.md)
- 迁移说明：[MIGRATION.md](MIGRATION.md)
- 内容指纹接口：[content-fingerprint.schema.json](schemas/content-fingerprint.schema.json)
- 账号声音证据：[voice-profile.md](references/quality/voice-profile.md)

当前账号声音样本和真实模型行为证据均属于 `missing evidence`，不会在文档中虚构成已验证能力。

## 许可证

内部使用，详见 [LICENSE](LICENSE)。
