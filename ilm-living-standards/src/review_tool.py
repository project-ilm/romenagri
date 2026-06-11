#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
review_tool.py — community governance over the living-standards ledger
======================================================================
Implements the "avoid top-down finality" mandate: the 13,668 generator seeds are
a BASE LAYER. Native speakers propose, endorse, contest, and fork idiomatic
keyword choices. State transitions are explicit and auditable.

State machine (review_state.status):
    default ──propose──> proposed ──review──> under-review
    under-review ──endorse(threshold)──> endorsed
    under-review ──competing proposal──> contested
    any ──fork──> forked   (a divergent native standard, recorded not erased)

Rules enforced:
  * Every proposed/forked romenagri_ed must remain C-identifier-legal.
  * Reversibility is not broken: an alternative changes the NATIVE/idiom choice;
    its romenagri_ed must still be a legal identifier and is validated.
  * No personal data: reviewers are chosen handles only.
  * Generator seeds can be superseded but never silently deleted — the seed
    remains as provenance history.

Copyright (c) 1993-2026 Abhishek Choudhary. Apache-2.0.
"""
from __future__ import annotations
import json
import re

C_IDENT = re.compile(r"^[a-z_][a-z0-9_]*$")
ENDORSE_THRESHOLD = 3   # endorsements needed to move under-review -> endorsed


def _legal(rom: str) -> bool:
    return bool(C_IDENT.match(rom))


def propose(entry: dict, native: str, romenagri_ed: str, rationale: str, handle: str) -> dict:
    """A native speaker proposes an idiomatic alternative for a construct."""
    if not _legal(romenagri_ed):
        raise ValueError(f"proposed romenagri_ed {romenagri_ed!r} is not C-identifier-legal")
    alt = {"native": native, "romenagri_ed": romenagri_ed,
           "rationale": rationale, "votes": 0, "proposer": handle}
    entry["review_state"].setdefault("alternatives", []).append(alt)
    if entry["review_state"]["status"] == "default":
        entry["review_state"]["status"] = "proposed"
    return entry


def endorse(entry: dict, handle: str) -> dict:
    """Endorse the CURRENT primary form. Crosses threshold -> endorsed."""
    rs = entry["review_state"]
    if handle not in rs["reviewers"]:
        rs["reviewers"].append(handle)
        rs["endorsements"] = rs.get("endorsements", 0) + 1
    if rs["status"] in ("default", "proposed"):
        rs["status"] = "under-review"
    if rs["endorsements"] >= ENDORSE_THRESHOLD and rs["status"] == "under-review":
        rs["status"] = "endorsed"
        if entry["provenance"] != "hand-authored":
            entry["provenance"] = "community-revised"
    return entry


def vote_alternative(entry: dict, romenagri_ed: str, handle: str) -> dict:
    """Vote for a competing alternative. Two live alternatives => contested."""
    rs = entry["review_state"]
    found = False
    for alt in rs.get("alternatives", []):
        if alt["romenagri_ed"] == romenagri_ed:
            alt["votes"] += 1
            found = True
    if not found:
        raise ValueError(f"no alternative with romenagri_ed {romenagri_ed!r}")
    live = [a for a in rs["alternatives"] if a["votes"] > 0]
    if len(live) >= 2:
        rs["status"] = "contested"
    return entry


def promote_alternative(entry: dict, romenagri_ed: str) -> dict:
    """Promote a winning alternative to the primary form. Seed kept as history."""
    rs = entry["review_state"]
    alt = next((a for a in rs.get("alternatives", []) if a["romenagri_ed"] == romenagri_ed), None)
    if not alt:
        raise ValueError("alternative not found")
    if not _legal(alt["romenagri_ed"]):
        raise ValueError("winning alternative is not C-identifier-legal")
    # record the superseded seed in history (never silently deleted)
    entry.setdefault("history", []).append({
        "was_native": entry["native"], "was_romenagri_ed": entry["romenagri_ed"],
        "superseded_by": romenagri_ed,
    })
    entry["native"] = alt["native"]
    entry["romenagri_ed"] = alt["romenagri_ed"]
    entry["provenance"] = "community-revised"
    rs["status"] = "endorsed"
    return entry


def fork(entry: dict, native: str, romenagri_ed: str, rationale: str, handle: str) -> dict:
    """Record a divergent native standard (regional/idiomatic split). Not erased."""
    if not _legal(romenagri_ed):
        raise ValueError("forked romenagri_ed not C-identifier-legal")
    entry.setdefault("forks", []).append({
        "native": native, "romenagri_ed": romenagri_ed,
        "rationale": rationale, "by": handle,
    })
    entry["review_state"]["status"] = "forked"
    return entry


if __name__ == "__main__":
    # demo over a single synthetic entry
    e = {
        "construct_id": "KW_FUNC", "language": "hin", "layer": 3,
        "native": "कृत्य", "romenagri_ed": "krtya",
        "maps_into": {"standard": "ISO/IEC 9899", "governance": "de-jure"},
        "provenance": "tatsama<sanskrit",
        "review_state": {"status": "default", "endorsements": 0, "reviewers": [], "alternatives": []},
    }
    propose(e, native="फलन", romenagri_ed="phalana",
            rationale="phalana is the prevailing CS-pedagogy term in Hindi", handle="reviewer_a")
    endorse(e, "reviewer_a"); endorse(e, "reviewer_b"); endorse(e, "reviewer_c")
    print(json.dumps(e, ensure_ascii=False, indent=2))
