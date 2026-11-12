# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""The extension recipes of TRANSLITERATION.md, section 8, carried out on scratch copies of the patched tree.

    python3 tests/test_extension_recipes.py

R1  table-only extension (recipe A): U+0934 DEVANAGARI LETTER LLLA gets the byte D3 -- ISCII's own code for "Consonant ZHA" -- and
    the key `lha`, which the parser already asks for (section 11.3) but the table lacks.  Only the three tables change.  Checked:
    the lint finds no error; the rebuilt library maps `lha` to D3 (the patched library crashes on it); the converters and the filter
    pair round-trip it; and no other input changes its result (all strings up to length 3, and every table key, give the same output
    as before unless they contain `lh`).  The row is an ILLUSTRATION: it is not part of the shipped tables (section 10.4).
R2  a key the parser cannot read (a new family letter without a parser branch): the lint must report ERROR T6.
R3  the other mistakes the lint exists for: a repeated key, a repeated byte, a key outside [a-z_], a table length that was not updated.

Exit status 1 if any expectation fails.  Everything is built under build/recipes (override with RMN_BUILD)."""
import itertools
import os
import re
import shutil
import subprocess
import sys

import config
import model
import rmn_tables

CRLF = b"\r\n"
TOOLS = os.path.join(config.ROOT, "tools")
fail = False


def check(name, ok, detail=""):
    global fail
    fail |= not ok
    print("    %-4s %s%s" % ("ok" if ok else "FAIL", name, ("  (%s)" % detail) if detail else ""))


def scratch(tag):
    """a copy of the patched tree, without objects, to edit and rebuild"""
    d = os.path.join(config.BUILD, "recipes", tag)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copytree(config.need(config.NEW), d)
    for f in os.listdir(d):
        if f.endswith(".o") or f in ("librmnagri.a", "lexyy.c"):
            os.remove(os.path.join(d, f))
    return d


def add_rows(path, macro, rows, bump):
    """append rows (each given without its trailing comma) after the last row of the table and, if bump, raise the declared length"""
    data = open(path, "rb").read()
    if bump:
        m = re.search(rb"#define\s+" + macro + rb"\s+(\d+)", data)
        data = data[:m.start(1)] + str(int(m.group(1)) + len(rows)).encode() + data[m.end(1):]
    end = data.rindex(b"};")
    last = data.rindex(b"}", 0, end)                       # the brace that closes the last row
    eol = data.index(CRLF, last) + 2                       # the rest of that line (a comment) stays with it
    lines = [(r + ("," if i < len(rows) - 1 else "")).encode("latin-1") + CRLF for i, r in enumerate(rows)]
    open(path, "wb").write(data[:last + 1] + b"," + data[last + 1:eol] + b"".join(lines) + data[eol:])


def edit_tables(d, uni=(), acii=(), hin=(), bump=True):
    """uni = [(code point, byte)], acii = [(key, byte)], hin = [(key, byte)]"""
    if uni:
        add_rows(os.path.join(d, "unicode.h"), b"UNI_LEN",
                 ["    {%d, %d, '\\x%02X'} //illustration" % (cp & 255, cp >> 8, b) for cp, b in uni], bump)
    if acii:
        add_rows(os.path.join(d, "acii.h"), b"ACII_LEN", ['{"%s", "\\x%02X"} //illustration' % t for t in acii], bump)
    if hin:
        add_rows(os.path.join(d, "aciihin.h"), b"ACII_HIN_LEN", ['    {"%s", "\\x%02X"} //illustration' % t for t in hin], bump)


def lint(d, *extra):
    p = subprocess.run([sys.executable, os.path.join(TOOLS, "check_tables.py"), d, *extra], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def build(d):
    subprocess.run(["make", "librmnagri"], cwd=d, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    subprocess.run(["gcc", "-O1", "-I", d, "-o", os.path.join(d, "h"), os.path.join(config.ROOT, "tests", "harness.c"),
                    os.path.join(d, "librmnagri.a")], check=True)
    for prog in ("uni2acii", "acii2uni"):
        subprocess.run(["gcc", "-o", os.path.join(d, prog), os.path.join(d, prog + ".c")], check=True)


def harness(h, mode, lines):
    args = [h] + ([mode] if mode else [])
    return subprocess.run(args, input=("\n".join(lines) + "\n").encode(), stdout=subprocess.PIPE).stdout.decode().split("\n")[:-1]


# ------------------------------------------------------------------------------------------------------------------ R1
print("R1  table-only extension: U+0934 LLLA = byte D3 = key `lha`")
d = scratch("r1")
names = rmn_tables.iscii_names(d)
check("D3 is ISCII's 'Consonant ZHA'", names.get(0xD3, "").startswith("Consonant ZHA"), names.get(0xD3, ""))
T_before = model.parse_table(d)
h_before = config.need(config.H_NEW)
check("`lha` is a key the parser asks for and the patched table lacks", "lha" not in T_before)
before = harness(h_before, "", ["lha", "lh"])
check("the patched library crashes on `lha` and on `lh`", before == ["SEGV", "SEGV"], " ".join(before))
rc, text = lint(d, "--free")
check("D3 is listed as a free byte before the edit", re.search(r"0xD3 ", text.split("Free bytes")[1]) is not None)
edit_tables(d, uni=[(0x0934, 0xD3)], acii=[("lha", 0xD3)], hin=[("lha", 0xD3)])
rc, text = lint(d, "--free")
check("lint: no error", rc == 0, [l for l in text.splitlines() if "error(s)" in l][-1])
check("D3 is no longer listed as free", re.search(r"0xD3 ", text.split("Free bytes")[1]) is None)
build(d)
h = os.path.join(d, "h")
after = harness(h, "", ["lha", "lh", "lhaa", "kalha"])
check("`lha` -> D3, `lh` -> D3 + halant, `lhaa` -> D3 + sign AA, `kalha` -> KA, LHA",
      after == ["d3", "d3e8", "d3da", "b3d3"], " ".join(after))
rt = harness(h, "-f", ["d3", "d1d3", "b3e8d3", "d3dbd1"])
check("filter round trip: D3 | LA LHA | KA halant LHA | LHA sign-I LA", rt == ["d3", "d1d3", "b3e8d3", "d3dbd1"], " ".join(rt))
u2a = subprocess.run([os.path.join(d, "uni2acii")], input=b"\xff\xfe\x34\x09", stdout=subprocess.PIPE).stdout
a2u = subprocess.run([os.path.join(d, "acii2uni")], input=b"\xd3", stdout=subprocess.PIPE).stdout
check("uni2acii: U+0934 -> D3", u2a == b"\xd3", u2a.hex())
check("acii2uni: D3 -> U+0934", a2u == b"\xff\xfe\x34\x09", a2u.hex())
alpha = "abcdefghijklmnopqrstuvwxyz_^|"
strings = [k for k in T_before if k] + ["".join(t) for n in (1, 2, 3) for t in itertools.product(alpha, repeat=n)]
r_old, r_new = harness(h_before, "", strings), harness(h, "", strings)
moved = [s for s, a, b in zip(strings, r_old, r_new) if a != b]
check("%d strings compared: results differ only on strings that contain `lh`" % len(strings),
      all("lh" in s for s in moved) and len(moved) > 0, "%d differ, all with lh: %s" % (len(moved), all("lh" in s for s in moved)))

# ------------------------------------------------------------------------------------------------------------------ R2
print("R2  a key without a parser branch is caught (T6)")
d = scratch("r2")
edit_tables(d, uni=[(0x0972, 0x8D)], acii=[("_ka", 0x8D)])
rc, text = lint(d)
check("lint reports ERROR T6 for `_ka` (the parser reads it as the text `ka`)", rc == 1 and re.search(r"ERROR\s+T6 key '_ka' parses to 6b61", text) is not None)

# ------------------------------------------------------------------------------------------------------------------ R3
print("R3  repeated key, repeated byte, bad alphabet, stale length")
d = scratch("r3a")
edit_tables(d, uni=[(0x0972, 0x8D)], acii=[("_li", 0x8D)])
rc, text = lint(d)
check("a repeated key `_li`: ERROR T4", rc == 1 and re.search(r"ERROR\s+T4 key '_li' appears", text) is not None)
d = scratch("r3b")
edit_tables(d, uni=[(0x0972, 0x81)])
rc, text = lint(d)
check("a byte given to two code points (81): ERROR T4", rc == 1 and re.search(r"ERROR\s+T4 ACII byte 0x81 is given to both", text) is not None)
d = scratch("r3c")
edit_tables(d, uni=[(0x0972, 0x8D)], acii=[("_k1", 0x8D)])
rc, text = lint(d)
check("a key with a digit: ERROR T3", rc == 1 and re.search(r"ERROR\s+T3 key '_k1'", text) is not None)
d = scratch("r3d")
edit_tables(d, acii=[("lha", 0x8D)], bump=False)
rc, text = lint(d)
check("a table length that was not updated: ERROR T1", rc == 1 and re.search(r"ERROR\s+T1 ACII_LEN", text) is not None)

print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
