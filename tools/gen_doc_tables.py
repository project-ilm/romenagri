#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Generates the tables and counts of Romenagri/TRANSLITERATION.md from the real headers and from the grammar printed in the
document itself, so that the document cannot drift from the code.

    python3 tools/gen_doc_tables.py --check <Romenagri dir>      exit 1 if a generated block of the document is out of date
    python3 tools/gen_doc_tables.py --write <Romenagri dir>      rewrite the generated blocks in place
    python3 tools/gen_doc_tables.py --print <block> <Romenagri dir>

A generated block sits between   <!-- BEGIN GENERATED name -->   and   <!-- END GENERATED name -->   in the document, with a blank line on each side.
Blocks: stats, table-new, table-all, reserved-keys, unchecked-skips, family-letters, halant-popped, free-bytes, supply-demand, unmapped,
nukta-table, examples, traces, sync-breakers, guards, underscore-runs, underscore-counts.
Nine of them (stats, table-all, reserved-keys, unchecked-skips, traces, sync-breakers, guards, underscore-runs, underscore-counts) read the grammar
block of the document (section 5.3) as well as the headers.  The grammar has three versions, selected by the tags of its rules: without the tagged
rules (the unpatched parser), without the '!' rules (patch 0001, the Sanskrit characters), and with all of them (this package).
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "tests"))
import model  # noqa: E402
import rmn_tables  # noqa: E402
import spec_model  # noqa: E402

SANSKRIT_ADDITIONS = [0x090C, 0x0961, 0x0960, 0x0962, 0x0963, 0x0944, 0x0965, 0x0951, 0x0952, 0x0953, 0x0954, 0x0950]
NOTES = {
    "": "ISCII attribute prefix `EF` + `B` (script = Devanagari); acii2rmn drops it",
    "__": "a literal underscore `_` (the escape that keeps `_` free as the family marker)",
    "^a": "the inherent vowel written as a sign: invisible in ACII",
    "|": "danda U+0964",
    "^": "halant U+094D (at the start of a token: the sign `^`)",
    "_rda": "DDA + nukta: the parser's spelling of `_rd` + `a`; acii2rmn builds it in its nukta rule",
    "_rdha": "DDHA + nukta: the parser's spelling of `_rd` + `ha`; acii2rmn builds it in its nukta rule",
    "^ra": "halant + RA. Dead: acii2rmn finds the halant row `^` first and the parser reads `^r` as text (section 11.2)",
    "r": "derived: what the parser writes for the letter `r` (RA, then the halant), see `ra`",
    "kxa": "derived: what the parser writes for `k` followed by `xa`",
    "_tra": "derived: what the parser writes for `_t` followed by `ra`",
    "j_yna": "derived: what the parser writes for `j` followed by `_yna`",
    "shra": "derived: what the parser writes for `sh` followed by `ra`",
}


def short(cp):
    return unicodedata.name(chr(cp), "U+%04X" % cp).replace("DEVANAGARI ", "")


def load(d):
    n_a, acii = rmn_tables.parse_acii(d)
    n_u, uni = rmn_tables.parse_unicode(d)
    n_h, hin = rmn_tables.parse_hin(d)
    return acii, uni, hin


def need_spec(spec):
    if spec is None:
        sys.exit("the document has no ```rmn2acii-grammar block (section 5.3)")
    return spec


def uni_of(bs, byte2cp):
    if not any(b in byte2cp for b in bs):
        return "-"
    return " ".join("U+%04X" % byte2cp[b] if b in byte2cp else "?" for b in bs)


def used_bytes(acii, uni, hin):
    return {x for _, bs in acii for x in bs} | {b for _, b in uni} | {x for _, bs in hin for x in bs}


