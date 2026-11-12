#!/bin/bash
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
#
# Builds three Romenagri trees side by side (tests/build_trees.sh) and runs the whole test suite.
#
#   old   the unpatched sources                      mid   patch 0001 only: the Sanskrit characters
#   new   this package's Romenagri/: patches 0001, 0002 and 0003 (the Sanskrit characters, the guards of section 14.7 and the nukta
#         layer of section 15)
#
#   tests/run_all.sh                       quick run (about a minute and a half)
#   tests/run_all.sh --full                the exhaustive run (many minutes in all, so it is meant to be run in pieces: see below)
#   tests/run_all.sh --full --resume       the same, in pieces that can be interrupted: every step leaves a marker (<step>.rc) in
#                                          build/logs, and a step that passed earlier on the same sources is not run again
#   tests/run_all.sh --full --resume --only build
#   tests/run_all.sh --full --resume --only parser_vs_model,roundtrip,underscore_U1,underscore_U2,underscore_U3
#                                          run only the named steps (names as in the SUMMARY; `underscore` stands for the nine
#                                          steps underscore_U1 ... underscore_U9, `build` for the build of the three trees).
#                                          Steps that do not depend on one another can be run by several such commands at once
#                                          (after `--only build`); a last `--full --resume` without `--only` then prints the whole
#                                          console output from the logs and the SUMMARY, and runs whatever is still missing.
#                                          A pool of two, the longest steps first (every step that is run asks for its own --only):
#   tests/run_all.sh --full --resume --only build
#   printf '%s\n' underscore_U7 underscore_U1 parser_vs_model roundtrip underscore_U5 underscore_U6 underscore_U8 underscore_U9 \
#     underscore_U4 underscore_U2 underscore_U3 corpus limitations recipes unicode nukta saral table_lint_new reserved_keys \
#     doc_tables_in_sync e2e_new | xargs -P 2 -I{} tests/run_all.sh --full --resume --only {}
#   tests/run_all.sh --full --resume
#
# The long check of section 14 (tests/test_underscore.py, `--full`) is run as nine steps, one per check (U1 ... U9), so that no
# single step is long, and so that an interrupted run loses at most one of them.
#
# needs: gcc, make, flex (+ libfl), patch, python3.  The end-to-end test additionally needs hincc and the Hindawi converters on PATH
# (it is skipped otherwise).  Everything is built under build/ (override with RMN_BUILD); logs go to build/logs.
#
# environment:
#   RMN_BASELINE=<dir>   the Romenagri directory to use as the old tree; default: this package's Romenagri/ with every patch taken off
#   RMN_CORPUS=<files>   more Hindi text files for tests/test_corpus.py, separated by ':'   (for example
#                        RMN_CORPUS=$(find /path/to/chintamani -name '*.uhin' | paste -sd:) tests/run_all.sh)
#   HINDAWI_SRC=<dir>    the Hindawi/ directory of chintamani: lets the end-to-end test rebuild the shailis with the Romenagri under test
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(dirname "$HERE")
BUILD=${RMN_BUILD:-$ROOT/build}
LOGS=$BUILD/logs
export LC_ALL=C.UTF-8 RMN_BUILD=$BUILD PYTHONUNBUFFERED=1
FULL=0; RESUME=0; ONLY=""
args=("$@"); i=0
while [ $i -lt ${#args[@]} ]; do
  case "${args[$i]}" in
    --full) FULL=1;;
    --resume) RESUME=1;;
    --only) i=$((i+1)); ONLY=${args[$i]:-};;
    --only=*) ONLY=${args[$i]#--only=};;
  esac
  i=$((i+1))
done
UNDERSCORE_STEPS="underscore_U1,underscore_U2,underscore_U3,underscore_U4,underscore_U5,underscore_U6,underscore_U7,underscore_U8,underscore_U9"
ONLY=$(echo "$ONLY" | sed "s/\bunderscore\b/$UNDERSCORE_STEPS/g")
if [ $FULL = 1 ]; then DP="4 300000 200000"; RT="3 200000"; UF="--full"; else DP="3 20000 20000"; RT="3 20000"; UF=""; fi

want() {                                 # want <step> : is the step selected (everything is, unless --only was given)?
  [ -z "$ONLY" ] && return 0
  case ",$ONLY," in *",$1,"*) return 0;; esac
  return 1
}

stamp() {                                # a short hash of the sources, the tests and the settings: a marker is only valid for the same stamp
  ( cd "$ROOT" && { find Romenagri patches tools tests -type f ! -path '*/__pycache__/*' -print0 | sort -z | xargs -0 sha256sum
                    echo "full=$FULL corpus=${RMN_CORPUS:-} hindawi=${HINDAWI_SRC:-}"; } | sha256sum | cut -c1-16 )
}
STAMP=$(stamp)

