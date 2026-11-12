# -*- coding: utf-8 -*-
import html, random
from cases import INTRO, CASES, WHAT, HOW, SYSTEMS, RULES, FAQ
import re, json
from parts import AGENTS, FLOW_TRIGGER, FLOW_STEPS, FLOW_END, NUMBERS
from icons import svg
e = html.escape
random.seed(7)

# ── the week: 5 days x 11 hours. some blocks are manual work, they empty out.
DAYS = ["Mon","Tue","Wed","Thu","Fri"]
cells=[]
ROWS = 22
for h in range(ROWS):
    for d in range(5):
        r = random.random()
        if r < .36:   k, delay = "m", 1700 + (h*5+d)*13   # manual — clears
        elif r < .50: k, delay = "w", 0                    # real work — stays
        else:         k, delay = "e", 0                    # empty
        cells.append('<i class="%s" style="--k:%d"></i>' % (k, h*5+d))
MANUAL = sum(1 for c in cells if 'class="m"' in c)
HOURS = round(MANUAL*.5)
WEEK = ('<div class="week" id="week" aria-hidden="true">%s</div>' % "".join(cells))
DAYLBL = "".join('<span>%s</span>' % d for d in DAYS)
HOURS_COL = "".join('<span>%s</span>' % h for h in ["08","10","12","14","16","18","20"])

MARKS = {
 "build": '<svg class="pm" viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="36" width="36" height="5" rx="1.5" fill="var(--door)"/><rect x="6" y="27" width="27" height="5" rx="1.5" fill="var(--door)"/><rect x="6" y="18" width="18" height="5" rx="1.5" fill="var(--door)"/><rect x="6" y="9" width="9" height="5" rx="1.5" fill="var(--ochre)"/></svg>',
 "automate": '<svg class="pm auto" viewBox="0 0 48 48" aria-hidden="true"><g class="ring"><path d="M37.9 16A16 16 0 1 0 40 24" fill="none" stroke="var(--door)" stroke-width="1.6" stroke-linecap="round"/><circle cx="40" cy="24" r="2.6" fill="var(--ochre)"/></g><circle class="core" cx="24" cy="24" r="2.4" fill="var(--door)"/></svg>',
 "create": '<svg class="pm" viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="8" width="14" height="14" rx="1.5" fill="var(--door)"/><circle class="draw" cx="31" cy="29" r="11" fill="none" stroke="var(--door)" stroke-width="1.6"/><rect x="6" y="36" width="14" height="5" rx="1.5" fill="var(--ochre)"/></svg>',
}
def mark(name, cls="pm"): return MARKS[name]
_drng = random.Random(11)
def divider():
    cells=[]
    for i in range(14):
        r=_drng.random()
        k = "o" if r<.14 else ("b" if r<.34 else "e")
        cells.append('<i class="%s" style="--n:%d"></i>' % (k, i))
    return '<div class="wrap"><div class="dv" aria-hidden="true">%s</div></div>' % "".join(cells)
HEROMARK = '<div class="mark" aria-hidden="true">' + "".join('<i class="%s"></i>' % k for k in ["b","e","o","e","b","e","o","e","b","b","e","e"]) + '</div>'

def gap(t): return t.startswith("[")
def P(t, cls=""):
    c = (cls + " gap").strip() if gap(t) else cls
    return '<p%s>%s</p>' % ((' class="%s"' % c) if c else "", e(t))

cases = "\n".join(
 """<article class="case">
  <div class="chd"><h3>%s</h3><p class="meta">%s</p></div>
  <div class="arc">
    <div><span>Challenge</span>%s</div>
    <div><span>Work delivered</span>%s</div>
    <div><span>Status</span>%s</div>
  </div>
 </article>""" % (e(c["who"]), e(c["kind"]), P(c["before"]), P(c["did"]), P(c["now"]))
 for c in CASES)

AG_IC = ["moon_mail","invoice","cv_read","calendar_tick","pen","speech","bars","folder_in"]
agents = "\n".join(
 '<li style="--i:%d">%s<b>%s</b><span>%s</span></li>' % (i, svg(AG_IC[i]), e(a), e(b))
 for i,(a,b) in enumerate(AGENTS))

flow = ('<div class="flow">'
  '<div class="fnode t">%s<p>%s</p></div>'
  '<div class="fline"><i></i></div>'
  '<div class="fmid">%s</div>'
  '<div class="fline"><i style="--d:1.1s"></i></div>'
  '<div class="fnode o">%s<p>%s</p></div>'
  '</div>') % (svg("form"), e(FLOW_TRIGGER),
    "".join('<div class="fstep" style="--i:%d"><span></span>%s</div>' % (i, e(x))
            for i,x in enumerate(FLOW_STEPS)),
    svg("eye"), e(FLOW_END))

nums = "\n".join(
 '<div%s><b>%s</b><span>%s</span><i>%s</i></div>' % (' class="fill"' if n.startswith("[") else "",
   e(n), e(l), e(w)) for n,l,w in NUMBERS)

