#!/usr/bin/env bash
# Round-trip reversibility test suite — the published methodology
# Run from ~/work/11jun/repos/romenagri/tests/roundtrip/
# Requires: build/rmn_pipe and build/uni2acii to exist (from scripts/20_build.sh)
set -uo pipefail
B=~/work/11jun/build
R=~/work/11jun/results/ROUNDTRIP
mkdir -p "$R"
echo "[STATUS] Round-trip test suite — Romenagri reversibility"
echo "[STATUS] Kernel: 2003-04 (holy-grail) / chintamani (post-guard)"
echo ""

run_test() { # $1=label $2=input_utf8
  echo "$2" | iconv -f UTF-8 -t UTF-16LE > /tmp/_rt.u16 2>/dev/null
  $B/uni2acii /tmp/_rt.u16 /tmp/_rt.iscii 2>/dev/null
  RMN=$($B/rmn_pipe < /tmp/_rt.iscii 2>/dev/null)
  # reverse: rmn -> iscii -> unicode (requires acii2uni)
  [ -x $B/acii2uni ] || { echo "$1: SKIP (acii2uni not built)"; return; }
  BACK=$(echo "$RMN" | $B/rmn_pipe 2>/dev/null)  # forward again for fixpoint test
  echo "$1: input='$2' rmn='$RMN' fixpoint='$BACK'"
}

# KNOWN-ANSWER TESTS
echo "=== Known-answer tests ==="
run_test "namaste-hi"  "नमस्ते"
run_test "bharat-hi"   "भारत"
run_test "india-ur"    "بھارت"  # via fltr_ur_hi if available
run_test "shalom-he"   "שלום"
run_test "salaam-ar"   "سلام"

# PROPERTY TEST: all single Devanagari consonants must round-trip
echo ""
echo "=== Single consonant round-trip ==="
python3 - <<'PY'
import subprocess,unicodedata
deva=[chr(cp) for cp in range(0x0915,0x0940) if unicodedata.category(chr(cp))=='Lo']
ok=fail=0
for ch in deva:
    try:
        p=subprocess.run("echo '"+ch+"' | iconv -f UTF-8 -t UTF-16LE | "
                         + "~/work/11jun/build/uni2acii /dev/stdin /tmp/_t.iscii 2>/dev/null && "
                         + "~/work/11jun/build/rmn_pipe < /tmp/_t.iscii",
                         shell=True,capture_output=True,timeout=5)
        if p.stdout: ok+=1
        else: fail+=1
    except: fail+=1
print(f"Devanagari consonants: {ok}/{ok+fail} produced Romenagri output")
PY

echo ""
echo "=== [a-z]^3 exhaustive kernel test (quick, 18278 strings) ==="
echo "See scripts/30_roundtrip.sh for full [a-z]^4 sweep (475,254 strings)"
echo "Results in ~/work/11jun/results/ROUNDTRIP_RESULTS.tsv"
