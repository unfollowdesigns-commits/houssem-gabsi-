# -*- coding: utf-8 -*-
# v4 content. Wording supplied word for word by Houssem on 16 Nov 2026. Do not rewrite, shorten or "improve" it.
# Voice rules are in CLAUDE.md.

# ── hero ──
HEAD_TEXT = "The work a firm repeats every week, rebuilt to run on its own."
INTRO = ("Loose Ends is a one-person studio. It designs and builds the websites, automations and content systems "
         "that established firms in the US and Europe work on every day.")
HERO_BTN = "Request a free review"
HERO_LINK = "See the work"
# tool names shown under the hero buttons
HERO_TOOLS = ["Gmail", "Outlook", "Google Calendar", "Slack", "Microsoft Teams", "Claude", "ChatGPT", "Notion", "Airtable",
              "Google Sheets", "Excel", "HubSpot", "Salesforce", "Pipedrive", "Shopify", "Etsy", "WooCommerce", "Stripe",
              "QuickBooks", "Xero", "Calendly", "Substack", "Mailchimp", "LinkedIn", "Instagram", "WordPress", "Webflow",
              "Google Drive", "Dropbox", "DocuSign", "Zoom", "Asana", "Loxo", "BrightHire", "Zapier", "Make", "n8n"]
PANEL2_HEAD = "A week, before."
PANEL2_TEXT = "Answering, confirming, chasing, retyping. Each loose ochre thread is an hour spent moving information from one place to another."
COUNTER_TEXT = "hours a week returned to the team."
WEEK_NOTE = "Sample week."

# ── statement ──
STATEMENT = ("Every firm has work only its people can do, and work that simply has to get done. The second kind fills most of the week: "
             "answering, confirming, chasing, retyping. Systems take that part. People keep the judgement, and approve everything that leaves the building.")
STATEMENT_LINK = "How an engagement works"

# ── selected work. who = title, kind = label, did = text, now = proof line ──
WORK_LABEL = "Selected work"
WORK_HEAD = "Every piece of work started with one loose end."
CASES = [
 dict(kind="Executive search, Washington D.C.", who="Open roles entered once, live everywhere.",
  did="Roles go into the firm's recruiting system and appear on its eighteen-page website without anyone retyping them. Candidate CVs are put into the firm's format in one step. The same database now answers the team's questions through their AI assistant.",
  now="Website live. Candidate scoring in development."),
 dict(kind="Maison d'hôte, La Marsa", who="A nineteenth-century house that looks like itself online.",
  did="An identity drawn by hand from the house's own tiles, doors and objects. It runs through a website in French and English and the printed pieces guests hold, from the room card to the table d'hôte menu.",
  now="Identity and print delivered. Website in development."),
 dict(kind="Yoga studio", who="A class booked on one screen, not in a message thread.",
  did="Schedule, places and payment sit on a single phone screen, in French and English. Bookings moved out of Instagram messages and into one place.",
  now="Live."),
 dict(kind="Journalist, video production", who="An AI assistant that works the way he does.",
  did="His assistant is set up around his editorial week, not the software's defaults. The tasks he repeats now run the same way every time, with video production at the centre.",
  now="Delivered 2026."),
]
# Own products. Shown under the four client cases, with their own small label (Houssem, 16 Nov 2026: "we did all of that").
PRODUCTS_LABEL = "Products"
PRODUCTS = [
 dict(kind="Vero. Recruiting software", who="Candidates ranked, with the reasoning behind every score.",
  did="The platform reads a batch of résumés against a role and ranks the candidates. Every score shows its reasoning and the source text it came from. Outreach is drafted from each candidate's own work, and the decision stays with the recruiter.",
  now="In use."),
 dict(kind="ZonedInOut. Market analytics", who="A daily risk score for stocks, funds and crypto.",
  did="Each trading day, stocks, funds and cryptocurrencies are scored on how far the price has moved from its average, with an entry zone and a stop level. Past calls are published and graded. It is a scoring system, not financial advice.",
  now="In use."),
]

