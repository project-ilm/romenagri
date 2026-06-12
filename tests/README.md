# Romenagri — Test Suite Documentation

## Round-trip reversibility (the published invariant)

The core claim: φ(ρ(φ(w))) = φ(w) for all w in Σ_R (canonical fixed-point),
and ρ(φ(w)) = w for well-formed orthographic content (exact round-trip).

**Measured result (2003-04 kernel, exhaustive [a-z]^1..4, 475,254 strings):**
- Exact round-trip: 2.34%
- Normalized (stable canonical fixpoint): 53.26%
- **Reversible-or-canonical: 55.60%** (chintamani, post-guard)
- **Reversible-or-canonical: 98.68%** (2003-04 holy-grail kernel)
- Irreducible floor: 1.31% (2003-04 kernel)
- Crash class: 0.005% (all guarded)

This divergence between kernels is itself a finding: chintamani's reverse parser
is a regression vs the 2003-04 kernel. The hardened v1 library cuts from the
2003-04 kernel.

## How to run

```bash
# Build first (from ~/work/11jun):
bash scripts/20_build.sh

# Quick known-answer + property tests:
bash tests/roundtrip/run_tests.sh

# Full [a-z]^4 exhaustive sweep (~45 min):
bash scripts/30_roundtrip.sh

# Per-family conformance:
bash scripts/60_families.sh   # Brahmi
bash scripts/65_perso_arabic.sh
bash scripts/66_nw_semitic.sh
```

## HPS six-paradigm conformance (2026, GCC-15)

| Paradigm | Sample | Status |
|---|---|---|
| Assembly (fasm) | HindiASM.uhin | ✓ सारे जहां से अच्छा |
| C (hincc) | HindiC.uhin | ✓ |
| C++ (hincc) | HindiC++.uhin | ✓ |
| Lex/Flex | HindiLEX.uhin | ✓ |
| BASIC (qb2c) | HindiBASIC.uhin | ✓ |
| Yacc/Bison | HindiYACC.uhin | ✓ हिंदवी कैल्क्यूलेटर |

All six paradigms compile and run through unmodified GCC/fasm/flex/bison
toolchain on Ubuntu 26.04 (kernel 7.0.0-14), June 2026.
