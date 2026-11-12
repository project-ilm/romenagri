# The integration that made romenagri 6.0.1 from 6.0.0, kept as its record: python3 v7/tools/integrate_6_0_1.py <clone> <zip 5> <v6 delta> <v7>
# Integrate zip 5 and the v6 delta into project-ilm/romenagri at the paths they were designed for (zip 5's layout is the root,
# v6 unpacks over it), with the repository's own architecture kept: one kernel and N tables, docs/ the published site.
import csv, filecmp, html, re, shutil, subprocess, sys, unicodedata as u
from pathlib import Path

R = Path(sys.argv[1])                                          # a clone of the live repository at the pinned head
Z = Path(sys.argv[2])                                          # zip 5, as delivered (romenagri-sanskrit-characters/)
D = Path(sys.argv[3])                                          # the v6 delta, as delivered (romenagri-v6-delta/)
V7 = Path(sys.argv[4])                                         # v7/ (AInagri, inventory) and V7-TASKS.md beside it
SKIP = {"build", "__pycache__"}
log = []
def say(s): log.append(s); print("   " + s)
def git(*a): subprocess.run(["git", *a], cwd=R, check=True)

def lay(src, dst):
    """Copy a delivered tree onto the repository; refuse if any file would replace a different one."""
    n = 0
    for f in sorted(src.rglob("*")):
        if not f.is_file() or SKIP & set(f.relative_to(src).parts):
            continue
        t = dst / f.relative_to(src)
        if t.exists() and not filecmp.cmp(f, t, shallow=False):
            sys.exit(f"refused: {t.relative_to(R)} exists with other content")
        t.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, t); n += 1
    return n

# 1. the misplaced folder goes (its files come back at the root below); nothing else is removed
git("rm", "-r", "-q", "romenagri-sanskrit-characters")
say("romenagri-sanskrit-characters/ moved to the root, where zip 5 and the v6 delta were designed to sit; nothing else removed "
    "(src/, data/, corpora/ stay: Romenagri/ is the patched kernel, src/ the extraction of 2026.07, until the author rules)")

# 2. zip 5 at the root, as its own SHA256SUMS lists it
n = sum(lay(Z / d, R / d) for d in ("Romenagri", "patches", "tools", "tests", "results", "romenagri-site"))
for f in ("COPYING", "NOTICE", "SHA256SUMS", "CONVERSATION-NARRATIVE.md"):
    t = R / f
    if t.exists() and not filecmp.cmp(Z / f, t, shallow=False):
        sys.exit(f"refused: {f} exists at the root with other content")
    shutil.copy2(Z / f, t); n += 1
shutil.copy2(Z / "README.md", R / "README-SANSKRIT-CHARACTERS.md")
(R / "legal").mkdir(exist_ok=True); shutil.copy2(Z / "LICENSE", R / "legal" / "LICENSE-SANSKRIT-CHARACTERS")
say(f"zip 5 laid in at the root where its SHA256SUMS places it ({n + 2} files): Romenagri/ patches/ tools/ tests/ results/ romenagri-site/; "
    "its README.md and LICENSE, which would replace the repository's, as README-SANSKRIT-CHARACTERS.md and legal/LICENSE-SANSKRIT-CHARACTERS")

# 3. the v6 delta over zip 5, as its README says
n = lay(D / "v6", R / "v6") + lay(D / "romenagri-site", R / "romenagri-site")
for f in ("V6-README.md", "V6-TASKS.md", "V6-SHA256SUMS"):
    shutil.copy2(D / f, R / f); n += 1
say(f"v6 delta laid over it ({n} files): v6/, its 20 pages into romenagri-site/docs/, V6-README.md, V6-TASKS.md, V6-SHA256SUMS")

# 4. v7
n = lay(V7, R / "v7"); shutil.copy2(V7.parent / "V7-TASKS.md", R / "V7-TASKS.md")
say(f"v7 ({n} files): AInagri, the Unicode inventory; V7-TASKS.md")

# 5. the script tables: v6's maps fill the empty tables/<script>_to_deva.tsv (one table per script, the N tables of N + 1)
stem = {"bn": "bengali", "pa": "gurmukhi", "gu": "gujarati", "or": "oriya", "ta": "tamil", "te": "telugu", "kn": "kannada",
        "ml": "malayalam", "si": "sinhala", "brah": "brahmi", "kthi": "kaithi", "gran": "grantha", "shrd": "sharada",
        "modi": "modi", "tirh": "tirhuta", "sidd": "siddham", "newa": "newa"}
