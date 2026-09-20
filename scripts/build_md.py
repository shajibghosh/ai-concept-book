import json, os, re, collections, sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "."
D = json.load(open(os.path.join(BASE, "data/concepts.json")))
M, K, L, T = D["META"], D["KIND_NAMES"], D["LEVELS"], D["TAGS"]
os.makedirs(os.path.join(BASE, "book"), exist_ok=True)
os.makedirs(os.path.join(BASE, "indexes"), exist_ok=True)

def slug(s):  # GitHub heading anchor
    s = s.lower().strip()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")
def fslug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s
def cell(s): return s.replace("|", "\\|")

CH = D["CHAPTERS"]
for ci, c in enumerate(CH, 1):
    c["n"] = ci
    c["file"] = f"{ci:02d}-{fslug(c['title'].split(' (')[0])}.md"
    for k in c["concepts"]:
        k["ch"] = c; k["anchor"] = slug(k["name"])
C = [k for c in CH for k in c["concepts"]]
nc, nl = len(C), sum(len(k["links"]) for k in C)
n26 = sum(1 for k in C if k["upd"] >= 2026)

def status(k):
    return "**New in 2026**" if k["since"] >= 2026 else ("**Active in 2026**" if k["upd"] >= 2026 else "Established")
def tags(k): return ", ".join(T[t] for t in k["tags"] if t not in ("new-2026", "updated-2026"))
def span(k): return str(k["since"]) if k["since"] == k["upd"] else f"{k['since']}, last active {k['upd']}"

def concept_md(k):
    o = [f"### {k['name']}", ""]
    meta = []
    if k["aka"]: meta.append(f"`{k['aka']}`")
    meta += [status(k), f"Emerged {span(k)}", L[k["level"]]]
    if tags(k): meta.append(tags(k))
    o += [" · ".join(meta), "", k["text"], ""]
    if k["points"]:
        o += ["**Key points**", ""] + [f"- {p}" for p in k["points"]] + [""]
    if k["sota"]:
        o += ["> [!NOTE]", f"> **State of the art, Sept 2026:** {k['sota']}", ""]
    o += ["| Type | Year | Resource |", "|---|---|---|"]
    o += [f"| {K[l['kind']]} | {l['year']} | [{cell(l['label'])}]({l['url']}) |" for l in k["links"]]
    return "\n".join(o) + "\n"

def chapter_md(c, prefix_nav=True, rel=""):
    o = []
    if prefix_nav:
        i = c["n"] - 1
        nav = [f"[Contents]({rel}../README.md#contents)"]
        if i > 0: nav.append(f"[← {CH[i-1]['n']}. {CH[i-1]['title']}]({CH[i-1]['file']})")
        if i < len(CH) - 1: nav.append(f"[{CH[i+1]['n']}. {CH[i+1]['title']} →]({CH[i+1]['file']})")
        o += [" · ".join(nav), ""]
    o += [f"# {c['n']}. {c['title']}", "", f"> {c['intro']}", ""]
    o += ["**In this chapter:** " + " · ".join(f"[{k['name']}](#{k['anchor']})" for k in c["concepts"]), "", "---", ""]
    for k in c["concepts"]:
        o += [concept_md(k), "[↑ Back to top](#" + slug(f"{c['n']}. {c['title']}") + ")", "", "---", ""]
    return "\n".join(o)

for c in CH:
    open(os.path.join(BASE, "book", c["file"]), "w").write(chapter_md(c))

def link(k, frm="indexes"):
    pre = "../book/" if frm == "indexes" else "book/"
    return f"[{cell(k['name'])}]({pre}{k['ch']['file']}#{k['anchor']})"
def cat(k): return f"{k['ch']['n']}. {k['ch']['title']}"
HDR = lambda title: [f"[Contents](../README.md#contents) · [Browse indexes](../README.md#browse-and-filter)", "", f"# {title}", ""]

# by year
o = HDR("Concepts by year of emergence")
o += ["The Markdown equivalent of the **Timeline** view and the *Emerged in* filter.", ""]
by = collections.defaultdict(list)
for k in C: by[max(k["since"], 2019)].append(k)
o += ["Jump to: " + " · ".join(f"[{'≤2019' if y == 2019 else y}](#{'2019-and-earlier' if y == 2019 else y})" for y in sorted(by, reverse=True)), ""]
for y in sorted(by, reverse=True):
    o += [f"## {'2019 and earlier' if y == 2019 else y}", "", f"{len(by[y])} concepts", "", "| Concept | Since | Status | Level | Category |", "|---|---|---|---|---|"]
    o += [f"| {link(k)} | {k['since']} | {status(k).strip('*')} | {L[k['level']]} | {cell(cat(k))} |" for k in by[y]] + [""]
open(os.path.join(BASE, "indexes/by-year.md"), "w").write("\n".join(o))

# by level
o = HDR("Concepts by level") + ["Suggested reading path: start with Beginner, then Intermediate, then Advanced.", ""]
for lv in "BIA":
    ks = [k for k in C if k["level"] == lv]
    o += [f"## {L[lv]}", "", f"{len(ks)} concepts", "", "| Concept | Category | Status |", "|---|---|---|"]
    o += [f"| {link(k)} | {cell(cat(k))} | {status(k).strip('*')} |" for k in ks] + [""]
