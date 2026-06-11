# ILM / HPS Per-Language Programming Standards

**Copyright © 1993-2026 Abhishek Choudhary. All rights reserved.**

Complete programming-language keyword standards across human languages and
the full hardware-to-AGI paradigm stack, with reversible Romenagri ASCII-7
identifier forms for every keyword.

## Scope of this release

- **68 human languages** across 3 script families (Brahmi, Perso-Arabic, NW Semitic)
- **201 programming constructs** across **17 paradigms** (hardware definition -> AGI)
- **13,668 keyword standards**, every one verified ASCII-7 / C-identifier-legal (zero violations)
- Full stack: HDL -> firmware/IoT -> systems/memory -> GPU -> AI/ML -> robotics -> distributed -> verification

### The 68 languages

**Brahmi / Indo-Aryan (23):** Hindi, Bengali, Marathi, Gujarati, Punjabi, Odia,
Assamese, Nepali, Maithili, Bhojpuri, Magahi, Awadhi, Chhattisgarhi, Rajasthani,
Marwari, Konkani, Dogri, Kashmiri (Devanagari), Sindhi (Devanagari), Santali,
Bodo, Manipuri, Sinhala

**Brahmi / Dravidian (5):** Tamil, Telugu, Kannada, Malayalam, Tulu

**Brahmi / Classical (3):** Sanskrit, Pali, Prakrit

**Brahmi / Tibeto-Burman & Himalayan (5):** Tibetan, Dzongkha, Newari, Limbu, Lepcha

**Brahmi / Southeast Asian (5):** Thai, Lao, Khmer, Burmese, Shan

**Brahmi / Insular SE Asian (5):** Balinese, Javanese, Sundanese, Buginese, Batak

**Brahmi / Philippine (1):** Tagalog

**Perso-Arabic (14):** Arabic, Urdu, Persian, Pashto, Sindhi, Saraiki, Kashmiri,
Uyghur, Kurdish (Sorani), Balochi, Punjabi (Shahmukhi), Malay (Jawi),
Hausa (Ajami), Dari

**Northwest Semitic (7):** Hebrew, Syriac, Imperial Aramaic, Phoenician,
Samaritan, Mandaic, Nabataean

Adding a language is one row in `data/language_registry.csv` + a re-run of
`autoseed_from_registry.py`. The generator and ontology never change.


## The 17 paradigms (hardware → AGI)

| Paradigm | Constructs | Covers |
|---|---|---|
| hdl | 11 | entity, architecture, signal, port, wire, reg, always, assign |
| systems | 13 | struct, union, enum, pointer, alloc, free, extern, volatile, inline |
| memory | 8 | own, borrow, move, mut, lifetime, arena, gc, pin |
| iot | 14 | pin, read, write, analog, digital, pwm, interrupt, timer, sensor, actuator, bus, protocol, sleep, wake |
| gpu | 11 | kernel, device, host, global, shared, threadidx, blockidx, grid, barrier, atomic, warp |
| ai | 20 | tensor, matrix, vector, gradient, backprop, forward, layer, model, train, infer, loss, optimize, activation, weight, bias, epoch, batch, dataset, embed, attention |
| robotics | 13 | motor, servo, joint, pose, trajectory, feedback, pid, deadline, periodic, priority, actuate, perceive, plan |
| dataflow | 10 | stream, pipe, map, filter, reduce, fold, observe, emit, subscribe, debounce |
| distributed | 9 | node, replica, consensus, shard, gossip, leader, rpc, actor, message |
| concurrent | 6 | thread, spawn, lock, sync, channel, select |
| verification | 8 | requires, ensures, invariant, assert, assume, prove, refines, modelcheck |
| imperative | 32 | full control flow, types, literals, exceptions |
| oop | 15 | class, object, interface, inheritance, access modifiers |
| functional | 10 | lambda, match, fun, rec, data, type, module |
| procedural | 7 | function, procedure, call, param, yield, await, async |
| logic | 6 | rule, fact, query, not, and, or |
| common | 8 | import, export, package, namespace, use, include, from, as |

This spans the complete AGI stack: a single human language can express VHDL/Verilog
hardware definition, embedded firmware, GPU kernels, neural-network training,
robotic control loops, distributed consensus, and formally-verified contracts.

## Languages covered

