[Contents](../README.md#contents) · [← 7. Model Architectures](07-model-architectures.md) · [9. Inference and Serving →](09-inference-and-serving.md)

# 8. Training at Scale and Fine-Tuning

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
