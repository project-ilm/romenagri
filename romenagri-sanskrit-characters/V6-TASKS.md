<!-- SPDX-License-Identifier: GPL-2.0-or-later -->
# Romenagri v6: mapping layers for the other Indic and Perso-Arabic scripts, tasks

Copyright (C) 1993-2026 Abhishek Choudhary. GPL-2.0-or-later (COPYING, LICENSE, NOTICE of zip no. 5 apply).
Written 12 November 2026, before any work on v6. Base: zip no. 5 (`SHA256 41c25a49...0ea9`). v6 is a **delta zip**: only new or changed files, to be unpacked over zip no. 5.

## 1. What is asked (his message of 12 Nov, 11:55 IST), in my reading

| # | Request | Reading |
|---|---|---|
| R1 | All Indic scripts, mapped onto Devanagari | Each script gets a letter-for-letter mapping layer to Devanagari (the pivot) and back. |
| R2 | The `fltr_*` method, as before `uni2acii` | Mapping layers are `sed` scripts named `fltr_<xx>_hi` / `fltr_hi_<xx>` working on UTF-8 Unicode, in front of the core, like the existing `fltr_hi_te`, `fltr_te_hi`. |
| R3 | Other easy Brahmi-derived scripts | Only scripts whose letters pair one-to-one with Devanagari by Unicode name or block layout (tier B below). Hard ones are listed, not built. |
| R4 | Do not retest the core from zip 5 | Zip 5 suites are not re-run. The core is only used, as a black box, in the end-to-end test. |
| R5 | Test and prove reversibility from the Unicode mapping, and through the core end to end only | Two tests per script: (a) Unicode -> Devanagari -> Unicode, (b) Unicode -> Devanagari -> core -> Devanagari -> Unicode. |
| R6 | Report percentage reversibility | Defined in section 3; reported per script and per test. |
| R7 | `fltr_hi_ur` etc. for Perso-Arabic, Unicode to Unicode only, run through zip 5 | Urdu (existing pair, checked), Shahmukhi (Punjabi), Sindhi, built on the same `urdu_map.csv` method. Tested Unicode -> Unicode; "through zip 5" means the Devanagari side is passed through the zip 5 converters in (b). |
| R8 | Fix only the mapping layers; point out open issues for linguists | No change to `Romenagri/*.c`, `*.lex`, tables, parser or the three patches. Everything else is an issue list. |
| R9 | A page per script | One HTML page per script in `romenagri-site/`, generated from the mapping data. |
| R10 | A language-based navigator leading linguists to the script pages; explain the research needed | A page: language -> script -> script page, with the research each needs. |
| R11 | Open issues: phonetic fidelity, dialect-level phonetic mapping | A page and a section on every script page. |
| R12 | Call it v6; one-pager per script per run, as a delta zip; do not boil the ocean | Zip name `romenagri-v6-delta.zip`; one one-pager per script (Markdown, same text in the page) for the recorded run. |
| R13 | First document the tasks | This file. |

## 2. Scope: tiers (what is built, what is only listed)

- **Tier A, built (the ten scripts of `iscii_map.csv`, plus the Assamese variant)**: Bengali, Assamese, Gurmukhi, Gujarati, Oriya (Odia), Tamil, Telugu, Kannada, Malayalam. Telugu pair already exists (`fltr_hi_te`, `fltr_te_hi`): re-derived by the same generator and compared with the hand-kept files.
- **Tier B, built if the Unicode names pair cleanly**: Sinhala, and the historic Brahmi-derived scripts of the Unicode "same letter name" kind (Brahmi, Kaithi, Grantha, Sharada, Modi, Tirhuta, Siddham, Newa). Each is built by matching `<SCRIPT> LETTER X` with `DEVANAGARI LETTER X` in Python's `unicodedata`; unmatched letters go to the open-issue list of that script. Scripts with no clean pairing are listed, not built.
- **Tier C, listed only (not built)**: Myanmar, Khmer, Tibetan, Thai, Lao, Javanese, Balinese and the like: different consonant inventories and ordering, so not "easy".
- **Perso-Arabic (R7)**: Urdu, Shahmukhi, Sindhi.

## 3. Method and definitions