what = "\n".join('<div>%s<span class="pl">%s</span><h3>%s</h3><p>%s</p></div>' % (mark(m), e(k), e(a), e(b)) for m,k,a,b in WHAT)
systems = "\n".join('<article class="sys"><div><h3>%s</h3><p class="prob">%s</p></div><div><p>%s</p><p class="st">%s</p></div></article>' % (e(a),e(b),e(c),e(d)) for a,b,c,d in SYSTEMS)
rules = "\n".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a,b in RULES)
faq = "\n".join('<div><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a,b in FAQ)
SITE = "https://houssem-gabsi.vercel.app/"
EMAIL = "unfollow.designs@gmail.com"
HEAD = "Most of a week goes on work nobody should be doing by hand."
TITLE = "Websites, automation and content for firms | Houssem Gabsi"
OG_TITLE = "Websites, automation and content for established firms"
DESC = ("A studio of one for established firms. Websites, booking systems, automated follow-up "
        "and content systems. A person approves before anything is sent.")
OG_DESC = "Follow-ups that are never forgotten, bookings confirmed, candidates scored against your own criteria. Built by one person, approved by yours."
OG_ALT = HEAD + " Websites, automation and content for established firms."
ABOUT = "A studio of one that builds websites, booking systems, follow-up and candidate scoring automations, and content systems for established firms."
LANGS = ["English","French","Arabic"]
PLACE = {"@type":"PostalAddress","addressLocality":"Tunis","addressCountry":"TN"}
LD = json.dumps({"@context":"https://schema.org","@graph":[
 {"@type":"WebSite","@id":SITE+"#website","url":SITE,"name":"Houssem Gabsi","description":ABOUT,
  "inLanguage":"en","publisher":{"@id":SITE+"#studio"}},
 {"@type":"WebPage","@id":SITE+"#webpage","url":SITE,"name":TITLE,"description":DESC,"inLanguage":"en",
  "isPartOf":{"@id":SITE+"#website"},"about":{"@id":SITE+"#studio"},
  "primaryImageOfPage":{"@type":"ImageObject","url":SITE+"og.png","width":1200,"height":630}},
 {"@type":"ProfessionalService","@id":SITE+"#studio","name":"Houssem Gabsi",
  "description":ABOUT,
  "founder":{"@id":SITE+"#person"},
  "url":SITE,
  "image":SITE+"og.png",
  "email":EMAIL,
  "address":PLACE,
  "areaServed":["United States","Europe","Tunisia"],
  "availableLanguage":LANGS,
  "knowsAbout":["website design and build","booking systems","invoice and quote follow-up","candidate scoring for recruiting firms","content systems","answer engine optimisation","branding"],
  "hasOfferCatalog":{"@type":"OfferCatalog","name":"Services","itemListElement":[
    {"@type":"Offer","itemOffered":{"@type":"Service","name":t,"description":d,"provider":{"@id":SITE+"#studio"}}} for _,_,t,d in WHAT]}},
 {"@type":"Person","@id":SITE+"#person","name":"Houssem Gabsi","url":SITE,"email":EMAIL,
  "worksFor":{"@id":SITE+"#studio"},"knowsLanguage":LANGS,"address":PLACE},
 {"@type":"ItemList","@id":SITE+"#work","name":"Selected work","itemListElement":[
    {"@type":"ListItem","position":i+1,"item":{"@type":"CreativeWork","@id":SITE+"#case-%d" % i,"url":SITE+"#case-%d" % i,
      "name":c["who"],"description":c["did"],"creator":{"@id":SITE+"#person"}}} for i,c in enumerate(CASES)]},
 {"@type":"FAQPage","@id":SITE+"#faq","isPartOf":{"@id":SITE+"#webpage"},"mainEntity":[
    {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
]}, ensure_ascii=False, indent=1)

# plain-text summary for AI assistants, written from the same lists as the page
def _llms():
    L = ["# Houssem Gabsi", "", "> " + ABOUT, "",
         "Based in Tunis. Works in English, French and Arabic. Contact: " + EMAIL, "",
         "Site: " + SITE, "", "## Services", ""]
    L += ["- %s: %s" % (t, d) for _,_,t,d in WHAT]
    L += ["", "## Systems", ""]
    L += ["- %s: %s %s Status: %s" % (a, b, c, d) for a,b,c,d in SYSTEMS]
    L += ["", "## Selected work", "", "Clients are not named."]
    for c in CASES:
        L += ["", "### " + c["who"], "", c["kind"], "",
              "- Challenge: " + c["before"], "- Work delivered: " + c["did"], "- Status: " + c["now"]]
    L += ["", "## How I work", ""]
    L += ["- %s %s" % (a, b) for a,b in RULES]
    L += ["", "## Process", ""]
    L += ["%d. %s: %s" % (i+1, a, b) for i,(a,b) in enumerate(HOW)]
    L += ["", "## Common questions"]
    for q,a in FAQ: L += ["", "### " + q, "", a]
    L += ["", "## Free tool", "",
          "- [Stock, sales and production tracker](%stools/stock-sales-production-tracker/): a free tracker for product businesses." % SITE, ""]
    return "\n".join(L)
LLMS = _llms()
how  = "\n".join('<li><h3>%s</h3><p>%s</p></li>' % (e(a), e(b)) for a,b in HOW)

HTML = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TITLEHERE</title>
<meta name="description" content="DESCHERE">
<meta name="author" content="Houssem Gabsi">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="theme-color" content="#E9E7DE">
<link rel="canonical" href="SITEHERE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="/llms.txt" title="Plain-text summary of this site">
<meta property="og:site_name" content="Houssem Gabsi">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="SITEHERE">
<meta property="og:image" content="SITEHEREog.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="OGALTHERE">
<meta property="og:type" content="website">
<meta property="og:title" content="OGTITLEHERE">
<meta property="og:description" content="OGDESCHERE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="OGTITLEHERE">
<meta name="twitter:description" content="OGDESCHERE">
<meta name="twitter:image" content="SITEHEREog.png">
<script type="application/ld+json">
LDHERE
</script>
<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{font-family:Archivo;font-style:normal;font-weight:400 600;font-display:swap;src:url(/fonts/archivo-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:Archivo;font-style:normal;font-weight:400 600;font-display:swap;src:url(/fonts/archivo-latin-ext.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C4,U+2113,U+2C60-2C7F,U+A720-A7FF}
@font-face{font-family:Fraunces;font-style:normal;font-weight:300 700;font-display:swap;src:url(/fonts/fraunces-latin.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:Fraunces;font-style:normal;font-weight:300 700;font-display:swap;src:url(/fonts/fraunces-latin-ext.woff2) format("woff2");unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C4,U+2113,U+2C60-2C7F,U+A720-A7FF}
:root{
  --wall:#E9E7DE;       /* lime-washed wall */
  --wall-2:#DFDCD1;
  --ink:#1B201C;        /* warm near-black, green cast */
  --ink-soft:#4E554E;
  --door:#2B4C6F;       /* deep Tunisian door blue */
  --ochre:#B4743A;
  --sand:#CFC9B8;
  --pad:clamp(22px,5vw,78px);
  --ease:cubic-bezier(.22,1,.36,1);
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--wall);color:var(--ink);
  font-family:Archivo,system-ui,sans-serif;font-size:clamp(16px,1.02vw,17.5px);
  line-height:1.6;-webkit-font-smoothing:antialiased;position:relative}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:9;opacity:.5;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.16'/%3E%3C/svg%3E")}
::selection{background:var(--door);color:var(--wall)}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto;padding:0 var(--pad)}

h1,h2,h3,h4{font-family:Fraunces,Georgia,serif;font-weight:400;
  font-variation-settings:"opsz" 110,"SOFT" 28,"WONK" 1;letter-spacing:-.018em;line-height:1.06}

/* ── hero: the week ── */
.hero{padding:clamp(48px,8vh,88px) 0 clamp(36px,5vh,60px)}
.htop{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);
  gap:clamp(24px,5vw,72px);align-items:end}
@media(max-width:860px){.htop{grid-template-columns:1fr;align-items:start;gap:20px}}
.hero h1{font-size:clamp(2.1rem,4.4vw,3.6rem);max-width:15ch;
  font-variation-settings:"opsz" 144,"SOFT" 36,"WONK" 1}
.hero .sub{max-width:44ch;font-size:clamp(17px,1.25vw,19.5px);
  color:var(--ink-soft);line-height:1.58}

.weekwrap{margin-top:clamp(34px,5vh,58px)}
.wk-head{display:flex;justify-content:space-between;align-items:baseline;gap:20px;
  padding-bottom:12px;border-bottom:1px solid var(--sand)}
.wk-head p{font-size:14.5px;color:var(--ink-soft);max-width:40ch}
.wk-head b{font-family:Fraunces,serif;font-weight:400;font-size:clamp(1rem,1.3vw,1.2rem);
  font-variation-settings:"opsz" 40,"SOFT" 20,"WONK" 0}
.days{display:grid;grid-template-columns:repeat(5,1fr);gap:clamp(3px,.34vw,5px);
  margin:12px 0 6px}
.days span{font-size:12.5px;color:var(--ink-soft)}
.week{display:grid;grid-template-columns:repeat(5,1fr);gap:clamp(2px,.26vw,4px)}
.week i{display:block;height:clamp(8px,.78vw,11px);border-radius:1.5px}
.week i.e{background:transparent;box-shadow:inset 0 0 0 1px rgba(27,32,28,.09)}
.week i.w{background:var(--door)}
.week i.m{background:var(--ochre)}
.week.play i.m{animation:clear .55s var(--ease) var(--d) forwards}
@keyframes clear{to{background:transparent;box-shadow:inset 0 0 0 1px rgba(27,32,28,.09)}}
.key{display:flex;gap:26px;margin-top:20px;font-size:13px;color:var(--ink-soft);flex-wrap:wrap}
.key i{display:inline-block;width:11px;height:11px;border-radius:2px;margin-right:7px;
  vertical-align:-1px}
.key .k1 i{background:var(--door)} .key .k2 i{background:var(--ochre)}


/* ── icons ── */
.ic{width:22px;height:22px;color:var(--door);flex:none}

/* ── the team you don't pay for ── */
.team{margin-top:clamp(32px,4.6vh,50px);list-style:none;display:grid;
  grid-template-columns:repeat(auto-fit,minmax(224px,1fr));gap:1px;background:var(--sand);
  border:1px solid var(--sand)}
.team li{background:var(--wall);padding:clamp(18px,2.2vw,24px);display:grid;gap:9px;
  align-content:start;position:relative;overflow:hidden}
.team li::after{content:"";position:absolute;inset:auto 0 0 0;height:2px;background:var(--door);
  transform:scaleX(0);transform-origin:0 50%;
  animation:sweep 5.6s var(--ease) calc(var(--i) * .34s) infinite}
@keyframes sweep{0%{transform:scaleX(0)}10%{transform:scaleX(1)}38%{transform:scaleX(1)}
  48%{transform:scaleX(0);transform-origin:100% 50%}100%{transform:scaleX(0);transform-origin:100% 50%}}
.team b{font-family:Fraunces,serif;font-weight:400;font-size:clamp(1rem,1.25vw,1.13rem);
  font-variation-settings:"opsz" 30,"SOFT" 22,"WONK" 0;letter-spacing:-.015em;line-height:1.25}
.team span{font-size:14px;color:var(--ink-soft)}
.teamnote{margin-top:22px;font-size:15px;color:var(--ink-soft);max-width:60ch}

/* ── a workflow, drawn ── */
.flow{margin-top:clamp(32px,4.6vh,50px);display:grid;
  grid-template-columns:minmax(0,1fr) 54px minmax(0,1.5fr) 54px minmax(0,1fr);
  gap:clamp(10px,1.6vw,22px);align-items:center}
.fnode{border:1px solid var(--ink);padding:clamp(16px,2vw,22px);display:grid;gap:10px;
  align-content:start;background:var(--wall)}
.fnode p{font-size:15px;line-height:1.4}
.fnode.o{background:var(--ink);color:var(--wall);border-color:var(--ink)}
.fnode.o .ic{color:var(--wall)}
.fline{position:relative;height:1px;background:var(--sand)}
.fline i{position:absolute;top:-2.5px;left:0;width:6px;height:6px;border-radius:50%;
  background:var(--ochre);animation:run 2.4s var(--ease) var(--d,0s) infinite}
@keyframes run{0%{left:0;opacity:0}12%{opacity:1}88%{opacity:1}100%{left:100%;opacity:0}}
.fmid{display:grid;gap:7px}
.fstep{display:flex;align-items:center;gap:11px;font-size:14.5px;color:var(--ink-soft);
  border:1px solid var(--sand);padding:9px 13px;background:var(--wall)}
.fstep span{width:7px;height:7px;border-radius:50%;background:var(--sand);flex:none;
  animation:lit 5.6s var(--ease) calc(.5s + var(--i) * .3s) infinite}
@keyframes lit{0%,100%{background:var(--sand)}8%,30%{background:var(--door)}}
@media(max-width:900px){.flow{grid-template-columns:1fr;gap:14px}
  .fline{height:26px;width:1px;justify-self:start;margin-left:22px}
  .fline i{top:0;left:-2.5px;animation:rund 2.4s var(--ease) var(--d,0s) infinite}
  @keyframes rund{0%{top:0;opacity:0}12%{opacity:1}88%{opacity:1}100%{top:100%;opacity:0}}}

/* ── numbers ── */
.nums{margin-top:clamp(30px,4.4vh,48px);display:grid;
  grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:clamp(20px,2.6vw,40px)}
.nums div{border-top:2px solid var(--ink);padding-top:15px}
.nums b{display:block;font-family:Fraunces,serif;font-weight:400;
  font-size:clamp(2.2rem,4.6vw,3.5rem);line-height:.95;letter-spacing:-.03em;
  font-variation-settings:"opsz" 120,"SOFT" 30,"WONK" 1}
.nums .fill b{color:var(--ochre)}
.nums span{display:block;margin-top:9px;font-size:15px}
.nums i{display:block;margin-top:3px;font-style:normal;font-size:13.5px;color:var(--ink-soft)}


/* ── page chrome ── */
.bar{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;justify-content:space-between;
  align-items:center;gap:18px;padding:13px var(--pad);
  background:rgba(233,231,222,.86);backdrop-filter:blur(12px);
  border-bottom:1px solid transparent;transform:translateY(-102%);
  transition:transform .42s var(--ease),border-color .42s}
.bar.on{transform:none;border-bottom-color:var(--sand)}
.bar b{font-family:Fraunces,serif;font-weight:400;font-size:15px;
  font-variation-settings:"opsz" 24,"SOFT" 20,"WONK" 0}
.bar a{font-size:14px;color:var(--ink-soft);text-decoration:none;
  border-bottom:1px solid var(--sand);padding-bottom:1px;transition:color .25s,border-color .25s}
@media(hover:hover) and (pointer:fine){.bar a:hover{color:var(--ochre);border-color:var(--ochre)}}

/* ── the mark ── */
.mark{width:34px;height:34px;color:var(--ochre);margin-bottom:clamp(26px,3.4vh,38px);display:block}
.mark circle,.mark path{transform-origin:50% 50%}
.mark .r1{animation:spin 26s linear infinite}
.mark .r2{animation:spin 18s linear infinite reverse}
@keyframes spin{to{transform:rotate(360deg)}}

/* ── hero type entrance: one orchestrated moment ── */
.hero h1 span{display:inline-block;opacity:0;transform:translateY(.42em);
  animation:rise .78s var(--ease) forwards;animation-delay:calc(var(--w) * .052s)}
@keyframes rise{to{opacity:1;transform:none}}
.hero .sub{opacity:0;animation:rise .8s var(--ease) .62s forwards}

/* ── the counter ── */
.count{margin-top:clamp(22px,3vh,30px);display:flex;align-items:baseline;gap:12px;
  opacity:0;animation:rise .8s var(--ease) 1.4s forwards}
.count b{font-family:Fraunces,serif;font-weight:400;font-size:clamp(2.4rem,5vw,3.9rem);
  line-height:.9;letter-spacing:-.035em;color:var(--ochre);
  font-variation-settings:"opsz" 120,"SOFT" 30,"WONK" 1;font-variant-numeric:tabular-nums}
.count span{font-size:15.5px;color:var(--ink-soft);max-width:26ch;line-height:1.35}

/* ── hour gutter on the week ── */
.grid{display:grid;grid-template-columns:30px 1fr;gap:clamp(8px,1.1vw,14px)}
.hrs{display:grid;align-content:space-between;padding-top:2px}
.hrs span{font-size:11px;color:var(--ink-soft);line-height:1}
.gcol{min-width:0}


.qa{display:grid;gap:clamp(26px,3.4vw,44px);grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));
  margin-top:clamp(30px,4vw,46px)}
.qa h3{font-size:clamp(1.08rem,1.35vw,1.26rem);margin-bottom:9px;
  font-variation-settings:"opsz" 34,"SOFT" 24,"WONK" 0}
.qa p{color:var(--ink-soft);font-size:15.5px;max-width:46ch}


/* ── v3.1: studio marks, systems, rules ── */
.dv{display:flex;gap:4px;padding:2px 0}
.dv i{display:block;width:13px;height:5px;border-radius:1.5px;box-shadow:inset 0 0 0 1px rgba(27,32,28,.13)}
.dv i.b{background:var(--door);box-shadow:none}
.dv i.o{background:var(--ochre);box-shadow:none}
.mark{display:grid;grid-template-columns:repeat(3,13px);gap:3px;width:max-content;
  margin-bottom:clamp(22px,3vh,34px)}
.mark i{display:block;height:5px;border-radius:1.5px;box-shadow:inset 0 0 0 1px rgba(27,32,28,.16)}
.mark i.b{background:var(--door);box-shadow:none}
.mark i.o{background:var(--ochre);box-shadow:none;animation:pulse 5.2s var(--ease) infinite}
.mark i.o:nth-of-type(7){animation-delay:2.6s}
@keyframes pulse{0%,38%{background:var(--ochre)}50%,88%{background:transparent;box-shadow:inset 0 0 0 1px rgba(27,32,28,.16)}100%{background:var(--ochre)}}
.pm{display:block;width:46px;height:46px;margin-bottom:16px}
.pl{display:block;font-size:14px;color:var(--ochre);margin-bottom:6px}
.sysl{margin-top:clamp(30px,4.4vh,48px);display:grid}
.sys{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:clamp(16px,3.4vw,50px);
  padding:clamp(22px,3vh,30px) 0;border-top:1px solid var(--sand)}
.sys h3{font-size:clamp(1.14rem,1.6vw,1.42rem);max-width:22ch;font-variation-settings:"opsz" 40,"SOFT" 24,"WONK" 1}
.sys .prob{margin-top:8px;color:var(--ink-soft);font-size:15px;max-width:38ch}
.sys p{max-width:56ch}
.sys .st{margin-top:10px;font-size:14px;color:var(--door)}
.sysnote{margin-top:22px;font-size:15px;color:var(--ink-soft);max-width:62ch}
.rules{margin-top:clamp(30px,4.4vh,48px);display:grid;gap:clamp(24px,3vw,42px);
  grid-template-columns:repeat(auto-fit,minmax(min(100%,270px),1fr))}
.rules div{border-top:2px solid var(--ink);padding-top:14px}
.rules h3{font-size:clamp(1.06rem,1.35vw,1.22rem);font-variation-settings:"opsz" 34,"SOFT" 24,"WONK" 0}
.rules p{margin-top:8px;color:var(--ink-soft);font-size:15px;max-width:44ch}
.wk-note{margin-top:10px;font-size:13px;color:var(--ink-soft)}
.close .lead{margin-top:14px;color:rgba(233,231,222,.72);max-width:46ch}
@media(max-width:820px){.sys{grid-template-columns:1fr;gap:10px}}
@media(prefers-reduced-motion:reduce){.mark i.o{animation:none}}


/* ── v3.2 motion ── */
.wks{display:inline-block;color:var(--ochre);transition:opacity .35s var(--ease),transform .35s var(--ease)}
.wks.sw{opacity:0;transform:translateY(.3em)}
.week i{transition:transform .25s var(--ease)}
@media(hover:hover) and (pointer:fine){.week i.w:hover{transform:scaleY(1.7)}}
.case,.sys{position:relative}
.case::before,.sys::before{content:"";position:absolute;top:-1px;left:0;height:2px;width:100%;background:var(--ochre);
  transform:scaleX(0);transform-origin:left;transition:transform 1.1s var(--ease)}
.sys .st::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--door);
  margin-right:9px;vertical-align:1px;animation:beat 2.4s ease-in-out infinite}