if want build; then
  if [ $RESUME = 1 ] && [ -f "$LOGS/stamp" ] && [ "$(cat "$LOGS/stamp")" = "$STAMP" ] && [ -x "$BUILD/h_old" ] && [ -x "$BUILD/h_mid" ] && [ -x "$BUILD/h_new" ]; then
    echo "== 1. the three trees are already built for these sources"
  else
    bash "$HERE/build_trees.sh" || exit 2
    echo "$STAMP" > "$LOGS/stamp"
  fi
elif [ ! -x "$BUILD/h_new" ]; then
  echo "the trees are not built (run with --only build first)"; exit 2
fi
if [ -f "$LOGS/stamp" ] && [ "$(cat "$LOGS/stamp")" != "$STAMP" ]; then
  echo "the sources or the settings changed since the trees in $BUILD were built; run with --only build, or without --resume"; exit 2
fi

declare -a NAMES RESULTS
run() {                                  # run <name> <command...> : log to $LOGS/<name>.log, record PASS/FAIL in $LOGS/<name>.rc
  local name=$1; shift
  want "$name" || return 0
  if [ $RESUME = 1 ] && [ -f "$LOGS/$name.rc" ] && [ "$(cut -d' ' -f1 "$LOGS/$name.rc")" = 0 ]; then
    echo "== $name   (passed earlier: $(cut -d' ' -f2- "$LOGS/$name.rc"))"
  else
    echo "== $name"
    local t0; t0=$(date +%s)
    "$@" > "$LOGS/$name.log" 2>&1; local rc=$?
    echo "$rc $(( $(date +%s) - t0 )) s, finished $(date -u +%FT%TZ)" > "$LOGS/$name.rc"
  fi
  tail -n 40 "$LOGS/$name.log" | sed 's/^/   /'
  NAMES+=("$name"); RESULTS+=("$(cut -d' ' -f1 "$LOGS/$name.rc")")
}

e2e_both() {                             # the end-to-end programs through hincc on the new tree; the old tree is expected to fail to compile
  "$HERE/e2e/run_e2e.sh" new "$BUILD/new/Romenagri" "$BUILD/e2e_new"; local rc=$?
  "$HERE/e2e/run_e2e.sh" old "$BUILD/old/Romenagri" "$BUILD/e2e_old" > "$LOGS/e2e_old.log" 2>&1
  return $rc
}

run table_lint_new   python3 "$ROOT/tools/check_tables.py" "$BUILD/new/Romenagri" --free
run unicode          python3 "$HERE/test_unicode.py"
run nukta            python3 "$HERE/test_nukta.py" $UF
run saral            python3 "$HERE/test_acii2hin.py"
run parser_vs_model  python3 "$HERE/diff_parser.py" $DP
run roundtrip        python3 "$HERE/rt_filters.py" $RT
run corpus           python3 "$HERE/test_corpus.py"
run recipes          python3 "$HERE/test_extension_recipes.py"
run limitations      python3 "$HERE/test_limitations.py"
for u in U1 U2 U3 U4 U5 U6 U7 U8 U9; do
  run "underscore_$u" python3 "$HERE/test_underscore.py" $UF --only $u
done
run reserved_keys    python3 "$ROOT/tools/reserved_keys.py" "$ROOT/Romenagri"
if [ -f "$ROOT/Romenagri/TRANSLITERATION.md" ] && [ -f "$ROOT/tools/gen_doc_tables.py" ]; then
  run doc_tables_in_sync python3 "$ROOT/tools/gen_doc_tables.py" --check "$ROOT/Romenagri"
fi
# the old tree is expected to show the avagraha defect (T3/T6/T7 errors): informational only
if [ -z "$ONLY" ]; then
  python3 "$ROOT/tools/check_tables.py" "$BUILD/old/Romenagri" > "$LOGS/table_lint_old.log" 2>&1
  echo "== table_lint_old (informational: the unpatched tables)"; tail -n 3 "$LOGS/table_lint_old.log" | sed 's/^/   /'
fi

if command -v hincc > /dev/null 2>&1; then
  if want e2e_new; then
    echo "== end-to-end through hincc (new build must pass; the old build is expected to fail to compile)"
    run e2e_new e2e_both
    [ -f "$LOGS/e2e_old.log" ] && tail -n 4 "$LOGS/e2e_old.log" | sed 's/^/   old: /'
  fi
else
  want e2e_new && echo "== end-to-end: skipped (hincc not on PATH)"
fi

echo; echo "================ SUMMARY"
bad=0
for i in "${!NAMES[@]}"; do
  if [ "${RESULTS[$i]}" = 0 ]; then s=PASS; else s=FAIL; bad=1; fi
  printf "  %-22s %s\n" "${NAMES[$i]}" "$s"
done
echo "  logs: $LOGS"
exit $bad
