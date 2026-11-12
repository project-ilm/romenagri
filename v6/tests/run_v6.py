#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
"""v6: reversibility of the mapping layers. T1 = script -> Devanagari -> script; T2 = through the zip 5 core as a black box (its suites are not run).
usage: run_v6.py <v6 dir> <Romenagri dir of zip 5 (sources, for corpora and Urdu filters)> <built core dir> <out json>"""
import csv, json, os, subprocess, sys
V6, RS, CORE, OUT = sys.argv[1:5]
sys.path.insert(0, V6 + "/tools"); import gen_fltr
E = {"LC_ALL": "C.UTF-8", "PATH": os.environ["PATH"]}

def sh(path, text, shell="sh"):
    return subprocess.run([shell, path], input=text.encode(), stdout=subprocess.PIPE, env=E, timeout=300).stdout.decode()
def core(prog, data, args=()):
    p = subprocess.run([CORE + "/" + prog] + list(args), input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
    return p.returncode, p.stdout
def via_core_lines(lines):
    """Devanagari lines -> Devanagari lines through uni2acii, acii2rmn, rmn2acii, acii2uni (default form). Line by line; None if the core fails."""
    out = []
    for l in lines:
        r = core("uni2acii", b"\xff\xfe" + l.encode("utf-16-le"))
        if r[0]: out.append(None); continue
        r = core("acii2rmn", r[1])
        if r[0]: out.append(None); continue
        r = core("rmn2acii", r[1])
        if r[0]: out.append(None); continue
        r = core("acii2uni", r[1])
        out.append(None if r[0] else r[1].decode("utf-16", "replace").replace("\r\n", "\n").rstrip("\n"))
    return out
def pct(a, b): return round(100.0 * a / b, 2) if b else None

def one(code, prefix, tier, rep, pairs):
    f = "%s/Romenagri/fltr_%s_hi" % (V6, code); b = "%s/Romenagri/fltr_hi_%s" % (V6, code)
    chars = [chr(c) for c in rep]
    fw = sh(f, "\n".join(chars)).split("\n"); bk = sh(b, "\n".join(fw)).split("\n")
    mapped = [i for i, c in enumerate(rep) if c in pairs]
    t1 = [i for i in range(len(rep)) if bk[i] == chars[i] and rep[i] in pairs]
    tgt = {}
    for c, (d, _) in pairs.items(): tgt.setdefault(d, []).append(c)
    coll = {chr(d): [chr(c) for c in cs] for d, cs in tgt.items() if len(cs) > 1}
    import unicodedata
    ka = next((chr(c) for c in rep if unicodedata.name(chr(c)).endswith("LETTER KA")), "")
    probes = [(ka + chars[i]) if (unicodedata.category(chars[i]).startswith("M") and ka) else chars[i] for i in mapped]   # a sign is probed on a base letter
    pdev = sh(f, "\n".join(probes)).split("\n"); cr = via_core_lines(pdev)
    ok2 = 0; lim = []; maploss = []
    for k, i in enumerate(mapped):
        if bk[i] != chars[i]: maploss.append(chars[i]); continue
        if cr[k] is not None and sh(b, cr[k]).rstrip("\n") == probes[k]: ok2 += 1
        else: lim.append(chars[i])
    res = {"script": prefix, "code": code, "tier": tier, "repertoire": len(rep), "mapped": len(mapped), "coverage_pct": pct(len(mapped), len(rep)),
           "T1_reversible": len(t1), "T1_pct": pct(len(t1), len(rep)), "T1_pct_of_mapped": pct(len(t1), len(mapped)),
           "T2_reversible": ok2, "T2_pct": pct(ok2, len(rep)), "T2_pct_of_mapped": pct(ok2, len(mapped)),
           "collisions": coll, "core_limit": lim, "lost_by_mapping": maploss,
           "unmapped": [chars[i] for i in range(len(rep)) if rep[i] not in pairs]}
    return res

def corpus(code, name, n=1500):
    p = RS + "/" + name
    if not os.path.exists(p): return None
    lines = [l.rstrip("\n") for l in open(p, encoding="utf-8", errors="replace") if l.strip()][:n]
    f = "%s/Romenagri/fltr_%s_hi" % (V6, code); b = "%s/Romenagri/fltr_hi_%s" % (V6, code)
    dev = sh(f, "\n".join(lines)).split("\n"); back = sh(b, "\n".join(dev)).split("\n")
    t1 = sum(1 for a, c in zip(lines, back) if a == c)
    cr = via_core_lines(dev); t2 = sum(1 for a, c in zip(lines, cr) if c is not None and sh(b, c).rstrip("\n") == a)
    return {"file": name, "lines": len(lines), "T1_line_pct": pct(t1, len(lines)), "T2_line_pct": pct(t2, len(lines))}

def perso():
    out = {}
    fu = RS + "/fltr_ur_hi"; fh = RS + "/fltr_hi_ur"
    letters = [l.strip() for l in open(RS + "/alpha_urdu.txt", encoding="utf-8") if l.strip()]
    chars = sorted({c for l in letters for c in l if 0x600 <= ord(c) <= 0x6FF})
    dev = sh(fu, "\n".join(chars), "bash").split("\n"); back = sh(fh, "\n".join(dev), "bash").split("\n")
    okc = [c for c, bk in zip(chars, back) if bk == c]
    lines = [l.rstrip("\n") for l in open(RS + "/corp_ur.txt", encoding="utf-8", errors="replace") if l.strip()][:1500]
    d2 = sh(fu, "\n".join(lines), "bash").split("\n"); b2 = sh(fh, "\n".join(d2), "bash").split("\n")
    t1 = sum(1 for a, c in zip(lines, b2) if a == c)
    cr = via_core_lines(d2); t2 = sum(1 for a, c, d in zip(lines, cr, d2) if c is not None and sh(fh, c, "bash").rstrip("\n") == a)
    out["urdu"] = {"letters_in_alpha_urdu": len(chars), "T1_char_reversible": len(okc), "T1_char_pct": pct(len(okc), len(chars)), "not_reversible": [c for c in chars if c not in okc],
                   "corpus_lines": len(lines), "T1_line_pct": pct(t1, len(lines)), "T2_line_pct": pct(t2, len(lines))}
    for name, ex in (("sindhi", "ٻڀٺٽٿڦڄڃڇڍڊڏڌڙڻڱڳڪھ"), ("shahmukhi", "ٹڈڑںھݨ")):
        img = sh(fu, "\n".join(ex), "bash").split("\n")
        out[name] = {"extra_letters": len(ex), "with_devanagari_image": sum(1 for a, b in zip(ex, img) if a != b), "no_image": [a for a, b in zip(ex, img) if a == b]}
    return out

res = gen_fltr.build(RS); R = {"scripts": {}, "perso": perso()}
CORP = {"bn": "corp_bn.txt", "pa": "corp_pb.txt", "te": "corp_te.txt"}
for code, (prefix, tier, rep, pairs) in res.items():
    r = one(code, prefix, tier, rep, pairs)
    if code in CORP: r["corpus"] = corpus(code, CORP[code])
    R["scripts"][code] = r
    print(code, prefix, r["coverage_pct"], r["T1_pct"], r["T2_pct"], flush=True)
json.dump(R, open(OUT, "w"), ensure_ascii=False, indent=1)
print(json.dumps(R["perso"], ensure_ascii=False)[:600])
