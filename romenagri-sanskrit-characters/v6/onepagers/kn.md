# Kannada (KANNADA), tier A

Mapping layer: `Romenagri/fltr_kn_hi` (script to Devanagari) and `fltr_hi_kn` (back); table `v6/maps/kn.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 91 |
| Mapped to Devanagari (coverage) | 83 (91.21 %) |
| **T1** reversible, script -> Devanagari -> script | 83 = **91.21 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 72 = **79.12 %** of the repertoire (86.75 % of the mapped) |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 11 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ಀ ಄ ೕ ೖ ೝ ೱ ೲ ೳ
- Core limit: ೞ ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯

## Open issues for linguists

- Phonetic fidelity and dialects: ೞ ಱ archaic (not mapped); /e/ and /o/ short/long pairs; Mysore/Dharwad/Coastal differ.
- Research needed: Archaic letter policy (ೞ ಱ); dialect tables.

