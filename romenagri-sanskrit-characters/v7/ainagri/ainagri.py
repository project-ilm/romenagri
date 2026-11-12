# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""AInagri: a script for Sanskrit and the Devanagari languages, written with characters that readers across the world
already know, one visual unit for each Devanagari letter, and reversible to the byte.

Rules (the letters themselves are data, in ainagri.csv, and can be changed there without touching this code):
  1. Base letters are the Latin letters most of the world reads.
  2. Length is a macron (ā ī ū), as in every scholarly romanisation.
  3. Retroflex is a dot below (ṭ ḍ ṇ ṣ ḷ), as in ISO 15919 and IAST.
  4. Aspiration is a raised h (kʰ gʰ tʰ dʰ ...), as in the IPA, never a second full letter: one letter stays one unit.
  5. The two diphthongs are single letters, ê and ô, so that a following vowel can never be misread.
  6. Vocalic r and l carry a ring below (r̥ r̥̄ l̥ l̥̄), which leaves ṛ free for ड़, as in ISO 15919.
  7. Every character is in the fonts that ship with every current operating system.

    python3 ainagri.py to   "text"      Devanagari -> AInagri        python3 ainagri.py from "text"  AInagri -> Devanagari
    python3 ainagri.py table             the table, with Romenagri beside it when zip 5's core is built (tests/build_trees.sh)
"""
import csv
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
VIRAMA, NUKTA = "\u094d", "\u093c"
SEP = "\u00b7"                          # an explicit virama before a vowel (Vedic and rare forms): k·a = क्अ
ORPHAN = "\u25cc"                       # a vowel sign with no consonant before it
ESC_OPEN, ESC_CLOSE = "\u27e6", "\u27e7"   # text that is already in Latin letters, kept as it is: ⟦Linux⟧


def load(path=HERE / "ainagri.csv"):
    cons, vow, matra, sign = {}, {}, {}, {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        d, a, k = unicodedata.normalize("NFC", r["devanagari"]), unicodedata.normalize("NFC", r["ainagri"]), r["kind"]
        if k == "consonant":
            cons[d] = a
        elif k == "vowel":
            vow[d] = a
            if r["matra"]:
                matra[r["matra"]] = a
        else:
            sign[d] = a
    return cons, vow, matra, sign


CONS, VOW, MATRA, SIGN = load()
_all = {**CONS, **VOW, **SIGN}
assert len(set(_all.values())) == len(_all), "two Devanagari letters have the same AInagri form"
R_CONS = {v: k for k, v in CONS.items()}
R_VOW = {v: k for k, v in VOW.items()}
R_MATRA = {v: k for k, v in MATRA.items()}
R_SIGN = {v: k for k, v in SIGN.items()}
TOKENS = sorted(set(R_CONS) | set(R_VOW) | set(R_SIGN), key=len, reverse=True)
AIN_CHARS = set("".join(TOKENS)) | {SEP, ORPHAN, ESC_OPEN, ESC_CLOSE}


def to_ainagri(text):
    t = unicodedata.normalize("NFC", text)
    out, i, n = [], 0, len(t)
    while i < n:
        ch = t[i]
        if ch in AIN_CHARS or (ch.isascii() and ch.isalnum()):      # already Latin (or AInagri): kept, marked
            j = i
            while j < n and (t[j] in AIN_CHARS or (t[j].isascii() and t[j].isalnum())) and t[j] != ESC_CLOSE:
                j += 1
            j = max(j, i + 1)
            out.append(ESC_OPEN + t[i:j] + ESC_CLOSE)
            i = j
            continue
        key = t[i:i + 2] if t[i:i + 2] in CONS else (ch if ch in CONS else None)
        if key:
            out.append(CONS[key])
            i += len(key)
            if i < n and t[i] == VIRAMA:
                i += 1
                if i < n and t[i] in VOW:
                    out.append(SEP)
            elif i < n and t[i] in MATRA:
                out.append(MATRA[t[i]])
                i += 1
            else:
                out.append(VOW["अ"])
            continue
        if ch in VOW:
            out.append(VOW[ch])
        elif ch in MATRA:
            out.append(ORPHAN + MATRA[ch])
        elif ch in SIGN:
            out.append(SIGN[ch])
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def from_ainagri(text):
    t = unicodedata.normalize("NFC", text)
    out, i, n, slot = [], 0, len(t), False      # slot: a consonant is waiting for its vowel
    while i < n:
        if t[i] == ESC_OPEN:
            j = t.find(ESC_CLOSE, i + 1)
            j = n if j < 0 else j
            if slot:
                out.append(VIRAMA); slot = False
            out.append(t[i + 1:j])
            i = j + 1
            continue
        if t[i] == ORPHAN:
            tok = next((x for x in TOKENS if t.startswith(x, i + 1) and x in R_MATRA), None)
            if tok:
                if slot:
                    out.append(VIRAMA); slot = False
                out.append(R_MATRA[tok]); i += 1 + len(tok)
                continue
        if t[i] == SEP and slot:
            out.append(VIRAMA); slot = False; i += 1
            continue
        tok = next((x for x in TOKENS if t.startswith(x, i)), None)
        if tok in R_CONS:
            if slot:
                out.append(VIRAMA)
            out.append(R_CONS[tok]); slot = True
        elif tok in R_VOW:
            if slot:
                if tok != VOW["अ"]:
                    out.append(R_MATRA[tok])
                slot = False
            else:
                out.append(R_VOW[tok])
        else:
            if slot:
                out.append(VIRAMA); slot = False
            if tok in R_SIGN:
                out.append(R_SIGN[tok])
            else:
                tok = t[i]
                out.append(tok)
        i += len(tok)
    if slot:
        out.append(VIRAMA)
    return "".join(out)


def romenagri(dev):
    """The same letter through zip 5's own core (uni2acii, then acii2rmn), if it is built; else None."""
    root = HERE.parents[1]
    sys.path.insert(0, str(root / "tests"))
    try:
        import rn
        return rn.new.a2r(rn.new.u2a(dev)).decode("utf-8", "replace").strip()
    except Exception:
        return None


def table():
    rows = list(csv.DictReader(open(HERE / "ainagri.csv", encoding="utf-8")))
    print("| Devanagari | AInagri | Romenagri | Unicode name |")
    print("|---|---|---|---|")
    for r in rows:
        rmn = romenagri(r["devanagari"])
        print(f"| {r['devanagari']} | {r['ainagri']} | {rmn if rmn is not None else ''} | {r['name']} |")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "table"
    arg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else sys.stdin.read()
    if cmd == "to":
        sys.stdout.write(to_ainagri(arg))
    elif cmd == "from":
        sys.stdout.write(from_ainagri(arg))
    else:
        table()
