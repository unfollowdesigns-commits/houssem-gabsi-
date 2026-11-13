# -*- coding: utf-8 -*-
# v3.2 content. Professional register, plain language. Clients unnamed. Nothing invented.

SERVICES_INTRO = ("Most of the work is making the tools a business already has do more: finding where time is lost, "
                  "removing repeated and administrative work, and connecting what is already there. "
                  "Most engagements combine all three.")

# short examples shown as a list on each service card
EXAMPLES = {
 "build": ["Company and marketing websites", "Online shops on Shopify and Etsy", "Booking applications", "Dashboards and reporting", "Internal tools"],
 "automate": ["Enquiry and invoice follow-up", "Booking confirmations", "Screening of applications and enquiries", "Weekly reports and newsletters", "Social media scheduling", "Claude and other AI assistants set up for your team"],
 "create": ["Brand identity and illustration", "Video editing and motion graphics", "Articles, blog posts and Substack newsletters", "LinkedIn and Instagram content", "Visibility in search and AI answers (SEO and GEO)"],
}

CTA_NOTE = "Free. One page. No call required."
CTA_WORK = "A similar problem in your business?"
CTA_CONNECT = "Not sure what could be connected in your business? The free review answers that."
NEXT = [
 ("You write a few lines", "about the business and what takes the most time each week."),
 ("I send a one-page review", "of where time is being lost and what could be automated first."),
 ("You decide", "whether to go further. The review is yours either way."),
]

INTRO = ("Websites, automation and content for any business, from a single professional to an established firm, built so the systems "
         "you already pay for work together. One person, end to end.")

WHAT = [
 ("build", "Build", "Websites and applications",
  "Client-facing websites, online shops, booking systems, dashboards and internal tools, designed and built end to end, with as much care for how they are used as for how they look."),
 ("automate", "Automate", "Operations that run without manual effort",
  "Follow-up, booking confirmations, screening, reporting and newsletters, handled automatically inside the tools you already use: email, Slack, your calendar and the specialist software of your trade. A member of your team approves anything before it is sent."),
 ("create", "Create", "Brand identity and content systems",
  "Visual identity, illustration, video editing and motion graphics, and a content process that turns one idea into a month of publishing across your blog, newsletter, LinkedIn and Instagram, in your voice and structured for search engines and AI assistants."),
]

CASES = [
 dict(who="A recruiting website that keeps itself current", kind="Executive search firm, Washington D.C., since 2025",
  before="The firm had outgrown its website. Open roles were maintained manually in two places, candidates were assessed one at a time, and client reports were assembled by hand.",
  did="An eighteen-page website with open roles synchronised from the firm's recruiting system. A tool that formats candidate CVs to the firm's standard. An interactive map of its consultant network. The firm's recruiting database and internal chat connected to its AI assistant, so the team can query its own candidate data.",
  now="Website live. Candidate scoring in development: each candidate assessed against the criteria of the search, with written reasoning for every score."),
 dict(who="An identity drawn from the house itself", kind="Maison d'hôte, La Marsa, 2026",
  before="A nineteenth-century house of nine rooms with an excellent reputation, and a website that did not reflect it.",
  did="A visual identity drawn from the house itself: its tiles, doors and objects. A bilingual website in French and English designed around that identity, and the printed material guests handle, including room cards and the table d'hôte menu.",
  now="Identity and print delivered. Website in development."),
 dict(who="Class booking on a single screen", kind="Yoga studio, Tunis, 2026",
  before="Classes were booked through Instagram messages, leaving the studio without a reliable view of attendance.",
  did="A mobile-first booking application. Class schedule, availability and payment on a single screen, in French and English.",
  now="Live."),
 dict(who="An AI assistant built around an editorial week", kind="Journalist, video production, 2026",
  before="He had access to AI tools but was getting little practical value from them. Recurring work was still done manually.",
  did="His AI assistant configured around his editorial work rather than the software's defaults. Recurring weekly tasks now follow a consistent, repeatable process, with video production at the centre.",
  now="Delivered."),
 dict(who="A recruiting platform that explains every score", kind="Own product, 2026",
  before="Most candidate screening tools return a score without the reasoning behind it, so a recruiter can neither defend it nor question it.",
  did="Vero, a web application that reads a batch of résumés against a role, ranks the candidates, and shows the reasoning and the source text behind every score. It also drafts outreach based on each candidate's own work. The decision stays with a person.",
  now="Live.",
  link="https://vero-woad.vercel.app/", img="vero.jpg", alt="The Vero home page: Hiring intelligence that reads between the lines."),
 dict(who="A daily entry-risk score for stocks and crypto", kind="Own product, 2026",
  before="A price shows what an asset costs today, not whether today is a sensible moment to buy it.",
  did="ZonedInOut, a website that scores stocks, ETFs and cryptocurrencies every trading day on how far the price has moved from its average, with an entry zone and a stop level for each. Past calls are published and graded. It is a scoring system, not financial advice.",
  now="Live.",
  link="https://zonedinout.vercel.app/", img="zonedinout.jpg", alt="The ZonedInOut home page: Know the risk before you enter."),
]

