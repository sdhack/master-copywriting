# Product Acquisition（产品事实获取层）

> **Source of Truth：产品事实获取 Product Acquisition。** 主 SKILL.md 只保留简要调用；本文件是 Product Acquisition 的唯一 Source of Truth。
> **版本**：v4.6.2 新增
> **类型**：执行可靠性补丁（不新增文案技巧；不修改 24 模式 / 四平台 Canonical Core / Content / Seed / Sell 核心定义 / CTA Permission / Dynamic Angle / Natural Depth）
> **解决问题**：当用户没有主动提供完整产品资料时，Agent 没有稳定联网检索，而是过早要求用户提交详情页/配料表/规格/价格。
> **最高原则**：# Search Before Ask.
> 只要宿主拥有 WEB_SEARCH，并且用户已经提供足以搜索产品的品牌/产品线索，Agent 必须先主动检索，不能先把产品资料收集工作退回给用户。

---

## 一、两个独立变量：Product Fact Source 与 Product Fact Sufficiency

### 1.1 PRODUCT_FACT_SOURCE（产品事实来源）

可能取值：

- composed_skill
- user_input
- file
- mcp
- database
- official_web
- authorized_official_listing
- mixed_verified
- unknown

### 1.2 PRODUCT_FACT_SUFFICIENCY（产品事实充分度）

只能取值：

- NONE
- IDENTITY_ONLY
- PARTIAL_FACTS
- SUFFICIENT_FOR_CONTENT
- SUFFICIENT_FOR_SEED
- SUFFICIENT_FOR_SELL

### 1.3 铁则

**禁止**使用 `product_fact_source != unknown` 作为"不需要联网检索"的依据。

例如用户说：

- 品牌 = 赵宜主
- 产品 = 每日营养包女士版

此时：

- PRODUCT_FACT_SOURCE = user_input
- 但 PRODUCT_FACT_SUFFICIENCY = IDENTITY_ONLY

对于 Sell：事实仍然不足。如果 WEB_SEARCH 存在：**必须继续 Product Source Retrieval。**

> **Product name is not the same as sufficient product facts.**
> **User input may identify the product without being the Product Fact Source.**

---

## 二、PRE-GATE 0 — Product Acquisition（产品获取预检）

正式 Hard Gates 之前新增：

```
User Task
↓
Identify Product Clues
↓
Assess Product Fact Sufficiency
↓
Sufficient for current Purpose?

YES → G1 Product Truth
NO
↓
WEB_SEARCH available?

YES → Product Source Retrieval
NO → PRODUCT_FACT_LIMITED_MODE
```

只有完成 Product Acquisition 之后，才进入 G1 Product Truth。

**禁止**：先进入 G1，发现事实不足，然后直接要求用户提交资料。

---

## 三、Search Before Ask（先搜索，再询问）

建立最高优先规则：

> # If the agent can search, search before asking the user for product facts.

当同时满足：

1. 当前任务需要具体产品事实；
2. Product Facts 不足；
3. 用户已经给出品牌、产品名、型号、产品线等可搜索线索；
4. WEB_SEARCH available；

Agent 必须：**先搜索。**

禁止第一反应：

- "请上传详情页。"
- "请提供配料表。"
- "资料不足无法完成。"

只有执行过 Product Source Retrieval 以后仍不能解决，才可以请求用户补充信息。

---

## 四、WEB_ONLY 模式修复

当前类似：

> WEB_ONLY = External intelligence works but must rely on user-provided product facts.

删除。

正确：

**WEB_ONLY = WEB_SEARCH available, local file source unavailable.**

- 可以运行 Product Source Retrieval；
- 可以从经验证的当前产品官方网页建立 Product Ledger；
- 可以运行 External Intelligence；
- 没有 FILE_READ 只意味着不能读取本地 Product Skill/File；
- 不代表只能依赖用户提供 SKU 事实。

如果产品可通过公开官方来源识别：自动搜索。

---

## 五、WEB_SEARCH 有两种完全不同的任务

### A. PRODUCT_SOURCE_RETRIEVAL

回答：**当前这个具体产品到底是什么？**

目标：建立 P1 Product Facts。

### B. EXTERNAL_INTELLIGENCE

回答：**用户现在关心什么？**

目标：问题、趋势、竞争语境、外部知识。

二者不得混淆。所有 Adapter 都必须同时映射这两种能力。

---

## 六、Product Retrieval 优先于 External Intelligence

商业任务中，如果产品事实不足：

```
Product Source Retrieval
>
External Intelligence
```

