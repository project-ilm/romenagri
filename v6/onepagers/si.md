# Sinhala (SINHALA), tier B

Mapping layer: `Romenagri/fltr_si_hi` (script to Devanagari) and `fltr_hi_si` (back); table `v6/maps/si.csv`.

| Measure | Value |
|---|---|
| Repertoire (assigned code points of the block) | 111 |
| Mapped to Devanagari (coverage) | 1 (0.9 %) |
| **T1** reversible, script -> Devanagari -> script | 1 = **0.9 %** of the repertoire (100.0 % of the mapped) |
| **T2** reversible through the zip 5 core | 1 = **0.9 %** of the repertoire (100.0 % of the mapped) |

T2 losses are of two kinds: **mapping** (T1 already fails: 0 letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: 0 letters, v6 does not touch the core).

- Collisions (several letters to one Devanagari letter): none
- Unmapped (no Devanagari counterpart yet): ං ඃ අ ආ ඇ ඈ ඉ ඊ උ ඌ ඍ ඎ ඏ ඐ එ ඒ ඓ ඔ ඕ ඖ ක ඛ ග ඝ ඞ ඟ ච ඡ ජ ඣ ඤ ඥ ඦ ට ඨ ඩ ඪ ණ ඬ ත ථ ද ධ න ඳ ප ඵ බ භ ම ඹ ය ර ල ව ශ ෂ ස හ ළ ෆ ් ා ැ ෑ ි ී ු ූ ෘ ෙ ේ ෛ ො ෝ ෞ ෟ ෦ ෧ ෨ ෩ ෪ ෫ ෬ ෭ ෮ ෯ ෲ ෳ ෴ 𑇡 𑇢 𑇣 𑇤 𑇥 𑇦 𑇧 𑇨 𑇩 𑇪 𑇫 𑇬 𑇭 𑇮 𑇯 𑇰 𑇱 𑇲 𑇳 𑇴
- Core limit: none

## Open issues for linguists

- Phonetic fidelity and dialects: Unicode names do not match Devanagari (KAYANNA, not KA): a name pairing finds almost nothing; prenasalised consonants and ඇ ඈ vowels (/æ/) have no Devanagari letter.
- Research needed: A hand-built table (ISO 15919 pairs) and a decision on /æ/ and the prenasalised series. Not done in v6.

