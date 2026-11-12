# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Compare what the compiled Hindi programs printed with the Devanagari source text.   usage: check.py <run dir> [-v]

Three programs: c (C, lines A-F), c0 (the same C program without the two identifier lines, lines A-E: the control that lets the
unpatched build compile, so that string-literal damage can be told apart from identifier damage) and j (Java, lines A-F)."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
exp = json.load(open(os.path.join(HERE, "expect.json"), encoding="utf-8"))
RUNS = (("C            ", "c", "ABCDEF"), ("C (control)  ", "c0", "ABCDE"), ("Java         ", "j", "ABCDEF"))


def show(s):
    return " ".join("U+%04X" % ord(c) if ord(c) > 0x7F or ord(c) < 0x20 else c for c in s)


rc = 0
for lang, sub, keys in RUNS:
    path = os.path.join(sys.argv[1], sub, "out.txt")
    try:
        text = open(path, "rb").read().decode("utf-8", "replace")
    except OSError:
        print(lang, "no output")
        rc = 1
        continue
    got = {l[0]: l[2:] for l in text.splitlines() if len(l) > 1 and l[1] == ":"}
    ok = 0
    for k in keys:
        same = got.get(k) == exp[k]
        ok += same
        if not same and len(sys.argv) > 2:
            print("   %s %s differs\n      want %s\n      got  %s" % (lang.strip(), k, show(exp[k]), show(got.get(k, "<missing>"))))
    print("%s: %d of %d lines identical to the Devanagari source  %s" % (lang, ok, len(keys), "".join(("." if got.get(k) == exp[k] else "x") for k in keys)))
    rc |= ok != len(keys)
sys.exit(rc)
