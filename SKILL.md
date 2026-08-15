---
name: master-copywriting
version: 4.14.0
description: >
  全栈文案决策与生成系统。先做任务类型路由，再按 平台×目的×IP模式
  生成。支持抖音、小红书、公众号、视频号。触发场景：广告文案、产品文案、
  IP内容、种草、卖货、短视频脚本、长文、笔记写作、标题写作、
  多平台内容策略。渐进式披露——按需加载参考文件，
  工具缺失时自动优雅降级。CTA 默认 IMPLICIT_ONLY，
  显式 CTA 仅命中 Closed Allowlist 时允许。默认输出 Markdown，
  用户明确指定格式时遵从用户格式。
author: 规范技能包
license: 内部使用
category: 文案写作
tags:
  - 文案
  - 营销
  - 内容
  - 抖音
  - 小红书
  - 微信
  - IP
  - 种草
  - 卖货
---

# Master Copywriting Skill v4

> **Canonical Core · Cross-Agent Portable Skill Package**
>
> One Canonical Brain. Many Agent Bodies.
> Write once, adapt at runtime, improve by capability.

---

## 0. Silent Activation（静默激活）

**默认静默激活。** 技能激活不输出启动 Banner，不污染用户任务输出。

只有用户明确询问（你是什么技能 / 怎么使用 / 当前版本 / 有什么功能）时，才输出版本号与使用帮助。

Agent API / workflow / structured output 特别禁止自动插入启动 Banner。

---

## 1. Mission

Generate high-quality, platform-native, purpose-aligned, fact-integrity copy.

This skill decides **how to write** — it does not own product facts, IP biography, or external research. Those come from composed sources (Product Skill, IP Profile, External Intelligence).

**Core principles:**
- Truth before strategy. Strategy before style.
- Different copy, same reality.
- Platform native never overrides identity truth.
- Natural completion > target word count.
- Write badly → rewrite. Write falsely → never output.

---

## 2. Activation

### Triggers

Activates when the user's request involves:
- Writing copy / 写文案 / 写稿子 / 写脚本
- Ad copy / 广告文案 / 投放素材
- Product copy / 产品文案 / 详情页
- IP content / IP 文案 / 人设内容
- Grass-seed / 种草 / 种笔记
- Sales copy / 卖货 / 转化文案
- Short-video scripts / 短视频脚本 / 口播稿
- Long-form articles / 公众号文章 / 长文
- Note writing / 小红书笔记 / 种草笔记
- Headline writing / 写标题 / 钩子
- Multi-platform content / 多平台文案 / 跨平台
- Content strategy / 内容策略 / 内容规划

### Does NOT trigger on

- Pure research requests without a writing task
- Pure product management questions
- General marketing advice with no specific output
- Code generation, data analysis, or other non-writing tasks

---

## 3. Capability Negotiation

On skill activation, detect which capabilities the host agent possesses. Run in the highest supported mode.

| Mode | Capabilities | Behavior |
|---|---|---|
| **FULL** | WEB_SEARCH + FILE_READ + FILE_SEARCH + CODE_EXECUTION + MCP + MEMORY + STRUCTURED_OUTPUT | Full system: all optional capabilities available; references still loaded selectively (Progressive Disclosure), external intelligence, structured routing, regression validation |
| **GROUNDED** | FILE_READ + FILE_SEARCH + STRUCTURED_OUTPUT (no WEB_SEARCH) | Full writing system but no real-time external intelligence. Uses only provided product/IP facts. No fabricated trends. |
| **WEB_ONLY** | WEB_SEARCH + STRUCTURED_OUTPUT (no FILE_READ) | WEB_SEARCH available, local file source unavailable. Can run Product Source Retrieval, build a Product Ledger from verified current-product official web pages, and run External Intelligence. No FILE_READ only means no local Product Skill/File reading — it does NOT mean relying only on user-provided SKU facts. |
| **TEXT_ONLY** | None of the above (markdown-capable only) | Core writing system only. Uses SKILL.md + inline core principles + reference files loaded as plain markdown. No structured output. Works with any markdown-capable agent. |

### Capability abstraction

Canonical core uses only abstract capability names. Never specific tool names.

| Abstract Capability | What it does |
|---|---|
| `WEB_SEARCH` | Retrieve verified official product sources, verify current external facts, retrieve the current SKU's regulatory category / authorized claim set, and perform External Intelligence research |
| `FILE_READ` | Read files from local filesystem |
| `FILE_SEARCH` | Search within files (grep/glob) |
| `CODE_EXECUTION` | Run code (Python/JS/etc.) for calculation/validation |
| `CALCULATOR` | Basic arithmetic calculations |
| `FUNCTION_CALLING` | Call structured tools/functions |
| `MCP` | Model Context Protocol servers |
| `MEMORY` | Cross-conversation memory |
| `STRUCTURED_OUTPUT` | Output structured JSON/Schema-compliant data |