因为：不知道产品是什么，搜索再多用户趋势也无法安全带货。

标准顺序：

```
Product Truth Acquisition
↓
External Intelligence
↓
Angle Discovery
↓
Writing
```

---

## 七、Product Identity Status（产品身份状态）

建立 PRODUCT_IDENTITY_STATUS：

- EXACT
- PARTIAL
- UNKNOWN

注意："用户写了产品名"不代表 EXACT。必须判断：这个名称是否唯一对应当前 SKU。

例如：品牌 + 产品系列，但存在多个年龄版本 / 多个规格 / 多个代际 / 多个配方 / 多个地区版本 → PARTIAL。

---

## 八、PARTIAL 也必须先搜

当前 Partial 状态不能直接 ask user。

正确：

```
PARTIAL
+
WEB_SEARCH
↓
先执行 SKU Discovery Search
```

目的：找出可能的官方 SKU 候选。

例如搜索发现：同一个女士营养包存在 20+ / 30+ / 40+ / 50+，则内部生成 CANDIDATE_SKUS。

- 如果一个候选明显唯一：自动继续。
- 如果多个候选仍合理：才向用户提出 Minimum Disambiguation Question。

---

## 九、Minimum Disambiguation（最小消歧）

如果搜索后仍有多个 SKU：只问区分 SKU 所需的最少问题。

例如：

- 不要："请提供配料表、营养表、价格、规格、详情页、售后……"
- 应该："我查到女士版有 20+/30+/40+/50+ 几个版本，你指哪一版？"

用户回答"30+" → Agent 自动继续搜索 30+ 对应的成分 / 规格 / 使用方式 / 价格 / 售后 / 官方卖点。

原则：

> # Ask for identity, not for information the agent can retrieve itself.

---

## 十、产品信息请求分成两种

### IDENTIFIER REQUEST（身份请求）

询问：哪个 SKU？哪个年龄版？哪个型号？哪个规格？

允许在搜索无法唯一确定时询问。

### PRODUCT DATA REQUEST（产品数据请求）

要求用户提交：详情页 / 配料表 / 规格 / 价格 / 售后。

只有以下情况才允许：

1. WEB_SEARCH 不存在；
2. 官方资料无法访问；
3. 产品是未公开新品；
4. 私域/内部 SKU；
5. 搜索后关键事实仍缺失；
6. 用户拥有的信息明显比公开资料更新。

否则：优先自己检索。

---

## 十一、Purpose-Specific Fact Minimum（目的化事实最低要求）

不要要求所有任务都拥有完整商品详情。

### Content

只需要完成核心命题所必需事实。

### Seed

需要：

- 产品/方案身份
- 支持偏好建立的核心事实

不要求：完整价格 / 完整售后 / 全部规格。

### Sell

通常需要更完整：

- Exact Product Identity
- Core Product Facts
- Key Differentiators
- Usage / Specification if relevant
- Main Proof
- Important Fit / Boundary
- Current Offer if the copy uses price
- After-sales only if used

但：某字段缺失不代表整篇不能写。只要当前 Angle 不依赖该字段，可以不用。

原则：

> # Missing optional facts should shrink the claim set, not automatically cancel the whole writing task.

---

## 十二、No Exhaustive Data Demand（禁止穷举式资料索取）

禁止出现这种默认回复：

> "请提供：成分表 / 营养表 / 规格 / 食用方式 / 核心卖点 / 价格 / 优惠 / 售后……"

除非这些全部对用户当前任务不可缺少，并且 WEB_SEARCH 已经失败。

Agent 必须优先问：

> # What is the minimum missing fact blocking this exact task?

---

## 十三、High-Risk Product Retrieval（高风险产品检索）

当检测到：营养补充剂 / 保健食品 / 食品营养 / 美妆功效 / 医疗相关

自动提高 Source Quality Threshold。

但：

> # Higher verification threshold ≠ no search.

正确行为：搜索更严格。不是：直接让用户交资料。

优先来源：

1. 产品官方标签/详情
2. 官方旗舰店当前 SKU
3. 官方说明/备案信息
4. 监管/标准资料（如适用）

第三方文章只能用于：外部背景或风险验证。不能替代产品标签。

---

## 十四、High-Risk Claims Separate（高风险主张分离）

营养产品搜索到资料以后，必须把 PRODUCT FACT 和 HEALTH / FUNCTION CLAIM 分开。

例如官方配料表写"含维生素B族、铁、钙等" → 这是 Product Fact。

但"改善代谢 / 抗衰 / 调节激素 / 改善贫血 / 增强免疫" → 属于更高风险功能/健康 Claim。

