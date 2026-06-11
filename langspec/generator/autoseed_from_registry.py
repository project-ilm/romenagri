#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
autoseed_from_registry.py
=========================
For EVERY language in data/language_registry.csv, produce a complete
data/lang_<code>.csv covering all 201 constructs.

Method (honest, marked per row):
  - Romenagri form: taken from the SOURCE language (sanskrit or arabic).
    Romenagri is script-independent, so it is correct for every language
    that uses the source's canonical keyword. This is the reversible,
    C-identifier-legal identifier the compiler actually consumes.
  - Native-script form:
      * If the language's script shares Devanagari's parallel Unicode block
        (most Indic scripts), transliterate the Sanskrit native keyword by
        codepoint offset.  note = tatsama<sanskrit
      * If the source is Arabic and the language uses Arabic script
        (Urdu, Persian, Pashto, Sindhi, ... and — for technical vocab —
        Hebrew/Syriac via shared Semitic roots), keep the Arabic native
        keyword.  note = borrowed<arabic
      * If the script is NON-parallel (Thai, Tibetan, Khmer, Myanmar, Lao,
        Balinese, Javanese, etc.) we cannot offset-transliterate reliably,
        so the native field carries the Romenagri form as a placeholder and
        note = romenagri_pending_<script>  (flagged for native-speaker fill).
        The Romenagri identifier is still fully correct and usable.

Languages that already have a hand-authored data/lang_<code>.csv are NOT
overwritten unless --force is given; instead missing constructs are appended.

Copyright (c) 1993-2026 Abhishek Choudhary
License: GPL v3
"""
import csv, os, sys, glob

DATA = "data"

# Parallel-block Indic scripts: Devanagari offset works for tatsama.
PARALLEL = {
    "devanagari": 0x0000, "bengali": 0x0080, "gurmukhi": 0x0100,
    "gujarati": 0x0180, "odia": 0x0200, "tamil": 0x0280,
    "telugu": 0x0300, "kannada": 0x0380, "malayalam": 0x0400,
}
# Non-parallel scripts: cannot offset; flag for native fill.
NONPARALLEL = {"sinhala", "tibetan", "thai", "lao", "khmer", "myanmar",
               "limbu", "lepcha", "balinese", "javanese", "sundanese",
               "buginese", "batak", "tagalog", "olchiki"}


def load_ontology():
    order = []
    onto = {}
    for line in open(os.path.join(DATA, "keyword_ontology.csv"), encoding="utf-8"):
        if line.startswith("#") or line.startswith("construct_id") or not line.strip():
            continue
        p = next(csv.reader([line.strip()]))
        onto[p[0]] = p
        order.append(p[0])
    return onto, order


def load_lang(code):
    path = os.path.join(DATA, f"lang_{code}.csv")
    meta, rows = [], {}
    if not os.path.exists(path):
        return meta, rows
    for line in open(path, encoding="utf-8"):
        if line.startswith("#"):
            meta.append(line.rstrip("\n")); continue
        if line.startswith("construct_id") or not line.strip():
            continue
        p = next(csv.reader([line.strip()]))
        if len(p) >= 3:
            rows[p[0]] = p
    return meta, rows


def dev_offset(text, off):
    if off == 0:
        return text
    out = []
    for ch in text:
        cp = ord(ch)
        if 0x0900 <= cp <= 0x097F:
            try:
                out.append(chr(cp + off))
            except ValueError:
                out.append(ch)
        else:
            out.append(ch)
    return "".join(out)


def parse_registry():
    langs = []
    for line in open(os.path.join(DATA, "language_registry.csv"), encoding="utf-8"):
        if line.startswith("#") or line.startswith("code,") or not line.strip():
            continue
        p = next(csv.reader([line.strip()]))
        if len(p) >= 7:
            langs.append({
                "code": p[0], "name": p[1], "iso": p[2], "script": p[3],
                "xlit": p[4], "source": p[5], "speakers": p[6],
            })
    return langs


def main():
    onto, order = load_ontology()
    _, sanskrit = load_lang("sanskrit")
    _, arabic = load_lang("arabic")
    registry = parse_registry()

    created, extended, skipped = 0, 0, 0
    for L in registry:
        code = L["code"]
        if L["source"] == "self":
            skipped += 1
            continue  # sanskrit / arabic are the sources themselves
        src = sanskrit if L["source"] == "sanskrit" else arabic
        xlit = L["xlit"]
        meta, existing = load_lang(code)

        # Build full row set
        path = os.path.join(DATA, f"lang_{code}.csv")
        new_file = not os.path.exists(path)
        if new_file:
            meta = [
                f"# language_name: {L['name']}",
                f"# code: {code}",
                f"# iso639: {L['iso']}",
                f"# script: {L['script']}",
                f"# speakers: {L['speakers']}",
            ]

        out_rows = []
        added = 0
        for cid in order:
            if cid in existing:
                out_rows.append(existing[cid])
                continue
            if cid not in src:
                continue
            s = src[cid]
            s_native, s_rom = s[1], s[2]
            if L["source"] == "arabic":
                native = s_native
                note = "borrowed<arabic"
            else:  # sanskrit
                if xlit in PARALLEL:
                    native = dev_offset(s_native, PARALLEL[xlit])
                    note = "tatsama<sanskrit"
                elif xlit in NONPARALLEL or xlit not in PARALLEL:
                    native = s_rom  # placeholder = romenagri; flagged
                    note = f"romenagri_pending_{L['script'].lower().replace(' ','_')}"
                else:
                    native = dev_offset(s_native, PARALLEL.get(xlit, 0))
                    note = "tatsama<sanskrit"
            out_rows.append([cid, native, s_rom, note])
            added += 1

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(meta) + "\n")
            f.write("construct_id,native_keyword,romenagri,note\n")
            for r in out_rows:
                # re-quote if commas
                cells = []
                for c in r[:4] if len(r) >= 4 else (r + [""] * (4 - len(r))):
                    if "," in c:
                        c = '"' + c + '"'
                    cells.append(c)
                f.write(",".join(cells[:4]) + "\n")

        if new_file:
            created += 1
        elif added:
            extended += 1
        print(f"  {code:22s} {L['script']:22s} rows={len(out_rows):3d} added={added:3d} "
              f"{'(new)' if new_file else ''}")

    print(f"\n  Created {created} new, extended {extended}, skipped {skipped} (source langs).")


if __name__ == "__main__":
    main()
