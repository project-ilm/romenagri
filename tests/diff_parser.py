# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Differential test of the Romenagri -> ACII parser: the real C parser (tests/harness.c; the library of the three builds: old, mid, new)
against two executable descriptions of it,

    spec   the formal grammar printed in Romenagri/TRANSLITERATION.md, section 5.3 (tests/spec_model.py reads it from the document)
    hand   the same parser written out by hand as ordinary Python (tests/handwritten_parser.py), an independent cross-check;
           RMN_SKIP_HANDWRITTEN=1 leaves it out (after an extension that has not been mirrored there, section 8)

The three builds are the unpatched Romenagri (old), the one with patch 0001 only, the Sanskrit characters (mid), and the one of this
package, with patch 0002 as well, the guards of section 14.7 (new).  The grammar has the rules of each patch tagged ('+' and '!'), so one
text describes all three.

    python3 tests/diff_parser.py [MAXLEN [NRANDOM [NKEYS]]]       default 3 20000 20000   (full run: 4 300000 200000)

Inputs: every string up to MAXLEN over  a-z _ ^ |  ;  NRANDOM random strings of length 5-12 biased towards the grammar's own
letters ; NKEYS random concatenations of 1-8 table keys (with and without their '^'), i.e. realistic long inputs that contain the
new tokens in context.  Strings on which the model says the C code reads past the terminator (undefined behaviour) are skipped.

