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
CONNECT_INTRO = ("The method is the same in every business, whatever the trade. If a tool can share its data, "
                 "it can be connected to the others and to an AI assistant. Most teams use a fraction of what an assistant such as Claude can do. Setting that up properly is a large part of the work.")
CONNECTS = [
 ("moon_mail", "Email and calendar", "the inbox and diary you already run on"),
 ("speech", "Slack", "alerts and approvals where the team already talks"),
 ("cv_read", "Software of your trade", "booking, sales and recruiting platforms, such as Loxo and BrightHire"),
 ("bars", "Spreadsheets and databases", "read and updated in place"),
 ("eye", "Claude and other AI assistants", "connected to your own data and set up for the whole team"),
 ("form", "Websites and online shops", "Shopify, Etsy, and the forms and bookings on your own site"),
 ("pen", "Newsletters and social channels", "Substack, email, LinkedIn and Instagram"),
 ("folder_in", "The tools specific to your business", "connected the same way as the rest"),
]
CONNECT_NOTE = "Nothing is replaced. The tools stay where they are and start working together."