def block_stats(d, spec):
    acii, uni, hin = load(d)
    n_states, n_rules, n_new, n_guards, longest = spec_model.stats(need_spec(spec))
    keys = spec_model.lookup_keys(spec, True)
    T = rmn_tables.key_table(acii)
    missing = [k for k in keys if k not in T]
    used = {b for b in used_bytes(acii, uni, hin) if b >= 0x80}
    lines = [
        "- `acii.h` %d rows, `unicode.h` %d rows, `aciihin.h` %d rows" % (len(acii), len(uni), len(hin)),
        "- ACII bytes in use: %d of the 128 bytes `80`-`FF`; free: %d" % (len(used), 128 - len(used)),
        "- parser grammar (section 5.3): %d states, %d rules (%d of them added for the Sanskrit characters, %d guards against the underscore and the end of the string), longest guard %d characters"
        % (n_states, n_rules, n_new, n_guards, longest),
        "- keys the grammar can look up: %d; of these, %d have no row in `acii.h` (section 11.3)" % (len(keys), len(missing)),
    ]
    return "\n".join(lines)


def block_table_new(d, spec=None):
    acii, uni, hin = load(d)
    byte2cp = {b: cp for cp, b in uni}
    cp2byte = {cp: b for cp, b in uni}
    key_of = {}
    for k, bs in acii:
        if len(bs) == 1:
            key_of.setdefault(bs[0], k)
    hin_of = {}
    for k, bs in hin:
        if len(bs) == 1:
            hin_of.setdefault(bs[0], k)
    lines = ["| ACII | Unicode | Character | Romenagri | saral (acii2hin) |", "|---|---|---|---|---|"]
    for cp in SANSKRIT_ADDITIONS:
        b = cp2byte[cp]
        saral = hin_of.get(b, "")
        lines.append("| `%02X` | U+%04X | %s | `%s` | %s |" % (b, cp, short(cp), key_of[b], "`%s`" % saral.replace("|", "\\|") if saral else "(empty: the mark vanishes)"))
    return "\n".join(lines)


def block_table_all(d, spec):
    acii, uni, hin = load(d)
    byte2cp = {b: cp for cp, b in uni}
    hin_of = {}
    for k, bs in hin:
        hin_of.setdefault(bs, k)
    added = {cp for cp in SANSKRIT_ADDITIONS}
    parser_keys = spec_model.lookup_keys(need_spec(spec), True)
    first_row = {}
    for i, (k, bs) in enumerate(acii):
        if bs:
            first_row.setdefault(bs[0], i)
    lines = ["| # | Romenagri | ACII | Unicode | Meaning | saral | used by |", "|--:|---|---|---|---|---|---|"]
    for i, (k, bs) in enumerate(acii):
        names = "; ".join(short(byte2cp[b]).lower() for b in bs if b in byte2cp)
        meaning = NOTES.get(k) or names or "-"
        cps = uni_of(bs, byte2cp) if bs else "-"
        new = " **new**" if any(byte2cp.get(b) in added for b in bs) else ""
        by_parser = k in parser_keys
        by_decoder = i == 0 or (bool(bs) and first_row.get(bs[0]) == i)
        used = "both" if by_parser and by_decoder else "parser" if by_parser else "decoder" if by_decoder else "neither"
        lines.append("| %d | `%s` | `%s` | %s | %s%s | %s | %s |" % (i, k.replace("|", "\\|"), bs.hex().upper() if bs else "-", cps, meaning, new,
                     ("`%s`" % hin_of[bs].replace("|", "\\|")) if bs and bs in hin_of and hin_of[bs] else "-", used))
    return "\n".join(lines)


def stem_order(stem):
    return (stem.startswith("_"), len(stem) > 1 and not stem.startswith("_"), stem)


def block_reserved_keys(d, spec):
    """The 14 consonant stems of state L2b against the three things the parser can build from a stem: stem+a, stem+ha, stem+vra."""
    acii, uni, hin = load(d)
    T = rmn_tables.key_table(acii)
    stems = {}
    keys = spec_model.lookup_keys(need_spec(spec), True, stems)
    missing = sorted(k for k in keys if k not in T)

    def cell(key, typed):
        if key in T:
            return "`%s` %s" % (key, T[key].hex().upper())
        return "**no row**: `%s` crashes" % typed

    lines = ["- keys the grammar can ask for: %d; without a row in `acii.h`: **%d**" % (len(keys), len(missing)),
             "- the 14 stems of state L2b make 42 keys; the other %d keys of the grammar are not built from a stem" % (len(keys) - 42),
             "- all %d missing keys are in the columns `h` and `v` of the table below" % len(missing), "",
             "| stem (typed) | plain: stem + `a` | aspirate: stem + `ha` | stem + `vra` |", "|---|---|---|---|"]
    for st in sorted(stems["L2b"], key=stem_order):
        lines.append("| `%s` | %s | %s | %s |" % (st, cell(st + "a", st), cell(st + "ha", st + "h"), cell(st + "vra", st + "vr")))
    return "\n".join(lines)


