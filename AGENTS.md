# For any agent or person taking work on Romenagri

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI.

1. Read `AI_CONTRACT.md` (the working agreement), `CONTINUITY.md` (the architecture: three axes; one kernel and N tables),
   `CONTEXT.md` (where the work stands, the versions, the decisions waiting for the author), then the README and the tasks file of
   the latest version (`V6-README.md`, `V7-TASKS.md`). The estate's contract is zistgah/governance `CONTRACT.md`.
2. Retrieve before building. Clone this repository and read what is already here (`Romenagri/`, `src/`, `tables/`, `results/`,
   `docs/`) before proposing anything. Nothing that exists is rebuilt (C51); a defect in it is fixed where it lives.
3. Work arrives as numbered versions: a full zip (zip no. 5) or a delta zip over the one before (v6, v7, ...). A version comes
   with its own README, a tasks file written before the work, and its checksum list (`SHA256SUMS`, `V6-SHA256SUMS`, ...). A delta
   only adds files; changing a file of the version beneath it is said in its README.
4. A version lands at the paths it was designed for: its own layout at the root of this repository, never in a folder by
   itself. After it lands, every checksum list of every version still verifies.
5. One kernel and N tables. The kernel is `Romenagri/`; it changes only by a numbered patch in `patches/`, with the author's
   agreement. Every script has one table, `tables/<script>_to_deva.tsv`, onto the Devanagari hub; mapping layers and script
   pages are generated from the data, never edited by hand.
6. The site is `docs/`. When a version is published, its front page becomes the face (`docs/index.html`). No page of the
   earlier site is lost: the face it replaces is kept whole in `docs/versions/<version>/` and listed in
   `docs/versions/index.html`; every page carries one navigation; `docs/sw.js` caches every page, and its cache name changes
   with each release.
7. Done means the tests pass, with their output pasted: `tests/run_all.sh` (the kernel), each version's own tests
   (`v6/tests/run_v6.py`, `v7/ainagri/test_ainagri.py`), every checksum list, and no broken link in `docs/`. A step not run is
   reported as not run. Reversibility is reported as `V6-TASKS.md` section 3 defines it (coverage, T1, T2, collisions).
8. A release is one update script in the estate's proven shape: the pinned head, a dry run first, typed PUSH and MINT gates,
   misty on the author's machine, a new version beneath the previous DOI, the DOI recorded back and the tree resealed; commits
   under ayeai.ayeam@gmail.com (C63). `CONTEXT.md` is brought up to date in the same release.
9. Every script is taken with the languages that use it across the world, low-resource ones included.
10. The author's words, spellings and claims are kept as he gave them; what cannot be verified carries a disclaimer (C38).
    The names are spelt Romenagri, AInagri, Hindawi, Devanagari.
