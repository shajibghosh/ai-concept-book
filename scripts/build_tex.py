import json, os, collections
D = json.load(open("data/concepts.json"))
M, K, L, T = D["META"], D["KIND_NAMES"], D["LEVELS"], D["TAGS"]

def tex(s):
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
           "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
           "<": r"\textless{}", ">": r"\textgreater{}", "\u2013": "--", "\u2014": "---", "\u00b7": r"\textperiodcentered{}",
           "\u2019": "'", "\u201c": "``", "\u201d": "''"}
    return "".join(rep.get(ch, ch) for ch in s)
def turl(u): return u.replace("%", r"\%").replace("#", r"\#")

C = []
for ci, c in enumerate(D["CHAPTERS"]):
    for i, k in enumerate(c["concepts"]):
        k["lab"] = f"c:{c['id']}-{i}"; k["chn"] = ci + 1; k["cht"] = c["title"]; C.append(k)
nc, nl = len(C), sum(len(k["links"]) for k in C)

o = []
o.append(r"""% The Modern AI Concept Book, Edition 2 -- Overleaf-ready (pdfLaTeX)
\documentclass[10pt,a4paper,openany]{report}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{mathpazo}
\usepackage[scaled=0.92]{helvet}
\usepackage{courier}
\usepackage{microtype}
\usepackage[a4paper,margin=2.2cm,top=2.3cm,bottom=2.5cm]{geometry}
\usepackage[dvipsnames,table]{xcolor}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{needspace}
\usepackage{enumitem}
\usepackage{multicol}
\usepackage{longtable}
\usepackage{array}
\usepackage{tikz}
\usepackage[most]{tcolorbox}
\usepackage{xurl}
\usepackage[hidelinks]{hyperref}

% ---- palette (edit here to re-theme the whole book) ---------------------
\definecolor{ink}{HTML}{1D2124}
\definecolor{muted}{HTML}{5E666C}
\definecolor{accent}{HTML}{2F5D8A}
\definecolor{accentbg}{HTML}{E9EFF6}
\definecolor{rule}{HTML}{D7DAD3}
\definecolor{newc}{HTML}{B0431F}
\definecolor{kG}{HTML}{24292F}\definecolor{kB}{HTML}{8A4B08}\definecolor{kP}{HTML}{7A2E7A}
\definecolor{kD}{HTML}{1F6B4F}\definecolor{kS}{HTML}{A3261E}\definecolor{kV}{HTML}{2F5D8A}
\hypersetup{colorlinks=true,linkcolor=accent,urlcolor=accent,pdftitle={The Modern AI Concept Book},pdfauthor={AI Concept Book}}
\color{ink}
\setlength{\parindent}{0pt}\setlength{\parskip}{3pt}

\titleformat{\chapter}[display]{\sffamily\bfseries\color{ink}}{\color{accent}\fontsize{50}{50}\selectfont\thechapter}{4pt}{\huge}[\vspace{3pt}{\color{rule}\titlerule[1pt]}]
\titlespacing*{\chapter}{0pt}{-14pt}{14pt}
\titleformat{\section}{\sffamily\bfseries\large}{}{0pt}{}
\setcounter{secnumdepth}{0}\setcounter{tocdepth}{1}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\sffamily\footnotesize\color{muted}The Modern AI Concept Book}
\fancyhead[R]{\sffamily\footnotesize\color{muted}\leftmark}
\fancyfoot[C]{\sffamily\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\sffamily\footnotesize\thepage}\renewcommand{\headrulewidth}{0pt}}

% ---- concept macros -----------------------------------------------------
% \concept{label}{Name}{alias}{meta line}
\newcommand{\concept}[4]{\Needspace{8\baselineskip}\vspace{9pt}\phantomsection\label{#1}\addcontentsline{toc}{section}{#2}%
 {\sffamily\bfseries\large #2}\if\relax\detokenize{#3}\relax\else\ \ {\sffamily\small\color{accent}(#3)}\fi\par\nopagebreak
 {\sffamily\scriptsize\color{muted}#4}\par\nopagebreak\vspace{2pt}}
\newcommand{\newtag}{\colorbox{newc}{\sffamily\scriptsize\bfseries\color{white}NEW 2026}}
\newcommand{\acttag}{\fcolorbox{newc}{white}{\sffamily\scriptsize\color{newc}ACTIVE 2026}}
\newenvironment{keypoints}{\begin{itemize}[leftmargin=14pt,itemsep=1pt,topsep=2pt,parsep=0pt]\small}{\end{itemize}}
\newtcolorbox{sota}{enhanced,breakable,colback=accentbg,colframe=accent,boxrule=0pt,leftrule=2.5pt,sharp corners,left=6pt,right=6pt,top=3pt,bottom=3pt,fontupper=\small,
 before upper={{\sffamily\scriptsize\bfseries\color{accent}STATE OF THE ART, SEPT 2026}\par}}
\newcommand{\lk}[5]{\item[\textcolor{k#1}{\rule{5pt}{5pt}}]{\sffamily\scriptsize\bfseries\textcolor{k#1}{#2}}\ {\sffamily\scriptsize\color{muted}#3}\ \href{#5}{#4}\\[-1pt]{\ttfamily\scriptsize\color{muted}\url{#5}}}
\newenvironment{links}{\begin{itemize}[leftmargin=14pt,itemsep=1pt,topsep=3pt,labelsep=6pt]\small}{\end{itemize}}
\newcommand{\chapintro}[1]{{\itshape\color{muted}\large #1\par}\vspace{4pt}}

\begin{document}
\begin{titlepage}
\begin{tikzpicture}[remember picture,overlay]\fill[accent] (current page.north west) rectangle ([yshift=-8cm]current page.north east);\end{tikzpicture}
\vspace*{0.3cm}
{\color{white}\sffamily\bfseries\fontsize{42}{44}\selectfont The Modern AI\\[4pt] Concept Book\par}
\vspace{0.4cm}{\color{white}\sffamily\large """ + tex(M["edition"]) + r"""\par}
\vspace{2.4cm}
{\Large """ + tex(M["subtitle"][0].upper() + M["subtitle"][1:]) + r""".\par}
\vspace{0.4cm}{\color{muted}Current to """ + tex(M["asof"]) + r""".\par}
\vfill
{\sffamily\small\color{muted}""" + f"{len(D['CHAPTERS'])} categories \\quad {nc} concepts \\quad {nl} dated resources" + r"""\\[6pt]
Resource types:\ \textcolor{kG}{\rule{5pt}{5pt}} GitHub\quad \textcolor{kB}{\rule{5pt}{5pt}} Blog\quad \textcolor{kP}{\rule{5pt}{5pt}} Paper\quad \textcolor{kD}{\rule{5pt}{5pt}} Docs\quad \textcolor{kS}{\rule{5pt}{5pt}} Spec\quad \textcolor{kV}{\rule{5pt}{5pt}} Video\par}
\end{titlepage}

\chapter*{How to use this book}\markboth{How to use this book}{}
Each entry gives a plain-language definition, key points, a \emph{state of the art} note where the picture changed in 2026, and dated resources (GitHub repositories, blogs, papers, documentation, specifications and videos).

The header line under each concept shows the year it emerged, its most recent active year, its level (Beginner, Intermediate, Advanced) and tags. \newtag\ marks concepts that appeared in 2026; \acttag\ marks older concepts that were still changing in 2026.

A printed book cannot be filtered, so the appendices provide the same cuts as the interactive HTML edition: concepts by year of emergence, concepts by level, all resources grouped by type and sorted by year, and an index of acronyms. For live filtering by category, year, level, tag, resource type and resource year, open the HTML edition or the spreadsheet catalog.

Resource years show when an article, paper or specification was published, or when a repository or site launched (approximate for long-running projects). Chapter 1 reflects public reporting as of """ + tex(M["asof"]) + r""" and will date quickly.

\tableofcontents
\clearpage
""")

