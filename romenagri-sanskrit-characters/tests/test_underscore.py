#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Section 14 of Romenagri/TRANSLITERATION.md as executable statements: runs of underscores, the escape, case folding, joiners.

    python3 tests/test_underscore.py [--full] [--deep]

    (default)   about a minute          --full  several minutes (larger samples, longer exhaustive ranges)
    --deep      adds the exhaustive search over 12.2 million strings of length <= 6 (about 8 minutes)

P is the parser of section 5.3 without the guards (the rules tagged '+' but not those tagged '!': the parser of patch 0001 alone), Q the
parser of this package (all the rules: patch 0001 and the twelve guards of patch 0002).  tests/spec_model.py runs the grammar of the
document; tests/diff_parser.py has shown that it is the C parser, build by build.  D is the decoder (tests/model.py).  "closed" is
defined in section 14.2.  The laws of U1 to U3 are checked for both P and Q: the guards do not change them, they make Law 3 unconditional.

U1  the cut law and the run law: P(u __ w) = P(u) 5F P(w) for every closed u, and P(u _^n w) = P(u) 5F^(n div 2) P((_ if n odd) w)
    for n >= 2: exhaustive for short u and w, random for longer ones, and on the C parser for a sample
U2  closedness is needed: a u that is not closed breaks the law for some w
U3  parity is all that a run needs to remember: two prefixes that differ in the parity of the run are told apart by the suffix `ta`
    (so one state is not enough), and for n >= 2 the future depends on n only through its parity (so two are enough)
U4  the marker rule and the decoder: in the decoder's output every run of underscores is (__)^k or (__)^k followed by a letter, the
    reading of such a run is unique, and the two translators invert each other on well-formed texts with any number of literal underscores;
    outside well-formed ACII the decoder can leave a lone underscore (shown on six sequences)
U5  the escape: P(E(s)) with E = sed 's/_/__/g' puts one byte 5F for every underscore of s, on spec and on C
U6  eleven rules read an underscore, or step over the terminator, without testing it: found by static analysis in the parser before the
    guards, each has a shortest string that breaks the law, and the C parser of that build (mid) behaves like the grammar on those strings
    (the escaped underscore is lost, or the filter crashes)
U7  the twelve guards (the rules tagged '!' of the grammar of section 5.3): no rule is left that does it; the pairing law holds, and the
    parser reads past the end of the input never, for every string in the range; each guard is needed; a guard never fires on a decoder
    output; and the C parser of this package agrees: the same bytes whatever follows the terminator, the witnesses fixed, the laws held
U8  case folding: tr A-Z a-z is a letter-by-letter map that fixes `_` (it keeps every run); capital letters are inert in the parser;
    the fold can create a key letter; random mutations of the environment crash the parser without the guards in several ways, and the
    one with them only where the table lacks a row (section 11.3)
U9  joiners and operators: the single ASCII bytes that each filter changes, the joiners the converters cannot carry, and what adding a
    joiner to the grammar costs (one rule, no state, no new gap)

  python3 tests/test_underscore.py --only U1,U7   run only some of the checks (U1 ... U9); tests/run_all.sh --resume runs them one by one

