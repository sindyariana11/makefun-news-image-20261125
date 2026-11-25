#!/usr/bin/env python3
"""THE GLOBAL LEDGER - NI25 Akun 10 - Variant A (horizontal lead trio)."""
from PIL import Image, ImageDraw, ImageFont
import os

FD = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry_a.png")

def F(name, size):
    return ImageFont.truetype(FD + name, size)
PB = "PlayfairDisplay-Black.ttf"; PBD = "PlayfairDisplay-Bold.ttf"
AR = "Archivo.ttf"; AB = "Archivo-Bold.ttf"

W = 1024
CHAR = (35, 38, 44); CHAR2 = (48, 52, 60); PAPER = (243, 240, 233)
CREAM = (250, 247, 240); ORANGE = (255, 106, 26); ORANGE_D = (204, 74, 8)
INK = (24, 26, 30); GREY = (96, 101, 110); LINE = (190, 186, 176)
REGION_COL = {
    "EUROPE": (38, 92, 145), "MIDDLE EAST": (204, 74, 8), "AFRICA": (146, 96, 22),
    "AMERICAS": (34, 122, 84), "ASIA": (172, 44, 62), "SOUTH ASIA": (110, 66, 160),
    "ASIA-PACIFIC": (0, 128, 140), "OCEANIA": (44, 140, 160), "WORLD": (84, 88, 98),
}

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def text(d, x, y, s, font, fill, maxw=None, lh=None, maxlines=None):
    lines = wrap(d, s, font, maxw) if maxw else [s]
    if maxlines: lines = lines[:maxlines]
    for i, ln in enumerate(lines):
        d.text((x, y + i * (lh or font.size + 2)), ln, font=font, fill=fill)
    return y + len(lines) * (lh or font.size + 2)

