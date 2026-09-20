import json, html
D = json.load(open("data/concepts.json"))
M = D["META"]
esc = html.escape
nc = sum(len(c["concepts"]) for c in D["CHAPTERS"])
nl = sum(len(k["links"]) for c in D["CHAPTERS"] for k in c["concepts"])
n26 = sum(1 for c in D["CHAPTERS"] for k in c["concepts"] if k["upd"] >= 2026)

CSS = r"""
:root{--f-body:"Newsreader",Georgia,"Times New Roman",serif;--f-ui:"Bricolage Grotesque","Segoe UI",system-ui,-apple-system,sans-serif;
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
*,*::before,*::after{box-sizing:inherit}
html{scroll-padding-top:calc(env(safe-area-inset-top,0px) + 140px)}
:root,[data-theme="paper"]{--bg:#FBFBF8;--bg2:#F0F1EC;--fg:#1D2124;--mut:#5E666C;--rule:#D7DAD3;--acc:#2F5D8A;--acc2:#E4ECF4;--new:#B0431F;
--G:#24292F;--B:#8A4B08;--P:#7A2E7A;--D:#1F6B4F;--S:#A3261E;--V:#2F5D8A}
[data-theme="ink"]{--bg:#15181C;--bg2:#1E2228;--fg:#E6E8EA;--mut:#99A2AB;--rule:#2F353D;--acc:#8FB8E8;--acc2:#23303F;--new:#F2A07B;
--G:#D0D6DC;--B:#E9A96A;--P:#D39BE0;--D:#7ED3AE;--S:#F08A80;--V:#8FB8E8}
[data-theme="sepia"]{--bg:#F3EAD8;--bg2:#E9DDC4;--fg:#3B2F22;--mut:#7A6A55;--rule:#D5C5A6;--acc:#7B4F1E;--acc2:#E7D6B5;--new:#A0321F;
--G:#3B2F22;--B:#8C4A12;--P:#6D3B5B;--D:#3F6A3A;--S:#9A2F22;--V:#7B4F1E}
[data-theme="blueprint"]{--bg:#0F2A47;--bg2:#15365A;--fg:#E8F0F8;--mut:#A6BCD3;--rule:#2B4F77;--acc:#FFD479;--acc2:#1C416B;--new:#FF9E8A;
--G:#E8F0F8;--B:#FFD479;--P:#F5B3E0;--D:#9BE7C4;--S:#FF9E8A;--V:#9CCBFF}
[data-theme="forest"]{--bg:#EEF2EC;--bg2:#E1E8DD;--fg:#1F2A20;--mut:#5A6B5B;--rule:#C6D2C3;--acc:#2E6B3A;--acc2:#D5E4D2;--new:#A0321F;
--G:#1F2A20;--B:#8A5A12;--P:#6A3E7A;--D:#2E6B3A;--S:#A0321F;--V:#2B5C7A}
[data-theme="contrast"]{--bg:#000;--bg2:#000;--fg:#FFF;--mut:#E6E6E6;--rule:#FFF;--acc:#FFEA00;--acc2:#262626;--new:#FF7B6B;
--G:#FFF;--B:#FFEA00;--P:#FF9CF5;--D:#6CFFB0;--S:#FF7B6B;--V:#7CC8FF}
@media (prefers-color-scheme:dark){:root:not([data-theme="paper"]):not([data-theme="sepia"]):not([data-theme="forest"]):not([data-theme="blueprint"]):not([data-theme="contrast"]):not([data-theme="ink"]){--bg:#15181C;--bg2:#1E2228;--fg:#E6E8EA;--mut:#99A2AB;--rule:#2F353D;--acc:#8FB8E8;--acc2:#23303F;--new:#F2A07B;--G:#D0D6DC;--B:#E9A96A;--P:#D39BE0;--D:#7ED3AE;--S:#F08A80;--V:#8FB8E8}}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.6 var(--f-body);-webkit-font-smoothing:antialiased}
a{color:var(--acc)}
:focus-visible{outline:3px solid var(--acc);outline-offset:2px;border-radius:3px}
button{font:inherit;color:inherit}
.wrap{display:grid;grid-template-columns:300px minmax(0,1fr);max-width:1400px;margin:0 auto}
/* sidebar */
.side{position:sticky;top:0;height:100vh;height:100dvh;overflow:auto;padding:24px 20px 60px;border-right:1px solid var(--rule);font-family:var(--f-ui);font-size:14px}
.brand{font-weight:800;font-size:19px;line-height:1.15;letter-spacing:-.01em;margin:0 0 2px}
.ed{color:var(--mut);font-size:12.5px;margin:0 0 10px}
.fs{border-top:1px solid var(--rule);padding:12px 0 6px}
.fs h4{font-size:13px;font-weight:700;margin:0 0 8px;display:flex;justify-content:space-between;align-items:center}
.fs h4 button{border:0;background:none;color:var(--acc);font-size:12px;cursor:pointer;padding:0}
.chips{display:flex;flex-wrap:wrap;gap:5px}
.chip{display:inline-flex;align-items:center;gap:6px;padding:4px 9px;border:1px solid var(--rule);border-radius:999px;background:transparent;cursor:pointer;font-size:13px;line-height:1.3}
.chip .ct{color:var(--mut);font-size:11.5px;font-variant-numeric:tabular-nums}
.chip[aria-pressed="true"]{background:var(--acc);border-color:var(--acc);color:var(--bg)}
.chip[aria-pressed="true"] .ct{color:inherit;opacity:.8}
.chip.zero{opacity:.45}
.list .chip{border-radius:7px;width:100%;justify-content:space-between;text-align:left}
.themes{display:grid;grid-template-columns:1fr 1fr;gap:5px}
.tb{display:flex;align-items:center;gap:7px;padding:5px 8px;border:1px solid var(--rule);background:transparent;border-radius:7px;cursor:pointer;font-size:13px;text-align:left}
.tb[aria-pressed="true"]{border-color:var(--acc);background:var(--acc2)}
.sw{width:14px;height:14px;border-radius:50%;border:1px solid var(--rule);flex:none}
.sw-paper{background:linear-gradient(135deg,#FBFBF8 50%,#2F5D8A 50%)}.sw-ink{background:linear-gradient(135deg,#15181C 50%,#8FB8E8 50%)}
.sw-sepia{background:linear-gradient(135deg,#F3EAD8 50%,#7B4F1E 50%)}.sw-blueprint{background:linear-gradient(135deg,#0F2A47 50%,#FFD479 50%)}
.sw-forest{background:linear-gradient(135deg,#EEF2EC 50%,#2E6B3A 50%)}.sw-contrast{background:linear-gradient(135deg,#000 50%,#FFEA00 50%)}
.kd{font-size:10px}
.kG{color:var(--G)}.kB{color:var(--B)}.kP{color:var(--P)}.kD{color:var(--D)}.kS{color:var(--S)}.kV{color:var(--V)}
/* main */
main{padding:0 clamp(16px,4vw,56px) 80px;min-width:0}
.hero{padding:52px 0 28px}
.hero h1{font-family:var(--f-ui);font-weight:800;font-size:clamp(38px,6vw,78px);line-height:.95;letter-spacing:-.035em;margin:0 0 16px;max-width:13ch}
.hero .sub{font-size:20px;max-width:46ch;margin:0 0 20px;color:var(--mut)}
.stats{display:flex;flex-wrap:wrap;gap:26px;font-family:var(--f-ui);font-size:13.5px;color:var(--mut)}
.stats b{display:block;font-size:28px;color:var(--fg);font-weight:700;letter-spacing:-.02em}
.toolbar{position:sticky;top:0;z-index:5;background:var(--bg);padding:12px 0 10px;border-bottom:1px solid var(--rule);border-top:2px solid var(--fg);font-family:var(--f-ui)}
.row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.row+.row{margin-top:9px}
#q{flex:1 1 260px;font:inherit;font-size:15.5px;padding:9px 13px;border:1px solid var(--rule);border-radius:8px;background:var(--bg2);color:var(--fg);min-width:0}
.tabs{display:inline-flex;border:1px solid var(--rule);border-radius:8px;overflow:hidden}
.tabs button{border:0;background:transparent;padding:8px 12px;font-size:14px;cursor:pointer;border-right:1px solid var(--rule)}
.tabs button:last-child{border-right:0}
.tabs button[aria-selected="true"]{background:var(--fg);color:var(--bg)}
select{font:inherit;font-size:14px;padding:8px 10px;border:1px solid var(--rule);border-radius:8px;background:var(--bg2);color:var(--fg)}
.tog{display:inline-flex;align-items:center;gap:6px;font-size:14px;cursor:pointer}
.count{font-size:13.5px;color:var(--mut)}
.act{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.act .chip{font-size:12.5px;padding:3px 9px}
.act .chip::after{content:"\00d7";margin-left:2px;opacity:.7}
.clear{border:0;background:none;color:var(--acc);cursor:pointer;font-size:13px;text-decoration:underline}
.fbtn{display:none;border:1px solid var(--rule);background:var(--bg2);border-radius:8px;padding:8px 12px;cursor:pointer}
/* book */
.chapter{padding-top:38px}
.chead{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--rule);padding-bottom:8px}
.cnum{font-family:var(--f-ui);font-weight:800;font-size:40px;color:var(--acc);letter-spacing:-.03em;line-height:1;font-variant-numeric:tabular-nums}
.chead h2{font-family:var(--f-ui);font-size:clamp(24px,2.8vw,32px);font-weight:700;letter-spacing:-.02em;margin:0;line-height:1.1}
.intro{font-size:18.5px;font-style:italic;color:var(--mut);max-width:64ch;margin:12px 0 6px}
.entry{padding:20px 0 18px;border-bottom:1px solid var(--rule);max-width:80ch}
.eh{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px;margin-bottom:6px}
.eh h3{font-family:var(--f-ui);font-size:21px;font-weight:700;letter-spacing:-.01em;margin:0;line-height:1.2}
.meta{display:flex;flex-wrap:wrap;gap:6px;font-family:var(--f-ui);font-size:12.5px;margin:0 0 8px;color:var(--mut)}
.pill{padding:1px 8px;border-radius:20px;background:var(--acc2);color:var(--fg);font-family:var(--f-ui);font-size:12.5px}
.pill.new{background:var(--new);color:var(--bg);font-weight:600}
.pill.upd{border:1px solid var(--new);color:var(--new);background:transparent}
.entry p{margin:0 0 10px}
.pts{margin:0 0 10px;padding-left:20px}
.pts li{margin-bottom:3px}
.sota{margin:0 0 12px;padding:8px 12px;border-left:3px solid var(--acc);background:var(--bg2);font-size:16.5px}
.sota b{font-family:var(--f-ui);font-size:12.5px;color:var(--acc);display:block}
.links{display:flex;flex-wrap:wrap;gap:6px}
.lk{display:inline-flex;align-items:center;gap:6px;font-family:var(--f-ui);font-size:13.5px;line-height:1.3;padding:5px 10px 5px 8px;border:1px solid var(--rule);border-radius:7px;text-decoration:none;color:var(--fg);background:var(--bg2);max-width:100%}
.lk:hover{border-color:var(--acc)}
.kt{font-size:11px;font-weight:600;color:var(--mut)}
.ly{font-size:11px;color:var(--mut);font-variant-numeric:tabular-nums}
.lk.dim{opacity:.3}
/* cards */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:12px;padding-top:20px}
.card{border:1px solid var(--rule);border-radius:10px;padding:14px 16px;background:var(--bg);display:flex;flex-direction:column;gap:6px}
.card h3{font-family:var(--f-ui);font-size:17px;margin:0;line-height:1.25}
.card .ch{font-family:var(--f-ui);font-size:12px;color:var(--mut)}
.card p{margin:0;font-size:15.5px;line-height:1.5}
.card details{font-size:15px}
.card summary{font-family:var(--f-ui);font-size:13px;color:var(--acc);cursor:pointer}
.card .links{margin-top:8px}
/* resources */
.tblwrap{overflow-x:auto;padding-top:18px}
table{border-collapse:collapse;width:100%;font-family:var(--f-ui);font-size:14px}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-size:12.5px;color:var(--mut);font-weight:600;position:sticky;top:0;background:var(--bg)}
th button{border:0;background:none;cursor:pointer;color:inherit;font-weight:600;padding:0}
td.y{font-variant-numeric:tabular-nums;white-space:nowrap}
td a{text-decoration:none}
td .u{display:block;font-size:11.5px;color:var(--mut);word-break:break-all}
/* timeline */
.tl{padding-top:16px}
.yr{display:grid;grid-template-columns:90px 1fr;gap:16px;border-bottom:1px solid var(--rule);padding:16px 0}
.yr h3{font-family:var(--f-ui);font-size:30px;font-weight:800;color:var(--acc);margin:0;letter-spacing:-.02em;line-height:1}
.yr .n{font-family:var(--f-ui);font-size:12px;color:var(--mut)}
.tli{display:flex;flex-wrap:wrap;gap:6px}
.tli a{display:inline-block;font-family:var(--f-ui);font-size:13.5px;padding:4px 10px;border:1px solid var(--rule);border-radius:7px;text-decoration:none;color:var(--fg)}
.tli a span{color:var(--mut);font-size:11.5px;margin-left:6px}
/* index */
.idx{columns:2 300px;padding-top:18px;font-family:var(--f-ui);font-size:14.5px}
.idx a{display:block;break-inside:avoid;text-decoration:none;color:var(--fg);padding:3px 0}
.idx a b{color:var(--acc);font-weight:700}
.idx a span{color:var(--mut)}
.idx h4{break-after:avoid;margin:14px 0 4px;color:var(--mut);font-size:13px}
.tblwrap .count{font-family:var(--f-ui);margin:0 0 6px}
td.t{white-space:nowrap}
.empty{padding:40px 0;color:var(--mut);font-family:var(--f-ui)}
footer{margin-top:60px;padding-top:16px;border-top:1px solid var(--rule);font-family:var(--f-ui);font-size:13px;color:var(--mut);max-width:80ch}
.hl{animation:hl 1.6s ease-out}
@keyframes hl{from{background:var(--acc2)}to{background:transparent}}
@media (prefers-reduced-motion:reduce){.hl{animation:none}}
@media (max-width:960px){
 .wrap{grid-template-columns:1fr}
 .side{position:fixed;inset:0 12% 0 0;z-index:20;background:var(--bg);transform:translateX(-103%);transition:transform .2s;padding-top:calc(env(safe-area-inset-top,0px) + 20px)}
 .side.open{transform:none;box-shadow:0 0 0 100vmax rgba(0,0,0,.45)}
 .fbtn{display:inline-block}
 .toolbar{position:static}
 .tabs{overflow-x:auto;max-width:100%}
 .tabs button{white-space:nowrap}
 .yr{grid-template-columns:1fr}
}
@media print{.side,.toolbar,.fbtn{display:none}.wrap{display:block}.lk{border:0;background:none;padding:0}.lk::after{content:" <" attr(href) ">";font-size:10px}.entry{break-inside:avoid}}
"""

