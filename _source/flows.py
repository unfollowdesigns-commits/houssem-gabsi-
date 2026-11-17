# -*- coding: utf-8 -*-
# How each connection works: one small moving diagram and three steps per tile in the Connections section.
# Same order as CONNECTS in parts.py. Dots travel along the lines with SVG animateMotion.
# (source, hub, destinations, result, three steps)
FLOWS = [
 ("The team asks", "Claude", ["Inbox", "Drive", "CRM"], "Answer from the firm's data",
  ["A connector (MCP) goes in for each tool the team already uses.",
   "Each one gets its own permissions, so the assistant sees the calendar but not, say, payroll.",
   "Then anyone can ask it a question and get an answer pulled from the real data. If it drafts something for a client, a person sends it."]),
 ("A tool with no connector", "API link", ["Claude", "Firm system"], "Connected",
  ["First, a look at what the tool's API offers and which fields actually matter.",
   "Then a small integration, tested and written up. The firm owns the code.",
   "After that, the odd tool out behaves like everything else."]),
 ("Email", "Assistant", ["Calendar", "Draft reply"], "Meeting booked",
  ["A meeting request comes in.",
   "The calendar is checked and a reply is drafted with a time that works.",
   "One click to approve, and the reply and the invite both go out."]),
 ("New approval", "Slack", ["The team", "Alerts"], "Approved in Slack",
  ["Drafts and alerts show up in the channel the team already reads.",
   "Approve, edit or leave it, without opening another app.",
   "And the assistant can be asked things right there in Slack."]),
 ("Recruiting system", "Sync", ["Website", "Assistant"], "Records current",
  ["Roles and candidates stay where they live, in Loxo or BrightHire.",
   "Open roles show up on the website, and CVs come out in the firm's format.",
   "The team can ask the assistant about its own candidates."]),
 ("Shopify", "Stock sync", ["Etsy", "Sheet"], "Stock updated",
  ["An order comes in on one channel.",
   "Stock drops everywhere else, including the spreadsheet.",
   "The last one can't be sold twice."]),
 ("One article", "Publishing", ["Substack", "LinkedIn", "Instagram"], "Scheduled",
  ["One piece gets written and researched, every figure traced to a source.",
   "It's cut down and reshaped for each channel.",
   "Someone reads it over, and each version is scheduled."]),
 ("Database", "Sync", ["Website", "Dashboard"], "Updated from the source",
  ["The numbers stay in the database they already live in.",
   "The website and the dashboard read straight from it.",
   "Update it once and every page catches up."]),
 ("Booking page", "Bookings", ["Calendar", "Payment", "Reminder"], "Confirmed",
  ["A client picks a time on one screen.",
   "They pay, and the calendar updates.",
   "Confirmation now, reminder the day before, no messages to answer."]),
 ("Invoices", "Follow-up", ["Reminder draft", "Folder"], "Filed and chased",
  ["Quotes and invoices that went quiet get flagged.",
   "A polite reminder is drafted and waits for someone to say yes.",
   "Once it's paid or signed, it's filed where it belongs."]),
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