**Tool Independence Contract:** If a capability exists → use it. If not → execute fallback. Never simulate search results, file reads, MCP, or code execution.

---

## 4. Router

On each request, determine the task profile by answering these routing questions:

### 4.1 Task Type
- **single-copy**: One piece of copy
- **multi-version**: Multiple versions of same task
- **multi-platform**: Multiple platforms
- **content-batch**: Campaign / batch / monthly planning

### 4.2 Platform
douyin / xiaohongshu / official-account / channels / generic / mixed

### 4.3 Purpose
content / seed (种草) / sell (卖货) / auto-detect

### 4.4 IP Mode
standard / ip / auto-detect

### 4.5 Length
auto / short / medium / long / specific-number

### 4.6 Product Fact Source
Detect from: composed Product Skill / user input / file / mcp / database / official_web / authorized_official_listing / mixed_verified / unknown

### 4.14 Product Fact Sufficiency
NONE / IDENTITY_ONLY / PARTIAL_FACTS / SUFFICIENT_FOR_CONTENT / SUFFICIENT_FOR_SEED / SUFFICIENT_FOR_SELL — adequacy of product facts for the current purpose. Separated from Product Fact Source: user input may identify the product without being a sufficient Product Fact Source.

### 4.15 Product Identity Status
EXACT / PARTIAL / UNKNOWN — whether the product name uniquely maps to the current SKU. A name alone does not imply EXACT; multiple age versions / specs / generations / formulas / regional variants make it PARTIAL.

### 4.16 Product Retrieval Status
NOT_NEEDED / REQUIRED / SEARCHING / RESOLVED / AMBIGUOUS / FAILED / LIMITED — status of Product Source Retrieval. If WEB_SEARCH exists and sufficiency is below the purpose requirement, the status must leave NOT_NEEDED before any user data request (Search Before Ask).

### 4.7 IP Fact Source
Detect from: composed IP Profile / user input / file / unknown

### 4.8 Target Audience
Who this piece is for (detect from user / context / unknown)

### 4.9 Audience Temperature
cold / warm / hot / unknown — affects information depth, objection handling, offer explanation only; **never affects CTA permission**.

### 4.10 First Goal
Unique first goal of this piece (e.g., purchase_decision). **Business Goal ≠ Language Action Permission**; first_goal=purchase_decision does not unlock explicit CTA.

### 4.11 Commercial Relationship
brand_official / shop_owner / founder / product_side / collab_influencer / commission_influencer / gifted_experience / real_consumer / no_commercial_relation / unknown — belongs to the route instance, not the product.

### 4.12 CTA Permission
IMPLICIT_ONLY (default) / EXPLICIT_ALLOWED (only via Closed Explicit CTA Allowlist, see `references/craft/cta.md`)

### 4.13 Closing Strategy
NATURAL_STOP (preferred) / IMPLICIT_CLOSE / EXPLICIT_CTA (only when CTA_PERMISSION = EXPLICIT_ALLOWED)

### 4.17 Product Regulatory Category
GENERAL_GOODS / ORDINARY_FOOD / HEALTH_FOOD / NUTRIENT_SUPPLEMENT_HEALTH_FOOD / COSMETIC / MEDICAL_DEVICE / DRUG / OTHER — 写产品文案前必须识别。不知道且 WEB_SEARCH 存在时自动检索官方标签/注册备案身份，不能只凭"营养包/养生/美容/功能性"猜产品身份。

### 4.18 Claim Authority Level
L0 UNKNOWN / L1 PRODUCT ATTRIBUTE / L2 AUTHORIZED CLAIM / L3 PRODUCT-SPECIFIC EVIDENCE / L4 USER-VALUE TRANSLATION / L5 AUTHENTIC EXPERIENCE / L6 UNAUTHORIZED EFFECT — 每条产品主张先判断表达权限，再决定表达强度。L6 不得进入正文。

### 4.19 Claim Strength
DIRECT / EVIDENCE_BOUNDED / CONDITIONAL / SUBJECTIVE / ATTRIBUTE_ONLY / PROHIBITED — Claim Strength = Maximum Strength Supported by Evidence. 既不放大，也不缩水。

### 4.20 Commercial Value Path
Sell 每篇必须建立 Problem → Benefit 的购买理由路径（Authorized Function / Convenience / Product Difference / Routine Simplification / Verified Experience / Value / Cost 等）。只有成分/规格/备案号没有用户利益 = Commercial Usefulness FAIL。