for ci, c in enumerate(D["CHAPTERS"]):
    o.append(r"\chapter{" + tex(c["title"]) + "}\n\\chapintro{" + tex(c["intro"]) + "}\n")
    for k in c["concepts"]:
        tagstr = ", ".join(T[t] for t in k["tags"] if t not in ("new-2026", "updated-2026"))
        status = r"\newtag\ " if k["since"] >= 2026 else (r"\acttag\ " if k["upd"] >= 2026 else "")
        span = f"{k['since']}" if k["since"] == k["upd"] else f"{k['since']}--{k['upd']}"
        meta = status + f"Since {span} \\quad {L[k['level']]}" + (f" \\quad {tex(tagstr)}" if tagstr else "")
        o.append(r"\concept{" + k["lab"] + "}{" + tex(k["name"]) + "}{" + tex(k["aka"]) + "}{" + meta + "}\n")
        o.append(tex(k["text"]) + "\n")
        if k["points"]:
            o.append("\\begin{keypoints}\n" + "".join("  \\item " + tex(p) + "\n" for p in k["points"]) + "\\end{keypoints}\n")
        if k["sota"]:
            o.append("\\begin{sota}" + tex(k["sota"]) + "\\end{sota}\n")
        o.append("\\begin{links}\n")
        for l in k["links"]:
            o.append("  \\lk{" + l["kind"] + "}{" + K[l["kind"]] + "}{" + str(l["year"]) + "}{" + tex(l["label"]) + "}{" + turl(l["url"]) + "}\n")
        o.append("\\end{links}\n\n")

