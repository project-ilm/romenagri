# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Well-formed ACII texts: the members of the set W of TRANSLITERATION.md, section 9.2.  Shared by tests/rt_filters.py (parts 4 and 5)
and tests/test_underscore.py.

    is_well_formed(data, new)          True if the bytes are a member of W (a regular expression written from the grammar of section 9.2);
                                       new = the Sanskrit additions (bytes 81-8C) belong to the alphabet
    well_formed(rnd, new)              rnd = random.Random(seed); new = also draw from the Sanskrit additions (bytes 81-8C)
    well_formed(rnd, new, between)     between(rnd) -> bytes is called after every syllable (and after the space that may follow it)
                                       and its bytes are inserted there: the way to put ASCII text, say literal underscores (5F),
                                       between the syllables of a well-formed text.  With between=None no extra random number is drawn,
                                       so the stream of texts is the one rt_filters.py has always used.
"""
import re

import config
import rmn_tables

new_uni = rmn_tables.parse_unicode(config.need(config.NEW))[1]
REP = {b for _, b in new_uni}
VOW_OLD = [b for b in range(0xA4, 0xB3) if b in REP]
VOW_NEW = [0x81, 0x82, 0x83]
CONS = [b for b in list(range(0xB3, 0xD9)) + [0x80] if b in REP]
MAT_OLD = [b for b in range(0xDA, 0xE8) if b in REP]
MAT_NEW = [0x84, 0x85, 0x86]
MOD, ACC, HAL, NUK = [0xA1, 0xA2, 0xA3], [0x88, 0x89, 0x8A, 0x8B], 0xE8, 0xE9
NUKTA_OK = {0xB3, 0xB4, 0xB5, 0xBA, 0xBF, 0xC0, 0xC9, 0xCD, 0xC6, 0xCF, 0xD2}      # KA KHA GA JA DDA DDHA PHA YA NA RA LLA


def _recognizer(new):
    """the grammar of section 9.2 as a regular expression over bytes (the rule that a syllable ending in a halant is followed by a space
    or by the end of the text is a lookahead)"""
    def cls(bs):
        return b"[" + b"".join(b"\\x%02x" % b for b in sorted(bs)) + b"]"
    vowel = cls(VOW_OLD + (VOW_NEW if new else []))
    sign = cls(MAT_OLD + (MAT_NEW if new else []))
    acc = cls(ACC) if new else b"(?!)"
    mod = cls(MOD)
    special = cls([0xEB] + ([0x87, 0x8C] if new else []))
    withn = cls(sorted(c for c in CONS if c in NUKTA_OK))
    without = cls(sorted(c for c in CONS if c not in NUKTA_OK))
    one = b"(?:" + withn + b"\\xe9?|" + without + b")"
    cluster = one + b"(?:\\xe8" + one + b")*"
    syl = (b"(?:" + cluster + b"\\xe8(?=\\x20|\\Z)"
           + b"|" + cluster + b"\\xe8" + mod
           + b"|(?:" + vowel + acc + b"?|" + special + b"|" + cluster + acc + b"?" + sign + b"?" + acc + b"?)" + mod + b"?)")
    return re.compile(b"(?:" + syl + b"|\\x20)*")


_RECOGNIZERS = {}


def is_well_formed(data, new=True):
    """is the byte string a member of W?"""
    rx = _RECOGNIZERS.get(new)
    if rx is None:
        rx = _RECOGNIZERS[new] = _recognizer(new)
    return rx.fullmatch(data) is not None


def syllable(rnd, new):
    vow = VOW_OLD + (VOW_NEW if new else [])
    mat = MAT_OLD + (MAT_NEW if new else [])
    r = rnd.random()
    out = []
    if r < 0.12:                                                    # independent vowel [accent]
        out.append(rnd.choice(vow))
        if new and rnd.random() < 0.3:
            out.append(rnd.choice(ACC))
    elif r < 0.17:                                                  # avagraha, OM, double danda
        out.append(rnd.choice([0xEB] + ([0x87, 0x8C] if new else [])))
    else:                                                           # consonant [nukta] { halant consonant [nukta] } ...
        n = rnd.choice([1, 1, 1, 2, 2, 3])
        for i in range(n):
            c = rnd.choice(CONS)
            out.append(c)
            if c in NUKTA_OK and rnd.random() < 0.3:
                out.append(NUK)
            if i < n - 1:
                out.append(HAL)
        t = rnd.random()
        if t < 0.15:                                                # ... a final halant
            out.append(HAL)
        else:                                                       # ... or [accent] [vowel sign] [accent]
            if new and rnd.random() < 0.15:
                out.append(rnd.choice(ACC))
            if t < 0.75:
                out.append(rnd.choice(mat))
            if new and rnd.random() < 0.15:
                out.append(rnd.choice(ACC))
    if rnd.random() < 0.2:
        out.append(rnd.choice(MOD))
    return out


def well_formed(rnd, new, between=None):
    seq = []
    for _ in range(rnd.randint(1, 6)):
        sy = syllable(rnd, new)
        seq += sy
        if (sy and sy[-1] == HAL) or rnd.random() < 0.3:             # a halant-final syllable ends its word
            seq.append(0x20)
        if between is not None:
            seq += between(rnd)
    return bytes(seq)
