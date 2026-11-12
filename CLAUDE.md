# Houssem Gabsi studio site

Read this first, every session.

## What this is
A one-page static site, live on Vercel. Vercel redeploys on every push to this repo.

## How it is built
`index.html` is generated. Do not edit it by hand.

- `_source/cases.py`: all the wording. Hero line, services, the four cases, systems, working rules, process, questions.
- `_source/parts.py`: the capacity grid and the enquiry diagram wording.
- `_source/icons.py`: the small line icons.
- `_source/build.py`: layout, styles, motion, and the script that writes `index.html`.

To change the site: edit the files in `_source`, then run

    cd _source && python3 build.py

It writes `../index.html`. Open it in a browser, check it, then commit and push.

## Rules
- Plain, professional language. No jargon, no buzzwords, no em dashes.
- Nothing invented: no numbers, quotes or results that were not given by Houssem. Fictional or illustrative data is always labelled.
- Clients are not named. Cases are titled by the work, with the client type underneath.
- Audience: established firms. Not "founders", not small struggling businesses.
- No background or CV content on the page. It shows what the studio builds.
- Do not advertise speed of delivery.
- The questions section and the hidden structured data are generated from the same list in `cases.py`, so they always match.
- Keep `tools/`, `downloads/`, `fonts/` and `media/` as they are unless asked.
- Nothing is pushed live without Houssem's OK.

## Before pushing
Run the build, open the page, and check: the Before / After switch, the accordions, the menu marker, a phone-width view, and that there are no script errors.
