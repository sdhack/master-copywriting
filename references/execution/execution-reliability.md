# Execution Reliability Patch（执行可靠性补丁）

> **版本**：v1.0（v3.6 新增）
> **类型**：执行可靠性补丁（不新增创意框架/钩子/公式/平台理论/24模式/角度发现/外部情报架构）
> **解决问题**：Skill 知道规则，但 Hard Gate 没有稳定阻止错误成品输出
> **第一原则**：Truth before Strategy. Strategy before Style. 写得差可以重写，写错事实不能输出。

---

## 一、Hard-Gate Execution Order（硬门槛执行顺序）

最终生成必须严格按照以下 Gate 顺序执行。任何后面的 Gate 都不能覆盖前面的失败。

```
PRE-GATE 0 — Product Acquisition（Search Before Ask）
  ↓
GATE 1 — Product Truth
  ↓
GATE 2 — Numeric / Calculation Integrity
  ↓
GATE 3 — IP / Commercial Identity Truth
  ↓
GATE 4 — External Claim Integrity
  ↓
GATE 5 — Demonstration / Comparison Truth
  ↓
GATE 6 — Purpose Completion
  ↓
GATE 7 — Platform Native
  ↓
GATE 8 — Natural Depth / Humanization
  ↓
GATE 9 — Set-Level Diversity
  ↓
GATE 10 — Final Output Sanitizer
```

### PRE-GATE 0 — Product Acquisition（产品获取预检）

正式 Hard Gates 之前，先完成产品事实获取。完整规则见 `references/execution/product-acquisition.md`。

- 识别 Product Clues（品牌 / 产品名 / 型号 / 产品线）
- 评估 PRODUCT_FACT_SUFFICIENCY（NONE / IDENTITY_ONLY / PARTIAL_FACTS / SUFFICIENT_FOR_CONTENT / SUFFICIENT_FOR_SEED / SUFFICIENT_FOR_SELL）
- 不足且 WEB_SEARCH 存在 → 先执行 Product Source Retrieval（Search Before Ask）
- 只有检索 FAILED / AMBIGUOUS 才允许向用户请求最小信息（IDENTIFIER REQUEST，不是 PRODUCT DATA REQUEST）
- 禁止：没有搜索就声称"资料不足"（Premature Information Request = Hard Gate FAIL）

### 核心原则

**Truth before Strategy. Strategy before Style.**

如果 Fact Gate 失败：

不得因为 Platform Fit 很好 / Purpose 完成 / 文案很自然 / Angle 很漂亮 / 转化很强 而放行。

**Fact Gate 失败 = 整篇失败。**

不是"其他 9 项通过所以总体可以"。

### 各 Gate 定义

| Gate # | Gate 名称 | 检查什么 | 失败 = 什么 |
|---|---|---|---|
| G1 | Product Truth | 产品事实是否全部来自 Canonical Product Ledger | 任何产品事实漂移/虚构/越界 |
| G2 | Numeric / Calculation Integrity | 数字数学正确 + 单位正确 + 输入事实正确 | 计算错误/单位偷换/输入事实不对 |
| G3 | IP / Commercial Identity Truth | 身份真实、第一人称真实、商业关系真实 | 虚构经历/身份越界/伪 UGC |
| G4 | External Claim Integrity | 外部知识准入、强度匹配、无级联越权 | 外部事实越权/主张级联/研究奖励作弊 |
| G5 | Demonstration / Comparison Truth | 演示真实、对比有证据、画面不预写结果 | 虚构观察结果/虚构对比数据/伪对照镜头 |
| G6 | Purpose Completion | Seed 真的建立偏好？Sell 真的完成决定？ | Seed 只是 Content / Sell 只是 Seed |
| G7 | Platform Native | 平台原生、证据偏好匹配、命题重新立题 | 平台互换失败/只是换包装 |
| G8 | Natural Depth / Humanization | 自然充分度、真人感、无模板感 | AI 感/模块感/产品说明书感 |
| G9 | Set-Level Diversity | 多角度、多角色、多 IP 资产、不重复 | 伪多版本/固定五件套/角度过弱 |
| G10 | Final Output Sanitizer | 内部 metadata 全部剥离 | 泄露内部标签/验证/路由 |

---

## 二、Canonical Product Ledger（标准产品台账）

