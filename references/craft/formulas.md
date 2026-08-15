# 文案公式库与候选池路由（references/formulas.md）

> **Source of Truth：公式。** 来源：`ecommerce-copywriting-book-library` 的 86 个经典文案公式（`strategy-cards/classic-formulas.jsonl`）。
> 用法：**先判断任务，再进入候选池，再选一个主结构。** 最多一个主结构 + 一个辅助机制，禁止"公式拼盘"。
> 公式是骨架不是模板，必须用真实产品事实填充；禁止复制书中案例数字/人物/结论。

## 零、公式安全标签

- **SAFE**：默认可用。场景 / 信息差 / 对比 / 选择标准 / 真实体验 / 明确利益 / 真实证据类公式。
- **CONDITIONAL**：只有满足事实条件时才能使用。限时 / 限量 / 销量 / 复购 / 用户数据 / 权威背书 / 第一人称经历 / 实测 / 价格对比 / 原价 / 折扣 / 产地 / 认证类公式。使用前必须检查事实表。
- **AVOID / LEGACY**：默认不参与自动生成。虚假稀缺 / 无依据恐吓 / 极端焦虑 / 机械主播黑话类公式。默认路由不得召回。

## 一、候选池路由（按模式）

每种主要任务只提供 2-5 种优先结构，AI 从池中选一个主结构。

| 模式 | 优先候选（2-5 个） | 说明 |
|---|---|---|
| 抖音普通内容 | Hook→Value→Proof / 问题→反转→答案 / BAB | 信息增量 + 完播推进 |
| 抖音普通种草 | BAB / 痛点-痒点-爽点 / Hook→Experience→Value | 场景 > 参数，需求建立 > 强成交 |
| 抖音普通卖货 | PAS / AIDA / FABE / The 3 Whys | 减少犹豫，提高决策效率 |
| 抖音 IP 内容 | 观点→经历→方法论 / 冲突→判断→立场 / 故事→观点 | 让人记住"这个人是谁" |
| 抖音 IP 种草 | 经历→选择→生活方式 / 痛点-痒点-爽点 / 场景→体验→判断 | 用 IP 信用建偏好，不透支 |
| 抖音 IP 卖货 | The 3 Whys / 经历→判断标准→产品→边界 / FABE | 成交不能建立在透支 IP 信用之上 |
| 小红书普通内容 | SCQA / 场景→体验→判断 / 六感体验 | 搜索匹配 + 参考价值 |
| 小红书普通种草 | SCQA / BAB / 场景→体验→判断 / 六感体验 | 真实参考价值 > 广告感 |
| 小红书普通卖货 | FABE / 对比决策 / 选购指南 / 适合-不适合 | 像可信购买攻略，不是促销海报 |
| 小红书 IP 内容 | 经历→选择→生活方式 / 观点→审美→判断 | 让用户参考这个人的品味 |
| 小红书 IP 种草 | 经历→选择→生活方式 / 六感体验 / 场景→体验→判断 | 产品选择本身是 IP 的一部分 |
| 小红书 IP 卖货 | 判断标准→产品→边界 / FABE / 对比决策 | 成交 + 人设强化同时完成 |
| 公众号普通内容 | SCQA / 故事→观点→论证 / 金字塔 / 冲突→判断→方法论 | 深度阅读 + 认知增量 |
| 公众号普通种草 | SCQA / 认知重构→产品 / 故事→观点→论证 | 先种认知，再种产品 |
| 公众号普通卖货 | PASTOR / AIDPPC / 4P 说服 / 金字塔 | 把"为什么值得买"讲透 |
| 公众号 IP 内容 | 观点→论证→价值观 / SCQA / 故事→观点→论证 | 先认同判断，再认同选择 |
| 公众号 IP 种草 | 判断→选择→价值观 / SCQA / 故事→观点→论证 | 用长期标准筛出的方案 |
| 公众号 IP 卖货 | 判断标准→产品→边界 / PASTOR / 4P 说服 | 深度成交 + 强化价值观 |
| 视频号普通内容 | 问题→可信解释→答案 / 场景→共鸣→方案 / 故事→观点 | 有道理、靠谱、想转发 |
| 视频号普通种草 | 问题→可信解释→推荐 / 场景→共鸣→方案 | 值得推荐给身边人 |
| 视频号普通卖货 | 利益→证据→放心 / FABE / The 3 Whys | 让用户放心买 |
| 视频号 IP 内容 | 经历→判断→价值观 / 故事→观点 | 让人信任这个人 |
| 视频号 IP 种草 | 经历→选择→边界 / 问题→可信解释→推荐 | IP 信任 → 产品信任 |
| 视频号 IP 卖货 | The 3 Whys / HEART / FABE / 经历→判断标准→产品→边界 | 信任先于成交，长期价值高于一次 GMV |
| 详情页/落地页 | FABE / ABCD / 4P 说服 / 5 大异议 / 落地页公式 5 式 | 减少摩擦提升清晰 |
| 信息流广告 | 广告公式 5 式 / SLAP / AIDA / BAB | 把说服压缩进数秒 |
| 直播话术 | AIDA / 痛点-痒点-爽点 / 价格锚点 / 憋单 / 5 大异议 | 留人→互动→成交→追单→转款 |
| 私域朋友圈 | 卖货五要素 / 3+2 黄金公式 / 五大内容模型 | 价值分层交替 |
| 私聊转化 | SPIN / 5 大异议 / The 3 Whys | 引导自我觉醒而非强推 |

