[Contents](../README.md#contents) · [← 2. Agents and Harnesses](02-agents-and-harnesses.md) · [4. Agentic Coding and Developer Workflow →](04-agentic-coding-and-developer-workflow.md)

# 3. Protocols and Interoperability Standards

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
