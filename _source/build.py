# -*- coding: utf-8 -*-
import html, random
from cases import (HEAD_TEXT, INTRO, HERO_BTN, HERO_LINK, PANEL2_HEAD, PANEL2_TEXT, COUNTER_TEXT, WEEK_NOTE, STATEMENT, STATEMENT_LINK,
    WORK_LABEL, WORK_HEAD, CASES, SERVICES_LABEL, SERVICES_HEAD, WHAT, EXAMPLES, SYSTEMS_LABEL, SYSTEMS_HEAD, SYSTEMS, SYSTEMS_NOTE, SYSTEMS_NOTE_LINK,
    CAPACITY_LABEL, CAPACITY_HEAD, CAPACITY_INTRO, ENQUIRY_LABEL, ENQUIRY_HEAD, ENQUIRY_INTRO, COMMIT_LABEL, COMMIT_HEAD, RULES,
    PROCESS_LABEL, PROCESS_HEAD, PROCESS_INTRO, HOW, FAQ_LABEL, FAQ_HEAD, FAQ, CLOSE_HEAD, CLOSE_TEXT, CLOSE_BTN, CLOSE_NOTE,
    FOOT_DESC, PAGE_TITLE, PAGE_DESC, CTA_NOTE, CTA_CONNECT, PRODUCTS, PRODUCTS_LABEL, ANY_NOTE)
WORK = CASES + PRODUCTS   # four client cases, then the studio's own products
import re, json
from urllib.parse import quote
from parts import AGENTS, FLOW_TRIGGER, FLOW_STEPS, FLOW_END, NUMBERS, DAY_HOURS, CONNECT_INTRO, CONNECTS, CONNECT_NOTE, CONNECT_LABEL, CONNECT_HEAD
from icons import svg
from pages import PAGES
DISC_LINKS = {"Websites and online shops":"websites-and-online-shops","Automation":"ai-automation","Claude and AI setup":"claude-consulting","SEO and GEO":"seo-geo"}
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

AG_IC = ["moon_mail","invoice","cv_read","calendar_tick","pen","speech","bars","folder_in"]
agents = "\n".join(
 '<li style="--i:%d">%s<b>%s</b><span>%s</span></li>' % (i, svg(AG_IC[i]), e(a), e(b))
 for i,(a,b) in enumerate(AGENTS))

connects = "\n".join(
 '<li style="--i:%d">%s<b>%s</b><span>%s</span></li>' % (i, svg(ic), e(a), e(b))
 for i,(ic,a,b) in enumerate(CONNECTS))

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
EMAIL = ""   # contact address shown on the site. Left empty for now at Houssem's request. Set it and the review buttons become email links again.
HEAD = HEAD_TEXT
HEAD_ACCENT = 3   # how many closing words of the headline take the accent colour
TITLE = PAGE_TITLE
OG_TITLE = HEAD_TEXT
DESC = PAGE_DESC
OG_DESC = PAGE_DESC
OG_ALT = HEAD_TEXT
ABOUT = FOOT_DESC
LANGS = ["English","French","Arabic"]
PLACE = None   # no location shown, at Houssem's request
LD = json.dumps({"@context":"https://schema.org","@graph":[
 {"@type":"WebSite","@id":SITE+"#website","url":SITE,"name":"Loose Ends","description":ABOUT,
  "inLanguage":"en","publisher":{"@id":SITE+"#studio"}},
 {"@type":"WebPage","@id":SITE+"#webpage","url":SITE,"name":TITLE,"description":DESC,"inLanguage":"en",
  "isPartOf":{"@id":SITE+"#website"},"about":{"@id":SITE+"#studio"},
  "primaryImageOfPage":{"@type":"ImageObject","url":SITE+"og.png","width":1200,"height":630}},
 {"@type":"ProfessionalService","@id":SITE+"#studio","name":"Loose Ends",
  "description":ABOUT,
  "founder":{"@id":SITE+"#person"},
  "url":SITE,
  "image":SITE+"og.png",
  **({"email":EMAIL} if EMAIL else {}),
  "areaServed":["United States","Europe"],
  "availableLanguage":LANGS,
  "knowsAbout":["website design and build","booking systems","dashboards","process automation","invoice and quote follow-up","candidate scoring for recruiting firms","integrations with email, Slack, Loxo and BrightHire","newsletter automation","Shopify and Etsy shops","Substack newsletters","setting up Claude and other AI assistants for teams","search engine optimisation","generative engine optimisation","content systems","social media content","video editing","motion graphics","answer engine optimisation","branding"],
  "hasOfferCatalog":{"@type":"OfferCatalog","name":"Services","itemListElement":[
    {"@type":"Offer","itemOffered":{"@type":"Service","name":t,"description":d,"provider":{"@id":SITE+"#studio"}}} for _,_,t,d in WHAT]}},
 {"@type":"Person","@id":SITE+"#person","name":"Houssem Gabsi","url":SITE,**({"email":EMAIL} if EMAIL else {}),
  "worksFor":{"@id":SITE+"#studio"},"knowsLanguage":LANGS},
 {"@type":"ItemList","@id":SITE+"#work","name":"Selected work","itemListElement":[
    {"@type":"ListItem","position":i+1,"item":{"@type":"CreativeWork","@id":SITE+"#case-%d" % i,"url":SITE+"#case-%d" % i,
      "name":c["who"],"description":c["did"],"creator":{"@id":SITE+"#person"},
      **({"sameAs":c["link"],"image":SITE+"media/"+c["img"]} if c.get("link") else {})}} for i,c in enumerate(WORK)]},
 {"@type":"FAQPage","@id":SITE+"#faq","isPartOf":{"@id":SITE+"#webpage"},"mainEntity":[
    {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
]}, ensure_ascii=False, indent=1)

# plain-text summary for AI assistants, written from the same lists as the page
def _llms():
    L = ["# Loose Ends", "", "> " + ABOUT, "",
         "Works with firms in the US and Europe, in English, French and Arabic." + ((" Contact: " + EMAIL) if EMAIL else ""), "",
         "Site: " + SITE, "", "## Services", ""]
    L += ["- %s: %s" % (t, d) for _,_,t,d in WHAT]
    L += ["", "## Cases", "", "Client work. Clients are not named."]
    for c in CASES[:4]:
        L += ["", "### " + c["who"], "", c["kind"], "", c["did"], "", "Status: " + c["now"]]
    L += ["", "## " + PRODUCTS_LABEL]
    for c in PRODUCTS:
        L += ["", "### " + c["who"], "", c["did"], "", "Status: " + c["now"], "", "Link: " + c["link"]]
    L += ["", "## Systems", ""]
    L += ["- %s: %s Status: %s" % (a, c, d) for a,b,c,d in SYSTEMS]
    L += ["", "## How an engagement starts", ""]
    L += ["%d. %s %s" % (i+1, a, b) for i,(a,b,_) in enumerate(HOW[:3])]
    L += ["", "## Contact", "",
          ("Email: " + EMAIL) if EMAIL else "Request a free review from the contact section of the site: " + SITE + "#contact", ""]
    L += ["## Pages", "", "- [Home](%s): the whole studio on one page." % SITE,
          "- [The home page as Markdown](%sindex.md)" % SITE]
    L += ["- [%s](%s%s/): %s" % (pg["title"], SITE, pg["slug"], pg["desc"]) for pg in PAGES]
    L += ["- [Stock, sales and production tracker](%stools/stock-sales-production-tracker/): a free tracker for product businesses." % SITE, ""]
    return "\n".join(L)
LLMS = _llms()

# the whole home page as clean Markdown, in page order, from the same lists
def _md():
    L = ["# " + HEAD, "", INTRO, "", STATEMENT, "", "## " + WORK_HEAD]
    for c in CASES:
        L += ["", "### " + c["who"], "", c["kind"], "", c["did"], "", c["now"]]
    L += ["", "## " + PRODUCTS_LABEL]
    for c in PRODUCTS:
        L += ["", "### " + c["who"], "", c["kind"], "", c["did"], "", c["now"], "", c["link"]]
    L += ["", "## " + SERVICES_HEAD]
    for m,k,t,dsc in WHAT:
        L += ["", "### %s: %s" % (k, t), "", dsc, ""] + ["- " + x for x in EXAMPLES[m]]
    L += ["", "## " + CONNECT_HEAD, "", CONNECT_INTRO, ""]
    L += ["- **%s.** %s" % (a, b) for _,a,b in CONNECTS]
    L += ["", CONNECT_NOTE, "", "## " + SYSTEMS_HEAD]
    for a,b,c,dd in SYSTEMS:
        L += ["", "### " + a, "", c, "", dd]
    L += ["", "## " + CAPACITY_HEAD, "", CAPACITY_INTRO, ""]
    L += ["- %s, %s." % (a, b) for a,b in AGENTS]
    L += ["", "## " + ENQUIRY_HEAD, "", ENQUIRY_INTRO, "", "1. " + FLOW_TRIGGER]
    L += ["%d. %s" % (i+2, x) for i,x in enumerate(FLOW_STEPS)]
    L += ["%d. %s" % (len(FLOW_STEPS)+2, FLOW_END), "", "## " + COMMIT_HEAD, ""]
    L += ["- **%s** %s" % (a, b) for a,b in RULES]
    L += ["", "## " + PROCESS_HEAD, "", PROCESS_INTRO, ""]
    L += ["%d. **%s** %s (%s)" % (i+1, a, b, t) for i,(a,b,t) in enumerate(HOW)]
    L += ["", "## " + FAQ_HEAD]
    for q,a in FAQ: L += ["", "### " + q, "", a]
    L += ["", "## " + CLOSE_HEAD, "", CLOSE_TEXT, "", CLOSE_NOTE, "",
          ("Email: " + EMAIL) if EMAIL else "Request it from the contact section of the site: " + SITE + "#contact",
          "", "## More pages", ""]
    L += ["- [%s](%s%s/)" % (pg["title"], SITE, pg["slug"]) for pg in PAGES]
    L += ["- [Stock, sales and production tracker](%stools/stock-sales-production-tracker/)" % SITE,
          "- [Short guide for AI assistants](%sllms.txt)" % SITE, ""]
    return "\n".join(L)
PAGE_MD = _md()
how  = "\n".join('<li><h3>%s</h3><p>%s</p><span class="tag">%s</span></li>' % (e(a), e(b), e(t)) for a,b,t in HOW)

HTML = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TITLEHERE</title>
<meta name="description" content="DESCHERE">
<meta name="author" content="Houssem Gabsi">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="theme-color" content="#E9E7DE">
<link rel="canonical" href="SITEHERE">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="/llms.txt" title="Plain-text summary of this site">
<link rel="alternate" type="text/markdown" href="/index.md">
<meta property="og:site_name" content="Loose Ends">
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
  background-image:url(/grain.png);background-size:96px 96px}
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
.hero h1{font-size:clamp(2.1rem,4.4vw,3.6rem);max-width:15ch;text-wrap:balance;
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
.btn.inv{background:var(--wall);color:var(--ink)}
.cta-note{margin-top:14px;font-size:13.5px;color:var(--ink-soft);opacity:0;animation:rise .8s var(--ease) 1s forwards}
.ctarow{margin-top:clamp(34px,5vh,54px);padding-top:clamp(22px,3vh,30px);border-top:1px solid var(--sand);display:flex;align-items:center;gap:14px 22px;flex-wrap:wrap}
.ctarow p{font-family:Fraunces,serif;font-size:clamp(1.12rem,1.55vw,1.4rem);letter-spacing:-.018em;line-height:1.2;max-width:34ch;margin-right:auto}
.ctarow span{font-size:13.5px;color:var(--ink-soft);flex-basis:100%}
.band.dark .ctarow{border-top-color:rgba(233,231,222,.16)} .band.dark .ctarow span{color:rgba(233,231,222,.55)}
.ex{list-style:none;margin-top:16px;padding-top:14px;border-top:1px solid var(--sand);display:grid;gap:6px;font-size:14.5px}
.ex li{padding-left:16px;position:relative} .ex li::before{content:"";position:absolute;left:0;top:.72em;width:7px;height:2px;background:var(--ochre)}
.next{list-style:none;counter-reset:n;margin-top:clamp(28px,4vh,40px);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,2.4vw,34px);max-width:860px}
.next li{counter-increment:n;border-top:1px solid rgba(233,231,222,.2);padding-top:14px;display:grid;gap:5px;align-content:start}
.next li::before{content:counter(n);font-family:Fraunces,serif;font-size:13px;color:var(--ochre)}
.next b{font-family:Fraunces,serif;font-weight:400;font-size:clamp(1.02rem,1.3vw,1.16rem);line-height:1.25}
.next span{font-size:14.5px;color:rgba(233,231,222,.7)}
@media(max-width:700px){.next{grid-template-columns:1fr}}
.demo{margin-top:20px;max-width:300px} .demo video{display:block;width:100%;height:auto;border-radius:6px;border:1px solid var(--sand);background:var(--wall-2)}
.demo figcaption{margin-top:8px;font-size:13.5px;color:var(--ink-soft)}
.day{margin-top:clamp(28px,4vh,44px)}
.dayhd{display:flex;justify-content:space-between;align-items:baseline;gap:8px 20px;flex-wrap:wrap}
.dayhd b{font-family:Fraunces,serif;font-weight:400;font-size:clamp(1.7rem,3vw,2.5rem);letter-spacing:-.02em;font-variant-numeric:tabular-nums;line-height:1}
.dayhd span{font-size:15px;color:var(--ink-soft)} .dayhd i{font-style:normal;color:var(--ink);font-variant-numeric:tabular-nums}
.dayline{position:relative;height:28px;margin-top:14px;border-top:1px solid var(--sand);border-bottom:1px solid var(--sand)}
.dayline .office{position:absolute;top:0;bottom:0;left:37.5%;width:37.5%;background:rgba(27,32,28,.07)}
.dayline .ev{position:absolute;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--ochre);transform:scale(0);transition:transform .5s var(--spring)}
.dayline .ev.on{transform:scale(1)}
.dayline .now{position:absolute;top:-5px;bottom:-5px;left:0;width:2px;margin-left:-1px;background:var(--door)}
.dayax{display:flex;justify-content:space-between;margin-top:6px;font-size:12.5px;color:var(--ink-soft);font-variant-numeric:tabular-nums}
.day + .team{margin-top:clamp(18px,2.6vh,26px)}
.team.live li::after{animation:none;transition:transform .5s var(--ease)}
.team.live li.hit::after{transform:scaleX(1)}
.team.live li .ic{transition:color .3s,transform .5s var(--spring)} .team.live li.hit .ic{color:var(--ochre);transform:scale(1.18)}
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
.shot{display:block;max-width:640px;text-decoration:none;color:var(--wall)}
.shot img{display:block;width:100%;height:auto;border-radius:6px;border:1px solid rgba(233,231,222,.16);transition:border-color .3s}
.shot span{display:inline-block;margin-top:12px;font-size:15px;border-bottom:1px solid rgba(233,231,222,.5);padding-bottom:2px;transition:border-color .3s,color .3s}
@media(hover:hover){.shot:hover img{border-color:var(--ochre)}.shot:hover span{color:var(--ochre);border-color:var(--ochre)}}
.shot:focus-visible{outline:2px solid var(--ochre);outline-offset:3px}
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

/* ── hero: full-height, type-led ── */
.hero{min-height:calc(100svh - 58px);display:flex;align-items:center;padding:clamp(40px,7vh,84px) 0 clamp(30px,5vh,56px)}
.hero .wrap{width:100%}
.eyebrow{display:flex;align-items:center;gap:14px;flex-wrap:wrap;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);
  margin-bottom:clamp(22px,4vh,44px);opacity:0;animation:rise .8s var(--ease) .1s forwards}
