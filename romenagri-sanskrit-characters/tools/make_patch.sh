#!/bin/bash
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
#
# Regenerates a patch of this package: the difference between two Romenagri/ directories.
#
#   patches/0001-add-missing-sanskrit-characters.patch   an upstream Romenagri/ (a `git archive` of hindawiai/chintamani, commit 3ad87785)
#                                                        against the Romenagri/ with patch 0001 only
#   patches/0002-apply-underscore-guards.patch           the Romenagri/ with patch 0001 only against the Romenagri/ with patches 0001 and 0002
#   patches/0003-add-nukta-layer.patch                   the Romenagri/ with patches 0001 and 0002 against the Romenagri/ of this package
#
#   tools/make_patch.sh <older Romenagri dir> <newer Romenagri dir> <output .patch>
#
# The patch applies with  patch -p1  from the directory that contains Romenagri/ .
set -e
[ $# = 3 ] || { sed -n '2,15p' "$0"; exit 2; }
A=$(cd "$1" && pwd); B=$(cd "$2" && pwd); OUT=$3
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/a" "$TMP/b"
cp -R "$A" "$TMP/a/Romenagri"
cp -R "$B" "$TMP/b/Romenagri"
( cd "$TMP" && git -c core.autocrlf=false -c core.safecrlf=false diff --no-index --no-color --no-prefix a b > "$TMP/raw.patch" || true )
cp "$TMP/raw.patch" "$OUT"
grep '^diff --git' "$OUT"
