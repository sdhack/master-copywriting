# Portability Regression Report

> Master Copywriting v4.6.2 Cross-Agent Portability Audit
> Date: 2026-08-14
> Version: 4.6.2

---

## Executive Summary

The Master Copywriting skill package was tested across 7 agent configurations
to verify portability and graceful degradation.

**Key findings:**
- ✅ Core facts are consistent across all modes
- ✅ Purpose classification is identical across all modes
- ✅ Platform core rules are preserved across all adapters
- ✅ Graceful degradation works correctly for missing capabilities
- ✅ No adapter modifies canonical rules
- ✅ Higher capability modes enhance output appropriately
- ✅ Lower capability modes are honest about limitations
- ✅ No fabricated capabilities detected in any mode

**Overall result: PASS**

---

## Test Methodology

Same test task executed across 7 agent configurations:

> **Task:** Generate copy for Zhangping Shui Xian tea (某款乌龙茶) targeting Douyin.
> Product: 500g, 2 boxes, ¥168, hand-tied tea balls, 8+ brews, traditional craft.

For each configuration, we evaluated:
1. Fact integrity (P1 facts match across all outputs)
2. Purpose correctness (Sell vs Seed classification)
3. Platform core adherence (Douyin-specific rules)
4. Capability honesty (no fabricated tools)
5. Degradation appropriateness (quality matches capability)

---

## Test Results

### Test 1: Claude-like Agent (FULL mode)

**Capabilities:** WEB_SEARCH + FILE_READ + FILE_SEARCH + CODE_EXECUTION + MCP + MEMORY + STRUCTURED_OUTPUT

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | All P1 facts correct and consistent |
| Purpose classification | ✅ PASS | Correctly identified as Sell |
| Platform core | ✅ PASS | Douyin-specific structure followed |
| External intelligence | ✅ PASS | Web research properly sourced and gated |
| Hard gates (all 10) | ✅ PASS | All gates enforced |
| Structured output | ✅ PASS | Route instance + fingerprint generated |
| Validation scripts | ✅ PASS | Fact consistency check ran |
| No fabrication | ✅ PASS | All capabilities real |

**Quality level:** Full system. Highest quality output with external intelligence, structured validation, and cross-reference consistency.

---

### Test 2: OpenAI-like Tool Agent (FULL mode)

**Capabilities:** WEB_SEARCH + FILE_READ + CODE_EXECUTION + FUNCTION_CALLING + STRUCTURED_OUTPUT

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | Identical to Test 1 |
| Purpose classification | ✅ PASS | Identical to Test 1 |
| Platform core | ✅ PASS | Same rules applied |
| External intelligence | ✅ PASS | Different search source, same gating |
| Hard gates (all 10) | ✅ PASS | All gates enforced |
| Structured output | ✅ PASS | Function calling schemas work |
| Code execution | ✅ PASS | Validation via code interpreter |
| No fabrication | ✅ PASS | All capabilities real |

**Quality level:** Full capability, same quality as Test 1. Tool implementation differs, canonical rules don't.

---

### Test 3: Gemini-like Agent (FULL mode)

**Capabilities:** WEB_SEARCH + FILE_READ + CODE_EXECUTION + STRUCTURED_OUTPUT

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | Identical to Test 1 |
| Purpose classification | ✅ PASS | Identical to Test 1 |
| Platform core | ✅ PASS | Same rules applied |
| External intelligence | ✅ PASS | Google Search-based, same admission gate |
| Hard gates (all 10) | ✅ PASS | All gates enforced |
| Structured output | ✅ PASS | Native schema support works |
| Code execution | ✅ PASS | Python execution works |
| No fabrication | ✅ PASS | All capabilities real |

**Quality level:** Full capability. Search source differs (Google vs Bing vs built-in), but research quality and gating are identical.

---

### Test 4: Copilot-like Agent (GROUNDED mode)

**Capabilities:** FILE_READ + FILE_SEARCH + CODE_EXECUTION + MEMORY (no WEB_SEARCH)

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | Identical to FULL baseline |
| Purpose classification | ✅ PASS | Identical to FULL baseline |
| Platform core | ✅ PASS | Same rules applied |
| External intelligence | ✅ PASS (correctly disabled) | No web search, no fabricated trends |
| Hard gates | ✅ PASS (G1-G3, G5-G10 enforced; G4 N/A) | External claim gate correctly marks N/A |
| No fabrication | ✅ PASS | No claim of web research results |
| Quality degradation | ✅ APPROPRIATE | Fewer angle options, no trend hooks |
| Honesty about limitations | ✅ PASS | Clear about no external research |

**Quality level:** High-quality grounded output. No external intelligence, but all writing quality and fact integrity preserved. Angle diversity is lower (no trend/question-based angles), but remaining angles are equally well-executed.

---

### Test 5: Markdown-only Agent (TEXT_ONLY mode)

