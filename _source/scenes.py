# -*- coding: utf-8 -*-
# Small moving scenes for the Systems section. One per system, in the same order as SYSTEMS in cases.py.
# Each element carries a time (ms) in a six second loop: the script adds the class "on" at that time, and CSS does the motion.
# Kinds: f fade in, u rise in, g grow from the left, gy grow from the bottom, p pop in, d draw a line, x fade out.
B, O, S, I, W = "var(--door)", "var(--ochre)", "var(--sand)", "var(--ink)", "#F7F5EF"
LN = "rgba(27,32,28,.14)"

def a(kind, t): return ' class="a %s" data-t="%d"' % (kind, t)
def R(x, y, w, h, f, rx=3, an="", st=""):
    return '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s"%s%s/>' % (x, y, w, h, rx, f,
        (' stroke="%s" stroke-width="1.2"' % st) if st else "", an)
def T(x, y, s, f=I, an="", size=10, anchor="start", weight=500):
    return '<text x="%g" y="%g" font-size="%g" font-weight="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, weight, f, anchor, an, s)
def C(cx, cy, r, f, an="", st=""):
    return '<circle cx="%g" cy="%g" r="%g" fill="%s"%s%s/>' % (cx, cy, r, f, (' stroke="%s" stroke-width="1.4"' % st) if st else "", an)
def P(d, stroke, an="", w=2):
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%g" stroke-linecap="round" stroke-linejoin="round" pathLength="1"%s/>' % (d, stroke, w, an)
def tick(x, y, c, t): return P("M%g %g l4 4 l8 -9" % (x, y), c, a("d", t), 2.2)
def arrow(x1, y, x2, t): return P("M%g %g H%g m-6 -5 l6 5 l-6 5" % (x1, y, x2), S, a("d", t), 1.8)
def chip(x, y, w, f, s, t, kind="p", tc=W):
    return R(x, y, w, 20, f, 10, a(kind, t)) + T(x + w / 2, y + 13.5, s, tc, a("f", t + 80), 9.5, "middle")

def enquiry():
    o = "".join(R(18, 26 + i * 30, 120, 20, W, 4, "", LN) + C(30, 36 + i * 30, 4, B) + R(40, 33 + i * 30, 72 - i * 9, 6, S) for i in range(4))
    o += R(18, 56, 120, 20, O, 4, a("g", 500)) + T(144, 70, "No reply", O, a("f", 800), 9.5)
    o += R(196, 22, 108, 128, W, 6, a("u", 1400), LN)
    o += "".join(R(208, 38 + i * 16, 84 - i * 14, 6, S, 3, a("g", 1700 + i * 220)) for i in range(4))
    o += chip(208, 118, 74, B, "Approve", 2900)
    o += chip(18, 164, 58, B, "Sent", 3900) + tick(84, 170, B, 4000)
    return o

def candidates():
    ws = [190, 168, 146, 120, 96]
    o = ""
    for i, w in enumerate(ws):
        y = 24 + i * 30
        o += R(18, y, w, 14, O if i == 0 else B, 3, a("g", 300 + i * 220))
        o += R(18, y + 18, w * .55, 4, S, 2, a("g", 1500 + i * 180))
        o += C(262, y + 7, 9, O if i == 0 else W, a("p", 2300 + i * 160), "" if i == 0 else LN)
    return o + T(18, 186, "The recruiter decides", I, a("f", 3600))