1. **Data first.** One generator `tools/gen_fltr.py` reads the Unicode character database (Python `unicodedata`) and `iscii_map.csv` and writes, per script, a mapping table (CSV), and from it the two `sed` scripts in the style of the existing `fltr_*` files (one `s/x/y/g` per letter; longest sequences first).
2. **Pivot.** Devanagari. A letter with no Devanagari counterpart (Tamil ழ, Malayalam ഴ, Sinhala letters, Assamese ৰ ৱ, ...) is not forced; it is listed in the script's open issues with the pivot choice that the linguists must make. Code points the mapping does not know pass through unchanged and are reported as "unmapped".
3. **Reversibility, defined.** For script S with repertoire R (all assigned letters, vowel signs, signs, digits and punctuation of its Unicode block):
   - **Character reversibility** = share of the code points in R for which back(forth(c)) = c, in percent. Also reported: **coverage** (share of R that has a Devanagari counterpart) and the list of **collisions** (several letters of S mapping to one Devanagari letter, which makes the way back lossy).
   - **Text reversibility** = share of lines (and of words) of the available corpus (`corp_bn`, `corp_hi`, `corp_pb`, `corp_te`, `corp_ur`, `corp_ar`, plus the generated all-letter strings) that come back byte-identical, in percent.
4. **Two tests per script, nothing else**:
   - **T1 (Unicode only):** S -> Devanagari -> S.
   - **T2 (end to end through the core):** S -> Devanagari -> zip 5 core (`uni2acii`, `acii2rmn`, `rmn2acii`, `acii2uni`, default form `asis`) -> Devanagari -> S. Reported as above, with the loss attributed to the mapping layer or to the core (a letter that already fails Devanagari -> core -> Devanagari in zip 5 is counted as "core limit", not as a mapping defect).
   The core is run as built from zip 5; its suites are not re-run.
5. **Perso-Arabic:** Unicode -> Devanagari -> Unicode only (T1) and T2 on the Devanagari side. Arabic-script letters that Devanagari cannot tell apart (ث س ص, ذ ز ض ظ, ...) make it lossy by design; the percentage shows how much, and the collisions are listed.

## 4. Deliverables (delta zip `romenagri-v6-delta.zip`, unpack over zip no. 5)

1. `V6-TASKS.md` (this file).
2. `Romenagri/fltr_<xx>_hi`, `Romenagri/fltr_hi_<xx>` for each built script (new files; no existing file is changed), and `tools/gen_fltr.py`.
3. `v6/maps/<script>.csv` (the mapping tables), `v6/tests/test_v6.py` (T1, T2) and its output.
4. `v6/onepagers/<script>.md`: one page per script for this run: coverage, reversibility T1 and T2 in percent, collisions, unmapped letters, open issues.
5. `romenagri-site/` additions: one page per script (`docs/script-<xx>.html`), `docs/navigator.html` (language -> script -> page; the research each needs), `docs/open-issues.html` (phonetic fidelity, dialect-level mapping), and the index updated. Built by the existing `build_site.py` method.
6. `v6/README.md` (how to apply, how to run the tests, results table), and a `NOTICE` addition. All new files carry the 1993-2026 Abhishek Choudhary notice.

## 5. Order of work (no step is repeated; each result is recorded once)

1. Generator and tier A (nine scripts) with T1. 2. T2 for tier A. 3. Tier B by name pairing, T1/T2, with unmapped lists. 4. Perso-Arabic. 5. One-pagers. 6. Site pages and navigator. 7. Delta zip, sums, one clean-unpack check (the v6 tests only), delivery.

## 6. Open issues that will be listed, not fixed (for linguists)

- **Phonetic fidelity:** letter-for-letter mapping is orthographic, not phonetic. Examples to be filled per script: Bengali/Assamese inherent vowel and ব/ভ, ও; Tamil's unvoiced-only consonants against Devanagari's four-way series; Gurmukhi tippi/addak; Malayalam chillu letters; Sinhala prenasalised consonants; Urdu/Arabic vowel omission, ن/ں, ہ/ھ, ی/ے.
- **Dialect level:** the same letter is read differently by region and community (the four-region pronunciation table already asked for on 3 Nov). A mapping must be a table that can be swapped per dialect; v6 ships one default table per script and marks where dialect tables are needed.
- **Research needed per script:** a native-speaker-checked phoneme table, loanword conventions (Sanskrit tatsama vs native), treatment of conjuncts that exist in one script only, numeral and punctuation conventions, and a corpus with ground truth for the text-reversibility test.

## 7. Not done, on purpose

No change to the core or to patches 0001-0003; no re-run of zip 5 suites; no phonetic transliteration; no Tier C; nothing published or committed.
