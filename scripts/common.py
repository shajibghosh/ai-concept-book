# Schema v2. Every concept:
#   name, aka, since (year concept emerged), upd (latest major update year),
#   level: B=Beginner I=Intermediate A=Advanced
#   tags: space-separated from TAGS
#   text: definition; points: key ideas; sota: state of the art as of Sept 2026
#   links: (kind, label, url, year)  kind: G GitHub, B Blog/article, P Paper, D Docs/site, S Spec/standard, V Video
TAGS = {
 "foundational": "Foundational",
 "production": "Production practice",
 "research": "Research frontier",
 "open-source": "Open source / open weights",
 "open-standard": "Open standard",
 "enterprise": "Enterprise",
 "security": "Security",
 "cost": "Cost & efficiency",
}
LEVELS = {"B": "Beginner", "I": "Intermediate", "A": "Advanced"}
KIND_NAMES = {"G": "GitHub", "B": "Blog", "P": "Paper", "D": "Docs", "S": "Spec", "V": "Video"}

def C(name, aka, since, upd, level, tags, text, points, sota, links):
    t = tags.split()
    if since >= 2026: t.append("new-2026")
    elif upd >= 2026: t.append("updated-2026")
    return dict(name=name, aka=aka, since=since, upd=upd, level=level, tags=t, text=text,
                points=points, sota=sota,
                links=[dict(kind=k, label=l, url=u, year=y) for k, l, u, y in links])
