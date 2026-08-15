# Master Copywriting Skill v4.6.2

> Full-stack copywriting decision & generation system. Cross-agent portable.

**One Canonical Brain. Many Agent Bodies.**

同一套规则，不同Agent根据自己的工具、上下文和执行环境发挥最大能力。

---

## Quick Start

### For any agent (Standard Package)

1. Read `SKILL.md`
2. Follow the router to determine task type
3. Load references as needed (progressive disclosure)
4. Follow the execution order
5. Apply hard gates before output

### For high-capability agents (Agentic Package)

1. Read `SKILL.md`
2. Run capability negotiation (detect available tools)
3. Set runtime mode (FULL / GROUNDED / WEB_ONLY / TEXT_ONLY)
4. Load schemas for structured I/O
5. Use validation scripts for QA
6. Run regression tests after changes

---

## Architecture

```
Canonical Core (SKILL.md)
├── Capability Negotiation → Runtime mode detection
├── Router → Task classification
├── Execution Order → Step-by-step workflow
├── Hard Gates → 10-level gate system
└── Progressive Disclosure → Reference loading map

References/ (Single Source of Truth)
├── modes/ (24 modes, platforms)
├── angle/ (dynamic angles, natural depth)
├── external/ (external intelligence)
├── cross-platform/ (re-conception protocol)
├── execution/ (hard gates, purpose, expression authority)
├── quality/ (anti-patternization, length engine, final output)
├── account/ (account-level system)
└── craft/ (hooks, formulas, examples, CTA)

Adapters/ (Platform-specific, no rule changes)
├── generic (markdown-only baseline)
├── claude
├── openai
├── gemini
├── copilot
└── limited-agent

Schemas/ (Structured I/O for high-capability agents)
├── product-facts.schema.json
├── ip-facts.schema.json
├── route-instance.schema.json
├── research-brief.schema.json
└── content-fingerprint.schema.json
```

---

## Runtime Modes

| Mode | Capabilities | Use Case |
|---|---|---|
| **FULL** | Web + Files + Code + MCP + Memory + Structured | High-end agent, full system |
| **GROUNDED** | Files + Structured (no web) | Workspace agent, no internet needed |
| **WEB_ONLY** | Web + Structured (no files) | Search-capable chat agent |
| **TEXT_ONLY** | Markdown only | Basic agent, safe baseline |

---

## Installation

### Claude
1. Copy skill folder to Claude skills directory
2. Skill auto-loads via SKILL.md
3. See `adapters/claude.md` for details

### OpenAI / Assistants API
1. Upload SKILL.md + references as files
2. Configure file search + code interpreter + web browsing
3. See `adapters/openai.md` for details

### Gemini
1. Add SKILL.md to system instructions
2. Upload references to Drive
3. Enable Google Search + code execution
4. See `adapters/gemini.md` for details

### Copilot / VS Code
1. Place folder in workspace
2. Skill accessible via Copilot Chat
3. See `adapters/copilot.md` for details

### Generic / Any agent
1. Just read SKILL.md
2. Works with any markdown-capable agent
3. See `adapters/generic.md` for details

---

## Distribution Packages

### Standard Package
- `SKILL.md`
- `references/`
- `assets/`

Works with any markdown-capable agent. No dependencies.

### Agentic Package
- Everything in Standard
- `adapters/`
- `schemas/`
- `tests/`
- `scripts/`

For high-capability agents with tool use, code execution, and structured output.

---

## Versioning

Semantic Versioning:
- **Major**: Canonical behavior changes
- **Minor**: New capabilities / platform adapters
- **Patch**: Rule fixes, fact gate fixes

See `CHANGELOG.md` for version history.

---

## License

Internal use.
