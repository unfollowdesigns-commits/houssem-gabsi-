# Houssem Gabsi studio site

Read this first, every session.

## What this is
A one-page static site, live on Vercel. Vercel redeploys on every push to this repo.
Vercel serves the site from the top level of this repo. The Root Directory setting in the Vercel project must stay empty.

## How it is built
`index.html` is generated. Do not edit it by hand.

- `_source/cases.py`: all the wording. Hero line, services, the cases (client work and own products), systems, working rules, process, questions.
- `_source/parts.py`: the capacity grid and the enquiry diagram wording.
- `_source/icons.py`: the small line icons.
- `_source/build.py`: layout, styles, motion, and the script that writes `index.html`.

To change the site: edit the files in `_source`, then run

    cd _source && python3 build.py

It writes `../index.html` and `../llms.txt`. Open the page in a browser, check it, then commit and push.

`llms.txt` is a plain-text summary for AI assistants. It is generated from the same lists as the page. Do not edit it by hand.

## What the studio offers
Keep all of these on the page. Houssem has had to repeat them.
- Websites, online shops (Shopify, Etsy), booking applications, dashboards, internal tools.
- Automation inside the tools a business already has: follow-up, bookings, screening, reports, newsletters, social media scheduling.
- Connections between tools: email, calendar, Slack, spreadsheets, Loxo, BrightHire, Shopify, Etsy, Substack.
- Setting up Claude and other AI assistants for a team, connected to its own data. Most people use a fraction of what the assistant can do. That gap is the studio's main offer.
- SEO and GEO (visibility in AI answers).
- Brand identity, illustration, content, video editing, motion graphics.
- Own products: Vero and ZonedInOut.

## Rules
- Plain, professional language. No jargon, no buzzwords, no em dashes.
- Nothing invented: no numbers, quotes or results that were not given by Houssem. Fictional or illustrative data is always labelled, briefly, as "sample" data. Do not write "fictional firm" or "not a client's figures".
- Clients are not named. Cases are titled by the work, with the client type underneath.
- Audience: any business, from an independent professional to an established firm. The page must not read as if it serves one industry. Recruiting is one example among several. Not "founders", not "struggling".
- No background or CV content on the page. It shows what the studio builds.
- Do not advertise speed of delivery.
- The questions section and the hidden structured data are generated from the same list in `cases.py`, so they always match.
- The page title and search description are set at the end of `cases.py`. The site address is set near the structured data in `build.py`.
- The wording in `cases.py` was supplied word for word by Houssem (16 Nov 2026). Do not rewrite, shorten or "improve" it.

### Voice rules
- Headings are full sentences that make a claim and end with a full stop. Category words go in the small label above, never in the heading.
- Say "the firm" and "the team", not "you" and "your". Never "we help", never hype words.
- Name the actual chores: answering, confirming, chasing, retyping.
- Work is titled by its result, not by the client type.
- A person approves before anything is sent. Say it wherever it applies.

- The studio is called Loose Ends. Wording speaks as the studio, never as 'I'. Use the loose end idea in three places only: process step 1, the work heading and the closing heading.

### Other rules
- Keep `tools/`, `downloads/`, `fonts/` and `media/` as they are unless asked.
- The page's two typefaces are served from `fonts/` (Fraunces and Archivo). The page loads nothing from other sites.
- Commit and push to the working branch after every step, without asking (Houssem, 16 Nov 2026). The branch only produces a Vercel preview.
- Nothing goes onto `main`, which is the live site, without Houssem's OK.

## Before pushing
Run the build, open the page, and check: the Before / After switch, the accordions, the menu marker, a phone-width view, and that there are no script errors.
