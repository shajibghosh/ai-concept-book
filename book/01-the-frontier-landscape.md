[Contents](../README.md#contents) · [2. Agents and Harnesses →](02-agents-and-harnesses.md)

# 1. The Frontier Landscape (September 2026)

> A snapshot of where frontier and open-weight models stand as of September 2026. This chapter dates quickly; use the trackers at the end to stay current.

**In this chapter:** [Mythos-class tier and trusted access](#mythos-class-tier-and-trusted-access) · [GPT-6 Astra and the Critical cyber threshold](#gpt-6-astra-and-the-critical-cyber-threshold) · [Tiered access for dual-use models](#tiered-access-for-dual-use-models) · [Open-weight frontier models](#open-weight-frontier-models) · [Model release trackers](#model-release-trackers)

---

### Mythos-class tier and trusted access

`Fable / Mythos` · **New in 2026** · Emerged 2026 · Beginner · Enterprise, Security

Anthropic introduced a capability tier above Opus. The same underlying model ships in two forms: Claude Fable for general use with extra safeguards in biology, cybersecurity and LLM R&D, and Claude Mythos for vetted defenders and partners through Project Glasswing.

**Key points**

- Mythos Preview (April 2026) was first restricted to trusted organisations for cyber defense.
- Fable 5 / Mythos 5 launched June 9, 2026; access was suspended June 12 to comply with US export controls and restored July 1 after the controls were lifted.
- Fable 5.1 and Mythos 5.1 followed on September 1, 2026, with 1M-token context.

> [!NOTE]
> **State of the art, Sept 2026:** Fable 5.1 is Anthropic's generally available flagship; Opus 5 (July 2026) and Sonnet 5 sit below it.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) |
| Docs | 2026 | [Anthropic statement on Fable and Mythos access](https://www.anthropic.com/news/fable-mythos-access) |
| Blog | 2026 | [DataNorth: Claude Fable 5 and Mythos 5 explained](https://datanorth.ai/news/anthropic-releases-claude-fable-5-and-mythos-5) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### GPT-6 Astra and the Critical cyber threshold

`GPT-6` · **New in 2026** · Emerged 2026 · Beginner · Security, Enterprise

OpenAI's first GPT-6 generation model, released September 3, 2026. It is the first model OpenAI classified at the Critical cybersecurity level of its Preparedness Framework, so it launched in phases with stronger safeguards and a trusted-access program for defenders.

**Key points**

- Critical means the model can find and exploit unknown vulnerabilities in hardened systems without step-by-step human guidance.
- Public versions refuse advanced offensive tasks; vetted defenders get more through OpenAI's trusted-access programs.
- Its system card also reported reduced chain-of-thought monitorability, a notable safety signal.

> [!NOTE]
> **State of the art, Sept 2026:** GPT-6 Astra sits above the GPT-5.6 Sol / Terra / Luna tiers.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [OpenAI: Path to Astra](https://openai.com/index/path-to-astra/) |
| Docs | 2026 | [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) |
| Blog | 2026 | [OpenAI: Safety overview of GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/) |
| Blog | 2026 | [InfoQ: Astra is first model rated Critical for cyber](https://www.infoq.com/news/2026/09/gpt-6-astra-critical-cyber/) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### Tiered access for dual-use models

`trusted access` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Security, Enterprise

A 2026 industry pattern: the most cyber-capable models are released in a public version with guardrails and a restricted version for vetted security teams and critical-infrastructure operators.

**Key points**

- Anthropic (Glasswing), OpenAI (trusted access for cyber) and Google (defender-only cyber variants) all adopted versions of it.
- It lets defenders patch vulnerabilities before equivalent capabilities spread.
- Enterprises now need to track which model variant, safeguards and data-retention terms they are using.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) |
| Blog | 2026 | [CSO Online: Astra crosses the Critical cyber threshold](https://www.csoonline.com/article/4218679/openai-launches-gpt-6-astra-its-first-model-to-cross-a-critical-cybersecurity-threshold.html) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### Open-weight frontier models

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Open source / open weights, Cost & efficiency

Open-weight models trail the closed frontier by months, not years. 2026's leading families are mostly large sparse MoEs with 1M-token context and permissive licences.

**Key points**

- DeepSeek V4 (April 2026): Pro has 1.6T total / 49B active parameters, Flash has 284B / 13B, both with 1M context, MIT licence.
- Other active families: Qwen 3.x, Kimi, GLM-5.x, MiniMax, Mistral Large 3, NVIDIA Nemotron 3, Google Gemma 4.
- Open weight does not always mean open source: check licence terms and whether data and code are released.

> [!NOTE]
> **State of the art, Sept 2026:** DeepSeek V4 is the reference open model for long-context efficiency; small open models now run strong coding workloads on a single GPU.

| Type | Year | Resource |
|---|---|---|
| Paper | 2026 | [DeepSeek-V4 technical report](https://arxiv.org/abs/2606.19348) |
| Blog | 2026 | [HF blog: DeepSeek V4 architecture analysis](https://huggingface.co/blog/ResterChed/deepseek-v4-ga-architecture) |
| Docs | 2016 | [Hugging Face models hub](https://huggingface.co/models) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---

### Model release trackers

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Production practice

In 2026 frontier labs shipped new models every few weeks. Trackers and independent benchmark aggregators are the practical way to keep up.

**Key points**

- Compare on your own evals, not headline benchmarks.
- Watch pricing changes as closely as capability changes: cache-read and small-tier prices fell sharply in 2026.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Artificial Analysis](https://artificialanalysis.ai) |
| Docs | 2024 | [Epoch AI benchmarking hub](https://epoch.ai/benchmarks) |
| Docs | 2023 | [LMArena](https://lmarena.ai) |
| Docs | 2023 | [OpenRouter model list](https://openrouter.ai/models) |

[↑ Back to top](#1-the-frontier-landscape-september-2026)

---