同一 SKU 的一次任务中，先从 Sell-point Skill 抽取**唯一的** Canonical Product Ledger。

### 台账包含字段

- 克重
- 包装规格
- 每盒数量
- 价格
- 优惠
- 泡数
- 冷泡比例/方法
- 热泡比例/方法
- 工艺
- 香型
- 原料
- 人物（传承人/品牌人）
- 售后
- 其他所有 P1 级产品事实

### 铁则

**四个平台 × Content/Seed/Sell 全部共享同一个现实。**

- 任何平台不得修改
- 任何 Purpose 不得修改
- 任何 Creative Variation 不得修改
- 任何 External Intelligence 不得修改
- 任何 Humanization 不得修改

**Different Copy, Same Reality.**

---

## 三、Cross-Output Product Consistency（跨输出产品一致性）

一次生成 8 篇（4 平台 × Seed/Sell）完成后，统一扫描所有 SKU 事实，自动比较：

- 数字是否一致？
- 规格是否一致？
- 泡法是否一致？
- 泡数是否一致？
- 价格是否一致？
- 人物是否一致？
- 工艺是否一致？
- 售后是否一致？

### 冲突示例

- 一个稿说 100 克 11 颗，另一个稿不能说 100 克 20 颗
- 一个稿使用 1/4 颗冷泡，另一个不能自动整颗冷泡
- 一个稿说"兰花香+奶香"，另一个不能说"蜜兰香+桂花香"

### 冲突处理

如果冲突 → **不允许输出**。回到 Canonical Product Ledger 修复。

---

## 四、Calculation Semantics（计算语义）

升级 Numeric Integrity 为 Calculation Semantics。

**不仅检查：1 + 1 是否算对。**
**还检查：算的到底是不是同一个单位。**

### 示例

价格 ÷ 克数 → 得到的是 **元/克**。
不能直接叫 **元/泡**。

要得到元/泡：
必须拥有：**每泡投茶克数**。

### 单位清单

所有商业计算先建立单位：
- RMB（元）
- gram（克）
- piece（颗/片/块）
- brew（泡）
- box（盒）
- day（天）
- use（次/使用）

### 三层校验

| 层级 | 检查 |
|---|---|
| Equation Correct? | 数学计算是否正确 |
| Unit Correct? | 单位是否匹配，是否偷换单位 |
| Input Facts Correct? | 输入的数字是否来自 Canonical Ledger |

**三项全部通过才能使用。**

---

## 五、Comparison Evidence Gate（对比证据门）

凡是生成：A 产品 vs B 产品 / 三款对比 / 竞品比较 / 品类价格对比

必须判断：**比较数据来自哪里？**

### 如果没有真实来源 → 禁止自动创造

禁止虚构：
- 价格
- 克重
- 泡数
- 使用体验
- 口感
- 缺点
- 性价比

尤其禁止：**"我最近试了三款……"**（无来源时 = 虚构试喝经历）

### 可以做：Decision-Dimension Comparison

用户在铁观音、单丛、乌龙茶之间选择时，可以比较：
- 香型倾向
- 常见品类特点
- 选择问题
- 适合什么样的人

但具体价格和体验：**必须有真实数据来源。**

### 原则

**Compare dimensions freely. Compare facts only with evidence.**

---

## 六、Seed Completion Gate 重新定义

### 当前错误

系统容易认为：
无价格 + 无售后 + 无 CTA = Seed

**错误。**

### Seed 必须产生：Preference Shift

用户从"无感/不知道"变成"我开始偏向这种产品、这种解决方案或当前 SKU"。

### 每篇 Seed 必须回答

> 用户最后偏好了什么？

### 如果答案只是

- "这个人挺靠谱。"
- "我学会了一个方法。"
- "我知道怎么选茶了。"
- "我获得了一个观点。"

但没有形成任何 **Product / Solution Preference** → 是 **Content**，不是 **Seed**。

---

## 七、Seed Preference Target（种草偏好目标）

生成 Seed 之前内部明确：**Preference Target 是什么？**

### 可能的 Preference Target

- 当前 SKU
- 当前产品类别
- 某个工艺路线（如焙火 vs 抽湿）
- 某种解决方案（如冷泡 vs 热泡）
- 某种使用方式（如日常口粮 vs 送礼）
- 当前 IP 的选择标准

