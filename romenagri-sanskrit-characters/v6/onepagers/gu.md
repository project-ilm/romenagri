# Gujarati (GUJARATI), tier A

Mapping layer: `Romenagri/fltr_gu_hi` (script to Devanagari) and `fltr_hi_gu` (back); table `v6/maps/gu.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 91 |
| Mapped to Devanagari (coverage) | 84 (92.31 %) |
| **T1** reversible, script -> Devanagari -> script | 84 = **92.31 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 73 = **80.22 %** of the repertoire (86.9 % of the mapped) |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 11 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ૱ ૺ ૻ ૼ ૽ ૾ ૿
- Core limit: ૦ ૧ ૨ ૩ ૪ ૫ ૬ ૭ ૮ ૯ ૰

## Open issues for linguists

- Phonetic fidelity and dialects: Inherent-vowel deletion is regular in speech (schwa not pronounced word-finally); ળ; ૅ ૉ vowels.
- Research needed: Schwa-deletion rule set; dialect tables (Kathiawadi, Surati).