Reported:  agreement of the C code with the spec and with the hand-written parser, for the old parser and for the new one; agreement
of spec and hand-written parser with each other (outcome for outcome, including "reads past the terminator" and "row missing");
every string whose result
changed between the old and the mid parser (each must contain one of the new tokens or the repaired avagraha string "_s"), and every
string whose result changed between the mid and the new parser (in each, the grammar must have applied a guard); and that the grammar
with the guards never reads past the end of a string (no string is skipped for the new build).
Exit status 1 on any disagreement or unexplained change."""
import itertools
import os
import random
import subprocess
import sys
import time

import config
import handwritten_parser
import model
import spec_model

ALPHA = "abcdefghijklmnopqrstuvwxyz_^|"
MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 3
NRANDOM = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
NKEYS = int(sys.argv[3]) if len(sys.argv) > 3 else 20000

SKIP_HAND = bool(os.environ.get("RMN_SKIP_HANDWRITTEN"))
T_old = model.parse_table(config.need(config.OLD))
T_mid = model.parse_table(config.need(config.MID))
T_new = model.parse_table(config.need(config.NEW))
SPEC = spec_model.load_doc()
print("table rows: old %d  mid %d  new %d" % (len(T_old), len(T_mid), len(T_new)))
print("grammar read from the document: %d states, %d rules (%d of them added by patch 0001, %d guards added by patch 0002)" % (
    len(SPEC.states), sum(len(r) for _, r in SPEC.states.values()), sum(x.tag == "+" for _, r in SPEC.states.values() for x in r),
    sum(x.tag == "!" for _, r in SPEC.states.values() for x in r)))


def strings():
    for L in range(1, MAXLEN + 1):
        for t in itertools.product(ALPHA, repeat=L):
            yield "".join(t)
    rnd = random.Random(20261016)
    weighted = "aaaeeiioouuhhzzmnnyywxrrggccttddppbbssllkkjjv___^|"            # biased towards the grammar's own letters
    for _ in range(NRANDOM):
        yield "".join(rnd.choice(weighted) for _ in range(rnd.randint(5, 12)))
    keys = [k for k in T_new if k]
    rnd = random.Random(20261017)
    for _ in range(NKEYS):
        parts = []
        for _ in range(rnd.randint(1, 8)):
            k = rnd.choice(keys)
            if k.startswith("^") and rnd.random() < 0.5:
                k = k[1:]
            parts.append(k)
        yield "".join(parts)


def run(h, data):
    p = subprocess.run([h], input=data.encode(), stdout=subprocess.PIPE, timeout=3600)
    return p.stdout.decode().split("\n")[:-1]


def outcome(impl, s, T, new):
    """('ok', hex) | ('overrun',) | ('segv',) : what a description of the parser predicts for s"""
    try:
        if impl == "spec":
            return ("ok", spec_model.spec_parse(SPEC, s, T, new=new).hex())
        return ("ok", handwritten_parser.handwritten_parse(s, T, new=new).hex())
    except model.Overrun:
        return ("overrun",)
    except model.Missing:
        return ("segv",)


t0 = time.time()
allstr = list(strings())
print("strings:", len(allstr))
data = "\n".join(allstr) + "\n"
res = {}
for tag, h in (("old", config.H_OLD), ("mid", config.H_MID), ("new", config.H_NEW)):
    res[tag] = run(config.need(h), data)
    assert len(res[tag]) == len(allstr), (tag, len(res[tag]))
print("C parsers done in %.0fs" % (time.time() - t0))

CASES = (("old", T_old, model.OLD), ("mid", T_mid, model.MID), ("new", T_new, model.NEW))
IMPLS = ("spec",) if SKIP_HAND else ("spec", "hand")
stats = {(tag, impl): [0, 0, 0, 0] for tag, _, _ in CASES for impl in IMPLS}     # agree, disagree, overrun (skipped), both crash
bad = {key: [] for key in stats}
same = {tag: [0, 0] for tag, _, _ in CASES}                                       # spec == model : yes, no
bad_same = []
for idx, s in enumerate(allstr):
    for tag, T, flag in CASES:
        got = {impl: outcome(impl, s, T, flag) for impl in IMPLS}
        if "hand" in got:
            if got["spec"] == got["hand"]:
                same[tag][0] += 1
            else:
                same[tag][1] += 1
                if len(bad_same) < 15:
                    bad_same.append((tag, s, got["spec"], got["hand"]))
        for impl in IMPLS:
            st, o = stats[(tag, impl)], got[impl]
            if o[0] == "overrun":
                st[2] += 1
                continue
            exp = "SEGV" if o[0] == "segv" else o[1]
            if res[tag][idx] == exp:
                st[0] += 1
                st[3] += exp == "SEGV"
            else:
                st[1] += 1
                if len(bad[(tag, impl)]) < 15:
                    bad[(tag, impl)].append((s, exp, res[tag][idx]))
fail = False
for tag, _, _ in CASES:
    for impl in IMPLS:
        a, d, o, sg = stats[(tag, impl)]
        print("%s C parser vs %-4s: agree %d (of which both crash: %d), DISAGREE %d, skipped (undefined behaviour) %d" % (tag, impl, a, sg, d, o))
        for b in bad[(tag, impl)]:
            print("    ", b)
        fail |= d > 0
    if not SKIP_HAND:
        print("%s spec vs hand     : identical outcome %d, different %d" % (tag, same[tag][0], same[tag][1]))
        fail |= same[tag][1] > 0
for b in bad_same:
    print("     spec/hand differ:", b)

PAT = ("_li", "_lee", "_ree", "_om", "_vd", "_vu", "_vn", "_vg", "_vc", "_s")


def defined(s, T, version):
    """None if the C code reads past the terminator on s (undefined behaviour: its result is not a statement about the parser), else True"""
    try:
        model.model_parse(s, T, version)
    except model.Overrun:
        return None
    except model.Missing:
        pass
    return True


# ---- patch 0001: old -> mid.  A changed result needs one of the new tokens in the string.
unexplained, changed, ub = [], 0, 0
for idx, s in enumerate(allstr):
    if res["old"][idx] != res["mid"][idx]:
        if defined(s, T_mid, model.MID) is None or defined(s, T_old, model.OLD) is None:
            ub += 1
            continue
        changed += 1
        if not any(p in s for p in PAT) and len(unexplained) < 20:
            unexplained.append((s, res["old"][idx], res["mid"][idx]))
print("(old/mid results that differ only because the C code reads past the terminator: %d)" % ub)
print("strings whose result changed old -> mid (patch 0001): %d ; unexplained (no new token inside): %d" % (changed, len(unexplained)))
for u in unexplained:
    print("   UNEXPLAINED", u)
fail |= bool(unexplained)

# ---- patch 0002: mid -> new.  A changed result needs a guard: the grammar must have applied one of the '!' rules on the way.
def guard_fired(s):
    trace = []
    try:
        spec_model.spec_parse(SPEC, s, T_new, model.NEW, trace=trace)
    except (model.Overrun, model.Missing):
        pass
    return any(rule.startswith("!") for _, _, _, rule, _ in trace)


unexplained, changed, ub = [], 0, 0
for idx, s in enumerate(allstr):
    differs = res["mid"][idx] != res["new"][idx]
    if differs:
        if defined(s, T_mid, model.MID) is None:
            ub += 1
            continue
        changed += 1
        if not guard_fired(s) and len(unexplained) < 20:
            unexplained.append((s, res["mid"][idx], res["new"][idx]))
print("(mid/new results that differ only because the mid C code reads past the terminator: %d)" % ub)
print("strings whose result changed mid -> new (patch 0002): %d ; unexplained (no guard applied): %d" % (changed, len(unexplained)))
for u in unexplained:
    print("   UNEXPLAINED", u)
fail |= bool(unexplained)
# the strings on which the grammar of the new parser reads past the end: none (every string is compared)
over_new = stats[("new", "spec")][2]
print("strings on which the new grammar reads past the terminator: %d (must be 0: no string is skipped for the new build)" % over_new)
fail |= over_new > 0
print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
