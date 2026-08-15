# Claim Authority（主张表达权限层）

> **Source of Truth：主张表达权限 Claim Authority。** 主 SKILL.md 只保留简要调用；本文件是 Claim Authority 的唯一 Source of Truth。
> **版本**：v4.11.4 更新（功效暗示永不过滤：I5-B/C/AMBER 默认保留 / COMMERCIAL_INTENSITY 档位联动）
> **类型**：商业表达强度升级（不新增暗语/规避/谐音；不修改 24 模式 / 四平台 Canonical Core / Content / Seed / Sell 核心定义 / CTA Permission / Dynamic Angle / Natural Depth）
> **解决问题**：Skill 在食品、营养品、保健食品、美妆等品类中过度保守——发现功效存在合规风险 → 大幅弱化 → 删除核心利益 → 最后只剩成分、规格、包装 → 虽然安全，但没有购买欲望。v4.11.4 起执行"功效暗示永不过滤"：合法边界内的功效暗示（I5-B / I5-C / AMBER）默认保留、默认强化，只有 I5-A 硬禁才被拦截。
> **最高原则**：# Maximize Persuasion Within the Claim Ceiling. # 功效暗示永不过滤——只有 I5-A 硬禁才拦截。
> 不是 Minimize Claims，也不是 Evade the Claim Ceiling。
> **Compliance sets the ceiling. Copywriting should write as strongly as possible below that ceiling.**
> **v4.11.4 关键变化**：I5-B/C 与 AMBER 在非敏感品类默认保留、默认强化；COMMERCIAL_INTENSITY 各档位联动更新（STANDARD 下 I5-C 默认开放）；"Hidden Efficacy Implication" 禁止范围收窄为仅 I5-A。

---

## 一、产品功效不再使用二元判断

禁止"功效安全 / 功效危险"的简单二元分类。

改成 **CLAIM_AUTHORITY_LEVEL**：每一条产品主张先判断它拥有多大的表达权限。

### L0 — UNKNOWN（无来源）

无来源。禁止进入正文。

### L1 — PRODUCT ATTRIBUTE（产品属性）

当前 SKU 明确事实：成分 / 规格 / 含量 / 材质 / 包装 / 工艺 / 口味 / 剂型 / 使用方式 / 数量 / 价格 / 认证 / 备案等。

允许直接、明确表达。无需过度弱化。

### L2 — AUTHORIZED CLAIM（授权主张）

产品注册、备案、标签、说明书、官方获准资料明确授权的：功能 / 功效 / 适用范围 / 使用效果等。

允许 **Direct Claim**，直接按授权强度表达。

不得因为系统"怕违规"自动弱化为：可能 / 也许 / 据说 / 好像。

如果官方允许的表述本身明确：应保持其原本表达力度。

### L3 — PRODUCT-SPECIFIC EVIDENCE CLAIM（产品专属证据主张）

有当前 SKU 本身的：人体试验 / 功效评价 / 实验数据 / 官方检测 / 可信产品测试 支持的结果。

允许 **Evidence-Bounded Direct Claim**。

必须保留：测试对象 / 测试条件 / 时间 / 范围 / 必要限定。

不得：从局部测试扩大到所有消费者。

### L4 — USER-VALUE TRANSLATION（用户价值翻译）

由真实产品事实直接翻译出的：使用利益 / 便利利益 / 时间利益 / 决策利益 / 生活方式利益。

这是商业文案重点放宽区域。

示例：

- Fact：每天独立一包 → "每天拿一包就行，不需要自己从好几瓶里搭。"
- Fact：一包已经组合多个营养素 → "对于嫌每天瓶瓶罐罐麻烦的人，这种组合方式更省事。"

这是 **Convenience Benefit**，不是未经授权的健康功效。允许大胆表达。

### L5 — AUTHENTIC EXPERIENCE（真实体验）

真实 IP 资料明确支持的：口感 / 使用感 / 便利程度 / 真实选择理由 / 主观偏好。

允许第一人称表达。

但不能：个人体验 → 推导大众必然效果。

### L6 — UNAUTHORIZED EFFECT CLAIM（未授权效果主张）

包括：没有产品授权/证据支持的：生理变化 / 身体改善 / 健康结果 / 疾病结果 / 治疗结果 / 预防结果 / 量化效果 / 普遍性结果。

