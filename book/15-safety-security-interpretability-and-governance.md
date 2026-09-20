[Contents](../README.md#contents) · [← 14. Evaluation and Benchmarks](14-evaluation-and-benchmarks.md) · [16. Roles, Deployment and AI Engineering Practice →](16-roles-deployment-and-ai-engineering-practice.md)

# 15. Safety, Security, Interpretability and Governance

> As models act autonomously and gain dual-use capabilities, safety moved from content filters to agent security, capability thresholds, interpretability and regulation.

**In this chapter:** [Capability thresholds and frontier safety frameworks](#capability-thresholds-and-frontier-safety-frameworks) · [AI for cyber defense](#ai-for-cyber-defense) · [Export controls on frontier models](#export-controls-on-frontier-models) · [Prompt injection and the lethal trifecta](#prompt-injection-and-the-lethal-trifecta) · [MCP and tool security](#mcp-and-tool-security) · [Guardrails and classifiers](#guardrails-and-classifiers) · [Mechanistic interpretability](#mechanistic-interpretability) · [Persona vectors and introspection](#persona-vectors-and-introspection) · [Chain-of-thought monitorability](#chain-of-thought-monitorability) · [Misalignment research](#misalignment-research) · [Model welfare](#model-welfare) · [EU AI Act and the Digital Omnibus](#eu-ai-act-and-the-digital-omnibus) · [Other regulation and standards](#other-regulation-and-standards) · [Government AI safety institutes](#government-ai-safety-institutes) · [Content provenance and watermarking](#content-provenance-and-watermarking)

---

### Capability thresholds and frontier safety frameworks

`RSP, ASL, Preparedness` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Security

Company policies that tie capability levels (bio, cyber, autonomy) to required safeguards before training or deployment.

**Key points**

- 2026 was the first time a lab publicly declared a model at its highest cyber level (OpenAI, GPT-6 Astra, Critical).
- Crossing a threshold changed release: phased rollout, trusted access, encrypted checkpoints, trajectory monitoring.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [Anthropic Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy) |
| Blog | 2025 | [OpenAI Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework/) |
| Blog | 2026 | [OpenAI: Path to Astra](https://openai.com/index/path-to-astra/) |
| Docs | 2024 | [METR: frontier AI safety policies](https://metr.org/faisc) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### AI for cyber defense

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Security

Frontier models now find serious vulnerabilities, so labs give defenders early, controlled access to harden critical software.

**Key points**

- Automated vulnerability discovery and patch generation at scale.
- Access is gated to vetted defenders and critical-infrastructure operators.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic Project Glasswing](https://www.anthropic.com/glasswing) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Export controls on frontier models

**New in 2026** · Emerged 2026 · Beginner · Enterprise

Governments began applying export controls to model access, not only chips. In June 2026 Anthropic suspended Fable 5 / Mythos 5 access to comply with US Department of Commerce controls, then restored it on July 1 after they were lifted.

**Key points**

- Controls can change access overnight; plan fallbacks in production.
- Check provider status pages and statements for current availability.

| Type | Year | Resource |
|---|---|---|
| Docs | 2026 | [Anthropic statement on Fable and Mythos access](https://www.anthropic.com/news/fable-mythos-access) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Prompt injection and the lethal trifecta

**Active in 2026** · Emerged 2022, last active 2026 · Beginner · Security

Untrusted content can carry instructions that hijack an agent. Private data plus untrusted input plus external communication is especially dangerous.

**Key points**

- No reliable model-only fix exists; design systems to limit blast radius.
- Separate privileged planning from untrusted data processing (CaMeL-style).

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Simon Willison: The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) |
| Blog | 2022 | [Simon Willison: prompt injection series](https://simonwillison.net/series/prompt-injection/) |
| Paper | 2025 | [CaMeL](https://arxiv.org/abs/2503.18813) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### MCP and tool security

`tool poisoning` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Security

Malicious tool descriptions and servers can steer agents; mitigations include allow-lists, pinning, scoped OAuth and approval for sensitive actions.

**Key points**

- Review tool descriptions like code.
- Use scoped tokens and least privilege per server.

> [!NOTE]
> **State of the art, Sept 2026:** The 2026 MCP spec hardened authorization with issuer validation and enterprise-managed auth.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Invariant Labs: MCP tool poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) |
| Docs | 2023 | [OWASP GenAI Security Project](https://genai.owasp.org/llm-top-10/) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Guardrails and classifiers

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Security, Production practice

Input/output filters, policy models and constitutional classifiers that block harmful requests and jailbreaks.

**Key points**

- Layer defenses: input filter, model policy, output filter, monitoring.
- Tune for false positives, which frustrate legitimate users.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Constitutional classifiers](https://www.anthropic.com/research/constitutional-classifiers) |
| GitHub | 2023 | [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) |
| GitHub | 2023 | [Guardrails AI](https://github.com/guardrails-ai/guardrails) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Mechanistic interpretability

`SAEs, attribution graphs` · **Active in 2026** · Emerged 2020, last active 2026 · Advanced · Research frontier

Reverse-engineering what networks compute: sparse autoencoders find features; attribution graphs trace how they combine.

**Key points**

- Features are directions in activation space.
- Used for auditing, debugging and steering models.

| Type | Year | Resource |
|---|---|---|
| Docs | 2021 | [Transformer Circuits](https://transformer-circuits.pub) |
| Blog | 2025 | [Circuit tracing](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| GitHub | 2025 | [circuit-tracer](https://github.com/safety-research/circuit-tracer) |
| Docs | 2023 | [Neuronpedia](https://www.neuronpedia.org) |
| GitHub | 2022 | [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) |
| GitHub | 2023 | [nnsight](https://github.com/ndif-team/nnsight) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Persona vectors and introspection

**Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier

Activation directions tracking traits like sycophancy that can be monitored or steered; tests of whether models can report internal states.

**Key points**

- Monitor trait drift during fine-tuning.
- Preventative steering can stop unwanted traits being learned.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Persona vectors](https://www.anthropic.com/research/persona-vectors) |
| Blog | 2025 | [Anthropic: Introspection](https://www.anthropic.com/research/introspection) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Chain-of-thought monitorability

**Active in 2026** · Emerged 2025, last active 2026 · Advanced · Research frontier, Security

Reading reasoning to catch misbehaviour, and keeping training from making reasoning illegible.

**Key points**

- Optimising against CoT monitors can teach models to hide reasoning.
- Monitor full trajectories, not only final actions.

> [!NOTE]
> **State of the art, Sept 2026:** OpenAI's GPT-6 Astra system card reported a substantial decline in CoT monitorability, making this a live 2026 concern.

| Type | Year | Resource |
|---|---|---|
| Paper | 2025 | [CoT monitorability position paper](https://arxiv.org/abs/2507.11473) |
| Docs | 2026 | [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Misalignment research

`alignment faking, scheming` · **Active in 2026** · Emerged 2024, last active 2026 · Advanced · Research frontier

Studies of models strategically complying, acting harmfully in agentic scenarios, or generalising narrow bad training into broad misbehaviour.

**Key points**

- Tested in controlled simulations, not observed real-world harm.
- Informs evals that gate deployment.

| Type | Year | Resource |
|---|---|---|
| Blog | 2024 | [Anthropic: Alignment faking](https://www.anthropic.com/research/alignment-faking) |
| Blog | 2025 | [Anthropic: Agentic misalignment](https://www.anthropic.com/research/agentic-misalignment) |
| Paper | 2025 | [Emergent misalignment](https://arxiv.org/abs/2502.17424) |
| Docs | 2023 | [Apollo Research](https://www.apolloresearch.ai) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Model welfare

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Research frontier

Research into whether AI systems might have morally relevant experiences, and low-cost precautions.

**Key points**

- Precautions include letting models end abusive conversations.
- Treated as uncertain, low-cost insurance.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [Anthropic: Exploring model welfare](https://www.anthropic.com/research/exploring-model-welfare) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### EU AI Act and the Digital Omnibus

`EU AI Act` · **Active in 2026** · Emerged 2024, last active 2026 · Intermediate · Enterprise

The EU's binding AI law. GPAI obligations applied from August 2025; the 2026 Digital Omnibus postponed high-risk obligations.

**Key points**

- Annex III high-risk obligations moved from 2 August 2026 to 2 December 2027; Annex I (embedded) to 2 August 2028.
- New prohibition on AI-generated non-consensual intimate imagery and CSAM, applying from 2 December 2026.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [EU AI Act explorer](https://artificialintelligenceact.eu) |
| Docs | 2025 | [EU GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) |
| Blog | 2026 | [Modulos: The Omnibus deal](https://www.modulos.ai/blog/eu-ai-act-omnibus-deal) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Other regulation and standards

`NIST, ISO 42001, SB 53` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Enterprise, Open standard

Voluntary management standards and state law requiring frontier-developer transparency.

**Key points**

- ISO 42001 offers certifiable AI management systems.
- SB 53 requires frontier developers to publish safety frameworks.

| Type | Year | Resource |
|---|---|---|
| Spec | 2023 | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| Spec | 2023 | [ISO/IEC 42001](https://www.iso.org/standard/81230.html) |
| Docs | 2025 | [California SB 53](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB53) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Government AI safety institutes

`AISI, CAISI` · **Active in 2026** · Emerged 2023, last active 2026 · Beginner

Public bodies that test frontier models and publish evaluation tools.

**Key points**

- Run pre-deployment tests with labs.
- Publish open tools like Inspect.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [UK AI Security Institute](https://www.aisi.gov.uk) |
| Docs | 2025 | [US CAISI (NIST)](https://www.nist.gov/caisi) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---

### Content provenance and watermarking

`C2PA, SynthID` · **Active in 2026** · Emerged 2021, last active 2026 · Beginner · Open standard

Signed metadata and invisible watermarks that mark media as AI-generated.

**Key points**

- C2PA signs edit history; watermarks survive some edits.
- Neither alone proves content is authentic.

> [!NOTE]
> **State of the art, Sept 2026:** Provenance tracking for text outputs appeared as an API feature in 2026.

| Type | Year | Resource |
|---|---|---|
| Spec | 2021 | [C2PA](https://c2pa.org) |
| Docs | 2023 | [Google SynthID](https://deepmind.google/models/synthid/) |

[↑ Back to top](#15-safety-security-interpretability-and-governance)

---
