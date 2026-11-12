#!/bin/bash
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
#
# End-to-end test through Hindawi's hincc: a Hindi C program and a Hindi Java program that use the new characters in identifiers,
# string literals and comments are compiled, run, and what they print is compared with the Devanagari source text.  A third
# program (the "control") is the C program without its two identifier lines, so that the unpatched build can still compile it.
#
# usage:  tests/e2e/run_e2e.sh <label> <directory holding the Romenagri binaries to test> [<output dir>]
# needs:  hincc and the Hindawi converters (Hindawi/ of the full chintamani repository, built and on PATH), gcc, javac/java.
#         Not run by tests/run_all.sh unless hincc is found on PATH.
# env:    HINDAWI_SRC=<path of chintamani/Hindawi>   additionally rebuilds the C and Java shailis (guru, kritrima) with the Romenagri
#         under test, as a fresh "install Romenagri, then install Hindawi" would; without it the installed converters are used.
label=$1; bindir=$(cd "$2" && pwd)
HERE=$(cd "$(dirname "$0")" && pwd)
OUT=${3:-$HERE/run_$label}
export LC_ALL=C.UTF-8 PATH="$bindir:$PATH"
rm -rf "$OUT"; mkdir -p "$OUT/c" "$OUT/c0" "$OUT/j"; OUT=$(cd "$OUT" && pwd)
if [ -n "${HINDAWI_SRC:-}" ]; then
  mkdir -p "$OUT/shailis/bin"
  for s in guru kritrima; do
    cp -R "$HINDAWI_SRC/$s" "$OUT/shailis/$s"
    ( cd "$OUT/shailis/$s" && make all > "$OUT/shailis/$s.log" 2>&1 )
    for b in h2c c2h h2j j2h; do [ -x "$OUT/shailis/$s/$b" ] && cp "$OUT/shailis/$s/$b" "$OUT/shailis/bin/$b"; done
  done
  export PATH="$OUT/shailis/bin:$PATH"
  echo "shailis rebuilt with this Romenagri: $(ls "$OUT/shailis/bin" | tr '\n' ' ')"
fi
( cd "$OUT/c" && cp "$HERE/c.uhin" . && hincc c.uhin > compile.log 2>&1; ./hin.exe > out.txt 2> run.err; echo "C    : hin.exe $( [ -x hin.exe ] && echo built || echo MISSING )" )
( cd "$OUT/c0" && grep -v -F -e 'ॐ = 42' -e 'ऌ = 7' -e 'F:identifiers' "$HERE/c.uhin" > c0.uhin && hincc c0.uhin > compile.log 2>&1; ./hin.exe > out.txt 2> run.err; echo "C0   : hin.exe $( [ -x hin.exe ] && echo built || echo MISSING )" )
( cd "$OUT/j" && cp "$HERE/j.uhin" . && hincc j.uhin > compile.log 2>&1; ls *.class > /dev/null 2>&1 && java Test > out.txt 2> run.err; echo "Java : $(ls *.class 2>/dev/null | tr '\n' ' ')" )
python3 -I "$HERE/check.py" "$OUT" -v
