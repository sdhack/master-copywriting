# Cross-Agent Behavioral Test（跨 Agent 行为一致性测试）

> **版本**：v4.6.2（PATCH 38）
> **目的**：验证同一批 Prompt 安装到不同 Agent 后，Canonical Decision 一致。
> **核心检查不是句子一样，而是 Canonical Decision 一样。**

---

## 一、测试原则

同一批 Prompt 在以下 Agent 上运行：

- OpenAI-like
- Claude-like
- Gemini-like
- Copilot-like
- Generic
- Limited Agent

允许：**措辞不同**（模型差异导致的合理风格差异）。

不允许：**Canonical Decision 不同**。

---

## 二、记录维度

每个 Agent 运行后，记录以下 Canonical Decision：

| 维度 | 说明 |
|---|---|
| Route | 平台 / 目的 / IP 模式 / 任务类型 |
| Purpose | content / seed / sell |
| CTA_PERMISSION | IMPLICIT_ONLY / EXPLICIT_ALLOWED |
| Commercial Relationship | brand_official / shop_owner / founder / collab_influencer / ... |
| Fact Set | 使用的产品事实集合（必须一致） |
| Hard Gate Result | G1-G10 PASS/FAIL |

预期：**全部一致。**

---

## 三、测试用例（与 regression-tests.md 的 CTA-01 ~ IDENTITY-01 对应）

| Case | Prompt | 预期 Canonical Decision |
|---|---|---|
| CTA-01 | 写一条抖音卖货口播，某款乌龙茶 | platform=douyin, purpose=sell, CTA=IMPLICIT_ONLY，无显式 CTA |
| CTA-02 | 写一条小红书卖货笔记，某款乌龙茶 | platform=xiaohongshu, purpose=sell, CTA=IMPLICIT_ONLY |
| CTA-03 | 写一条视频号 IP 卖货口播，某款乌龙茶 | platform=channels, ip_mode=ip, CTA=IMPLICIT_ONLY |
| CTA-04 | 写一条公众号卖货长文，某款乌龙茶 | platform=official_account, purpose=sell, CTA=IMPLICIT_ONLY |
| CTA-05 | 热用户卖货，某款乌龙茶 | CTA 仍 = IMPLICIT_ONLY（热用户不改变 CTA Permission） |
| CTA-06 | 直播最后30秒明确成交口令 | CTA=EXPLICIT_ALLOWED（命中 Closed Allowlist B） |
| CTA-07 | 商品卡按钮文案 | CTA=EXPLICIT_ALLOWED |
| CTA-08 | 给种草稿加明确购买 CTA | 用户明确授权 → CTA=EXPLICIT_ALLOWED |
| OUTPUT-01 | 多版文案 | 不出现收口家族/角度/QA 等 metadata |
| FORMAT-01 | 用户要求 JSON | 不得强制 Markdown |
| ROUTE-01 | 店主写 | commercial_relationship=shop_owner |
| ROUTE-02 | 合作达人写 | commercial_relationship=collab_influencer，Product Facts 不变 |
| MEMORY-01 | 无 MEMORY 且无 History | 不得声称"上一批已经用过" |
| IDENTITY-01 | 平台规则 | 不得自动生成"我一直在用" |

---

## 四、运行方式

### 无模型环境（默认）

```bash
python scripts/run_behavioral_regression.py
```

输出：**Behavioral Regression = NOT RUN**。

不得伪装成 PASS。

### 有模型环境

```bash
export MASTER_COPYWRITING_MODEL=openai:gpt-4o
python scripts/run_behavioral_regression.py
```

输出：PASS / FAIL，并附每个 Case 的 Canonical Decision 记录表。

---

## 五、Build Gate 集成（PATCH 39）

Release 前：

1. Static Validation = PASS
2. Schema Validation = PASS
3. Conflict Lint = PASS
4. Packaging Smoke Test = PASS
5. Behavioral Regression = PASS / FAIL / **NOT RUN**（无模型时如实标注 NOT RUN）