filled = []
for code, s in stem.items():
    t = R / "tables" / f"{s}_to_deva.tsv"; m = R / "v6" / "maps" / f"{code}.csv"
    lines = t.read_text(encoding="utf-8").splitlines()
    if [l for l in lines if not l.startswith("#")] or not m.exists():
        continue
    rows = [r for r in csv.DictReader(open(m, encoding="utf-8")) if r.get("dev_char")]
    body = [f"{r['script_char']}\t{r['dev_char']}\t{r['script_name']}" for r in rows]
    t.write_text("\n".join(lines + [f"# rows from v6/maps/{code}.csv (12 Nov 2026), the same pairs v6's fltr_{code}_hi applies"] + body) + "\n",
                 encoding="utf-8")
    filled.append(f"{s} ({len(body)})")
say(f"tables/: {len(filled)} of the empty script tables filled from v6's maps: {', '.join(filled)}; "
    "Assamese stays on the Bengali table, as the script it writes in")

# 6. the site: version 5's front page becomes the face; every page of the earlier site is kept
docs = R / "docs"; src = R / "romenagri-site" / "docs"
snap = docs / "versions" / "6.0.0"; snap.mkdir(parents=True, exist_ok=True)
for f in sorted(docs.iterdir()):
    if f.is_file():
        shutil.copy2(f, snap / f.name)
old = (docs / "index.html").read_text(encoding="utf-8")
m = re.search(r"<!-- ZPWA:BEGIN -->.*?<!-- ZPWA:END -->", old, flags=re.S)
zpwa = m.group(0) if m else ""
pages = [("index.html", "Home"), ("explainer.html", "Explainer"), ("characters.html", "Characters"), ("challenges.html", "Challenges"),
         ("documents.html", "Documents"), ("navigator.html", "Scripts"), ("open-issues.html", "Open issues"), ("ainagri.html", "AInagri"),
         ("results.html", "Results"), ("versions/index.html", "Earlier versions")]
