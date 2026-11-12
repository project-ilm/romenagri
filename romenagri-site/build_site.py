#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Builds the site of romenagri-site/ from the headers of Romenagri/, and checks it.

    python3 romenagri-site/build_site.py                 writes docs/romenagri.js, docs/examples.js, docs/*.html and the notebook
    python3 romenagri-site/build_site.py --check         builds all of it in memory and compares it with the files on disk; checks the pages
                                                         (tags, anchors, links) and the notebook; then compares the JavaScript (docs/romenagri.js)
                                                         with the compiled C programs and with the Python models of tests/ on random and on
                                                         exhaustive inputs, and runs twelve deliberately broken copies of it to show that the
                                                         comparison notices (needs node)
    python3 romenagri-site/build_site.py --cbin DIR      use the compiled programs of DIR (a built Romenagri/ directory, for example
                                                         build/new/Romenagri) instead of compiling a copy of ../Romenagri in a temporary directory

Nothing on the pages is typed in by hand where it can be read from the package: the tables of the JavaScript are the rows of unicode.h,
acii.h and nukta.h; every output shown on the pages and in the notebook was written by the compiled C programs when the site was built.
Needs: python3, gcc, make, flex (+ libfl) for the C programs; node for --check.
"""
import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import itertools  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import random  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import struct  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402
from html.parser import HTMLParser  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, "src")
DOCS = os.path.join(HERE, "docs")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tests"))
import rmn_tables as T  # noqa: E402
import site_pages as P  # noqa: E402

FORMS = ("asis", "nfc", "nfd")
STATIC_DOCS = ("style.css", "demo.js")     # written by hand, not generated


# ----------------------------------------------------------------------------------------------------------------------------
# the tables
# ----------------------------------------------------------------------------------------------------------------------------
def load_tables(rdir=None):
    d = rdir or os.path.join(ROOT, "Romenagri")
    n_uni, uni = T.parse_unicode(d)
    n_acii, acii = T.parse_acii(d)
    n_hin, hin = T.parse_hin(d)
    n_nukta, nukta_byte, default_form, nukta = T.parse_nukta(d)
    assert n_uni == len(uni) and n_acii == len(acii) and n_hin == len(hin) and n_nukta == len(nukta) == 11, "the headers are not what this script reads"
    return dict(uni=uni, acii=acii, hin=hin, nukta=nukta, nukta_byte=nukta_byte, default_form=default_form)


def render_js(tb):
    src = open(os.path.join(SRC, "romenagri.js.in"), encoding="utf-8").read()
    uni = json.dumps([[cp, b] for cp, b in tb["uni"]], separators=(",", ":"))
    nukta = json.dumps([[a, b, c] for a, b, c in tb["nukta"]], separators=(",", ":"))
    acii = json.dumps([[k, list(v)] for k, v in tb["acii"]], separators=(",", ":"), ensure_ascii=True)
    for token, value in (("__UNI__", uni), ("__NUKTA__", nukta), ("__ACII__", acii), ("__NUKTA_BYTE__", str(tb["nukta_byte"])),
                         ("__DEFAULT_FORM__", str(tb["default_form"]))):
        assert token in src, token
        src = src.replace(token, value)
    return src


# ----------------------------------------------------------------------------------------------------------------------------
# the compiled C programs
# ----------------------------------------------------------------------------------------------------------------------------
class Programs:
    """The compiled converters of a built Romenagri/ directory.  Bytes in, bytes out."""

    def __init__(self, d):
        self.d = d

    def run(self, prog, data, args=(), env=None, timeout=60):
        e = {k: v for k, v in os.environ.items() if not k.startswith("ROMENAGRI_NUKTA_")}
        e.update(env or {})
        p = subprocess.run([os.path.join(self.d, prog)] + list(args), input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=e)
        return p.returncode, p.stdout, p.stderr

    def u2a(self, units, form, warn=False):
        """units: a list of UTF-16 code units; form: a name, or None for the default of the build.  Returns (bytes, [stderr lines])."""
        data = b"\xff\xfe" + struct.pack("<%dH" % len(units), *units)
        args = (["-f", form] if form else []) + (["-w"] if warn else [])
        rc, out, err = self.run("uni2acii", data, args)
        assert rc == 0, ("uni2acii", rc, err)
        return out, err.decode("utf-8").splitlines()

    def a2u(self, data, form):
        """Returns the code units (a list), without the byte order mark."""
        rc, out, _ = self.run("acii2uni", bytes(data), ["-f", form] if form else [])
        assert rc == 0 and out[:2] == b"\xff\xfe", ("acii2uni", rc)
        return list(struct.unpack("<%dH" % ((len(out) - 2) // 2), out[2:]))

    def a2r(self, data):
        """Returns ("text", bytes) or ("crash", returncode)."""
        rc, out, _ = self.run("acii2rmn", bytes(data))
        return ("text", out) if rc == 0 else ("crash", rc)

    def r2a(self, data):
        rc, out, _ = self.run("rmn2acii", bytes(data))
        return ("bytes", out) if rc == 0 else ("crash", rc)


def build_c(workdir):
    """Compiles a copy of ../Romenagri in workdir; returns Programs."""
    dst = os.path.join(workdir, "Romenagri")
    shutil.copytree(os.path.join(ROOT, "Romenagri"), dst)
    for f in os.listdir(dst):
        if f.endswith(".o") or f in ("librmnagri.a", "lexyy.c"):
            os.remove(os.path.join(dst, f))
    p = subprocess.run(["make", "all"], cwd=dst, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p.returncode != 0:
        sys.exit("make all failed in the copy of Romenagri/:\n" + p.stdout.decode("utf-8", "replace")[-2000:])
    for prog in ("uni2acii", "acii2uni", "acii2rmn", "rmn2acii"):
        if not os.path.exists(os.path.join(dst, prog)):
            sys.exit("the build made no " + prog)
    return Programs(dst)


# ----------------------------------------------------------------------------------------------------------------------------
# everything that the build writes
# ----------------------------------------------------------------------------------------------------------------------------
def build_outputs(tb, c, tmp):
    """{path relative to romenagri-site/: bytes}.  The pages and the notebook come from runs of the C programs of c."""
    out = {"docs/romenagri.js": render_js(tb), "docs/examples.js": P.examples_js(), "docs/.nojekyll": ""}
    for name, html in P.render_pages(tb, c).items():
        out["docs/" + name] = html
    nbdir = os.path.join(tmp, "nb")
    os.makedirs(nbdir, exist_ok=True)
    nb = P.notebook_text(P.run_notebook(c.d, nbdir))
    out["docs/" + P.NBNAME] = nb
    out["notebooks/" + P.NBNAME] = nb
    return {k: (v.encode("utf-8") if isinstance(v, str) else v) for k, v in out.items()}


def write_outputs(outputs):
    for rel, data in sorted(outputs.items()):
        path = os.path.join(HERE, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        print("  wrote %s (%d bytes)" % (rel, len(data)))


# ----------------------------------------------------------------------------------------------------------------------------
# checking
# ----------------------------------------------------------------------------------------------------------------------------
class Check:
    def __init__(self):
        self.failed = False
        self.n = 0

    def row(self, what, n, bad, examples=(), unit="cases"):
        ok = bad == 0
        self.failed |= not ok
        self.n += 1
        print("  %-104s %8s %s, %d disagreements  %s" % (what, "{:,}".format(n), unit, bad, "ok" if ok else "FAIL"))
        for e in list(examples)[:3]:
            print("      e.g. " + str(e)[:300])

    def line(self, what, ok, detail=""):
        self.failed |= not ok
        self.n += 1
        print("  %-104s %s%s" % (what, "ok" if ok else "FAIL", ("  " + detail) if detail else ""))


def node_path():
    n = shutil.which("node") or shutil.which("nodejs")
    if not n:
        sys.exit("--check needs node (the JavaScript is run with it)")
    return n


def run_js(cases, jspath):
    """Runs the cases (a list of dicts) through the JavaScript file jspath in one node process; returns the list of results."""
    p = subprocess.run([node_path(), os.path.join(SRC, "check_js.js"), jspath], input=json.dumps(cases).encode("utf-8"),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        sys.exit("node failed:\n" + p.stderr.decode("utf-8", "replace")[-2000:])
    return json.loads(p.stdout.decode("utf-8"))


def rand_units(rnd, pool, n):
    return [rnd.choice(pool) for _ in range(rnd.randint(0, n))]


class Category:
    """cases for the JavaScript, what the C programs (or a Python model) say about each, and how to compare."""

    def __init__(self, label, cases, want, agree):
        self.label, self.cases, self.want, self.agree = label, cases, want, agree


def build_suite(c, tb):
    """The cases and the expected results.  The C programs and the models are run here, once; the JavaScript is run against them later."""
    import handwritten_parser
    import model

    rnd = random.Random(20261109)
    nukta_cp = [r[0] for r in tb["nukta"]]
    uni_cp = [cp for cp, _ in tb["uni"]]
    pool_u = (uni_cp + nukta_cp * 6 + [0x093C] * 12 + [0x094D] * 4 + [0x0928, 0x0930, 0x0933] * 6 +
              [0x00E9, 0x00C6, 0x00D0, 0x0100, 0x2019, 0x200C, 0x200D, 0xD83D, 0xDE00, 0xFEFF, 0x0D, 0x0A, 0x20, 0x41, 0x7A, 0x30, 0x0964, 0x0965] * 2)
    pool_b = ([b for _, b in tb["uni"]] * 2 + [0xE9] * 30 + [0xC6, 0xCF, 0xD2, 0xC7, 0xD0] * 8 + [0xE8] * 6 +
              [0x0A, 0x20, 0x41, 0x61, 0x5F, 0x31, 0xEF, 0x80, 0xFF, 0x00] + list(range(256)))
    suite = []

    # uni2acii: every form and the default of the build, with and without the warning layer
    cases = []
    for form in FORMS + (None,):
        for warn in (False, True):
            for _ in range(700 if form else 350):
                cases.append(dict(fn="uni2acii", units=rand_units(rnd, pool_u, 30), form=form, warn=warn))
    want = [c.u2a(cs["units"], cs["form"], cs["warn"]) for cs in cases]
    suite.append(Category("uni2acii (3 forms and the default, with and without -w): the bytes and the lines written on stderr", cases, want,
                          lambda cs, w, g: list(w[0]) == g["bytes"] and w[1] == g["warnings"]))

    # acii2uni
    cases = [dict(fn="acii2uni", bytes=[rnd.choice(pool_b) for _ in range(rnd.randint(0, 30))], form=form) for form in FORMS + (None,)
             for _ in range(700 if form else 350)]
    want = [c.a2u(cs["bytes"], cs["form"]) for cs in cases]
    suite.append(Category("acii2uni (3 forms and the default): the code units", cases, want, lambda cs, w, g: w == [ord(ch) for ch in g["text"]]))

    # acii2rmn against the compiled filter
    rows = T.parse_acii(os.path.join(ROOT, "Romenagri"))[1]
    cases = [dict(fn="acii2rmn", bytes=[rnd.choice(pool_b) for _ in range(rnd.randint(1, 14))]) for _ in range(3000)]
    want = [c.a2r(cs["bytes"]) for cs in cases]
    suite.append(Category("acii2rmn against the compiled filter (a crash on an empty stack included)", cases, want,
                          lambda cs, w, g: (w[0] == "crash") if "crash" in g else (w[0] == "text" and w[1] == g["text"].encode("latin-1"))))

    # rmn2acii against the compiled filter
    letters = "abcdeghijklmnoprstuvwxyz_"
    pool_r = list(letters) * 2 + list("nmywxr") * 3 + ["_r", "_rr", "_rd", "lv", "vr", "ch", "kh", "gh", "_ha", "_om", "_li", "_lee", "_ree", "_vd", "_vu", "z", "^"] * 2
    cases = []
    for _ in range(3500):
        s = "".join(rnd.choice(pool_r) for _ in range(rnd.randint(1, 7)))
        if rnd.random() < 0.15:
            s += rnd.choice([" ", "1", ",", ".", " ka", '"e_ab"'])
        cases.append(dict(fn="rmn2acii", text=s))
    want = [c.r2a(cs["text"].encode("latin-1")) for cs in cases]
    suite.append(Category("rmn2acii against the compiled filter (a key that the table lacks is a crash)", cases, want,
                          lambda cs, w, g: (w[0] == "crash") if "crash" in g else (w[0] == "bytes" and w[1] == bytes(g["bytes"]))))

    # the whole chain
    cases = [dict(fn="chain", units=rand_units(rnd, pool_u, 14), form=form) for form in FORMS for _ in range(450)]
    pool_c = [0x0928, 0x0915, 0x0921, 0x094D, 0x093C, 0x094D, 0x093C, 0x0939, 0x0020, 0x0941, 0x095C, 0x0934]      # a halant and a nukta, near each other
    cases += [dict(fn="chain", units=[rnd.choice(pool_c) for _ in range(rnd.randint(1, 6))], form=form) for form in FORMS for _ in range(300)]
    want = []
    for cs in cases:
        a, _ = c.u2a(cs["units"], cs["form"])
        k1, v1 = c.a2r(a)
        if k1 == "crash":
            want.append({"crash": "acii2rmn"})
        else:
            k2, v2 = c.r2a(v1)
            want.append({"crash": "rmn2acii"} if k2 == "crash" else {"units": c.a2u(v2, cs["form"])})
    suite.append(Category("the chain, Unicode to ACII to Romenagri to ACII to Unicode (3 forms; where it stops: the same program)", cases, want,
                          lambda cs, w, g: w == ({"crash": g["crash"]} if "crash" in g else {"units": [ord(ch) for ch in g["text"]]})))

    # the decoder against the Python model of tests/model.py: every pair of bytes, and a family of triples
    cases = [dict(fn="acii2rmnTok", bytes=[x, y]) for x in range(1, 256) for y in range(1, 256) if x not in (10, 8, 34, 94) and y not in (10, 8, 34, 94)]
    cases += [dict(fn="acii2rmnTok", bytes=[x, y, z]) for x in (0xB3, 0xBF, 0xC6, 0xE8, 0xE9, 0xDA, 0xEF) for y in (0xE8, 0xE9, 0xBF, 0xC0, 0xC6, 0xDA, 0xEF, 0x41)
              for z in range(1, 256) if z not in (10, 8, 34, 94)]
    want = []
    for cs in cases:
        try:
            want.append(model.model_encode(bytes(cs["bytes"]), rows))
        except model.Crash:
            want.append(None)
    suite.append(Category("the decoder against the Python model of tests/model.py: every pair of bytes, and 7 x 8 x 251 triples", cases, want,
                          lambda cs, w, g: w == (None if "crash" in g else g["text"])))

    # the parser against the hand-written parser of tests/: every short string, and random long ones
    tbl = T.key_table(tb["acii"])
    alpha = "abcdghijklmnoprstuvwxz_"
    cases = [dict(fn="rmn2aciiRun", text="".join(t)) for n in range(1, 5) for t in itertools.product(alpha, repeat=n)]
    cases += [dict(fn="rmn2aciiRun", text="".join(rnd.choice(pool_r) for _ in range(rnd.randint(5, 12)))) for _ in range(20000)]
    want = []
    for cs in cases:
        try:
            want.append(list(handwritten_parser.handwritten_parse(cs["text"], tbl, new=True)))
        except model.Missing:
            want.append(None)
    suite.append(Category("the parser against the hand-written parser of tests/: every string of up to 4 letters over 23 letters, and 20,000 longer ones",
                          cases, want, lambda cs, w, g: w == (None if "crash" in g else g["bytes"])))
    return suite


def run_suite(suite, jspath, stop_at_first=False):
    """[(label, n cases, n disagreements, examples)]; with stop_at_first, ends after the first category that has one."""
    results = []
    for cat in suite:
        got = run_js(cat.cases, jspath)
        bad = [(cs, w, g) for cs, w, g in zip(cat.cases, cat.want, got) if not cat.agree(cs, w, g)]
        results.append((cat.label, len(cat.cases), len(bad), bad[:3]))
        if stop_at_first and bad:
            break
    return results


# the JavaScript with one deliberate fault each: the comparison above has to notice every one of them
def _sub(old, new):
    def f(s):
        assert s.count(old) == 1, ("the mutation does not apply once", old, s.count(old))
        return s.replace(old, new)
    return f


def _resub(pattern, repl):
    def f(s):
        t, n = re.subn(pattern, repl, s, count=1)
        assert n == 1, ("the mutation does not apply", pattern)
        return t
    return f


MUTATIONS = [
    ("uni2acii: the rule is dropped (a letter that has no row is written as its low byte again)",
     _sub("if (j >= 0 && (row === undefined || form === 2)) {", "if (j >= 0 && form === 2) {")),
    ("uni2acii, form nfc: a consonant and a nukta are not joined", _sub("if (u === NUKTA_SIGN) { out.push(JOIN[held]);", "if (false) { out.push(JOIN[held]);")),
    ("uni2acii: the warning layer reports every occurrence, not each code point once", _sub("if (seen[u]) { repeated++; return; }", "if (false) { repeated++; return; }")),
    ("uni2acii: the warning layer reports ASCII characters too", _sub("(u > 255 || (u & 255) > 127)", "true")),
    ("the default form is nfc, not asis", _sub("var DEFAULT_FORM = 0;", "var DEFAULT_FORM = 1;")),
    ("acii2uni, form nfd: C7 and D0 are not written as pairs", _sub("if (form === 2 && j >= 0) {", "if (false) {")),
    ("acii2uni: a line feed is not written as CR LF", _sub("if (t === 10) { out.push(13, 10); continue; }", "if (t === 10) { out.push(10); continue; }")),
    ("acii2rmn: DA and a nukta is not _rda", _sub('else if (t1 === "d") pushAll("_rda");', 'else if (t1 === "d") pushAll("dza");')),
    ("acii2rmn: the last row with the byte is taken, not the first", _sub("{ hit = j; break; }", "{ hit = j; }")),
    ("acii2rmn: a nukta on an empty stack does not stop", _sub("if (stack.length === 0) throw {", "if (false) throw {")),
    ("rmn2acii: the guard of the letter c is gone", _resub(r"if \(noPartner\(at\(i \+ 1\)\)\) (\{ raw\(c\); level1\(i \+ 1\); \}\s+/\* guard: a 'c')", r"if (false) \1")),
    ("rmn2acii: vocalic does not replace a halant", _sub("if (lastIsHalant()) { out.pop(); lk(dep); } else lk(indep);", "lk(indep);")),
]


def controls(suite, tb, tmp, ck):
    print("deliberately broken copies of the JavaScript (each has to be caught by the comparison above)")
    base = render_js(tb)
    for i, (label, mutate) in enumerate(MUTATIONS):
        d = os.path.join(tmp, "mutant%02d" % i)
        os.makedirs(d)
        path = os.path.join(d, "romenagri.js")
        open(path, "w", encoding="utf-8").write(mutate(base))
        res = run_suite(suite, path, stop_at_first=True)
        caught = [r for r in res if r[2] > 0]
        ck.line(label, bool(caught), ("caught by: %s (%d disagreements)" % (caught[0][0].split(":")[0].split(" (")[0], caught[0][2])) if caught else "NOT CAUGHT")


def coverage(suite, tb, ck):
    """How much of the interesting ground the cases cover: a population that never reaches a path proves nothing about it."""
    print("what the cases reach")
    by = {cat.label.split(" ")[0]: cat for cat in suite}
    u = suite[0]
    letters = [r[0] for r in tb["nukta"]]
    fewest = min(sum(1 for cs in u.cases if l in cs["units"]) for l in letters)
    ck.line("uni2acii cases that contain a letter with a nukta: the fewest, over the eleven letters", fewest >= 40, "%d" % fewest)
    joined = sum(1 for cs in u.cases if cs["form"] == "nfc" and any(a in (0x0928, 0x0930) and b == 0x093C for a, b in zip(cs["units"], cs["units"][1:])))
    ck.line("uni2acii cases, form nfc, with na or ra directly before a nukta (the byte that waits)", joined >= 20, "%d" % joined)
    warned = sum(1 for cs, w in zip(u.cases, u.want) if cs["warn"] and w[1])
    ck.line("uni2acii cases in which the warning layer wrote something", warned >= 200, "%d" % warned)
    a = suite[1]
    fold = sum(1 for cs in a.cases if cs["form"] == "nfc" and any(x in (0xC6, 0xCF, 0xD2) and y == 0xE9 for x, y in zip(cs["bytes"], cs["bytes"][1:])))
    ck.line("acii2uni cases, form nfc, with C6, CF or D2 directly before E9", fold >= 20, "%d" % fold)
    nfd = sum(1 for cs in a.cases if cs["form"] == "nfd" and (0xC7 in cs["bytes"] or 0xD0 in cs["bytes"]))
    ck.line("acii2uni cases, form nfd, with C7 or D0", nfd >= 100, "%d" % nfd)
    r = suite[2]
    cr = sum(1 for w in r.want if w[0] == "crash")
    ck.line("acii2rmn cases on which the C program crashes (and the JavaScript with it)", cr >= 50, "%d" % cr)
    r2 = suite[3]
    cr2 = sum(1 for w in r2.want if w[0] == "crash")
    ck.line("rmn2acii cases on which the C program crashes (and the JavaScript with it)", cr2 >= 50, "%d" % cr2)
    ch = suite[4]
    ends = {"acii2rmn": 0, "rmn2acii": 0, "complete": 0}
    for w in ch.want:
        ends[w["crash"] if "crash" in w else "complete"] += 1
    ck.line("chain cases: stop in acii2rmn, stop in rmn2acii (none can: no missing key is decoded), complete",
            ends["acii2rmn"] >= 30 and ends["complete"] >= 30, "%d, %d, %d" % (ends["acii2rmn"], ends["rmn2acii"], ends["complete"]))


def differential(suite, ck):
    print("the JavaScript (docs/romenagri.js) against the C programs and the models")
    for label, n, bad, ex in run_suite(suite, os.path.join(DOCS, "romenagri.js")):
        ck.row(label, n, bad, ex)


# ----------------------------------------------------------------------------------------------------------------------------
# the pages and the notebook
# ----------------------------------------------------------------------------------------------------------------------------
class Page(HTMLParser):
    VOID = {"meta", "link", "br", "hr", "img", "input", "area", "base", "col", "source", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.hrefs, self.srcs, self.errors, self.title = [], [], [], [], [], None
        self._in_title = False
        self.lang = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])
        if tag == "link" and a.get("href"):
            self.hrefs.append(a["href"])
        if tag == "script" and a.get("src"):
            self.srcs.append(a["src"])
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self._in_title = True
            self.title = ""
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in self.VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append("</%s> where %s is open" % (tag, self.stack[-1] if self.stack else "nothing"))
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
            return
        self.stack.pop()

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def check_pages(outputs, ck):
    print("the pages: tags, anchors, links")
    names = sorted(k[5:] for k in outputs if k.endswith(".html"))
    parsed = {}
    for name in names:
        text = outputs["docs/" + name].decode("utf-8")
        p = Page()
        p.feed(text)
        p.close()
        parsed[name] = p
        problems = list(p.errors)
        if p.stack:
            problems.append("not closed: " + ", ".join(p.stack))
        dup = sorted({i for i in p.ids if p.ids.count(i) > 1})
        if dup:
            problems.append("an id twice: " + ", ".join(dup))
        if "{{" in text or "}}" in text:
            problems.append("a placeholder is left")
        if p.lang != "en" or not p.title or 'name="viewport"' not in text:
            problems.append("lang, title or viewport is missing")
        ck.line("%s: well-formed, ids unique, no placeholder left, lang, title, viewport" % name, not problems, "; ".join(problems)[:200])
    known = set(parsed) | {k[5:] for k in outputs if k.startswith("docs/")} | set(STATIC_DOCS)
    bad = []
    for name, p in parsed.items():
        for ref in p.hrefs + p.srcs:
            if re.match(r"^(https?:|mailto:|data:)", ref):
                continue
            page, _, frag = ref.partition("#")
            page = page or name
            if page not in known:
                bad.append("%s -> %s (no such file)" % (name, ref))
            elif frag and (page not in parsed or frag not in parsed[page].ids):
                bad.append("%s -> %s (no such anchor)" % (name, ref))
    ck.line("every link and script of the five pages leads to a file or an anchor that exists", not bad, "; ".join(bad)[:300])


def validate_notebook(doc, ck):
    ok = (doc.get("nbformat") == 4 and isinstance(doc.get("cells"), list) and "metadata" in doc and doc.get("nbformat_minor", 0) >= 5)
    ids = set()
    for cell in doc["cells"]:
        ok &= cell.get("cell_type") in ("markdown", "code") and isinstance(cell.get("source"), list) and "metadata" in cell
        ok &= cell.get("id") not in ids and bool(re.match(r"^[a-zA-Z0-9_-]{1,64}$", cell.get("id", "")))
        ids.add(cell.get("id"))
        if cell.get("cell_type") == "code":
            ok &= "execution_count" in cell and isinstance(cell.get("outputs"), list)
    detail = "structure"
    try:
        import nbformat
        nb = nbformat.reads(json.dumps(doc), as_version=4)
        nbformat.validate(nb)
        detail = "structure, and nbformat.validate"
    except ImportError:
        detail += " (nbformat is not installed: not validated with it)"
    except Exception as e:  # noqa: BLE001
        ok = False
        detail = "nbformat: %s" % str(e)[:150]
    ck.line("the notebook is a valid nbformat 4 document", ok, detail)


def check_outputs(outputs, ck):
    print("the files on disk against a new build")
    stale = []
    for rel, data in sorted(outputs.items()):
        path = os.path.join(HERE, rel)
        if not os.path.exists(path) or open(path, "rb").read() != data:
            stale.append(rel)
    ck.line("%d generated files are what the build gives now" % len(outputs), not stale, ("out of date or missing: " + ", ".join(stale)) if stale else "")
    extra = sorted(set(os.listdir(DOCS)) - {k[5:] for k in outputs if k.startswith("docs/")} - set(STATIC_DOCS))
    ck.line("docs/ holds only the generated files and %s" % " and ".join(STATIC_DOCS), not extra, ("also: " + ", ".join(extra)) if extra else "")
    for need in STATIC_DOCS:
        ck.line("docs/%s exists and carries the copyright line" % need,
                os.path.exists(os.path.join(DOCS, need)) and "Copyright (C) 1993-2026 Abhishek Choudhary" in open(os.path.join(DOCS, need), encoding="utf-8").read())
    js = outputs["docs/romenagri.js"].decode("utf-8")
    ck.line("docs/romenagri.js says that it is generated and that it is not the production code", "GENERATED by romenagri-site/build_site.py" in js and "It is not the production code" in js)
    return stale


# ----------------------------------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--cbin", help="a built Romenagri/ directory")
    args = ap.parse_args()
    tmp = tempfile.mkdtemp(prefix="romenagri-site-")
    try:
        tb = load_tables()
        c = Programs(os.path.abspath(args.cbin)) if args.cbin else build_c(tmp)
        outputs = build_outputs(tb, c, tmp)
        if not args.check:
            os.makedirs(DOCS, exist_ok=True)
            os.makedirs(os.path.join(HERE, "notebooks"), exist_ok=True)
            write_outputs(outputs)
            return 0
        ck = Check()
        print("romenagri-site/build_site.py --check")
        check_outputs(outputs, ck)
        check_pages(outputs, ck)
        validate_notebook(json.loads(outputs["notebooks/" + P.NBNAME].decode("utf-8")), ck)
        suite = build_suite(c, tb)
        differential(suite, ck)
        coverage(suite, tb, ck)
        controls(suite, tb, tmp, ck)
        print("%d checks, %s" % (ck.n, "FAILED" if ck.failed else "all ok"))
        return 1 if ck.failed else 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