Exit status 1 if an asserted line fails.  Lines marked (informational) print a measurement that the document quotes and never fail."""
import itertools
import os
import random
import re
import subprocess
import sys
import time

import config
import model
import rmn_tables
import rn
import spec_model
import wellformed

FULL = "--full" in sys.argv or "--deep" in sys.argv
DEEP = "--deep" in sys.argv

# --only U1,U4 : run only some of the checks.  Each check is independent of the others, so they can be run one at a time, in separate
# processes (tests/run_all.sh --resume does that, so that a long run can be split and need not be repeated from the start).
ALL_CHECKS = ("U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9")
ONLY = None
for _i, _a in enumerate(sys.argv):
    if _a == "--only" and _i + 1 < len(sys.argv):
        ONLY = set(sys.argv[_i + 1].replace(" ", "").split(","))
    elif _a.startswith("--only="):
        ONLY = set(_a[len("--only="):].replace(" ", "").split(","))
if ONLY is not None and not ONLY <= set(ALL_CHECKS):
    sys.exit("--only: unknown check(s) %s; the checks are %s" % (sorted(ONLY - set(ALL_CHECKS)), ", ".join(ALL_CHECKS)))


def want(tag):
    return ONLY is None or tag in ONLY


fail = False
OVERRUN, MISSING = "overrun", "missing"


PREFIX = ""                                     # put in front of every message: which parser a check is about


def check(tag, what, ok, detail=""):
    global fail
    fail |= not ok
    print("  %-3s %-112s %s%s" % (tag, PREFIX + what, "ok" if ok else "FAIL", ("   " + detail) if (detail and not ok) else ""))


def info(tag, what, detail):
    print("  %-3s %-112s (informational) %s" % (tag, PREFIX + what, detail))


def heading(text):
    print("\n" + text)
    return time.time()


# ----------------------------------------------------------------------------------------------------------------------
# the models
# ----------------------------------------------------------------------------------------------------------------------
NEWDIR = config.need(config.NEW)
T = model.parse_table(NEWDIR)
ROWS = model.parse_rows(NEWDIR)
SPEC = spec_model.load_doc()
GUARDS = spec_model.guard_rows(SPEC)
KEYS = spec_model.lookup_keys(SPEC, True)
T2 = dict(T)                                    # the table with the 15 missing rows filled in by a dummy byte (section 11.3)
for _k in KEYS:
    T2.setdefault(_k, b"\xff")
HARNESS = config.need(config.H_NEW)               # the C parser of this package (with the guards)
HARNESS_MID = config.need(config.H_MID)           # the C parser of patch 0001 alone (without them)
RAND = random.Random(20261021)


class Parser:
    """P for one grammar and one table: bytes, or the strings OVERRUN / MISSING where the C code would read past the end / crash"""

    def __init__(self, spec, table, version):
        self.spec, self.table, self.version, self.memo, self.closed_memo = spec, table, version, {}, {}

    def __call__(self, s):
        r = self.memo.get(s)
        if r is None:
            try:
                r = spec_model.spec_parse(self.spec, s, self.table, self.version)
            except model.Overrun:
                r = OVERRUN
            except model.Missing:
                r = MISSING
            self.memo[s] = r
        return r

    def closed(self, u):
        """the parse of u reaches the terminator in state L1, L2a or L2b (an underscore that follows can then only start a unit)"""
        r = self.closed_memo.get(u)
        if r is None:
            tr = []
            try:
                spec_model.spec_parse(self.spec, u, self.table, self.version, trace=tr)
                r = bool(tr) and tr[-1][0] in ("L1", "L2a", "L2b")
            except (model.Overrun, model.Missing):
                r = False
            self.closed_memo[u] = r
        return r


P = Parser(SPEC, T, spec_model.MID)             # the grammar without the guards ('!'), the table as it is: the parser of patch 0001 alone
Q = Parser(SPEC, T, spec_model.NEW)             # the grammar with the guards, the table as it is: the parser of this package
Q2 = Parser(SPEC, T2, spec_model.NEW)           # the same with the 15 missing rows filled in: a total function


def defined(r):
    return isinstance(r, bytes)


def pairs_of(s):
    """the number of literal underscores the law demands: floor(n/2) for every maximal run of n underscores"""
    return sum(len(m.group(0)) // 2 for m in re.finditer(r"_+", s))


def c_parse(strings, harness=None, tail=None):
    """the C parser through tests/harness.c: [bytes or None for a crash].  harness: the build (default: this package's);
    tail: a character to write after the terminator of every string (the harness's RMN_TAIL)"""
    env = dict(os.environ)
    env.pop("RMN_TAIL", None)
    if tail is not None:
        env["RMN_TAIL"] = tail
    p = subprocess.run([harness or HARNESS], input=("\n".join(strings) + "\n").encode("latin-1"), stdout=subprocess.PIPE, env=env)
    out = p.stdout.decode().split("\n")[:-1]
    assert len(out) == len(strings), (len(out), len(strings))
    return [None if o == "SEGV" else bytes.fromhex(o) for o in out]


def rnd_string(maxlen, alphabet, p_us=0.25):
    return "".join("_" if RAND.random() < p_us else RAND.choice(alphabet) for _ in range(RAND.randint(0, maxlen)))


LETTERS = "abcdefghijklmnopqrstuvwxyz"
t_all = time.time()

CTX_U = ["", "k", "ka", "kh", "n", "ch", "_t", "_rd", "_rr", "kaa", "ra", "s", "_ta", "_ha", "p", "w"]
CTX_W = ["", "a", "ta", "ri", "x", "h", "ka", "aa", "e", "ee", "m", "u", "rd", "n", "o", "y"]


def laws(LABEL, PP, HAR):
    """U1, U2 and U3 for one parser: PP is the model (P without the guards, Q with them), HAR the C harness of the same build"""
    global PREFIX
    PREFIX = "[%s] " % ("P" if PP is P else "Q")
    ALPHA = "aeiouhvzcktlnr_"
    U = ["".join(t) for L in range(0, 4) for t in itertools.product(ALPHA, repeat=L)]
    W_ = ["".join(t) for L in range(0, 3) for t in itertools.product(ALPHA, repeat=L)]
    if want("U1"):
        # ======================================================================================================================
        t0 = heading("U1  the cut law and the run law  (section 14.2): the parser %s" % LABEL)
        # ======================================================================================================================
        checked = viol = whole_undef = skipped_u = 0
        examples = []
        for u in U:
            pu = PP(u)
            if not defined(pu) or not PP.closed(u):
                skipped_u += 1
                continue
            for w in W_:
                pw = PP(w)
                if not defined(pw):
                    continue
                whole = PP(u + "__" + w)
                if not defined(whole):
                    whole_undef += 1
                    continue
                checked += 1
                if whole != pu + b"\x5f" + pw:
                    viol += 1
                    examples.append((u, w, whole.hex(), (pu + b"\x5f" + pw).hex()))
        check("U1", "cut law P(u__w) = P(u) 5F P(w): every closed u of length <= 3 and every w of length <= 2 over %r (%d cases)" % (ALPHA, checked),
              viol == 0 and checked > 100000, "%d violations, e.g. %s" % (viol, examples[:3]))
        check("U1", "  ... and whenever P(u) and P(w) are defined, P(u__w) is defined too", whole_undef == 0, "%d undefined" % whole_undef)

        N = 100000 if FULL else 20000
        pairs = []
        while len(pairs) < N:
            u, w = rnd_string(8, LETTERS), rnd_string(8, LETTERS)
            if defined(PP(u)) and defined(PP(w)) and PP.closed(u):
                pairs.append((u, w))
        bad = [(u, w) for u, w in pairs if defined(PP(u + "__" + w)) and PP(u + "__" + w) != PP(u) + b"\x5f" + PP(w)]
        check("U1", "cut law on %d random pairs (length <= 8 over a-z and _)" % N, not bad, "%d violations, e.g. %s" % (len(bad), bad[:3]))

        n_c = 30000 if FULL else 6000
        sample = pairs[:n_c]
        cw = c_parse([u + "__" + w for u, w in sample], HAR)
        cu = c_parse([u for u, w in sample], HAR)
        cv = c_parse([w for u, w in sample], HAR)
        bad = [(u, w, a, b, c) for (u, w), a, b, c in zip(sample, cw, cu, cv) if a != b + b"\x5f" + c]
        check("U1", "cut law on the C parser of that build (tests/harness.c): %d of the pairs" % n_c, not bad, "%d violations, e.g. %s" % (len(bad), bad[:2]))

        cases = bad_run = 0
        for u in CTX_U:
            for w in CTX_W:
                for n in range(2, 41):
                    whole, pu, pm = PP(u + "_" * n + w), PP(u), PP(("_" if n % 2 else "") + w)
                    if not (defined(whole) and defined(pu) and defined(pm)):
                        continue
                    cases += 1
                    bad_run += whole != pu + b"\x5f" * (n // 2) + pm
        check("U1", "run law P(u _^n w) = P(u) 5F^(n div 2) P((_ if n odd) w), n = 2 .. 40: %d runs, %d contexts" % (cases, len(CTX_U) * len(CTX_W)), bad_run == 0 and cases > 8000,
              "%d violations" % bad_run)
        # n = 1 is the exception that proves the rule: the single underscore meets the halant of the consonant before it, and vocalic looks at it
        one = [(u, w, PP(u + "_" + w), PP(u) + PP("_" + w)) for u, w in (("k", "ri"), ("k", "ree"), ("k", "li"), ("kh", "ri"))]
        check("U1", "n = 1 is different, and only through `vocalic`: k_ri is KA + the sign RI, k___ri is KA, halant, 5F, the vowel RI",
              all(a != b for _, _, a, b in one) and PP("k_ri") == b"\xb3\xdf" and PP("k___ri") == b"\xb3\xe8\x5f\xaa", "%s" % one)
        print("      (%.0fs)" % (time.time() - t0))

    if want("U2"):
        # ======================================================================================================================
        t0 = heading("U2  closedness is needed: the parser %s" % LABEL)
        # ======================================================================================================================
        nonclosed = [u for u in U if defined(PP(u)) and not PP.closed(u)]
        survivors = []
        for u in nonclosed:
            if all((not defined(PP(u + "__" + w))) or PP(u + "__" + w) == PP(u) + b"\x5f" + PP(w) for w in W_ if defined(PP(w))):
                survivors.append(u)
        check("U2", "a lone marker: P(___ta) = 5F C2 but P(_) 5F P(ta) = E8 5F BD", PP("___ta") == b"\x5f\xc2" and PP("_") + b"\x5f" + PP("ta") == b"\xe8\x5f\xbd")
        check("U2", "every one of the %d strings u (length <= 3) that is not closed breaks the law for some w of length <= 2" % len(nonclosed), not survivors,
              "%d survive, e.g. %s" % (len(survivors), survivors[:5]))
        print("      (%.0fs)" % (time.time() - t0))

    if want("U3"):
        # ======================================================================================================================
        t0 = heading("U3  parity is all that a run remembers: the parser %s" % LABEL)
        # ======================================================================================================================
        CLOSED_CTX = [u for u in CTX_U if defined(PP(u)) and PP.closed(u)]
        dist = ok_dist = 0
        for u in CLOSED_CTX:
            for k in range(0, 21):
                even, odd = PP(u + "_" * (2 * k) + "ta"), PP(u + "_" * (2 * k + 1) + "ta")
                dist += 1
                ok_dist += defined(even) and defined(odd) and even[-1:] == b"\xbd" and odd[-1:] == b"\xc2"
        check("U3", "after any closed prefix, the suffix `ta` ends in TA after an even run and in the family letter _ta after an odd one (%d runs)" % dist, ok_dist == dist,
              "%d of %d" % (ok_dist, dist))
        SUFFIXES = ["", "a", "ta", "ri", "ka", "h", "e", "ee", "o", "m", "u", "x", "_ta", "tha", "_rd", "kh"]
        classes = {}
        for u in CLOSED_CTX:
            for n in range(2, 14):
                sig = []
                for w in SUFFIXES:
                    r = PP(u + "_" * n + w)
                    head = PP(u) + b"\x5f" * (n // 2)
                    sig.append(r[len(head):] if defined(r) and r.startswith(head) else None)
                classes.setdefault(u, {}).setdefault(tuple(sig), []).append(n)
        two = all(len(c) == 2 and sorted(n % 2 for ns in c.values() for n in ns[:1]) == [0, 1] for c in classes.values())
        check("U3", "for n = 2 .. 13 the residual behaviour after n underscores falls into exactly two classes, even and odd, for every closed prefix (%d prefixes)" % len(classes), two,
              "%s" % {u: [v for v in c.values()] for u, c in classes.items() if len(c) != 2})
        print("      (%.0fs)" % (time.time() - t0))

    PREFIX = ""


laws("without the guards (patch 0001 alone)", P, HARNESS_MID)
laws("with the guards (this package)", Q, HARNESS)

if want("U4"):
    # ======================================================================================================================
    t0 = heading("U4  the marker rule and the decoder  (sections 14.3 and 14.5)")
    # ======================================================================================================================


    def between(rnd):
        r = rnd.random()
        return b"" if r < 0.6 else b"\x5f" * rnd.choice([1, 1, 1, 2, 3, 4, 5, 8, 9, 20, 21])


    def filter_with(parser, a):
        """acii2rmn on the whole text, then the parser on every maximal [A-Za-z_] run (what tests/harness.c -f does)"""
        r = model.model_encode(a, ROWS)
        out, i = bytearray(), 0
        while i < len(r):
            if r[i].isascii() and (r[i].isalpha() or r[i] == "_"):
                j = i
                while j < len(r) and r[j].isascii() and (r[j].isalpha() or r[j] == "_"):
                    j += 1
                res = parser(r[i:j])
                if not defined(res):
                    return res
                out.extend(res)
                i = j
            else:
                out.append(ord(r[i]))
                i += 1
        return bytes(out)


    n_wf = 30000 if FULL else 5000
    rnd_wf = random.Random(11)
    texts = []
    for _ in range(n_wf):
        head = between(rnd_wf)
        texts.append(head + wellformed.well_formed(rnd_wf, True, between))
    n_lit = sum(t.count(b"\x5f") for t in texts)
    longest = max(max((len(m.group(0)) for m in re.finditer(rb"\x5f+", t)), default=0) for t in texts)
    rule_ok = bad_rule = lost = 0
    for t in texts:
        r = model.model_encode(t, ROWS)
        for m in re.finditer(r"_+", r):
            n = len(m.group(0))
            after = r[m.end()] if m.end() < len(r) else ""
            rule_ok += (n % 2 == 0) or after.isalpha()
            bad_rule += not ((n % 2 == 0) or after.isalpha())
    check("U4", "decoder output of %d well-formed texts with literal underscores (%d bytes 5F, runs up to %d): every odd run is followed by a letter" % (n_wf, n_lit, longest),
          bad_rule == 0, "%d violate" % bad_rule)
    # the unique reading of a run: decompositions into pairs and at most one marker that must be last
    for n in range(0, 12):
        dec = [(k, mark) for k in range(0, n + 1) for mark in (0, 1) if 2 * k + mark == n]       # pairs, and a marker only as the last underscore
        assert len(dec) == 1
    check("U4", "a run of n underscores followed by a letter splits in exactly one way into pairs and a last marker (n = 0 .. 11): pairs first, marker last", True)
    same = [(t, filter_with(P, t), filter_with(Q, t)) for t in texts]
    bad_p = [t for t, a, b in same if a != t]
    bad_q = [t for t, a, b in same if b != t]
    check("U4", "decoder then parser (the grammar without the guards) returns the text exactly, for all %d texts" % n_wf, not bad_p, "%d fail, e.g. %s" % (len(bad_p), [t.hex() for t in bad_p[:2]]))
    check("U4", "decoder then parser (the grammar with the guards) returns the text exactly, for all %d texts" % n_wf, not bad_q, "%d fail" % len(bad_q))
    n_cs = 20000 if FULL else 3000
    for hname, har in (("without the guards (mid)", HARNESS_MID), ("with the guards (new)", HARNESS)):
        cres = []
        for i in range(0, n_cs, 1000):
            p = subprocess.run([har, "-f"], input=("\n".join(t.hex() for t in texts[i:i + 1000]) + "\n").encode(), stdout=subprocess.PIPE)
            cres += p.stdout.decode().split("\n")[:-1]
        bad_c = [t for t, o in zip(texts, cres) if o != t.hex()]
        check("U4", "decoder then parser on the C library, %s (harness -f): %d of the texts return exactly" % (hname, n_cs), not bad_c, "%d fail, e.g. %s" % (len(bad_c), [t.hex() for t in bad_c[:2]]))
    # outside the well-formed texts the rule does not hold (section 14.3, last paragraph): the real decoder, a stack that pops letters
    # without regard to where a key begins, leaves the underscore of a key whose letters it took away
    ill_lone = [bytes.fromhex(h) for h in ("a4e8", "a2e8", "ebe8")]                  # independent vowel, then a halant
    ill_other = {bytes.fromhex("c4e9"): b"__rda", bytes.fromhex("c5e9"): b"__rdha", bytes.fromhex("a4e9"): b"_za"}
    lone_ok = all(rn.new.run("acii2rmn", s) == (0, b"_") for s in ill_lone)
    other_ok = all(rn.new.run("acii2rmn", s) == (0, w) for s, w in ill_other.items())
    check("U4", "outside well-formed ACII the decoder can leave an underscore without its letter: A4 E8, A2 E8 and EB E8 are written `_` (an odd run at the end)", lone_ok)
    check("U4", "... or put it in front of the letters of another key: C4 E9 is written `__rda`, C5 E9 `__rdha`, A4 E9 `_za` (the contract of section 9 excludes these)", other_ok)
    print("      (%.0fs)" % (time.time() - t0))

def escape_law(LABEL, PP, HAR):
    """U5 for one parser: PP is the model (P without the guards, Q with them), HAR the C harness of the same build"""
    global PREFIX
    PREFIX = "[%s] " % ("P" if PP is P else "Q")
    # ======================================================================================================================
    t0 = heading("U5  the escape E = sed 's/_/__/g'  (section 14.5): the parser %s" % LABEL)
    # ======================================================================================================================


    def segment():
        while True:
            x = "".join(RAND.choice(LETTERS) for _ in range(RAND.randint(1, 6)))
            if defined(PP(x)) and PP.closed(x):
                return x


    def make_text():
        segs = [segment() if RAND.random() < 0.8 else "" for _ in range(RAND.randint(1, 5))]
        runs = [RAND.choice([1, 1, 1, 2, 3, 4, 5, 8]) for _ in segs]
        parts, expect = [], b""
        for i, (x, m) in enumerate(zip(segs, runs)):
            parts.append(x)
            expect += PP(x)
            if i < len(segs) - 1 or RAND.random() < 0.5:
                parts.append("_" * m)
                expect += b"\x5f" * m
        s = "".join(parts)
        return s, expect


    n_e = 100000 if FULL else 20000
    cases = [make_text() for _ in range(n_e)]
    bad = [(s, e) for s, e in cases if PP(s.replace("_", "__")) != e]
    check("U5", "P(E(s)) = P(x0) 5F^m1 P(x1) ... for %d random strings whose segments x_i are closed and defined: one 5F per underscore of s" % n_e, not bad,
          "%d fail, e.g. %s" % (len(bad), bad[:2]))
    n_ce = 30000 if FULL else 5000
    cr = c_parse([s.replace("_", "__") for s, e in cases[:n_ce]], HAR)
    bad = [(s, e, c) for (s, e), c in zip(cases[:n_ce], cr) if c != e]
    check("U5", "the same on the C parser of that build, %d strings" % n_ce, not bad, "%d fail, e.g. %s" % (len(bad), bad[:2]))
    # without E, markers survive: the law of the unescaped string is different
    check("U5", "E is not the identity on markers: P(k_ta) is KA, halant, _ta; P(E(k_ta)) is KA, halant, 5F, TA", PP("k_ta") == b"\xb3\xe8\xc2" and PP("k__ta") == b"\xb3\xe8\x5f\xbd")
    print("      (%.0fs)" % (time.time() - t0))

    PREFIX = ""


if want("U5"):
    escape_law("without the guards (patch 0001 alone)", P, HARNESS_MID)
    escape_law("with the guards (this package)", Q, HARNESS)

if want("U6") or want("U7") or want("U9"):
    sites = spec_model.sync_breakers(SPEC, spec_model.MID)          # used by U6, U7 and U9
    wit = spec_model.breaker_witnesses(SPEC, T, new=spec_model.MID)  # used by U6 and U7

if want("U6"):
    # ======================================================================================================================
    t0 = heading("U6  eleven rules read an underscore unseen  (section 14.6): the parser without the guards (patch 0001 alone)")
    # ======================================================================================================================
    rules = sorted({(a, r.src) for a, r, j, k in sites})
    check("U6", "static analysis finds %d positions in %d rules that consume an underscore other than as the first character of a unit" % (len(sites), len(rules)),
          (len(sites), len(rules)) == (12, 11), "%d positions, %d rules" % (len(sites), len(rules)))
    sites0 = spec_model.sync_breakers(SPEC, spec_model.MID, char="\0")
    check("U6", "the same rules, at the same positions, are the ones that can step over the terminator (a read past the end of the input)",
          {(a, r.src, j) for a, r, j, k in sites0} == {(a, r.src, j) for a, r, j, k in sites})
    check("U6", "every one of the %d rules has a string, at most 4 letters long, on which it breaks the pairing law" % len(rules), set(wit) == set(rules),
          "missing: %s" % sorted(set(rules) - set(wit)))
    ws = sorted(set(wit.values()))
    cw = c_parse(ws, HARNESS_MID)
    agree = [s for s, c in zip(ws, cw) if c is not None and defined(P(s)) and c == P(s)]
    undefined = [s for s in ws if not defined(P(s))]
    check("U6", "on those %d strings the C parser of patch 0001 alone writes what the grammar writes (the grammar is undefined on %d of them, where C reads past the end)" % (len(ws), len(undefined)),
          all((not defined(P(s))) or (c is not None and c == P(s)) for s, c in zip(ws, cw)))
    broken = [s for s in ws if defined(P(s)) and P(s).count(b"\x5f") != pairs_of(s)]
    check("U6", "and on %d of them the output has the wrong number of literal underscores (the escaped underscore is lost, or one is made up)" % len(broken), len(broken) >= 8,
          "%d" % len(broken))
    # the effect in a program: Hindawi doubles every _ of the source (std2hin.awk), so an identifier like tc_flag reaches the parser as tc__flag
    for ident in ("tc__flag", "abc__x"):
        rc, out = rn.mid.r2a(ident.encode())
        check("U6", "the filter of patch 0001 alone turns the escaped identifier `%s` into bytes without any underscore: %s" % (ident, out.hex(" ")), rc == 0 and b"\x5f" not in out, "rc=%d" % rc)
    rc, out = rn.mid.r2a(b"tv__set")
    check("U6", "the filter of patch 0001 alone crashes on `tv__set` (the stem t, then v: the row `tvra` does not exist, section 11.3)", rc < 0 or rc >= 128, "rc=%d" % rc)
    for ident in ("tc__flag", "abc__x"):
        rc, out = rn.new.r2a(ident.encode())
        check("U6", "the filter of this package keeps the underscore of `%s`: %s" % (ident, out.hex(" ")), rc == 0 and out.count(b"\x5f") == 1, "rc=%d" % rc)
    rc, out = rn.new.r2a(b"tv__set")
    check("U6", "... and does not crash on `tv__set`: the guard does not ask for the row `tvra`", rc == 0 and out.count(b"\x5f") == 1, "rc=%d" % rc)
    print("      (%.0fs)" % (time.time() - t0))

if want("U7"):
    # ======================================================================================================================
    t0 = heading("U7  the twelve guards  (section 14.7)")
    # ======================================================================================================================
    check("U7", "the grammar has %d guards (the rules tagged '!'), one for each position found in U6 (%d)" % (len(GUARDS), len(sites)), len(GUARDS) == len(sites) == 12)
    _left = sorted({(a, r.src) for a, r, j, k in spec_model.sync_breakers(SPEC, spec_model.NEW)}
                   | {(a, r.src) for a, r, j, k in spec_model.sync_breakers(SPEC, spec_model.NEW, char="\0")})
    check("U7", "no rule of the grammar with the guards can consume an underscore, or step over the terminator, unseen",
          not _left, "no guard rule in front of: %s (section 8.3, step 3)" % "; ".join("%s: %s" % x for x in _left))
    st0, st1 = spec_model.stats(SPEC, spec_model.MID), spec_model.stats(SPEC, spec_model.NEW)
    check("U7", "the guards add %d rules and no state (%d states, longest guard %d characters)" % (st1[1] - st0[1], st1[0], st1[4]),
          st1[0] == st0[0] and st1[4] == st0[4] and st1[1] - st0[1] == len(GUARDS) and st1[3] == len(GUARDS) and st0[3] == 0)
    check("U7", "the witness that each guard names is, for every rule of U6, the string that the search of U6 found (the second guard of state M has its own)",
          set(wit.values()) <= {g[3] for g in GUARDS}, "%s" % sorted(set(wit.values()) - {g[3] for g in GUARDS}))
    max_all = 4 if FULL else 3
    ALL = LETTERS + "_"


    def exhaustive(name, alphabet, maxlen):
        t1 = time.time()
        cnt = {"ok": 0, OVERRUN: 0, MISSING: 0}
        viol = over_rep = 0
        first = None
        for L in range(0, maxlen + 1):
            for t in itertools.product(alphabet, repeat=L):
                s = "".join(t)
                r = spec_model_parse_rep(s)
                if r == OVERRUN:
                    over_rep += 1
                elif defined(r):
                    if r.count(b"\x5f") != pairs_of(s):
                        viol += 1
                        first = first or s
                cnt["ok" if defined(r) else r] += 1
        return cnt, viol, over_rep, first, time.time() - t1


    def spec_model_parse_rep(s):
        try:
            return spec_model.spec_parse(SPEC, s, T, spec_model.NEW)
        except model.Overrun:
            return OVERRUN
        except model.Missing:
            return MISSING


    cnt, viol, over, first, dt = exhaustive("all", ALL, max_all)
    n_all = sum(26 ** 0 * 27 ** L for L in range(0, max_all + 1))
    check("U7", "every one of the %d strings of length <= %d over a-z and _: the grammar with the guards writes one 5F per pair of underscores (%d defined, %d with a missing row)" % (n_all, max_all, cnt["ok"], cnt[MISSING]),
          viol == 0 and over == 0, "%d violations (first %r), %d reads past the end" % (viol, first, over))
    KEYL = "acehjklnortvyz_^"
    max_key = 6 if DEEP else (5 if FULL else 4)
    cnt, viol, over, first, dt = exhaustive("key", KEYL, max_key)
    n_key = sum(len(KEYL) ** L for L in range(0, max_key + 1))
    check("U7", "every one of the %d strings of length <= %d over the letters that the rules test (%s): the same (%d defined, %d with a missing row)" % (n_key, max_key, KEYL, cnt["ok"], cnt[MISSING]),
          viol == 0 and over == 0, "%d violations (first %r), %d reads past the end" % (viol, first, over))
    # the table is complete: totality
    cnt = {"ok": 0, OVERRUN: 0, MISSING: 0}
    for L in range(0, max_all + 1):
        for t in itertools.product(ALL, repeat=L):
            r = Q2("".join(t))
            cnt["ok" if defined(r) else r] += 1
    check("U7", "with the table completed, the parser with the guards is defined on all %d strings of length <= %d over a-z and _ (a total function in this range)" % (n_all, max_all),
          cnt[OVERRUN] == 0 and cnt[MISSING] == 0, "%s" % cnt)
    cnt0 = {"ok": 0, OVERRUN: 0, MISSING: 0}
    for L in range(0, max_all + 1):
        for t in itertools.product(ALL, repeat=L):
            r = P("".join(t))
            cnt0["ok" if defined(r) else r] += 1
    info("U7", "the grammar without the guards with the table as it is, same strings", "defined %d, reads past the end %d, missing row %d" % (cnt0["ok"], cnt0[OVERRUN], cnt0[MISSING]))
    # each guard is needed
    for n, (state, rule, anchor, w) in enumerate(GUARDS):
        without = spec_model.without_guard(SPEC, n)
        try:
            r = spec_model.spec_parse(without, w, T, spec_model.NEW)
            broke = r.count(b"\x5f") != pairs_of(w)
        except (model.Overrun, model.Missing):
            broke = False
        kept = Q(w)
        check("U7", "guard %-3s %-34s witness %-7r: breaks the law without it, holds with it" % (state, rule.split("->")[0].strip(), w), broke and defined(kept) and kept.count(b"\x5f") == pairs_of(w))
    # the guards are invisible on everything the decoder can write
    keyset = sorted(k for k in T if k)
    two = fires = undefined_before = 0
    for a in keyset:
        for b in keyset:
            s = a + b
            two += 1
            if not defined(P(s)):
                undefined_before += 1
                fires += not defined(Q(s)) and Q(s) != MISSING
            else:
                fires += P(s) != Q(s)
    check("U7", "no guard changes the parse of two table keys written one after the other (%d strings), except where the parser without the guards reads past the end (%d: the key `^` followed by an underscore key)"
          % (two, undefined_before), fires == 0, "%d differ" % fires)
    changed = tot = held = 0
    ex = []
    for L in range(0, 4):
        for t in itertools.product(ALL, repeat=L):
            s = "".join(t)
            a, b = P(s), Q(s)
            if defined(a) and defined(b):
                tot += 1
                if a != b:
                    changed += 1
                    held += a.count(b"\x5f") == pairs_of(s)
                    if len(ex) < 5 and a.count(b"\x5f") == pairs_of(s):
                        ex.append((s, a.hex(" "), b.hex(" ")))
    info("U7", "strings of length <= 3 that both grammars read", "%d; the output differs on %d (on %d of them the parser without the guards kept the law); e.g. %s" % (tot, changed, held, ex[:3]))
    # the C parser of this package: the witnesses, and no read past the end of the string
    wits = [g[3] for g in GUARDS]
    cw = c_parse(wits)
    check("U7", "on the %d witness strings the C parser of this package writes what the grammar with the guards writes, one 5F per pair" % len(wits),
          all(c is not None and c == Q(w) and c.count(b"\x5f") == pairs_of(w) for w, c in zip(wits, cw)), "%s" % [(w, c and c.hex()) for w, c in zip(wits, cw)])
    def all_strings(m_all, m_key):
        for L in range(0, m_all + 1):
            for t in itertools.product(ALL, repeat=L):
                yield "".join(t)
        for L in range(0, m_key + 1):
            for t in itertools.product(KEYL, repeat=L):
                yield "".join(t)


    def tail_dependence(har, m_all, m_key, chunk=20000):
        """(strings, how many give other bytes when `x` follows the terminator instead of `_`, how many do not give the same bytes whatever follows it:
        `_`, `x` or what an earlier string left).  Done in chunks: a parser that reads past the end writes up to 4,096 bytes for such a string,
        and all of them held at once need gigabytes (patch 0001 alone on all the strings of --full: 6 GB and ten minutes)"""
        gen, n, d1, d2 = all_strings(m_all, m_key), 0, 0, 0
        while True:
            part = list(itertools.islice(gen, chunk))
            if not part:
                return n, d1, d2
            r_us, r_x, r_stale = c_parse(part, har, "_"), c_parse(part, har, "x"), c_parse(part, har)
            n += len(part)
            d1 += sum(1 for a, b in zip(r_us, r_x) if a != b)
            d2 += sum(1 for a, b, c in zip(r_us, r_x, r_stale) if not (a == b == c))


    n_new, *dep_new = tail_dependence(HARNESS, max_all, max_key)
    n_mid, *dep_mid = tail_dependence(HARNESS_MID, 3, 4)           # patch 0001 alone: the strings of the quick run are enough to show the difference
    check("U7", "the C parser of this package: on %d strings the output is the same whatever follows the terminator (an underscore, a letter, what an earlier string left)" % n_new,
          tuple(dep_new) == (0, 0), "%s strings differ" % (tuple(dep_new),))
    info("U7", "the C parser without the guards (patch 0001 alone), on the %d strings of the quick run" % n_mid, "%d give other bytes when `x` follows the terminator instead of `_`" % dep_mid[0])
    check("U7", "... so the measurement can see a read past the end: the parser without the guards fails it", dep_mid[0] > 0)
    print("      (%.0fs)" % (time.time() - t0))

if want("U8"):
    # ======================================================================================================================
    t0 = heading("U8  case folding and mutations of the environment  (section 14.8)")
    # ======================================================================================================================


    def phi(s):
        return s.translate({c: c + 32 for c in range(65, 91)})


    def runs_of(s):
        return [len(m.group(0)) for m in re.finditer(r"_+", s)]


    mixed = [rnd_string(12, LETTERS + LETTERS.upper() + "|^0123456789 ") for _ in range(20000)]
    check("U8", "tr A-Z a-z is idempotent, fixes `_`, and keeps every run of underscores (the lengths of the runs, in order) on %d random strings" % len(mixed),
          all(phi(phi(s)) == phi(s) and runs_of(phi(s)) == runs_of(s) and phi(s).count("_") == s.count("_") for s in mixed))
    check("U8", "tr A-Z a-z is a monoid homomorphism (phi(uv) = phi(u) phi(v)) but not injective: A and a go to a", phi("Ab" + "cD") == phi("Ab") + phi("cD") and phi("A") == phi("a"))
    cap = lambda s: re.sub("[A-Z]", "Q", s)                                  # noqa: E731
    capb = lambda b: bytes(0x51 if 0x41 <= x <= 0x5A else x for x in b)      # noqa: E731
    n_inert = n_def = 0
    for s in mixed:
        a, b = P(s), P(cap(s))
        if defined(a) and defined(b):
            n_def += 1
            n_inert += capb(a) == b
        else:
            n_inert += a == b
    check("U8", "capital letters are inert: P(s) and P(s with every capital replaced by Q) agree up to that replacement, on %d random strings (%d defined)" % (len(mixed), n_def),
          n_inert == len(mixed), "%d disagree" % (len(mixed) - n_inert))
    check("U8", "but the fold can create a key letter: the escaped `C_f` keeps its underscore (C 5F f), the folded `c_f` loses it in the parser without the guards and keeps it in the parser with them",
          P("C__f") == b"C\x5f" + b"f" and P(phi("C__f")) == b"\xb8\xe8f" and Q(phi("C__f")) == b"c\x5ff")
    check("U8", "... on the C filters too: patch 0001 alone writes B8 E8 66 for `c__f`, this package writes 63 5F 66, and both write 43 5F 66 for `C__f`",
          rn.mid.r2a(b"c__f") == (0, b"\xb8\xe8f") and rn.new.r2a(b"c__f") == (0, b"c\x5ff") and rn.mid.r2a(b"C__f") == rn.new.r2a(b"C__f") == (0, b"C\x5ff"))

    # mutations
    base = []
    rnd_m = random.Random(5)
    for _ in range(3000):
        a = wellformed.well_formed(rnd_m, True)
        base.append(model.model_encode(a, ROWS))
    ALPHA_M = LETTERS + LETTERS.upper() + "_^|0123456789 "


    def mutate(s, rnd):
        r = rnd.random()
        if r < 0.2 and s:
            return s[:rnd.randint(0, len(s) - 1)]
        if r < 0.3:
            return s.upper()
        if r < 0.4:
            return s.lower()
        if r < 0.55:
            i = rnd.randint(0, len(s))
            return s[:i] + rnd.choice(ALPHA_M) + s[i:]
        if r < 0.65 and s:
            i = rnd.randint(0, len(s) - 1)
            return s[:i] + s[i + 1:]
        if r < 0.8 and s:
            i = rnd.randint(0, len(s) - 1)
            return s[:i] + rnd.choice(ALPHA_M) + s[i + 1:]
        if r < 0.9:
            return s.replace("_", "__")
        return s + rnd.choice(base)


    N_M = 60000 if FULL else 15000
    muts = [mutate(rnd_m.choice(base), rnd_m) for _ in range(N_M)]
    muts = [m for m in muts if m and "\n" not in m]
    res = {"without the guards": {"ok": 0, OVERRUN: 0, MISSING: 0}, "with the guards": {"ok": 0, OVERRUN: 0, MISSING: 0}, "total": {"ok": 0, OVERRUN: 0, MISSING: 0}}
    for m in muts:
        for tag, prs in (("without the guards", P), ("with the guards", Q), ("total", Q2)):
            r = prs(m)
            res[tag]["ok" if defined(r) else r] += 1
    n_c = min(len(muts), 20000)
    cr_mid, cr_new = c_parse(muts[:n_c], HARNESS_MID), c_parse(muts[:n_c])
    crash_mid, crash_new = sum(1 for c in cr_mid if c is None), sum(1 for c in cr_new if c is None)
    info("U8", "%d random mutations of valid spellings (truncate, case, insert, delete, replace, escape, concatenate)" % len(muts),
         "grammar without the guards: %s; with the guards: %s; C parser without the guards: %d crashes in %d; with the guards: %d" % (res["without the guards"], res["with the guards"], crash_mid, n_c, crash_new))
    check("U8", "the grammar with the guards and the completed table is defined on every mutation (no read past the end, no missing row)", res["total"][OVERRUN] == 0 and res["total"][MISSING] == 0,
          "%s" % res["total"])
    check("U8", "the parser without the guards is not: it reads past the end or asks for a row that is missing on some mutations", res["without the guards"][OVERRUN] + res["without the guards"][MISSING] > 0)
    exp_crash = [Q(m) == MISSING for m in muts[:n_c]]
    check("U8", "the C parser of this package crashes on a mutation exactly when the grammar asks for a row that is missing (%d of the %d), and on no other" % (sum(exp_crash), n_c),
          [c is None for c in cr_new] == exp_crash, "%d crash, %d expected" % (crash_new, sum(exp_crash)))
    print("      (%.0fs)" % (time.time() - t0))

if want("U9"):
    # ======================================================================================================================
    t0 = heading("U9  joiners and operators  (section 14.9)")
    # ======================================================================================================================
    NEW = rn.new
    changed = {}
    for prog in ("rmn2acii", "acii2rmn", "acii2cf", "acii2pcf"):
        ch = []
        for c in range(0x20, 0x7F):
            rc, out = NEW.run(prog, bytes([c]))
            if out != bytes([c]):
                ch.append(chr(c))
        changed[prog] = "".join(ch)
    mid_changed = "".join(chr(c) for c in range(0x20, 0x7F) if rn.mid.run("rmn2acii", bytes([c]))[1] != bytes([c]))
    check("U9", "rmn2acii changes 16 of the 95 printable ASCII bytes: the 15 letters `bdgjklmnprstwxy` and `_` (patch 0001 alone changes 17: a lone `c` reads past the end of the string and becomes CHA; the guard of section 14.7 keeps it the letter c)",
          changed["rmn2acii"] == "_bdgjklmnprstwxy" and mid_changed == "_bcdgjklmnprstwxy", "%s / %s" % (changed["rmn2acii"], mid_changed))
    check("U9", "acii2cf and acii2pcf change none of them: operators, digits, quotes and the underscore pass through", changed["acii2cf"] == "" and changed["acii2pcf"] == "")
    check("U9", "acii2rmn wraps every ASCII letter and the underscore (53 bytes) as \"e_x\"; the 31 other punctuation marks pass", len(changed["acii2rmn"]) == 53 and not (set(changed["acii2rmn"]) - set(LETTERS + LETTERS.upper() + "_")))
    punct = [chr(c) for c in range(0x21, 0x7F) if not chr(c).isalnum() and chr(c) != "_"]
    check("U9", "the parser's alphabet [a-z_] meets the %d other ASCII punctuation marks of a host language in no character at all" % len(punct), all(chr(0) not in p for p in punct) and "_" not in punct)
    rc, out = NEW.run("uni2acii", b"\xff\xfe" + "क‍ष".encode("utf-16-le"))
    rc2, out2 = NEW.run("uni2acii", b"\xff\xfe" + "क्‌ष".encode("utf-16-le"))
    check("U9", "ZWJ and ZWNJ have no row: uni2acii writes their low bytes 0D and 0C (section 11.6)", out == b"\xb3\x0d\xd6" and out2 == b"\xb3\xe8\x0c\xd6", "%s %s" % (out.hex(), out2.hex()))
    rc, out = NEW.run("acii2rmn", b"\xb3\xe8\xe8")
    rc2, out2 = NEW.run("acii2rmn", b"\xb3\xe8\xe9")
    check("U9", "the ISCII explicit halant (E8 E8) is eaten by the decoder (KA disappears) and the soft halant (E8 E9) crashes it", rc == 0 and out == b"" and (rc2 < 0 or rc2 >= 128))
    check("U9", "yet `k_` and `x_` write E8 E8: a final underscore is a halant, and the consonant has one already", P("k_") == b"\xb3\xe8\xe8" and P("x_") == b"\xd6\xe8\xe8")
    rc, out = NEW.run("acii2cf", b"\xb3")
    rc2, out2 = NEW.run("acii2cf", b"ka")
    check("U9", "acii2cf is a projection: the Devanagari letter KA and the Latin word `ka` both come out as `ka`", out.strip() == out2.strip() == b"ka", "%r %r" % (out, out2))

    # what a joiner would cost: two rules in the family state and two rows
    grammar_text = spec_model.BLOCK.search(spec_model.doc_text()).group(1)
    lines = grammar_text.split("\n")
    at = max(i for i, l in enumerate(lines) if re.match(r"^\s+\.\s+->\s+raw c ; skip 1 ; goto L1\s+# an unknown family letter", l))
    extra = ["  'zwj'                   -> emit '_zwj' ; skip 3 ; goto L1", "  'zwn'                   -> emit '_zwn' ; skip 3 ; goto L1"]
    ext = spec_model.parse_grammar("\n".join(lines[:at] + extra + lines[at:]))
    T3 = dict(T)
    T3["_zwj"], T3["_zwn"] = b"\xfd", b"\xfc"
    s0, s1 = spec_model.stats(SPEC), spec_model.stats(ext)
    check("U9", "adding the two joiners _zwj and _zwn takes %d rules, %d states and no longer guard (%d states, longest guard %d)" % (s1[1] - s0[1], s1[0] - s0[0], s1[0], s1[4]),
          s1[1] - s0[1] == 2 and s1[0] == s0[0] and s1[4] == s0[4])
    check("U9", "...creates no new place where an underscore can be read unseen (the %d of section 14.6 remain without the guards, none with them)" % len(sites),
          len(spec_model.sync_breakers(ext, spec_model.MID)) == len(sites) and spec_model.sync_breakers(ext, spec_model.NEW) == [])
    Pj = Parser(ext, T3, spec_model.NEW)
    bad = []
    for u in CTX_U:
        for n in range(1, 12):
            for key, byte in (("zwj", b"\xfd"), ("zwn", b"\xfc")):
                whole, pu = Pj(u + "_" * n + key), Pj(u)
                if not (defined(whole) and defined(pu)):
                    continue
                if n >= 2 and whole != pu + b"\x5f" * (n // 2) + (byte if n % 2 else Pj(key)):
                    bad.append((u, n, key))
    check("U9", "...and the run law holds for them: a joiner after an odd run is the joiner, after an even run it is the plain letters z w j", not bad, "%s" % bad[:3])
    print("      (%.0fs)" % (time.time() - t0))

print("\nRESULT: %s   (%.0f s)" % ("FAIL" if fail else "PASS", time.time() - t_all) + (("   [only %s]" % ",".join(sorted(ONLY))) if ONLY else ""))
sys.exit(1 if fail else 0)