def block_unchecked_skips(d, spec):
    lines = ["| state | rule | characters tested | characters jumped over unseen |", "|---|---|--:|--:|"]
    for name, (param, rules) in need_spec(spec).states.items():
        for r in rules:
            skip = sum(int(a[1]) for a in r.actions if a[0] == "skip")
            tested = sum(1 for item in r.guard if item[0] != "end")
            if skip > tested:
                lines.append("| %s | `%s` | %d | %d |" % (name, r.text.split("->")[0].strip().replace("|", "\\|") + " -> ..." , tested, skip - tested))
    return "\n".join(lines)


def ranges(vals):
    out, i = [], 0
    vals = sorted(vals)
    while i < len(vals):
        j = i
        while j + 1 < len(vals) and vals[j + 1] == vals[j] + 1:
            j += 1
        out.append("`%02X`" % vals[i] if i == j else "`%02X`-`%02X`" % (vals[i], vals[j]))
        i = j + 1
    return ", ".join(out)


NBSP_BYTE = 0xA0          # the low byte of U+00A0 NO-BREAK SPACE, which uni2acii writes for it (section 11.6)


def free_classes(d):
    acii, uni, hin = load(d)
    names = rmn_tables.iscii_names(d)
    used = used_bytes(acii, uni, hin)
    free = [b for b in range(0x80, 0x100) if b not in used]
    c1 = [b for b in free if b < 0xA0]
    avoid = [b for b in free if b == NBSP_BYTE]
    iscii = [b for b in free if b in names and not names[b].lower().startswith("unused") and not 0xF1 <= b <= 0xFA and b != 0xF0 and b not in avoid]
    digits = [b for b in free if 0xF1 <= b <= 0xFA]
    unassigned = [b for b in free if b >= 0xA0 and b in names and names[b].lower().startswith("unused")]
    never = [b for b in free if b == 0xF0]
    return free, c1, iscii, unassigned, digits, never, avoid, names


def block_free_bytes(d, spec=None):
    free, c1, iscii, unassigned, digits, never, avoid, names = free_classes(d)
    lines = ["| Class | Bytes | Count | Use |", "|---|---|--:|---|",
             "| C1 extension block | %s | %d | first choice for a new character with no ISCII byte |" % (ranges(c1), len(c1)),
             "| ISCII-assigned, unused by ACII | %s | %d | only for the character ISCII gives it (%s) |"
             % (ranges(iscii), len(iscii), "; ".join("`%02X` %s" % (b, names[b]) for b in iscii)),
             "| ISCII-unassigned | %s | %d | second choice |" % (ranges(unassigned), len(unassigned)),
             "| ISCII digits | %s | %d | reserved for Devanagari digits (fixuninum currently turns them into ASCII digits) |" % (ranges(digits), len(digits))]
    if avoid:
        lines.append("| avoided | %s | %d | U+00A0 NO-BREAK SPACE reaches this byte through the low-byte fallback of `uni2acii` (section 11.6); a character placed here would replace every no-break space. "
                     "The repository's CSV calls the byte \"Sign OM\"; OM is at `8C` for this reason |" % (ranges(avoid), len(avoid)))
    lines += ["| ISCII extension prefix | %s | %d | never: `EXT` introduces a following byte |" % (ranges(never), len(never)),
              "| **free in total** | | **%d** | `EF` (attribute prefix) is used, not free |" % len(free)]
    return "\n".join(lines)


