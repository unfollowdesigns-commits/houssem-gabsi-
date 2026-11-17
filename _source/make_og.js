// Share pictures (1200 x 630) for the home page and every blog post.
// Run after build.py, with the site served locally:  cd .. && python3 -m http.server 8765  then  node _source/make_og.js
// Writes ../og.png and ../blog/<slug>/og.png. Uses the Playwright that comes with the environment.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..'), BASE = 'http://localhost:8765';
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const page = (kicker, title, svg, foot) => `<!doctype html><meta charset="utf-8"><style>
@font-face{font-family:Fraunces;src:url(${BASE}/fonts/fraunces-latin.woff2) format("woff2");font-weight:300 700}
@font-face{font-family:Archivo;src:url(${BASE}/fonts/archivo-latin.woff2) format("woff2");font-weight:400 600}
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;overflow:hidden;background:#1B201C;color:#E9E7DE;font-family:Archivo,sans-serif;position:relative;
  --door:#2B4C6F;--ochre:#B4743A;--sand:#CFC9B8;--ink:#1B201C;--wall:#E9E7DE}
body::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 70% at 85% 0%,rgba(43,76,111,.55),transparent 65%),radial-gradient(50% 60% at 0% 110%,rgba(180,116,58,.18),transparent 60%)}
.l{position:absolute;left:72px;top:64px;bottom:60px;width:${svg ? 560 : 1000}px;display:flex;flex-direction:column}
.b{font-family:Fraunces,serif;font-size:28px;letter-spacing:-.01em}
.k{margin-top:auto;font-size:15px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:#C88A4E}
h1{margin-top:18px;font-family:Fraunces,serif;font-weight:300;font-size:${svg ? 54 : 74}px;line-height:1.06;letter-spacing:-.02em;text-wrap:balance}
.f{margin-top:30px;font-size:17px;color:rgba(233,231,222,.6)}
.r{position:absolute;right:64px;top:110px;width:470px;padding:14px;border-radius:22px;background:#DFDCD1;box-shadow:0 50px 90px -40px rgba(0,0,0,.7)}
.r .sviz{border-radius:12px;background:#EFEDE5;overflow:hidden}.r svg{display:block;width:100%;height:auto}
.r text{font-family:Archivo,sans-serif;font-size:9.5px}
</style><div class="l"><div class="b">Loose Ends</div><p class="k">${esc(kicker)}</p><h1>${esc(title)}</h1><p class="f">${esc(foot)}</p></div>${svg ? `<div class="r">${svg}</div>` : ''}`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.goto(BASE + '/blog/'); await p.waitForTimeout(500);
  const cards = await p.evaluate(() => [...document.querySelectorAll('.bcard')].map(c => ({ slug: c.getAttribute('href').split('/')[2], cat: c.querySelector('small').textContent,
    title: c.querySelector('h3').textContent, svg: c.querySelector('.sviz').outerHTML })));
  const shoot = async (html, out) => { await p.setContent(html, { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150); await p.screenshot({ path: out }); };
  for (const c of cards) await shoot(page(c.cat, c.title, c.svg, 'Loose Ends blog  ·  houssem-gabsi.vercel.app'), path.join(ROOT, 'blog', c.slug, 'og.png'));
  await p.goto(BASE + '/'); await p.waitForTimeout(500);
  const h = await p.evaluate(() => ({ t: document.querySelector('.hp1 h1').getAttribute('aria-label') || document.querySelector('.hp1 h1').textContent, svg: document.querySelectorAll('.stile .sviz')[0].outerHTML }));
  await shoot(page('Websites, automation and AI', h.t.trim(), h.svg.replace(/class="a [^"]*"/g, ''), 'A one-person studio for established firms  ·  houssem-gabsi.vercel.app'), path.join(ROOT, 'og.png'));
  console.log('share pictures', cards.length + 1);
  await b.close();
})();
