# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""uni2acii / acii2uni: the new characters convert both ways, nothing that worked before changes.   usage: python3 tests/test_unicode.py

  (a) every code point that is new in unicode.h:  new build  U+XXXX -> its ACII byte -> U+XXXX ;  old build does not do that
  (b) every code point of the old unicode.h converts exactly as before (both directions)
  (c) a mixed text containing every mapped code point, ASCII and newlines survives  UTF-16 -> ACII -> UTF-16
  (d) the code points of the Devanagari block that unicode.h still does not map (the classes of TRANSLITERATION.md, section 10.4):
        - uni2acii writes the LOW BYTE of each of them except the nine composites (a silent corruption: U+0900 becomes a NUL),
        - the ten digits are turned into ASCII digits by fixuninum, which runs before uni2acii,
        - the nine composites (U+0934, U+0958-U+095F) have a canonical decomposition into mapped code points, and since patch 0003
          (the nukta layer, section 15; tests/test_nukta.py tests the layer itself) uni2acii writes each of them as the byte of its
          consonant and E9, where the unpatched converter wrote the low byte (U+0934 became "4").  Whether they go in as the single
          code point or as consonant + nukta, they go through the whole chain  uni2acii -> acii2rmn -> rmn2acii -> acii2uni  and come
          out as a consonant and a nukta (the default form, asis: what acii2uni always wrote for a consonant and E9); with -f nfc on both
          converters they come out as Unicode's NFC writes them, with -f nfd as NFD writes them.
  (e) characters that real text contains and that are neither Devanagari nor ASCII (no-break space, dashes, quotes, bullets, the rupee
      sign, ...): uni2acii writes their low byte, so none of them may land on a NEW byte, and each must come out of
      uni2acii -> acii2uni exactly as it did before the patch.  (This is why OM is at 8C and not at A0, section 10.3: the no-break
      space is U+00A0.)  The rarer characters that do reach a new byte are counted, not asserted.
