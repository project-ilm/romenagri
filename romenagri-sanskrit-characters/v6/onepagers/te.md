# Telugu (TELUGU), tier A

Mapping layer: `Romenagri/fltr_te_hi` (script to Devanagari) and `fltr_hi_te` (back); table `v6/maps/te.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 100 |
| Mapped to Devanagari (coverage) | 83 (83.0 %) |
| **T1** reversible, script -> Devanagari -> script | 83 = **83.0 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 72 = **72.0 %** of the repertoire (86.75 % of the mapped) |
| Corpus `corp_te.txt`, 87 lines, exact lines back | T1 100.0 %, T2 95.4 % |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 11 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ఀ ఄ ౕ ౖ ౘ ౙ ౚ ౝ ౷ ౸ ౹ ౺ ౻ ౼ ౽ ౾ ౿
- Core limit: ఴ ౦ ౧ ౨ ౩ ౪ ౫ ౬ ౭ ౮ ౯

## Open issues for linguists

- Phonetic fidelity and dialects: ఁ ఀ; ఱ ఴ archaic; Telangana vs Coastal vs Rayalaseema differ in ఎ/ఏ and ళ.
- Research needed: Archaic letter policy; dialect tables.

