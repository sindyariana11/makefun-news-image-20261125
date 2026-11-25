#!/usr/bin/env python3
"""THE GLOBAL LEDGER - NI25 Akun 10 - Variant B (spotlight lead + dark grid).
Layout B emphasis: one wide spotlight card for the NATO lead, twin leads
beneath it, dark charcoal grid cards. Same verified pool data as variant A.
"""
from PIL import Image, ImageDraw
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compose_a import (F, PB, AB, AR, W, CHAR, CHAR2, PAPER, CREAM, ORANGE,
                       ORANGE_D, INK, GREY, LINE, REGION_COL, wrap, text, rr,
                       scene, CARDS, BRIEFS)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry_b.png")

def dark_card(d, box, c):
    x0, y0, x1, y1 = box
    num, region, place, head, deck, src, cert, chip, kind = c
    rr(d, box, 6, fill=CHAR, outline=(70, 74, 82), width=1)
    ih = int((y1 - y0) * 0.30)
    scene(d, (x0 + 3, y0 + 3, x1 - 3, y0 + ih), kind, num + 2)
    d.rectangle([x0 + 3, y0 + 3, x0 + 34, y0 + 21], fill=ORANGE)
    d.text((x0 + 8, y0 + 5), str(num), font=F(AB, 12), fill=(255, 255, 255))
    col = REGION_COL[region]
    d.rectangle([x0 + 3, y0 + ih, x1 - 3, y0 + ih + 13], fill=col)
    d.text((x0 + 7, y0 + ih + 1), f"{region} - {place}".upper()[:42], font=F(AB, 9), fill=(255, 255, 255))
    yy = y0 + ih + 16
    yy = text(d, x0 + 7, yy, head, F(AB, 12), CREAM, maxw=x1 - x0 - 14, lh=13, maxlines=2)
    text(d, x0 + 7, yy + 1, deck, F(AR, 8), (206, 210, 216), maxw=x1 - x0 - 14, lh=9, maxlines=3)
    by = y1 - 17
    d.rectangle([x0 + 6, by, x0 + 6 + d.textlength(chip, font=F(AB, 8)) + 10, by + 13], fill=ORANGE)
    d.text((x0 + 11, by + 2), chip, font=F(AB, 8), fill=(30, 20, 10))
    st = f"{src} - {cert}"
    d.text((x1 - 7 - d.textlength(st, font=F(AR, 7)), by + 3), st, font=F(AR, 7), fill=(170, 174, 182))

def big_lead(d, box, c):
    x0, y0, x1, y1 = box
    num, region, place, head, deck, src, cert, chip, kind = c
    rr(d, box, 8, fill=CREAM, outline=ORANGE, width=2)
    scene(d, (x0 + 4, y0 + 4, x0 + 330, y1 - 4), kind, num)
    d.rectangle([x0 + 4, y0 + 4, x0 + 38, y0 + 24], fill=ORANGE)
    d.text((x0 + 10, y0 + 6), str(num), font=F(AB, 13), fill=(255, 255, 255))
    d.rectangle([x0 + 4, y1 - 24, x0 + 330, y1 - 4], fill=REGION_COL[region])
    d.text((x0 + 10, y1 - 20), f"{region} - {place}".upper(), font=F(AB, 11), fill=(255, 255, 255))
    xx = x0 + 348
    d.text((xx, y0 + 10), "LEAD STORY", font=F(AB, 11), fill=ORANGE_D)
    yy = text(d, xx, y0 + 28, head, F(AB, 25), INK, maxw=x1 - xx - 14, lh=27, maxlines=3)
    yy = text(d, xx, yy + 4, deck, F(AR, 14), (52, 55, 60), maxw=x1 - xx - 14, lh=16, maxlines=5)
    by = y1 - 26
    d.rectangle([xx, by, xx + d.textlength(chip, font=F(AB, 10)) + 14, by + 17], fill=CHAR)
    d.text((xx + 7, by + 3), chip, font=F(AB, 10), fill=(255, 210, 170))
    d.text((xx + 190, by + 4), f"{src} - {cert}", font=F(AR, 9), fill=GREY)

