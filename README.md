# The Modern AI Concept Book

**A curated, dated field guide to the concepts that define modern AI: LLMs, VLMs, agents and harnesses, protocols, post-training, inference, AI hardware standards, evaluation, safety and AI engineering practice. Every concept comes with a plain-language definition, key points, a state-of-the-art note and hand-picked GitHub repos, blogs, papers, docs and specs.**

![Edition](https://img.shields.io/badge/edition-2%20%C2%B7%20Sept%202026-2F5D8A)
![Concepts](https://img.shields.io/badge/concepts-173-2F5D8A)
![Resources](https://img.shields.io/badge/resources-400%2B-2F5D8A)
![Content license](https://img.shields.io/badge/content-CC%20BY%204.0-1F6B4F)
![Code license](https://img.shields.io/badge/code-MIT-1F6B4F)

<!-- stats:start -->
**17 chapters · 173 concepts · 402 unique resources (430 citations) · 12 new in 2026 · 146 active in 2026**
<!-- stats:end -->

Current to **September 20, 2026**.

---

## Why this exists

The AI vocabulary now changes every few months. Terms like *harness engineering*, *MCP*, *forward deployed engineer*, *on-policy distillation*, *UALink* or *NVFP4* show up in job posts, papers and product launches long before anyone explains them together. This book puts them in one place, says plainly what each one means, marks what is new or still changing in 2026, and points to the primary sources so you can go deeper.

It is written for engineers, researchers, product and technical leaders, and anyone ramping up on the field.

## Read it

| Format | File | Best for |
|---|---|---|
| **Markdown (GitHub)** | [`book/`](book/) (one file per chapter) · [`CONCEPT_BOOK.md`](CONCEPT_BOOK.md) (single file) | Reading on GitHub, linking to a concept, pull requests |
| **Interactive HTML** | [`editions/AI_Concept_Book.html`](editions/AI_Concept_Book.html) | Filtering and searching: 6 themes, 5 views, shareable filter links |
| **PDF** | [`editions/AI_Concept_Book.pdf`](editions/AI_Concept_Book.pdf) | Offline reading and printing (with printed indexes) |
| **Word** | [`editions/AI_Concept_Book.docx`](editions/AI_Concept_Book.docx) | Editing, annotating, sharing inside organisations |
| **LaTeX / Overleaf** | [`editions/AI_Concept_Book.tex`](editions/AI_Concept_Book.tex) | Typesetting your own edition (upload to Overleaf, compile with pdfLaTeX) |
| **Spreadsheet catalog** | [`editions/AI_Concept_Book_Catalog.xlsx`](editions/AI_Concept_Book_Catalog.xlsx) | Filtering concepts and resources in Excel or Google Sheets |
| **Data** | [`data/concepts.json`](data/concepts.json) | Building your own tools, quizzes or search |

> [!TIP]
> GitHub shows `.html` files as source. To use the interactive edition, download it and open it in a browser, or enable **GitHub Pages** for this repository and visit `/editions/AI_Concept_Book.html`.

## Contents

<!-- contents:start -->
| # | Chapter | Concepts | New / active in 2026 |
|---|---|---|---|
| 1 | [The Frontier Landscape (September 2026)](book/01-the-frontier-landscape.md) | 5 | 2 / 5 |
| 2 | [Agents and Harnesses](book/02-agents-and-harnesses.md) | 14 | 3 / 11 |
| 3 | [Protocols and Interoperability Standards](book/03-protocols-and-interoperability-standards.md) | 12 | 0 / 10 |
| 4 | [Agentic Coding and Developer Workflow](book/04-agentic-coding-and-developer-workflow.md) | 8 | 1 / 7 |
| 5 | [Context, Memory and Retrieval](book/05-context-memory-and-retrieval.md) | 10 | 0 / 6 |
| 6 | [Reasoning and Post-Training](book/06-reasoning-and-post-training.md) | 12 | 1 / 8 |
| 7 | [Model Architectures](book/07-model-architectures.md) | 13 | 1 / 9 |
| 8 | [Training at Scale and Fine-Tuning](book/08-training-at-scale-and-fine-tuning.md) | 10 | 0 / 8 |
| 9 | [Inference and Serving](book/09-inference-and-serving.md) | 9 | 0 / 7 |
| 10 | [Quantization and Number Formats](book/10-quantization-and-number-formats.md) | 7 | 0 / 5 |
| 11 | [AI Hardware, Interconnect and Datacenter Standards](book/11-ai-hardware-interconnect-and-datacenter-standards.md) | 17 | 1 / 16 |
| 12 | [Vision-Language and Multimodal Models](book/12-vision-language-and-multimodal-models.md) | 10 | 0 / 8 |
| 13 | [Embodied AI, World Models and Generative Media](book/13-embodied-ai-world-models-and-generative-media.md) | 8 | 1 / 8 |
| 14 | [Evaluation and Benchmarks](book/14-evaluation-and-benchmarks.md) | 11 | 1 / 11 |
| 15 | [Safety, Security, Interpretability and Governance](book/15-safety-security-interpretability-and-governance.md) | 15 | 1 / 15 |
| 16 | [Roles, Deployment and AI Engineering Practice](book/16-roles-deployment-and-ai-engineering-practice.md) | 8 | 0 / 8 |
| 17 | [Keep Learning: Curated Resources](book/17-keep-learning-curated-resources.md) | 4 | 0 / 4 |
<!-- contents:end -->

## Browse and filter

The HTML edition filters live by category, year of emergence, 2026 status, level, tag, resource type and resource year. On GitHub, the same cuts are available as pre-built indexes:

| Index | What it answers |
|---|---|
| [By year of emergence](indexes/by-year.md) | What appeared in 2026? What is foundational? |
| [By level](indexes/by-level.md) | Where should a beginner start? |
| [By tag and 2026 status](indexes/by-tag.md) | What is new, open source, an open standard, security-related, enterprise-focused? |
| [Resources by type and year](indexes/resources-by-type.md) | All GitHub repos, all papers, all specs, newest first |
| [Resources by year](indexes/resources-by-year.md) | What was published recently? |
| [Acronyms and aliases](indexes/glossary.md) | What do MCP, A2A, FDE, RLVR, MOPD, MXFP4 mean? |

## How each entry is structured

```text
### Concept name
`Alias` · New in 2026 | Active in 2026 | Established · Emerged <year>, last active <year> · Level · Tags

Definition in plain language.

Key points
- 2 to 4 bullets on how it works and why it matters

> State of the art, Sept 2026: what changed recently (where relevant)

| Type | Year | Resource |    <- GitHub, Blog, Paper, Docs, Spec or Video, with publication or launch year
```

**Status:** *New in 2026* means the concept emerged this year. *Active in 2026* means an older concept that still saw significant change this year.
**Levels:** Beginner, Intermediate, Advanced.
**Resource year:** when an article, paper or spec was published, or when a repository or site launched (approximate for long-running projects).

## Repository layout

```text
.
├── README.md                 this file
├── LICENSE                   CC BY 4.0 for content, MIT for code
├── CONCEPT_BOOK.md           single-file Markdown edition
├── book/                     Markdown edition, one file per chapter
├── indexes/                  browse-by pages (year, level, tag, resources, glossary)
├── editions/                 HTML, PDF, DOCX, LaTeX and XLSX editions
├── data/concepts.json        all content as structured data
├── scripts/                  content sources and generators
│   ├── d1.py … d4.py         concept content (edit these)
│   ├── points.py             extra key points
│   ├── assemble.py           validates content and writes data/concepts.json
│   └── build_*.py / .js      one generator per format
└── build.sh                  rebuild everything
```

## Rebuild the editions

Content lives in `scripts/d1.py` to `scripts/d4.py` (plus `scripts/points.py`). Every format is generated from it, so an edit in one place updates all editions.

```bash
# requirements: Python 3 with openpyxl, Node.js with the docx package, and TeX Live (pdflatex)
pip install openpyxl
npm install docx
./build.sh
```

`assemble.py` validates the content first (unique names, valid years, levels, tags and link types) and stops with a clear message if something is wrong.

## Contributing

Corrections and additions are welcome.

- **Broken or moved link:** open an issue or a pull request that updates the URL in `scripts/d*.py`.
- **New concept:** add a `C(...)` entry to the right chapter in `scripts/d*.py` with a definition, 2–4 key points, and at least two resources, ideally including a primary source (official docs, spec, paper or repository).
- **Style:** plain language, no hype, dates for anything time-sensitive, and your own words rather than quoted text.
- Run `./build.sh` and include the regenerated files in your pull request.

## Caveats

- **Chapter 1 (Frontier Landscape) is a snapshot.** It reflects public reporting as of September 20, 2026 and will date quickly. Check the linked trackers for current releases.
- **Links rot.** Repositories in this space are renamed and moved often. If a link fails, search for the project name, and please report it.
- **Not affiliated** with any company, lab or project mentioned. Product names and trademarks belong to their owners.

## License

- **Content** (text in `book/`, `indexes/`, `CONCEPT_BOOK.md`, `editions/` and `data/`): [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may share and adapt it, including commercially, with attribution.
- **Code** (`scripts/`, `build.sh`): [MIT](LICENSE).
- Linked third-party resources remain under their own licenses.

See [LICENSE](LICENSE) for full terms.

## Cite

```text
@misc{ghosh2026modernaiconceptbook,
  author       = {Ghosh, Shajib},
  title        = {The Modern {AI} Concept Book},
  edition      = {2},
  year         = {2026},
  month        = sep,
  howpublished = {\url{https://github.com/shajibghosh/ai-concept-book}},
  note         = {Licensed under CC BY 4.0.}
}
```