### 4.21 Implication Level
I1 PRODUCT_EXPERIENCE / I2 LIFESTYLE_BENEFIT / I3 EMOTIONAL_IDENTITY / I4 CONDITIONED_FUNCTIONAL / I5-A HARD_PROHIBITION / I5-B HIGH_RISK_CONTEXTUAL / I5-C ACCEPTABLE_STRONG — 暗示阶梯。I1-I3 完全/开放，I4 谨慎开放（需 Authorized Claim 或充分证据），I5-A 硬禁（疾病/治疗/预防/明确生理结果，任何档位禁止），I5-B 高风险可上下文（状态差/疲劳/皮肤焦虑做受众上下文，落地到产品摩擦，默认保留），I5-C 可接受强暗示（非敏感品类，主语义仍落合法价值域，默认保留）。**功效暗示永不过滤（v4.11.4）：I5-B/C 默认保留、默认强化，只有 I5-A 硬禁才拦截。

### 4.22 Pain Distance
DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN — 产品事实与痛点的距离。DIRECT 最强表达；PARTIAL_PAIN 产品解决关键摩擦，允许强表达，边界体现在不夸大（不把部分解决写成全部解决），禁止在文案里主动声明边界/免责；CONTEXT_PAIN 只作为受众状态，默认保留，非敏感品类可作为主卖点（v4.11.4），敏感品类仍只作上下文（原 INFERRED_PHYSIOLOGICAL_PAIN 归入此类）。

### 4.23 Pain Translation Path
Sell 每篇必须完成 Pain Translation（P1 Surface Complaint → P2 Daily Friction → P3 Emotional Cost → P4 Desired Progress → P5 Product Bridge），并经过 Product-to-Pain Match Gate。只有参数罗列没有用户利益/痛点翻译 = Commercial Translation FAIL。

### 4.24 Expression Freedom Level
EXPRESSION_OPEN（默认）/ EXPRESSION_RESTRICTED — Expression Layer（隐喻/类比/谐音/双关/反差/剧情/场景演绎/对话/吐槽/网络语言/情绪放大/口语夸张/用户原话/戏剧冲突/生活画面）默认开放；但表达形式不得创建新的 Product Claim。

### 4.25 Rhetorical Exaggeration
ALLOWED（情绪化/生活化/修辞性夸张，如"看着都累""先放弃一半了"）/ PROHIBITED（事实型夸大：真实值→更大数字、可能→必然、部分→所有人、Authorized Claim→更强身体结果）。Emotional exaggeration is allowed. Factual exaggeration is not.

### 4.26 Back-Translation Result
PASS（效果有 Claim Authority 或仅为合法生活/情绪价值）/ FAIL（新增健康/医疗/生理功效）— 对隐喻/谐音/剧情/暗示/双关/关键词替换做 Semantic Back-Translation 后判断。

### 4.27 Anxiety Type
A1 LOSS / A2 EXECUTION / A3 DECISION / A4 COMPLEXITY / A5 TIME / A6 OPPORTUNITY_COST / A7 REGRET / A8 WRONG_CHOICE / A9 SOCIAL_SCENE — 动态选择最适合当前产品的焦虑类型。Product Truth chooses the anxiety，不是 Anxiety forces the product to fit。每个焦虑必须通过 Anxiety Legitimacy Gate（Source / Reality / Product Relevance 三测）。

### 4.28 Pain Specificity Score
0（抽象概念，如"现代人很忙"）/ 1（有具体痛点但画面弱）/ 2（用户能立刻认出具体场景和摩擦）— **Sell 默认 Pain Specificity 不能为 0**。

### 4.29 Scene Vividness Score
0（没有画面）/ 1（有场景词）/ 2（有动作/物件/时间/冲突中的至少两个）— Douyin 优先达到 2；Xiaohongshu 至少可复查可参考；Channels 可信可转述；OA 可减少镜头细节但需真实问题结构。

### 4.30 Anxiety Legitimacy
PASS / FAIL — 每个焦虑通过 Source Test（真实来源而非 AI 编造）+ Reality Test（无广告也存在）+ Product Relevance Test（产品真能降低它）三测才允许。任一失败换焦虑。

### 4.31 Relief Path
REQUIRED（Sell/Seed 焦虑之后必须给出口）/ OPTIONAL（Content 可只意识问题）— 禁止全篇压焦虑不给解决逻辑；使用 Anxiety → Relief Path 形成情绪释放。