@keyframes beat{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.35;transform:scale(.7)}}
.sys{transition:padding-left .4s var(--ease)}
@media(hover:hover) and (pointer:fine){.sys:hover{padding-left:14px}.sys:hover::before{transform:scaleX(1)}}
.rules div,.how li{border-top-color:transparent;position:relative}
.rules div::after,.how li::after{content:"";position:absolute;top:-2px;left:0;width:100%;height:2px;background:var(--ink);
  transform-origin:left;transition:transform .9s var(--ease);transition-delay:calc(var(--i,0) * .22s)}
.how li::before{transition:color .5s var(--ease);transition-delay:calc(var(--i,0) * .22s + .5s)}
.pm rect,.pm circle,.pm path{transform-box:fill-box;transform-origin:left center}
.pm.auto .ring{transform-origin:center;animation:spin 9s linear infinite}
.pm.auto .core{transform-origin:center;animation:beat 2.4s ease-in-out infinite}
.pm .draw{stroke-dasharray:70;stroke-dashoffset:0;transition:stroke-dashoffset 1.3s var(--ease) .25s}
.close a.mail{background:linear-gradient(currentColor,currentColor) 0 100%/0 2px no-repeat;border-bottom-color:transparent;
  transition:background-size 1.2s var(--ease) .3s,color .3s var(--ease)}

