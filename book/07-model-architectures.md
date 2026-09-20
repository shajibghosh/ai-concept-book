[Contents](../README.md#contents) · [← 6. Reasoning and Post-Training](06-reasoning-and-post-training.md) · [8. Training at Scale and Fine-Tuning →](08-training-at-scale-and-fine-tuning.md)

# 7. Model Architectures

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