# ---- Appendices
o.append(r"\appendix" + "\n")
def ref(k): return r"\hyperref[" + k["lab"] + "]{" + tex(k["name"]) + r"}\,{\color{muted}\scriptsize p.\,\pageref{" + k["lab"] + "}}"

o.append(r"\chapter{Concepts by year of emergence}" + "\n")
o.append("The same view as the Timeline tab in the HTML edition. Concepts that emerged before 2020 are grouped.\n\n")
by = collections.defaultdict(list)
for k in C: by[max(k["since"], 2019)].append(k)
for y in sorted(by, reverse=True):
    lab = "2019 and earlier" if y == 2019 else str(y)
    o.append(r"\Needspace{5\baselineskip}\section{" + lab + f" ({len(by[y])})" + "}\n\\begin{multicols}{2}\\small\\raggedright\n")
    for k in by[y]:
        o.append(ref(k) + r" {\color{muted}\scriptsize " + tex(k["cht"]) + r"}\par\vspace{2pt}" + "\n")
    o.append("\\end{multicols}\n")

o.append(r"\chapter{Concepts by level}" + "\n")
for lv in "BIA":
    ks = [k for k in C if k["level"] == lv]
    o.append(r"\Needspace{5\baselineskip}\section{" + L[lv] + f" ({len(ks)})" + "}\n\\begin{multicols}{2}\\small\\raggedright\n")
    for k in ks:
        o.append(ref(k) + r"\par\vspace{1pt}" + "\n")
    o.append("\\end{multicols}\n")

o.append(r"\chapter{Resources by type and year}" + "\n")
o.append("Every resource in the book, grouped by type and sorted newest first. Duplicates that support several concepts are listed once, with the first concept that cites them.\n\n")
seen = {}
for k in C:
    for l in k["links"]:
        seen.setdefault(l["url"], (l, k))
for kind in "GBPDSV":
    rows = sorted([v for v in seen.values() if v[0]["kind"] == kind], key=lambda v: (-v[0]["year"], v[0]["label"].lower()))
    if not rows: continue
    o.append(r"\section{" + K[kind] + f" ({len(rows)})" + "}\n")
    o.append(r"{\small\begin{longtable}{@{}p{0.07\linewidth}>{\raggedright}p{0.55\linewidth}>{\raggedright\arraybackslash}p{0.34\linewidth}@{}}" + "\n")
    o.append(r"\textbf{\sffamily Year} & \textbf{\sffamily Resource} & \textbf{\sffamily Concept}\\ \hline\endhead" + "\n")
    for l, k in rows:
        o.append(f"{l['year']} & \\href{{{turl(l['url'])}}}{{{tex(l['label'])}}} & {ref(k)}\\\\\n")
    o.append(r"\end{longtable}}" + "\n")

o.append(r"\chapter{Acronyms and aliases}" + "\n\\begin{multicols}{2}\\small\\raggedright\n")
for t, n, a in D["GLOSS"]:
    k = next(x for x in C if x["name"] == n)
    o.append(r"\textbf{\sffamily\color{accent}" + tex(t) + r"}\ \ " + ref(k) + r"\par\vspace{2pt}" + "\n")
o.append("\\end{multicols}\n\\end{document}\n")

os.makedirs("build/tex", exist_ok=True)
open("build/tex/main.tex", "w").write("".join(o))
print("tex ok")