html.js h2 .w{display:inline-block;opacity:0;transform:translateY(.45em);
  transition:opacity .7s var(--ease),transform .7s var(--ease);transition-delay:calc(var(--w) * .055s)}
html.js h2.in .w{opacity:1;transform:none}
html.js .rv{opacity:0;transform:translateY(16px);transition:opacity .8s var(--ease),transform .8s var(--ease);
  transition-delay:calc(var(--i,0) * .09s)}
html.js .rv.in{opacity:1;transform:none}
html.js .dv i{transform:scaleX(0);transform-origin:left;transition:transform .5s var(--ease);transition-delay:calc(var(--n) * .045s)}
html.js .dv.in i{transform:none}
html.js .arc > div{opacity:0;transform:translateX(14px);transition:opacity .7s var(--ease),transform .7s var(--ease)}
html.js .arc > div:nth-child(1){transition-delay:.25s}
html.js .arc > div:nth-child(2){transition-delay:.5s}
html.js .arc > div:nth-child(3){transition-delay:.75s}
html.js .case.in .arc > div{opacity:1;transform:none}
html.js .case.in::before,html.js .sys.in::before{transform:scaleX(1)}
html.js .case.in::before{transition-delay:.1s}
html.js .sys.in::before{transform:scaleX(.12)}
html.js .rules div::after,html.js .how li::after{transform:scaleX(0)}
html.js .rules div.in::after,html.js .how li.in::after{transform:scaleX(1)}
html.js .how li.in::before{color:var(--ochre)}
html.js .offer > div .pm rect{transform:scaleX(0);transition:transform .7s var(--ease)}
html.js .offer > div .pm rect:nth-of-type(1){transition-delay:.15s}
html.js .offer > div .pm rect:nth-of-type(2){transition-delay:.3s}
html.js .offer > div .pm rect:nth-of-type(3){transition-delay:.45s}
html.js .offer > div .pm rect:nth-of-type(4){transition-delay:.6s}
html.js .offer > div.in .pm rect{transform:none}
html.js .offer > div .pm .draw{stroke-dashoffset:70}
html.js .offer > div.in .pm .draw{stroke-dashoffset:0}
html.js .close.in a.mail{background-size:100% 2px}
@media(prefers-reduced-motion:reduce){
  html.js h2 .w,html.js .rv,html.js .dv i,html.js .arc > div,html.js .offer > div .pm rect{opacity:1!important;transform:none!important;transition:none!important}
  html.js .rules div::after,html.js .how li::after,html.js .case::before{transform:scaleX(1)!important;transition:none!important}
  .pm.auto .ring,.pm.auto .core,.sys .st::before{animation:none}
  html.js .offer > div .pm .draw{stroke-dashoffset:0!important}
  .close a.mail{background-size:100% 2px}}

/* ── sections ── */
section{padding:clamp(54px,8vh,100px) 0}
.rule{height:1px;background:var(--sand)}
h2{font-size:clamp(1.65rem,3.3vw,2.6rem);max-width:17ch}
.intro-l{margin-top:16px;max-width:52ch;color:var(--ink-soft)}

.offer{margin-top:clamp(34px,5vh,54px);display:grid;
  grid-template-columns:repeat(auto-fit,minmax(248px,1fr));gap:clamp(26px,3.2vw,46px)}
