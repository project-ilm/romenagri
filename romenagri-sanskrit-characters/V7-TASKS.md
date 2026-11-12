<!-- SPDX-License-Identifier: GPL-2.0-or-later -->
# Romenagri v7: every other Unicode script, and AInagri, tasks

Copyright (C) 1993-2026 Abhishek Choudhary. GPL-2.0-or-later (COPYING, LICENSE, NOTICE of zip no. 5 apply).
Written 12 November 2026. Base: zip no. 5 with the v6 delta laid over it (both checksum lists verify). Like V6-TASKS.md, this file
comes before the work; only AInagri (section 6) and the inventory (`v7/inventory/unicode_scripts.csv`) are built in this run.

## 1. What is asked (his message of 12 Nov), in my reading

| # | Request | Reading |
|---|---|---|
| R1 | Seed and mint zip 5 and the v6 delta as project-ilm/romenagri | The repository exists (Perso-Arabic seed, 640 files, last commit 56cb798, never minted). `update_romenagri.sh` lays zip 5 + v6 + v7 over it as `romenagri-sanskrit-characters/`, removes nothing, and mints its first DOI. |
| R2 | The open scripts, from Hebrew all the way to Egyptian Hieroglyphs | Every script of the Unicode database not yet mapped: the right-to-left abjads and alphabets (Hebrew first), the alphabets, the syllabaries, and the logographic and hieroglyphic scripts (Egyptian Hieroglyphs last). |
| R3 | The Brahmi side: Brahmi, Sharada and the other Unicode-supported Brahmic scripts | The scripts whose letters pair with Devanagari by name. Brahmi (66.09 %) and Sharada (86.46 %) were built in v6; their gaps, and every Brahmic script not yet built, are tasks. |
| R4 | Cyrillic and the like | The alphabets, cased (Cyrillic, Greek, Latin, Armenian, Georgian, Glagolitic, Coptic, ...) and uncased (Gothic, Runic, Ogham, Old Italic, ...). |
| R5 | Other abugidas | The abugidas whose inventory is not Devanagari's: v6's tier C (Myanmar, Khmer, Tibetan, Thai, Lao, Javanese, Balinese) and every other one in Unicode. |
| R6 | A new script from various characters that improves aesthetics globally, called AInagri; show its table | Built in `v7/ainagri/` (section 6). Its letters are data (`ainagri.csv`) and his to change. |

## 2. Scope: tiers, from the data

`v7/tools/inventory.py` reads every assigned code point of the Unicode character database in this environment (Unicode 15.0,
Script property from fontTools 4.67.0) and writes `v7/inventory/unicode_scripts.csv`: 161 scripts, each with its counts and a
first sort read from its own character names and direction (vowel signs, virama-like signs, the letter names KA, KHA, GHA,
syllable names, hieroglyph names, right-to-left letters). The sort is a starting point for linguists, not a classification;
known misfires are listed at the end of this section. Scripts added in Unicode 16.0 and 17.0 are not in this data and are added
from it when the environment has it.

- **Done in v6 (18):** Bengali, Assamese, Gurmukhi, Gujarati, Oriya, Tamil, Telugu, Kannada, Malayalam, Sinhala, Brahmi, Kaithi,
  Grantha, Sharada, Modi, Tirhuta, Siddham, Newa; Urdu on the Perso-Arabic side.
- **V7-A, Brahmic, pairs with Devanagari by letter name, not yet built (19):** Ahom, Bhaiksuki, Cham, Dives Akuru, Dogra,
  Gunjala Gondi, Kawi, Kharoshthi, Khojki, Khudawadi, Limbu, Masaram Gondi, Myanmar, Nandinagari, Saurashtra, Soyombo, Takri,
  Tibetan, Zanabazar Square. Method: v6's `gen_fltr.py`, unchanged. Also: the gaps of Brahmi (66.09 %), Siddham (70.65 %) and
  Sinhala (0.90 %, its letters do not pair by name and need a table of their own).
- **V7-B, other abugidas (22):** Balinese, Batak, Buginese, Buhid, Chakma, Hanunoo, Javanese, Khmer, Lao, Lepcha, Makasar, Marchen,
  Meetei Mayek, Miao, New Tai Lue, Rejang, Sundanese, Syloti Nagri, Tagalog, Tagbanwa, Tai Tham, Thai; with Ethiopic and
  Canadian Aboriginal Syllabics, which Unicode names as syllables. Method: a table per script, consonant by consonant and vowel
  by vowel, onto Devanagari, with the inventory differences listed (series without aspirates, tone letters, final forms).
- **V7-C, right-to-left abjads and alphabets, Hebrew first (30):** Hebrew, Syriac, Samaritan, Mandaic, Phoenician, Imperial
  Aramaic, Nabataean, Palmyrene, Hatran, Old South Arabian, Old North Arabian, Inscriptional Parthian, Inscriptional Pahlavi,
  Psalter Pahlavi, Avestan, Sogdian, Old Sogdian, Old Uyghur, Chorasmian, Elymaic, Manichaean, Old Turkic, Old Hungarian, Lydian,
  Meroitic Cursive, Yezidi, Thaana, Nko, Adlam, Hanifi Rohingya. Method: v6's Perso-Arabic method (the `urdu_map.csv` way),
  Unicode to Unicode; letters Devanagari cannot tell apart make it lossy by design, and the percentage says how much.
