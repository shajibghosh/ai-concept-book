[Contents](../README.md#contents) · [← 15. Safety, Security, Interpretability and Governance](15-safety-security-interpretability-and-governance.md) · [17. Keep Learning: Curated Resources →](17-keep-learning-curated-resources.md)

# 16. Roles, Deployment and AI Engineering Practice

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
