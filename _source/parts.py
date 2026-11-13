# -*- coding: utf-8 -*-
AGENTS = [
 ("Responds to enquiries", "at any hour"),
 ("Follows up on unpaid invoices", "on a set schedule"),
 ("Screens every new CV", "before a consultant opens it"),
 ("Confirms bookings", "as they are made"),
 ("Prepares first drafts", "in the firm's voice"),
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
CONNECT_INTRO = ("The method is the same in every firm, whatever the industry. If a tool can share its data, "
                 "it can be connected to the others and to the AI assistant your team already uses.")
CONNECTS = [
 ("moon_mail", "Email and calendar", "the inbox and diary the firm already runs on"),
 ("speech", "Slack", "alerts and approvals where the team already talks"),
 ("cv_read", "Recruiting platforms", "such as Loxo and BrightHire"),
 ("bars", "Spreadsheets and databases", "read and updated in place"),
 ("eye", "AI assistants", "connected to the firm's own data, so the team can question it"),
 ("form", "Websites and forms", "enquiries and bookings passed into your systems"),
 ("pen", "Newsletters and social channels", "email, LinkedIn and Instagram"),
 ("folder_in", "The tools specific to your firm", "connected the same way as the rest"),
]
CONNECT_NOTE = "Nothing is replaced. The tools stay where they are and start working together."
