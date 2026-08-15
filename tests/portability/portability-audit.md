# Portability Audit Tests

> Test suite for verifying cross-agent portability of the Master Copywriting skill package.
> These tests validate that canonical rules are preserved across different agent platforms and capability levels.

---

## Test Framework

For each agent type / capability combination, run the same task and verify:

1. **Core facts are identical** — same SKU = same facts across all outputs
2. **Purpose is identical** — same task = same purpose classification
3. **Platform core is respected** — each platform's core logic is preserved
4. **Missing tools → correct degradation** — no fabricated capabilities
5. **Higher capability → appropriate enhancement** — more tools = better output, not different rules
6. **No adapter overrides canonical rules** — adapters map tools, not rewrite logic

---

## Test 1: Claude-like Agent (FULL mode)

**Setup:** All capabilities available (WEB_SEARCH + FILE_READ + FILE_SEARCH + CODE_EXECUTION + MCP + MEMORY + STRUCTURED_OUTPUT)

**Task:** Generate 4-platform × Seed/Sell = 8 pieces for one SKU

**Checks:**
- [ ] All 10 hard gates enforced
- [ ] Canonical Product Ledger established and consistent
- [ ] Cross-platform re-conception: 8 different propositions
- [ ] External intelligence properly sourced and gated
- [ ] Structured output (schemas) used correctly
- [ ] Validation scripts run successfully
- [ ] Purpose completion correct (4 seeds + 4 sells)
- [ ] IP identity consistent across platforms
- [ ] Final output sanitized (no internal metadata)
- [ ] All reference modules accessible

**Expected result:** Full system capability. Highest quality output.

---

## Test 2: OpenAI-like Tool Agent (FULL mode)

**Setup:** WEB_SEARCH + FILE_READ + CODE_EXECUTION + FUNCTION_CALLING + STRUCTURED_OUTPUT

**Task:** Generate 4-platform × Seed/Sell = 8 pieces for one SKU

**Checks:**
- [ ] Same core facts as Test 1
- [ ] Same purpose classification as Test 1
- [ ] Same platform core logic as Test 1
- [ ] Hard gates enforced same way
- [ ] Different tool implementations, same canonical rules
- [ ] Structured output works via function calling
- [ ] Code execution for validation works

**Expected result:** Full capability, same quality as Test 1. Tool implementation differs, rules don't.

---

## Test 3: Gemini-like Agent (FULL mode)

**Setup:** WEB_SEARCH + FILE_READ + CODE_EXECUTION + STRUCTURED_OUTPUT

**Task:** Generate 4-platform × Seed/Sell = 8 pieces for one SKU

**Checks:**
- [ ] Same core facts as Test 1
- [ ] Same purpose classification as Test 1
- [ ] Same platform core logic as Test 1
- [ ] All hard gates enforced
- [ ] Google Search-based external intelligence
- [ ] Structured output via native schema support

**Expected result:** Full capability, same rule compliance. Search source differs, logic doesn't.

---

## Test 4: Copilot-like Agent (GROUNDED mode)

**Setup:** FILE_READ + FILE_SEARCH + CODE_EXECUTION + MEMORY (no WEB_SEARCH)

**Task:** Generate 4-platform × Seed/Sell = 8 pieces for one SKU

**Checks:**
- [ ] Same core facts as FULL mode
- [ ] Same purpose classification
- [ ] Same platform core logic
- [ ] External intelligence DISABLED (no web search)
- [ ] No fabricated trends, competitor data, or user questions
- [ ] All product facts from provided sources only
- [ ] Hard gates still enforced (G1-G3, G5-G10)
- [ ] G4 (External Claim) effectively N/A but no fabrication
- [ ] Quality degradation is appropriate (fewer angles, no trend-based hooks)
- [ ] No claim of "research shows" or "users say" without source

**Expected result:** High-quality grounded output. No external research. Fewer angle options but same fact integrity and writing quality.

---

## Test 5: Markdown-only Agent (TEXT_ONLY mode)

**Setup:** No tools. Only SKILL.md + reading markdown references.

**Task:** Generate single-platform sell copy for one SKU

**Checks:**
- [ ] Core routing works (platform, purpose, IP mode)
- [ ] Hard gates enforced as checklist
- [ ] No fabricated web results
- [ ] No fabricated file reads
- [ ] No fabricated code execution results
- [ ] No structured output claimed
- [ ] Fact integrity maintained
- [ ] Purpose correctly identified
- [ ] Platform core respected
- [ ] Output quality is lower but factually safe
- [ ] All claims conservative
- [ ] No reference to capabilities that don't exist

**Expected result:** Baseline functional. Lower capability but correct behavior. No fabrication. Fact integrity > feature richness.

---

## Test 6: Web-only Agent (WEB_ONLY mode)

**Setup:** WEB_SEARCH + STRUCTURED_OUTPUT (no FILE_READ, no local references)

**Task:** Generate single-platform seed copy using external research

**Checks:**
- [ ] External intelligence works
- [ ] External Claim Admission Gate enforced
- [ ] No reference to "loaded references" or "read from file"
- [ ] Product facts only from user input (no file sources)
- [ ] Research-to-content conversion works
- [ ] Hard gates enforced for what's available
- [ ] No fabricated product facts to fill gaps
- [ ] Honest about what can and can't do

**Expected result:** Research capability works, but grounded in user-provided facts only. No file access = no reference depth. Honest about limitations.

---

## Test 7: File-only Agent (GROUNDED lite)

**Setup:** FILE_READ (no WEB_SEARCH, no code exec, no MCP)

**Task:** Generate multi-version copy for one SKU

**Checks:**
- [ ] References loaded from files
- [ ] No web search claimed
- [ ] No code execution claimed
- [ ] All product facts from file sources
- [ ] Dynamic angle discovery works (from references)
- [ ] Hard gates enforced manually
- [ ] No numeric validation script run
- [ ] Calculations are conservative

**Expected result:** Full reference access, no external intel, no automated validation. High quality writing, manual QA.

---

## Cross-Test Consistency Checks

Across all 7 test scenarios:

| Check | Tests Compared |
|---|---|
| Same SKU facts identical across all modes? | All 7 |
| Purpose classification consistent? | All 7 |
| Platform core rules same? | All 7 |
| No fabricated capabilities? | All 7 |
| Graceful degradation appropriate? | All 7 vs FULL baseline |
| Adapters never rewrite canonical rules? | All 7 |
| Fact gate priority same everywhere? | All 7 |

---

## Failure Definitions

### Critical Failures (must fix before release)
- Different facts for same SKU across modes
- Different purpose classification for same task
- Platform core rules modified by adapter
- Fabricated web search results
- Fabricated file reads
- Fabricated code execution results
- Adapter redefines canonical rules

### Quality Degradation (acceptable if appropriate)
- Fewer angle options (no web search)
- No automated validation (no code exec)
- Simpler QA process (no structured output)
- Less reference depth (no file access)

These are expected and correct — as long as the system is honest about them.
