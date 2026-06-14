#!/usr/bin/env python3
"""rom2deva_heur — totalising Roman->Romenagri normaliser (front-end to the kernel).
Longest-prefix match (<=5 chars) over the canonical Romenagri token inventory extracted
from acii.h, with fallback rules for arbitrary Latin runs (alphabet limits). Output is valid
Romenagri, fed to the unchanged kernel (rmn2acii) to reach Devanagari.
(C) 1993-2026 Abhishek Choudhary, GPL-3.0-or-later"""
import re,sys,os
ACII=os.environ.get("ACII_H", os.path.join(os.path.dirname(__file__),"..","bindings","c","acii.h"))
TOKENS=set(a for a,b in re.findall(r'\{"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\}',open(ACII,encoding="latin1").read()) if a)
MAXLEN=max((len(t) for t in TOKENS),default=5)
FALLBACK={'x':'kxa','q':'ka','f':'pha','z':'za','c':'ka','w':'wa','y':'ya',
 'sh':'sha','ch':'cha','th':'_tha','ph':'pha','bh':'bha','gh':'gha','dh':'_dha','kh':'kha',
 'ee':'^ee','aa':'^aa','oo':'^oo','ai':'^ai','au':'^au'}
SV={'a':'_a','i':'^i','e':'^ee','o':'^oo','u':'^u'}
def normalise(s):
    out=[]; i=0; n=len(s)
    while i<n:
        m=None
        for Lh in range(min(MAXLEN,n-i),0,-1):
            if s[i:i+Lh] in TOKENS: m=s[i:i+Lh]; break
        if m: out.append(m); i+=len(m); continue
        if i+2<=n and s[i:i+2] in FALLBACK: out.append(FALLBACK[s[i:i+2]]); i+=2; continue
        c=s[i]
        if c in FALLBACK: out.append(FALLBACK[c]); i+=1; continue
        if c in SV: out.append(SV[c]); i+=1; continue
        if c.isalpha() and (c+'a') in TOKENS: out.append(c+'a'); i+=1; continue
        out.append(c); i+=1
    return "".join(out)
if __name__=="__main__":
    for line in sys.stdin:
        sys.stdout.write(normalise(line.rstrip("\n"))+"\n")
