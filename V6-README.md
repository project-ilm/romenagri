<!-- SPDX-License-Identifier: GPL-2.0-or-later -->
# Romenagri v6 delta (mapping layers for other scripts)

Copyright (C) 1993-2026 Abhishek Choudhary. GPL-2.0-or-later (COPYING, LICENSE, NOTICE of zip no. 5 apply to every file here).
Unpack **over zip no. 5**. Every file is new; **no file of zip 5 is changed or overwritten** (the generated sed filters are in `v6/Romenagri/`, so the existing `fltr_hi_te` and friends stay as they are). The core, the tables and patches 0001-0003 are untouched and their suites were not re-run. Tasks: `V6-TASKS.md`.

## Contents
- `v6/Romenagri/fltr_<xx>_hi`, `fltr_hi_<xx>`: sed layers, 18 scripts (the `fltr_*` method). `v6/maps/<xx>.csv`: the tables (source = csv / name / pivot).
- `v6/tools/gen_fltr.py` (generator), `v6/tools/gen_pages.py` (pages), `v6/tests/run_v6.py` (T1, T2), `v6/results.json`, `v6/run.log`.
- `v6/onepagers/<xx>.md`: one page per script for this run. `romenagri-site/docs/script-<xx>.html`, `navigator.html`, `open-issues.html`: copy into zip 5's `romenagri-site/docs/` (links to them from `index.html` are not added: zip 5's site check compares that file).

## Results (this run; T1 = script -> Devanagari -> script; T2 = the same through zip 5: uni2acii, acii2rmn, rmn2acii, acii2uni; percent of the script's repertoire)
| code | script | tier | coverage | T1 | T2 |
|---|---|---|---|---|---|
| bn | BENGALI | A | 84.38 % | 83.33 % | 69.79 % |
| as | BENGALI | A | 84.38 % | 83.33 % | 69.79 % |
| pa | GURMUKHI | A | 91.25 % | 91.25 % | 72.5 % |
| gu | GUJARATI | A | 92.31 % | 92.31 % | 80.22 % |
| or | ORIYA | A | 87.91 % | 87.91 % | 74.73 % |
| ta | TAMIL | A | 48.78 % | 48.78 % | 39.84 % |
| te | TELUGU | A | 83.0 % | 83.0 % | 72.0 % |
| kn | KANNADA | A | 91.21 % | 91.21 % | 79.12 % |
| ml | MALAYALAM | A | 70.34 % | 70.34 % | 61.02 % |
| si | SINHALA | B | 0.9 % | 0.9 % | 0.9 % |
| brah | BRAHMI | B | 66.09 % | 66.09 % | 56.52 % |
| kthi | KAITHI | B | 92.65 % | 92.65 % | 86.76 % |
| gran | GRANTHA | B | 87.67 % | 87.67 % | 87.67 % |
| shrd | SHARADA | B | 86.46 % | 86.46 % | 71.88 % |
| modi | MODI | B | 97.47 % | 97.47 % | 82.28 % |
| tirh | TIRHUTA | B | 97.56 % | 97.56 % | 84.15 % |
| sidd | SIDDHAM | B | 70.65 % | 70.65 % | 69.57 % |
| newa | NEWA | B | 82.47 % | 82.47 % | 69.07 % |

Perso-Arabic, Unicode to Unicode: Urdu 27 of 41 alphabet letters return (65.85 %); corpus lines exact T1 0.0 %, T2 0.0 % (lossy by design); Sindhi and Shahmukhi have no layer of their own (see the navigator).
T2 below T1 is the **core limit** (mostly digits and signs that do not survive Devanagari -> Romenagri -> Devanagari in zip 5); it is listed per script, not fixed.

## Run
`python3 v6/tools/gen_fltr.py Romenagri v6 && python3 v6/tests/run_v6.py v6 Romenagri <built core dir> v6/results.json && python3 v6/tools/gen_pages.py v6` (run from the unpacked folder; Romenagri/ is zip 5's, with built programs in the core dir).

## Pivot choices made (12 Nov): Assamese ৰ->U+0931, ৱ->U+0979; Tamil/Malayalam ழ ഴ->U+0934, ற റ->U+0931, ன ഩ->U+0929; Malayalam chillus -> consonant+virama (forward only). Open issues: `open-issues.html`.