def classify_unmapped(d):
    """[(code point, class, detail)] for every unassigned-in-unicode.h code point of the Devanagari block U+0900-U+097F.
    Classes: digit, nukta (a letter that nukta.h, the nukta layer, writes as its consonant and the nukta byte; only in a tree that has
    nukta.h), composite (the same kind of letter in a tree that has no nukta layer), uncovered."""
    acii, uni, hin = load(d)
    mapped = {cp for cp, _ in uni}
    byte_of = dict(uni)
    n_nk, nukta_byte, _, nrows = rmn_tables.parse_nukta(d)
    layer = {cp: base for cp, base, _ in nrows if base in byte_of}
    out = []
    for cp in range(0x900, 0x980):
        if cp in mapped:
            continue
        ch = chr(cp)
        if unicodedata.category(ch) == "Nd":
            out.append((cp, "digit", "ASCII digit %d" % unicodedata.digit(ch)))
            continue
        if cp in layer:
            out.append((cp, "nukta", "U+%04X U+093C: `%02X %02X`" % (layer[cp], byte_of[layer[cp]], nukta_byte)))
            continue
        nfd = unicodedata.normalize("NFD", ch)
        if nfd != ch and all(ord(c) in mapped for c in nfd):
            out.append((cp, "composite", " ".join("U+%04X" % ord(c) for c in nfd)))
            continue
        out.append((cp, "uncovered", ""))
    return out


def block_supply_demand(d, spec=None):
    cls = classify_unmapped(d)
    free, c1, iscii, unassigned, digits, never, avoid, names = free_classes(d)
    n = {k: sum(1 for _, c, _ in cls if c == k) for k in ("digit", "nukta", "composite", "uncovered")}
    lines = [
        "- code points of the Devanagari block U+0900-U+097F that `unicode.h` does not map: **%d**" % len(cls),
        "  - %d digits (rewritten to ASCII digits by `fixuninum` before `uni2acii`, by design)" % n["digit"],
    ]
    if n["nukta"]:
        lines.append("  - %d precomposed nukta letters (written by `uni2acii` as the byte of the consonant and the nukta byte `E9`: the nukta layer, section 15)" % n["nukta"])
    if n["composite"]:
        lines.append("  - %d composites (a canonical decomposition into mapped code points: covered once the text is NFD-normalised)" % n["composite"])
    lines += [
        "  - %d characters that nothing covers yet" % n["uncovered"],
        "- free ACII bytes: **%d**; of these %d (the free part of the C1 block `80`-`9F`) plus %d (ISCII-unassigned) can hold a new character, %d are reserved "
        "for characters ISCII itself gives them, %d for digits, %d is avoided (no-break space) and %d is never used"
        % (len(free), len(c1), len(unassigned), len(iscii), len(digits), len(avoid), len(never)),
        "- so the %d uncovered characters fit into the %d allocatable single bytes with %d to spare" % (
            n["uncovered"], len(c1) + len(unassigned), len(c1) + len(unassigned) - n["uncovered"]),
    ]
    return "\n".join(lines)


def block_unmapped(d, spec=None):
    lines = ["| Code point | Category | Name | Class | `uni2acii` writes | Remedy |", "|---|---|---|---|---|---|"]
    for cp, cls, detail in classify_unmapped(d):
        remedy = {"digit": detail, "nukta": "= %s: the nukta layer (section 15)" % detail.split(":")[0],
                  "composite": "= %s: normalise to NFD first" % detail, "uncovered": "needs a byte and a string (section 8)"}[cls]
        writes = detail.split(": ")[1] if cls == "nukta" else "`%02X`" % (cp & 255)
        lines.append("| U+%04X | %s | %s | %s | %s | %s |" % (cp, unicodedata.category(chr(cp)), short(cp).lower(), cls, writes, remedy))
    return "\n".join(lines)


