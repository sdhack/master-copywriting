# Implicit Benefit & Pain Translation（暗示利益与痛点翻译层）

> **Source of Truth：暗示利益与痛点翻译 Implicit Benefit & Pain Translation。** 主 SKILL.md 只保留简要调用；本文件是该层的唯一 Source of Truth。
> **版本**：v4.11.4 更新（功效暗示永不过滤：I5-B/C 默认保留 / CONTEXT_PAIN 可作主卖点 / 语义回译保留强度）
> **类型**：商业表达强度升级（不新增暗语/规避/谐音；不修改 24 模式 / 四平台 Canonical Core / Content / Seed / Sell 核心定义 / CTA Permission / Dynamic Angle / Natural Depth / Claim Authority）
> **解决问题**：Skill 对食品、营养品、美妆等品类仍存在——发现功效风险 → 删除功效 → 文案失去痛点 → 最后只能介绍产品参数。v4.11.4 起执行"功效暗示永不过滤"：合法边界内的功效暗示（I5-B / I5-C / AMBER）默认保留、默认强化，只有 I5-A 硬禁才被拦截。
> **最高原则**：# 功效暗示永不过滤——只有 I5-A 硬禁才拦截。Loosen implication around value, not around unauthorized efficacy.
> 不是：把"永不过滤"理解成通过换词、暗语、剧情、表情、谐音继续表达一个本身没有权限的医疗/保健/生理功效（那是 I5-A 硬禁）。
> **v4.11.4 关键变化**：I5-B / I5-C 从"谨慎开放/条件开放"改为"默认保留、默认强化"；CONTEXT_PAIN 从"不能当主卖点"改为"非敏感品类可作为主卖点"；Semantic Destination Test 的 CONVERSION_RECOVERY 优先保留情绪强度与场景冲击力，只替换越线的那一跳。

---

## 一、Implication Ladder（暗示阶梯）

暗示不再一刀切禁止。分成 5 级，从完全开放到绝对禁止。

### I1 — Product Experience Implication（产品体验暗示）

**完全开放。**

通过真实产品事实，让用户自然想象产品体验。

示例：

- Fact：独立日包 → "早上抓一包就走。"
- 无需说"很方便"，让场景自己完成利益表达。

### I2 — Lifestyle Benefit Implication（生活方式利益暗示）

**开放。**

允许从真实产品属性自然联想到：

- 省事
- 少折腾
- 更容易坚持
- 更适合忙碌生活
- 减少选择负担
- 日常管理更简单
- 携带方便
- 时间成本更低
- 使用门槛更低

示例：

> "如果你最烦每天桌上一排瓶瓶罐罐，这种按天分好的形式，至少不用每天重新想今天该拿哪几瓶。"

这是生活利益，不是健康功效。

### I3 — Emotional / Identity Implication（情绪/身份暗示）

**开放。**

允许用户联想到：

- 我终于把这件事安排明白了
- 更有秩序
- 对自己认真一点
- 少一点内耗
- 生活更从容
- 做选择更安心

但必须来自真实使用场景，不要写成空洞鸡汤。

### I4 — Conditioned Functional Implication（有条件的功能暗示）

**谨慎开放。**

当产品拥有 Authorized Claim 或充分产品证据时，可以：不机械重复官方术语，而是把它翻译成用户能够理解的需求语言。

示例：

- 官方 Authorized Claim：补充多种维生素矿物质。
- 可以围绕："平时本来就在做日常维矿补充的人，它把这件事从好几瓶变成了一包。"

这里：官方功能仍然明确存在，文案重点翻译成"用户为什么需要这个产品"。不得继续升级为新的身体效果。

### I5 — Hidden Health / Medical Implication（隐藏健康/医疗暗示）

**v4.11.0 起拆分为三级：I5-A 硬禁 / I5-B 高风险可上下文 / I5-C 可接受强暗示。** 不再一刀切禁止。

#### I5-A — Hard Prohibition（硬禁）

如果合理消费者最终会理解成：

- 改善疾病
- 预防疾病
- 治疗
- 改善某生理指标
- 改善激素
- 补血
- 抗疲劳
- 提高免疫
- 改善睡眠
- 减肥
- 改善月经
- 改善焦虑
- 改善某器官功能

而当前 SKU 没有对应表达权限，即使没有出现这些词，仍然属于 Unauthorized Claim。

**硬禁。** 任何品类、任何 COMMERCIAL_INTENSITY 下都不得进入正文。

