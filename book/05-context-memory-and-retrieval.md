[Contents](../README.md#contents) · [← 4. Agentic Coding and Developer Workflow](04-agentic-coding-and-developer-workflow.md) · [6. Reasoning and Post-Training →](06-reasoning-and-post-training.md)

# 5. Context, Memory and Retrieval

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
