# Changelog

## [4.24.0] - 2026-08-20

### Added
- Minimal route compiler, persistent fingerprints, privacy-safe telemetry, evidence-based voice profiles, severity levels, and real-model behavioral fixtures/runner.

### Changed
- Slim progressive-disclosure entrypoint; synchronized Draft/H1/G1-G12/H2/invariant flow and corrected stale pain-distance schema rules.

All notable changes to the Master Copywriting skill.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.23.2] - 2026-08-20

### Changed
- **四平台常识开放**：可靠常识准入从单一案例扩展到抖音、小红书、公众号、视频号，并按动作现场、选择参考、推理论证、可信转述分别适配。
- **Anti-Overblocking**：审核不得仅因内容未进入 Product Ledger 就删除、弱化或免责声明化；只拦截从常识跳到当前 SKU 专属结论的无证据跃迁。

### Tests
- 回归检查新增四平台常识矩阵、真实常识默认保留与 SKU 跃迁边界断言。

## [4.23.1] - 2026-08-20

### Changed
- **可靠常识准入**：稳定、广泛成立、非时效性且无合理争议的常识，可直接用于解释、场景与类比，不再要求全部来自 Product Ledger。
- **SKU 推断边界**：常识不得自动升级为当前商品的配料、检测值、工艺归属、认证、价格、库存、功效或实测结果；这些仍需产品证据或用户确认。

### Tests
- 回归检查新增 Common Knowledge Admission Gate 与 SKU 事实边界断言。

## [4.23.0] - 2026-08-20

### Added
- **双遍去 AI 闭环**：所有可发布成稿固定执行“初稿 → H1 去 AI → G1-G12 全面复审修错 → H2 再去 AI → Final Invariant Check”。
- **机器可读状态**：`route-instance.schema.json` 新增 `humanization_passes=2` 与 `final_invariant_check=PENDING/PASS/FAIL`。
- **有界返修**：终检失败回到全面复审，最多返修 2 轮；仍失败则停止交付并报告阻塞，不无限重写。

### Tests
- 回归检查新增双遍次数、阶段顺序、终检状态与最大返修轮次断言。

## [4.22.1] - 2026-08-20

### Changed
- **四平台同步优化**：抖音、小红书、公众号、视频号全部接入风险分级 Humanization，不再只对短视频或直播引流生效。
- **平台独立复审**：分别校验口播现场感、选择依据与可复查性、真实推理、可信可转述性；跨平台稿从选角度开始独立生成和去 AI，不允许母稿机械换皮。

### Tests
- 回归检查新增四平台矩阵完整性与跨平台独立 Humanization 断言。

## [4.22.0] - 2026-08-20

### Changed
- **Humanization 默认路由**：草稿/内部推演才使用 `INTERNAL_ONLY`；一般可发布交付默认 `DETECT_AND_REPAIR`；千川、付费广告、直播引流、批量商业文案和明确去 AI 味的任务强制进入 `DOUBLE_AUDIT`。
- **DOUBLE_AUDIT 执行链**：明确为双检测 → `stop-slop` → `humanizer` → Meaning Lock/G1-G12 复审，避免“已安装但未实际调用”。
- **route-instance.schema.json**：默认值由 `INTERNAL_ONLY` 改为 `DETECT_AND_REPAIR`。

### Tests
- 回归检查新增一般交付默认路线和付费商业成稿强制路线断言。

## [4.21.0] - 2026-08-20

### Added
- **external-humanization-orchestration.md**：正式接入 `chatgpt-comparison-detection`、`ai-slop-detector`、`stop-slop`、`humanizer`、`writing-style`、`personal-chinese-writing-style`、`agent-style` 与 `huashu-nuwa`，定义触发条件、职责边界、七种路由模式、Meaning Lock、诊断结构、最小修复、复审、冲突优先级和缺失降级。
- **route-instance.schema.json**：新增 `humanization_pipeline` 与 `voice_source_status`，把去 AI 技能组合从口头约定变成可验证路由字段。

### Changed
- **SKILL.md / reference-index.md / human-voice-pass.md**：版本升至 v4.21.0；G8 在外部技能命中时执行组合协议，所有候选稿必须重新通过 G1-G12。

### Boundaries
- 检测器只识别写作信号，不能证明作者身份；单个词或单个标点不得触发重写。
- 中文个人文风包、英文技术文风包和人物蒸馏包均按载体条件调用，不作为普通中文营销稿的默认末端滤镜。

## [4.20.0] - 2026-08-20

### Added
- **references/quality/human-voice-pass.md**：根据《你的文案一眼像 AI？问题根本不在逻辑和内容》提炼并内化的 Human Voice Pass。新增四维 AI 痕迹诊断（空泛开场、元话语套头、机械对称、无信息升华）、最小修复流程、历史样稿文风证据对齐、陌生产品替换测试与朗读检查。

### Changed
- **SKILL.md / reference-index.md**：版本升至 v4.20.0；Final QA 在需要时加载 Human Voice Pass。

### Boundaries
- 文章中推荐的外部 humanizer / detector / stop-slop 等工具不作为运行时硬依赖；技能只内化其可验证的方法。
- 去 AI 味不等于故意错别字、口头禅、虚构经历或放松事实、合规、Claim Ceiling、平台目标和 CTA 规则。

## [4.19.0] - 2026-08-17

### Added
- **references/craft/cta.md 二·五 新增「判断留白机械句」反模式族（核心新增）**：把"值不值得，自己判断 / 自己心里有数 / 你自己定 / 你自己掂量 / 自己最清楚 / 值不值 / 合不合适"定义为禁止的万能收口——它看似高级隐式，实则换任何产品、任何正文都能用。新增**互换性测试（Interchangeability Test）**：把收口句里的产品/场景/标准词全部替换成另一个产品，若句子依然成立 → 机械句，重写。收口必须证明"只属于这一篇"，回扣本版正文的具体卖点、具体标准、具体场景。
- **references/quality/anti-patternization.md**：句末强化句识别信号新增"自己判断 / 自己掂量 / 值不值得"；Rule Visibility Test 的 CTA 模板行新增判断留白机械句；Set-Level QA 16.6 Ending Check 新增第 4 项（3 篇以上以判断留白机械句结束 → 打散收尾方式）

### Changed
- **references/craft/cta.md**：修正被误标为"合格高级隐式"的机械示例（"这一场讲透怎么挑，值不值得听，你自己定" → "听完这一场，挑茶那点门道就齐了"）；家族句式变体库 8 处机械变体改为携带具体标准/场景/物件的自然变体（如"合不合适，自己判断" → "是真是假，泡一杯就有答案"）；分口径原则表、种草/卖货示例、平台层示例同步去机械化
- **zhangping-shuixian-sell-point/assets/scripts.json**：重写 5 条机械收口模板（s10 门道留一半 / s11 自己心里有数 / s13 自己对照 / s14 坚持再看 / s15 回到开头），改为承接具体卖点的槽位结构，并在 compliance 中明确禁止判断留白机械句
- **SKILL.md / reference-index.md**：版本升至 v4.19.0

### Root Cause（本轮迭代根因）
- 机械 CTA 的源头不是生成环节，而是**参考文件里的"合格示例"本身是机械句**——cta.md 高级 vs 低质对照表、家族句式变体库、scripts.json 三处锚点同时把"自己判断/你自己定"当作正面示例，模型照抄导致同批次 5 版收口雷同
- 上一轮修复使用的"谁喝谁知道"同样属于已标记的句末强化句，属于"换一种机械"——真正的修复是**收口携带本版具体内容**，而不是换一个万能句

---
## [4.18.0] - 2026-08-17

### Added
- **references/craft/qianchuan-manual.md（核心新增）**：千川素材创作爆量手册拆解（全 15 万字实战体系）。来源：第三方数据中心《千川素材创作爆量手册》拆解（2026-08 抓取）。内容：
  - **要素组合体系**：创作手法 3 × 素材类型 7 × 脚本创意 11 × 开头三秒 9 × 中间卖点 12 × 尾部结尾 5 的选型矩阵
  - **七大素材类型**：情景种草 / 素人口播 / 产品展款 / 达人测评 / 明星测评 / 剧情演绎 / 卖家促销（作品特征 × 核心目标 × 团队适配）
  - **十一大脚本创意**：身份推荐 / 人群圈定 / 痛点放大 / 效果开头 / 价格利益 / 过程测评 / 悬念揭秘 / 剧情引出 / 权威讲解 / 知识科普 / 行业揭秘
  - **开头三秒 9 大结构句式**：价格利益 / 身份推荐 / 点名人群 / 直陈痛点 / 直陈效果 / 提出疑问 / 引发好奇 / 正话反说 / 塑造情绪
  - **中间卖点 12 大句式 + 卖点排序方法论**：用户视角优先 / 竞品对比 / 重复度重构 / 痛点爽点 / 视觉化前置
  - **结尾引导 5 大句式**：优惠诱导 / 饥饿营销 / 艾特人群 / 从众引导 / 身份推荐
  - **完爆前三秒 7 大方法** + **素材视觉化 10 大技巧** + **爆量模板生命周期管理** + **数据分析框架**
  - **方法论精华**：100 条提炼（第三方数据中心观点）
- **SKILL.md / reference-index.md**：版本升至 v4.18.0；千川素材深度方法论注册到 Progressive Disclosure 与 Reference Loading Map

### Changed
- **references/reference-index.md**：craft/ 目录注册 qianchuan-manual.md；Reference Loading Map 新增「千川素材深度方法论」行
- **SKILL.md**：版本号升至 4.18.0；G7 Platform Native 与 Progressive Disclosure 新增 qianchuan-manual.md 引用

### Compliance Hard Bottom Lines（合规硬底线）
- 手册中「逼近极限 / 无中生有 / 虚假宣传是对用户的善意谎言」等观点与技能硬底线冲突，**一律不得采纳为生成规则**，仅保留结构价值
- 所有 CONDITIONAL 标签（价格/福利/限量/销量/背书/第一人称经历/实测/对比/稀缺）使用前必须检查事实表
- AVOID 类（极限用语/虚假稀缺/无依据恐吓/编造背书/编造卖点）默认路由不得召回
- 效果/背书/稀缺表达受 Claim Ceiling 约束；I5-A 硬禁、CTA 分口径、看播收口无时间限定词等规则不变

---
## [4.17.0] - 2026-08-17

### Added
- **references/craft/eight-hundred-hooks.md（核心新增）**：800个短视频爆款开头钩子模板库。来源：第三方数据中心 PDF《800个短视频爆款开头钩子》拆解（2026-08 抓取）。内容：10 大类 × 800 条分类句式（痛点共鸣 76 / 内幕揭秘·反常识 88 / 利益诱惑·捷径 190 / 稀缺紧迫 46 / 夸张安利·承诺 111 / 警示避雷 66 / 人群定向 61 / 对比·挑战·测评 45 / 实战经历 55 / 提问互动 62），每条带安全标签（SAFE / CONDITIONAL / AVOID）与使用规则
- **references/craft/hooks.md 第十四节「第三方模板化钩子库」**：新增 10 大类 × 800 句式的最小可执行版索引表（大类 × 数量 × 核心机制 × 安全标签），引用 eight-hundred-hooks.md 为 Source of Truth

### Changed
- **references/reference-index.md**：版本号升至 v4.17.0；craft/ 目录注册 eight-hundred-hooks.md；Reference Loading Map 的 Hook writing 行加入该文件
- **SKILL.md**：版本号升至 4.17.0；G7 Platform Native 新增短视频/直播引流素材开头钩子按大类快速检索参考 eight-hundred-hooks.md；Progressive Disclosure 加载表新增「短视频/直播引流素材开头钩子」行

### Hard Bottom Lines Preserved（硬底线保留）
- 800 钩子库是**模板句式库**，不是实证原句库；禁止复制原句或仅换词，只迁移结构 + 产品事实现场生成
- 安全标签与 hooks.md 体系完全兼容：SAFE 默认可用；CONDITIONAL（价格/福利/限量/数据/第一人称经历/实测/对比）使用前必须检查事实表；AVOID（手慢无/炸单/天花板/封神/第一/唯一/90% 的人/99% 的人/无依据恐吓/极端焦虑/虚假稀缺）默认路由不得召回
- 与 gold3s-database.md（1499 条实证套路）互补：需要"按大类快速出钩子"查本库，需要"基于真实投放数据的套路优先级"查 gold3s；两库均不改变 Claim Ceiling
- 钩子承诺必须在正文兑现；效果表达不得新增未授权功效（I5-A 硬禁仍生效）
- 所有内容生成规则（Hard Gates、Humanization、平台原生、真人感）不变

---
## [4.16.0] - 2026-08-17

