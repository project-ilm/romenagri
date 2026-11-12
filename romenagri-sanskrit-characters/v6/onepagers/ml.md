# Malayalam (MALAYALAM), tier A

Mapping layer: `Romenagri/fltr_ml_hi` (script to Devanagari) and `fltr_hi_ml` (back); table `v6/maps/ml.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 118 |
| Mapped to Devanagari (coverage) | 83 (70.34 %) |
| **T1** reversible, script -> Devanagari -> script | 83 = **70.34 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 72 = **61.02 %** of the repertoire (86.75 % of the mapped) |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 11 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ഀ ഄ ഺ ഻ ഼ ൎ ൏ ൔ ൕ ൖ ൗ ൘ ൙ ൚ ൛ ൜ ൝ ൞ ൟ ൰ ൱ ൲ ൳ ൴ ൵ ൶ ൷ ൸ ൹ ൺ ൻ ർ ൽ ൾ ൿ
- Core limit: ഴ ൦ ൧ ൨ ൩ ൪ ൫ ൬ ൭ ൮ ൯

## Open issues for linguists

- Phonetic fidelity and dialects: Chillu letters ൺ ൻ ർ ൽ ൾ are written as consonant + virama in the pivot (forward only, lossy); ഴ ഩ റ pivoted to ऴ ऩ ऱ; /ə/ vs /ɨ/ for the vowel sign ് .
- Research needed: Chillu policy (a pivot with a joiner or private code point would make them reversible); samvruthokaram.

