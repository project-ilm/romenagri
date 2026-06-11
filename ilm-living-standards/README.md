# ILM Localized Living-Standards Generator

**Copyright © 1993–2026 Abhishek Choudhary.** Source: Apache-2.0 · Data/spec/docs: CC BY-SA 3.0
Contact: https://ilm.codes · +91 77 99 802 802

A framework that takes the **institutional standards** governing each layer of
the 9-Layer AGI stack (ISO/IEC, IEEE, IETF, W3C, Khronos, OMG) and produces a
**localized, living, community-governed ledger** binding native-language
Romenagri-ED identifiers *into* those standards — with an Informed-Pedagogy layer
and explicit community review state.

## What this is — and what it is NOT

- It is **not** a re-authoring of any institutional standard. ISO/IEC 9899,
  IEEE 1800, etc. are untouched. Native identifiers **map INTO** them so code
  written in native keywords compiles through an unmodified, standards-conformant
  toolchain — the global computational ecosystem does not fracture.
- The 13,668 verified identifiers are a **base seed layer**, not a final
  authority. Every generated entry is marked `review_state.status = "default"`
  (unreviewed). Idiomatic correctness is decided by native-speaker review, not by
  the generator.

## Three principles (enforced in code, not just stated)

1. **Democratized control.** Output is a seed; nothing is presented as final.
   The review tool lets native speakers propose, endorse, contest, fork, and
   promote idiomatic keyword choices. Superseded seeds are kept as history,
   never silently deleted.
2. **Informed public.** Every entry carries a pedagogy schema explaining *what
   the underlying spec construct does*. The generator fills only mechanics it can
   **cite** to a standard clause; `localized_explanation` is left empty for
   native-speaker authoring. No invented mechanics.
3. **Institutional interop.** `maps_into` records the governing standard and its
   **honest governance class**: `de-jure` (ISO/IEEE/IETF/W3C), `de-facto`
   (community-stabilized — Rust, ONNX), `proprietary` (CUDA), `academic`
   (Raft/Paxos), `unstandardized` (cognitive architectures). Nothing is dressed
   up as an ISO spec that isn't one.

## Components

```
schema/living-standard-entry.schema.json   # the data model (JSON Schema draft-07)
data/institutional_standards.csv           # per-layer standards, honestly classed
src/living_standards_generator.py          # seed-ledger generator
src/review_tool.py                         # community governance state machine
examples/hindi_living_standards.jsonl      # 201 real Hindi entries (generated)
```

## Status by component

| Component | Status |
|---|---|
| Seed generator (identifier → standard binding) | **Built & verified** — 201/201 Hindi entries, all C-identifier-legal |
| Institutional standards registry | **Built**; AI-governance spec numbers (ISO/IEC 22989/23053) flagged "verify" |
| Informed-Pedagogy stubs | **Partial** — cited mechanics for ~8 anchor constructs; the rest await sourced authoring (no invented mechanics) |
| `localized_explanation` (native idiom) | **Open** — native-speaker authored; empty by default |
| Community review tool | **Built & tested** — propose/endorse/contest/fork/promote state machine works |
| Live contributor community | **Not yet** — the mechanics exist; the community is to be convened |

## Quick start

```bash
python3 src/living_standards_generator.py \
    data/lang_hindi.csv data/keyword_ontology.csv \
    examples/hindi_living_standards.jsonl
python3 src/review_tool.py    # demo: propose + endorse -> endorsed
```

## How an entry flows

1. **Generator** emits a seed: native form (tatsama/borrowed/pending default),
   reversible Romenagri-ED identifier, `maps_into` the governing standard,
   pedagogy stub, `status: default`.
2. **Native speakers** `propose` idiomatic alternatives (validated C-identifier-legal),
   `endorse` (3 endorsements → `endorsed`), `vote_alternative`, or `fork` a
   regional variant. Competing live alternatives → `contested`.
3. **Promotion** swaps the primary form to a community-endorsed one; the seed is
   preserved in `history`.

## Honest boundaries

- The generator produces **correct, reversible, legal defaults** — never a claim
  of idiomatic correctness. That elevation is the community's act.
- Pedagogy mechanics are **cited or empty**. The system never fabricates what a
  standard does.
- This is the **Pillar-2 (participation)** instrument. It does not by itself
  deliver Pillar-1 phonetic fidelity (the 2km×2km fieldwork) — that is a separate
  open programme.

Copyright © 1993–2026 Abhishek Choudhary.
