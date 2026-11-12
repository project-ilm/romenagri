# Romenagri — Reversible Transliteration Library (Perso-Arabic seed)

DOI (6.0.0): [10.5281/zenodo.24170925](https://doi.org/10.5281/zenodo.24170925)

Deterministic, reversible transliteration engine underlying the Hindawi
Programming System (first public release 15 August 2004) and Project ILM.
Original Romenagri release: 2003 (GPL).

**This seed release** packages the Romenagri core (round-trip transliteration
engine) together with the **Perso-Arabic** data — covering the Perso-Arabic-
family languages demonstrated live at https://ilm.codes/map.html
(transpile-and-execute). Other-script corpora are included for context.

## Layout
- `src/`     — the reversible core: ACII layer, acii2rmn/rmn2acii, stack, lexer,
               uni<->acii, hin paths. (Extracted from the chintamani lineage.)
- `data/`    — Perso-Arabic: Arabic/Urdu character maps, corpora, tashkil,
               alphabet, and the Urdu<->Hindi filter (fltr_ur_hi).
- `corpora/` — other-script corpora (Hindi, Bengali, Punjabi, Telugu).
- `tests/`   — sample round-trip inputs.
- `docs/`    — conversion notes / instructions.

## Status (honest)
Reversibility (measured over arbitrary [a-z] input): ~98.68% exact-or-
canonicalizable, ~1.31% irreducible-ambiguity floor. The engine compiles with
GCC; hardening (totality over the full input space, O(n), re-entrancy, WASM)
is the next step. This is a SEED release for prior-art and reuse, not a
hardened v1.

## Lineage / prior art
SourceForge (sf.net/projects/hindawi, 2004), Savannah (savannah.nongnu.org/
projects/hindawi, 2005), CSI YITPA 2005, FOSS India (CDAC), TDIL recognition.

Copyright (C) 1993-2026 Abhishek Choudhary. Licensed GPL (see LICENSE).
Dedicated, among others, to Dr. A.P.J. Abdul Kalam. May Allah forgive and bless
his soul.

<!-- trademarks:begin -->
---
AyeAI®, AyeCNSe® and AyeAM® are registered trademarks of Abhishek Choudhary in India, used and claimed worldwide since
2019. The names of his products and projects are his trademarks; see [legal/TRADEMARKS.md](legal/TRADEMARKS.md). Code
licences in this repository grant copyright permissions only and no right in any mark.
© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.
<!-- trademarks:end -->

## Layout since 6.0.1 (12 Nov 2026)

Version 5 (zip no. 5, the Romenagri core with the missing Sanskrit characters) is the face: the site opens on its front page,
and every page of the earlier site is kept (`docs/results.html`, and whole in `docs/versions/6.0.0/`). zip 5 sits at the root as
its `SHA256SUMS` lists it: `Romenagri/` (the kernel with patches 0001 to 0003), `patches/`, `tests/` (`tests/run_all.sh`),
`tools/`, `results/`, `romenagri-site/` (the site's sources), with its README as `README-SANSKRIT-CHARACTERS.md` and its LICENSE
as `legal/LICENSE-SANSKRIT-CHARACTERS`. The v6 delta lies over it as designed: `v6/` (sed mapping layers for 18 scripts onto the
Devanagari hub) and its pages; its pairs also fill 17 script tables in `tables/`. `v7/` holds AInagri and the Unicode inventory,
`V7-TASKS.md` the next work. `src/`, `data/` and `corpora/` (the extraction of 2026.07) stay until the author rules on them.
How work proceeds: `AGENTS.md`; where it stands: `CONTEXT.md`.