Exit status 1 if (a), (b), (c), (d) or (e) fails."""
import sys
import unicodedata

import config
import rmn_tables
import rn

old_u = rmn_tables.parse_unicode(config.need(config.OLD))[1]
new_u = rmn_tables.parse_unicode(config.need(config.NEW))[1]
added = [r for r in new_u if r not in old_u]
fail = False

print("(a) %d new rows in unicode.h" % len(added))
ok = 0
for cp, b in added:
    ch = chr(cp)
    fwd, back = rn.new.u2a(ch), rn.new.a2u(bytes([b]))
    o_fwd, o_back = rn.old.u2a(ch), rn.old.a2u(bytes([b]))
    good = fwd == bytes([b]) and back == ch
    ok += good
    fail |= not good or (o_fwd == bytes([b]) and o_back == ch)
    print("    U+%04X %-34s -> new 0x%s -> U+%s %s | old: %s -> %s" % (
        cp, unicodedata.name(ch, "?"), fwd.hex(), "%04X" % ord(back[0]) if back else "----", "ok" if good else "WRONG",
        o_fwd.hex(), "U+%04X" % ord(o_back[0]) if o_back else "----"))
print("    round trip exact in the new build: %d of %d" % (ok, len(added)))

print("(b) the %d old rows" % len(old_u))
same = 0
for cp, b in old_u:
    ch = chr(cp)
    r = (rn.new.u2a(ch), rn.new.a2u(bytes([b])), rn.old.u2a(ch), rn.old.a2u(bytes([b])))
    same += r[0] == r[2] and r[1] == r[3] and r[0] == bytes([b])
print("    identical to the old build and to the table: %d of %d" % (same, len(old_u)))
fail |= same != len(old_u)

print("(c) mixed text")
chars = [chr(cp) for cp, _ in new_u]
text = "Rigveda 1.1.1: " + " ".join(chars) + "\n" + "".join(chars) + " abc 123 (x) ; \"q\"\n" + "ॐ भूर्भुवः स्वः ॥\n"
a = rn.new.u2a(text)
back = rn.new.a2u(a)
exact = back.replace("﻿", "") == text
print("    %d characters, %d ACII bytes, round trip exact: %s" % (len(text), len(a), exact))
fail |= not exact

print("(d) the unmapped code points of U+0900-U+097F")
mapped_new = {c for c, _ in new_u}
unm = [cp for cp in range(0x900, 0x980) if cp not in mapped_new]
digits = [cp for cp in unm if unicodedata.category(chr(cp)) == "Nd"]
composites = [cp for cp in unm if cp not in digits and unicodedata.normalize("NFD", chr(cp)) != chr(cp)
              and all(ord(c) in mapped_new for c in unicodedata.normalize("NFD", chr(cp)))]
uncovered = [cp for cp in unm if cp not in digits and cp not in composites]
print("    %d unmapped: %d digits, %d composites, %d uncovered" % (len(unm), len(digits), len(composites), len(uncovered)))
low = [cp for cp in unm if rn.new.u2a(chr(cp)) == bytes([cp & 255])]
low_mid = [cp for cp in unm if rn.mid.u2a(chr(cp)) == bytes([cp & 255])]
layered = [cp for cp in composites if len(rn.new.u2a(chr(cp))) == 2 and rn.new.u2a(chr(cp))[1] == 0xE9]
print("    patch 0001 only: uni2acii writes the low byte for %d of %d (a silent corruption of text)" % (len(low_mid), len(unm)))
print("    new build: uni2acii writes the byte of the consonant and E9 for %d of the %d composites; the low byte for %d of the other %d"
      % (len(layered), len(composites), len(low), len(unm) - len(composites)))
fail |= len(low_mid) != len(unm) or len(layered) != len(composites) or len(low) != len(unm) - len(composites)
rc, out = rn.new.run("fixuninum", "".join(chr(cp) for cp in digits).encode("utf-8"))
print("    fixuninum on the ten digits: %r" % out)
fail |= out != b"0123456789"


def chain(text, form=None):
    """the whole chain; `form` is the -f flag of the two Unicode converters (None: the default form)"""
    data = b"\xff\xfe" + text.encode("utf-16-le")
    for prog in ("uni2acii", "acii2rmn", "rmn2acii", "acii2uni"):
        rc, data = rn.new.run(prog, data, args=("-f", form) if form and prog in ("uni2acii", "acii2uni") else ())
        if rc != 0:
            return None
    return data.decode("utf-16", "replace")


nfc = lambda t: unicodedata.normalize("NFC", t)
nfd = lambda t: unicodedata.normalize("NFD", t)
good = [cp for cp in composites if chain(nfd(chr(cp))) == nfd(chr(cp))]
print("    composites whose NFD form (consonant + nukta) comes out of the whole chain as that NFD form: %d of %d" % (len(good), len(composites)))
fail |= len(good) != len(composites)
raw = [cp for cp in composites if chain(chr(cp)) == nfd(chr(cp))]
print("    ... and composites whose single code point comes out as consonant + nukta, WITHOUT normalisation first: %d of %d" % (len(raw), len(composites)))
fail |= len(raw) != len(composites)
as_nfc = [cp for cp in composites if chain(chr(cp), "nfc") == nfc(chr(cp)) and chain(nfd(chr(cp)), "nfc") == nfc(chr(cp))]
print("    with -f nfc on both converters, either spelling comes out as NFC writes it: %d of %d (%d of them as the single code point)"
      % (len(as_nfc), len(composites), sum(1 for cp in as_nfc if nfc(chr(cp)) == chr(cp))))
fail |= len(as_nfc) != len(composites)
as_nfd = [cp for cp in composites if chain(chr(cp), "nfd") == nfd(chr(cp)) and chain(nfd(chr(cp)), "nfd") == nfd(chr(cp))]
print("    with -f nfd on both converters, either spelling comes out as NFD writes it: %d of %d" % (len(as_nfd), len(composites)))
fail |= len(as_nfd) != len(composites)
print("    still uncovered: %s" % " ".join("U+%04X" % cp for cp in uncovered))
for cp in (0x200C, 0x200D):
    print("    U+%04X %-30s uni2acii -> %s (not in the Devanagari block; ZWNJ/ZWJ are not mapped)" % (cp, unicodedata.name(chr(cp), "?"), rn.new.u2a(chr(cp)).hex()))

print("(e) characters of real text outside Devanagari and ASCII (uni2acii writes the low byte of each)")
NEWB = {b for _, b in added}
COMMON = [0x00A0, 0x00AD, 0x00B7, 0x00D7, 0x00E9, 0x2002, 0x2003, 0x2009, 0x200B, 0x200C, 0x200D, 0x200E, 0x200F, 0x2010, 0x2011, 0x2012,
          0x2013, 0x2014, 0x2015, 0x2018, 0x2019, 0x201C, 0x201D, 0x2020, 0x2022, 0x2026, 0x2030, 0x20B9, 0x2122, 0x2190, 0x2192, 0xFFFD]
on_new = [cp for cp in COMMON if (cp & 255) in NEWB]
changed = [cp for cp in COMMON if rn.new.a2u(rn.new.u2a(chr(cp))) != rn.old.a2u(rn.old.u2a(chr(cp)))]
print("    %d common characters; reaching a new byte: %d; coming out differently than before the patch: %d" % (len(COMMON), len(on_new), len(changed)))
for cp in on_new + changed:
    print("      U+%04X %s -> byte %02X" % (cp, unicodedata.name(chr(cp), "?"), cp & 255))
fail |= bool(on_new) or bool(changed)
nbsp = rn.new.a2u(rn.new.u2a("\u00a0"))
print("    U+00A0 through uni2acii and acii2uni: %r (the old build: %r)" % (nbsp, rn.old.a2u(rn.old.u2a("\u00a0"))))
fail |= nbsp != rn.old.a2u(rn.old.u2a("\u00a0"))
hit = {}
for cp in range(0x80, 0x3000):
    if (cp & 255) in NEWB and not 0x900 <= cp < 0x980 and unicodedata.category(chr(cp))[0] in "LNPS":
        hit.setdefault(cp >> 8, []).append(cp)
print("    rarer characters that DO reach a new byte, by block (informational): %s" % ", ".join(
    "U+%02X00 %d" % (hb, len(v)) for hb, v in sorted(hit.items())))
print("RESULT:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