### Added
- **references/craft/qianchuan-material-sop.md（核心新增）**：千川爆款素材 SOP。来源：第三方数据平台「内容中心」栏目《千川爆款复刻操作手册》《电商AI素材锦囊妙计》等官方运营指南拆解（2026-08 抓取）。内容：①素材生产四维定位（品牌策略→产品定位→内容策略→素材策略，四步流程）；②素材三段式组合库（21 式爆款开头 × 6 大种草方式 × 6 大结尾引导句式，各配机制与安全标签）；③爆款基因复刻（高光 3 秒榜 / 话术榜 / 脚本榜，拆解基因→迁移机制→结合货盘重组）；④AI 素材能力矩阵（AI 绘图 / AI 视频 / AI 文案 / AI 智能编辑，三步走路径：选模板→AI生成→投放优化）
- **references/modes/viral-content-map.md 新增三节（v1.1）**：①第六节「八大人群内容定向」——EATM 四维模型（环境场景/人设形象/文案方向/内容主题）+ 八大人群画像与内容方向（小镇新贵/小镇中老年/GenZ/精致妈妈/新锐白领/资深中产/都市银发/都市蓝领）+ 人群定向写作规则；②第七节「对标拆解方法论」——四个无效拆解误区 + 竞品对标五维（基础数据/流量结构/爆款内容/选品策略/用户画像）+ 品牌对标五维（品牌整体数据/品牌自播/品牌达播/商品策略/用户资产沉淀）；③第八节「反季清仓策略」——反季清仓四步法（货品优化/心智种草/直播承接/测款补量）+ 写作规则

### Changed
- **references/reference-index.md**：版本号升至 v4.16.0；craft/ 目录注册 qianchuan-material-sop.md；Reference Loading Map 新增「千川/付费素材」与「人群定向/对标拆解/反季清仓」两行
- **SKILL.md**：版本号升至 4.16.0；G7 Platform Native 新增千川素材与人群定向/对标拆解/反季清仓引用；Progressive Disclosure 加载表新增两行

### Hard Bottom Lines Preserved（硬底线保留）
- 千川素材 SOP 是机制与结构的实证来源，不是例句库；禁止复制原句或仅换词，只迁移「结构×机制×组合逻辑」
- 素材三段式组合中，开头 3 秒选型以 gold3s-database.md 套路频次实证为准；福利优惠/限时限量/价格折扣类属 CONDITIONAL，使用前必须检查事实表；"手慢无/炸单/虚假稀缺"属 AVOID 不召回
- 结尾收口口径按用户明确目标选定一个（看播/预约/成交/留资/加热），禁止模板默认类别覆盖用户目标；看播口径收口不写时间限定词
- 人群定向不改变 Claim Ceiling：面向银发/妈妈人群时功效表达仍受约束（I5-A 硬禁仍生效）；对标学到的表达结构同样受 Claim Ceiling 约束
- 反季清仓的价格/折扣/限量/活动期限表达仍属 CONDITIONAL，须查事实表
- AI 素材产出必须过 AI_STYLE_SCORE 人味化检测与平台合规校验；AI 生成内容不得新增未授权功效
- 所有内容生成规则（Hard Gates、Humanization、平台原生、真人感）不变

---
## [4.15.0] - 2026-08-17

### Added
- **references/craft/gold3s-database.md（核心新增）**：某数据平台「黄金3秒台词」实证库。数据来源：第三方数据平台黄金3秒台词榜单，30 页 × 50 条 = 1499 条付费广告真实投放台词，含关联素材数/创意数/直播数/总点赞数。内容：23 种套路频次总览（点名产品 44% 居首）、TOP 套路句式结构（机制×结构×示例）、高频套路组合（组合占 71%，含组合黄金公式）、高赞台词拆解（点赞 TOP 20 机制归纳）、生成规则（选套路顺序 + 硬规则 + 与现有规则关系）
- **references/craft/hooks.md 第六节「抖音黄金三秒」升级为数据驱动版**：从 4 条通用机制扩展为 10 条实证套路 + 组合黄金公式 + 硬规则，引用 gold3s-database.md 为 Source of Truth

### Changed
- **references/reference-index.md**：版本号升至 v4.15.0；craft/ 目录注册 gold3s-database.md；Reference Loading Map 的 Hook writing 行加入该文件
- **SKILL.md**：版本号升至 4.15.0；G7 Platform Native 新增抖音/直播开头 3 秒钩子优先参考 gold3s-database.md；Progressive Disclosure 加载表新增「抖音/直播开头 3 秒钩子」行

### Hard Bottom Lines Preserved（硬底线保留）
- 黄金3秒台词库是机制与结构的实证来源，不是例句库；禁止复制原句或仅换词，只迁移机制/句式结构/表达逻辑
- 福利优惠类（价格/折扣/赠品/限量/倒计时）属 CONDITIONAL，使用前必须检查事实表；"手慢无/炸单/虚假稀缺"属 AVOID 不召回
- 钩子承诺必须在正文兑现；效果表达不得新增未授权功效（I5-A 硬禁仍生效）
- 套路频次是"选什么"的参考，不是"必须这么写"的模板；同一批次不得全部套同一组合（anti-patternization 仍生效）
- 所有内容生成规则（Hard Gates、Humanization、平台原生、真人感）不变

---
## [4.14.0] - 2026-08-15

### Added
- **references/templates/ 模块（核心新增）**：新增输出模板与 MD 文件生成契约。references/templates/output-templates.md 定义输出模板结构（单版/多版表格/多平台三种模板）、MD 文件生成规则（文件名 {平台}-{产品}-{行动}-{YYMMDDHHMM}.md）、模板填充规则与执行步骤。创作完内容后强制套用模板并生成 .md 文件交付。
- **SKILL.md §10.5 强制模板套用 + MD 文件生成（v4.14.0 新增）**：创作完内容之后强制套用模板并生成 .md 文件。执行时机：G10 输出净化之后 → 套模板 → 落盘。例外：用户明确指定其他格式时遵从用户格式。引用 references/templates/output-templates.md 为 Source of Truth。
- **final-output.md §26.5 强制模板套用 + MD 文件生成**：与 SKILL.md §10.5 同步，补充说明"模板是交付外壳，不是内容替代品"——内容层禁止模板化（anti-patternization.md），交付层强制模板化，两者不冲突。

### Changed
- **references/reference-index.md**：版本号升至 v4.14.0；目录结构注册 templates/ 模块；Reference Loading Map 新增"创作完内容后强制套用模板 + 生成 MD 文件"行，加载 templates/output-templates.md
- **SKILL.md**：版本号升至 4.14.0；§10 头部新增 Canonical output template 引用行

### Hard Bottom Lines Preserved（硬底线保留）
- 模板是交付外壳，不是内容替代品（内容层禁止模板化由 anti-patternization.md 管，交付层强制模板化由 output-templates.md 管，两者不冲突）
- 内部元数据输出规则不变（v4.11.3 例外仍生效）
- 收口家族任何场景不输出（v4.11.3 硬规则）
- 用户明确指定格式时遵从用户格式（File Override 不变）
- 所有内容生成规则（Hard Gates、Humanization、平台原生、真人感）不变

---

## [4.13.0] - 2026-08-15

### Added
- **references/modes/viral-content-map.md（核心新增）**：基于《四大平台爆款内容图谱（2026 信源版）》调研转译的爆款内容图谱。三条跨平台爆款规律（情绪先行信息后置 / 活人感取代精致人设 / 电商爆款=信任×场景而非流量×低价）+ 平台爆款内容类型图谱 + 分发机制适配 + 平台电商打法图谱 + 按目标选平台决策地图。信源窗口 2026-01-01 至 2026-08-15（平台官方年度报告 / 官方战报 / 腾讯财报 / 新榜 / 飞瓜 / 千瓜 / 果集·友望 / QuestMobile 交叉验证）

### Changed
- **references/modes/platforms.md**：平台总览表新增"2026 爆款实证要点"列（抖音：算法赛马+热点广场、完播/互动/转发权重、活人感官方风向标；小红书：70% 月活搜索、笔记长尾、攻略测评长尾之王；视频号：转发权重>点赞、生活类点赞 TOP 43%、300 元+ 占 GMV 一半；公众号：订阅+算法双轨、标题与开头段权重放大、千粉小号出圈机会）；文件头新增对 viral-content-map.md 的引用说明
- **references/cross-platform/cross-platform-reconception.md**：新增"〇、跨平台爆款规律输入（2026）"章节，三条跨平台规律（情绪先行 / 活人感 / 信任×场景）作为每个平台重新立题前的底层输入，分别落到四平台的具体命题检查；文件版本升至 v1.1
- **SKILL.md**：G7 Platform Native 新增 2026 爆款实证引用（情绪先行、活人感、信任×场景三条跨平台规律；平台内容类型/分发机制/电商打法按图谱适配，但不得成为固定五件套）；Progressive Disclosure 加载表 Platform-specific 与 Multi-platform 行加入 viral-content-map.md；版本号升至 4.13.0
- **references/reference-index.md**：目录结构注册 viral-content-map.md；Reference Loading Map 平台行加入该文件；索引版本升至 v4.13.0

### Hard Bottom Lines Preserved（硬底线保留）
- 平台内容类型图谱不得成为固定选题五件套（Example Anti-Anchoring 仍生效）；图谱用于拓宽角度搜索空间，不是"每次必须选一篇"的固定栏目
- 规律三（信任×场景）不改变 Claim Ceiling；信任与场景是表达层，不是主张层
- 平台功能（粉丝门槛、广告产品、挂载规范）时效性强，投放前必须官方复核
- 硬底线（未授权疾病/治疗/预防、虚假证据、硬功效偷渡、显式 CTA 全口径隐式）不变

---

## [4.12.0] - 2026-08-15

### Changed
- **PATCH 01 — 全口径默认高级隐式收口（核心）**：CTA 分口径原则从"看播/预约/成交/留资口径允许显式动作"改为"所有口径默认 NATURAL_STOP 或 IMPLICIT_CLOSE"。显式动作（进直播间 / 点预约 / 点购物车 / 下单 / 去拍 / 去看看 / 点我头像 / 点下方）不属于任何口径的默认选项，只有命中 Closed Explicit CTA Allowlist 才允许
- **PATCH 02 — 新增"高级隐式收口"定义与六项质检**：零动作指令 / 零目的地 / 零时间限定 / 零直播间行为预告 / 承接本版核心观点 / 同批次句式指纹不重复；附"低质隐式 vs 高级隐式"对照表，禁止万能句（"值不值自己判断"式）
- **PATCH 03 — 看播/预约口径示例全部隐式化**：分口径表格的预约示例从"下方预约点一下，开播我提醒你"改为"这一场讲透怎么挑，值不值得听，你自己定"；成交/留资口径明确"动作由商品组件/表单组件承接"
- **PATCH 04 — 48 CTA 模板速查门禁强化**：广告类模板（D7/D8/D9、X5/X6/X7、S5/S6、G4/G5/G6）与成交/留资/私域类模板明确"默认禁止召回，仅 EXPLICIT_ALLOWED 时可召回且须转译自然口语"；种草类模板中"引导动作"同样默认转译隐式

### Added
- references/craft/cta.md：第二节改为"全口径默认高级隐式收口"；新增第二节·五"高级隐式收口定义与质检"；第九节模板门禁强化；文件版本升至 v4.7.0
- references/craft/examples.md：第三节 CTA 结构演示改为全口径隐式，看播/预约示例隐式化，新增两条显式禁止示例
- SKILL.md 更新 10.4 CTA 最小硬规则（全口径隐式 + 六项质检）；版本号升至 4.12.0

### Hard Bottom Lines Preserved（硬底线保留）
- Closed Explicit CTA Allowlist 不变：用户明确要求 / 按钮 / 落地页 / 表单场景仍可显式
- 看播稿免时间限定、不描述直播间行为两条硬约束不变
- 硬底线（未授权疾病/治疗/预防、虚假证据、硬功效偷渡）不变

---

## [4.11.4] - 2026-08-15

### Changed
- **PATCH 01 — 功效暗示永不过滤（核心）**：合法边界内的功效暗示（I5-B / I5-C / AMBER）默认保留、默认强化，只有 I5-A 硬禁（疾病/治疗/预防/明确生理结果）才被拦截。I5-B 从"谨慎开放"改为"默认保留"；I5-C 从"仅 AGGRESSIVE 开放"改为"STANDARD 起默认开放（非敏感品类）"；AMBER 灰色区在非敏感品类默认开放、可强化
- **PATCH 02 — CONTEXT_PAIN 可作为主卖点**：CONTEXT_PAIN（状态差/疲劳/皮肤焦虑/年龄焦虑/熬夜/饮食不规律）从"不能当主卖点"改为"默认保留，非敏感品类可作为主卖点切入，敏感品类仍只作受众上下文"
- **PATCH 03 — Semantic Destination Test 收窄失败范围**：只有 Back-Translation 后主语义明确变成"产品在治疗/预防/改善生理结果"（I5-A）才算 FAIL；I5-B/C/AMBER 默认保留，不得当作越线删除；拦截后走 CONVERSION_RECOVERY（保留情绪强度与场景冲击力，只替换越线那一跳）
- **PATCH 04 — Hidden Efficacy Implication 禁止范围收窄为仅 I5-A**：claim-authority.md 第九节"禁止 Hidden Efficacy Implication"明确标注仅 I5-A 硬禁（"以前下午三点就撑不住，现在你懂的 / 女生那几天我都会多来一包 / 熬夜党第二天状态差别很明显 / 脸色这个东西，补没补自己最清楚"），I5-B/C/AMBER 默认保留
- **PATCH 05 — PARTIAL_PAIN 露出边界残留修复**：commercial-expression-freedom.md 第二十九/三十章与 anxiety-pain-scenification.md 第四十章残留的"PARTIAL_PAIN 必须露出边界 / 允许强表达但露出边界"统一改为"边界体现在不夸大"（v4.11.1 口径）