# ── services: (mark, label, title, text) ──
SERVICES_LABEL = "Services"
SERVICES_HEAD = "Websites, automation and content, built as one system."
WHAT = [
 ("build", "Build", "Websites and applications.",
  "The site clients judge the firm by and the tools the team opens every morning, designed and built end to end."),
 ("automate", "Automate", "Work that runs without anyone doing it.",
  "Follow-up, confirmations and reports happen on their own. A person approves what matters before anything is sent."),
 ("create", "Create", "Identity and content.",
  "A visual identity, and a content process that turns one idea into a week of publishing in the firm's own voice."),
]
# short points listed on each service card. Not part of the v4 wording; kept from the earlier version.
EXAMPLES = {
 "build": ["Company and marketing websites", "Online shops on Shopify and Etsy", "Booking applications", "Dashboards and reporting", "Internal tools and client portals", "Web applications built to order"],
 "automate": ["Enquiry and invoice follow-up", "Booking confirmations", "Screening of applications and enquiries", "Weekly reports and newsletters", "Social media scheduling", "Claude and other AI assistants set up for the team", "Custom Claude skills for the tasks the team repeats", "Connectors (MCP) and custom API integrations"],
 "create": ["Brand identity and illustration", "Video editing and motion graphics", "Articles, blog posts and Substack newsletters", "LinkedIn and Instagram content", "Visibility in search and AI answers (SEO and GEO)"],
}

# ── systems: (title, "", text, status) ──
SYSTEMS_LABEL = "Systems"
SYSTEMS_HEAD = "Each system is built around one costly habit."
SYSTEMS = [
 ("Every unanswered enquiry, found and drafted.", "",
  "The system reads the inbox, quotes and invoices, finds what went quiet, and drafts each reply. Someone approves, then it sends.",
  "Works with email, quotes and invoices."),
 ("Every candidate read against the search.", "",
  "Each candidate is assessed against that search's own criteria, with the reasoning written beside the score. The recruiter decides.",
  "Works with the firm's recruiting system."),
 ("One idea, a week of publishing.", "",
  "A researched article and a week of posts from a single idea. Every figure is checked against a named source before it goes out.",
  "Works with the blog, Substack, LinkedIn and Instagram."),
 ("Interview notes in, client report out.", "",
  "Raw notes become a finished report in the firm's format. Every rating points to its source, and gaps are flagged, never filled.",
  "Works with interview notes and the firm's report template."),
 ("A skill for every task the team repeats.", "",
  "The proposal, the weekly report, the candidate summary. Each one is written down once as a Claude skill, with the firm's format and its quirks, so whoever runs it gets the same result. Someone still signs off before it leaves.",
  "Works with Claude skills and the firm's own templates."),
 ("An assistant that knows the firm's own data.", "",
  "Claude gets read access to the files, the inbox and the database. Ask it which invoices are overdue and it checks, instead of guessing.",
  "Works with Claude connectors (MCP) and the firm's own tools."),
 ("Bookings confirmed, reminded and rescheduled.", "",
  "Clients pick a time on one screen. The confirmation goes out, the reminder goes out the day before, and when someone moves, the calendar moves with them.",
  "Works with the calendar, the booking page and payments."),
 ("Every invoice followed up until it is paid.", "",
  "When an invoice slips past its date, a polite reminder is drafted and waits for a yes. Then a firmer one, a week later. Nobody has to remember to chase.",
  "Works with the accounting tool and email."),
 ("New clients onboarded without the paperwork chase.", "",
  "The new client fills in one form, signs once and uploads what's needed. It all lands in their folder, and the team hears when the last piece arrives.",
  "Works with forms, e-signature and shared drives."),
 ("Weekly figures prepared before anyone asks.", "",
  "Monday morning, the numbers are already in one place, with a short note in Slack saying what moved. Nobody spent Sunday on a spreadsheet.",
  "Works with spreadsheets, databases and Slack."),
 ("Orders, stock and listings kept in step.", "",
  "Something sells on Etsy, and Shopify knows a second later. Stock stays right on every channel, so the last one is never sold twice.",
  "Works with Shopify, Etsy and spreadsheets."),
 ("A newsletter that assembles itself.", "",
  "By Thursday the week's posts and updates are pulled into a draft that sounds like the firm. Someone reads it, tweaks a line, and sends.",
  "Works with Substack and the firm's email platform."),
 ("Posts scheduled across every channel.", "",
  "One approved piece becomes a LinkedIn post, an Instagram caption and a blog excerpt, each sized for where it goes, and scheduled on a calendar the team can see.",
  "Works with LinkedIn, Instagram and the content calendar."),
 ("Meeting notes turned into actions.", "",
  "After the call, a summary lands in the CRM with the decisions and who owns what. The reminders go to those people, not to everyone.",
  "Works with the calendar, call recordings and the CRM."),
 ("Documents filed where they belong.", "",
  "A signed contract arrives as an attachment. It's renamed properly and filed in the client's folder before anyone opens their inbox.",
  "Works with email, shared drives and the firm's database."),
 ("A website that search engines and AI assistants can read.", "",
  "When someone asks ChatGPT or Perplexity who does this kind of work, the firm's pages are written and marked up so the answer can name it.",
  "Works with the website and its content."),
]
SYSTEMS_NOTE = "A free %s for product businesses is also available."
SYSTEMS_NOTE_LINK = "stock, sales and production tracker"

