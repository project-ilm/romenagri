# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Every script in the Unicode character database, with what its characters' own names and directions say about it.
Nothing here is a linguist's classification: each column is read from the data, so it can be checked.
    python3 v7/tools/inventory.py v7/inventory/unicode_scripts.csv      (needs fontTools for the Script property)"""
import csv, sys, unicodedata as u
from collections import defaultdict
from fontTools import unicodedata as fu, version as ftv
DONE_V6 = {"Deva": "pivot", "Beng": "v6", "Guru": "v6", "Gujr": "v6", "Orya": "v6", "Taml": "v6", "Telu": "v6", "Knda": "v6",
           "Mlym": "v6", "Sinh": "v6", "Brah": "v6", "Kthi": "v6", "Gran": "v6", "Shrd": "v6", "Modi": "v6", "Tirh": "v6",
           "Sidd": "v6", "Newa": "v6", "Arab": "v6 (Urdu)"}
S = defaultdict(lambda: defaultdict(int)); names = defaultdict(set)
for cp in range(0x110000):
    c = chr(cp)
    if u.category(c) == "Cn":
        continue
    sc = fu.script(c)
    if sc in ("Zyyy", "Zinh", "Zzzz"):
        continue
    s = S[sc]; cat = u.category(c); nm = u.name(c, "")
    s["chars"] += 1; s["letters"] += cat.startswith("L"); s["marks"] += cat.startswith("M")
    s["rtl"] += u.bidirectional(c) in ("R", "AL")
    s["capital"] += " CAPITAL LETTER " in nm
    s["vowel_sign"] += "VOWEL SIGN" in nm
    s["virama"] += any(w in nm for w in ("VIRAMA", "HALANT", "KILLER", "ASAT", "COENG", "SIGN PAMAAEH", "PANGOLAT"))
    s["syllable"] += any(w in nm for w in ("SYLLABLE", "SYLLABICS"))
    s["logo"] += any(w in nm for w in ("HIEROGLYPH", "CUNEIFORM", "IDEOGRAPH", "LOGOGRAM", "TANGUT COMPONENT"))
    names[sc] |= {w for w in nm.split() if w in ("KA", "KHA", "GA", "GHA", "NGA")}
def kind(sc, s):
    if s["logo"] > s["letters"] / 3: return "logographic or hieroglyphic"
    if s["syllable"] > s["letters"] / 3: return "syllabary"
    if s["vowel_sign"] and {"KA", "KHA", "GHA"} <= names[sc]: return "Brahmic abugida, pairs with Devanagari by letter name"
    if s["vowel_sign"]: return "abugida, other inventory"
    if s["rtl"] > s["chars"] / 2: return "right-to-left alphabet or abjad"
    if s["capital"]: return "cased alphabet"
    return "alphabet or other"
rows = []
for sc, s in S.items():
    rows.append({"code": sc, "script": fu.script_name(sc), "kind (read from the data)": kind(sc, s), "chars": s["chars"],
                 "letters": s["letters"], "marks": s["marks"], "vowel signs": s["vowel_sign"], "virama-like": s["virama"],
                 "right-to-left": s["rtl"], "status": DONE_V6.get(sc, "v7 task")})
rows.sort(key=lambda r: (r["kind (read from the data)"], r["script"]))
with open(sys.argv[1], "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(f"{len(rows)} scripts, Unicode {u.unidata_version} (Python), fontTools {ftv} Script data")
