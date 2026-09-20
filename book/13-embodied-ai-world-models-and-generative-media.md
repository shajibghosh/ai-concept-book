[Contents](../README.md#contents) · [← 12. Vision-Language and Multimodal Models](12-vision-language-and-multimodal-models.md) · [14. Evaluation and Benchmarks →](14-evaluation-and-benchmarks.md)

# 13. Embodied AI, World Models and Generative Media

> Models that act in the physical world, simulate it, or generate images and video of it.

**In this chapter:** [Vision-language-action models](#vision-language-action-models) · [World action models](#world-action-models) · [World models](#world-models) · [JEPA](#jepa) · [Robot simulation and sim-to-real](#robot-simulation-and-sim-to-real) · [Diffusion transformers and flow matching](#diffusion-transformers-and-flow-matching) · [Video generation](#video-generation) · [AI for science and algorithm discovery](#ai-for-science-and-algorithm-discovery)

---

### Vision-language-action models

`VLA` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Research frontier, Open source / open weights

VLMs extended to output robot actions, trained on cross-embodiment data.

**Key points**

- Architectures split between dual-system (slow VLM reasoning plus fast action policy), think-then-act, and flow/diffusion action heads.
- Small VLAs (SmolVLA, about 450M parameters) are competitive on many tasks.

> [!NOTE]
> **State of the art, Sept 2026:** Leading 2026 families: Physical Intelligence pi-series, NVIDIA GR00T N1.7, Gemini Robotics 1.5, Figure Helix.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [openpi (Physical Intelligence)](https://github.com/Physical-Intelligence/openpi) |
| GitHub | 2025 | [NVIDIA Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T) |
| GitHub | 2024 | [OpenVLA](https://github.com/openvla/openvla) |
| GitHub | 2024 | [LeRobot](https://github.com/huggingface/lerobot) |
| Docs | 2025 | [Gemini Robotics](https://deepmind.google/models/gemini-robotics/) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### World action models

`WAM` · **New in 2026** · Emerged 2026 · Advanced · Research frontier

Models that jointly imagine future observations and the actions that lead to them, merging a world model and a policy.

**Key points**

- NVIDIA's DreamZero research underpins the previewed GR00T N2.
- Claimed better generalisation to unseen tasks from modest teleoperation data.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [Metavert: World models for robotics](https://metavert.io/world-models-for-robotics) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### World models

**Active in 2026** · Emerged 2018, last active 2026 · Intermediate · Research frontier

Models that predict how an environment evolves under actions, for planning, simulation and interactive 3D worlds.

**Key points**

- Genie-style models generate playable 3D environments from prompts.
- Used for training agents and robots in simulation.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [DeepMind: Genie 3](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/) |
| GitHub | 2025 | [NVIDIA Cosmos](https://github.com/nvidia-cosmos) |
| Docs | 2025 | [World Labs Marble](https://marble.worldlabs.ai) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### JEPA

`Joint-Embedding Predictive Architecture` · **Active in 2026** · Emerged 2022, last active 2026 · Advanced · Research frontier

Predict representations of missing input rather than pixels to learn world knowledge efficiently from video.

**Key points**

- Avoids wasting capacity on unpredictable pixel details.
- V-JEPA 2 adds action-conditioned planning with little robot data.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [V-JEPA 2](https://github.com/facebookresearch/vjepa2) |
| Blog | 2026 | [VentureBeat: AI research trends for 2026](https://venturebeat.com/technology/four-ai-research-trends-enterprise-teams-should-watch-in-2026) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### Robot simulation and sim-to-real

**Active in 2026** · Emerged 2012, last active 2026 · Intermediate · Open source / open weights

Physics simulators for training policies at scale before transferring to real robots.

**Key points**

- Domain randomisation bridges the reality gap.
- GPU-parallel simulation runs thousands of environments at once.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2024 | [Isaac Lab](https://github.com/isaac-sim/IsaacLab) |
| GitHub | 2021 | [MuJoCo](https://github.com/google-deepmind/mujoco) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### Diffusion transformers and flow matching

`DiT` · **Active in 2026** · Emerged 2022, last active 2026 · Advanced

The backbone of modern image and video generators.

**Key points**

- Flow matching learns straight paths from noise to data.
- Few-step distillation enables real-time generation.

| Type | Year | Resource |
|---|---|---|
| Paper | 2022 | [DiT](https://arxiv.org/abs/2212.09748) |
| Paper | 2022 | [Flow matching](https://arxiv.org/abs/2210.02747) |
| GitHub | 2024 | [FLUX](https://github.com/black-forest-labs/flux) |
| GitHub | 2023 | [ComfyUI](https://github.com/comfyanonymous/ComfyUI) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### Video generation

**Active in 2026** · Emerged 2024, last active 2026 · Beginner

Text- and image-to-video with synchronised audio and increasingly consistent physics.

**Key points**

- Native audio, longer clips and camera control arrived in 2025-26.
- Provenance marks (C2PA, SynthID) are standard on major services.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: Sora 2](https://openai.com/index/sora-2/) |
| Docs | 2024 | [Google Veo](https://deepmind.google/models/veo/) |
| GitHub | 2025 | [Wan 2.2](https://github.com/Wan-Video/Wan2.2) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---

### AI for science and algorithm discovery

**Active in 2026** · Emerged 2020, last active 2026 · Intermediate · Research frontier

LLM-driven evolutionary search and specialised models finding new algorithms, proofs and structures.

**Key points**

- In 2026 open communities of agents set new records on math problems through shared submissions and verifiers.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [DeepMind: AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) |
| GitHub | 2025 | [OpenEvolve](https://github.com/codelion/openevolve) |
| GitHub | 2024 | [AlphaFold 3](https://github.com/google-deepmind/alphafold3) |
| Paper | 2026 | [EinsteinArena: collective agent discovery](https://arxiv.org/abs/2606.10402) |

[↑ Back to top](#13-embodied-ai-world-models-and-generative-media)

---