.eyebrow .mark{margin:0 4px 0 0}
.eyebrow span + span::before{content:"";display:inline-block;width:22px;height:1px;background:var(--sand);vertical-align:middle;margin-right:14px}
.hero h1{font-size:clamp(2.7rem,8.3vw,8.4rem);max-width:none;line-height:.96;letter-spacing:-.038em;text-wrap:balance}
.hero h1 .hl{color:var(--ochre)}
.hbot{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:clamp(22px,5vw,80px);align-items:end;margin-top:clamp(28px,5vh,56px)}
.hero .sub{max-width:50ch;font-size:clamp(17px,1.4vw,21px)}
.hact .cta{margin-top:0}
.btn.big2{font-size:clamp(15px,1.2vw,17px);padding:16px 28px}
.disc{list-style:none;display:flex;flex-wrap:wrap;gap:8px 0;margin-top:clamp(30px,6vh,64px);padding-top:18px;border-top:1px solid var(--sand);
  font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);opacity:0;animation:rise .8s var(--ease) 1.1s forwards}
.disc li + li::before{content:"";display:inline-block;width:4px;height:4px;border-radius:50%;background:var(--ochre);margin:0 16px;vertical-align:middle}
#week .weekwrap{margin-top:clamp(26px,4vh,40px)}
@media(max-width:560px){.eyebrow span + span{flex-basis:100%}.eyebrow span + span::before{display:none}}
@media(max-width:860px){.disc{display:grid;grid-template-columns:1fr 1fr;gap:10px 18px}.disc li + li::before{display:none}.hbot{grid-template-columns:1fr;align-items:start}.hero{min-height:0;padding-top:clamp(36px,6vh,56px)}}
@media(prefers-reduced-motion:reduce){.eyebrow,.disc{opacity:1;animation:none}}

/* ── editorial scale: numbered sections, larger headings, services as an index ── */
main{counter-reset:sec}
section:not(.close) > .wrap > h2{font-size:clamp(2rem,4.7vw,4.1rem);max-width:17ch;line-height:1;letter-spacing:-.032em}
section:not(.close) > .wrap > h2::before{counter-increment:sec;content:counter(sec,decimal-leading-zero);display:block;
  font-family:Archivo,sans-serif;font-size:13px;font-weight:500;letter-spacing:.14em;line-height:1;color:var(--ochre);margin-bottom:clamp(16px,2.4vh,24px)}
.intro-l{font-size:clamp(16.5px,1.25vw,19px);margin-top:clamp(16px,2.4vh,24px)}
section{padding:clamp(64px,11vh,140px) 0}
.offer{grid-template-columns:1fr;gap:0;border-bottom:1px solid var(--sand)}
.offer > div{border-top:1px solid var(--sand)}
.card{background:none;border-radius:0;transform:none;padding:clamp(28px,5vh,52px) 0;height:auto;display:grid;
  grid-template-columns:minmax(0,.42fr) minmax(0,1.15fr) minmax(0,1.35fr);grid-template-areas:"m t d" "l t e";grid-template-rows:auto 1fr;
  column-gap:clamp(20px,4vw,64px);align-items:start;transition:none}
.card .pm{grid-area:m;margin-bottom:10px}
.card .pl{grid-area:l;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin:0}
.offer .card h3{grid-area:t;font-size:clamp(1.7rem,3.3vw,2.9rem);max-width:14ch;line-height:1.02;letter-spacing:-.028em;transition:color .4s var(--ease)}
.offer .card p{grid-area:d;margin-top:4px;font-size:clamp(16px,1.2vw,18px);max-width:46ch}
.card .ex{grid-area:e;grid-template-columns:1fr 1fr;gap:8px 24px;margin-top:20px}
@media(hover:hover){.card:hover{box-shadow:none}.offer .card:hover h3{color:var(--door)}}
@media(max-width:860px){.card{grid-template-columns:1fr;grid-template-areas:"m" "l" "t" "d" "e";grid-template-rows:auto;row-gap:10px}.card .ex{grid-template-columns:1fr}}
/* ── statement: one large centred paragraph that lights up word by word ── */
.stmt{padding:clamp(90px,18vh,220px) 0}
.stp{font-family:Fraunces,Georgia,serif;font-weight:300;font-size:clamp(1.6rem,3.6vw,3.3rem);line-height:1.2;letter-spacing:-.022em;
  text-align:center;max-width:22em;margin:0 auto;text-wrap:balance;font-variation-settings:"opsz" 110,"SOFT" 30,"WONK" 0}
html.js .stp span{color:rgba(27,32,28,.2);transition:color .3s ease}
html.js .stp span.lit{color:var(--ink)}
@supports (animation-timeline:view()){
  .stmt{view-timeline-name:--stmt;view-timeline-axis:block}
  html.js .stp span{transition:none;animation:lit linear both;animation-timeline:--stmt;
    animation-range:cover calc(24% + var(--i) * .95%) cover calc(29% + var(--i) * .95%)}
  @keyframes lit{from{color:rgba(27,32,28,.2)}to{color:var(--ink)}}
  html.js .track i{animation:grow linear both;animation-timeline:view();animation-range:entry 100% cover 62%}
  @keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
}

/* ── services: an expanding row. The open card is wide and dark; the others show mark and title ── */
.offer{display:flex;gap:12px;border-bottom:0}
.offer > div{flex:1 1 0;min-width:0;border-top:0}
html.js .offer > div.rv{transition:flex-grow .4s ease,opacity .6s ease,transform .6s ease}
html.js .offer > div.act{flex-grow:3.1}
.card{display:flex;flex-direction:column;height:100%;min-height:clamp(400px,54vh,500px);padding:clamp(22px,2.4vw,34px);border-radius:16px;
  background:var(--wall-2);overflow:hidden;transition:background-color .3s ease,color .3s ease}
.card .pm{margin:0}
.card .pl{margin-top:auto;padding-top:24px}
.offer .card h3{font-size:clamp(1.15rem,1.5vw,1.42rem);max-width:none;line-height:1.1;letter-spacing:-.018em;margin-top:8px}
.offer .card p{font-size:clamp(15.5px,1.15vw,17px);max-width:52ch;margin-top:14px}
.card .ex{grid-template-columns:1fr 1fr;gap:8px 24px;margin-top:18px}
html.js .card{cursor:pointer}
html.js .offer > div:not(.act) .card p,html.js .offer > div:not(.act) .card .ex{display:none}
html.js .offer > div.act .card{background:var(--ink);color:var(--wall);cursor:default}
html.js .offer > div.act .card .pm{--door:var(--wall)}
html.js .offer > div.act .card h3{font-size:clamp(1.7rem,2.8vw,2.5rem);max-width:16ch;color:var(--wall)}
html.js .offer > div.act .card p{color:rgba(233,231,222,.78);animation:fadein .4s ease .12s both}
html.js .offer > div.act .card .ex{border-top-color:rgba(233,231,222,.18);animation:fadein .4s ease .2s both}
@keyframes fadein{from{opacity:0}to{opacity:1}}
.card:focus-visible{outline:2px solid var(--ochre);outline-offset:3px}
@media(hover:hover){.offer .card:hover h3{color:inherit}}
@media(max-width:860px){.offer{flex-direction:column}.offer > div,html.js .offer > div.act{flex:none}
  .card{min-height:0;display:block}.card .pl{padding-top:14px}.card .ex{grid-template-columns:1fr}}

/* ── process: one row per stage, the numeral growing from 1 to 5 ── */
.how{display:block;margin-top:0}
.how li{display:grid;grid-template-columns:minmax(0,.55fr) minmax(0,1fr) minmax(0,1.5fr);column-gap:clamp(16px,4vw,64px);align-items:baseline;
  padding:clamp(16px,2.8vh,28px) 0;border-top:1px solid var(--sand)}
.how li::before{font-family:Fraunces,Georgia,serif;font-weight:300;line-height:.9;letter-spacing:-.04em;color:var(--ink);
  font-size:calc(2rem + var(--n,0) * .95rem);font-variation-settings:"opsz" 144,"SOFT" 30,"WONK" 0;transition:color .3s ease;transition-delay:0s}
