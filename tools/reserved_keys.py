#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""The keys that the parser asks for and the table lacks (TRANSLITERATION.md, section 11.3), and what the real parser does with them.

    python3 tools/reserved_keys.py <Romenagri dir> [--strict] [--no-diff]

Reads the grammar of the document in <Romenagri dir>/TRANSLITERATION.md and the table <Romenagri dir>/acii.h, works out every key that
the grammar can ask for, and lists those without a row, with the typed form that makes the parser ask for each (`kvr` asks for `kvra`,
`lh` asks for `lha`) and what the C parser does with that form today.  Then, unless --no-diff is given, it runs every string of at
most three letters over a-z and _ through the C parser and through the grammar, and reports every disagreement outside the missing
rows: a fix to rmn2acii.c or to the table that is not matched by a change of the grammar block shows up there.

The directory is copied to a scratch directory and built there (gcc and make; flex is not needed); it is never changed.
Exit status 1 if the build fails or the C parser and the grammar disagree.  With --strict also 1 while any key is still missing, so that
the script can serve as the check of a fix:  it passes when all of them are closed (by rows, or by a change of the parser).
"""
import itertools
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "tests"))
import model  # noqa: E402
import spec_model  # noqa: E402


def typed_form(key):
    """what a person types to make the parser ask for this key: the stem and the letter that selects it"""
    if key.endswith("vra"):
        return key[:-3] + "vr"
    if key.endswith("ha"):
        return key[:-2] + "h"
    return key


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    strict, diff = "--strict" in argv, "--no-diff" not in argv
    d = os.path.abspath(args[0])
    doc = os.path.join(d, "TRANSLITERATION.md")
    for f in ("acii.h", "rmn2acii.c", "TRANSLITERATION.md"):
        if not os.path.exists(os.path.join(d, f)):
            sys.exit("%s is not a Romenagri directory with a TRANSLITERATION.md (no %s)" % (d, f))
    spec = spec_model.load_doc(doc)
    T = model.parse_table(d)
    stems = {}
    keys = spec_model.lookup_keys(spec, True, stems)
    missing = sorted(k for k in keys if k not in T)
    print("%s: the grammar can ask for %d keys; %d have no row in acii.h" % (d, len(keys), len(missing)))

    work = tempfile.mkdtemp(prefix="rmn_reserved_")
    try:
        tree = os.path.join(work, "Romenagri")
        shutil.copytree(d, tree)
        for f in os.listdir(tree):
            if f.endswith(".o") or f in ("librmnagri.a", "lexyy.c"):
                os.remove(os.path.join(tree, f))
        for cmd in (["make", "librmnagri"],
                    ["gcc", "-O1", "-I", tree, "-o", os.path.join(work, "harness"), os.path.join(HERE, "..", "tests", "harness.c"), os.path.join(tree, "librmnagri.a")]):
            p = subprocess.run(cmd, cwd=tree, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if p.returncode:
                print(p.stdout.decode(errors="replace"))
                print("the build failed: %s" % " ".join(cmd))
                return 1
        harness = os.path.join(work, "harness")

        def c_parse(strings):
            p = subprocess.run([harness], input=("\n".join(strings) + "\n").encode("latin-1"), stdout=subprocess.PIPE)
            out = p.stdout.decode().split("\n")[:-1]
            assert len(out) == len(strings)
            return [None if o == "SEGV" else bytes.fromhex(o) for o in out]

        names = {}
        for k, bs in T.items():
            if len(bs) == 1:
                names.setdefault(bs[0], k)

        def describe(bs):
            return "crash (SEGV): nothing is written" if bs is None else " ".join(names.get(b) and "%02X(%s)" % (b, names[b]) or "%02X" % b for b in bs) or "nothing"

        if missing:
            print("\n%-8s %-9s %s" % ("typed", "asks for", "what the C parser does with the typed form"))
            forms = [typed_form(k) for k in missing]
            for key, form, res in zip(missing, forms, c_parse(forms)):
                print("%-8s %-9s %s" % (form, key, describe(res)))
            ok = [k for k in sorted(T) if k.endswith("vra") and k not in missing]
            if ok:
                forms = [typed_form(k) for k in ok]
                print("\nthe rows of the same shape that do exist:")
                for key, form, res in zip(ok, forms, c_parse(forms)):
                    print("%-8s %-9s %s" % (form, key, describe(res)))
        else:
            print("nothing is missing: every key that the grammar asks for has a row")

        bad = 0
        if diff:
            strings = ["".join(t) for L in range(0, 4) for t in itertools.product("abcdefghijklmnopqrstuvwxyz_", repeat=L)]
            cres = c_parse(strings)
            agree = both_crash = overrun = 0
            shown = []
            for s, c in zip(strings, cres):
                try:
                    m = spec_model.spec_parse(spec, s, T, True)
                except model.Overrun:
                    overrun += 1
                    continue
                except model.Missing:
                    if c is None:
                        both_crash += 1
                    else:
                        bad += 1
                        shown.append((s, "grammar: missing row", "C: " + describe(c)))
                    continue
                if c == m:
                    agree += 1
                else:
                    bad += 1
                    shown.append((s, "grammar: " + describe(m), "C: " + describe(c)))
            print("\n%d strings of at most three letters over a-z and _: the C parser and the grammar agree on %d; both reach a missing row on %d; "
                  "%d read past the end of the input (undefined, not compared); they disagree on %d" % (len(strings), agree, both_crash, overrun, bad))
            for row in shown[:10]:
                print("   ", row)
            if bad:
                print("The grammar block of section 5.3 and rmn2acii.c must change together (section 11.3, last paragraph).")
        status = 1 if bad else 0
        if strict and missing:
            print("\n--strict: %d key(s) still missing" % len(missing))
            status = 1
        return status
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
