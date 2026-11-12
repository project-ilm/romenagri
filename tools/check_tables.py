#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Lint for the three Romenagri tables (acii.h, unicode.h, aciihin.h).

    python3 tools/check_tables.py <Romenagri dir> [--free]

Run it after every edit of a table.  It needs no compiler: the parser and the transducer are checked through the executable
models in tests/model.py (themselves checked against the C code by tests/diff_parser.py and tests/rt_filters.py).

Checks (ERROR makes the exit status 1; "warn" lines are the known, documented legacy oddities):
  T1  ACII_LEN, UNI_LEN and ACII_HIN_LEN equal the number of rows
  T2  the control row {"", "\\xEFB"} is at index 0 (acii2rmn.c tests tok[i-1] against acii_chrt[0][1][0])
  T3  every key uses the alphabet  [a-z_]  with an optional leading '^'  (legacy exceptions: "", "__", "|", "^")
  T4  no duplicate key, no duplicate Unicode code point, no ACII byte shared by two code points
  T5  every Unicode row has an acii.h row for its byte, and every one-byte acii.h row with a byte >= 0x80 has a Unicode row
  T6  every key parses (rmn2acii) to exactly the bytes of its own row; every one-byte row is produced (acii2rmn) from its byte
  T7  conjunct check: consonant + halant + X  and  X + consonant  survive acii2rmn followed by rmn2acii for every letter X
      (this is the check that catches a new string that extends an existing token, e.g. "_d" + "ha")
  T8  marker rule: in every key except "__" each '_' is followed by a letter (TRANSLITERATION.md, section 14.3).  Together with the
      decoder doubling every literal underscore this makes a marker the LAST underscore of its run and the run before it even,
      which is what lets the parser pair the underscores of a run from the left (a regular language, two states)
  --free   prints the map of free ACII bytes with their ISCII-91 meaning and the allocation class
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "tests"))
import model  # noqa: E402
import rmn_tables  # noqa: E402