### 示例

视频号 Seed：
- 如果全文只是"我选茶不追名气" → 这是 **IP Content**
- 如果进一步自然形成"所以对日常喝的人，我会更偏向这种原料/工艺/价值结构的茶" → 才开始进入 **Seed**

---

## 八、Sell 的 Angle 不能自动获得额外事实权限

### 系统目前容易出现的问题

先选择"新手推荐"Angle → 然后为了证明新手适合，自动创造：
- 接受度高
- 大多数人喜欢
- 不苦涩
- 容错率高
- 泡久也不会难喝

**禁止。**

### 正确顺序

```
Product Facts
  ↓
Can these facts support "Newbie Recommendation"?
  ↓
YES → 使用 Angle
NO → 换 Angle
```

### 最高原则

**Facts choose the angle. The angle never manufactures facts.**

---

## 九、Audience Fit Claim Gate（人群适配主张门）

所有"适合 X 人群"类主张必须检查来源：

| 来源类型 | 示例 | 处理 |
|---|---|---|
| A. Product Fact 明确支持 | "焙火茶更耐泡，适合喝得多的人"（耐泡=Fact，喝得多=需求条件） | ✅ 可以 |
| B. 用户需求条件推导 | "如果你在意耐泡度和性价比，这款适合" | ✅ 优先用条件式 |
| C. AI 人口标签想象 | "新手都适合""长辈肯定喜欢""女性爱喝" | ❌ 禁止 |

### 优先表达

**条件式匹配**："如果你在意 X、需要 Y……"
**而非人口标签**："新手都适合。"

---

## 十、Demonstration Truth 再次强化

视频脚本里的画面建议不能创建结果。

### 已知"产品可以冷泡"时

✅ 可以设计：
- 放入冰箱
- 第二天拍真实成品
- 实际喝

❌ 最终画面描述不要预写（除非是 Known Result）：
- "喝一口马上点头"
- "第三泡明显变厚"
- "第十泡香气还很浓"

### 更好的画面说明

> **拍摄时真实记录实际结果，以现场表现为准。**

---

## 十一、禁止 Fake Comparison Visual（伪对比画面）

如果没有真实对照样本，不要建议：

> 好叶底 vs 普通叶底

这种镜头。

### 为什么禁止

否则拍摄阶段会被迫：
- 找一个差的茶充当对照
- 制造不公平比较
- 伪造"普通产品"

### 规则

没有真实、同条件对照 → 只展示当前产品。

---

## 十二、First-Person Claim Scanner 继续升级

### 新增扫描关键词（除原有外）

- 经常有人问我
- 最近很多人问
- 我的朋友
- 我的客户
- 我一直推荐
- 我自己店里放了
- 我最近试了几款
- 我常喝
- 我每天
- 我做了几年
- 我开了几年
- 我一直这么选

### 铁则

没有 IP Fact Source → 不得使用。

即使这些句子非常平台原生，也不能使用。

---

## 十三、External Thesis Gate（外部论题门）

尤其针对公众号。

AI 可以通过互联网发现好问题（茶叶存放 / 被低估 / 工艺差异）。

但标题一旦提出一个 Thesis，例如"为什么有些茶越放越好喝"，正文中的核心因果必须真的有可靠来源。

### 禁止

先有漂亮论题，再用 AI 常识补齐整套理论。

### 如果 Research 不足以支持

换成更窄、更准确的论题。

### 原则

**Better a narrow true thesis than a broad impressive thesis.**

---

## 十四、QA 不能自我庆祝

禁止内部出现类似逻辑：

```
Purpose验证 ✅
Product Removal ✅
Platform Native ✅
→ 直接放行
```

每个 ✅ 只有在 Hard Gates 全部通过后才有效。

### 铁则

**Fact Gate 失败 = 整篇失败。**

不是"其他 7 项通过，所以总体可以"。

---

## 十五、Final Output Sanitizer（最终输出清洗器）

最终用户只要求文案时，必须删除所有内部信息：

- Product Role
- IP Asset
- Primary Proof
- Purpose 验证
- Demo Truth 验证
- Reasoning Consistency
- Route
- Angle Score
- Source Type
- Fact Ledger
- QA 结果
- 模式判定
- Creative Driver
- 任何内部标签

### 最终只留下

