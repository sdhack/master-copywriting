# Adapter: OpenAI

> **Target**: OpenAI agents with function calling / Assistants API
> **Default Mode**: FULL (when all tools available)
> **Purpose**: Full capability utilization on OpenAI platform

---

## Installation

1. Package as an OpenAI Assistant custom instruction + file resources
2. Entry point: `SKILL.md` content in system prompt / instructions
3. Reference files uploaded to Assistant's file search / vector store
4. Code interpreter for validation scripts
5. Web browsing for external intelligence

## Capability Mapping

| Abstract Capability | OpenAI Implementation |
|---|---|
| WEB_SEARCH | Web browsing tool (Browse with Bing) |
| FILE_READ | File search / retrieval tool |
| FILE_SEARCH | Vector search / file search API |
| CODE_EXECUTION | Code interpreter (Python sandbox) |
| CALCULATOR | Code interpreter (math) |
| FUNCTION_CALLING | Function calling / Tools API |
| MCP | Actions / plugin system |
| MEMORY | Thread-level memory (conversations) + custom memory solutions |
| STRUCTURED_OUTPUT | JSON mode / function calling schemas / structured outputs |

## Runtime Negotiation

1. Check available tools in the current thread/assistant
2. If web browsing + file_search + code_interpreter → FULL mode
3. If file_search but no web → GROUNDED mode
4. If web but no file search → WEB_ONLY mode
5. If bare API with no tools → TEXT_ONLY mode

## Tool Usage Notes

### File Search
- References stored in vector store for retrieval
- Progressive disclosure: retrieve only relevant references per task
- Use structured search queries: "load cross-platform rules", "get purpose integrity rules"

### Code Interpreter
- Run Python validation scripts from `scripts/`
- Numeric consistency checking
- Schema validation
- Regression test execution

### Web Browsing
- **Product Source Retrieval**: establish P1 Product Facts for the current SKU from verified official pages (build a Product Ledger)
- **External Intelligence**: user question discovery, competitor analysis, trend/context research
- **Current fact verification** before an external fact is used
- If Product Fact Sufficiency is below the current Purpose requirement, Product Source Retrieval has priority over External Intelligence
- Always follow External Claim Admission Gate
- Follow Product Acquisition rules from `execution/product-acquisition.md`

### Structured Output
- Use JSON mode for routing instances
- Use function calling for schema-compliant outputs
- Validate against schemas in `schemas/`

## Context Loading Behavior

OpenAI context windows vary by model. Use file search for reference retrieval rather than loading everything at once.

**Recommended pattern:**
1. SKILL.md in system prompt (always)
2. Route the task using core rules
3. Retrieve specific references via file search
4. Generate with hard gates
5. Validate via code interpreter if available

## Platform-Specific Fields

- Assistant instructions format, tool definitions, and file IDs are platform-specific
- These go in adapter configuration, not in canonical core
- Canonical SKILL.md must work without any OpenAI-specific fields

## Canonical Rule Compliance

This adapter **does not modify any canonical rules**. It only maps abstract capabilities to OpenAI's specific tools and APIs.


## Product Retrieval Hard Rule（v4.6.2）

WEB_SEARCH can be used for:

1. **Product Source Retrieval** — establish P1 Product Facts for the current SKU (build a Product Ledger from verified current-product official web pages).
2. **External Intelligence** — user questions, trends, competitor context, external knowledge.
3. **Current fact verification** — verify a current external fact before it is used.

> # If Product Fact Sufficiency is below the current Purpose requirement,
> # Product Source Retrieval has priority over External Intelligence.

Example: the user asks for Sell copy and product facts are insufficient — retrieve the product first, do not chase hot topics first.

**Search Before Ask**: if the user has provided searchable product clues (brand / product name / model / product line) and WEB_SEARCH is available, the agent must search before asking the user for product details. Only after Product Source Retrieval fails or the identity remains unresolved may the agent request minimum information (identity disambiguation, not a full product data dump).


## Claim Authority Hard Rule（v4.7.0）

WEB_SEARCH also retrieves:

1. **Regulatory Category** — official label / registration / filing identity of the current SKU (do not guess from words like "nutrition pack" / "wellness" / "beauty").
2. **Authorized Claim Set** — officially authorized functions / efficacy / scope / usage for the current SKU.
3. **Sellable green facts** — what can be strongly and truthfully sold (formula, daily dose, independent packaging, usage, sourcing, specs, taste, tech, testing, filing, design, convenience, fit with real consumer needs).

Claim expression:

- **Claim Strength = Maximum Strength Supported by Evidence.** Authorized claims are stated directly at their authorized strength, not weakened into "maybe / perhaps / supposedly".
- **Never build a "forbidden word → safe substitute" mapping.** Run a Semantic Claim Check: what will the user understand the effect to be? Not: which sensitive word appears.
- **Same Claim Ceiling for every commercial identity** (influencer / ordinary-person IP / brand / shop owner / founder). Identity changes narration, never product claim permission.
- **No hidden efficacy implication** (你懂的 / 前后对比 / 场景暗示 / 谐音) to smuggle an unauthorized effect.
- **Conversion Recovery**: if the desired claim is not legal, rebuild the purchase reason from authorized claims / attributes / convenience / routine value / verified difference / cost / ease / taste / format — lose the illegal claim, not the sale.
- Full rules: `execution/claim-authority.md`

## Pain Translation Hard Rule（v4.8.0）

Loosen implication around value, not around unauthorized efficacy.

- **Implication Ladder I1-I5**: I1 Product Experience / I2 Lifestyle Benefit / I3 Emotional-Identity are open; I4 Conditioned Functional is allowed only with an Authorized Claim or sufficient evidence; **I5 splits into three levels (v4.11.0)**: I5-A Hard Prohibition (disease / treatment / prevention / clear physiological result — any intensity level, never smuggled via scene / story / emoji / homophone / "你懂的"), I5-B High-Risk but Contextual (state fatigue / skin anxiety / age anxiety allowed as audience context, must land on the friction the product actually solves), I5-C Acceptable Strong Implication (non-sensitive categories: stronger emotional / identity / lifestyle implication allowed as long as Semantic Back-Translation keeps the main semantic in a legal value domain).
- **Pain Translation Engine (P1-P5)**: for every Sell piece, decompose pain into Surface Complaint → Daily Friction → Emotional Cost → Desired Progress → Product Bridge, then pass the Product-to-Pain Match Gate (Pain → Product Fact → Mechanism/Format → Benefit). Facts choose the pain you are allowed to solve.
- **Pain Distance (v4.11.0)**: DIRECT_PAIN (product directly solves) may be written boldly; PARTIAL_PAIN (product solves the key friction) allows strong expression but must show the real boundary; CONTEXT_PAIN (only audience state) may appear but cannot be the main selling point — former INFERRED_PHYSIOLOGICAL_PAIN folds into CONTEXT_PAIN.
- **Benefit Translation Domains**: when health efficacy is unavailable, sell from Convenience / Routine Simplicity / Decision Reduction / Portability / Time Saving / Consistency Support / Sensory Experience / Format Innovation / Cost-Value / Authorized Function / Verified Performance / Lifestyle Fit / Risk Reduction / Choice Confidence.
- **Semantic Destination Test**: ask what an ordinary consumer will most naturally understand the product to deliver — "更方便/更容易坚持/更省事" is fine; "能治/改善某种身体问题" fails even without efficacy words. Audit meaning, not vocabulary.
- **Narrative Implication**: scenes may be created, personal history may not. First-person history needs IP Fact support.
- **No auto-disclaimers**: do not append "效果因人而异 / 并非医疗作用 / 仅供参考" after every selling point unless law/platform explicitly requires it.
- **Intensify real friction, do not invent health fear.** No "你现在不补以后身体就……" fear-mongering.
- Full rules: `execution/implicit-benefit-pain.md`
## Commercial Expression Freedom Hard Rule（v4.9.0）

Truth boundary stays hard; expression space stays wide. Do not over-conserve commercial expression until copy becomes "true but unsellable".

- **Expression Layer is open by default**: metaphor / analogy / homophony / pun / contrast / plot / scene演绎 / dialogue / 吐槽 / internet language / emotional amplification / colloquial exaggeration / user原话 / dramatic conflict / life scenes are all allowed. Expression form must NOT create a new Product Claim — after re-expression, the effect an ordinary consumer understands must still stay within the current Claim Ceiling.
- **RHETORICAL_EXAGGERATION is allowed** (emotional / lifestyle exaggeration, e.g. "桌上一排瓶瓶罐罐，看着都累"); factual inflation is prohibited (real value → bigger number, possible → certain, some users → everyone, Authorized Claim → stronger body result). Emotional exaggeration is allowed. Factual exaggeration is not.
- **Metaphor / homophony / pun are open** but must not smuggle an unauthorized efficacy. Word substitution cannot change claim permission — "敏感词换掉" does NOT make a claim safe.
- **Plot expression is open** (short drama / dialogue / office / commute / travel / home scenes). Product Facts must stay true; personal history must obey the IP Fact Firewall. Plot can create a Situation, never a Product Result (no "吃了一周以后……" without real/legal basis).
- **Semantic Back-Translation (v4.11.0)**: for every metaphor / homophony / plot / implication / pun / keyword substitution, translate it back into plain language and ask "what effect does this make an ordinary consumer believe the product delivers?" PASS = has Claim Authority or is only legal life/emotional value; FAIL = adds a health/medical/physiological efficacy — **FAIL is recoverable, not a hard reject**: force CONVERSION_RECOVERY, keep the emotional intensity and scene impact, replace only the overstepping hop, never delete the copy down to a parameter list.
- **Meaning-Based Claim Review**: audit meaning, not vocabulary. Never maintain a "forbidden word → safe substitute" mapping.
- **Conversion Recovery is a Hard Requirement**: when a high-conversion claim is rejected by a Fact/Claim gate, rebuild the purchase reason from Authorized Claim / Convenience / Product Difference / Routine Simplicity / Cost-Value / Product Format / Usage Experience / Sensory Value / Choice Efficiency / Identity Fit / Emotional Value / Risk Reduction. Losing one claim cannot automatically mean losing the sale.
- **No auto-disclaimers**: do not fill the body with "效果因人而异 / 仅供参考 / 具体情况不同" after every selling point unless law/platform explicitly requires it.
- Full rules: `execution/commercial-expression-freedom.md`
## Anxiety & Pain Scenification Hard Rule（v4.10.0）