### Added
- references/execution/implicit-benefit-pain.md：I5-B/C 默认保留、默认强化；CONTEXT_PAIN 非敏感品类可作主卖点；Semantic Destination Test 仅 I5-A 算失败；第二十节最高原则加入"功效暗示永不过滤"
- references/execution/claim-authority.md：COMMERCIAL_INTENSITY 档位联动更新（STANDARD 下 I5-C 默认开放）；第九节 Hidden Efficacy Implication 收窄为仅 I5-A；AMBER ZONE 非敏感品类默认保留；第二十节最高原则加入"功效暗示永不过滤"
- references/execution/commercial-expression-freedom.md：第二十五章新增"功效暗示默认保留，除非属于 I5-A 硬禁"条款；Edge Expression Policy AMBER 区默认开放、可强化；修复 PARTIAL_PAIN 露出边界残留
- references/execution/anxiety-pain-scenification.md：第四十章痛点距离同步（CONTEXT_PAIN 非敏感品类可作主卖点 / PARTIAL_PAIN 边界体现在不夸大）
- SKILL.md 更新 4.21 Implication Level / 4.22 Pain Distance / 4.32 Commercial Intensity / G6.6 Pain Translation / G6.7 Expression Freedom Validation / G11 Semantic Claim Audit；版本号升至 4.11.4
- scripts/validate_skill.py 新增 Check 24（功效暗示永不过滤契约）

### Hard Bottom Lines Preserved（硬底线保留）
- I5-A 硬禁（未授权疾病/治疗/预防/明确生理结果）任何档位禁止，不得通过暗示/隐喻/谐音/剧情偷渡
- 虚假前后对比、虚构证据、硬功效偷渡一律禁止
- 事实边界（产品真实属性）保留；Truth before strategy 原则不变
- "功效暗示永不过滤"不等于"未授权功效可偷渡"——放宽的是合法边界内的暗示空间，不是 Claim Ceiling

---

## [4.11.3] - 2026-08-15

### Changed
- **PATCH 01 — 输出模板去掉收口家族行**：多行表格模板从"版本标题行 + 角度行 + 收口家族行 + 完整口播稿行"改为"版本标题行 + 角度行 + 完整口播稿行"；单版单表格同步去掉收口家族行
- **PATCH 02 — 收口家族任何场景不输出**：Closing Family（收口家族）保持内部，任何场景都不作为输出内容；多版表格模板的唯一例外仅保留 Angle（角度）作为表格行随交付输出
- **PATCH 03 — 单版轻量输出角度也保持内部**：单版轻量输出时角度保持内部，只有多版表格模板场景下角度随表格输出

### Added
- references/quality/final-output.md 第 26.2/26.3 节更新：多行表格模板去掉收口家族行；角度唯一例外；收口家族任何场景不输出
- SKILL.md 第 10.2/10.3 节同步更新；版本号升至 4.11.3
- 回归测试更新：多版表格模板契约检查改为角度行 + 收口家族不输出（v4.11.3）

### Hard Bottom Lines Preserved（硬底线保留）
- 多版表格模板仍输出版本标题行 + 角度行 + 完整口播稿行
- 每版口播稿必须能独立复制使用
- 内部元数据保持内部原则不变；收口家族回归纯内部
- 硬底线（未授权疾病/治疗/预防、虚假证据、硬功效偷渡）不变

---

## [4.11.2] - 2026-08-15

### Changed
- **PATCH 01 — 多版文案输出模板固化（多行表格）**：多版文案（2 版及以上）默认输出恢复为每版独立多行表格（版本标题行 + 角度行 + 收口家族行 + 完整口播稿行），版本间用空行分隔；单版文案（1 版）可用单表格或轻量输出。这是用户工作流交付格式要求，用于版本区分与审核
- **PATCH 02 — 角度/收口家族输出例外**：Angle（角度）与 Closing Family（收口家族）默认保持内部，唯一例外是多版表格模板场景下作为表格行随交付输出；单版轻量输出时仍保持内部
- **PATCH 03 — Metadata Leak Linter 增加表格模板豁免**：validate_skill.py 与 run_regression.py 的 Metadata Leak 检查识别"多行表格/多版表格/单表格/表格模板/表格行"上下文，不再把多版表格模板误报为元数据泄漏

### Added
- references/quality/final-output.md 第 26.2/26.3 节更新：多版多行表格模板（版本标题行+角度行+收口家族行+完整口播稿行）+ 角度/收口家族输出例外（v4.11.2）
- SKILL.md 第 10.2/10.3 节同步更新；版本号升至 4.11.2
- 回归测试新增多版表格模板契约检查（final-output.md 声明 / SKILL.md 同步 / 单版内部元数据保持）

### Hard Bottom Lines Preserved（硬底线保留）
- 单版轻量输出仍保持"内部元数据保持内部"
- 用户明确要求创作分析时仍先输出文案再输出分析
- 每版口播稿必须能独立复制使用
- 硬底线（未授权疾病/治疗/预防、虚假证据、硬功效偷渡）不变

---

## [4.11.1] - 2026-08-15

### Changed
- **PATCH 01 — Boundary is Internal, Not Content（边界是内部标准，不是文案内容）**：合规边界由内部 Hard Gate 执行，不是文案内容。禁止把边界、免责、说教写进正文——边界不能抢走购买理由。新增免责声明式表达（禁止）与说教式表达（禁止）两类清单：免责声明式（"它不负责让你瘦 / 它不负责改善皮肤 / 我不指望它一夜之间改变什么 / 按法规，普通食品不能宣传功效"）；说教式（"别被神药话术骗 / 那些话术听听就好 / 焦虑驱动的东西，往往买完就后悔 / 买之前先学会看这一行字"）
- **PATCH 02 — PARTIAL_PAIN 不再要求"文中露出真实边界"**：边界体现在"不夸大"（不把部分解决写成全部解决、不把成分写成功效），是内部审查标准，禁止在文案里主动声明边界/免责。同步删除 ibp.md 原则块与 SKILL.md 4.22 中残留的"必须露出真实边界"旧表述
- **PATCH 03 — Relief Contrast After 禁止免责语气**：After 用正面表达（"按天拿一份，这件事就简单了"），禁止"它不负责让你…… / 别指望它…… / 我不指望它……"式自我设限
- **PATCH 04 — Conversion Recovery 禁止说教式自我设限**：恢复 = 把越线那一跳换成合法价值跳，保留情绪强度，不添加免责/说教（禁止"我不指望它改变什么，但每天这件事确实简单了"式自我设限）
- **PATCH 05 — 事实边界保留**：非保健食品/营养素饮品/成分/规格等产品真实属性可自然带出作为可信度，但边界永远不能抢走购买理由；硬底线（未授权疾病/治疗/预防/明确生理结果、虚假证据、硬功效偷渡）不变

### Added
- references/execution/commercial-expression-freedom.md 新增第二十五章"Boundary is Internal, Not Content"（免责声明式表达禁止 + 说教式表达禁止 + 原则）
- references/execution/implicit-benefit-pain.md 更新 PARTIAL_PAIN（v4.11.1：不再要求"文中露出真实边界"，边界体现在不夸大，禁止主动声明边界/免责）
- references/execution/anxiety-pain-scenification.md 更新 Relief Contrast（After 禁止免责语气）
- references/execution/claim-authority.md 更新 COMMERCIAL_INTENSITY 各档位与 PARTIAL_PAIN 联动（任何档位禁止免责声明）
- SKILL.md 更新 4.22 Pain Distance（PARTIAL_PAIN 边界体现在不夸大）与 G6.7 Expression Freedom Validation（Boundary is Internal）
- scripts/validate_skill.py 新增 Check 23（Boundary is Internal contract：cef.md 声明 / 免责+说教禁止声明 / 旧"露出真实边界"残留检测 / PARTIAL_PAIN 内部边界规则 / Relief Contrast After 免责语气禁止 / SKILL.md 声明 / 免责说教短语仅出现在禁止语境）
- 回归测试 6 例（BI-01~06）：Boundary is Internal 声明、免责/说教禁止声明、旧边界残留移除、PARTIAL_PAIN 内部边界、Relief Contrast After、免责说教短语仅禁止语境

### Hard Bottom Lines Preserved（硬底线保留）
- 未授权疾病/治疗/预防/明确生理结果（I5-A）任何档位禁止
- 虚假前后对比、虚构证据、硬功效偷渡一律禁止
- 事实边界（产品真实属性）保留作为可信度，但不得抢走购买理由
- Truth before strategy 原则不变；产品事实与 Claim Ceiling 不因表达放宽而改变

---

## [4.11.0] - 2026-08-15

### Changed
- **PATCH 01 — I5 拆分为三级（最重要）**：I5 Hidden Health/Medical Implication 从一刀切禁止改为 I5-A 硬禁 / I5-B 高风险可上下文 / I5-C 可接受强暗示。I5-A 硬禁（疾病/治疗/预防/明确器官/激素/免疫/睡眠/减肥等生理结果，无授权时任何档位禁止）；I5-B 高风险但可上下文（状态差/疲劳/皮肤焦虑/年龄焦虑允许作为受众上下文，但必须落地到产品实际解决的摩擦，主语义不能变成"产品在改生理"）；I5-C 可接受强暗示（非敏感品类下允许更强的情绪/身份/生活方式暗示，只要 Semantic Back-Translation 后主语义仍落在合法价值域）
- **PATCH 02 — Semantic Back-Translation 从"硬拒"改为"可恢复"**：检测到语义终点越线后不再整篇拒绝，强制进入 CONVERSION_RECOVERY；Recovery 优先保留情绪强度和场景冲击力，只替换掉越线的那一跳；禁止直接删成参数列表
- **PATCH 03 — 痛点距离增加 PARTIAL_PAIN**：Pain Distance 从两级改为三级——DIRECT_PAIN（产品直接解决 → 最强表达）/ PARTIAL_PAIN（产品解决其中关键摩擦 → 允许强表达，但文中要露出真实边界）/ CONTEXT_PAIN（只作为受众状态 → 允许出现，但不能当主卖点；原 INFERRED_PHYSIOLOGICAL_PAIN 归入此类）
- **PATCH 04 — 新增 Edge Expression Policy**：表达分三层——GREEN（用隐喻/剧情/谐音强化已经授权或真实存在的价值：方便/省事/选择成本/感官/仪式感/身份感）；AMBER（灰色区，非敏感品类允许"合理消费者可能产生轻微联想，但主语义仍落在合法价值"的写法）；RED（用同样手法制造未授权功效，禁止）
- **PATCH 05 — 品类差异化天花板**：普通食品/日用品/非宣称功效化妆品 → 明显放宽情绪与生活方式暗示（I5-C 开放、PARTIAL_PAIN 强表达、AMBER 开放）；保健食品/有功效评价的化妆品/医疗器械 → 保持严格（I5-B 仅做受众上下文、I5-C/AMBER 收紧、PARTIAL_PAIN 必须露出边界）；抖音允许更高情绪密度，小红书更强调标准与对比
- **PATCH 06 — 新增 COMMERCIAL_INTENSITY 路由参数**：CONSERVATIVE（当前严格标准）/ STANDARD（默认，适度放宽 I5-B/C 和痛点距离）/ AGGRESSIVE（非敏感品类下允许更强场景冲击和身份暗示，仍禁止硬功效偷渡）。COMMERCIAL_INTENSITY 只改变"怎么说"，不改变"能说什么"——Claim Ceiling 是硬上限，任何档位不得突破
- **PATCH 07 — 品类差异化焦虑强度**：非敏感品类允许更高焦虑密度（更强的情绪语言/更快的痛点切入/更强的 Continuing Cost/更高的 Accumulated Friction 密度）；敏感品类焦虑聚焦"执行/选择/使用"摩擦，身体状态类痛点只能做 CONTEXT_PAIN 不得当主卖点，负面未来场景只描述"行为继续"不描述"身体继续"

### Added
- references/execution/claim-authority.md 新增 COMMERCIAL_INTENSITY（CONSERVATIVE / STANDARD / AGGRESSIVE）路由参数与 Claim Ceiling 关系说明
- references/execution/implicit-benefit-pain.md 更新 I5 三级拆分（I5-A / I5-B / I5-C）与 Pain Distance 三级（DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN）
- references/execution/commercial-expression-freedom.md 新增 Edge Expression Policy（GREEN / AMBER / RED）与品类差异化天花板
- references/execution/anxiety-pain-scenification.md 新增品类差异化焦虑强度
- schemas/route-instance.schema.json 新增 commercial_intensity 字段（enum CONSERVATIVE/STANDARD/AGGRESSIVE，default STANDARD）；implication_level 枚举更新为 I1-I4 + I5-A/B/C；pain_distance 枚举更新为 DIRECT_PAIN / PARTIAL_PAIN / CONTEXT_PAIN
- SKILL.md 新增 Router 4.32 Commercial Intensity、更新 4.21 Implication Level（I5-A/B/C）与 4.22 Pain Distance（PARTIAL_PAIN）
- 6 个 Adapter 新增 Commercial Intensity Hard Rule（I5-A/B/C 阶梯 / PARTIAL_PAIN / Edge Expression Policy / 品类差异化天花板 / 平台强度差异 / 硬底线不变）
- scripts/validate_skill.py 新增 Check 22（Commercial Intensity contract：schema 字段 / claim-authority.md COMMERCIAL_INTENSITY 声明 / I5-A/B/C 声明 / Edge Expression Policy 声明 / 品类差异化天花板声明 / I5-A 硬底线短语仅出现在禁止语境 / Back-Translation 可恢复声明 / SKILL.md Commercial Intensity 声明）
- 回归测试 10 例（CI-01~10，Case 254-263）