用户真正需要的：
- 标题
- 正文 / 口播
- 必要的画面建议（画面建议本身也受事实约束）

### 例外

如果用户明确要求"把创作逻辑也给我"，才展示分析。

---

## 十六、Internal Metadata 永远不得反向驱动正文

例如内部指定：
- IP Asset = 会生活

不代表正文必须编：
- "我每天都这样喝。"

内部指定：
- IP Asset = 对朋友负责

不代表必须编：
- "我经常给朋友推荐。"

### 规则

内部资产只能指导**现在的判断和表达**。
不能创建**过去的经历**。

---

## 十七、8 篇终检表

一次生成 Douyin Seed / Douyin Sell / XHS Seed / XHS Sell / OA Seed / OA Sell / Channels Seed / Channels Sell

输出前统一检查 12 项：

| # | 检查项 | 对应 Gate |
|---|---|---|
| 1 | Same SKU, same facts? | G1 Product Truth |
| 2 | 所有数字一致吗？ | G2 Numeric Integrity |
| 3 | 所有计算单位正确吗？ | G2 Calculation Semantics |
| 4 | Seed 真的建立偏好吗？ | G6 Purpose Completion |
| 5 | Sell 真的完成决定吗？ | G6 Purpose Completion |
| 6 | 有没有为了 Angle 补事实？ | G1 + G5 |
| 7 | 有没有虚构对比对象？ | G5 Comparison Truth |
| 8 | 有没有虚构实测过程？ | G5 Demonstration Truth |
| 9 | 有没有虚构人物经历？ | G3 Identity Truth |
| 10 | 外部论题是否有足够来源？ | G4 External Claim |
| 11 | 八篇是否平台重新立题？ | G7 Platform Native |
| 12 | 内部 metadata 是否全部被剥离？ | G10 Output Sanitizer |

### 任何 Hard Gate 失败

先修复，再输出。

---

## 十八、最终优先级

```
1. Truth（事实真实）
2. Identity（身份真实）
3. Numeric Integrity（数字完整）
4. Purpose（目的完成）
5. Platform（平台原生）
6. Naturalness（自然度）
7. Conversion（转化力）
8. Creative Variation（创意多样性）
```

**禁止：为了后面的目标破坏前面的目标。**

---

## 十九、最终最高原则

> **写得差可以重写，写错事实不能输出。**
> **Seed 不是"没有 CTA"，而是"产生偏好"。**
> **Sell 不是"信息更多"，而是"完成决定"。**
> **画面可以设计，结果不能预演。**
> **对比可以设计维度，数据不能编。**
> **八篇可以有八种创意，只能有一套现实。**
> **内部系统越复杂，最终用户看到的反而应该越干净。**

---

## 二十、No Fake Memory Gate（禁止伪记忆）（PATCH 33）

所有涉及"历史"的执行规则，只有在以下任一条件成立时才能执行：

- `MEMORY` capability 存在
- 用户当前上下文明确提供 Content History
- 当前会话历史确实包含相关内容

涉及项包括：

- 上一批次
- 历史使用次数
- 最近 30 篇
- 长期频率
- 跨批次轮换

条件不成立时：**只执行 Current Batch QA。**

不得假装记得上一批用了什么，不得虚构使用次数。

原则：

**No memory capability → no cross-session memory claim.**

---

## 二十一、Research / Tool Claim Integrity（研究/工具声称完整性）（PATCH 34）

没有实际执行工具，不得声称工具结果。

### 21.1 没有 WEB_SEARCH

不得说：

- 最近大家都在搜
- 现在流行
- 网友都在讨论
- 根据搜索结果
- 当前市场趋势
- 最近很火

除非这些内容已经出现在用户当前上下文（用户自己提供）。

### 21.2 没有 FILE_READ

不得说：

- "根据你的产品 Skill……"
- "根据你的 IP 资料……"

除非该内容已经出现在当前上下文。

### 21.3 没有 CODE_EXECUTION / CALCULATOR

复杂商业计算（如单克价、单泡价、组合优惠）要么谨慎人工核算，要么省略。

不能假装运行了工具。

### 21.4 没有 MEMORY

不得声称：

- 上一批用了什么
- 历史使用次数
- 最近 30 篇
- 长期频率

只做 Current Batch QA。

### 原则

**Capability affects what can be verified, not what is allowed to be invented.**
