# Tamil (TAMIL), tier A

Mapping layer: `Romenagri/fltr_ta_hi` (script to Devanagari) and `fltr_hi_ta` (back); table `v6/maps/ta.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 123 |
| Mapped to Devanagari (coverage) | 60 (48.78 %) |
| **T1** reversible, script -> Devanagari -> script | 60 = **48.78 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 49 = **39.84 %** of the repertoire (81.67 % of the mapped) |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 11 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ௗ ௰ ௱ ௲ ௳ ௴ ௵ ௶ ௷ ௸ ௹ ௺ 𑿀 𑿁 𑿂 𑿃 𑿄 𑿅 𑿆 𑿇 𑿈 𑿉 𑿊 𑿋 𑿌 𑿍 𑿎 𑿏 𑿐 𑿑 𑿒 𑿓 𑿔 𑿕 𑿖 𑿗 𑿘 𑿙 𑿚 𑿛 𑿜 𑿝 𑿞 𑿟 𑿠 𑿡 𑿢 𑿣 𑿤 𑿥 𑿦 𑿧 𑿨 𑿩 𑿪 𑿫 𑿬 𑿭 𑿮 𑿯 𑿰 𑿱 𑿿
- Core limit: ழ ௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯

## Open issues for linguists

- Phonetic fidelity and dialects: No voiced/aspirate series: one letter covers क ग, च ज, ट ड, त द, प ब by position; ழ ற ன pivoted to ऴ ऱ ऩ; Grantha letters ஜ ஷ ஸ ஹ are loan-only; Chennai/Madurai/Jaffna/Kongu differ.
- Research needed: Positional voicing rules for a Tamil->Devanagari direction (the map is lossy backward); Grantha usage policy.