def main():
    img = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(img)
    # masthead on cream, charcoal type, orange rule (inverse of A)
    d.rectangle([0, 0, W, 74], fill=CREAM)
    tw = d.textlength("THE GLOBAL LEDGER", font=F(PB, 50))
    d.text(((W - tw) / 2, 10), "THE GLOBAL LEDGER", font=F(PB, 50), fill=CHAR)
    d.rectangle([0, 74, W, 80], fill=ORANGE)
    d.rectangle([0, 80, W, 132], fill=ORANGE)
    tw = d.textlength("TUESDAY 25 NOVEMBER 2026", font=F(PB, 40))
    d.text(((W - tw) / 2, 86), "TUESDAY 25 NOVEMBER 2026", font=F(PB, 40), fill=(255, 255, 255))
    d.rectangle([0, 132, W, 156], fill=CHAR)
    d.text((12, 139), "37 STORIES  -  9 REGIONS  -  EVERY STORY DATED TUESDAY  -  WIRES CHECKED  -  ONE FRONT PAGE", font=F(AB, 12), fill=CREAM)
    # numbers strip as orange-outlined boxes
    nums = [("700,000+", "RUSSIAN DEAD #6"), ("50", "BOEING JETS #10"), ("23", "INJURED #8"), ("12", "CORAL #13"), ("5-1", "MADRID #11"), ("+31.5%", "NVIDIA #36"), ("7", "KILLED GAZA #4"), ("3", "TANKERS #2")]
    cw = W // 8
    for i, (n, lab) in enumerate(nums):
        x = i * cw
        rr(d, (x + 3, 160, x + cw - 3, 192), 5, fill=(255, 255, 255), outline=ORANGE, width=1)
        tw = d.textlength(n, font=F(AB, 15)); d.text((x + (cw - tw) / 2, 162), n, font=F(AB, 15), fill=ORANGE_D)
        tw = d.textlength(lab, font=F(AB, 7)); d.text((x + (cw - tw) / 2, 180), lab, font=F(AB, 7), fill=GREY)
    # region strip
    regs = [("EUROPE", 8), ("MIDDLE EAST", 6), ("AFRICA", 5), ("AMERICAS", 4), ("ASIA", 2), ("SOUTH ASIA", 2), ("ASIA-PACIFIC", 2), ("OCEANIA", 2), ("WORLD", 6)]
    x = 8; d.text((x, 199), "REGIONS:", font=F(AB, 10), fill=CHAR); x += 62
    for name, cnt in regs:
        s = f"{name} {cnt}"; wdt = d.textlength(s, font=F(AB, 9)) + 14
        rr(d, (x, 196, x + wdt, 212), 4, fill=REGION_COL[name])
        d.text((x + 7, 199), s, font=F(AB, 9), fill=(255, 255, 255)); x += wdt + 5
    # timeline
    tl = [("22 NOV", "Iran rationing began"), ("MON CLOSE", "Nvidia +31.5%"), ("TUE 25 NOV", "PCE report due"), ("TODAY", "AWACS plan, Poland"), ("2027", "Punjab alliance vote")]
    cw = W // 5
    for i, (t, s) in enumerate(tl):
        x = i * cw
        if i: d.line([x, 220, x, 238], fill=LINE, width=1)
        d.text((x + 8, 219), t, font=F(AB, 10), fill=ORANGE_D)
        d.text((x + 8, 231), s, font=F(AR, 8), fill=INK)
    # spotlight lead #1, twin leads #3 #4
    big_lead(d, (8, 246, 1016, 416), CARDS[0])
    from compose_a import card
    card(d, (8, 422, 504, 586), CARDS[1], lead=True)
    card(d, (512, 422, 1016, 586), CARDS[2], lead=True)
    # dark grid 10: 5 x 2
    grid = CARDS[3:]
    for i, c in enumerate(grid):
        col, row = i % 5, i // 5
        x0 = 8 + col * 202; y0 = 592 + row * 138
        dark_card(d, (x0, y0, x0 + 194, y0 + 132), c)
    # map + date check compact
    y0 = 874
    rr(d, (8, y0, 560, 928), 6, fill=CHAR)
    d.text((16, y0 + 4), "MAP PINS = CARD NUMBERS: 1 POLAND - 2 HORMUZ - 3 IRAQ - 4 GAZA - 8 COLOMBIA - 10 CHINA - 13 REEF - 18 SENEGAL", font=F(AB, 8), fill=CREAM)
    import random
    rnd = random.Random(7)
    for _ in range(200):
        px, py = rnd.uniform(18, 550), rnd.uniform(y0 + 20, y0 + 48)
        d.ellipse([px, py, px + 2, py + 2], fill=(120, 126, 136))
    for num, px, py in [(1, 300, 30), (3, 360, 40), (4, 370, 46), (2, 378, 42), (10, 455, 36), (8, 96, 44), (13, 495, 48), (18, 302, 50)]:
        ay = y0 + py
        d.ellipse([px - 8, ay - 8, px + 8, ay + 8], fill=ORANGE)
        s = str(num); d.text((px - d.textlength(s, font=F(AB, 8)) / 2, ay - 5), s, font=F(AB, 8), fill=(255, 255, 255))
    rr(d, (568, y0, 1016, 928), 6, fill=(252, 238, 226), outline=ORANGE, width=1)
    d.text((578, y0 + 4), "DATE CHECK - NOT TODAY", font=F(AB, 10), fill=ORANGE_D)
    yy = y0 + 20
    for s in ["Merkury - 23 Nov, excluded", "COP31 wrap - earlier Nov, excluded", "Liverpool 4-0 - earlier, excluded", "GTA VI hype - no release today"]:
        d.text((578, yy), "X  " + s, font=F(AR, 9), fill=INK); yy += 12
    # briefs
    y0 = 934
    d.text((8, y0), "ALSO ON THIS PAGE - BRIEF, NUMBERED", font=F(AB, 9), fill=CHAR)
    cols = [BRIEFS[:8], BRIEFS[8:16], BRIEFS[16:]]
    for ci, colitems in enumerate(cols):
        x = 8 + ci * 340; yy = y0 + 12
        for num, s in colitems:
            yy = text(d, x, yy, f"{num}. {s}", F(AR, 6), (52, 55, 60), maxw=332, lh=7, maxlines=2)
    d.rectangle([0, 1006, W, W], fill=CHAR)
    d.text((10, 1010), "Sources: wire reports, RFE/RL, Al Jazeera, Starlit Daily, DW, Forbes via wires. Claims labelled as claims. Original drawings.", font=F(AR, 8), fill=CREAM)
    img.save(OUT, optimize=True)
    print(OUT, os.path.getsize(OUT))

if __name__ == "__main__":
    main()