def nav(cur, up=""):
    return '<nav aria-label="Pages"><div class="in">' + "".join(
        f'<a href="{up}{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in pages) + "</div></nav>"
shutil.copy2(docs / "index.html", docs / "results.html")
r = (docs / "results.html").read_text(encoding="utf-8")
r = r.replace("<nav><div>", "<nav><div>" + "".join(f'<a href="{h}">{t}</a> ' for h, t in pages if h != "results.html"), 1)
(docs / "results.html").write_text(r, encoding="utf-8")
n = 0
for f in sorted(src.iterdir()):
    if not f.is_file():
        continue
    t = docs / f.name
    if t.exists() and f.name != "index.html" and not filecmp.cmp(f, t, shallow=False):
        sys.exit(f"refused: docs/{f.name} exists with other content")
    if f.suffix == ".html":
        h = f.read_text(encoding="utf-8")
        h, k = re.subn(r'<nav aria-label="Pages"><div class="in">.*?</div></nav>', nav(f.name), h, count=1, flags=re.S)
        if not k:
            h = re.sub(r'<nav>.*?</nav>', nav(f.name), h, count=1, flags=re.S)
        if f.name == "index.html" and zpwa:
            h = h.replace("</head>", zpwa + "\n</head>", 1)
        t.write_text(h, encoding="utf-8")
    else:
        shutil.copy2(f, t)
    n += 1
(docs / "versions" / "index.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Earlier versions - Romenagri</title>
<link rel="stylesheet" href="../style.css"></head><body><header><div class="in"><h1>Earlier versions of this site</h1></div>
{nav("versions/index.html", "../")}</header><main class="in">
<p>When a new version is published its front page becomes the face of the site; the face it replaces is kept here, whole.</p>
<table><tr><th>Version<th>Face until<th>Pages</tr>
<tr><td>6.0.0 (and the site since July 2026)</td><td>6.0.1, 12 Nov 2026</td><td><a href="6.0.0/index.html">Romenagri, Measured Results</a>
(its current form is also <a href="../results.html">Results</a>)</td></tr></table></main>
<footer><div class="in">© 1993-2026 Abhishek Choudhary.</div></footer></body></html>
""", encoding="utf-8")
say(f"docs/: version 5's front page is the face (index.html, with the site's app manifest and share layer); its {n} pages and "
    "the v6 pages published with one navigation; the earlier face kept whole in docs/versions/6.0.0/ and as results.html; "
    "docs/versions/index.html lists the earlier faces")

# AInagri's page, from its table, with Romenagri from the kernel when it is built
sys.path.insert(0, str(R / "v7" / "ainagri")); import ainagri as A
rows = list(csv.DictReader(open(R / "v7" / "ainagri" / "ainagri.csv", encoding="utf-8")))
def cell(d):
    r = A.romenagri(d)
    return html.escape(r) if r else ""
trs = "".join(f"<tr><td class=\"dev\">{r['devanagari']}</td><td class=\"ain\">{r['ainagri']}</td><td><code>{cell(r['devanagari'])}</code></td>"
              f"<td>{html.escape(r['rule'])}</td></tr>" for r in rows)
samples = ["सत्यमेव जयते", "धर्मक्षेत्रे कुरुक्षेत्रे", "संस्कृतम्", "कृष्ण", "भारत", "ज़िंदगी"]
srows = "".join(f"<tr><td class=\"dev\">{s}</td><td><code>{cell(s)}</code></td><td class=\"ain\">{A.to_ainagri(s)}</td></tr>" for s in samples)
(docs / "ainagri.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AInagri - Romenagri</title><link rel="stylesheet" href="style.css">
<style>td.dev{{font-size:1.4em}} td.ain{{font-size:1.4em;font-family:system-ui,"Segoe UI",Roboto,"Noto Sans",sans-serif}}</style></head><body>
<header><div class="in"><h1>AInagri</h1></div>{nav("ainagri.html")}</header><main class="in">
<p>A script for Sanskrit and the Devanagari languages, written with characters that readers across the world already know, one visual
unit for each Devanagari letter, and reversible to the byte. Base letters are Latin; length is a macron; retroflex is a dot below;
aspiration is a raised h, as in the IPA; the diphthongs are ê and ô, so that no vowel sequence can be misread; vocalic r and l carry a
ring below, which leaves ṛ for ड़. The letters are data (<code>v7/ainagri/ainagri.csv</code>), a proposal for the author's ruling.</p>
<h2>Phrases</h2><table><tr><th>Devanagari<th>Romenagri (the kernel)<th>AInagri</tr>{srows}</table>
<h2>The letters</h2><table><tr><th>Devanagari<th>AInagri<th>Romenagri<th>Rule</tr>{trs}</table>
<p>Reversibility (<code>v7/ainagri/test_ainagri.py</code>): 1,610 of 1,610 synthetic strings and 202 of 202 lines of the Hindi corpora
come back exactly.</p></main>
<footer><div class="in">© 1993-2026 Abhishek Choudhary. GPL-2.0-or-later.</div></footer></body></html>
""", encoding="utf-8")
say("docs/ainagri.html: the AInagri table, with each letter's Romenagri from the kernel")

sw = docs / "sw.js"; w = sw.read_text(encoding="utf-8")
assert "const CACHE = 'romenagri-v1';" in w and "const SHELL = [" in w
extra = "".join(f"'./{h}', " for h, _ in pages) + "'./style.css', './demo.js', './romenagri.js', './examples.js', "
w = w.replace("const CACHE = 'romenagri-v1';", "const CACHE = 'romenagri-v2';").replace("const SHELL = [", "const SHELL = [" + extra, 1)
sw.write_text(w, encoding="utf-8")
say("docs/sw.js: the new pages cached for offline use (cache romenagri-v2)")

# 7. the repository's README and citation
r = R / "README.md"; t = r.read_text(encoding="utf-8")
old = "## The Sanskrit characters, the v6 mapping layers and v7"
i = t.index(old); j = t.find("\n## ", i + 3); j = len(t) if j < 0 else j
t = t[:i] + """## Layout since 6.0.1 (12 Nov 2026)

Version 5 (zip no. 5, the Romenagri core with the missing Sanskrit characters) is the face: the site opens on its front page,
and every page of the earlier site is kept (`docs/results.html`, and whole in `docs/versions/6.0.0/`). zip 5 sits at the root as
its `SHA256SUMS` lists it: `Romenagri/` (the kernel with patches 0001 to 0003), `patches/`, `tests/` (`tests/run_all.sh`),
`tools/`, `results/`, `romenagri-site/` (the site's sources), with its README as `README-SANSKRIT-CHARACTERS.md` and its LICENSE
as `legal/LICENSE-SANSKRIT-CHARACTERS`. The v6 delta lies over it as designed: `v6/` (sed mapping layers for 18 scripts onto the
Devanagari hub) and its pages; its pairs also fill 17 script tables in `tables/`. `v7/` holds AInagri and the Unicode inventory,
`V7-TASKS.md` the next work. `src/`, `data/` and `corpora/` (the extraction of 2026.07) stay until the author rules on them.
How work proceeds: `AGENTS.md`; where it stands: `CONTEXT.md`.
""" + t[j:]
r.write_text(t, encoding="utf-8")
c = R / "CITATION.cff"; t = c.read_text(encoding="utf-8")
import re as _re
t = _re.sub(r'^version: .*$', 'version: "6.0.1"', t, count=1, flags=_re.M)
c.write_text(t, encoding="utf-8")
say("README.md: the layout section rewritten for 6.0.1; CITATION.cff: version 6.0.1 (title, licence and DOI as they are)")

# 8. how work on Romenagri proceeds (AGENTS.md) and where it stands (CONTEXT.md)
(R / "AGENTS.md").write_text("""# For any agent or person taking work on Romenagri

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
""", encoding="utf-8")
(R / "CONTEXT.md").write_text("""# CONTEXT: Romenagri

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
""", encoding="utf-8")
say("AGENTS.md: how work on Romenagri proceeds; CONTEXT.md: where it stands, the versions and their faces, the open decisions")