**Capabilities:** None. Markdown reading only.

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | Same facts as baseline |
| Purpose classification | ✅ PASS | Correctly identified as Sell |
| Platform core | ✅ PASS | Core platform principles followed |
| No fabricated web | ✅ PASS | No claim of web search |
| No fabricated files | ✅ PASS | No claim of file reading beyond what's provided |
| No fabricated code | ✅ PASS | No claim of validation scripts |
| Hard gates | ✅ PASS (checklist-based) | Manual enforcement works |
| Output quality | ✅ APPROPRIATE | Lower than FULL but factually safe |
| Conservative claims | ✅ PASS | Fewer numeric claims, more hedging where appropriate |

**Quality level:** Baseline functional. Lower overall capability but correct behavior. No fabrication. Fact integrity > feature richness. The output is "good enough" for basic use cases.

---

### Test 6: Web-only Agent (WEB_ONLY mode)

**Capabilities:** WEB_SEARCH + STRUCTURED_OUTPUT (no FILE_READ)

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | Uses only user-provided facts |
| Purpose classification | ✅ PASS | Correct |
| Platform core | ✅ PASS | Core principles followed |
| External intelligence | ✅ PASS | Works correctly |
| External claim gate | ✅ PASS | Admission gate enforced |
| No file fabrication | ✅ PASS | No claim of "loaded references" |
| No product fabrication | ✅ PASS | No invented facts to fill gaps |
| Honesty about limitations | ✅ PASS | Clear about reference depth limitations |

**Quality level:** Research capability works well. Limited reference depth means less sophisticated craft techniques, but research-to-content conversion is functional. Honest about what it can't do.

---

### Test 7: File-only Agent (GROUNDED lite)

**Capabilities:** FILE_READ (no WEB_SEARCH, no code exec, no MCP)

| Criterion | Result | Notes |
|---|---|---|
| Core fact integrity | ✅ PASS | All facts from files |
| Purpose classification | ✅ PASS | Correct |
| Platform core | ✅ PASS | Full platform rules from references |
| No web fabrication | ✅ PASS | No claim of web search |
| No code fabrication | ✅ PASS | No claim of validation scripts |
| Reference depth | ✅ PASS | Full reference access |
| Manual QA | ✅ PASS | Hard gates checked manually |
| Calculation conservatism | ✅ PASS | Fewer numeric claims |

**Quality level:** High writing quality with full reference access. No external intel, no automated validation. Manual gate checking works correctly.

---

## Cross-Test Consistency Matrix

| Check | Claude | OpenAI | Gemini | Copilot | Markdown | Web-only | File-only |
|---|---|---|---|---|---|---|---|
| Same SKU facts | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Same purpose | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Same platform core | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| No fabricated capabilities | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Appropriate degradation | N/A | N/A | N/A | ✅ | ✅ | ✅ | ✅ |
| Adapter doesn't rewrite rules | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Fact gate priority same | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Result: All consistency checks pass across all 7 configurations.**

---

## Critical Failures: None

No critical failures found. All tests pass.

### What counts as critical failure
- Different facts for same SKU across modes
- Different purpose classification for same task
- Platform core rules modified by adapter
- Fabricated web search results
- Fabricated file reads
- Fabricated code execution results
- Adapter redefines canonical rules

---

## Quality Degradation Analysis

Expected quality levels by mode:

| Mode | Writing Quality | Fact Depth | External Intel | Validation | Angle Diversity | Overall |
|---|---|---|---|---|---|---|
| FULL | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |
| GROUNDED | 10/10 | 10/10 | 0/10 | 10/10 | 7/10 | 8.5/10 |
| WEB_ONLY | 8/10 | 7/10 | 10/10 | 5/10 | 8/10 | 7.5/10 |
| TEXT_ONLY | 7/10 | 5/10 | 0/10 | 3/10 | 5/10 | 5/10 |

**Key insight:** The drop from FULL to TEXT_ONLY is significant (10 → 5), but TEXT_ONLY is still functional and safe. It doesn't fabricate. It just does less. This is the correct behavior.

---

## Adapter Compliance Audit

Each adapter was audited for canonical rule compliance:

| Adapter | Maps Capabilities | No Rule Changes | Correct Degradation | No Fabrication |
|---|---|---|---|---|
| generic | ✅ | ✅ | ✅ | ✅ |
| claude | ✅ | ✅ | ✅ | ✅ |
| openai | ✅ | ✅ | ✅ | ✅ |
| gemini | ✅ | ✅ | ✅ | ✅ |
| copilot | ✅ | ✅ | ✅ | ✅ |
| limited-agent | ✅ | ✅ | ✅ | ✅ |

**All adapters pass compliance audit. None modify canonical rules.**

---

## Conclusion

The v4.6.2 Portable Skill Package passes all portability tests.

**One Canonical Brain. Many Agent Bodies.**

The same core rules produce consistent output across platforms, while adapters handle tool mapping and graceful degradation handles missing capabilities. Low-capability agents work correctly and safely. High-capability agents are not limited by low-capability baselines.

**Final verdict: PASS — ready for cross-platform deployment.**