def rr(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

# ---------- flat layered scenes ----------
def scene(d, box, kind, seed):
    x0, y0, x1, y1 = box; w = x1 - x0; h = y1 - y0
    skies = [(70, 92, 118), (96, 84, 74), (58, 74, 92), (110, 96, 70), (44, 96, 110), (80, 70, 96)]
    sky = skies[seed % len(skies)]
    d.rectangle(box, fill=sky)
    d.ellipse([x0 + w*0.78, y0 + h*0.08, x0 + w*0.92, y0 + h*0.30], fill=(245, 214, 130))
    for i in range(3):
        d.rectangle([x0, y0 + h*(0.62 + i*0.12), x1, y0 + h*(0.68 + i*0.12)], fill=(sky[0]+18+i*6, sky[1]+14+i*5, sky[2]+8))
    cx, cy = x0 + w*0.5, y0 + h*0.42
    if kind == "awacs":
        d.ellipse([cx-52, cy-16, cx+52, cy+2], fill=(232, 234, 238))
        d.polygon([(cx+40, cy-8), (cx+72, cy+2), (cx+40, cy+2)], fill=(200, 204, 210))
        d.polygon([(cx-44, cy-10), (cx-64, cy-22), (cx-58, cy-4)], fill=(200, 204, 210))
        d.ellipse([cx-16, cy-30, cx+16, cy-14], fill=ORANGE)
        d.line([cx-70, cy+14, cx+70, cy+14], fill=(240, 240, 240), width=2)
    elif kind == "oil":
        for i, ox in enumerate([0.22, 0.5, 0.78]):
            px = x0 + w*ox
            d.polygon([(px-16, y0+h*0.66), (px, y0+h*0.14), (px+16, y0+h*0.66)], outline=(20, 20, 22), width=3)
            d.line([px-10, y0+h*0.48, px+10, y0+h*0.48], fill=(20, 20, 22), width=2)
            d.line([px, y0+h*0.14, px, y0+h*0.66], fill=(20, 20, 22), width=2)
        d.ellipse([x0+w*0.06, y0+h*0.70, x0+w*0.20, y0+h*0.80], fill=ORANGE)
    elif kind == "drone":
        for i, bx in enumerate([0.08, 0.30, 0.58, 0.80]):
            bh = [0.34, 0.46, 0.30, 0.42][i]
            d.rectangle([x0+w*bx, y0+h*(0.68-bh), x0+w*(bx+0.17), y0+h*0.68], fill=(52, 54, 60))
            for r_ in range(3):
                d.rectangle([x0+w*(bx+0.03), y0+h*(0.68-bh+0.05+r_*0.09), x0+w*(bx+0.07), y0+h*(0.68-bh+0.09+r_*0.09)], fill=(250, 214, 130))
        d.polygon([(cx-26, cy-18), (cx+26, cy-18), (cx+12, cy-6), (cx-12, cy-6)], fill=(18, 18, 20))
        for dx in (-30, 30):
            d.ellipse([cx+dx-9, cy-26, cx+dx+9, cy-14], outline=(240, 240, 240), width=2)
    elif kind == "ship":
        d.polygon([(x0+w*0.18, y0+h*0.58), (x0+w*0.82, y0+h*0.58), (x0+w*0.72, y0+h*0.74), (x0+w*0.28, y0+h*0.74)], fill=(30, 34, 40))
        d.rectangle([x0+w*0.36, y0+h*0.40, x0+w*0.62, y0+h*0.58], fill=(210, 120, 50))
        d.rectangle([x0+w*0.42, y0+h*0.28, x0+w*0.56, y0+h*0.40], fill=(226, 228, 232))
        for i in range(4):
            d.arc([x0+w*(0.08+i*0.22), y0+h*0.78, x0+w*(0.26+i*0.22), y0+h*0.94], 0, 180, fill=(220, 235, 245), width=2)
        d.ellipse([x0+w*0.84, y0+h*0.62, x0+w*0.94, y0+h*0.76], fill=ORANGE)
    elif kind == "field":
        for i in range(6):
            px = x0 + w*(0.10 + i*0.16)
            d.line([px, y0+h*0.30, px, y0+h*0.58], fill=(238, 238, 238), width=3)
            d.line([px-7, y0+h*0.36, px+7, y0+h*0.36], fill=(238, 238, 238), width=3)
    elif kind == "flags":
        for i, col in enumerate([(58, 110, 180), (240, 200, 60), (200, 60, 60), (60, 160, 90), (240, 240, 240)]):
            px = x0 + w*(0.14 + i*0.18)
            d.line([px, y0+h*0.16, px, y0+h*0.66], fill=(230, 230, 230), width=2)
            d.rectangle([px, y0+h*0.16, px+w*0.11, y0+h*0.30], fill=col)
    elif kind == "jet":
        d.polygon([(cx-64, cy+4), (cx+30, cy-12), (cx+66, cy-4), (cx+24, cy+6), (cx-40, cy+14)], fill=(236, 238, 242))
        d.polygon([(cx-30, cy+2), (cx-52, cy-18), (cx-38, cy+10)], fill=(190, 196, 205))
        d.rectangle([cx-8, cy-16, cx+14, cy-6], fill=(70, 120, 180))
        for i in range(3):
            d.line([x0+w*0.08, y0+h*(0.70+i*0.08), x0+w*0.5, y0+h*(0.70+i*0.08)], fill=(220, 230, 240), width=2)
    elif kind == "car":
        d.rounded_rectangle([cx-56, cy-8, cx+56, cy+16], radius=8, fill=(196, 60, 44))
        d.polygon([(cx-30, cy-8), (cx-14, cy-24), (cx+26, cy-24), (cx+40, cy-8)], fill=(160, 46, 34))
        for dx in (-34, 34):
            d.ellipse([cx+dx-11, cy+8, cx+dx+11, cy+28], fill=(18, 18, 20))
        for a in range(0, 360, 45):
            import math
            ex, ey = cx+78+16*math.cos(math.radians(a)), cy-20+16*math.sin(math.radians(a))
            d.line([cx+78, cy-20, ex, ey], fill=(250, 200, 70), width=3)
    elif kind == "coral":
        d.rectangle(box, fill=(26, 92, 116))
        for i, col in enumerate([(255, 120, 90), (255, 170, 80), (240, 110, 160), (120, 220, 190)]):
            px = x0 + w*(0.14 + i*0.22)
            d.line([px, y0+h*0.86, px, y0+h*0.44], fill=col, width=5)
            d.line([px, y0+h*0.60, px-14, y0+h*0.46], fill=col, width=4)
            d.line([px, y0+h*0.56, px+14, y0+h*0.40], fill=col, width=4)
        for i in range(5):
            d.ellipse([x0+w*(0.1+i*0.18), y0+h*0.12, x0+w*(0.15+i*0.18), y0+h*0.20], outline=(220, 245, 250), width=2)
    elif kind == "ball":
        d.ellipse([cx-26, cy-26, cx+26, cy+26], fill=(245, 245, 245))
        d.polygon([(cx-8, cy-12), (cx+10, cy-12), (cx+16, cy+4), (cx, cy+14), (cx-16, cy+4)], fill=(24, 24, 26))
        d.arc([x0+w*0.06, y0+h*0.60, x0+w*0.94, y0+h*0.98], 180, 360, fill=(240, 240, 240), width=3)
    elif kind == "chip":
        d.rounded_rectangle([cx-34, cy-30, cx+34, cy+30], radius=6, fill=(28, 30, 36), outline=ORANGE, width=3)
        for i in range(5):
            d.line([cx-44, cy-22+i*12, cx-34, cy-22+i*12], fill=ORANGE, width=3)
            d.line([cx+34, cy-22+i*12, cx+44, cy-22+i*12], fill=ORANGE, width=3)
        pts = [(cx-24, cy+14), (cx-8, cy-2), (cx+6, cy+6), (cx+24, cy-16)]
        d.line(pts, fill=(90, 230, 140), width=3)
    elif kind == "doc":
        d.rectangle([cx-30, cy-36, cx+30, cy+36], fill=(246, 246, 242))
        for i in range(5):
            d.line([cx-20, cy-22+i*11, cx+20, cy-22+i*11], fill=(120, 124, 132), width=3)
        d.ellipse([cx+16, cy+16, cx+38, cy+38], outline=ORANGE_D, width=3)
    elif kind == "trophy":
        d.polygon([(cx-18, cy-30), (cx+18, cy-30), (cx+14, cy+2), (cx-14, cy+2)], fill=(245, 198, 70))
        d.arc([cx-34, cy-28, cx-12, cy+2], 270, 90, fill=(245, 198, 70), width=4)
        d.arc([cx+12, cy-28, cx+34, cy+2], 90, 270, fill=(245, 198, 70), width=4)
        d.rectangle([cx-5, cy+2, cx+5, cy+18], fill=(220, 170, 50))
        d.rectangle([cx-18, cy+18, cx+18, cy+26], fill=(160, 120, 40))
    else:
        d.ellipse([cx-30, cy-20, cx+30, cy+20], fill=ORANGE)

CARDS = [
    (1, "EUROPE", "Poland", "NATO sends early-warning jets to Poland", "NATO plans AWACS deployment in Poland after Russian missiles landed in Poland during an attack on Ukraine. Chancellor Merz vows complete support.", "Wires", "REPORTED", "AWACS TO POLAND", "awacs"),
    (3, "MIDDLE EAST", "Iraq", "Baghdad orders Kurdish oilfields seized", "PM Ali al-Zaidi directs federal units to seize oilfields and crossings in Kurdish-run regions. President Barzani: Kurdistan will not submit.", "Starlit", "REPORTED", "OILFIELDS ORDER", "oil"),
    (4, "MIDDLE EAST", "Gaza", "Drone strikes kill Hamas security chief", "Israeli drone strikes across Gaza killed a senior Hamas security official, three policemen and three siblings, one a child: 7 killed in all.", "Al Jazeera", "REPORTED", "7 KILLED IN STRIKES", "drone"),
    (2, "MIDDLE EAST", "Strait of Hormuz", "Iran says 3 tankers hit by mines", "IRGC Navy claims three oil tankers were hit by naval mines in the Strait of Hormuz. Shipping concerns rise. A claim, not confirmed.", "Iran claim", "CLAIMED", "3 TANKERS HIT", "ship"),
    (6, "WORLD", "Ukraine war data", "700,000 Russian dead, new count finds", "New analysis finds more than 700,000 Russian soldiers killed in the nearly five-year war on Ukraine.", "RFE/RL", "REPORTED", "700,000+ KILLED", "field"),
    (5, "EUROPE", "Brussels", "EU unveils new Russia sanctions", "The European Union announced further restrictive measures against Russia amid the war in Ukraine.", "Wires", "REPORTED", "EU SANCTIONS", "flags"),
    (10, "ASIA", "China", "Xiamen Airlines orders 50 Boeing jets", "Xiamen Airlines, a China Southern unit, agreed to acquire 50 Boeing 737-8 jets.", "Wires", "REPORTED", "50 JETS ORDERED", "jet"),
    (8, "AMERICAS", "Colombia", "Car bomb injures at least 23", "A car bomb in Colombia injured at least 23 people. In Cartagena, gunmen hold dozens hostage in a supermarket.", "Wires", "REPORTED", "23 INJURED", "car"),
    (13, "OCEANIA", "Australia", "12 coral species brought back", "Great Barrier Reef genetic analysis resurrects 12 Acropora coral species. Reef diversity is wider than known.", "Science", "REPORTED", "12 SPECIES BACK", "coral"),
    (11, "EUROPE", "Madrid", "Madrid rout PSV 5-1 in comeback", "Real Madrid overturned a deficit to beat PSV Eindhoven 5-1. Bellingham stunner and an Mbappe brace.", "Wires", "REPORTED", "MADRID 5-1 PSV", "ball"),
    (36, "WORLD", "Nvidia - MONDAY CLOSE", "Nvidia's $1 trillion Monday", "Monday close: Nvidia shares +31.5%, nearly $1 trillion of market value clawed back as Jensen Huang was reinstated as CEO, +$34 billion in a day (Forbes).", "Forbes", "REPORTED", "+31.5% MONDAY", "chip"),
    (33, "WORLD", "Washington", "PCE inflation report due today", "The US PCE inflation report is due Tuesday 25 November. Markets watch for the Fed's next signal. No figure published yet.", "Scheduled", "SCHEDULED", "PCE DUE TODAY", "doc"),
    (18, "AFRICA", "Senegal", "Senegal's AFCON title restored", "CAS ruling gives Senegal its 2025 Africa Cup of Nations title back.", "Wires", "REPORTED", "TITLE RESTORED", "trophy"),
]
BRIEFS = [
    (7, "First German Lynx KF41 fighting vehicles enter Ukrainian service - 5 Lynx IFVs"),
    (9, "Gunmen hold dozens hostage in a Cartagena supermarket"),
    (12, "England beat Australia by 8 wickets, chasing 185, T20I series 1-1 - Fraser-McGurk 27 off 13"),
    (14, "Fiji declares nationwide disaster amid an El Nino dry spell"),
    (15, "Iran pharmacies run dry: medicine shortage shuts pharmacies, hospitals halted"),
    (16, "Iran braces for winter gas shortages - electricity rationing began 22 Nov"),
    (17, "Britain sanctions Houthi leaders and four top Yemeni rebel officials"),
    (19, "Rebels pull back from DR Congo areas after clashes"),
    (20, "Nigerian emir suspended after a sexual assault allegation"),
    (21, "Sudan RSF commander defects in Sudan conflict"),
    (22, "Cameroon separatist leader in a Norway court on war crimes charges"),
    (23, "Punjab: BJP and Shiromani Akali Dal reunite for 2027 - alliance again"),
    (24, "Bangladesh opens an Invest Bangladesh office in Guangzhou, China"),
    (25, "Indonesia's vice-president resigns amid political strain"),
    (26, "Solomon Islands eye Australia treaty to replace China defence pact"),
    (27, "North Korea touts China ties as top diplomat visits embassy in Pyongyang"),
    (28, "Denmark court upholds ghetto evictions law at Supreme Court in Copenhagen"),
    (29, "Sarkozy headed for Libya-case trial in Paris"),
    (30, "Black Sea clash at the UN over shipping and energy attacks"),
    (31, "Shortwave school returns for Afghan girls excluded from school"),
    (32, "Asteroid eclipse: Dimorphos shadow crosses Didymos, beamed from deep space"),
    (34, "US targets 7 firms over chip diversion - one owned by Alibaba"),
    (35, "Decoy army: Moscow buys inflatable decoys from China"),
    (37, "Storms target Thanksgiving travel on both US coasts"),
]

def card(d, box, c, lead=False):
    x0, y0, x1, y1 = box
    num, region, place, head, deck, src, cert, chip, kind = c
    rr(d, box, 6, fill=CREAM, outline=LINE, width=1)
    ih = int((y1 - y0) * (0.42 if lead else 0.30))
    scene(d, (x0 + 3, y0 + 3, x1 - 3, y0 + ih), kind, num)
    d.rectangle([x0 + 3, y0 + 3, x0 + 34, y0 + 21], fill=ORANGE)
    d.text((x0 + 8, y0 + 5), str(num), font=F(AB, 12), fill=(255, 255, 255))
    col = REGION_COL[region]
    d.rectangle([x0 + 3, y0 + ih, x1 - 3, y0 + ih + 13], fill=col)
    d.text((x0 + 7, y0 + ih + 1), f"{region} - {place}".upper()[:42], font=F(AB, 9 if not lead else 10), fill=(255, 255, 255))
    yy = y0 + ih + 16
    yy = text(d, x0 + 7, yy, head, F(AB, 16 if lead else 12), INK, maxw=x1 - x0 - 14, lh=17 if lead else 13, maxlines=2)
    yy = text(d, x0 + 7, yy + 1, deck, F(AR, 11 if lead else 8), (52, 55, 60), maxw=x1 - x0 - 14, lh=12 if lead else 9, maxlines=4 if lead else 3)
    by = y1 - 17
    d.rectangle([x0 + 6, by, x0 + 6 + d.textlength(chip, font=F(AB, 8)) + 10, by + 13], fill=CHAR)
    d.text((x0 + 11, by + 2), chip, font=F(AB, 8), fill=(255, 210, 170))
    st = f"{src} - {cert}"
    d.text((x1 - 7 - d.textlength(st, font=F(AR, 7)), by + 3), st, font=F(AR, 7), fill=GREY)

def main():
    img = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(img)
    # kicker
    d.rectangle([0, 0, W, 26], fill=ORANGE)
    d.text((12, 6), "37 STORIES  -  9 REGIONS  -  EVERY STORY DATED TUESDAY  -  WIRES CHECKED", font=F(AB, 13), fill=(255, 255, 255))
    d.text((W - 12 - d.textlength("ONE FRONT PAGE", font=F(AB, 13)), 6), "ONE FRONT PAGE", font=F(AB, 13), fill=(255, 255, 255))
    # masthead
    d.rectangle([0, 26, W, 104], fill=CHAR)
    tw = d.textlength("THE GLOBAL LEDGER", font=F(PB, 56))
    d.text(((W - tw) / 2, 38), "THE GLOBAL LEDGER", font=F(PB, 56), fill=CREAM)
    d.text((12, 30), "EST. TODAY", font=F(AB, 9), fill=(200, 204, 210))
    d.text((W - 92, 30), "No. 25-11", font=F(AB, 9), fill=(200, 204, 210))
    # giant date
    d.rectangle([0, 104, W, 158], fill=CHAR2)
    tw = d.textlength("TUESDAY 25 NOVEMBER 2026", font=F(PB, 42))
    d.text(((W - tw) / 2, 110), "TUESDAY 25 NOVEMBER 2026", font=F(PB, 42), fill=ORANGE)
    # numbers strip
    nums = [("700,000+", "RUSSIAN DEAD #6"), ("50", "BOEING JETS #10"), ("23", "INJURED, COLOMBIA #8"), ("12", "CORAL SPECIES #13"), ("5-1", "MADRID v PSV #11"), ("+31.5%", "NVIDIA MON #36"), ("7", "KILLED, GAZA #4"), ("3", "TANKERS, IRAN SAYS #2")]
    d.rectangle([0, 158, W, 192], fill=(232, 228, 218))
    cw = W // 8
    for i, (n, lab) in enumerate(nums):
        x = i * cw
        if i: d.line([x, 162, x, 188], fill=LINE, width=1)
        tw = d.textlength(n, font=F(AB, 16)); d.text((x + (cw - tw) / 2, 160), n, font=F(AB, 16), fill=ORANGE_D)
        tw = d.textlength(lab, font=F(AB, 7)); d.text((x + (cw - tw) / 2, 180), lab, font=F(AB, 7), fill=GREY)
    # region strip
    regs = [("EUROPE", 8), ("MIDDLE EAST", 6), ("AFRICA", 5), ("AMERICAS", 4), ("ASIA", 2), ("SOUTH ASIA", 2), ("ASIA-PACIFIC", 2), ("OCEANIA", 2), ("WORLD", 6)]
    d.rectangle([0, 192, W, 216], fill=CHAR)
    x = 8
    d.text((x, 199), "REGIONS:", font=F(AB, 10), fill=CREAM); x += 62
    for name, cnt in regs:
        s = f"{name} {cnt}"
        wdt = d.textlength(s, font=F(AB, 9)) + 14
        rr(d, (x, 196, x + wdt, 212), 4, fill=REGION_COL[name])
        d.text((x + 7, 199), s, font=F(AB, 9), fill=(255, 255, 255)); x += wdt + 5
    # timeline
    d.rectangle([0, 216, W, 242], fill=(250, 247, 240))
    tl = [("22 NOV", "Iran rationing began"), ("MON CLOSE", "Nvidia +31.5%"), ("TUE 25 NOV", "PCE report due"), ("TODAY", "AWACS plan for Poland"), ("2027", "Punjab alliance vote")]
    cw = W // 5
    for i, (t, s) in enumerate(tl):
        x = i * cw
        if i: d.line([x, 220, x, 238], fill=LINE, width=1)
        d.text((x + 8, 219), t, font=F(AB, 10), fill=ORANGE_D)
        d.text((x + 8, 231), s, font=F(AR, 8), fill=INK)
    # lead trio
    leads = CARDS[:3]
    for i, c in enumerate(leads):
        x0 = 8 + i * 338
        card(d, (x0, 248, x0 + 330, 500), c, lead=True)
    # grid 10: 5 x 2
    grid = CARDS[3:]
    for i, c in enumerate(grid):
        col, row = i % 5, i // 5
        x0 = 8 + col * 202; y0 = 506 + row * 168
        card(d, (x0, y0, x0 + 194, y0 + 162), c)
    # map + date check
    y0 = 848
    rr(d, (8, y0, 560, 918), 6, fill=CHAR, outline=None)
    d.text((16, y0 + 4), "THE DAY ON THE MAP - PINS = CARD NUMBERS", font=F(AB, 9), fill=CREAM)
    import random
    rnd = random.Random(25)
    for _ in range(260):
        px, py = rnd.uniform(18, 550), rnd.uniform(y0 + 22, y0 + 62)
        d.ellipse([px, py, px + 2, py + 2], fill=(120, 126, 136))
    pins = [(1, 300, 28), (3, 356, 38), (4, 366, 44), (2, 372, 40), (6, 330, 26), (5, 292, 30), (10, 452, 36), (8, 96, 48), (13, 492, 58), (11, 282, 36), (36, 110, 30), (33, 118, 28), (18, 300, 52)]
    for num, px, py in pins:
        ay = y0 + py
        d.ellipse([px - 8, ay - 8, px + 8, ay + 8], fill=ORANGE)
        s = str(num); d.text((px - d.textlength(s, font=F(AB, 8)) / 2, ay - 5), s, font=F(AB, 8), fill=(255, 255, 255))
    d.text((16, y0 + 64), "EUROPE 1 5 11 - MIDEAST 2 3 4 - ASIA 10 - AMERICAS 8 - OCEANIA 13 - WORLD 6 33 36 - AFRICA 18", font=F(AB, 7), fill=(200, 204, 210))
    rr(d, (568, y0, 1016, 918), 6, fill=(252, 238, 226), outline=ORANGE, width=1)
    d.text((578, y0 + 4), "DATE CHECK - NOT TODAY'S NEWS", font=F(AB, 10), fill=ORANGE_D)
    dc = ["Merkury mission story - dated 23 Nov, excluded", "COP31 summit wrap - earlier November, excluded", "Liverpool 4-0 result - earlier round, excluded", "GTA VI launch hype - no release today, excluded"]
    yy = y0 + 20
    for s in dc:
        yy = text(d, 578, yy, "X  " + s, F(AR, 9), INK, maxw=428, lh=11, maxlines=1) + 2
    # also on briefs
    y0 = 924
    d.text((8, y0), "ALSO ON THIS PAGE - BRIEF, NUMBERED", font=F(AB, 10), fill=CHAR)
    cols = [BRIEFS[:8], BRIEFS[8:16], BRIEFS[16:]]
    for ci, colitems in enumerate(cols):
        x = 8 + ci * 340; yy = y0 + 14
        for num, s in colitems:
            yy = text(d, x, yy, f"{num}. {s}", F(AR, 7), (52, 55, 60), maxw=332, lh=8, maxlines=2)
    # footer
    d.rectangle([0, 1006, W, W], fill=CHAR)
    d.text((10, 1010), "Sources: wire reports, RFE/RL, Al Jazeera, Starlit Daily, DW, Forbes via wires. Claims labelled as claims. Original drawings.", font=F(AR, 8), fill=CREAM)
    img.save(OUT, optimize=True)
    print(OUT, os.path.getsize(OUT))

if __name__ == "__main__":
    main()