LEGACY_KEYS = {"", "__", "|", "^"}
# rows that exist in the table but that no translator can reach any more (documented in TRANSLITERATION.md, section 11)
KNOWN_UNREACHABLE = {"^ra"}
HALANT, NUKTA = 0xE8, 0xE9


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    d = argv[0]
    errors = []

    def err(msg):
        errors.append(msg)
        print("ERROR  " + msg)

    def warn(msg):
        print("warn   " + msg)

    n_a, acii = rmn_tables.parse_acii(d)
    n_u, uni = rmn_tables.parse_unicode(d)
    n_h, hin = rmn_tables.parse_hin(d)
    T = rmn_tables.key_table(acii)
    print("acii.h: %d rows, unicode.h: %d rows, aciihin.h: %d rows" % (len(acii), len(uni), len(hin)))

    # T1
    for name, declared, rows in (("ACII_LEN", n_a, acii), ("UNI_LEN", n_u, uni), ("ACII_HIN_LEN", n_h, hin)):
        if declared != len(rows):
            err("T1 %s is %s but the table has %d rows" % (name, declared, len(rows)))
    # T2
    if not acii or acii[0] != ("", b"\xefB"):
        err("T2 row 0 of acii.h must be the control row {\"\", \"\\xEFB\"}")
    # T3
    for key, _ in acii:
        if key in LEGACY_KEYS:
            continue
        body = key[1:] if key.startswith("^") else key
        if not body or any(c not in "abcdefghijklmnopqrstuvwxyz_" for c in body):
            err("T3 key %r uses characters outside [a-z_]" % key)
    # T4
    seen = {}
    for i, (key, bs) in enumerate(acii):
        if key in seen:
            err("T4 key %r appears in acii.h rows %d and %d (the second is unreachable: lookup() takes the first)" % (key, seen[key], i))
        seen.setdefault(key, i)
    cps, byts = {}, {}
    for cp, b in uni:
        if cp in cps:
            err("T4 U+%04X appears twice in unicode.h" % cp)
        cps[cp] = b
        if b in byts:
            err("T4 ACII byte 0x%02X is given to both U+%04X and U+%04X in unicode.h (acii2uni can only return the first)" % (b, byts[b], cp))
        byts.setdefault(b, cp)
    # T5
    first_bytes = {bs[0] for _, bs in acii if bs}
    single = {bs[0] for _, bs in acii if len(bs) == 1}
    for b in sorted(byts):
        if b not in first_bytes:
            err("T5 unicode.h maps U+%04X to 0x%02X but acii.h has no row for that byte" % (byts[b], b))
    for b in sorted(single):
        if b >= 0x80 and b not in byts:
            warn("T5 acii.h row for byte 0x%02X has no Unicode row" % b)
    hin_bytes = {x for _, bs in hin for x in bs}
    missing_hin = sorted(b for b in single if b >= 0x80 and b not in hin_bytes)
    if missing_hin:
        print("       (no saral rendering in aciihin.h for: %s)" % " ".join("%02X" % b for b in missing_hin))

    # T6  keys -> bytes (parser) and bytes -> keys (encoder)
    rows = acii
    for i, (key, bs) in enumerate(acii):
        if i == 0:
            continue
        try:
            got = model.model_parse(key, T, new=True)
        except (model.Missing, model.Overrun) as e:
            err("T6 parsing the key %r of its own row fails (%s)" % (key, type(e).__name__))
            continue
        if got != bs:
            (warn if key in KNOWN_UNREACHABLE else err)("T6 key %r parses to %s but its row says %s" % (key, got.hex(), bs.hex()))
        first = next((k for k, b2 in acii if b2 and b2[0] == bs[0]), None) if bs else None
        if len(bs) == 1:
            if first != key:
                err("T6 byte 0x%02X is claimed by the earlier row %r before this row %r (acii2rmn takes the first row)" % (bs[0], first, key))
            else:
                enc = model.model_encode(bs, rows)
                if enc != key:
                    err("T6 acii2rmn turns byte 0x%02X into %r, the table says %r" % (bs[0], enc, key))
        elif bs and first != key:
            print("       (row %r is shadowed in acii2rmn by %r; it is still the parser's output for that key)" % (key, first))

    # T8  marker rule
    bad8 = 0
    for key, _ in acii:
        if key in LEGACY_KEYS:
            continue
        for i, c in enumerate(key):
            if c == "_" and not (i + 1 < len(key) and "a" <= key[i + 1] <= "z"):
                bad8 += 1
                err("T8 key %r: the underscore at position %d is not followed by a letter (marker rule, TRANSLITERATION.md section 14.3)" % (key, i))
    n_us = sum(1 for key, _ in acii if key not in LEGACY_KEYS and "_" in key)
    print("T8: %d keys contain a marker underscore, %d violate the marker rule" % (n_us, bad8))

    # T7  conjunct check
    consonant_bytes = [bs[0] for k, bs in acii if len(bs) == 1 and k.endswith("a") and not k.startswith("^") and (0xB3 <= bs[0] <= 0xD8 or bs[0] == 0x80)]
    letters = [bs[0] for k, bs in acii if len(bs) == 1 and not k.startswith("^") and k not in ("", "|", "__") and bs[0] >= 0x80
               and bs[0] not in (HALANT, NUKTA) and not (bs[0] in (0xA1, 0xA2, 0xA3) or bs[0] >= 0xE8 and bs[0] != 0xEB)]
    # the independent vocalic vowels conflate with their sign after a halant by design (as "_ri" always did): exclude them
    vocalic = {bs[0] for k, bs in acii if k in ("_ri", "_li", "_lee", "_ree")}
    bad = 0
    for c in consonant_bytes:
        for x in letters:
            for seq, tag in ((bytes([c, HALANT, x]), "C+halant+X"), (bytes([x, c]), "X+C")):
                if tag == "C+halant+X" and x in vocalic:
                    continue
                try:
                    back = model.model_filter(seq, rows, T)
                except (model.Missing, model.Overrun, model.Crash):
                    back = None
                if back != seq:
                    bad += 1
                    if bad <= 12:
                        err("T7 %s %s does not survive acii2rmn + rmn2acii: %s -> %r -> %s"
                            % (tag, seq.hex(), "", model.model_encode(seq, rows), back and back.hex()))
    print("T7: %d consonants x %d letters, both orders: %d failures" % (len(consonant_bytes), len(letters), bad))

    if "--free" in argv:
        free_report(d, acii, uni, hin)

    print("%d error(s)" % len(errors))
    return 1 if errors else 0


def free_report(d, acii, uni, hin):
    names = rmn_tables.iscii_names(d)
    used = {x for _, bs in acii for x in bs} | {b for _, b in uni} | {x for _, bs in hin for x in bs}
    reserved = {0xEF: "attribute prefix (ISCII ATR) - acii2rmn skips the byte after it", 0xF0: "extension prefix (ISCII EXT)"}
    avoided = {0xA0: "U+00A0 NO-BREAK SPACE reaches this byte through uni2acii's low-byte fallback (TRANSLITERATION.md, section 10.3)"}
    print("\nFree bytes in 0x80-0xFF, with the ISCII-91 meaning and the allocation class:")
    counts = {}
    for b in range(0x80, 0x100):
        if b in used:
            continue
        if b in reserved:
            cls = "never"
        elif b in avoided:
            cls = "avoided (no-break space)"
        elif 0xF1 <= b <= 0xFA:
            cls = "digits (reserved for Devanagari digits)"
        elif b in names and not names[b].strip().lower().startswith("unused"):
            cls = "ISCII-assigned: use for that very character"
        elif b < 0xA0:
            cls = "C1 extension block (first choice for new characters)"
        else:
            cls = "ISCII-unassigned"
        counts[cls] = counts.get(cls, 0) + 1
        print("   0x%02X  %-46s %s" % (b, cls, reserved.get(b) or avoided.get(b) or names.get(b, "")))
    print("   total free: %d  (%s)" % (sum(counts.values()), "; ".join("%s: %d" % kv for kv in sorted(counts.items()))))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