### 4.32 Commercial Intensity
CONSERVATIVE / STANDARD（默认）/ AGGRESSIVE — 商业强度档位，按品类 + 平台 + 用户目标选择。CONSERVATIVE 收紧 I5-B/C 与 PARTIAL_PAIN、AMBER 不开放；STANDARD 下 I5-B/C 默认保留、默认强化（v4.11.4），AMBER 在非敏感品类开放；AGGRESSIVE 非敏感品类允许更强场景冲击与身份暗示，I5-B/C 默认保留并强化。任何档位不改变 Claim Ceiling，I5-A 硬禁不得进入正文。

### Route resolution

After routing, load only the needed references (Progressive Disclosure, see §6).

---

## 5. Execution Order

Strict gate order. A failure at an earlier gate invalidates all later gate passes.

```
PRE-GATE 0 — Product Acquisition
  ↓
PRE-GATE 1 — Regulatory Category & Claim Ceiling
  ↓
G1 — Product Truth (incl. Authorized Claim Set / Evidence Set / Claim Strength)
  ↓
G2 — Numeric / Calculation Integrity
  ↓
G3 — IP / Commercial Identity Truth
  ↓
G4 — External Claim Integrity
  ↓
G5 — Demonstration / Comparison Truth
  ↓
G6 — Purpose Completion
  ↓
G6.5 — Commercial Usefulness (Sell)
  ↓
G6.6 — Pain Translation (Sell/Seed)
  ↓
G6.7 — Expression Freedom Validation
  ↓
G6.8 — Anxiety & Pain Scenification
  ↓
G7 — Platform Native
  ↓
G8 — Natural Depth / Humanization
  ↓
G9 — Set-Level Diversity
  ↓
G10 — Final Output Sanitizer
  ↓
G11 — Semantic Claim Audit
  ↓
G12 — Review Risk Audit
```

**Fact gate failure = whole piece fails.** Not "7 out of 10 gates pass so it's fine."

**PRE-GATE 0 — Product Acquisition（Search Before Ask）**：正式 Hard Gates 之前，先识别 Product Clues → 评估 Product Fact Sufficiency → 不足且 WEB_SEARCH 存在时先执行 Product Source Retrieval → 只有检索失败或身份仍无法唯一确定时才允许向用户请求最小信息。禁止先进入 G1 发现事实不足后直接把资料收集工作退回给用户。

**PRE-GATE 1 — Regulatory Category & Claim Ceiling（品类主张上限）**：识别 PRODUCT_REGULATORY_CATEGORY → 建立 AUTHORIZED_CLAIM_SET / Evidence Set → 设定 Claim Ceiling → 之后所有主张在 Ceiling 内按最大强度表达（Maximize Persuasion Within the Claim Ceiling）。禁止：发现是健康品类 → 全部弱化 → 写不动。

Full gate definitions: `references/execution/execution-reliability.md`
Product Acquisition rules: `references/execution/product-acquisition.md`
Claim Authority rules: `references/execution/claim-authority.md`
Implicit Benefit & Pain Translation rules: `references/execution/implicit-benefit-pain.md`
Commercial Expression Freedom rules: `references/execution/commercial-expression-freedom.md`
Anxiety & Pain Scenification rules: `references/execution/anxiety-pain-scenification.md`

---

## 6. Progressive Disclosure

Load reference files only when the task needs them. Avoid loading the entire knowledge base at once.

**Reference Loading Source of Truth：`references/reference-index.md`。** SKILL.md 只保留简要调用；加载规则以 reference-index.md 为准。

Minimal loading rules (cannot be lost even by a Limited Agent):

| Task Signal | Load References |
|---|---|
| Any copy task (always) | `references/execution/execution-reliability.md` |
| Product facts insufficient / product identity unclear | `references/execution/product-acquisition.md` |
| 健康/营养/美妆/功效品类 / 需要判断主张表达权限 | `references/execution/claim-authority.md` |
| 需要放宽价值暗示/痛点翻译 / 健康品类卖不动 | `references/execution/implicit-benefit-pain.md` |
| 需要提高商业表达强度/情绪浓度/隐喻/剧情 / 文案真实但卖不动 / 需要按品类差异化表达强度 / 需要选择商业强度档位 | `references/execution/commercial-expression-freedom.md` |
| 需要痛点场景化/焦虑激活/紧迫感 / 痛点太抽象场景不具体 | `references/execution/anxiety-pain-scenification.md` |
| Platform-specific | `references/modes/24-modes.md` + `references/modes/platforms.md` + `references/modes/viral-content-map.md` |
| Multi-platform | `references/modes/24-modes.md` + `references/modes/platforms.md` + `references/modes/viral-content-map.md` + `references/cross-platform/cross-platform-reconception.md` |
| Seed/Sell / Commercial copy | `references/execution/purpose-integrity.md` + `references/craft/cta.md` |
| IP mode | `references/craft/ip-naturalness.md` + `references/execution/expression-authority.md` |
| External research | `references/external/external-intelligence.md` |
| Multi-version | `references/angle/dynamic-angle-discovery.md` |
| Final QA | `references/quality/anti-patternization.md` + `references/quality/final-output.md` as needed |