.offer h3{font-size:clamp(1.14rem,1.55vw,1.36rem);max-width:19ch;
  font-variation-settings:"opsz" 40,"SOFT" 24,"WONK" 1}
.offer p{margin-top:9px;color:var(--ink-soft);font-size:15.5px}

/* ── cases: asymmetric, three beats ── */
.cases{margin-top:clamp(34px,5vh,54px);display:grid;gap:clamp(34px,5vh,58px)}
.case{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,2.1fr);
  gap:clamp(18px,3.4vw,50px);padding-top:clamp(26px,3.6vh,38px);border-top:1px solid var(--sand)}
.chd{align-self:start}
.case h3{font-size:clamp(1.3rem,2.1vw,1.85rem);max-width:17ch;
  font-variation-settings:"opsz" 60,"SOFT" 30,"WONK" 1}
.case .meta{margin-top:9px;font-size:14px;color:var(--ink-soft)}
.arc{display:grid;gap:18px}
.arc > div{display:grid;grid-template-columns:118px 1fr;gap:clamp(12px,1.6vw,26px);align-items:start}
.arc span{font-size:14px;color:var(--ink-soft);padding-top:3px}
.arc p{max-width:58ch}
.arc > div:nth-child(2) p{color:var(--ink)}
.arc > div:nth-child(1) p,.arc > div:nth-child(3) p{color:var(--ink-soft)}
.gap{color:var(--ochre)}
@media(max-width:820px){.case{grid-template-columns:1fr;gap:16px}
  .arc > div{grid-template-columns:1fr;gap:3px}}

/* ── how: a real sequence, so numbers earn their place ── */
.how{margin-top:clamp(34px,5vh,54px);list-style:none;counter-reset:s;
  display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:clamp(20px,2.4vw,34px)}
.how li{counter-increment:s;padding-top:16px;border-top:2px solid var(--ink)}
.how li::before{content:counter(s);font-family:Fraunces,serif;font-size:13px;
  color:var(--ink-soft);display:block;margin-bottom:10px;
  font-variation-settings:"opsz" 20,"SOFT" 0,"WONK" 0}
.how h3{font-size:clamp(1.04rem,1.35vw,1.2rem);
  font-variation-settings:"opsz" 30,"SOFT" 22,"WONK" 0}
.how p{margin-top:7px;font-size:14.5px;color:var(--ink-soft)}

/* ── close ── */
.close{background:var(--ink);color:var(--wall);margin-top:clamp(50px,7vh,90px)}
.close h2{color:var(--wall);max-width:15ch}
.close a.mail{display:inline-block;margin-top:clamp(22px,3vh,32px);
  font-family:Fraunces,serif;font-size:clamp(1.3rem,3.6vw,2.6rem);text-decoration:none;
  border-bottom:2px solid rgba(233,231,222,.3);padding-bottom:4px;
  font-variation-settings:"opsz" 80,"SOFT" 30,"WONK" 1;
  transition:border-color .3s var(--ease),color .3s var(--ease);word-break:break-word}
@media(hover:hover) and (pointer:fine){.close a.mail:hover{color:var(--ochre);border-color:var(--ochre)}}
.sig{margin-top:clamp(28px,4vh,44px);display:flex;gap:30px;flex-wrap:wrap;
  font-size:14px;color:rgba(233,231,222,.62)}

@media(prefers-reduced-motion:reduce){
  .week i.m{animation:none;background:transparent;box-shadow:inset 0 0 0 1px rgba(27,32,28,.09)}}

/* ══════════ v3.3: a site, not a document ══════════ */
:root{
 --spring:linear(0,.009,.035 2.1%,.141 4.4%,.723 12.9%,.938 16.7%,1.017,1.077,1.121,1.149 24.3%,1.159,1.163,1.161,1.154 29.9%,1.129 32.8%,1.051 39.6%,1.017 43.1%,.991,.977 51%,.974 53.8%,.975 57.1%,.997 69.8%,1.003 76.9%,1.004 83.8%,1);
 --soft:linear(0,.006,.025 2.8%,.101 6.1%,.539 18.9%,.721 25.3%,.849 31.5%,.937 38.1%,.968 41.8%,.991 45.7%,1.006 50.1%,1.015 55%,1.017 63.9%,1.001 85.9%,1);
}
html{scroll-behavior:smooth}
main{padding-top:58px}
section[id]{scroll-margin-top:64px}

/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;align-items:center;justify-content:space-between;gap:20px;
  padding:11px var(--pad);background:rgba(233,231,222,.82);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid transparent;transition:border-color .4s}
.nav.sc{border-bottom-color:var(--sand)}
.brand{font-family:Fraunces,serif;font-size:16px;text-decoration:none;font-variation-settings:"opsz" 24,"SOFT" 20,"WONK" 0}
.nav nav{position:relative;display:flex;gap:clamp(14px,2.2vw,30px)}
.nav nav a{font-size:14px;color:var(--ink-soft);text-decoration:none;padding:8px 0;transition:color .3s}
.nav nav a.on{color:var(--ink)}
@media(hover:hover){.nav nav a:hover{color:var(--ink)}}
.ind{position:absolute;bottom:2px;left:0;height:2px;width:20px;background:var(--ochre);border-radius:2px;opacity:0;
  transition:transform .8s var(--spring),width .8s var(--spring),opacity .3s}
@media(max-width:820px){.nav nav{display:none}}

/* buttons */
.btn{display:inline-flex;align-items:center;background:var(--ink);color:var(--wall);text-decoration:none;font-size:15px;
  padding:13px 22px;border-radius:999px;transition:transform .7s var(--spring),background-color .3s,color .3s,scale .25s var(--ease)}
.btn:active{scale:.95}
.btn.sm{padding:9px 16px;font-size:14px}
.btn.big{font-size:clamp(1rem,1.4vw,1.2rem);padding:18px 32px;background:var(--ochre);color:var(--ink)}
@media(hover:hover){.btn:hover{background:var(--door);color:var(--wall)}.btn.big:hover{background:var(--wall);color:var(--ink)}}
.btn:focus-visible,.acch:focus-visible,.sw button:focus-visible,.windex a:focus-visible,.tl:focus-visible{outline:2px solid var(--ochre);outline-offset:3px}
.cta{display:flex;align-items:center;gap:22px;margin-top:26px;flex-wrap:wrap;opacity:0;animation:rise .8s var(--ease) .85s forwards}
.tl{font-size:15px;text-decoration:none;border-bottom:1px solid var(--ink);padding-bottom:2px;transition:border-color .3s,color .3s}
@media(hover:hover){.tl:hover{color:var(--ochre);border-color:var(--ochre)}}

/* hero week: a control you operate */
.hero h1,.hero .mark{will-change:transform}
.wk-head{align-items:center}
.wk-head .count{margin:0;opacity:1;animation:none;align-items:baseline}
.wk-head .count b{font-size:clamp(2rem,3.4vw,2.9rem)}
.sw{position:relative;display:inline-grid;grid-template-columns:1fr 1fr;background:var(--wall-2);border-radius:999px;padding:3px}
.sw button{position:relative;z-index:1;border:0;background:none;font:inherit;font-size:14px;padding:7px 20px;color:var(--ink-soft);
  cursor:pointer;border-radius:999px;transition:color .3s}
.sw button[aria-pressed=true]{color:var(--wall)}
.sw .thumb{position:absolute;top:3px;bottom:3px;left:3px;width:calc(50% - 3px);background:var(--ink);border-radius:999px;
  transition:transform .75s var(--spring)}