### Hard Bottom Lines Preserved（硬底线保留）
- 未授权疾病/治疗/预防/明确生理结果（I5-A）任何档位禁止
- 虚假前后对比、虚构证据、硬功效偷渡一律禁止
- 不引入"为了过审而设计的关键词替换技巧"；Semantic Claim Check 仍是唯一审查方式
- Truth before strategy 原则不变；产品事实与 Claim Ceiling 不因表达放宽而改变

---

---

## [4.10.0] - 2026-08-15

### Changed
- **PATCH 01 — 建立完整 Pain Chain（P1-P8）**：任何商业内容不停留在"用户有 X 痛点"，必须继续向下拆——P1 Surface Problem（嘴上说的问题）/ P2 Trigger Scene（什么时候发生）/ P3 Friction（哪里麻烦）/ P4 Emotional Cost（什么情绪）/ P5 Repeated Cost（反复发生持续损失什么）/ P6 Anxiety（真正担心什么）/ P7 Desired Escape（最希望结束哪种状态）/ P8 Product Bridge（SKU 凭什么接住）；完整链路 Problem → Scene → Friction → Cost → Anxiety → Desired Change → Product
- **PATCH 02 — 禁止抽象痛点直接进入正文**："现代女性生活节奏快，营养补充很重要"太抽象；必须继续问"节奏快到底表现在哪里"落到早上来不及/经常外卖/出差/桌上一堆瓶子/今天吃哪个都要想/买了但总忘/一周坚持三天/临出门又懒得装；正文优先写可看见的麻烦，不是概念
- **PATCH 03 — Pain Scene 满足 Camera Test**：痛点场景尽量做到"摄像机能拍出来"——"早上已经迟到了，桌上还摆着五六个瓶子，这个两粒、那个一粒，最后一看时间，全推回柜子里"；用户应能看到动作/东西/犹豫/麻烦
- **PATCH 04 — 增加 Scene Components**：场景由 TIME / PLACE / OBJECT / ACTION / INTERRUPTION / INNER VOICE / CONSEQUENCE 组成；不要求每篇全部出现，至少选 2–4 个形成真实画面
- **PATCH 05 — 焦虑不是开场硬吓**：禁止"你再不解决就晚了"；优先通过 Accumulated Friction 制造焦虑（第一天麻烦一次→一周忘几次→一个月没形成固定使用习惯→"我是不是又白买了？"）
- **PATCH 06 — 建立 Anxiety Types（A1-A9）**：A1 Loss（已花的钱可能浪费）/ A2 Execution（知道该做但长期做不下来）/ A3 Decision（不知道怎么选）/ A4 Complexity（步骤太复杂）/ A5 Time（持续拖延）/ A6 Opportunity Cost（继续旧方案持续浪费资源）/ A7 Regret（怕最后发现早知道选简单的）/ A8 Wrong-Choice（怕买错/规格错/场景不适合，适合小红书/对比/卖货）/ A9 Social Scene（真实社交场景选择压力，禁止虚构羞辱和社会排斥）
- **PATCH 07 — Anxiety Selection 必须与产品相关**：禁止为了强刺激随便选最大焦虑；Product Truth chooses the anxiety，不是 Anxiety forces the product to fit——独立分装→Execution/Complexity/Portability Friction；售后政策→Wrong-Choice/Purchase Risk；价格/大规格→Cost/Value Anxiety
- **PATCH 08 — 增加 Cost Layer**：痛点不能只是"很烦"，进一步量化/具体化用户付出——TIME / MONEY / MENTAL LOAD / ATTENTION / SPACE / EFFORT / DECISION / EMOTIONAL / SOCIAL / ROUTINE COST；没有真实数字不编数字，用具体行为表达成本
- **PATCH 09 — 建立"继续不解决会怎样"**：每个 Sell Angle 内部问 If nothing changes, what realistically continues?——继续忘/继续闲置/继续每天做重复选择/继续占地方/继续花冤枉钱/继续拖延/继续纠结；Continuing Cost 允许明显强化，但只写真实会继续发生的事
- **PATCH 10 — 允许负面未来场景**：建立在真实逻辑上允许"照这个买法下去，半年后柜子里大概率又多一排开封没吃完的瓶子"；"大概率"无数据支持时改"最容易出现的结果就是……"；第一人称经历需要 IP Fact
- **PATCH 11 — Pain Escalation**：痛点允许逐层升级（小麻烦→每天重复→越来越烦→开始影响执行→钱/时间已付出→用户开始想换方案）= Natural Anxiety Build；不要第一句话就跳到最严重后果
- **PATCH 12 — 建立 Micro-Pain**：不要只找大痛点，高转化内容往往来自 Micro-Pain——每天开很多瓶盖/出差分装/忘记今天吃没吃/包里瓶子响/柜子越来越满/每瓶快吃完日期不同/重复下单/每次都重新查成分/站在货架前不知道选哪个；具体、可信、容易代入、广告感低，优先使用
- **PATCH 13 — 痛点之后不要马上上产品**：禁止固定"痛点→产品出现"；中间可增加 Recognition/Tension——痛点→用户通常怎么解决→为什么旧方法仍麻烦→用户真正缺的是什么→产品出现 = Solution Arrival
- **PATCH 14 — 建立 Failed Solution**：允许讨论过去常见解决方法为什么没解决摩擦（Problem 东西太多→Old Solution 自己分装→New Friction 还是要每天整理→产品支持预先按天组合）；不能虚构竞品缺陷，重点写旧解决方式本身的摩擦
- **PATCH 15 — Pain → Product 必须存在 Mechanism**：禁止"用户焦虑→突然推荐 SKU"；中间必须回答为什么当前产品能降低这个摩擦（Pain 每天自己搭麻烦→Product Fact 按天组合包装→Mechanism 减少每天重复搭配动作→Benefit 执行更简单→Scene 早上拿一包）
- **PATCH 16 — 产品不是救世主**：产品只解决它真正能解决的那一段问题；用户生活很忙产品不能"解决忙"但可以"把日常某一个动作变简单"；Solve the nearest real friction
- **PATCH 17 — Pain Specificity Score（0/1/2）**：0 抽象概念（"现代人很忙"）/ 1 有具体痛点但画面弱 / 2 用户能立刻认出具体场景和摩擦；**Sell 默认 Pain Specificity 不能为 0**
- **PATCH 18 — Scene Vividness Score（0/1/2）**：0 没有画面 / 1 有场景词 / 2 有动作/物件/时间/冲突中至少两个；Douyin 优先达到 2；Xiaohongshu 至少可复查可参考；Channels 可信可转述；OA 可减少镜头细节但需真实问题结构
- **PATCH 19 — Anxiety Legitimacy Gate**：每个焦虑必须通过 Source Test（真实用户问题/合理生活摩擦/搜索评论信号/产品使用场景/用户需求，而非 AI 编造）+ Reality Test（无广告也存在）+ Product Relevance Test（产品真能降低它）三测；任一失败换焦虑
- **PATCH 20 — 禁止的焦虑**：不得创造虚假疾病风险/虚假身体恶化/无证据健康倒计时/无依据年龄恐吓/虚假育儿危险/虚假老人健康风险/虚假失去伴侣家庭后果/虚假社会排斥/虚假库存/虚假涨价/虚假最后机会/无依据"现在不做以后一定后悔"
- **PATCH 21 — 允许更强的情绪语言**：底层事实真实时允许烦死了/最怕/最容易踩坑/最不值/最折腾/真没必要/白花钱/越买越乱/看着都累/最后全闲置/根本坚持不下来；强度必须对应用户真实情绪，不要每篇都喊
- **PATCH 22 — 场景必须服务 Angle**：不要为了真人感随机加早晨/办公室/下班/沙发/厨房；Scene proves the angle——便携→出差/通勤/旅行；减少选择→早晨/每天固定 Routine；性价比→重复购买/闲置/使用次数
- **PATCH 23 — 素人 IP 重点加强生活摩擦**：素人 IP 不自动讲专业理论，优先"我会遇到什么麻烦/我为什么懒得做/什么让我觉得麻烦/我会怎么选"建立真人感；不得自动虚构"我以前每天……""我吃了三个月……"，无 IP Fact 时用当前判断+泛场景
- **PATCH 24 — 达人 IP 重点加强选择焦虑**：达人更适合"我为什么没选 A/我更看重什么/买这一类我最怕什么/我先排除什么/什么信息值得看"；用 Decision Anxiety + Selection Standard 建立专业信用，仍不虚构经历
- **PATCH 25 — 商家重点加强购买风险**：品牌/商家直接帮用户解决买错/规格选错/不适合/不知道怎么用/售后担心/价格疑虑；商家不要假装消费者，利用透明/清楚/直接降低焦虑
- **PATCH 26 — Seed 和 Sell 的焦虑强度不同**：CONTENT 焦虑只让用户意识问题不要求产品介入；SEED 焦虑→用户开始想换方案，重点 Solution Preference；SELL 焦虑→当前 SKU 解释→证据→风险降低→Decision Completion；Sell 焦虑可以更明确但不能为转化制造不存在的严重后果
- **PATCH 27 — 焦虑之后必须给出口**：禁止全篇压焦虑最后不给解决逻辑；使用 Anxiety → Relief Path 形成情绪释放，否则容易恐吓/疲劳/反感；产品扮演"把这件事变简单"而不是"继续吓你"
- **PATCH 28 — Relief Contrast**：允许 Before Friction vs After Simplicity（Before 桌上一排瓶子每天重新想→After 按天拿一份）；After 只能描述产品真实能改变的行为/体验，不能虚构身体结果
- **PATCH 29 — 开头可以直接使用焦虑场景**：Douyin 优先画面冲突+一句现实问题（镜头桌上一排瓶子，口播"这种东西我最怕的不是买贵，是最后全买回来，然后每天根本懒得弄"）；比"今天给大家分享一款产品"更有停留能力
- **PATCH 30 — Xiaohongshu 焦虑要变成 Decision Value**：小红书不要只煽情，焦虑之后必须给判断标准/比较维度/避坑方法/适合条件；目标"我知道怎么避免这个坑了"
- **PATCH 31 — 公众号焦虑升级为问题认知**：公众号不要大量短促恐吓句；一个现实问题→为什么长期存在→我们为什么总用错方式解决→真正需要改变什么；焦虑服务认知推进
- **PATCH 32 — 视频号焦虑必须可转述**：视频号重点"这件事确实很多家庭/普通人会遇到"，让用户能转给朋友/伴侣/家人；不使用家庭健康恐吓
- **PATCH 33 — 多版本不得重复同一种焦虑**：5 篇文案不要全部"怕浪费钱"；动态探索 Version A 执行焦虑/B 选择焦虑/C 时间成本/D 复杂度/E 后悔成本，前提都必须被产品事实支持
- **PATCH 34 — 动态 Angle Discovery 加入 Pain Candidates**：候选 Angle 生成时加入 Micro Pain/Repeated Friction/Loss/Decision Anxiety/Execution Anxiety/Opportunity Cost/Desired Escape；生成 12–20 个 Angle 时也从 What keeps bothering the user? 出发，最终仍必须经过 Product Relevance Gate
- **PATCH 35 — External Intelligence 强化 Pain Discovery**：有 WEB_SEARCH 时研究重点不仅"用户问什么"还要找"用户在抱怨什么"，提炼 REPEATED FRICTION / COMMON CONFUSION / BUYER REGRET / DECISION FEAR / USAGE COMPLAINT / SEARCH ANXIETY；互联网用户抱怨只能产生 Pain Signal，不能自动产生 Product Fact
- **PATCH 36 — 痛点语言优先用户原生表达**：搜索/评论出现大量"太麻烦/总忘/不知道怎么买/买了一堆/放着吃不完"时优先学习这种语言模式，不要自动翻译成"用户存在较高的决策认知成本"；Research 可以专业，正文要像人
- **PATCH 37 — 禁止"五段式焦虑模板"**：不要固定"痛点→放大→后果→产品→CTA"；Scene 可以从结果/动作/抱怨/问题/对话/失败解决/物件/选择任意位置切入；规则应该控制逻辑，不能暴露结构
- **PATCH 38 — 最终 Humanization Pass 增加**：检查"这句话是用户真的会抱怨，还是营销人在替用户制造抱怨？"像后者重写；焦虑越强越需要真人语言
- **PATCH 39 — Commercial Intensity Recovery**：稿子"不够想买"时按顺序检查 Pain 是否具体→Scene 是否能看见→Cost 是否真实→Anxiety 是否有后果感→Desired Escape 是否明确→Product Bridge 是否足够近→Benefit 是否说成人话→Proof 是否支持→Relief Contrast 是否明显；不要第一反应增加更多卖点
- **PATCH 40 — 最终 Hard Gate（PAIN & ANXIETY INTEGRITY GATE）**：检查 Pain Reality / Scene Specificity / Cost Reality / Anxiety Legitimacy / Product Relevance / Claim Integrity / Relief Path；任何虚假危险/无依据灾难/产品接不住的焦虑 = FAIL；但只因为焦虑"有点强"不能自动削弱，只要真实相关可支撑允许保持商业强度