## 二、转化结构公式（核心 39 个）

### 经典四步
- **AIDA**：Attention 强钩子 → Interest 相关利益/痛点 → Desire 使用后蜕变 → Action 单一明确 CTA。适用：冷受众、落地页、产品发布。
- **AIDCA**：AIDA + Conviction（证据打消疑虑）。适用：高客单、需建信任的销售页。
- **AIDAS**：AIDA + Satisfaction（售后/复购）。适用：会员制、订阅、重 LTV 品牌。
- **AIDPPC**：Attention → Interest → Description → Persuasion → Proof → Close。适用：高客单销售信、复杂 offer 长落地页。
- **IDA**：省去注意阶段。适用：再营销、热受众。

### 问题驱动
- **PAS**：Problem 用户原话点出痛点 → Agitate 放大后果 → Solution 产品是自然答案。适用：痛点明确的广告、再营销。
- **PASTOR**：Problem → Amplify → Story → Transformation → Offer → Response。适用：长销售页、webinar 脚本。
- **PAPA**：Problem → Agitate → Promise → Action。适用：社交广告、快速促销。
- **SPIN**：Situation → Problem → Implication → Need-Payoff。适用：顾问式销售、高客单 B2B。

### 蜕变桥接
- **BAB**：Before 现状 → After 理想 → Bridge 产品是路径。适用：案例、见证、产品页。
- **PPPP**：Picture → Promise → Prove → Push。适用：品牌故事、感性品类。
- **PPP**：Picture → Promise → Proof。适用：信任敏感、线索获取广告。
- **4Ps 说服**：Promise → Picture → Proof → Push。适用：销售页、提案。

### 叙事框架
- **Hook-Story-Offer**：钩子 → 故事 → offer。适用：短视频、直播、funnel 落地。
- **Star-Chain-Hook**：吸睛开头 → 逻辑串联卖点 → 收尾行动号召。
- **Star-Story-Solution**：人物 → 挣扎与蜕变 → 产品是催化剂。适用：见证营销、创始人内容。
- **StoryBrand（SB7）**：角色-问题-向导-计划-行动-成功-失败。适用：品牌故事、关于页。
- **Soap Opera Sequence**：多封邮件连续剧，悬念-连接-转化。适用：邮件序列、私域培育。

