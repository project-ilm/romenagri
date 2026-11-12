# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""acii2hin (the one-way, lossy "saral" Latin rendering used by hin2std) for the new bytes.   usage: python3 tests/test_acii2hin.py

The expected strings are the ones written in aciihin.h by tools/apply_sanskrit.py; the vocalic signs and the accents are context
dependent, so each is tried after KA.  Also checks that the old repertoire renders exactly as before.  Exit status 1 on a mismatch."""
import sys

import config
import rn

CASES = [                      # (name, ACII bytes, expected saral text)
    ("OM", b"\x8c", b"om"),
    ("vocalic L", b"\x81", b"lri"),
    ("vocalic LL", b"\x82", b"lri"),
    ("vocalic RR", b"\x83", b"ri"),
    ("KA + sign L", b"\xb3\x84", b"klri"),
    ("KA + sign LL", b"\xb3\x85", b"klri"),
    ("KA + sign RR", b"\xb3\x86", b"kri"),
    ("double danda", b"\x87", b"||"),
    ("KA + udatta", b"\xb3\x88", b"ka"),
    ("KA + anudatta", b"\xb3\x89", b"ka"),
    ("KA + grave", b"\xb3\x8a", b"ka"),
    ("KA + acute", b"\xb3\x8b", b"ka"),
    ("OM bhur (mixed)", b"\x8c \xcb\xe9\xcf", b"om bhara"),
]
fail = False
for name, a, want in CASES:
    got = rn.new.a2h(a)
    ok = got == want
    fail |= not ok
    print("%-18s %-12s -> %-10r %s%s" % (name, a.hex(), got, "ok" if ok else "WRONG, expected %r" % want, "   (old build: %r)" % rn.old.a2h(a)))
# the old repertoire renders as before: every single byte and every byte pair of the old table
pairs = [bytes([x]) for x in range(0xA1, 0xF0) if x != 0xEB] + [bytes([x, y]) for x in (0xB3, 0xCF, 0xD5) for y in range(0xA1, 0xF0) if y != 0xEB]
diff = [p for p in pairs if rn.old.a2h(p) != rn.new.a2h(p)]
print("old-repertoire inputs (%d) rendering differently in the new build: %d" % (len(pairs), len(diff)))
fail |= bool(diff)
print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