### Added
- references/execution/anxiety-pain-scenification.md — 焦虑激活与痛点场景化引擎 Source of Truth（40 节：Pain Chain P1-P8 / 抽象痛点禁止 / Camera Test / Scene Components / Accumulated Friction / Anxiety Types A1-A9 / Anxiety Selection / Cost Layer / Continuing Cost / 负面未来场景 / Pain Escalation / Micro-Pain / Solution Arrival / Failed Solution / Mechanism / 产品不是救世主 / Pain Specificity Score / Scene Vividness Score / Anxiety Legitimacy Gate / 禁止的焦虑 / 情绪语言 / 场景服务 Angle / 素人/达人/商家 / Seed-Sell 焦虑强度 / Relief Path / Relief Contrast / 焦虑开场 / 平台焦虑差异 / 多版本焦虑多样 / Angle Pain Candidates / External Pain Discovery / 用户原生语言 / 禁止五段式模板 / Humanization Pass / Commercial Intensity Recovery / PAIN & ANXIETY INTEGRITY GATE）
- schemas/route-instance.schema.json 新增字段：anxiety_type / pain_specificity_score / scene_vividness_score / anxiety_legitimacy / relief_path
- SKILL.md 新增 Router 4.27-4.31（Anxiety Type / Pain Specificity Score / Scene Vividness Score / Anxiety Legitimacy / Relief Path）、G6.8 Anxiety & Pain Scenification 硬门、Progressive Disclosure 加载项、Skill Composition 行
- 6 个 Adapter 新增 Anxiety & Pain Scenification Hard Rule（Pain Chain / Camera Test / Anxiety Legitimacy Gate / Accumulated Friction / Relief Path / 禁止虚假焦虑）
- scripts/validate_skill.py 新增 Check 21（Anxiety & Pain Scenification contract：schema 字段 / anxiety-pain-scenification.md 存在 / SKILL.md 引用 / Anxiety Legitimacy Gate 声明 / 禁止虚假焦虑声明 / Relief Path 声明 / Camera Test 声明）
- 回归测试 10 例（ANX-01~10，Case 254-263）

---

## [4.9.0] - 2026-08-15

### Changed
- **PATCH 01 — 重新定义"表达自由"**：Expression Layer（隐喻/类比/谐音/双关/反差/剧情/场景演绎/对话/吐槽/网络语言/情绪放大/口语夸张/关键词变化/用户原话/戏剧冲突/身份表达/生活画面/视觉暗示）默认开放；但表达形式不得创建新的 Product Claim——换一种表达以后消费者理解到的产品效果仍必须在当前 Claim Ceiling 内
- **PATCH 02 — 修辞夸张与事实夸张分离**：新增 RHETORICAL_EXAGGERATION（允许情绪化/生活化/修辞性夸张，如"桌上一排瓶瓶罐罐，看着都累""每天光想今天吃哪几瓶，我已经先放弃一半了"）；Emotional exaggeration is allowed. Factual exaggeration is not
- **PATCH 03 — 禁止事实型夸大**：真实值→更大数字（真实5种不能写10种）、可能→必然、部分用户→所有人、Authorized Claim→更强身体结果、普通体验→医疗效果 全部禁止
- **PATCH 04 — 隐喻全面开放**：隐喻可用于 Convenience / Emotion / Lifestyle / Choice / Product Form / Product Difference / Sensory Experience / Authorized Function（"一包把桌上的瓶瓶罐罐收拾明白了""像给每天这件事按了个快捷键"）；隐喻不得偷偷创造无权限身体功效——翻译回直白语言后越过 Claim Ceiling 即禁止
- **PATCH 05 — 谐音双关开放但不得洗 Claim**：谐音/双关可用于品牌记忆/标题/趣味/场景/情绪/人设/产品特征；Word substitution cannot change claim permission；不是"敏感词换掉 = Claim 自动安全"
- **PATCH 06 — 剧情表达全面开放**：短剧情/夫妻对话/同事场景/办公室/出差/起床/通勤/健身/购物/家庭/收纳/选择困难/懒人场景均允许；剧情中 Product Fact 仍必须真实、人物经历仍遵守 IP Fact Firewall；剧情可以创造 Situation，不能创造 Product Result（禁止"吃了一周以后……""她之前总是……现在……"）
- **PATCH 07 — 放宽痛点表达**：Pain 可以更强，优先挖 Daily / Emotional / Choice / Time / Routine / Cost / Usage / Social Friction（"不是舍不得买，是买回来根本坚持不了""买的时候很认真，吃的时候全靠缘分"）；真实生活摩擦允许明显放大表现
- **PATCH 08 — Pain Translation 强制执行**：所有商业稿走 Surface Pain → Daily Friction → Emotional Cost → Desired Progress → Product Bridge；文案落点"不是让你再记住几瓶，而是尽量把每天这件事变成一个动作"
- **PATCH 09 — 身体痛点不自动删除**：疲惫/熬夜/状态差/饮食不规律/年龄焦虑/皮肤状态可作为 Audience Context；必须区分 User Problem 和 Product Claim；允许用户问题存在，产品能解决到哪里由 Claim Ceiling 决定
- **PATCH 10 — 允许"需求邻接"**：产品不一定直接解决最终大痛点，可以解决 Pain 旁边那个真实摩擦（每天搭配麻烦/携带麻烦/选择成本高/执行复杂）；从大需求进入，最后落到产品真正解决的小摩擦
- **PATCH 11 — Benefit 比参数更靠近用户**：每个核心 Fact 内部走 FACT → WHAT IT DOES → WHY USER CARES → REAL SCENE；正文优先 WHY USER CARES + REAL SCENE，参数作为 Proof
- **PATCH 12 — 允许"结果感"但结果必须属于允许领域**：更省事/更简单/更容易执行/更容易携带/更少选择/少占空间/更容易形成固定流程/更舒服/更符合生活习惯 可以明显、具体、有画面地说；结果感不等于身体功效
- **PATCH 13 — Authorized Claim 允许情绪化表达**：官方 Claim + 用户语言 + 场景；语义强度不超过授权范围（"如果你本来就在做日常维矿补充，这类组合装最大的好处，是不用自己桌上摆一排"）
- **PATCH 14 — 用户原话可用但不能借用户之口洗 Claim**：评论/搜索词/用户痛点用于发现问题；User question gives topic permission. It does not give product claim permission
- **PATCH 15 — 达人/素人更口语更大胆**：吐槽/段子/自嘲/反差/不完整句/网络表达/情绪化表达/强个人判断均允许；Personality Freedom ≠ Claim Freedom
- **PATCH 16 — 商家文案不自动官腔**：品牌/商家身份可以直接/有态度/有商业性/强调产品设计/强调购买理由；商业身份只影响关系透明度，不要求降低文案吸引力
- **PATCH 17 — 开放强利益表达**：Benefit 由真实事实直接支持时允许"最大的价值就在这""它不是多给你一个东西，而是少给你几件每天要操心的事"；无需自动加"可能/也许/一定程度/似乎"无意义弱化词
- **PATCH 18 — Claim Strength 不允许自动缩水**：Strong Evidence → Strong Claim；Weak Evidence → Qualified Claim；No Evidence → No Claim；禁止 Strong Evidence → Weak Marketing 和 Weak Evidence → Strong Marketing
- **PATCH 19 — Semantic Back-Translation**：对隐喻/谐音/剧情/暗示/双关/关键词替换内部做一次 Back-Translation（"这段表达最终让消费者相信产品具有什么效果？"）；有 Claim Authority 或仅合法生活/情绪价值 = PASS；新增健康/医疗/生理功效 = FAIL
- **PATCH 20 — 禁止关键词审查式写作**：不维护"这个词不能说所以换成那个词"的低级系统；改成 Meaning-Based Claim Review；审核 Meaning > Keyword
- **PATCH 21 — Conversion Recovery 成为 Hard Requirement**：高转化 Claim 被 Fact/Claim Gate 拒绝时禁止删除后直接交稿；从 Authorized Claim / Convenience / Product Difference / Routine Simplicity / Cost-Value / Product Format / Usage Experience / Sensory Value / Choice Efficiency / Identity Fit / Emotional Value / Risk Reduction 重建购买理由；Losing one claim cannot automatically mean losing the sale
- **PATCH 22 — Sell Commercial Density**：每篇 Sell 至少 1 个强 Pain/Desire + 1 个与 Pain 直接相关的真实 Product Difference + 1 个明确 User Benefit + 1 个可信 Proof + 1 个 Decision Reason；只剩品牌/成分/参数/"可以了解" = SELL WEAK 重新生成
- **PATCH 23 — Seed Desire Strength**：Seed 允许更强场景想象/产品向往/生活方式投射/选择欲/身份欲/便利欲；最终必须产生"这东西我开始想要了"而不是"我知道这个产品存在"
- **PATCH 24 — 允许一句商业金句但不模板化**：每篇最多一个高浓度利益句/判断句；不能每篇都"真正的 X 不是 A 而是 B"；金句必须从当前 Angle 自然产生
- **PATCH 25 — 不为了合规把正文写满免责声明**：只有法律/平台/产品明确要求展示的警示/声明/限制才进入正文；其余边界由内部 Hard Gate 执行；不每说一个卖点就加"效果因人而异/仅供参考/具体情况不同"
- **PATCH 26 — 最终文案优化顺序**：不够能卖时第一优先提高 Pain Specificity → Product Relevance → Benefit Strength → Scene Vividness → Proof → Emotional Intensity → Decision Clarity；不是第一反应扩大未经授权健康功效
- **PATCH 27 — 最终 Creative Permission**：允许大胆写痛/写烦/写懒/写纠结/写欲望/写生活混乱/写选择困难/写消费者真实吐槽/写戏剧/写冲突/写隐喻/写谐音/写反差/写自嘲/写幽默/写强判断/写商业欲望；不要把 Skill 训练成"合规机器人"；所有创造性最终不能改变现实世界里的产品事实

### Added
- references/execution/commercial-expression-freedom.md — 商业表达自由层 Source of Truth（27 节：Expression Layer 开放 / RHETORICAL_EXAGGERATION / 事实型夸大禁止 / 隐喻开放 / 谐音双关 / 剧情表达 / 痛点放宽 / Pain Translation 强制 / 身体痛点不删除 / 需求邻接 / Benefit 靠近用户 / 结果感 / Authorized Claim 情绪化 / 用户原话 / 达人素人大胆 / 商家不官腔 / 强利益表达 / Claim Strength 不缩水 / Semantic Back-Translation / Meaning-Based Review / Conversion Recovery / Sell Density / Seed Desire / 金句 / 不写满免责声明 / 优化顺序 / Creative Permission）
- schemas/route-instance.schema.json 新增字段：expression_freedom_level / rhetorical_exaggeration / back_translation_result
- SKILL.md 新增 Router 4.24-4.26（Expression Freedom Level / Rhetorical Exaggeration / Back-Translation Result）、G6.7 Expression Freedom Validation 硬门、Progressive Disclosure 加载项、Skill Composition 行
- 6 个 Adapter 新增 Commercial Expression Freedom Hard Rule（Expression Layer 开放 / RHETORICAL_EXAGGERATION / Semantic Back-Translation / Meaning-Based Review / Conversion Recovery / 不写满免责声明）
- scripts/validate_skill.py 新增 Check 20（Commercial Expression Freedom contract：schema 字段 / commercial-expression-freedom.md 存在 / SKILL.md 引用 / Semantic Back-Translation 声明 / Meaning-Based Review 声明 / 事实型夸大禁止声明 / Conversion Recovery 声明）
- 回归测试 10 例（EXPR-01~10，Case 244-253）

---

## [4.8.0] - 2026-08-15

