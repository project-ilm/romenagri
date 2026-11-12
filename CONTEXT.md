# CONTEXT: Romenagri

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. Kept up to date with every release (AGENTS.md, point 8).

## What it answers

Romenagri (GPL, 2003) is the deterministic, reversible transliteration kernel under the Hindawi Programming System (2004) and
Project ILM: any script onto the Devanagari hub and into Romenagri ASCII-7, and back, byte for byte. One kernel, N tables
(`CONTINUITY.md`).

## Versions and the face of the site

| Release | Date | What it is | Face of the site |
|---|---|---|---|
| seed | Jun to Jul 2026 | the Perso-Arabic seed: `src/` (the kernel's extraction), `data/`, `corpora/`, the measured results, `tables/` named for 73 scripts | Romenagri, Measured Results |
| 6.0.0 | 12 Nov 2026, DOI 10.5281/zenodo.24170925 | zip no. 5 and the v6 delta added, but in a folder by themselves, with the site unchanged | Measured Results |
| 6.0.1 | 12 Nov 2026 | zip 5 and v6 where they were designed to sit; version 5 becomes the face | version 5's front page; the earlier face in `docs/versions/6.0.0/` and as `docs/results.html` |

## Where things are (6.0.1)

`Romenagri/` the kernel with patches 0001 to 0003 (the missing Sanskrit characters, the guards, the nukta layer); `patches/`;
`tests/` (`tests/run_all.sh`); `tools/`; `results/`; `romenagri-site/` (the site's sources, built by
`romenagri-site/build_site.py`); `v6/` (sed mapping layers for 18 scripts, their maps, generator and tests); `tables/` (17 of
the 73 script tables now hold rows, from v6); `v7/` (AInagri, the Unicode inventory) and `V7-TASKS.md`; `docs/` the site; the seed's
`src/`, `data/`, `corpora/`, `langs/`, `langspec/`, `bindings/`, `demos/`, `papers/` as they were.

## Work retrieved before building 6.0.1

The live repository at 5403a1a (6.0.0); zip no. 5 and its SHA256SUMS; the v6 delta and V6-SHA256SUMS; the site's earlier face
and its app layer (ZPWA block, service worker, share layer); chandah's AGENTS.md and CONTEXT.md as the estate's shape.

## Choices made in 6.0.1, flagged for the author

- `src/`, `data/` and `corpora/` are kept beside `Romenagri/`; `Romenagri/` is the patched kernel, `src/` the unpatched
  extraction (seven of its files differ), `data/` and `corpora/` byte-identical copies. Which stays is the author's ruling.
- `v6/maps/` is kept beside the 17 tables it filled; two copies of those pairs until the author rules.
- Licence: zip 5's files say GPL-2.0-or-later; this repository's LICENSE and CITATION.cff say GPL-3.0-or-later.
- zip 5's README and LICENSE are kept as `README-SANSKRIT-CHARACTERS.md` and `legal/LICENSE-SANSKRIT-CHARACTERS`, since they
  would have replaced the repository's own.
- The earlier face's app layer (manifest, theme, share layer) is carried onto the new face unchanged.

## Evidence states

Verified by execution when 6.0.1 was made: zip 5's SHA256SUMS and V6-SHA256SUMS at their paths; `tests/run_all.sh` (the kernel
builds from `Romenagri/`, every suite passes); AInagri's test (1,610 of 1,610 synthetic strings, 202 of 202 corpus lines); no
broken local link in `docs/`. v6's own T1 and T2 are as recorded in `v6/results.json`, not rerun.

## Open

`V7-TASKS.md` (56 empty script tables; 90 Unicode scripts with no table, Hebrew to Egyptian Hieroglyphs, Cyrillic and the other
alphabets, the other abugidas; AInagri's own tasks); the decisions above.
