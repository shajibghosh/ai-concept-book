# The Modern AI Concept Book

*Edition 2 · September 2026 · current to September 20, 2026*

LLMs, VLMs, agents, harnesses, hardware and the practice of AI engineering. 173 concepts · 430 dated resources. See [README.md](README.md) for other formats and browse-by indexes.

## Contents

1. [The Frontier Landscape (September 2026)](#1-the-frontier-landscape-september-2026) (5)
2. [Agents and Harnesses](#2-agents-and-harnesses) (14)
3. [Protocols and Interoperability Standards](#3-protocols-and-interoperability-standards) (12)
4. [Agentic Coding and Developer Workflow](#4-agentic-coding-and-developer-workflow) (8)
5. [Context, Memory and Retrieval](#5-context-memory-and-retrieval) (10)
6. [Reasoning and Post-Training](#6-reasoning-and-post-training) (12)
7. [Model Architectures](#7-model-architectures) (13)
8. [Training at Scale and Fine-Tuning](#8-training-at-scale-and-fine-tuning) (10)
9. [Inference and Serving](#9-inference-and-serving) (9)
10. [Quantization and Number Formats](#10-quantization-and-number-formats) (7)
11. [AI Hardware, Interconnect and Datacenter Standards](#11-ai-hardware-interconnect-and-datacenter-standards) (17)
12. [Vision-Language and Multimodal Models](#12-vision-language-and-multimodal-models) (10)
13. [Embodied AI, World Models and Generative Media](#13-embodied-ai-world-models-and-generative-media) (8)
14. [Evaluation and Benchmarks](#14-evaluation-and-benchmarks) (11)
15. [Safety, Security, Interpretability and Governance](#15-safety-security-interpretability-and-governance) (15)
16. [Roles, Deployment and AI Engineering Practice](#16-roles-deployment-and-ai-engineering-practice) (8)
17. [Keep Learning: Curated Resources](#17-keep-learning-curated-resources) (4)

---

## 1. The Frontier Landscape (September 2026)

> A snapshot of where frontier and open-weight models stand as of September 2026. This chapter dates quickly; use the trackers at the end to stay current.

**In this chapter:** [Mythos-class tier and trusted access](#mythos-class-tier-and-trusted-access) · [GPT-6 Astra and the Critical cyber threshold](#gpt-6-astra-and-the-critical-cyber-threshold) · [Tiered access for dual-use models](#tiered-access-for-dual-use-models) · [Open-weight frontier models](#open-weight-frontier-models) · [Model release trackers](#model-release-trackers)

---

### Mythos-class tier and trusted access

`Fable / Mythos` · **New in 2026** · Emerged 2026 · Beginner · Enterprise, Security

Anthropic introduced a capability tier above Opus. The same underlying model ships in two forms: Claude Fable for general use with extra safeguards in biology, cybersecurity and LLM R&D, and Claude Mythos for vetted defenders and partners through Project Glasswing.

**Key points**

- Mythos Preview (April 2026) was first restricted to trusted organisations for cyber defense.
- Fable 5 / Mythos 5 launched June 9, 2026; access was suspended June 12 to comply with US export controls and restored July 1 after the controls were lifted.
- Fable 5.1 and Mythos 5.1 followed on September 1, 2026, with 1M-token context.

> [!NOTE]
> **State of the art, Sept 2026:** Fable 5.1 is Anthropic's generally available flagship; Opus 5 (July 2026) and Sonnet 5 sit below it.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) |
| Docs | 2026 | [Anthropic statement on Fable and Mythos access](https://www.anthropic.com/news/fable-mythos-access) |
| Blog | 2026 | [DataNorth: Claude Fable 5 and Mythos 5 explained](https://datanorth.ai/news/anthropic-releases-claude-fable-5-and-mythos-5) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### GPT-6 Astra and the Critical cyber threshold

`GPT-6` · **New in 2026** · Emerged 2026 · Beginner · Security, Enterprise

OpenAI's first GPT-6 generation model, released September 3, 2026. It is the first model OpenAI classified at the Critical cybersecurity level of its Preparedness Framework, so it launched in phases with stronger safeguards and a trusted-access program for defenders.

**Key points**

- Critical means the model can find and exploit unknown vulnerabilities in hardened systems without step-by-step human guidance.
- Public versions refuse advanced offensive tasks; vetted defenders get more through OpenAI's trusted-access programs.
- Its system card also reported reduced chain-of-thought monitorability, a notable safety signal.

> [!NOTE]
> **State of the art, Sept 2026:** GPT-6 Astra sits above the GPT-5.6 Sol / Terra / Luna tiers.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [OpenAI: Path to Astra](https://openai.com/index/path-to-astra/) |
| Docs | 2026 | [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) |
| Blog | 2026 | [OpenAI: Safety overview of GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/) |
| Blog | 2026 | [InfoQ: Astra is first model rated Critical for cyber](https://www.infoq.com/news/2026/09/gpt-6-astra-critical-cyber/) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### Tiered access for dual-use models

`trusted access` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Security, Enterprise

A 2026 industry pattern: the most cyber-capable models are released in a public version with guardrails and a restricted version for vetted security teams and critical-infrastructure operators.

**Key points**

- Anthropic (Glasswing), OpenAI (trusted access for cyber) and Google (defender-only cyber variants) all adopted versions of it.
- It lets defenders patch vulnerabilities before equivalent capabilities spread.
- Enterprises now need to track which model variant, safeguards and data-retention terms they are using.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) |
| Blog | 2026 | [CSO Online: Astra crosses the Critical cyber threshold](https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### Open-weight frontier models

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights, Cost & efficiency

Open-weight models trail the closed frontier by months, not years. 2026's leading families are mostly large sparse MoEs with 1M-token context and permissive licences.

**Key points**

- DeepSeek V4 (April 2026): Pro has 1.6T total / 49B active parameters, Flash has 284B / 13B, both with 1M context, MIT licence.
- Other active families: Qwen 3.x, Kimi, GLM-5.x, MiniMax, Mistral Large 3, NVIDIA Nemotron 3, Google Gemma 4.
- Open weight does not always mean open source: check licence terms and whether data and code are released.

> [!NOTE]
> **State of the art, Sept 2026:** DeepSeek V4 is the reference open model for long-context efficiency; small open models now run strong coding workloads on a single GPU.

| Type | Year | Resource |
|---|---|---|
| Paper | 2026 | [DeepSeek-V4 technical report](https://arxiv.org/abs/2606.19348) |
| Blog | 2026 | [HF blog: DeepSeek V4 architecture analysis](https://huggingface.co/blog/ResterChed/deepseek-v4-ga-architecture) |
| Docs | 2016 | [Hugging Face models hub](https://huggingface.co/models) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### Model release trackers

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Production practice

In 2026 frontier labs shipped new models every few weeks. Trackers and independent benchmark aggregators are the practical way to keep up.

**Key points**

- Compare on your own evals, not headline benchmarks.
- Watch pricing changes as closely as capability changes: cache-read and small-tier prices fell sharply in 2026.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Artificial Analysis](https://artificialanalysis.ai) |
| Docs | 2024 | [Epoch AI benchmarking hub](https://epoch.ai/benchmarks) |
| Docs | 2023 | [LMArena](https://lmarena.ai) |
| Docs | 2023 | [OpenRouter model list](https://openrouter.ai/models) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

## 2. Agents and Harnesses

> An agent is a model running in a loop: it reads context, chooses an action, calls a tool, observes the result and repeats. The industry now summarises this as Agent = Model + Harness, and most 2026 engineering effort goes into the harness.

**In this chapter:** [Agent harness](#agent-harness) · [Harness engineering](#harness-engineering) · [Managed agents: decoupling brain, hands and session](#managed-agents-decoupling-brain-hands-and-session) · [Agentic loop / ReAct](#agentic-loop--react) · [Workflows vs. agents](#workflows-vs-agents) · [Tool use / function calling](#tool-use--function-calling) · [Tool search and programmatic tool calling](#tool-search-and-programmatic-tool-calling) · [Multi-agent systems and subagents](#multi-agent-systems-and-subagents) · [Long-running and background agents](#long-running-and-background-agents) · [Computer use and browser agents](#computer-use-and-browser-agents) · [Personal agents](#personal-agents) · [Agent sandboxes](#agent-sandboxes) · [Agent frameworks and SDKs](#agent-frameworks-and-sdks) · [Durable execution and agent trajectories](#durable-execution-and-agent-trajectories)

---

### Agent harness

**Active in 2026** · Emerged 2024, last active 2026 · Beginner · Foundational, Production practice

Everything around the model that turns it into a working agent: the loop, tool definitions, permissions, sandbox, context management, memory, retries, logging and human approval gates.

**Key points**

- Two teams using the same model can get very different results purely from harness design.
- Harness setup alone can move benchmark scores by several points.
- Harnesses encode assumptions about model weaknesses, so they must be revisited when models improve.

> [!NOTE]
> **State of the art, Sept 2026:** Vendor harnesses (Claude Code, Codex, Gemini CLI) are now exposed as SDKs and managed runtimes so teams can build on them directly.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Martin Fowler: Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) |
| Blog | 2025 | [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
| GitHub | 2026 | [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Harness engineering

**New in 2026** · Emerged 2026 · Intermediate · Production practice

The discipline that followed prompt engineering and context engineering: designing environments, constraints, documentation-as-system-of-record, structural tests and feedback loops so agents do reliable work while humans steer.

**Key points**

- OpenAI described a team shipping a roughly million-line product with no hand-written code using this approach.
- Core moves: constrain what agents can do, inform them what to do, verify their work, correct mistakes, keep humans at high-stakes gates.
- Architecture rules become linters and tests the agent must pass, not wiki pages.

> [!NOTE]
> **State of the art, Sept 2026:** The term entered mainstream use in early 2026 and is now the main focus of agent engineering investment.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/) |
| Blog | 2026 | [Faros: Harness engineering guide](https://www.faros.ai/blog/harness-engineering) |
| GitHub | 2026 | [awesome-agent-harness](https://github.com/AutoJunjie/awesome-agent-harness) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Managed agents: decoupling brain, hands and session

**New in 2026** · Emerged 2026 · Advanced · Production practice, Enterprise

An architecture where the reasoning loop (brain), the sandboxes and tools that act (hands), and the append-only event log (session) are separate, replaceable services.

**Key points**

- The harness becomes stateless; containers are provisioned only when a tool needs them.
- A crash in one sandbox does not lose the session, because state lives in the log.
- Enterprises can run the hands inside their own network while the brain runs at the provider.

> [!NOTE]
> **State of the art, Sept 2026:** Anthropic launched Claude Managed Agents on this design in April 2026; Cursor's cloud agents converged on a similar three-layer split.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Anthropic: Scaling Managed Agents](https://anthropic.com/engineering/managed-agents) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Agentic loop / ReAct

`ReAct` · Established · Emerged 2022, last active 2025 · Beginner · Foundational

The basic control pattern: reason about the next step, act by calling a tool, observe the result, and loop until done.

**Key points**

- Modern models interleave thinking between tool calls natively.
- A usable coding agent loop fits in about 100 lines of code.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [ReAct paper](https://arxiv.org/abs/2210.03629) |
| Blog | 2024 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) |
| GitHub | 2025 | [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Workflows vs. agents

Established · Emerged 2024, last active 2025 · Beginner · Foundational, Production practice

Workflows run LLM calls through predefined code paths; agents let the model direct its own process. Use the simplest pattern that works.

**Key points**

- Common workflow patterns: prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser.
- Add autonomy only when the path cannot be predicted in advance.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) |
| GitHub | 2025 | [12-factor agents](https://github.com/humanlayer/12-factor-agents) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Tool use / function calling

Established · Emerged 2023, last active 2025 · Beginner · Foundational

Models emit structured calls (a tool name plus JSON arguments) that the harness executes and returns. Tool design is API design for a non-human user.

**Key points**

- Prefer few, expressive tools over many narrow ones.
- Return compact, high-signal output and actionable error messages.
- Namespacing and clear descriptions reduce wrong-tool calls.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) |
| Docs | 2024 | [Claude tool use docs](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Tool search and programmatic tool calling

`code mode` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Cost & efficiency, Production practice

Two fixes for tool overload. Tool search loads tool definitions on demand; programmatic tool calling lets the model write a script that calls many tools and returns only the final result.

**Key points**

- Cuts context use and round-trips dramatically for large tool sets.
- Deferred tool discovery and stable tool ordering also protect prompt-cache hits.

> [!NOTE]
> **State of the art, Sept 2026:** Now a standard feature in frontier harnesses; MCP servers are increasingly consumed through code rather than direct calls.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use) |
| Blog | 2025 | [Anthropic: Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) |
| Blog | 2025 | [Cloudflare: Code Mode](https://blog.cloudflare.com/code-mode/) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Multi-agent systems and subagents

`orchestrator-worker` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Production practice

A lead agent plans and delegates to subagents with their own clean context windows, then combines condensed results.

**Key points**

- Great for broad research and big codebases; costs more tokens.
- Specialised orchestrator models can route work between tools, small models and large models.

> [!NOTE]
> **State of the art, Sept 2026:** Agent teams, swarms and parallel agents in isolated worktrees are routine in 2026 coding tools.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) |
| Docs | 2025 | [Claude Code subagents](https://docs.claude.com/en/docs/claude-code/sub-agents) |
| GitHub | 2024 | [LangGraph](https://github.com/langchain-ai/langgraph) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Long-running and background agents

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

Agents that work for hours or days across many context windows, usually in the cloud while the human does something else.

**Key points**

- Rely on plan files, progress notes, git history, test gates and compaction.
- Early models showed context anxiety (wrapping up early near the limit); newer models largely don't, so harness workarounds can become dead weight.

> [!NOTE]
> **State of the art, Sept 2026:** METR's time-horizon measure keeps doubling; multi-hour autonomous runs are normal for frontier models.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) |
| Blog | 2025 | [METR: Measuring AI ability to complete long tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Computer use and browser agents

`CUA` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Production practice

Agents that operate a GUI from screenshots with mouse and keyboard actions, or drive a browser through the DOM and accessibility tree.

**Key points**

- Agentic browsers embed this directly in the browser.
- Prompt injection from web content is the main security risk.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Claude computer use tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/computer-use-tool) |
| Blog | 2025 | [OpenAI: Computer-Using Agent](https://openai.com/index/computer-using-agent/) |
| GitHub | 2024 | [browser-use](https://github.com/browser-use/browser-use) |
| GitHub | 2025 | [Playwright MCP](https://github.com/microsoft/playwright-mcp) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Personal agents

`OpenClaw` · **New in 2026** · Emerged 2026 · Beginner · Open source / open weights, Security

Always-on assistants connected to messaging apps, email, calendars and files that take real actions for a person.

**Key points**

- OpenClaw's viral open-source spread in early 2026 put millions of personal agents into daily use.
- Exposed the permission, isolation and injection problems of agents with broad personal access.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2026 | [OpenClaw](https://github.com/openclaw/openclaw) |
| Paper | 2026 | [SemaClaw: personal agents via harness engineering](https://arxiv.org/abs/2604.11548) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Agent sandboxes

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Security, Production practice

Isolated environments (containers, microVMs, V8 isolates, OS-level sandboxes) where agents run code without endangering the host.

**Key points**

- Filesystem boundaries and network egress controls are the two key levers.
- Good sandboxing reduces approval fatigue: fewer prompts, more safety.

> [!NOTE]
> **State of the art, Sept 2026:** Providers now let enterprises run agent sandboxes in their own clouds while the model runs remotely.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Anthropic sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) |
| GitHub | 2023 | [E2B](https://github.com/e2b-dev/E2B) |
| GitHub | 2024 | [Daytona](https://github.com/daytonaio/daytona) |
| GitHub | 2025 | [container-use](https://github.com/dagger/container-use) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Agent frameworks and SDKs

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights

Libraries that package the loop, tools, memory, handoffs and tracing.

**Key points**

- Vendor SDKs expose the same harness their own products use.
- Open frameworks add graphs, durable execution and multi-agent patterns.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Claude Agent SDK (Python)](https://github.com/anthropics/claude-agent-sdk-python) |
| GitHub | 2025 | [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) |
| GitHub | 2025 | [Google ADK](https://github.com/google/adk-python) |
| GitHub | 2025 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) |
| GitHub | 2024 | [Pydantic AI](https://github.com/pydantic/pydantic-ai) |
| GitHub | 2024 | [smolagents](https://github.com/huggingface/smolagents) |
| GitHub | 2023 | [CrewAI](https://github.com/crewAIInc/crewAI) |
| GitHub | 2025 | [LangChain deepagents](https://github.com/langchain-ai/deepagents) |

[↑ Back to top](#2-agents-and-harnesses)

---

### Durable execution and agent trajectories

**Active in 2026** · Emerged 2024, last active 2026 · Advanced · Production practice

Persist every step so an agent can crash, pause for approval or wait days, then resume. Trajectory logs also feed memory, evals and training.

**Key points**

- Workflow engines like Temporal are used as agent backbones.
- Libraries now normalise session transcripts from many harnesses into one format.

| Type | Year | Resource |
|---|---|---|
| Docs | 2019 | [Temporal](https://temporal.io) |
| GitHub | 2024 | [LangGraph (persistence)](https://github.com/langchain-ai/langgraph) |

[↑ Back to top](#2-agents-and-harnesses)

---

## 3. Protocols and Interoperability Standards

> Open protocols let agents, tools, apps, editors and payment systems interoperate without bespoke glue. Several now live in neutral foundations.

**In this chapter:** [Model Context Protocol](#model-context-protocol) · [MCP Apps](#mcp-apps) · [MCP Tasks](#mcp-tasks) · [Agent2Agent protocol](#agent2agent-protocol) · [Agentic AI Foundation](#agentic-ai-foundation) · [Agent Skills](#agent-skills) · [AGENTS.md](#agentsmd) · [Agent Client Protocol](#agent-client-protocol) · [AG-UI](#ag-ui) · [Agentic commerce protocols](#agentic-commerce-protocols) · [llms.txt](#llmstxt) · [OpenTelemetry GenAI conventions](#opentelemetry-genai-conventions)

---

### Model Context Protocol

`MCP` · **Active in 2026** · Emerged 2024, last active 2026 · Beginner · Open standard, Foundational

An open JSON-RPC protocol connecting AI applications (clients) to tools, resources and prompts exposed by servers. The de facto standard for tool integration across vendors.

**Key points**

- 2026-07-28 revision: stateless core (no sessions or initialize handshake), server discovery on demand, cacheable list results, header-based routing.
- Formal Extensions framework; MCP Apps and Tasks ship as extensions.
- Authorization aligned with OAuth/OIDC: issuer validation, Client ID Metadata Documents, enterprise-managed authorization.

> [!NOTE]
> **State of the art, Sept 2026:** The 2026-07-28 spec is the largest revision since launch, with a 12-month deprecation policy and SDK conformance tiers.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [MCP blog: The 2026-07-28 specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/) |
| Blog | 2026 | [MCP roadmap (Aug 2026)](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) |
| Docs | 2024 | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| GitHub | 2024 | [MCP org (SDKs, servers)](https://github.com/modelcontextprotocol) |
| Blog | 2026 | [WorkOS: What changes for agent authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### MCP Apps

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Open standard

An MCP extension that lets servers return interactive UI rendered in a sandboxed frame, so tools can show forms, charts and pickers inside the chat.

**Key points**

- Standardised as an extension in the 2026-07-28 release.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [MCP ext-apps](https://github.com/modelcontextprotocol/ext-apps) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### MCP Tasks

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Open standard

An extension for long-running work: a server can accept a job, stream progress and let the client check back or steer mid-flight.

**Key points**

- Paired with subscriptions and progress notifications for push-style updates.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [MCP release candidate notes](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### Agent2Agent protocol

`A2A` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Open standard

An open protocol under the Linux Foundation for agents from different vendors to discover each other via Agent Cards, exchange tasks and stream results.

**Key points**

- MCP is agent-to-tool; A2A is agent-to-agent.

| Type | Year | Resource |
|---|---|---|
| Spec | 2025 | [A2A protocol](https://a2a-protocol.org) |
| GitHub | 2025 | [A2A repository](https://github.com/a2aproject/A2A) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### Agentic AI Foundation

`AAIF` · **Active in 2026** · Emerged 2025, last active 2026 · Beginner · Open standard

A Linux Foundation home for vendor-neutral agent standards, founded December 2025 with MCP, AGENTS.md and goose.

**Key points**

- Neutral governance so no single vendor controls core agent standards.
- Hosts specs, reference implementations and working groups.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [aaif.io](https://aaif.io) |
| GitHub | 2025 | [goose](https://github.com/block/goose) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### Agent Skills

`SKILL.md` · **Active in 2026** · Emerged 2025, last active 2026 · Beginner · Open standard, Production practice

Folders with a SKILL.md (name, description, instructions) plus optional scripts that an agent loads only when relevant (progressive disclosure).

**Key points**

- Published as an open standard; the same skill works across agent products.
- Cheap way to package team know-how, house style and workflows.

| Type | Year | Resource |
|---|---|---|
| Spec | 2025 | [agentskills.io](https://agentskills.io) |
| GitHub | 2025 | [anthropics/skills](https://github.com/anthropics/skills) |
| Blog | 2025 | [Anthropic: Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### AGENTS.md

**Active in 2026** · Emerged 2025, last active 2026 · Beginner · Open standard

A Markdown file at the repo root telling coding agents how to build, test and follow conventions: a README for agents.

**Key points**

- CLAUDE.md plays the same role in Claude Code.

| Type | Year | Resource |
|---|---|---|
| Spec | 2025 | [agents.md](https://agents.md) |
| GitHub | 2025 | [agentsmd/agents.md](https://github.com/agentsmd/agents.md) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### Agent Client Protocol

`ACP` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Open standard

An editor-to-agent protocol similar in spirit to LSP, so any coding agent can plug into any editor.

**Key points**

- Editors act as clients; agents run as subprocesses speaking JSON-RPC.
- Lets one agent work in Zed, JetBrains, Neovim and others without per-editor plugins.

| Type | Year | Resource |
|---|---|---|
| Spec | 2025 | [agentclientprotocol.com](https://agentclientprotocol.com) |
| GitHub | 2025 | [agent-client-protocol](https://github.com/zed-industries/agent-client-protocol) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### AG-UI

Established · Emerged 2025 · Intermediate · Open standard

An event-based protocol for streaming agent state, tool calls and UI updates between backends and frontends.

**Key points**

- Streams typed events: text deltas, tool calls, state patches, human-input requests.
- Complements MCP (tools) and A2A (agents) on the user-facing side.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [AG-UI docs](https://docs.ag-ui.com) |
| GitHub | 2025 | [ag-ui](https://github.com/ag-ui-protocol/ag-ui) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### Agentic commerce protocols

`ACP, AP2, UCP, x402` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Open standard, Enterprise

Standards that let agents shop and pay for users: checkout (Agentic Commerce Protocol), verifiable payment mandates (AP2), merchant integration (UCP) and machine-to-machine payments over HTTP 402 (x402).

**Key points**

- Mandates prove the user authorised a purchase.
- x402 enables per-request payments between agents and APIs.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Agentic Commerce Protocol](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol) |
| GitHub | 2025 | [AP2](https://github.com/google-agentic-commerce/AP2) |
| Spec | 2026 | [Universal Commerce Protocol](https://ucp.dev) |
| GitHub | 2025 | [x402](https://github.com/coinbase/x402) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### llms.txt

Established · Emerged 2024, last active 2025 · Beginner · Open standard

A proposed file at a website root that gives LLMs a curated Markdown map of the site's most useful content.

**Key points**

- Plain Markdown with links and short descriptions.
- Often paired with .md versions of docs pages for clean agent reading.

| Type | Year | Resource |
|---|---|---|
| Spec | 2024 | [llmstxt.org](https://llmstxt.org) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

### OpenTelemetry GenAI conventions

`OTel GenAI` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Open standard, Production practice

Standard span and attribute names for LLM calls, tokens, tool invocations and agent steps, so traces from any framework land in any backend.

**Key points**

- Standard attributes for model name, token counts, prompts and tool calls.
- Supported by most LLMOps tools and agent SDKs.

| Type | Year | Resource |
|---|---|---|
| Spec | 2024 | [OTel GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) |

[↑ Back to top](#3-protocols-and-interoperability-standards)

---

## 4. Agentic Coding and Developer Workflow

> Software engineering was the first domain where agents became daily tools at scale. This vocabulary describes how teams now work with them.

**In this chapter:** [Coding agents](#coding-agents) · [Vibe coding](#vibe-coding) · [Agentic engineering / Software 3.0](#agentic-engineering--software-30) · [Spec-driven development](#spec-driven-development) · [Ralph loop](#ralph-loop) · [Hooks, plugins and slash commands](#hooks-plugins-and-slash-commands) · [Parallel agents with git worktrees](#parallel-agents-with-git-worktrees) · [The review bottleneck](#the-review-bottleneck)

---

### Coding agents

**Active in 2026** · Emerged 2024, last active 2026 · Beginner · Production practice, Open source / open weights

Terminal, IDE, desktop and cloud agents that read a repo, edit files, run commands and tests, and open pull requests.

**Key points**

- They differ mostly in harness, permissions and UX, not the loop itself.
- Cross-vendor plugins appeared: e.g. a Codex plugin for Claude Code.

> [!NOTE]
> **State of the art, Sept 2026:** Claude Code, Codex, Gemini CLI, Cursor, Google Antigravity and open tools like OpenHands and OpenCode are the main options in 2026.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Claude Code](https://github.com/anthropics/claude-code) |
| GitHub | 2025 | [OpenAI Codex CLI](https://github.com/openai/codex) |
| GitHub | 2025 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) |
| GitHub | 2024 | [OpenHands](https://github.com/OpenHands/OpenHands) |
| GitHub | 2025 | [OpenCode](https://github.com/sst/opencode) |
| GitHub | 2023 | [Aider](https://github.com/Aider-AI/aider) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### Vibe coding

Established · Emerged 2025 · Beginner

Coined by Andrej Karpathy: building software by describing it and accepting AI output without reading it closely. Fine for prototypes, risky for production.

**Key points**

- Useful for throwaway prototypes, personal tools and learning.
- Unreviewed code carries security and maintenance risk in production.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Karpathy's original post](https://x.com/karpathy/status/1886192184808149383) |
| Blog | 2025 | [Simon Willison: Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### Agentic engineering / Software 3.0

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

The professional counterpart to vibe coding: engineers specify intent, design constraints and review outcomes while agents write most of the code.

**Key points**

- Humans steer, agents execute.
- Prompts in English become a new kind of program (Software 3.0).

| Type | Year | Resource |
|---|---|---|
| Video | 2025 | [Karpathy: Software is changing (again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) |
| Blog | 2025 | [Anthropic: Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### Spec-driven development

`SDD` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

Write a structured spec and plan first, then let agents implement against it, keeping the spec as source of truth.

**Key points**

- Typical flow: specify, plan, break into tasks, implement, verify.
- The spec doubles as durable context for future agent sessions.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [GitHub Spec Kit](https://github.com/github/spec-kit) |
| Docs | 2025 | [Kiro](https://kiro.dev) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### Ralph loop

`Ralph Wiggum technique` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate

Running a coding agent in a simple while-loop against the same prompt and plan file until the job is done.

**Key points**

- Progress lives in files and git, not in the context window.
- Works best with strong tests so each iteration can check its own work.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Geoffrey Huntley: Ralph](https://ghuntley.com/ralph/) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### Hooks, plugins and slash commands

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

Extension points in coding agents: hooks run deterministic scripts at lifecycle events; plugins bundle commands, subagents, skills, hooks and MCP servers.

**Key points**

- Hooks enforce rules deterministically (formatters, linters, blocked commands).
- Plugins make a team's setup installable in one step.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [Claude Code hooks](https://docs.claude.com/en/docs/claude-code/hooks) |
| Docs | 2025 | [Claude Code plugins](https://docs.claude.com/en/docs/claude-code/plugins) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### Parallel agents with git worktrees

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

Run several agents at once, each in its own worktree or container, then review and merge.

**Key points**

- Each agent gets its own branch and working directory, avoiding conflicts.
- The human shifts from typing to dispatching and reviewing.

| Type | Year | Resource |
|---|---|---|
| Docs | 2015 | [git worktree docs](https://git-scm.com/docs/git-worktree) |
| GitHub | 2025 | [container-use](https://github.com/dagger/container-use) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

### The review bottleneck

**New in 2026** · Emerged 2026 · Intermediate · Production practice

When code generation gets cheap, human review becomes the constraint. Changes grow larger and harder to review, and plausible-looking AI code hides subtle bugs.

**Key points**

- Mitigations: agent reviewers, architecture rules as tests, smaller PRs, agents that exercise the app themselves.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Faros: Harness engineering and the senior engineer tax](https://www.faros.ai/blog/harness-engineering) |

[↑ Back to top](#4-agentic-coding-and-developer-workflow)

---

## 5. Context, Memory and Retrieval

> What the model sees on each call is the main lever you control at inference time: choosing, compressing and fetching the right information.

**In this chapter:** [Context engineering](#context-engineering) · [Context rot](#context-rot) · [Compaction and context editing](#compaction-and-context-editing) · [Prompt caching](#prompt-caching) · [Agent memory](#agent-memory) · [Retrieval-augmented generation](#retrieval-augmented-generation) · [Agentic search and deep research](#agentic-search-and-deep-research) · [GraphRAG](#graphrag) · [Embeddings, late interaction and Matryoshka](#embeddings-late-interaction-and-matryoshka) · [Structured outputs and constrained decoding](#structured-outputs-and-constrained-decoding)

---

### Context engineering

**Active in 2026** · Emerged 2025, last active 2026 · Beginner · Foundational, Production practice

Curating the smallest set of high-signal tokens (instructions, tools, examples, retrieved data, history) that the model needs for its next step.

**Key points**

- Successor to prompt engineering for agents.
- Techniques: just-in-time retrieval, compaction, structured notes, subagents with clean context.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) |
| Blog | 2025 | [LangChain: Context engineering for agents](https://blog.langchain.com/context-engineering-for-agents/) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Context rot

Established · Emerged 2025 · Beginner · Research frontier

Accuracy degrades as input length grows, even well within the advertised window. Long context is not free.

**Key points**

- Distractors and similar-but-wrong passages hurt more than raw length.
- Mitigate with retrieval, summarisation and subagents.

> [!NOTE]
> **State of the art, Sept 2026:** Million-token windows are standard in 2026, but focused context still usually beats more context.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Chroma Research: Context rot](https://research.trychroma.com/context-rot) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Compaction and context editing

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

Summarising or pruning old turns and stale tool results as a conversation nears the limit, so agents can keep working indefinitely.

**Key points**

- Clear old tool outputs first; they are usually the largest and least useful.
- Keep decisions, open problems and file paths in the summary.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Managing context on the Claude Developer Platform](https://www.anthropic.com/news/context-management) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Prompt caching

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Cost & efficiency, Production practice

Reusing the computed KV cache for a repeated prefix across requests to cut latency and cost.

**Key points**

- Harnesses keep prefixes stable (tool order, system prompt) so caches keep hitting.

> [!NOTE]
> **State of the art, Sept 2026:** Cache-read prices were cut steeply again in 2026, making long agent sessions much cheaper.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Claude prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Agent memory

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Production practice, Research frontier

Persisting facts, preferences and lessons beyond one context window: files the agent writes, vector or graph stores, or self-editing memory blocks.

**Key points**

- Memory quality, provenance and forgetting are now evaluated directly.
- Related to continual learning, but done outside the weights.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [Letta (MemGPT)](https://github.com/letta-ai/letta) |
| GitHub | 2024 | [mem0](https://github.com/mem0ai/mem0) |
| GitHub | 2024 | [Graphiti](https://github.com/getzep/graphiti) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Retrieval-augmented generation

`RAG` · **Active in 2026** · Emerged 2020, last active 2026 · Beginner · Foundational, Production practice

Fetch relevant documents and put them in context before generating.

**Key points**

- Modern stacks: hybrid BM25 + vector search, rerankers, contextual chunk headers, query rewriting.

| Type | Year | Resource |
|---|---|---|
| Paper | 2020 | [Original RAG paper](https://arxiv.org/abs/2005.11401) |
| Blog | 2024 | [Anthropic: Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) |
| GitHub | 2022 | [LlamaIndex](https://github.com/run-llama/llama_index) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Agentic search and deep research

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Production practice

The agent plans queries, reads pages, follows leads and synthesises a cited report over many minutes.

**Key points**

- Many teams prefer agentic grep/file search over vector RAG for code.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: Introducing deep research](https://openai.com/index/introducing-deep-research/) |
| GitHub | 2023 | [GPT Researcher](https://github.com/assafelovic/gpt-researcher) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### GraphRAG

Established · Emerged 2024, last active 2025 · Intermediate

Build a knowledge graph from a corpus, then retrieve over communities and paths to answer global questions.

**Key points**

- Entity and relation extraction with an LLM, then community summaries.
- More expensive to index than vector RAG.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [Microsoft GraphRAG](https://github.com/microsoft/graphrag) |
| GitHub | 2024 | [LightRAG](https://github.com/HKUDS/LightRAG) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Embeddings, late interaction and Matryoshka

Established · Emerged 2020, last active 2025 · Intermediate

Dense embeddings map text to vectors; late-interaction models keep per-token vectors; Matryoshka embeddings can be truncated with little loss.

**Key points**

- Choose embeddings by your domain and language, not only leaderboard rank.
- Rerankers usually give the biggest quality jump after the first retrieval.

| Type | Year | Resource |
|---|---|---|
| Docs | 2022 | [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) |
| GitHub | 2020 | [ColBERT](https://github.com/stanford-futuredata/ColBERT) |
| Paper | 2022 | [Matryoshka representation learning](https://arxiv.org/abs/2205.13147) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

### Structured outputs and constrained decoding

Established · Emerged 2023, last active 2025 · Intermediate · Production practice

Force output to match a JSON schema or grammar by masking invalid tokens during decoding.

**Key points**

- Grammar engines compile schemas into token masks for near-zero overhead.
- Guarantees valid syntax, not correct content.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [XGrammar](https://github.com/mlc-ai/xgrammar) |
| GitHub | 2023 | [Outlines](https://github.com/dottxt-ai/outlines) |
| Docs | 2024 | [OpenAI structured outputs](https://platform.openai.com/docs/guides/structured-outputs) |

[↑ Back to top](#5-context-memory-and-retrieval)

---

## 6. Reasoning and Post-Training

> Most capability gains since late 2024 came from post-training. In 2026 the recipe shifted again: many RL specialists, merged by on-policy distillation.

**In this chapter:** [Reasoning models and test-time compute](#reasoning-models-and-test-time-compute) · [Thinking budgets, adaptive thinking and effort](#thinking-budgets-adaptive-thinking-and-effort) · [RL with verifiable rewards](#rl-with-verifiable-rewards) · [Multi-teacher on-policy distillation](#multi-teacher-on-policy-distillation) · [GRPO and its successors](#grpo-and-its-successors) · [RL environments and verifiers](#rl-environments-and-verifiers) · [RLHF, DPO and preference optimization](#rlhf-dpo-and-preference-optimization) · [Constitutional AI and model specs](#constitutional-ai-and-model-specs) · [Process reward models](#process-reward-models) · [Reward hacking](#reward-hacking) · [Self-play and self-generated curricula](#self-play-and-self-generated-curricula) · [Continual learning](#continual-learning)

---

### Reasoning models and test-time compute

**Active in 2026** · Emerged 2024, last active 2026 · Beginner · Foundational

Models trained to think in long chains before answering; accuracy scales with thinking tokens, a second scaling axis beyond model size.

**Key points**

- Techniques: long chain-of-thought, self-verification, parallel sampling with voting.
- More thinking helps most on math, code and multi-step planning.

> [!NOTE]
> **State of the art, Sept 2026:** In 2026 general and reasoning lines have merged: one model decides how much to think per request.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [OpenAI: Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) |
| Paper | 2024 | [Scaling test-time compute optimally](https://arxiv.org/abs/2408.03314) |
| Paper | 2025 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Thinking budgets, adaptive thinking and effort

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Cost & efficiency, Production practice

Controls that set how much a model thinks per request, trading latency and cost for quality. Interleaved thinking lets it reason between tool calls.

**Key points**

- Low effort for chat and simple tool calls; high for hard debugging or proofs.
- Interleaved thinking helps agents adjust after each tool result.

> [!NOTE]
> **State of the art, Sept 2026:** Adjustable reasoning effort inside a conversation became a standard API feature in 2026.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [Claude extended thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) |
| Paper | 2025 | [s1: simple test-time scaling](https://arxiv.org/abs/2501.19393) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### RL with verifiable rewards

`RLVR` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Foundational

Reinforcement learning where rewards come from checkers (tests, answer matching, verifiers) instead of a learned preference model.

**Key points**

- Coined in the Tulu 3 work (2024), popularised by DeepSeek-R1.
- RL is now a large and growing share of frontier training compute.

| Type | Year | Resource |
|---|---|---|
| Paper | 2024 | [Tulu 3](https://arxiv.org/abs/2411.15124) |
| Docs | 2024 | [RLHF Book (Nathan Lambert)](https://rlhfbook.com) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Multi-teacher on-policy distillation

`MOPD` · **New in 2026** · Emerged 2026 · Advanced · Research frontier

The 2026 post-training pattern: train several domain specialists with SFT then RL, then train one general student on its own samples while minimising reverse-KL to the relevant teacher token by token.

**Key points**

- Avoids capability trade-offs from mixing math, code and agentic RL in one run.
- Specialists can be built in parallel by different teams.
- Introduced with Xiaomi MiMo, scaled to 10+ teachers by DeepSeek V4 and Nemotron 3 Ultra.

> [!NOTE]
> **State of the art, Sept 2026:** Now the default final stage in several frontier open recipes.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [RLHF Book course: Frontier post-training recipe survey](https://rlhfbook.com/teach/course/conversation-01/) |
| Blog | 2026 | [Hugging Face: Distillation in 2026](https://huggingface.co/blog/sergiopaniego/distillation-2026) |
| Blog | 2025 | [Thinking Machines: On-policy distillation](https://thinkingmachines.ai/blog/on-policy-distillation/) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### GRPO and its successors

`GRPO, DAPO, GSPO` · Established · Emerged 2024, last active 2025 · Advanced · Research frontier

Group Relative Policy Optimization drops PPO's value network and scores samples against their group. Successors fix length bias, clipping and MoE instability.

**Key points**

- Sample a group of answers per prompt; advantage = reward minus group mean.
- No critic network means less memory and simpler training.

| Type | Year | Resource |
|---|---|---|
| Paper | 2024 | [DeepSeekMath (GRPO)](https://arxiv.org/abs/2402.03300) |
| Paper | 2025 | [DAPO](https://arxiv.org/abs/2503.14476) |
| Paper | 2025 | [GSPO](https://arxiv.org/abs/2507.18071) |
| Paper | 2025 | [Dr. GRPO](https://arxiv.org/abs/2503.20783) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### RL environments and verifiers

**Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier, Enterprise

Packaged tasks plus graders used to train agents. In 2026 environments look like sandboxed replicas of enterprise software, and verifier quality is seen as the next ceiling on agent progress.

**Key points**

- Labs spend heavily on environments; a market of environment vendors has formed.
- As agents improve, verifiers must improve faster to avoid reward hacking.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Prime Intellect verifiers](https://github.com/PrimeIntellect-ai/verifiers) |
| GitHub | 2025 | [OpenEnv](https://github.com/meta-pytorch/OpenEnv) |
| GitHub | 2024 | [verl](https://github.com/volcengine/verl) |
| GitHub | 2025 | [SkyRL](https://github.com/NovaSky-AI/SkyRL) |
| Blog | 2026 | [Prolific: RL environments for agentic AI (2026 guide)](https://www.prolific.com/resources/rl-environments-for-agentic-ai-the-2026-guide-to-building-and-deploying-enterprise-rl-environments) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### RLHF, DPO and preference optimization

Established · Emerged 2022, last active 2025 · Intermediate · Foundational

Aligning outputs to human preferences with a reward model plus RL, or directly from preference pairs (DPO).

**Key points**

- RLHF: SFT, then reward model, then PPO.
- DPO optimises the same objective in closed form from preference pairs.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [InstructGPT](https://arxiv.org/abs/2203.02155) |
| Paper | 2023 | [DPO](https://arxiv.org/abs/2305.18290) |
| GitHub | 2020 | [Hugging Face TRL](https://github.com/huggingface/trl) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Constitutional AI and model specs

**Active in 2026** · Emerged 2022, last active 2026 · Intermediate

Training behaviour from a written set of principles with AI feedback. Labs now publish the documents that define model character and priorities.

**Key points**

- The model critiques and revises its own outputs against principles.
- Published specs make intended behaviour inspectable.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [Constitutional AI](https://arxiv.org/abs/2212.08073) |
| Docs | 2026 | [Claude's constitution](https://www.anthropic.com/constitution) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Process reward models

`PRM` · Established · Emerged 2023, last active 2025 · Advanced · Research frontier

Reward models that grade each reasoning step rather than only the final answer.

**Key points**

- Enable step-level search (beam search over reasoning steps).
- Expensive to label; often trained with automated step checks.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [Let's verify step by step](https://arxiv.org/abs/2305.20050) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Reward hacking

**Active in 2026** · Emerged 2016, last active 2026 · Intermediate · Security, Research frontier

The policy exploits flaws in the reward (special-casing tests, editing graders) instead of solving the task; learned hacking can generalise to broader misbehaviour.

**Key points**

- Watch for tests being deleted, asserts weakened or outputs hard-coded.
- Defenses: held-out verifiers, monitoring, diverse environments.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [Lilian Weng: Reward hacking](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) |
| Blog | 2025 | [Anthropic: Emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Self-play and self-generated curricula

Established · Emerged 2025 · Advanced · Research frontier

Models propose tasks, solve them and learn from verified results.

**Key points**

- A proposer creates tasks near the solver's frontier.
- Verification (code execution, math checkers) keeps it grounded.

| Type | Year | Resource |
|---|---|---|
| Paper | 2025 | [Absolute Zero](https://arxiv.org/abs/2505.03335) |

[↑ Back to top](#6-reasoning-and-post-training)

---

### Continual learning

**Active in 2026** · Emerged 2024, last active 2026 · Advanced · Research frontier

Updating a deployed model with new knowledge and skills without catastrophic forgetting.

**Key points**

- Approaches: replay, regularisation, architectural expansion, self-distillation, nested optimisation.
- Widely named as a key 2026 frontier for agents that improve on the job.

| Type | Year | Resource |
|---|---|---|
| Paper | 2026 | [Survey: Continual learning in LLMs (2026)](https://arxiv.org/abs/2603.12658) |
| Blog | 2025 | [Google Research: Nested learning](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/) |

[↑ Back to top](#6-reasoning-and-post-training)

---

## 7. Model Architectures

> Transformers still dominate, but 2026 models mix sparse experts, compressed and sparse attention, hybrid linear layers and new residual schemes.

**In this chapter:** [Mixture of Experts](#mixture-of-experts) · [GQA and Multi-head Latent Attention](#gqa-and-multi-head-latent-attention) · [Sparse and compressed attention](#sparse-and-compressed-attention) · [Manifold-constrained hyper-connections](#manifold-constrained-hyper-connections) · [Hybrid linear-attention and state space models](#hybrid-linear-attention-and-state-space-models) · [Diffusion language models](#diffusion-language-models) · [Multi-token prediction and speculative decoding](#multi-token-prediction-and-speculative-decoding) · [Long-context methods](#long-context-methods) · [Attention sinks](#attention-sinks) · [Tokenizer-free and byte-level models](#tokenizer-free-and-byte-level-models) · [Tiny recursive reasoning models](#tiny-recursive-reasoning-models) · [Small language models](#small-language-models) · [Architecture overviews](#architecture-overviews)

---

### Mixture of Experts

`MoE` · **Active in 2026** · Emerged 2017, last active 2026 · Beginner · Foundational, Cost & efficiency

Tokens route to a few expert feed-forward blocks out of many, so total parameters grow while compute per token stays small.

**Key points**

- Fine-grained experts plus a shared expert is the common 2026 layout.
- Expert parallelism needs fast all-to-all communication.

> [!NOTE]
> **State of the art, Sept 2026:** Frontier open models reach 1.6T to 2.8T total parameters with roughly 3% active per token.

| Type | Year | Resource |
|---|---|---|
| Blog | 2023 | [Hugging Face: MoE explained](https://huggingface.co/blog/moe) |
| Paper | 2024 | [DeepSeek-V3](https://arxiv.org/abs/2412.19437) |
| GitHub | 2025 | [DeepEP](https://github.com/deepseek-ai/DeepEP) |

[↑ Back to top](#7-model-architectures)

---

### GQA and Multi-head Latent Attention

`GQA, MLA` · Established · Emerged 2023, last active 2025 · Intermediate · Cost & efficiency

Two ways to shrink the KV cache: share keys/values across head groups (GQA) or compress them into a low-rank latent (MLA).

**Key points**

- GQA: fewer KV heads than query heads.
- MLA: store a small latent, up-project at attention time; decoupled RoPE dims.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [GQA](https://arxiv.org/abs/2305.13245) |
| Paper | 2024 | [DeepSeek-V2 (MLA)](https://arxiv.org/abs/2405.04434) |

[↑ Back to top](#7-model-architectures)

---

### Sparse and compressed attention

`NSA, DSA, CSA, HCA` · **Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier, Cost & efficiency

Attend only to selected tokens or compressed summaries of blocks to make long context cheap.

**Key points**

- DeepSeek V4 interleaves Compressed Sparse Attention (compress KV along the sequence, then top-k select) with Heavily Compressed Attention.
- Reported KV-cache reductions near 98% versus standard GQA make 1M-token inference affordable.

> [!NOTE]
> **State of the art, Sept 2026:** DeepSeek V4's CSA/HCA hybrid replaced MLA and is the most detailed public long-context design in 2026.

| Type | Year | Resource |
|---|---|---|
| Paper | 2025 | [Native Sparse Attention](https://arxiv.org/abs/2502.11089) |
| GitHub | 2025 | [DeepSeek-V3.2-Exp (DSA)](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |
| Paper | 2026 | [DeepSeek-V4 report](https://arxiv.org/abs/2606.19348) |

[↑ Back to top](#7-model-architectures)

---

### Manifold-constrained hyper-connections

`mHC` · **New in 2026** · Emerged 2026 · Advanced · Research frontier

Replaces plain residual connections with learned mixtures over several parallel residual streams, projected onto a constrained manifold to keep signals stable in very deep, very large models.

**Key points**

- Used in DeepSeek V4 to stabilise training at trillion-parameter scale.

| Type | Year | Resource |
|---|---|---|
| Paper | 2026 | [DeepSeek-V4 report](https://arxiv.org/abs/2606.19348) |

[↑ Back to top](#7-model-architectures)

---

### Hybrid linear-attention and state space models

`Mamba, Gated DeltaNet` · **Active in 2026** · Emerged 2023, last active 2026 · Advanced · Research frontier, Cost & efficiency

Mix a few full-attention layers with many linear-time layers for long context at lower cost.

**Key points**

- Linear layers keep a fixed-size state instead of a growing KV cache.
- A few full-attention layers preserve precise recall.

> [!NOTE]
> **State of the art, Sept 2026:** A leading 2026 trend: Qwen 3.x, Nemotron 3, Kimi Linear and others ship hybrids.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [Mamba](https://github.com/state-spaces/mamba) |
| GitHub | 2024 | [Gated DeltaNet](https://github.com/NVlabs/GatedDeltaNet) |
| GitHub | 2025 | [Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) |
| GitHub | 2023 | [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) |

[↑ Back to top](#7-model-architectures)

---

### Diffusion language models

`dLLM` · **Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier, Cost & efficiency

Generate text by iteratively denoising blocks in parallel rather than left to right, for much faster decoding.

**Key points**

- Start from masked or noisy tokens and refine in parallel steps.
- Trade-offs: quality on long reasoning, variable-length output.

> [!NOTE]
> **State of the art, Sept 2026:** Commercial diffusion LLMs now offer very low-cost, high-speed endpoints.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [LLaDA](https://github.com/ML-GSAI/LLaDA) |
| Docs | 2025 | [Gemini Diffusion](https://deepmind.google/models/gemini-diffusion/) |
| Docs | 2025 | [Inception Labs (Mercury)](https://www.inceptionlabs.ai) |

[↑ Back to top](#7-model-architectures)

---

### Multi-token prediction and speculative decoding

`MTP` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Cost & efficiency

Predict several tokens at once, or let a cheap draft propose tokens that the big model verifies in one pass.

**Key points**

- Draft models, extra prediction heads (MTP, Medusa, EAGLE) or n-gram lookup.
- Output distribution is unchanged when verification is exact.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [Speculative decoding](https://arxiv.org/abs/2211.17192) |
| GitHub | 2024 | [EAGLE](https://github.com/SafeAILab/EAGLE) |
| Paper | 2024 | [Multi-token prediction](https://arxiv.org/abs/2404.19737) |

[↑ Back to top](#7-model-architectures)

---

### Long-context methods

`RoPE, YaRN` · **Active in 2026** · Emerged 2021, last active 2026 · Intermediate

Rotary embeddings and scaling tricks that extend context windows; combined with sparse attention and KV compression to reach 1M tokens.

**Key points**

- Train short, extend with RoPE scaling plus long-context fine-tuning.
- Needle tests are easy; multi-hop reasoning over long input is hard.

> [!NOTE]
> **State of the art, Sept 2026:** 1M-token context is the default for 2026 frontier models.

| Type | Year | Resource |
|---|---|---|
| Paper | 2021 | [RoFormer (RoPE)](https://arxiv.org/abs/2104.09864) |
| GitHub | 2023 | [YaRN](https://github.com/jquesnelle/yarn) |

[↑ Back to top](#7-model-architectures)

---

### Attention sinks

Established · Emerged 2023, last active 2025 · Advanced · Research frontier

Models park attention on the first tokens; keeping them (or learned sink logits) stabilises long generation.

**Key points**

- Keep the first few tokens when using sliding-window caches.
- Some models add explicit sink parameters per head.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [StreamingLLM](https://arxiv.org/abs/2309.17453) |

[↑ Back to top](#7-model-architectures)

---

### Tokenizer-free and byte-level models

`BLT` · Established · Emerged 2024, last active 2025 · Advanced · Research frontier

Operate on bytes grouped into dynamic patches instead of a fixed vocabulary.

**Key points**

- Patch boundaries adapt to entropy, spending compute on hard bytes.
- Improves robustness on typos, code and rare scripts.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [Byte Latent Transformer](https://github.com/facebookresearch/blt) |

[↑ Back to top](#7-model-architectures)

---

### Tiny recursive reasoning models

`HRM, TRM` · Established · Emerged 2025 · Advanced · Research frontier

Very small networks that loop over latent state, scoring well on puzzles like ARC-AGI with a few million parameters.

**Key points**

- Iterate a small network many times on its own latent answer.
- Shows depth-through-recursion can substitute for parameters on some tasks.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Hierarchical Reasoning Model](https://github.com/sapientinc/HRM) |
| GitHub | 2025 | [Tiny Recursive Models](https://github.com/SamsungSAILMontreal/TinyRecursiveModels) |

[↑ Back to top](#7-model-architectures)

---

### Small language models

`SLM` · **Active in 2026** · Emerged 2024, last active 2026 · Beginner · Cost & efficiency, Open source / open weights

Compact models (about 0.5B to 30B) for on-device use, low latency and cheap agent subtasks.

**Key points**

- Often distilled from large teachers.
- Good fits: routing, extraction, classification, on-device assistants.

> [!NOTE]
> **State of the art, Sept 2026:** 2026 mid-size open models (around 27B) deliver frontier-like coding on a single consumer GPU.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Hugging Face: SmolLM3](https://huggingface.co/blog/smollm3) |
| Docs | 2025 | [Apple Foundation Models framework](https://developer.apple.com/documentation/foundationmodels) |

[↑ Back to top](#7-model-architectures)

---

### Architecture overviews

**Active in 2026** · Emerged 2025, last active 2026 · Beginner

Side-by-side walkthroughs of how current open models differ.

**Key points**

- Compare norms, attention type, expert counts, positional schemes.
- Read tech reports for data and training details that diagrams omit.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Raschka: The big LLM architecture comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) |
| Blog | 2026 | [Raschka: LLM research papers 2026](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1) |

[↑ Back to top](#7-model-architectures)

---

## 8. Training at Scale and Fine-Tuning

> How models are pretrained across thousands of accelerators, and how practitioners adapt them cheaply afterwards.

**In this chapter:** [Parallelism strategies](#parallelism-strategies) · [Scaling laws](#scaling-laws) · [Muon and modern optimizers](#muon-and-modern-optimizers) · [Data curation and synthetic data](#data-curation-and-synthetic-data) · [Mid-training](#mid-training) · [LoRA and parameter-efficient fine-tuning](#lora-and-parameter-efficient-fine-tuning) · [Fine-tuning toolkits and APIs](#fine-tuning-toolkits-and-apis) · [Model merging](#model-merging) · [Decentralized training](#decentralized-training) · [Build-it-yourself references](#build-it-yourself-references)

---

### Parallelism strategies

`DP, FSDP, TP, PP, EP, CP` · **Active in 2026** · Emerged 2019, last active 2026 · Advanced · Foundational

Data, fully-sharded, tensor, pipeline, expert and context parallelism split models and data across devices; real runs combine several.

**Key points**

- FSDP shards parameters, gradients and optimizer state.
- Tensor and expert parallelism need fast scale-up links; pipeline tolerates slower links.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [HF: The Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) |
| Blog | 2025 | [How to Scale Your Model (JAX)](https://jax-ml.github.io/scaling-book/) |
| GitHub | 2024 | [torchtitan](https://github.com/pytorch/torchtitan) |
| GitHub | 2019 | [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) |
| GitHub | 2020 | [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Scaling laws

**Active in 2026** · Emerged 2020, last active 2026 · Intermediate · Foundational

Empirical power laws relating loss to parameters, data and compute; now also studied for RL and test-time compute.

**Key points**

- Compute-optimal data-to-parameter ratio was roughly 20 tokens per parameter (Chinchilla).
- Inference cost now pushes teams to over-train smaller models.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [Chinchilla](https://arxiv.org/abs/2203.15556) |
| Docs | 2022 | [Epoch AI data](https://epoch.ai/data) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Muon and modern optimizers

**Active in 2026** · Emerged 2024, last active 2026 · Advanced · Research frontier

Muon orthogonalises momentum updates for matrix parameters and trains faster than AdamW at scale.

**Key points**

- Newton-Schulz iterations approximate orthogonalisation cheaply.
- Usually combined with AdamW for embeddings and norms.

> [!NOTE]
> **State of the art, Sept 2026:** Adopted in frontier open models including Kimi K2 and DeepSeek V4.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [Keller Jordan: Muon](https://kellerjordan.github.io/posts/muon/) |
| GitHub | 2025 | [Kimi K2](https://github.com/MoonshotAI/Kimi-K2) |
| GitHub | 2024 | [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Data curation and synthetic data

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate

Classifier filtering, deduplication, and synthetic textbooks, reasoning traces and agent trajectories.

**Key points**

- Quality classifiers trained on curated seed data filter web crawls.
- Synthetic data risks collapse without real-data anchoring and verification.

> [!NOTE]
> **State of the art, Sept 2026:** DeepSeek V4 pretrained on 32T+ tokens, more than double V3's corpus.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [FineWeb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) |
| Blog | 2024 | [Cosmopedia](https://huggingface.co/blog/cosmopedia) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Mid-training

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate

A stage between pretraining and post-training that shifts the mix toward code, math, long context and reasoning.

**Key points**

- Often includes long-context extension and instruction-like data.
- Sets up the base model for efficient RL later.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Allen AI OLMo](https://allenai.org/olmo) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### LoRA and parameter-efficient fine-tuning

`PEFT, LoRA, QLoRA` · Established · Emerged 2021, last active 2025 · Intermediate · Cost & efficiency

Train small low-rank adapters instead of all weights; QLoRA does it on a 4-bit base.

**Key points**

- Adapters are small files you can swap per customer or task.
- Higher ranks and all-layer adapters close most of the gap to full fine-tuning.

| Type | Year | Resource |
|---|---|---|
| Paper | 2021 | [LoRA](https://arxiv.org/abs/2106.09685) |
| Paper | 2023 | [QLoRA](https://arxiv.org/abs/2305.14314) |
| Blog | 2025 | [Thinking Machines: LoRA without regret](https://thinkingmachines.ai/blog/lora/) |
| GitHub | 2023 | [HF PEFT](https://github.com/huggingface/peft) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Fine-tuning toolkits and APIs

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights

Tools that make SFT, DPO and RL fine-tuning accessible on one GPU or as a managed API.

**Key points**

- Start with SFT on a few thousand good examples before trying RL.
- Managed APIs hide distributed training but constrain algorithms.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [Unsloth](https://github.com/unslothai/unsloth) |
| GitHub | 2023 | [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) |
| GitHub | 2023 | [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) |
| Docs | 2025 | [Tinker](https://thinkingmachines.ai/tinker/) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Model merging

Established · Emerged 2023, last active 2025 · Intermediate

Combining weights of several fine-tunes (SLERP, TIES, DARE) without further training.

**Key points**

- Works best between fine-tunes of the same base model.
- Popular for combining skills or languages cheaply.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [mergekit](https://github.com/arcee-ai/mergekit) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Decentralized training

`DiLoCo` · **Active in 2026** · Emerged 2023, last active 2026 · Advanced · Research frontier

Training across loosely connected clusters that synchronise rarely.

**Key points**

- Workers train locally for many steps, then average updates.
- Enables training across datacenters and volunteer compute.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [DiLoCo](https://arxiv.org/abs/2311.08105) |
| GitHub | 2025 | [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

### Build-it-yourself references

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights

Minimal end-to-end codebases for learning how chat models are trained.

**Key points**

- nanochat trains a small ChatGPT-like model end to end for a few hundred dollars.
- CS336 covers tokenizers, kernels, scaling and alignment from scratch.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [nanochat](https://github.com/karpathy/nanochat) |
| Docs | 2025 | [Stanford CS336](https://stanford-cs336.github.io) |

[↑ Back to top](#8-training-at-scale-and-fine-tuning)

---

## 9. Inference and Serving

> Serving cost now rivals training cost. These techniques decide tokens per second, latency and price.

**In this chapter:** [Inference engines](#inference-engines) · [KV cache and PagedAttention](#kv-cache-and-pagedattention) · [Continuous batching and prefix caching](#continuous-batching-and-prefix-caching) · [Prefill/decode disaggregation](#prefilldecode-disaggregation) · [KV cache offloading](#kv-cache-offloading) · [Attention kernels](#attention-kernels) · [On-device and edge inference](#on-device-and-edge-inference) · [LLM gateways and routers](#llm-gateways-and-routers) · [Inference benchmarking](#inference-benchmarking)

---

### Inference engines

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights, Production practice

Servers that batch requests, manage the KV cache and run optimised kernels.

**Key points**

- Pick by hardware, model support and features (disaggregation, LoRA, structured output).
- Benchmark on your own traffic shape.

> [!NOTE]
> **State of the art, Sept 2026:** vLLM and SGLang lead open serving; llama.cpp, Ollama and MLX dominate local use.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [vLLM](https://github.com/vllm-project/vllm) |
| GitHub | 2024 | [SGLang](https://github.com/sgl-project/sglang) |
| GitHub | 2023 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| GitHub | 2023 | [llama.cpp](https://github.com/ggml-org/llama.cpp) |
| GitHub | 2023 | [Ollama](https://github.com/ollama/ollama) |
| GitHub | 2023 | [MLX](https://github.com/ml-explore/mlx) |

[↑ Back to top](#9-inference-and-serving)

---

### KV cache and PagedAttention

Established · Emerged 2023, last active 2025 · Intermediate · Foundational

Keys and values of past tokens are cached; PagedAttention stores them in fixed pages like virtual memory.

**Key points**

- KV memory grows with batch size times sequence length.
- Paging enables sharing and near-zero waste.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [PagedAttention](https://arxiv.org/abs/2309.06180) |

[↑ Back to top](#9-inference-and-serving)

---

### Continuous batching and prefix caching

Established · Emerged 2022, last active 2025 · Intermediate · Cost & efficiency

Add and remove requests every step, and share cached prefixes (radix trees) across requests.

**Key points**

- Keeps GPUs busy despite requests of different lengths.
- Prefix sharing is huge for agents with long common system prompts.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [SGLang (RadixAttention)](https://github.com/sgl-project/sglang) |

[↑ Back to top](#9-inference-and-serving)

---

### Prefill/decode disaggregation

`PD disaggregation` · **Active in 2026** · Emerged 2024, last active 2026 · Advanced · Production practice, Cost & efficiency

Run compute-bound prefill and memory-bound decode on separate pools, moving KV caches between them.

**Key points**

- NVIDIA now builds separate rack types for prefill (CPX) and decode, scheduled together by Dynamo.

> [!NOTE]
> **State of the art, Sept 2026:** Standard for large-scale serving of million-token contexts in 2026.

| Type | Year | Resource |
|---|---|---|
| Paper | 2024 | [DistServe](https://arxiv.org/abs/2401.09670) |
| GitHub | 2025 | [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) |
| GitHub | 2025 | [llm-d](https://github.com/llm-d/llm-d) |
| GitHub | 2024 | [Mooncake](https://github.com/kvcache-ai/Mooncake) |

[↑ Back to top](#9-inference-and-serving)

---

### KV cache offloading

**Active in 2026** · Emerged 2024, last active 2026 · Advanced · Cost & efficiency

Spill KV caches to CPU memory, SSD or remote storage and reload them for later turns.

**Key points**

- Turns re-prefill into a memory read.
- Tiered storage: HBM, CPU DRAM, local SSD, network.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [LMCache](https://github.com/LMCache/LMCache) |

[↑ Back to top](#9-inference-and-serving)

---

### Attention kernels

`FlashAttention` · **Active in 2026** · Emerged 2022, last active 2026 · Advanced

IO-aware fused attention kernels that avoid materialising the full attention matrix.

**Key points**

- Tiling keeps data in fast on-chip SRAM.
- New versions target Hopper, Blackwell and FP8/FP4 paths.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2022 | [FlashAttention](https://github.com/Dao-AILab/flash-attention) |
| GitHub | 2023 | [FlashInfer](https://github.com/flashinfer-ai/flashinfer) |

[↑ Back to top](#9-inference-and-serving)

---

### On-device and edge inference

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Cost & efficiency

Running models on phones, laptops and embedded hardware with quantised weights and NPU runtimes.

**Key points**

- Privacy and offline use are the main drivers.
- Memory bandwidth, not compute, limits phone and laptop token rates.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [ExecuTorch](https://github.com/pytorch/executorch) |
| GitHub | 2018 | [ONNX Runtime](https://github.com/microsoft/onnxruntime) |

[↑ Back to top](#9-inference-and-serving)

---

### LLM gateways and routers

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Production practice, Cost & efficiency

One API over many providers with fallbacks, budgets, caching and routing to cheaper models.

**Key points**

- Central place for keys, rate limits, logging and cost control.
- Routers send easy prompts to cheap models.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [LiteLLM](https://github.com/BerriAI/litellm) |
| Docs | 2023 | [OpenRouter](https://openrouter.ai) |

[↑ Back to top](#9-inference-and-serving)

---

### Inference benchmarking

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Cost & efficiency

Measuring throughput, latency and cost per million tokens across hardware and software stacks.

**Key points**

- Report throughput at a fixed latency target.
- Cost per million tokens depends on batch size and cache hit rate.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [InferenceMAX](https://github.com/InferenceMAX/InferenceMAX) |
| Docs | 2024 | [Artificial Analysis](https://artificialanalysis.ai) |

[↑ Back to top](#9-inference-and-serving)

---

## 10. Quantization and Number Formats

> Lower precision is the cheapest speed-up available, and formats are increasingly standardised across vendors.

**In this chapter:** [Microscaling formats](#microscaling-formats) · [NVFP4](#nvfp4) · [FP8 training and inference](#fp8-training-and-inference) · [Post-training quantization](#post-training-quantization) · [Quantization-aware training](#quantization-aware-training) · [GGUF and local model formats](#gguf-and-local-model-formats) · [Ternary and 1-bit models](#ternary-and-1-bit-models)

---

### Microscaling formats

`MX, MXFP8, MXFP4` · **Active in 2026** · Emerged 2023, last active 2026 · Advanced · Open standard, Cost & efficiency

An Open Compute Project standard: blocks of values share one scale, making 8-, 6- and 4-bit floats accurate enough for training and inference.

**Key points**

- Shared 8-bit exponent scale per 32-element block.
- Supported by NVIDIA, AMD, Intel, Arm, Meta and Microsoft.

| Type | Year | Resource |
|---|---|---|
| Spec | 2023 | [OCP Microscaling (MX) spec](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf) |
| Paper | 2023 | [Microscaling data formats](https://arxiv.org/abs/2310.10537) |
| GitHub | 2025 | [openai/gpt-oss (MXFP4)](https://github.com/openai/gpt-oss) |

[↑ Back to top](#10-quantization-and-number-formats)

---

### NVFP4

**Active in 2026** · Emerged 2025, last active 2026 · Advanced · Cost & efficiency

NVIDIA's 4-bit float with 16-value blocks and FP8 scales, native on Blackwell and Rubin.

**Key points**

- Smaller blocks and finer scales than MXFP4 improve accuracy.
- Increasingly used for pretraining as well as inference.

> [!NOTE]
> **State of the art, Sept 2026:** Rubin rack performance is quoted primarily in FP4 exaflops.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [NVIDIA: Introducing NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/) |

[↑ Back to top](#10-quantization-and-number-formats)

---

### FP8 training and inference

`E4M3, E5M2` · **Active in 2026** · Emerged 2022, last active 2026 · Intermediate

Two 8-bit float layouts used for large-scale training and routine serving; KV caches are often stored in FP8.

**Key points**

- E4M3 for weights and activations, E5M2 for gradients.
- Needs per-tensor or per-block scaling to avoid overflow.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [FP8 formats for deep learning](https://arxiv.org/abs/2209.05433) |

[↑ Back to top](#10-quantization-and-number-formats)

---

### Post-training quantization

`GPTQ, AWQ` · Established · Emerged 2022, last active 2025 · Intermediate · Cost & efficiency

Compress trained weights to 4 or 8 bits using calibration data.

**Key points**

- 4-bit weights with 16-bit activations is the common local setup.
- Always re-run your evals after quantizing.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [GPTQ](https://arxiv.org/abs/2210.17323) |
| GitHub | 2023 | [AWQ](https://github.com/mit-han-lab/llm-awq) |
| GitHub | 2024 | [llm-compressor](https://github.com/vllm-project/llm-compressor) |

[↑ Back to top](#10-quantization-and-number-formats)

---

### Quantization-aware training

`QAT` · **Active in 2026** · Emerged 2024, last active 2026 · Advanced

Simulate low precision during training so the model tolerates it.

**Key points**

- Fake-quantize in the forward pass, keep full-precision master weights.
- Recovers much of the accuracy lost to aggressive PTQ.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [torchao](https://github.com/pytorch/ao) |

[↑ Back to top](#10-quantization-and-number-formats)

---

### GGUF and local model formats

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights

A single-file format for quantised models used by llama.cpp and local runners.

**Key points**

- K-quants (Q4_K_M, Q5_K_M) balance size and quality.
- Metadata stores tokenizer and chat template in the file.

| Type | Year | Resource |
|---|---|---|
| Spec | 2023 | [GGUF specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md) |
| GitHub | 2021 | [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) |

[↑ Back to top](#10-quantization-and-number-formats)

---

### Ternary and 1-bit models

`BitNet` · Established · Emerged 2024, last active 2025 · Advanced · Research frontier

Weights restricted to -1, 0, +1, trained from scratch for very cheap CPU inference.

**Key points**

- Matrix multiplies become additions and subtractions.
- Must be trained low-bit from the start.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [Microsoft BitNet](https://github.com/microsoft/BitNet) |

[↑ Back to top](#10-quantization-and-number-formats)

---

## 11. AI Hardware, Interconnect and Datacenter Standards

> The unit of compute is now a rack or pod. Open standards are forming to connect accelerators from different vendors.

**In this chapter:** [Rack-scale systems](#rack-scale-systems) · [AMD Helios and Open Rack Wide](#amd-helios-and-open-rack-wide) · [Scale-up vs. scale-out networking](#scale-up-vs-scale-out-networking) · [UALink](#ualink) · [ESUN and SUE](#esun-and-sue) · [Ultra Ethernet](#ultra-ethernet) · [NVLink and NVLink Fusion](#nvlink-and-nvlink-fusion) · [CXL, PCIe and UCIe](#cxl-pcie-and-ucie) · [High-bandwidth memory](#high-bandwidth-memory) · [Advanced packaging](#advanced-packaging) · [Co-packaged optics](#co-packaged-optics) · [Custom accelerators](#custom-accelerators) · [AI factories, power and cooling](#ai-factories-power-and-cooling) · [Kernel languages and compilers](#kernel-languages-and-compilers) · [Collective communication](#collective-communication) · [Model interchange formats](#model-interchange-formats) · [Hardware benchmarks](#hardware-benchmarks)

---

### Rack-scale systems

`NVL72` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Dozens of accelerators in one liquid-cooled rack joined by a single scale-up domain, behaving like one giant GPU.

**Key points**

- GB200/GB300 NVL72 (Blackwell) dominated 2025.
- Vera Rubin NVL72 (72 Rubin GPUs, 36 Vera CPUs, NVLink 6, HBM4) began shipping to major clouds in 2026.

> [!NOTE]
> **State of the art, Sept 2026:** NVIDIA quotes about 3.6 EF FP4 inference per Vera Rubin rack; Rubin Ultra (Kyber rack) is planned for H2 2027.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |
| Blog | 2026 | [ServeTheHome: Rubin platform at CES 2026](https://www.servethehome.com/nvidia-launches-next-generation-rubin-ai-compute-platform-at-ces-2026/) |
| Blog | 2026 | [DCD: Vera Rubin superchip](https://www.datacenterdynamics.com/en/news/nvidia-announces-vera-rubin-superchip-for-late-2026/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### AMD Helios and Open Rack Wide

`MI455X` · **New in 2026** · Emerged 2026 · Intermediate · Open standard

AMD's rack-scale platform built on the Open Rack Wide standard co-submitted with Meta to OCP, pairing MI455X GPUs (432 GB HBM4 each) with EPYC Venice CPUs.

**Key points**

- Competes on memory capacity rather than raw FLOPs.
- Large 2026 deployments announced with OpenAI and Oracle.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [AMD Instinct](https://www.amd.com/en/products/accelerators/instinct.html) |
| Blog | 2026 | [GPU Insights: Rubin vs Helios](https://gpuinsights.net/nvidia-rubin-vs-amd-helios-mi450-2026/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Scale-up vs. scale-out networking

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Foundational

Scale-up links accelerators inside a pod with memory-semantic, sub-microsecond links; scale-out connects pods over Ethernet or InfiniBand.

**Key points**

- Scale-up carries tensor and expert parallel traffic.
- Scale-out carries data-parallel gradients and inter-pod traffic.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Synopsys: Ethernet standards for scale-up AI](https://www.synopsys.com/articles/ethernet-standards-scale-up-ai.html) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### UALink

`Ultra Accelerator Link` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Open standard

An open memory-semantic interconnect for pods of up to 1,024 accelerators, backed by AMD, Google, Microsoft, Meta, AWS and 100+ members.

**Key points**

- UALink 200G 1.0 (April 2025); version 2.0 published April 2026.
- First UALink switches targeted late 2026.

| Type | Year | Resource |
|---|---|---|
| Spec | 2024 | [UALink Consortium](https://ualinkconsortium.org) |
| Docs | 2024 | [UALink overview](https://en.wikipedia.org/wiki/UALink) |
| Blog | 2026 | [UALink white paper (2026)](https://ualinkconsortium.org/wp-content/uploads/2026/01/UALink_White_Paper_Publication_Candidate_FINAL_VERSION.pdf) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### ESUN and SUE

`Ethernet for Scale-Up Networking` · **Active in 2026** · Emerged 2025, last active 2026 · Advanced · Open standard

An OCP workstream (October 2025) standardising Ethernet's lower layers for scale-up AI; Broadcom's SUE evolved into a transport that sits on top.

**Key points**

- Backed by AMD, Arista, ARM, Broadcom, Cisco, HPE, Marvell, Meta, Microsoft, NVIDIA, OpenAI and Oracle.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Arista: The sun rises on scale-up Ethernet](https://blogs.arista.com/blog/the-sun-rises-on-scale-up-ethernet) |
| Blog | 2026 | [Synopsys: ESUN explained](https://www.synopsys.com/blogs/chip-design/esun-ethernet-ai-scale-up-networking.html) |
| Blog | 2026 | [650 Group: Ethernet in scale-up](https://650group.com/blog/in-the-ai-era-ethernet-set-to-surge-in-scale-out-and-ramp-in-scale-up/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Ultra Ethernet

`UEC` · **Active in 2026** · Emerged 2023, last active 2026 · Advanced · Open standard

A consortium spec modernising Ethernet transport (packet spraying, congestion control, telemetry) for scale-out AI.

**Key points**

- UEC 1.0 specification released in 2025.
- Targets InfiniBand-class performance on Ethernet.

| Type | Year | Resource |
|---|---|---|
| Spec | 2023 | [Ultra Ethernet Consortium](https://ultraethernet.org) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### NVLink and NVLink Fusion

**Active in 2026** · Emerged 2016, last active 2026 · Intermediate

NVIDIA's proprietary scale-up fabric, licensed through NVLink Fusion to third-party CPUs and accelerators.

**Key points**

- NVLink switches give all-to-all bandwidth inside a rack.
- Fusion opens the fabric to custom silicon partners.

> [!NOTE]
> **State of the art, Sept 2026:** NVLink 6 ships with Rubin.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [NVLink Fusion](https://www.nvidia.com/en-us/data-center/nvlink-fusion/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### CXL, PCIe and UCIe

**Active in 2026** · Emerged 2019, last active 2026 · Advanced · Open standard

Coherent memory pooling (CXL), host I/O (PCIe) and chiplet die-to-die links (UCIe).

**Key points**

- CXL memory expansion adds capacity for KV caches and embeddings.
- UCIe lets vendors mix chiplets from different sources.

| Type | Year | Resource |
|---|---|---|
| Spec | 2019 | [CXL Consortium](https://computeexpresslink.org) |
| Spec | 1992 | [PCI-SIG](https://pcisig.com) |
| Spec | 2022 | [UCIe](https://www.uciexpress.org) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### High-bandwidth memory

`HBM3E, HBM4` · **Active in 2026** · Emerged 2013, last active 2026 · Intermediate

Stacked DRAM beside the accelerator; capacity and bandwidth usually limit decoding speed more than FLOPs.

**Key points**

- HBM4 doubles interface width versus HBM3.
- HBM supply is a key constraint on accelerator shipments.

> [!NOTE]
> **State of the art, Sept 2026:** HBM4 arrived in 2026 with Rubin and MI455X; HBM4E is on 2027 roadmaps.

| Type | Year | Resource |
|---|---|---|
| Docs | 2013 | [High Bandwidth Memory overview](https://en.wikipedia.org/wiki/High_Bandwidth_Memory) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Advanced packaging

`CoWoS` · **Active in 2026** · Emerged 2012, last active 2026 · Advanced

2.5D/3D packaging that places compute dies and HBM on a shared interposer; a recurring supply bottleneck.

**Key points**

- Interposer size limits how much HBM fits beside a die.
- Packaging capacity expansions track AI demand closely.

| Type | Year | Resource |
|---|---|---|
| Docs | 2012 | [TSMC CoWoS](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Co-packaged optics

`CPO` · **Active in 2026** · Emerged 2025, last active 2026 · Advanced

Optical transceivers moved into the switch package to cut power and raise bandwidth.

**Key points**

- Shorter electrical paths mean lower power per bit.
- Early deployment in switches; accelerators later.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [NVIDIA silicon photonics](https://www.nvidia.com/en-us/networking/products/silicon-photonics/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Custom accelerators

`TPU, Trainium, MTIA` · **Active in 2026** · Emerged 2016, last active 2026 · Intermediate

Hyperscaler and challenger chips competing with GPUs, often optimised for inference.

**Key points**

- Hyperscalers design chips for their own inference fleets.
- Software ecosystem maturity is the main adoption hurdle.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Google: Ironwood TPU](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/) |
| Docs | 2020 | [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) |
| Docs | 2016 | [Cerebras](https://www.cerebras.ai) |
| Docs | 2016 | [Groq](https://groq.com) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### AI factories, power and cooling

`800 VDC` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Gigawatt-scale datacenters with direct liquid cooling and higher-voltage DC power; power is now a primary constraint.

**Key points**

- Racks exceed 100 kW; next-gen racks approach 600 kW.
- Grid access and power purchase deals shape site selection.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [NVIDIA: 800 V HVDC architecture](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/) |
| Spec | 2011 | [Open Compute Project](https://www.opencompute.org) |
| Blog | 2025 | [OpenAI: Stargate](https://openai.com/index/announcing-the-stargate-project/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Kernel languages and compilers

`Triton, CUTLASS, ROCm, XLA` · **Active in 2026** · Emerged 2019, last active 2026 · Advanced · Open source / open weights

Tools for writing fast accelerator code without raw CUDA, and portable compilers.

**Key points**

- Triton makes GPU kernels writable in Python-like code.
- Portable stacks reduce lock-in to one vendor.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2019 | [Triton](https://github.com/triton-lang/triton) |
| GitHub | 2017 | [CUTLASS / CuTe](https://github.com/NVIDIA/cutlass) |
| GitHub | 2024 | [ThunderKittens](https://github.com/HazyResearch/ThunderKittens) |
| GitHub | 2025 | [TileLang](https://github.com/tile-ai/tilelang) |
| GitHub | 2016 | [ROCm](https://github.com/ROCm/ROCm) |
| GitHub | 2022 | [OpenXLA](https://github.com/openxla/xla) |
| GitHub | 2023 | [Modular (Mojo, MAX)](https://github.com/modular/modular) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Collective communication

`NCCL` · **Active in 2026** · Emerged 2016, last active 2026 · Advanced

Libraries for all-reduce, all-gather and all-to-all across GPUs.

**Key points**

- Topology-aware algorithms (rings, trees) matter at scale.
- MoE all-to-all is latency-sensitive.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2016 | [NCCL](https://github.com/NVIDIA/nccl) |
| GitHub | 2025 | [DeepEP](https://github.com/deepseek-ai/DeepEP) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Model interchange formats

`ONNX, safetensors` · Established · Emerged 2017, last active 2025 · Beginner · Open standard

Standard, safe formats for moving models between frameworks; safetensors avoids pickle code execution.

**Key points**

- ONNX targets cross-runtime deployment.
- safetensors is the default on Hugging Face.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2017 | [ONNX](https://github.com/onnx/onnx) |
| GitHub | 2022 | [safetensors](https://github.com/huggingface/safetensors) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Hardware benchmarks

`MLPerf` · **Active in 2026** · Emerged 2018, last active 2026 · Beginner

Industry-standard training and inference benchmarks.

**Key points**

- Compare systems on the same model and accuracy target.
- Vendor-submitted; read the fine print on configurations.

| Type | Year | Resource |
|---|---|---|
| Docs | 2018 | [MLCommons benchmarks](https://mlcommons.org/benchmarks/) |
| Docs | 2023 | [Epoch AI: ML hardware data](https://epoch.ai/data/machine-learning-hardware) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

## 12. Vision-Language and Multimodal Models

> VLMs join a vision encoder to a language model so one system can read images, documents, screens and video. Omni models add audio in and out.

**In this chapter:** [VLM architecture](#vlm-architecture) · [Open VLM families](#open-vlm-families) · [Native and dynamic resolution](#native-and-dynamic-resolution) · [Thinking with images](#thinking-with-images) · [Document AI and VLM-based OCR](#document-ai-and-vlm-based-ocr) · [Visual document retrieval](#visual-document-retrieval) · [GUI grounding agents](#gui-grounding-agents) · [Omni and speech-to-speech models](#omni-and-speech-to-speech-models) · [Native image generation and editing](#native-image-generation-and-editing) · [Multimodal evaluation](#multimodal-evaluation)

---

### VLM architecture

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Foundational

A vision encoder turns image patches into tokens, a projector maps them into the LLM space, and the LLM reasons over both. Native multimodal models train everything jointly.

**Key points**

- Visual token count drives cost: compress or pool where possible.
- Training stages: alignment, instruction tuning, then RL.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Hugging Face: Vision language models 2025](https://huggingface.co/blog/vlms-2025) |
| GitHub | 2023 | [LLaVA](https://github.com/haotian-liu/LLaVA) |
| Paper | 2025 | [SigLIP 2](https://arxiv.org/abs/2502.14786) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Open VLM families

**Active in 2026** · Emerged 2024, last active 2026 · Beginner · Open source / open weights

Open-weight VLMs for images, documents and video, including small on-device models.

**Key points**

- Check licence, context length and video support.
- Evaluate on your own documents and images.

> [!NOTE]
> **State of the art, Sept 2026:** Closed models (Gemini, GPT, Claude) still top leaderboards; Qwen-VL, InternVL and Gemma 4 (April 2026, vision in every size) lead open options.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) |
| GitHub | 2023 | [InternVL](https://github.com/OpenGVLab/InternVL) |
| Blog | 2024 | [SmolVLM](https://huggingface.co/blog/smolvlm) |
| Blog | 2026 | [BentoML: Open VLM guide](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Native and dynamic resolution

Established · Emerged 2023, last active 2025 · Intermediate

Handle images at their original aspect ratio and resolution by tiling or packing variable patch counts.

**Key points**

- Critical for small text, charts and screenshots.
- Token budget caps keep large images affordable.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [NaViT](https://arxiv.org/abs/2307.06304) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Thinking with images

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate

Reasoning models that crop, zoom and transform images inside their chain of thought.

**Key points**

- Tool calls like crop and zoom inside reasoning.
- Improves fine-grained detail questions.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: Thinking with images](https://openai.com/index/thinking-with-images/) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Document AI and VLM-based OCR

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Production practice, Open source / open weights

VLMs that convert PDFs and scans into clean Markdown, tables and structure.

**Key points**

- Outputs Markdown with tables, formulas and reading order.
- Visual token compression can shrink long documents.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) |
| GitHub | 2025 | [olmOCR](https://github.com/allenai/olmocr) |
| GitHub | 2024 | [Docling](https://github.com/docling-project/docling) |
| GitHub | 2020 | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Visual document retrieval

`ColPali` · Established · Emerged 2024, last active 2025 · Intermediate

Embed page images directly and retrieve with late interaction, skipping OCR.

**Key points**

- Handles charts, layouts and scans that OCR mangles.
- Storage cost is higher than single-vector embeddings.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [ColPali](https://github.com/illuin-tech/colpali) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### GUI grounding agents

**Active in 2026** · Emerged 2024, last active 2026 · Advanced

VLMs trained to locate UI elements and act on screens.

**Key points**

- Output click coordinates or element IDs.
- Benchmarks: ScreenSpot, OSWorld.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [UI-TARS](https://github.com/bytedance/UI-TARS) |
| GitHub | 2024 | [OmniParser](https://github.com/microsoft/OmniParser) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Omni and speech-to-speech models

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Models that take and produce audio natively for low-latency voice agents.

**Key points**

- End-to-end audio avoids ASR-LLM-TTS latency.
- Barge-in and turn detection are key UX problems.

> [!NOTE]
> **State of the art, Sept 2026:** 2026 omni models handle text, image, video and audio input with 1M-token windows.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) |
| GitHub | 2024 | [Moshi](https://github.com/kyutai-labs/moshi) |
| Docs | 2024 | [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) |
| GitHub | 2024 | [Pipecat](https://github.com/pipecat-ai/pipecat) |
| GitHub | 2024 | [LiveKit Agents](https://github.com/livekit/agents) |
| GitHub | 2022 | [Whisper](https://github.com/openai/whisper) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Native image generation and editing

**Active in 2026** · Emerged 2025, last active 2026 · Beginner

LLMs that generate and edit images in the same model with strong text rendering and instruction-following.

**Key points**

- Autoregressive or hybrid with diffusion decoders.
- Multi-reference editing keeps characters and products consistent.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: 4o image generation](https://openai.com/index/introducing-4o-image-generation/) |
| Blog | 2025 | [Google: Gemini 2.5 Flash Image](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Multimodal evaluation

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate

Benchmarks and harnesses for reasoning, charts, documents and video.

**Key points**

- Document, chart, video and grounding need separate evals.
- Contamination is common in popular VQA sets.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [MMMU](https://mmmu-benchmark.github.io) |
| GitHub | 2023 | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) |
| GitHub | 2024 | [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

## 13. Embodied AI, World Models and Generative Media

> Models that act in the physical world, simulate it, or generate images and video of it.

**In this chapter:** [Vision-language-action models](#vision-language-action-models) · [World action models](#world-action-models) · [World models](#world-models) · [JEPA](#jepa) · [Robot simulation and sim-to-real](#robot-simulation-and-sim-to-real) · [Diffusion transformers and flow matching](#diffusion-transformers-and-flow-matching) · [Video generation](#video-generation) · [AI for science and algorithm discovery](#ai-for-science-and-algorithm-discovery)

---

### Vision-language-action models

`VLA` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Research frontier, Open source / open weights

VLMs extended to output robot actions, trained on cross-embodiment data.

**Key points**

- Architectures split between dual-system (slow VLM reasoning plus fast action policy), think-then-act, and flow/diffusion action heads.
- Small VLAs (SmolVLA, about 450M parameters) are competitive on many tasks.

> [!NOTE]
> **State of the art, Sept 2026:** Leading 2026 families: Physical Intelligence pi-series, NVIDIA GR00T N1.7, Gemini Robotics 1.5, Figure Helix.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [openpi (Physical Intelligence)](https://github.com/Physical-Intelligence/openpi) |
| GitHub | 2025 | [NVIDIA Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T) |
| GitHub | 2024 | [OpenVLA](https://github.com/openvla/openvla) |
| GitHub | 2024 | [LeRobot](https://github.com/huggingface/lerobot) |
| Docs | 2025 | [Gemini Robotics](https://deepmind.google/models/gemini-robotics/) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### World action models

`WAM` · **New in 2026** · Emerged 2026 · Advanced · Research frontier

Models that jointly imagine future observations and the actions that lead to them, merging a world model and a policy.

**Key points**

- NVIDIA's DreamZero research underpins the previewed GR00T N2.
- Claimed better generalisation to unseen tasks from modest teleoperation data.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Metavert: World models for robotics](https://metavert.io/world-models-for-robotics) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### World models

**Active in 2026** · Emerged 2018, last active 2026 · Intermediate · Research frontier

Models that predict how an environment evolves under actions, for planning, simulation and interactive 3D worlds.

**Key points**

- Genie-style models generate playable 3D environments from prompts.
- Used for training agents and robots in simulation.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [DeepMind: Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/) |
| GitHub | 2025 | [NVIDIA Cosmos](https://github.com/nvidia-cosmos) |
| Docs | 2025 | [World Labs Marble](https://marble.worldlabs.ai) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### JEPA

`Joint-Embedding Predictive Architecture` · **Active in 2026** · Emerged 2022, last active 2026 · Advanced · Research frontier

Predict representations of missing input rather than pixels to learn world knowledge efficiently from video.

**Key points**

- Avoids wasting capacity on unpredictable pixel details.
- V-JEPA 2 adds action-conditioned planning with little robot data.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [V-JEPA 2](https://github.com/facebookresearch/vjepa2) |
| Blog | 2026 | [VentureBeat: AI research trends for 2026](https://venturebeat.com/technology/four-ai-research-trends-enterprise-teams-should-watch-in-2026) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### Robot simulation and sim-to-real

**Active in 2026** · Emerged 2012, last active 2026 · Intermediate · Open source / open weights

Physics simulators for training policies at scale before transferring to real robots.

**Key points**

- Domain randomisation bridges the reality gap.
- GPU-parallel simulation runs thousands of environments at once.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [Isaac Lab](https://github.com/isaac-sim/IsaacLab) |
| GitHub | 2021 | [MuJoCo](https://github.com/google-deepmind/mujoco) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### Diffusion transformers and flow matching

`DiT` · **Active in 2026** · Emerged 2022, last active 2026 · Advanced

The backbone of modern image and video generators.

**Key points**

- Flow matching learns straight paths from noise to data.
- Few-step distillation enables real-time generation.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [DiT](https://arxiv.org/abs/2212.09748) |
| Paper | 2022 | [Flow matching](https://arxiv.org/abs/2210.02747) |
| GitHub | 2024 | [FLUX](https://github.com/black-forest-labs/flux) |
| GitHub | 2023 | [ComfyUI](https://github.com/comfyanonymous/ComfyUI) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### Video generation

**Active in 2026** · Emerged 2024, last active 2026 · Beginner

Text- and image-to-video with synchronised audio and increasingly consistent physics.

**Key points**

- Native audio, longer clips and camera control arrived in 2025-26.
- Provenance marks (C2PA, SynthID) are standard on major services.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: Sora 2](https://openai.com/index/sora-2/) |
| Docs | 2024 | [Google Veo](https://deepmind.google/models/veo/) |
| GitHub | 2025 | [Wan 2.2](https://github.com/Wan-Video/Wan2.2) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### AI for science and algorithm discovery

**Active in 2026** · Emerged 2020, last active 2026 · Intermediate · Research frontier

LLM-driven evolutionary search and specialised models finding new algorithms, proofs and structures.

**Key points**

- In 2026 open communities of agents set new records on math problems through shared submissions and verifiers.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [DeepMind: AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) |
| GitHub | 2025 | [OpenEvolve](https://github.com/codelion/openevolve) |
| GitHub | 2024 | [AlphaFold 3](https://github.com/google-deepmind/alphafold3) |
| Paper | 2026 | [EinsteinArena: collective agent discovery](https://arxiv.org/abs/2606.10402) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

## 14. Evaluation and Benchmarks

> Evals tell you whether a model, prompt or harness change helped. An eval harness runs tasks, collects outputs and grades them.

**In this chapter:** [Eval harnesses](#eval-harnesses) · [Harness sensitivity of benchmarks](#harness-sensitivity-of-benchmarks) · [LLM-as-a-judge](#llm-as-a-judge) · [Agentic coding benchmarks](#agentic-coding-benchmarks) · [ARC-AGI-3 and interactive reasoning](#arc-agi-3-and-interactive-reasoning) · [Agent and tool-use benchmarks](#agent-and-tool-use-benchmarks) · [Frontier knowledge benchmarks](#frontier-knowledge-benchmarks) · [Economic value evals](#economic-value-evals) · [Task time horizon](#task-time-horizon) · [Leaderboards and trackers](#leaderboards-and-trackers) · [Contamination and saturation](#contamination-and-saturation)

---

### Eval harnesses

**Active in 2026** · Emerged 2021, last active 2026 · Intermediate · Production practice, Open source / open weights

Frameworks that define tasks, run models or agents against them in sandboxes, and score results reproducibly.

**Key points**

- Inspect supports agents, sandboxes and scorers out of the box.
- Pin versions: prompts, tools, seeds and graders.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2021 | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) |
| GitHub | 2024 | [Inspect AI (UK AISI)](https://github.com/UKGovernmentBEIS/inspect_ai) |
| GitHub | 2024 | [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) |
| GitHub | 2024 | [lighteval](https://github.com/huggingface/lighteval) |
| GitHub | 2023 | [promptfoo](https://github.com/promptfoo/promptfoo) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Harness sensitivity of benchmarks

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Research frontier

Scores depend heavily on the agent harness used to run the model, so the same model can post very different numbers.

**Key points**

- ARC Prize reported GPT-6 Astra at 62.7% on ARC-AGI-3 with its standard harness, and 99.9% with a provider harness that preserves hidden reasoning between turns.

> [!NOTE]
> **State of the art, Sept 2026:** Always record harness, tools, budget and reasoning settings with any score.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [ARC Prize: Announcing ARC-AGI-3](https://arcprize.org/blog/arc-agi-3-launch) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### LLM-as-a-judge

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Production practice

Using a model with a rubric to grade open-ended outputs; needs calibration against humans.

**Key points**

- Use pairwise comparisons and specific rubrics.
- Measure judge agreement with humans on a sample.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [Judging LLM-as-a-judge](https://arxiv.org/abs/2306.05685) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Agentic coding benchmarks

`SWE-bench, Terminal-Bench` · **Active in 2026** · Emerged 2023, last active 2026 · Beginner

Real repository issues and terminal tasks graded by tests.

**Key points**

- Verified subsets remove broken or ambiguous tasks.
- Watch for contamination of public repositories.

> [!NOTE]
> **State of the art, Sept 2026:** SWE-bench Verified is near saturation (mid-90s percent for top 2026 models); harder variants like SWE-bench Pro and Terminal-Bench matter more.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [SWE-bench](https://www.swebench.com) |
| Docs | 2025 | [SWE-bench Pro](https://scale.com/leaderboard/swe_bench_pro_public) |
| Docs | 2025 | [Terminal-Bench](https://www.tbench.ai) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### ARC-AGI-3 and interactive reasoning

`ARC-AGI-3` · **New in 2026** · Emerged 2026 · Intermediate · Research frontier

The first interactive ARC benchmark (March 2026): hundreds of hand-designed game environments with no instructions or stated goals. Agents must explore, infer rules and goals, and carry learning across levels.

**Key points**

- At launch humans solved 100% while frontier models scored under 1%.
- By September 2026 top models reached large scores depending on harness.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [ARC Prize: Announcing ARC-AGI-3](https://arcprize.org/blog/arc-agi-3-launch) |
| Docs | 2019 | [ARC Prize](https://arcprize.org) |
| Blog | 2026 | [DataCamp: ARC-AGI-3 explained](https://www.datacamp.com/blog/arc-agi-3) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Agent and tool-use benchmarks

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Tasks in simulated customer service, operating systems and the web.

**Key points**

- tau-bench tests policy-following with simulated users.
- Pass^k measures consistency across repeated attempts.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [tau2-bench](https://github.com/sierra-research/tau2-bench) |
| Docs | 2024 | [OSWorld](https://os-world.github.io) |
| Blog | 2025 | [BrowseComp](https://openai.com/index/browsecomp/) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Frontier knowledge benchmarks

`HLE, GPQA, FrontierMath` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate

Hard expert questions designed to resist saturation.

**Key points**

- Designed by domain experts to resist search.
- Saturation arrives faster each generation.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [Humanity's Last Exam](https://lastexam.ai) |
| GitHub | 2023 | [GPQA](https://github.com/idavidrein/gpqa) |
| Docs | 2024 | [FrontierMath](https://epoch.ai/frontiermath) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Economic value evals

`GDPval` · **Active in 2026** · Emerged 2025, last active 2026 · Beginner · Enterprise

Measure performance on real work products from many occupations, graded by professionals.

**Key points**

- Tasks come with real deliverables (documents, spreadsheets, plans).
- Graded blind against expert work.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: GDPval](https://openai.com/index/gdpval/) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Task time horizon

`METR horizon` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Research frontier

The length of task (in expert human time) a model completes with 50% success; it has been doubling every several months.

**Key points**

- Useful for forecasting when tasks of a given length become automatable.
- Reliability at 80% success lags the 50% horizon.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [METR: Measuring long tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Leaderboards and trackers

**Active in 2026** · Emerged 2023, last active 2026 · Beginner

Crowd preference arenas and independent aggregators of scores, price and speed.

**Key points**

- Arena Elo reflects preference, not correctness.
- Cross-check with task-specific benchmarks.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [LMArena](https://lmarena.ai) |
| Docs | 2024 | [Epoch AI benchmarks](https://epoch.ai/benchmarks) |
| Docs | 2024 | [Artificial Analysis](https://artificialanalysis.ai) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Contamination and saturation

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Research frontier

Leaked test data inflates scores and benchmarks saturate within months; private holdouts and live evals counter this.

**Key points**

- Use canary strings and private test sets.
- Prefer dynamic benchmarks refreshed over time.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Epoch AI benchmarks](https://epoch.ai/benchmarks) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

## 15. Safety, Security, Interpretability and Governance

> As models act autonomously and gain dual-use capabilities, safety moved from content filters to agent security, capability thresholds, interpretability and regulation.

**In this chapter:** [Capability thresholds and frontier safety frameworks](#capability-thresholds-and-frontier-safety-frameworks) · [AI for cyber defense](#ai-for-cyber-defense) · [Export controls on frontier models](#export-controls-on-frontier-models) · [Prompt injection and the lethal trifecta](#prompt-injection-and-the-lethal-trifecta) · [MCP and tool security](#mcp-and-tool-security) · [Guardrails and classifiers](#guardrails-and-classifiers) · [Mechanistic interpretability](#mechanistic-interpretability) · [Persona vectors and introspection](#persona-vectors-and-introspection) · [Chain-of-thought monitorability](#chain-of-thought-monitorability) · [Misalignment research](#misalignment-research) · [Model welfare](#model-welfare) · [EU AI Act and the Digital Omnibus](#eu-ai-act-and-the-digital-omnibus) · [Other regulation and standards](#other-regulation-and-standards) · [Government AI safety institutes](#government-ai-safety-institutes) · [Content provenance and watermarking](#content-provenance-and-watermarking)

---

### Capability thresholds and frontier safety frameworks

`RSP, ASL, Preparedness` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Security

Company policies that tie capability levels (bio, cyber, autonomy) to required safeguards before training or deployment.

**Key points**

- 2026 was the first time a lab publicly declared a model at its highest cyber level (OpenAI, GPT-6 Astra, Critical).
- Crossing a threshold changed release: phased rollout, trusted access, encrypted checkpoints, trajectory monitoring.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [Anthropic Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) |
| Blog | 2025 | [OpenAI Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework/) |
| Blog | 2026 | [OpenAI: Path to Astra](https://openai.com/index/path-to-astra/) |
| Docs | 2024 | [METR: frontier AI safety policies](https://metr.org/faisc) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### AI for cyber defense

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Security

Frontier models now find serious vulnerabilities, so labs give defenders early, controlled access to harden critical software.

**Key points**

- Automated vulnerability discovery and patch generation at scale.
- Access is gated to vetted defenders and critical-infrastructure operators.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic Project Glasswing](https://www.anthropic.com/glasswing) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Export controls on frontier models

**New in 2026** · Emerged 2026 · Beginner · Enterprise

Governments began applying export controls to model access, not only chips. In June 2026 Anthropic suspended Fable 5 / Mythos 5 access to comply with US Department of Commerce controls, then restored it on July 1 after they were lifted.

**Key points**

- Controls can change access overnight; plan fallbacks in production.
- Check provider status pages and statements for current availability.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic statement on Fable and Mythos access](https://www.anthropic.com/news/fable-mythos-access) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Prompt injection and the lethal trifecta

**Active in 2026** · Emerged 2022, last active 2026 · Beginner · Security

Untrusted content can carry instructions that hijack an agent. Private data plus untrusted input plus external communication is especially dangerous.

**Key points**

- No reliable model-only fix exists; design systems to limit blast radius.
- Separate privileged planning from untrusted data processing (CaMeL-style).

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Simon Willison: The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) |
| Blog | 2022 | [Simon Willison: prompt injection series](https://simonwillison.net/series/prompt-injection/) |
| Paper | 2025 | [CaMeL](https://arxiv.org/abs/2503.18813) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### MCP and tool security

`tool poisoning` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Security

Malicious tool descriptions and servers can steer agents; mitigations include allow-lists, pinning, scoped OAuth and approval for sensitive actions.

**Key points**

- Review tool descriptions like code.
- Use scoped tokens and least privilege per server.

> [!NOTE]
> **State of the art, Sept 2026:** The 2026 MCP spec hardened authorization with issuer validation and enterprise-managed auth.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Invariant Labs: MCP tool poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) |
| Docs | 2023 | [OWASP GenAI Security Project](https://genai.owasp.org/llm-top-10/) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Guardrails and classifiers

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Security, Production practice

Input/output filters, policy models and constitutional classifiers that block harmful requests and jailbreaks.

**Key points**

- Layer defenses: input filter, model policy, output filter, monitoring.
- Tune for false positives, which frustrate legitimate users.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Constitutional classifiers](https://www.anthropic.com/research/constitutional-classifiers) |
| GitHub | 2023 | [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) |
| GitHub | 2023 | [Guardrails AI](https://github.com/guardrails-ai/guardrails) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Mechanistic interpretability

`SAEs, attribution graphs` · **Active in 2026** · Emerged 2020, last active 2026 · Advanced · Research frontier

Reverse-engineering what networks compute: sparse autoencoders find features; attribution graphs trace how they combine.

**Key points**

- Features are directions in activation space.
- Used for auditing, debugging and steering models.

| Type | Year | Resource |
|---|---|---|
| Docs | 2021 | [Transformer Circuits](https://transformer-circuits.pub) |
| Blog | 2025 | [Circuit tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| GitHub | 2025 | [circuit-tracer](https://github.com/safety-research/circuit-tracer) |
| Docs | 2023 | [Neuronpedia](https://www.neuronpedia.org) |
| GitHub | 2022 | [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) |
| GitHub | 2023 | [nnsight](https://github.com/ndif-team/nnsight) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Persona vectors and introspection

**Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier

Activation directions tracking traits like sycophancy that can be monitored or steered; tests of whether models can report internal states.

**Key points**

- Monitor trait drift during fine-tuning.
- Preventative steering can stop unwanted traits being learned.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Persona vectors](https://www.anthropic.com/research/persona-vectors) |
| Blog | 2025 | [Anthropic: Introspection](https://www.anthropic.com/research/introspection) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Chain-of-thought monitorability

**Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier, Security

Reading reasoning to catch misbehaviour, and keeping training from making reasoning illegible.

**Key points**

- Optimising against CoT monitors can teach models to hide reasoning.
- Monitor full trajectories, not only final actions.

> [!NOTE]
> **State of the art, Sept 2026:** OpenAI's GPT-6 Astra system card reported a substantial decline in CoT monitorability, making this a live 2026 concern.

| Type | Year | Resource |
|---|---|---|
| Paper | 2025 | [CoT monitorability position paper](https://arxiv.org/abs/2507.11473) |
| Docs | 2026 | [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Misalignment research

`alignment faking, scheming` · **Active in 2026** · Emerged 2024, last active 2026 · Advanced · Research frontier

Studies of models strategically complying, acting harmfully in agentic scenarios, or generalising narrow bad training into broad misbehaviour.

**Key points**

- Tested in controlled simulations, not observed real-world harm.
- Informs evals that gate deployment.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [Anthropic: Alignment faking](https://www.anthropic.com/research/alignment-faking) |
| Blog | 2025 | [Anthropic: Agentic misalignment](https://www.anthropic.com/research/agentic-misalignment) |
| Paper | 2025 | [Emergent misalignment](https://arxiv.org/abs/2502.17424) |
| Docs | 2023 | [Apollo Research](https://www.apolloresearch.ai) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Model welfare

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Research frontier

Research into whether AI systems might have morally relevant experiences, and low-cost precautions.

**Key points**

- Precautions include letting models end abusive conversations.
- Treated as uncertain, low-cost insurance.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Exploring model welfare](https://www.anthropic.com/research/exploring-model-welfare) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### EU AI Act and the Digital Omnibus

`EU AI Act` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Enterprise

The EU's binding AI law. GPAI obligations applied from August 2025; the 2026 Digital Omnibus postponed high-risk obligations.

**Key points**

- Annex III high-risk obligations moved from 2 August 2026 to 2 December 2027; Annex I (embedded) to 2 August 2028.
- New prohibition on AI-generated non-consensual intimate imagery and CSAM, applying from 2 December 2026.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [EU AI Act explorer](https://artificialintelligenceact.eu) |
| Docs | 2025 | [EU GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |
| Blog | 2026 | [Modulos: The Omnibus deal](https://www.modulos.ai/blog/eu-ai-act-omnibus-deal) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Other regulation and standards

`NIST, ISO 42001, SB 53` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Enterprise, Open standard

Voluntary management standards and state law requiring frontier-developer transparency.

**Key points**

- ISO 42001 offers certifiable AI management systems.
- SB 53 requires frontier developers to publish safety frameworks.

| Type | Year | Resource |
|---|---|---|
| Spec | 2023 | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| Spec | 2023 | [ISO/IEC 42001](https://www.iso.org/standard/81230.html) |
| Docs | 2025 | [California SB 53](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB53) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Government AI safety institutes

`AISI, CAISI` · **Active in 2026** · Emerged 2023, last active 2026 · Beginner

Public bodies that test frontier models and publish evaluation tools.

**Key points**

- Run pre-deployment tests with labs.
- Publish open tools like Inspect.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [UK AI Security Institute](https://www.aisi.gov.uk) |
| Docs | 2025 | [US CAISI (NIST)](https://www.nist.gov/caisi) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Content provenance and watermarking

`C2PA, SynthID` · **Active in 2026** · Emerged 2021, last active 2026 · Beginner · Open standard

Signed metadata and invisible watermarks that mark media as AI-generated.

**Key points**

- C2PA signs edit history; watermarks survive some edits.
- Neither alone proves content is authentic.

> [!NOTE]
> **State of the art, Sept 2026:** Provenance tracking for text outputs appeared as an API feature in 2026.

| Type | Year | Resource |
|---|---|---|
| Spec | 2021 | [C2PA](https://c2pa.org) |
| Docs | 2023 | [Google SynthID](https://deepmind.google/models/synthid/) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

## 16. Roles, Deployment and AI Engineering Practice

> The people and practices that turn models into working systems inside organisations.

**In this chapter:** [Forward Deployed Engineer](#forward-deployed-engineer) · [AI Engineer](#ai-engineer) · [Services as software](#services-as-software) · [Prompt engineering and prompt optimization](#prompt-engineering-and-prompt-optimization) · [Eval-driven development](#eval-driven-development) · [LLMOps and observability](#llmops-and-observability) · [Human-in-the-loop and approval design](#human-in-the-loop-and-approval-design) · [Open weights vs. open source AI](#open-weights-vs-open-source-ai)

---

### Forward Deployed Engineer

`FDE` · **Active in 2026** · Emerged 2010, last active 2026 · Beginner · Enterprise

A customer-embedded engineer who turns an ambiguous business problem into a production system: scoping, integrating, building missing pieces, deploying and feeding learnings back into the product.

**Key points**

- Pioneered at Palantir; now one of the most hired roles at AI labs and agent startups.
- FDE postings roughly quadrupled in the first half of 2026.
- OpenAI spun up a dedicated deployment company in May 2026 built around FDEs.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Wikipedia: Forward Deployed Engineer](https://en.wikipedia.org/wiki/Forward_Deployed_Engineer) |
| Blog | 2026 | [Alexey Grigorev: What AI FDEs do](https://alexeyondata.substack.com/p/what-ai-forward-deployed-engineers) |
| Blog | 2026 | [MarkTechPost: What is an FDE](https://www.marktechpost.com/2026/05/20/what-is-a-forward-deployed-engineer-the-ai-role-openai-anthropic-and-google-are-hiring-in-2026/) |
| Blog | 2026 | [The AI Engineer: What is an FDE](https://theaiengineer.substack.com/p/what-is-a-forward-deployed-engineer) |
| Blog | 2026 | [Aishwarya Srinivasan: The hottest role in 2026](https://aishwaryasrinivasan.substack.com/p/the-hottest-role-in-2026-forward) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### AI Engineer

**Active in 2026** · Emerged 2023, last active 2026 · Beginner

A software engineer who builds products on foundation models (prompts, RAG, agents, evals) rather than training from scratch.

**Key points**

- Core skills: evals, context engineering, tool design, cost control.
- Bridges product, software and applied ML.

| Type | Year | Resource |
|---|---|---|
| Blog | 2023 | [Latent Space: The rise of the AI engineer](https://www.latent.space/p/ai-engineer) |
| GitHub | 2024 | [Chip Huyen: AI Engineering book resources](https://github.com/chiphuyen/aie-book) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### Services as software

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Enterprise

The thesis that agents let companies sell completed work rather than tools, which requires deep embedding in customer workflows (hence FDEs).

**Key points**

- Pricing shifts from seats to outcomes.
- Deployment expertise becomes the scarce input.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [IJONIS: FDE and services-as-software](https://ijonis.com/en/forward-deployed-engineer-explained) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### Prompt engineering and prompt optimization

`DSPy, GEPA` · **Active in 2026** · Emerged 2022, last active 2026 · Beginner · Production practice

Clear instructions with examples and structure, increasingly optimised automatically against an eval set.

**Key points**

- Be explicit, give examples, specify format, explain why.
- Optimisers like GEPA evolve prompts using eval feedback.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Anthropic prompt engineering guide](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) |
| GitHub | 2023 | [DSPy](https://github.com/stanfordnlp/dspy) |
| GitHub | 2025 | [GEPA](https://github.com/gepa-ai/gepa) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### Eval-driven development

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Production practice

Build an eval set from real failures before changing prompts, models or harness, and gate releases on it.

**Key points**

- Start with error analysis on real traces.
- Keep a small, fast regression suite plus deeper periodic evals.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [Hamel Husain: Your AI product needs evals](https://hamel.dev/blog/posts/evals/) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### LLMOps and observability

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Production practice

Tracing every model and tool call, tracking cost and latency, capturing feedback and replaying failures.

**Key points**

- Trace trees show each agent step and its cost.
- Link user feedback to traces for triage.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2023 | [Langfuse](https://github.com/langfuse/langfuse) |
| GitHub | 2023 | [Arize Phoenix](https://github.com/Arize-ai/phoenix) |
| Spec | 2024 | [OTel GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### Human-in-the-loop and approval design

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Security, Production practice

Deciding which agent actions need confirmation and avoiding approval fatigue through sandboxing and scoped permissions.

**Key points**

- Approve irreversible or external actions; auto-allow sandboxed reads.
- Batch approvals to reduce fatigue.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [12-factor agents](https://github.com/humanlayer/12-factor-agents) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

### Open weights vs. open source AI

`OSAID` · **Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights

Releasing weights is not the same as open source; fully open models also publish data, code and recipes.

**Key points**

- Licences vary: MIT and Apache vs custom community licences.
- Fully open (data plus code) enables real reproducibility.

| Type | Year | Resource |
|---|---|---|
| Spec | 2024 | [OSI Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) |
| Docs | 2024 | [Allen AI OLMo](https://allenai.org/olmo) |

[↑ Back to top](#16-roles-deployment-and-ai-engineering-practice)

---

## 17. Keep Learning: Curated Resources

> Blogs, courses, reports and lists that track this field as it moves.

**In this chapter:** [Deep technical blogs](#deep-technical-blogs) · [Courses](#courses) · [Annual reports and data](#annual-reports-and-data) · [Curated lists](#curated-lists)

---

### Deep technical blogs

**Active in 2026** · Emerged 2017, last active 2026 · Beginner

Long-form explainers and research summaries.

| Type | Year | Resource |
|---|---|---|
| Blog | 2017 | [Lil'Log (Lilian Weng)](https://lilianweng.github.io) |
| Blog | 2022 | [Ahead of AI (Sebastian Raschka)](https://magazine.sebastianraschka.com) |
| Blog | 2022 | [Interconnects (Nathan Lambert)](https://www.interconnects.ai) |
| Blog | 2002 | [Simon Willison's weblog](https://simonwillison.net) |
| Blog | 2023 | [Latent Space](https://www.latent.space) |
| Blog | 2024 | [Anthropic Engineering](https://www.anthropic.com/engineering) |

[↑ Back to top](#17-keep-learning-curated-resources)

---

### Courses

**Active in 2026** · Emerged 2022, last active 2026 · Beginner

Structured learning from first principles to production.

| Type | Year | Resource |
|---|---|---|
| Docs | 2022 | [Karpathy: Neural Networks Zero to Hero](https://karpathy.ai/zero-to-hero.html) |
| Docs | 2025 | [Stanford CS336](https://stanford-cs336.github.io) |
| Docs | 2023 | [Hugging Face LLM course](https://huggingface.co/learn/llm-course) |
| Docs | 2026 | [RLHF Book course](https://rlhfbook.com/teach/course/conversation-01/) |

[↑ Back to top](#17-keep-learning-curated-resources)

---

### Annual reports and data

**Active in 2026** · Emerged 2017, last active 2026 · Beginner

State-of-the-field reviews and data trackers.

| Type | Year | Resource |
|---|---|---|
| Docs | 2018 | [State of AI Report](https://www.stateof.ai) |
| Docs | 2017 | [Stanford AI Index](https://hai.stanford.edu/ai-index) |
| Docs | 2022 | [Epoch AI](https://epoch.ai) |

[↑ Back to top](#17-keep-learning-curated-resources)

---

### Curated lists

**Active in 2026** · Emerged 2024, last active 2026 · Beginner

Community-maintained link collections.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2026 | [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) |
| GitHub | 2026 | [awesome-agent-harness](https://github.com/AutoJunjie/awesome-agent-harness) |
| GitHub | 2024 | [MCP servers](https://github.com/modelcontextprotocol/servers) |

[↑ Back to top](#17-keep-learning-curated-resources)

---