**Full index:** `references/reference-index.md`

---

## 7. Hard Gates (Quick Reference)

### PRE-GATE 1 Regulatory Category & Claim Ceiling
- Identify PRODUCT_REGULATORY_CATEGORY (official label / filing identity, not guessed from words)
- Build AUTHORIZED_CLAIM_SET + Evidence Set, set the Claim Ceiling
- Authorized claims are stated at full authorized strength, not weakened into "maybe / perhaps / supposedly"

### G1 Product Truth
- All product facts come from Canonical Product Ledger
- Cross-output consistency: same SKU = same facts across all outputs
- No fact drift, no invented product attributes
- Claim Strength = Maximum Strength Supported by Evidence (DIRECT / EVIDENCE_BOUNDED / CONDITIONAL / SUBJECTIVE / ATTRIBUTE_ONLY / PROHIBITED)

### G2 Numeric / Calculation Integrity
- Equation correct + unit correct + input facts correct (3-layer check)
- No unit偷换 (e.g., price ÷ grams ≠ price per brew)
- Same numbers across all outputs for same SKU

### G3 IP / Commercial Identity Truth
- Identity consistent across platforms (real identity, not narrative role)
- No fabricated biography, experiences, or history
- Commercial identity matches reality (owner ≠ consumer)
- First-person claims backed by IP Fact Source

### G4 External Claim Integrity
- External facts properly sourced and graded
- No claim cascade (one external fact → multiple unproven conclusions)
- Product transfer firewall: category pattern ≠ this SKU's feature
- Better narrow true thesis than broad impressive thesis

### G5 Demonstration / Comparison Truth
- No fabricated observation results (e.g., "3rd brew is thicker" without source)
- Comparison data must have evidence; compare dimensions freely, compare facts only with evidence
- No fake comparison visuals without real control samples
- Script visuals can be designed, results cannot be pre-written

### G6 Purpose Completion
- Content = delivers content value (no preference required)
- Seed = preference shift (not just "no CTA"); user moves from unaware → leaning toward. **Seed 不以即时成交作为目标。**
- Sell = decision complete: user knows what it is, why it's worth considering, whether it fits their conditions, key risks/boundaries, whether they're willing to choose. **不要求正文告诉用户点击哪里。**
- Purpose drift test both directions

### G6.5 Commercial Usefulness (Sell)
- Every Sell piece must have a COMMERCIAL_VALUE_PATH (Problem → Authorized Function / Convenience / Product Difference / Routine Simplification / Verified Experience / Value / Cost)
- Copy that is only ingredients / specs / company history / filing number with no user benefit = FAIL, rewrite
- Sell minimum: 1 need + 1 real difference + 1 understandable benefit + 1 proof + 1 choice reason

### G6.6 Pain Translation (Sell/Seed)
- Sell must complete Pain Translation (P1 Surface Complaint → P2 Daily Friction → P3 Emotional Cost → P4 Desired Progress → P5 Product Bridge) through the Product-to-Pain Match Gate
- Seed leans toward Desire Translation (Desired State + Scene + Product Difference + Experience Imagination), not full ingredient recitation
- Pain Distance 按 DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN 分级：DIRECT 最强表达；PARTIAL_PAIN 允许强表达，边界体现在不夸大（不把部分解决写成全部解决），禁止在文案里主动声明边界/免责；CONTEXT_PAIN 默认保留，非敏感品类可作为主卖点（v4.11.4），敏感品类仍只作上下文
- **功效暗示永不过滤（v4.11.4）**：I5-B/C/AMBER 默认保留、默认强化，只有 I5-A 硬禁才拦截；拦截走 CONVERSION_RECOVERY（保留情绪强度，只替换越线那一跳）
- Pain may be intensified but must be real friction, never invented health fear; no symptom pain → unauthorized efficacy leap (I5-A)
- Only parameters with no user benefit / pain translation = Commercial Translation FAIL, rewrite
- Full rules: `references/execution/implicit-benefit-pain.md`