默认不得进入正文。

不能通过：暗示 / 隐喻 / 缩写 / 谐音 / 场景暗示 / "懂的都懂" / 前后对比 / 表情动作 绕过。

---

## 二、Category Claim Ceiling（品类主张上限）

正式写产品文案前必须识别 **PRODUCT_REGULATORY_CATEGORY**：

- GENERAL_GOODS
- ORDINARY_FOOD
- HEALTH_FOOD
- NUTRIENT_SUPPLEMENT_HEALTH_FOOD
- COSMETIC
- MEDICAL_DEVICE
- DRUG
- OTHER

不知道时：如果 WEB_SEARCH 存在，自动查当前 SKU 的：官方标签 / 注册/备案身份 / 官方详情页 / 监管备案信息。

不能只根据"营养包 / 养生 / 美容 / 功能性"猜产品身份。

---

## 二·五、COMMERCIAL_INTENSITY（商业强度路由参数）

**v4.11.0 新增。** 路由时按品类 + 平台 + 用户目标选择商业强度档位。它控制"怎么说"，不改变"能说什么"。

### CONSERVATIVE（保守）

- 当前严格标准。
- I5-B/C 收紧为"只做受众上下文、不强化"；PARTIAL_PAIN 强表达但边界体现在不夸大；AMBER 不开放。
- 适用：敏感品类 / 平台规则严格 / 用户明确要求稳妥。

### STANDARD（标准，默认）

- **I5-B/C 默认保留、默认强化（v4.11.4）**；PARTIAL_PAIN 允许强表达（边界体现在不夸大）；AMBER 在非敏感品类开放。
- I5-B 作为受众上下文并落地到摩擦；I5-C 在非敏感品类默认开放（不再仅限 AGGRESSIVE）。
- 适用：大多数普通食品 / 日用品 / 非宣称功效化妆品。

### AGGRESSIVE（激进）

- 非敏感品类下允许更强场景冲击和身份暗示。
- I5-B/C 默认保留并强化；PARTIAL_PAIN 强表达；AMBER 灰色区充分使用；抖音情绪密度拉满。
- 仍禁止：I5-A 硬禁、硬功效偷渡、虚假疾病 / 灾难 / 稀缺、虚构身体结果。

**COMMERCIAL_INTENSITY 与 Claim Ceiling 的关系**：

- Claim Ceiling 是硬上限（L0-L6 / Category Ceiling / Strength Matching），任何档位都不得突破。
- COMMERCIAL_INTENSITY 只改变表达强度与暗示空间。
- 档位越高，表达越强，事实边界越不能动。

原则：

> # COMMERCIAL_INTENSITY 控制"怎么说"，Claim Ceiling 控制"能说什么"。
> # Maximize Persuasion Within the Claim Ceiling——档位越高，越要在 Ceiling 内把话说到最满。

---

## 三、普通食品（ORDINARY_FOOD）

可以强表达：

- 成分
- 营养成分
- 口味
- 工艺
- 规格
- 食用便利
- 场景
- 饱腹/口感等有可靠依据且法律允许的感官/产品属性
- 营养成分本身的真实信息

但不得升级成：

- 保健功能
- 疾病预防
- 疾病治疗
- 医疗效果
- 未授权身体功能改善

因此不要用暗语表达："气色好了 / 姨妈更舒服 / 熬夜扛得住 / 免疫力上来了 / 代谢快了 / 身体不虚了"——如果这些实质上仍然是在表达未经授权的身体功效：禁止。

但可以重新寻找真正的 **User Value**。

---

## 四、保健食品 / 营养素补充剂（HEALTH_FOOD / NUTRIENT_SUPPLEMENT_HEALTH_FOOD）

如果当前 SKU 属于依法注册/备案的保健食品：

首先检索并建立 **AUTHORIZED_CLAIM_SET**：

- 注册/备案保健功能
- 功效成分/标志性成分
- 含量
- 适宜人群
- 不适宜人群
- 食用量
- 食用方法
- 必要警示

正文允许：**把 AUTHORIZED_CLAIM_SET 讲清楚、讲具体、讲有购买价值。**

禁止系统因为"健康品类"自动全部弱化。