def publishing():
    o = R(18, 54, 86, 92, B, 8, a("p", 300)) + R(30, 70, 56, 6, W, 3, a("g", 700)) + R(30, 84, 44, 6, W, 3, a("g", 850))
    o += arrow(116, 100, 156, 1300)
    for j in range(6):
        x, y = 170 + (j % 3) * 46, 46 + (j // 3) * 50
        o += R(x, y, 38, 38, O if j == 0 else W, 6, a("p", 1700 + j * 220), "" if j == 0 else LN)
    return o + T(170, 168, "Sources checked", I, a("f", 3300)) + tick(258, 160, B, 3400)

def report():
    o = "".join(P("M18 %d q12 -8 24 0 t24 0 t24 0 t24 0" % (40 + i * 22), S, a("d", 200 + i * 220), 2) for i in range(5))
    o += arrow(126, 96, 162, 1400)
    o += R(176, 18, 126, 162, W, 6, a("u", 1700), LN) + R(188, 32, 70, 8, I, 3, a("g", 2000))
    for i in range(4):
        y = 56 + i * 26
        o += R(188, y, 60, 6, S, 3, a("g", 2200 + i * 150))
        o += "".join(C(262 + k * 9, y + 3, 3, B if k <= 3 - i % 3 else S, a("p", 2700 + i * 150)) for k in range(4))
    return o + chip(188, 158, 62, O, "Gap flagged", 3700)

def assistant():
    o = R(18, 24, 190, 36, S, 14, a("u", 300)) + T(32, 46, "Which invoices are overdue?", I, a("f", 400), 10)
    o += "".join(C(40 + k * 12, 84, 3.5, S, a("p", 1100 + k * 150)) for k in range(3))
    o += R(96, 72, 206, 62, B, 14, a("u", 1800)) + "".join(R(110, 88 + k * 14, 150 - k * 30, 6, W, 3, a("g", 2100 + k * 200)) for k in range(3))
    return o + chip(96, 146, 124, W, "From: the firm's data", 3200, "p", I).replace('fill="#F7F5EF" ', 'fill="#F7F5EF" stroke="rgba(27,32,28,.2)" ', 1)

def bookings():
    o = ""
    for r in range(3):
        for c in range(5):
            o += R(18 + c * 40, 30 + r * 34, 34, 28, W, 4, "", LN)
    o += R(98, 64, 34, 28, B, 4, a("p", 600)) + chip(222, 34, 82, B, "Confirmed", 1200)
    o += C(116, 60, 9, "none", a("p", 2100), O) + chip(222, 66, 82, W, "Reminder sent", 2200, "p", I).replace('fill="#F7F5EF" ', 'fill="#F7F5EF" stroke="rgba(27,32,28,.2)" ', 1)
    o += R(98, 64, 34, 28, W, 4, a("p", 3200), LN) + R(138, 98, 34, 28, O, 4, a("p", 3300)) + chip(222, 98, 82, O, "Rescheduled", 3400)
    return o

def invoices():
    o = R(18, 20, 104, 156, W, 6, "", LN) + R(30, 34, 50, 8, I, 3) + "".join(R(30, 56 + i * 16, 80 - i * 8, 5, S, 2) for i in range(5))
    o += R(30, 146, 40, 10, O, 3, a("p", 300))
    o += chip(150, 30, 92, B, "Sent", 700) + P("M196 54 v14", S, a("d", 1300), 1.6)
    o += chip(150, 72, 92, O, "Reminder drafted", 1500) + P("M196 96 v14", S, a("d", 2100), 1.6)
    o += chip(150, 114, 92, W, "Approved", 2300, "p", I).replace('fill="#F7F5EF" ', 'fill="#F7F5EF" stroke="rgba(27,32,28,.2)" ', 1) + P("M196 138 v14", S, a("d", 2900), 1.6)
    o += chip(150, 156, 92, B, "Paid", 3200) + tick(252, 162, B, 3400)
    return o + R(30, 146, 40, 10, B, 3, a("p", 3300))

def onboarding():
    o = ""
    for i in range(5):
        y = 22 + i * 28
        o += R(18, y, 18, 18, W, 4, "", LN) + R(46, y + 6, 120 - i * 10, 6, S, 3)
        o += tick(21, y + 7, B, 500 + i * 450)
    return o + chip(190, 70, 112, B, "Everything is in", 3000) + chip(190, 100, 112, O, "Team notified", 3500)

def figures():
    hs = [40, 64, 52, 86, 74, 108]
    o = P("M18 160 H200", LN, "", 1.2)
    o += "".join(R(26 + i * 28, 160 - h, 18, h, B if i < 5 else O, 3, a("gy", 300 + i * 200)) for i, h in enumerate(hs))
    o += P("M35 124 L63 102 L91 112 L119 78 L147 90 L175 56", I, a("d", 1700), 1.6)
    return o + R(214, 60, 92, 54, W, 10, a("u", 2800), LN) + R(226, 74, 60, 6, S, 3, a("g", 3100)) + R(226, 88, 44, 6, S, 3, a("g", 3250)) + T(214, 134, "Sent to the team", I, a("f", 3400))

def orders():
    o = ""
    for k, (x, lab) in enumerate([(18, "Shop"), (170, "Marketplace")]):
        o += R(x, 22, 132, 150, W, 6, "", LN) + T(x + 12, 40, lab, I, "", 10)
        o += "".join(R(x + 12, 54 + i * 24, 108, 16, S if i else B, 3) for i in range(4))
        o += T(x + 12, 160, "Stock 12", I, a("x", 1200 + k * 600), 10) + T(x + 12, 160, "Stock 11", O, a("f", 1300 + k * 600), 10)
    return o + chip(70, 50, 56, O, "Sold", 500) + P("M150 62 H170", O, a("d", 1500), 1.8) + R(182, 54, 108, 16, O, 3, a("g", 1700))

def newsletter():
    pos = [(22, 28), (78, 52), (30, 96), (90, 120)]
    o = "".join(R(x, y, 46, 30, B if i % 2 == 0 else O, 5, a("p", 200 + i * 250)) for i, (x, y) in enumerate(pos))
    o += arrow(148, 96, 178, 1300)
    o += R(190, 20, 112, 156, W, 6, a("u", 1500), LN) + R(202, 34, 60, 8, I, 3, a("g", 1800))
    o += "".join(R(202, 56 + i * 22, 88, 14, B if i % 2 == 0 else O, 3, a("g", 2000 + i * 200)) for i in range(4))
    return o + chip(202, 150, 80, B, "Draft ready", 3200)

def posts():
    o = R(18, 54, 80, 92, O, 8, a("p", 300)) + R(30, 70, 50, 6, W, 3, a("g", 600))
    o += "".join(T(120, 52 + i * 46, s, I, "", 9.5) for i, s in enumerate(["LinkedIn", "Instagram", "Blog"]))
    o += "".join(P("M120 %d H304" % (62 + i * 46), LN, "", 1.2) for i in range(3))
    o += "".join(R(186 + i * 40, 38 + i * 46, 36, 20, B, 5, a("p", 1200 + i * 450)) for i in range(3))
    return o + chip(120, 168, 82, B, "Scheduled", 2900)

def meeting():
    hs = [16, 34, 22, 46, 30, 52, 24, 40, 18, 30]
    o = "".join(R(18 + i * 10, 96 - h / 2, 6, h, S, 3, a("p", 150 + i * 90)) for i, h in enumerate(hs))
    o += arrow(124, 96, 156, 1300)
    for i in range(3):
        y = 46 + i * 36
        o += C(180, y + 8, 9, O if i == 1 else B, a("p", 1600 + i * 300)) + R(196, y + 4, 90 - i * 14, 8, S, 4, a("g", 1700 + i * 300))
        o += tick(288, y + 4, B, 2900 + i * 200)
    return o

def documents():
    o = "".join(R(70 + i * 70, 18, 28, 36, W, 3, a("u", 300 + i * 350), LN) for i in range(3))
    o += "".join(R(70 + i * 70, 18, 28, 36, W, 3, a("x", 1900 + i * 150), LN) for i in range(3))
    o += "".join(P("M%d 64 v40" % (84 + i * 70), S, a("d", 1300 + i * 150), 1.6) for i in range(3))
    o += "".join(R(52 + i * 70, 118, 64, 52, O if i == 1 else B, 6) + R(52 + i * 70, 112, 28, 10, O if i == 1 else B, 3) for i in range(3))
    return o + "".join(R(66 + i * 70, 128, 36, 6, W, 3, a("g", 2200 + i * 300)) for i in range(3))

def website():
    o = R(18, 20, 118, 156, W, 6, "", LN) + R(30, 34, 70, 8, I, 3) + "".join(R(30, 54 + i * 18, 92 - (i % 2) * 20, 6, S, 3) for i in range(6))
    o += "".join(R(30, 54 + i * 36, 4, 6, B, 1, a("p", 300 + i * 200)) for i in range(3))
    o += "".join(R(156, 30 + i * 40, 146, 30, W, 5, a("u", 1200 + i * 250), LN) for i in range(3))
    o += R(156, 70, 146, 30, O, 5, a("g", 2400)) + T(166, 89, "The firm, cited", W, a("f", 2700), 10)
    return o + chip(156, 158, 64, B, "Found", 3200)

SCENES = [enquiry, candidates, publishing, report, assistant, bookings, invoices, onboarding,
          figures, orders, newsletter, posts, meeting, documents, website]
SKILLS_SCENE = 15

def scene(i):
    return '<div class="sviz" aria-hidden="true"><svg viewBox="0 0 320 200">%s</svg></div>' % SCENES[i % len(SCENES)]()

# ── scenes for the Connections cards: the actual screens a connection changes ──
def emailcal():
    o = R(14, 18, 142, 76, W, 8, a("u", 200), LN) + T(26, 36, "New message", S, a("f", 300), 8.5) + T(26, 54, "Can we meet on Tuesday?", I, a("f", 400), 9.5)
    o += R(26, 64, 96, 5, S, 2, a("g", 600)) + R(26, 74, 70, 5, S, 2, a("g", 700))
    for r in range(3):
        for c in range(4):
            o += R(172 + c * 34, 22 + r * 26, 28, 20, W, 4, "", LN)
    o += T(172, 16, "Calendar", S, "", 8.5) + R(206, 48, 28, 20, B, 4, a("p", 1300)) + T(220, 61.5, "Free", W, a("f", 1400), 8.5, "middle")
    o += R(14, 108, 142, 76, W, 8, a("u", 1900), LN) + T(26, 126, "Draft reply", S, a("f", 2000), 8.5) + T(26, 144, "Tuesday at 10:00 works.", I, a("f", 2100), 9.5)
    o += chip(26, 154, 64, B, "Approve", 2900) + tick(98, 160, B, 3100)
    o += R(206, 48, 28, 20, O, 4, a("p", 3600)) + chip(172, 110, 92, O, "Meeting booked", 3700)
    return o

def slack():
    o = R(14, 14, 292, 172, W, 10, "", LN) + T(28, 34, "# approvals", I, "", 10, "start", 600) + P("M14 44 H306", LN, "", 1)
    o += C(34, 66, 9, B, a("p", 200)) + R(50, 58, 120, 6, S, 3, a("g", 300)) + R(50, 70, 86, 6, S, 3, a("g", 400))
    o += C(34, 106, 9, O, a("p", 1000)) + T(50, 102, "Draft reply ready for a new enquiry", I, a("f", 1100), 9.5)
    o += R(50, 110, 200, 30, "#EFEDE5", 6, a("u", 1300)) + R(60, 119, 150, 5, S, 2, a("g", 1500)) + R(60, 129, 110, 5, S, 2, a("g", 1650))
    o += chip(50, 150, 64, B, "Approve", 2000) + chip(122, 150, 48, W, "Edit", 2100, "p", I).replace('fill="#F7F5EF" ', 'fill="#F7F5EF" stroke="rgba(27,32,28,.2)" ', 1)
    o += T(186, 164, "Approved, then sent", B, a("f", 3200), 9.5) + tick(286, 155, B, 3300)
    return o

def recruiting():
    o = R(14, 18, 138, 164, W, 8, "", LN) + T(26, 36, "Recruiting system", I, "", 9.5, "start", 600)
    o += "".join(R(26, 48 + k * 26, 112, 16, S, 3) for k in range(4)) + R(26, 48, 112, 16, O, 3, a("g", 400)) + T(32, 60, "New role", W, a("f", 600), 9)
    o += arrow(152, 96, 172, 1100)
    o += R(178, 18, 128, 92, W, 8, a("u", 1500), LN) + T(190, 36, "Careers page", I, a("f", 1600), 9.5, "start", 600)
    o += R(190, 46, 104, 18, B, 4, a("g", 2000)) + R(190, 70, 80, 6, S, 3, a("g", 2200)) + R(190, 82, 60, 6, S, 3, a("g", 2300))
    o += R(178, 120, 128, 62, W, 8, a("u", 2700), LN) + R(190, 132, 50, 7, I, 3, a("g", 2900)) + R(190, 146, 96, 5, S, 2, a("g", 3000)) + R(190, 156, 80, 5, S, 2, a("g", 3100))
    o += T(190, 175, "CV in the firm's format", B, a("f", 3300), 8.5)
    return o

def api():
    o = R(14, 34, 104, 132, W, 8, "", LN) + T(26, 52, "Their tool", I, "", 9.5, "start", 600)
    o += "".join(R(26, 64 + k * 22, 80, 12, S, 3) for k in range(4))
    o += R(202, 34, 104, 132, W, 8, "", LN) + T(214, 52, "Firm system", I, "", 9.5, "start", 600)
    o += "".join(R(214, 64 + k * 22, 80, 12, "#EFEDE5", 3, "", LN) for k in range(4))
    for k in range(4):
        y = 70 + k * 22
        o += P("M106 %d C 150 %d 158 %d 214 %d" % (y, y, y, y), O if k == 0 else B, a("d", 700 + k * 260), 1.6)
        o += R(214, 64 + k * 22, 80, 12, B if k else O, 3, a("g", 1500 + k * 260))
    return o + chip(110, 176, 100, B, "Connected", 3000) + tick(218, 182, B, 3200)

def skills():
    names = ["Weekly report", "Client proposal", "Candidate summary"]
    o = R(14, 16, 130, 168, W, 8, "", LN) + T(26, 34, "Skills", I, "", 9.5, "start", 600)
    for k, n in enumerate(names):
        y = 44 + k * 36
        o += R(26, y, 106, 28, "#EFEDE5" if k != 1 else W, 6, "", LN) + T(36, y + 18, n, I, "", 8.6)
    o += R(26, 80, 106, 28, B, 6, a("p", 500)) + T(36, 98, "Client proposal", W, a("f", 550), 8.6)
    o += chip(26, 152, 60, O, "Run", 900)
    o += arrow(146, 100, 168, 1300)
    o += R(178, 16, 128, 140, W, 8, a("u", 1500), LN) + R(190, 30, 64, 8, I, 3, a("g", 1800))
    o += "".join(R(190, 48 + k * 14, 100 - (k % 3) * 18, 5, S, 2, a("g", 2000 + k * 120)) for k in range(5))
    o += T(190, 140, "The firm's format", B, a("f", 2700), 8.5)
    o += chip(178, 164, 64, B, "Approve", 3100) + tick(250, 170, B, 3300)
    return o

SCENES.append(skills)
CONN_SCENES = [assistant, api, emailcal, slack, recruiting, orders, posts, figures, bookings, invoices]
def conn_scene(i):
    return '<div class="sviz"><svg viewBox="0 0 320 200">%s</svg></div>' % CONN_SCENES[i % len(CONN_SCENES)]()