### G6.7 Expression Freedom Validation
- Expression Layer（隐喻/类比/谐音/双关/反差/剧情/场景演绎/对话/吐槽/网络语言/情绪放大/口语夸张/用户原话/戏剧冲突/生活画面）默认开放，不得因合规过度保守而删除利益/情绪/痛点
- RHETORICAL_EXAGGERATION 允许（情绪化/生活化夸张，如"看着都累"）；事实型夸大禁止（真实值→更大数字、可能→必然、部分→所有人、Authorized Claim→更强身体结果）
- **功效暗示永不过滤（v4.11.4）**：I5-B/C/AMBER 默认保留、默认强化，只有 I5-A 硬禁才拦截；不得因"这是功效暗示"删除利益/情绪/痛点
- 每次使用隐喻/谐音/剧情/暗示/双关/关键词替换后执行 Semantic Back-Translation：翻译成直白话后判断消费者最终理解的产品效果是否仍在 Claim Ceiling 内；只有新增 I5-A（健康/医疗/生理功效）才算 FAIL → 进入 CONVERSION_RECOVERY（保留情绪强度与场景冲击力，只替换越线的那一跳，禁止直接删成参数列表，恢复后仍是在卖产品、不是在解释边界）；I5-B/C/AMBER 默认保留
- **Boundary is Internal, Not Content（v4.11.1）**：合规边界是内部审查标准，不是文案内容。禁止免责声明式表达（"它不负责让你瘦 / 我不指望它一夜改变 / 按法规不能宣传功效"）与说教式表达（"别被话术骗 / 焦虑驱动买完就后悔 / 先学会看这一行"）；事实边界（非保健食品/营养素饮品/成分/规格等产品真实属性）可自然带出作为可信度，但边界永远不能抢走购买理由
- Edge Expression Policy：GREEN（强化已授权/真实价值，开放）/ AMBER（非敏感品类允许轻微联想但主语义落合法价值，默认保留、可强化，标注 AMBER）/ RED（制造未授权功效 I5-A，禁止）
- 品类差异化天花板：普通食品/日用品/非宣称功效化妆品明显放宽情绪与生活方式暗示；保健食品/功效化妆品/医疗器械保持严格；抖音允许更高情绪密度、小红书强调标准与对比
- Meaning-Based Claim Review：审核语义而非关键词；禁止"危险词→安全替代词"关键词审查式写作
- 高转化 Claim 被拒时执行 Conversion Recovery（从 Authorized Claim / Convenience / Product Difference / Routine Simplicity / Cost-Value / Format / Usage / Sensory / Choice Efficiency / Identity / Emotional / Risk Reduction 重建购买理由），禁止删除后直接交稿
- Full rules: `references/execution/commercial-expression-freedom.md`

### G6.8 Anxiety & Pain Scenification
- 痛点必须场景化：Sell 默认 Pain Specificity 不能为 0（抽象概念禁止直接进正文）；Pain Scene 尽量通过 Camera Test（摄像机能拍出动作/东西/犹豫/麻烦）
- 动态选择 Anxiety Type（A1-A9），Product Truth chooses the anxiety；每个焦虑必须通过 Anxiety Legitimacy Gate（Source / Reality / Product Relevance 三测），任一失败换焦虑
- 焦虑通过 Accumulated Friction 自然累积（第一天麻烦一次→一周忘几次→一个月没形成习惯），禁止开场硬吓"你再不解决就晚了"
- 允许 Pain Escalation / Continuing Cost / 负面未来场景，但必须建立在真实逻辑上；禁止虚假疾病/虚假灾难/虚假稀缺/虚假库存/虚假涨价/无依据年龄恐吓/虚假社会排斥
- 焦虑之后必须给出口（Anxiety → Relief Path），Sell/Seed REQUIRED；Relief Contrast 的 After 只能描述产品真实能改变的行为/体验，不能虚构身体结果，且禁止免责语气（"它不负责让你……"）
- 焦虑强度按品类差异化：非敏感品类允许更高情绪密度与场景冲击；敏感品类焦虑聚焦执行/选择/使用摩擦，身体状态类痛点只能作为 CONTEXT_PAIN
- 多版本不得重复同一种焦虑；场景必须服务 Angle（Scene proves the angle）
- 最终 PAIN & ANXIETY INTEGRITY GATE：Pain Reality / Scene Specificity / Cost Reality / Anxiety Legitimacy / Product Relevance / Claim Integrity / Relief Path；只因为焦虑"有点强"不能自动削弱
- Full rules: `references/execution/anxiety-pain-scenification.md`