JS = r"""
(function(){
var D=JSON.parse(document.getElementById('data').textContent);
var K=D.KIND_NAMES,T=D.TAGS,L=D.LEVELS,ICON={G:'\u25CF',B:'\u25A0',P:'\u25C6',D:'\u25B2',S:'\u2605',V:'\u25B6'};
function e(s){return String(s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
// flatten
var C=[],ord=0;D.CHAPTERS.forEach(function(ch,ci){ch.concepts.forEach(function(k,i){k.ch=ch.id;k.chn=ci+1;k.cht=ch.title;k.id=ch.id+'-'+i;k.ord=ord++;
 k.s=(k.name+' '+k.aka+' '+k.text+' '+(k.points||[]).join(' ')+' '+k.sota+' '+k.links.map(function(l){return l.label+' '+l.url}).join(' ')).toLowerCase();C.push(k)})});
function sb(y){return y<=2022?'2022':String(y)} // since bucket
function lb(y){return y<=2023?'2023':String(y)} // link-year bucket
var SB=[['2022','Before 2023'],['2023','2023'],['2024','2024'],['2025','2025'],['2026','2026']];
var LB=[['2023','Before 2024'],['2024','2024'],['2025','2025'],['2026','2026']];
var FACETS=[
 {key:'ch',title:'Category',list:true,opts:D.CHAPTERS.map(function(c,i){return [c.id,(i+1)+'. '+c.title]}),get:function(k){return [k.ch]}},
 {key:'since',title:'Emerged in',opts:SB,get:function(k){return [sb(k.since)]}},
 {key:'st',title:'2026 status',opts:[['new-2026','New in 2026'],['active','Active in 2026']],get:function(k){var r=[];if(k.since>=2026)r.push('new-2026');if(k.upd>=2026)r.push('active');return r}},
 {key:'lv',title:'Level',opts:Object.keys(L).map(function(x){return [x,L[x]]}),get:function(k){return [k.level]}},
 {key:'tag',title:'Tags',opts:Object.keys(T).filter(function(t){return t!=='new-2026'&&t!=='updated-2026'}).map(function(t){return [t,T[t]]}),get:function(k){return k.tags}},
 {key:'kind',title:'Resource type',link:true,opts:Object.keys(K).map(function(x){return [x,K[x]]})},
 {key:'ly',title:'Resource published',link:true,opts:LB}
];
var S={q:'',view:'book',sort:'book',det:true,f:{}};FACETS.forEach(function(f){S.f[f.key]=new Set()});
function linkOk(l){var a=S.f.kind,b=S.f.ly;return (!a.size||a.has(l.kind))&&(!b.size||b.has(lb(l.year)))}
function linkFiltered(){return S.f.kind.size||S.f.ly.size}
function match(k,skip){
 if(S.q){var ws=S.q.toLowerCase().split(/\s+/);for(var i=0;i<ws.length;i++)if(ws[i]&&k.s.indexOf(ws[i])<0)return false}
 for(var j=0;j<FACETS.length;j++){var f=FACETS[j];if(f.key===skip||f.link)continue;var set=S.f[f.key];if(!set.size)continue;
  var v=f.get(k),ok=false;for(var m=0;m<v.length;m++)if(set.has(v[m])){ok=true;break}if(!ok)return false}
 if(skip!=='kind'&&skip!=='ly'&&linkFiltered()&&!k.links.some(linkOk))return false;
 if((skip==='kind'||skip==='ly')){var a=skip==='kind'?S.f.ly:S.f.kind;var fn=skip==='kind'?function(l){return !a.size||a.has(lb(l.year))}:function(l){return !a.size||a.has(l.kind)};if(a.size&&!k.links.some(fn))return false}
 return true}
function facetCount(f,val){var n=0;C.forEach(function(k){if(!match(k,f.key))return;
 if(f.link){var ok=k.links.some(function(l){return f.key==='kind'?(l.kind===val&&(!S.f.ly.size||S.f.ly.has(lb(l.year)))):(lb(l.year)===val&&(!S.f.kind.size||S.f.kind.has(l.kind)))});if(ok)n++}
 else if(f.get(k).indexOf(val)>=0)n++});return n}
// ---------- sidebar
var side=document.getElementById('filters');
function buildSide(){var h='';FACETS.forEach(function(f){h+='<section class="fs"><h4>'+e(f.title)+'<button type="button" data-clr="'+f.key+'">Clear</button></h4><div class="chips'+(f.list?' list':'')+'">';
 f.opts.forEach(function(o){var ic=f.key==='kind'?'<span class="kd k'+o[0]+'" aria-hidden="true">'+ICON[o[0]]+'</span>':'';
  h+='<button type="button" class="chip" data-f="'+f.key+'" data-v="'+e(o[0])+'" aria-pressed="false">'+ic+'<span>'+e(o[1])+'</span><span class="ct"></span></button>'});
 h+='</div></section>'});side.innerHTML=h;
 side.addEventListener('click',function(ev){var b=ev.target.closest('.chip');if(b){var s=S.f[b.dataset.f];if(s.has(b.dataset.v))s.delete(b.dataset.v);else s.add(b.dataset.v);render();return}
  var c=ev.target.closest('[data-clr]');if(c){S.f[c.dataset.clr].clear();render()}})}
function updSide(){side.querySelectorAll('.chip').forEach(function(b){var f=FACETS.filter(function(x){return x.key===b.dataset.f})[0];var on=S.f[f.key].has(b.dataset.v);b.setAttribute('aria-pressed',on);
 var n=facetCount(f,b.dataset.v);b.querySelector('.ct').textContent=n;b.classList.toggle('zero',!n&&!on)})}
// ---------- renderers
function pills(k){var h='<span class="pill">'+e(k.cht)+'</span>';
 if(k.since>=2026)h+='<span class="pill new">New in 2026</span>';else if(k.upd>=2026)h+='<span class="pill upd">Active in 2026</span>';
 h+='<span>Since '+k.since+'</span><span>'+e(L[k.level])+'</span>';
 k.tags.forEach(function(t){if(t!=='new-2026'&&t!=='updated-2026')h+='<span>#'+e(T[t])+'</span>'});return h}
function linksH(k){var lf=linkFiltered();return '<div class="links">'+k.links.map(function(l){var ok=linkOk(l);
 return '<a class="lk'+(lf&&!ok?' dim':'')+'" href="'+e(l.url)+'" target="_blank" rel="noopener"><span class="kd k'+l.kind+'" aria-hidden="true">'+ICON[l.kind]+'</span><span class="kt">'+K[l.kind]+'</span>'+e(l.label)+' <span class="ly">'+l.year+'</span></a>'}).join('')+'</div>'}
function body(k){var h='<p>'+e(k.text)+'</p>';
 if(S.det&&k.points&&k.points.length)h+='<ul class="pts">'+k.points.map(function(p){return '<li>'+e(p)+'</li>'}).join('')+'</ul>';
 if(S.det&&k.sota)h+='<div class="sota"><b>State of the art, Sept 2026</b>'+e(k.sota)+'</div>';return h+linksH(k)}
function entry(k){return '<article class="entry" id="'+k.id+'"><div class="eh"><h3>'+e(k.name)+'</h3>'+(k.aka?'<span class="pill">'+e(k.aka)+'</span>':'')+'</div><div class="meta">'+pills(k)+'</div>'+body(k)+'</article>'}
var SORTS={book:function(a,b){return a.ord-b.ord},az:function(a,b){return a.name.localeCompare(b.name)},newest:function(a,b){return b.since-a.since||a.ord-b.ord},
 oldest:function(a,b){return a.since-b.since||a.ord-b.ord},updated:function(a,b){return b.upd-a.upd||b.since-a.since||a.ord-b.ord},level:function(a,b){return 'BIA'.indexOf(a.level)-'BIA'.indexOf(b.level)||a.ord-b.ord}};
function vBook(list){var h='',by={};list.forEach(function(k){(by[k.ch]=by[k.ch]||[]).push(k)});
 D.CHAPTERS.forEach(function(c,i){var ks=by[c.id];if(!ks)return;ks.sort(SORTS[S.sort]);
  h+='<section class="chapter" id="ch-'+c.id+'"><div class="chead"><span class="cnum">'+String(i+1).padStart(2,'0')+'</span><h2>'+e(c.title)+'</h2></div><p class="intro">'+e(c.intro)+'</p>'+ks.map(entry).join('')+'</section>'});return h}
function vCards(list){list.sort(SORTS[S.sort]);return '<div class="grid">'+list.map(function(k){
 return '<article class="card" id="'+k.id+'"><span class="ch">'+e(k.chn+'. '+k.cht)+'</span><h3>'+e(k.name)+(k.aka?' <span class="pill">'+e(k.aka)+'</span>':'')+'</h3><div class="meta">'+
 (k.since>=2026?'<span class="pill new">New in 2026</span>':k.upd>=2026?'<span class="pill upd">Active 2026</span>':'')+'<span>Since '+k.since+'</span><span>'+L[k.level]+'</span></div><p>'+e(k.text)+'</p>'+
 '<details><summary>Key points and '+k.links.length+' resource'+(k.links.length>1?'s':'')+'</summary>'+(k.points&&k.points.length?'<ul class="pts">'+k.points.map(function(p){return '<li>'+e(p)+'</li>'}).join('')+'</ul>':'')+(k.sota?'<div class="sota"><b>State of the art, Sept 2026</b>'+e(k.sota)+'</div>':'')+linksH(k)+'</details></article>'}).join('')+'</div>'}
var RS={col:'year',dir:-1};
function vRes(list){var rows=[];list.forEach(function(k){k.links.forEach(function(l){if(!linkOk(l))return;if(S.q){var q=S.q.toLowerCase();if((l.label+' '+l.url+' '+k.name+' '+k.aka).toLowerCase().indexOf(q)<0&&k.s.indexOf(q)<0)return}rows.push({l:l,k:k})})});
 var dedupe={};rows=rows.filter(function(r){var key=r.l.url+'|'+r.k.id;if(dedupe[key])return false;dedupe[key]=1;return true});
 var f={year:function(r){return r.l.year},type:function(r){return K[r.l.kind]},title:function(r){return r.l.label.toLowerCase()},concept:function(r){return r.k.name.toLowerCase()},chapter:function(r){return r.k.chn}}[RS.col];
 rows.sort(function(a,b){var x=f(a),y=f(b);return (x<y?-1:x>y?1:0)*RS.dir||a.k.ord-b.k.ord});
 function th(c,t){return '<th><button type="button" data-sort="'+c+'">'+t+(RS.col===c?(RS.dir>0?' \u2191':' \u2193'):'')+'</button></th>'}
 return '<div class="tblwrap"><p class="count">'+rows.length+' resources</p><table><thead><tr>'+th('year','Year')+th('type','Type')+th('title','Resource')+th('concept','Concept')+th('chapter','Category')+'</tr></thead><tbody>'+
 rows.map(function(r){return '<tr><td class="y">'+r.l.year+'</td><td class="t"><span class="kd k'+r.l.kind+'">'+ICON[r.l.kind]+'</span> '+K[r.l.kind]+'</td><td><a href="'+e(r.l.url)+'" target="_blank" rel="noopener">'+e(r.l.label)+'</a><span class="u">'+e(r.l.url)+'</span></td><td><a href="#'+r.k.id+'" data-go="'+r.k.id+'">'+e(r.k.name)+'</a></td><td>'+e(r.k.chn+'. '+r.k.cht)+'</td></tr>'}).join('')+'</tbody></table></div>'}
function vTime(list){var by={};list.forEach(function(k){(by[k.since]=by[k.since]||[]).push(k)});var ys=Object.keys(by).map(Number).sort(function(a,b){return b-a});
 return '<div class="tl">'+ys.map(function(y){var ks=by[y].sort(SORTS.book);return '<div class="yr"><div><h3>'+y+'</h3><span class="n">'+ks.length+' concept'+(ks.length>1?'s':'')+' emerged</span></div><div class="tli">'+
 ks.map(function(k){return '<a href="#'+k.id+'" data-go="'+k.id+'">'+e(k.name)+'<span>'+e(k.cht)+'</span></a>'}).join('')+'</div></div>'}).join('')+'</div>'}
function vIndex(list){var items=[];list.forEach(function(k){items.push({t:k.name,s:k.cht,id:k.id});if(k.aka)k.aka.split(/,\s*/).forEach(function(a){items.push({t:a,s:'see '+k.name,id:k.id})})});
 items.sort(function(a,b){return a.t.localeCompare(b.t,undefined,{sensitivity:'base'})});var h='',cur='';
 items.forEach(function(it){var c=it.t[0].toUpperCase();if(!/[A-Z]/.test(c))c='#';if(c!==cur){cur=c;h+='<h4>'+c+'</h4>'}h+='<a href="#'+it.id+'" data-go="'+it.id+'"><b>'+e(it.t)+'</b> <span>'+e(it.s)+'</span></a>'});return '<div class="idx">'+h+'</div>'}
// ---------- main render
var out=document.getElementById('out'),cnt=document.getElementById('cnt'),act=document.getElementById('act');
function render(){var list=C.filter(function(k){return match(k)});
 var v={book:vBook,cards:vCards,res:vRes,time:vTime,index:vIndex}[S.view];
 out.innerHTML=list.length?v(list.slice()):'<p class="empty">No concepts match these filters. Remove a filter or clear the search.</p>';
 cnt.textContent=list.length+' of '+C.length+' concepts';
 var h='';FACETS.forEach(function(f){S.f[f.key].forEach(function(v){var o=f.opts.filter(function(x){return x[0]===v})[0];h+='<button type="button" class="chip" aria-pressed="true" data-rm="'+f.key+'" data-v="'+e(v)+'">'+e(f.title)+': '+e(o?o[1]:v)+'</button>'})});
 if(S.q)h+='<button type="button" class="chip" aria-pressed="true" data-rmq="1">Search: '+e(S.q)+'</button>';
 act.innerHTML=h?h+'<button type="button" class="clear" id="clearall">Clear all</button>':'';
 document.querySelectorAll('.tabs button').forEach(function(b){b.setAttribute('aria-selected',b.dataset.v===S.view)});
 document.getElementById('sort').disabled=(S.view==='res'||S.view==='time'||S.view==='index');
 updSide();saveHash()}
act.addEventListener('click',function(ev){var b=ev.target.closest('[data-rm]');if(b){S.f[b.dataset.rm].delete(b.dataset.v);render();return}
 if(ev.target.closest('[data-rmq]')){S.q='';q.value='';render();return}if(ev.target.id==='clearall'){FACETS.forEach(function(f){S.f[f.key].clear()});S.q='';q.value='';render()}});
out.addEventListener('click',function(ev){var s=ev.target.closest('[data-sort]');if(s){if(RS.col===s.dataset.sort)RS.dir*=-1;else{RS.col=s.dataset.sort;RS.dir=s.dataset.sort==='year'?-1:1}render();return}
 var g=ev.target.closest('[data-go]');if(g){ev.preventDefault();S.view='book';render();var el=document.getElementById(g.dataset.go);if(el){el.scrollIntoView();el.classList.remove('hl');void el.offsetWidth;el.classList.add('hl')}}});
var q=document.getElementById('q'),tmr;q.addEventListener('input',function(){clearTimeout(tmr);tmr=setTimeout(function(){S.q=q.value.trim();render()},120)});
document.querySelector('.tabs').addEventListener('click',function(ev){var b=ev.target.closest('button');if(b){S.view=b.dataset.v;render();window.scrollTo(0,document.querySelector('.toolbar').offsetTop)}});
document.getElementById('sort').addEventListener('change',function(ev){S.sort=ev.target.value;render()});
var det=document.getElementById('det');det.addEventListener('change',function(){S.det=det.checked;render()});
document.addEventListener('keydown',function(ev){if(ev.key==='/'&&document.activeElement!==q&&!/input|select|textarea/i.test(document.activeElement.tagName)){ev.preventDefault();q.focus()}});
// hash state
function saveHash(){var p=new URLSearchParams();if(S.q)p.set('q',S.q);if(S.view!=='book')p.set('view',S.view);if(S.sort!=='book')p.set('sort',S.sort);if(!S.det)p.set('det','0');
 FACETS.forEach(function(f){if(S.f[f.key].size)p.set(f.key,Array.from(S.f[f.key]).join(','))});var s=p.toString();
 try{history.replaceState(null,'',s?'#'+s:location.pathname+location.search)}catch(x){}}
function loadHash(){var h=location.hash.slice(1);if(!h||h.indexOf('=')<0)return;var p=new URLSearchParams(h);S.q=p.get('q')||'';q.value=S.q;S.view=p.get('view')||'book';S.sort=p.get('sort')||'book';S.det=p.get('det')!=='0';det.checked=S.det;
 document.getElementById('sort').value=S.sort;FACETS.forEach(function(f){var v=p.get(f.key);if(v)v.split(',').forEach(function(x){S.f[f.key].add(x)})})}
// theme
var root=document.documentElement;function setTheme(t){root.setAttribute('data-theme',t);document.querySelectorAll('.tb').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.t===t)});try{localStorage.setItem('acb2-theme',t)}catch(x){}}
var saved=null;try{saved=localStorage.getItem('acb2-theme')}catch(x){}
setTheme(saved||((window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'ink':'paper'));
document.querySelectorAll('.tb').forEach(function(b){b.addEventListener('click',function(){setTheme(b.dataset.t)})});
// mobile
var sd=document.querySelector('.side');document.getElementById('fbtn').addEventListener('click',function(){sd.classList.toggle('open')});
document.addEventListener('click',function(ev){if(sd.classList.contains('open')&&!sd.contains(ev.target)&&ev.target.id!=='fbtn')sd.classList.remove('open')});
// presets
document.querySelectorAll('[data-preset]').forEach(function(b){b.addEventListener('click',function(){FACETS.forEach(function(f){S.f[f.key].clear()});S.q='';q.value='';
 var p=b.dataset.preset.split(':');S.f[p[0]].add(p[1]);if(p[2])S.view=p[2];render();window.scrollTo(0,document.querySelector('.toolbar').offsetTop)})});
buildSide();loadHash();render();
})();
"""

