# -*- coding: utf-8 -*-
# How each connection works: one small moving diagram and three steps per tile in the Connections section.
# Same order as CONNECTS in parts.py. Dots travel along the lines with SVG animateMotion.
# (source, hub, destinations, result, three steps)
FLOWS = [
 ("The team asks", "Claude", ["Inbox", "Drive", "CRM"], "Answer from the firm's data",
  ["A connector (MCP) is set up for each tool the firm already uses.",
   "Permissions are chosen per tool, so the assistant only sees what it should.",
   "Anyone on the team asks a question and gets the answer from the source. Anything sent out is approved by a person."]),
 ("A tool with no connector", "API link", ["Claude", "Firm system"], "Connected",
  ["The tool's own API is read and the data the firm needs is mapped.",
   "A small integration is built, tested and documented, owned by the firm.",
   "The tool then works with the assistant and the rest of the firm's systems like any other."]),
 ("Email", "Assistant", ["Calendar", "Draft reply"], "Meeting booked",
  ["Incoming requests are read and sorted.",
   "Free times are checked against the calendar and a reply is drafted.",
   "A person approves, then the reply goes out and the meeting is booked."]),
 ("New approval", "Slack", ["The team", "Alerts"], "Approved in Slack",
  ["Drafts, alerts and daily summaries are posted to the right channel.",
   "The team approves or edits in Slack, where it already talks.",
   "The assistant can be asked questions from inside Slack, within its permissions."]),
 ("Recruiting system", "Sync", ["Website", "Assistant"], "Records current",
  ["Roles and candidates live in one place, such as Loxo or BrightHire.",
   "Open roles appear on the website and CVs are put into the firm's format, without retyping.",
   "The team asks the assistant about its own candidate data."]),
 ("Shopify", "Stock sync", ["Etsy", "Sheet"], "Stock updated",
  ["A sale on one channel is picked up as it happens.",
   "Stock and listings are updated on every other channel and in the sheet.",
   "Nothing is sold twice, and nobody retypes an order."]),
 ("One article", "Publishing", ["Substack", "LinkedIn", "Instagram"], "Scheduled",
  ["One researched piece is written in the firm's voice, every figure checked against a named source.",
   "It is adapted for each channel.",
   "A person approves, then each version is scheduled where it belongs."]),
 ("Database", "Sync", ["Website", "Dashboard"], "Updated from the source",
  ["The figures and records stay in the database the firm already uses.",
   "Website pages and dashboards read from that source.",
   "Nothing is maintained twice, so nothing goes out of date."]),
 ("Booking page", "Bookings", ["Calendar", "Payment", "Reminder"], "Confirmed",
  ["A client picks a time and a place on one screen.",
   "Payment is taken and the calendar is updated.",
   "Confirmations, reminders and changes go out on their own."]),
 ("Invoices", "Follow-up", ["Reminder draft", "Folder"], "Filed and chased",
  ["Quotes and invoices that went quiet are found.",
   "A polite reminder is drafted at each stage and approved by a person before it is sent.",
   "Paid invoices and signed documents are filed in the right place."]),
]

def _t(x, y, s, fill, size=9.5, anchor="middle", weight=500):
    return '<text x="%g" y="%g" font-size="%g" font-weight="%d" fill="%s" text-anchor="%s">%s</text>' % (x, y, size, weight, fill, anchor, s)

def flow_svg(i):
    src, hub, dests, result, _ = FLOWS[i]
    n = len(dests)
    ys = [100] if n == 1 else [100 - 30 * (n - 1) + 60 * k for k in range(n)]
    o = []
    # lines
    o.append('<path d="M92 100 H120" stroke="#CFC9B8" stroke-width="2" fill="none"/>')
    paths = ["M92 100 H160 C 205 100 205 %d 236 %d" % (y, y) for y in ys]
    for y in ys:
        o.append('<path d="M200 100 C 218 100 218 %d 236 %d" stroke="#CFC9B8" stroke-width="2" fill="none"/>' % (y, y))
    # moving dots, under the hub
    for k, pth in enumerate(paths):
        for j in range(2):
            o.append('<circle r="3.6" fill="%s"><animateMotion dur="2.4s" begin="%.2fs" repeatCount="indefinite" path="%s" keyPoints="0;1" keyTimes="0;1" calcMode="linear"/></circle>'
                     % ("#B4743A" if k == 0 else "#2B4C6F", k * .35 + j * 1.2, pth))
    # nodes
    o.append('<rect x="10" y="84" width="82" height="32" rx="8" fill="#F7F5EF" stroke="rgba(27,32,28,.18)" stroke-width="1.2"/>' + _t(51, 103.5, src, "#1B201C", 8.6))
    o.append('<rect x="120" y="80" width="80" height="40" rx="20" fill="#2B4C6F"/>' + _t(160, 103.5, hub, "#F7F5EF", 9.5))
    o.append('<circle cx="160" cy="100" r="26" fill="none" stroke="#2B4C6F" stroke-opacity=".35" stroke-width="1.5"><animate attributeName="r" values="22;34" dur="2.4s" repeatCount="indefinite"/><animate attributeName="stroke-opacity" values=".45;0" dur="2.4s" repeatCount="indefinite"/></circle>')
    for y, d in zip(ys, dests):
        o.append('<rect x="236" y="%g" width="74" height="28" rx="8" fill="#F7F5EF" stroke="rgba(27,32,28,.18)" stroke-width="1.2"/>' % (y - 14) + _t(273, y + 3.5, d, "#1B201C", 8.6))
    # result
    w = max(70, len(result) * 5.6 + 30)
    o.append('<g><rect x="%g" y="166" width="%g" height="22" rx="11" fill="#B4743A"/>%s'
             '<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;.45;.6;1" dur="2.4s" repeatCount="indefinite"/></g>'
             % (160 - w / 2, w, _t(160, 180.5, "✓ " + result, "#F7F5EF", 9)))
    return '<div class="sviz"><svg viewBox="0 0 320 200">%s</svg></div>' % "".join(o)
