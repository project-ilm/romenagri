#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Repeats the measurements that sections 10.6, 11.1, 11.3, 11.4, 11.5 and 11.6 of Romenagri/TRANSLITERATION.md state, on the unpatched build
(old), on the build with the Sanskrit characters only (mid: patch 0001) and on the patched build (new: patches 0001, 0002 and 0003: the guards
of section 14.7 and the nukta layer of section 15), and fails when one of them comes out differently.

A limitation that the document describes and that no test holds in place is a claim that can go stale unnoticed.  This script holds them:
the behaviours are the quirks of the code (the section numbers are printed in the first column), so what it asserts is that they are still
the quirks that the document says they are.  A change to the converters that removes one of them is good news; the document and this
script are then updated together.

Two kinds of line:
    ok / FAIL        asserted: deterministic on any build (a table lookup that returns NULL, a pop of an empty stack, a static buffer that is
                     never cleared, the arithmetic of the 16-bit fallback)
    (informational)  depends on how the compiler lays out memory (the exact size at which a fixed-size buffer overflows into a crash): the
                     result is printed so that the number in the document can be compared, and never fails the run
Exit status 1 if an asserted line fails.
"""
import sys

import config
import model
import rmn_tables
import rn
import spec_model

fail = 0
ROWS = []


def check(section, what, ok, detail=""):
    global fail
    fail |= not ok
    print("  %-5s %-86s %s%s" % (section, what, "ok" if ok else "FAIL", ("   " + detail) if (detail and not ok) else ""))


def info(section, what, detail):
    print("  %-5s %-86s (informational) %s" % (section, what, detail))


def crashed(rc):
    return rc < 0 or rc >= 128


def a2r(t, data):
    return t.run("acii2rmn", data)


def uni_chain(t, text):
    """text -> uni2acii -> (bytes) -> acii2uni -> text (CRLF folded to LF as in rn.Tools.a2u)."""
    return t.a2u(t.u2a(text))


BUILDS = (("old", rn.old), ("mid", rn.mid), ("new", rn.new))
DIRS = {"old": config.OLD, "mid": config.MID, "new": config.NEW}
VERSION = {"old": spec_model.OLD, "mid": spec_model.MID, "new": spec_model.NEW}

print("11.1  the lexical layer")
for name, t in BUILDS:
    check("11.1", "%s: typed `k^aa` gives KA, halant and the ASCII text `^aa`" % name, t.r2a(b"k^aa") == (0, b"\xb3\xe8^aa"))
    check("11.1", "%s: a sign alone (DA) is written `^aa`, and that comes back as the ASCII text 5E 61 61" % name,
          a2r(t, b"\xda") == (0, b"^aa") and t.r2a(b"^aa") == (0, b"^aa"))
    check("11.1", "%s: the danda (EA) is written `|`, and `|` comes back as the ASCII bar 7C" % name,
          a2r(t, b"\xea") == (0, b"|") and t.r2a(b"|") == (0, b"|"))
    check("11.1", "%s: a Latin word and a quoted string cross acii2rmn wrapped, and rmn2acii unwraps them" % name,
          a2r(t, b"abc") == (0, b'"e_abc"') and a2r(t, b'"xy"') == (0, b'""xy""')
          and t.r2a(b'"e_abc"') == (0, b"abc") and t.r2a(b'""xy""') == (0, b'"xy"'))
    check("11.1", "%s: a literal underscore is the row `__` (5F); `_` followed by a letter is a family letter" % name,
          t.r2a(b"a__b") == (0, b"a\x5f\xca\xe8") and t.r2a(b"x_yna") == (0, b"\xd6\xe8\xbc"))
    rc, out = t.run("acii2cf", b"trace_\xb3")
    rc2, out2 = t.run("acii2pcf", b"trace_\xb3")
    check("11.1", "%s: acii2cf writes `trace__ka` and acii2pcf `trace_ka` for the Latin word `trace_` followed by KA" % name,
          (rc, rc2) == (0, 0) and out.strip() == b"trace__ka" and out2.strip() == b"trace_ka", "%r %r" % (out, out2))

print("11.3  keys the parser asks for and the table lacks")
SPEC = spec_model.load_doc()


def typed_form(key):
    """what a person types to make the parser ask for this key: the stem and the letter that selects it"""
    if key.endswith("vra"):
        return key[:-3] + "vr"
    if key.endswith("ha"):
        return key[:-2] + "h"
    raise ValueError(key)


for name, t in BUILDS:
    d = DIRS[name]
    T = model.parse_table(d)
    all_holes = sorted(k for k in spec_model.lookup_keys(SPEC, VERSION[name]) if k not in T)
    holes = [k for k in all_holes if k != "_s"]                  # `_s` (avagraha) is the one hole of the unpatched tables that the patch closes
    vra = [k for k in holes if k.endswith("vra")]
    asp = [k for k in holes if k.endswith("ha")]
    check("11.3", "%s: the grammar asks for 15 keys that the table lacks: 13 `...vra` keys and the aspirates %s" % (name, ", ".join("`%s`" % k for k in asp)),
          len(holes) == 15 and len(vra) == 13 and asp == ["_rrha", "lha"] and "lvra" not in holes, "%s" % holes)
    check("11.3", "%s: and the avagraha key `_s` is %s" % (name, "missing (the defect the patch repairs)" if name == "old" else "present"),
          (all_holes == sorted(holes + ["_s"])) if name == "old" else (all_holes == sorted(holes)), "%s" % all_holes)
    for key in holes:
        forms = [typed_form(key)] + ([typed_form(key) + "a"] if key.endswith("vra") else [])
        for form in forms:
            rc, out = t.r2a(form.encode())
            check("11.3", "%s: `%s` (asks for `%s`) crashes the filter and writes nothing" % (name, form, key), crashed(rc) and out == b"", "rc=%d out=%r" % (rc, out))
    rc, out = t.r2a(b"lvr")
    check("11.3", "%s: `lvr` works (the row `lvra` exists)" % name, rc == 0 and out != b"", "rc=%d out=%r" % (rc, out))
    rc, out = t.r2a(b"nv")
    rc2, out2 = t.r2a(b"nh")
    check("11.3", "%s: `nv` and `nh` do not crash: the stem `n` is not read in L2b (`nv` is NA and the letter v as text, `nh` is NA, a halant and the letter h)" % name,
          (rc, rc2) == (0, 0) and out == b"\xc6v" and out2 == b"\xc6\xe8h", "%r %r" % (out, out2))

print("11.4  buffers, limits and unchecked reads")
for name, t in BUILDS:
    rc1, o1 = a2r(t, b"\xb3" * 5119 + b" ")
    check("11.4", "%s: a stretch of 10,239 decoded characters (5,119 x KA and a space) is accepted" % name, rc1 == 0 and len(o1) == 10239, "rc=%d len=%d" % (rc1, len(o1)))
    rc2, o2 = a2r(t, b"\xb3" * 5119 + b"  ")
    info("11.4", "%s: 10,240 decoded characters (the same and two spaces)" % name, "crashes (rc=%d)" % rc2 if crashed(rc2) else "does not crash here (rc=%d)" % rc2)
    rc3, o3 = t.r2a(b"ka" * 511 + b"k")
    check("11.4", "%s: a run of 1,023 letters goes through the parser" % name, rc3 == 0 and o3 == b"\xb3" * 511 + b"\xb3\xe8", "rc=%d len=%d" % (rc3, len(o3)))
    rc4, _ = t.r2a(b"ka" * 512)
    rc5, _ = t.r2a(b"ka" * 512 + b"k")
    info("11.4", "%s: a run of 1,024 letters / of 1,025 letters" % name, "rc=%d / rc=%d" % (rc4, rc5))
    rc6, o6 = t.r2a(b"kakakaka c")
    fresh = t.r2a(b"c")
    if name == "new":
        check("11.4", "new: after `kakakaka`, the `c` of the next word is the letter c, as in a fresh process: the guard of section 14.7 does not step over the end",
              rc6 == 0 and o6 == b"\xb3\xb3\xb3\xb3\x20c" and fresh == (0, b"c"), "%s / %s" % (o6.hex(" "), fresh[1].hex(" ")))
    else:
        check("11.4", "%s: after `kakakaka`, the `c` of the next word reads the stale buffer; in a fresh process `c` is B8 E8" % name,
              rc6 == 0 and o6 == b"\xb3\xb3\xb3\xb3\x20\xb8\xe8\xb3\xb3\xb3" and fresh == (0, b"\xb8\xe8"), "%s / %s" % (o6.hex(" "), fresh[1].hex(" ")))
    head = t.r2a(b"kakakaka ")
    for tail in ("lv", "ke", "_e", "_y", "_o", "_n", "_r", "_j"):
        fresh = t.r2a(tail.encode())
        stale = t.r2a(b"kakakaka " + tail.encode())
        if name == "new":
            check("11.4", "new: after `kakakaka`, `%s` at the end of the next word is read as in a fresh process (%s): the guards stop at the end" % (tail, fresh[1].hex(" ") or "nothing"),
                  head[0] == fresh[0] == stale[0] == 0 and stale[1] == head[1] + fresh[1], "%s" % stale[1].hex(" "))
        else:
            check("11.4", "%s: after `kakakaka`, `%s` at the end of the next word reads the stale buffer (fresh process: %s)" % (name, tail, fresh[1].hex(" ") or "nothing"),
                  head[0] == fresh[0] == stale[0] == 0 and stale[1] != head[1] + fresh[1], "%s" % stale[1].hex(" "))
    for seq in (b"\xe8\xe9", b"\xea\xe9", b"\xb3\xe8\xe9"):
        rc, out = a2r(t, seq)
        check("11.4", "%s: acii2rmn crashes on %s (a nukta with fewer than two characters below it)" % (name, seq.hex(" ").upper()), crashed(rc), "rc=%d" % rc)

print("11.5  what does not survive a round trip")
for name, t in BUILDS:
    for c, sign in ((b"\xaa", b"\xdf"), (b"\x81", b"\x84"), (b"\x82", b"\x85"), (b"\x83", b"\x86")):
        if name == "old" and c in (b"\x81", b"\x82", b"\x83"):
            continue
        rc, mid = a2r(t, b"\xb3\xe8" + c)
        back = t.r2a(mid)
        check("11.5", "%s: KA, halant, independent vocalic vowel %s comes back as KA and the sign %s" % (name, c.hex().upper(), sign.hex().upper()),
              rc == 0 and back == (0, b"\xb3" + sign), "%r -> %r" % (mid, back))
    rc, mid = a2r(t, b"\xc4\xe9")
    back = t.r2a(mid)
    check("11.5", "%s: dental DA and the nukta (C4 E9) is written `__rda`, which is read as a literal underscore and `rda`" % name,
          rc == 0 and mid == b"__rda" and back[0] == 0 and back[1].startswith(b"\x5f"), "%r -> %r" % (mid, back))
    rc, mid = a2r(t, b"\xb3\xe8\xe8\xb4")
    check("11.5", "%s: ISCII's explicit halant (KA, E8, E8, KHA) comes out of acii2rmn as `kha`: the consonant before it is lost" % name,
          (rc, mid) == (0, b"kha"), "%r" % mid)
    rc, mid = a2r(t, b"\xb3\xe8\xe9\xb4")
    check("11.5", "%s: ISCII's soft halant (KA, E8, E9, KHA) crashes acii2rmn" % name, crashed(rc), "rc=%d" % rc)

# the nukta after every consonant byte (section 10.6, step 2)
print("10.6  a consonant followed by the nukta")
for name, t, d in (("old", rn.old, config.OLD), ("mid", rn.mid, config.MID), ("new", rn.new, config.NEW)):
    rows = rmn_tables.parse_acii(d)[1]
    consonants = sorted({r[1][0] for r in rows if len(r[1]) == 1 and 0xB3 <= r[1][0] <= 0xD8})       # bytes that have a one-byte row
    bad = []
    for b in consonants:
        data = bytes([b, 0xE9])
        rc, mid = a2r(t, data)
        if rc != 0:
            bad.append("%02X(crash)" % b)
        elif t.r2a(mid) != (0, data):
            bad.append("%02X" % b)
    check("10.6", "%s: of the %d consonant bytes (one-byte rows in B3-D8), `byte, nukta` survives acii2rmn | rmn2acii except C4 and C5" % (name, len(consonants)),
          bad == ["C4", "C5"], "fails for %s" % " ".join(bad))

print("11.6  what uni2acii does with characters it has no row for (the low byte, and acii2uni's byte % 128)")
CASES = [
    (0x00A0, " "), (0x00AD, "ऐ"), (0x00B7, "ङ"), (0x00D7, "स"), (0x00E9, "़"), (0x20B9, "छ"),
    (0x2022, '"'), (0x2122, '"'), (0x2026, "&"), (0x2020, " "), (0xFFFD, "}"), (0x1CD0, "ऱ"),
]
for name, t in BUILDS:
    for cp, want in CASES:
        got = uni_chain(t, chr(cp))
        check("11.6", "%s: U+%04X comes back as %r" % (name, cp, want), got == want, "got %r" % got)
    want = "\u0933\u093c" if name == "new" else "4"      # the nukta layer (patch 0003, section 15) writes ऴ as D2 E9, which acii2uni writes as the pair; without it the low byte 34 is a "4"
    got = uni_chain(t, "\u0934")
    check("11.6", "%s: U+0934 comes back as %r (%s)" % (name, want, "the nukta layer writes D2 E9, and acii2uni writes ळ and a nukta, section 15" if name == "new" else "the low byte 34"),
          got == want, "got %r" % got)
    if name == "new":
        got = t.a2u(t.u2a("\u0934", form="nfc"), form="nfc")
        check("11.6", "new: with -f nfc on both converters U+0934 comes back as itself (D2 E9 is composed by acii2uni, section 15)", got == "\u0934", "got %r" % got)
    ctl = [cp for cp in list(range(0x2002, 0x201A)) + [0x201C, 0x201D] if not all(ord(ch) < 0x20 for ch in uni_chain(t, chr(cp)))]
    check("11.6", "%s: U+2002-U+2019, U+201C, U+201D (including ZWNJ U+200C and ZWJ U+200D) all come back as control characters" % name, not ctl,
          " ".join("U+%04X" % c for c in ctl))
    check("11.6", "%s: ZWNJ comes back as U+000C (form feed) and ZWJ as U+000D (carriage return)" % name,
          t.u2a("‌") == b"\x0c" and t.u2a("‍") == b"\x0d" and uni_chain(t, "‌") == "\x0c" and uni_chain(t, "‍") == "\r",
          "%r %r" % (t.u2a("‌"), t.u2a("‍")))
    check("11.6", "%s: U+2190 comes back as a control character" % name, all(ord(ch) < 0x20 for ch in uni_chain(t, "←")) and uni_chain(t, "←") != "")
    raw = t.u2a("\U0001F600")
    check("11.6", "%s: U+1F600 gives the bytes 3D 00" % name, raw == b"\x3d\x00", raw.hex(" "))

old_dd, new_dd = uni_chain(rn.old, "॥"), uni_chain(rn.new, "॥")
check("11.6", "the double danda U+0965 came back as `e` before the patch and comes back as itself now", (old_dd, new_dd) == ("e", "॥"), "%r %r" % (old_dd, new_dd))

print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