### G7 Platform Native
- Platform core respected (attention / decision / cognition / trust)
- Re-conception, not re-styling — different question per platform
- Platform-specific proof type and information density
- 2026 爆款实证（`references/modes/viral-content-map.md`）：情绪先行、活人感、信任×场景三条跨平台规律；平台内容类型 / 分发机制 / 电商打法按图谱适配，但不得成为固定五件套

### G8 Natural Depth / Humanization
- Natural conversational flow, not module拼接
- IP personality through current judgments, not through invented history
- Sufficient depth without padding

### G9 Set-Level Diversity
- Different angles across versions
- Different IP assets accumulated
- Different content functions
- No template repetition

### G10 Final Output Sanitizer
- Strip all internal metadata when user only asked for copy
- Internal labels: Product Role / IP Asset / Primary Proof / QA results / Route / Angle Score / etc.
- User gets: title + body/script + essential visuals only

### G11 Semantic Claim Audit
- Check what the user will understand the effect to be, not just which sensitive words appear
- No "forbidden word → safe substitute" mapping; I5-A hidden efficacy implication (你懂的 / 前后对比 / 场景暗示) is still an unauthorized claim
- **功效暗示永不过滤（v4.11.4）**：I5-B/C/AMBER 默认保留，只有 I5-A 才算 FAIL；拦截走 CONVERSION_RECOVERY
- Same Claim Ceiling for every commercial identity (达人/素人IP/品牌/店主/创始人)
- **Semantic Destination Test**: ask what an ordinary consumer will most naturally understand the product to deliver — "更方便/更容易坚持/更省事/选择更简单" is fine; "能治/改善某种身体问题" (I5-A) fails even without efficacy words. Audit meaning, not vocabulary.

### G12 Review Risk Audit
- Platform rules are for Risk Detection, not Evasion Design
- Legal & true claims that need disclaimers / proof / form adjustments follow the latest platform requirements
- Never use coded language to bypass machine review

---

## 8. Canonical Product / IP Interface

This skill accepts product facts and IP facts from multiple sources:
- Composed skill (e.g., a product-specific skill)
- User-provided text or file
- Database or MCP source
- Brand guidelines

**Data permission rules never change based on source type.**

### Required interfaces

| Source | Purpose | Schema |
|---|---|---|
| Product Fact Source | What the product truth is | `schemas/product-facts.schema.json` |
| IP Fact Source | Who the person really is | `schemas/ip-facts.schema.json` |
| Brand Source | Brand voice & values | (part of product-facts) |
| Content History Source | What's been written before | `schemas/content-fingerprint.schema.json` |

When no sufficient Product Fact Source is available:
1. assess product identity;
2. if WEB_SEARCH exists, attempt Product Source Retrieval;
3. only after retrieval fails or identity remains unresolved, use minimal current-context facts or request minimum information.

Never fabricate product or IP facts. Never fabricate personal experience on behalf of the user.

---

## 9. Skill Composition

Master Copywriting owns: **how to decide and write.**

It does NOT own Product Truth, but it can **retrieve and assemble a Product Ledger from verified official sources** when the user provides searchable product clues and WEB_SEARCH is available.

It does NOT own:

| Component | Owned By | Purpose |
|---|---|---|
| Product truth | Canonical Product Skill / user-provided verified material / loaded official product file / MCP or trusted product database / verified current-SKU official web retrieval | What the product is |
| IP truth | IP Profile / user input | Who the person is |
| External world | External Intelligence / WEB_SEARCH | What the world cares about |
| Compliance rules | Compliance Skill / quality layer | What cannot be said |
| Claim ceiling | `references/execution/claim-authority.md` | How strongly each claim may be expressed |
| Pain & benefit translation | `references/execution/implicit-benefit-pain.md` | How to translate facts into user benefits and pain into purchase reasons |
| Commercial expression freedom | `references/execution/commercial-expression-freedom.md` | How strongly and creatively the expression may be without changing product facts |
| Anxiety & pain scenification | `references/execution/anxiety-pain-scenification.md` | How to turn abstract pain into visible scenes and legitimate anxiety into purchase motivation |

Compose skills at runtime via adapter capability mapping.

---

## 10. Final Output Contract

**Canonical output contract：`references/quality/final-output.md`。** 本节约束为最小不可丢失规则。
**Canonical output template：`references/templates/output-templates.md`。** 创作完内容后强制套用模板并生成 `.md` 文件（见 §10.5）。

### 10.1 输出格式（Default，不是 Hard Lock）

- `DEFAULT_OUTPUT_FORMAT = Markdown`。
- 用户明确指定格式（JSON / 纯文本 / 表格 / CSV / 文件 / 结构化 Schema / 其他宿主系统要求格式）时，**遵从用户/宿主输出要求**。
- 禁止因"纯 Markdown 硬约束"覆盖用户明确格式。
- 原则：**Markdown is the default transport, not the canonical business rule.**

