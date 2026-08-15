# Master Copywriting Skill v4.14.0

> **One Canonical Brain. Many Agent Bodies.**
> _Cross-agent portable copywriting decision & generation system — writes platform-native, purpose-aligned, fact-integrity copy across any LLM agent._

[![Version](https://img.shields.io/badge/version-4.14.0-6B46C1?style=flat-square)]()
[![Agents](https://img.shields.io/badge/agents-CLAUDE%20|%20OpenAI%20|%20Gemini%20|%20Copilot-10B981?style=flat-square)]()
[![Platforms](https://img.shields.io/badge/platforms-%E6%8A%96%E9%9F%B3%20%7C%20%E5%B0%8F%E7%BA%A2%E4%B9%A6%20%7C%20%E8%A7%86%E9%A2%91%E5%8F%B7%20%7C%20%E5%85%AC%E4%BC%97%E5%8F%B7-3B82F6?style=flat-square)]()
[![Modes](https://img.shields.io/badge/modes-24%20writing%20modes-F59E0B?style=flat-square)]()
[![Status](https://img.shields.io/badge/status-production-EF4444?style=flat-square)]()

---

## What Makes This Different

Not a prompt library. Not a template collection. **A single-source-of-truth writing intelligence layer** that drives any agent to produce consistent, platform-native, high-conversion copy — from the same product facts.

| vs. | Typical Approach | This Skill |
|---|---|---|
| **Consistency** | Each agent writes differently | 1 canonical brain, N agent bodies |
| **Platform Fit** | Generic templates | 4 platform-specific engines + 2026 viral content map |
| **Compliance** | Manual review | 10-level hard gate system, auto-filter |
| **CTA Control** | "Buy now" everywhere | 4-tier implicit-only permission system |
| **Portability** | Claude-only | 6 adapters, from FULL to TEXT_ONLY |
| **Quality** | Subjective review | Regression tests, fingerprint validation |

---

## Architecture

```
Canonical Core (SKILL.md)
├── Capability Negotiation → Runtime mode detection
├── Router → 24-mode task classification
├── Execution Order → Step-by-step workflow
├── Hard Gates → 10-level gate system
└── Progressive Disclosure → Reference loading map

References/ (Single Source of Truth)
├── modes/ (24 modes, platforms, 2026 viral-content-map)
├── angle/ (dynamic angles, natural depth)
├── external/ (external intelligence)
├── cross-platform/ (re-conception protocol)
├── execution/ (hard gates, purpose, expression authority)
├── quality/ (anti-patternization, length engine, final output)
├── account/ (account-level system)
├── craft/ (hooks, formulas, examples, CTA)
└── templates/ (output-templates — mandatory enforcement)

Adapters/ (Platform-specific, no rule changes)
├── generic (markdown-only baseline)
├── claude / openai / gemini / copilot / limited-agent

Schemas/ (Structured I/O for high-capability agents)
├── product-facts.schema.json
├── ip-facts.schema.json
├── route-instance.schema.json
├── research-brief.schema.json
└── content-fingerprint.schema.json
```

---

## Key Innovations

### v4.14.0 — Template Enforcement (Latest)
- **Mandatory Output Templates**: Every copy output auto-fills into structured table templates
- **Auto File Generation**: Creates `{Platform}-{Product}-{Action}-{YYMMDDHHMM}.md` files on delivery
- **3 Template Types**: Single-version, Multi-version, Multi-platform

### v4.13.0 — 2026 Viral Content Map
- **3 Cross-Platform Viral Rules**: Emotion-first, Authenticity over polish, Trust+Scenario commerce
- **4 Platform Viral Playbooks**: Algorithm-specific content types, distribution mechanics, e-commerce strategies
- **Empirical Data Layer**: Cross-referenced from 8 authoritative 2026 reports

### v4.12.0 — Full Implicit Close Revolution
- **Zero-Command CTA**: All 5 CTA families default to IMPLICIT_CLOSE — no action words, no destinations, no time limits
- **6-Point Close Audit**: Every closing line must pass a framework check before output
- **Closed Allowlist**: Only an explicit allowlist can unlock explicit CTA

### v4.11.x — Gate System & Compliance
- **10-Level Hard Gate System**: From product fact integrity to platform compliance
- **AI Style Score**: Detects LLM-typical patterns, auto-humanizes when >35
- **E-commerce Compliance Engine**: 2104 rules across 17 industries, 7 platforms

---

## Runtime Modes

| Mode | Capabilities | Use Case |
|---|---|---|
| **FULL** | Web + Files + Code + MCP + Memory + Structured | High-end agent, full system |
| **GROUNDED** | Files + Structured (no web) | Workspace agent, no internet |
| **WEB_ONLY** | Web + Structured (no files) | Search-capable chat agent |
| **TEXT_ONLY** | Markdown only | Basic agent, safe baseline |

Auto-detected via capability negotiation. No manual config needed.

---

## Distribution Packages

### Standard Package
`SKILL.md` + `references/` + `assets/` — works with any markdown-capable agent. Zero dependencies. **~252 KB (v4.14.0)**

### Agentic Package
Standard + `adapters/` + `schemas/` + `tests/` + `scripts/` — for high-capability agents with tool use, code execution, and structured output. **~412 KB (v4.14.0)**

---

## Quality Assurance

```
validate_skill.py     → 0 errors (v4.14.0)
run_regression.py     → 102/102 passed
build_package.py      → standard + agentic
content-fingerprint   → format compliance
```

---

## Installation

### Claude
Copy skill folder to Claude skills directory. Auto-loads via `SKILL.md`. See `adapters/claude.md`.

### OpenAI / Assistants API
Upload `SKILL.md` + references as files. Enable file search + code interpreter. See `adapters/openai.md`.

### Gemini
Add `SKILL.md` to system instructions. Upload references to Drive. Enable Google Search. See `adapters/gemini.md`.

### Copilot / VS Code
Place folder in workspace. Accessible via Copilot Chat. See `adapters/copilot.md`.

### Any Agent
Just read `SKILL.md`. Works with any markdown-capable LLM. See `adapters/generic.md`.

---

## By the Numbers

| Metric | Value |
|---|---|
| Versions shipped | 14+ (v4.0.0 → v4.14.0) |
| Platform engines | 4 (抖音 / 小红书 / 视频号 / 公众号) |
| Writing modes | 24 |
| Compliance rules | 2104 |
| Reference files | 30+ |
| Agent adapters | 6 |
| Regression tests | 102 |
| CTA families | 5 (all implicit by default) |

---

## Versioning

**Semantic Versioning:**
- **Major**: Canonical behavior changes
- **Minor**: New capabilities / platform adapters
- **Patch**: Rule fixes, fact gate fixes

[Full Changelog](CHANGELOG.md) · [Migration Guide](MIGRATION.md)

---

## License

Internal use. 

---

_同一套规则，不同 Agent 根据自己的工具、上下文和执行环境发挥最大能力。_
