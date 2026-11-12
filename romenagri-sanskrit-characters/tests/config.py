# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Where the tests find things.  tests/build_trees.sh (which tests/run_all.sh calls first) builds three copies of Romenagri:

    build/new/Romenagri   the patched tree (this package's Romenagri/: all three patches), compiled
    build/mid/Romenagri   the same tree with patches 0003 (the nukta layer) and 0002 (the guards) taken off again: patch 0001 only,
                          the Sanskrit characters, compiled
    build/old/Romenagri   the same tree with all the patches/*.patch taken off again (the unpatched sources), compiled;
                          or a copy of the directory named in RMN_BASELINE

and compiles tests/harness.c against each library (build/h_old, build/h_mid, build/h_new).  Environment overrides: RMN_BUILD, RMN_OLD,
RMN_MID, RMN_NEW.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for p in (os.path.join(ROOT, "tools"), HERE):
    if p not in sys.path:
        sys.path.insert(0, p)

BUILD = os.environ.get("RMN_BUILD", os.path.join(ROOT, "build"))
OLD = os.environ.get("RMN_OLD", os.path.join(BUILD, "old", "Romenagri"))
MID = os.environ.get("RMN_MID", os.path.join(BUILD, "mid", "Romenagri"))
NEW = os.environ.get("RMN_NEW", os.path.join(BUILD, "new", "Romenagri"))
H_OLD = os.path.join(BUILD, "h_old")
H_MID = os.path.join(BUILD, "h_mid")
H_NEW = os.path.join(BUILD, "h_new")
RESULTS = os.path.join(ROOT, "results")


def need(path):
    if not os.path.exists(path):
        sys.exit("missing %s -- run tests/run_all.sh (it builds the old, mid and new trees first)" % path)
    return path
