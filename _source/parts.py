# -*- coding: utf-8 -*-
AGENTS = [
 ("Responds to enquiries", "at any hour"),
 ("Follows up on unpaid invoices", "on a set schedule"),
 ("Screens every application", "before anyone opens it"),
 ("Confirms bookings", "as they are made"),
 ("Prepares first drafts", "in your voice"),
 ("Publishes on schedule", "every week"),
 ("Sends the weekly figures", "to the people who need them"),
 ("Files documents", "in the right place, every time"),
]
# illustrative day for the capacity animation: hours at which each process above acts
DAY_HOURS = [[1,6,11,15,22],[9],[8,13,19],[7,12,17,21],[10,16],[8],[7],[9,11,14,18,23]]
FLOW_TRIGGER = "A client submits your enquiry form"
FLOW_STEPS = ["Read and categorised", "Recorded in your system", "Reply drafted in your voice", "Added to the weekly report"]
FLOW_END = "Ready for your approval"
NUMBERS = []

# what the systems connect to: (icon, name, detail)
CONNECT_LABEL = "Connections"
CONNECT_HEAD = "Any tool the firm already uses can be connected."
CONNECT_INTRO = ("Claude reaches a firm's tools through connectors, known as MCP. Where a connector exists, it is set up and tested. "
                 "Where none exists, the integration is built against the tool's own API.")
CONNECTS = [
 ("eye", "Any Claude connector (MCP)", "The team's assistant reads and acts on the firm's own data, not on what someone pastes in."),
 ("folder_in", "Custom API integrations", "A tool with no ready connector gets one built for it, so it joins the rest."),
 ("moon_mail", "Email and calendar", "Replies are drafted and meetings booked without the back and forth."),
 ("speech", "Slack", "Approvals and alerts arrive where the team already talks."),
 ("cv_read", "Loxo, BrightHire and trade software", "Records stay current, and nobody copies between systems."),
 ("form", "Shopify and Etsy", "Orders, stock and listings stay in step without retyping."),
 ("pen", "Substack, LinkedIn and Instagram", "One piece of writing is published everywhere it belongs."),
 ("bars", "Websites, spreadsheets and databases", "Pages and figures update from the source, so nothing is maintained twice."),
 ("calendar_tick", "Bookings and payments", "Schedule, places and payment sit on one screen, not in a message thread."),
 ("invoice", "Quotes, invoices and documents", "What went quiet is found and followed up, and files land in the right place."),
]
CONNECT_NOTE = "Nothing is replaced. The tools stay where they are and start working together."