.sw[data-s=after] .thumb{transform:translateX(100%)}
.week i{transition:transform .55s var(--spring)}
.week i.m{transition:background-color .45s var(--ease) calc(var(--k) * 7ms),box-shadow .45s var(--ease) calc(var(--k) * 7ms),transform .55s var(--spring)}
.week.after i.m{background:transparent;box-shadow:inset 0 0 0 1px rgba(27,32,28,.09)}

/* service cards: tilt toward the pointer */
.offer{gap:clamp(14px,1.6vw,22px)}
.card{height:100%;padding:clamp(22px,2.4vw,32px);border-radius:6px;
  background:radial-gradient(280px circle at var(--mx,50%) var(--my,0%),rgba(255,255,255,.6),transparent 70%),var(--wall-2);
  transform:perspective(900px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transition:transform .9s var(--spring),box-shadow .5s var(--ease)}
@media(hover:hover){.card:hover{box-shadow:0 22px 44px -26px rgba(27,32,28,.4)}}

/* bands */
.band.dark{background:var(--ink);color:var(--wall)}
.band.dark h2{color:var(--wall)}
.band.tint{background:var(--wall-2)}
.worklay{display:grid;grid-template-columns:minmax(0,.78fr) minmax(0,2fr);gap:clamp(24px,5vw,84px);margin-top:clamp(34px,5vh,54px)}
.windex{position:sticky;top:96px;align-self:start;list-style:none;display:grid;gap:2px}
.windex a{display:block;padding:13px 0 13px 16px;border-left:2px solid rgba(233,231,222,.16);color:rgba(233,231,222,.48);
  text-decoration:none;font-family:Fraunces,serif;font-size:clamp(1rem,1.2vw,1.1rem);line-height:1.25;letter-spacing:-.012em;
  transition:color .4s,border-color .4s,padding-left .7s var(--spring)}
.windex small{display:block;font-family:Archivo,sans-serif;font-size:12.5px;letter-spacing:0;margin-top:4px;opacity:.75}
.windex li.on a{color:var(--wall);border-color:var(--ochre);padding-left:26px}
@media(hover:hover){.windex a:hover{color:var(--wall)}}
.band.dark .cases{margin-top:0}
.band.dark .case{grid-template-columns:1fr;gap:20px;border-top-color:rgba(233,231,222,.16);scroll-margin-top:96px}
.band.dark .case h3{max-width:24ch}
.band.dark .case .meta,.band.dark .arc span{color:rgba(233,231,222,.55)}
.band.dark .arc > div:nth-child(2) p{color:var(--wall)}
.band.dark .arc > div:nth-child(1) p,.band.dark .arc > div:nth-child(3) p{color:rgba(233,231,222,.7)}
@media(max-width:900px){.worklay{grid-template-columns:1fr}.windex{display:none}}

/* accordions: systems and questions */
.accl{margin-top:clamp(30px,4.4vh,48px)}
.acc{border-top:1px solid var(--sand)} .acc:last-child{border-bottom:1px solid var(--sand)}
.acch{width:100%;display:grid;align-items:baseline;gap:6px clamp(16px,3vw,44px);text-align:left;background:none;border:0;
  font:inherit;color:inherit;cursor:pointer;padding:clamp(18px,2.5vh,26px) 0;transition:padding-left .7s var(--spring)}
@media(hover:hover){.acch:hover{padding-left:12px}}
.sysr h3{font:inherit;font-variation-settings:inherit;letter-spacing:inherit}
.sysr .acch{grid-template-columns:minmax(0,1fr) minmax(0,1.3fr) 16px}
.sysn,.q .acch span{font-family:Fraunces,serif;font-size:clamp(1.12rem,1.55vw,1.4rem);letter-spacing:-.018em;line-height:1.18;
  font-variation-settings:"opsz" 40,"SOFT" 24,"WONK" 1}
.q .acch{grid-template-columns:1fr 16px}
.prob{color:var(--ink-soft);font-size:15px}
.pm2{position:relative;width:16px;height:16px;align-self:center}
.pm2::before,.pm2::after{content:"";position:absolute;left:0;top:7px;width:16px;height:2px;background:var(--ochre);
  transition:transform .8s var(--spring)}
.pm2::after{transform:rotate(90deg)}
.acc.open .pm2::after{transform:rotate(0deg)} .acc.open .pm2::before{transform:rotate(180deg)}
.accb{display:grid;grid-template-rows:0fr;transition:grid-template-rows .6s var(--ease)}
.acc.open .accb{grid-template-rows:1fr}
.acci{overflow:hidden;min-height:0}
.acci > div{padding:0 0 clamp(20px,2.8vh,30px);max-width:64ch;opacity:0;transform:translateY(-10px);
  transition:opacity .45s var(--ease),transform .8s var(--spring)}
.acc.open .acci > div{opacity:1;transform:none;transition-delay:.12s}
.acci .st{margin-top:12px;font-size:14px;color:var(--door)}
.acci .st::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--door);margin-right:9px;
  vertical-align:1px;animation:beat 2.4s ease-in-out infinite}
.qa{display:block;max-width:860px;margin-top:0}
@media(max-width:820px){.sysr .acch{grid-template-columns:1fr 16px}.sysr .prob{grid-column:1;grid-row:2}}

/* capacity grid: light follows the pointer */
.team li{background:radial-gradient(220px circle at var(--mx,50%) var(--my,50%),rgba(43,76,111,.14),transparent 70%),var(--wall)}
html.js .team li.rv.done{transition:opacity .8s var(--ease),transform .7s var(--spring)}
@media(hover:hover){html.js .team li.rv.in:hover{transform:translateY(-5px)}}

/* flow and process: driven by scroll */
html.js .fline i{animation:none;opacity:0}
html.js .fstep{opacity:.4;transform:translateX(-8px);transition:opacity .5s var(--ease),transform .8s var(--spring)}
html.js .fstep span{animation:none;transition:background-color .4s}
html.js .fstep.on{opacity:1;transform:none} html.js .fstep.on span{background:var(--door)}
html.js .fnode.o{transition:background-color .5s,color .5s,transform .9s var(--spring)}
html.js .fnode.o:not(.on){background:transparent;color:var(--ink)}
html.js .fnode.o:not(.on) .ic{color:var(--ink)}
html.js .fnode.o.on{transform:scale(1.04)}
.track{height:2px;background:var(--sand);margin-top:clamp(34px,5vh,54px);position:relative}
.band.tint .track,.band.tint .acc{border-color:var(--sand)}
.track i{position:absolute;inset:0;background:var(--ochre);transform-origin:left;transform:scaleX(1)}
html.js .track i{transform:scaleX(0)}
.how{margin-top:0;grid-template-columns:repeat(5,minmax(0,1fr))}
.how li{border-top:0;padding-top:20px}
.how li::after{display:none}
html.js .how li{opacity:.34;transform:translateY(10px);transition:opacity .6s var(--ease),transform .9s var(--spring)}
html.js .how li.on{opacity:1;transform:none}
html.js .how li.on::before{color:var(--ochre)}
@media(max-width:820px){.how{grid-template-columns:1fr 1fr}}

/* reveals get a spring */
html.js h2 .w{transition:opacity .7s var(--ease),transform 1s var(--soft)}
html.js .rv{transition:opacity .8s var(--ease),transform 1.1s var(--soft)}
html.js .rv.done{transition-delay:0s}

/* close */
.close .btn.big{margin-top:clamp(24px,3.4vh,36px)}
.close a.mail{display:block;width:max-content;max-width:100%;margin-top:22px;font-family:Archivo,sans-serif;font-size:15px;
  color:rgba(233,231,222,.7);padding-bottom:3px}