禁止使用："懂的都懂" / "女生那几天……" / "下午三点不垮了" / "第二天状态差别很明显" / "脸色这个东西自己照镜子" / "睡得踏实多了" 等方式偷渡。

#### I5-B — High-Risk but Contextual（高风险但可上下文）

**默认保留（v4.11.4）。** 状态差 / 疲劳 / 皮肤焦虑 / 年龄焦虑 / 熬夜 / 饮食不规律等，允许作为 **Audience Context** 出现，且默认保留、默认强化——不得因为"这是功效风险"就把受众状态描述删掉。

落地指引（用于把 I5-B 写得更强，不是用于过滤）：

1. 作为受众状态描述出现，落地到产品实际解决的摩擦（携带 / 搭配 / 选择 / 执行 / 计量 / 口感）；
2. 主语义不变成"产品在改生理"——Semantic Back-Translation 后，消费者理解的主效果落在合法价值域（省事 / 更简单 / 更容易坚持 / 选择更少）；
3. 只有 Back-Translation 后主语义明确滑向 I5-A（产品在治疗/预防/改善生理结果）才被拦截，拦截时走 CONVERSION_RECOVERY（保留情绪强度，只替换越线那一跳）。

示例（允许，默认保留）：

> "天天外卖、三餐没个准，是很多上班族真实生活状态。这种按天分装的形式，至少不用每天重新想该拿哪几瓶。"

示例（I5-A 硬禁，拦截后恢复）：

> "天天外卖身体亏空，吃这个补回来。"（主语义 = 产品做生理修复 → 拦截 → 恢复为"把每天这件事变简单"的合法价值跳）

#### I5-C — Acceptable Strong Implication（可接受强暗示）

**默认保留（v4.11.4，非敏感品类）。** 在普通食品 / 日用品 / 非宣称功效化妆品下，更强的情绪、身份、生活方式暗示默认保留、默认强化——只要 Semantic Back-Translation 后主语义仍落在合法价值域。

允许（默认保留，可强化）：

- 更强的身份认同："对自己认真一点的人，会把每天这件事安排明白。"
- 更强的生活方式暗示："不是再给生活加一个任务，而是把原来复杂的任务收起来。"
- 更强的情绪表达："最烦的不是贵，是每天还得想今天吃哪几瓶。"

边界：主语义必须落在 Convenience / Routine Simplicity / Choice / Identity / Lifestyle / Sensory 等合法价值域。若 Back-Translation 后消费者理解的主效果变成"产品改善某种身体状态"→ 降级为 I5-B 处理（落地到摩擦）或按 I5-A 拦截后走 CONVERSION_RECOVERY——不得直接删除整段暗示。

**COMMERCIAL_INTENSITY 联动（v4.11.4）**：I5-B / I5-C 在 STANDARD / AGGRESSIVE 下默认保留、默认强化；CONSERVATIVE 下 I5-B/C 收紧为"只做受众上下文、不强化"；I5-A 任何档位硬禁。

---

## 二、Pain Translation Engine（痛点翻译引擎）

当前系统不要只问"用户有什么痛点？"，必须把痛点拆成五层：

### P1 — Surface Complaint（表面抱怨）

用户嘴上说什么？

示例："每天吃营养品太麻烦。"

### P2 — Daily Friction（日常摩擦）

现实中到底哪里麻烦？

示例：早上赶时间；好几瓶；经常忘；出差不方便；不知道今天拿什么。

### P3 — Emotional Cost（情绪成本）

这个摩擦带来什么心理感受？

示例：烦 / 懒得坚持 / 觉得复杂 / 容易放弃 / 选择疲劳。

### P4 — Desired Progress（期望的变化）

用户真正想要什么变化？

示例："我希望这件事简单一点。"

注意：这里不要自动变成身体功效。

### P5 — Product Bridge（产品桥梁）

当前 SKU 哪些真实事实能够接住这个 Desired Progress？

示例：

- 独立日包 + 组合式设计 + 每天按量使用
- → "把每天要做的一堆选择，变成拿一包。"

这就是 **Pain Translation**。

---

## 三、从"症状痛点"向"生活痛点"下沉

健康/营养品用户经常会说："累 / 气色差 / 熬夜 / 状态不好 / 饮食不规律"。

不要立刻把这些词绑定成产品治疗目标。应该进一步翻译。

示例："饮食不规律"可以产生合法内容方向：

- 平时很难每天精确安排饮食
- 日常营养管理复杂
- 不想自己买一堆单品组合
- 出差时携带麻烦