### Changed
- **PATCH 01 — Implication Ladder I1-I5**：暗示不再一刀切禁止，分成 5 级——I1 Product Experience（完全开放，场景自己完成利益表达）/ I2 Lifestyle Benefit（开放：省事/少折腾/更容易坚持/减少选择负担）/ I3 Emotional-Identity（开放：更有秩序/少内耗/更从容，须来自真实场景）/ I4 Conditioned Functional（谨慎开放：有 Authorized Claim 或充分证据时把官方术语翻译成需求语言，不得升级新身体效果）/ I5 Hidden Health-Medical（禁止：即使没有功效词，合理消费者理解成"能治/改善某种身体问题"即 Unauthorized Claim）
- **PATCH 02 — Pain Translation Engine P1-P5**：痛点必须拆成五层——P1 Surface Complaint / P2 Daily Friction / P3 Emotional Cost / P4 Desired Progress（不自动变身体功效）/ P5 Product Bridge（真实事实接住期望变化）；"把每天要做的一堆选择，变成拿一包"即 Pain Translation
- **PATCH 03 — 症状痛点下沉为生活痛点**："累/气色差/熬夜/状态不好/饮食不规律"不绑定成产品治疗目标；"饮食不规律"→ 很难每天精确安排饮食 / 日常营养管理复杂 / 不想买一堆单品组合 / 出差携带麻烦；禁止自动"所以改善营养不良/提高免疫"
- **PATCH 04 — 痛点更狠但必须真实**：允许"最烦的不是贵，是每天还得想今天吃哪几瓶"；Intensify real friction. Do not invent health fear；禁止"你现在不补以后身体就……/长期缺这个一定会……/女人过了30不补就……"恐惧制造
- **PATCH 05 — Product Fact 三次翻译**：每个关键卖点内部完成 FACT → FUNCTION → USER VALUE → SCENE；正文优先使用 USER VALUE + SCENE，而不是只念 FACT
- **PATCH 06 — Benefit Translation Domains（14 域）**：健康功效不能用时从 Convenience / Routine Simplicity / Decision Reduction / Portability / Time Saving / Consistency Support / Sensory Experience / Format Innovation / Cost-Value / Authorized Function / Verified Performance / Lifestyle Fit / Risk Reduction / Choice Confidence 找销售理由；不得因不能使用生理功效就认为"没有卖点"
- **PATCH 07 — Semantic Destination Test**：审核暗示时问"普通消费者看完这句话最自然理解成什么结果？"——"更方便/更容易坚持/更省事"可以，"能治/改善某种身体问题"即使无功效词仍失败；Audit meaning, not vocabulary
- **PATCH 08 — Narrative Implication**：真实场景让 Benefit 自己出现（"出差时不用带一排瓶子，按天数拿几包就行"）；场景可以创建，人物历史不能创建（第一人称历史需 IP Fact 支持）
- **PATCH 09 — Pain Hook 更商业化**：健康品类开头可从真实摩擦切（"买营养品最容易出现一个场面：桌上七八瓶，真正每天都记得吃的没几个"）；"日常营养补充"必须符合当前产品身份和 Authorized Claim
- **PATCH 10 — Product-to-Pain Match Gate**：不能先找高转化痛点再硬接产品；必须 Pain → Product Fact → Mechanism/Format → Benefit 链条成立；Facts choose the pain you are allowed to solve；"下午疲劳"+"仅含B族"未经授权不得自动"所以解决下午疲劳"
- **PATCH 11 — Pain Distance**：DIRECT PAIN（携带/操作/计量/口感/价格/选择麻烦）大胆写；AUTHORIZED FUNCTIONAL PAIN 按 Claim Ceiling 写；INFERRED PHYSIOLOGICAL PAIN 默认不写、优先寻找更近的 Pain；The closer the pain is to the product fact, the stronger the copy may be
- **PATCH 12 — Desire Translation**：不只挖痛点，很多产品更适合卖 Desired State（"我想把每天这件事变简单""不想研究十几种单品""希望出差也容易带"）；强购买欲望不需要依赖健康焦虑
- **PATCH 13 — 体验型轻暗示但不伪造结果**：味道/质地/使用方式/方便程度支持时允许"每天这件事突然变得没那么费劲"；涉及身体结果必须回到 Claim Authority
- **PATCH 14 — 身份统一 Claim Ceiling，痛点语言可不同**：商家偏产品逻辑 / 达人偏选择逻辑与真实体验 / 素人偏日常场景与生活摩擦；允许 Voice Difference，禁止 Fact Permission Difference
- **PATCH 15 — Sell 强制 Pain Translation**：每篇 Sell 至少 1 个真实 Pain/Desire + 1 个 Product Fact + 1 个 User Benefit + 1 个 Proof + 1 个 Decision Reason；正文只有"含有 A、B、C、D……" = Commercial Translation FAIL 重新写
- **PATCH 16 — Seed 偏欲望翻译**：Seed 不必解决全部问题，重点建立"这种解决方式好像挺适合我"；通过 Scene + Pain + Product Difference + Experience Imagination 形成偏好，不急着念完成分
- **PATCH 17 — Pain Translation Quality Check**：五项检查（真实摩擦还是制造焦虑？SKU 凭什么接住？有没有从成分跳到身体结果？Benefit 是否比参数易理解？删除产品后痛点是否过泛？）；⑤ 是说明 Pain 过泛，重新具体化
- **PATCH 18 — 不自动加入免责声明破坏文案**：内部审核与正文表达分开；法律/平台明确要求才展示警示语；否则不每说一个卖点就加"效果因人而异/并非医疗作用/仅供参考"；事实边界由后台 Hard Gate 控制
- **PATCH 19 — 商业强度优先从 Pain 和 Benefit 提高**：卖不动时优先提高 Pain Specificity / Desire Strength / Scene Vividness / Product Relevance / Benefit Clarity / Proof Strength / Decision Value；不要优先扩大未经授权功效
- **PATCH 20 — 最终最高原则**：痛点可以讲深不要讲假；场景可以讲狠不要制造疾病恐惧；用户价值可以暗示，未经授权的身体功效不能偷渡；不要把"不能说某个功效"理解成"不能卖这个产品"；少一点"它能把你身体变成什么样"，多一点"它能把你每天这件事变得怎么样"

### Added
- references/execution/implicit-benefit-pain.md — 暗示利益与痛点翻译层 Source of Truth（20 节：Implication Ladder I1-I5 / Pain Translation Engine P1-P5 / 症状痛点下沉 / 痛点真实强度 / Fact 三次翻译 / Benefit Domains / Semantic Destination Test / Narrative Implication / Pain Hook / Product-to-Pain Match Gate / Pain Distance / Desire Translation / 体验型轻暗示 / 身份统一 Ceiling / Sell 强制 Pain Translation / Seed 偏欲望翻译 / Pain Translation Quality Check / 不自动免责声明 / 商业强度优先 / 最高原则）
- schemas/route-instance.schema.json 新增字段：implication_level / pain_distance / pain_translation_path / benefit_translation_domain
- SKILL.md 新增 Router 4.21-4.23（Implication Level / Pain Distance / Pain Translation Path）、G6.6 Pain Translation 硬门、G11 Semantic Destination Test、Progressive Disclosure 加载项
- 6 个 Adapter 新增 Pain Translation Hard Rule（Implication Ladder / Pain Translation Engine / Semantic Destination Test / Narrative Implication / 不自动免责声明 / 不制造疾病恐惧）
- scripts/validate_skill.py 新增 Check 19（Pain Translation contract：schema 字段 / implicit-benefit-pain.md 存在 / SKILL.md 引用 / 隐藏健康医疗暗示仅出现在禁止语境 / Semantic Destination Test 声明 / 不制造疾病恐惧声明）
- 回归测试 10 例（PAIN-01~10，Case 234-243）

---

## [4.7.0] - 2026-08-15

### Changed
- **PATCH 01 — CLAIM_AUTHORITY_LEVEL L0-L6**：产品功效不再使用"安全/危险"二元判断；每条主张先判断表达权限（L0 UNKNOWN / L1 PRODUCT ATTRIBUTE / L2 AUTHORIZED CLAIM / L3 PRODUCT-SPECIFIC EVIDENCE / L4 USER-VALUE TRANSLATION / L5 AUTHENTIC EXPERIENCE / L6 UNAUTHORIZED EFFECT）；L2 授权主张按官方表达力度 Direct Claim，不得自动弱化为"可能/也许/据说/好像"；L6 默认不得进入正文
- **PATCH 02 — Category Claim Ceiling**：写产品文案前必须识别 PRODUCT_REGULATORY_CATEGORY（GENERAL_GOODS / ORDINARY_FOOD / HEALTH_FOOD / NUTRIENT_SUPPLEMENT_HEALTH_FOOD / COSMETIC / MEDICAL_DEVICE / DRUG / OTHER）；不知道且 WEB_SEARCH 存在时自动检索官方标签/注册备案身份，不能只凭"营养包/养生/美容"猜
- **PATCH 03 — 普通食品**：成分/营养成分/口味/工艺/规格/食用便利/场景可强表达；不得升级为保健功能/疾病预防/治疗；禁止"气色好了/姨妈更舒服/熬夜扛得住"等暗语身体功效，但可重新寻找真正 User Value
- **PATCH 04 — 保健食品/营养素补充剂**：依法注册/备案的保健食品先建立 AUTHORIZED_CLAIM_SET（注册功能/功效成分/含量/适宜人群/不适宜人群/食用量/食用方法/警示）；正文把授权功能讲清楚讲具体讲有购买价值；禁止因"健康品类"自动全部弱化；禁止无依据推导"所以改善疲劳/气色更好"
- **PATCH 05 — 美妆产品**：COSMETIC 不得自动进入"功效不能说"；有充分依据的保湿/抗皱/紧致/舒缓/控油/防晒/祛斑美白等合法功效宣称可直接表达；Evidence-backed efficacy is a selling point, not a forbidden word
- **PATCH 06 — Claim-to-Benefit Translation**：每个重要 Product Fact 问"So what for the customer?"；答案只能进入 12 个合法 Benefit Domain（Convenience / Time Saving / Ease of Use / Portability / Routine Simplicity / Taste / Product Experience / Choice Efficiency / Cost / Authorized Functional Benefit / Verified Performance / Lifestyle Fit）；不得自行创造 Medical/Physiological Outcome
- **PATCH 07 — Strength Matching**：建立 CLAIM_STRENGTH（DIRECT / EVIDENCE_BOUNDED / CONDITIONAL / SUBJECTIVE / ATTRIBUTE_ONLY / PROHIBITED）；Claim Strength = Maximum Strength Supported by Evidence；强证据不弱化，弱证据不升级
- **PATCH 08 — Commercial Usefulness Gate**：每篇 Sell 必须建立 COMMERCIAL_VALUE_PATH（Problem → Authorized Function / Convenience / Product Difference / Routine Simplification / Verified Experience / Value / Cost）；只有成分/规格/备案号没有用户利益 = FAIL 必须重写
- **PATCH 09 — 功效暗示 vs 价值联想**：允许 Value Association（"早上赶时间，拿一包就走"=便利）；禁止 Hidden Efficacy Implication（"你懂的/女生那几天多来一包/熬夜党第二天状态差别很明显"=暗语偷渡）；Imply lifestyle value, not hidden medical efficacy
- **PATCH 10 — 禁止违规词替换器**：禁止建立"危险词→安全替代词"映射表（改善睡眠→夜里更踏实 / 补血→脸色更漂亮）；执行 Semantic Claim Check 而非 Keyword Check——检查用户最终会理解成什么效果
- **PATCH 11 — 平台审核不是写作目标**：平台规则用于 Risk Detection 不得用于 Evasion Design；合法真实 Claim 需要免责/证明/表达形式调整时按最新平台要求调整，不能隐语绕开机器审核
- **PATCH 12 — Commercial Claim Zone**：每篇内容把主张分成 GREEN（明确事实/授权 Claim/真实价格规格/真实体验/直接使用利益，大胆讲）/ AMBER（有证据但条件多/有限测试/适配性判断，准确限定）/ RED（未授权疾病功效/绝对效果/隐语偷渡/原料功效自动等同产品功效，禁止）；GREEN 不要因为 RED 存在就一起变弱
- **PATCH 13 — 素材优先寻找可卖的绿色事实**：联网 Product Retrieval 不能只问"哪些话不能说"，必须主动搜索"What can we strongly and truthfully sell?"（授权功能/配方组合/每日剂量/独立包装/食用方式/原料来源/规格/味道/技术/检测/备案/设计/便利/需求匹配）；Expand the sellable truth set
- **PATCH 14 — 不同商业身份同一 Claim Ceiling**：达人/素人 IP/品牌商家/店主/创始人在同一产品上的产品功效权限必须相同；身份影响叙述方式，不改变产品事实权限；禁止"素人用个人体验暗示功效""达人说体验绕过 Claim"
- **PATCH 15 — 真实个人体验不能成为功效许可证**：IP Fact Source 真实支持的习惯/偏好/口味可表达；真实身体体验必须同时判断是否允许用于商业传播；True personal experience does not automatically equal legal commercial claim
- **PATCH 16 — Conversion Recovery**：最想讲的功效不能合法使用时禁止"那就什么都不说"；从 Authorized Claim / Attribute / Convenience / Routine Value / Product Design / Verified Difference / Cost / Ease / Taste / Format / Risk Reduction 重建购买理由；Lose the illegal claim, not the sale
- **PATCH 17 — Sell Copy 最低商业要求**：每篇卖货稿至少 1 个明确需求 + 1 个当前 SKU 真实差异 + 1 个能被理解的 Benefit + 1 个证明 + 1 个选择理由；不能退化为"这个产品成分很多，可以了解一下"
- **PATCH 18 — 营养品示例**：备案营养素补充剂授权"补充多种维生素矿物质"可明确说"备案功能就是补充多种维生素矿物质"+"按天分装最大的价值就是省事"；不自动写"吃完精神更好/气色更好/免疫更好"
- **PATCH 19 — Hard Gate 顺序调整**：新增 PRE-GATE 1（Regulatory Category & Claim Ceiling）、G6.5（Commercial Usefulness）、G11（Semantic Claim Audit）、G12（Review Risk Audit）；最终顺序 Product Identity → Regulatory Category → Product Retrieval → Authorized Claim Set → Evidence Set → Claim Ceiling → Audience Need → Benefit Translation → Commercial Value Path → Platform Native → Write → Semantic Claim Audit → Review Risk Audit → Final
- **PATCH 20 — 最终最高原则**：Compliance sets the ceiling. Copywriting should write as strongly as possible below that ceiling；商业内容第一任务是把真实价值卖出去；不做"最安全但卖不动"，也不做"靠违规功效才能成交"