def block_nukta_table(d, spec=None):
    """the eleven rows of nukta.h, with what Python's unicodedata says about each (the independent check of the nfc column of the rows)"""
    n, nukta_byte, default, rows = rmn_tables.parse_nukta(d)
    if n is None:
        return "(this tree has no nukta.h)"
    acii, uni, hin = load(d)
    byte_of = dict(uni)
    lines = ["| Letter | Code point | Name | = | ACII of the pair | `uni2acii` before, after (default form) | Unicode NFC |", "|---|---|---|---|---|---|---|"]
    for cp, base, nfc in rows:
        pair = "`%02X %02X`" % (byte_of[base], nukta_byte)
        before = "`%02X`" % byte_of[cp] if cp in byte_of else "`%02X` (the low byte: corruption)" % (cp & 255)
        after = "`%02X`" % byte_of[cp] if cp in byte_of else pair
        composes = unicodedata.normalize("NFC", chr(base) + "\u093c") == chr(cp)
        lines.append("| %s | U+%04X | %s | %s + %s | %s | %s, %s | %s |" % (
            chr(cp), cp, short(cp).replace("LETTER ", "").lower(), chr(base), "\u25cc\u093c", pair, before, after,
            "composes it" if composes else "leaves it decomposed (composition exclusion)"))
    lines.append("")
    lines.append("`NUKTA_BYTE` is `%02X`, the byte of U+093C in `unicode.h`; the default `NUKTA_FORM` is %d (%s)." % (
        nukta_byte, default, ("asis", "nfc", "nfd")[default]))
    return "\n".join(lines)


def block_halant_popped(d, spec=None):
    acii, uni, hin = load(d)
    toks = []
    for k, bs in acii:
        if len(bs) == 1 and k.endswith("a") and not k.startswith("^") and (0xB3 <= bs[0] <= 0xD8 or bs[0] == 0x80):
            toks.append(model.model_encode(bytes([bs[0], 0xE8]), acii))
    return ", ".join("`%s`" % t for t in toks)


def block_family_letters(d, spec=None):
    acii, uni, hin = load(d)
    used = sorted({(k[2] if k.startswith("^_") else k[1]) for k, _ in acii if (k.startswith("_") and len(k) > 1 and k != "__") or k.startswith("^_")})
    free = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in used]
    return "second letter after `_` already used: %s\n\nfree: %s" % (" ".join("`%s`" % c for c in used), " ".join("`%s`" % c for c in free))


EXAMPLES = [
    "राम", "कृष्ण", "क्षत्रिय", "ज्ञान", "श्री", "ऋग्वेद",
    "कॢप्त", "कॣ", "कॄ", "ऌ", "ॡ", "ॠ", "ॐ", "हलोऽन्तराः",
    "क़", "ड़", "ढ़", "ऴ",
    "अ॒ग्निमी॑ळे", "क॑ु", "क॒ि", "क़॑ा", "॥",
]


def block_examples(d, spec=None):
    acii, uni, hin = load(d)
    cp2byte = {cp: b for cp, b in uni}
    T = rmn_tables.key_table(acii)
    lines = ["| Devanagari | Unicode | ACII | Romenagri | exact round trip |", "|---|---|---|---|---|"]
    for w in EXAMPLES:
        data = bytes(cp2byte[ord(c)] for c in w)
        rmn = model.model_encode(data, acii)
        back = model.model_filter(data, acii, T)
        lines.append("| %s | %s | `%s` | `%s` | %s |" % (
            "◌" + w if len(w) == 1 and unicodedata.category(w) in ("Mn", "Mc") else w,
            " ".join("%04X" % ord(c) for c in w), data.hex().upper(), rmn.replace("|", "\\|"), "yes" if back == data else "**no**"))
    return "\n".join(lines)


TRACES = ["k_rix_nna", "k_lip_ta", "ka_vuu"]


def block_traces(d, spec):
    acii, uni, hin = load(d)
    T = rmn_tables.key_table(acii)
    out = []
    for s in TRACES:
        trace = []
        res = spec_model.spec_parse(need_spec(spec), s, T, new=True, trace=trace)
        out.append("`%s` gives `%s`:\n" % (s, res.hex().upper()))
        out.append("| state | input left | rule applied | output so far |")
        out.append("|---|---|---|---|")
        for state, stem, i, rule, o in trace:
            rest = s[i:].replace("|", "\\|")
            out.append("| %s | `%s` | `%s` | `%s` |" % (state + ("(%s)" % stem if stem is not None else ""), rest or "\u2205", rule.replace("|", "\\|"),
                                                    o.hex().upper() or "-"))
        out.append("")
    return "\n".join(out).rstrip("\n")


