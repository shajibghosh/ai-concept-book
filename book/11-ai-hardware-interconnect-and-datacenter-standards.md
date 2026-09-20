[Contents](../README.md#contents) · [← 10. Quantization and Number Formats](10-quantization-and-number-formats.md) · [12. Vision-Language and Multimodal Models →](12-vision-language-and-multimodal-models.md)

# 11. AI Hardware, Interconnect and Datacenter Standards

> The unit of compute is now a rack or pod. Open standards are forming to connect accelerators from different vendors.

**In this chapter:** [Rack-scale systems](#rack-scale-systems) · [AMD Helios and Open Rack Wide](#amd-helios-and-open-rack-wide) · [Scale-up vs. scale-out networking](#scale-up-vs-scale-out-networking) · [UALink](#ualink) · [ESUN and SUE](#esun-and-sue) · [Ultra Ethernet](#ultra-ethernet) · [NVLink and NVLink Fusion](#nvlink-and-nvlink-fusion) · [CXL, PCIe and UCIe](#cxl-pcie-and-ucie) · [High-bandwidth memory](#high-bandwidth-memory) · [Advanced packaging](#advanced-packaging) · [Co-packaged optics](#co-packaged-optics) · [Custom accelerators](#custom-accelerators) · [AI factories, power and cooling](#ai-factories-power-and-cooling) · [Kernel languages and compilers](#kernel-languages-and-compilers) · [Collective communication](#collective-communication) · [Model interchange formats](#model-interchange-formats) · [Hardware benchmarks](#hardware-benchmarks)

---

### Rack-scale systems

`NVL72` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Dozens of accelerators in one liquid-cooled rack joined by a single scale-up domain, behaving like one giant GPU.

**Key points**

- GB200/GB300 NVL72 (Blackwell) dominated 2025.
- Vera Rubin NVL72 (72 Rubin GPUs, 36 Vera CPUs, NVLink 6, HBM4) began shipping to major clouds in 2026.

> [!NOTE]
> **State of the art, Sept 2026:** NVIDIA quotes about 3.6 EF FP4 inference per Vera Rubin rack; Rubin Ultra (Kyber rack) is planned for H2 2027.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) |
| Blog | 2026 | [ServeTheHome: Rubin platform at CES 2026](https://www.servethehome.com/nvidia-launches-next-generation-rubin-ai-compute-platform-at-ces-2026/) |
| Blog | 2026 | [DCD: Vera Rubin superchip](https://www.datacenterdynamics.com/en/news/nvidia-announces-vera-rubin-superchip-for-late-2026/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### AMD Helios and Open Rack Wide

`MI455X` · **New in 2026** · Emerged 2026 · Intermediate · Open standard

AMD's rack-scale platform built on the Open Rack Wide standard co-submitted with Meta to OCP, pairing MI455X GPUs (432 GB HBM4 each) with EPYC Venice CPUs.

**Key points**

- Competes on memory capacity rather than raw FLOPs.
- Large 2026 deployments announced with OpenAI and Oracle.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [AMD Instinct](https://www.amd.com/en/products/accelerators/instinct.html) |
| Blog | 2026 | [GPU Insights: Rubin vs Helios](https://gpuinsights.net/nvidia-rubin-vs-amd-helios-mi450-2026/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Scale-up vs. scale-out networking

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Foundational

Scale-up links accelerators inside a pod with memory-semantic, sub-microsecond links; scale-out connects pods over Ethernet or InfiniBand.

**Key points**

- Scale-up carries tensor and expert parallel traffic.
- Scale-out carries data-parallel gradients and inter-pod traffic.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Synopsys: Ethernet standards for scale-up AI](https://www.synopsys.com/articles/ethernet-standards-scale-up-ai.html) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### UALink

`Ultra Accelerator Link` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Open standard

An open memory-semantic interconnect for pods of up to 1,024 accelerators, backed by AMD, Google, Microsoft, Meta, AWS and 100+ members.

**Key points**

- UALink 200G 1.0 (April 2025); version 2.0 published April 2026.
- First UALink switches targeted late 2026.

| Type | Year | Resource |
|---|---|---|
| Spec | 2024 | [UALink Consortium](https://ualinkconsortium.org) |
| Docs | 2024 | [UALink overview](https://en.wikipedia.org/wiki/UALink) |
| Blog | 2026 | [UALink white paper (2026)](https://ualinkconsortium.org/wp-content/uploads/2026/01/UALink_White_Paper_Publication_Candidate_FINAL_VERSION.pdf) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### ESUN and SUE

`Ethernet for Scale-Up Networking` · **Active in 2026** · Emerged 2025, last active 2026 · Advanced · Open standard

An OCP workstream (October 2025) standardising Ethernet's lower layers for scale-up AI; Broadcom's SUE evolved into a transport that sits on top.

**Key points**

- Backed by AMD, Arista, ARM, Broadcom, Cisco, HPE, Marvell, Meta, Microsoft, NVIDIA, OpenAI and Oracle.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Arista: The sun rises on scale-up Ethernet](https://blogs.arista.com/blog/the-sun-rises-on-scale-up-ethernet) |
| Blog | 2026 | [Synopsys: ESUN explained](https://www.synopsys.com/blogs/chip-design/esun-ethernet-ai-scale-up-networking.html) |
| Blog | 2026 | [650 Group: Ethernet in scale-up](https://650group.com/blog/in-the-ai-era-ethernet-set-to-surge-in-scale-out-and-ramp-in-scale-up/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Ultra Ethernet

`UEC` · **Active in 2026** · Emerged 2023, last active 2026 · Advanced · Open standard

A consortium spec modernising Ethernet transport (packet spraying, congestion control, telemetry) for scale-out AI.

**Key points**

- UEC 1.0 specification released in 2025.
- Targets InfiniBand-class performance on Ethernet.

| Type | Year | Resource |
|---|---|---|
| Spec | 2023 | [Ultra Ethernet Consortium](https://ultraethernet.org) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### NVLink and NVLink Fusion

**Active in 2026** · Emerged 2016, last active 2026 · Intermediate

NVIDIA's proprietary scale-up fabric, licensed through NVLink Fusion to third-party CPUs and accelerators.

**Key points**

- NVLink switches give all-to-all bandwidth inside a rack.
- Fusion opens the fabric to custom silicon partners.

> [!NOTE]
> **State of the art, Sept 2026:** NVLink 6 ships with Rubin.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [NVLink Fusion](https://www.nvidia.com/en-us/data-center/nvlink-fusion/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### CXL, PCIe and UCIe

**Active in 2026** · Emerged 2019, last active 2026 · Advanced · Open standard

Coherent memory pooling (CXL), host I/O (PCIe) and chiplet die-to-die links (UCIe).

**Key points**

- CXL memory expansion adds capacity for KV caches and embeddings.
- UCIe lets vendors mix chiplets from different sources.

| Type | Year | Resource |
|---|---|---|
| Spec | 2019 | [CXL Consortium](https://computeexpresslink.org) |
| Spec | 1992 | [PCI-SIG](https://pcisig.com) |
| Spec | 2022 | [UCIe](https://www.uciexpress.org) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### High-bandwidth memory

`HBM3E, HBM4` · **Active in 2026** · Emerged 2013, last active 2026 · Intermediate

Stacked DRAM beside the accelerator; capacity and bandwidth usually limit decoding speed more than FLOPs.

**Key points**

- HBM4 doubles interface width versus HBM3.
- HBM supply is a key constraint on accelerator shipments.

> [!NOTE]
> **State of the art, Sept 2026:** HBM4 arrived in 2026 with Rubin and MI455X; HBM4E is on 2027 roadmaps.

| Type | Year | Resource |
|---|---|---|
| Docs | 2013 | [High Bandwidth Memory overview](https://en.wikipedia.org/wiki/High_Bandwidth_Memory) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Advanced packaging

`CoWoS` · **Active in 2026** · Emerged 2012, last active 2026 · Advanced

2.5D/3D packaging that places compute dies and HBM on a shared interposer; a recurring supply bottleneck.

**Key points**

- Interposer size limits how much HBM fits beside a die.
- Packaging capacity expansions track AI demand closely.

| Type | Year | Resource |
|---|---|---|
| Docs | 2012 | [TSMC CoWoS](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Co-packaged optics

`CPO` · **Active in 2026** · Emerged 2025, last active 2026 · Advanced

Optical transceivers moved into the switch package to cut power and raise bandwidth.

**Key points**

- Shorter electrical paths mean lower power per bit.
- Early deployment in switches; accelerators later.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [NVIDIA silicon photonics](https://www.nvidia.com/en-us/networking/products/silicon-photonics/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Custom accelerators

`TPU, Trainium, MTIA` · **Active in 2026** · Emerged 2016, last active 2026 · Intermediate

Hyperscaler and challenger chips competing with GPUs, often optimised for inference.

**Key points**

- Hyperscalers design chips for their own inference fleets.
- Software ecosystem maturity is the main adoption hurdle.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Google: Ironwood TPU](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/) |
| Docs | 2020 | [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) |
| Docs | 2016 | [Cerebras](https://www.cerebras.ai) |
| Docs | 2016 | [Groq](https://groq.com) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### AI factories, power and cooling

`800 VDC` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Gigawatt-scale datacenters with direct liquid cooling and higher-voltage DC power; power is now a primary constraint.

**Key points**

- Racks exceed 100 kW; next-gen racks approach 600 kW.
- Grid access and power purchase deals shape site selection.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [NVIDIA: 800 V HVDC architecture](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/) |
| Spec | 2011 | [Open Compute Project](https://www.opencompute.org) |
| Blog | 2025 | [OpenAI: Stargate](https://openai.com/index/announcing-the-stargate-project/) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Kernel languages and compilers

`Triton, CUTLASS, ROCm, XLA` · **Active in 2026** · Emerged 2019, last active 2026 · Advanced · Open source / open weights

Tools for writing fast accelerator code without raw CUDA, and portable compilers.

**Key points**

- Triton makes GPU kernels writable in Python-like code.
- Portable stacks reduce lock-in to one vendor.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2019 | [Triton](https://github.com/triton-lang/triton) |
| GitHub | 2017 | [CUTLASS / CuTe](https://github.com/NVIDIA/cutlass) |
| GitHub | 2024 | [ThunderKittens](https://github.com/HazyResearch/ThunderKittens) |
| GitHub | 2025 | [TileLang](https://github.com/tile-ai/tilelang) |
| GitHub | 2016 | [ROCm](https://github.com/ROCm/ROCm) |
| GitHub | 2022 | [OpenXLA](https://github.com/openxla/xla) |
| GitHub | 2023 | [Modular (Mojo, MAX)](https://github.com/modular/modular) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Collective communication

`NCCL` · **Active in 2026** · Emerged 2016, last active 2026 · Advanced

Libraries for all-reduce, all-gather and all-to-all across GPUs.

**Key points**

- Topology-aware algorithms (rings, trees) matter at scale.
- MoE all-to-all is latency-sensitive.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2016 | [NCCL](https://github.com/NVIDIA/nccl) |
| GitHub | 2025 | [DeepEP](https://github.com/deepseek-ai/DeepEP) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Model interchange formats

`ONNX, safetensors` · Established · Emerged 2017, last active 2025 · Beginner · Open standard

Standard, safe formats for moving models between frameworks; safetensors avoids pickle code execution.

**Key points**

- ONNX targets cross-runtime deployment.
- safetensors is the default on Hugging Face.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2017 | [ONNX](https://github.com/onnx/onnx) |
| GitHub | 2022 | [safetensors](https://github.com/huggingface/safetensors) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---

### Hardware benchmarks

`MLPerf` · **Active in 2026** · Emerged 2018, last active 2026 · Beginner

Industry-standard training and inference benchmarks.

**Key points**

- Compare systems on the same model and accuracy target.
- Vendor-submitted; read the fine print on configurations.

| Type | Year | Resource |
|---|---|---|
| Docs | 2018 | [MLCommons benchmarks](https://mlcommons.org/benchmarks/) |
| Docs | 2023 | [Epoch AI: ML hardware data](https://epoch.ai/data/machine-learning-hardware) |

[↑ Back to top](#11-ai-hardware-interconnect-and-datacenter-standards)

---
