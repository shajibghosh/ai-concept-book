[Contents](../README.md#contents) · [← 13. Embodied AI, World Models and Generative Media](13-embodied-ai-world-models-and-generative-media.md) · [15. Safety, Security, Interpretability and Governance →](15-safety-security-interpretability-and-governance.md)

# 14. Evaluation and Benchmarks

> Evals tell you whether a model, prompt or harness change helped. An eval harness runs tasks, collects outputs and grades them.

**In this chapter:** [Eval harnesses](#eval-harnesses) · [Harness sensitivity of benchmarks](#harness-sensitivity-of-benchmarks) · [LLM-as-a-judge](#llm-as-a-judge) · [Agentic coding benchmarks](#agentic-coding-benchmarks) · [ARC-AGI-3 and interactive reasoning](#arc-agi-3-and-interactive-reasoning) · [Agent and tool-use benchmarks](#agent-and-tool-use-benchmarks) · [Frontier knowledge benchmarks](#frontier-knowledge-benchmarks) · [Economic value evals](#economic-value-evals) · [Task time horizon](#task-time-horizon) · [Leaderboards and trackers](#leaderboards-and-trackers) · [Contamination and saturation](#contamination-and-saturation)

---

### Eval harnesses

**Active in 2026** · Emerged 2021, last active 2026 · Intermediate · Production practice, Open source / open weights

Frameworks that define tasks, run models or agents against them in sandboxes, and score results reproducibly.

**Key points**

- Inspect supports agents, sandboxes and scorers out of the box.
- Pin versions: prompts, tools, seeds and graders.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2021 | [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) |
| GitHub | 2024 | [Inspect AI (UK AISI)](https://github.com/UKGovernmentBEIS/inspect_ai) |
| GitHub | 2024 | [inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) |
| GitHub | 2024 | [lighteval](https://github.com/huggingface/lighteval) |
| GitHub | 2023 | [promptfoo](https://github.com/promptfoo/promptfoo) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Harness sensitivity of benchmarks

**Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Research frontier

Scores depend heavily on the agent harness used to run the model, so the same model can post very different numbers.

**Key points**

- ARC Prize reported GPT-6 Astra at 62.7% on ARC-AGI-3 with its standard harness, and 99.9% with a provider harness that preserves hidden reasoning between turns.

> [!NOTE]
> **State of the art, Sept 2026:** Always record harness, tools, budget and reasoning settings with any score.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [ARC Prize: Announcing ARC-AGI-3](https://arcprize.org/blog/arc-agi-3-launch) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### LLM-as-a-judge

**Active in 2026** · Emerged 2023, last active 2026 · Beginner · Production practice

Using a model with a rubric to grade open-ended outputs; needs calibration against humans.

**Key points**

- Use pairwise comparisons and specific rubrics.
- Measure judge agreement with humans on a sample.

| Type | Year | Resource |
|---|---|---|
| Paper | 2023 | [Judging LLM-as-a-judge](https://arxiv.org/abs/2306.05685) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Agentic coding benchmarks

`SWE-bench, Terminal-Bench` · **Active in 2026** · Emerged 2023, last active 2026 · Beginner

Real repository issues and terminal tasks graded by tests.

**Key points**

- Verified subsets remove broken or ambiguous tasks.
- Watch for contamination of public repositories.

> [!NOTE]
> **State of the art, Sept 2026:** SWE-bench Verified is near saturation (mid-90s percent for top 2026 models); harder variants like SWE-bench Pro and Terminal-Bench matter more.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [SWE-bench](https://www.swebench.com) |
| Docs | 2025 | [SWE-bench Pro](https://scale.com/leaderboard/swe_bench_pro_public) |
| Docs | 2025 | [Terminal-Bench](https://www.tbench.ai) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### ARC-AGI-3 and interactive reasoning

`ARC-AGI-3` · **New in 2026** · Emerged 2026 · Intermediate · Research frontier

The first interactive ARC benchmark (March 2026): hundreds of hand-designed game environments with no instructions or stated goals. Agents must explore, infer rules and goals, and carry learning across levels.

**Key points**

- At launch humans solved 100% while frontier models scored under 1%.
- By September 2026 top models reached large scores depending on harness.

| Type | Year | Resource |
|---|---|---|
| Blog | 2026 | [ARC Prize: Announcing ARC-AGI-3](https://arcprize.org/blog/arc-agi-3-launch) |
| Docs | 2019 | [ARC Prize](https://arcprize.org) |
| Blog | 2026 | [DataCamp: ARC-AGI-3 explained](https://www.datacamp.com/blog/arc-agi-3) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Agent and tool-use benchmarks

**Active in 2026** · Emerged 2024, last active 2026 · Intermediate

Tasks in simulated customer service, operating systems and the web.

**Key points**

- tau-bench tests policy-following with simulated users.
- Pass^k measures consistency across repeated attempts.

| Type | Year | Resource |
|---|---|---|
| GitHub | 2025 | [tau2-bench](https://github.com/sierra-research/tau2-bench) |
| Docs | 2024 | [OSWorld](https://os-world.github.io) |
| Blog | 2025 | [BrowseComp](https://openai.com/index/browsecomp/) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Frontier knowledge benchmarks

`HLE, GPQA, FrontierMath` · **Active in 2026** · Emerged 2023, last active 2026 · Intermediate

Hard expert questions designed to resist saturation.

**Key points**

- Designed by domain experts to resist search.
- Saturation arrives faster each generation.

| Type | Year | Resource |
|---|---|---|
| Docs | 2025 | [Humanity's Last Exam](https://lastexam.ai) |
| GitHub | 2023 | [GPQA](https://github.com/idavidrein/gpqa) |
| Docs | 2024 | [FrontierMath](https://epoch.ai/frontiermath) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Economic value evals

`GDPval` · **Active in 2026** · Emerged 2025, last active 2026 · Beginner · Enterprise

Measure performance on real work products from many occupations, graded by professionals.

**Key points**

- Tasks come with real deliverables (documents, spreadsheets, plans).
- Graded blind against expert work.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [OpenAI: GDPval](https://openai.com/index/gdpval/) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Task time horizon

`METR horizon` · **Active in 2026** · Emerged 2025, last active 2026 · Intermediate · Research frontier

The length of task (in expert human time) a model completes with 50% success; it has been doubling every several months.

**Key points**

- Useful for forecasting when tasks of a given length become automatable.
- Reliability at 80% success lags the 50% horizon.

| Type | Year | Resource |
|---|---|---|
| Blog | 2025 | [METR: Measuring long tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Leaderboards and trackers

**Active in 2026** · Emerged 2023, last active 2026 · Beginner

Crowd preference arenas and independent aggregators of scores, price and speed.

**Key points**

- Arena Elo reflects preference, not correctness.
- Cross-check with task-specific benchmarks.

| Type | Year | Resource |
|---|---|---|
| Docs | 2023 | [LMArena](https://lmarena.ai) |
| Docs | 2024 | [Epoch AI benchmarks](https://epoch.ai/benchmarks) |
| Docs | 2024 | [Artificial Analysis](https://artificialanalysis.ai) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---

### Contamination and saturation

**Active in 2026** · Emerged 2023, last active 2026 · Intermediate · Research frontier

Leaked test data inflates scores and benchmarks saturate within months; private holdouts and live evals counter this.

**Key points**

- Use canary strings and private test sets.
- Prefer dynamic benchmarks refreshed over time.

| Type | Year | Resource |
|---|---|---|
| Docs | 2024 | [Epoch AI benchmarks](https://epoch.ai/benchmarks) |

[↑ Back to top](#14-evaluation-and-benchmarks)

---