必须依据合法允许的当前标签/监管口径决定是否可以用于带货。

**禁止**：因为产品含某个营养素 → AI 自行推导身体效果。

---

## 十五、Search Discovery 和 Fact Retrieval 分两轮

### Round 1 — Identity Discovery

搜索：品牌 + 产品名。目的：确定 Exact Product / variants。

### Round 2 — Product Fact Retrieval

确定 SKU 后搜索：品牌 + Exact Product + 官方 + 配料/规格/食用方法/官方商城等。

避免：一开始搜到多个版本，然后把不同版本事实混在一起。

---

## 十六、搜索结果必须形成 Product Ledger

检索结束以后不能马上写。先建立内部 CANONICAL_PRODUCT_LEDGER。

每条至少：

- Fact
- Value
- Source
- Source Type
- SKU/Variant
- Observed Date if dynamic
- Confidence

然后 G1 Product Truth。这一步默认不展示给用户。

---

## 十七、Search Failure 才允许 Ask

只有执行过 Product Source Retrieval，结果 FAILED 或 AMBIGUOUS，才允许停下来问用户。而且必须说明具体缺什么。

正确：

> "我查到该产品有 20+/30+/40+/50+ 多个女士版本，目前无法确定你指哪一个。告诉我年龄版本即可，我继续查官方资料。"

不正确：

> "资料不足，请把产品详情全部发我。"

---

## 十八、禁止没有搜索就声称"资料不足"

如果 WEB_SEARCH = true 且 PRODUCT_FACT_SUFFICIENCY < required level，但 product_retrieval_status = NOT_NEEDED 或没有调用 Search，Agent 不得输出"目前仍缺少可用于带货的产品事实"。

这是 **Premature Information Request. Hard Gate FAIL。**

---

## 十九、Tool Use Evidence（工具使用证据）

Product Retrieval 触发后，内部必须留下 TOOL_EXECUTION_STATE：

- SEARCH_NOT_REQUIRED
- SEARCH_EXECUTED
- SEARCH_FAILED
- SEARCH_UNAVAILABLE

如果 SEARCH_EXECUTED，再判断是否足够。

不得："理论上我可以搜索"但实际上没调用工具，然后声称查不到。

---

## 二十、不要向用户暴露内部搜索流程

正常成功：Agent 直接完成文案。不需要先说"我要搜索产品"。除非宿主平台需要工具使用提示。

搜索成功后：默认不展示 Research Brief / Product Ledger。

如果需要一个最小 SKU 消歧：直接问一个问题即可。

---

## 二十一、素人 IP 带货特殊规则

"素人IP"不等于可以虚构消费者经历。

区分：

- ORDINARY_PERSON_TONE（真实自然的素人口吻 / 低广告感表达）
- REAL_PERSONAL_EXPERIENCE（真实个人经历）

用户要求"抖音素人IP带货"默认理解为 ORDINARY_PERSON_TONE。

不得自动生成：

- 我吃了三个月
- 我以前总是……
- 吃完之后身体……
- 我朋友都……
- 我老公说……
- 医生让我……

除非 IP Fact Source 支持。

产品事实可以通过 Product Retrieval 补齐。人物经历不能通过互联网替用户编。

---

## 二十二、最终执行顺序

```
TASK
↓
CAPABILITY DETECTION
↓
ROUTE
↓
PRODUCT FACT SUFFICIENCY
↓
PRODUCT ACQUISITION PREFLIGHT
↓
SKU DISCOVERY if needed
↓
MINIMUM DISAMBIGUATION if necessary
↓
OFFICIAL PRODUCT RETRIEVAL
↓
CANONICAL PRODUCT LEDGER
↓
G1 PRODUCT TRUTH
↓
EXTERNAL INTELLIGENCE if useful
↓
ANGLE DISCOVERY
↓
PURPOSE
↓
PLATFORM
↓
WRITE
↓
QA
↓
OUTPUT
```

绝对禁止：

```
TASK
↓
发现用户没给详情页
↓
直接把资料收集工作退回给用户
```

---

## 二十三、最终原则

> # Search Before Ask.
> # Product name is not the same as sufficient product facts.
> # User input may identify the product without being the Product Fact Source.
> # A capable Agent should retrieve public product facts itself.
> # Partial identity triggers discovery search, not immediate refusal.
> # Ask the user only for information that search cannot resolve.
> # High-risk product means search more carefully, not search less.
> # Missing one optional field means omit that claim, not cancel the whole task.
> # Product truth can be retrieved; personal experience cannot be invented.
