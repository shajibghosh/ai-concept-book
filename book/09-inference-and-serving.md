[Contents](../README.md#contents) · [← 8. Training at Scale and Fine-Tuning](08-training-at-scale-and-fine-tuning.md) · [10. Quantization and Number Formats →](10-quantization-and-number-formats.md)

# 9. Inference and Serving

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
