[Contents](../README.md#contents) · [← 11. AI Hardware, Interconnect and Datacenter Standards](11-ai-hardware-interconnect-and-datacenter-standards.md) · [13. Embodied AI, World Models and Generative Media →](13-embodied-ai-world-models-and-generative-media.md)

# 12. Vision-Language and Multimodal Models

> VLMs join a vision encoder to a language model so one system can read images, documents, screens and video. Omni models add audio in and out.

**In this chapter:** [VLM architecture](#vlm-architecture) · [Open VLM families](#open-vlm-families) · [Native and dynamic resolution](#native-and-dynamic-resolution) · [Thinking with images](#thinking-with-images) · [Document AI and VLM-based OCR](#document-ai-and-vlm-based-ocr) · [Visual document retrieval](#visual-document-retrieval) · [GUI grounding agents](#gui-grounding-agents) · [Omni and speech-to-speech models](#omni-and-speech-to-speech-models) · [Native image generation and editing](#native-image-generation-and-editing) · [Multimodal evaluation](#multimodal-evaluation)

---

### VLM architecture

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Foundational

A vision encoder turns image patches into tokens, a projector maps them into the LLM space, and the LLM reasons over both. Native multimodal models train everything jointly.

**Key points**

- Visual token count drives cost: compress or pool where possible.
- Training stages: alignment, instruction tuning, then RL.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Hugging Face: Vision language models 2025](https://huggingface.co/blog/vlms-2025) |
| GitHub | 2023 | [LLaVA](https://github.com/haotian-liu/LLaVA) |
| Paper | 2025 | [SigLIP 2](https://arxiv.org/abs/2502.14786) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Open VLM families

**Active in 2026** · Emerged 2024, last active 2026 · Beginner · Open source / open weights

Open-weight VLMs for images, documents and video, including small on-device models.

**Key points**

- Check licence, context length and video support.
- Evaluate on your own documents and images.

> [!NOTE]
> **State of the art, Sept 2026:** Closed models (Gemini, GPT, Claude) still top leaderboards; Qwen-VL, InternVL and Gemma 4 (April 2026, vision in every size) lead open options.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) |
| GitHub | 2023 | [InternVL](https://github.com/OpenGVLab/InternVL) |
| Blog | 2024 | [SmolVLM](https://huggingface.co/blog/smolvlm) |
| Blog | 2026 | [BentoML: Open VLM guide](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Native and dynamic resolution

Established · Emerged 2023, last active 2025 · Intermediate

Handle images at their original aspect ratio and resolution by tiling or packing variable patch counts.

**Key points**

- Critical for small text, charts and screenshots.
- Token budget caps keep large images affordable.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [NaViT](https://arxiv.org/abs/2307.06304) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Thinking with images

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate

Reasoning models that crop, zoom and transform images inside their chain of thought.

**Key points**

- Tool calls like crop and zoom inside reasoning.
- Improves fine-grained detail questions.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: Thinking with images](https://openai.com/index/thinking-with-images/) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Document AI and VLM-based OCR

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Production practice, Open source / open weights

VLMs that convert PDFs and scans into clean Markdown, tables and structure.

**Key points**

- Outputs Markdown with tables, formulas and reading order.
- Visual token compression can shrink long documents.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) |
| GitHub | 2025 | [olmOCR](https://github.com/allenai/olmocr) |
| GitHub | 2024 | [Docling](https://github.com/docling-project/docling) |
| GitHub | 2020 | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Visual document retrieval

`ColPali` · Established · Emerged 2024, last active 2025 · Intermediate

Embed page images directly and retrieve with late interaction, skipping OCR.

**Key points**

- Handles charts, layouts and scans that OCR mangles.
- Storage cost is higher than single-vector embeddings.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [ColPali](https://github.com/illuin-tech/colpali) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### GUI grounding agents

**Active in 2026** · Emerged 2024, last active 2026 · Advanced

VLMs trained to locate UI elements and act on screens.

**Key points**

- Output click coordinates or element IDs.
- Benchmarks: ScreenSpot, OSWorld.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [UI-TARS](https://github.com/bytedance/UI-TARS) |
| GitHub | 2024 | [OmniParser](https://github.com/microsoft/OmniParser) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Omni and speech-to-speech models

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Models that take and produce audio natively for low-latency voice agents.

**Key points**

- End-to-end audio avoids ASR-LLM-TTS latency.
- Barge-in and turn detection are key UX problems.

> [!NOTE]
> **State of the art, Sept 2026:** 2026 omni models handle text, image, video and audio input with 1M-token windows.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) |
| GitHub | 2024 | [Moshi](https://github.com/kyutai-labs/moshi) |
| Docs | 2024 | [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) |
| GitHub | 2024 | [Pipecat](https://github.com/pipecat-ai/pipecat) |
| GitHub | 2024 | [LiveKit Agents](https://github.com/livekit/agents) |
| GitHub | 2022 | [Whisper](https://github.com/openai/whisper) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Native image generation and editing

**Active in 2026** · Emerged 2025, last active 2026 · Beginner

LLMs that generate and edit images in the same model with strong text rendering and instruction-following.

**Key points**

- Autoregressive or hybrid with diffusion decoders.
- Multi-reference editing keeps characters and products consistent.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: 4o image generation](https://openai.com/index/introducing-4o-image-generation/) |
| Blog | 2025 | [Google: Gemini 2.5 Flash Image](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---

### Multimodal evaluation

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate

Benchmarks and harnesses for reasoning, charts, documents and video.

**Key points**

- Document, chart, video and grounding need separate evals.
- Contamination is common in popular VQA sets.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [MMMU](https://mmmu-benchmark.github.io) |
| GitHub | 2023 | [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) |
| GitHub | 2024 | [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) |

[↑ Back to top](#12-vision-language-and-multimodal-models)

---