如果产品事实能够支持这些场景：就写这些真实摩擦。

不要自动："所以吃这个改善营养不良/提高免疫。"

---

## 四、痛点允许更狠，但必须真实

**放宽痛点表达强度。**

允许说：

- "最烦的不是贵，是每天还得想今天吃哪几瓶。"
- "买了一桌子，真正能每天坚持的没几个。"
- "很多东西不是买不起，是复杂到最后懒得弄。"

前提：这是合理的用户摩擦/场景表达，而不是虚构疾病焦虑。

**禁止**为了卖货制造：

- "你现在不补以后身体就……"
- "长期缺这个一定会……"
- "女人过了30不补就……"

这种恐惧。

原则：

> # Intensify real friction. Do not invent health fear.

---

## 五、从 Product Fact 做三次翻译

每个关键卖点至少内部完成：

```
FACT
↓
FUNCTION
↓
USER VALUE
↓
SCENE
```

示例：

- FACT：每日独立包装。
- FUNCTION：预先分装。
- USER VALUE：减少每天搭配、计量和携带负担。
- SCENE："早上赶时间，拿一包塞进包里就走。"

最终正文优先使用 **USER VALUE + SCENE**，而不是只念 FACT。

---

## 六、Benefit Translation Domains（利益翻译域）

当健康功效不能使用时，优先从这些合法价值区域找销售理由：

1. **Convenience** — 方便
2. **Routine Simplicity** — 简化日常流程
3. **Decision Reduction** — 减少选择成本
4. **Portability** — 携带方便
5. **Time Saving** — 省时间
6. **Consistency Support** — 更容易维持固定使用习惯
7. **Sensory Experience** — 口味/质地/使用感
8. **Format Innovation** — 剂型/包装/组合方式
9. **Cost / Value** — 成本与价值
10. **Authorized Function** — 已授权功能
11. **Verified Product Performance** — 当前 SKU 证据支持的效果
12. **Lifestyle Fit** — 与某种真实生活方式匹配
13. **Risk Reduction** — 试用/售后/使用门槛
14. **Choice Confidence** — 帮用户减少"到底怎么选"的不确定性

不要因为不能使用生理功效，自动认为"没有卖点"。

---

## 七、Semantic Destination Test（语义目的地测试）

审核暗示时，不要只扫描敏感词。

问：

> # 普通消费者看完这句话，最自然会理解成产品带来什么结果？

如果答案是：

- "这个产品更方便"
- "这件事更容易坚持"
- "出差更省事"
- "选择更简单"

可以。

如果答案其实是：

- "这个产品能治/改善某种身体问题"

即使正文没有出现功效词，仍然失败。

**v4.11.0 起：失败不是终点，而是 CONVERSION_RECOVERY 的入口。v4.11.4 起：只有 I5-A 才算失败，I5-B/C/AMBER 默认保留。**

检测到语义终点越线后：

1. **先判定是否真的越线**——只有 Back-Translation 后主语义明确变成"产品在治疗/预防/改善生理结果"（I5-A）才算越线；I5-B（受众状态落地到摩擦）与 I5-C（主语义落合法价值域的强暗示）默认保留，不得当作越线删除；
2. **保留情绪强度和场景冲击力**——不删除整段利益表达；
3. **只替换越线的那一跳**——把"产品改善身体"那一跳换成"产品把这件事变简单"的合法价值跳；
4. 禁止直接删成参数列表（那等于放弃销售）。

示例：

- 越线（I5-A）："下午三点不垮了。"（主语义 = 产品改善疲劳）
- 恢复："下午不用再靠第三杯咖啡硬撑，是很多人的真实状态；这种按天分装，至少让每天这件事不用再想。"（主语义 = 执行更简单 / 省事，情绪强度保留）

原则：

> # Audit meaning, not vocabulary.
> # 功效暗示永不过滤——只有 I5-A 硬禁才拦截。
> # 语义终点越线 → 恢复购买理由，而不是删除购买理由。

---

## 八、Narrative Implication（叙事暗示）

真实场景可以让 Benefit 自己出现。

示例（不要）：

> "本产品便携性强。"

示例（可以）：

> "以前出差瓶瓶罐罐占半个洗漱包，这种一天一包，我直接按天数塞进行李箱。"

但前提："以前出差瓶瓶罐罐……"如果是第一人称历史，需要 IP Fact 支持。

没有 IP Fact 时可以写：

> "出差时不用带一排瓶子，按天数拿几包就行。"

