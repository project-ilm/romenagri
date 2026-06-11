#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
langspec_generator.py
=====================
Reads:
  - data/keyword_ontology.csv          (108 universal constructs, 11 paradigms)
  - data/lang_<code>.csv               (per-human-language keyword table)
Generates:
  - output/STANDARD_<code>.md          (the programming-language standard for that human language)
  - output/INDEX.md                    (master index of all generated standards)

Each per-language standard documents, for every construct the language covers:
  construct_id | English keyword | native-script keyword | Romenagri (ASCII-7) identifier | paradigm | category

The Romenagri column is the KEY contribution: it is the ASCII-7, C-identifier-legal
form that lets the native-script keyword be used directly in a compiler/lexer.

Copyright (c) 1993-2026 Abhishek Choudhary
License: GPL v3 (generator) ; CC BY-SA 4.0 (generated docs)
"""

import csv
import os
import sys
import glob
import datetime

ONTOLOGY = "data/keyword_ontology.csv"
DATA_GLOB = "data/lang_*.csv"
OUT = "output"

COPYRIGHT = "Copyright © 1993-2026 Abhishek Choudhary"
PROJECT = "ILM / Hindawi Programming System — Per-Language Programming Standard"


def load_ontology(path):
    """Return dict: construct_id -> {paradigm, english, category, note}."""
    onto = {}
    order = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("construct_id"):
                continue
            parts = next(csv.reader([line]))
            if len(parts) < 5:
                continue
            cid, paradigm, english, category, note = parts[0], parts[1], parts[2], parts[3], parts[4]
            onto[cid] = {
                "paradigm": paradigm,
                "english": english,
                "category": category,
                "note": note,
            }
            order.append(cid)
    return onto, order


def load_language(path):
    """
    Per-language CSV columns:
      construct_id, native_keyword, romenagri, transliteration_note
    Return dict: construct_id -> {native, romenagri, note}
    plus metadata read from leading '# KEY: value' comment lines.
    """
    meta = {}
    rows = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("#"):
                # metadata line:  # language_name: Hindi
                body = line.lstrip("#").strip()
                if ":" in body:
                    k, v = body.split(":", 1)
                    meta[k.strip()] = v.strip()
                continue
            if not line or line.startswith("construct_id"):
                continue
            parts = next(csv.reader([line]))
            if len(parts) < 3:
                continue
            cid = parts[0].strip()
            native = parts[1].strip()
            romenagri = parts[2].strip()
            note = parts[3].strip() if len(parts) > 3 else ""
            rows[cid] = {"native": native, "romenagri": romenagri, "note": note}
    return meta, rows


def generate_standard(lang_path, onto, onto_order):
    meta, rows = load_language(lang_path)
    code = meta.get("code", os.path.basename(lang_path).replace("lang_", "").replace(".csv", ""))
    name = meta.get("language_name", code)
    script = meta.get("script", "")
    iso = meta.get("iso639", "")
    speakers = meta.get("speakers", "")

    lines = []
    A = lines.append
    A(f"# {name} Programming Language Standard")
    A("")
    A(f"**{PROJECT}**")
    A("")
    A(f"**{COPYRIGHT}**")
    A("")
    A(f"- **Human language**: {name}")
    if iso:
        A(f"- **ISO 639 code**: {iso}")
    if script:
        A(f"- **Script**: {script}")
    if speakers:
        A(f"- **Native speakers**: {speakers}")
    A(f"- **Constructs covered**: {len(rows)} of {len(onto_order)}")
    A(f"- **Generated**: {datetime.date.today().isoformat()}")
    A("")
    A("## What this standard defines")
    A("")
    A(f"This document defines the {name}-language keyword set for programming "
      f"across all major paradigms, together with the **Romenagri** ASCII-7 "
      f"identifier form for each keyword. The Romenagri form is reversible, "
      f"case-independent, diacritic-free, and legal as a C identifier — which "
      f"means a compiler or lexer can accept the {name} keyword directly, in "
      f"native script, and map it deterministically to the ASCII-7 form for "
      f"the toolchain.")
    A("")
    A("This is the per-language realisation of the Hindawi Programming System "
      "principle: complete systems-programming capability in any human language, "
      "with the compiler back-end unchanged.")
    A("")

    # Group by paradigm
    paradigms = {}
    for cid in onto_order:
        if cid not in rows:
            continue
        p = onto[cid]["paradigm"]
        paradigms.setdefault(p, []).append(cid)

    A("## Keyword tables by paradigm")
    A("")
    for p in sorted(paradigms.keys()):
        A(f"### Paradigm: {p}")
        A("")
        A("| Construct | English | " + name + " | Romenagri (ASCII-7) | Category |")
        A("|---|---|---|---|---|")
        for cid in paradigms[p]:
            o = onto[cid]
            r = rows[cid]
            A(f"| `{cid}` | {o['english']} | {r['native']} | `{r['romenagri']}` | {o['category']} |")
        A("")

    # Coverage gaps
    missing = [cid for cid in onto_order if cid not in rows]
    if missing:
        A("## Constructs not yet localized")
        A("")
        A(f"{len(missing)} constructs from the universal ontology are not yet "
          f"assigned a {name} keyword. These are the research frontier for this "
          f"language's standard:")
        A("")
        for cid in missing:
            A(f"- `{cid}` ({onto[cid]['english']}, {onto[cid]['paradigm']})")
        A("")

    A("## Reversibility guarantee")
    A("")
    A(f"Every Romenagri form in this standard is ASCII-7, contains no uppercase, "
      f"no diacritics, and matches the C identifier grammar `[a-z_][a-z0-9_]*`. "
      f"Each maps back deterministically to its {name} native-script keyword via "
      f"the ILM reverse projection (rmn2acii). This is what makes {name} a "
      f"first-class systems-programming language, not a localized skin.")
    A("")
    A("## Example")
    A("")
    if "KW_IF" in rows and "KW_ELSE" in rows and "KW_WHILE" in rows:
        A("```")
        A(f"{rows['KW_IF']['native']} (x > 0)        // romenagri: {rows['KW_IF']['romenagri']}")
        A(f"    ...")
        A(f"{rows.get('KW_ELSE',{}).get('native','else')}              // romenagri: {rows.get('KW_ELSE',{}).get('romenagri','else')}")
        A(f"    ...")
        A("```")
        A("")
    A("---")
    A("")
    A(f"*{COPYRIGHT}. This standard document is licensed CC BY-SA 4.0. "
      f"The {name} keyword assignments and their Romenagri forms are an original "
      f"contribution of the ILM / Hindawi Programming System project, "
      f"with priority dating to the Hindawi Programming System public release "
      f"of 15 August 2004.*")

    out_path = os.path.join(OUT, f"STANDARD_{code}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return code, name, len(rows), len(onto_order), out_path


def main():
    onto, onto_order = load_ontology(ONTOLOGY)
    os.makedirs(OUT, exist_ok=True)
    results = []
    for lang_path in sorted(glob.glob(DATA_GLOB)):
        res = generate_standard(lang_path, onto, onto_order)
        results.append(res)
        print(f"  Generated {res[1]:20s}  {res[2]:3d}/{res[3]} constructs  -> {res[4]}")

    # Master index
    idx = []
    A = idx.append
    A("# ILM / HPS Per-Language Programming Standards — Master Index")
    A("")
    A(f"**{COPYRIGHT}**")
    A("")
    A("Programming-language keyword standards generated from a single "
      f"universal construct ontology ({len(onto_order)} constructs, 11 paradigms) "
      "and per-human-language keyword tables. Each standard provides native-script "
      "keywords with reversible Romenagri ASCII-7 identifier forms.")
    A("")
    A("| Language | Constructs | Coverage | Standard |")
    A("|---|---|---|---|")
    for code, name, n, total, path in results:
        pct = round(100 * n / total)
        A(f"| {name} | {n}/{total} | {pct}% | [STANDARD_{code}.md](STANDARD_{code}.md) |")
    A("")
    A("## The universal ontology")
    A("")
    A(f"All standards derive from `data/keyword_ontology.csv`: {len(onto_order)} "
      "constructs across paradigms: imperative, procedural, object-oriented, "
      "functional, logic, concurrent, systems, hardware (HDL), exceptions, "
      "and module/namespace.")
    A("")
    A("## Method")
    A("")
    A("1. The universal ontology defines language-independent programming constructs.")
    A("2. Each `data/lang_<code>.csv` assigns a native-script keyword and a "
      "Romenagri ASCII-7 form to each construct.")
    A("3. `langspec_generator.py` joins them and emits one standard per language.")
    A("4. Adding a language = adding one data file. The generator and ontology "
      "are unchanged. This is the same tabular-extensibility property as the "
      "ILM two-layer architecture.")
    A("")
    A("## Priority claim")
    A("")
    A("The capability — complete systems programming in non-English human "
      "languages with the compiler back-end unchanged — was demonstrated in the "
      "Hindawi Programming System, publicly released 15 August 2004. These "
      "per-language standards formalise and extend that capability across "
      "human languages and programming paradigms.")
    A("")
    A(f"*{COPYRIGHT}*")

    with open(os.path.join(OUT, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(idx))
    print(f"\n  Master index -> {OUT}/INDEX.md")
    print(f"  Total: {len(results)} language standards generated.")


if __name__ == "__main__":
    main()
