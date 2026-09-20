const fs = require("fs");
const D = JSON.parse(fs.readFileSync("data/concepts.json", "utf8"));
const { Document, Packer, Paragraph, TextRun, HeadingLevel, ExternalHyperlink, InternalHyperlink, Bookmark, TableOfContents,
  Footer, Header, AlignmentType, PageNumber, LevelFormat, PageBreak, BorderStyle, ShadingType,
  Table, TableRow, TableCell, WidthType } = require("docx");

const M = D.META, K = D.KIND_NAMES, L = D.LEVELS, T = D.TAGS;
const COL = { G: "24292F", B: "8A4B08", P: "7A2E7A", D: "1F6B4F", S: "A3261E", V: "2F5D8A" };
const ACC = "2F5D8A", MUT = "5E666C", RULE = "D7DAD3", NEW = "B0431F", ACCBG = "E9EFF6";
const SANS = "Arial", SERIF = "Georgia";
const C = [];
D.CHAPTERS.forEach((c, ci) => c.concepts.forEach((k, i) => { k.bm = `c_${c.id.replace(/-/g, "_")}_${i}`; k.chn = ci + 1; k.cht = c.title; C.push(k); }));
const nl = C.reduce((a, k) => a + k.links.length, 0);

const P = (text, o = {}) => new Paragraph({ ...o, children: [new TextRun({ text, ...(o.run || {}) })] });
const kids = [];
// title
kids.push(new Paragraph({ spacing: { before: 2000, after: 120 }, children: [new TextRun({ text: "The Modern AI", font: SANS, bold: true, size: 76, color: ACC })] }));
kids.push(new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: "Concept Book", font: SANS, bold: true, size: 76, color: ACC })] }));
kids.push(P(M.edition, { spacing: { after: 360 }, run: { font: SANS, size: 26, color: MUT } }));
kids.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ACC, space: 8 } }, spacing: { after: 300 },
  children: [new TextRun({ text: M.subtitle[0].toUpperCase() + M.subtitle.slice(1) + ".", font: SERIF, size: 30 })] }));
kids.push(P(`Current to ${M.asof}.  ${D.CHAPTERS.length} categories, ${C.length} concepts, ${nl} dated resources.`, { run: { font: SANS, size: 21, color: MUT } }));
const legend = [];
Object.entries(K).forEach(([k, v]) => { legend.push(new TextRun({ text: "\u25A0 ", color: COL[k], font: SANS, size: 20 })); legend.push(new TextRun({ text: v + "   ", font: SANS, size: 20, color: MUT })); });
kids.push(new Paragraph({ spacing: { before: 1400 }, children: [new TextRun({ text: "Resource types:  ", font: SANS, size: 20, color: MUT }), ...legend] }));
kids.push(new Paragraph({ children: [new PageBreak()] }));
// how to use
kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("How to use this book")] }));
[
  "Each entry gives a plain-language definition, key points, a state-of-the-art note where the picture changed in 2026, and dated resources: GitHub repositories, blogs, papers, documentation, specifications and videos.",
  "The line under each concept name shows when it emerged, its most recent active year, its level (Beginner, Intermediate, Advanced) and tags. NEW 2026 marks concepts that appeared in 2026; ACTIVE 2026 marks older concepts still changing in 2026.",
  "Word cannot filter content interactively, so the appendices provide the same cuts as the HTML edition: concepts by year of emergence, by level, every resource by type and year, and an acronym index. Every concept name in the appendices links back to its entry. For live filtering, use the HTML edition or the spreadsheet catalog.",
  "Resource years show when an article, paper or specification was published, or when a repository or site launched (approximate for long-running projects). Chapter 1 reflects public reporting as of " + M.asof + " and will date quickly.",
].forEach((t) => kids.push(P(t, { style: "Body" })));
kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("Contents")] }));
kids.push(new TableOfContents("Contents", { hyperlink: true, headingStyleRange: "1-2" }));
kids.push(P("If page numbers are missing, right-click the table and choose Update Field.", { run: { italics: true, size: 18, color: MUT } }));

