# Bengali (Bangla) (BENGALI), tier A

Mapping layer: `Romenagri/fltr_bn_hi` (script to Devanagari) and `fltr_hi_bn` (back); table `v6/maps/bn.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 96 |
| Mapped to Devanagari (coverage) | 81 (84.38 %) |
| **T1** reversible, script -> Devanagari -> script | 80 = **83.33 %** of the repertoire (98.77 % of the mapped) |
| **T2** reversible through the zip 5 core | 67 = **69.79 %** of the repertoire (82.72 % of the mapped) |
| Corpus `corp_bn.txt`, 24 lines, exact lines back | T1 100.0 %, T2 29.17 % |

T2 losses are of two kinds: **mapping** (T1 already fails: 1 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 13 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): ऱ <- ড় ৰ
- Unmapped (no Devanagari counterpart yet): ঀ ৎ ৗ ৲ ৳ ৴ ৵ ৶ ৷ ৸ ৹ ৺ ৻ ৼ ৾
- Core limit: ঢ় য় ০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯ ৽

## Open issues for linguists

- Phonetic fidelity and dialects: Inherent vowel is /ɔ/ not /a/; অ ও pair; ব/ভ, শ ষ স all /ʃ/ in speech; য় ড় ঢ় as separate letters; Sylheti and Rarhi/Barendri readings differ.
- Research needed: Native-speaker phoneme table per dialect; policy for ড় ঢ় য় (precomposed vs nukta).

