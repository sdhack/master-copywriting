# Capability Matrix

> Maps abstract capabilities to runtime modes and adapter implementations.

---

## Runtime Modes

| Mode | WEB_SEARCH | FILE_READ | FILE_SEARCH | CODE_EXECUTION | MCP | MEMORY | STRUCTURED_OUTPUT |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **FULL** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **GROUNDED** | ❌ | ✅ | ✅ | ❌/✅ | ❌/✅ | ❌/✅ | ✅ |
| **WEB_ONLY** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **TEXT_ONLY** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## Graceful Degradation by Capability

### Without WEB_SEARCH

- **Turn off**: Real-time External Intelligence, trend-based angles, competitor research
- **Keep**: All writing logic, product-fact-based angles, all platforms, all purposes
- **Must not**: Fabricate trends, user questions, competitor data, market prices
- **Fallback**: Use only provided product/IP facts + in-memory category knowledge labeled as general pattern

### Without FILE_READ (WEB_ONLY mode)

- **Turn off**: Local reference file loading, local Product Skill/IP Profile reading
- **Keep**: WEB_SEARCH for Product Source Retrieval (build a Product Ledger from verified official web pages) + External Intelligence + all writing logic
- **Must not**: Claim to have loaded local references that weren't read
- **Fallback**: Use SKILL.md canonical core + Product Ledger from web retrieval + any references provided inline by user
- **WEB_ONLY ≠ user-provided-facts-only**: WEB_SEARCH can retrieve public product facts itself

### Without CODE_EXECUTIONUTION

- **Turn off**: Automated regression testing, numeric consistency scripts, schema validation
- **Keep**: All writing logic, manual numeric checking
- **Must not**: Simulate code execution results
- **Fallback**: Conservative numeric claims; reduce calculation complexity; mark calculations as approximate

### Without MCP

- **Turn off**: MCP-based product/IP fact sources, MCP-based research
- **Keep**: All writing logic, web search, file-based sources
- **Must not**: Fabricate MCP connections or data
- **Fallback**: User-provided facts, file-based sources, web research

### Without MEMORY

- **Turn off**: Cross-conversation content repetition check, long-term IP asset tracking
- **Keep**: Current-session diversity checks, all writing logic
- **Must not**: Claim to remember things from previous conversations that weren't referenced
- **Fallback**: Session-level repetition check only; explicit user-provided history

### Without STRUCTURED_OUTPUT

- **Turn off**: Schema-validated routing instances, structured research briefs
- **Keep**: All writing logic, all gates (implemented as prose checks)
- **Must not**: Output fake JSON or structured data that isn't validated
- **Fallback**: Markdown-based routing, manual QA checklists

---

## Adapter Capability Mapping

| Adapter | WEB_SEARCH | FILE_READ | FILE_SEARCH | CODE_EXECUTION | MCP | MEMORY | STRUCTURED_OUTPUT | Default Mode |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| generic | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | TEXT_ONLY |
| claude | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | FULL |
| openai | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | FULL |
| gemini | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | FULL |
| copilot | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | FULL |
| limited-agent | ❌/✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | TEXT_ONLY → WEB_ONLY |

---

## Capability Discovery Flow

1. On skill activation, probe for each abstract capability
2. Map discovered capabilities to the highest runtime mode
3. Announce mode to user (silently or explicitly, depending on adapter convention)
4. Gracefully degrade features that require missing capabilities
5. Never pretend a capability exists when it doesn't

### Probing methods

- **FILE_READ**: Try to read a known reference file → success = exists
- **WEB_SEARCH**: Adapter-specific (function list / tool manifest / trial search)
- **CODE_EXECUTIONUTION**: Adapter-specific (code interpreter flag / runtime check)
- **MCP**: Check MCP server list
- **MEMORY**: Adapter-specific (memory tool presence)
- **STRUCTURED_OUTPUT**: Adapter-specific (JSON mode / function calling support)