- **V7-D, alphabets (Cyrillic and the like):** cased: Latin, Greek, Cyrillic, Armenian, Georgian, Glagolitic, Coptic, Deseret,
  Osage, Vithkuqi, Warang Citi, Medefaidrin; uncased: Gothic, Runic, Ogham, Old Italic, Old Permic, Carian, Lycian, Elbasan,
  Caucasian Albanian, Osmanya, Shavian, Tifinagh, Ol Chiki, Lisu, and the rest of the "alphabet or other" group. Method: one
  script serves many languages (Cyrillic writes Russian, Ukrainian, Bulgarian, Serbian, Kazakh, Kyrgyz, Mongolian, Tajik and
  many low-resource languages), so the table is per language, letter to phoneme (IPA) to Devanagari, swappable as v6 section 6
  asks for dialects.
- **V7-E, syllabaries:** Cherokee, Vai, Yi, Linear B, Cypriot, Cypro-Minoan, Hiragana, Katakana, Hangul (featural, by jamo),
  Mende Kikakui, Bamum, and the syllabic sides of Ethiopic and Canadian Syllabics. Method: syllable to Devanagari akshara.
- **V7-F, logographic and hieroglyphic, Egyptian Hieroglyphs last:** Cuneiform, Anatolian Hieroglyphs, Meroitic Hieroglyphs,
  Egyptian Hieroglyphs, Han, Tangut, Khitan Small Script, Nushu, Linear A. No letter mapping exists. Path: an established
  transliteration first (for Egyptian, Gardiner's sign list and the Manuel de Codage), then Devanagari; built for the phonetic
  signs only (the Egyptian uniliterals first), the rest listed with the research it needs.
- **Not a writing system for this purpose:** Braille, SignWriting, Duployan (shorthand): listed, not mapped.

Known misfires of the first sort, to be moved by a linguist and recorded in the CSV: Mongolian sorts as Brahmic because of its
Ali Gali transcription letters; Arabic and Samaritan sort as abugidas because of their vowel signs; Thai, Mahajani, Multani and
Phags-pa land in "alphabet or other" because their names carry no vowel signs; Tangut, Khitan, Nushu and Linear A land there
because their names carry no hieroglyph or syllable word.

## 3. Method and definitions

As V6-TASKS.md section 3, unchanged: data first, Devanagari the pivot, character reversibility, coverage, collisions, text
reversibility, T1 (script to Devanagari to script) and T2 (the same through zip 5's core), each in percent per script. Added for
v7: a phoneme (IPA) column in every table outside V7-A, so that a mapping that cannot be letter for letter is at least explicit;
per-language tables where one script writes many languages; no project is read from one country's view, so every script is
taken with the languages that use it worldwide, low-resource ones included.

## 4. Deliverables (delta zip `romenagri-v7-delta.zip`, over zip 5 and v6)

`v7/maps/<script>.csv`, `v7/Romenagri/fltr_<xx>_hi` and `fltr_hi_<xx>`, `v7/tests/run_v7.py` (T1, T2), `v7/results.json`,
`v7/onepagers/<script>.md`, `romenagri-site/docs/script-<xx>.html` and the navigator extended, `v7/README.md`, every new file
with the 1993-2026 notice. Already here: `v7/inventory/`, `v7/tools/inventory.py`, `v7/ainagri/`.

## 5. Order of work

1. V7-A with v6's generator (cheapest, same method). 2. The Brahmi, Siddham and Sinhala gaps. 3. V7-C, Hebrew first.
4. V7-D, Cyrillic, Greek, Armenian and Georgian first. 5. V7-B. 6. V7-E. 7. V7-F, Egyptian uniliterals first.
8. One-pagers, site pages, navigator. 9. AInagri's tasks (section 6).

## 6. AInagri (built in this run)

A script for Sanskrit and the Devanagari languages written with characters readers across the world already know, one visual
unit for each Devanagari letter. Base letters are Latin; length is a macron; retroflex is a dot below; aspiration is a raised h
(the IPA's ʰ) instead of a second letter; the diphthongs are ê and ô so that no vowel sequence is ambiguous; vocalic r and l carry
a ring below (r̥, l̥), which leaves ṛ for ड़. Every character is in the default fonts of current systems. `ainagri.py` converts
both ways; `TABLE.md` sets each letter beside its Romenagri form from zip 5's own core.

Results of this run (`python3 v7/ainagri/test_ainagri.py`): 1,610 of 1,610 synthetic strings and 202 of 202 corpus lines
(`corp_hi`, `corp_hi_nums`) come back exactly; 98 of the 128 assigned code points of the Devanagari block have an AInagri form,
and the other 30 (Vedic tone marks, ॐ, the letters U+0972 to U+097F for other languages) pass through unchanged and still return.

Tasks: (a) the Vedic signs and ॐ; (b) the letters U+0972 to U+097F (Marathi ॲ, the Sindhi implosives ॻ ॼ ॾ ॿ, ...);
(c) AInagri for every script of v6 and v7 through the Devanagari pivot, with T1 and T2; (d) a rendering check in the default fonts
of Windows, macOS, Linux, Android and iOS, recorded as images; (e) a review by readers of several scripts and countries, recorded;
(f) an input method (keyboard layout); (g) a phonetic variant (Hindi word-final schwa), as a separate table, since AInagri
follows the letters as v6 does.

## 7. Open issues (for linguists, as V6-TASKS.md section 6)

Phonetic fidelity against orthographic mapping; dialect-level tables; for AInagri, the danda as | and the Devanagari digits as
0 to 9 (both reversible, both choices of appearance), and whether ê and ô suit every reader.

## 8. Not done, on purpose

No change to the core, to patches 0001 to 0003, or to any file of zip 5 or v6; no tier of section 2 built beyond AInagri and the
inventory.
