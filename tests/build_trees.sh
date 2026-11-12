#!/bin/bash
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
#
# Builds three copies of Romenagri side by side, and the library-level harness (tests/harness.c) against each of them:
#
#   build/new/Romenagri   this package's Romenagri/: every patch applied (patches/0001 the Sanskrit characters, 0002 the guards,
#                         0003 the nukta layer)
#   build/mid/Romenagri   the same with every patch but the first taken off again, last one first: patch 0001 only, the Sanskrit
#                         characters, no guards, no nukta layer
#   build/old/Romenagri   the same with patch 0001 taken off as well (the unpatched sources); or a copy of the directory named in
#                         RMN_BASELINE
#   build/h_old, build/h_mid, build/h_new      the harnesses;     build/logs/make_*.log      the build logs
#
#   tests/build_trees.sh          (tests/run_all.sh calls it first; run it alone to rebuild the trees for ad-hoc work)
#
# needs: gcc, make, flex (+ libfl), patch.  Environment: RMN_BUILD (default build/), RMN_BASELINE.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(dirname "$HERE")
BUILD=${RMN_BUILD:-$ROOT/build}
LOGS=$BUILD/logs
case "$BUILD" in ""|/|/home|/root|/tmp) echo "refusing to use '$BUILD' as the build directory"; exit 2;; esac
rm -rf "$BUILD"; mkdir -p "$BUILD/old" "$BUILD/mid" "$BUILD/new" "$LOGS"
PATCHES=$(ls "$ROOT"/patches/*.patch | sort)
FIRST=$(echo "$PATCHES" | head -n 1)
cp -R "$ROOT/Romenagri" "$BUILD/new/Romenagri"
cp -R "$ROOT/Romenagri" "$BUILD/mid/Romenagri"
for p in $(echo "$PATCHES" | sed '1d' | sort -r); do                 # every patch but the first, the last one first
  ( cd "$BUILD/mid" && patch -R -p1 --quiet < "$p" ) || { echo "cannot take $p off the copy"; exit 2; }
done
if [ -n "${RMN_BASELINE:-}" ]; then
  echo "== 1. building: the patched tree, the tree with patch 0001 only, and the baseline $RMN_BASELINE"
  cp -R "$RMN_BASELINE" "$BUILD/old/Romenagri" || { echo "cannot copy the baseline"; exit 2; }
else
  echo "== 1. building: the patched tree, the tree with patch 0001 only, and the tree without any patch"
  cp -R "$BUILD/mid/Romenagri" "$BUILD/old/Romenagri"
  ( cd "$BUILD/old" && patch -R -p1 --quiet < "$FIRST" ) || { echo "cannot take $FIRST off the copy"; exit 2; }
fi
for t in old mid new; do
  ( cd "$BUILD/$t/Romenagri" && rm -f ./*.o librmnagri.a lexyy.c && make all > "$LOGS/make_$t.log" 2>&1 ) \
    || { echo "build of the $t tree failed, see $LOGS/make_$t.log"; exit 2; }
  gcc -O1 -I "$BUILD/$t/Romenagri" -o "$BUILD/h_$t" "$HERE/harness.c" "$BUILD/$t/Romenagri/librmnagri.a" \
    || { echo "cannot build the harness for the $t tree"; exit 2; }
  echo "   $t: $(grep -c -i warning "$LOGS/make_$t.log") compiler warnings, binaries: $(cd "$BUILD/$t/Romenagri" && ls rmn2acii acii2rmn uni2acii acii2uni acii2hin 2>/dev/null | wc -l) of 5"
done
