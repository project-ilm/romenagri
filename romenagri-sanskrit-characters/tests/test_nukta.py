#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""The nukta layer of uni2acii and acii2uni (patch 0003; Romenagri/TRANSLITERATION.md, section 15).   usage: python3 tests/test_nukta.py [--full]

ACII writes a letter with a nukta as two bytes, the consonant and E9.  Unicode has eleven letters that are such a pair in one code point.
Before the layer, uni2acii wrote the low byte of nine of them (U+095C became a backslash).  The rule of the layer is that a letter with a
nukta is a consonant and a nukta, however it arrives: uni2acii writes the nine as the byte of the consonant and E9, from the single code
point and from consonant + nukta alike.  What the converters write for the family is the form (the Unicode layer, separate from the rule):
asis (the default: what they always wrote), nfc (as Unicode's NFC) or nfd (as NFD), chosen by -f, by ROMENAGRI_NUKTA_FORM, by the macro
NUKTA_FORM, or by nukta_set_form().  uni2acii -w reports the code points that it writes as low bytes (off by default).

  (a) nukta.h against Python's unicodedata: the eleven rows are exactly the code points of U+0900-U+097F whose canonical decomposition is
      a consonant and U+093C; a row has the nfc mark 1 if and only if NFC composes it; NUKTA_BYTE is the byte of U+093C in unicode.h;
      the default form is asis; D3 (ISCII's ZHA) is not used
  (b) uni2acii in the three forms: what each of the eleven letters, and each consonant + nukta, is written as; patch 0001 alone wrote
      the low byte of the nine
  (c) how the form is chosen: the flag, the environment variable, the macro (builds compiled with -DNUKTA_FORM), nukta_set_form() in a
      program that includes nukta.h; which of them wins; the error cases; the old macro NUKTA_REBUILD stops the compiler
  (d) acii2uni in the three forms against a model of the rule, written here in Python on top of what the build without the layer writes
      for each byte: random streams, and the exhaustive streams  x y,  x E9 y  and  x y E9  for all 254 x 254 values of x and y
      (CR and LF left out); asis is exactly the build without the layer
  (e) uni2acii in the three forms against a model of the rule, on random streams and on the exhaustive pairs and triples of a set of
      forty code units (the letters, their consonants, the nukta, a halant, vowel signs, and the low-byte characters é, Æ, ...)
  (f) independent oracles: Python's NFC and NFD, for acii2uni (the output is NFC / NFD of what the build without the layer writes) and
      for uni2acii (the bytes of nfc and nfd are those that asis writes for the NFC / NFD of the input), on the streams whose marks are
      in canonical order (the layer, like the converters, never reorders: the one place where it does not do what NFC and NFD do),
      with negative controls
  (g) regression: uni2acii on all other 65,525 code units of the BMP writes exactly what patch 0001 alone writes, in every form; D3 is
      never written for one of the eleven letters
  (h) the edge cases of both converters, in every form
  (i) the warning layer: nothing is reported by default; -w and ROMENAGRI_NUKTA_WARN=1 report each code point once; the bytes written
      do not change
  (j) the whole chain  uni2acii -> acii2rmn -> rmn2acii -> acii2uni  on the eleven letters, in both spellings, and on the fifteen
      clusters of section 11.3 (DDA + nukta in both spellings), in every form
  (k) the cases of section 15.7 (C1 to C8), each asserted and printed with the code points, the ACII bytes and the Romenagri string, so
      that the document can quote them

Exit status 1 if an asserted line fails."""
import os
import random
import shutil
import struct
import subprocess
import sys
import tempfile
import unicodedata

import config
import rmn_tables
import rn

sys.stdout.reconfigure(encoding="utf-8")
FULL = "--full" in sys.argv
fail = 0
ZWJ, NUKTA = "‍", "़"
NFC = lambda t: unicodedata.normalize("NFC", t)
NFD = lambda t: unicodedata.normalize("NFD", t)
FORMS = ("asis", "nfc", "nfd")


def check(what, ok, detail=""):
    global fail
    fail |= not ok
    print("    %-112s %s%s" % (what, "ok" if ok else "FAIL", ("   " + detail) if (detail and not ok) else ""))


def cps(text):
    return " ".join("U+%04X" % ord(c) for c in text)


def hexs(b):
    return " ".join("%02X" % x for x in b)


def units(us):
    """UTF-16LE with a byte order mark, from a list of code units (lone surrogates allowed)"""
    return b"\xff\xfe" + b"".join(struct.pack("<H", u) for u in us)


N, NB, DEFAULT, ROWS = rmn_tables.parse_nukta(config.need(config.NEW))
UNI = {}
for _cp, _b in rmn_tables.parse_unicode(config.NEW)[1]:
    UNI.setdefault(_cp, _b)                                           # the converters take the first row that matches
BYTE_OF_NUKTA = UNI[0x093C]
LAYER = {cp: (base, nfc) for cp, base, nfc in ROWS}                   # letter -> (consonant, 1 if NFC composes the pair)
BASES = {UNI[base]: (cp, nfc) for cp, base, nfc in ROWS}              # consonant byte -> (letter, nfc mark)
NINE = sorted(cp for cp in LAYER if cp not in UNI)                    # the letters that unicode.h has no row for
JOIN_BYTE = {UNI[base]: UNI[cp] for cp, (base, nfc) in LAYER.items() if nfc and cp in UNI}   # byte of a consonant -> byte of the letter (C6 -> C7, CF -> D0)


# ------------------------------------------------------------------------------------------------ (a)
print("(a) nukta.h against Python's unicodedata (Unicode %s)" % unicodedata.unidata_version)
ends_in_nukta = [cp for cp in range(0x900, 0x980) if len(NFD(chr(cp))) == 2 and NFD(chr(cp))[1] == NUKTA]
check("%d rows (NUKTA_LEN %s); the code points of U+0900-U+097F whose NFD is a consonant and U+093C: %d" % (len(ROWS), N, len(ends_in_nukta)),
      N == len(ROWS) == len(ends_in_nukta) == 11)
check("the rows are exactly those code points", sorted(cp for cp, _, _ in ROWS) == ends_in_nukta)
check("every row is the NFD pair of its letter: base + U+093C", all(NFD(chr(cp)) == chr(base) + NUKTA for cp, base, _ in ROWS))
check("NUKTA_BYTE is 0x%02X, the byte of U+093C in unicode.h" % NB, NB == BYTE_OF_NUKTA == 0xE9)
check("every base letter has a byte in unicode.h", all(base in UNI for _, base, _ in ROWS))
check("the nfc mark of a row is 1 if and only if NFC composes the pair (%s)" % ", ".join("U+%04X" % cp for cp, _, m in ROWS if m == 1),
      all((NFC(chr(base) + NUKTA) == chr(cp)) == (m == 1) for cp, base, m in ROWS) and all(m in (0, 1) for _, _, m in ROWS))
check("the other eight (U+0958-U+095F) are the composition exclusions: NFC leaves their pair decomposed",
      all(NFC(chr(base) + NUKTA) == chr(base) + NUKTA for cp, base, m in ROWS if m == 0) and sum(1 for _, _, m in ROWS if m == 0) == 8)
check("only U+0929 and U+0931 have a row in unicode.h; the other nine have none", sorted(cp for cp in LAYER if cp in UNI) == [0x929, 0x931])
check("the default NUKTA_FORM is %d, asis: the converters write what they always wrote" % DEFAULT, DEFAULT == 0)
check("D3, the byte that ISCII gives ZHA (U+0934), is not a byte of unicode.h: the layer does not take it (section 15.7, C7)", 0xD3 not in set(UNI.values()))

# ------------------------------------------------------------------------------------------------ (b)
print("(b) uni2acii in the three forms")


def exp_u2a(cp, base, form, pair):
    """the bytes of the letter `cp` (single code point) or of its pair `base` + U+093C"""
    if form == "nfd":
        return bytes([UNI[base], NB])
    if cp in UNI:                                          # U+0929, U+0931: a row of unicode.h
        return bytes([UNI[cp]]) if (not pair or form == "nfc") else bytes([UNI[base], NB])
    return bytes([UNI[base], NB])


for form in FORMS:
    ok_single = ok_pair = 0
    for cp, (base, m) in LAYER.items():
        ok_single += rn.new.u2a(chr(cp), form) == exp_u2a(cp, base, form, False)
        ok_pair += rn.new.u2a(chr(base) + NUKTA, form) == exp_u2a(cp, base, form, True)
    check("form %-4s: the single code point is written as %d of 11 expected, consonant + nukta as %d of 11" % (form, ok_single, ok_pair),
          ok_single == ok_pair == 11)
same = sum(rn.new.u2a(chr(cp)) == rn.new.u2a(chr(base) + NUKTA) for cp, (base, m) in LAYER.items())
check("asis: the nine have one spelling in ACII (single code point = pair); U+0929 and U+0931 have two (C7 and C6 E9, D0 and CF E9): %d of 11" % same, same == 9)
same = sum(rn.new.u2a(chr(cp), "nfd") == rn.new.u2a(chr(base) + NUKTA, "nfd") for cp, (base, m) in LAYER.items())
check("nfd: all eleven have one spelling, the consonant and E9: %d of 11" % same, same == 11)
same = sum(rn.new.u2a(chr(cp), "nfc") == rn.new.u2a(chr(base) + NUKTA, "nfc") for cp, (base, m) in LAYER.items())
check("nfc: all eleven have one spelling (C7 and D0 for U+0929 and U+0931, the consonant and E9 for the other nine): %d of 11" % same, same == 11)
mids = sum(rn.mid.u2a(chr(cp)) == (bytes([UNI[cp]]) if cp in UNI else bytes([cp & 255])) for cp in LAYER)
check("patch 0001 alone wrote the low byte of the nine and the table byte of the two: %d of 11" % mids, mids == 11)

# ------------------------------------------------------------------------------------------------ (c)
print("(c) how the form is chosen")
TMP = tempfile.mkdtemp(prefix="nukta_forms_")
MB = {}


def build(label, flags, src_progs=("acii2uni", "uni2acii")):
    d = os.path.join(TMP, label)
    os.makedirs(d)
    out = ""
    for prog in src_progs:
        p = subprocess.run(["gcc", "-O1", "-Wall", "-Wextra"] + flags + ["-I", config.NEW, "-o", os.path.join(d, prog), os.path.join(config.NEW, prog + ".c")],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        out += p.stdout
        if p.returncode != 0:
            out += "(exit %d)" % p.returncode
    return d, out


for label, flag in (("asis", "-DNUKTA_FORM=NUKTA_ASIS"), ("nfc", "-DNUKTA_FORM=NUKTA_NFC"), ("nfd", "-DNUKTA_FORM=NUKTA_NFD"), ("nfc_n", "-DNUKTA_FORM=1")):
    d, out = build("macro_" + label, [flag])
    if out.strip():
        print(out)
    check("both converters compile with %s and -Wall -Wextra without a warning" % flag, not out.strip())
    MB[label] = rn.Tools(d)
d, out = build("none", [])
check("both converters compile with no macro, and the default build is asis (see (a))", not out.strip())
MB["none"] = rn.Tools(d)
for flag, why in (("-DNUKTA_REBUILD=1", "the old macro NUKTA_REBUILD"), ("-DNUKTA_FORM=3", "a NUKTA_FORM that is not 0, 1 or 2")):
    p = subprocess.run(["gcc", "-fsyntax-only", flag, "-I", config.NEW, os.path.join(config.NEW, "acii2uni.c")], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       universal_newlines=True)
    msg = [l for l in p.stderr.splitlines() if "error:" in l]
    check("%s stops the compiler (%s)" % (why, msg[0].split("error:", 1)[1].strip()[:70] if msg else "no message"),
          p.returncode != 0 and "NUKTA_FORM" in p.stderr)

PROBE_A = b"\xc6\xe9\xcf\xe9\xd2\xe9\xc7\xd0\xb3\xe9\xc6\n"        # the eleven bytes of the family, a pair at the end of a line
PROBE_U = units([0x0928, 0x093C, 0x0929, 0x0930, 0x093C, 0x0931, 0x0934, 0x0915, 0x093C, 0x0928, 0x000A, 0x095C])
for form in FORMS:
    want_a, want_u = rn.new.a2u(PROBE_A, form), rn.new.run("uni2acii", PROBE_U, args=("-f", form))[1]
    check("%-4s: the build compiled with the macro writes the same by default as the flag -f %s, for both converters" % (form, form),
          MB[form].a2u(PROBE_A) == want_a and MB[form].run("uni2acii", PROBE_U)[1] == want_u)
    check("%-4s: the environment variable writes the same as the flag, for both converters" % form,
          rn.new.run("acii2uni", PROBE_A, env={"ROMENAGRI_NUKTA_FORM": form})[1].decode("utf-16").replace("\r\n", "\n") == want_a and
          rn.new.run("uni2acii", PROBE_U, env={"ROMENAGRI_NUKTA_FORM": form})[1] == want_u)
check("--form=NFC (upper case) is the form nfc; -f needs a separate argument", rn.new.run("uni2acii", PROBE_U, args=("--form=NFC",))[1] ==
      rn.new.run("uni2acii", PROBE_U, args=("-f", "nfc"))[1])
check("an empty ROMENAGRI_NUKTA_FORM is not set", rn.new.run("uni2acii", PROBE_U, env={"ROMENAGRI_NUKTA_FORM": ""})[1] == rn.new.run("uni2acii", PROBE_U)[1])
check("precedence, the last winning: macro nfd < environment nfc < flag asis",
      MB["nfd"].run("uni2acii", PROBE_U)[1] != MB["nfd"].run("uni2acii", PROBE_U, env={"ROMENAGRI_NUKTA_FORM": "nfc"})[1] ==
      rn.new.run("uni2acii", PROBE_U, args=("-f", "nfc"))[1] and
      MB["nfd"].run("uni2acii", PROBE_U, env={"ROMENAGRI_NUKTA_FORM": "nfc"}, args=("-f", "asis"))[1] == rn.new.run("uni2acii", PROBE_U)[1])
C_SRC = os.path.join(TMP, "fn.c")
open(C_SRC, "w").write('#include <stdio.h>\n#include "unicode.h"\n#include "nukta.h"\nint main (void)\n{\n'
                       '  int a = nukta_set_form ("NFD"), b = nukta_form, c = nukta_set_form ("bogus"), d = nukta_form;\n'
                       '  printf ("%d %d %d %d\\n", a, b, c, d);\n  return 0;\n}\n')
p = subprocess.run(["gcc", "-Wall", "-Wno-unused-function", "-I", config.NEW, "-o", os.path.join(TMP, "fn"), C_SRC], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                   universal_newlines=True)
fn = subprocess.run([os.path.join(TMP, "fn")], stdout=subprocess.PIPE, universal_newlines=True).stdout.strip() if p.returncode == 0 else p.stdout
check("a program that includes nukta.h: nukta_set_form(\"NFD\") returns 0 and sets nukta_form to %d; \"bogus\" returns -1 and changes nothing: %r" % (2, fn),
      fn == "0 2 -1 2")
for prog, data in (("uni2acii", PROBE_U), ("acii2uni", PROBE_A)):
    for label, args, env in (("-f xyz", ("-f", "xyz"), None), ("-f without a form", ("-f",), None), ("--form=", ("--form=",), None),
                             ("an unknown option", ("--bogus",), None), ("one file name (the converters need two or none)", ("x",), None),
                             ("-- and one file name", ("--", "x"), None), ("ROMENAGRI_NUKTA_FORM=bad", (), {"ROMENAGRI_NUKTA_FORM": "bad"})):
        rc, out, err = rn.new.run3(prog, data, args=args, env=env)
        check("%-8s %-46s exit status %d, the usage line on stdout, nothing converted%s" % (prog, label, rc, ", a message on stderr" if err else ""),
              rc == 1 and out.startswith(b"Usage: " + prog.encode()) and (err or label.startswith(("one", "--"))) and b"\xff\xfe" not in out)
rc, out, err = rn.new.run3("acii2uni", PROBE_A, args=("-w",))
check("acii2uni has no -w (the warning layer is in uni2acii): exit status %d" % rc, rc == 1 and b"unknown option -w" in err)
src_u, dst_u = os.path.join(TMP, "in.u16"), os.path.join(TMP, "out.acii")
open(src_u, "wb").write(PROBE_U)
for args, form in ((("-f", "nfd"), "nfd"), (("--form=nfd",), "nfd"), (("-f", "nfd", "--"), "nfd"), (("--",), None)):
    rc = subprocess.run([os.path.join(config.NEW, "uni2acii")] + list(args) + [src_u, dst_u], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode
    want = rn.new.run("uni2acii", PROBE_U, args=("-f", form) if form else ())[1]
    check("file names after the options (%s): exit status %d, the output file holds what stdout would" % (" ".join(args), rc), rc == 0 and open(dst_u, "rb").read() == want)

# ------------------------------------------------------------------------------------------------ (d)
print("(d) acii2uni in the three forms: a model of the rule")
NOLF = [b for b in range(256) if b not in (10, 13)]
_out = rn.mid.a2u(b"".join(bytes([b, 10]) for b in NOLF))
OLD_TEXT = dict(zip(NOLF, _out.split("\n")))
check("the build without the layer writes one code point for each of the 254 bytes (the model's building block)",
      len(OLD_TEXT) == 254 and all(len(t) == 1 for t in OLD_TEXT.values()))


def model_a2u(data, form):
    """what acii2uni must write for the ACII bytes `data`, one line without newlines: the text that the build without the layer writes for
    each byte; except that in nfc a consonant byte of the letters whose pair NFC composes, directly followed by E9, is with the E9 the one
    code point of its row, and that in nfd a letter that a byte writes as one code point is written as its consonant and U+093C"""
    out, i = [], 0
    while i < len(data):
        b = data[i]
        if form == "nfc" and b in BASES and BASES[b][1] == 1 and i + 1 < len(data) and data[i + 1] == NB:
            out.append(chr(BASES[b][0]))
            i += 2
            continue
        t = OLD_TEXT[b]
        if form == "nfd" and ord(t) in LAYER:
            t = chr(LAYER[ord(t)][0]) + NUKTA
        out.append(t)
        i += 1
    return "".join(out)


def streams_agree(name, lines, expect_changed):
    """every form against the model, line by line (each line ends in a newline, which also ends a held byte); expect_changed[form] is the
    number of lines on which the form must differ from the build without the layer"""
    data = b"".join(l + b"\n" for l in lines)
    old = rn.mid.a2u(data).split("\n")[:-1]
    ok, report = True, []
    for form in FORMS:
        got = rn.new.a2u(data, form).split("\n")[:-1]
        exp = [model_a2u(l, form) for l in lines]
        wrong = (len(got) != len(exp)) or sum(g != e for g, e in zip(got, exp))
        changed = sum(g != o for g, o in zip(got, old))
        want = expect_changed[form]
        ok &= wrong == 0 and (changed == want if isinstance(want, int) else want(changed))
        report.append("%s: model disagrees on %s lines, differs from the build without the layer on %d" % (form, wrong, changed))
    check("%s: %d lines; %s" % (name, len(lines), "; ".join(report)), ok)


rng = random.Random(20261108)
HOT = sorted(BASES) + [0xC7, 0xD0, NB, NB, NB, 0xE8, 0xDA, 0xDB, 0xDC, 0x20]       # the consonants, the two letters with a byte, E9 (three times as often), a halant, vowel signs, a space
count = 200000 if FULL else 30000
rand_lines = []
for _ in range(count):
    n = rng.randint(3, 12)
    rand_lines.append(bytes(rng.choice(HOT) if rng.random() < 0.85 else rng.choice(NOLF) for _ in range(n)))
streams_agree("random streams", rand_lines, {"asis": 0, "nfc": lambda c: c > count // 25, "nfd": lambda c: c > count // 25})
pairs_xy = [bytes([x, y]) for x in NOLF for y in NOLF]
streams_agree("exhaustive  x y", pairs_xy, {"asis": 0, "nfc": 3, "nfd": 254 * 254 - 252 * 252})
streams_agree("exhaustive  x E9 y", [bytes([x, NB, y]) for x in NOLF for y in NOLF], {"asis": 0, "nfc": 3 * len(NOLF), "nfd": 254 * 254 - 252 * 252})
streams_agree("exhaustive  x y E9", [bytes([x, y, NB]) for x in NOLF for y in NOLF], {"asis": 0, "nfc": 3 * len(NOLF) + 3, "nfd": 254 * 254 - 252 * 252})
print("    (nfc differs on x y in the 3 lines C6 E9, CF E9, D2 E9; nfd on the 1,012 lines that hold C7 or D0; asis on none: it is the build without the layer)")

# ------------------------------------------------------------------------------------------------ (e)
print("(e) uni2acii in the three forms: a model of the rule")
LET = sorted(LAYER)
CONS = sorted(base for base, _ in LAYER.values())
HOT_U = LET + CONS + [0x093C, 0x094D, 0x093E, 0x093F, 0x00C6, 0x00CF, 0x00D2, 0x00E9, 0x00E8, 0x2019, 0x0061, 0x0020, 0x000A, 0x0915, 0x0905, 0x0964]
ANY_U = [u for u in range(0x10000) if u not in (0x0D, 0xFEFF)]        # every code unit but the two that the converter eats (CR and the byte order mark)


def old_u2a(u):
    return bytes([UNI[u]]) if u in UNI else bytes([u & 255])


def model_u2a(us, form):
    """what uni2acii must write for the code units `us`: what patch 0001 alone writes for each unit (its row, or its low byte), except that a
    letter of nukta.h is the byte of its consonant and E9 unless it has a row (and the form is not nfd), and that in nfc a consonant whose
    byte unicode.h has for the letter (U+0928 and U+0930) directly followed by U+093C is the one byte of the letter"""
    out, i = bytearray(), 0
    while i < len(us):
        u = us[i]
        if u in LAYER:
            base, _ = LAYER[u]
            out += old_u2a(u) if (u in UNI and form != "nfd") else bytes([UNI[base], NB])
            i += 1
            continue
        if form == "nfc" and UNI.get(u) in JOIN_BYTE and i + 1 < len(us) and us[i + 1] == 0x093C:
            out.append(JOIN_BYTE[UNI[u]])
            i += 2
            continue
        out += old_u2a(u)
        i += 1
    return bytes(out)


def u2a_agree(name, us, expect_changed=None):
    data = units(us)
    res = []
    ok = True
    for form in FORMS:
        rc, got = rn.new.run("uni2acii", data, args=("-f", form))
        exp = model_u2a(us, form)
        ok &= rc == 0 and got == exp
        res.append("%s: %s" % (form, "model agrees" if got == exp else "MODEL DISAGREES (%d vs %d bytes)" % (len(got), len(exp))))
    check("%s: %d code units; %s" % (name, len(us), "; ".join(res)), ok)


u2a_agree("random streams", [rng.choice(HOT_U) if rng.random() < 0.85 else rng.choice(ANY_U) for _ in range(count * 7)])
u2a_agree("exhaustive pairs", [u for x in HOT_U for y in HOT_U for u in (x, y, 0x000A)])
SMALL = [0x0929, 0x0928, 0x093C, 0x094D, 0x00C6, 0x0931, 0x0930, 0x0934, 0x0933, 0x095C, 0x0921, 0x000A]
u2a_agree("exhaustive triples of %d code units" % len(SMALL), [u for x in SMALL for y in SMALL for z in SMALL for u in (x, y, z, 0x000A)])
check("a low-byte character is not a consonant: Æ (U+00C6, low byte C6) followed by U+093C is C6 E9 in every form, never C7",
      all(rn.new.u2a("Æ" + NUKTA, f) == b"\xc6\xe9" for f in FORMS))

# ------------------------------------------------------------------------------------------------ (f)
print("(f) independent oracles: Python's NFC and NFD")
CCC = {b: unicodedata.combining(OLD_TEXT[b]) for b in NOLF}
print("    combining classes among the bytes: %s" % ", ".join("%d: %s" % (c, " ".join("%02X" % b for b in NOLF if CCC[b] == c)) for c in sorted(set(CCC.values()) - {0})))


def in_canonical_order(line):
    """no mark of a lower combining class directly after a mark of a higher one; NFC and NFD reorder such marks, and neither the
    converters nor the layer ever reorder anything"""
    return not any(CCC[b] != 0 and CCC[a] > CCC[b] for a, b in zip(line, line[1:]))


domain = [l for l in rand_lines if in_canonical_order(l)]
data = b"".join(l + b"\n" for l in domain)
l0 = rn.mid.a2u(data).split("\n")[:-1]
for form, norm in (("nfc", NFC), ("nfd", NFD)):
    lf = rn.new.a2u(data, form).split("\n")[:-1]
    diff = sum(a != norm(b) for a, b in zip(lf, l0))
    check("acii2uni -f %s writes %s of what the build without the layer writes, on %d of %d random streams (the others have marks out of canonical order); disagreements: %d"
          % (form, form.upper(), len(domain), len(rand_lines), diff), len(lf) == len(l0) == len(domain) and diff == 0 and len(domain) > count // 2)
    neg = sum(a != norm(a) for a in l0)
    check("negative control: the build without the layer is not in %s on %d of those streams, so this oracle can fail" % (form.upper(), neg), neg > count // 100)
l_asis = rn.new.a2u(data).split("\n")[:-1]
check("acii2uni's default (asis) is neither: it equals the build without the layer on all of them, in NFC on %d and in NFD on %d of them"
      % (sum(a == NFC(a) for a in l_asis), sum(a == NFD(a) for a in l_asis)), l_asis == l0)
outside = [l for l in rand_lines if not in_canonical_order(l)]
odata = b"".join(l + b"\n" for l in outside)
o0 = rn.mid.a2u(odata).split("\n")[:-1]
for form, norm in (("nfc", NFC), ("nfd", NFD)):
    of = rn.new.a2u(odata, form).split("\n")[:-1]
    model_ok = all(a == model_a2u(l, form) for a, l in zip(of, outside))
    nfx_differs = sum(a != norm(b) for a, b in zip(of, o0))
    nukta_after = sum(1 for l in outside if any(CCC[a] > CCC[NB] and b == NB for a, b in zip(l, l[1:])))
    check("the limit, %s: on the %d streams with marks out of canonical order (%d of them a nukta after a halant or an accent) the form is the model's; %s would reorder, and differs on %d"
          % (form, len(outside), nukta_after, form.upper(), nfx_differs), model_ok and nfx_differs > 0 and nukta_after > 0)
canon_u = []
for _ in range(count):
    seq = [rng.choice(LET + CONS + [0x093C, 0x093C, 0x094D, 0x0951, 0x093E, 0x093F, 0x0061, 0x0020, 0x000A, 0x0915]) for _ in range(rng.randint(2, 8))]
    if all(not (unicodedata.combining(chr(b)) != 0 and unicodedata.combining(chr(a)) > unicodedata.combining(chr(b))) for a, b in zip(seq, seq[1:])):
        canon_u.append(seq)
for form, norm in (("nfc", NFC), ("nfd", NFD)):
    bad = 0
    for k in range(0, len(canon_u), 500):                       # in blocks, so that one call converts many strings
        block = canon_u[k:k + 500]
        text = "\n".join("".join(map(chr, s)) for s in block)
        got = rn.new.u2a(text, form)
        want = rn.new.u2a(norm(text))                           # the bytes that asis writes for the NFC / NFD of the input
        bad += got != want
    check("uni2acii -f %s writes the bytes that asis writes for the %s of the input, on %d random strings in canonical order; blocks that disagree: %d"
          % (form, form.upper(), len(canon_u), bad), bad == 0 and len(canon_u) > count // 4)
check("negative control: uni2acii's asis is not that on the same strings (the pair and the single code point differ)",
      rn.new.u2a("ऩ") != rn.new.u2a(NFC("ऩ")) and rn.new.u2a("ऩ") != rn.new.u2a(NFD("ऩ")))

# ------------------------------------------------------------------------------------------------ (g)
print("(g) uni2acii on the BMP")
rest = [u for u in range(0x10000) if u not in LAYER]
data_rest = units(rest)
n_mid = rn.mid.run("uni2acii", data_rest)
for form in FORMS:
    n_new = rn.new.run("uni2acii", data_rest, args=("-f", form))
    check("form %-4s: all %d code units of U+0000-U+FFFF but the eleven letters: the new build writes exactly the bytes of the build with patch 0001 alone (%d bytes)"
          % (form, len(rest), len(n_mid[1])), n_new[0] == n_mid[0] == 0 and n_new[1] == n_mid[1])
check("... and of the eleven letters, asis changes the nine (two bytes now, the low byte before); the two with a row keep their byte",
      all(rn.mid.u2a(chr(cp)) == bytes([cp & 255]) and len(rn.new.u2a(chr(cp))) == 2 for cp in NINE)
      and all(rn.new.u2a(chr(cp)) == rn.mid.u2a(chr(cp)) for cp in LAYER if cp in UNI))
check("... nfd changes all eleven: each is the consonant and E9", all(rn.new.u2a(chr(cp), "nfd") == bytes([UNI[LAYER[cp][0]], NB]) for cp in LAYER))
check("D3 is never written for one of the eleven letters, in any form, single or as a pair",
      all(0xD3 not in rn.new.u2a(t, f) for f in FORMS for cp in LAYER for t in (chr(cp), chr(LAYER[cp][0]) + NUKTA)))

# ------------------------------------------------------------------------------------------------ (h)
print("(h) the edge cases")
K = {n: bytes([UNI[b]]) for n, b in (("na", 0x0928), ("ra", 0x0930), ("lla", 0x0933), ("ka", 0x0915), ("nnna", 0x0929), ("halant", 0x094D), ("aa", 0x093E))}
E = bytes([NB])
P = NUKTA
EDGE = [   # what, ACII bytes, {form: text}; a dict of one entry stands for all three
    ("a consonant at the end of the stream, no newline", K["na"], "न"),
    ("a consonant before a newline", K["na"] + b"\n", "न\n"),
    ("a consonant before another consonant", K["na"] + K["ka"], "नक"),
    ("NA NA E9: only the second has a nukta", K["na"] + K["na"] + E, {"asis": "नन" + P, "nfc": "नऩ", "nfd": "नन" + P}),
    ("NA E9 E9: the second E9 stands alone", K["na"] + E + E, {"asis": "न" + P + P, "nfc": "ऩ" + P, "nfd": "न" + P + P}),
    ("E9 alone, and E9 after a newline", E + b"\n" + E, P + "\n" + P),
    ("NNNA (the byte C7) + E9: the byte with its own row is not a consonant", K["nnna"] + E,
     {"asis": "ऩ" + P, "nfc": "ऩ" + P, "nfd": "न" + P + P}),
    ("NA, newline, E9: the newline ends the held byte", K["na"] + b"\n" + E, "न\n" + P),
    ("NA, halant, E9: ISCII's E8 E9, not a nukta of NA", K["na"] + K["halant"] + E, "न्" + P),
    ("NA, vowel sign AA, E9: a vowel sign between", K["na"] + K["aa"] + E, "ना" + P),
    ("RA E9 and LLA E9", K["ra"] + E + K["lla"] + E, {"asis": "र" + P + "ळ" + P, "nfc": "ऱऴ", "nfd": "र" + P + "ळ" + P}),
    ("KA E9: a composition exclusion, a pair in every form", K["ka"] + E, "क" + P),
    ("C7 and D0 alone: the two letters that have a byte", b"\xc7\xd0", {"asis": "ऩऱ", "nfc": "ऩऱ", "nfd": "न" + P + "र" + P}),
]
for what, data, want in EDGE:
    want = want if isinstance(want, dict) else {f: want for f in FORMS}
    got = {f: rn.new.a2u(data, f) for f in FORMS}
    check("%-72s %-24s -> %s" % (what, hexs(data).replace("0A", "LF"), " | ".join("%s %s" % (f, cps(got[f]).replace("U+000A", "LF")) for f in FORMS if got[f] != want["asis"] or f == "asis")),
          got == want)
check("an empty input gives the byte order mark and nothing else", all(rn.new.run("acii2uni", b"", args=("-f", f)) == (0, b"\xff\xfe") for f in FORMS))
check("both converters print their usage line when called with one file name", all(subprocess.run(
    [os.path.join(config.NEW, prog), "x"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.startswith(b"Usage: " + prog.encode())
    for prog in ("acii2uni", "uni2acii")))
NA, NNNA, RA_, RRA, LA_, LLLA, KA_ = 0x0928, 0x0929, 0x0930, 0x0931, 0x0933, 0x0934, 0x0915
EDGE_U = [   # what, code units, {form: ACII bytes}
    ("NA at the end of the stream: the consonant that waited is written", [NA], b"\xc6"),
    ("NA + nukta at the end of the stream", [NA, 0x093C], {"asis": b"\xc6\xe9", "nfc": b"\xc7", "nfd": b"\xc6\xe9"}),
    ("NA, newline, nukta: the newline ends the wait", [NA, 0x0A, 0x093C], b"\xc6\x0a\xe9"),
    ("NA NA nukta: only the second has a nukta", [NA, NA, 0x093C], {"asis": b"\xc6\xc6\xe9", "nfc": b"\xc6\xc7", "nfd": b"\xc6\xc6\xe9"}),
    ("NA + nukta + nukta: the second nukta stands alone", [NA, 0x093C, 0x093C], {"asis": b"\xc6\xe9\xe9", "nfc": b"\xc7\xe9", "nfd": b"\xc6\xe9\xe9"}),
    ("RA + nukta, LLA + nukta", [RA_, 0x093C, LA_, 0x093C], {"asis": b"\xcf\xe9\xd2\xe9", "nfc": b"\xd0\xd2\xe9", "nfd": b"\xcf\xe9\xd2\xe9"}),
    ("NA + halant + nukta: not composed in any form", [NA, 0x094D, 0x093C], b"\xc6\xe8\xe9"),
    ("NA + vowel sign AA + nukta", [NA, 0x093E, 0x093C], b"\xc6\xda\xe9"),
    ("KA + nukta: a composition exclusion", [KA_, 0x093C], b"\xb3\xe9"),
    ("U+0929 and U+0931", [NNNA, RRA], {"asis": b"\xc7\xd0", "nfc": b"\xc7\xd0", "nfd": b"\xc6\xe9\xcf\xe9"}),
    ("U+0934 and U+095C: written as the consonant and E9 in every form", [LLLA, 0x095C], b"\xd2\xe9\xbf\xe9"),
    ("a consonant, then a low-byte character (U+00E9), then a nukta: the é is not the nukta", [NA, 0x00E9, 0x093C], {"asis": b"\xc6\xe9\xe9", "nfc": b"\xc6\xe9\xe9", "nfd": b"\xc6\xe9\xe9"}),
]
for what, us, want in EDGE_U:
    want = want if isinstance(want, dict) else {f: want for f in FORMS}
    got = {f: rn.new.run("uni2acii", units(us), args=("-f", f))[1] for f in FORMS}
    check("%-76s -> %s" % (what, " | ".join("%s %s" % (f, hexs(got[f])) for f in FORMS if got[f] != want["asis"] or f == "asis")), got == want)

# ------------------------------------------------------------------------------------------------ (i)
print("(i) the warning layer of uni2acii")
WTEXT = "aéb’éन क़।"
wdata = b"\xff\xfe" + WTEXT.encode("utf-16-le")
rc0, out0, err0 = rn.new.run3("uni2acii", wdata)
check("by default nothing is reported: stderr is empty, exit status %d" % rc0, rc0 == 0 and err0 == b"")
for label, args, env in (("-w", ("-w",), None), ("--warn", ("--warn",), None), ("ROMENAGRI_NUKTA_WARN=1", (), {"ROMENAGRI_NUKTA_WARN": "1"}),
                         ("-w and -f nfd", ("-w", "-f", "nfd"), None)):
    rc, out, err = rn.new.run3("uni2acii", wdata, args=args, env=env)
    lines = err.decode().splitlines()
    warns = [l for l in lines if ": warning: " in l]
    e_acute = [l for l in warns if "U+00E9" in l]
    same = out == rn.new.run("uni2acii", wdata, args=("-f", "nfd") if "nfd" in args else ())[1]
    check("%-24s: exit status %d, the bytes are those of the run without it: %s; %d warnings, one for U+00E9 (%s) and one for U+2019; a note and a count" %
          (label, rc, same, len(warns), "the nukta byte" if e_acute and "nukta byte" in e_acute[0] else "?"),
          rc == 0 and same and len(warns) == 2 and len(e_acute) == 1 and "nukta byte" in e_acute[0] and any("U+2019" in l for l in warns)
          and sum(1 for l in lines if ": note: " in l) == 1 and "2 code points" in lines[-1] and "were written as low bytes" in lines[-1] and "(1 further occurrence not listed)" in lines[-1])
rc, out, err = rn.new.run3("uni2acii", wdata, env={"ROMENAGRI_NUKTA_WARN": "0"})
check("ROMENAGRI_NUKTA_WARN=0 reports nothing", err == b"")
rc, out, err = rn.new.run3("uni2acii", units([0x0928, 0x093C, 0x0915, 0x0905, 0x0041, 0x000A, 0x0964]), args=("-w",))
check("-w on Devanagari, ASCII and a newline (everything unicode.h maps or ASCII): no warning", err == b"")
rc, out, err = rn.new.run3("uni2acii", units([0x00E9, 0x00E9, 0x00E9]), args=("-w",))
check("the same code point three times is reported once, and the count says so: %s" % err.decode().splitlines()[-1][:120],
      err.decode().count(": warning: ") == 1 and "1 code point with no ACII byte was written as its low byte (2 further occurrences not listed)" in err.decode())

# ------------------------------------------------------------------------------------------------ (j)
print("(j) the whole chain, every form")


def chain(t, text, form=None):
    a = t.u2a(text, form) if form else t.u2a(text)
    rc, back = t.r2a(t.a2r(a))
    return a, rc, ((t.a2u(back, form) if form else t.a2u(back)).lstrip("﻿") if rc == 0 else None)


def asis_expect(text):
    """what the default chain writes: a letter that unicode.h has no row for becomes its consonant and a nukta; the rest stays as it came"""
    return "".join(chr(LAYER[ord(c)][0]) + NUKTA if ord(c) in LAYER and ord(c) not in UNI else c for c in text)


NORM = {"asis": asis_expect, "nfc": NFC, "nfd": NFD}
each = {f: [] for f in FORMS}
for cp, (base, m) in LAYER.items():
    for spelling in (chr(cp), chr(base) + NUKTA):
        for text in (spelling, "क" + spelling + "ा", "न्" + spelling):
            for form in FORMS:
                a, rc, out = chain(rn.new, text, form)
                each[form].append(out == NORM[form](text))
for form in FORMS:
    check("form %-4s: the eleven letters, each as the single code point and as consonant + nukta, alone, with a consonant before and an aa sign after, and with a halant before:"
          " %d of %d come out as %s" % (form, sum(each[form]), len(each[form]), {"asis": "the input, but the nine as consonant + nukta", "nfc": "NFC of the input",
                                                                             "nfd": "NFD of the input"}[form]), all(each[form]))
mids = [chain(rn.mid, chr(cp))[2] == NFD(chr(cp)) for cp in NINE]
check("negative control: with patch 0001 alone, %d of the nine single code points come out as consonant + nukta" % sum(mids), sum(mids) == 0)

# the fifteen clusters of section 11.3, in Unicode.  DDA + nukta is written in the two spellings a keyboard may produce.
CLUSTERS = [("त्व", "त्व"), ("द्व", "द्व"), ("ट्व", "ट्व"), ("ड्व", "ड्व"),
            ("ड़्व (U+0921 U+093C)", "ड़्व"), ("ड़्व (U+095C)", "ड़्व"),
            ("ऱ्व", "ऱ्व"), ("ग्व", "ग्व"), ("च्व", "च्व"), ("ज्व", "ज्व"),
            ("क्व", "क्व"), ("प्व", "प्व"), ("ब्व", "ब्व"), ("स्व", "स्व"),
            ("ल्ह", "ल्ह"), ("ऱ्ह", "ऱ्ह")]
for form in FORMS:
    bad = []
    for label, text in CLUSTERS:
        a, rc, out = chain(rn.new, text, form)
        if out != NORM[form](text):
            bad.append((label, rc, out))
    check("form %-4s: the 15 clusters of section 11.3 (13 with व, 2 with ह; DDA + nukta in both spellings, so 16 strings): %d of %d come out as %s" %
          (form, len(CLUSTERS) - len(bad), len(CLUSTERS), "the input (the single code point U+095C as consonant + nukta)" if form == "asis" else form.upper() + " of the input"),
          not bad, str(bad))
oldfail = [label for label, text in CLUSTERS if chain(rn.old, text)[2] != NFD(text)]
check("negative control: on the unpatched build they fail for %s" % (", ".join(oldfail) or "none"), "ड़्व (U+095C)" in oldfail)
midfail = [label for label, text in CLUSTERS if chain(rn.mid, text)[2] != NFD(text)]
check("negative control: with patch 0001 alone they fail for %s" % (", ".join(midfail) or "none"), "ड़्व (U+095C)" in midfail)

# ------------------------------------------------------------------------------------------------ (k)
print("(k) the cases of section 15.7  (input -> ACII -> Romenagri -> output, in each form; the same form on both converters)")


def show(tag, what, text, wants, build=None, via_rmn=True, note=""):
    """one asserted case: the text goes through uni2acii, (acii2rmn, rmn2acii,) acii2uni, in each form; wants[form] is the text that must come out"""
    t = build or rn.new
    print("    %-3s %s" % (tag, what))
    print("        in: %s   %s%s" % (text, cps(text), ("   " + note) if note else ""))
    for form in (FORMS if build is None else ("asis",)):
        a = t.u2a(text, form) if build is None else t.u2a(text)
        if via_rmn:
            rc, back = t.r2a(t.a2r(a))
            rmn = "`" + t.a2r(a).decode("latin-1").replace("\r\n", " / ").replace("\n", " / ").strip() + "`"
            out = (t.a2u(back, form) if build is None else t.a2u(back)).lstrip("﻿") if rc == 0 else None
        else:
            rmn = "(not run)"
            out = (t.a2u(a, form) if build is None else t.a2u(a)).lstrip("﻿")
        print("        %-4s ACII %-26s Romenagri %-22s -> %s   %s" % (form, hexs(a), rmn, out, cps(out or "")))
        check("      %s expected: %s" % (form, cps(wants[form])), out == wants[form])


KA, NA_, RA, LLA, HALANT, SIGN_I, SIGN_AA, VA, E_ACUTE = "क", "न", "र", "ळ", "्", "ि", "ा", "व", "é"
eight = "".join(chr(cp) for cp, (b, m) in LAYER.items() if m == 0)
eight_pairs = NFD(eight)
three = "ऩऱऴ"
three_pairs = NA_ + NUKTA + RA + NUKTA + LLA + NUKTA
same = lambda t: {f: t for f in FORMS}

print("    C1  one letter in two spellings, and the eight composition exclusions: the rule is Level 1, a consonant and a nukta; no form writes the eight as single code points")
show("C1", "the single code point ड़ (U+095C)", "ड़", same(NFD("ड़")))
show("C1", "ड + nukta, the sequence a keyboard produces", "ड़", same(NFD("ड़")))
show("C1", "all eight: क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़ (U+0958-U+095F)", eight, same(eight_pairs))
print("    C2  ऩ ऱ ऴ: Unicode gave them code points and not the others; in the layer they are a consonant and a nukta like the rest")
show("C2", "the single code points", three, {"asis": "ऩऱ" + LLA + NUKTA, "nfc": three, "nfd": three_pairs})
show("C2", "consonant + nukta, three times", three_pairs, {"asis": three_pairs, "nfc": three, "nfd": three_pairs})
check("      C7 is %s in asis and nfc and %s in nfd; C6 E9 is %s in asis and nfd and %s in nfc" %
      (cps(rn.new.a2u(b"\xc7")), cps(rn.new.a2u(b"\xc7", "nfd")), cps(rn.new.a2u(b"\xc6\xe9")), cps(rn.new.a2u(b"\xc6\xe9", "nfc"))),
      rn.new.a2u(b"\xc7") == rn.new.a2u(b"\xc7", "nfc") == "ऩ" and rn.new.a2u(b"\xc7", "nfd") == NA_ + NUKTA and
      rn.new.a2u(b"\xc6\xe9") == rn.new.a2u(b"\xc6\xe9", "nfd") == NA_ + NUKTA and rn.new.a2u(b"\xc6\xe9", "nfc") == "ऩ")
check("      D0 is %s in asis and nfc and %s in nfd; CF E9 is %s in asis and nfd and %s in nfc" %
      (cps(rn.new.a2u(b"\xd0")), cps(rn.new.a2u(b"\xd0", "nfd")), cps(rn.new.a2u(b"\xcf\xe9")), cps(rn.new.a2u(b"\xcf\xe9", "nfc"))),
      rn.new.a2u(b"\xd0") == rn.new.a2u(b"\xd0", "nfc") == "ऱ" and rn.new.a2u(b"\xd0", "nfd") == RA + NUKTA and
      rn.new.a2u(b"\xcf\xe9") == rn.new.a2u(b"\xcf\xe9", "nfd") == RA + NUKTA and rn.new.a2u(b"\xcf\xe9", "nfc") == "ऱ")
check("      typed in Romenagri: nza is C6 E9 and _nza is C7 (acii2rmn writes them so); with uni2acii -f nfd the single code point U+0929 is `nza`, as the pair is",
      rn.new.a2r(b"\xc6\xe9").strip() == b"nza" and rn.new.a2r(b"\xc7").strip() == b"_nza" and rn.new.a2r(rn.new.u2a("ऩ", "nfd")).strip() == b"nza"
      and rn.new.a2r(rn.new.u2a("ऩ")).strip() == b"_nza")
print("    C3  a nukta after a halant is not rebuilt in any form: न् + nukta")
show("C3", "न + halant + nukta  (NFC and NFD reorder it before the halant; E8 E9 is ISCII's soft halant, so the layer leaves it alone: no decision taken)",
     NA_ + HALANT + NUKTA, same(NA_ + HALANT + NUKTA), via_rmn=False, note="NFC: %s" % cps(NFC(NA_ + HALANT + NUKTA)))
rc_halant = rn.new.run("acii2rmn", b"\xc6\xe8\xe9")[0]
check("      and acii2rmn cannot carry a halant + nukta on to Romenagri: C6 E8 E9 gives exit status %d (section 11.4, unchanged by the layer)" % rc_halant,
      rc_halant < 0 or rc_halant >= 128)
print("    C4  a nukta that does not follow a consonant directly is nothing to rebuild; the form of the output is the user's (flag, environment, macro, function)")
show("C4", "न + sign I + nukta  (NFC does not compose it either)", NA_ + SIGN_I + NUKTA, same(NA_ + SIGN_I + NUKTA), via_rmn=False)
show("C4", "न + space + nukta", NA_ + " " + NUKTA, same(NA_ + " " + NUKTA), via_rmn=False)
print("    C5  an e with an acute accent is written by uni2acii as its low byte E9, and E9 is the nukta: a character with no ACII byte is treated as any other such character; -w reports it")
show("C5", "नé: the é is not a nukta in the input; the byte E9 is read as one, as before the layer (asis: न and a nukta)",
     NA_ + E_ACUTE, {"asis": NA_ + NUKTA, "nfc": "ऩ", "nfd": NA_ + NUKTA}, note="the low-byte problem of section 11.6, not new")
rc, out, err = rn.new.run3("uni2acii", units([0x0928, 0x00E9]), args=("-w",))
print("        uni2acii -w on it, stderr: %s" % " / ".join(err.decode().splitlines()))
check("      with -w: a note, the warning for U+00E9 (the nukta byte) and a count; without -w: nothing",
      b"U+00E9" in err and b"nukta byte" in err and rn.new.run3("uni2acii", units([0x0928, 0x00E9]))[2] == b"")
print("    C6  the cluster ड़्व of section 11.3 with the single code point U+095C: not a case of its own; the rule of C1 gives it a consonant and a nukta before the halant is bound")
show("C6", "with the layer", "ड़" + HALANT + VA, same(NFD("ड़") + HALANT + VA))
show("C6", "ड + nukta + halant + व", "ड़" + HALANT + VA, same("ड़" + HALANT + VA))
show("C6", "patch 0001 alone: 5C is a backslash, and the Romenagri filter loses the ड़् altogether", "ड़" + HALANT + VA, {"asis": VA},
     build=rn.mid, note="what it did before")
print("    C7  ऴ has no byte of its own: ळ + nukta, D2 E9; ISCII's D3 stays unused in every form")
show("C7", "ऴ alone", "ऴ", {"asis": "ळ" + NUKTA, "nfc": "ऴ", "nfd": "ळ" + NUKTA})
show("C7", "in a word: कऴन", KA + "ऴ" + NA_, {"asis": KA + "ळ" + NUKTA + NA_, "nfc": KA + "ऴ" + NA_, "nfd": KA + "ळ" + NUKTA + NA_})
check("      D3 is written for none of these, and unicode.h has no row for it", all(0xD3 not in rn.new.u2a(t, f) for t in ("ऴ", KA + "ऴ" + NA_) for f in FORMS) and 0xD3 not in UNI.values())
print("    C8  the 15 reserved keys of section 11.3 are not touched: the Devanagari clusters are code points, passed through one for one; the typed keys still crash")
show("C8", "ऱ्ह and ल्ह, the two aspirate clusters", "ऱ" + HALANT + "ह" + "ल" + HALANT + "ह",
     {"asis": "ऱ" + HALANT + "ह" + "ल" + HALANT + "ह", "nfc": "ऱ" + HALANT + "ह" + "ल" + HALANT + "ह",
      "nfd": RA + NUKTA + HALANT + "ह" + "ल" + HALANT + "ह"})
for key in (b"lh", b"_rrh", b"_rdvr", b"tvr"):
    rc = rn.new.run("rmn2acii", key)[0]
    check("      the typed form %s (section 11.3) still crashes rmn2acii (exit status %d)" % (key.decode(), rc), rc < 0 or rc >= 128)

shutil.rmtree(TMP, ignore_errors=True)
print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