SYSTEMS = [
 ("Invoice and quote follow-up",
  "Revenue is lost in enquiries, quotes and invoices that nobody followed up.",
  "Reviews the inbox, quotes and invoices, identifies unanswered enquiries, stalled quotes and overdue invoices, and drafts a reply for each. Nothing is sent without approval.",
  "Built. Demonstrated on a fictional firm."),
 ("Content system",
  "Most businesses publish content that is neither found nor finished.",
  "Turns one idea into a researched article and a week of posts. Every figure is verified against a named source before publication, and each piece is structured to be cited by search engines and AI assistants.",
  "In weekly use on client work."),
 ("Candidate scoring in your recruiting database",
  "A recruiter can assess only a fraction of the candidates on a search in depth.",
  "Assesses every candidate on a search against that search's criteria, and records the score and the reasoning in the candidate's record. The decision stays with a person.",
  "In development for an executive search firm."),
 ("Interview notes to client report",
  "Converting interview notes into a client report takes hours each week.",
  "Converts raw notes into a finished report in your own format. Every rating references the source notes, and gaps are flagged rather than filled.",
  "Built. Demonstrated on fictional data."),
]

RULES = [
 ("One price, agreed in advance.", "Confirmed in writing before work begins. If the scope grows, the new price is agreed before the additional work starts."),
 ("You own everything.", "The code, the domain and the accounts are yours, and are transferred on request at no additional cost."),
 ("Nothing reaches your clients without approval.", "Every system drafts and prepares. A member of your team approves before anything is sent."),
 ("Honest advice on what to build.", "If a piece of work will not repay its cost, you will hear that in the first conversation."),
 ("You work with me directly.", "One person does the work, which is also why I take on a limited number of projects at a time."),
 ("Plain language.", "I explain what was built and why, in terms your team can repeat without me in the room."),
]

HOW = [
 ("Initial review", "A free one-page review of where the business is losing time. No call required."),
 ("Audit", "A paid assessment, with the first three improvements ranked. The fee is credited toward the build."),
 ("Build", "One fixed price, agreed in writing before work begins."),
 ("Launch", "Your team is trained on the system, and every process has a named owner."),
 ("Support", "Optional monthly support, if you want it."),
]

FAQ = [
 ("What kinds of businesses do you work with?",
  "Any business that runs on repeated work. So far that has meant an executive search firm in Washington D.C., a guesthouse in La Marsa, a yoga studio in Tunis and a journalist working in video, as well as two products of my own. The method is the same each time: find the repeated work, then build or connect what removes it."),
 ("What does an automation studio build for a business?",
  "It is usually three things: the follow-up nobody has time to send, the booking or intake process clients pass through, and the reports someone prepares by hand every week. The work is connecting the tools you already use, not replacing them."),
 ("Do we need to replace the software we already use?",
  "No. Every system is built around your existing email, calendar, spreadsheets and databases. Replacing software that works is the most expensive way to automate anything."),
 ("Will AI send anything to our clients without our approval?",
  "No. Every system drafts and prepares. A member of your team approves before anything reaches a client. That is a design rule, not a setting that can be switched off."),
 ("How is this different from hiring an automation freelancer?",
  "An automated workflow is one part of the work. I also build the website or application it runs inside, produce the content that feeds it, and make the short film that explains it to your clients."),
 ("What does it cost, and how is it priced?",
  "Every engagement begins with a paid Systems Audit at a fixed price, and that fee is credited toward the build. After the audit, each build has one fixed price, agreed in writing. There is no hourly billing."),
 ("Can a small team respond like a larger one?",
  "Yes. Enquiries answered at any hour, invoices followed up on a set schedule, bookings confirmed as they are made and weekly figures sent without anyone preparing them. Each is a small process that runs automatically, and a member of your team approves anything before it is sent."),
 ("Which tools do you connect to?",
  "The ones you already use: email, calendars, spreadsheets and Slack, the specialist software of your trade, such as Loxo and BrightHire in recruiting, and the AI assistant the team already works with. The aim is to make existing tools work together, not to add new ones."),
 ("Can you set up Claude or another AI assistant for our business?",
  "Yes. Most businesses use an AI assistant for single questions and little else. I connect it to your own tools and data, such as email, calendar, documents, your shop and your customer records, and set up the recurring tasks it should handle, so the whole team gets consistent results from it. Much of what is on this page is built that way."),
 ("Do you work on SEO and on visibility in AI answers?",
  "Yes. Search engine optimisation, and what is now called generative engine optimisation, or GEO: structuring a site and its content so that search engines and AI assistants such as ChatGPT, Claude and Perplexity can find it, understand it and cite it. This site is built that way."),
 ("Do you work with Shopify, Etsy and Substack?",
  "Yes. Online shops on Shopify and Etsy, and newsletters on Substack, can be built, tidied up and connected to the rest of your tools, so that orders, stock, listings and publishing no longer depend on someone copying things by hand."),
 ("How does an engagement start?",
  "With a free one-page review of where the business is losing time. No call is required. If you want to go further, a paid audit ranks the first three improvements, and its fee is credited toward the build."),
 ("Who owns the website, the code and the accounts?",
  "You do. The code, the domain and the accounts are yours, and are transferred on request at no additional cost."),
 ("What can be automated in a recruiting or executive search firm?",
  "The work around the search, not the judgement in it: keeping open roles current on the website, formatting candidate CVs to the firm's standard, assessing every candidate against the criteria of the search with written reasoning, and turning interview notes into a client report. The decision stays with a person."),
 ("Where are you based, and does it matter?",
  "Tunis. Most of the work is for clients abroad, in English, French or Arabic. Calls are scheduled in your time zone, and delivery is the same wherever you are."),
]