### 认知旅程
- **ACCA**：Awareness → Comprehension → Conviction → Action。适用：教育型内容、复杂产品。
- **ACC**：Awareness → Comprehension → Conversion。适用：教育广告、认知活动。
- **QUEST**：Qualify → Understand → Educate → Stimulate → Transition。适用：高客单、定向投放、B2B 线索。
- **CURVE**：Commit → Unexpected → Reframe → Visualize → Emotional。适用：品牌宣言、观点型内容。
- **EPIC**：Engage → Promise → Inform → Close。适用：落地页、促销广告。
- **CAB**：Context → Action → Benefit。适用：短广告、卖点高亮。
- **SOFA**：Solution → Outcome → Feature → Action。适用：热受众、产品导向促销。
- **PROVE**：Promise → Reason → Outcome → Verification → Engagement。适用：质疑型受众。
- **ABCD**：Attention → Benefit → Credibility → Direction。适用：付费广告、banner。
- **FAST**：Focus → Advantage → Specifics → Trigger。适用：移动广告。
- **G.R.A.B.**：Grab → Relate → Amplify → Benefit。适用：广告、邮件开头。
- **ODC**：Offer → Deadline → CTA。适用：限时闪购、促销。
- **SLAP**：Stop → Look → Act → Purchase。适用：短视频广告、社交帖子。
- **AICPBSAWN**：多心理触发器按序叠加。适用：销售页、限时 offer。
- **5 大异议对策**：Time / Money / Works / Trust / Need 逐一化解。适用：销售页、落地页。
- **The 3 Whys**：Why you（差异化）→ Why now（此刻）→ Why trust（证据）。适用：高客单决策页。

### 公式组（5 式系列）
- **落地页公式 5 式**：①Hero 问题→承诺→CTA ②好处→证据→CTA ③特性→利益→社会证明→CTA ④痛点→放大→方案→CTA ⑤BAB→CTA。
- **销售页公式 5 式**：①大承诺→故事→证明→offer→CTA ②问题→放大→故事→方案→offer→CTA ③欲望→阻碍→方案→证明→CTA ④蜕变→机制→offer→CTA ⑤故事→挣扎→突破→offer→CTA。
- **广告公式 5 式**：①问题→方案→CTA ②钩子→利益→CTA ③提问→利益→CTA ④痛点→缓解→CTA ⑤欲望→捷径→CTA。
- **邮件公式 5 式**：①问题→故事→方案 ②钩子→价值→CTA ③提问→洞察→CTA ④犯错→教训→CTA ⑤故事→转折→offer。
- **CTA 公式 5 式**：①动词+利益 ②获取+结果 ③开始+时间 ④下载+资源 ⑤领取+offer。

## 三、卖点提炼公式（4 个）

- **FAB**：Features 特性 → Advantages 优势 → Benefits 利益。把冷参数翻译成用户收益。
- **FABE**：FAB + Evidence 证据。用证据堵住"凭什么信你"。
- **USP**：提炼唯一/最强差异化：解决力道 + 感受词 + 记忆点。
- **痛点-痒点-爽点**：痛点（必须解决）→ 痒点（想要未说的期待）→ 爽点（超预期惊喜）。

## 四、逻辑与故事结构（5 个）

- **SCQA**：Situation 情境 → Complication 冲突 → Question 聚焦疑问 → Answer 方案。适用：干货文、深度文、方案展示。
- **SCQOR**：SCQ + Obstacle 克服阻力 + Resolution 收尾。适用：创始人故事、品牌故事、案例。
- **金字塔原理**：结论先行，上层论点-下层论据逐层支撑。适用：报告、方案、逻辑型长文。
- **黄金三段式**：开头炸场 → 中段故事金句 → 结尾升华互动。适用：公众号、小红书长文、短视频脚本。
- **冲突-反转-升华**：冲突 → 反转 → 升华。适用：情感文、故事文、短视频。

## 五、标题技法（5 个）

- **标题万能公式**：数字+结果 / 痛点+方案 / 反差+悬念 / 人群+共鸣。
- **爆款文章公式**：强情绪 + 真细节 + 短节奏 + 好标题 + 强结构 + 高互动。
- **中文标题三引擎**：情绪钩子 + 利益承诺 + 悬念缺口。
- **4U 标题法**：Urgent 急迫 + Unique 独特 + UltraSpecific 超具体 + Useful 有用（至少含 3 个 U）。
- **标题公式 10 式**：数字+承诺 / 如何+利益 / X 的秘密 / 最快方法 / X 个要避开的坑 / 人人都该知道 X / 关于 X 的真相 / 你也在犯这些错吗 / X 种方法达成 Y / 终极指南。

