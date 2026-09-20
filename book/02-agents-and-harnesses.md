[Contents](../README.md#contents) · [← 1. The Frontier Landscape (September 2026)](01-the-frontier-landscape.md) · [3. Protocols and Interoperability Standards →](03-protocols-and-interoperability-standards.md)

# 2. Agents and Harnesses

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