**场景可以创建。人物历史不能创建。**

---

## 九、Pain Hook 更商业化

健康品类开头不要只剩"今天给大家介绍一个营养包"。

可以从真实摩擦切：

- "买营养品最容易出现一个场面：桌上七八瓶，真正每天都记得吃的没几个。"
- "你有没有发现，很多人不是不想做日常营养补充，是这件事被弄得太复杂了。"

注意：第二句中的"日常营养补充"必须符合当前产品身份和 Authorized Claim。

---

## 十、Product-to-Pain Match Gate（产品-痛点匹配门）

不能：先找到一个高转化痛点，然后硬把产品接上去。

必须：

```
Pain
↓
Product Fact
↓
Mechanism / Format
↓
Benefit
```

链条成立才允许。

示例（Match 成立）：

- Pain：每天很多瓶太麻烦。
- Fact：当前 SKU 是每日组合装。
- Match：成立。

示例（Match 失败）：

- Pain：下午疲劳。
- Fact：仅含维生素 B 族。
- 未经额外授权：不得自动"所以解决下午疲劳"。
- Match 失败，换痛点。

原则：

> # Facts choose the pain you are allowed to solve.

---

## 十一、Pain Distance（痛点距离）

按产品事实与痛点距离分级。**v4.11.0 起改为三级：DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN。**

### DIRECT PAIN（直接痛点）

产品本身直接解决：携带麻烦 / 操作复杂 / 计量麻烦 / 口感问题 / 价格问题 / 选择麻烦 / 组合搭配。

**最强表达。** 大胆写，不需要额外限定。

（原 AUTHORIZED_FUNCTIONAL_PAIN 并入此类：有正式授权功能直接支撑的痛点，按 Claim Ceiling 直接表达。）

### PARTIAL PAIN（部分痛点）

产品只解决其中**关键摩擦**，不解决全部问题。

**允许强表达（v4.11.1：不再要求"文中露出真实边界"）。** 边界体现在"不夸大"：不把部分解决写成全部解决、不把成分写成功效。边界是内部审查标准，不是文案内容——禁止在文案里主动声明边界/免责。

示例：

- Pain：每天搭配麻烦（产品解决）。
- 写法（正确）："如果你烦的是每天瓶瓶罐罐自己搭，这种按天组合确实省事。"
- 写法（错误，免责声明）："如果你烦的是每天瓶瓶罐罐自己搭，这种按天组合确实省事；至于吃不吃得均衡，那是另一件事。"（后半句抢走购买理由）

原则：强表达落在产品真实解决的那一段摩擦上；边界由内部审查执行，不在文案里声明。

### CONTEXT PAIN（上下文痛点）

只作为受众状态出现：状态差 / 疲劳 / 皮肤焦虑 / 年龄焦虑 / 熬夜 / 饮食不规律等。

**默认保留（v4.11.4）。** 非敏感品类下可作为主卖点切入，不再禁止；敏感品类下仍作为受众上下文引入。

（原 INFERRED_PHYSIOLOGICAL_PAIN 归入此类：需要额外身体效果推导的痛点，作为受众上下文；非敏感品类可作主卖点，敏感品类仍只作上下文。）

写法：作为 Audience Context 引入 → 落地到产品真实解决的摩擦 → 主语义停在合法价值域。

**COMMERCIAL_INTENSITY 联动（v4.11.4）**：DIRECT_PAIN 在任何强度下都大胆写；PARTIAL_PAIN 在 STANDARD / AGGRESSIVE 下强表达、CONSERVATIVE 下也禁止免责声明（边界体现在不夸大）；CONTEXT_PAIN 在 STANDARD / AGGRESSIVE 且非敏感品类下可作为主卖点，CONSERVATIVE 下只作受众上下文、不强化。

原则：

> # The closer the pain is to the product fact, the stronger the copy may be.
> # PARTIAL_PAIN 允许强表达——强在摩擦上，不越到产品没解决的那一段。边界由内部审查执行，不在文案里声明（v4.11.1）。

---

## 十二、Desire Translation（欲望翻译）

不要只挖痛点。很多产品更适合卖 **Desired State**。

示例：

- "我想把每天这件事变简单。"
- "我不想研究十几种单品。"
- "想找一个更适合忙碌生活的方式。"
- "我想少一点瓶瓶罐罐。"
- "我希望出差的时候也容易带。"

这些都是很强的购买欲望，不需要依赖健康焦虑。

---