## 六、需求、感官与消费者行为（4 个）

- **文案 GPS**：受众 / 需知 / 结果 / 感受 / 触点 5 问定位。
- **六感写法**：眼耳鼻舌身心六种感官细节描绘理想场景。
- **AISAS**：Attention → Interest → Search → Action → Share。适用：种草-搜索-转化链路。
- **5A**：Aware → Appeal → Ask → Act → Advocate。适用：私域、会员、品牌资产运营。

## 七、营销理论与战略模型（7 个）

- **4I 理论**：Interesting 趣味 + Interests 利益 + Interaction 互动 + Individuality 个性。
- **4P 营销**：Product / Price / Place / Promotion。
- **4C 营销**：Customer / Cost / Convenience / Communication。
- **定位**：在用户心智中占据差异化位置。
- **黄金圈**：Why → How → What。先信念再能力。
- **SWOT**：优势-劣势-机会-威胁。
- **5W1H**：What-Why-Who-When-Where-How 六问拆解。

## 八、分析模型（4 个）

- **用户画像**：人口 / 心理 / 需求 / 触媒 / 痛点。
- **消费者旅程**：从认知到忠诚的全触点路径。
- **漏斗模型**：认知→兴趣→考虑→转化→留存 逐层收窄。
- **二八法则**：80% 结果来自 20% 原因/客户/内容。
- **海盗法则 AARRR**：获客-激活-留存-营收-自传播。

## 九、信息质量与信任（4 个）

- **4Cs**：Clear 清晰 + Concise 简洁 + Compelling 有说服力 + Credible 可信。
- **CLEAR**：Concise + Logical + Engaging + Action + Relevant。
- **SUCCES**：Simple + Unexpected + Concrete + Credible + Emotional + Story。让内容过目不忘。
- **STAR**：Situation → Task → Action → Result。展过程而非空口成就。

## 十、服务与受众（3 个）

- **HEART**：Hook → Empathy → Authority → Resolution → Trust。说服前先情感连接。
- **OATH**：Oblivious 不知问题 → Apathetic 知道不在乎 → Thinking 正在找方案 → Hurting 剧痛。按受众认知阶段选公式与语气。
- **AWARE**：Attention → Awareness → Resonance → Engagement。情绪对齐而非直接卖。
- **CAKE**：Curiosity → Attention → Knowledge → Engagement。先好奇再给知识。

## 组合打法（起点，最终以实际路由为准）

- 抖音种草：Hook-Story-Offer + 痛点-痒点-爽点 + 稀缺效应
- 小红书干货：SCQA + 黄金三段式 + 六感写法 + 中文标题三引擎
- 电商详情页：FABE/ABCD + 4P 说服 + 社会证明 + 损失厌恶
- 私域长文：PASTOR/AIDPPC + 文案 GPS + 从众 + The 3 Whys
- 直播带货：AIDA + 痛点-痒点-爽点 + 价格锚点 + 憋单 + 5 大异议
- 品牌故事：StoryBrand + 黄金圈 + SCQOR
- 再营销/热受众：IDA + SOFA + CAB + CTA
- 高客单信任：AIDPPC + SPIN + PROVE + OATH 分层

## 使用红线

- 一个主结构 + 一个辅助机制，禁止把多个大公式机械拼接成"公式拼盘"。
- 公式是骨架，必须用产品事实填充；禁止复制书中案例数字/人物/结论。
- 公式永远不能凌驾于事实、用户利益、IP 信用、平台逻辑之上（见 `references/execution/execution-reliability.md` 规则优先级）。
- **A/B 例外**：A/B 单变量测试只改变被测试变量，其他关键变量保持一致；批量差异化规则让位于 A/B 单变量原则。
