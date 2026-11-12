# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Executable models of the two Romenagri translators.

    model_parse(s, T, new=True)     Romenagri -> ACII  (rmn2acii.c: the recursive-descent parser)      -> bytes
                                    runs the grammar printed in Romenagri/TRANSLITERATION.md, section 5.3 (tests/spec_model.py);
                                    new = False (the unpatched parser), "mid" (patch 0001: the Sanskrit characters), True (patches 0001 and 0002:
                                    with the guards of section 14.7; patch 0003 does not touch the parser)
    model_encode(data, rows)        ACII -> Romenagri  (acii2rmn.c: the stack transducer)              -> str
    model_filter(data, rows, T)     what the two filters do to a run of ACII: acii2rmn, then rmn2acii on [A-Za-z_] runs
    parse_table(dir_or_acii_h)      {key: bytes}, first row wins (as lookup() does)
    parse_rows(dir_or_acii_h)       [(key, bytes)] in table order (as acii2rmn scans it)

The written grammar is only worth something if it predicts the C code.  tests/diff_parser.py compares it with the real parser
(library level, tests/harness.c) and with a second, hand-written parser (tests/handwritten_parser.py) on every string up to
length 4 over the whole input alphabet plus random longer ones, and tests/rt_filters.py compares model_encode and model_filter
with the real filters.

Conventions: s is a str of ASCII; "end" means the NUL terminator.
  Overrun  = the C code would read past the NUL (undefined behaviour: one of the eleven rules of TRANSLITERATION.md, section 14.6,
             jumps over, or keeps as text, a character that is the terminator -- 'c' as the last letter, `_e` or `ke` at the end ...);
             such inputs are not compared.  The parser of this package, with the guards of section 14.7, never raises it; the parsers
             without them (new=False, "mid") do.
  Missing  = lookup() returns NULL and strcat(NULL) crashes (SEGV) in C.
  Crash    = acii2rmn pops an empty stack and dereferences NULL (SEGV) in C.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
import rmn_tables  # noqa: E402

LEV1 = "|kgcjtdnpbmyrlwsxh_^"
OLD, MID, NEW = False, "mid", True                 # the three versions of the parser: unpatched; patch 0001; patches 0001 and 0002 (0003 leaves the parser alone)


def has_sanskrit(new):
    """does the version `new` of the parser have the rules of patch 0001?"""
    return new is True or new == MID


def has_guards(new):
    """does the version `new` of the parser have the guards of patch 0002 (section 14.7)?"""
    return new is True


class Overrun(Exception):
    pass


class Missing(Exception):
    pass


class Crash(Exception):
    pass


def _acii_h(path):
    return os.path.join(path, "acii.h") if os.path.isdir(path) else path


def parse_rows(path):
    d = os.path.dirname(os.path.abspath(_acii_h(path)))
    return rmn_tables.parse_acii(d)[1]


def parse_table(path):
    return rmn_tables.key_table(parse_rows(path))


_SPECS = {}


def model_parse(s, T, new=True):
    """Romenagri -> ACII (rmn2acii.c), by running the grammar of Romenagri/TRANSLITERATION.md, section 5.3 (tests/spec_model.py).
    RMN_GRAMMAR=<file> reads the ```rmn2acii-grammar block of another document.   -> bytes"""
    import spec_model
    if None not in _SPECS:
        _SPECS[None] = spec_model.load_doc()
    return spec_model.spec_parse(_SPECS[None], s, T, new=new)


# ------------------------------------------------------------------------------------------------------------------
# ACII -> Romenagri : acii2rmn.c
# ------------------------------------------------------------------------------------------------------------------
def model_encode(data, rows):
    """The stack machine of acii2rmn().  rows = table rows in table order.  Raises Crash where the C code dereferences NULL."""
    stack = []
    ef = rows[0][1][0]                                  # acii_chrt[0][1][0]: the ISCII attribute prefix 0xEF

    def pop1():
        if not stack:
            raise Crash("pop on an empty stack")
        return stack.pop()

    for i, b in enumerate(data):
        hit = None
        for key, bs in rows:                            # first row whose FIRST byte equals the input byte wins
            if bs and bs[0] == b:
                hit = key
                break
        if hit is not None:
            if hit[:1] == "^" and stack:                # a dependent sign (or the halant "^"): remove the consonant's 'a'
                stack.pop()
                if hit[1:2] == "z":                     # the nukta: "ka" + nukta -> "kza", with two exceptions
                    t1 = pop1()
                    if t1 == "h":
                        t2 = pop1()
                        if t2 == "d":
                            stack.extend("_rdha")
                        else:
                            stack.append(t2)
                            stack.extend("hza")
                    elif t1 == "d":
                        stack.extend("_rda")
                    else:
                        stack.append(t1)
                        stack.extend("za")
                else:
                    stack.extend(hit[1:])
            else:
                stack.extend(hit)
        else:
            prev = data[i - 1] if i > 0 else None       # acii2rmn.c reads tok[i-1], tok[-1] for i == 0: assume "not 0xEF"
            if prev != ef:
                stack.append(chr(b))
    return "".join(stack)


def model_filter(data, rows, T, new=True):
    """acii2rmn on the whole run, then rmn2acii on every maximal [A-Za-z_] run (what the two lex filters hand to the parser)."""
    rmn = model_encode(data, rows)
    out = bytearray()
    i = 0
    while i < len(rmn):
        c = rmn[i]
        if c.isascii() and (c.isalpha() or c == "_"):
            j = i
            while j < len(rmn) and rmn[j].isascii() and (rmn[j].isalpha() or rmn[j] == "_"):
                j += 1
            out.extend(model_parse(rmn[i:j], T, new=new))
            i = j
        else:
            out.append(ord(c))
            i += 1
    return bytes(out)