open(os.path.join(BASE, "indexes/by-level.md"), "w").write("\n".join(o))

# by tag / status
o = HDR("Concepts by tag and 2026 status")
groups = [("New in 2026", [k for k in C if k["since"] >= 2026]), ("Active in 2026 (older concepts still changing)", [k for k in C if k["since"] < 2026 <= k["upd"]])]
groups += [(T[t], [k for k in C if t in k["tags"]]) for t in T if t not in ("new-2026", "updated-2026")]
o += ["Jump to: " + " · ".join(f"[{g}](#{slug(g)})" for g, _ in groups), ""]
for g, ks in groups:
    o += [f"## {g}", "", f"{len(ks)} concepts", "", "| Concept | Level | Category |", "|---|---|---|"]
    o += [f"| {link(k)} | {L[k['level']]} | {cell(cat(k))} |" for k in ks] + [""]
open(os.path.join(BASE, "indexes/by-tag.md"), "w").write("\n".join(o))

# resources by type
seen = {}
for k in C:
    for l in k["links"]: seen.setdefault(l["url"], (l, k))
o = HDR("Resources by type and year")
o += [f"All {len(seen)} unique resources, grouped by type and sorted newest first. Resources cited by several concepts appear once, with the first concept that cites them.", ""]
o += ["Jump to: " + " · ".join(f"[{K[x]}](#{slug(K[x])})" for x in "GBPDSV"), ""]
for kind in "GBPDSV":
    rows = sorted([v for v in seen.values() if v[0]["kind"] == kind], key=lambda v: (-v[0]["year"], v[0]["label"].lower()))
    o += [f"## {K[kind]}", "", f"{len(rows)} resources", "", "| Year | Resource | Concept |", "|---|---|---|"]
    o += [f"| {l['year']} | [{cell(l['label'])}]({l['url']}) | {link(k)} |" for l, k in rows] + [""]
open(os.path.join(BASE, "indexes/resources-by-type.md"), "w").write("\n".join(o))

# resources by year
o = HDR("Resources by year") + ["Newest first. Use this to catch up on what was published recently.", ""]
ry = collections.defaultdict(list)
for l, k in seen.values(): ry[max(l["year"], 2019)].append((l, k))
o += ["Jump to: " + " · ".join(f"[{'≤2019' if y == 2019 else y}](#{'2019-and-earlier' if y == 2019 else y})" for y in sorted(ry, reverse=True)), ""]
for y in sorted(ry, reverse=True):
    rows = sorted(ry[y], key=lambda v: ("GBPDSV".index(v[0]["kind"]), v[0]["label"].lower()))
    o += [f"## {'2019 and earlier' if y == 2019 else y}", "", f"{len(rows)} resources", "", "| Type | Resource | Concept |", "|---|---|---|"]
    o += [f"| {K[l['kind']]} | [{cell(l['label'])}]({l['url']}) | {link(k)} |" for l, k in rows] + [""]
open(os.path.join(BASE, "indexes/resources-by-year.md"), "w").write("\n".join(o))

# glossary
o = HDR("Acronyms and aliases") + ["| Alias | Concept | Category |", "|---|---|---|"]
for t, n, a in D["GLOSS"]:
    k = next(x for x in C if x["name"] == n)
    o.append(f"| **{cell(t)}** | {link(k)} | {cell(cat(k))} |")
open(os.path.join(BASE, "indexes/glossary.md"), "w").write("\n".join(o) + "\n")

# single-file edition
o = [f"# {M['title']}", "", f"*{M['edition']} · current to {M['asof']}*", "",
     f"{M['subtitle'][0].upper() + M['subtitle'][1:]}. {nc} concepts · {nl} dated resources. See [README.md](README.md) for other formats and browse-by indexes.", "",
     "## Contents", ""]
o += [f"{c['n']}. [{c['title']}](#{slug(str(c['n']) + '. ' + c['title'])}) ({len(c['concepts'])})" for c in CH] + ["", "---", ""]
for c in CH:
    o.append("#" + chapter_md(c, prefix_nav=False))
open(os.path.join(BASE, "CONCEPT_BOOK.md"), "w").write("\n".join(o))

# README contents table (written to a fragment the README template includes)
rows = ["| # | Chapter | Concepts | New / active in 2026 |", "|---|---|---|---|"]
for c in CH:
    new = sum(1 for k in c["concepts"] if k["since"] >= 2026)
    act = sum(1 for k in c["concepts"] if k["upd"] >= 2026)
    rows.append(f"| {c['n']} | [{c['title']}](book/{c['file']}) | {len(c['concepts'])} | {new} / {act} |")

rp = os.path.join(BASE, "README.md")
if os.path.exists(rp):
    r = open(rp).read()
    def put(tag, text):
        global r
        a, b = f"<!-- {tag}:start -->", f"<!-- {tag}:end -->"
        if a in r and b in r:
            r = r[:r.index(a) + len(a)] + "\n" + text + "\n" + r[r.index(b):]
    put("contents", "\n".join(rows))
    put("stats", f"**{len(CH)} chapters · {nc} concepts · {len(seen)} unique resources ({nl} citations) · {sum(1 for k in C if k['since'] >= 2026)} new in 2026 · {n26} active in 2026**")
    open(rp, "w").write(r)
print("md ok", nc, nl, len(seen))
