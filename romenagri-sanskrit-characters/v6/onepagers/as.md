# Assamese (BENGALI), tier A

Mapping layer: `Romenagri/fltr_as_hi` (script to Devanagari) and `fltr_hi_as` (back); table `v6/maps/as.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 96 |
| Mapped to Devanagari (coverage) | 81 (84.38 %) |
| **T1** reversible, script -> Devanagari -> script | 80 = **83.33 %** of the repertoire (98.77 % of the mapped) |
| **T2** reversible through the zip 5 core | 67 = **69.79 %** of the repertoire (82.72 % of the mapped) |

T2 losses are of two kinds: **mapping** (T1 already fails: 1 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 13 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): ऱ <- ড় ৰ
- Unmapped (no Devanagari counterpart yet): ঀ ৎ ৗ ৲ ৳ ৴ ৵ ৶ ৷ ৸ ৹ ৺ ৻ ৼ ৾
- Core limit: ঢ় য় ০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯ ৽

## Open issues for linguists

- Phonetic fidelity and dialects: ৰ is /ɹ/ and ৱ /w/ (pivot: U+0931 and U+0979, a choice to confirm); শ ষ স are all /x/-ish in Assamese, not /ʃ/.
- Research needed: Confirm pivots for ৰ ৱ; Assamese-specific phoneme table (it shares the Bengali block, so the map is the same file).

