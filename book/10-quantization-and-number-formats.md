[Contents](../README.md#contents) · [← 9. Inference and Serving](09-inference-and-serving.md) · [11. AI Hardware, Interconnect and Datacenter Standards →](11-ai-hardware-interconnect-and-datacenter-standards.md)

# 10. Quantization and Number Formats

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