# ── capacity ──
CAPACITY_LABEL = "Capacity"
CAPACITY_HEAD = "A small team that answers like a large one."
CAPACITY_INTRO = "None of these are people. Each is a routine that now runs by itself, with someone approving the result."

# ── enquiry diagram ──
ENQUIRY_LABEL = "In practice"
ENQUIRY_HEAD = "One enquiry, handled before anyone opens it."
ENQUIRY_INTRO = "From the form to a reply ready for approval, with no manual step."

# ── commitments ──
COMMIT_LABEL = "Commitments"
COMMIT_HEAD = "What holds on every engagement."
RULES = [
 ("One price, agreed in advance.", "Confirmed in writing before work begins. If the scope grows, the new price is agreed before the additional work starts."),
 ("You own everything.", "The code, the domain and the accounts are yours, and are transferred on request at no additional cost."),
 ("Nothing reaches your clients without approval.", "Every system drafts and prepares. A member of your team approves before anything is sent."),
 ("Honest advice on what to build.", "If a piece of work will not repay its cost, you will hear that in the first conversation."),
 ("One person does the work.", "Houssem Gabsi runs every engagement himself, which is also why Loose Ends takes on a limited number of projects at a time."),
 ("Plain language.", "Everything built is explained, and why, in terms the team can repeat without the studio in the room."),
]

# ── process: (title, text, label) ──
PROCESS_LABEL = "Process"
PROCESS_HEAD = "Nothing is built until the problem is proven."
PROCESS_INTRO = "The first step is free. The audit findings belong to the firm whether or not anything is built."
HOW = [
 ("Find the loose end.", "A free one-page review of where the firm loses time. No call required.", "Free"),
 ("Measure it.", "A paid audit ranks the first three fixes by what they return. The fee is credited toward the build.", "Credited"),
 ("Build one thing.", "The fix with the most hours in it, at one price agreed in writing.", "Fixed price"),
 ("Hand it over.", "The team is trained and every routine has a named owner. Code, domain and accounts belong to the firm.", "Handover"),
 ("Stay, if useful.", "Optional monthly support.", "Optional"),
]