例如官方合法授权"补充多种维生素矿物质" → 可以明确说："它的备案功能就是补充多种维生素矿物质。" 而不是："里面有一些营养成分。"

但不得继续无依据推导："所以改善疲劳 / 所以气色更好 / 所以提高抵抗力"——除非该当前 SKU 本身有相应合法 Claim Authority。

---

## 五、美妆产品（COSMETIC）

COSMETIC 不得自动进入"功效不能说"。

先查：当前 SKU 备案/注册信息 + 功效宣称评价依据摘要 + 当前产品自己的官方功效资料。

如果当前 SKU 拥有充分依据的：保湿 / 抗皱 / 紧致 / 舒缓 / 控油 / 防晒 / 祛斑美白 等合法功效宣称，可以直接表达对应功效。

不同功效所需 Evidence Threshold 按当前法规和平台规则执行。

不要因为"这是功效"就全部删除。

原则：

> # Evidence-backed efficacy is a selling point, not a forbidden word.

---

## 六、Claim-to-Benefit Translation（主张到利益翻译）

当前系统太擅长 Fact Protection，但不够擅长 Benefit Translation。

增加强制流程：每个重要 Product Fact 问："So what for the customer?"

但答案只能进入以下合法 Benefit Domain：

1. Convenience（便利）
2. Time Saving（省时）
3. Ease of Use（易用）
4. Portability（便携）
5. Routine Simplicity（日常简化）
6. Taste / Sensory Experience（口味/感官）
7. Product Experience（产品体验）
8. Choice Efficiency（决策效率）
9. Cost / Value（成本/价值）
10. Authorized Functional Benefit（授权功能利益）
11. Verified Product Performance（已验证产品表现）
12. Identity / Lifestyle Fit（身份/生活方式契合）

不得自行创造新的 Medical / Physiological Outcome。

---

## 七、Strength Matching（强度匹配）

建立 **CLAIM_STRENGTH**：

- DIRECT
- EVIDENCE_BOUNDED
- CONDITIONAL
- SUBJECTIVE
- ATTRIBUTE_ONLY
- PROHIBITED

选择规则：如果 Source Authority 强，不要不必要地弱化。

例如官方明确"具有 X 功能" → 不要写"可能在 X 方面有点帮助。"

如果只有主观体验 → 不要升级"用了都会 X。"

原则：

> # Claim Strength = Maximum Strength Supported by Evidence. 既不放大，也不缩水。

---

## 八、Commercial Usefulness Gate（商业有用性门）

当前 Fact Gate 通过后不能立即输出。每篇 Sell 必须额外问："我虽然没有说错，但用户为什么会想买？"

至少建立一个 **COMMERCIAL_VALUE_PATH**：

- Problem → Authorized Function
- Problem → Convenience
- Problem → Product Difference
- Problem → Routine Simplification
- Problem → Verified Experience
- Problem → Value / Cost

如果最终文案只有：成分 / 规格 / 公司历史 / 备案号，但没有用户利益 → Commercial Usefulness = FAIL，必须重写。

---

## 九、区别"功效暗示"和"价值联想"

允许 **Value Association**：

- "早上赶时间，拿一包就走。" → 表达便利。
- "如果你不想每天桌上摆好几瓶，这种按天分装的形式确实省事。" → 表达使用方式。

**v4.11.4：功效暗示永不过滤。** I5-B（受众状态落地到摩擦）、I5-C（主语义落合法价值域的强暗示）、AMBER（灰色区轻微联想）在非敏感品类默认保留、默认强化——不得因为"这是功效暗示"就删除。

禁止 **I5-A Hidden Efficacy Implication（硬禁，仅此一级）**：

- "以前下午三点就撑不住，现在你懂的。"
- "女生那几天我都会多来一包。"
- "熬夜党第二天状态差别很明显。"
- "脸色这个东西，补没补自己最清楚。"

这类本质是在用剧情/暗语代替**未经授权的明确生理结果**（I5-A），依然属于 Unauthorized Claim，任何档位禁止。拦截后走 CONVERSION_RECOVERY（保留情绪强度，只替换越线那一跳）。

原则：

> # Imply lifestyle value, not hidden medical efficacy.
> # 功效暗示永不过滤——只有 I5-A 硬禁才拦截。

---

