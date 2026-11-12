# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Round trip  ACII -> Romenagri -> ACII  through the translators with filter semantics (acii2rmn, then rmn2acii on [A-Za-z_] runs),
old build against new build (and the mid build, which has the Sanskrit characters but not the guards of section 14.7, between them).
usage: python3 tests/rt_filters.py [MAXLEN [NRANDOM]]     default 3 20000   (full run: 3 200000)

 (1) regression:   every sequence over the OLD repertoire behaves exactly as before, except that avagraha is repaired.  The guards
                   (mid -> new) turn no exact round trip into a broken one; where they change the final output, the sequence is not
                   well-formed ACII (part 4 shows the same on random well-formed texts).
 (2) equivariance: a sequence with new bytes behaves like the same sequence with each new byte replaced by an existing
                   character of the same kind (vocalic vowels -> RI, vocalic signs -> the RI sign, everything else -> anusvara);
                   outputs may differ only on sequences whose analogue does not round-trip either (invalid ACII).
 (2b) the sharper statement: the analogue sequence round-trips exactly  <=>  the new sequence does.
 (3) models:       tests/model.py reproduces acii2rmn (-r) and the filter pair (-f) on every sequence up to length 2 over the new
                   repertoire and on NRANDOM random longer ones, for the old, the mid and the new build.
 (4) contract:     NRANDOM random WELL-FORMED texts (grammar in TRANSLITERATION.md, section 9) round-trip exactly in the new build;
                   the old build fails on them only where the text contains avagraha; the mid and the new build write the same
                   bytes on every one of them (the guards are invisible on well-formed text).
 (5) the same, exhaustively: every sequence of up to MAXLEN bytes over the new repertoire that belongs to W (section 9.2; tests/wellformed.py
                   has a recognizer for W): the mid and the new build write the same bytes, and the new build returns it exactly.