def block_sync_breakers(d, spec):
    """The rules that can swallow an underscore (section 14.6), with the shortest string that makes each of them break the pairing law.
    They are the rules of the parser without the guards (patch 0001 alone; the unpatched parser has the same ones); with the guards there are none."""
    spec = need_spec(spec)
    acii, uni, hin = load(d)
    T = rmn_tables.key_table(acii)
    wit = spec_model.breaker_witnesses(spec, T, new=spec_model.MID)
    sites = {}
    for name, r, j, kind in spec_model.sync_breakers(spec, spec_model.MID):
        sites.setdefault((name, r.src), []).append((j, kind))
    lines = ["| state | rule | what it does with the character after its guard | shortest string that breaks the pairing law |", "|---|---|---|---|"]
    for (name, src), js in sites.items():
        kinds = sorted({k for _, k in js})
        what = "keeps it as plain text (`.`)" if kinds == ["wildcard"] else "jumps over %d character%s unseen" % (len(js), "s" if len(js) > 1 else "")
        w = wit.get((name, src))
        lines.append("| %s | `%s` | %s | %s |" % (name, src.replace("|", "\\|"), what, ("`%s`" % w) if w else "(none found up to length 4)"))
    lines += ["", "%d rules, %d positions; with the guards: %d" % (len(sites), sum(len(v) for v in sites.values()), len(spec_model.sync_breakers(spec, spec_model.NEW)))]
    return "\n".join(lines)


def block_guards(d, spec):
    """The twelve guards (section 14.7): the rules of the grammar tagged '!', each with the rule it stands in front of and its witness."""
    rows = spec_model.guard_rows(need_spec(spec))
    esc = lambda t: t.replace("|", "\\|")                                                          # noqa: E731
    lines = ["| state | guard (a rule tagged `!`) | the rule it stands in front of | shortest string that breaks the pairing law without this guard |", "|---|---|---|---|"]
    for state, rule, anchor, w in rows:
        lines.append("| %s | `%s` | `%s` | `%s` |" % (state, esc(rule), esc(anchor), w))
    return "\n".join(lines)


def _describe(out, T):
    names = {}
    for k, bs in T.items():
        if len(bs) == 1:
            names.setdefault(bs[0], k)
    parts = []
    for b in out:
        parts.append("`_`" if b == 0x5F else "halant" if b == T["^"][0] else ("`%s`" % names[b]) if b in names else "%02X" % b)
    return " ".join(parts)


def block_underscore_runs(d, spec):
    """What the parser makes of a run of n underscores: followed by `ta`, and at the end of the input after `k`."""
    spec = need_spec(spec)
    acii, uni, hin = load(d)
    T = rmn_tables.key_table(acii)
    lines = ["| n | `_`\u00d7n + `ta` | result | read as | `k` + `_`\u00d7n | result | read as |", "|--:|---|---|---|---|---|---|"]
    for n in range(0, 9):
        a, b = "_" * n + "ta", "k" + "_" * n
        ra, rb = spec_model.spec_parse(spec, a, T, True), spec_model.spec_parse(spec, b, T, True)
        lines.append("| %d | `%s` | `%s` | %s | `%s` | `%s` | %s |" % (n, a, ra.hex(" ").upper(), _describe(ra, T), b, rb.hex(" ").upper(), _describe(rb, T)))
    return "\n".join(lines)


