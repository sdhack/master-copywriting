# Activation Regression Tests

> Test whether the skill activates correctly for the right prompts and doesn't activate for wrong ones.
> Important because agent skill activation heavily depends on name + description matching.

---

## Should Activate (Positive Tests)

These prompts should trigger the Master Copywriting skill.

### Explicit Copywriting Requests
1. "帮我写一篇抖音文案"
2. "Write a product description"
3. "做一篇小红书种草笔记"
4. "Generate ad copy for this product"
5. "写个公众号长文"
6. "Create a short video script"
7. "帮我写卖货文案"
8. "Write sales copy"

### Content-Type Requests
9. "做个内容规划"
10. "Generate multi-platform content"
11. "跨平台文案方案"
12. "写几个版本的标题"
13. "IP内容怎么写"
14. "种草文案怎么写"

### Implicit Copywriting Requests
15. "这个产品怎么推广" (with writing expectation)
16. "帮我出个脚本"
17. "写段口播"
18. "详情页怎么优化"

---

## Should NOT Activate (Negative Tests)

These prompts should NOT trigger the Master Copywriting skill.

### Pure Research Questions
1. "茶叶市场怎么样"
2. "What's the trend in skincare"
3. "行业分析"

### Pure Product Management
4. "这个产品定价多少合适"
5. "Product roadmap"
6. "供应链怎么优化"

### General Marketing Advice (no output)
7. "怎么做品牌"
8. "Marketing strategy advice"
9. "怎么引流" (general advice, no writing task)

### Code / Data Tasks
10. "写个Python脚本"
11. "Analyze this data"
12. "Build a website"

### Other Skill Domains
13. "帮我翻译一下"
14. "Summarize this article"
15. "给我做个PPT"

---

## Edge Cases (Should Activate, But Carefully)

These are borderline cases that should activate but with careful routing.

1. **"帮我看看这段文案写得怎么样"** → Activates for review/QA, not generation
2. **"这个产品有什么卖点"** → Activates for sell-point discovery if writing task follows
3. **"怎么做内容"** → Activates if content strategy/copywriting is implied
4. **"竞品分析"** → Activates only if it's for copywriting purposes, not pure market research
5. **"用户画像"** → Activates only if part of a copywriting task, not pure research

---

## Activation Quality Metrics

For each positive test, check:
- [ ] Skill activates
- [ ] Correct task type routing
- [ ] Correct platform detection
- [ ] Correct purpose detection (or auto-detect logic runs)
- [ ] No false certainty about purpose/platform if ambiguous

For each negative test, check:
- [ ] Skill does NOT activate
- [ ] No false positive activation
- [ ] If activation is borderline, it defers to user clarification

---

## Description Optimization Notes

Current description includes:
- ✅ Capabilities (full-stack copywriting decision & generation)
- ✅ Trigger scenarios (ad copy, product copy, IP content, seed, sales copy, etc.)
- ✅ Key platforms (Douyin, Xiaohongshu, WeChat Official Account, Channels)
- ✅ Main task types (short-video, long-form, notes, headlines, multi-platform)
- ✅ Progressive disclosure mention
- ✅ Graceful degradation mention

What NOT to put in description:
- ❌ Full rule list (too long, won't be read)
- ❌ Every mechanism name (overwhelming)
- ❌ Internal jargon (agents won't understand)
- ❌ Version numbers (not relevant for activation)

The description should be: clear enough to activate correctly, short enough to be read fully, keyword-rich for matching.