// chapters
D.CHAPTERS.forEach((c, ci) => {
  kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun(`${ci + 1}.  ${c.title}`)] }));
  kids.push(P(c.intro, { style: "Intro" }));
  c.concepts.forEach((k) => {
    const h = [new Bookmark({ id: k.bm, children: [new TextRun(k.name)] })];
    if (k.aka) h.push(new TextRun({ text: `   (${k.aka})`, color: ACC, bold: false, size: 22 }));
    kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, children: h }));
    const meta = [];
    if (k.since >= 2026) meta.push(new TextRun({ text: " NEW 2026 ", bold: true, color: "FFFFFF", shading: { type: ShadingType.CLEAR, fill: NEW, color: "auto" }, size: 15, font: SANS }), new TextRun({ text: "  ", size: 15 }));
    else if (k.upd >= 2026) meta.push(new TextRun({ text: "ACTIVE 2026", bold: true, color: NEW, size: 15, font: SANS }), new TextRun({ text: "   ", size: 15 }));
    const span = k.since === k.upd ? `${k.since}` : `${k.since}\u2013${k.upd}`;
    const tags = k.tags.filter((t) => t !== "new-2026" && t !== "updated-2026").map((t) => T[t]).join(", ");
    meta.push(new TextRun({ text: `Since ${span}   \u2502   ${L[k.level]}` + (tags ? `   \u2502   ${tags}` : ""), color: MUT, size: 16, font: SANS }));
    kids.push(new Paragraph({ keepNext: true, spacing: { after: 80 }, children: meta }));
    kids.push(P(k.text, { style: "Body", keepNext: true }));
    (k.points || []).forEach((p) => kids.push(new Paragraph({ numbering: { reference: "pts", level: 0 }, style: "Point", keepNext: true, children: [new TextRun(p)] })));
    if (k.sota) kids.push(new Paragraph({ style: "Sota", keepNext: true, children: [new TextRun({ text: "STATE OF THE ART, SEPT 2026   ", bold: true, color: ACC, size: 15, font: SANS }), new TextRun(k.sota)] }));
    k.links.forEach((l, li) => kids.push(new Paragraph({ numbering: { reference: "links", level: 0 }, style: "LinkItem", keepNext: li < k.links.length - 1, children: [
      new TextRun({ text: K[l.kind] + " ", bold: true, color: COL[l.kind], size: 16, font: SANS }),
      new TextRun({ text: l.year + "  ", color: MUT, size: 16, font: SANS }),
      new ExternalHyperlink({ link: l.url, children: [new TextRun({ text: l.label, style: "Hyperlink" })] }),
      new TextRun({ text: "  " + l.url, color: MUT, size: 14, font: "Courier New" }) ] })));
  });
});

// tables helper
const border = { style: BorderStyle.SINGLE, size: 4, color: RULE };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(children, w, fill) { return new TableCell({ borders, width: { size: w, type: WidthType.DXA }, margins: { top: 50, bottom: 50, left: 90, right: 90 },
  shading: fill ? { fill, type: ShadingType.CLEAR, color: "auto" } : undefined, children: [new Paragraph({ children })] }); }
