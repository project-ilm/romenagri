# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Real Hindi text through the whole chain, old build against new build.

    python3 tests/test_corpus.py [FILE ...]        default: Romenagri/corp_hi.txt, Romenagri/test_hi.txt and every file named in $RMN_CORPUS

Chain, per chunk of 400 lines:   UTF-8 text -> UTF-16LE -> uni2acii -> acii2rmn -> rmn2acii -> acii2uni -> UTF-8 text
(the same chain Hindawi's hincc runs, minus fixuninum).  A chunk on which a tool crashes is repeated line by line.

For every file it reports: lines; lines restored exactly by the old / new build; lines on which old and new differ and why
(a new character or avagraha in the line -> expected; anything else -> unexplained = failure); crashes.  Exit status 1 on an
unexplained difference, or when the new build restores fewer lines exactly than the old one."""
import os
import subprocess
import sys

import config
import rn

NEW_CP = {0x090C, 0x0961, 0x0960, 0x0962, 0x0963, 0x0944, 0x0965, 0x0951, 0x0952, 0x0953, 0x0954, 0x0950}
AVAGRAHA = 0x093D


def chain(tools, text):
    """text -> text through the six stages; returns (result or None on a crash)."""
    data = b"\xff\xfe" + text.encode("utf-16-le")
    for prog in ("uni2acii", "acii2rmn", "rmn2acii", "acii2uni"):
        p = subprocess.run([os.path.join(tools.d, prog)], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)
        if p.returncode != 0:
            return None
        data = p.stdout
    return data.decode("utf-16", "replace").replace("\r\n", "\n")


def run_lines(tools, lines):
    out = chain(tools, "\n".join(lines))
    if out is not None:
        o = out.split("\n")
        if len(o) == len(lines):
            return o
    res = []
    for l in lines:                                        # crash or line-count change: one line at a time
        r = chain(tools, l)
        res.append(r)
    return res


def main(files):
    fail = False
    for path in files:
        text = open(path, "rb").read().decode("utf-8", "replace")
        lines = text.split("\n")
        old_out, new_out = [], []
        for i in range(0, len(lines), 400):
            chunk = lines[i:i + 400]
            old_out += run_lines(rn.old, chunk)
            new_out += run_lines(rn.new, chunk)
        n = len(lines)
        ex_o = sum(1 for a, b in zip(lines, old_out) if a == b)
        ex_n = sum(1 for a, b in zip(lines, new_out) if a == b)
        cr_o = sum(1 for b in old_out if b is None)
        cr_n = sum(1 for b in new_out if b is None)
        diff = [(a, b, c) for a, b, c in zip(lines, old_out, new_out) if b != c]
        why = {"line contains a new character": 0, "line contains avagraha": 0, "unexplained": 0}
        unexplained = []
        for a, b, c in diff:
            cps = {ord(ch) for ch in a}
            if cps & NEW_CP:
                why["line contains a new character"] += 1
            elif AVAGRAHA in cps:
                why["line contains avagraha"] += 1
            else:
                why["unexplained"] += 1
                unexplained.append((a, b, c))
        print("%s\n    lines %d | restored exactly: old %d, new %d | crashed lines: old %d, new %d | old != new: %d  %s"
              % (os.path.relpath(path), n, ex_o, ex_n, cr_o, cr_n, len(diff), why))
        better = sum(1 for a, b, c in diff if c == a and b != a)
        worse = sum(1 for a, b, c in diff if b == a and c != a)
        print("    of the differing lines the new build restores %d that the old did not, and fails on %d that the old restored" % (better, worse))
        for a, b, c in diff[:4]:
            print("      e.g. %r\n           old -> %r\n           new -> %r" % (a[:60], (b or "")[:60], (c or "")[:60]))
        for u in unexplained[:5]:
            print("      UNEXPLAINED", u)
        fail |= bool(unexplained) or ex_n < ex_o or worse > 0
    print("RESULT:", "FAIL" if fail else "PASS")
    return 1 if fail else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = [os.path.join(config.ROOT, "Romenagri", "corp_hi.txt"), os.path.join(config.ROOT, "Romenagri", "test_hi.txt")]
        args += [p for p in os.environ.get("RMN_CORPUS", "").split(os.pathsep) if p]
    sys.exit(main(args))