# ── pricing. Set by Houssem on 17 Nov 2026 at the average market price for this work (US dollars, starting prices). ──
PRICING_LABEL = "Pricing"
PRICING_HEAD = "One fixed price for every build, agreed in writing."
PRICING_INTRO = "Starting prices in US dollars. The exact price is set after the audit and confirmed in writing before work begins. There is no hourly billing."
PRICING = [
 ("Free review", "Free", "", "A one-page review of where the firm loses time. No call required."),
 ("Systems audit", "$1,500", "", "The first fixes ranked by what they return. The fee is credited toward the build."),
 ("Automation", "$3,000", "from", "Follow-up, bookings, reports or screening, built inside the tools the team already opens every day."),
 ("AI assistant setup", "$4,500", "from", "Claude connected to the firm's data, with skills for the repeated tasks and a session to show the team how to use it."),
 ("Websites and online shops", "$5,000", "from", "Designed, written and built from scratch, Shopify and Etsy included, and set up to be found in search and AI answers."),
 ("Applications and integrations", "$9,000", "from", "Booking applications, dashboards, client portals and custom API or MCP connections."),
 ("Brand and content", "$3,500", "from", "Identity, illustration, video and a content system that turns one idea into a week of publishing."),
 ("Ongoing support", "$600", "a month", "Small changes, a watchful eye, and new routines as the firm grows. Optional, and easy to stop."),
]

# ── questions. The hidden structured data is generated from this same list. ──
FAQ_LABEL = "Questions"
FAQ_HEAD = "What firms ask before they start."
FAQ = [
 ("What does Loose Ends build for a firm?",
  "For most firms it is three things: the follow-up nobody has time to send, the booking or intake process clients pass through, and the reports someone prepares by hand every week. The work is connecting the tools already in use, not replacing them."),
 ("What happens when a system gets something wrong?",
  "Nothing reaches a client without a person approving it, so a wrong draft is caught at that step and corrected there. That approval is a design rule, not a setting that can be switched off."),
 ("Who owns what is built?",
  "The firm does. The code, the domain and the accounts are transferred on request at no additional cost."),
 ("Does it fit the tools already in use?",
  "Yes. Every system is built around the firm's existing email, calendar, spreadsheets and databases. Replacing software that works is the most expensive way to automate anything."),
 ("What does it cost, and how is it priced?",
  "Every engagement begins with a paid Systems Audit at a fixed price, credited toward the build. After the audit, each build has one fixed price agreed in writing. There is no hourly billing."),
 ("How is this different from hiring an automation freelancer?",
  "An automated workflow is one part of the work. The studio also builds the website or application it runs inside, produces the content that feeds it, and makes the short film that explains it to clients."),
 ("Where does the studio work, and does it matter?",
  "Anywhere. Most of the work is for clients abroad, in English, French or Arabic. Calls are scheduled in the client's time zone, and delivery is the same wherever the firm is."),
]

# ── closing ──
CLOSE_HEAD = "Find the loose ends in the week."
CLOSE_TEXT = "Send a line about the firm. A one-page review comes back, free, with the first three places to look."
CLOSE_BTN = "Request a free review"
CLOSE_NOTE = "A reply within 24 hours."

# ── footer, page title and description ──
FOOT_DESC = ("Loose Ends is a one-person studio run by Houssem Gabsi. It builds websites, automation and content systems "
             "for established firms, in English, French and Arabic.")
PAGE_TITLE = "Loose Ends | Websites, automation and content systems for established firms"
PAGE_DESC = ("Loose Ends is a one-person studio that designs and builds websites, automations and content systems for established firms in the US and Europe. "
             "Follow-up, booking and reporting that run on their own, with a person approving before anything is sent.")

# ── wording outside the v4 text. The connections section was not covered and is unchanged. ──
CTA_NOTE = "Free. One page. No call required."
CTA_CONNECT = "Not sure what could be connected? The free review answers that."

# shown under the three service cards
ANY_NOTE = "These are examples. If a task happens on a screen and comes back every week, it can probably be built to run by itself."
