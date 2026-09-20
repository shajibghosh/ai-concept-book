[Contents](../README.md#contents) · [← 5. Context, Memory and Retrieval](05-context-memory-and-retrieval.md) · [7. Model Architectures →](07-model-architectures.md)

# 6. Reasoning and Post-Training

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
