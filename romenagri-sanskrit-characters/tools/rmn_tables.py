# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Reader for the Romenagri tables: acii.h, unicode.h, aciihin.h and (since patch 0003) nukta.h.

The headers hold raw 8-bit data (an ACII byte can sit in the source as a literal Latin-1 character), use
CRLF line ends, and, since the Sanskrit additions, also use \\xNN escapes.  Everything here therefore works on
bytes and understands both spellings.

    parse_acii(dir)     -> (declared_len, [(key, bytes), ...])         ordered, duplicates kept (table order matters)
    parse_unicode(dir)  -> (declared_len, [(code_point, byte), ...])
    parse_hin(dir)      -> (declared_len, [(key, bytes), ...])
    parse_nukta(dir)    -> (declared_len, nukta_byte, default_form, [(code_point, base_code_point, nfc), ...])   nukta.h, the nukta layer;
                           (None, None, None, []) for a tree that has no nukta.h.  default_form is 0 (asis), 1 (nfc) or 2 (nfd);
                           nfc is 1 for a letter that Unicode's NFC composes from its consonant and the nukta, 0 for a composition exclusion
    key_table(rows)     -> {key: bytes}                                first row wins, as lookup() does
"""
import os
import re

_HEX = b"0123456789abcdefABCDEF"
_SIMPLE = {b"n": 10, b"r": 13, b"t": 9, b"0": 0, b"\\": 92, b'"': 34, b"'": 39}


def strip_comments(src):
    """Remove /* ... */ and // ... comments.  The tables never contain comment markers inside literals."""
    src = re.sub(rb"/\*.*?\*/", b"", src, flags=re.S)
    return re.sub(rb"//[^\r\n]*", b"", src)


def c_unescape(raw):
    """Decode the body of a C string or character literal that may hold raw bytes and \\xHH escapes."""
    out = bytearray()
    i = 0
    while i < len(raw):
        if raw[i:i + 1] == b"\\":
            nxt = raw[i + 1:i + 2]
            if nxt == b"x":
                j = i + 2
                while j < len(raw) and j < i + 4 and raw[j:j + 1] in _HEX:      # at most two digits are ever written
                    j += 1
                out.append(int(raw[i + 2:j], 16))
                i = j
            elif nxt in _SIMPLE:
                out.append(_SIMPLE[nxt])
                i += 2
            else:
                raise ValueError("unsupported escape in %r" % raw)
        else:
            out.append(raw[i])
            i += 1
    return bytes(out)


def _read(d, name):
    return open(os.path.join(d, name), "rb").read()


def _declared(src, macro):
    m = re.search(rb"#define\s+" + macro + rb"\s+(\d+)", src)
    return int(m.group(1)) if m else None


def _string_rows(d, name, macro):
    src = _read(d, name)
    n = _declared(src, macro)
    body = strip_comments(src)
    rows = []
    for k, v in re.findall(rb'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\}', body):
        rows.append((c_unescape(k).decode("latin-1"), c_unescape(v)))
    return n, rows


def parse_acii(d):
    return _string_rows(d, "acii.h", rb"ACII_LEN")


def parse_hin(d):
    return _string_rows(d, "aciihin.h", rb"ACII_HIN_LEN")


def parse_unicode(d):
    src = _read(d, "unicode.h")
    n = _declared(src, rb"UNI_LEN")
    body = strip_comments(src)
    rows = []
    for lo, hi, ch in re.findall(rb"\{\s*(\d+)\s*,\s*(\d+)\s*,\s*'((?:\\x[0-9A-Fa-f]{1,2}|\\.|[^'\\]))'\s*\}", body):
        b = c_unescape(ch)
        assert len(b) == 1, ch
        rows.append((int(lo) + 256 * int(hi), b[0]))
    return n, rows


_NUM = rb"(0[xX][0-9A-Fa-f]+|\d+)"


def parse_nukta(d):
    """The nukta layer: nukta.h holds NUKTA_LEN rows {low, high, base low, base high, nfc}, a NUKTA_BYTE and the default NUKTA_FORM (written as
    a number or as NUKTA_ASIS, NUKTA_NFC or NUKTA_NFD)."""
    if not os.path.exists(os.path.join(d, "nukta.h")):
        return None, None, None, []
    body = strip_comments(_read(d, "nukta.h"))
    n = _declared(body, rb"NUKTA_LEN")
    nb = re.search(rb"#define\s+NUKTA_BYTE\s+" + _NUM, body)
    fm = re.search(rb"#define\s+NUKTA_FORM\s+(\w+)", body)
    named = {b"NUKTA_ASIS": 0, b"NUKTA_NFC": 1, b"NUKTA_NFD": 2}
    default = named[fm.group(1)] if fm.group(1) in named else int(fm.group(1), 0)
    rows = []
    for m in re.findall(rb"\{\s*" + rb"\s*,\s*".join([_NUM] * 5) + rb"\s*\}", body):
        v = [int(x, 0) for x in m]
        rows.append((v[0] + 256 * v[1], v[2] + 256 * v[3], v[4]))
    return n, int(nb.group(1), 0), default, rows


def key_table(rows):
    t = {}
    for k, v in rows:
        t.setdefault(k, v)
    return t


# ISCII-91 byte meanings, from iscii_map.csv (column 0 = hex byte, column 1 = official name)
def iscii_names(d):
    import csv
    import io
    names = {}
    for r in list(csv.reader(io.StringIO(_read(d, "iscii_map.csv").decode("utf-8"))))[1:]:
        if len(r) > 1 and re.fullmatch(r"[0-9A-F]{2}", r[0]):
            names[int(r[0], 16)] = r[1]
    return names