### Added
- references/execution/claim-authority.md — 主张表达权限层 Source of Truth（20 节：L0-L6 / Category Ceiling / 普通食品 / 保健食品 / 美妆 / Benefit Translation / Strength Matching / Commercial Usefulness Gate / Value Association vs Hidden Efficacy / Semantic Claim Check / Claim Zone / Sellable Green Facts / 身份同一 Ceiling / Conversion Recovery / Sell 最低商业要求 / 营养品示例 / Hard Gate 顺序 / 最高原则）
- schemas/route-instance.schema.json 新增字段：product_regulatory_category / claim_authority_level / claim_strength / commercial_value_path
- 6 个 Adapter 新增 Claim Authority Hard Rule（Regulatory Category / Authorized Claim Set / Sellable Green Facts / Semantic Claim Check / 同一 Claim Ceiling / Conversion Recovery）
- scripts/validate_skill.py 新增 Check 18（Claim Authority contract：schema 字段 / claim-authority.md 存在 / SKILL.md 引用 / 无违规词替换器映射表 / Semantic Claim Check 声明 / Hidden Efficacy 禁止声明）
- 回归测试 10 例（CLAIM-01~10，Case 224-233）

---

## [4.6.2] - 2026-08-15

### Changed
- **PATCH 01 — Product Fact Source 与 Product Fact Sufficiency 分离**：新增 PRODUCT_FACT_SOURCE（含 official_web / authorized_official_listing / mixed_verified）和 PRODUCT_FACT_SUFFICIENCY（NONE / IDENTITY_ONLY / PARTIAL_FACTS / SUFFICIENT_FOR_CONTENT / SUFFICIENT_FOR_SEED / SUFFICIENT_FOR_SELL）；禁止使用 product_fact_source != unknown 作为"不需要联网检索"的依据
- **PATCH 02 — Product Acquisition Preflight（PRE-GATE 0）**：正式 Hard Gates 之前新增产品获取预检流程；只有在 Product Acquisition 完成后才进入 G1 Product Truth；禁止先进入 G1 发现事实不足后直接要求用户提交资料
- **PATCH 03 — Search Before Ask 最高优先规则**：用户提供可搜索线索 + WEB_SEARCH 存在时，Agent 必须先搜索；禁止第一反应"请上传详情页/请提供配料表/资料不足无法完成"
- **PATCH 04 — WEB_ONLY 模式修复**：WEB_ONLY = WEB_SEARCH available, local file source unavailable；不代表只能依赖用户提供 SKU 事实；可以从官方网页建立 Product Ledger
- **PATCH 05 — WEB_SEARCH 双任务区分**：明确区分 PRODUCT_SOURCE_RETRIEVAL（产品身份/事实检索）和 EXTERNAL_INTELLIGENCE（用户问题/趋势/竞争语境）
- **PATCH 06 — 6 个 Adapter 统一 WEB_SEARCH 声明**：所有支持 WEB_SEARCH 的 Adapter 新增 Product Source Retrieval + External Intelligence 双任务声明；统一 Hard Rule：Product Retrieval 优先于 External Intelligence
- **PATCH 07 — Product Retrieval 优先于 External Intelligence**：商业任务中产品事实不足时，先查产品，不要先查热点
- **PATCH 08 — Product Identity Status 重新定义**：EXACT / PARTIAL / UNKNOWN；"用户写了产品名"不代表 EXACT；必须判断名称是否唯一对应当前 SKU
- **PATCH 09 — PARTIAL 也必须先搜**：PARTIAL + WEB_SEARCH → 先执行 SKU Discovery Search
- **PATCH 10 — Minimum Disambiguation**：搜索后仍有多个 SKU 时只问区分 SKU 所需的最少问题；Ask for identity, not for information the agent can retrieve itself
- **PATCH 11 — 产品信息请求分成两种**：IDENTIFIER REQUEST（身份请求）vs PRODUCT DATA REQUEST（产品数据请求）；后者仅在 6 种限定条件下允许
- **PATCH 12 — SKILL.md 冲突句修复**："When no source is provided: assume minimal fact set from user input" 改为先评估→搜索→再决定
- **PATCH 13 — Skill Composition 声明修复**：Product Truth 来源扩展至官方网页检索；Master Copywriting 可以 retrieve and assemble a Product Ledger from verified official sources
- **PATCH 14 — Route Schema 升级**：route-instance.schema.json 新增 product_identity_status / product_fact_sufficiency / product_retrieval_status；product_fact_source 增加 official_web / authorized_official_listing / mixed_verified
- **PATCH 15 — Purpose-Specific Fact Minimum**：Content / Seed / Sell 各自定义最低事实要求；缺失可选字段不取消整篇任务
- **PATCH 16 — No Exhaustive Data Demand**：禁止穷举式资料索取；Agent 必须优先问"缺失的哪个字段真正阻塞当前任务"
- **PATCH 17 — High-Risk Product Retrieval**：营养补充剂/保健食品等自动提高 Source Quality 要求；Higher verification threshold ≠ no search
- **PATCH 18 — High-Risk Claims Separate**：Product Fact 与 Health/Function Claim 分开；禁止因产品含某种营养素自动推导身体效果
- **PATCH 19 — Search Discovery 和 Fact Retrieval 分两轮**：Round 1 Identity Discovery → Round 2 Product Fact Retrieval
- **PATCH 20 — 搜索结果必须形成 Product Ledger**：检索结束后建立 Canonical Product Ledger 再进入 G1
- **PATCH 21 — Search Failure 才允许 Ask**：只有执行过 Product Source Retrieval 且 FAILED/AMBIGUOUS 才允许问用户
- **PATCH 22 — 禁止没有搜索就声称"资料不足"**：Premature Information Request = Hard Gate FAIL
- **PATCH 23 — Tool Use Evidence**：Product Retrieval 触发后内部必须记录 TOOL_EXECUTION_STATE
- **PATCH 24 — 不要向用户暴露内部搜索流程**：成功搜索后默认不展示 Research Brief / Product Ledger
- **PATCH 25 — 素人 IP 带货特殊规则**：素人 IP 不等于可以虚构消费者经历；区分 ORDINARY_PERSON_TONE 和 REAL_PERSONAL_EXPERIENCE
- **PATCH 26 — 回归测试新增（6 例）**：PRODUCT-WEB-01 至 PRODUCT-WEB-06（Case 218-223）
- **PATCH 27 — 行为测试定义**：PRODUCT-WEB-01~06 案例覆盖产品名明确、多个 SKU、未搜索就拒绝、营养补充剂、第三方测评、价格缺失等场景
- **PATCH 28 — 所有 Adapter 新增统一 Hard Rule**：Commercial task + insufficient product facts → Product Retrieval first
- **PATCH 29 — Capability 表更新**：WEB_SEARCH 描述从"Search public internet for facts, questions, trends"改为"Retrieve verified official product sources, verify current external facts, and perform External Intelligence research"
- **PATCH 30 — 最终执行顺序统一**：PRE-GATE 0 加入执行顺序流程；绝对禁止"发现用户没给详情页→直接把资料收集工作退回给用户"

### Added
- references/execution/product-acquisition.md — 产品事实获取层 Source of Truth（30 节规则，含 Search Before Ask、Product Ledger、Minimum Disambiguation、High-Risk Product Retrieval、Purpose-Specific Fact Minimum 等）
- schemas/route-instance.schema.json 新增字段：product_identity_status / product_fact_sufficiency / product_retrieval_status
- 回归测试 6 例（PRODUCT-WEB-01~06，Case 218-223）

---

## [4.6.1] - 2026-08-15

### Changed
- **CTA Permission 硬化（PATCH 01/02/04/05/35/36）**：CTA 从"隐式优先"的 Preference 改为 Permission 问题。CTA_PERMISSION 只有 IMPLICIT_ONLY（默认）/ EXPLICIT_ALLOWED 两个值；删除 AUTO/MAYBE/PREFERRED/LAST_CHOICE 等模糊状态；Sell、热用户、高购买意向、first_goal=purchase_decision 均不自动解锁显式 CTA；只有命中 Closed Explicit CTA Allowlist（用户明确要求 / 直播成交阶段 / 商品卡 Button / 广告 CTA Button / Landing Page / 表单 / 明确私域动作）才允许显式
- **取消"每篇必须有收口家族"（PATCH 02）**：Closing Family 仅当 Closing Strategy = IMPLICIT_CLOSE 时才需要内部选择；NATURAL_STOP 不分配 Closing Family；多版可 NATURAL_STOP / NATURAL_STOP / IMPLICIT_A / IMPLICIT_B / NATURAL_STOP
- **Natural Stop 升级（PATCH 01.5）**：Closing Strategy 只允许 NATURAL_STOP / IMPLICIT_CLOSE / EXPLICIT_CTA；最高原则 No closing sentence is better than a forced closing sentence
- **No Fake Memory Gate（PATCH 03/33）**：跨批次收口轮换、家族使用计数、避开上一批次仅在 MEMORY capability 或用户上下文提供 Content History 时执行；否则只做 Current Batch QA
- **Research/Tool Claim Integrity（PATCH 34）**：无 WEB_SEARCH 不得声称「最近大家都在搜/现在流行/根据搜索结果/当前市场趋势」；无 FILE_READ 不得声称「根据你的产品 Skill」；无 CODE_EXECUTION/CALCULATOR 不得假装运行计算工具；无 MEMORY 不得声称历史使用次数
- **Silent Activation（PATCH 08）**：删除首次启动 12 行版本介绍；默认静默激活，仅用户明确询问时输出版本/帮助
- **Final Output Contract 冲突修复（PATCH 06/07/24）**：删除"禁止输出收口家族 + 顶部表格必须输出收口家族"的冲突；默认只输出 标题+正文/口播+必要画面建议；多版=每版独立块；禁止默认输出角度/收口家族/QA/路由/评分等内部元数据；输出格式改为 Default（Markdown 默认，用户明确格式优先）
- **Progressive Disclosure 统一（PATCH 09/10）**：references/reference-index.md 成为 Reference Loading Source of Truth；SKILL.md 只保留简要调用；FULL 模式 = 所有可选能力可用，references 仍选择性加载
- **Capability 命名统一（PATCH 11/32）**：全包 CODE_EXEC → CODE_EXECUTION；Capability Contract Test 自动扫描
- **Hard Gates 绝不可降级（PATCH 12）**：删除 route-instance.schema.json 的 hard_gate_exceptions，改为 verification_limits（只说明无法自动验证什么，不降低真实性标准）
- **Product Fact Schema 串源修复（PATCH 13/14/31）**：key_facts.source_type 仅接受 P1_PRODUCT_FACT；commercial_identity 移出 Product Schema，加入 route-instance.schema.json 的 commercial_relationship
- **Route Variables 恢复（PATCH 15）**：route-instance.schema.json 与 SKILL.md Router 补回 content_format / target_audience / audience_temperature / first_goal / commercial_relationship / cta_permission / closing_strategy；Audience Temperature 只影响信息深度/异议处理/Offer 解释，不影响 CTA Permission
- **24 Modes Purpose 旧逻辑修复（PATCH 16）**：普通种草去掉"即时成交"目标；普通卖货"行动"改为 Decision Readiness；决策信息锚点改为"是否选择当前方案/SKU"
- **平台禁止反向制造 IP 经历（PATCH 17/18）**：Platform Native 不能创建 biography；IP Persona Signal 优先当前判断/偏好/标准/原则/取舍，只有 IP Fact 支持时才用过去经历
- **CTA 示例清理（PATCH 19/20）**：显式 CTA 反例统一移入 NEGATIVE EXAMPLES — DO NOT RECALL；绝对化/过度承诺/压迫感/金句化示例降级或删除；CTA reference 重点保留机制而非成品句
- **Stale Cross-Reference 修复（PATCH 21）**：references 中"主 SKILL.md 第 X 节"改为稳定文件路径 + Heading Name；references/cta.md 改为 references/craft/cta.md
- **版本同步（PATCH 22）**：reference-index / README / build fallback / portability-report 统一至 4.6.1
- **Single Source of Truth 真正执行（PATCH 23）**：CTA 权限规则只定义在 craft/cta.md；其他 references 只引用不重新定义

### Added
- **验证脚本 Bug 修复（PATCH 26/27）**：validate_skill.py 改用标准化 heading 匹配（修复"Canonical Product/IP Interface"假失败）；run_regression.py 支持中文平台名（抖音/小红书/公众号/视频号）+ canonical ID
- **新增 Linter（PATCH 29/30）**：CTA Conflict Linter（检测"热用户明确CTA/点击下单 SAFE/卖货+条件→显式CTA"）；Metadata Leak Linter（检测"禁止输出收口家族 + 模板要求输出收口家族"冲突）
- **Source Separation Schema Tests（PATCH 31）**：自动验证 Product Facts 不接受 IP_FACT/MARKET_SIGNAL/EXTERNAL_FACT；Commercial Relationship 属于 Route Instance
- **Capability Contract Tests（PATCH 32）**：全包扫描只允许 Canonical Capability Names，发现 CODE_EXEC 直接 FAIL
- **Regression Cases 新增（PATCH 37）**：CTA-01 至 CTA-08 / OUTPUT-01 / FORMAT-01 / ROUTE-01 / ROUTE-02 / FACT-01 / MEMORY-01 / CAP-01 / PURPOSE-01 / IDENTITY-01（Case 201-217）
- **Static Contract Tests + Behavioral Regression 分层（PATCH 28/38/39）**：静态契约测试检查文件结构/Schema/Source of Truth/禁止冲突短语/Capability 命名/旧 Section Link/Output Metadata Leak/CTA Permission conflict；Behavioral Regression 未实际运行 Model 时报告 NOT RUN，不得伪装 PASS
- **Cross-Agent Behavioral Test（PATCH 38）**：tests/portability/cross-agent-behavioral-test.md 定义 6 类 Agent 的 Canonical Decision 一致性检查（Route/Purpose/CTA_PERMISSION/Commercial Relationship/Fact Set/Hard Gate）；scripts/run_behavioral_regression.py 无模型时如实报告 NOT RUN
- **Build Gate 更新（PATCH 39）**：build_package.py 构建前强制运行 validate_skill.py（Static Validation + Schema + Conflict Lint），任一失败即中止；Behavioral Regression 状态如实标注
- **Patch 完成后实际运行（PATCH 40）**：实际执行 validate_skill.py / run_regression.py --all / build_package.py --all --clean，解压新 ZIP 再次 Smoke Test
- **Smoke Test 目录匹配 Bug 修复（PATCH 40 执行期）**：smoke_test_zip 对目录期望值（如 references/）拼接出双斜杠 references// 导致永远匹配失败，改为 rstrip('/') 后匹配
- **Secret Scanner 误报修复（PATCH 40 执行期）**：扫描器误报自身源码中的 secret/token/credentials 词汇；正则改为要求真实赋值分隔符（= 或 :）并在关键词处强制标识符边界（lookbehind/lookahead），消除误报且不削弱真实密钥检测

