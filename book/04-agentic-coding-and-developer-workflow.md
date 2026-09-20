[Contents](../README.md#contents) · [← 3. Protocols and Interoperability Standards](03-protocols-and-interoperability-standards.md) · [5. Context, Memory and Retrieval →](05-context-memory-and-retrieval.md)

# 4. Agentic Coding and Developer Workflow

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