.how li:nth-child(2){--n:1}.how li:nth-child(3){--n:2}.how li:nth-child(4){--n:3}.how li:nth-child(5){--n:4}
.how h3{font-size:clamp(1.3rem,2.1vw,1.85rem);letter-spacing:-.02em;line-height:1.1}
.how p{margin-top:0;font-size:clamp(15.5px,1.15vw,17px);max-width:46ch}
html.js .how li{transition:opacity .4s ease,transform .4s ease}
@media(max-width:700px){.how li{grid-template-columns:minmax(52px,.34fr) minmax(0,1fr)}.how h3,.how p{grid-column:2}.how p{margin-top:6px}
  .how li::before{font-size:calc(1.7rem + var(--n,0) * .55rem);grid-row:1 / span 2}}

/* ── navigation: a rounded bar floating over the page ── */
.nav{top:10px;left:10px;right:10px;max-width:1300px;margin:0 auto;border-radius:999px;border:1px solid transparent;padding:7px 8px 7px 24px}
.nav.sc{border-color:var(--sand)}
main{padding-top:70px}
section[id]{scroll-margin-top:78px}
.pin .hero{top:66px;height:calc(100svh - 66px)}
@media(max-width:860px){.nav{top:6px;left:6px;right:6px;padding-left:18px}}

/* ── smoothness: cheaper painting and quicker reveals ── */
.nav{background:rgba(233,231,222,.95);backdrop-filter:none;-webkit-backdrop-filter:none}
.hero h1,.hero .mark{will-change:auto}
.week.pinning i.m{transition:none}
html.js h2 .w{transition:opacity .4s ease,transform .45s ease;transition-delay:calc(var(--w,0) * 24ms)}
html.js .rv{transition:opacity .4s ease,transform .45s ease;transition-delay:calc(var(--i,0) * 40ms)}
html.js .rv.done{transition-delay:0s}
html.js .offer > div.rv{transition:flex-grow .3s ease,opacity .4s ease,transform .45s ease}

/* ── calmer motion: the pinned hero is the one showpiece ── */
@media(max-width:860px){.pin{height:auto}}
@media(min-width:861px) and (max-height:640px){.pin{height:auto}}
.btn{transition:background-color .25s ease,color .25s ease,transform .2s ease}
.ind{transition:transform .35s ease,width .35s ease,opacity .25s ease}
.week i{transition:none}
.week i.m{transition:background-color .35s ease calc(var(--k) * 7ms),box-shadow .35s ease calc(var(--k) * 7ms)}
.week i.m.c{transition-delay:0s}
@media(hover:hover) and (pointer:fine){.week i.w:hover{transform:none}}
.team li::after{animation:none}
html.js .team li.rv.done{transition:opacity .4s ease,transform .3s ease}
@media(hover:hover){html.js .team li.rv.in:hover{transform:none}}
.team.live li::after{transition:transform .35s ease}
.team.live li .ic{transition:color .3s ease} .team.live li.hit .ic{transform:none}
.dayline .ev{transition:transform .3s ease}
.windex a{transition:color .3s ease,border-color .3s ease,padding-left .3s ease}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}
  .hero h1 span,.hero .sub,.cta,.cta-note,.eyebrow,.disc,html.js .rv,html.js h2 .w{opacity:1!important;transform:none!important}
  html.js .stp span{color:var(--ink)!important}
  html.js .track i{transform:scaleX(1)!important}
  .pin{height:auto!important}.pin .hero{position:static!important;height:auto!important}.pinspace{display:none!important}}
.acci > div:has(.demo){max-width:none;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,300px);column-gap:clamp(24px,6vw,96px);align-items:start}
.acci > div:has(.demo) > p{grid-column:1;max-width:60ch}
.acci > div:has(.demo) > .demo{grid-column:2;grid-row:1 / span 3;margin-top:0;justify-self:end}
@media(max-width:860px){.acci > div:has(.demo){display:block}.acci > div:has(.demo) > .demo{margin-top:20px}}
/* ── footer ── */
.ft{padding:clamp(40px,7vh,80px) 0 clamp(28px,5vh,48px);font-size:15px}
.ftg{display:grid;grid-template-columns:minmax(0,1.5fr) repeat(3,minmax(0,1fr));gap:clamp(24px,4vw,56px)}
.ft .brand{font-size:19px;color:var(--ink)}
.fta p{margin-top:12px;color:var(--ink-soft);max-width:38ch}
.ft nav,.ftc{display:grid;gap:9px;align-content:start}
.ft b{font-weight:500;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:4px}
.ft nav a,.ftc a,.askai a{color:var(--ink);text-decoration:none;justify-self:start;min-width:0;border-bottom:1px solid transparent;transition:color .25s ease,border-color .25s ease}
.ftc span{color:var(--ink-soft)}
@media(hover:hover){.ft nav a:hover,.ftc a:hover,.askai a:hover{color:var(--ochre);border-color:var(--ochre)}}
.askai{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px 26px;margin-top:clamp(28px,5vh,48px);padding-top:20px;border-top:1px solid var(--sand)}
.askai b{margin:0 8px 0 0}
@media(max-width:860px){.ftg{grid-template-columns:1fr 1fr}.fta{grid-column:1 / -1}}

/* ── step 2: pinned hero. The week grid sits beside the headline and clears as the visitor scrolls ── */
.pin{height:300svh}
.pin .hero{position:sticky;top:66px;min-height:0;height:calc(100svh - 66px);padding:clamp(18px,3.4vh,44px) 0 clamp(14px,2.6vh,30px);display:flex;align-items:center}
.hgrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.06fr);column-gap:clamp(28px,5vw,84px);align-items:center}
.hero h1{font-size:clamp(2.3rem,4.8vw,4.9rem);line-height:.98;letter-spacing:-.034em}
.hcopy .eyebrow{margin-bottom:clamp(16px,3vh,32px)}
@media(min-width:861px){.hcopy .eyebrow{font-size:12px;letter-spacing:.12em;gap:10px;flex-wrap:nowrap;white-space:nowrap}.hcopy .eyebrow span + span::before{width:14px;margin-right:10px}}
.hcopy .sub{margin-top:clamp(16px,3vh,30px);max-width:46ch;font-size:clamp(16px,1.25vw,19px)}
.hcopy .hact{margin-top:clamp(18px,3vh,30px)}
.hero .weekwrap{margin-top:0}
.hgrid .disc{grid-column:1 / -1;margin-top:clamp(16px,3.6vh,40px)}
.pinspace{display:none}
.week i.m.c{background:transparent;box-shadow:inset 0 0 0 1px rgba(27,32,28,.09);transition-delay:0s}
.pinhint{color:var(--ochre)}
@media(max-width:860px){
  .pin{height:auto} .pin .hero{position:static;height:auto;display:block;padding-top:clamp(30px,5vh,48px)}
  .hgrid{display:block}
  .hero .weekwrap{position:sticky;top:max(66px,calc(50svh - 205px));margin-top:30px;padding:10px 0 6px;background:var(--wall);z-index:2}
  .pinspace{display:block;height:130svh}
  .hgrid .disc{margin-top:0}}
@media(min-width:861px) and (max-height:640px){.pin{height:auto}.pin .hero{position:static;height:auto}.pinhint{display:none}}
@media(prefers-reduced-motion:reduce){.pin{height:auto}.pin .hero{position:static;height:auto}.hero .weekwrap{position:static}.pinspace{display:none}.pinhint{display:none}}

/* ── step 1: framed panels. Dark bands sit on the page with a margin and rounded corners ── */
.band.dark,.close{margin:10px;border-radius:22px;overflow:clip}
.close{margin-top:10px}
@media(max-width:860px){.band.dark,.close{margin:6px;border-radius:16px}.close{margin-top:6px}}
.disc a{color:inherit;text-decoration:none;transition:color .3s} @media(hover:hover){.disc a:hover{color:var(--ochre)}}
.foot{display:flex;flex-wrap:wrap;gap:10px 28px;margin-top:clamp(28px,4vh,44px);padding-top:20px;border-top:1px solid rgba(233,231,222,.16)}
.foot a{color:rgba(233,231,222,.8);text-decoration:none;font-size:15px;border-bottom:1px solid transparent;transition:color .3s,border-color .3s}
@media(hover:hover){.foot a:hover{color:var(--ochre);border-color:var(--ochre)}}

/* ══ v2 spec, steps 1 and 2: tokens and type scale. Later steps add below this line. ══ */
:root{
  --wrap:1200px;
  --gut:clamp(16px,4vw,56px);
  --inset:clamp(8px,1.2vw,16px);
  --r-panel:clamp(14px,1.4vw,21px);
  --r-card:16px;
  --sec:clamp(88px,12.2vw,180px);
  --sec-cta:clamp(100px,14.3vw,210px);
  --ease:cubic-bezier(.2,.7,.1,1);
  --ease-io:cubic-bezier(.65,0,.15,1);
  --h2gap:clamp(40px,5vw,72px);
  --t-h1:clamp(2.5rem,5.6vw,5.1rem);
  --t-h2:clamp(2.1rem,4.2vw,3.6rem);
  --t-h3l:clamp(1.5rem,2.4vw,2.3rem);
  --t-h3s:clamp(1.25rem,1.7vw,1.75rem);
  --t-stmt:clamp(1.75rem,3.3vw,2.85rem);
  --t-lede:clamp(1.02rem,1.2vw,1.12rem);
  --t-small:14.7px;
}
.wrap{width:min(var(--wrap),100% - 2 * var(--gut));max-width:none;margin:0 auto;padding:0}
body{font-size:16px;line-height:1.55}
section,.lp section{padding:var(--sec) 0}
.close{padding:var(--sec-cta) 0}
h1,h2,h3{font-weight:300;line-height:1.04;letter-spacing:-.02em}
.hero h1,.lph1{font-size:var(--t-h1);line-height:1.04;letter-spacing:-.02em;font-weight:300}
section:not(.close) > .wrap > h2,.close h2{font-size:var(--t-h2);line-height:1.04;letter-spacing:-.02em;font-weight:300}
section:not(.close) > .wrap > h2::before{font-family:Archivo,sans-serif;font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.14em;
  color:var(--ink-soft);margin-bottom:18px;line-height:1}
.case h3,.band.dark .case h3{font-size:var(--t-h3l);line-height:1.12;letter-spacing:-.02em;font-weight:300}
.how h3,.rules h3,.lpfaq h3,.offer .card h3{font-size:var(--t-h3s);line-height:1.12;letter-spacing:-.02em;font-weight:300}
.stp{font-weight:300;font-size:var(--t-stmt);line-height:1.22;max-width:1094px;letter-spacing:-.02em}
.intro-l,.lp section p.intro-l{font-size:var(--t-lede);line-height:1.55;color:var(--ink-soft)}
.wk-note,.teamnote,.sysnote,.cta-note,.case .meta,.arc span,.team span,.how p,.ctarow span,.windex small{font-size:var(--t-small);line-height:1.55}
.offer,.team,.accl,.worklay,.rules,.flow,.track,.day{margin-top:var(--h2gap)}
.intro-l + .offer,.intro-l + .team,.intro-l + .accl,.intro-l + .rules,.intro-l + .flow,.intro-l + .track,.intro-l + .day{margin-top:var(--h2gap)}
.day + .team{margin-top:clamp(18px,2.6vh,26px)}
.track + .how{margin-top:0}
/* the old side-by-side hero is unpinned until step 6 rebuilds it as a framed, pinned stage */
.pin{height:auto}.pin .hero{position:static;height:auto;display:block;padding:var(--sec) 0 clamp(40px,6vw,80px)}
.hgrid{display:block}.hero .weekwrap{position:static;margin-top:clamp(40px,5vw,72px);padding:0;background:none}
.pinspace,.pinhint{display:none}
.hgrid .disc{margin-top:clamp(28px,4vw,48px)}