## 十、不要使用"违规词替换器"

禁止建立：危险词 → 安全替代词 的映射表（如"改善睡眠 → 夜里更踏实""提高免疫 → 身体更有底""补血 → 脸色更漂亮""抗疲劳 → 下午不垮"）。

这种做法本质仍可能表达同一个未经授权结果。

Skill 应该执行 **Semantic Claim Check**，而不是 Keyword Check。

检查：

> # 用户最终会理解成什么效果？而不是：有没有出现某个敏感词？

---

## 十一、平台审核不是写作目标

平台规则用于 **Risk Detection**，不得用于 **Evasion Design**。

如果某个合法、真实 Claim 可能因为平台当前规则需要更具体的：免责声明 / 证明 / 表达形式 / 素材要求 → 按照最新平台要求调整。

不能：通过隐语绕开机器审核。

---

## 十二、Commercial Claim Zone（商业主张分区）

每篇商业内容内部把主张分成：

### GREEN ZONE（绿色区）

- 当前 SKU 明确事实
- 授权 Claim
- 真实价格/规格
- 真实体验
- 直接使用利益

允许大胆讲。

### AMBER ZONE（琥珀区）

- 有证据但条件较多
- 有限测试
- 行业知识向当前 SKU 解释
- 适配性判断
- **非敏感品类下的轻微功效联想（v4.11.4 默认保留）**：主语义落合法价值域（省事 / 更简单 / 更容易坚持 / 选择更少 / 身份感）的强暗示，默认保留、默认强化，不得因"有轻微联想"降级或删除

要求：准确限定；非敏感品类下按"功效暗示永不过滤"原则保留，敏感品类下收紧。

### RED ZONE（红色区）

- 未授权疾病功效
- 未授权保健功能
- 绝对效果
- 必然结果
- 虚假前后对比
- 隐语偷渡功效
- 将原料功效自动等同于产品功效

禁止。

核心改变：

> # GREEN 不要因为 RED 存在就一起变弱。

---

## 十三、素材优先寻找"可卖的绿色事实"

联网 Product Retrieval 不能只问"哪些话不能说？"必须主动搜索：

> # What can we strongly and truthfully sell?

例如：

- 当前 SKU 真正授权功能
- 配方组合
- 每日剂量
- 独立包装
- 食用方式
- 原料来源
- 规格
- 味道
- 技术
- 检测
- 备案
- 产品设计
- 使用便利
- 与目标消费者真实需求的匹配

目标：

> # Expand the sellable truth set. 而不是：只扩大禁用词库。

---

## 十四、不同商业身份使用同一 Claim Ceiling

达人 / 素人 IP / 品牌商家 / 店主 / 创始人 在同一产品上的产品功效权限必须相同。

禁止：

- "素人可以用个人体验暗示功效。"
- "达人说体验就能绕过 Product Claim。"
- "商家不能说，但用户口吻可以说。"

身份影响：叙述方式。不改变：产品事实权限。

---

## 十五、真实个人体验可以增强说服力，但不能成为功效许可证

如果 IP Fact Source 真实支持："我每天都会吃 / 我觉得这个形式方便 / 我能接受这个口味" → 可以表达。

如果真实支持某种身体体验：必须同时判断该身体结果是否允许用于当前商业传播。

> # True personal experience does not automatically equal legal commercial claim.

---

## 十六、Conversion Recovery（转化恢复）

如果一个最想讲的功效最终不能合法使用，Skill 禁止直接"那就什么都不说"。

启动 **Conversion Recovery**：

问：这个消费者为什么原本会因为该 Claim 产生购买欲？

然后寻找同需求下可以合法表达的：

- Authorized Claim
- Product Attribute
- Convenience
- Routine Value
- Product Design
- Verified Difference
- Cost
- Ease
- Taste
- Format
- Risk Reduction

重新建立购买理由。

**v4.11.0 强化：Recovery 必须保留情绪强度和场景冲击力。**

1. **不删除整段利益表达**——只替换越线的那一跳；
2. 把"产品改善身体"那一跳换成"产品把这件事变简单"的合法价值跳；
3. **禁止直接删成参数列表**（那等于放弃销售，违反 Sell Commercial Density）；
4. 恢复后必须重新检查：是否仍满足"1 个强 Pain/Desire + 1 个真实差异 + 1 个用户 Benefit + 1 个证明 + 1 个选择理由"。