Exit status 1 on any regression, any broken analogue, any disagreement between model and C, or any well-formed text that fails."""
import itertools
import random
import subprocess
import sys

import config
import model
import rmn_tables

MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 3
NRANDOM = int(sys.argv[2]) if len(sys.argv) > 2 else 20000

old_uni = rmn_tables.parse_unicode(config.need(config.OLD))[1]
new_uni = rmn_tables.parse_unicode(config.need(config.NEW))[1]
R_old = sorted({b for _, b in old_uni})
NEWB = sorted({b for _, b in new_uni} - set(R_old))
R_new = R_old + NEWB
assert NEWB == [0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C], [hex(b) for b in NEWB]
# analogue of every new byte among the old repertoire: vocalic vowel -> RI (AA), vocalic sign -> sign RI (DF), the rest -> anusvara (A2)
PHI = {0x81: 0xAA, 0x82: 0xAA, 0x83: 0xAA, 0x84: 0xDF, 0x85: 0xDF, 0x86: 0xDF, 0x87: 0xA2, 0x88: 0xA2, 0x89: 0xA2, 0x8A: 0xA2,
       0x8B: 0xA2, 0x8C: 0xA2}
AVAGRAHA = 0xEB
print("old repertoire: %d bytes, new: %d bytes" % (len(R_old), len(R_new)))


def seqs(rep, maxlen):
    for L in range(1, maxlen + 1):
        for t in itertools.product(rep, repeat=L):
            yield bytes(t)


def c_run(h, mode, lines):
    data = "\n".join(s.hex() for s in lines) + "\n"
    out = subprocess.run([config.need(h), mode], input=data.encode(), stdout=subprocess.PIPE).stdout.decode().split("\n")[:-1]
    assert len(out) == len(lines), (h, mode, len(out), len(lines))
    return [None if o == "SEGV" else bytes.fromhex(o) for o in out]


fail = False

# ---- (1) regression on the old repertoire
S_old = list(seqs(R_old, MAXLEN))
rt_o = c_run(config.H_OLD, "-f", S_old)
rt_m = c_run(config.H_MID, "-f", S_old)
rt_n = c_run(config.H_NEW, "-f", S_old)
ok_o = sum(1 for s, y in zip(S_old, rt_o) if s == y)
ok_n = sum(1 for s, y in zip(S_old, rt_n) if s == y)
same_out = sum(1 for a, b in zip(rt_o, rt_n) if a == b)
diff = [(s, a, b) for s, a, b in zip(S_old, rt_o, rt_n) if a != b]
diff_noeb = [d for d in diff if AVAGRAHA not in d[0]]
regress = [s for s, a, b in zip(S_old, rt_o, rt_n) if s == a and s != b]
repaired = [s for s, a, b in zip(S_old, rt_o, rt_n) if s != a and s == b]
print("(1) old repertoire, sequences up to length %d: %d" % (MAXLEN, len(S_old)))
print("    round-trip exact: old %d, new %d" % (ok_o, ok_n))
print("    final output identical old/new: %d of %d; differing sequences without avagraha: %d" % (same_out, len(S_old), len(diff_noeb)))
print("    REGRESSIONS (exact before, broken now): %d" % len(regress))
print("    repaired (broken before, exact now): %d  (all contain avagraha: %s)" % (len(repaired), all(AVAGRAHA in s for s in repaired)))
print("    crashes (SEGV) old/new: %d / %d" % (sum(1 for y in rt_o if y is None), sum(1 for y in rt_n if y is None)))
for s, a, b in diff_noeb[:8]:
    print("      differs (no avagraha):", s.hex(), a and a.hex(), b and b.hex())
fail |= bool(regress) or not all(AVAGRAHA in s for s in repaired)
# the guards of section 14.7: mid -> new
g_diff = [(s, a, b) for s, a, b in zip(S_old, rt_m, rt_n) if a != b]
g_regress = [s for s, a, b in zip(S_old, rt_m, rt_n) if s == a and s != b]
g_repaired = [s for s, a, b in zip(S_old, rt_m, rt_n) if s != a and s == b]
print("    the guards (mid -> new): final output identical on %d of %d; differs on %d (exact before and broken now: %d, broken before and exact now: %d)"
      % (len(S_old) - len(g_diff), len(S_old), len(g_diff), len(g_regress), len(g_repaired)))
print("    crashes (SEGV) mid/new: %d / %d" % (sum(1 for y in rt_m if y is None), sum(1 for y in rt_n if y is None)))
for s, a, b in g_diff[:5]:
    print("      guards change:", s.hex(), a and a.hex(), b and b.hex())
fail |= bool(g_regress)
from wellformed import is_well_formed as _wf  # noqa: E402
g_in_w = [s for s, a, b in g_diff if _wf(s, False)]
print("    of those %d sequences, those that belong to W (section 9.2) over the old repertoire: %d (must be 0)" % (len(g_diff), len(g_in_w)))
fail |= bool(g_in_w)

# ---- (2) equivariance for the new bytes
S_new = [s for s in seqs(R_new, MAXLEN) if any(b in NEWB for b in s)]
S_phi = [bytes(PHI.get(b, b) for b in s) for s in S_new]
y_new = c_run(config.H_NEW, "-f", S_new)
y_old = c_run(config.H_OLD, "-f", S_phi)
sub = lambda y: None if y is None else bytes(PHI.get(b, b) for b in y)        # noqa: E731
agree = sum(1 for yn, yo in zip(y_new, y_old) if sub(yn) == yo)
bad = [(s, sp, yn, yo) for s, sp, yn, yo in zip(S_new, S_phi, y_new, y_old) if sub(yn) != yo]
exact_new = sum(1 for s, y in zip(S_new, y_new) if s == y)
exact_old = sum(1 for s, y in zip(S_phi, y_old) if s == y)
print("(2) sequences with at least one new byte: %d" % len(S_new))
print("    round-trip exact: new bytes %d, analogue bytes %d" % (exact_new, exact_old))
print("    equivariant (new result == old result of the analogue sequence, modulo the substitution): %d of %d" % (agree, len(S_new)))
# A difference can only come from an INVALID sequence (e.g. a vowel sign right after a candrabindu): there both builds produce
# garbage, and the garbage spells letters of the key ('l' against 'r').  What must hold: an exact analogue implies an exact result.
noneq_exact = [b for b in bad if b[1] == b[3]]
print("    of the %d non-equivariant sequences, those whose analogue round-trips exactly: %d (must be 0)" % (len(bad), len(noneq_exact)))
for s, sp, yn, yo in bad[:4]:
    print("      e.g. invalid sequence", s.hex(), "->", yn and yn.hex(), "| analogue", sp.hex(), "->", yo and yo.hex())
fail |= bool(noneq_exact)
worse = [(s, sp) for s, sp, yn, yo in zip(S_new, S_phi, y_new, y_old) if sp == yo and s != yn]
better = [(s, sp) for s, sp, yn, yo in zip(S_new, S_phi, y_new, y_old) if s == yn and sp != yo]
print("(2b) analogue exact but new byte not: %d   new byte exact but analogue not: %d" % (len(worse), len(better)))
fail |= bool(worse)

# ---- (3) the models against the C code
rows_o, rows_m, rows_n = model.parse_rows(config.OLD), model.parse_rows(config.MID), model.parse_rows(config.NEW)
T_o, T_m, T_n = model.parse_table(config.OLD), model.parse_table(config.MID), model.parse_table(config.NEW)
rnd = random.Random(20261018)
S3 = list(seqs(R_new, 2)) + [bytes(rnd.choice(R_new) for _ in range(rnd.randint(3, 6))) for _ in range(NRANDOM)]
for tag, h, rows, T, flag in (("old", config.H_OLD, rows_o, T_o, model.OLD), ("mid", config.H_MID, rows_m, T_m, model.MID),
                              ("new", config.H_NEW, rows_n, T_n, model.NEW)):
    c_enc = c_run(h, "-r", S3)
    c_flt = c_run(h, "-f", S3)
    d_enc = d_flt = skipped = 0
    ex = []
    for s, ce, cf in zip(S3, c_enc, c_flt):
        try:
            me = model.model_encode(s, rows).encode("latin-1")
        except model.Crash:
            me = None
        if me != ce:
            d_enc += 1
            ex.append(("encode", s.hex(), me, ce))
        try:
            mf = model.model_filter(s, rows, T, new=flag)
        except model.Crash:
            mf = None
        except model.Missing:
            mf = None
        except model.Overrun:
            skipped += 1
            continue
        if mf != cf:
            d_flt += 1
            ex.append(("filter", s.hex(), mf and mf.hex(), cf and cf.hex()))
    print("(3) %s build, %d sequences: model_encode differs from acii2rmn on %d, model_filter differs from the filter pair on %d (skipped, undefined behaviour: %d)"
          % (tag, len(S3), d_enc, d_flt, skipped))
    for e in ex[:6]:
        print("      ", e)
    fail |= bool(d_enc or d_flt)

# ---- (4) the round-trip contract on well-formed text
from wellformed import well_formed  # noqa: E402

rnd = random.Random(7)
WF_old = [well_formed(rnd, False) for _ in range(NRANDOM)]
WF_new = [well_formed(rnd, True) for _ in range(NRANDOM)]
r_oo = c_run(config.H_OLD, "-f", WF_old)
r_no = c_run(config.H_NEW, "-f", WF_old)
r_nn = c_run(config.H_NEW, "-f", WF_new)
r_mo = c_run(config.H_MID, "-f", WF_old)
r_mn = c_run(config.H_MID, "-f", WF_new)
ex = lambda S, R: sum(1 for s, y in zip(S, R) if s == y)                  # noqa: E731
bad_old_without_avagraha = [s for s, y in zip(WF_old, r_oo) if s != y and AVAGRAHA not in s]
print("(4) %d well-formed texts over the old repertoire, %d over the new repertoire (vocalic L LL RR and signs, OM, double danda, accents)" % (NRANDOM, NRANDOM))
print("    old build, old repertoire: exact %d (%.2f%%), crashes %d, failing texts without avagraha: %d"
      % (ex(WF_old, r_oo), 100.0 * ex(WF_old, r_oo) / NRANDOM, sum(1 for y in r_oo if y is None), len(bad_old_without_avagraha)))
print("    new build, old repertoire: exact %d (%.2f%%), crashes %d" % (ex(WF_old, r_no), 100.0 * ex(WF_old, r_no) / NRANDOM, sum(1 for y in r_no if y is None)))
print("    new build, new repertoire: exact %d (%.2f%%), crashes %d" % (ex(WF_new, r_nn), 100.0 * ex(WF_new, r_nn) / NRANDOM, sum(1 for y in r_nn if y is None)))
for s, y in [(s, y) for s, y in zip(WF_new, r_nn) if s != y][:6]:
    print("      FAILS:", s.hex(), "->", y and y.hex())
fail |= ex(WF_old, r_no) != NRANDOM or ex(WF_new, r_nn) != NRANDOM or bool(bad_old_without_avagraha)
same_o = sum(1 for a, b in zip(r_mo, r_no) if a == b)
same_n = sum(1 for a, b in zip(r_mn, r_nn) if a == b)
print("    the guards are invisible: mid and new write the same bytes on %d of %d texts over the old repertoire and on %d of %d over the new one" % (same_o, NRANDOM, same_n, NRANDOM))
fail |= same_o != NRANDOM or same_n != NRANDOM

# ---- (5) the guards on every well-formed sequence of up to MAXLEN bytes
from wellformed import is_well_formed  # noqa: E402

S5 = list(seqs(R_new, MAXLEN))
r5_m, r5_n = c_run(config.H_MID, "-f", S5), c_run(config.H_NEW, "-f", S5)
in_w = [is_well_formed(x, True) for x in S5]
n_w = sum(in_w)
same_w = sum(1 for w, x, a, b in zip(in_w, S5, r5_m, r5_n) if w and a == b)
exact_w = sum(1 for w, x, b in zip(in_w, S5, r5_n) if w and b == x)
guard_out = sum(1 for w, a, b in zip(in_w, r5_m, r5_n) if not w and a != b)
print("(5) every sequence of up to %d bytes over the new repertoire: %d, of which %d belong to W (section 9.2)" % (MAXLEN, len(S5), n_w))
print("    in W: the mid and the new build write the same bytes on %d of %d, and the new build returns %d of them exactly" % (same_w, n_w, exact_w))
print("    not in W: the guards change the output of %d of %d" % (guard_out, len(S5) - n_w))
fail |= same_w != n_w or exact_w != n_w

print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