/* ══ v2 step 5: framed panels and section rhythm ══ */
body{overflow-x:clip}
main{padding-top:0}
.lp main{padding-top:calc(var(--inset) + 16px + 62px + 24px)}
section.panel{background:var(--ink);color:var(--wall);margin:0 var(--inset);border-radius:var(--r-panel)}
section.panel > .wrap > h2{color:var(--wall)}
section.panel > .wrap > h2::before{color:rgba(233,231,222,.55)}
section.panel .intro-l{color:rgba(233,231,222,.7)}
.band.tint{background:var(--wall-2)}
.paper{background:#F3F1EA}
.close{background:var(--ink);margin:0;border-radius:0}
.ft{background:var(--ink);color:var(--wall);padding-top:0}
.ft .brand,.ft nav a,.ftc a,.askai a{color:var(--wall)}
.fta p,.ft b,.ftc span{color:rgba(233,231,222,.6)}
.askai{border-top-color:rgba(233,231,222,.16)}
/* selected work sits on the cream page until step 8 rebuilds it as alternating rows */
.worklay{display:block}.windex{display:none}
.shot{color:var(--ink)}.shot img{border-color:var(--sand)}.shot span{border-bottom-color:rgba(27,32,28,.5)}

/* ══ v4 wording: a small label above each heading, replacing the section numbers ══ */
section:not(.close) > .wrap > h2::before{content:none}
.lab{font-family:Archivo,sans-serif;font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.14em;line-height:1;color:var(--ink-soft);margin:0 0 18px}
section.panel .lab{color:rgba(233,231,222,.55)}
section:not(.close) > .wrap > h2{max-width:22ch;text-wrap:balance}
.stl{text-align:center;margin-top:clamp(28px,4vw,48px)}
.pill{display:inline-flex;align-items:center;height:38px;padding:0 18px;border-radius:999px;border:1px solid rgba(27,32,28,.22);font-size:14px;font-weight:500;color:var(--ink);text-decoration:none;
  transition:background-color .2s var(--ease),color .2s var(--ease)}
@media(hover:hover){.pill:hover{background:var(--ink);color:var(--wall)}}
.chd .meta{margin:0 0 12px;font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.14em;line-height:1.4}
.arc > div{grid-template-columns:1fr}
.arc .proof p{color:var(--ink-soft);font-size:var(--t-small)}
.how li{grid-template-columns:minmax(0,.55fr) minmax(0,1fr) minmax(0,1.5fr) 104px}
.how .tag{font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.14em;color:var(--ink-soft);text-align:right}
@media(max-width:700px){.how li{grid-template-columns:minmax(52px,.34fr) minmax(0,1fr)}.how .tag{grid-column:2;text-align:left;margin-top:8px}}
.anynote{margin-top:clamp(28px,3.4vw,44px);max-width:62ch;font-family:Fraunces,Georgia,serif;font-weight:300;font-size:var(--t-h3s);line-height:1.25;letter-spacing:-.015em;color:var(--wall)}
.sublab{margin:clamp(56px,7vw,96px) 0 22px}
.cnote{margin-top:16px;font-size:var(--t-small);color:rgba(233,231,222,.6)}
.hp1 h1{max-width:1080px}

/* ══ v2 step 3: navigation, a floating bar ══ */
.nav{top:calc(var(--inset) + 16px);left:50%;right:auto;transform:translateX(-50%);width:min(var(--wrap),100% - 2 * var(--gut));max-width:none;height:62px;margin:0;
  padding:0 12px 0 26px;border-radius:30px;background:rgba(233,231,222,.72);backdrop-filter:blur(16px) saturate(1.3);-webkit-backdrop-filter:blur(16px) saturate(1.3);
  border:1px solid rgba(27,32,28,.10)}
.nav.sc{border-color:rgba(27,32,28,.10)}
.nav nav a{font-size:14px}
section[id]{scroll-margin-top:calc(var(--inset) + 16px + 62px + 12px)}
@media(max-width:860px){.nav{top:calc(var(--inset) + 10px);left:50%;right:auto;padding-left:20px}}

/* ══ v2 step 4: buttons ══ */
.btn,.btn.big,.btn.big2,.btn.inv{height:50px;padding:0 26px;border-radius:999px;font-family:Archivo,sans-serif;font-size:15.7px;font-weight:500;
  background:var(--ochre);color:var(--ink);transition:background-color .2s var(--ease),color .2s var(--ease),transform .2s var(--ease)}
.btn.sm{height:38px;padding:0 18px;font-size:14px}
@media(hover:hover){.btn:hover{transform:translateY(-1px)}}
.tl{border-bottom:1px solid currentColor;padding-bottom:2px;transition:color .2s var(--ease)}

/* ══ v2 step 6: pinned hero ══ */
.hero-track{height:420vh;position:relative}
.hero-stage{position:sticky;top:0;height:100vh}
.hero-card{position:absolute;inset:var(--inset);border-radius:var(--r-panel);background:var(--ink);color:var(--wall);overflow:hidden}
.hweek{position:absolute;left:50%;top:55%;transform:translate(-50%,-50%);width:min(980px,100% - 2 * var(--gut));opacity:.25}
.hweek .grid{margin:0}
.hweek .week{gap:clamp(3px,.75vh,7px) clamp(3px,.5vw,7px)}
.hweek .week i{height:clamp(6px,1.35vh,13px);border-radius:2px;transition:none}
.hweek .week i.e{background:transparent;box-shadow:inset 0 0 0 1px rgba(233,231,222,.11)}
.hweek .week i.w{background:#3F6C9B}
.hweek .week i.m{background:var(--ochre);box-shadow:none;transition:background-color .35s var(--ease),box-shadow .35s var(--ease)}
.hweek .week i.m.c{background:transparent;box-shadow:inset 0 0 0 1px rgba(233,231,222,.11)}
.hweek .days span,.hweek .hrs span{color:rgba(233,231,222,.5);font-size:12px}
.hcount{position:absolute;top:calc(16px + 62px + 26px);right:var(--gut);display:flex;align-items:baseline;gap:10px;margin:0;opacity:0;
  color:rgba(233,231,222,.75);font-size:var(--t-small)}
.hcount b{font-family:Fraunces,serif;font-weight:300;font-size:clamp(1.8rem,3vw,2.6rem);line-height:1;color:var(--ochre);font-variant-numeric:tabular-nums}
.hp{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 var(--gut);opacity:0;will-change:opacity,transform}
.hp1{align-items:center;text-align:center;opacity:1}
.hp1 h1{color:var(--wall);font-size:var(--t-h1);font-weight:300;line-height:1.04;letter-spacing:-.02em;max-width:min(1080px,16ch);text-wrap:balance;
  font-variation-settings:"opsz" 144,"SOFT" 36,"WONK" 1}
.hp1 h1 .hl{color:var(--ochre)}
.hp1 .sub{margin-top:clamp(18px,2.4vw,30px);max-width:60ch;color:rgba(233,231,222,.78);font-size:var(--t-lede);line-height:1.55;opacity:1;animation:none}
.hbtns{display:flex;gap:22px;align-items:center;justify-content:center;flex-wrap:wrap;margin-top:clamp(22px,3vw,36px)}
.hero-card .tl{color:var(--wall)}
.hp2{inset:auto;left:52%;bottom:18%;width:min(430px,42%);display:block;padding:26px 28px;background:rgba(27,32,28,.9);border:1px solid rgba(233,231,222,.12);border-radius:var(--r-card)}
.hp-h{font-family:Fraunces,serif;font-weight:300;font-size:var(--t-h3l);line-height:1.12;letter-spacing:-.02em}
.hp-t{margin-top:10px;color:rgba(233,231,222,.75)}
.hp4{align-items:center;text-align:center}
.hfinal{display:flex;flex-direction:column;align-items:center;gap:8px;margin:0;max-width:900px}
.hfinal b{font-family:Fraunces,serif;font-weight:300;font-size:clamp(4.5rem,13vw,11rem);line-height:.9;letter-spacing:-.04em;color:var(--ochre);font-variant-numeric:tabular-nums}
.hfinal span{font-size:var(--t-lede);color:rgba(233,231,222,.8)}
.hp4 .sw{margin-top:28px;background:rgba(233,231,222,.1)}
.hp4 .sw button{color:rgba(233,231,222,.7)} .hp4 .sw button[aria-pressed=true]{color:var(--ink)} .hp4 .sw .thumb{background:var(--wall)}
.hnote{position:absolute;left:var(--gut);bottom:22px;margin:0;font-size:12px;color:rgba(233,231,222,.45)}
.hscroll{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:rgba(233,231,222,.6);
  transition:opacity .3s var(--ease)}
@media(max-width:860px){.hero-track{height:320vh}.hweek{top:56%}
  .hp2{left:var(--gut);right:var(--gut);width:auto;bottom:11%;padding:20px 22px}
  .hnote{left:0;right:0;text-align:center;bottom:14px}.hscroll{bottom:38px}
  .hcount{top:calc(10px + 62px + 20px)}}
@media(prefers-reduced-motion:reduce){
  .hero-track{height:auto!important}.hero-stage{position:static!important;height:auto!important}
  .hero-card{position:relative!important;inset:auto!important;margin:var(--inset);padding:calc(62px + 70px) 0 56px;display:flex;flex-direction:column}
  .hp{position:static!important;opacity:1!important;transform:none!important}
  .hp1{order:1}.hweek{order:2;position:static!important;transform:none!important;margin:48px auto 40px;opacity:1!important}.hp4{order:3}.hnote{order:4;position:static!important;text-align:center;margin-top:28px}
  .hp2,.hcount,.hscroll{display:none!important}}

/* ══ v2 step 9: services, an expanding row inside the dark panel ══ */
.offer{display:flex;gap:12px;height:clamp(380px,35vw,510px);margin-top:var(--h2gap);border:0}
.offer > .svc{flex:1 1 0;min-width:0;border-top:0}
html.js .offer > .svc.rv,.offer > .svc{transition:flex-grow .45s var(--ease-io),opacity .4s ease,transform .45s ease}
html.js .offer > .svc.act,.offer > .svc.act{flex-grow:2.62}
.offer .svc .card,html.js .offer > .svc.act .card{position:relative;display:block;height:100%;min-height:0;padding:0;border-radius:var(--r-card);
  background:rgba(233,231,222,.06);border:1px solid rgba(233,231,222,.12);color:var(--wall);overflow:hidden;cursor:pointer}
html.js .offer > .svc.act .card{background:rgba(233,231,222,.1);cursor:default}
.c-min{position:absolute;inset:0;padding:clamp(18px,2vw,28px);display:flex;flex-direction:column;justify-content:space-between;transition:opacity .25s var(--ease)}
.c-min .idx{font-size:11px;font-weight:500;letter-spacing:.14em;color:rgba(233,231,222,.55)}
.c-min .c-t{font-family:Fraunces,serif;font-weight:300;font-size:var(--t-h3s);line-height:1.12;letter-spacing:-.02em}
.c-max{position:absolute;left:0;top:0;bottom:0;width:calc((min(var(--wrap),100vw - 2 * var(--gut) - 2 * var(--inset)) - 24px) * .567);
  padding:clamp(22px,2.6vw,36px);display:flex;flex-direction:column;opacity:0;visibility:hidden;transition:opacity .2s var(--ease),visibility 0s .2s}
.svc.act .c-min{opacity:0}
.svc.act .c-max{opacity:1;visibility:visible;transition:opacity .35s var(--ease) .2s,visibility 0s}
.c-max .pm{margin:0;--door:var(--wall);flex:none}
.c-max .pl{margin-top:auto;padding-top:20px}
html.js .offer > .svc .card .c-max h3,.offer .svc .c-max h3{font-size:2.2rem;line-height:1.08;color:var(--wall);max-width:16ch;margin-top:8px}
html.js .offer > .svc .card .c-max p,.offer .svc .c-max p{display:block;margin-top:12px;max-width:54ch;font-size:16px;color:rgba(233,231,222,.78);animation:none}
html.js .offer > .svc .card .c-max .ex,.offer .svc .c-max .ex{display:grid;grid-template-columns:1fr 1fr;gap:7px 24px;margin-top:16px;padding-top:14px;
  border-top:1px solid rgba(233,231,222,.18);font-size:var(--t-small);animation:none}
html.js .offer > .svc .card .c-max .c-links,.offer .svc .c-max .c-links{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:16px;font-size:var(--t-small)}
.c-links a{color:var(--wall);text-decoration:none;border-bottom:1px solid rgba(233,231,222,.4);transition:color .2s var(--ease),border-color .2s var(--ease)}
@media(hover:hover){.c-links a:hover{color:var(--ochre);border-color:var(--ochre)}}
@media(max-width:860px){.offer{flex-direction:column;height:auto}.offer > .svc,html.js .offer > .svc.act{flex:none}
  .offer .svc .card,html.js .offer > .svc.act .card{height:auto;cursor:default}.c-min{display:none}
  .c-max{position:static;width:auto;opacity:1;visibility:visible}
  html.js .offer > .svc .card .c-max .ex,.offer .svc .c-max .ex{grid-template-columns:1fr}}

/* ══ v2 step 7: statement, words lit by scroll position ══ */
html.js .stp span{animation:none!important;color:rgba(27,32,28,.26);transition:color .4s var(--ease)}
html.js .stp span.lit{color:var(--ink)}

/* ══ v2 step 8: selected work as alternating rows with drawn panels ══ */
.cases{display:block}
.case,.band.dark .case{display:grid;grid-template-columns:minmax(0,.87fr) minmax(0,1fr);gap:clamp(32px,6vw,88px);align-items:center;border-top:0;padding:0;position:relative}
.case::before{display:none!important}
.case + .case{margin-top:clamp(72px,11vw,160px)}
.case:nth-of-type(even) .ctext{order:2}
.ctext .meta{margin:0 0 14px;font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.14em;line-height:1.4;color:var(--ink-soft)}
.ctext h3{max-width:17ch}
.ctext .did{margin-top:clamp(18px,2vw,26px);max-width:50ch;color:var(--ink)}
.ctext .proof{margin-top:16px;padding-top:14px;border-top:1px solid var(--sand);font-size:var(--t-small);color:var(--ink-soft);max-width:50ch}
.ctext .clink{margin-top:16px;font-size:var(--t-small)}
.cviz{aspect-ratio:595 / 476;border-radius:var(--r-card);background:linear-gradient(160deg,#E6E3D9,var(--wall-2) 60%);overflow:hidden;
  box-shadow:inset 0 0 0 1px rgba(27,32,28,.06),inset 0 1px 0 rgba(255,255,255,.55),0 44px 70px -48px rgba(27,32,28,.42)}
.cviz svg{display:block;width:100%;height:112%;margin-top:-6%;will-change:transform}
html.js .cviz .d{opacity:0;transform:translateY(12px);transform-box:fill-box}
html.js .case.in .cviz .d{opacity:1;transform:none;transition:opacity .6s var(--ease),transform .7s var(--ease);transition-delay:calc(var(--j,0) * 55ms + .3s)}
html.js .cviz .draw{stroke-dasharray:1;stroke-dashoffset:1}
html.js .case.in .cviz .draw{stroke-dashoffset:0;transition:stroke-dashoffset 1.4s var(--ease-io) .45s}
.anynote{margin-top:clamp(28px,3.4vw,44px);max-width:62ch;font-family:Fraunces,Georgia,serif;font-weight:300;font-size:var(--t-h3s);line-height:1.25;letter-spacing:-.015em;color:var(--wall)}
.sublab{margin:clamp(72px,11vw,160px) 0 clamp(32px,4vw,56px);padding-top:22px;border-top:1px solid var(--sand)}
@media(max-width:820px){.case,.band.dark .case{grid-template-columns:1fr;gap:28px}.case:nth-of-type(even) .ctext{order:0}}

/* ══ v2 step 10: process, growing numbers ══ */
.track{display:none}
.how li{grid-template-columns:180px minmax(0,1.15fr) minmax(0,1.3fr) 104px;column-gap:clamp(16px,3vw,48px);align-items:center;min-height:156px;padding:18px 0;border-top:1px solid var(--sand)}
.how li:last-child{border-bottom:1px solid var(--sand)}
.how li::before{font-size:2.6rem;line-height:1;color:var(--ink)}
.how li:nth-child(2)::before{font-size:3.4rem}.how li:nth-child(3)::before{font-size:4.4rem}.how li:nth-child(4)::before{font-size:5.4rem}.how li:nth-child(5)::before{font-size:6.4rem}
.how h3{font-size:1.75rem;color:var(--ink)}
.how p{font-size:var(--t-small);max-width:44ch}
html.js .how li{opacity:1;transform:none;transition:none}
html.js .how li::before,html.js .how h3,html.js .how p,html.js .how .tag{transition:color .4s var(--ease)}
html.js .how li:not(.on)::before,html.js .how li:not(.on) h3,html.js .how li:not(.on) p,html.js .how li:not(.on) .tag{color:rgba(27,32,28,.45)}
html.js .how li.on::before{color:var(--ink)}
@media(max-width:700px){.how li{grid-template-columns:64px minmax(0,1fr);min-height:0;padding:22px 0;align-items:start}
  .how li::before{grid-row:1 / span 3;font-size:2rem}.how li:nth-child(2)::before{font-size:2.3rem}.how li:nth-child(3)::before{font-size:2.6rem}.how li:nth-child(4)::before{font-size:2.9rem}.how li:nth-child(5)::before{font-size:3.2rem}
  .how h3{font-size:1.4rem}}

/* ══ v2 step 11: questions in two columns ══ */
.qgrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,600px);gap:clamp(32px,6vw,88px);align-items:start}
.qhead{position:sticky;top:120px}
.qhead h2{font-size:var(--t-h2);line-height:1.04;letter-spacing:-.02em;font-weight:300;max-width:12ch;text-wrap:balance}
.qgrid .accl{margin-top:0}
.q .acch{min-height:72px;padding:16px 0;align-items:center}
.q .acch span{font-family:Archivo,sans-serif;font-size:17.3px;font-weight:500;letter-spacing:0;line-height:1.35}
.accb{transition:grid-template-rows .45s var(--ease-io)}
.acch{transition:none}
@media(max-width:900px){.qgrid{grid-template-columns:1fr;gap:var(--h2gap)}.qhead{position:static}.qhead h2{max-width:22ch}}

/* ══ v2 step 12: footer with the studio name set very large behind it ══ */
.ft{position:relative;overflow:hidden;padding-bottom:clamp(110px,19vw,330px)}
.ft .wrap{position:relative;z-index:1}
.ftbig{position:absolute;left:0;right:0;bottom:-.2em;text-align:center;white-space:nowrap;font-family:Fraunces,Georgia,serif;font-weight:300;
  font-size:clamp(4.6rem,19.5vw,24rem);line-height:1;letter-spacing:-.035em;color:#292E2A;pointer-events:none;user-select:none;font-variation-settings:"opsz" 144,"SOFT" 30,"WONK" 0}

/* ══ v2 step 13: two reveals only. Blocks rise 28px; headings rise line by line ══ */
html.js .rv,html.js .team li.rv,html.js .team li.rv.done{opacity:0;transform:translateY(28px);transition:opacity .7s var(--ease),transform .7s var(--ease);transition-delay:calc(var(--i,0) * 90ms + 80ms)}
html.js .rv.in,html.js .team li.rv.in{opacity:1;transform:none}
html.js .rv.done,html.js .team li.rv.done{transition-delay:0s}
html.js .offer > .svc.rv{transition:flex-grow .45s var(--ease-io),opacity .7s var(--ease),transform .7s var(--ease)}
html.js h2 .w{display:inline-block;opacity:1;transform:none;transition:none}
html.js h2 .ln{display:block;overflow:hidden;padding:.08em 0 .16em;margin:-.08em 0 -.16em}
html.js h2 .li{display:block;transform:translateY(112%);transition:transform .8s var(--ease);transition-delay:calc(var(--l,0) * 110ms + 230ms)}
html.js h2.in .li{transform:none}
html.js .fstep{transition:opacity .5s var(--ease),transform .5s var(--ease)}
.st::before,.pm.auto .core,.mark i.o{animation:none!important}

/* depth: a soft light inside the dark panels, so they do not read as flat blocks */
.hero-card,section.panel,.close{background-image:radial-gradient(90% 70% at 78% -10%,rgba(43,76,111,.42),transparent 62%),radial-gradient(70% 60% at 0% 110%,rgba(180,116,58,.13),transparent 60%)}
.close{background-image:radial-gradient(90% 60% at 78% -10%,rgba(43,76,111,.42),transparent 62%)}
.ft{background-image:none}
.offer .svc .card,html.js .offer > .svc.act .card{box-shadow:inset 0 1px 0 rgba(233,231,222,.1),0 30px 50px -36px rgba(0,0,0,.6)}
.team li,.rules div{position:relative}

@media(prefers-reduced-motion:reduce){
  html.js .rv,html.js .team li.rv,html.js h2 .li,html.js .cviz .d{opacity:1!important;transform:none!important;transition:none!important}
  html.js .cviz .draw{stroke-dashoffset:0!important;transition:none!important}
  html.js .stp span{color:var(--ink)!important}
  html.js .how li::before,html.js .how h3{color:var(--ink)!important}html.js .how p,html.js .how .tag{color:var(--ink-soft)!important}
  .cviz svg{transform:none!important}}
</style></head><body>
<header class="nav" id="nav">
  <a class="brand" href="#top">Loose Ends</a>
  <nav aria-label="Sections"><a href="#services">Services</a><a href="#work">Work</a><a href="#systems">Systems</a><a href="#process">Process</a><a href="#questions">Questions</a><i class="ind" id="ind"></i></nav>
  <a class="btn sm mag" href="MAILTOHERE">Free review</a>
</header>

<main id="top">
<div class="hero-track" id="pin">
<div class="hero-stage">
<div class="hero-card">
  <div class="hweek" id="hweek">
    <div class="grid">
      <div class="hrs">HOURSCOL</div>
      <div class="gcol">
        <div class="days">DAYSHERE</div>
        WEEKHERE
      </div>
    </div>
  </div>
  <p class="hcount" id="hcount"><b id="hrs">0</b><span>COUNTERTXT</span></p>
  <div class="hp hp1" id="hp1">
    <h1>HEADLINE</h1>
    <p class="sub">INTROHERE</p>
    <div class="hbtns"><a class="btn" href="MAILTOHERE">HEROBTN</a><a class="tl" href="#work">HEROLINK</a></div>
  </div>
  <div class="hp hp2" id="hp2">
    <p class="hp-h">P2HEAD</p>
    <p class="hp-t">P2TEXT</p>
  </div>
  <div class="hp hp4" id="hp4">
    <p class="hfinal"><b>HOURSVAL</b><span>COUNTERTXT</span></p>
    <div class="sw" id="sw" data-s="before" role="group" aria-label="Show the week before or after"><button type="button" data-s="before" aria-pressed="true">Before</button><button type="button" data-s="after" aria-pressed="false">After</button><i class="thumb"></i></div>
  </div>
  <p class="hnote">WEEKNOTE</p>
  <span class="hscroll" id="hscroll" aria-hidden="true">Scroll</span>
</div>
</div>
</div>

<section class="stmt" id="statement"><div class="wrap"><p class="stp">STMTHERE</p><p class="stl"><a class="pill" href="#process">STMTLINK</a></p></div></section>

<section id="work"><div class="wrap">
  <p class="lab">WORKLABEL</p>
  <h2>WORKHEAD</h2>
  <div class="worklay">
    <ol class="windex">WINDEXHERE</ol>
    <div class="cases">CASESHERE</div>
  </div>
</div></section>

<section class="panel" id="services"><div class="wrap">
  <p class="lab">SERVLABEL</p>
  <h2>SERVHEAD</h2>
  <div class="offer">WHATHERE</div>
  <p class="anynote">ANYNOTE</p>
</div></section>

<section class="band tint" id="connections"><div class="wrap">
  <p class="lab">CONNLABEL</p>
  <h2>CONNHEAD</h2>
  <p class="intro-l">CONNINTRO</p>
  <ul class="team">CONNECTSHERE</ul>
  <p class="teamnote">CONNNOTE <a class="tl" href="/mcp-integrations/">How MCP integrations work</a></p>
  <div class="ctarow"><p>CTACONNECT</p><a class="btn" href="MAILTOHERE">Request a free review</a><span>CTANOTE</span></div>
</div></section>

<section id="systems"><div class="wrap">
  <p class="lab">SYSLABEL</p>
  <h2>SYSHEAD</h2>
  <div class="accl">SYSHERE</div>
  <p class="sysnote">SYSNOTE</p>
</div></section>

<section class="band tint" id="capacity"><div class="wrap">
  <p class="lab">CAPLABEL</p>
  <h2>CAPHEAD</h2>
  <p class="intro-l">CAPINTRO</p>
  <div class="day" id="day" aria-hidden="true">
    <div class="dayhd"><b id="clk">00:00</b><span><i id="dn">0</i> tasks handled, <i id="do">0</i> outside office hours</span></div>
    <div class="dayline"><i class="office"></i><i class="now" id="dnow"></i></div>
    <div class="dayax"><span>00</span><span>06</span><span>12</span><span>18</span><span>24</span></div>
  </div>
  <ul class="team live" id="crew">AGENTSHERE</ul>
  <p class="teamnote">A sample day. The shaded band is office hours.</p>
</div></section>

<section id="enquiry"><div class="wrap">
  <p class="lab">ENQLABEL</p>
  <h2>ENQHEAD</h2>
  <p class="intro-l">ENQINTRO</p>
  FLOWHERE
</div></section>


DIVHERE

<section class="band tint" id="commitments"><div class="wrap">
  <p class="lab">COMLABEL</p>
  <h2>COMHEAD</h2>
  <div class="rules">RULESHERE</div>
</div></section>

DIVHERE

<section class="paper" id="process"><div class="wrap">
  <p class="lab">PROLABEL</p>
  <h2>PROHEAD</h2>
  <p class="intro-l">PROINTRO</p>
  <div class="track" aria-hidden="true"><i id="trk"></i></div>
  <ol class="how">HOWHERE</ol>
</div></section>

DIVHERE

<section id="questions"><div class="wrap qgrid">
  <div class="qhead"><p class="lab">FAQLABEL</p>
  <h2>FAQHEAD</h2></div>
  <div class="accl qa">FAQHERE</div>
</div></section>

<section class="close" id="contact"><div class="wrap">
  <h2>CLOSEHEAD</h2>
  <p class="lead">CLOSETEXT</p>
  <a class="btn big mag" href="MAILTOHERE">CLOSEBTN</a>
  <p class="cnote">CLOSENOTE</p>
  MAILLINE
</div></section>
</main>
FOOTERHERE
<script>
(function(){
  var d=document, root=d.documentElement, RM=matchMedia('(prefers-reduced-motion: reduce)').matches,
      FINE=matchMedia('(hover:hover) and (pointer:fine)').matches;
  root.classList.add('js');
  function $(q,c){return (c||d).querySelector(q);} function $$(q,c){return [].slice.call((c||d).querySelectorAll(q));}
  function clamp(v){return v<0?0:v>1?1:v;}

  /* headings and reveals */
  /* each h2 is split into the lines it actually wraps to; every line rises from behind its own edge */
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;');}
  function splitH(h){var t=h.getAttribute('data-t')||h.textContent.trim();h.setAttribute('data-t',t);h.setAttribute('aria-label',t);
    h.innerHTML=t.split(/\\s+/).map(function(w){return '<span class="w">'+esc(w)+'</span>';}).join(' ');
    var lines=[],top=null;$$('.w',h).forEach(function(w){if(top===null||Math.abs(w.offsetTop-top)>6){lines.push([]);top=w.offsetTop;}lines[lines.length-1].push(w.textContent);});
    h.innerHTML=lines.map(function(l,i){return '<span class="ln"><span class="li" style="--l:'+i+'">'+esc(l.join(' '))+'</span></span>';}).join(' ');}
  var h2s=$$('h2'), splitW=innerWidth, splitT=0;
  function splitAll(){h2s.forEach(splitH);}
  splitAll();
  if(d.fonts&&d.fonts.ready)d.fonts.ready.then(splitAll);
  addEventListener('resize',function(){if(innerWidth===splitW)return;splitW=innerWidth;clearTimeout(splitT);splitT=setTimeout(splitAll,180);});
  ['.intro-l','.offer > div','.team li','.teamnote','.flow','.acc','.sysnote','.ctext > *','.cviz','.stl','.close .lead','.close .btn','.close .cnote','.rules div','.ftg > *']
   .forEach(function(sel){$$(sel).forEach(function(n){n.classList.add('rv');n.style.setProperty('--i', Math.min(6,[].indexOf.call(n.parentNode.children,n)));});});
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){var t=x.target;t.classList.add('in');io.unobserve(t);
      setTimeout(function(){t.classList.add('done');},1700);}});},{threshold:.15,rootMargin:'0px 0px -6% 0px'});
  $$('h2,.rv,.dv,.case,.close').forEach(function(n){io.observe(n);});

  /* pinned hero: one scroll progress p (0 to 1) drives four text panels, the week clearing and the counter */
  var busy=40, lastY=-1, lastH=0;
  var hrs=$('#hrs'), target=HOURSVAL, wk=$('#week'), sw=$('#sw'), pin=$('#pin'), man=$$('i.m',wk), maxK=Math.max(1,man.length-1),
      hw=$('#hweek'), hp1=$('#hp1'), hp2=$('#hp2'), hp4=$('#hp4'), hcount=$('#hcount'), hscr=$('#hscroll'), sp=0, lastCleared=-1, lastSw='';
  function panel(el,o,y){el.style.opacity=o.toFixed(3);el.style.transform='translateY('+y.toFixed(1)+'px)';el.style.pointerEvents=o>.6?'auto':'none';}
  function heroPaint(p){
    var o1=1-clamp((p-.14)/.10); panel(hp1,o1,-26*(1-o1));
    var i2=clamp((p-.26)/.08), x2=1-clamp((p-.44)/.12); panel(hp2,Math.min(i2,x2),26*(1-i2)-26*(1-x2));
    var o4=clamp((p-.88)/.10); panel(hp4,o4,26*(1-o4));
    hw.style.opacity=(.25+.75*clamp((p-.14)/.12)-.7*o4).toFixed(3);
    hcount.style.opacity=(clamp((p-.2)/.08)*(1-o4)).toFixed(3);
    hscr.style.opacity=p>.05?0:1;
    var cleared=0; for(var i=0;i<man.length;i++){var on=p>.44+.40*(i/maxK); if(on)cleared++; if(on!==man[i]._c){man[i]._c=on;man[i].classList.toggle('c',on);}}
    if(cleared!==lastCleared){lastCleared=cleared;hrs.textContent=Math.round(target*cleared/man.length);}
    var s=p<.64?'before':'after'; if(s!==lastSw){lastSw=s;sw.setAttribute('data-s',s);
      $$('button',sw).forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-s')===s));});}}
  function herostep(vh){var tot=pin.offsetHeight-vh; if(tot<60)return;
    var p=clamp((scrollY-pin.offsetTop)/tot);
    sp+=(p-sp)*.16; if(Math.abs(p-sp)<.0005)sp=p; else busy=30;
    heroPaint(sp);}
  sw.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
    if(RM){var a=b.getAttribute('data-s')==='after';man.forEach(function(c){c.classList.toggle('c',a);});sw.setAttribute('data-s',a?'after':'before');
      $$('button',sw).forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});hrs.textContent=a?target:0;return;}
    scrollTo({top:b.getAttribute('data-s')==='after'?pin.offsetTop+pin.offsetHeight-innerHeight:pin.offsetTop,behavior:'smooth'});});
  if(RM){man.forEach(function(c){c.classList.add('c');});hrs.textContent=target;sw.setAttribute('data-s','after');
    $$('button',sw).forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-s')==='after'));});}
  else heroPaint(0);

  /* services: one card is open and wide, the other two show only an index and a title */
  var offs=$$('.offer > .svc');
  function pick(el){offs.forEach(function(o){var on=o===el;o.classList.toggle('act',on);var c=$('.card',o);if(c)c.setAttribute('aria-expanded',String(on));});}
  offs.forEach(function(o){o.addEventListener('mouseenter',function(){if(FINE)pick(o);});o.addEventListener('click',function(){pick(o);});
    o.addEventListener('focusin',function(){pick(o);});});

  /* the statement lights up word by word; browsers with scroll-driven CSS do this without script */
  var SDA=!!(window.CSS&&CSS.supports&&CSS.supports('animation-timeline: view()')), stm=$('.stp'), stw=$$('.stp span'), litN=-1, vz=$$('.cviz svg');

  /* capacity: one illustrative day, each process acting at its own hours */
  var day=$('#day');
  if(day){var crew=$$('#crew li'),SCH=DAYHOURS,dl=$('.dayline',day),clk=$('#clk'),dn=$('#dn'),dout=$('#do'),dnow=$('#dnow'),evs=[],dvis=false,dt0=0,di=0,dc=0,dco=0,DUR=18000,dlast=0;
    SCH.forEach(function(hs,i){hs.forEach(function(h){var x=d.createElement('i');x.className='ev';x.style.left=(h/24*100)+'%';dl.appendChild(x);evs.push({h:h,i:i,x:x});});});
    evs.sort(function(a,b){return a.h-b.h;});
    function two(n){return (n<10?'0':'')+n;}
    function fire(v,quiet){v.x.classList.add('on');dc++;if(v.h<9||v.h>=18)dco++;dn.textContent=dc;dout.textContent=dco;
      if(!quiet&&crew[v.i]){var t=crew[v.i];t.classList.add('hit');setTimeout(function(){t.classList.remove('hit');},1100);}}
    if(RM){evs.forEach(function(v){fire(v,true);});clk.textContent='24:00';dnow.style.left='100%';}
    else{new IntersectionObserver(function(es){dvis=es[0].isIntersecting;},{threshold:.2}).observe(day);
      (function tick(now){var step=dlast?now-dlast:0;dlast=now;
        if(dvis&&!d.hidden){dt0+=Math.min(step,100);
          if(dt0>DUR+2600){dt0=0;di=0;dc=0;dco=0;dn.textContent=0;dout.textContent=0;evs.forEach(function(v){v.x.classList.remove('on');});}
          var h=Math.min(24,dt0/DUR*24);clk.textContent=h>=24?'24:00':two(Math.floor(h))+':'+two(Math.floor((h%1)*6)*10);dnow.style.left=(h/24*100)+'%';
          while(di<evs.length&&evs[di].h<=h){fire(evs[di++]);}}
        requestAnimationFrame(tick);})(0);}}

  /* accordions */
  $$('.acch').forEach(function(b){b.addEventListener('click',function(){var a=b.closest('.acc'),o=a.classList.toggle('open');b.setAttribute('aria-expanded',String(o));});});

  /* one smoothed scroll loop drives everything that follows the page */
  var sy=scrollY, nav=$('#nav'), h1=$('.hero h1'), mk=$('.hero .mark'),
      flow=$('.flow'), fl=$$('.fline i'), fs=$$('.fstep'), fo=$('.fnode.o'), trk=$('#trk'), howl=$('.how'), how=$$('.how li'),
      links=$$('.nav nav a'), ind=$('#ind'), secs=links.map(function(a){return $(a.getAttribute('href'));}),
      wi=$$('.windex li'), cs=$$('.case'), pf=0, pt=0, act=-2, wact=-2;
  function frame(){
    /* do nothing while the page is still: the work below only matters when the scroll position changes */
    if(scrollY!==lastY||innerHeight!==lastH){lastY=scrollY;lastH=innerHeight;busy=70;}
    if(busy<=0){requestAnimationFrame(frame);return;} busy--;
    var vh=innerHeight;
    nav.classList.toggle('sc',scrollY>12);
    if(!RM)herostep(vh);
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
    if(!SDA)trk.style.transform='scaleX('+pt.toFixed(4)+')';
    if(!RM&&stm){var pr=clamp((vh*.72-stm.getBoundingClientRect().top)/(vh*.5)),n=0;
      for(var k=0;k<stw.length;k++)if(pr>k/stw.length)n++;
      if(n!==litN){litN=n;stw.forEach(function(w,i){w.classList.toggle('lit',i<n);});}}
    how.forEach(function(l){var hr=l.getBoundingClientRect();l.classList.toggle('on',RM||hr.top+hr.height/2<vh*.6);});
    if(!RM)vz.forEach(function(s){var vr=s.parentNode.getBoundingClientRect();if(vr.bottom<-80||vr.top>vh+80)return;
      s.style.transform='translate3d(0,'+(((vr.top+vr.height/2)-vh/2)*-.045).toFixed(1)+'px,0)';});
    requestAnimationFrame(frame);}
  requestAnimationFrame(frame);
})();
</script>
</body></html>"""

# services: each card has a closed face (index and title) and an open face (mark, title, text, points, page links)
SVC_LINKS = {"build": ["websites-and-online-shops"], "automate": ["ai-automation", "claude-consulting", "mcp-integrations"], "create": ["seo-geo"]}
_pg = {pg["slug"]: pg for pg in PAGES}
what = "\n".join(
 '<div class="svc%s"><div class="card" tabindex="0" role="button" aria-expanded="%s">'
 '<div class="c-min" aria-hidden="true"><span class="idx">%02d</span><span class="c-t">%s</span></div>'
 '<div class="c-max">%s<span class="pl">%s</span><h3>%s</h3><p>%s</p><ul class="ex">%s</ul><p class="c-links">%s</p></div>'
 '</div></div>'
 % (" act" if i == 0 else "", "true" if i == 0 else "false", i + 1, e(a), mark(m), e(k), e(a), e(b),
    "".join("<li>%s</li>" % e(x) for x in EXAMPLES[m]),
    "".join('<a href="/%s/">%s</a>' % (s, e(_pg[s]["nav"])) for s in SVC_LINKS[m]))
 for i, (m, k, a, b) in enumerate(WHAT))
if EMAIL:
    MAILTO = "mailto:" + EMAIL + "?subject=" + quote("Free review request") + "&amp;body=" + quote("Business:\nWebsite:\nWhat takes the most time each week:\n")
    MAILLINE = '<a class="mail" href="mailto:%s">%s</a>' % (EMAIL, EMAIL)
else:
    MAILTO = "#contact"
    MAILLINE = '<p class="lead">Contact details will be added here shortly.</p>'

# footer: description, section links, service pages, contact, languages, the free tracker, and the "Ask AI" row
ASK_Q = ("Tell me about Loose Ends (houssem-gabsi.vercel.app), a studio run by Houssem Gabsi that builds websites, automation and "
         "content systems for established firms, and how it could help my business.")
ASK = [("ChatGPT", "https://chatgpt.com/?q="), ("Claude", "https://claude.ai/new?q="), ("Perplexity", "https://www.perplexity.ai/search?q=")]
def footer_html(home):
    sec = "".join('<a href="%s#%s">%s</a>' % (home, i, n) for i, n in
                  [("services","Services"),("work","Work"),("systems","Systems"),("process","Process"),("questions","Questions")])
    pgs = "".join('<a href="/%s/">%s</a>' % (pg["slug"], e(pg["nav"])) for pg in PAGES)
    contact = ('<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)) if EMAIL else '<a href="%s#contact">Request a free review</a>' % home
    ask = "".join('<a href="%s%s" target="_blank" rel="noopener">%s</a>' % (u, quote(ASK_Q), n) for n, u in ASK)
    return ('<footer class="ft"><div class="wrap"><div class="ftg">'
            '<div class="fta"><a class="brand" href="%s#top">Loose Ends</a><p>%s</p></div>'
            '<nav aria-label="Sections"><b>Sections</b>%s</nav>'
            '<nav aria-label="Services"><b>Services</b>%s</nav>'
            '<div class="ftc"><b>Contact</b>%s<span>English, français, العربية</span>'
            '<a href="/tools/stock-sales-production-tracker/">Free stock, sales and production tracker</a></div>'
            '</div><div class="askai"><b>Ask AI about this studio</b>%s</div></div><div class="ftbig" aria-hidden="true">Loose Ends</div></footer>') % (home or "", e(ABOUT), sec, pgs, contact, ask)
DEMOS = {}   # demo films removed from the Systems section at Houssem's request
def demo(name):
    if name not in DEMOS: return ""
    f, t, cap = DEMOS[name]
    return ('<figure class="demo"><video controls playsinline preload="none" poster="/media/%s.jpg" width="540" height="676">'
            '<source src="/media/%s.webm" type="video/webm"><source src="/media/%s-s.mp4" type="video/mp4"></video>'
            '</figure>') % (f, f, f)
# ── drawn panels for the work: bars and cells in door blue and ochre, one composition per piece. No photos. ──
def _r(j, x, y, w, h, fill="door", rx=3, extra=""):
    return '<rect class="d" style="--j:%d" x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s"%s/>' % (
        j, x, y, w, h, rx, ("var(--%s)" % fill) if fill != "none" else "none", extra)
_OUT = ' stroke="rgba(27,32,28,.2)" stroke-width="1.2"'
def viz_roles():      # open roles entered once, appearing in a second place
    o = []
    for i, w in enumerate([180, 150, 168, 124, 172]):
        y = 104 + i * 58
        o.append(_r(i, 70, y, 180, 24))
        o.append('<line class="d" style="--j:%d" x1="262" y1="%g" x2="333" y2="%g" stroke="var(--ochre)" stroke-width="1.6" stroke-dasharray="3 5"/>' % (i + 3, y + 12, y + 12))
        o.append(_r(i + 5, 345, y, w, 24, "door" if i != 1 else "ochre"))
    return "".join(o)
def viz_tiles():      # a tile pattern, quarter circles meeting at the corners
    o, s, x0, y0 = [], 80, 57.5, 78
    for r in range(4):
        for c in range(6):
            x, y = x0 + c * s, y0 + r * s
            k = (r % 2) * 2 + (c % 2)
            dpath = {0: "M%g,%g L%g,%g A%g,%g 0 0 0 %g,%g Z" % (x + s, y + s, x, y + s, s, s, x + s, y),
                     1: "M%g,%g L%g,%g A%g,%g 0 0 0 %g,%g Z" % (x, y + s, x, y, s, s, x + s, y + s),
                     2: "M%g,%g L%g,%g A%g,%g 0 0 0 %g,%g Z" % (x + s, y, x + s, y + s, s, s, x, y),
                     3: "M%g,%g L%g,%g A%g,%g 0 0 0 %g,%g Z" % (x, y, x + s, y, s, s, x, y + s)}[k]
            col = "ochre" if (r, c) in [(1, 2), (1, 3), (2, 2), (2, 3)] else "door"
            o.append('<rect x="%g" y="%g" width="%g" height="%g" fill="none"%s/>' % (x, y, s, s, _OUT))
            o.append('<path class="d" style="--j:%d" d="%s" fill="var(--%s)"/>' % (r + c, dpath, col))
    return "".join(o)
def viz_booking():    # one phone screen: a schedule, one class chosen, one button
    o = ['<rect x="187" y="40" width="221" height="396" rx="28" fill="var(--wall)"%s/>' % _OUT, _r(0, 211, 72, 96, 12), _r(1, 211, 92, 58, 7, "sand")]
    for i in range(4):
        y = 124 + i * 58
        sel = i == 1
        o.append('<rect class="d" style="--j:%d" x="207" y="%g" width="181" height="46" rx="8" fill="%s"%s/>' % (i + 2, y, "var(--door)" if sel else "none", "" if sel else _OUT))
        o.append(_r(i + 3, 219, y + 13, 44, 8, "wall" if sel else "door"))
        o.append(_r(i + 3, 219, y + 27, 74, 6, "sand"))
        o.append('<circle class="d" style="--j:%d" cx="366" cy="%g" r="7" fill="%s"%s/>' % (i + 4, y + 23, "var(--ochre)" if sel else "none", "" if sel else _OUT))
    o.append(_r(8, 207, 372, 181, 38, "ochre", 19))
    return "".join(o)
def viz_week():       # the same working week, repeated
    o = ['<line x1="62" y1="388" x2="533" y2="388" stroke="rgba(27,32,28,.2)" stroke-width="1.2"/>']
    for d in range(7):
        x = 70 + d * 66
        if d > 4:
            o.append('<rect x="%g" y="92" width="46" height="282" rx="3" fill="none"%s/>' % (x, _OUT)); continue
        o += [_r(d, x, 92, 46, 64), _r(d + 1, x, 164, 46, 34, "ochre"), _r(d + 2, x, 206, 46, 96), _r(d + 3, x, 310, 46, 64, "none", 3, _OUT)]
    return "".join(o)
def viz_rank():       # candidates ranked, each score with its reasoning beside it
    o = []
    for i, w in enumerate([330, 286, 250, 196, 150, 96]):
        y = 86 + i * 54
        o.append(_r(i, 70, y, w, 20, "door" if i else "ochre"))
        o.append(_r(i + 1, 70, y + 27, w * .62, 5, "sand"))
        o.append('<circle class="d" style="--j:%d" cx="505" cy="%g" r="13" fill="%s"%s/>' % (i + 2, y + 13, "var(--ochre)" if i == 0 else "none", "" if i == 0 else _OUT))
    return "".join(o)
def viz_zone():       # a price line, the entry zone and the stop level
    pts = [(70, 300), (112, 284), (150, 310), (196, 252), (238, 268), (282, 206), (324, 228), (368, 170), (412, 196), (458, 138), (525, 156)]
    return ('<line x1="70" y1="92" x2="70" y2="388" stroke="rgba(27,32,28,.2)" stroke-width="1.2"/><line x1="70" y1="388" x2="525" y2="388" stroke="rgba(27,32,28,.2)" stroke-width="1.2"/>'
            + _r(0, 70, 236, 455, 62, "ochre", 0, ' fill-opacity=".22"')
            + '<line class="d" style="--j:2" x1="70" y1="338" x2="525" y2="338" stroke="var(--ochre)" stroke-width="1.6" stroke-dasharray="4 6"/>'
            + '<polyline class="draw" pathLength="1" points="%s" fill="none" stroke="var(--door)" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>' % " ".join("%d,%d" % p for p in pts)
            + '<circle class="d" style="--j:12" cx="525" cy="156" r="7" fill="var(--door)"/>')
VIZ = [viz_roles, viz_tiles, viz_booking, viz_week, viz_rank, viz_zone]
def viz(i): return '<div class="cviz" aria-hidden="true"><svg viewBox="0 0 595 476">%s</svg></div>' % VIZ[i % len(VIZ)]()
def visit(c):
    if not c.get("link"): return ""
    return '<p class="clink"><a class="tl" href="%s" target="_blank" rel="noopener">Visit %s</a></p>' % (e(c["link"]), e(c["link"].split("//")[1].strip("/")))
cases = "\n".join(
 ('<p class="lab sublab">%s</p>\n' % e(PRODUCTS_LABEL) if i == len(CASES) else "") +
 """<article class="case" id="case-%d">
  <div class="ctext"><p class="meta">%s</p><h3>%s</h3><p class="did">%s</p><p class="proof">%s</p>%s</div>
  %s
 </article>""" % (i, e(c["kind"]), e(c["who"]), e(c["did"]), e(c["now"]), visit(c), viz(i))
 for i,c in enumerate(WORK))
windex = "\n".join('<li><a href="#case-%d">%s<small>%s</small></a></li>' % (i, e(c["who"]), e(c["kind"])) for i,c in enumerate(WORK))
systems = "\n".join(
 '<div class="acc sysr%s"><h3><button type="button" class="acch" aria-expanded="%s"><span class="sysn">%s</span><span class="prob">%s</span><i class="pm2"></i></button></h3>'
 '<div class="accb"><div class="acci"><div><p>%s</p><p class="st">%s</p>%s</div></div></div></div>'
 % (" open" if i==0 else "", "true" if i==0 else "false", e(a), e(b), e(c), e(dd), demo(a)) for i,(a,b,c,dd) in enumerate(SYSTEMS))
faq = "\n".join(
 '<div class="acc q%s"><h3><button type="button" class="acch" aria-expanded="%s"><span>%s</span><i class="pm2"></i></button></h3>'
 '<div class="accb"><div class="acci"><div><p>%s</p></div></div></div></div>'
 % (" open" if i==0 else "", "true" if i==0 else "false", e(q), e(a)) for i,(q,a) in enumerate(FAQ))

_hw = HEAD.split()
HEAD_HTML = " ".join('<span%s style="--w:%d">%s</span>' % (' class="hl"' if i >= len(_hw)-HEAD_ACCENT else "", i, e(w)) for i,w in enumerate(_hw))
HTML = (HTML.replace("HEADLINE", HEAD_HTML).replace("INTROHERE", e(INTRO)).replace("FOOTLINKS", "".join('<a href="/%s/">%s</a>' % (pg["slug"], e(pg["nav"])) for pg in PAGES)).replace("WEEKHERE", WEEK)
            .replace("COUNTERTXT", e(COUNTER_TEXT)).replace("HEROBTN", e(HERO_BTN)).replace("HEROLINK", e(HERO_LINK)).replace("P2HEAD", e(PANEL2_HEAD)).replace("P2TEXT", e(PANEL2_TEXT))
            .replace("WEEKNOTE", e(WEEK_NOTE)).replace("STMTLINK", e(STATEMENT_LINK)).replace("WORKLABEL", e(WORK_LABEL)).replace("WORKHEAD", e(WORK_HEAD))
            .replace("SERVLABEL", e(SERVICES_LABEL)).replace("SERVHEAD", e(SERVICES_HEAD)).replace("SYSLABEL", e(SYSTEMS_LABEL)).replace("SYSHEAD", e(SYSTEMS_HEAD))
            .replace("SYSNOTE", e(SYSTEMS_NOTE) % ('<a class="tl" href="/tools/stock-sales-production-tracker/">%s</a>' % e(SYSTEMS_NOTE_LINK)))
            .replace("CAPLABEL", e(CAPACITY_LABEL)).replace("CAPHEAD", e(CAPACITY_HEAD)).replace("CAPINTRO", e(CAPACITY_INTRO))
            .replace("ENQLABEL", e(ENQUIRY_LABEL)).replace("ENQHEAD", e(ENQUIRY_HEAD)).replace("ENQINTRO", e(ENQUIRY_INTRO))
            .replace("COMLABEL", e(COMMIT_LABEL)).replace("COMHEAD", e(COMMIT_HEAD)).replace("PROLABEL", e(PROCESS_LABEL)).replace("PROHEAD", e(PROCESS_HEAD)).replace("PROINTRO", e(PROCESS_INTRO))
            .replace("FAQLABEL", e(FAQ_LABEL)).replace("FAQHEAD", e(FAQ_HEAD)).replace("CLOSEHEAD", e(CLOSE_HEAD)).replace("CLOSETEXT", e(CLOSE_TEXT)).replace("CLOSEBTN", e(CLOSE_BTN)).replace("CLOSENOTE", e(CLOSE_NOTE))
            .replace("DAYSHERE", DAYLBL).replace("HOURSCOL", HOURS_COL).replace("WHATHERE", what)
            .replace("CASESHERE", cases).replace("WINDEXHERE", windex).replace("HOWHERE", how)
            .replace("AGENTSHERE", agents).replace("CONNECTSHERE", connects).replace("MAILTOHERE", MAILTO).replace("MAILLINE", MAILLINE).replace("FOOTERHERE", footer_html("")).replace("STMTHERE", " ".join('<span style="--i:%d">%s</span>' % (i, e(w)) for i, w in enumerate(STATEMENT.split()))).replace("CTANOTE", e(CTA_NOTE)).replace("CTACONNECT", e(CTA_CONNECT)).replace("DAYHOURS", json.dumps(DAY_HOURS)).replace("CONNINTRO", e(CONNECT_INTRO)).replace("CONNLABEL", e(CONNECT_LABEL)).replace("ANYNOTE", e(ANY_NOTE)).replace("CONNHEAD", e(CONNECT_HEAD)).replace("CONNNOTE", e(CONNECT_NOTE)).replace("FLOWHERE", flow).replace("RULESHERE", rules).replace("SYSHERE", systems).replace("FAQHERE", faq).replace("ENSOHERE", HEROMARK).replace("LDHERE", LD).replace("OGTITLEHERE", e(OG_TITLE)).replace("OGDESCHERE", e(OG_DESC)).replace("OGALTHERE", e(OG_ALT)).replace("TITLEHERE", e(TITLE)).replace("DESCHERE", e(DESC)).replace("SITEHERE", SITE).replace("HOURSVAL", str(HOURS)))
HTML = HTML.replace("DIVHERE", "")   # the animated cell dividers are removed in the v2 structure
open("../index.html","w").write(HTML)
open("../llms.txt","w").write(LLMS)
open("../index.md","w").write(PAGE_MD)

# ── search pages: one per service, sharing the home page's styles ──
import os, datetime
STYLE = HTML[HTML.index("<style>")+7:HTML.index("</style>")]
LP_CSS = """
.lphero{padding:clamp(48px,9vh,110px) 0 clamp(28px,5vh,56px)}
.crumb{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:clamp(20px,3.4vh,36px)}
.crumb a{color:inherit;text-decoration:none} .crumb i{font-style:normal;margin:0 10px;color:var(--sand)}
.lph1{font-size:clamp(2.2rem,5.6vw,5rem);line-height:.98;letter-spacing:-.034em;max-width:18ch;text-wrap:balance;
  font-variation-settings:"opsz" 144,"SOFT" 36,"WONK" 1}
