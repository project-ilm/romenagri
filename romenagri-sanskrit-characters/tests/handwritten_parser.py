# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""The Romenagri -> ACII parser written out by hand, as ordinary Python, one function per state of rmn2acii.c.

This is the INDEPENDENT cross-check of the grammar in Romenagri/TRANSLITERATION.md, section 5.3: it was written from the C code,
the grammar from the C code and the document, and tests/diff_parser.py shows that the two agree with each other and with the C code
on more than a million strings.  Nothing else uses it -- everything else (the table lint, the round-trip tests, the document
generator) runs the grammar of the document through tests/spec_model.py, so that the document is the single place to change when
the parser changes.  After an extension (section 8) either mirror the change here or run the cross-check without it:

    RMN_SKIP_HANDWRITTEN=1 python3 tests/diff_parser.py

Same conventions as tests/model.py:  s is a str of ASCII, "end" is the NUL terminator, Overrun / Missing are the exceptions of model.py.
`new` names the version of the parser, as in tests/model.py: False (unpatched), "mid" (patch 0001: the Sanskrit characters, no guards),
True (patches 0001 and 0002: with the twelve guards of section 14.7, each of them a test `no_partner` in front of one branch;
patch 0003, the nukta layer, does not touch the parser).
"""
from model import LEV1, Missing, Overrun, has_guards, has_sanskrit


def handwritten_parse(s, T, new=True):
    out = bytearray()
    n = len(s)
    sk = has_sanskrit(new)                     # the branches of patch 0001
    gd = has_guards(new)                       # the guards of patch 0002

    def at(i):
        if i < n:
            return s[i]
        if i == n:
            return "\0"
        raise Overrun(i)

    def lk(key):
        if key not in T:
            raise Missing(key)
        out.extend(T[key])

    def raw(c):
        if c != "\0":
            out.extend(c.encode("latin-1"))

    def halant():
        lk("^")

    def starts_token(c):          # strstr (lev1, c2s (c)) != NULL ; true for the terminator too
        return c == "\0" or c in LEV1

    def no_partner(c):            # the test of every guard: an underscore or the end of the string
        return c == "_" or c == "\0"

    # ---- level1: the start of a unit -------------------------------------------------------------------
    def level1(i):
        if i > n:
            raise Overrun(i)
        if i == n:
            return
        c = s[i]
        if c == "|":
            lk("|"); level1(i + 1)
        elif c in "nmywxr":
            lk(c + "a"); level2a(i + 1)
        elif c in "gtdpbslkj":
            level2b(i + 1, c)
        elif c == "c":
            if gd and no_partner(at(i + 1)):   # guard: a 'c' with no 'h' after it is the letter c
                raw(c); level1(i + 1)
            else:                              # 'c' swallows the next letter unseen (it is the 'h' of "ch")
                level2b(i + 2, "ch")
        elif c == "_":
            level2c(i + 1)
        elif c == "^":
            matra(i + 1)
        else:
            raw(c); level1(i + 1)

    # ---- level2b: a consonant stem that may take an aspirate 'h' or the 'vr' of "lvra" --------------------
    def level2b(i, stem):
        if i > n:
            raise Overrun(i)
        if i == n:
            lk(stem + "a"); halant(); return
        c = s[i]
        if c == "h":
            lk(stem + "ha"); level2a(i + 1)
        elif c == "v" and not (gd and no_partner(at(i + 1))):      # guard: no 'r' after the v: the stem keeps its 'a'
            lk(stem + "vra"); level2a(i + 2)
        else:
            lk(stem + "a"); level2a(i)

    # ---- level2a: what follows a consonant that has just been written with its inherent vowel --------------
    def level2a(i):
        if i > n:
            raise Overrun(i)
        if i == n:
            halant(); return
        if s[i] in LEV1:
            halant(); level1(i)
        else:
            matra(i)

    # ---- matra: vowel sign after a consonant (or after an explicit '^') -----------------------------------
    def matra(i):
        if i > n:
            raise Overrun(i)
        if i == n:
            halant(); return
        c = s[i]
        if c == "i":
            lk("^i"); level1(i + 1)
        elif c == "u":
            lk("^u"); level1(i + 1)
        elif c == "e":
            if gd and no_partner(at(i + 1)):
                raw(c); level1(i + 1)
            else:
                lk("^ee"); level1(i + 2)
        elif c == "z":
            lk("^za"); level2a(i + 1)
        elif c == "_":
            if sk and at(i + 1) == "l" and at(i + 2) == "i":
                lk("^_li"); level1(i + 3)
            elif sk and at(i + 1) == "l" and at(i + 2) == "e" and at(i + 3) == "e":
                lk("^_lee"); level1(i + 4)
            elif sk and at(i + 1) == "r" and at(i + 2) == "e" and at(i + 3) == "e":
                lk("^_ree"); level1(i + 4)
            elif gd and (no_partner(at(i + 1)) or no_partner(at(i + 2))):
                level1(i)                       # guard: an underscore or the end where "ri" should be; the underscore is read again
            else:
                lk("^_ri"); level1(i + 3)
        elif c == "o":
            d = at(i + 1)
            if gd and no_partner(d):
                raw(c); level1(i + 1)
            elif d == "o":
                lk("^oo"); level1(i + 2)
            elif d == "w":
                lk("^ow"); level1(i + 2)
            elif d == "a":
                lk("^oa"); level1(i + 2)
            elif d == "u":
                lk("^ou"); level1(i + 2)
            else:
                raw(d); level1(i + 2)
        elif c == "a":
            d = at(i + 1)
            if starts_token(d):
                level1(i + 1)
            elif d == "a":
                lk("^aa"); level1(i + 2)
            elif d == "e":
                if at(i + 2) == "e":
                    lk("^aee"); level1(i + 3)
                else:
                    lk("^ae"); level1(i + 2)
            elif d == "i":
                lk("^ai"); level1(i + 2)
            elif d == "o":
                lk("^ao"); level1(i + 2)
            elif d == "u":
                lk("^au"); level1(i + 2)
            else:
                raw(d); level1(i + 2)
        else:
            raw(c); level1(i + 1)

    # ---- vocalic: independent byte, or the sign byte if a halant has just been written ----------------------
    def vocalic(indep, dep):
        if len(out) > 0 and out[-1] == T["^"][0]:
            out.pop(); lk(dep)
        else:
            lk(indep)

    # ---- level2c: everything introduced by '_' ----------------------------------------------------------
    def level2c(i):
        if i > n:
            raise Overrun(i)
        if i == n:
            halant(); return
        c = s[i]
        if c == "s":
            lk("_s"); level1(i + 1)
        elif c == "u":
            lk("_u"); level1(i + 1)
        elif c == "m":
            lk("_m"); level1(i + 1)
        elif c == "i":
            lk("_i"); level1(i + 1)
        elif c == "e":
            if gd and no_partner(at(i + 1)):
                raw(c); level1(i + 1)
            else:
                lk("_ee"); level1(i + 2)
        elif c == "y":
            if gd and no_partner(at(i + 1)):
                raw(c); level1(i + 1)
            else:
                lk("_yna"); level2a(i + 2)
        elif c == "t":
            level2b(i + 1, "_t")
        elif c == "d":
            level2b(i + 1, "_d")
        elif c == "h":
            if at(i + 1) == "h":
                lk("_hh"); level1(i + 2)
            else:
                lk("_ha"); level2a(i + 1)
        elif c == "o":
            d = at(i + 1)
            if gd and no_partner(d):
                raw(c); level1(i + 1)
            elif d == "o":
                lk("_oo"); level1(i + 2)
            elif d == "w":
                lk("_ow"); level1(i + 2)
            elif d == "a":
                lk("_oa"); level1(i + 2)
            elif d == "u":
                lk("_ou"); level1(i + 2)
            elif sk and d == "m":
                lk("_om"); level1(i + 2)
            else:
                raw(d); level1(i + 2)
        elif c == "n":
            d = at(i + 1)
            if gd and no_partner(d):
                raw(c); level1(i + 1)
            elif d == "a":
                lk("_na"); level1(i + 2)
            elif d == "n":
                lk("_nna"); level2a(i + 2)
            elif d == "g":
                lk("_nga"); level2a(i + 2)
            elif d == "z":
                lk("_nza"); level2a(i + 2)
            else:
                raw(d); level1(i + 2)
        elif c == "r":
            d = at(i + 1)
            if gd and no_partner(d):
                raw(c); level1(i + 1)
            elif d == "i":
                if len(out) > 0 and out[-1] == T["^"][0]:
                    out.pop(); lk("^_ri")
                else:
                    lk("_ri")
                level1(i + 2)
            elif d == "d":
                level2b(i + 2, "_rd")
            elif d == "r":
                level2b(i + 2, "_rr")
            elif sk and d == "e" and at(i + 2) == "e":
                vocalic("_ree", "^_ree"); level1(i + 3)
            else:
                raw(d); level1(i + 2)
        elif c == "a":
            d = at(i + 1)
            if starts_token(d):
                lk("_a"); level1(i + 1)
            elif d == "a":
                lk("_aa"); level1(i + 2)
            elif d == "e":
                if at(i + 2) == "e":
                    lk("_aee"); level1(i + 3)
                else:
                    lk("_ae"); level1(i + 2)
            elif d == "i":
                lk("_ai"); level1(i + 2)
            elif d == "o":
                lk("_ao"); level1(i + 2)
            elif d == "u":
                lk("_au"); level1(i + 2)
            else:
                raw(d); level1(i + 2)
        elif c == "j":
            d = at(i + 1)
            if gd and no_partner(d):
                raw(c); level1(i + 1)
            elif d == "z":
                lk("_jza"); level2a(i + 2)
            else:
                raw(d); level1(i + 2)
        elif sk and c == "l":
            if at(i + 1) == "i":
                vocalic("_li", "^_li"); level1(i + 2)
            elif at(i + 1) == "e" and at(i + 2) == "e":
                vocalic("_lee", "^_lee"); level1(i + 3)
            else:
                raw(c); level1(i + 1)
        elif sk and c == "v":
            d = at(i + 1)
            if d == "d":
                lk("_vd"); level1(i + 2)
            elif d in ("u", "n", "g", "c"):
                lk("_v" + d + "a"); level2a(i + 2)       # accents are written like the nukta
            else:
                raw("v"); level1(i + 1)
        else:
            raw(c); level1(i + 1)

    level1(0)
    return bytes(out)