示例：

- 越线："第二天状态差别很明显。"（主语义 = 产品改善身体状态）
- 恢复："每天这件事不用再想，坚持这件事本身就变简单了。"（主语义 = 执行更简单，情绪强度保留）

目标：

> # Lose the illegal claim, not the sale.
> # 越线的那一跳可以换，情绪强度和场景冲击力要留下。

---

## 十七、Sell Copy 最低商业要求

每篇卖货稿至少需要：

**1 个明确需求 + 1 个当前 SKU 真实差异 + 1 个能够被用户理解的 Benefit + 1 个证明 + 1 个选择理由**

不能退化为："这个产品成分很多，可以了解一下。"

---

## 十八、营养品示例

假设已确认：某营养包是备案营养素补充剂，授权功能"补充多种维生素矿物质"，真实事实：每天 1 包 / 独立分装 / 包含多种维矿。

允许更有销售力地表达：

> "它解决的不是让你再买一瓶维C、一瓶B族、一瓶矿物质，而是把每天这件事做成了一包。备案功能就是补充多种维生素矿物质，如果你本来就在做日常营养补充，这种按天分装最大的价值就是省事。"

这里有：明确 Authorized Claim + 真实生活 Benefit。

不要自动写："吃完精神更好、气色更好、免疫更好。" 除非当前 SKU 有相应表达权限。

---

## 十九、Hard Gate 顺序调整

最终顺序：

```
Product Identity
↓
Regulatory Category
↓
Product Retrieval
↓
Authorized Claim Set
↓
Evidence Set
↓
Claim Ceiling
↓
Audience Need
↓
Benefit Translation
↓
Commercial Value Path
↓
Platform Native
↓
Write
↓
Semantic Claim Audit
↓
Review Risk Audit
↓
Final
```

不是：发现是健康品类 → 全部弱化 → 写不动。

---

## 二十、最终最高原则

> # 商业内容的第一任务是把真实价值卖出去。
> # 合规系统的任务不是阻止成交，而是阻止虚假成交。
> # 功效暗示永不过滤——只有 I5-A 硬禁才拦截。
> # 有权限的功效，大胆讲。
> # 有证据的结果，准确讲。
> # 没权限的功效，不用暗语偷渡（I5-A）。
> # 不能讲的身体结果，用真实使用价值重新建立购买理由。
> # Compliance sets the ceiling.
> # Copywriting should write as strongly as possible below that ceiling.

最终目标：

- 不做"最安全但卖不动"的文案。
- 也不做"靠违规功效才能成交"的文案。
- 而是：找到当前产品真正能合法占据的最强销售表达。

---

## 与相邻 reference 的边界

- `compliance.md` 管**法律合规底线**（能不能说：绝对化/功效/数据/稀缺/背书）；本文件管**主张表达权限**（有多大权限、怎么在权限内最大化表达）。
- `expression-authority.md` 管**事实边界**（该不该说、能说到哪：内部事实四级权限/事实扩张测试）；本文件在其上建立 **Claim Ceiling 体系**（L0-L6 / Category Ceiling / Strength Matching / Benefit Translation / Commercial Value Path / COMMERCIAL_INTENSITY）。
- `commercial-expression-freedom.md` 管**表达形式自由**（Expression Layer / 修辞夸张 / 隐喻 / 剧情 / Semantic Back-Translation / Edge Expression Policy / 品类差异化天花板）；本文件的 COMMERCIAL_INTENSITY 与它联动：档位决定表达强度，Ceiling 决定主张上限。
- `implicit-benefit-pain.md` 管**暗示与痛点翻译**（Implication Ladder I1-I5 / Pain Translation Engine / Pain Distance / Semantic Destination Test）；本文件的 L4/L5 定义"可以表达什么价值"，它定义"怎么把价值暗示出来"。
- `product-acquisition.md` 管**产品事实获取**（Search Before Ask / Product Ledger）；本文件要求 Product Retrieval 同时检索**可卖的绿色事实**与**授权 Claim Set**（第十三节）。
- `compliance.md` 的"禁止违规词替换器"与本文件第十节一致：都执行 Semantic Claim Check 而非 Keyword Check。