---

## [4.6.0] - 2026-08-15

### Added
- **首次启动提示（First Launch Prompt）**：SKILL.md 新增第 0 节，当技能在当前对话中首次被激活时，先向用户输出一次简洁启动提示（仅一次，不重复）
- 启动提示包含四块：版本号（读 frontmatter）、功能概览、如何使用（平台/目的/产品事实/数量/特殊要求 + 示例触发语）、输出约定
- 触发规则：仅在本技能触发范围内输出；同一对话只输出一次；用户直接给完整任务时先提示再执行

### Changed
- SKILL.md frontmatter 版本升至 4.6.0；10.1 节与 final-output.md 第 26 节版本标签同步更新

---

## [4.5.3] - 2026-08-15

### Added
- **最终模板固化**：多版文案输出最终模板 = 顶部角度概览表（稿号 / 版本名 / 角度 / 收口家族 / 字数）+ 每版独立块（单行版本标题表格 + 表格外引用块完整口播稿）
- 每版独立块内不重复角度、收口家族（已在顶部概览表呈现）
- SKILL.md 10.1 节与 final-output.md 第 26 节同步更新；版本升至 4.5.3

---

## [4.5.2] - 2026-08-14

### Changed
- **最终交付不再显示角度、收口家族**：角度与收口家族仅用于生成阶段防重复与选型（G10 输出净化），最终交付只保留"版本标题表格 + 表格外完整口播稿"
- 每版结构 = 单行版本标题表格（稿N · 版本名）+ 下方引用块完整口播稿；角度概览等辅助信息仅用户明确要求时才呈现
- SKILL.md 10.1 节与 final-output.md 第 26 节同步更新；版本升至 4.5.2

---

## [4.5.1] - 2026-08-14

### Changed
- **完整口播稿移出表格单元格**：v4.5.0 把长稿塞进表格单元格会被截断、无法完整复制；改为"元信息表格（版本标题 + 角度 + 收口家族）+ 表格下方独立引用块输出完整口播稿"
- 每版结构 = 元信息表格 + 表格外完整口播稿；每版口播稿必须能独立复制使用
- SKILL.md 10.1 节与 final-output.md 第 26 节同步更新；版本升至 4.5.1

---

## [4.5.0] - 2026-08-14

### Changed
- **多版文案输出格式**：2 版及以上时，每版文案使用独立的多行表格分开（版本标题行 + 角度行 + 收口家族行 + 完整口播稿行），替代"所有稿塞进同一单元格"的旧格式
- 每版口播稿必须能独立复制使用；版本间用空行分隔
- 单版文案（1 版）仍可用单表格输出
- SKILL.md 10.1 节与 final-output.md 第 26 节同步更新；description 加入"多版文案每版用多行表格分开"

---

## [4.4.0] - 2026-08-14

### Added
- **输出格式硬约束**：Final Output Contract 新增 10.1 节，规定最终交付物一律使用纯 Markdown（md）格式
- 完整口播稿强制入表规则：表头"完整口播稿"仅允许出现一次，多篇稿在同一个单列表格同一单元格内用 **【稿N · 版本名】** 分隔
- 禁止 HTML / docx / pptx / 其他富文本作为最终交付物（除非用户明确要求 HTML 报告）

### Changed
- SKILL.md description 加入"最终输出纯md格式"
- references/quality/final-output.md 新增第 26 节输出格式约束

---

## [4.3.0] - 2026-08-14

### Added
- 隐式收口家族从 9 个扩展至 **15 个隐式家族**（新增 question_echo 问题回抛 / scene_leave 场景留白 / contrast_close 反差收束 / habit_seed 习惯种子 / story_open 故事留口 / taste_invite 味觉邀请）
- 家族句式变体库：每个家族至少 3 个句式变体，跨批次复用必须换变体
- 三重防重复机制：单批次配额（同家族最多 1 次）、跨批次轮换（不得复用上批次家族）、句式指纹防重（核心动词/价值理由词/收尾人称/句式结构四维检查）
- 家族使用计数：记录各家族使用次数，未使用过的家族优先
- 平台 × 目的 × 家族映射表：不同平台×目的锁定首选家族池，防跨内容收口雷同

### Changed
- references/craft/cta.md 升级至 v4.3.0，选择优先级扩展至 7 层
- SKILL.md description 加入"隐式收口丰富多元化，拒绝单一重复"，版本升至 4.3.0

---

## [4.2.0] - 2026-08-14

### Changed
- 隐式收口原则升级为四层结构：**种草一律隐式 → 卖货优先决策完成感 → 隐式收口备选 → 显式CTA是最后选择**
- references/craft/cta.md：卖货型内容优先决策完成感，隐式收口备选（choice_helper / verification_task），显式CTA是最后选择
- references/execution/purpose-integrity.md：CTA 优先决策完成感，隐式收口备选，显式引导是最后选择
- SKILL.md description 同步四层原则，版本升至 4.2.0

---

## [4.1.0] - 2026-08-14

### Changed
- 隐式收口优先：种草一律隐式，卖货优先决策完成感，显式CTA是最后选择
- SKILL.md description 加入隐式收口优先，版本升至 4.1.0

---

## [4.0.0] - 2026-08-14

### Added
- **Cross-Agent Portable Skill Package** architecture
- Canonical Core + Progressive Disclosure + Capability Negotiation design
- Platform Adapters (generic, claude, openai, gemini, copilot, limited-agent)
- Graceful Degradation across 4 runtime modes: FULL, GROUNDED, WEB_ONLY, TEXT_ONLY
- Capability abstraction: WEB_SEARCH, FILE_READ, FILE_SEARCH, CODE_EXECUTION, CALCULATOR, FUNCTION_CALLING, MCP, MEMORY, STRUCTURED_OUTPUT
- Runtime Capability Negotiation system
- Tool Independence Contract (never simulate missing tools)
- Skill Composition model (Master + Product + IP + External Intelligence)
- Canonical Product/IP Interface with standard schemas
- 5 JSON schemas: product-facts, ip-facts, route-instance, research-brief, content-fingerprint
- Portability Audit test suite (7 agent simulations)
- Activation regression tests (positive + negative tests)
- Validation scripts: skill structure, fact consistency
- Standard and Agentic distribution packages
- Capability matrix documentation
- Reference index with progressive disclosure loading map
- New directory structure with references organized by module

### Changed
- SKILL.md slimmed down to canonical core only
- Detailed rules moved to references/ (loaded progressively)
- Single Source of Truth: all business rules in canonical references only
- Adapters map tools, never modify rules
- Version jumped to 4.0.0 (major architecture change)

### Architecture Note
This is a packaging and portability release. The business rules (writing logic,
hard gates, purpose integrity, expression authority, etc.) are preserved from
v3.7. This release does NOT rewrite the intelligence — it packages it for
cross-agent deployment.

---

## [3.7.0] - 2026-08-14

### Added
- Default Length Engine
- Word count as information budget (not hard KPI)
- 12 default target word counts (4 platforms × 3 purposes)
- Complexity adjustment coefficients
- Stop Condition framework (4 conditions)
- Natural Completion > Target Word Count principle
- Word count self-check (10 questions)

---

## [3.6.0] - 2026-08-14

### Added
- Execution Reliability Patch
- Hard-Gate Execution Order (10 levels)
- Canonical Product Ledger
- Cross-Output Product Consistency
- Comparison Evidence Gate
- Demonstration Truth re-enforced
- Fake Comparison Visual prohibition
- Final Output Sanitizer
- Internal Metadata anti-leakage
- Eight-draft final checklist

---

## [3.5.0] - 2026-08-14

### Added
- Purpose Integrity (Content / Seed / Sell redefined)
- Purpose Drift Test (Seed Test + Sell Test)
- Seed is not a weakened version of Sell
- Demonstration Truth Gate (4 classifications)
- First-Person Claim Scanner
- Current Judgment vs Biography distinction
- Purpose-Specific Fact Selection

---

## [3.4.0] - 2026-08-14

### Added
- Cross-Platform Re-conception Protocol
- Platform Content Brief (6 questions)
- Commercial Identity Integrity
- Cross-Platform Proposition Collision Check
- Cross-Platform Fact Selection
- Platform-Specific Information Density
- Identity Consistency Across Platforms
- Identity vs Narrative Role
- Four-platform final QA

---

## [3.3.0] - 2026-08-14

### Added
- Claim Integrity Pass
- Source-of-Truth Precedence (6 levels)
- Numeric Consistency Gate
- Derived Claim Firewall (4 classifications)
- Causal Leap prohibition
- Business Fact Firewall
- Personality Asset ≠ Biography
- Cross-Draft Fact Consistency
- Reasoning Humility
- Claim Budget
- Fact Ledger

---

## [3.2.0] - 2026-08-14

### Added
- External Claim Admission Gate
- Source Type classification (P1, P2, E1, E2, S1, U1, C1)
- Claim Admission Test (8 questions)
- Claim Strength Matching
- Claim Cascade Check
- Product Transfer Firewall
- Research Reward Hacking prohibition
- 3-level external knowledge admission
- Commercial Claim Escalation
- Source Trace internal audit

---

## [3.1.0] - 2026-08-14

### Added
- Research-to-Content Intelligence Protocol
- Web Signal classification (7 types)
- Research → Angle forced mapping
- Search Value Gate
- Saturation Penalty
- Information Gain Score
- Category Diversity
- Research Novelty Test
- Research Quality QA
- Platform-specific Research-to-Content conversion

---

## [3.0.0] - 2026-08-14

### Added
- External Intelligence Layer
- Real-time web research integration
- Web signal detection and classification
- Research-to-angle mapping
- External fact boundary management
- Research quality QA
- Cross-validation of external and internal facts

---

## [2.9.0] - 2026-08-14

### Added
- Account-level content decision system
- Audience Tension Discovery
- Claim-Proof Matching
- Platform-Specific Proof Preference
- Account-Level IP Asset Planning
- IP Asset Hierarchy
- Content Portfolio Role

---

## [2.8.0] - 2026-08-14

### Added
- Anti-Patternization Layer
- Rule execution trace minimization
- Example Anti-Anchoring
- Set-Level QA enhancements
- Fixed topic check
- Excessive dilution check

---

## [2.7.0] - 2026-08-14

### Added
- Dynamic Angle Discovery Engine
- Natural Depth Layer
- Multi-version angle diversity
- Depth budget management
- Conversational flow optimization

---

## [2.6.0] - 2026-08-14

### Added
- Anti-Patternization Layer (initial)
- Rule execution invisibility
- Mandatory Constraint / Optional Expression distinction
- Structural Diversity
- Semantic Redundancy Check
- Natural Ending
- Set-Level QA

---

## [2.5.0] - 2026-08-14

### Added
- Cross-Platform Unified Expression Authority Layer
- Three information sources data boundary
- Four levels of expression authority
- Fact expansion test
- IP Fact Firewall
- Professional Humility
- Competitive Restraint
- Expansion Budget
- Information proliferation detection
- Source Trace Audit

---

## [2.4.0] - 2026-08-14

### Added
- Real Person Content Principles
- Information Subtraction Layer
- Excessive Completeness Detection
- Humanization Pass 2.0
- Platform Native Human Writing Layer
- Information Gain per sentence metric

---

## [2.3.0] - 2026-08-14

### Added
- Platform-specific native writing styles
- Douyin native voice
- Xiaohongshu native voice
- WeChat Official Account native voice
- WeChat Channels native voice
- Platform-specific quality standards

---

## [2.2.0] - 2026-08-14

### Added
- Stability improvements
- Rule conflict resolution
- Knowledge management optimization
- Routing refinements

---

## [2.1.0] - 2026-08-14

### Added
- Decision-focused system architecture
- Multiple decision models
- Reference knowledge base structure

---

## [2.0.0] - 2026-08-14

### Added
- Full-stack copywriting decision system
- 24 modes (4 platforms × 3 purposes × 2 IP modes)
- Multi-platform support
- IP mode support
- Seed/Sell differentiation
