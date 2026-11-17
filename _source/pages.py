# -*- coding: utf-8 -*-
# Search pages. One page per thing someone might type into Google or ask an AI assistant.
# Same rules as cases.py: plain language, nothing invented, clients unnamed, no speed claims.
# Each page: slug, title (search phrase first), h1, lead (a direct answer), short (summary points),
# sections [(heading, [paragraphs or lists])], faq [(question, answer)], related [slugs].

PAGES = [
 dict(
  slug="claude-consulting",
  nav="Claude consulting",
  title="Claude Consulting and Setup for Business",
  desc="Claude consulting for businesses of any size: setup, connection to your own tools and data, reusable instructions and team training. Designed and built end to end.",
  h1="Claude consulting and setup for business",
  lead="Most teams that pay for Claude use it for single questions and little else. Loose Ends sets it up so it works inside the business: connected to your own tools and data, given the instructions your work needs, and taught to the people who will use it.",
  short=["Claude connected to your email, calendar, documents, shop and customer records",
         "Recurring tasks written once and reused by the whole team",
         "A person approves anything before it reaches a client",
         "Training in plain language, so the team keeps using it"],
  sections=[
   ("What Claude consulting covers", [
     "Claude consulting is the work of turning an AI assistant your team already has into something the business runs on. It has four parts.",
     ["Setup: the right workspace, projects and permissions for how your team is organised.",
      "Connection: Claude linked to the tools you already use, so it works from live business data and not from what someone pastes in.",
      "Instructions: the tasks your team repeats each week, written once so anyone gets the same result.",
      "Training: short sessions built around your own work, not generic prompts."]]),
   ("What changes once Claude is set up properly", [
     "The difference is that people stop starting from a blank page. Anyone on the team can ask a question and get the answer from your own data. Replies, reports and first drafts are prepared in your voice. The weekly tasks nobody enjoys follow a consistent process.",
     "Nothing is sent to a client without a member of your team approving it. That is a design rule in every system the studio builds."]),
   ("An example from client work", [
     "A journalist working in video had access to AI tools but was getting little practical value from them. The studio configured his assistant around his editorial week rather than the software's defaults. Recurring weekly tasks now follow a consistent, repeatable process, with video production at the centre.",
     "For an executive search firm, the studio connected the firm's recruiting database and internal chat to its AI assistant, so the team can query its own candidate data."]),
   ("What Claude can be connected to", [
     "Email and calendar, Slack, spreadsheets and databases, Shopify and Etsy, Substack, and the specialist software of your trade, such as Loxo and BrightHire in recruiting. If a tool can share its data, it can usually be connected.",
     "These connections are built on the Model Context Protocol, or MCP, the open standard for linking an AI assistant to tools and data."]),
   ("How an engagement runs", [
     ["A free one-page review of where time is being lost. No call required.",
      "A paid audit that ranks the first three improvements. The fee is credited toward the build.",
      "The build, at one fixed price agreed in writing before work begins.",
      "Launch: your team is trained, and every process has a named owner.",
      "Optional monthly support, if you want it."]]),
  ],
  faq=[
   ("What does a Claude consultant do?",
    "A Claude consultant sets up Claude for a business: the workspace, the connections to the business's own tools and data, the reusable instructions for recurring tasks, and the training. The aim is that the whole team gets consistent results, not only the one person who is good with prompts."),
   ("Do we need to replace the software we already use?",
    "No. Claude is connected to your existing email, calendar, spreadsheets and databases. Replacing software that works is the most expensive way to automate anything."),
   ("Can Claude work with our own data?",
    "Yes. Through connectors built on the Model Context Protocol, Claude can read from and act on the tools you already use, with the permissions you set."),
   ("Is this only for large companies?",
    "No. The work is the same for an independent professional and for an established firm. What changes is how many people and tools are involved."),
   ("How is it priced?",
    "Every engagement begins with a paid audit at a fixed price, credited toward the build. Each build then has one fixed price, agreed in writing. There is no hourly billing."),
  ],
  related=["mcp-integrations", "ai-automation", "seo-geo"],
 ),
 dict(
  slug="ai-automation",
  nav="AI automation",
  title="AI Automation Services for Business",
  desc="AI automation built inside the tools a business already has: follow-up, bookings, screening, reports and publishing, approved by a person before sending.",
  h1="AI automation services for business",
  lead="AI automation means the repeated work in a business is done by a system, inside the tools the business already uses, with a person approving anything that goes out. Loose Ends finds that work, then builds what removes it.",
  short=["Follow-up on enquiries, quotes and invoices",
         "Booking confirmations and reminders",
         "Screening of applications and enquiries",
         "Weekly reports, newsletters and publishing"],
  sections=[
   ("What can be automated", [
     "In most businesses it is three things: the follow-up nobody has time to send, the booking or intake process clients pass through, and the reports someone prepares by hand every week.",
     ["Enquiry and invoice follow-up: unanswered enquiries, stalled quotes and overdue invoices are found, and a reply is drafted for each.",
      "Bookings: confirmed as they are made.",
      "Screening: every application or enquiry assessed against your own criteria, with the reasoning written down.",
      "Reporting: weekly figures sent to the people who need them, without anyone preparing them.",
      "Content: one idea turned into a researched article and a week of posts, published on schedule."]]),
   ("How it is different from buying another tool", [
     "Most automation products ask you to move your work into them. Loose Ends works the other way: the systems are built around your existing email, calendar, spreadsheets and databases. Nothing is replaced. The tools stay where they are and start working together.",
     "Every system drafts and prepares. A member of your team approves before anything reaches a client."]),
   ("Systems already built", [
     ["Invoice and quote follow-up: reviews the inbox, quotes and invoices, and drafts a reply for each item that has gone quiet.",
      "Candidate scoring: assesses every candidate on a search against that search's criteria, and records the score and the reasoning. The decision stays with a person.",
      "Content system: turns one idea into a researched article and a week of posts, with every figure checked against a named source.",
      "Interview notes to client report: converts raw notes into a finished report in your own format, with gaps flagged rather than filled."]]),
   ("Who it is for", [
     "Any business that runs on repeated work, from an independent professional to an established firm. Work so far includes an executive search firm in Washington D.C., a guesthouse in La Marsa, a yoga studio and a journalist working in video."]),
   ("How an engagement runs", [
     ["A free one-page review of where time is being lost. No call required.",
      "A paid audit that ranks the first three improvements. The fee is credited toward the build.",
      "The build, at one fixed price agreed in writing before work begins.",
      "Launch: your team is trained, and every process has a named owner."]]),
  ],
  faq=[
   ("What is AI automation?",
    "AI automation is the use of an AI system to carry out repeated work, such as follow-up, screening, reporting and drafting, inside the tools a business already uses. A person stays responsible for the decisions and approves what is sent."),
   ("Which tasks should a business automate first?",
    "Start with work that is frequent, follows the same pattern each time and costs money when it is forgotten: unanswered enquiries, unpaid invoices, booking confirmations and weekly reports."),
   ("Will AI send anything to our clients without our approval?",
    "No. Every system drafts and prepares. A member of your team approves before anything reaches a client. That is a design rule, not a setting that can be switched off."),
   ("Do you only work with small businesses?",
    "No. The method is the same at any size. What changes is the number of tools and people involved."),
   ("Who owns what is built?",
    "You do. The code, the domain and the accounts are yours, and are transferred on request at no additional cost."),
  ],
  related=["claude-consulting", "mcp-integrations", "websites-and-online-shops"],
 ),
 dict(
  slug="mcp-integrations",
  nav="MCP integrations",
  title="MCP Integrations: Connect Claude to Your Tools",
  desc="MCP integration services: Claude connected to email, Slack, Shopify, Etsy, Substack, spreadsheets, Loxo, BrightHire and the tools specific to your business.",
  h1="MCP integrations: connect Claude to your business tools",
  lead="MCP, the Model Context Protocol, is the open standard that lets an AI assistant such as Claude connect to the tools and data a business already has. Loose Ends designs and builds those connections, so the assistant works with your live information and not with what someone remembers to paste in.",
  short=["Email, calendar and Slack",
         "Shopify, Etsy and Substack",
         "Spreadsheets and databases",
         "Loxo, BrightHire and the software of your trade"],
  sections=[
   ("What gets connected, and what changes", [
     ["Email and calendar: replies are drafted and meetings booked without the back and forth.",
      "Slack: approvals and alerts arrive where the team already talks.",
      "Shopify and Etsy: orders, stock and listings stay in step without retyping.",
      "Substack, LinkedIn and Instagram: one piece of writing is published everywhere it belongs.",
      "Loxo, BrightHire and the software of your trade: records stay current, and nobody copies between systems.",
      "Spreadsheets and databases: figures update themselves, so reports no longer need preparing.",
      "Claude: anyone on the team can ask a question and get the answer from your own data."]]),
   ("Why connections matter more than prompts", [
     "An assistant that cannot see your data can only answer in general terms. Once it is connected, it can read the inbox, check the calendar, look up an order or a candidate, and prepare the next step. That is the gap between using a fraction of what Claude can do and using it properly.",
     "The method does not change with the trade. If a tool can share its data, it can be connected to the others and to an AI assistant."]),
   ("An example from client work", [
     "For an executive search firm in Washington D.C., the studio connected the firm's recruiting database and internal chat to its AI assistant, so the team can query its own candidate data. Open roles on the firm's website are synchronised from the same recruiting system, so they are no longer maintained by hand in two places."]),
   ("Control and approval", [
     "Each connection is given only the access it needs. Every system drafts and prepares, and a member of your team approves before anything is sent. You own the accounts and the code, and they are transferred on request at no additional cost."]),
  ],
  faq=[
   ("What is MCP?",
    "MCP stands for Model Context Protocol. It is an open standard that lets an AI assistant connect to external tools and data sources, such as email, databases and business software, so it can read information and take actions with the permissions it is given."),
   ("Which tools can be connected to Claude?",
    "Email, calendars, spreadsheets, databases and Slack; Shopify, Etsy and Substack; recruiting platforms such as Loxo and BrightHire; and most business software that can share its data."),
   ("Do we have to change the tools we use?",
    "No. Nothing is replaced. The tools stay where they are and start working together."),
   ("Is our data safe?",
    "Each connection is limited to the access it needs, and the accounts remain yours. Nothing reaches a client without a member of your team approving it."),
  ],
  related=["claude-consulting", "ai-automation", "websites-and-online-shops"],
 ),
 dict(
  slug="websites-and-online-shops",
  nav="Websites and online shops",
  title="Website and Online Shop Design: Shopify and Etsy",
  desc="Websites, booking applications and online shops on Shopify and Etsy, designed and built by one person and connected to the rest of your tools.",
  h1="Website and online shop design, connected to the rest of your business",
  lead="Loose Ends designs and builds websites, booking applications and online shops, and connect them to the tools behind them, so an enquiry, a booking or an order reaches the right place without anyone retyping it.",
  short=["Company and marketing websites",
         "Online shops on Shopify and Etsy",
         "Booking applications",
         "Dashboards and internal tools"],
  sections=[
   ("What the studio builds", [
     ["Company and marketing websites, designed around the identity of the business.",
      "Online shops on Shopify and Etsy, with orders, stock and listings kept in step.",
      "Booking applications, with schedule, availability and payment on a single screen.",
      "Dashboards and internal tools that show the figures a team needs."],
     "Each is designed and built end to end by one person, with as much care for how it is used as for how it looks."]),
   ("Selected work", [
     ["An eighteen-page website for an executive search firm in Washington D.C., with open roles synchronised from the firm's recruiting system.",
      "A bilingual website and visual identity for a guesthouse in La Marsa, drawn from the house itself: its tiles, doors and objects.",
      "A mobile-first booking application for a yoga studio, in French and English.",
      "The studio's own products: Vero, recruiting software that shows the reasoning behind every candidate score, and ZonedInOut, a daily risk score for stocks, funds and crypto."]]),
   ("Built to be found", [
     "Every site is structured for search engines and for AI assistants: clear headings, direct answers, structured data and a plain-text summary that assistants can read. See SEO and GEO for how that works."]),
   ("Ownership", [
     "The code, the domain and the accounts are yours, and are transferred on request at no additional cost. Each build has one fixed price, agreed in writing before work begins."]),
  ],
  faq=[
   ("Do you build Shopify and Etsy shops?",
    "Yes. Online shops on Shopify and Etsy can be built, tidied up and connected to the rest of your tools, so that orders, stock and listings no longer depend on someone copying things by hand."),
   ("Can you redesign an existing website?",
    "Yes. Most projects start from a site the business has outgrown. The existing content and accounts are kept where they still serve."),
   ("Do you work in languages other than English?",
    "Yes. The studio works in English, French and Arabic, and have built bilingual sites in French and English."),
   ("Who owns the website when it is finished?",
    "You do. The code, the domain and the accounts are yours, and are transferred on request at no additional cost."),
  ],
  related=["seo-geo", "ai-automation", "mcp-integrations"],
 ),
 dict(
  slug="seo-geo",
  nav="SEO and GEO",
  title="SEO and GEO: Visibility in Search and AI Answers",
  desc="SEO and generative engine optimisation: sites and content structured so Google, ChatGPT, Claude and Perplexity can find them, understand them and cite them.",
  h1="SEO and GEO: visibility in search and in AI answers",
  lead="People now find businesses in two places: search results, and the answers given by AI assistants such as ChatGPT, Claude and Perplexity. Loose Ends structures a site and its content so both can find it, understand it and cite it.",
  short=["Search engine optimisation",
         "Generative engine optimisation (GEO)",
         "Structured data and answer-first pages",
         "A content process that keeps publishing"],
  sections=[
   ("What GEO is", [
     "Generative engine optimisation, or GEO, is the practice of making a site easy for AI assistants to read and quote. It is sometimes called answer engine optimisation, or AEO. It builds on ordinary SEO rather than replacing it.",
     "An assistant can only cite what it can read and trust. So the work is plain: say clearly what the business does, answer the questions people actually ask, and mark the page up so a machine can tell a service from a case study from a question."]),
   ("What the work includes", [
     ["Page structure: one clear subject per page, headings that match what people search for, and a direct answer near the top.",
      "Structured data: the hidden labels that tell search engines and assistants what each part of the page is.",
      "Questions and answers, written to be quoted, with the same text visible on the page.",
      "A plain-text summary of the site for AI assistants.",
      "Technical basics: fast pages, clean addresses, a sitemap, and no blocked crawlers."]]),
   ("Content that keeps working", [
     "A site ranks for what it publishes. The studio's content system turns one idea into a researched article and a week of posts. Every figure is verified against a named source before publication, and each piece is structured to be cited by search engines and AI assistants. It is in weekly use on client work."]),
   ("This site as an example", [
     "This site is built the way the studio builds for clients: structured data for the studio, its services, its work and its questions; a plain-text summary for assistants; fonts and files served from its own address; and one page for each service."]),
  ],
  faq=[
   ("What is the difference between SEO and GEO?",
    "SEO is the practice of making a site rank in search engines. GEO, generative engine optimisation, is the practice of making a site easy for AI assistants such as ChatGPT, Claude and Perplexity to read, understand and cite. GEO builds on SEO: clear structure, direct answers and structured data help with both."),
   ("Is GEO the same as AEO?",
    "The two terms are used for the same idea. AEO stands for answer engine optimisation and GEO for generative engine optimisation. Both mean structuring content so AI systems can quote it."),
   ("Can you guarantee a ranking?",
    "No, and nobody honestly can. What can be done is to remove the reasons a site is overlooked: unclear pages, missing structure and thin content."),
   ("Do you write the content as well?",
    "Yes. Articles, blog posts, newsletters and social posts are produced through the same content system, in your voice, with figures checked against named sources."),
  ],
  related=["websites-and-online-shops", "claude-consulting", "ai-automation"],
 ),
]
