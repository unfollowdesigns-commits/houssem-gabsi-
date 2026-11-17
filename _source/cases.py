# -*- coding: utf-8 -*-
# v4 content. Wording supplied word for word by Houssem on 16 Nov 2026. Do not rewrite, shorten or "improve" it.
# Voice rules are in CLAUDE.md.

# ── hero ──
HEAD_TEXT = "The work a firm repeats every week, rebuilt to run on its own."
INTRO = ("Loose Ends is a one-person studio. It designs and builds the websites, automations and content systems "
         "that established firms in the US and Europe work on every day.")
HERO_BTN = "Request a free review"
HERO_LINK = "See the work"
PANEL2_HEAD = "A week, before."
PANEL2_TEXT = "Answering, confirming, chasing, retyping. Each ochre block is an hour spent moving information from one place to another."
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
 "automate": ["Enquiry and invoice follow-up", "Booking confirmations", "Screening of applications and enquiries", "Weekly reports and newsletters", "Social media scheduling", "Claude and other AI assistants set up for the team", "Connectors (MCP) and custom API integrations"],
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
 ("Plain language.", "Everything built is explained, and why, in terms your team can repeat without me in the room."),
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
ANY_NOTE = "These lists are examples, not limits. If the work happens on a screen and repeats, the studio can build the system that does it."
