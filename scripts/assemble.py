import json, collections
from common import TAGS, LEVELS, KIND_NAMES
from d1 import PART1
from d2 import PART2
from d3 import PART3
from d4 import PART4

CHAPTERS = PART1 + PART2 + PART3 + PART4
from points import POINTS
for _c in CHAPTERS:
    for _k in _c['concepts']:
        if not _k['points'] and _k['name'] in POINTS: _k['points'] = POINTS[_k['name']]
assert set(POINTS) <= {k['name'] for c in CHAPTERS for k in c['concepts']}, set(POINTS)-{k['name'] for c in CHAPTERS for k in c['concepts']}
META = dict(
    title="The Modern AI Concept Book",
    subtitle="LLMs, VLMs, agents, harnesses, hardware and the practice of AI engineering",
    edition="Edition 2 · September 2026",
    asof="September 20, 2026",
)

# validate
names = collections.Counter(k["name"] for c in CHAPTERS for k in c["concepts"])
dups = [n for n, v in names.items() if v > 1]
assert not dups, dups
for c in CHAPTERS:
    for k in c["concepts"]:
        assert k["level"] in LEVELS, k["name"]
        assert 1990 < k["since"] <= 2026 and k["since"] <= k["upd"] <= 2026, k["name"]
        for t in k["tags"]:
            assert t in TAGS or t in ("new-2026", "updated-2026"), (k["name"], t)
        for l in k["links"]:
            assert l["kind"] in KIND_NAMES and l["url"].startswith("http") and 1990 < l["year"] <= 2026, (k["name"], l)

gl = sorted({(k["aka"], k["name"], c["id"] + "-" + str(i))
             for c in CHAPTERS for i, k in enumerate(c["concepts"]) if k["aka"]}, key=lambda x: x[0].lower())

TAGS2 = dict(TAGS); TAGS2["new-2026"] = "New in 2026"; TAGS2["updated-2026"] = "Updated in 2026"
DATA = dict(META=META, CHAPTERS=CHAPTERS, TAGS=TAGS2, LEVELS=LEVELS, KIND_NAMES=KIND_NAMES, GLOSS=gl)
json.dump(DATA, open("data/concepts.json", "w"), ensure_ascii=False)

nc = sum(len(c["concepts"]) for c in CHAPTERS)
nl = sum(len(k["links"]) for c in CHAPTERS for k in c["concepts"])
new = sum(1 for c in CHAPTERS for k in c["concepts"] if k["since"] >= 2026)
upd = sum(1 for c in CHAPTERS for k in c["concepts"] if k["upd"] >= 2026)
print(f"chapters={len(CHAPTERS)} concepts={nc} links={nl} new2026={new} active2026={upd} gloss={len(gl)}")
