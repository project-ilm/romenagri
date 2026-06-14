#!/usr/bin/env python3
"""langspec_gen — turn a keyword CSV into a localized programming-language standard + verified C.
CSV columns: construct,native_keyword,romenagri    (header required)
  construct      = the canonical ontology id (maps to C/Python/VHDL/... ; semantics preserved)
  native_keyword = the word in the user's language / dialect / idiolect (any script)
  romenagri      = the reversible ASCII-7, C-identifier-legal surrogate
Outputs: STANDARD_<name>.md and (optionally) a compile-checked C file.
Localization of EXISTING standards (ISO/IEC 9899, 14882, IEEE 1800/1076, ...), not re-authorship.
(C) 1993-2026 Abhishek Choudhary, GPL-3.0-or-later"""
import sys,csv,os,subprocess,json
# canonical construct -> the standards it localizes into (sample; the ontology is the invariant)
ONTOLOGY={
 "if":{"c":"if","python":"if","vhdl":"if","verilog":"if","rust":"if","go":"if","iso":"ISO/IEC 9899 §6.8.4.1"},
 "else":{"c":"else","python":"else","vhdl":"else","rust":"else","iso":"ISO/IEC 9899 §6.8.4.1"},
 "while":{"c":"while","python":"while","vhdl":"while","rust":"while","iso":"ISO/IEC 9899 §6.8.5.1"},
 "for":{"c":"for","python":"for","vhdl":"for","rust":"for","iso":"ISO/IEC 9899 §6.8.5.3"},
 "return":{"c":"return","python":"return","rust":"return","iso":"ISO/IEC 9899 §6.8.6.4"},
 "int":{"c":"int","rust":"i32","iso":"ISO/IEC 9899 §6.7.2"},
 "void":{"c":"void","iso":"ISO/IEC 9899 §6.7.2"},
 "printf":{"c":"printf","iso":"ISO/IEC 9899 §7.21.6.3"},
 "break":{"c":"break","iso":"ISO/IEC 9899 §6.8.6.3"},
 "main":{"c":"main","iso":"ISO/IEC 9899 §5.1.2.2.1"},
}
def load(path):
    rows=[]
    for r in csv.DictReader(open(path,encoding="utf-8")):
        if r.get("construct"): rows.append({k:(v or "").strip() for k,v in r.items()})
    return rows
def standard_md(name,rows,meta):
    o=[f"# Programming-language standard — {name}",
       f"\n*Localization of existing standards (ISO/IEC 9899, 14882, IEEE 1800/1076, …) — not re-authorship.*",
       f"\nScript/locale: {meta.get('script','?')} · register: {meta.get('register','idiolect')} · "
       f"(C) 1993–2026 Abhishek Choudhary, GPL.\n",
       "| construct | this language | Romenagri (ASCII-7) | C | localizes |",
       "|---|---|---|---|---|"]
    for r in rows:
        c=r["construct"]; ont=ONTOLOGY.get(c,{})
        o.append(f"| `{c}` | {r['native_keyword']} | `{r['romenagri']}` | `{ont.get('c',c)}` | {ont.get('iso','—')} |")
    o.append("\n**Semantics are preserved**: each row maps a surface keyword onto the canonical construct; "
             "the execution target (GCC today, neuromorphic tomorrow) never sees the linguistic layer.\n")
    return "\n".join(o)
def verify_c(name,rows,outdir):
    kw={r["construct"]:r["romenagri"] for r in rows if r["romenagri"]}
    need=["if","while","return","int","printf"]
    use={k:kw[k] for k in need if k in kw and kw[k].isidentifier()}
    if len(use)<4: return {"compiled":"SKIP","reason":f"only {len(use)} C-legal core constructs"}
    defs="\n".join(f"#define {use[k]} {k}" for k in use if use[k]!=k)
    prog=f"""/* {name}: native-language keywords via Romenagri ASCII-7 identifiers -> unmodified GCC */
#include <stdio.h>
{defs}
{use.get('int','int')} main(void){{
  {use.get('int','int')} n=0;
  {use['while']}(n<3){{ {use['if']}(n%2==0) {use['printf']}("%d ok\\n",n); n++; }}
  {use['return']} 0;
}}
"""
    src=os.path.join(outdir,f"{name}.c"); open(src,"w",encoding="utf-8").write(prog)
    binp=os.path.join(outdir,f"{name}.bin")
    p=subprocess.run(["gcc","-O2","-o",binp,src],capture_output=True)
    if p.returncode!=0: return {"compiled":"FAIL","src":os.path.basename(src)}
    q=subprocess.run([binp],capture_output=True,timeout=10)
    return {"compiled":"OK","ran":"OK" if q.stdout else "no-out","src":os.path.basename(src),"constructs":len(use)}
def generate(csvpath,name,meta,verify_dir=None):
    rows=load(csvpath); md=standard_md(name,rows,meta)
    v=verify_c(name,rows,verify_dir) if verify_dir else {"compiled":"n/a"}
    return rows,md,v
if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("csv"); ap.add_argument("--name",required=True)
    ap.add_argument("--script",default="?"); ap.add_argument("--register",default="idiolect")
    ap.add_argument("--out",default="."); ap.add_argument("--verify",default=None)
    a=ap.parse_args()
    rows,md,v=generate(a.csv,a.name,{"script":a.script,"register":a.register},a.verify)
    open(os.path.join(a.out,f"STANDARD_{a.name}.md"),"w",encoding="utf-8").write(md)
    print(json.dumps({"name":a.name,"constructs":len(rows),"verify":v}))
