<!-- SPDX-License-Identifier: GPL-2.0-or-later -->
# Romenagri v7: every other Unicode script, and AInagri, tasks

Copyright (C) 1993-2026 Abhishek Choudhary. GPL-2.0-or-later (COPYING, LICENSE, NOTICE of zip no. 5 apply).
Written 12 November 2026, against the repository as it stands after 6.0.1 (AGENTS.md, CONTEXT.md). Every count below is read from
the repository and from the Unicode data (`v7/inventory/unicode_scripts.csv`, Unicode 15.0, 161 scripts), not from memory.

## 1. What is asked (his message of 12 Nov)

| # | Request | Reading |
|---|---|---|
| R1 | The open scripts, Hebrew all the way to Egyptian Hieroglyphs | Every script with no table in `tables/` yet: the right-to-left abjads and alphabets (Hebrew first), the alphabets, the syllabaries, the logographic and hieroglyphic scripts (Egyptian Hieroglyphs last). |
| R2 | The Brahmi side: Brahmi, Sharada and every other Unicode-supported Brahmic script | `tables/` names 73 scripts; 16 hold rows (from v6); the other 57 have a header and at most one row. Filling them is the Brahmic and South-East Asian work. |
| R3 | Cyrillic and the like | The alphabets with no table: 34 scripts. |
| R4 | Other abugidas | The abugidas among the empty tables, and those with no table at all (Makasar, Miao). |
| R5 | AInagri | Built in `v7/ainagri/`, published at `docs/ainagri.html`; its own tasks in section 6. |

## 2. What the repository already holds (not to be rebuilt)

- The method, Unicode name-projection onto the Devanagari hub (`results/FAMILIES/BRAHMI_ALL_REPORT.tsv`, 44 scripts measured); the
  Hebrew projection test (`results/FAMILIES/NW_SEMITIC_REPORT.tsv`); the family runbook (`docs/RUNBOOK.md`).