THEMES = [("paper","Paper"),("ink","Ink"),("sepia","Sepia"),("blueprint","Blueprint"),("forest","Forest"),("contrast","High contrast")]
themes = "".join(f'<button type="button" class="tb" data-t="{t}" aria-pressed="false"><span class="sw sw-{t}"></span>{n}</button>' for t, n in THEMES)
data_json = json.dumps(D, ensure_ascii=False).replace("</", "<\\/")

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(M["title"])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<aside class="side" aria-label="Filters and settings">
<p class="brand">{esc(M["title"])}</p>
<p class="ed">{esc(M["edition"])}</p>
<section class="fs"><h4>Theme</h4><div class="themes">{themes}</div></section>
<div id="filters"></div>
</aside>
<main>
<header class="hero">
<h1>{esc(M["title"])}</h1>
<p class="sub">{esc(M["subtitle"][0].upper()+M["subtitle"][1:])}. Current to {esc(M["asof"])}, with definitions, key points, state-of-the-art notes and dated resources for every concept.</p>
<div class="stats"><span><b>{len(D["CHAPTERS"])}</b>categories</span><span><b>{nc}</b>concepts</span><span><b>{nl}</b>dated resources</span><span><b>{n26}</b>active in 2026</span></div>
<p style="font-family:var(--f-ui);font-size:14px;margin:18px 0 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center"><span style="color:var(--mut)">Quick views:</span>
<button type="button" class="chip" data-preset="st:new-2026">New in 2026</button>
<button type="button" class="chip" data-preset="ly:2026:res">2026 resources</button>
<button type="button" class="chip" data-preset="kind:G:res">All GitHub repos</button>
<button type="button" class="chip" data-preset="kind:P:res">All papers</button>
<button type="button" class="chip" data-preset="lv:B">Beginner concepts</button>
<button type="button" class="chip" data-preset="tag:open-standard">Open standards</button></p>
</header>
<div class="toolbar">
<div class="row"><button type="button" class="fbtn" id="fbtn">Filters</button>
<input id="q" type="search" placeholder="Search concepts, resources, acronyms  ( / )" aria-label="Search concepts and resources">
<div class="tabs" role="tablist" aria-label="View">
<button type="button" role="tab" data-v="book">Book</button><button type="button" role="tab" data-v="cards">Cards</button><button type="button" role="tab" data-v="res">Resources</button><button type="button" role="tab" data-v="time">Timeline</button><button type="button" role="tab" data-v="index">A–Z</button></div>
<select id="sort" aria-label="Sort concepts"><option value="book">Book order</option><option value="az">A–Z</option><option value="newest">Newest first</option><option value="oldest">Oldest first</option><option value="updated">Recently active</option><option value="level">Beginner first</option></select>
<label class="tog"><input type="checkbox" id="det" checked> Details</label></div>
<div class="row"><span class="count" id="cnt"></span><div class="act" id="act"></div></div>
</div>
<div id="out"></div>
<footer>{esc(M["title"])}. {esc(M["edition"])}. Resource years show when an article, paper or spec was published, or when a repository or site launched (approximate for long-running projects). The 2026 landscape chapter reflects public reporting as of {esc(M["asof"])} and will date quickly. Filters are saved in the page address, so you can bookmark or share a filtered view.</footer>
</main>
</div>
<script id="data" type="application/json">{data_json}</script>
<script>{JS}</script>
</body>
</html>'''
open("editions/AI_Concept_Book.html", "w").write(page)
print("html ok", len(page)//1024, "KB")
