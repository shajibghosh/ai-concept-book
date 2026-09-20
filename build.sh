#!/usr/bin/env bash
# Rebuild every edition from the content files in scripts/.
# Requires: python3 (openpyxl), node (npm i docx), pdflatex (TeX Live). Run from the repo root.
set -euo pipefail
mkdir -p editions build/tex
python3 scripts/assemble.py            # content (scripts/d*.py, points.py) -> data/concepts.json
python3 scripts/build_md.py .          # Markdown edition + indexes
python3 scripts/build_html.py          # editions/AI_Concept_Book.html
python3 scripts/build_xlsx.py          # editions/AI_Concept_Book_Catalog.xlsx
node scripts/build_docx.js             # editions/AI_Concept_Book.docx
python3 scripts/build_tex.py           # build/tex/main.tex
( cd build/tex && for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null; done )
cp build/tex/main.pdf editions/AI_Concept_Book.pdf
cp build/tex/main.tex editions/AI_Concept_Book.tex
( cd build/tex && rm -f ../../editions/AI_Concept_Book_Overleaf.zip && zip -q ../../editions/AI_Concept_Book_Overleaf.zip main.tex )
echo "Done. See editions/ and book/."
