# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""AInagri reversibility, defined as in V6-TASKS.md section 3: T1 only (Devanagari -> AInagri -> Devanagari), since AInagri
is not a core form. Synthetic strings (every consonant with every vowel sign, with the virama and alone; every independent
vowel; every sign; conjunct chains) must come back exactly; the Devanagari corpora of zip 5 are reported line by line,
compared after NFC (the form the converter works in; lines NFC itself changes are counted separately).
    python3 v7/ainagri/test_ainagri.py        exit 0 when every synthetic string and every corpus line comes back"""
import sys
import unicodedata as u
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ainagri as a

def rt(s):
    s = u.normalize("NFC", s)
    return a.from_ainagri(a.to_ainagri(s)) == s

syn = []
for c in a.CONS:
    syn += [c, c + a.VIRAMA, c + a.VIRAMA + "अ"] + [c + m for m in a.MATRA] + [c + a.VIRAMA + c2 for c2 in list(a.CONS)[:12]]
    syn += [c + s for s in ("ं", "ः", "ँ")]
syn += list(a.VOW) + ["अइ", "कइ", "कउ", "क्ष", "ज्ञ", "श्र", "त्र", "द्ध्र्य", "क्\u200dष", "क्\u200cष", "ऽ", "।", "॥", "०१२३४५६७८९", "Linux 2026", "ा", "क\u093cा"]
ok = sum(rt(s) for s in syn)
print(f"synthetic: {ok} of {len(syn)} come back exactly ({100 * ok / len(syn):.2f} %)")
bad = [s for s in syn if not rt(s)][:5]
if bad:
    print("   not back:", bad)

root = HERE.parents[1]
total = same = nfc_changed = 0
for f in sorted((root / "Romenagri").glob("corp_hi*.txt")):
    lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
    k = sum(rt(l) for l in lines); total += len(lines); same += k
    nfc_changed += sum(u.normalize("NFC", l) != l for l in lines)
    print(f"{f.name}: {k} of {len(lines)} lines come back ({100 * k / max(1, len(lines)):.2f} %)")
print(f"corpora: {same} of {total} lines ({100 * same / max(1, total):.2f} %); lines that NFC alone changes: {nfc_changed}")

block = [chr(c) for c in range(0x0900, 0x0980) if u.category(chr(c)) != "Cn"]
have = {k for k in list(a.CONS) + list(a.VOW) + list(a.MATRA) + list(a.SIGN) + [a.VIRAMA, a.NUKTA] if len(k) == 1}
have |= {u.normalize("NFD", k)[0] for k in a.CONS if len(k) == 2}
nfc_split = {c for c in block if u.normalize("NFC", c) != c and all(x in have or x == a.NUKTA for x in u.normalize("NFC", c))}
mapped = [c for c in block if c in have or c in nfc_split]
through = [c for c in block if c not in mapped]
print(f"Devanagari block: {len(mapped)} of {len(block)} assigned code points have an AInagri form; "
      f"{len(through)} pass through unchanged (still reversible): {' '.join(through)}")
sys.exit(0 if ok == len(syn) and same == total else 1)