@media(prefers-reduced-motion:reduce){
 html{scroll-behavior:auto}
 .cta{opacity:1;animation:none}
 .card,.btn,.sw .thumb,.week i,.week i.m,.windex a,.acch,.pm2::before,.pm2::after,.accb,.acci > div{transition:none!important}
 html.js .fstep,html.js .how li{opacity:1!important;transform:none!important;transition:none!important}
 html.js .track i{transform:scaleX(1)!important}
 html.js .fnode.o{background:var(--ink)!important;color:var(--wall)!important;transform:none!important}
 html.js .fnode.o .ic{color:var(--wall)!important}
}
</style></head><body>
<header class="nav" id="nav">
  <a class="brand" href="#top">Houssem Gabsi</a>
  <nav aria-label="Sections"><a href="#services">Services</a><a href="#work">Work</a><a href="#systems">Systems</a><a href="#process">Process</a><a href="#questions">Questions</a><i class="ind" id="ind"></i></nav>
  <a class="btn sm mag" href="mailto:unfollow.designs@gmail.com">Request a review</a>
</header>

<main id="top">
<div class="hero"><div class="wrap">
  ENSOHERE
  <div class="htop">
    <h1>HEADLINE</h1>
    <div>
      <p class="sub">INTROHERE</p>
      <div class="cta"><a class="btn mag" href="mailto:unfollow.designs@gmail.com">Request a free review</a><a class="tl" href="#work">See selected work</a></div>
    </div>
  </div>

  <div class="weekwrap">
    <div class="wk-head">
      <div class="sw" id="sw" data-s="before" role="group" aria-label="Show the week before or after"><button type="button" data-s="before" aria-pressed="true">Before</button><button type="button" data-s="after" aria-pressed="false">After</button><i class="thumb"></i></div>
      <p class="count"><b id="hrs">0</b><span>hours a week returned to the team</span></p>
    </div>
    <div class="grid">
      <div class="hrs">HOURSCOL</div>
      <div class="gcol">
        <div class="days">DAYSHERE</div>
        WEEKHERE
      </div>
    </div>
    <p class="wk-note">Illustrative week. Not a client's figures. Ochre is repeated manual work, blue is work that requires a person.</p>
  </div>
</div></div>

DIVHERE

<section id="services"><div class="wrap">
  <h2>Services</h2>
  <p class="intro-l">Most engagements combine all three.</p>
  <div class="offer">WHATHERE</div>
</div></section>

<section class="band dark" id="work"><div class="wrap">
  <h2>Selected work</h2>
  <div class="worklay">
    <ol class="windex">WINDEXHERE</ol>
    <div class="cases">CASESHERE</div>
  </div>
</div></section>

<section id="systems"><div class="wrap">
  <h2>Systems</h2>
  <p class="intro-l">Four systems, each built to solve a specific operational problem. Select one to see what it does.</p>
  <div class="accl">SYSHERE</div>
  <p class="sysnote">A free <a class="tl" href="/tools/stock-sales-production-tracker/">stock, sales and production tracker</a> for product businesses is also available.</p>
</div></section>

<section class="band tint" id="capacity"><div class="wrap">
  <h2>A small team with the capacity of a larger one</h2>
  <p class="intro-l">Each of these is a process that runs automatically. From the outside, the firm simply responds faster.</p>
  <ul class="team">AGENTSHERE</ul>
  <p class="teamnote">Individually these are small. Together they let a small team operate like a much larger one.</p>
</div></section>

<section id="enquiry"><div class="wrap">
  <h2>An enquiry, handled end to end</h2>
  <p class="intro-l">From form submission to a prepared reply, without manual steps. Scroll to follow it through.</p>
  FLOWHERE
</div></section>

DIVHERE

<section id="commitments"><div class="wrap">
  <h2>How I work</h2>
  <p class="intro-l">Six commitments that apply to every engagement.</p>
  <div class="rules">RULESHERE</div>
</div></section>

DIVHERE

<section id="process"><div class="wrap">
  <h2>Process</h2>
  <p class="intro-l">Five stages. The first is free, and the audit findings are yours whether or not you proceed to a build.</p>
  <div class="track" aria-hidden="true"><i id="trk"></i></div>
  <ol class="how">HOWHERE</ol>
</div></section>

DIVHERE

<section id="questions"><div class="wrap">
  <h2>Common questions</h2>
  <div class="accl qa">FAQHERE</div>
</div></section>

<section class="close"><div class="wrap">
  <h2>Find out where your firm is losing time.</h2>
  <p class="lead">A free one-page review of your follow-up, booking and administration. No call required.</p>
  <a class="btn big mag" href="mailto:unfollow.designs@gmail.com">Request a free review</a>
  <a class="mail" href="mailto:unfollow.designs@gmail.com">unfollow.designs@gmail.com</a>
  <div class="sig">
    <span>Houssem Gabsi</span>
    <span>A studio of one, for established firms</span>
    <span>English, français, العربية</span>
  </div>