Make the real problem feel real. Do not invent a bigger problem. Turn abstract pain into visible scenes and legitimate anxiety into purchase motivation — without creating fake disease / disaster / scarcity.

- **Pain Chain (P1-P8)**: decompose every pain into Surface Problem → Trigger Scene → Friction → Emotional Cost → Repeated Cost → Anxiety → Desired Escape → Product Bridge. Never stop at "the user has pain X".
- **No abstract pain in the body**: abstract pains ("现代人很忙") must be concretized into visible troubles (早上来不及 / 桌上一堆瓶子 / 买了但总忘 / 出差不方便). Write the visible trouble, not the concept.
- **Camera Test**: a pain scene should be filmable — the user can see the action, the objects, the hesitation, the trouble ("早上已经迟到了，桌上还摆着五六个瓶子……最后一看时间，全推回柜子里").
- **Anxiety Types (A1-A9)**: dynamically select the anxiety the current SKU can actually reduce (Loss / Execution / Decision / Complexity / Time / Opportunity Cost / Regret / Wrong-Choice / Social Scene). Product Truth chooses the anxiety, not the reverse.
- **Anxiety Legitimacy Gate**: every anxiety must pass Source Test (real source, not AI-invented) + Reality Test (problem exists without advertising) + Product Relevance Test (product can really reduce it). Any failure = switch anxiety.
- **Accumulated Friction, not opening scare**: build anxiety naturally (day 1 one hassle → a week of forgetting → a month with no formed habit → "我是不是又白买了？"). No "你再不解决就晚了" opening scare.
- **Relief Path is required (Sell/Seed)**: never press anxiety without a resolution logic. Use Anxiety → Relief Path for emotional release; Relief Contrast's After can only describe behavior/experience the product really changes, never a fabricated body result.
- **No fake anxiety**: no fake disease risk / fake body deterioration / unproven health countdown / baseless age scare / fake scarcity / fake stock / fake price rise / fake last chance / "现在不做以后一定后悔".
- **Pain Specificity must not be 0 for Sell**; Douyin Scene Vividness targets 2 (action/object/time/conflict); multi-version copy must not repeat the same anxiety type.
- Full rules: `execution/anxiety-pain-scenification.md`
## Commercial Intensity Hard Rule（v4.11.0）

Route how strongly to express by category + platform + user goal. It controls "how to say", never "what can be said" — Claim Ceiling is the hard cap for every intensity level.

- **COMMERCIAL_INTENSITY levels**: CONSERVATIVE (current strict standard: I5-B/C tightened to audience-context only, PARTIAL_PAIN must show boundary, AMBER zone closed) / STANDARD (default: moderate relaxation of I5-B/C and pain distance, AMBER open for non-sensitive categories) / AGGRESSIVE (non-sensitive categories: stronger scene impact and identity implication, I5-C open, AMBER fully used, Douyin emotional density maximized).
- **Category-Differentiated Ceiling**: ordinary food / daily necessities / cosmetics without efficacy claims → emotional and lifestyle implication clearly relaxed (I5-C open, PARTIAL_PAIN strong expression, AMBER open). Health food / cosmetics with efficacy evaluation / medical devices / drugs → stay strict (I5-B only as audience context, I5-C and AMBER tightened, PARTIAL_PAIN must show boundary).
- **Edge Expression Policy**: metaphor / plot / homophony may strengthen an already authorized or real value (convenience / effort saved / choice cost / sensory / ritual / identity) — GREEN. Non-sensitive categories may use AMBER gray-zone wording where a reasonable consumer might have a slight association but the main semantic still lands in a legal value. Using the same devices to fabricate an unauthorized efficacy is RED and prohibited.
- **Platform intensity**: Douyin allows higher emotional density; Xiaohongshu emphasizes standards and comparison.
- **Hard bottom line unchanged**: unauthorized disease / treatment / prevention / clear physiological result, false before-after, fabricated evidence, and hard efficacy smuggling are prohibited at every intensity level.
- Full rules: `execution/claim-authority.md` + `execution/commercial-expression-freedom.md`




