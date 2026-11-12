# Punjabi (Gurmukhi) (GURMUKHI), tier A

Mapping layer: `Romenagri/fltr_pa_hi` (script to Devanagari) and `fltr_hi_pa` (back); table `v6/maps/pa.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 80 |
| Mapped to Devanagari (coverage) | 73 (91.25 %) |
| **T1** reversible, script -> Devanagari -> script | 73 = **91.25 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 58 = **72.5 %** of the repertoire (79.45 % of the mapped) |
| Corpus `corp_pb.txt`, 159 lines, exact lines back | T1 100.0 %, T2 30.19 % |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 15 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ੑ ੰ ੱ ੲ ੳ ੴ ੵ
- Core limit: ਖ਼ ਗ਼ ਜ਼ ਫ਼ ੦ ੧ ੨ ੩ ੪ ੫ ੬ ੭ ੮ ੯ ੶

## Open issues for linguists

- Phonetic fidelity and dialects: Tones are not written; tippi/bindi and addak (gemination) need rules; ਙ ਞ rare; Majhi/Malwai/Doabi differ.
- Research needed: Addak and tippi handling; tone-marking convention.