- Tables with rows (16, from v6's maps in 6.0.1): Bengali, Brahmi, Grantha, Gujarati, Gurmukhi, Kaithi, Kannada, Malayalam, Modi, Newa, Oriya, Sharada, Siddham, Tamil, Telugu, Tirhuta.
- Tables named but empty or nearly (57): Ahom, Balinese, Batak, Bhaiksuki, Buginese, Buhid, Chakma, Cham, Dives Akuru, Dogra, Gunjala Gondi, Gurung Khema, Hanunoo, Javanese, Kawi, Kayah Li, Kharoshthi, Khmer, Khojki, Khudawadi, Kirat Rai, Lao, Lepcha, Limbu, Mahajani, Marchen, Masaram Gondi, Meetei Mayek, Mongolian, Multani, Myanmar, Nag Mundari, Nandinagari, New Tai Lue, Ol Chiki, Ol Onal, Pau Cin Hau, Phags-pa, Rejang, Saurashtra, Sinhala, Soyombo, Sundanese, Sunuwar, Syloti Nagri, Tagalog, Tagbanwa, Tai Le, Tai Tham, Tai Viet, Takri, Tangsa, Thai, Tibetan, Toto, Wancho, Zanabazar Square. Gurung Khema, Kirat Rai, Ol Onal, Sunuwar are scripts of Unicode 16.0 or later, beyond this
  environment's data.
- v6's tools (`v6/tools/gen_fltr.py`, `v6/tests/run_v6.py`, `v6/tools/gen_pages.py`) make the table's pairs, the two sed layers,
  T1, T2 and the script page from the Unicode data for any script whose letters pair by name.

## 3. Tasks

- **A. Fill the empty tables** with v6's generator, writing the rows into `tables/<script>_to_deva.tsv` and generating the layers,
  T1, T2 and the page from it. Where the letters do not pair by name (Sinhala; Thai, Lao, Khmer, Myanmar and the other South-East
  Asian scripts), the table is written from each script's own consonant and vowel order, with the differences listed.
- **B. Abugidas with no table:** Makasar, Miao.
- **C. Right-to-left abjads and alphabets, Hebrew first (30):** Adlam, Avestan, Chorasmian, Elymaic, Hanifi Rohingya, Hatran, Hebrew, Imperial Aramaic, Inscriptional Pahlavi, Inscriptional Parthian, Lydian, Mandaic, Manichaean, Meroitic Cursive, Nabataean, Nko, Old Hungarian, Old North Arabian, Old Sogdian, Old South Arabian, Old Turkic, Old Uyghur, Palmyrene, Phoenician, Psalter Pahlavi, Sogdian, Syriac, Thaana, Yezidi, Samaritan. The Hebrew projection test becomes a
  Hebrew table to the Devanagari hub, then the same for the rest, the Perso-Arabic way (Unicode to Unicode; letters the hub
  cannot tell apart make it lossy by design, and the percentage says how much).
- **D. Alphabets, Cyrillic and the like (34):** Armenian, Coptic, Cyrillic, Deseret, Georgian, Glagolitic, Greek, Medefaidrin, Osage, Vithkuqi, Warang Citi, Bamum, Bassa Vah, Carian, Caucasian Albanian, Elbasan, Gothic, Lisu, Lycian, Mro, Nyiakeng Puachue Hmong, Ogham, Old Italic, Old Permic, Old Persian, Osmanya, Pahawh Hmong, Runic, Shavian, SignWriting, Sora Sompeng, Tangut, Tifinagh, Ugaritic. One script writes many languages (Cyrillic writes
  Russian, Ukrainian, Bulgarian, Serbian, Kazakh, Kyrgyz, Mongolian, Tajik and many low-resource languages), so the table is per
  language, letter to phoneme to Devanagari, swappable for dialects.
- **E. Syllabaries (13):** Canadian Aboriginal, Cypriot, Ethiopic, Hangul, Linear B, Mende Kikakui, Vai, Yi, Cherokee, Hiragana, Katakana, Bopomofo, Cypro Minoan. Syllable to Devanagari akshara.
- **F. Logographic and hieroglyphic, Egyptian Hieroglyphs last (8):** Anatolian Hieroglyphs, Cuneiform, Egyptian Hieroglyphs, Han, Meroitic Hieroglyphs, Linear A, Khitan Small Script, Nushu. Through an established
  transliteration first (for Egyptian, Gardiner's sign list and the Manuel de Codage), phonetic signs only, the Egyptian
  uniliterals first; the rest listed with the research it needs.
- **G. Not mapped:** Braille, Duployan (shorthand), SignWriting.
- **H. Unicode 16.0 and 17.0:** the newer scripts added to the inventory, then to A to F.
- **I. The site:** each new table gets its script page and its place in the navigator, as v6's did; AGENTS.md point 6 holds.

The inventory's first sort reads character names, not a linguist's classification: Mongolian sorts as Brahmic for its Ali Gali
letters; Arabic and Samaritan as abugidas for their vowel signs; Thai, Mahajani, Multani and Phags-pa as "alphabet or other";
Tangut, Khitan, Nushu and Linear A likewise.

## 4. Method and reversibility

As V6-TASKS.md section 3: data first, Devanagari the hub, coverage, collisions, T1 and T2 in per cent per script, every table read
with the languages that use it worldwide, low-resource ones included.

## 5. Order

A, then C with Hebrew first, D with Cyrillic, Greek, Armenian and Georgian first, B, E, F with the Egyptian uniliterals first,
then H; I goes with each.

## 6. AInagri

Built: `v7/ainagri/` (`ainagri.csv`, `ainagri.py`, `test_ainagri.py`), `docs/ainagri.html`. 1,610 of 1,610 synthetic strings and
202 of 202 corpus lines come back exactly; 98 of the Devanagari block's 128 code points have an AInagri form, the other 30 pass
through and return. Tasks: the Vedic signs and ॐ; the letters U+0972 to U+097F; AInagri for every filled table through the hub;
a rendering check in the default fonts of Windows, macOS, Linux, Android and iOS; a readers' review across scripts and countries;
an input method; a phonetic variant as a separate table.

## 7. Not done, on purpose

No change to the kernel, the patches, zip 5 or v6; no table filled beyond v6's in this release.