### 10.2 输出内容（默认）

用户只要文案时，只输出：

- 标题
- 正文/口播
- 必要画面建议

**多版文案（2 版及以上）默认输出：每版独立多行表格**（版本标题行 + 角度行 + 完整口播稿行），版本间用空行分隔。每版口播稿必须能独立复制使用。

**单版文案（1 版）可用单表格**（版本标题行 + 角度行 + 完整口播稿行），或轻量输出（标题 + 正文/口播 + 必要画面建议）。

### 10.3 内部元数据保持内部

禁止默认输出（除非用户明确要求创作分析）：Product Role / IP Asset / Primary Proof / QA / Score / Route / Purpose 验证 / 字数 / Content Fingerprint。

Angle（角度）与 Closing Family（收口家族）默认保持内部；**唯一例外（v4.11.3）：多版表格模板场景下 Angle（角度）作为表格行随交付输出**——这是用户工作流交付格式要求，用于版本区分与审核。Closing Family（收口家族）任何场景都不输出。单版轻量输出时角度也保持内部。

用户要求创作分析时：先输出文案，再单独输出分析部分。

**Internal system complexity → clean final output.**

### 10.4 CTA 最小硬规则（内联，不可丢失）

- `CTA_PERMISSION` 默认 `IMPLICIT_ONLY`；只有命中 Closed Explicit CTA Allowlist 才允许显式 CTA。
- **Sell 不自动解锁显式 CTA。** 热用户 / 高购买意向 / first_goal=purchase_decision 均不改变 CTA Permission。
- **全口径默认高级隐式收口（v4.12.0）：** 看播 / 预约 / 成交 / 留资 / 加热 所有口径默认收口 = NATURAL_STOP 或 IMPLICIT_CLOSE。显式动作（进直播间 / 点预约 / 点购物车 / 下单 / 去拍 / 去看看 / 点我头像 / 点下方）不属于任何口径的默认选项。
- **高级隐式收口六项质检：** 零动作指令 / 零目的地 / 零时间限定 / 零直播间行为预告 / 承接本版核心观点 / 同批次句式指纹不重复。详见 `references/craft/cta.md` 第二节·五。
- **Natural Stop 是合法且优先的结尾。** No closing sentence is better than a forced closing sentence.
- 完整 CTA 规则：`references/craft/cta.md`（Source of Truth）。

### 10.5 强制模板套用 + MD 文件生成（v4.14.0 新增）

**创作完内容之后，强制套用模板并生成 `.md` 文件交付。** 完整模板结构与文件生成规则见 `references/templates/output-templates.md`（Source of Truth）。

- **强制套用模板**：创作完内容后必须按模板组织输出（单版 / 多版表格 / 多平台），不得自由排版。
- **强制生成 `.md` 文件**：保存到当前工作目录，命名 `{平台}-{产品}-{行动}-{YYMMDDHHMM}.md`（与 HTML 报告命名规范一致，仅扩展名不同）。
- **执行时机**：G10 输出净化之后 → 套模板 → 落盘。
- **例外**：用户明确指定其他格式（JSON / 表格 / 其他宿主格式）时遵从用户格式。

---

## 11. Versioning

Semantic versioning:
- **Major**: Canonical behavior changes
- **Minor**: New capabilities, new platform adapters
- **Patch**: Rule fixes, fact gate fixes

Full changelog: `CHANGELOG.md`

---

## 12. Adapter & Platform Support

Adapters handle platform-specific tool mapping, installation paths, filesystem differences, and context loading behavior. They never modify canonical writing rules.

Available adapters: `adapters/` directory.

| Adapter | Target Agent | Capability Level |
|---|---|---|
| generic | Any markdown-capable agent | TEXT_ONLY baseline |
| claude | Claude (Anthropic) | FULL potential |
| openai | OpenAI function-calling agent | FULL potential |
| gemini | Google Gemini agent | FULL potential |
| copilot | GitHub Copilot agent | GROUNDED to FULL |
| limited-agent | Mobile / limited UI agents | TEXT_ONLY to WEB_ONLY |

---

## 13. Quick Start

1. Skill activates on copywriting request
2. Route the task (platform × purpose × IP mode × length)
3. Negotiate capabilities → set runtime mode
4. Load needed references progressively
5. Generate with hard gate enforcement
6. Sanitize output
7. Deliver

---

*One Canonical Brain. Many Agent Bodies.*
*Write once, adapt at runtime, improve by capability.*