.lplead{margin-top:clamp(22px,4vh,40px);max-width:58ch;font-size:clamp(18px,1.5vw,22px);line-height:1.5;color:var(--ink)}
.lphero .cta{opacity:1;animation:none;margin-top:clamp(24px,4vh,36px)} .lphero .cta-note{opacity:1;animation:none}
.lpshort{max-width:900px;grid-template-columns:1fr 1fr;gap:10px 32px;margin-top:clamp(28px,5vh,48px);font-size:16px}
.lp section{padding:clamp(44px,7vh,88px) 0}
.lp section p{max-width:64ch;margin-top:16px;font-size:clamp(16.5px,1.2vw,18.5px)}
.lp section p + p{margin-top:14px}
.lp .pts{list-style:none;max-width:70ch;margin-top:20px;display:grid;gap:12px;font-size:clamp(16px,1.15vw,18px)}
.lp .pts li{padding-left:22px;position:relative}
.lp .pts li::before{content:"";position:absolute;left:0;top:.72em;width:10px;height:2px;background:var(--ochre)}
.lpfaq{margin-top:clamp(24px,4vh,40px);display:grid;gap:0;max-width:860px;border-bottom:1px solid var(--sand)}
.lpfaq > div{border-top:1px solid var(--sand);padding:clamp(20px,3vh,28px) 0}
.lpfaq h3{font-size:clamp(1.14rem,1.6vw,1.42rem);letter-spacing:-.018em;line-height:1.2}
.lp .lpfaq p{margin-top:10px;color:var(--ink-soft)}
.rel{display:flex;flex-wrap:wrap;gap:12px 28px;margin-top:24px}
@media(max-width:700px){.lpshort{grid-template-columns:1fr}}
"""
def lp_block(x):
    if isinstance(x, (list, tuple)):
        return '<ul class="pts">%s</ul>' % "".join("<li>%s</li>" % e(i) for i in x)
    return "<p>%s</p>" % e(x)
BYSLUG = {pg["slug"]: pg for pg in PAGES}
NAVLINKS = "".join('<a href="/%s/">%s</a>' % (pg["slug"], e(pg["nav"])) for pg in PAGES)
for pg in PAGES:
    url = SITE + pg["slug"] + "/"
    ptitle = pg["title"] + " | Loose Ends"
    ld = json.dumps({"@context":"https://schema.org","@graph":[
      {"@type":"WebPage","@id":url+"#webpage","url":url,"name":ptitle,"description":pg["desc"],"inLanguage":"en",
       "isPartOf":{"@id":SITE+"#website"},"about":{"@id":url+"#service"},"breadcrumb":{"@id":url+"#breadcrumb"}},
      {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Loose Ends","item":SITE},
        {"@type":"ListItem","position":2,"name":pg["nav"],"item":url}]},
      {"@type":"Service","@id":url+"#service","name":pg["title"],"description":pg["desc"],"serviceType":pg["nav"],
       "provider":{"@type":"ProfessionalService","@id":SITE+"#studio","name":"Loose Ends","url":SITE},
       "areaServed":["United States","Europe"]},
      {"@type":"FAQPage","@id":url+"#faq","isPartOf":{"@id":url+"#webpage"},"mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pg["faq"]]},
    ]}, ensure_ascii=False, indent=1)
    body = "".join('<section><div class="wrap"><h2>%s</h2>%s</div></section>\n' % (e(h), "".join(lp_block(x) for x in blocks)) for h, blocks in pg["sections"])
    faqh = "".join("<div><h3>%s</h3><p>%s</p></div>" % (e(q), e(a)) for q,a in pg["faq"])
    rel = "".join('<a class="tl" href="/%s/">%s</a>' % (r, e(BYSLUG[r]["nav"])) for r in pg["related"])
    doc = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="author" content="Houssem Gabsi">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="theme-color" content="#E9E7DE">
<link rel="canonical" href="%(url)s">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:site_name" content="Loose Ends">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="%(url)s">
<meta property="og:type" content="website">
<meta property="og:title" content="%(ogtitle)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="%(site)sog.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
%(ld)s
</script>
<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>%(style)s%(lpcss)s</style></head><body class="lp">
<header class="nav sc" id="nav">
  <a class="brand" href="/">Loose Ends</a>
  <nav aria-label="Services">%(navlinks)s</nav>
  <a class="btn sm" href="%(mailto)s">Free review</a>
</header>
<main>
<div class="lphero"><div class="wrap">
  <p class="crumb"><a href="/">Loose Ends</a><i>/</i>%(nav)s</p>
  <h1 class="lph1">%(h1)s</h1>
  <p class="lplead">%(lead)s</p>
  <div class="cta"><a class="btn big2" href="%(mailto)s">Request a free review</a><a class="tl" href="/#work">See selected work</a></div>
  <p class="cta-note">%(ctanote)s</p>
  <ul class="ex lpshort">%(short)s</ul>
</div></div>
%(body)s<section><div class="wrap"><h2>Questions</h2><div class="lpfaq">%(faq)s</div></div></section>
<section><div class="wrap"><h2>Related services</h2><div class="rel">%(rel)s</div></div></section>
<section class="close" id="contact"><div class="wrap">
  <h2>Find out where your business is losing time.</h2>
  <p class="lead">A free one-page review of your follow-up, booking and administration. No call required.</p>
  <a class="btn big" href="%(mailto)s">Request a free review</a>
  %(mailline)s
</div></section>
</main>
%(footer)s
</body></html>""" % dict(title=e(ptitle), desc=e(pg["desc"]), url=url, ogtitle=e(pg["title"]), site=SITE, ld=ld, style=STYLE, lpcss=LP_CSS,
        navlinks=NAVLINKS, mailto=MAILTO, nav=e(pg["nav"]), h1=e(pg["h1"]), lead=e(pg["lead"]), ctanote=e(CTA_NOTE),
        short="".join("<li>%s</li>" % e(x) for x in pg["short"]), body=body, faq=faqh, rel=rel, mailline=MAILLINE, footer=footer_html("/"))
    os.makedirs("../" + pg["slug"], exist_ok=True)
    open("../%s/index.html" % pg["slug"], "w").write(doc)

TODAY = "2026-11-16"   # update when the pages change
SM = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
      '  <url><loc>%s</loc><lastmod>%s</lastmod></url>' % (SITE, TODAY)]
SM += ['  <url><loc>%s%s/</loc><lastmod>%s</lastmod></url>' % (SITE, pg["slug"], TODAY) for pg in PAGES]
SM += ['  <url><loc>%stools/stock-sales-production-tracker/</loc><lastmod>2026-10-26</lastmod></url>' % SITE, '</urlset>', '']
open("../sitemap.xml","w").write("\n".join(SM))
print("pages", len(PAGES))
print("ok", len(HTML))