</div></section>
</main>
<script>
(function(){
  var d=document, root=d.documentElement, RM=matchMedia('(prefers-reduced-motion: reduce)').matches,
      FINE=matchMedia('(hover:hover) and (pointer:fine)').matches;
  root.classList.add('js');
  function $(q,c){return (c||d).querySelector(q);} function $$(q,c){return [].slice.call((c||d).querySelectorAll(q));}
  function clamp(v){return v<0?0:v>1?1:v;}

  /* headings and reveals */
  $$('h2').forEach(function(h){h.innerHTML=h.textContent.trim().split(/\\s+/).map(function(w,i){return '<span class="w" style="--w:'+i+'">'+w+'</span>';}).join(' ');});
  ['.intro-l','.offer > div','.team li','.teamnote','.flow','.acc','.sysnote','.chd','.close .lead','.close .btn','.sig','.rules div','.windex li']
   .forEach(function(sel){$$(sel).forEach(function(n){n.classList.add('rv');n.style.setProperty('--i', sel==='.chd'?0:[].indexOf.call(n.parentNode.children,n));});});
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){var t=x.target;t.classList.add('in');io.unobserve(t);
      setTimeout(function(){t.classList.add('done');},1700);}});},{threshold:.15,rootMargin:'0px 0px -6% 0px'});
  $$('h2,.rv,.dv,.case,.close').forEach(function(n){io.observe(n);});

  /* the week: before and after, on a switch */
  var hrs=$('#hrs'), target=HOURSVAL, cur=0, raf=0, wk=$('#week'), sw=$('#sw'), state='before', auto=true;
  function count(to){cancelAnimationFrame(raf);var from=cur,t0=performance.now(),dur=1500;
    (function step(t){var k=clamp((t-t0)/dur);k=1-Math.pow(1-k,4);cur=from+(to-from)*k;hrs.textContent=Math.round(cur);
      if(k<1)raf=requestAnimationFrame(step);})(t0);}
  function setState(v){state=v;wk.classList.toggle('after',v==='after');sw.setAttribute('data-s',v);
    $$('button',sw).forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-s')===v));});
    if(RM){cur=v==='after'?target:0;hrs.textContent=cur;}else count(v==='after'?target:0);}
  sw.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;auto=false;setState(b.getAttribute('data-s'));});
  if(RM){setState('after');}
  else{setTimeout(function(){setState('after');},1500);
       setInterval(function(){if(auto&&!d.hidden)setState(state==='after'?'before':'after');},6500);}

  /* cells swell under the pointer */
  if(FINE&&!RM){var cells=$$('i',wk),pts=null;
    function measure(){var r=wk.getBoundingClientRect();pts=cells.map(function(c){var b=c.getBoundingClientRect();return [b.left-r.left+b.width/2,b.top-r.top+b.height/2,b.width/2];});}
    wk.addEventListener('pointerenter',measure);addEventListener('resize',function(){pts=null;});
    wk.addEventListener('pointermove',function(e){if(!pts)measure();var r=wk.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;
      cells.forEach(function(c,i){var dx=Math.max(0,Math.abs(pts[i][0]-x)-pts[i][2]),dy=pts[i][1]-y,di=Math.sqrt(dx*dx+dy*dy);
        c.style.transform=di<52?'scaleY('+(1+(1-di/52)*1.5).toFixed(2)+')':'';});});
    wk.addEventListener('pointerleave',function(){cells.forEach(function(c){c.style.transform='';});});}

  /* cards tilt, grid cells catch the light, buttons pull toward the pointer */
  if(FINE&&!RM){
    $$('.card').forEach(function(c){
      c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),px=(e.clientX-r.left)/r.width-.5,py=(e.clientY-r.top)/r.height-.5;
        c.style.setProperty('--rx',(-py*6).toFixed(2)+'deg');c.style.setProperty('--ry',(px*7).toFixed(2)+'deg');
        c.style.setProperty('--mx',((px+.5)*100).toFixed(1)+'%');c.style.setProperty('--my',((py+.5)*100).toFixed(1)+'%');});
      c.addEventListener('pointerleave',function(){c.style.setProperty('--rx','0deg');c.style.setProperty('--ry','0deg');});});
    $$('.team li').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();
        c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px');});});
    $$('.mag').forEach(function(b){
      b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();
        b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.24).toFixed(1)+'px,'+((e.clientY-r.top-r.height/2)*.34).toFixed(1)+'px)';});
      b.addEventListener('pointerleave',function(){b.style.transform='';});});}

  /* accordions */
  $$('.acch').forEach(function(b){b.addEventListener('click',function(){var a=b.closest('.acc'),o=a.classList.toggle('open');b.setAttribute('aria-expanded',String(o));});});

  /* one smoothed scroll loop drives everything that follows the page */
  var sy=scrollY, nav=$('#nav'), h1=$('.hero h1'), mk=$('.hero .mark'),
      flow=$('.flow'), fl=$$('.fline i'), fs=$$('.fstep'), fo=$('.fnode.o'), trk=$('#trk'), howl=$('.how'), how=$$('.how li'),
      links=$$('.nav nav a'), ind=$('#ind'), secs=links.map(function(a){return $(a.getAttribute('href'));}),
      wi=$$('.windex li'), cs=$$('.case'), pf=0, pt=0, act=-2, wact=-2;
  function frame(){
    var vh=innerHeight; sy+=(scrollY-sy)*(RM?1:.12);
    nav.classList.toggle('sc',scrollY>12);
    if(!RM&&sy<vh*1.2){h1.style.transform='translateY('+(sy*-.07).toFixed(1)+'px)';mk.style.transform='translateY('+(sy*.12).toFixed(1)+'px)';}
    var a=-1;secs.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<vh*.42)a=i;});
    if(a!==act){act=a;links.forEach(function(l,i){l.classList.toggle('on',i===a);});
      if(a<0){ind.style.opacity=0;}else{ind.style.opacity=1;ind.style.width=links[a].offsetWidth+'px';ind.style.transform='translateX('+links[a].offsetLeft+'px)';}}
    var w=0;cs.forEach(function(c,i){if(c.getBoundingClientRect().top<vh*.5)w=i;});
    if(w!==wact){wact=w;wi.forEach(function(l,i){l.classList.toggle('on',i===w);});}
    var r=flow.getBoundingClientRect(), t=clamp((vh*.82-r.top)/(vh*.5)); pf+=(t-pf)*(RM?1:.09);
    var a1=clamp(pf/.24), a2=clamp((pf-.74)/.24);
    fl[0].style.left=(a1*100)+'%';fl[0].style.opacity=(a1>.02&&a1<.98)?1:0;
    fl[1].style.left=(a2*100)+'%';fl[1].style.opacity=(a2>.02&&a2<.98)?1:0;
    fs.forEach(function(s,i){s.classList.toggle('on',pf>.26+i*.12);});
    fo.classList.toggle('on',pf>.97);
    var r2=howl.getBoundingClientRect(), t2=clamp((vh*.86-r2.top)/(vh*.46)); pt+=(t2-pt)*(RM?1:.09);
    trk.style.transform='scaleX('+pt.toFixed(4)+')';
    how.forEach(function(l,i){l.classList.toggle('on',pt>(i+.12)/how.length);});
    requestAnimationFrame(frame);}
  requestAnimationFrame(frame);
})();
</script>
</body></html>"""

what = "\n".join('<div><div class="card">%s<span class="pl">%s</span><h3>%s</h3><p>%s</p></div></div>' % (mark(m), e(k), e(a), e(b)) for m,k,a,b in WHAT)
cases = "\n".join(
 """<article class="case" id="case-%d">
  <div class="chd"><h3>%s</h3><p class="meta">%s</p></div>
  <div class="arc">
    <div><span>Challenge</span>%s</div>
    <div><span>Work delivered</span>%s</div>
    <div><span>Status</span>%s</div>
  </div>
 </article>""" % (i, e(c["who"]), e(c["kind"]), P(c["before"]), P(c["did"]), P(c["now"]))
 for i,c in enumerate(CASES))
windex = "\n".join('<li><a href="#case-%d">%s<small>%s</small></a></li>' % (i, e(c["who"]), e(c["kind"])) for i,c in enumerate(CASES))
systems = "\n".join(
 '<div class="acc sysr%s"><h3><button type="button" class="acch" aria-expanded="%s"><span class="sysn">%s</span><span class="prob">%s</span><i class="pm2"></i></button></h3>'
 '<div class="accb"><div class="acci"><div><p>%s</p><p class="st">%s</p></div></div></div></div>'
 % (" open" if i==0 else "", "true" if i==0 else "false", e(a), e(b), e(c), e(dd)) for i,(a,b,c,dd) in enumerate(SYSTEMS))
faq = "\n".join(
 '<div class="acc q%s"><h3><button type="button" class="acch" aria-expanded="%s"><span>%s</span><i class="pm2"></i></button></h3>'
 '<div class="accb"><div class="acci"><div><p>%s</p></div></div></div></div>'
 % (" open" if i==0 else "", "true" if i==0 else "false", e(q), e(a)) for i,(q,a) in enumerate(FAQ))

HEAD_HTML = " ".join('<span style="--w:%d">%s</span>' % (i, e(w)) for i,w in enumerate(HEAD.split()))
HTML = (HTML.replace("HEADLINE", HEAD_HTML).replace("INTROHERE", e(INTRO)).replace("WEEKHERE", WEEK)
            .replace("DAYSHERE", DAYLBL).replace("HOURSCOL", HOURS_COL).replace("WHATHERE", what)
            .replace("CASESHERE", cases).replace("WINDEXHERE", windex).replace("HOWHERE", how)
            .replace("AGENTSHERE", agents).replace("FLOWHERE", flow).replace("RULESHERE", rules).replace("SYSHERE", systems).replace("FAQHERE", faq).replace("ENSOHERE", HEROMARK).replace("LDHERE", LD).replace("OGTITLEHERE", e(OG_TITLE)).replace("OGDESCHERE", e(OG_DESC)).replace("OGALTHERE", e(OG_ALT)).replace("TITLEHERE", e(TITLE)).replace("DESCHERE", e(DESC)).replace("SITEHERE", SITE).replace("HOURSVAL", str(HOURS)))
while "DIVHERE" in HTML: HTML = HTML.replace("DIVHERE", divider(), 1)
open("../index.html","w").write(HTML)
open("../llms.txt","w").write(LLMS)
print("ok", len(HTML))