## 十三、体验型轻暗示，但不能伪造结果

如果产品事实支持某种：味道 / 质地 / 使用方式 / 方便程度。

允许：

- "每天这件事突然变得没那么费劲。"
- "最打动我的反而不是配方表有多长，是它把每天这件事做简单了。"

但如果涉及身体结果，必须回到 Claim Authority。

---

## 十四、达人/素人/商家统一 Product Claim Ceiling

痛点语言可以不同：

- 商家：更偏产品逻辑。
- 达人：更偏选择逻辑和真实体验。
- 素人：更偏日常场景和生活摩擦。

允许 **Voice Difference**。禁止 **Fact Permission Difference**。

素人不能因为像消费者，就获得更多健康暗示权限。

---

## 十五、Sell 模式必须强制 Pain Translation

每篇 Sell 内部至少完成：

1. 一个真实 Pain / Desire
2. 一个 Product Fact
3. 一个 User Benefit
4. 一个 Proof
5. 一个 Decision Reason

如果正文仍然只是"含有 A、B、C、D……"：判定 **Commercial Translation FAIL**，重新写。

---

## 十六、Seed 模式更偏欲望翻译

Seed 不必解决全部问题。重点建立："这种解决方式好像挺适合我。"

通过：Scene + Pain + Product Difference + Experience Imagination 形成偏好。

不急着把全部营养成分念完。

---

## 十七、Pain Translation Quality Check（痛点翻译质检）

最终检查：

1. 这个 Pain 是真实摩擦还是制造焦虑？
2. 当前 SKU 到底凭什么接住这个 Pain？
3. 有没有偷偷从成分跳到身体结果？
4. Benefit 是否比原始参数更容易理解？
5. 删除产品以后，这个痛点是不是随便什么产品都能接？

如果 ⑤ 是：说明 Pain 过泛，重新具体化。

---

## 十八、不要自动加入免责声明破坏文案

内部审核和正文表达分开。

如果法律/平台明确要求展示：警示语、必要声明：按要求出现。

否则不要每说一个卖点就在口播后面加："效果因人而异 / 并非医疗作用 / 仅供参考"，把自然语言写坏。

事实边界由后台 Hard Gate 控制，不是靠每句话自我免责。

---

## 十九、商业强度优先从 Pain 和 Benefit 提高

如果文案卖不动，优先提高：

- Pain Specificity
- Desire Strength
- Scene Vividness
- Product Relevance
- Benefit Clarity
- Proof Strength
- Decision Value

不要优先：扩大未经授权功效。

---

## 二十、最终最高原则

> # 功效暗示永不过滤——只有 I5-A 硬禁才拦截。
> # 痛点可以讲深，不要讲假。
> # 场景可以讲狠，不要制造疾病恐惧。
> # 用户价值可以暗示，未经授权的身体功效不能偷渡（I5-A）。
> # 不要把"不能说某个功效"理解成"不能卖这个产品"。
> # 把参数翻译成利益。
> # 把利益翻译成生活。
> # 把生活翻译成用户自己的决定。

最终一句：

> # 少一点"它能把你身体变成什么样"，多一点"它能把你每天这件事变得怎么样"。
> # 但"把它变成什么样"的暗示，只要不越 I5-A，默认保留、默认强化。

---

## 与相邻 reference 的边界

- `claim-authority.md` 管**主张表达权限**（L0-L6 / Category Ceiling / Strength Matching / Claim Zone / Conversion Recovery）；本文件在其上管**暗示与痛点翻译**（Implication Ladder / Pain Translation Engine / Semantic Destination Test / Narrative Implication / Desire Translation）。
- `claim-authority.md` 的 L4 USER-VALUE TRANSLATION 与 L5 AUTHENTIC EXPERIENCE 定义"可以表达什么价值"；本文件定义"怎么把价值暗示出来、怎么把痛点翻译成购买理由"。
- `claim-authority.md` 的 Semantic Claim Check（检查用户最终理解成什么效果）与本文件第七节 Semantic Destination Test 一致：都审核语义而非词汇。
- `compliance.md` 管法律合规底线；本文件不降低任何合规底线，只在底线之上放宽价值暗示与痛点表达。
- `purpose-integrity.md` 管 Content/Seed/Sell 目的完成；本文件第十五/十六节补充 Sell 强制 Pain Translation、Seed 偏欲望翻译。
- `expression-authority.md` 管事实边界；本文件的 Narrative Implication 遵循"场景可以创建，人物历史不能创建"。