**Modern Indic (Brahmi family)** — hand-authored core + Sanskrit-tatsama technical vocab:
Hindi, Bengali, Telugu, Marathi, Tamil, Kannada, Gujarati, Malayalam, Odia, Punjabi, Nepali, Assamese, Sinhala

**Classical/liturgical (Brahmi family)**:
Sanskrit (fully hand-authored, the canonical reference), Pali, Prakrit

**Perso-Arabic family** — hand-authored core + Arabic technical vocab:
Arabic, Urdu, Persian

**Northwest Semitic family** — hand-authored core + Arabic-cognate technical vocab:
Hebrew, Syriac, Imperial Aramaic, Phoenician

## Provenance honesty (the `note` column)

Every one of the 13,668 rows records its provenance. Real counts in this release:

| Provenance | Rows | Meaning |
|---|---|---|
| `tatsama<sanskrit` | 4,639 | Indic technical term borrowed from Sanskrit (the actual historical pathway for Indic scientific vocabulary), rendered in the target script via parallel-block transliteration |
| `borrowed<arabic` | 3,761 | Perso-Arabic / NW-Semitic technical term from shared Semitic roots, in native Arabic-family script |
| hand-authored | 1,851 | Native keyword written directly (cores: Sanskrit, Hindi, Arabic, and hand-seeded control-flow for classical/Semitic languages) |
| `romenagri_pending_<script>` | 3,417 | Non-parallel scripts (Thai, Tibetan, Khmer, Burmese, Lao, Balinese, Javanese, Sundanese, Buginese, Batak, Tagalog, Sinhala, Limbu, Lepcha, Santali). The **Romenagri identifier is correct and usable now**; the native-script glyph is flagged for native-speaker fill because these scripts do not share Devanagari's codepoint layout and cannot be safely offset-transliterated. |

This is documented borrowing and honest flagging, not invention. Every derived
or pending row is machine-marked so a native-speaker reviewer can override it.

### Why `romenagri_pending` is still a complete standard
Romenagri is script-independent and reversible. For a pending language, the
ASCII-7 keyword the compiler/lexer consumes is already final and correct; only
the human-facing native-script rendering awaits a native speaker. The language
is fully programmable today via its Romenagri keywords.

### Known caveat: Tamil
Tamil is a defective abugida (lacks distinct letters for kh, gh, j, jh, etc.;
historically uses Grantha for Sanskrit loans). Some Tamil tatsama rows contain
fallback codepoints needing Grantha-aware review. Romenagri stays correct.


## The key property

All 4,623 Romenagri forms pass `^[a-z_][a-z0-9_]*$` — pure ASCII-7, no
uppercase, no diacritics, legal as C identifiers. Because Romenagri is
script-independent, a construct's Romenagri form is **identical across every
language that shares the canonical keyword** — which is exactly the point:
the compiler back-end is unchanged across all human languages.

## Architecture

```
keyword_ontology.csv  (201 constructs, 17 paradigms)
        +
data/lang_<code>.csv  (per-language keyword + Romenagri)
        ↓  langspec_generator.py
output/STANDARD_<code>.md  (one standard per language)

derive_keywords.py  — completes a language's technical vocabulary from its
                      linguistically-correct source (Sanskrit / Arabic)
```

## How to extend

- New language: add `data/lang_<code>.csv` with metadata + any hand-authored
  core keywords, then run `derive_keywords.py` to complete technical vocab,
  then `langspec_generator.py`.
- New construct/paradigm: append to `keyword_ontology.csv`, add the keyword to
  each language file (or re-derive), regenerate.

## Precedence and priority

The capability — complete systems-to-AGI programming in non-English human
languages, across all paradigms, with the compiler back-end unchanged, using
reversible romanised identifiers — was first publicly realised in the
**Hindawi Programming System, released 15 August 2004** (world's first
complete non-English systems programming stack), built on **Romenagri**.

- 15 Aug 2004 — Hindawi Programming System v1 public release
- 2005 — CSI National Young IT Professional Award of India
- 2006 — GNU Savannah LGPL v2 registration of Romenagri
- 2006 — Sarai/CSDS FLOSS Fellowship
- ongoing — TDIL (Government of India) recognition

Every keyword assignment and Romenagri form is an original contribution of
the ILM / Hindawi Programming System project by Abhishek Choudhary, with the
priority dates above.

## License
- Generator code: GPL v3
- Data files and generated standards: CC BY-SA 4.0
- All: **Copyright © 1993-2026 Abhishek Choudhary**
