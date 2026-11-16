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
CONNECT_INTRO = ("Most teams use a fraction of what their tools, and an assistant such as Claude, can do together. "
                 "This is what changes once they are connected.")
CONNECTS = [
 ("moon_mail", "Email and calendar", "Replies are drafted and meetings booked without the back and forth."),
 ("speech", "Slack", "Approvals and alerts arrive where the team already talks."),
 ("form", "Shopify and Etsy", "Orders, stock and listings stay in step without retyping."),
 ("pen", "Substack, LinkedIn and Instagram", "One piece of writing is published everywhere it belongs."),
 ("cv_read", "Loxo, BrightHire and the software of your trade", "Records stay current, and nobody copies between systems."),
 ("bars", "Spreadsheets and databases", "Figures update themselves, so reports no longer need preparing."),
 ("eye", "Claude", "Anyone on the team can ask a question and get the answer from your own data."),
 ("folder_in", "Anything else you rely on", "If it can share its data, it joins the rest."),
]
CONNECT_NOTE = "Nothing is replaced. The tools stay where they are and start working together."