def block_underscore_counts(d, spec):
    """Every string of length <= 3 over a-z and _ (20,440 of them), run through the grammar without the guards (patch 0001 alone) and with
    them, with the table as it is and with the 15 missing rows filled in by a dummy byte."""
    spec = need_spec(spec)
    import itertools
    acii, uni, hin = load(d)
    T = rmn_tables.key_table(acii)
    keys = spec_model.lookup_keys(spec, True)
    T2 = dict(T)
    for k in keys:
        T2.setdefault(k, b"\xff")
    strings = ["".join(t) for L in range(0, 4) for t in itertools.product("abcdefghijklmnopqrstuvwxyz_", repeat=L)]
    lines = ["| grammar | table | defined | read past the end | missing row | of the defined: break the pairing law |", "|---|---|--:|--:|--:|--:|"]
    for gname, version in (("without the guards (patch 0001 alone)", spec_model.MID), ("with the guards of section 14.7 (this package)", spec_model.NEW)):
        for tname, tab in (("as it is", T), ("15 rows filled in", T2)):
            ok = over = miss = bad = 0
            for s in strings:
                try:
                    out = spec_model.spec_parse(spec, s, tab, version)
                except model.Overrun:
                    over += 1
                    continue
                except model.Missing:
                    miss += 1
                    continue
                ok += 1
                bad += out.count(b"_") != sum(len(m.group(0)) // 2 for m in re.finditer(r"_+", s))
            lines.append("| %s | %s | %d | %d | %d | %d |" % (gname, tname, ok, over, miss, bad))
    # what the guards change, among the strings that both grammars read (the table as it is)
    both = changed = law_held = 0
    for s in strings:
        try:
            a = spec_model.spec_parse(spec, s, T, spec_model.MID)
            b = spec_model.spec_parse(spec, s, T, spec_model.NEW)
        except (model.Overrun, model.Missing):
            continue
        both += 1
        if a != b:
            changed += 1
            law_held += a.count(b"_") == sum(len(m.group(0)) // 2 for m in re.finditer(r"_+", s))
    lines += ["", "Of the %d strings that both versions read (the table as it is), the guards change the output of %d; on %d of those the version without the guards kept the law, "
              "the others are the strings on which it did not." % (both, changed, law_held)]
    return "\n".join(lines)


BLOCKS = {"stats": block_stats, "table-new": block_table_new, "table-all": block_table_all, "reserved-keys": block_reserved_keys,
          "unchecked-skips": block_unchecked_skips, "family-letters": block_family_letters, "halant-popped": block_halant_popped, "free-bytes": block_free_bytes,
          "supply-demand": block_supply_demand, "unmapped": block_unmapped, "nukta-table": block_nukta_table, "examples": block_examples, "traces": block_traces,
          "sync-breakers": block_sync_breakers, "guards": block_guards, "underscore-runs": block_underscore_runs, "underscore-counts": block_underscore_counts}


def grammar_of(doc):
    m = spec_model.BLOCK.search(doc)
    return spec_model.parse_grammar(m.group(1)) if m else None


def apply(doc, d, write):
    changed = []
    spec = grammar_of(doc)
    for name, fn in BLOCKS.items():
        pat = re.compile(r"(<!-- BEGIN GENERATED %s -->\n)(.*?)(\n<!-- END GENERATED %s -->)" % (re.escape(name), re.escape(name)), re.S)
        m = pat.search(doc)
        if not m:
            changed.append((name, "block missing from the document"))
            continue
        fresh = "\n" + fn(d, spec) + "\n"          # blank lines around the content, so that every Markdown renderer ends the comment block
        if m.group(2) != fresh:
            changed.append((name, "out of date"))
            if write:
                doc = doc[:m.start(2)] + fresh + doc[m.end(2):]
    return doc, changed


def main(argv):
    if len(argv) == 3 and argv[0] == "--print":
        path = os.path.join(argv[2], "TRANSLITERATION.md")
        spec = grammar_of(open(path, encoding="utf-8").read()) if os.path.exists(path) else None
        print(BLOCKS[argv[1]](argv[2], spec))
        return 0
    if len(argv) != 2 or argv[0] not in ("--check", "--write"):
        sys.exit(__doc__)
    d = argv[1]
    path = os.path.join(d, "TRANSLITERATION.md")
    doc = open(path, encoding="utf-8").read()
    new, changed = apply(doc, d, argv[0] == "--write")
    if argv[0] == "--write":
        open(path, "w", encoding="utf-8").write(new)
        print("rewrote %d block(s): %s" % (len(changed), ", ".join(n for n, _ in changed) or "none"))
        return 0
    for n, why in changed:
        print("%s: %s" % (n, why))
    print("generated blocks: %d, out of date or missing: %d" % (len(BLOCKS), len(changed)))
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
