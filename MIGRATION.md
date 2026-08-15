# Migration Guide: v3.x → v4.0

This guide helps you migrate from Master Copywriting v3.x to the v4.0
Portable Skill Package.

---

## Overview

v4.0 is a **packaging and architecture release**. The business rules are
preserved from v3.7. No writing logic has been changed.

What changed:
- Directory structure reorganized
- SKILL.md slimmed down
- References organized by module
- Platform adapters added
- Capability negotiation added
- Schemas and validation scripts added

What didn't change:
- 24 Modes
- Platform Core rules
- Purpose definitions
- Expression Authority Layer
- External Intelligence Layer
- All Hard Gates
- Cross-Platform Re-conception
- Default Length Engine
- All writing quality mechanisms

---

## File Migration Map

### v3.x structure (monolithic)
```
SKILL.md (huge, 30+ sections)
references/
  ├── external-intelligence.md
  ├── expression-authority.md
  ├── dynamic-angle-discovery.md
  ├── natural-depth.md
  ├── anti-patternization.md
  ├── default-length-engine.md
  ├── final-output.md
  ├── cross-platform-reconception.md
  ├── purpose-integrity.md
  ├── execution-reliability.md
  ├── account-level-system.md
  ├── platforms.md
  ├── compliance.md
  ├── examples.md
  ├── before-after-example.md
  └── ... (many more)
tests/
  └── regression-tests.md
metadata/
  └── version-history.md
```

### v4.0 structure (modular)
```
SKILL.md (slim, canonical core only)
references/
  ├── reference-index.md         ← NEW: loading map
  ├── modes/
  │   ├── 24-modes.md
  │   └── platforms.md
  ├── angle/
  │   ├── dynamic-angle-discovery.md
  │   └── natural-depth.md
  ├── external/
  │   └── external-intelligence.md
  ├── cross-platform/
  │   └── cross-platform-reconception.md
  ├── execution/
  │   ├── execution-reliability.md
  │   ├── purpose-integrity.md
  │   └── expression-authority.md
  ├── quality/
  │   ├── anti-patternization.md
  │   ├── default-length-engine.md
  │   ├── final-output.md
  │   └── compliance.md
  ├── account/
  │   └── account-level-system.md
  └── craft/
      ├── hooks.md
      ├── formulas.md
      ├── cta.md
      ├── voice.md
      ├── psychology.md
      ├── ip-naturalness.md
      ├── method-cards.md
      ├── examples.md
      └── before-after-example.md
adapters/                        ← NEW
  ├── generic.md
  ├── claude.md
  ├── openai.md
  ├── gemini.md
  ├── copilot.md
  └── limited-agent.md
schemas/                         ← NEW
  ├── product-facts.schema.json
  ├── ip-facts.schema.json
  ├── route-instance.schema.json
  ├── research-brief.schema.json
  └── content-fingerprint.schema.json
tests/
  ├── regression/
  │   └── regression-tests.md
  ├── portability/               ← NEW
  │   └── portability-audit.md
  └── activation/                ← NEW
      └── activation-tests.md
scripts/                         ← NEW
  ├── validate_skill.py
  └── validate_facts.py
assets/
  └── capability-matrix.md
```

---

## SKILL.md Migration

### What to keep in SKILL.md (v4.0 canonical core)
- Mission
- Activation triggers
- Capability Negotiation
- Router
- Execution Order (high-level)
- Progressive Disclosure map
- Hard Gates (quick reference only)
- Canonical Product/IP Interface
- Skill Composition
- Final Output Contract
- Versioning

### What to move to references
- Platform-specific details → `modes/platforms.md`
- 24 modes details → `modes/24-modes.md`
- Dynamic angle discovery → `angle/dynamic-angle-discovery.md`
- Natural depth → `angle/natural-depth.md`
- External intelligence → `external/external-intelligence.md`
- Cross-platform re-conception → `cross-platform/cross-platform-reconception.md`
- Execution reliability / hard gates detail → `execution/execution-reliability.md`
- Purpose integrity → `execution/purpose-integrity.md`
- Expression authority → `execution/expression-authority.md`
- Anti-patternization → `quality/anti-patternization.md`
- Default length engine → `quality/default-length-engine.md`
- Final output polish → `quality/final-output.md`
- Compliance → `quality/compliance.md`
- Account-level system → `account/account-level-system.md`
- Hooks, formulas, CTA, examples → `craft/`

---

## For Existing Installations

### If you're using v3.x on a single agent

1. **Back up** your current skill folder
2. **Replace** with v4.0 package
3. **Load** the appropriate adapter for your platform
4. **Test** with your standard test cases
5. **Verify** output quality matches v3.7 baseline

### If you want to deploy to multiple agents

1. Start with the **Agentic Package**
2. Set up each platform's adapter
3. Run capability negotiation on each agent
4. Compare output across agents (should have same core facts, same purpose)
5. Run portability audit

---

## Breaking Changes

None for writing logic. This is a packaging release.

**Potential integration changes:**
- File paths have changed (references reorganized)
- SKILL.md is much shorter — if you had custom prompts referencing specific sections, update them
- New YAML frontmatter format in SKILL.md

---

## Compatibility

v4.0 is fully backward compatible with v3.7 writing output.

| Feature | v3.7 | v4.0 |
|---|---|---|
| 24 Modes | ✅ | ✅ |
| Platform Cores | ✅ | ✅ |
| Hard Gates (10 levels) | ✅ | ✅ |
| Expression Authority | ✅ | ✅ |
| External Intelligence | ✅ | ✅ |
| Cross-Platform Re-conception | ✅ | ✅ |
| Purpose Integrity | ✅ | ✅ |
| Default Length Engine | ✅ | ✅ |
| Dynamic Angle Discovery | ✅ | ✅ |
| Natural Depth | ✅ | ✅ |
| Anti-Patternization | ✅ | ✅ |
| Account-Level System | ✅ | ✅ |
| Portable across agents | ❌ | ✅ |
| Capability negotiation | ❌ | ✅ |
| Graceful degradation | ❌ | ✅ |
| Structured schemas | ❌ | ✅ |
| Validation scripts | ❌ | ✅ |
| Platform adapters | ❌ | ✅ |

---

## After Migration Checklist

- [ ] SKILL.md loads correctly
- [ ] YAML frontmatter parses correctly
- [ ] All reference files accessible via new paths
- [ ] Capability negotiation detects correct mode
- [ ] Hard gates enforced same as before
- [ ] Output quality matches v3.7 baseline
- [ ] Same test cases pass
- [ ] Platform-specific behavior unchanged
- [ ] Progressive disclosure works (references load on demand)
- [ ] No fabricated capabilities reported

---

## Need Help?

1. Check the adapter file for your platform in `adapters/`
2. Run `scripts/validate_skill.py` to check structure
3. Review `tests/portability/portability-audit.md` for test cases