const tr = (t, o = {}) => new TextRun({ text: String(t), font: SANS, size: 17, ...o });
const conceptLink = (k) => new InternalHyperlink({ anchor: k.bm, children: [new TextRun({ text: k.name, style: "Hyperlink", font: SANS, size: 17 })] });
function table(widths, head, rows) {
  const total = widths.reduce((a, b) => a + b, 0);
  const trs = [new TableRow({ tableHeader: true, children: head.map((h, i) => cell([tr(h, { bold: true })], widths[i], "E4ECF4")) })];
  rows.forEach((r) => trs.push(new TableRow({ children: r.map((ch, i) => cell(ch, widths[i])) })));
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, rows: trs });
}
// Appendix A: timeline
kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("Appendix A.  Concepts by year of emergence")] }));
const yrs = [...new Set(C.map((k) => Math.max(k.since, 2019)))].sort((a, b) => b - a);
yrs.forEach((y) => {
  const ks = C.filter((k) => Math.max(k.since, 2019) === y);
  kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`${y === 2019 ? "2019 and earlier" : y}  (${ks.length})`)] }));
  kids.push(table([4200, 900, 1300, 2960], ["Concept", "Since", "Level", "Category"], ks.map((k) => [[conceptLink(k)], [tr(k.since)], [tr(L[k.level])], [tr(`${k.chn}. ${k.cht}`)]])));
});
// Appendix B: level
kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("Appendix B.  Concepts by level")] }));
["B", "I", "A"].forEach((lv) => {
  const ks = C.filter((k) => k.level === lv);
  kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`${L[lv]}  (${ks.length})`)] }));
  kids.push(table([5000, 4360], ["Concept", "Category"], ks.map((k) => [[conceptLink(k)], [tr(`${k.chn}. ${k.cht}`)]])));
});
// Appendix C: resources
kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("Appendix C.  Resources by type and year")] }));
kids.push(P("Every resource, grouped by type and sorted newest first. Resources cited by several concepts are listed once with the first concept that cites them.", { style: "Body" }));
const seen = new Map(); C.forEach((k) => k.links.forEach((l) => { if (!seen.has(l.url)) seen.set(l.url, [l, k]); }));
"GBPDSV".split("").forEach((kind) => {
  const rows = [...seen.values()].filter(([l]) => l.kind === kind).sort((a, b) => b[0].year - a[0].year || a[0].label.localeCompare(b[0].label));
  if (!rows.length) return;
  kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`${K[kind]}  (${rows.length})`)] }));
  kids.push(table([760, 5200, 3400], ["Year", "Resource", "Concept"], rows.map(([l, k]) => [[tr(l.year)], [new ExternalHyperlink({ link: l.url, children: [new TextRun({ text: l.label, style: "Hyperlink", font: SANS, size: 17 })] })], [conceptLink(k)]])));
});
// Appendix D: acronyms
kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("Appendix D.  Acronyms and aliases")] }));
kids.push(table([3000, 6360], ["Alias", "Concept"], D.GLOSS.map(([t, n]) => { const k = C.find((x) => x.name === n); return [[tr(t, { bold: true, color: ACC })], [conceptLink(k)]]; })));

const doc = new Document({
  creator: "AI Concept Book", title: M.title,
  styles: {
    default: { document: { run: { font: SERIF, size: 21 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: SANS, size: 38, bold: true, color: ACC },
        paragraph: { spacing: { before: 0, after: 160 }, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: RULE, space: 6 } } } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: SANS, size: 26, bold: true, color: "1D2124" }, paragraph: { spacing: { before: 280, after: 40 }, outlineLevel: 1 } },
      { id: "Intro", name: "Intro", basedOn: "Normal", run: { italics: true, color: MUT, size: 23 }, paragraph: { spacing: { after: 160, line: 300 } } },
      { id: "Body", name: "Body", basedOn: "Normal", paragraph: { spacing: { after: 80, line: 290 } } },
      { id: "Point", name: "Key Point", basedOn: "Normal", run: { size: 19 }, paragraph: { spacing: { after: 20 } } },
      { id: "Sota", name: "State of the Art", basedOn: "Normal", run: { size: 19 }, paragraph: { spacing: { before: 80, after: 80 }, indent: { left: 120 },
        shading: { type: ShadingType.CLEAR, fill: ACCBG, color: "auto" }, border: { left: { style: BorderStyle.SINGLE, size: 18, color: ACC, space: 6 } } } },
      { id: "LinkItem", name: "Link Item", basedOn: "Normal", run: { size: 19 }, paragraph: { spacing: { after: 30 } } },
    ],
  },
  numbering: { config: [
    { reference: "links", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u25AA", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] },
    { reference: "pts", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] } ] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1300, bottom: 1300, left: 1440, right: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: M.title + "  \u00b7  " + M.edition, font: SANS, size: 16, color: MUT })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: 16, color: MUT })] })] }) },
    children: kids,
  }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync("editions/AI_Concept_Book.docx", b); console.log("docx ok"); });
