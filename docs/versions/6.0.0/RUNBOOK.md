# ROMENAGRI / ILM — FAMILY TEST SUITE RUNBOOK
Copyright (C) 1993-2026 Abhishek Choudhary.

## What each test measures (publishable definitions)
- KERNEL invariant: over exhaustive [a-z]^n, classify each string s by
  phi(s) -> rho(phi(s)) -> phi(rho(phi(s))):
  EXACT (rho∘phi = id) | NORMALIZED (stable canonical fixed point) |
  IRREDUCIBLE (no stable fixed point) | CRASH. Report all four; the headline
  is reversible-or-canonical = EXACT+NORMALIZED. ALWAYS name the kernel
  variant measured (chintamani vs 2003-04 holy-grail) — the figure is
  variant-dependent (measured: holy-grail 98.68%; chintamani pre-guard 55.6%
  with 4.05% crash; post-guard figure in KERNEL_POSTGUARD.tsv).
- BRAHMI family: script -> Devanagari hub (ISCII block offset, bijective on
  the aligned subset) -> kernel round trip. Report per script: coverage%
  (chars on the aligned subset), hub_rt_exact%, sample output. Script-specific
  letters outside the aligned subset are flagged research frontier, not failure.
- PERSO-ARABIC: authentic corpora (corp_ur, test_ar) -> fltr_ur_hi projection
  -> hub -> kernel. Abjad vowel underspecification is a property of the source
  orthography; reversibility claim is to the CANONICAL form.
- NW-SEMITIC: 22-letter abjad projection to Arabic hub (finals merge =
  documented many-to-one); reversible to canonical form.

## How to run
  bash scripts/60_families.sh     # Brahmi (8 scripts) + post-guard kernel re-measure
  bash scripts/65_perso_arabic.sh # Urdu/Arabic corpora via legacy filter
  bash scripts/66_nw_semitic.sh   # Hebrew (embedded table)
  # full kernel sweep (45-60 min) after guards:
  bash scripts/30_roundtrip.sh
Results in results/FAMILIES/*.tsv ; logs in logs/run.log.

## Publishing
Each TSV is a paper table. The honest claims: (1) the measured kernel
invariant with variant named; (2) per-script hub coverage + round trip;
(3) byte 1.76x / alphabet 51->24 compression (COMPRESSION_RESULTS.json);
(4) token-count k<1 at matched merges — report it, do not hide it; the
gain is byte-level and alphabet-level, lossless.
