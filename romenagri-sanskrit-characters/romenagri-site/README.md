<!-- SPDX-License-Identifier: GPL-2.0-or-later -->
# romenagri-site

Copyright (C) 1993-2026 Abhishek Choudhary. Free software under the GNU General Public License, version 2 or (at your option) any later version: see `COPYING`, `LICENSE` and `NOTICE` at the root of the package.

A static site of five pages and a notebook about the converters of `Romenagri/` (Unicode <-> ACII <-> Romenagri) and the three patches of this package. It is built from the headers of `Romenagri/` and from runs of the compiled C programs, so that nothing a table or an output shows is typed in by hand.

## The pages (`docs/`)

| Page | What it has |
|---|---|
| `index.html` | the chain in one line; a box in which the text that you type is carried through every stage of the chain (13 examples, the form of the nukta letters, the warning layer); the nukta layer in a paragraph; the author's note on the danda |
| `explainer.html` | the three layers; the tables; the decoder (`acii2rmn`) and the parser (`rmn2acii`); the round-trip contract; the nukta layer (rule, form, warning), the choice of the form, a worked example, and where the layer stops |
| `characters.html` | the twelve characters of patch 0001 with their bytes, Romenagri strings and saral spellings, and why; the eleven letters with a nukta in the three forms; what each form writes in each direction |
| `challenges.html` | the danda; the eight cases C1 to C8 and the decision on each, every one run through the compiled converters in the three forms; the fifteen reserved keys; what is open |
| `documents.html` | the specification and its sections, the patches, the tests, the notebook, how to rebuild and publish the site, sources, licence |

`docs/` also holds `style.css` and `demo.js` (written by hand), `romenagri.js` and `examples.js` (generated), `romenagri-explainer.ipynb` (generated; the same file as `notebooks/romenagri-explainer.ipynb`) and the empty file `.nojekyll`.

## The box on the front page

The box runs `romenagri.js`, a JavaScript port of the four converters (`uni2acii`, `acii2rmn`, `rmn2acii`, `acii2uni`) whose tables are generated from `unicode.h`, `acii.h` and `nukta.h`. **It is not the production code.** `build_site.py --check` compares it with the compiled C programs, byte for byte and crash for crash, on random and on exhaustive inputs, and with the Python models of `tests/` (`model.py`, `handwritten_parser.py`); it also runs twelve deliberately broken copies of it, to show that the comparison notices (see `results/site-check.txt` at the root of the package).

## The notebook

`notebooks/romenagri-explainer.ipynb` runs the compiled C programs on Devanagari text and shows what each stage writes. Nothing in it is a model. It needs Python 3, `gcc`, `make` and `flex`; the first cell compiles a copy of `Romenagri/` in a temporary directory, or you can set `ROMENAGRI_BIN` to a directory of built programs (`ROMENAGRI_SRC` names the `Romenagri/` directory to compile). The outputs stored in the file are those of the build of the site.

## Building and checking

```
python3 romenagri-site/build_site.py             writes docs/ and notebooks/
python3 romenagri-site/build_site.py --check     builds in memory and compares with the files; checks the pages; then
                                                 compares the JavaScript with the C programs and the Python models
python3 romenagri-site/build_site.py --cbin DIR  use the programs of DIR (a built Romenagri/ directory) instead of
                                                 compiling a copy of ../Romenagri in a temporary directory
```

Needs `python3`, `gcc`, `make` and `flex` (with `-lfl`); `--check` also needs `node`. The `--check` of the recorded run took 48 seconds. `build_site.py` writes `docs/` and `notebooks/` only (the programs are compiled in a temporary directory that is removed afterwards), and `--check` writes no file of the package.

What `--check` verifies, in 39 checks:

1. the ten generated files on disk are what a new build gives, and `docs/` holds only generated files and `style.css` and `demo.js`;
2. every page is well-formed, has unique ids, no placeholder left, a language, a title and a viewport, and every link and script leads to a file or an anchor that exists; the notebook is a valid nbformat 4 document (its structure; `nbformat` itself is used only if it is installed);
3. the JavaScript agrees with the compiled programs and with the models on 4,900 (`uni2acii`), 2,450 (`acii2uni`), 3,000 (`acii2rmn`), 3,500 (`rmn2acii`) and 2,250 (the whole chain) cases, and with the models of `tests/` on 77,057 (the decoder) and 312,560 (the parser) cases;
4. the cases reach what they are meant to reach (every nukta letter, the joins of `nfc`, the warnings, the crashes of `acii2rmn` and `rmn2acii`);
5. each of twelve broken copies of the JavaScript is caught.

## Publishing on GitHub Pages

Copy the contents of `romenagri-site/docs/` into a folder named `docs/` at the root of the repository that is to host the site, commit, and in the repository's settings, under Pages, choose "Deploy from a branch", the branch and the `/docs` folder. `.nojekyll` makes Pages serve the files as they are. The pages use relative links only, so they work from any path. Nothing in this package publishes anything.

## What to edit, and what not to

- The pages are `src/*.body.html` (the text) and `site_pages.py` (the tables, the cases, the notebook cells, the notes). Edit those and run `build_site.py`; do not edit `docs/*.html`, `docs/romenagri.js`, `docs/examples.js` or the notebook, which are overwritten (and `--check` fails if they are out of date).
- `src/romenagri.js.in` is the template of the port, and `src/check_js.js` the node runner of the comparison.
- **The author's note on the danda** (on the front page and on the Challenges page) comes from the draft of another AI model (see below); it is marked there as carried over and not confirmed. In `site_pages.py`, `NOTE_STATUS = None` removes the mark, and `AUTHOR_NOTE = None` and `DANDA_NOTE = None` remove the note.
- If a header of `Romenagri/` changes, run `build_site.py`: the tables follow, and `--check` says whether the port still agrees with the C programs.

## Where it came from

On 9 November the author sent a site that he had had Grok build from the v4 zip of this package: five HTML pages with their own copy of the style, a notebook and a short README, and nothing else. This site takes from it the plan (five pages, a front page with a box, an explainer, the characters, the challenges, the documents), the look of the header band, the idea of a notebook, and the author's note on the danda.

It does not take its tables, its demonstration or its notebook. Their tables were typed by hand and differ from the headers of `Romenagri/` (16 of the 63 rows of its Unicode table and 29 of the 53 rows of its key table are not the rows of `unicode.h` and `acii.h`, and two of the eleven nukta letters are missing), the Romenagri that its model writes for a cluster is not the Romenagri that `acii2rmn` writes (`Dzva`, where the program writes `_rdwa`), and the model gives the single code point U+095C back from the whole chain, which the decision C1 excludes and the converters do not do. The zip changed no converter code: the claim that it fixed the remaining nukta issues is a claim about these pages and this model. The pages here were therefore written again, from the headers and from the programs.
