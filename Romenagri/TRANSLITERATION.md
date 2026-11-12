# Romenagri transliteration: the formal definition, the Sanskrit additions, and how to extend them

Copyright (C) 1993-2026 Abhishek Choudhary. Licensed under the GNU General Public License, version 2 or (at your option) any later
version; see the file `COPYING`. SPDX-License-Identifier: GPL-2.0-or-later.

This is `Romenagri/TRANSLITERATION.md`. It describes the `Romenagri/` directory of the hindawiai/chintamani repository as it was at
commit `3ad87785a75dc2b18438a8b068807103cb920c81`, plus three patches: `patches/0001-add-missing-sanskrit-characters.patch`, which adds the twelve Sanskrit
characters and the first version of this file; `patches/0002-apply-underscore-guards.patch`, which adds twelve guards to the parser and brings this file up to date (section 14.7); and `patches/0003-add-nukta-layer.patch`, which adds the nukta layer to the two Unicode converters (section 15).
The scripts named below (`tools/...`, `tests/...`) belong to the package that carries the patches. They read the files of `Romenagri/`; they are not part of it.

**Contents**

1. Purpose, status, vocabulary
2. The three layers and the programs
3. The tables
4. ACII to Romenagri: the decoder (`acii2rmn`)
5. Romenagri to ACII: the parser (`rmn2acii`), with its formal grammar
6. How the strings are built: the conventions
7. The Sanskrit additions
8. How to extend: the recipes
9. The round-trip contract
10. Larger character sets, character-set conflicts, missing sounds
11. Known limitations and quirks
12. Provenance and standards
13. Running the checks
14. Underscores: runs, escapes, case folding, joiners
15. The nukta layer: precomposed nukta letters in the Unicode converters
- Appendix A: the complete table; Appendix B: examples

## 1. Purpose, status, vocabulary

This document does six things.

1. It defines, as exactly as the code allows, how Romenagri converts between Unicode Devanagari, the 8-bit ACII encoding, and the
   ASCII transliteration that programs and shell tools work with. The recursive-descent parser in `rmn2acii.c`, which is the hard
   part, is written down as a formal grammar (section 5.3) that a program reads and runs.
2. It records the twelve Sanskrit characters that were added, with the reasoning for every byte and every string (section 7).
3. It states the rules by which the scheme can be extended to larger character sets, how conflicts between character sets are
   resolved, and what to do about sounds that have no spelling yet (sections 8 and 10).
4. It lists what does not work, so that nobody has to rediscover it (section 11).
5. It answers three formal questions about the underscore, the one character that is both a letter of the script and an escape (runs of
   any length, case folding and mutated input, joiners next to the operators of a host language), and records the twelve guard rules, added to
   the parser by the second patch, that make its reading of underscores exact (section 14).
6. It records the nukta layer that the third patch adds to `uni2acii` and `acii2uni`, so that the eleven precomposed nukta letters of Unicode go through the pipeline, the form in which the two converters write them (a choice of the user), what the layer does not do, and the eight challenges that were reviewed, each with the decision taken on it (section 15).

**How the document is kept true.** Statements here are of three kinds.

- *Defined*: the tables (generated from the headers) and the grammar of section 5.3, which includes the guards of section 14.7. `tools/gen_doc_tables.py --check` fails when a
  generated block is out of date, and `tests/diff_parser.py` runs the grammar against the C parser of each of the three builds (and against a second,
  hand-written parser) on more than a million inputs. If the grammar printed here were wrong, a test would fail.
- *Observed*: a behaviour that was measured, with the test or experiment named next to it (mostly in section 11).
- *Cited*: a fact about an outside standard or implementation, with its source in section 12.

**Vocabulary.**

| Term | Meaning |
|---|---|
| Unicode | the Unicode Devanagari block, U+0900 to U+097F; files are UTF-16LE for the converters, UTF-8 elsewhere |
| ACII | the 8-bit encoding used inside Romenagri: ISCII-91's Devanagari layout in the upper half (`80`-`FF`), plus extensions of this project; ASCII in the lower half |
| Romenagri | the ASCII transliteration of ACII text: bare letters, digits and punctuation |
| row | one entry of a table: `{key, bytes}` in `acii.h`, `{low, high, byte}` in `unicode.h` |
| key | the Romenagri string of a row, for example `ka`, `_ri`, `^aa` |
| unit | what the parser consumes in one trip through its start state: one consonant with its vowel sign, one vowel, one sign |
| stem | a consonant key without its final `a`: `k`, `kh`, `_t`, `lvr` |
| halant | the virama, U+094D, ACII `E8`; written in Romenagri only by what follows a consonant, and as `^` |
| nukta | the dot below, U+093C, ACII `E9`; written `z` after a consonant stem |
| nukta layer | what patch 0003 adds to `uni2acii` and `acii2uni` (`nukta.h`, section 15): the rule that a letter with a nukta is a consonant and a nukta, the form in which the two converters write such letters, and the warning layer |
| form | how the two Unicode converters write a letter with a nukta, as one code point or as two: `asis` (the default, what they always wrote), `nfc` or `nfd` (section 15.2) |
| level 1, level 2 | the two stages of the parser (section 5.1): at level 1 (`level1`) a consonant is recognised and its sound mapped; at level 2 (`level2a`, `level2b`, `level2c`, `matra`) the halant, the adjunct consonants and the vowel signs are bound to it. The decision of section 15.7 (C1, C6) is that a nukta letter is a consonant and a nukta before level 2 binds anything |
| family | the keys that share their letter after `_`: `_li` and `_lee` are the `_l` family |
| guard | two senses, told apart by the context (section 5.2): the part of a rule of the grammar before `->`, the condition under which it applies; and a *guard rule*, one of the twelve rules tagged `!` (patch 0002), which stands in front of a rule that jumps over a character it has not tested and sends an underscore or the end of the string to the right place instead (section 14.7) |
| old, mid, new | the three builds that the tests compile and compare: the unpatched Romenagri; Romenagri with patch 0001 (the Sanskrit characters: *mid*); and this package's Romenagri, with patches 0002 (the guards) and 0003 (the nukta layer) as well (*new*) |
| Hindawi | the programming system whose language styles (shailis) are built on these tools; it is not part of Romenagri |

## 2. The three layers and the programs

```
   Unicode text (UTF-8 in files)
        |  iconv -f utf8 -t utf16
        v
   UTF-16LE, with or without a byte-order mark
        |  uni2acii                      table: unicode.h, nukta.h
        v
   ACII bytes                            <- also read and written by the Hindawi translators
        |  acii2rmn | acii2cf | acii2pcf         table: acii.h   (the decoder, section 4)
        v
   Romenagri: ASCII letters, digits, punctuation     <- the text that programs, sed scripts and shailis see
        |  rmn2acii                            table: acii.h   (the parser, section 5)
        v
   ACII bytes
        |  acii2uni                      table: unicode.h, nukta.h
        v
   UTF-16LE with a byte-order mark       -> iconv -f utf16 -t utf8
```

`fixuninum` runs on UTF-8 text before `iconv`: it rewrites the digits of the ten Indic scripts of `iscii_map.csv` (Devanagari to Malayalam) to ASCII digits (section 11.1).
`acii2hin` is a side branch: it renders ACII as lossy "saral" (simple) Latin, using `aciihin.h`; nothing converts back.
The commands that Hindawi runs are in `Romenagri/mass_hindawi`, for example
`iconv -futf8 -tutf16 | uni2acii | acii2pcf | h2c` for Hindi source to C, and `c2h | acii2uni | iconv -futf16 -tutf8` for the way back;
`h2c` and `c2h` are Hindawi's, not Romenagri's.

| Program | Reads, writes | Table | Source |
|---|---|---|---|
| `uni2acii` | UTF-16LE, ACII bytes | `unicode.h`, `nukta.h` | `uni2acii.c` |
| `acii2uni` | ACII bytes, UTF-16LE (with BOM; LF becomes CR LF) | `unicode.h`, `nukta.h` | `acii2uni.c` |
| `acii2rmn` | ACII, Romenagri; Latin words are wrapped as `"e_word"`, quoted strings as `""string""` | `acii.h` | `acii2rmn.lex`, `acii2rmn.c`, `stack.c` |
| `rmn2acii` | the reverse; unwraps `"e_word"` and `""string""`, hands every run of `[A-Za-z_]` to the parser | `acii.h` | `rmn2acii.lex`, `rmn2acii.c` |
| `acii2cf`, `acii2pcf` | ACII, Romenagri for program text: Latin words and string and character literals are left as they are; the two differ in how literals with escapes are recognised | `acii.h` | `acii2cf.lex`, `acii2pcf.lex` |
| `acii2hin` | ACII, "saral" Latin | `aciihin.h` | `acii2hin.lex`, `acii2hin.c` |
| `fixuninum` | UTF-8, UTF-8 with ASCII digits | none (generated by `gen_fixuninum` from `iscii_map.csv`) | `fixuninum.lex` |

The two translators that matter for the formal definition are the decoder (ACII to Romenagri, section 4) and the parser (Romenagri to ACII,
section 5). The `.lex` files are the *lexical layer*: they cut the text into runs and decide which runs go to the translators
(section 11.1 lists what that implies). `librmnagri.a` contains the two translators and the stack they use; the filters and the
Unicode converters are separate programs.

## 3. The tables

### 3.1 `unicode.h`: Unicode and ACII bytes

`unicode_hin[UNI_LEN][3]` holds rows `{low, high, byte}`; the code point is `low + 256 * high`.

- `uni2acii` reads UTF-16LE in pairs of bytes. It drops a byte-order mark (`FF FE`) and a carriage return (`0D 00`). For every other
  pair it looks for the first row with the same code point and writes that row's byte. If there is no such row it writes **the low byte of the pair and discards the high byte**
  ("presuming 0 to 127", says the source). Section 11.6 shows what this does to the characters the table lacks. (Since patch 0003 the nine precomposed nukta letters that the table lacks are the exception: `uni2acii` writes each as the byte of its consonant and `E9`, section 15.)
- `acii2uni` writes the byte-order mark `FF FE` first. A line feed becomes `0D 00 0A 00`. For every other byte it looks for the first row with that byte and
  writes the row's code point. If there is none it writes `byte mod 128` as an ASCII character; ASCII bytes are therefore unchanged,
  and an unknown byte of the upper half folds into the lower half. (Since patch 0003, and only in the form `nfc`, a consonant byte followed directly by `E9` is written as one code point, instead of two, when `nukta.h` has a letter for the pair that NFC composes: `C6 E9`, `CF E9` and `D2 E9`; in the form `nfd`, `C7` and `D0` are written as pairs. The default form, `asis`, writes what the converter always wrote, section 15.2.)

So the table is a partial function from code points to bytes, and the lint (section 3.5) insists that it is injective: no code point twice, no byte twice.
Patch 0003 adds a second, small table beside it, `nukta_hin` in `nukta.h`: eleven rows that let the two converters treat a precomposed nukta letter as a consonant and a nukta (section 15). It does not change a row of `unicode.h`.

### 3.2 `acii.h`: ACII bytes and Romenagri keys

`acii_chrt[ACII_LEN][2]` holds rows `{key, bytes}`; `bytes` is one to three bytes. Two lookups use the table, and they use it differently.

- The parser calls `lookup(key)`: **the first row whose key equals the argument** gives its bytes; `NULL` if there is none (the next
  `strcat` then crashes, section 11.3).
- The decoder scans for **the first row whose first byte equals the input byte** and takes its key.

Consequences. Row order matters. A multi-byte row (a conjunct such as `kxa` = `B3 E8 D6`) is invisible to the decoder as soon as an earlier row starts with the same byte,
and every multi-byte row of the table is shadowed in this way. Two of them, `_rda` and `_rdha`, are keys that the parser looks up; the others are never used by either translator (section 11.2). Row 0 is a control row `{"", "\xEFB"}`:
`EF` is ISCII's attribute code, `42` ('B') selects Devanagari. The decoder reads `acii_chrt[0][1][0]` to know the attribute code, and drops the byte that follows it.

### 3.3 `aciihin.h`: the "saral" rendering

Same shape as `acii.h`, read only by `acii2hin`, which uses the decoder's algorithm with this table. It is one-way and lossy by design: several letters
share a spelling (`na` for four different nasals, `i` for short and long I), and what has no simple Latin spelling is left out. The new characters follow that style (section 7).

### 3.4 The byte space

`unicode.h` and `acii.h` use the bytes `80`-`FF` like ISCII-91 does, with these differences from the layout in `iscii_map.csv` (section 12):

| Bytes | ISCII-91 layout (`iscii_map.csv`) | In ACII |
|---|---|---|
| `A0` | Sign OM in this repository's CSV; the ICU table makes it a no-break space, the Apple table leaves it unused (section 12) | unused, and kept unused: `uni2acii` writes U+00A0 as `A0` (section 10.3) |
| `A1`-`A3` | candrabindu, anusvara, visarga | the same |
| `A4`-`B2` | independent vowels | the same |
| `B3`-`D8` | consonants KA to HA | the same; `D9` (the "invisible" consonant) is unused |
| `DA`-`E7` | dependent vowel signs | the same |
| `E8`, `E9` | halant, nukta | the same |
| `EA` | danda ("full stop") | the same |
| `EB` | unused in the CSV | avagraha |
| `EF`, `F0` | attribute code, extension code | `EF` only, in row 0; `F0` is never used |
| `F1`-`FA` | digits | unused: `fixuninum` turns Devanagari digits into ASCII digits first |
| `80` | not in ISCII-91 | U+0979 (ZHA), an earlier extension |
| `81`-`8C` | not in ISCII-91 | the Sanskrit additions of section 7, with `80` an extension block of this project |

### 3.5 Invariants, and the lint that checks them

`tools/check_tables.py <Romenagri dir>` runs without a compiler (it uses the executable models in `tests/`) and checks:

| Check | What must hold |
|---|---|
| T1 | `ACII_LEN`, `UNI_LEN`, `ACII_HIN_LEN` equal the number of rows |
| T2 | row 0 of `acii.h` is the control row |
| T3 | every key uses `[a-z_]`, with an optional leading `^` (legacy keys `""`, `__`, `\|`, `^` excepted) |
| T4 | no key twice, no code point twice, no byte given to two code points |
| T5 | every Unicode row has an `acii.h` row for its byte, and every one-byte `acii.h` row of the upper half has a Unicode row |
| T6 | every key, read by the parser, gives exactly the bytes of its own row; every one-byte row is produced by the decoder from its byte |
| T7 | consonant + halant + X, and X + consonant, survive decoder and parser for every letter X (this catches a new string that extends an existing token) |
| T8 | marker rule: in every key except `__` each `_` is followed by a letter (section 14.3: this is what makes a marker the last underscore of its run) |

`--free` prints the free bytes with their allocation class (section 10.1).

## 4. ACII to Romenagri: the decoder (`acii2rmn`)

The decoder is a stack machine. Its state is a stack of characters, initially empty, of at most 10,239 characters (`stack.c`: 10,240 bytes including the terminator).
For each input byte `b`, in order:

```
r := the first row (table order) whose first byte is b
if there is no such row:
    unless b follows the byte EF (attribute code): push the character b      -- ASCII and unknown bytes pass through
                                                                             -- the byte after EF is dropped
otherwise, if r.key starts with '^' and the stack is not empty:           -- a dependent sign, or the halant
    pop one character                                                     -- the 'a' of the consonant before
    if r.key starts with "^z":                                            -- the nukta
        t1 := pop one character
        if t1 = 'h':   t2 := pop one character
                       if t2 = 'd': push "_rdha"   else: push t2, "hza"
        elif t1 = 'd': push "_rda"
        else:          push t1, "za"
    else: push r.key without its '^'
otherwise: push r.key
output the stack
```

(For the first byte of a run the C code reads the byte *before* its buffer to test the `EF` condition, which is undefined behaviour; the model assumes it is not `EF`.)

What follows from this:

- **The 'a' protocol.** Every consonant key ends in `a`. A consonant followed by a vowel sign, a nukta or a halant has that `a` popped, so `ka` + sign I (`^i`) is `k` + `i` = `ki`; `ka` + halant (`^`) is `k`. The parser relies on this: a stem
  that is followed by another unit gets its halant back (the list of stems follows these bullets).
- **The nukta exceptions.** Plain nukta handling is "stem + `z` + `a`": `ka` + nukta = `kza`. Two consonants have their own nukta letters in the Hindi tradition, DDA and DDHA (`ड़`, `ढ़`), so `da` + nukta is `_rda` and `dha` + nukta is `_rdha`; a stem ending in `h` has the `h` moved after the `z` (`khza`, not `kzha`).
- **A dependent sign pops whatever is on top.** The decoder does not check that the top of the stack is the `a` of a consonant. A vowel sign after something else (a vowel, a danda) deletes the last character of that: this is garbage in, garbage out, and section 9 says which ACII text is guaranteed to work.
- **Limit and crashes.** More than 10,239 characters in one run overflow the stack; a nukta with at most one character below it pops an empty stack (section 11.4).

The stems that remain after popping, one for each consonant byte of the table (`80`, `B3`-`D8`), written the way the decoder writes them:

<!-- BEGIN GENERATED halant-popped -->

`k`, `kh`, `g`, `gh`, `_ng`, `ch`, `chh`, `j`, `jh`, `_yn`, `t`, `th`, `d`, `dh`, `_nn`, `_t`, `_th`, `_d`, `_dh`, `n`, `p`, `ph`, `b`, `bh`, `m`, `y`, `r`, `_rr`, `l`, `w`, `lvr`, `sh`, `x`, `s`, `_h`, `_jz`, `_nz`

<!-- END GENERATED halant-popped -->

The decoder needs no look-ahead, and the only part of its own output it ever looks at or changes is the last three characters. `tests/model.py` (`model_encode`) transcribes it, and `tests/rt_filters.py` compares the transcription with the C code on every sequence of up to two bytes over the whole repertoire and on random longer ones.

## 5. Romenagri to ACII: the parser (`rmn2acii`)

### 5.1 How a string is read

The parser in `rmn2acii.c` is five mutually recursive C functions, `level1`, `level2a`, `level2b`, `level2c` and `matra`. The grammar below
calls the corresponding states L1, L2a, L2b, L2c and M. A string is read once from the left, with no backtracking, and the output is a sequence of table rows and raw characters.

- **L1, the start of a unit.** The next character says what begins. A consonant that can stand alone (`n m y w x r`) is written as its row (`na`, `ma`, ...) and the parser goes to L2a.
  A consonant that may take an aspirate (`g t d p b s l k j`, and `c`, which is really `ch`) goes to L2b, which looks for an `h`; a `c` is read as `ch` whatever letter follows it, except an underscore or the end of the string, where it is the plain letter `c` (a guard rule, section 14.7). `_` opens a family (L2c); `^` opens a dependent sign (M);
  `|` is the danda. **Anything else is copied to the output unchanged**: digits, punctuation, upper-case letters, and also the letters `a e h i o u f q v z` when they start a unit.
  This is why a vowel always needs its `_`, and why `h` can only be written after a letter that takes it.
- **L2a, after a consonant row.** The parser has written the consonant *with its inherent vowel*. If the string ends, or the next character starts a new unit, it appends a halant (this is how a bare consonant,
  a conjunct or a final dead consonant is written; the comment above `level2a` says "Schwa deletion is not supported for phonetic accuracy"). Otherwise a vowel follows: state M.
- **L2b(stem).** A stem has been read (`k`, or `_t`, ...). An `h` asks for the aspirate row (`kha`, `_tha`), a `v` for the row *stem* + `vra` (only `lvra`, the letter `ळ`, exists; for every other stem the row is missing, section 11.3), and anything else for the plain row (`ka`); all three go to L2a. A `v` that is followed by an underscore or by the end of the string does not ask for `vra`: the stem gets its plain row and the `v` is text (a guard rule).
- **L2c, after `_`.** The letter after `_` selects a family: homophones and letters that have no plain spelling. `_t`, `_d`, `_rd`, `_rr` re-enter L2b with a longer stem.
- **M, a vowel sign** after a consonant or after an explicit `^`. `a` alone means "the consonant keeps its inherent vowel" and is dropped; `aa ae aee ai ao au i u e(e) oo ow oa ou`, `z` (the nukta) and `_ri` `_li` `_lee` `_ree` write the signs.

The inherent vowel is therefore always written. In Romenagri `ka` is क, `k` is क् (a bare consonant), `ki` is कि, `kaa` is का, and `raama` is राम.

**Letters that need a partner.** Eleven branches of the parser read a letter and then jump over, or keep as text, the next character without looking at it: the `h` of `ch`, the `r` of `vra`, the second `e` of `_ee` and of `^ee`, the `n` of `_yna`, the two letters of `^_ri`, and the character after an unknown `_o`, `_n`, `_r`, `_j` or `^o` (section 5.4). Patch 0002 puts a test in front of each of them: if the character that would be jumped over is an underscore or the end of the string, the branch is not taken, and the letter is written as plain text, like any other letter that the parser does not know. These tests are the rules tagged `!` in the grammar; section 14.7 says why they are needed and what they establish.

The recursion is only apparent. Every call in `rmn2acii.c` is the last thing its branch does, so the parser is a loop over five states, not a pushdown machine. `main.c` calls the parser "LA(1)"; the grammar shows that it looks at up to four characters at once (section 5.4).

### 5.2 Notation

The grammar is a list of states; each state is a *decision list* of rules, and the first rule whose guard matches at the cursor applies. The notation is explained in the header of the grammar itself. In short:

| Part | Meaning |
|---|---|
| `class NAME = ...` | a named set of characters; `UNIT` is the set of characters that can start a new unit |
| `state NAME`, `state NAME(stem)` | a state; L2b has one parameter, the stem, which is the key prefix its caller chose |
| guard `$` | the end of the string (the NUL byte) |
| guard `.` | any character, including the end |
| guard `'ab'` | the characters `a`, `b`, in that order |
| guard `[x y $]` | one character out of the set (`$` is a member only where written) |
| `c`, `d` | the first and second character matched by the guard |
| `emit E` | append the bytes of the table row whose key is E (strings and variables, joined: `stem 'ha'`) |
| `halant` | `emit '^'` |
| `raw V` | append the ASCII character V (nothing for the end of the string) |
| `vocalic 'I' 'D'` | if the output so far ends with the halant byte: remove it and emit row D; otherwise emit row I |
| `skip N` | move the cursor N characters on **without looking at them** |
| `goto S [E]`, `accept` | continue in state S, giving it E as its stem; or stop |
| `+` before a rule | the rule was added by patch 0001, the Sanskrit characters; the unpatched parser is the grammar without the `+` and `!` rules |
| `!` before a rule | the rule is a *guard rule*, added by patch 0002 (section 14.7); the parser of patch 0001 alone is the grammar without the `!` rules, and the parser of this package is the whole grammar |
| `witness: S` in the comment of a `!` rule | the shortest string that shows what the guard rule is for: without the rule, the pairing law of section 14.2 fails on S (checked by `tests/test_underscore.py`, U7) |

The word *guard* has two senses here, and the context tells them apart: the part of a rule before `->`, the condition under which the rule applies; and, for the twelve rules tagged `!`, a *guard rule*, a rule that guards another rule against an underscore or the end of the string. The section titles use the second sense.

A guard (the first sense) that reads beyond the end of the string stops at the NUL byte, so rules are safe there; a `skip` that jumps over the NUL is not, unless a guard rule has seen to it (section 5.4).

### 5.3 The grammar

This block is the single place where the parser is defined. `tests/spec_model.py` reads it from this file and runs it; `tests/diff_parser.py` compares its output with the C parser of the three builds (old, mid and new: section 13) and with the hand-written parser; the tags `+` and `!` select the version of the parser that each build is.
**When the parser changes, change this block and `rmn2acii.c` together, in the same commit.**

```rmn2acii-grammar
# ---------------------------------------------------------------------------------------------------------------------
# rmn2acii: the Romenagri -> ACII translator, as a table of decision lists.
#
#   state NAME [(param)]     a decision list; the rules are tried from the top, the first whose guard matches applies
#   +  rule                  a rule added by patch 0001, the Sanskrit characters (the unpatched parser is this grammar without the '+' and '!' rules)
#   !  rule                  a guard added by patch 0002 (section 14.7); the parser of patch 0001 alone is this grammar without the '!' rules
#   guard  -> actions        guard items, matched left to right at the cursor:  $  end of input (the NUL byte)
#                                                                                .  any character, including the NUL
#                                                                                'ab'  the characters a, b, in that order
#                                                                                [x y $]  one character out of a set
#                            c and d name the first and the second character matched by the guard
#   emit E                   append the bytes of the table row whose key is E (E: quoted strings and variables, joined)
#   halant                   emit '^'                      raw V   append the ASCII character V (nothing for the NUL)
#   vocalic 'I' 'D'          if the output ends with the halant: replace that byte by row D, else emit row I
#   skip N                   move the cursor N characters on -- without looking at them
#   goto S [E]               continue in state S (E becomes its parameter 'stem')          accept   stop
# ---------------------------------------------------------------------------------------------------------------------
class UNIT = | k g c j t d n p b m y r l w s x h _ ^         # the characters that can start a new unit

state L1                                                    # the start of a unit
  $                       -> accept
  '|'                     -> emit '|' ; skip 1 ; goto L1
  [n m y w x r]           -> emit c 'a' ; skip 1 ; goto L2a
  [g t d p b s l k j]     -> skip 1 ; goto L2b c
! 'c' [_ $]               -> raw c ; skip 1 ; goto L1             # no 'h' to skip: the letter c; witness: c__
  'c'                     -> skip 2 ; goto L2b 'ch'         # the letter after the c is skipped unseen (it is the h of "ch")
  '_'                     -> skip 1 ; goto L2c
  '^'                     -> skip 1 ; goto M
  .                       -> raw c ; skip 1 ; goto L1       # anything else (digits, punctuation, stray letters) passes through

state L2a                                                   # a consonant has just been written together with its 'a'
  $                       -> halant ; accept
  [UNIT]                  -> halant ; goto L1               # the next unit starts: the consonant carries a halant
  .                       -> goto M                         # otherwise a vowel (or the explicit 'a') follows

state L2b(stem)                                             # a consonant stem has been read; aspirate or "vra"?
  $                       -> emit stem 'a' ; halant ; accept
  'h'                     -> emit stem 'ha' ; skip 1 ; goto L2a
! 'v' [_ $]               -> emit stem 'a' ; goto L2a             # no 'r' to skip: the stem keeps its 'a'; witness: lv__
  'v'                     -> emit stem 'vra' ; skip 2 ; goto L2a    # only "lvra" is a row; the r is skipped unseen
  .                       -> emit stem 'a' ; goto L2a

state L2c                                                   # after '_': the letters that need an underscore
  $                       -> halant ; accept
  's'                     -> emit '_s' ; skip 1 ; goto L1
  'u'                     -> emit '_u' ; skip 1 ; goto L1
  'm'                     -> emit '_m' ; skip 1 ; goto L1
  'i'                     -> emit '_i' ; skip 1 ; goto L1
! 'e' [_ $]               -> raw c ; skip 1 ; goto L1             # no second 'e' to skip: the letter e; witness: _e__
  'e'                     -> emit '_ee' ; skip 2 ; goto L1  # the second e is skipped unseen
! 'y' [_ $]               -> raw c ; skip 1 ; goto L1             # no 'n' to skip: the letter y; witness: _y__
  'y'                     -> emit '_yna' ; skip 2 ; goto L2a
  't'                     -> skip 1 ; goto L2b '_t'
  'd'                     -> skip 1 ; goto L2b '_d'
  'hh'                    -> emit '_hh' ; skip 2 ; goto L1
  'h'                     -> emit '_ha' ; skip 1 ; goto L2a
  'oo'                    -> emit '_oo' ; skip 2 ; goto L1
  'ow'                    -> emit '_ow' ; skip 2 ; goto L1
  'oa'                    -> emit '_oa' ; skip 2 ; goto L1
  'ou'                    -> emit '_ou' ; skip 2 ; goto L1
+ 'om'                    -> emit '_om' ; skip 2 ; goto L1
! 'o' [_ $]               -> raw c ; skip 1 ; goto L1             # nothing to keep as text: the letter o; witness: _o_
  'o' .                   -> raw d ; skip 2 ; goto L1       # an unknown "_o?": the o is dropped, the next character kept
  'na'                    -> emit '_na' ; skip 2 ; goto L1
  'nn'                    -> emit '_nna' ; skip 2 ; goto L2a
  'ng'                    -> emit '_nga' ; skip 2 ; goto L2a
  'nz'                    -> emit '_nza' ; skip 2 ; goto L2a
! 'n' [_ $]               -> raw c ; skip 1 ; goto L1             # nothing to keep as text: the letter n; witness: _n_
  'n' .                   -> raw d ; skip 2 ; goto L1
  'ri'                    -> vocalic '_ri' '^_ri' ; skip 2 ; goto L1
  'rd'                    -> skip 2 ; goto L2b '_rd'
  'rr'                    -> skip 2 ; goto L2b '_rr'
+ 'ree'                   -> vocalic '_ree' '^_ree' ; skip 3 ; goto L1
! 'r' [_ $]               -> raw c ; skip 1 ; goto L1             # nothing to keep as text: the letter r; witness: _r_
  'r' .                   -> raw d ; skip 2 ; goto L1
  'a' [UNIT $]            -> emit '_a' ; skip 1 ; goto L1
  'aa'                    -> emit '_aa' ; skip 2 ; goto L1
  'aee'                   -> emit '_aee' ; skip 3 ; goto L1
  'ae'                    -> emit '_ae' ; skip 2 ; goto L1
  'ai'                    -> emit '_ai' ; skip 2 ; goto L1
  'ao'                    -> emit '_ao' ; skip 2 ; goto L1
  'au'                    -> emit '_au' ; skip 2 ; goto L1
  'a' .                   -> raw d ; skip 2 ; goto L1
  'jz'                    -> emit '_jza' ; skip 2 ; goto L2a
! 'j' [_ $]               -> raw c ; skip 1 ; goto L1             # nothing to keep as text: the letter j; witness: _j_
  'j' .                   -> raw d ; skip 2 ; goto L1
+ 'li'                    -> vocalic '_li' '^_li' ; skip 2 ; goto L1
+ 'lee'                   -> vocalic '_lee' '^_lee' ; skip 3 ; goto L1
+ 'vd'                    -> emit '_vd' ; skip 2 ; goto L1
+ 'vu'                    -> emit '_vua' ; skip 2 ; goto L2a      # the four accents are written like the nukta:
+ 'vn'                    -> emit '_vna' ; skip 2 ; goto L2a      # the accent, then an explicit 'a', then an
+ 'vg'                    -> emit '_vga' ; skip 2 ; goto L2a      # optional vowel sign
+ 'vc'                    -> emit '_vca' ; skip 2 ; goto L2a
  .                       -> raw c ; skip 1 ; goto L1       # an unknown family letter is kept as plain text (the '_' is lost)

state M                                                     # a vowel sign: after a consonant, or after an explicit '^'
  $                       -> halant ; accept
  'i'                     -> emit '^i' ; skip 1 ; goto L1
  'u'                     -> emit '^u' ; skip 1 ; goto L1
! 'e' [_ $]               -> raw c ; skip 1 ; goto L1             # no second 'e' to skip: the letter e; witness: je__
  'e'                     -> emit '^ee' ; skip 2 ; goto L1  # the second e is skipped unseen
  'z'                     -> emit '^za' ; skip 1 ; goto L2a # the nukta; an 'a' (or a vowel) follows
+ '_li'                   -> emit '^_li' ; skip 3 ; goto L1
+ '_lee'                  -> emit '^_lee' ; skip 4 ; goto L1
+ '_ree'                  -> emit '^_ree' ; skip 4 ; goto L1
! '_' [_ $]               -> goto L1                              # no "ri" to skip: no sign, the '_' is read again in L1; witness: ^__a
! '_' . [_ $]             -> goto L1                              # the same, one character later; witness: ^_^__
  '_'                     -> emit '^_ri' ; skip 3 ; goto L1       # "_ri": the two letters after the '_' are skipped unseen
  'oo'                    -> emit '^oo' ; skip 2 ; goto L1
  'ow'                    -> emit '^ow' ; skip 2 ; goto L1
  'oa'                    -> emit '^oa' ; skip 2 ; goto L1
  'ou'                    -> emit '^ou' ; skip 2 ; goto L1
! 'o' [_ $]               -> raw c ; skip 1 ; goto L1             # nothing to keep as text: the letter o; witness: jo_
  'o' .                   -> raw d ; skip 2 ; goto L1
  'a' [UNIT $]            -> skip 1 ; goto L1               # the inherent 'a': the consonant keeps its vowel
  'aa'                    -> emit '^aa' ; skip 2 ; goto L1
  'aee'                   -> emit '^aee' ; skip 3 ; goto L1
  'ae'                    -> emit '^ae' ; skip 2 ; goto L1
  'ai'                    -> emit '^ai' ; skip 2 ; goto L1
  'ao'                    -> emit '^ao' ; skip 2 ; goto L1
  'au'                    -> emit '^au' ; skip 2 ; goto L1
  'a' .                   -> raw d ; skip 2 ; goto L1
  .                       -> raw c ; skip 1 ; goto L1
```

### 5.4 What the grammar shows

<!-- BEGIN GENERATED stats -->

- `acii.h` 96 rows, `unicode.h` 85 rows, `aciihin.h` 87 rows
- ACII bytes in use: 86 of the 128 bytes `80`-`FF`; free: 42
- parser grammar (section 5.3): 5 states, 95 rules (12 of them added for the Sanskrit characters, 12 guards against the underscore and the end of the string), longest guard 4 characters
- keys the grammar can look up: 102; of these, 15 have no row in `acii.h` (section 11.3)

<!-- END GENERATED stats -->

- **Deterministic, ordered.** Every state is a decision list; there is no backtracking. The order of the rules is part of the definition: in L2c the rule `'om'` must come before `'o' .`, which would otherwise swallow it,
  and in M the rules for `'_li'`, `'_lee'` and `'_ree'` must come before the generic `'_'`, which jumps over two characters without looking at them. A guard rule (tag `!`) stands directly in front of the rule that it guards.
- **Bounded look-ahead.** The longest guard is four characters (`'_lee'` and `'_ree'` in M). The comment in `main.c` that calls the parser LA(1) was true of a smaller scheme.
- **Finite-state.** All control is in the state and the cursor. The one action that reads what has already been written is `vocalic`, and it asks only whether the last byte is the halant. Among the rows that the grammar emits, only the halant itself
  (`^`) ends in the halant byte, so the answer is "yes" exactly when the unit before ended with a halant that L2a wrote because a `_` followed: one bit of extra state. The parser is a finite-state transducer, although the C code is written as mutually recursive functions.
- **Table access.** The grammar touches the table only through the keys it emits. `tools/gen_doc_tables.py` works out from the rules alone which keys that can be (section 11.3).

**Jumps over unchecked characters.** These are the rules whose `skip` is longer than their guard:

<!-- BEGIN GENERATED unchecked-skips -->

| state | rule | characters tested | characters jumped over unseen |
|---|---|--:|--:|
| L1 | `'c' -> ...` | 1 | 1 |
| L2b | `'v' -> ...` | 1 | 1 |
| L2c | `'e' -> ...` | 1 | 1 |
| L2c | `'y' -> ...` | 1 | 1 |
| M | `'e' -> ...` | 1 | 1 |
| M | `'_' -> ...` | 1 | 2 |

<!-- END GENERATED unchecked-skips -->

The parser trusts that the rest of the key follows: the `h` of `ch`, the `r` of `vra`, the second `e` of `_ee` and of `^ee`, the `n` of `_yna`, the two letters after the `_` of `^_ri`. So `_ex` is read as `_ee`, `lvx` as `lvr`, and `^_ro` as `^_ri`.
Before patch 0002 the jump could also swallow an underscore, or leave the string and read what lies beyond its end: undefined behaviour in C, `Overrun` in the executable grammar, and the tests left such strings out (section 11.4). With the guard rules of section 14.7 in front of these rules, they are not taken when the character that they would jump over is an underscore or the end of the string; the grammar of this package never raises `Overrun`, and the grammar without the `!` rules (patch 0001 alone) still does.

**Wildcard rules.** Five more rules have the wildcard `.` as the second item of their guard: the rules for an unknown key `_o?`, `_n?`, `_r?` and `_j?` in L2c and `^o?` in M. They drop the letter and keep the character after it as plain text, whatever it is. Without a guard rule, the wildcard matches the terminator at the end of the input, the rule steps over it, and the parser reads past the end exactly as the six rules above do. Together the eleven rules are the ones that section 14.6 lists; there they matter for a second reason, because a character that they take unseen can be an underscore. Each of them has a guard rule in front of it (section 14.7).

### 5.5 Worked examples

Each step is one rule applied. The tables are generated by running the grammar with `trace` on; the byte strings are the parser's real output.

<!-- BEGIN GENERATED traces -->

`k_rix_nna` gives `B3DFD6E8C1`:

| state | input left | rule applied | output so far |
|---|---|---|---|
| L1 | `k_rix_nna` | `[g t d p b s l k j] -> skip 1 ; goto L2b c` | `-` |
| L2b(k) | `_rix_nna` | `. -> emit stem 'a' ; goto L2a` | `B3` |
| L2a | `_rix_nna` | `[UNIT] -> halant ; goto L1` | `B3E8` |
| L1 | `_rix_nna` | `'_' -> skip 1 ; goto L2c` | `B3E8` |
| L2c | `rix_nna` | `'ri' -> vocalic '_ri' '^_ri' ; skip 2 ; goto L1` | `B3DF` |
| L1 | `x_nna` | `[n m y w x r] -> emit c 'a' ; skip 1 ; goto L2a` | `B3DFD6` |
| L2a | `_nna` | `[UNIT] -> halant ; goto L1` | `B3DFD6E8` |
| L1 | `_nna` | `'_' -> skip 1 ; goto L2c` | `B3DFD6E8` |
| L2c | `nna` | `'nn' -> emit '_nna' ; skip 2 ; goto L2a` | `B3DFD6E8C1` |
| L2a | `a` | `. -> goto M` | `B3DFD6E8C1` |
| M | `a` | `'a' [UNIT $] -> skip 1 ; goto L1` | `B3DFD6E8C1` |
| L1 | `∅` | `$ -> accept` | `B3DFD6E8C1` |

`k_lip_ta` gives `B384C8E8C2`:

| state | input left | rule applied | output so far |
|---|---|---|---|
| L1 | `k_lip_ta` | `[g t d p b s l k j] -> skip 1 ; goto L2b c` | `-` |
| L2b(k) | `_lip_ta` | `. -> emit stem 'a' ; goto L2a` | `B3` |
| L2a | `_lip_ta` | `[UNIT] -> halant ; goto L1` | `B3E8` |
| L1 | `_lip_ta` | `'_' -> skip 1 ; goto L2c` | `B3E8` |
| L2c | `lip_ta` | `+ 'li' -> vocalic '_li' '^_li' ; skip 2 ; goto L1` | `B384` |
| L1 | `p_ta` | `[g t d p b s l k j] -> skip 1 ; goto L2b c` | `B384` |
| L2b(p) | `_ta` | `. -> emit stem 'a' ; goto L2a` | `B384C8` |
| L2a | `_ta` | `[UNIT] -> halant ; goto L1` | `B384C8E8` |
| L1 | `_ta` | `'_' -> skip 1 ; goto L2c` | `B384C8E8` |
| L2c | `ta` | `'t' -> skip 1 ; goto L2b '_t'` | `B384C8E8` |
| L2b(_t) | `a` | `. -> emit stem 'a' ; goto L2a` | `B384C8E8C2` |
| L2a | `a` | `. -> goto M` | `B384C8E8C2` |
| M | `a` | `'a' [UNIT $] -> skip 1 ; goto L1` | `B384C8E8C2` |
| L1 | `∅` | `$ -> accept` | `B384C8E8C2` |

`ka_vuu` gives `B388DD`:

| state | input left | rule applied | output so far |
|---|---|---|---|
| L1 | `ka_vuu` | `[g t d p b s l k j] -> skip 1 ; goto L2b c` | `-` |
| L2b(k) | `a_vuu` | `. -> emit stem 'a' ; goto L2a` | `B3` |
| L2a | `a_vuu` | `. -> goto M` | `B3` |
| M | `a_vuu` | `'a' [UNIT $] -> skip 1 ; goto L1` | `B3` |
| L1 | `_vuu` | `'_' -> skip 1 ; goto L2c` | `B3` |
| L2c | `vuu` | `+ 'vu' -> emit '_vua' ; skip 2 ; goto L2a` | `B388` |
| L2a | `u` | `. -> goto M` | `B388` |
| M | `u` | `'u' -> emit '^u' ; skip 1 ; goto L1` | `B388DD` |
| L1 | `∅` | `$ -> accept` | `B388DD` |

<!-- END GENERATED traces -->

## 6. How the strings are built: the conventions

A Romenagri string that is meant to go into the table is not free text. It has to be read by the parser above as one token, and it has to leave the reading of every existing string unchanged.
The conventions below are what the existing strings have in common; section 8 turns them into a procedure. They are *observed* from the table, checked by the lint (T3, T6, T7), and not stated in the source.

| # | Convention | Examples |
|---|---|---|
| R1 | A key uses `a`-`z` and `_`; a leading `^` marks the dependent (sign) form. Digits, capitals and punctuation are never in a key: the parser copies them to the output, and the filters do not hand them to the parser at all (section 11.1). | `ka`, `_ri`, `^aa` |
| R2 | A consonant key is its stem plus `a`. The `a` is the inherent vowel. In running text the bare consonant is written without `a`, and the parser adds the halant. | `ka` (क), `k` (क्) |
| R3 | The plain letter is the primary reading of the sound. Where Devanagari has two sounds for one Roman letter, the retroflex takes the plain letter and the dental takes the `_` form: `t th d dh` (ट ठ ड ढ) and `_t _th _d _dh` (त थ द ध). The nasals are `_ng _yn _nn n m`, the sibilants `sh x s`, the aspirates add `h`. | `ta` ट, `_ta` त |
| R4 | `h` is reserved for aspiration, so the letter ha is written `_ha`. `w` writes व. | `_ha`, `wa` |
| R5 | An independent vowel is `_` + its spelling. The dependent form is `^` + the spelling without the `_` when the spelling begins with one of the letters that state M reads (`i u e z o a`); otherwise the `_` stays, because M reads `_` as the start of `^_ri`-like keys. | `_aa` / `^aa`, `_i` / `^i`, `_ri` / `^_ri` |
| R6 | Vowel spellings: `a aa i ee u oo ri` for अ आ इ ई उ ऊ ऋ; `ae aee ai` for ऎ ए ऐ; `ow oa ou` for ऒ ओ औ; `ao au` for the candra vowels ऍ ऑ. | `_aee`, `_oa` |
| R7 | A mark written after its base letter ends in `a`, like a consonant, so that the decoder's rule "a following sign pops the `a`" works for it unchanged. The nukta is the model: stem + `z` + `a`. | `kza`, `_nza`, `_vua` |
| R8 | The letter after `_` selects the family: the used letters are listed below. A new family takes a letter that is still free. | `_l`, `_v` (new) |
| R9 | A new key must be parsed as one token by the rules that exist, or the rules must be extended in the same change (section 8). It must not begin with a string that an earlier rule already reads differently: `_dda` is read as `_da` + `da`. | |

The second letters after `_` that the table already uses, and those that are still free:

<!-- BEGIN GENERATED family-letters -->

second letter after `_` already used: `a` `d` `e` `h` `i` `j` `l` `m` `n` `o` `r` `s` `t` `u` `v` `y`

free: `b` `c` `f` `g` `k` `p` `q` `w` `x` `z`

<!-- END GENERATED family-letters -->

Some consequences worth knowing:

- Whatever the lexical layer does not hand to the parser cannot be part of a key: the parser never sees `^`, `|` or digits from the filters (section 11.1).
- The family letter and the plain letter are read in different states (L2c after `_`, L1 at the start of a unit), so one letter can be both: `t` is the retroflex T, and `_t` opens the family of the dental letters (`_ta`, `_tha`, `_tra`...). A letter of the free list is free in L2c; if it is also unused in L1 (`f` and `q`, section 8.5) it could in addition start plain letters.
- The scheme is phonetic, not orthographic: a conjunct is written as its consonants one after the other (`k` + `xa` for क्ष), never as a single key; the multi-byte rows of the table (`kxa`, `_tra`, ...) are not how conjuncts are written (section 11.2).

## 7. The Sanskrit additions

### 7.1 What was added

Twelve characters of the Devanagari block that Sanskrit and Vedic text needs had no ACII byte. Each got one byte, one Romenagri string, and one saral spelling:

<!-- BEGIN GENERATED table-new -->

| ACII | Unicode | Character | Romenagri | saral (acii2hin) |
|---|---|---|---|---|
| `81` | U+090C | LETTER VOCALIC L | `_li` | `lri` |
| `82` | U+0961 | LETTER VOCALIC LL | `_lee` | `lri` |
| `83` | U+0960 | LETTER VOCALIC RR | `_ree` | `ri` |
| `84` | U+0962 | VOWEL SIGN VOCALIC L | `^_li` | `^lri` |
| `85` | U+0963 | VOWEL SIGN VOCALIC LL | `^_lee` | `^lri` |
| `86` | U+0944 | VOWEL SIGN VOCALIC RR | `^_ree` | `^ri` |
| `87` | U+0965 | DOUBLE DANDA | `_vd` | `\|\|` |
| `88` | U+0951 | STRESS SIGN UDATTA | `_vua` | (empty: the mark vanishes) |
| `89` | U+0952 | STRESS SIGN ANUDATTA | `_vna` | (empty: the mark vanishes) |
| `8A` | U+0953 | GRAVE ACCENT | `_vga` | (empty: the mark vanishes) |
| `8B` | U+0954 | ACUTE ACCENT | `_vca` | (empty: the mark vanishes) |
| `8C` | U+0950 | OM | `_om` | `om` |

<!-- END GENERATED table-new -->

None of the twelve has a canonical decomposition in Unicode, so normalisation cannot help (contrast the nukta letters, which the nukta layer of section 15 writes as two bytes, a consonant and the nukta): each needs a byte of its own.
The files that patch 0001 changes, besides the three tables, are those that had to learn the new rows:

| File | Change |
|---|---|
| `unicode.h` | 12 rows appended; `UNI_LEN` 73 to 85 |
| `acii.h` | the avagraha row `_3` renamed `_s`; 12 rows appended; `ACII_LEN` 84 to 96 |
| `aciihin.h` | 12 rows appended; `ACII_HIN_LEN` 75 to 87 |
| `acii2hin.c` | the loop over the table ended at the literal `75`; it now ends at `ACII_HIN_LEN`, otherwise the new rows would never be read |
| `rmn2acii.c` | the helper `vocalic()` and the twelve rules that are marked `+` in the grammar of section 5.3 |
| `TRANSLITERATION.md` | this document |

The decoder, the Unicode converters, the lexers and the Makefile are untouched. The parser keeps its five states and its decision lists; it gained branches, not a new mechanism. Patch 0002 changes only `rmn2acii.c` and this document, and adds twelve tests in front of existing branches, again with no new state (section 14.7). Patch 0003 changes `uni2acii.c`, `acii2uni.c`, the Makefile and this document, and adds the header `nukta.h` (section 15).

**The avagraha.** Byte `EB` (U+093D) was written `_3` by the decoder. That string cannot come back: the lexical layer gives the parser only letters and `_`, so `_3` reaches it as `_`, which writes a halant, followed by a plain `3`
(measured on the unpatched build: `EB` through `acii2rmn | rmn2acii` gives `E8 33`). Meanwhile the parser's own branch for avagraha, written in the source as `case 's': //avagraha _s`, asks for a row `_s` that did not exist, and `rmn2acii` crashed on the input `_s`.
Renaming the row to `_s` makes both directions agree. The byte did not change, so existing ACII files are unaffected.

### 7.2 Why these bytes

The policy is section 10.3. Applied here:

| Bytes | Characters | Reason |
|---|---|---|
| `81`-`8C` | vocalic L, LL, RR; their three signs; double danda; the four accents; OM | ACII's first extension, U+0979 at `80`, already used the block `80`-`9F`. ISCII-91 assigns nothing there and ASCII does not reach it. The twelve characters continue the block in a fixed order: three vowels, three signs, double danda, four accents, OM. |

**Why OM is not at `A0`.** `A0` looks like the natural byte: it is "Sign OM" in this repository's own `iscii_map.csv`, and ACII did not use it. An earlier draft of patch 0001 put OM there, and a test showed that this is wrong.
`uni2acii` writes the *low byte* of every code point it has no row for (section 3.1), and the low byte of U+00A0 NO-BREAK SPACE is `A0`. Before patch 0001 that byte meant nothing: `acii2uni` folded it to a space (`A0` mod 128 is `20`). With OM there, every no-break space in a text
(word processors and web pages produce them freely) would have become ॐ. `tests/test_unicode.py`, part (e), now asserts that none of the common characters outside Devanagari and ASCII reaches one of the new bytes, and `tools/check_tables.py --free` keeps `A0` out of the free list.
The ICU converter points the same way: it reads `A0` as no-break space; Apple's table leaves `A0` unused. Both write OM as the two bytes `A1 E9` (section 12; the conflict is discussed in section 10.5).

**Why single bytes, not ISCII's two-byte sequences.** ISCII-91, as ICU and Apple implement it, writes seven of these characters as an existing code followed by the nukta: `A1 E9` for OM, `A6 E9` for vocalic L, and so on (section 12 has the table). Three things in the architecture rule that out:
`uni2acii` is a table of one byte per code point and cannot write two for these characters (patch 0003 gives it an exception for the eleven nukta letters, and for nothing else, section 15); the decoder handles a nukta only after a consonant (after a vowel, `A6 E9` comes out as the text `_za`, measured); and the task was to find unused bytes in the 8-bit page. A byte per character is what the three tables can express.

### 7.3 Why these strings

Each string follows the conventions of section 6; the second column says which.

| Character | String | Derivation |
|---|---|---|
| ऌ ॡ ॠ | `_li` `_lee` `_ree` | R5, R6: `_` and the spelling of the vowel. Vocalic R is already `_ri`; the L vowel is `li`, and the long forms double the vowel as `_ee` and `_oo` do. The family letter `l` was unused. |
| ॢ ॣ ॄ | `^_li` `^_lee` `^_ree` | R5: a sign is `^` and the vowel's own spelling. The `_` stays, as in `^_ri`, because state M reads a `_` after `^` as the start of such a key. |
| ॥ | `_vd` | a new family `v`, for verse and Vedic signs; `d` for danda. `_dd` would have been read as `_d` and `d`. The double danda cannot be `\|\|`: the filters never give `\|` to the parser (section 11.1). It has no final `a`, because nothing attaches to it. |
| ॑ ॒ ॓ ॔ | `_vua` `_vna` `_vga` `_vca` | the same family: u(datta), (a)n(udatta), g(rave), c(acute). R7: an accent attaches to the letter before it, so it is written like the nukta, with an explicit `a` at the end. |
| ॐ | `_om` | the family `_o` already held the O vowels (`_oo`, `_ow`, `_oa`, `_ou`); `_om` extends it. Without `_` the string `om` would be Latin text (section 5.1, L1). |

Three things could have gone wrong and were checked. (1) *Existing text changes meaning.* Before patch 0001 `_l`, `_v` and `_om` were garbage: `_li` read as the plain text `li` with the `_` lost. `tests/diff_parser.py` compares the old and the mid parser (the parser of patch 0001 alone) on more than a million strings
and requires that every string whose reading changed contains one of the new tokens. (2) *The new string extends an old token.* Lint check T7 tries, for every consonant C and every letter X, the sequences C + halant + X and X + C. (3) *The decoder must give the string back.* T6 checks both directions for every key.

### 7.4 What the parser does with them

The twelve new rules are three kinds, and they are the three recipes of section 8.

- **Independent vowel or sign that stands alone** (`_om`, `_vd`): emit the row, go to L1.
- **A vowel with a sign form** (`_li`, `_lee`, `_ree`): `vocalic`. After a consonant the parser has already written the halant, because it saw `_` and a new unit began; `vocalic` replaces that halant by the sign. So `k_li` is क + ॢ and `k` + `_li` cannot be क + ् + ऌ.
  This is how `_ri` has always worked (`k_ri` is कृ; the code is inline in `level2c`, and patch 0001 leaves it as it was). The new vowels copy it in the helper `vocalic()`; the grammar writes all four with the same action.
  The explicit form `^_li` is a sign that stands alone, at the start of a line for instance, where no consonant is before it (the decoder writes a sign with its `^` when its stack is empty). It reaches state M, which has a rule for each of the three new signs.
- **A mark that attaches** (`_vua` and the other accents): emit the row and go to L2a, which expects the `a` that the key ends in and then an optional vowel sign.

Worked traces for `k_lip_ta` (क + ॢ + प् + त) and `ka_vuu` (क + udatta + sign U) are in section 5.5.

### 7.5 The saral table

`aciihin.h` is one-way and lossy, so the new rows follow the style of the old ones: the vocalic letters are `lri` and `ri` (length is dropped, as it is for ई), the signs are `^lri` and `^ri`, OM is `om`, the double danda is `||`, and the accents are empty: they vanish.
`tests/test_acii2hin.py` pins these and checks that every old byte and byte pair renders as before.

## 8. How to extend: the recipes

### 8.1 The checklist common to all recipes

1. **Classify the character** (section 10.4). A digit is `fixuninum`'s business. A precomposed nukta letter needs no byte: the nukta layer (section 15) writes it as its consonant and the nukta. Only an *uncovered* character needs the rest of this section.
2. **Choose the byte** by the policy of section 10.3 and confirm with `python3 tools/check_tables.py Romenagri --free`.
3. **Choose the string** by the conventions of section 6.
4. **Edit the three tables.** Append one row to `unicode.h` (`{low, high, '\xNN'}`, the code point split into its low and high byte), one to `acii.h` (`{"key", "\xNN"}`) and one to `aciihin.h` (`{"saral", "\xNN"}`; an empty string is allowed). Raise `UNI_LEN`, `ACII_LEN` and `ACII_HIN_LEN`. **Append, never reorder or delete:** both translators take the first row that matches (section 3.2), so row order is part of the meaning.
   The three headers use CRLF line endings and contain raw 8-bit bytes. An editor that converts them to UTF-8 or to LF corrupts the tables; write new bytes as `\xNN` escapes, as patch 0001 does.
5. **Run the lint** (`python3 tools/check_tables.py Romenagri`). No complaint means the parser already reads the string as one token: recipe A, nothing more to do in the parser. `T6 key '...' parses to ...` means it reads the string as something else: write a rule, by recipe B, C, D or E, and change the grammar of section 5.3 and `rmn2acii.c` in the same commit. Mirror the rule in `tests/handwritten_parser.py`, or run the differential test with `RMN_SKIP_HANDWRITTEN=1`. If the rule jumps over characters that it has not looked at, it also needs a guard rule (recipe B, step 3).
6. **Regenerate the document's tables:** `python3 tools/gen_doc_tables.py --write Romenagri`; describe the character in sections 7 and 10.
7. **Run the tests** (section 13). `tests/rt_filters.py` asserts the exact list of new bytes and lists the analogue of each (`NEWB` and `PHI`): add yours. To compare against a baseline other than the unpatched sources, name its `Romenagri` directory in `RMN_BASELINE`.

`tests/test_extension_recipes.py` carries out recipe A and the mistakes of step 5 on scratch copies of the tree and checks that the lint and the build behave as described below.

### 8.2 Recipe A: tables only

*When:* the parser already asks for the string. It asks for 15 keys that the table lacks (section 11.3). Of the 15, only `lha` could name a character that exists in Unicode (ऴ, U+0934), and there the spelling is contested: `lh` is also how people type the conjunct ल्ह. The worked example below is therefore a demonstration of the mechanism, which is the only table-only extension there is, and not a recommendation.

*Worked example, an illustration that is not shipped:* U+0934 DEVANAGARI LETTER LLLA (section 10.4 says why it is not). ISCII gives the character the byte `D3` ("Consonant ZHA"; Apple's table agrees), which ACII does not use. The edit is three rows and three lengths:

```c
/* unicode.h */  {52, 9, '\xD3'}          /* U+0934: 0x34 = 52, 0x09 = 9 */
/* acii.h    */  {"lha", "\xD3"}
/* aciihin.h */  {"lha", "\xD3"}
```

Result, as measured by the test: `lha` gives `D3`, `lh` gives `D3 E8`, `lhaa` gives `D3 DA`, `kalha` gives `B3 D3`; the filter pair restores `D3`, `D1 D3`, `B3 E8 D3` and `D3 DB D1`; `uni2acii` writes `D3` for U+0934 and `acii2uni` reads it back; and of all strings up to length 3 and all table keys, only those containing `lh` change their result. Before the edit the parser of this package crashes on `lha` and `lh`. With the nukta layer (section 15) U+0934 already goes through the pipeline as `D2 E9`; the recipe then gives it a second, one-byte spelling, as U+0929 and U+0931 have (`C7` and `C6 E9`, `D0` and `CF E9`), and `uni2acii` prefers the row of the table.

### 8.3 Recipe B: a new key that needs a parser rule

*When:* the lint says T6, or you chose a string the parser reads differently. This is the case of `_li`, `_om` and `_vd`.

1. **Find the state.** A key that starts with `_` is a rule of L2c (the letter after `_` is its guard). A new plain letter at the start of a unit is a rule of L1, and then the letter must also be added to the class `UNIT` of the grammar and to the string `lev1` of `rmn2acii.c`: both mean "this letter starts a unit", and L2a decides between "halant" and "vowel follows" by them. A sign after a consonant is a rule of M.
2. **Place the rule.** Rules are tried from the top. A rule whose guard is longer than that of another rule with the same beginning goes first (`'om'` before `'o' .`, `'ree'` before `'r' .`), and the catch-all `.` stays last. Nothing that an existing rule reads properly may reach the new rule: that is what the differential test checks.
3. **Write the actions.** `emit K ; skip N ; goto S`, where N counts every character of the key after the cursor (the guard, and any characters the rule trusts to follow); S is L1 for a complete unit, L2a if an `a` or a vowel sign may follow, L2b with a stem if an `h` may follow.
   **If N is larger than the number of characters that the guard matched, the rule trusts a character to follow, and it needs a guard rule** (section 14.7): the same rule with `[_ $]` in the place of the trusted character, tagged `!`, placed directly in front of it, with a `witness:` in its comment, and with the action `raw c ; skip 1 ; goto L1` (the letter is plain text), or the rule's own action cut short where the plain-text reading is not the right one (the guards of L2b `v` and of M `_`). Without it an underscore that follows the key is swallowed, the pairing of `__` (section 14.2) is lost, and at the end of the string the parser reads beyond it.
4. **Mirror it in C**, in the function of the same state, in the form of its neighbours: `strcat (msg, lookup ("key")); tok += N; level1 (tok); break;`. Every call stays the last thing its branch does.
5. **Run `tests/diff_parser.py`.** It compares the grammar with the C parser (old, mid and new build) and lists every string whose reading changed; each must contain a new token, or the grammar must have applied a guard rule. An unexplained change is a rule that stole an old input. Then run `tests/test_underscore.py`: its test U7 fails, and names the rule, for every rule that takes an underscore or the end of the string unseen and has no guard rule.

*Example, from patch 0001:* `_li`. L2c gets `+ 'li' -> vocalic '_li' '^_li' ; skip 2 ; goto L1`, and `rmn2acii.c` gets `case 'l':` with the branches shown in the diff. M gets `+ '_li' -> emit '^_li' ; skip 3 ; goto L1` for the explicit sign, placed before the generic `'_'` rule.

### 8.4 Recipe C: a mark that attaches to the letter before it

*When:* the character is written after a consonant or a vowel sign and has no meaning alone (the accents; in principle any further combining mark).

Write it like the nukta: the key ends in `a`, and the rule goes to L2a. Both halves are forced.

- *Decoder.* A following vowel sign pops the last character of what is on top of the stack; the `a` is meant to be popped. If the key did not end in `a`, a sign after the mark would eat a letter of the key.
- *Parser.* After the mark the parser is in L2a, which writes a halant at the end of the string or before the next unit unless an `a` follows (rule M, `'a' [UNIT $]`). The explicit `a` is what makes the mark inert.

*Example:* `_vua`; traces of `ka_vuu` in section 5.5. The test generator allows `[accent] [sign] [accent]` after a consonant (section 9).

### 8.5 Recipe D: a new consonant

A consonant row is its stem plus `a` (R2), and the parser reaches it through L1 or L2c and then continues in L2a: the halant logic costs nothing. Four cases:

- *A nukta variant of an existing consonant* (क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़ ऩ ऱ ऴ): nothing. The nukta is a separate mark (`kza` is `ka` and `E9`), and the nukta layer (section 15) writes the single code points of Unicode as that pair, so nothing has to be normalised first.
- *An aspirate or a `vra` form of an existing stem:* the string is built by L2b and may already be a reserved key (recipe A).
- *A letter with a free plain Latin letter.* `f` and `q` are not used at the start of a unit (nor are `v` and `z`, but `z` is the nukta after a consonant and `v` follows stems, so they would be confusing). Add an L1 rule `[f] -> emit c 'a' ; skip 1 ; goto L2a` (or `goto L2b c` if an aspirate exists), add the letter to `UNIT` and to `lev1`, and note that existing text with that letter at the start of a unit, which is copied through today, changes.
- *A letter behind `_`:* an L2c rule, `'xy' -> emit '_xya' ; skip 2 ; goto L2a`, as for `_nga` and `_yna`.

### 8.6 Recipe E: a new vowel with a sign form

Use `_` and the spelling for the independent vowel and `^_` and the spelling for the sign, and write the L2c rule with `vocalic` and the M rule for the explicit form, exactly as for `_li` (recipe B). Give both rows their bytes; the independent vowel and the sign are different bytes in ISCII and in ACII.
The one thing that cannot be expressed is a halant directly followed by the *independent* vowel: `k_li` is always क + ॢ (section 11.5).

### 8.7 Recipe F: repair or retire a row

The lint finds defects (T3 a character outside `[a-z_]`, T6 a key the parser reads differently, T7 a key that disturbs its neighbours). The avagraha row was repaired by renaming its key and keeping its byte: no ACII file changes, and the Romenagri spelling of the character begins to work.
A row that nothing uses (section 11.2) can stay: it costs nothing and deleting it moves every later row. Never reorder rows to "tidy"; reorder only to change on purpose which row the decoder finds first.

## 9. The round-trip contract

### 9.1 The statement

Let `W` be the set of ACII texts defined by the grammar below. For every text in `W`, `acii2rmn` followed by `rmn2acii` (with filter semantics: the second program sees every run of `[A-Za-z_]` separately) returns the same bytes. This holds for the mid and the new build, and the guards of patch 0002 are invisible on `W`: every sequence of up to three bytes of `W` gives the same result on both and round-trips on the new one (section 14.7, `tests/rt_filters.py`). The unpatched build satisfies the contract for the old repertoire except at the avagraha.
`tests/rt_filters.py`, part (4), generates random members of `W` and requires every one to round-trip. At the Unicode end, every code point that `unicode.h` maps survives `uni2acii` and `acii2uni` (`tests/test_unicode.py`); a consonant followed by the nukta comes back as that pair in the default form and, with `-f nfc` on both converters, as the single code point where NFC composes the pair (section 15).

### 9.2 Well-formed ACII

```
text      = { syllable | SPACE } ;
syllable  = body [ modifier ] ;
body      = vowel [ accent ]
          | AVAGRAHA | DOUBLE-DANDA | OM
          | cluster ( HALANT | [ accent ] [ sign ] [ accent ] ) ;
cluster   = consonant [ nukta ] { HALANT consonant [ nukta ] } ;
```

A syllable that ends in a halant is followed by a space or by the end of the text. The sets, as bytes:

| Name | Members |
|---|---|
| vowel | `A4`-`B2` and `81` `82` `83` (vocalic L, LL, RR) |
| consonant | `B3`-`D8` and `80` |
| sign | `DA`-`E7` and `84` `85` `86` (vocalic signs) |
| accent | `88` `89` `8A` `8B` |
| modifier | `A1` `A2` `A3` (candrabindu, anusvara, visarga) |
| AVAGRAHA, DOUBLE-DANDA, OM | `EB`, `87`, `8C` |
| HALANT, nukta | `E8`, `E9`; a nukta only after one of the eleven consonants KA KHA GA JA DDA DDHA PHA YA NA RA LLA (`B3` `B4` `B5` `BA` `BF` `C0` `C9` `CD` `C6` `CF` `D2`) |
| SPACE | ASCII `20` |

### 9.3 What the contract leaves out

Everything that is not in `W` may work, but nothing promises it. The cases that are known to fail are in section 11; the ones that are easy to meet are:

- a halant followed directly by an *independent* vocalic vowel: it comes back as the sign (`B3 E8 AA` returns `B3 DF`; the same for `81`, `82`, `83`). The generator ends a word after a final halant for this reason;
- a vowel sign, a halant or a nukta in a place the grammar does not allow (after a space, after a vowel, after another sign): the decoder pops whatever is on top of the stack, and the result is garbage or, for a nukta on an almost empty stack, a crash (section 11.4);
- the danda (`EA`): the decoder writes `|`, and the filters pass `|` through as the ASCII character `7C` (section 11.1);
- runs longer than the buffer limits (section 11.4);
- ASCII letters, digits and punctuation: these are the lexers' business, not the translators'.

### 9.4 Keeping the contract when extending

A new character that can occur in running text belongs in the generator of `tests/rt_filters.py` and in the grammar above, in the same change. A character that must not occur in a certain position is a reason to say so in section 11, not to leave it out of the test silently.

## 10. Larger character sets, character-set conflicts, missing sounds

This section turns sections 3 to 9 into procedures. None of them changes the architecture: the tables stay ordered first-match lists, the parser stays a decision-list automaton, the decoder stays a stack machine. Where a procedure would need to change one of these, the text says so and says what it would cost.

Three rules govern everything below.

- **G1. Append; never change a meaning.** Existing ACII files and Romenagri sources must keep their meaning. A row is added at the end of its table, an existing key never gets another meaning, an existing byte never gets another character (section 3.2 explains why the row order is part of the meaning).
- **G2. One meaning per byte and per key inside; conflicts are settled at the boundary.** What another standard says about a byte is handled by a rewrite *before* `uni2acii` or *after* `acii2uni`, never by giving the byte a second meaning inside (section 10.5).
- **G3. Every change passes the same checks:** the lint (tables), the differential test (parser against the grammar), the round-trip test (decoder and parser together) and the Unicode test (section 13). Section 10.7 states what they establish.

### 10.1 How much room is left

ACII has 128 upper-half bytes. The free ones, by the class that decides what each may be used for (`python3 tools/check_tables.py Romenagri --free` prints the same list byte by byte):

<!-- BEGIN GENERATED free-bytes -->

| Class | Bytes | Count | Use |
|---|---|--:|---|
| C1 extension block | `8D`-`9F` | 19 | first choice for a new character with no ISCII byte |
| ISCII-assigned, unused by ACII | `CE`, `D3`, `D9` | 3 | only for the character ISCII gives it (`CE` Consonant JYA (Bengali, Assamese & Oriya); `D3` Consonant ZHA (Tamil & Malayalam); `D9` Consonant INVISIBLE) |
| ISCII-unassigned | `EC`-`EE`, `FB`-`FF` | 8 | second choice |
| ISCII digits | `F1`-`FA` | 10 | reserved for Devanagari digits (fixuninum currently turns them into ASCII digits) |
| avoided | `A0` | 1 | U+00A0 NO-BREAK SPACE reaches this byte through the low-byte fallback of `uni2acii` (section 11.6); a character placed here would replace every no-break space. The repository's CSV calls the byte "Sign OM"; OM is at `8C` for this reason |
| ISCII extension prefix | `F0` | 1 | never: `EXT` introduces a following byte |
| **free in total** | | **42** | `EF` (attribute prefix) is used, not free |

<!-- END GENERATED free-bytes -->

What is still missing from the Devanagari block (section 10.4 lists the characters):

<!-- BEGIN GENERATED supply-demand -->

- code points of the Devanagari block U+0900-U+097F that `unicode.h` does not map: **43**
  - 10 digits (rewritten to ASCII digits by `fixuninum` before `uni2acii`, by design)
  - 9 precomposed nukta letters (written by `uni2acii` as the byte of the consonant and the nukta byte `E9`: the nukta layer, section 15)
  - 24 characters that nothing covers yet
- free ACII bytes: **42**; of these 19 (the free part of the C1 block `80`-`9F`) plus 8 (ISCII-unassigned) can hold a new character, 3 are reserved for characters ISCII itself gives them, 10 for digits, 1 is avoided (no-break space) and 1 is never used
- so the 24 uncovered characters fit into the 27 allocatable single bytes with 3 to spare

<!-- END GENERATED supply-demand -->

The Devanagari block can therefore be covered completely with single bytes. Larger repertoires cannot. In Unicode 15.1 (the version of the `unicodedata` module that was used to count) the Vedic Extensions block (U+1CD0-U+1CFA) has 43 assigned characters and Devanagari Extended (U+A8E0-U+A8FF) has 32. Together they are 75, for the 27 bytes that can still be allocated. What can be done when single bytes run out:

| Option | Gives | Cost |
|---|---|---|
| the ten digit bytes `F1`-`FA` | 10 | free only as long as `fixuninum` keeps turning digits into ASCII digits; spends the option of keeping native digits as ISCII digits |
| ISCII's extension code `F0` followed by a byte (ICU writes the anudatta as `F0 B8`) | as many characters as the second byte allows | **changes the architecture**: `unicode.h` holds one byte per code point, and the decoder compares only the *first* byte of an `acii.h` row, so the decoder, `uni2acii` and `acii2uni` would all have to learn pairs |
| a second table selected by ISCII's attribute code `EF` | a whole table per attribute | the same, and the decoder today throws away the byte after `EF` |

Nothing in this package implements the last two. They are listed so that the choice is made knowingly when the 27 bytes are near their end. A character above U+FFFF cannot be written at all by the three tables (section 11.6).

### 10.2 What a character needs, layer by layer

| Layer | File | What the character needs there |
|---|---|---|
| Unicode and ACII | `unicode.h` | a row `{low, high, byte}`. Any code point of the Basic Multilingual Plane can be written. |
| ACII and Romenagri, decoder | `acii.h` | a row `{key, bytes}` whose first byte is the new byte; the decoder takes the key from the first row that starts with the byte |
| Romenagri and ACII, parser | `acii.h`, `rmn2acii.c` | the key must be read by the parser as one token; a rule if it is not (recipes B to E, section 8) |
| saral | `aciihin.h` | a row; an empty string if the character should vanish from the simple spelling |
| other scripts | `flatten_uni_dev` | nothing if the letter has a Devanagari counterpart (next paragraph) |

**Other scripts.** The repository carries the other Indic scripts the way ISCII does, through one pivot repertoire. `gen_flatten_uni_dev` reads `iscii_map.csv`, which has one row per ISCII code and the letter of each of ten scripts in it (Devanagari, Bengali, Assamese, Gurmukhi, Gujarati, Oriya, Tamil, Telugu, Kannada, Malayalam), and writes the lexer `flatten_uni_dev.lex`: every letter of another script is replaced by the Devanagari letter in the same row. (The Makefile does not build that lexer; the repository carries a built `flatten_uni_dev`.) The text is Devanagari after that, and everything in this document applies to it. In the other direction `fltr_hi_te`, `fltr_te_hi`, `fltr_hi_ur` and `fltr_ur_hi` are `sed` scripts that replace letters one by one between Devanagari and Telugu or Urdu (the Urdu ones with `urdu_map.csv` and `ur_ar_delta`). So a letter of another script is one of two cases.

- It has a Devanagari counterpart already in the tables: nothing to do in Romenagri; its row in `iscii_map.csv` is what makes it work.
- It has none (Tamil ழ and Malayalam ഴ, which the CSV maps to U+0934; the letters of Sinhala, which `iscii_map.csv` does not cover): a pivot character must be chosen, a Devanagari-block code point if Unicode has one, and the pivot character is then a new character for the tables (sections 10.4 and 8). U+0934 is the live example: `flatten_uni_dev` writes it, `unicode.h` has no row for it, and `uni2acii` wrote the digit `4` for it until the nukta layer (section 15) made it write `D2 E9`, the byte of ळ and the nukta.

### 10.3 Choosing the byte

The order of preference, and the test that guards it:

| Order | Class | Rule |
|---|---|---|
| 1 | a byte that ISCII-91 assigns to this very character | `D3` for U+0934, `CE` for the JYA letter of Bengali, Assamese and Oriya, `D9` for the "invisible" consonant. ISCII text that contains the character then needs no rewrite. Apple's table and ICU agree that `D3` is U+0934. |
| 2 | the C1 block `8D`-`9F` | no meaning in ISCII or ASCII, and no character of the Latin-1 Supplement, of Latin Extended-A, of General Punctuation or of the currency block has its low byte there (test (e), below). Letters of other scripts do (Greek capitals `91`-`A9`, Ukrainian Ґ ґ `90` `91`, Urdu ڈ `88` and ڑ `91`), and so do arrows and mathematical operators; every upper-half byte is exposed to something. |
| 3 | the ISCII-unassigned bytes `EC`-`EE`, `FB`-`FF` | free, but the low bytes of Latin-1 letters (ì í î û ü ý þ ÿ) |
| never | `EF`, `F0`, `F1`-`FA`, `A0` | `EF` and `F0` are ISCII's prefixes; `F1`-`FA` are reserved for digits; `A0` is the low byte of the no-break space |

**The low-byte test.** A byte is *exposed* when a character of real text has it as its low byte: `uni2acii` writes such a character as that byte (section 11.6), and `acii2uni` then reads it as whatever the table says. Almost every exposure is a corruption that existed before: é comes back as a nukta, because `E9` is the nukta. One is not. The no-break space came back as an ordinary space, which is harmless, and `A0` is the byte it lands on. A byte that is harmless today must not be given a meaning, or a harmless fallback becomes a harmful one. This is the reason why OM is at `8C` and not at `A0` (section 7.2). `tests/test_unicode.py`, part (e), keeps a list of everyday characters and requires that none of them lands on a new byte and that each comes out as it did before the change; add to the list when a byte is allocated, and `tools/check_tables.py --free` keeps `A0` off the free list.

### 10.4 Classifying a Unicode character

For a code point `u` that the text may contain, in this order:

1. **A digit.** `fixuninum` rewrites the digits of the Indic scripts to ASCII digits before `uni2acii`; the Devanagari digit bytes `F1`-`FA` stay unused.
2. **Mapped.** `unicode.h` has a row for it. Done.
3. **A precomposed nukta letter.** Unicode gives it a canonical decomposition into a consonant and the nukta, U+093C: U+0929, U+0931 and U+0934, which NFC composes, and U+0958-U+095F, which are composition exclusions and stay decomposed even in NFC. Two of the eleven, U+0929 and U+0931, have a row in `unicode.h`. For the other nine the **nukta layer** (patch 0003, section 15) makes `uni2acii` write the byte of the consonant and `E9`, so no normalisation is needed before it, and the NFC form and the NFD form of the text give the same bytes. (In the default form the NFC and the NFD spelling of U+0929 and U+0931 give different bytes, `C7` and `C6 E9`, `D0` and `CF E9`; with `-f nfc` or `-f nfd` on `uni2acii` they give the same bytes, section 15.2.) (Before patch 0003 the text had to be normalised to NFD, and the NFD step had to be the last one before `uni2acii`, because `flatten_uni_dev` can write U+0934 itself and an NFC step after the NFD one would recompose it. For these letters the order no longer matters.) The layer does not reorder marks: a nukta that follows a halant stays where it is (section 15.5).
4. **A letter of another script** with a Devanagari counterpart: flatten it (section 10.2).
5. **Uncovered.** It needs a byte, a key, possibly a parser rule, and a saral spelling: section 8. The list for the Devanagari block:

<!-- BEGIN GENERATED unmapped -->

| Code point | Category | Name | Class | `uni2acii` writes | Remedy |
|---|---|---|---|---|---|
| U+0900 | Mn | sign inverted candrabindu | uncovered | `00` | needs a byte and a string (section 8) |
| U+0904 | Lo | letter short a | uncovered | `04` | needs a byte and a string (section 8) |
| U+0934 | Lo | letter llla | nukta | `D2 E9` | = U+0933 U+093C: the nukta layer (section 15) |
| U+093A | Mn | vowel sign oe | uncovered | `3A` | needs a byte and a string (section 8) |
| U+093B | Mc | vowel sign ooe | uncovered | `3B` | needs a byte and a string (section 8) |
| U+094E | Mc | vowel sign prishthamatra e | uncovered | `4E` | needs a byte and a string (section 8) |
| U+094F | Mc | vowel sign aw | uncovered | `4F` | needs a byte and a string (section 8) |
| U+0955 | Mn | vowel sign candra long e | uncovered | `55` | needs a byte and a string (section 8) |
| U+0956 | Mn | vowel sign ue | uncovered | `56` | needs a byte and a string (section 8) |
| U+0957 | Mn | vowel sign uue | uncovered | `57` | needs a byte and a string (section 8) |
| U+0958 | Lo | letter qa | nukta | `B3 E9` | = U+0915 U+093C: the nukta layer (section 15) |
| U+0959 | Lo | letter khha | nukta | `B4 E9` | = U+0916 U+093C: the nukta layer (section 15) |
| U+095A | Lo | letter ghha | nukta | `B5 E9` | = U+0917 U+093C: the nukta layer (section 15) |
| U+095B | Lo | letter za | nukta | `BA E9` | = U+091C U+093C: the nukta layer (section 15) |
| U+095C | Lo | letter dddha | nukta | `BF E9` | = U+0921 U+093C: the nukta layer (section 15) |
| U+095D | Lo | letter rha | nukta | `C0 E9` | = U+0922 U+093C: the nukta layer (section 15) |
| U+095E | Lo | letter fa | nukta | `C9 E9` | = U+092B U+093C: the nukta layer (section 15) |
| U+095F | Lo | letter yya | nukta | `CD E9` | = U+092F U+093C: the nukta layer (section 15) |
| U+0966 | Nd | digit zero | digit | `66` | ASCII digit 0 |
| U+0967 | Nd | digit one | digit | `67` | ASCII digit 1 |
| U+0968 | Nd | digit two | digit | `68` | ASCII digit 2 |
| U+0969 | Nd | digit three | digit | `69` | ASCII digit 3 |
| U+096A | Nd | digit four | digit | `6A` | ASCII digit 4 |
| U+096B | Nd | digit five | digit | `6B` | ASCII digit 5 |
| U+096C | Nd | digit six | digit | `6C` | ASCII digit 6 |
| U+096D | Nd | digit seven | digit | `6D` | ASCII digit 7 |
| U+096E | Nd | digit eight | digit | `6E` | ASCII digit 8 |
| U+096F | Nd | digit nine | digit | `6F` | ASCII digit 9 |
| U+0970 | Po | abbreviation sign | uncovered | `70` | needs a byte and a string (section 8) |
| U+0971 | Lm | sign high spacing dot | uncovered | `71` | needs a byte and a string (section 8) |
| U+0972 | Lo | letter candra a | uncovered | `72` | needs a byte and a string (section 8) |
| U+0973 | Lo | letter oe | uncovered | `73` | needs a byte and a string (section 8) |
| U+0974 | Lo | letter ooe | uncovered | `74` | needs a byte and a string (section 8) |
| U+0975 | Lo | letter aw | uncovered | `75` | needs a byte and a string (section 8) |
| U+0976 | Lo | letter ue | uncovered | `76` | needs a byte and a string (section 8) |
| U+0977 | Lo | letter uue | uncovered | `77` | needs a byte and a string (section 8) |
| U+0978 | Lo | letter marwari dda | uncovered | `78` | needs a byte and a string (section 8) |
| U+097A | Lo | letter heavy ya | uncovered | `7A` | needs a byte and a string (section 8) |
| U+097B | Lo | letter gga | uncovered | `7B` | needs a byte and a string (section 8) |
| U+097C | Lo | letter jja | uncovered | `7C` | needs a byte and a string (section 8) |
| U+097D | Lo | letter glottal stop | uncovered | `7D` | needs a byte and a string (section 8) |
| U+097E | Lo | letter ddda | uncovered | `7E` | needs a byte and a string (section 8) |
| U+097F | Lo | letter bba | uncovered | `7F` | needs a byte and a string (section 8) |

<!-- END GENERATED unmapped -->

Whether any of the 24 uncovered characters should be added depends on which texts the tables are meant to carry; they are named in the table, and none of them is one of the characters of section 7. The method is the same for each (section 8).

**Two characters outside the block.** Devanagari text also uses U+200C ZERO WIDTH NON-JOINER and U+200D ZERO WIDTH JOINER after the halant, to choose between a conjunct, a half form and a visible halant. They are not in the Devanagari block, so the list above does not show them, and `unicode.h` has no row for either: they fall back to the bytes `0C` and `0D` and come back as a form feed and a carriage return (section 11.6). ISCII writes the pairs *halant, ZWNJ* and *halant, ZWJ* as `E8 E8` (the "explicit halant") and `E8 E9` (the "soft halant"); Apple's table and ICU's converter agree (conflict C8). This package does not add them: they are format characters, not letters or signs, and the request was for the characters of the Devanagari block that Sanskrit needs. Adding them would take two bytes of the C1 block (section 10.1), two keys, and a decoder and parser that know that a joiner follows a halant (recipes B and C, section 8). Until then the pairs are misread, as section 11.5 shows.

*A tested recipe that is not shipped.* U+0934 is the one nukta letter that the pipeline can produce by itself, because `flatten_uni_dev` writes it for Tamil and Malayalam; since patch 0003 it goes through as `D2 E9` (Romenagri `lvrza`, section 15), and the recipe is no longer needed to keep it from being corrupted. Recipe A (section 8.2) would add it as the single byte `D3`, key `lha`, in three rows; `tests/test_extension_recipes.py` carries it out on a scratch copy and checks it. It is not in the shipped tables because U+0934 is not a Sanskrit character, because it changes what the Hindawi pipeline does with Tamil and Malayalam text, which is for the owner of that pipeline to decide, and because the key `lha` is also the natural reading of the typed conjunct ल्ह (`lh`), which Hindi and Marathi need far more often (section 11.3). A key that does not collide, such as `_la`, needs a parser rule (recipe B).

### 10.5 Conflicts between standards and files

A *conflict* is a case where two sources that the project has to respect say different things about the same byte, character or spelling. The cases that are known:

| # | Conflict | Sources | Settled by |
|---|---|---|---|
| C1 | byte `A0`: Sign OM, no-break space, or unused | `iscii_map.csv` and the chart in Wikipedia: OM. ICU: U+00A0. Apple's table: unused. | ACII leaves it unused and avoided; OM is `8C` (section 7.2) |
| C2 | OM, vocalic L, LL, RR and their three signs, avagraha: one byte in ACII, **two bytes (a code and the nukta)** in ISCII as ICU and Apple implement it | ICU `ucnvisci.cpp`, Apple `DEVANAGA.TXT`; Wikipedia's nukta table | a rewrite at the boundary, below; the rewrite is **not** in this package |
| C3 | double danda: `EA EA` (ICU), `90` (Apple), `87` (ACII) | ICU, Apple | the same rewrite |
| C4 | "ZHA": ISCII's `D3` is U+0934; ACII's `80` is U+0979 | `iscii_map.csv`, `unicode.h` | both stand: they are different characters; `D3` stays free for U+0934 (recipe A); U+0934 itself is written `D2 E9` by the nukta layer (section 15) |
| C5 | avagraha: `EB` in ACII (an extension of this project), `EA E9` in ISCII | ICU, Apple | both stand; the rewrite maps one to the other |
| C6 | spellings: ISO 15919's 7-bit form writes the vocalic letters `,r` `,rr` `,l` `,ll` and the marks `;m` `.h`; Romenagri writes `_ri` `_ree` `_li` `_lee` | `iso15919_map.csv` | a separate table outside the parser: the lexical layer hands the parser only letters and `_` (section 11.1), so punctuation can never be part of a key |
| C7 | many-to-one: the CSV gives four different Perso-Arabic letters (ذ ض ظ ژ) the same Devanagari spelling झ़ | `iso15919_map.csv` | the merger is a decision that the table records; add a character if the distinction matters (section 10.6) |
| C8 | explicit and soft halant: ISCII writes the halant followed by ZWNJ (U+200C) as `E8 E8`, and the halant followed by ZWJ (U+200D) as `E8 E9` | Apple `DEVANAGA.TXT`, ICU `ucnvisci.cpp` | not settled: ACII has no byte and no key for either character (section 10.4), and the decoder misreads the pairs (section 11.5) |

**The rewrite for real ISCII.** ICU and Apple write the characters of C2 and C3 as follows, and a program that reads real ISCII text and feeds it to this chain has to translate before `uni2acii`'s output reaches the decoder (or work in Unicode, where ICU's converter already does it):

| ISCII-91 (ICU and Apple) | Character | ACII |
|---|---|---|
| `A1 E9` | OM | `8C` |
| `A6 E9`, `A7 E9`, `AA E9` | vocalic L, LL, RR | `81`, `82`, `83` |
| `DB E9`, `DC E9`, `DF E9` | vowel sign vocalic L, LL, RR | `84`, `85`, `86` |
| `EA E9` | avagraha | `EB` |
| `EA EA` (ICU), `90` (Apple) | double danda | `87` |
| `F0 B8` (ICU) | anudatta | `89` |
| none | udatta, grave, acute | `88`, `8A`, `8B` |
| `E8 E8`, `E8 E9` | explicit halant (U+094D U+200C), soft halant (U+094D U+200D) | none: ACII has no byte for ZWNJ or ZWJ (C8) |

Without the rewrite, measured on the new build with `acii2rmn | rmn2acii` (the mid build gives the same): `A1 E9` comes back as `C7` (NNNA, because the decoder reads candrabindu + nukta as "N + nukta"), `A6 E9` as the ASCII text `za`, `EA EA` as two ASCII bars `7C 7C`, and `EA E9` crashes `acii2rmn` (a nukta after a danda, section 11.4). Only `F0 B8` survives, by accident: the decoder passes the unknown byte `F0` through, and `B8` is read as the letter CA and written back as itself. The pairs of C8 have nothing to be rewritten to: `B3 E8 E8 B4` comes out as `kha`, and `B3 E8 E9 B4` crashes (section 11.5).

**How to settle a new conflict.**

1. Write down the claims and their sources, as the table above does. A claim from a converter's source or a mapping file counts for more than a claim from a chart: Wikipedia's chart says `A0` is OM, and the same page's nukta table says `A1` plus the nukta is OM.
2. Decide whether the conflict is *inside* ACII (two meanings for one byte or key) or *at the boundary* (another encoding writes the character differently). Inside, the table is the definition and G1 applies: nothing existing changes. At the boundary, write a rewrite there; do not give the byte a second meaning.
3. Record the decision in this table, and add a test that fails if someone undoes it (as test (e) does for `A0`).

### 10.6 Missing sounds

A *missing sound* is one that a text needs and the repertoire cannot write. What to do, in order:

1. **Look for the character.** Unicode may have it in the Devanagari block (section 10.4), in Vedic Extensions, in Devanagari Extended, or in the block of another Indic script. An assigned character is always better than a private one.
2. **Use a nukta.** A consonant followed by the nukta is the established way of writing sounds that Devanagari did not have: क़ ख़ ग़ ज़ फ़ and the rest of the Perso-Arabic set, which `iso15919_map.csv` lists with the letters that the project uses for them. No byte is needed: the nukta is already `E9`, the key is the stem plus `za` (R7), and `uni2acii`, the decoder and the parser already handle it; since patch 0003 `uni2acii` also takes the single code points of Unicode's nukta letters (section 15). Measured on the patched build: the pair *consonant, nukta* survives `acii2rmn | rmn2acii` for every consonant byte except dental DA and DHA (`C4`, `C5`). The decoder's special case for `d` + nukta, meant for the retroflex DDA, also catches them and writes `__rda`, which is read as a literal underscore and `rda`. The round-trip contract of section 9 promises the nukta only for the eleven consonants for which Unicode has a code point.
3. **Merge knowingly.** If a neighbouring sound is close enough, map to it and record the merger (conflict C7). A merger loses the distinction for good.
4. **Add a new letter.** If a letter is unavoidable and Unicode has no code point for it, use a code point of the Private Use Area (U+E000-U+F8FF): `unicode.h` can hold it, since it stores any 16-bit value. Record it here; it is local to the project. Then give it a byte (section 10.3) and a spelling.
5. **Spell it by the conventions of section 6.** The plain letter is the primary reading; where a Roman letter serves two sounds the second one takes `_`; an aspirate adds `h`; a mark that attaches ends in `a`. Check the result with the lint: T6 says whether the parser reads the key as one token, T7 whether it disturbs its neighbours.
6. **Run the checks** (section 13).

No missing sound has a key that is waiting for it. Of the 15 keys that the parser asks for and the table lacks (section 11.3), only `lha` could be the spelling of a letter, the ZHA of Tamil and Malayalam; but `lh` is also how the conjunct ल्ह is typed, so the key is not free (recipe A, section 8.2, shows the mechanism).

### 10.7 The admissibility conditions in one place

A change to the tables (and, if needed, to the parser) is admissible when all of the following hold. The right-hand column names the check that decides each.

| # | Condition | Check |
|---|---|---|
| A1 | The key uses `a`-`z` and `_`, with an optional leading `^` | lint T3 |
| A2 | The parser reads the key as one token and writes exactly the bytes of its row | lint T6 |
| A3 | For a one-byte row, the decoder turns the byte back into the key: no earlier row begins with the same byte | lint T6 |
| A4 | No key twice, no code point twice, no byte for two code points; every Unicode row has an ACII row | lint T4, T5 |
| A5 | The new key does not extend or split an existing token: consonant + halant + X and X + consonant still survive the filter pair for every letter X | lint T7 |
| A6 | Every string that the parser read before is read as before, unless it contains the new key | `tests/diff_parser.py` |
| A7 | Well-formed ACII over the repertoire, with the new character in the generator, survives `acii2rmn | rmn2acii` | `tests/rt_filters.py` |
| A8 | The character survives `uni2acii` and `acii2uni`; no everyday character is moved to the new byte | `tests/test_unicode.py` |
| A9 | The grammar printed in section 5.3 and `rmn2acii.c` describe the same parser | `tests/diff_parser.py`, and the generated tables of this document: `tools/gen_doc_tables.py --check` |
| A10 | No rule of the parser consumes an underscore, or steps over the end of the input, without having looked at it: a rule that jumps over a character it has not tested has its guard rule (section 14.7) | `tests/test_underscore.py` (U7) |
| A11 | Each precomposed nukta letter of Unicode goes through `uni2acii` and `acii2uni` as a consonant and a nukta and comes out in the form that is asked for: as the converters always wrote it by default, as NFC writes it with `-f nfc`, as NFD writes it with `-f nfd` (section 15.2); every other code unit of the BMP is written as before | `tests/test_nukta.py` |

## 11. Known limitations and quirks

Everything in this section was observed on the builds of this package (gcc, x86-64 Linux), and `tests/test_limitations.py` repeats the measurements on all three: *old*, the unpatched sources; *mid*, with patch 0001, the Sanskrit characters; *new*, with patch 0002 as well, the guards (section 13). Where the old build behaves the same, the text says "all builds" or "pre-existing". Patch 0001 introduces one change of exposure, in section 11.6; nothing else here is caused by it. Patch 0002 closes the unchecked reads of section 11.4 and changes nothing else in this section. Exact crash thresholds depend on how the compiler lays out memory; the defects behind them (fixed-size buffers, unchecked reads) are undefined behaviour everywhere.

### 11.1 The lexical layer: what the translators never see

The translators are called from lexers, and what a lexer does not pass on cannot be part of any key.

**`acii2rmn.lex`** has three rules. A double-quoted string (escaped quotes allowed; no `^` and no newline inside) is copied inside a second pair of quotes: `""string""`. A run of ASCII letters and `_` is copied as `"e_word"`. A run of all other bytes, except `^`, newline, backspace and `"`, goes to the decoder. The decoder therefore sees digits, spaces, punctuation and every upper-half byte, in stretches that end at the next Latin letter, `_`, `^`, quote, newline or backspace. The stack is reset for each stretch. `acii2cf.lex` and `acii2pcf.lex` are for program text: they copy Latin words, character literals and string literals unchanged (without the `"e_"` wrapper) and give the decoder only the other stretches. They differ in how literals are recognised, and in one visible detail: a Latin word that ends in `_` and is directly followed by Devanagari is written `trace__ka` by `acii2cf` and `trace_ka` by `acii2pcf` (the underscore is doubled by the first, through the row `__`).

**`rmn2acii.lex`** has three rules. `"e_word"` is written as the word, `""string""` as the string, and a run of `[A-Za-z_]` goes to the parser. Everything else is copied by the default rule of the lexer: digits, spaces, punctuation, `^`, `|`, and bytes of the upper half. So the parser sees letters and `_` and nothing else.

What follows:

- **Keys are made of letters and `_`** (R1). The keys `^aa`, `|` and the other keys with `^` are reached only from inside the parser: typed `k^aa` gives `B3 E8 5E 61 61`, which is KA, halant, and the ASCII text `^aa`.
- **A stand-alone sign loses its meaning.** The decoder writes a sign at the start of a stretch with its `^` (`DA` gives `^aa`); the filter does not hand `^` to the parser, and the text comes back as `5E 61 61`.
- **The danda is lost.** The decoder writes `|` for `EA`; the filter copies `|` to the output as the ASCII byte `7C`; `acii2uni` reads it as U+007C. In the repository's own `corp_hi.txt`, "चोला।" comes back as "चोला|" (`tests/test_corpus.py`).
- **Digits.** ASCII digits pass through untouched. `fixuninum` rewrites the digits of the Indic scripts of `iscii_map.csv` (Devanagari, Bengali and Assamese, which share theirs, Gurmukhi, Gujarati, Oriya, Tamil, Telugu, Kannada, Malayalam) to ASCII digits *before* `uni2acii`, so the digit bytes `F1`-`FA` stay unused.
- **The underscore.** `_` is the family marker, so a literal underscore has to be doubled: the row `__` is its spelling. Hindawi's `Hindawi/hindrv/std2hin.awk` runs `sed 's/_/__/g'` on the translated program before `rmn2acii` for this reason, in twelve of its thirteen language branches (the thirteenth, `roaboata`, prints "Not supported as yet").
- **Typed text reaches the parser.** `std2hin.awk`, `RomenagriMail/mailfilter.awk` and `RomenagriUI/RomenagriUI.kmdr` run `rmn2acii` on text that people or other programs wrote, so the crashes of sections 11.3 and 11.4 are reachable from outside.

### 11.2 Rows that nothing reaches

Appendix A says, for every row, whether the decoder, the parser, both or neither uses it. The rows with fewer than both:

- `kxa`, `_tra`, `j_yna`, `shra` and the stem `r` (`CF E8`) are conjunct rows. The decoder finds an earlier single-byte row with the same first byte, and the parser never asks for them: it writes a conjunct as single rows one after the other (section 5.1). `^ra` (halant, RA) is dead twice: the decoder finds the halant row `^` first, and the parser reads `^r` as the text `r`.
- `_rda` and `_rdha` are asked for by the parser; the decoder builds those two keys itself in its nukta rule, so its own rows for them are shadowed.
- `^a` has no bytes: the inherent vowel written as a sign is invisible in ACII.
- Row 0 (`EF 42`) is read by the decoder, which takes the attribute code from it and drops the byte after it; the parser never uses it.

These rows cost nothing and can stay. Removing one moves every later row (G1).

### 11.3 Keys the parser asks for and the table lacks

One state of the parser, L2b, builds its keys from a parameter. After one of fourteen consonant stems (`g t d p b s l k j`, `ch`, and the underscore stems `_t _d _rd _rr`) it looks at the next letter and builds one of three keys: the stem and `a` (nothing special follows), the stem and `ha` (an `h` follows: an aspirate) or the stem and `vra` (a `v` follows). The table has a row for all fourteen plain keys, for twelve of the fourteen aspirates and for one of the fourteen `vra` keys. Every other key of the grammar is read off the input as it stands, and the table has all of them. The fifteen holes:

<!-- BEGIN GENERATED reserved-keys -->

- keys the grammar can ask for: 102; without a row in `acii.h`: **15**
- the 14 stems of state L2b make 42 keys; the other 60 keys of the grammar are not built from a stem
- all 15 missing keys are in the columns `h` and `v` of the table below

| stem (typed) | plain: stem + `a` | aspirate: stem + `ha` | stem + `vra` |
|---|---|---|---|
| `b` | `ba` CA | `bha` CB | **no row**: `bvr` crashes |
| `d` | `da` BF | `dha` C0 | **no row**: `dvr` crashes |
| `g` | `ga` B5 | `gha` B6 | **no row**: `gvr` crashes |
| `j` | `ja` BA | `jha` BB | **no row**: `jvr` crashes |
| `k` | `ka` B3 | `kha` B4 | **no row**: `kvr` crashes |
| `l` | `la` D1 | **no row**: `lh` crashes | `lvra` D2 |
| `p` | `pa` C8 | `pha` C9 | **no row**: `pvr` crashes |
| `s` | `sa` D7 | `sha` D5 | **no row**: `svr` crashes |
| `t` | `ta` BD | `tha` BE | **no row**: `tvr` crashes |
| `ch` | `cha` B8 | `chha` B9 | **no row**: `chvr` crashes |
| `_d` | `_da` C4 | `_dha` C5 | **no row**: `_dvr` crashes |
| `_rd` | `_rda` BFE9 | `_rdha` C0E9 | **no row**: `_rdvr` crashes |
| `_rr` | `_rra` D0 | **no row**: `_rrh` crashes | **no row**: `_rrvr` crashes |
| `_t` | `_ta` C2 | `_tha` C3 | **no row**: `_tvr` crashes |

<!-- END GENERATED reserved-keys -->

When the parser asks for a missing key, `lookup()` returns `NULL` and the next `strcat` crashes. Measured on all three builds, the filter exits with status 139 (SIGSEGV) and writes nothing for the typed forms of the table, and `tests/test_limitations.py` repeats the measurement for every one of them; `lvr` (ळ) works, because `lvra` is a row. Typed text can reach every one of the fifteen (section 11.1); the guard rule of L2b changes only the two endings of a run: a `v` that is the last character of a run, or is followed by an underscore, no longer asks for the row (`kv` crashed before patch 0002 and now gives `ka` and the letter `v`, as `nv` always gave `na` and the letter `v`; `kv_` gives the same and a halant). Every typed form of the table has a letter after the `v`, so each of them still crashes. The decoder cannot reach them, because it never writes an `h` or a `v` straight after a consonant stem, so the round trip of section 9 is not touched.

**The fifteen are not fifteen missing characters.** They are two things of different kinds.

*Thirteen `vra` keys: the Latin letter `v` after a consonant.* `v` is not a letter of Romenagri: व is `w` (`swar`, `dwaar`, `jwaala`, `kwaath` work). The one spelling in which the parser accepts a `v` is that of ळ, `lvra`: after the stem `l` the letter `v` selects the key `lvra` and the parser jumps over the letter after it without looking at it (it expects the `r`; section 11.4), unless that letter is an underscore or the end of the string (a guard rule, section 14.7). That code is shared by all stems, so every stem followed by `v` asks for a `...vra` key, and only `lvra` exists. The other thirteen would be letters that no script has (क, ग, ज... "with vra"). The input that reaches them is typing a व as `v`, as ITRANS, IAST and Harvard-Kyoto do: `svar`, `dvaar`, `tvam`, `kvaath`, `jvaala`, `gvaal` all crash the filter; with `w` instead of `v` they work.

*Two aspirate keys, `lha` and `_rrha`: conjuncts typed as aspirates.* Devanagari has no letter for an aspirated `l` or an aspirated ऱ. Hindi and Marathi write those sounds as conjuncts with ह: ल्ह (दुल्हन, चूल्हा, कुल्हाड़ी, मल्हार, उल्हासनगर) and ऱ्ह (वऱ्हाड, Marathi). Romenagri's own way of writing them is `l_ha` and `_rr_ha`, because plain `h` is the aspirate marker and ह is `_ha`; the decoder always writes them so (LA, halant, HA, the bytes `D1 E8 D8`, come out as `l_ha`, and `D0 E8 D8` as `_rr_ha`; never as `lh` or `_rrh`). But `lh` is what a person at a keyboard types for ल्ह (`dulhan`, `ullhaas`), and today it crashes. The other sonorants do not crash on the same typing: `nh` and `mh` give NA or MA, a halant and the ASCII letter `h`, because their stems do not go through L2b.

*Why `lha` is not simply ऴ.* U+0934 ऴ (ISCII byte `D3`, "Consonant ZHA (Tamil & Malayalam)"; Unicode's note: "for transcribing Dravidian l") has no row, and `D3` is free. `lha` is the one of the fifteen keys that could name an existing character, and recipe A (section 8.2) adds it for that reason, to show the mechanism. But it would take the typed form `lh` away from ल्ह, which Hindi and Marathi need far more often than ऴ. A spelling that does not collide, a family key such as `_la`, needs a parser rule (recipe B). Since patch 0003 the character is not lost on its way through the pipeline either way: U+0934 is written `D2 E9`, read back as U+0934, and shown by Romenagri as `lvrza` (section 15.7, C7).

**Ways to close them.** None is applied in this package, except for the one corner of option A that the guard rule of L2b covers (a `v` that is followed by an underscore or by the end of the string, section 14.7); which one is right is the author's decision. Each of them leaves the decoder, and so the round trip, as it is.

| Option | Change | `kv` and the other twelve | `lh`, `_rrh` | Consequence |
|---|---|---|---|---|
| A. look before you leap | in L2b take the `h` and the `v` branch only when the row exists; otherwise fall to the plain rule | the consonant, then the letter `v` as text (as `nv` does today) | ल् and the letter `h` as text (as `nh` does today) | smallest change, no table edit; the behaviour is that of the sonorants; typed ल्ह must still be `l_ha` |
| B. conjunct fall-back | as A, but when `stem` + `ha` has no row, read the `h` as `_ha` | as A | ल्ह and ऱ्ह, as the typist meant | gives Hindi and Marathi typists what they expect; `nh`, `mh`, `rh` would then want the same rule in L2a |
| C. `v` as `w` | after a stem, read `v` as `w` | स्व, द्व, त्व | as A or B | accepts ITRANS-style typing; but `lv` is ळ today, and ल्व would then need another spelling, and `v` would mean व after a consonant only |
| D. add rows | one row per key | (13 letters that no script has) | `lha` = ऴ (the one letter) or the conjunct (not a row) | for `lha` only; the choice between ऴ and ल्ह is the whole question |

`tools/reserved_keys.py <Romenagri directory>` builds the parser in a scratch copy, lists the typed form of each of the fifteen with what the parser does with it, and compares every other behaviour with the grammar of section 5.3, so that a fix can be checked while it is being made. When a fix changes the grammar, change the grammar block of section 5.3 with it: the differential test (`tests/diff_parser.py`) then holds the C parser to the new grammar, `tools/gen_doc_tables.py --write` refreshes the table above, and the measurements of this section in `tests/test_limitations.py` (which assert the crashes) are the ones to update.

### 11.4 Buffers, limits and unchecked reads

| Where | Defect | Observed |
|---|---|---|
| decoder stack (`stack.c`, `char stack2[10240]`) | a stretch (section 11.1) may decode to at most 10,239 characters; at 10,240 the terminating NUL no longer fits | 5,119 bytes `B3` (`ka` each, 10,238 characters) plus one space work; plus two spaces (10,240) crashes, in both builds. Spaces and punctuation do not end a stretch; a newline does, so a text of many short lines is safe. |
| parser buffer (`rmn2acii.lex`, `hldtxt2[1024]`) | a run of more than 1,023 letters overflows | 1,023 and 1,024 letters work (the NUL of 1,024 lands one byte past the array); 1,025 crash |
| parser buffer, never cleared | the buffer is `static` and each run is copied over its start only, so after a short run the tail of an earlier, longer run is still behind the terminator. In the old and mid builds the eleven rules of section 5.4 (six unchecked skips, five wildcards) can read it. In the new build the guards of section 14.7 stop every read at the terminator: the buffer is still not cleared, and nothing can see it | old and mid: `kakakaka c` gives `B3 B3 B3 B3 20 B8 E8 B3 B3 B3`: the `c` of the second word borrows three `ka` from the first. In a fresh process `c` gives `B8 E8`. The same for `lv`, `ke`, `_e`, `_y`, and `_o`, `_n`, `_r`, `_j` (`kakakaka _n` gives `B3 B3 B3 B3 20 61 B3 B3`, where a fresh process writes nothing). New: `kakakaka c` gives `B3 B3 B3 B3 20 63` and `kakakaka _n` gives `B3 B3 B3 B3 20 6E`, the same as in a fresh process: the last word is the plain letter. |
| parser, reads past the end | a string that ends inside a key makes the parser read past its terminator: `c`, `_e`, `_y`, `_o`, `_n`, `_r` or `_j` at the end of a run, the stem `l` followed by `v` (`lv`), a consonant followed by `e` (`ke`), and, through the library only, `^_` and `^o`. These are the eleven rules of section 5.4. **Closed in the new build** by the twelve guards of section 14.7, each of which leaves its branch when the next character is the terminator | old and mid builds: undefined behaviour in C; `Overrun` in the executable grammar without the `!` rules. New build: `c`, `lv`, `ke`, `_e`, `_y`, `_o`, `_n`, `_r`, `_j` give the plain letter (`63`; `D1 76`; `B3 65`; `65`; `79`; `6F`; `6E`; `72`; `6A`), and neither the grammar nor the harness finds a read past the end (`tests/test_underscore.py`, U7). The differential test leaves the strings out for the old and mid builds and counts them (section 11.7) |
| decoder, nukta | a nukta with fewer than two characters below it pops an empty stack: `*pop(1)` is a null dereference | `E8 E9`, `EA E9` and `B3 E8 E9` crash `acii2rmn`. Real ISCII writes the avagraha as `EA E9` (section 10.5). |
| decoder, first byte | the test "the previous byte was `EF`" reads `tok[-1]` for the first byte of a stretch | undefined behaviour; the model assumes the byte is not `EF` |

The decoder and the parser both use static buffers and are not reentrant.

**What can still crash the parser of the new build.** Two things only: a key that the table lacks (section 11.3), and a run of more than 1,024 letters (the parser-buffer row above). The measurement of section 14.8 shows it: of 14,762 strings made by mutating the grammar's own examples, the new build crashes on the 35 that ask for a missing key and on no other. The decoder rows (the stack, the nukta, the first byte) are as they were.

### 11.5 What does not survive a round trip

Section 9 defines the text for which `acii2rmn | rmn2acii` returns its input. Outside it, the cases that are easy to meet:

- **A halant followed directly by an independent vocalic vowel** comes back as the sign: `B3 E8 AA` returns `B3 DF`, and the same for `81`, `82`, `83`. The parser cannot tell "consonant, halant, vowel" from "consonant with the vowel's sign", because the halant is replaced by the sign (`vocalic`, section 7.4), as it always was for `_ri`.
- **Dental DA or DHA followed by a nukta.** The decoder's special case for `d` + nukta, meant for the retroflex DDA, also catches the dental letters: `C4 E9` is written `__rda`, which the parser reads as a literal underscore and `rda`. The pair is not Hindi, and the round-trip contract excludes it.
- **A sign, halant or nukta where the grammar of section 9.2 does not allow it** (after a space, a vowel or another sign): the decoder pops whatever is on top of the stack.
- **ISCII's explicit halant and soft halant.** `E8 E8` and `E8 E9` are how ISCII writes a halant followed by ZWNJ or ZWJ (section 10.4). The decoder reads them as a halant after a halant and as a nukta after a halant. The second halant pops the letter before it: `B3 E8 E8 B4` (KA, halant, halant, KHA) is written `kha`, and the KA is gone. The nukta needs two characters below it and finds one: `B3 E8 E9 B4` crashes `acii2rmn` (section 11.4). The nukta layer (section 15) never rebuilds a nukta that follows a halant, for this reason.
- **The danda** and **a stand-alone sign** (section 11.1).
- **Canonical equivalence at the Unicode end.** Since patch 0003 `uni2acii` writes the precomposed nukta letters as a consonant and a nukta, and `acii2uni` writes that pair back as two code points (as one, where NFC composes it, with `-f nfc`), so the round trip through the two converters is exact only up to canonical equivalence (section 15.5, item 2).
- **Schwa deletion is not supported.** `k` is क्, `ka` is क; Romenagri text has to write every inherent vowel (`raama`, not `raam`), which is what the comment above `level2a` says it does on purpose.

### 11.6 What `uni2acii` does with characters it has no row for

`uni2acii` writes the **low byte** of the code point and drops the high byte; `acii2uni` reads a byte with no row as the byte modulo 128. Both fallbacks are silent by default (`uni2acii -w` reports each code point that falls back, once, on stderr: section 15.2). The effects, measured with `uni2acii | acii2uni` and held in place by `tests/test_limitations.py`; `tests/test_unicode.py`, part (e), keeps a longer list of everyday characters and requires that none of them reaches a new byte:

| Character | Low byte | Comes back as |
|---|---|---|
| U+00A0 NO-BREAK SPACE | `A0` | an ordinary space (harmless; the reason `A0` stays unused, section 10.3) |
| U+00AD SOFT HYPHEN | `AD` | ऐ |
| U+00B7 MIDDLE DOT | `B7` | ङ |
| U+00D7 MULTIPLICATION SIGN | `D7` | स |
| U+00E9 é | `E9` | the nukta |
| U+20B9 INDIAN RUPEE SIGN | `B9` | छ |
| U+2022 BULLET, U+2122 TRADE MARK SIGN | `22` | `"` |
| U+2026 HORIZONTAL ELLIPSIS | `26` | `&` |
| U+2020 DAGGER | `20` | a space |
| U+FFFD REPLACEMENT CHARACTER | `FD` | `}` |
| U+2002 to U+2019, U+201C, U+201D (spaces, dashes, quotes, and the zero-width joiners U+200C and U+200D, section 10.4) | `02` to `1D` | control characters (U+200C a form feed, U+200D a carriage return) |
| U+0934 ऴ | `34` (old and mid builds; the new build writes `D2 E9`, section 15) | `4` (old and mid builds; ळ and a nukta in the new build, ऴ with `-f nfc`) |
| U+1CD0 VEDIC TONE KARSHANA | `D0` | ऱ |
| U+2190 LEFTWARDS ARROW | `90` | a control character |
| any character above U+FFFF (an emoji, a Brahmi letter) | the low byte of each of its two UTF-16 units | U+1F600 gives `3D 00`, an equals sign and a NUL |

The table lacks 43 code points of the Devanagari block itself (section 10.4). Ten of them are the digits, which `fixuninum` rewrites first; the others fall back this way, except the nine nukta letters, which the nukta layer writes as two bytes (section 15). In the corpus of the repository the effect is visible in the double danda: "चोला॥" came back as "चोलाe", because U+0965 has the low byte `65`, the letter `e`; with patch 0001 it comes back as it went in (`tests/test_corpus.py`, `Romenagri/corp_hi.txt`, two lines).

**What patch 0001 changes here.** The bytes `81`-`8C` were not in the table, so characters whose low byte is one of them came back as control characters. They now come back as the twelve new characters. Twelve of every 256 code points are affected: the block elements ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ (U+2581-U+258C) become ऌ ॡ ॠ ॢ ॣ ॄ ॥ ॑ ॒ ॓ ॔ ॐ, and so on. None of the everyday characters of the list above is affected, which is what test (e) asserts. The fix for all of it is to deal with characters that are not in the tables before `uni2acii`, not to give every character a byte.

### 11.7 What the tests leave out

So that the claims of this document can be weighed:

- **Memory-layout thresholds are printed, not asserted.** The sizes at which the fixed buffers overflow (10,240 decoded characters, 1,025 letters) depend on how the compiler lays out memory; `tests/test_limitations.py` prints them for comparison and asserts only what does not depend on layout.
- **Undefined behaviour is excluded, not tested, for the old and mid builds.** `tests/diff_parser.py` skips the strings on which the C parser of those builds reads past its terminator (section 11.4); it counts them and prints the count. The executable grammar without the `!` rules raises `Overrun` for them. For the new build there is nothing to skip: the grammar with the guards never raises `Overrun`, and the test fails if it ever does. What stays outside the tests are the fixed buffers and the decoder's empty stack (section 11.4), where the behaviour depends on the memory layout.
- **Crashes are compared, not repaired.** Where both the grammar and the C parser crash (missing rows, section 11.3), that counts as agreement.
- **The round-trip generator is narrower than the code.** It generates only the text of section 9.2, so the cases of section 11.5 are described, not tested for success.
- **The end-to-end test needs `hincc`.** `tests/e2e/run_e2e.sh` compiles and runs a Hindi C program and a Hindi Java program with the new characters; it is skipped when `hincc` is not on the `PATH`.
- **Normalisation is tested for the nukta letters only.** `tests/test_unicode.py` and `tests/test_nukta.py` take the eleven letters and their NFD forms from Python's `unicodedata` and show that both come out of the chain as the form asks (as NFC writes them with `-f nfc`, as NFD writes them with `-f nfd`), and that, outside the cases of section 15.5, the two forms do what NFC and NFD do; they do not test normalisation of any other character, nor the order of the steps in a real pipeline.

## 12. Provenance and standards

### 12.1 Sources

| Source | Used for |
|---|---|
| the repository, [hindawiai/chintamani](https://github.com/hindawiai/chintamani), directory `Romenagri/`, commit `3ad87785a75dc2b18438a8b068807103cb920c81` | the code and the tables that sections 3 to 6 describe |
| ISCII-91, the Bureau of Indian Standards' IS 13194:1991, as the repository reproduces it in `Romenagri/iscii_map.csv` | the layout of the bytes `80`-`FF`. A row marked `*` in the CSV means "this code followed by the nukta". |
| Apple's Mac OS Devanagari mapping, [DEVANAGA.TXT](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/DEVANAGA.TXT) (header revision c02, 2005-Apr-05) | an implementation of ISCII-91 for Devanagari: byte pairs with the nukta, `90` for the double danda, `D3` for U+0934, `E8 E8` and `E8 E9` for the halant followed by ZWNJ and by ZWJ |
| ICU's ISCII converter, [ucnvisci.cpp](https://searchfox.org/mozilla-central/source/intl/icu/source/common/ucnvisci.cpp) (the copy in Mozilla's tree) | another implementation: the same nukta pairs, `EA EA` for the double danda, `F0 B8` for the anudatta, `A0` as the no-break space, `E8 E8` and `E8 E9` for the halant followed by ZWNJ and by ZWJ |
| Wikipedia, [Indian Script Code for Information Interchange](https://en.wikipedia.org/wiki/Indian_Script_Code_for_Information_Interchange) | the code chart (`A0` is "Sign OM"), the nukta table (`A1` plus the nukta is OM), the codes `EF` (attribute) and `F0` (extension) |
| the Unicode Character Database file `CompositionExclusions.txt`, section "(1) Script Specifics", read in [a copy of an early version](https://stuff.mit.edu/afs/sipb/contrib/doc/specs/protocol/unicode/CompositionExclusions.txt), which lists U+0958 to U+095F, DEVANAGARI LETTER QA to YYA; and the thread [Query Regarding NFC Normalization and Script-Specific Exclusions for Devanagari](https://corp.unicode.org/pipermail/unicode/2025-May/011443.html) on the Unicode mailing list (1 May 2025), in which U+0958 is called a script-specific composition exclusion and the decomposed forms are said to have been the representation that experts preferred for Devanagari at the time | why NFC leaves the eight nukta letters U+0958-U+095F decomposed (section 15.3). The early copy is old and the thread names only U+0958, so the property that the layer relies on is also measured on the machine, with the `unicodedata` of Python 3 (Unicode 15.1): `tests/test_nukta.py`, part (a). |
| the Unicode Standard: the Devanagari, Vedic Extensions and Devanagari Extended blocks; UAX #15, Normalization Forms | names and properties of the characters. The counts in this document were taken with the `unicodedata` module of Python 3, which carries Unicode 15.1. |
| ISO 15919, as the repository reproduces it in `Romenagri/iso15919_map.csv` | the 7-bit transliteration scheme that section 10.5 compares with Romenagri |

The two pages about composition exclusions were read on 6 November 2026. The three web sources of the other rows were read on 19 October 2026 (Apple's table and ICU's source once more on 20 October, for the explicit and soft halant). Two of them (Apple's table, ICU's source) are mapping tables that programs execute; the third (Wikipedia) is an encyclopedia page that disagrees with itself about OM (section 10.5), and is cited for the codes, not as the authority for any byte.

### 12.2 How each source writes the characters of section 7

| Character | `iscii_map.csv` | Apple | ICU | ACII, patches 0001 and 0003 |
|---|---|---|---|---|
| OM, U+0950 | `A0` | `A1 E9` | `A1 E9` | `8C` |
| vocalic L, U+090C | `A6*` | `A6 E9` | `A6 E9` | `81` |
| vocalic LL, U+0961 | `A7*` | `A7 E9` | `A7 E9` | `82` |
| vocalic RR, U+0960 | `AA*` | `AA E9` | `AA E9` | `83` |
| sign vocalic L, U+0962 | `DB*` | `DB E9` | `DB E9` | `84` |
| sign vocalic LL, U+0963 | `DC*` | `DC E9` | `DC E9` | `85` |
| sign vocalic RR, U+0944 | `DF*` | `DF E9` | `DF E9` | `86` |
| double danda, U+0965 | not listed | `90` | `EA EA` | `87` |
| udatta, U+0951 | not listed | not mapped | not mapped | `88` |
| anudatta, U+0952 | not listed | not mapped | `F0 B8` | `89` |
| grave accent, U+0953 | not listed | not mapped | not mapped | `8A` |
| acute accent, U+0954 | not listed | not mapped | not mapped | `8B` |
| avagraha, U+093D (not new) | `EA*` | `EA E9` | `EA E9` | `EB` |
| LLLA, U+0934 (not added) | `D3` | `D3` | `D3` | not mapped; `D3` is free; written `D2 E9` by the nukta layer (section 15) |

ISCII-91 leaves the bytes `80`-`9F` unassigned (`iscii_map.csv` has no row there), so the choice of the bytes of section 7.2 is not a choice between standards, with one exception: Apple's table writes the double danda as the single byte `90`, ACII uses `87`, and the rewrite of section 10.5 translates between them (C3). Only OM is a real disagreement between the repository's CSV and the converters (section 10.5, C1).

### 12.3 Licence and copyright

- The code of `Romenagri/` is free software under the GNU General Public License, version 2 or (at your option) any later version; its text is `Romenagri/copying`, and the package carries it as `COPYING`. The new files (this document, `tools/*`, `tests/*`, including `tools/apply_guards.py` and `tests/build_trees.sh` of patch 0002, and `tools/apply_nukta.py`, `tests/test_nukta.py` and the header `nukta.h` of patch 0003) carry `SPDX-License-Identifier: GPL-2.0-or-later`.
- The `corp_*` text files of `Romenagri/` come from Wikipedia and are, as `Romenagri/LEGAL` says, "usually" under CC BY-SA 3.0; the terms are those of the original articles. The package changes none of them.
- The five files that patch 0001 changes (`acii.h`, `unicode.h`, `aciihin.h`, `acii2hin.c`, `rmn2acii.c`) and the new files carry the line `Copyright (C) 1993-2026 Abhishek Choudhary`. Patch 0002 changes one more file of the code, `rmn2acii.c` again, and this document. Patch 0003 changes `uni2acii.c`, `acii2uni.c` and the Makefile (their notice now reads 1993-2026 as well), adds `nukta.h`, and changes this document. Files that the patches do not touch keep the notices they have.
- Each changed file has an entry for each patch that changed it in its own "Modifications" log (`rmn2acii.c` has two). The entries name the alias `<obonac>` and mark the work "(prepared with Claude)"; the mark can be removed without affecting anything else.

## 13. Running the checks

### 13.1 What is needed

`gcc`, `make`, `flex` with its library (`-lfl`), `patch`, and `python3`. The end-to-end test needs, in addition, `hincc` and Hindawi's converters on the `PATH`, `iconv`, `gcc` and a Java compiler; it is skipped without `hincc`. `tools/check_tables.py`, `tools/gen_doc_tables.py` and the model-based tests need no compiler.

### 13.2 Commands

```
tests/run_all.sh                 quick run: builds the three trees under build/ (old, unpatched; mid, patch 0001; new, all three patches), runs every check
tests/run_all.sh --full          the exhaustive run: many minutes in all, so it is meant to be run in pieces (below)
tests/run_all.sh --full --resume                  the same run, restartable: a step that passed on the same sources is not run again
tests/run_all.sh --full --resume --only <steps>   only the named steps (comma-separated: `build`, or the names that the summary prints)
tests/build_trees.sh             only the build of the three trees and of the harnesses, for ad-hoc work (what run_all.sh starts with)
python3 tools/check_tables.py Romenagri --free     lint the three tables and print the free bytes
python3 tests/test_underscore.py [--full|--deep] [--only U1,U7]   the laws, tests and measurements of section 14, all or the named checks (needs the build/ of run_all.sh)
python3 tools/reserved_keys.py Romenagri [--strict]  the keys of section 11.3, tried on the C parser in a scratch build
python3 tools/gen_doc_tables.py --check Romenagri  fail if a generated block of this document is out of date
python3 tools/gen_doc_tables.py --write Romenagri  refresh the generated blocks
python3 -I tools/apply_sanskrit.py <pristine Romenagri>    repeats the edits of patch 0001 (not the document) on a clean tree
python3 -I tools/apply_guards.py <Romenagri with patch 0001>    repeats the edits of patch 0002 to rmn2acii.c (not the document)
python3 -I tools/apply_nukta.py <Romenagri with patches 0001 and 0002>    repeats the edits of patch 0003 to uni2acii.c, acii2uni.c and the Makefile and writes nukta.h (not the document)
patch -p1 < patches/0001-add-missing-sanskrit-characters.patch     the same as patch 0001, from the directory that holds Romenagri/
patch -p1 < patches/0002-apply-underscore-guards.patch             then patch 0002 (the C parser and this document)
patch -p1 < patches/0003-add-nukta-layer.patch                     then patch 0003 (the nukta layer and this document)
```

The environment variables of `tests/run_all.sh`: `RMN_BUILD` (where to build), `RMN_BASELINE` (a `Romenagri` directory to use as the old tree instead of "the patched tree with every patch taken off"; the mid tree is always "the patched tree with every patch but the first taken off", that is, with patch 0001 only), `RMN_CORPUS` (more Hindi text files for the corpus test, separated by `:`), `RMN_SKIP_HANDWRITTEN=1` (leave out the hand-written parser in the differential test), `RMN_GRAMMAR=<file>` (read the grammar block of another copy of this document), `HINDAWI_SRC` (the `Hindawi/` directory of the repository, for rebuilding the shailis in the end-to-end test).

**Long runs in pieces.** The exhaustive run is long (the check of section 14 alone reads more than a million strings through each build), so `tests/run_all.sh` runs that check as nine steps, `underscore_U1` to `underscore_U9`, one for each of U1 to U9, and every step writes, besides its log `build/logs/<step>.log`, a marker `build/logs/<step>.rc` (exit status, seconds, time of the end). With `--resume` a step whose marker says that it passed is not run again, and the three trees are not built again, as long as the files of `Romenagri/`, `patches/`, `tools/` and `tests/` and the settings are the same as when `build/logs/stamp` was written (otherwise the script says so and stops). `--only` takes the names of the steps: `build` (the three trees and the harnesses), `table_lint_new`, `unicode`, `nukta`, `saral`, `parser_vs_model`, `roundtrip`, `corpus`, `recipes`, `limitations`, `underscore_U1` to `underscore_U9` (`underscore` stands for all nine), `reserved_keys`, `doc_tables_in_sync` and `e2e_new`. After `build` the steps do not depend on one another, so they can be run by several commands at the same time, and a run that is interrupted loses at most the steps that were running:

```
tests/run_all.sh --full --resume --only build
printf '%s\n' underscore_U7 underscore_U1 parser_vs_model roundtrip underscore_U5 underscore_U6 underscore_U8 underscore_U9 \
  underscore_U4 underscore_U2 underscore_U3 corpus limitations recipes unicode nukta saral table_lint_new reserved_keys \
  doc_tables_in_sync e2e_new | xargs -P 2 -I{} tests/run_all.sh --full --resume --only {}
tests/run_all.sh --full --resume         # runs whatever is still missing, then prints every step and the summary
```

### 13.3 What each check establishes

| Check | Script | Establishes | Conditions of section 10.7 |
|---|---|---|---|
| table lint | `tools/check_tables.py` | T1-T8 of section 3.5 on the three tables; `--free` prints the free bytes | A1-A5 |
| Unicode conversion | `tests/test_unicode.py` | (a) the new code points convert both ways and the old build does not; (b) the old rows convert exactly as before; (c) a mixed text survives; (d) the unmapped Devanagari code points are classified as in section 10.4; (e) everyday characters outside Devanagari and ASCII do not reach a new byte | A8 |
| nukta layer | `tests/test_nukta.py` | the eleven letters of `nukta.h` against Python's `unicodedata`; `uni2acii` and `acii2uni` in the three forms (and how the form is chosen) against a model of the rule on random and on exhaustive streams, and against Python's NFC and NFD as independent oracles; the warning layer; no change to the other 65,525 code units of the BMP; the edge cases; the whole chain; the challenges of section 15.7, each asserted (section 15.8) | A11 |
| saral | `tests/test_acii2hin.py` | the new rows render as section 7.5 says, and every old byte and byte pair renders as before | |
| parser against the grammar | `tests/diff_parser.py` | the C parser of each of the three builds agrees with the grammar of section 5.3 (the rules tagged `+` and `!` select the build) and with the hand-written parser on all short strings and on random long ones; every string whose result changed between old and mid contains a new token, and every one whose result changed between mid and new has had a guard rule applied; the grammar with the guards never reads past the end | A6, A9 |
| round trip | `tests/rt_filters.py` | (1) no regression on the old repertoire, except the repaired avagraha; (2) every sequence with a new byte behaves like its analogue with an old byte; (3) the models of the decoder and of the filter pair agree with the C programs; (4) well-formed texts of section 9.2 round-trip exactly, and the guards of patch 0002 do not change the reading of any of them (all sequences of up to three bytes of `W`) | A7 |
| corpus | `tests/test_corpus.py` | Hindi text through the whole chain, old against mid and against new: no unexplained difference, and no line that the old build restored and the others do not | A6 |
| extension recipes | `tests/test_extension_recipes.py` | recipe A and the mistakes of section 8.1 step 5 behave as described (R1-R3) | A1-A5 |
| limitations | `tests/test_limitations.py` | the measurements of sections 10.6, 11.1, 11.3 (all fifteen missing keys, typed from the grammar), 11.4 (the stale buffer at each of its sites), 11.5 and 11.6 come out as stated, on the three builds; sizes that depend on memory layout are printed only | |
| underscore laws | `tests/test_underscore.py` | U1-U9 of section 14 (`tests/run_all.sh` runs them as the nine steps `underscore_U1` to `underscore_U9`): the cut and run laws, closedness, parity (two states), the marker rule and the decoder, the escape, the eleven rules that read an underscore unseen, the twelve guards (no breaker left, no read past the end, each needed, none fires on decoder output), case folding and random mutations, joiners and operators | A10 |
| reserved keys | `tools/reserved_keys.py` | a tool, not a check: lists the keys of section 11.3, what the C parser does with each typed form, and where the C parser and the grammar differ; run it while fixing them. `tests/run_all.sh` runs it once as a smoke test | |
| document tables | `tools/gen_doc_tables.py --check` | every generated block of this document, including the counts, equals what the headers and the grammar give | A9 |
| end to end | `tests/e2e/run_e2e.sh` | Hindi C and Java programs with the new characters in identifiers, strings and comments compile through `hincc`, run, and print the Devanagari text that was written | |

The exit status of every script is 1 when an expectation fails. `tests/run_all.sh` prints a summary and exits with 1 if any check failed; the logs and the markers of the steps are in `build/logs`.

### 13.4 After a change

1. Edit the tables (section 8.1 steps 1-4) and, if the lint says so, the grammar of section 5.3 and `rmn2acii.c` together; a rule that jumps over a character it has not looked at needs its guard rule (section 8.3, step 3).
2. `python3 tools/check_tables.py Romenagri --free`
3. `python3 tools/gen_doc_tables.py --write Romenagri`, then describe the character in sections 7 and 10.
4. `tests/run_all.sh`, and `tests/run_all.sh --full --resume` (in pieces, if need be) before a release.

## 14. Underscores: runs, escapes, case folding, joiners

This section answers three formal questions that were put about the underscore in Romenagri's design. Each answer says first what the code does and then what can be proved or measured. The statements are held by `tests/test_underscore.py` (the checks U1 to U9 are named where they apply), and the arguments are written so that they can be checked by hand against the grammar of section 5.3.

### 14.1 The questions, and what the code makes of their premises

The questions, in the order in which they were put:

- **Q1.** If single underscores are structural markers and `__` is the escape for a literal underscore, what happens to runs of three, four, five or N underscores? Is there a minimal grammar bound that makes reading and writing mutually inverse (a bijection) for runs of any length, without a second pass or a lookahead beyond the run?
- **Q2.** If the input is guaranteed to be lower case, what does that restriction do to the algebra of the language, and can the translator be verified not to crash on text that the host environment has changed arbitrarily?
- **Q3.** How many states does it take to keep the joiners of the script apart from the operators and escapes of a programming language, in one 7-bit ASCII front end?

Some premises hold and some do not. This is what the code does with them.

| The question assumes | The code |
|---|---|
| single underscores mark structure, `__` is a literal underscore | Yes, with a twist. `_` before a letter starts a family letter (`_ta`, `_ri`). `__` writes one literal underscore, the byte `5F`, but there is no rule for it: it is what the family state does with an *unknown* family letter (section 5.3, state L2c, last rule: the next character is kept as plain text), and here that character is `_`. A `_` at the end of the text is a halant. |
| runs of three or more underscores are ambiguous | They are not, in any text the decoder writes for well-formed ACII (section 14.3), and the parser reads every run from the left (section 14.2). |
| the input is guaranteed to be lower case | There is no such guarantee anywhere in the converters. The parser passes capital letters through as text; the only `tr 'A-Z' 'a-z'` is in two of the pipelines of Hindawi's `std2hin.awk` (section 14.8). |
| a unified front end separates script from host language | The lexers do (section 11.1), by rules that need no memory. Inside the parser the two alphabets meet in one character, `_` (section 14.9). |

**Short answers.**

- **Q1: yes, and the bound is small.** Reading a run needs a two-state automaton that works from left to right (the parity of the run so far). The language of runs is regular, so no context-free power is needed; the only lookahead is the character after the run, and only to say whether an odd run ends in a marker. Two states are also *necessary* (section 14.4). For well-formed ACII the decoder writes every literal underscore doubled and never writes a marker anywhere but as the last underscore of its run, so the two translators invert each other for runs of any length (section 14.5); ACII that is not well-formed can make it leave a lone underscore (section 14.3). Before patch 0002 the parser kept these laws except at eleven rules that read an underscore without looking at it (section 14.6); the twelve guard rules of patch 0002 close the gap in the C parser, and with them the laws hold without exception (section 14.7).
- **Q2: the premise is false, and the answer splits in two.** The fold is a letter-by-letter map that fixes `_`, so it keeps every run, and capital letters are inert in the parser. But the fold is not a homomorphism of the translator: it can turn an inert capital into a key letter, and that can destroy an escaped underscore. Crash-resilience against arbitrary strings can be *proved* (by an induction on the rules plus an exhaustive check) for the grammar with the guards and a complete table, where the parser is a total function. For the C code of this package it holds except for three reasons that have nothing to do with the underscore (fifteen missing rows, fixed buffers, the decoder's empty stack); patch 0001 alone had a fourth, the eleven rules (section 14.8).
- **Q3: two states, for one character.** The script alphabet that reaches the parser and the operator alphabet of a host language share the underscore and nothing else. Telling the underscore's roles apart is the parity automaton, two states. Everything else that separates script from host is decided by the lexers without memory. A joiner costs one parser rule and no state, if it follows the marker rule (section 14.9).

### 14.2 Runs of underscores: the laws

**Notation.** `P(s)` is what the parser writes for the string `s` (the grammar of section 5.3, run by `tests/spec_model.py`; with all its rules, unless a sentence says that the guards are left out). Laws 1 and 2 hold for the grammar with the guards and for the grammar without them alike (U1 checks both); the guards matter for Law 3 and for the strings that the two laws do not cover. A string `u` is *closed* if the parse of `u` reaches the terminator in state L1, L2a or L2b: a consonant may be pending, but no marker is. `u _` then cannot be read as anything but the start of a unit. The empty string is closed.

**What the parser makes of a run.** The generated table below gives the output for `_` repeated n times before `ta`, and after `k` at the end of the input. The bytes: `5F` is the literal underscore, `E8` the halant, `BD` TA, `C2` the family letter `_ta`.

<!-- BEGIN GENERATED underscore-runs -->

| n | `_`×n + `ta` | result | read as | `k` + `_`×n | result | read as |
|--:|---|---|---|---|---|---|
| 0 | `ta` | `BD` | `ta` | `k` | `B3 E8` | `ka` halant |
| 1 | `_ta` | `C2` | `_ta` | `k_` | `B3 E8 E8` | `ka` halant halant |
| 2 | `__ta` | `5F BD` | `_` `ta` | `k__` | `B3 E8 5F` | `ka` halant `_` |
| 3 | `___ta` | `5F C2` | `_` `_ta` | `k___` | `B3 E8 5F E8` | `ka` halant `_` halant |
| 4 | `____ta` | `5F 5F BD` | `_` `_` `ta` | `k____` | `B3 E8 5F 5F` | `ka` halant `_` `_` |
| 5 | `_____ta` | `5F 5F C2` | `_` `_` `_ta` | `k_____` | `B3 E8 5F 5F E8` | `ka` halant `_` `_` halant |
| 6 | `______ta` | `5F 5F 5F BD` | `_` `_` `_` `ta` | `k______` | `B3 E8 5F 5F 5F` | `ka` halant `_` `_` `_` |
| 7 | `_______ta` | `5F 5F 5F C2` | `_` `_` `_` `_ta` | `k_______` | `B3 E8 5F 5F 5F E8` | `ka` halant `_` `_` `_` halant |
| 8 | `________ta` | `5F 5F 5F 5F BD` | `_` `_` `_` `_` `ta` | `k________` | `B3 E8 5F 5F 5F 5F` | `ka` halant `_` `_` `_` `_` |

<!-- END GENERATED underscore-runs -->

Read the left half from top to bottom. Every pair of underscores becomes one `5F`; if one underscore is left over it is a marker for the letters that follow (`_ta` is the letter `C2`), and at the end of the input it is a halant. The right half shows the same at the end of the text, with the halant that a consonant brings with it. The behaviour does not depend on n except through the number of pairs and the parity.

**Law 1 (cut).** If `u` is closed, and `P(u)` and `P(w)` are defined, then `P(u __ w) = P(u) 5F P(w)`.

**Law 2 (run).** If `u` is closed and n >= 2, then `P(u _^n w) = P(u) 5F^(n div 2) P(m w)`, where `m` is `_` if n is odd and empty if n is even.

*Proof of Law 2.* The parse of `u` ends in L1, L2a or L2b (that is what closed means; for the empty `u` it is L1). In L1 the first `_` is read by the rule `'_' -> skip 1 ; goto L2c`; the second `_` finds no rule of L2c that starts with `_`, so the last rule of L2c applies (`raw c`: the character is kept as text) and writes `5F`; the parser is back in L1. In L2a the rule `[UNIT]` writes the halant that the consonant needs and goes to L1; in L2b the rule `.` writes the consonant with its `a` and goes to L2a. From L1 the argument is the one before. After two underscores the parser is in L1 and has written the same bytes as `P(u)` followed by `5F`, so the claim follows by induction on n. When one underscore is left, L1 reads it as a marker for the characters of `w`, which is the definition of `P(_ w)`; when none is left, the rest is `P(w)`. Law 1 is Law 2 with n = 2. The tests (U1) check both laws for every closed `u` of at most three letters and every `w` of at most two over the fifteen letters `aeiouhvzcktlnr_`, for random pairs of strings of up to eight letters, for n = 2 to 40 in sixteen times sixteen contexts, and on the C parser for a sample. ∎

**Closedness is needed.** If `u` ends in a marker, the first underscore of the run completes the marker's pair: `P(_ __ ta) = 5F C2`, not `E8 5F BD`. Every string of at most three letters (over the same fifteen letters) that is not closed breaks Law 1 for some `w` of at most two letters (U2).

**One underscore is different, and only through the halant.** For n = 1 the underscore meets the halant of the consonant before it: `k_ri` is KA and the *sign* RI (`B3 DF`), because `vocalic` finds the halant and replaces it; `k___ri` is KA, halant, `5F`, and the independent vowel RI (`B3 E8 5F AA`), because after the pair `vocalic` finds `5F`. This is the only interaction (U1).

**Law 3 (count).** For every string `s` that the grammar reads, the output has exactly one byte `5F` for every pair of underscores of `s`, counted run by run: `#5F(P(s)) = sum over the maximal runs of floor(n/2)`. This follows from Law 2 where it applies. It is *not* true for the grammar without the guards (the parser of patch 0001 alone, and the unpatched one), because of eleven rules (section 14.6), and it is true without exception for the grammar of this package, with the guards of section 14.7.

### 14.3 The marker rule: why a run has one reading

**The marker rule.** In every key of `acii.h` except `__`, each `_` is directly followed by a letter. (Keys: the 42 that start with `_`, `j_yna`, and the four `^_ri`, `^_li`, `^_lee`, `^_ree` that have the underscore after the `^`; `tools/check_tables.py` check T8 enforces the rule.)

**Consequences for the decoder's output.** The decoder writes a literal `5F` as the key `__`, doubled, and every other underscore it writes comes from a key and is followed by a letter of the same key. So in any text that the decoder writes for well-formed ACII (section 9.2), a run of n underscores consists of `(__)^k` (n = 2k), or of `(__)^k` followed by one marker that is directly followed by a letter (n = 2k + 1); a marker is never followed by another underscore, and never ends the text. The test (U4) decodes 5,000 random well-formed texts (default run) with 61,822 literal underscores in runs of up to 21 and checks that every run has this shape.

**The reading is unique.** Split a run of n underscores that is followed by a letter into tokens `__` (a literal) and at most one `_` (a marker), where the marker must be the last underscore of the run because it must touch the letter. For n even there is no marker, for n odd there is exactly one, and the number of pairs is fixed by n. There is exactly one split: the pairs first, the marker last. A "greedy" reader that takes `__` whenever it can, and a reader that works from the left one character at a time, both find it; a reader that prefers the marker, or that pairs from the right, finds a marker followed by an underscore and rejects the decoder's own output. The parser is a greedy left-to-right reader, so the rule that makes it correct is a property of the table, not of the parser.

**What the rule does not cover.** Text typed by people may have three underscores before a letter and mean something else; the parser still reads `___ta` as a literal underscore followed by `_ta`. A human who wants the two markers of `_ta` and `_ta` next to each other writes `_ta_ta`.

**Outside well-formed ACII the decoder does not keep the rule.** It builds its output by popping letters off a stack without regard to where a key begins, so a halant or a nukta in a place that section 9.2 forbids can take the letters of a key away and leave its underscore. `A4 E8` (an independent vowel, then a halant), `A2 E8` and `EB E8` are written `_`: an odd run with no letter after it, which the parser reads as a halant. `C4 E9` (dental DA, nukta) is written `__rda`, a literal underscore and `rda` (section 11.5). `A4 E9` is written `_za`, a marker in front of the letters of another key. The round-trip contract excludes such input (section 9.3). The test (U4) writes these sequences through the real decoder, so that the statement above is not read more widely than it holds.

### 14.4 The smallest machine

**Two states are necessary.** Take any closed `x`. The strings `x` and `x _` can be followed by the same suffix, `ta`, and the outputs differ: `P(x ta)` ends in TA (`BD`), `P(x _ ta)` ends in the letter `_ta` (`C2`). A transducer that distinguishes them must be in different states after reading `x` and `x _`. This is the distinguishing-suffix argument of Myhill and Nerode applied to the output (U3).

**Two states are sufficient.** By Law 2, after n >= 2 underscores the future behaviour depends on n only through its parity: the residual output of `P(x _^n w)` after the prefix `P(x) 5F^(n div 2)` is the same for all even n and the same for all odd n. The test (U3) collects these residuals for 16 closed prefixes and 16 suffixes and finds exactly two classes. The count of underscores is carried by the output (the number of `5F` bytes), not by the state, which is why N is unbounded and the machine is not.

The machine, as a transition table (`E` = even number of underscores read so far in this run, `O` = odd):

| state | reads `_` | reads a letter | reads the end |
|---|---|---|---|
| E | go to O | the run is over; no marker | nothing |
| O | write `5F`, go to E | the run is over; the underscore was a marker for this letter | the underscore was a halant |

This is a right-linear grammar with two non-terminals, `Run -> _ Odd | e`, `Odd -> _ Run | LETTER ...`, and so a regular language. A context-free grammar of the runs is not needed, and nothing in the runs asks for a second pass: the decision for each underscore is taken when the next character is seen. The lookahead is one character, *past* the run, and it only tells whether an odd run ends in a marker; the pairs themselves need none.

**The whole parser.** The state of the parser as a whole is: one of the five control states L1, L2a, L2b, L2c, M; the stem of L2b (one of 14); and the one bit that `vocalic` reads, whether the output ends in a halant. The lookahead is at most four characters (the guard of the longest rule). The two states of the run automaton are inside this: they are L1 against L2c.

### 14.5 The decoder, the escape, and the bijection

**The bijection.** Let `W` be the well-formed ACII texts of section 9.2, with any number of literal underscores (`5F`) between their syllables, and let `R` be the strings that the decoder `acii2rmn` writes for them. The decoder is injective on `W`, `rmn2acii` restricted to `R` is its inverse, and the underscore runs of the strings of `R` are the ones of section 14.3. So a run of N underscores in `R` stands for floor(N/2) literal underscores and, if N is odd, one marker, for every N; the correspondence needs no lookahead beyond the run. In the default run the test (U4) round-trips 5,000 random texts, some with runs of 21 underscores, through the models of both programs, for the grammar without the guards and for the grammar with them, and 3,000 of them through the C library of the mid and of the new build (`harness -f`).

**What it is not.** The inverse is partial: strings outside `R` have several spellings for the same bytes, so `acii2rmn(rmn2acii(r))` is a normalisation of `r`, not `r`. The filters (`acii2rmn.lex`) wrap every run of Latin letters and underscores in `"e_..."`, so a literal underscore of a Latin word never reaches the decoder; the bijection is a statement about the two library functions and the composition that the test harness calls the filter semantics.

**The escape.** For text that must go *through* the parser unchanged, for example the identifiers of a program, Hindawi uses `E = sed 's/_/__/g'` on the translated program before `rmn2acii` (`std2hin.awk`, twelve of its thirteen branches). After `E` every run has even length, so there is no marker, and every underscore of the text comes out as one `5F`. Precisely: let `s = x0 _^m1 x1 _^m2 x2 ...` with underscore-free segments `x_i`. If every segment is closed and `P(x_i)` is defined, then

```
P(E(s)) = P(x0) 5F^m1 P(x1) 5F^m2 P(x2) ...
```

This follows from Law 1 applied once for every underscore. The condition "closed and defined" is not a technicality: a segment that ends in `^` is not closed, and in the parser without the guards neither is a segment that ends in the letter `c` (or in `lv`, `_n` ...): the parser reads the first underscore of the next pair as something else (section 14.6), and the law fails. In the default run the test (U5) checks the equation, for the grammar without and with the guards, on 20,000 random strings with segments of one to six letters and on 5,000 of them in the C parser of each build.

### 14.6 Where the laws fail: eleven rules that read an underscore unseen

This section describes the parser before patch 0002: the unpatched parser and the parser of patch 0001 alone have the same eleven rules, and the analysis below is run on the grammar without the `!` rules. Section 14.7 is the repair.

A rule consumes the characters from the cursor up to its `skip` count. An underscore that is consumed as the *first* character of a unit, or as the second of a pair, is read as the grammar means. An underscore that is consumed in any other place is not looked at: either the guard has a wildcard `.` there, and the rule keeps the character as plain text, or the guard does not test the character at all and the rule jumps over it ("unseen"). Both break the count of Law 3, because a character that should have been the second half of a pair, or the start of the next unit, is swallowed. The same positions are the ones where a rule can step over the terminator and read the bytes that follow it (section 11.4). A static analysis of the grammar (`spec_model.sync_breakers`; U6) finds the eleven rules:

<!-- BEGIN GENERATED sync-breakers -->

| state | rule | what it does with the character after its guard | shortest string that breaks the pairing law |
|---|---|---|---|
| L1 | `'c' -> skip 2 ; goto L2b 'ch'` | jumps over 1 character unseen | `c__` |
| L2b | `'v' -> emit stem 'vra' ; skip 2 ; goto L2a` | jumps over 1 character unseen | `lv__` |
| L2c | `'e' -> emit '_ee' ; skip 2 ; goto L1` | jumps over 1 character unseen | `_e__` |
| L2c | `'y' -> emit '_yna' ; skip 2 ; goto L2a` | jumps over 1 character unseen | `_y__` |
| L2c | `'o' . -> raw d ; skip 2 ; goto L1` | keeps it as plain text (`.`) | `_o_` |
| L2c | `'n' . -> raw d ; skip 2 ; goto L1` | keeps it as plain text (`.`) | `_n_` |
| L2c | `'r' . -> raw d ; skip 2 ; goto L1` | keeps it as plain text (`.`) | `_r_` |
| L2c | `'j' . -> raw d ; skip 2 ; goto L1` | keeps it as plain text (`.`) | `_j_` |
| M | `'e' -> emit '^ee' ; skip 2 ; goto L1` | jumps over 1 character unseen | `je__` |
| M | `'_' -> emit '^_ri' ; skip 3 ; goto L1` | jumps over 2 characters unseen | `^__a` |
| M | `'o' . -> raw d ; skip 2 ; goto L1` | keeps it as plain text (`.`) | `jo_` |

11 rules, 12 positions; with the guards: 0

<!-- END GENERATED sync-breakers -->

The twelfth position is the second skipped character of the rule of state M that reads `_ri`; it is part of the same rule. The rules for `_o`, `_n`, `_r`, `_j`, `^o` keep the next character as text ("an unknown `_o?`: the o is dropped, the next character kept"); the others jump over it.

**What happens.** The string with the smallest length that breaks the law through each rule is in the last column. On every one of them the C parser of patch 0001 alone writes what the grammar writes (U6), so the table is a statement about the code and not only about the model. Three consequences were real in Hindawi's pipelines, which double every underscore of the translated program before they call the parser (twelve of the thirteen branches of `std2hin.awk`); the new build has none of them (U6):

- An identifier that has the letter `c` before an underscore lost the underscore. `tc_flag` reaches the parser as `tc__flag`; the filter of patch 0001 alone writes `BD E8 B8 E8 66 D1 B5 E8`, which has no `5F`: the rule for `c` has swallowed the first underscore of the pair, and the second has become a marker in front of `f`. The escaped underscore is gone. The new build writes `BD E8 63 5F 66 D1 B5 E8`: the `c` is a plain letter, and the pair is one `5F`.
- An identifier with `v` after one of the consonants that begin a stem asks for a row that does not exist (`tvra`): `tv_set`, which reaches the parser as `tv__set`, crashes the filter of patch 0001 alone (section 11.3). The new build does not ask for the row when the `v` is followed by an underscore or by the end of the string: it writes TA, the letter `v`, `5F` and the rest (`BD 76 5F D7 DC`).
- A rule that steps over the terminator reads whatever the buffer held before: `kakakaka _n` after another line gave different bytes depending on what came before (section 11.4). The new build writes the letter `n`, whatever came before.

### 14.7 Twelve guards (patch 0002)

Patch 0002 adds twelve rules to the grammar of section 5.3 and the twelve matching tests to `rmn2acii.c`. Each guard stands in front of one of the eleven rules above and has the form *if the character that the rule would jump over unseen is `_` or the end of the input, do not take the rule: write the letter as plain text, as the parser does for any other letter that it does not know*. In the grammar they are the rules tagged `!`, and the comment of each names its witness. The table is generated from them; its last column is the shortest string that breaks the pairing law if that guard alone is left out.

<!-- BEGIN GENERATED guards -->

| state | guard (a rule tagged `!`) | the rule it stands in front of | shortest string that breaks the pairing law without this guard |
|---|---|---|---|
| L1 | `'c' [_ $] -> raw c ; skip 1 ; goto L1` | `'c' -> skip 2 ; goto L2b 'ch'` | `c__` |
| L2b | `'v' [_ $] -> emit stem 'a' ; goto L2a` | `'v' -> emit stem 'vra' ; skip 2 ; goto L2a` | `lv__` |
| L2c | `'e' [_ $] -> raw c ; skip 1 ; goto L1` | `'e' -> emit '_ee' ; skip 2 ; goto L1` | `_e__` |
| L2c | `'y' [_ $] -> raw c ; skip 1 ; goto L1` | `'y' -> emit '_yna' ; skip 2 ; goto L2a` | `_y__` |
| L2c | `'o' [_ $] -> raw c ; skip 1 ; goto L1` | `'o' . -> raw d ; skip 2 ; goto L1` | `_o_` |
| L2c | `'n' [_ $] -> raw c ; skip 1 ; goto L1` | `'n' . -> raw d ; skip 2 ; goto L1` | `_n_` |
| L2c | `'r' [_ $] -> raw c ; skip 1 ; goto L1` | `'r' . -> raw d ; skip 2 ; goto L1` | `_r_` |
| L2c | `'j' [_ $] -> raw c ; skip 1 ; goto L1` | `'j' . -> raw d ; skip 2 ; goto L1` | `_j_` |
| M | `'e' [_ $] -> raw c ; skip 1 ; goto L1` | `'e' -> emit '^ee' ; skip 2 ; goto L1` | `je__` |
| M | `'_' [_ $] -> goto L1` | `'_' -> emit '^_ri' ; skip 3 ; goto L1` | `^__a` |
| M | `'_' . [_ $] -> goto L1` | `'_' -> emit '^_ri' ; skip 3 ; goto L1` | `^_^__` |
| M | `'o' [_ $] -> raw c ; skip 1 ; goto L1` | `'o' . -> raw d ; skip 2 ; goto L1` | `jo_` |

<!-- END GENERATED guards -->

The last two guards test the two characters that the old rule for `_ri` jumps over; the explicit `^` that led to state M is dropped, as the rule `.` of M already drops it for other characters, and the underscore is read again in L1. A guard that sends the underscore to L1 never keeps it as text: a literal underscore comes only from a pair. The guard of L2b is the one that does not write its letter as text: the stem keeps its `a`, and L2a and M read the `v` again as the plain letter that it is.

**In the C code.** Each guard is a test in front of an existing branch of `rmn2acii.c`: in `level1` for the letter `c`; in `level2b` for `v`; in `level2c` for `e`, `y`, `o`, `n`, `r`, `j`; in `matra` for `e`, `o` and for the `_` that follows an explicit `^`. The test is a one-line helper, `no_partner (char next)`, which is true for `_` and for the NUL byte. The action of a guard is the one that the function already has for "any other character", so no new function and no new state is needed: the parser has the same five control states, the same lookahead and the same recursive-descent shape (section 14.4). The edits are in `patches/0002-apply-underscore-guards.patch`; `tools/apply_guards.py` makes the same edits to the `rmn2acii.c` of patch 0001, each with an assertion that its anchor occurs exactly once.

**What changes for the user.** The guards change what a small set of invalid inputs mean, and nothing else. A letter that needs a partner (`c` without an `h`, `_e` without a second `e`, and so on) that is followed by an underscore or by the end of the string is now the plain letter, where patch 0001 alone swallowed the underscore or read the bytes that lay beyond the end. `c_` is the letter `c` and a halant (the `_` at the end of a text is a halant), not CHA with its `h` missing; `c` alone is the letter `c`; `lv` is LA and the letter `v`; `ke` is KA and the letter `e`; `_o_` is the letter `o` and a halant. Text that the decoder writes for well-formed ACII does not contain any of them (section 14.3), so for it nothing changes: all 331,621 sequences of up to three bytes that belong to `W` (section 9.2) read the same on the mid and on the new build, and the new build returns every one of them exactly (`tests/rt_filters.py`, part 5). Among the 394,419 sequences of up to three bytes over the old repertoire the guards change 2,482, none of them in `W`, none that was a round trip before and none that becomes one (for example `A1 DF`, a modifier followed by a sign: the decoder writes `_n_ri`, patch 0001 alone turns that into `5F CF DB` and the new build into `6E AA`, the letter `n` and the vowel RI). Patch 0002 is a patch of its own so that a project that does not want the change can leave it out, or take it off again with `patch -R`, without touching the Sanskrit characters of patch 0001.

**What the guards establish** (all of them are checked, U7):

1. No rule of the grammar can consume an underscore, or step over the terminator, unseen (the static analysis that finds the eleven rules in the grammar without the `!` rules finds none in the whole grammar).
2. Law 3 holds without exception: for every string that the parser reads, in the ranges of the next paragraph, the output has one `5F` for every pair of underscores.
3. The parser never reads past the end of the input. Together with a complete table this makes it a **total function**: every rule consumes at least one character or moves to a state that does, every state ends in a catch-all rule, no rule steps over the terminator, and every row that a rule asks for exists, so the parse of any string ends with an output. The first three conditions hold for the grammar with the guards; the last holds if the fifteen rows of section 11.3 are filled in.
4. Each guard is needed: with the rule left out, the string in the last column of the block breaks the law, and with it the law holds.
5. No guard fires on what the decoder writes for well-formed ACII: the parse of any two table keys written one after the other is unchanged, except where the parser of patch 0001 alone reads past the end (the key `^` followed by an underscore key: a halant at the start of a stretch, which is not well-formed ACII), and the round trips of section 14.5 are exact with and without the guards.
6. The guards change the output only of strings that contain a letter that needs a partner (`c`, `_e`, `_o` ...) directly before an underscore or the end of the input, where the parser of patch 0001 alone jumps over the underscore.
7. The C parser agrees with the grammar: on the twelve witnesses it writes what the grammar writes, one `5F` for every pair; and on 90,345 strings (the default run) its output is the same whatever follows the terminator (an underscore, a letter, what an earlier string left), where the C parser of patch 0001 alone differs on 11,000 of them.

The ranges of the option `--full`: all 551,881 strings of at most four letters over `a-z` and `_`, and all 1,118,481 strings of at most five letters over `acehjklnortvyz_^` (the letters that the rules test): no violation, no read past the end. The option `--deep` extends the second range to the 17.9 million strings of at most six letters. The table counts the strings of at most three letters over `a-z` and `_` (20,440) for the grammar without the guards (patch 0001 alone) and for the grammar with them, with the table as it is and with the fifteen missing rows filled in with a dummy byte:

<!-- BEGIN GENERATED underscore-counts -->

| grammar | table | defined | read past the end | missing row | of the defined: break the pairing law |
|---|---|--:|--:|--:|--:|
| without the guards (patch 0001 alone) | as it is | 18208 | 1726 | 506 | 20 |
| without the guards (patch 0001 alone) | 15 rows filled in | 18474 | 1966 | 0 | 20 |
| with the guards of section 14.7 (this package) | as it is | 20179 | 0 | 261 | 0 |
| with the guards of section 14.7 (this package) | 15 rows filled in | 20440 | 0 | 0 | 0 |

Of the 18208 strings that both versions read (the table as it is), the guards change the output of 86; on 66 of those the version without the guards kept the law, the others are the strings on which it did not.

<!-- END GENERATED underscore-counts -->

### 14.8 Case folding, and arbitrary changes to the text (Q2)

**What the code has.** The parser tests only lower-case letters, `_`, `^` and `|` in its guards; a capital letter is not a key letter and is passed through as text, with one exception, the wildcards, which keep any character. The lexers pass `[A-Za-z_]` runs to the parser, so capitals do arrive. The only place that folds is `Hindawi/hindrv/std2hin.awk`, which runs `tr 'A-Z' 'a-z'` on the program text for two of its language styles (`praa_tha`, `praa_thamika`), before the translation to Romenagri and before the escape `E` of section 14.5.

**The algebra.** Let `phi` be that fold, letter by letter.

- `phi` is a monoid homomorphism of strings, `phi(uv) = phi(u) phi(v)`, it is idempotent, it fixes `_`, digits and punctuation, and it is not injective (`A` and `a` go to `a`). It keeps every run of underscores: the number and lengths of the runs are the same before and after (U8).
- Capital letters are inert in the parser: if every capital of `s` is replaced by `Q`, the output is the same up to that replacement (U8). So the restriction to lower case removes only letters that the parser would pass through anyway; it does not change the transducer on the strings that remain, and the laws of section 14.2 hold on both sides of the restriction.
- The parser is not a homomorphism, with or without the restriction (`P(uv) != P(u) P(v)` in general: the halant, `vocalic`). It is closed under composition with `phi`: `P` after `phi` is again a sequential function.
- `phi` does not commute with `P`, and it could create a breaker. The escaped text `C__f` parses to `C 5F f` (`43 5F 66`). Its fold `c__f` parses, in patch 0001 alone, to `B8 E8 66`: the letter `c` swallows the first underscore (section 14.6) and the escaped underscore is lost (U8). With the guards `c__f` is `63 5F 66`: the fold turns a capital into a lower-case letter and the underscore stays.

**Crash-resilience.** "Arbitrary string mutations by the host" include a case change, truncation at any point, insertion or deletion of any character, doubling or halving of underscores, and concatenation. For the grammar with the guards and a complete table, the parser is a total function (section 14.7, item 3), so none of them can make it fail: the claim is proved by the induction on the rules that item 3 states, and checked on all strings in the ranges of section 14.7. The checks include 14,762 random mutations of valid spellings in the default run, with the parser defined on every one once the table is complete (U8).

The C code of this package is as resilient as that grammar, except for three things, none of which involves the underscore:

1. fifteen rows that the grammar asks for are missing (section 11.3), so a mutation that puts a letter after the `v` that follows a consonant stem (`kva`, `tvx`), or that produces `lh` or `_rrh`, crashes the parser;
2. the buffers have fixed sizes (section 11.4), so a long enough run overflows them;
3. the decoder pops an empty stack on a stray halant or nukta (section 11.4).

Patch 0001 alone had a fourth: eleven rules read an underscore or the terminator unseen (section 14.6), so a truncation after `c` or `_n` read past the end of the input. On the 14,762 mutations of the default run, the grammar without the guards reads past the end of the input on 360 (2.4%) and asks for a missing row on 40 (0.3%), and the C parser of patch 0001 alone crashes on 43. With the guards the grammar never reads past the end and asks for a missing row on 35, and the C parser of this package crashes on exactly those 35 and on no other (U8). So the answer to "can it be formally verified as crash-resilient" is: *yes, by the argument above, for the grammar of section 14.7 once the table is complete*, and *for the C code of this package up to the three reasons above*; for patch 0001 alone it was *not*. The proof is an induction and a finite exhaustive check, not a machine-checked proof; the connection between the grammar and the C code is the agreement test of `tests/diff_parser.py`, not a proof either.

### 14.9 Joiners and operators (Q3)

**Where the two alphabets meet.** Through the lexers, the parser sees only runs of `[A-Za-z_]`; the rest of the text, host operators and escapes included, is copied by the lexer (section 11.1). The parser changes 16 of the 95 printable ASCII bytes when each is given alone: the fifteen letters `bdgjklmnprstwxy` and `_`. (Patch 0001 alone changed 17: a lone `c` read past the end of the string and came out as CHA; the guard of section 14.7 leaves it the letter `c`.) `acii2cf` and `acii2pcf` change none of the 95; `acii2rmn` wraps all 52 letters and `_` in `"e_x"` and leaves the other 31 punctuation marks, among them every operator of C, C++, Java and Python. So the script and the host languages share *one* character, the underscore, and the only context that has to be kept is the one of section 14.4: two states (U9).

**The joiners that the converters cannot carry.** ZWJ (U+200D) and ZWNJ (U+200C) have no row in any table. `uni2acii` writes their low bytes, `0D` and `0C`, a carriage return and a form feed (section 11.6). ISCII encodes the same two things as the byte pairs halant-halant (explicit halant) and halant-nukta (soft halant); `acii2rmn` does not read them: `B3 E8 E8` comes out empty (the consonant is lost), `B3 E8 E9` crashes it. By accident the parser *writes* the first pair: `k_` is `B3 E8 E8`, because a `_` at the end is a halant and the consonant has one already. So the spelling exists in one direction and cannot be read back.

**What a joiner costs.** The grammar is open to joiners at one place. A joiner key with an underscore in front is a family letter. Adding `_zwj` and `_zwn` takes two rules in state L2c and two rows in `acii.h`, and nothing else in the grammar (U9): the states, the longest guard and the list of unguarded rules of section 14.6 are unchanged (the two joiner rules test every character that they skip, so they need no guard rule), the marker rule holds, and the run law holds with them (`k___zwj` is KA, halant, a literal underscore and the joiner; `k__zwj` the same with the ordinary reading of `zwj`). The cost is in the other direction: the decoder has to know that a halant follows a halant, which is a look at the byte before, as it already does for the attribute prefix `EF`; and a byte has to be found (section 10.3), because the ISCII pairs are already the encoding of the halant.

**The collisions that remain.** The projection of `acii2cf` is not injective: the Devanagari letter KA and the Latin word `ka` both come out as `ka` (U9). That is a design choice of the C-friendly filters, not an artefact of the underscore, and it is where the script and the host language cannot be told apart again after the fact. The underscore at the junction of a Latin word and Devanagari text (`trace_` followed by KA) is written `trace__ka` by `acii2cf` and `trace_ka` by `acii2pcf` (section 11.1): the first lets the decoder double it, the second does not.

**The answer.** The minimal state-transition complexity to tell the underscore's roles apart is two states; joiners that obey the marker rule cost zero; the separation of script from host language costs no state in the parser because it is made, without memory, in the lexers.

### 14.10 What is proved, what is tested, what is open

| Statement | Status |
|---|---|
| Laws 1 and 2 (cut, run) for closed prefixes | proved in section 14.2; tested exhaustively in a range, at random, and on the C parser (U1, U2) |
| the marker rule | a property of the table, checked by lint T8; its consequences for the decoder's output on well-formed texts tested on 5,000 texts, and what happens outside them shown on six sequences (U4) |
| two states are necessary and sufficient for runs | argued in section 14.4; tested (U3) |
| the bijection of section 14.5 | tested on random well-formed texts, models and C (U4); argued from Law 2 |
| the escape law | argued from Law 1; tested on models and C (U5) |
| eleven rules read an underscore unseen (patch 0001 alone) | static analysis, and C against the grammar on the witnesses (U6) |
| the twelve guards: Law 3, no read past the end, totality with a complete table | argued by induction on the rules; checked exhaustively in the ranges of section 14.7 (U7) |
| the guards in the C code | **implemented** (patch 0002); the C parser agrees with the grammar on every string of the differential test, fixes the twelve witnesses, and does not depend on what follows the terminator (U7) |
| crash-resilience of the C code of this package | **true except for three reasons** that do not involve the underscore (missing rows, fixed buffers, the decoder's empty stack); false for patch 0001 alone, for a fourth (U8) |
| a machine-checked proof (Coq, Lean) of any of this | **open**; the models are small enough that it could be done |

## 15. The nukta layer (patch 0003)

Patch 0003 adds a layer to the two Unicode converters, `uni2acii` and `acii2uni`. It has three parts, which are kept apart:

- the **rule**: a letter with a nukta is a consonant and a nukta, however it arrives. `uni2acii` writes the eleven precomposed nukta letters of Unicode that way. The rule is not an option;
- the **form**: what the two converters write for the letters of this family, as one code point or as two. That is the Unicode layer, and it belongs to the user: `asis` (the default, which is what the converters always wrote), `nfc` or `nfd`, chosen on the command line, in the environment, when the converter is compiled, or by a function call;
- the **warning**: `uni2acii -w` reports each code point that it writes as a low byte, among them the é that collides with the nukta. It is off unless it is asked for.

No row of any table changes, and neither the decoder nor the parser is touched. The design is the one that the author decided on, case by case, on 8 November (section 15.7). The first form of this patch, which rebuilt the pairs by default and was steered by a macro, is gone (section 15.6). The statements below are of the three kinds of section 1: *defined* (the table and the rules, which are `nukta.h` and the two programs), *observed* (each names the part of `tests/test_nukta.py` that measures it) and *cited* (section 12.1).

### 15.1 What was missing

ACII writes a letter with a nukta as two bytes, the consonant and `E9`, which is U+093C (R7 of section 6 gives its key: the stem, `z`, `a`). Unicode has eleven letters that are such a pair in one code point. `unicode.h` had a row for two of them, U+0929 and U+0931 (`C7` and `D0`), and none for the other nine. For those, `uni2acii` fell back to the low byte of the code point (section 3.1): U+095C became `5C`, a backslash, and U+0934 became the digit `4` (section 11.6). The damage does not stop at the letter. The decoder takes `5C` for an ordinary character, and a halant behind it takes that character off again (the rule of section 11.5 for a halant where the grammar does not allow one): `5C E8 D4` is written `wa`, so the cluster ड़्व of section 11.3, written with the single code point U+095C, came back as व alone (test (k), C6). Section 10.4 used to advise a normalisation to NFD before `uni2acii`. That works, but it asks every pipeline to do it, and it fails silently where someone forgets.

The other direction produced correct Unicode, but it wrote a consonant and `E9` as two code points. Whether the text that comes back should be in normalisation form C, in form D, or in neither is not for a converter to say: it depends on what reads the text next. So the layer makes it a choice (section 15.2), and the default stays what it was.

### 15.2 The design

| File | Change |
|---|---|
| `nukta.h` | **new.** The table `nukta_hin`, eleven rows `{low, high, base low, base high, nfc}` (section 15.3); `NUKTA_BYTE`, the byte of U+093C (`E9`); the forms `NUKTA_ASIS`, `NUKTA_NFC`, `NUKTA_NFD` and the macro `NUKTA_FORM`, the default form (`NUKTA_ASIS`); the variable `nukta_form` and the function `nukta_set_form()`; the function `nukta_options()`, which reads the environment and the flags of the two converters; and the helpers `nukta_acii_of` and `nukta_row_of`. It is included after `unicode.h`. |
| `uni2acii.c` | the rule, the form, the options `-f` and `-w`, and the warning layer |
| `acii2uni.c` | the table lookup moved, unchanged, into a function `put`; the form; the option `-f` |
| `Makefile` | `nukta.h` is a prerequisite of the `unicode` target, and is installed and removed with `unicode.h` |
| `TRANSLITERATION.md` | this document |

**The rule.** Unicode did not apply one rule to the letters with a nukta. Some of them were given a code point of their own and the others were not, and of those that were, three are composed by NFC and eight are not (section 15.3). The layer is uniform where Unicode is not: inside, a letter with a nukta is a consonant and a nukta, as ACII writes it, whether it arrives as the single code point, as two code points, as the ACII bytes (`BF E9`) or as Romenagri (`_rda`). So `uni2acii` writes a code point that `unicode.h` has no row for and that `nukta.h` lists (the eight of U+0958 to U+095F, and U+0934) as the byte of its consonant, then `E9`. This is how the sound of the modified consonant is found, and it is always done: it is what makes the cluster ड़्व with the single code point U+095C work (section 15.7, C1 and C6).

**Level 1.** The parser maps a consonant at its first stage, `level1` (the state L1 of section 5.1), and what attaches to the consonant (the halant, an adjunct consonant, a vowel sign) at its second stage, `level2a`, `level2b`, `level2c` and `matra`. The author's decision is that a nukta letter is broken into its base sound and the nukta at the first stage, before anything is bound at the second; otherwise the sound of the modified consonant could not be mapped. The converters stand in front of the parser in every chain that starts with Unicode, so the rule is applied earlier still, where the text enters: when `uni2acii` has written the consonant and `E9`, the decoder, the parser and the filters never meet a precomposed letter, and what they bind a halant, an adjunct consonant or a vowel sign to is a consonant with its nukta. The parser (`rmn2acii.c`) is not changed, and it needs no rule for a cluster of such a letter.

**The form** is the Unicode layer, and it is kept apart from the rule. The rule fixes what a nukta letter is inside; the form fixes how the two converters write the family at the Unicode end (and, for `uni2acii`, at the byte end), as one code point or as two:

- `asis`, the **default**, is what the converters always wrote. The byte of a row of `unicode.h` is used as it is (U+0929 is `C7` and `C7` is U+0929), and a consonant and a nukta that arrive as two code points, or as two bytes, stay two. The one change is the nine letters that `unicode.h` has no row for, which are no longer written as a low byte;
- `nfc` is Unicode's normalisation form C. Where NFC composes a consonant and a nukta they are one code point (`acii2uni`: `C6 E9`, `CF E9` and `D2 E9` are U+0929, U+0931 and U+0934), or the one byte that `unicode.h` has for the letter (`uni2acii`: U+0928 U+093C is `C7`, U+0930 U+093C is `D0`). The eight letters that NFC leaves decomposed stay a consonant and a nukta;
- `nfd` is form D: all eleven letters are a consonant and a nukta in both programs (`acii2uni` writes `C7` as U+0928 U+093C and `D0` as U+0930 U+093C; `uni2acii` writes U+0929 as `C6 E9` and U+0931 as `CF E9`).

What each form writes (a real run of the built converters; `tests/test_nukta.py`, parts (b), (d) and (h)):

| | `asis` (default) | `nfc` | `nfd` |
|---|---|---|---|
| **`acii2uni`**, ACII in, Unicode out | | | |
| `C7` | ऩ (`U+0929`) | ऩ (`U+0929`) | ऩ (`U+0928 U+093C`) |
| `D0` | ऱ (`U+0931`) | ऱ (`U+0931`) | ऱ (`U+0930 U+093C`) |
| `C6 E9` | ऩ (`U+0928 U+093C`) | ऩ (`U+0929`) | ऩ (`U+0928 U+093C`) |
| `CF E9` | ऱ (`U+0930 U+093C`) | ऱ (`U+0931`) | ऱ (`U+0930 U+093C`) |
| `D2 E9` (ळ and a nukta) | ऴ (`U+0933 U+093C`) | ऴ (`U+0934`) | ऴ (`U+0933 U+093C`) |
| `BF E9` (and the other seven) | ड़ (`U+0921 U+093C`) | ड़ (`U+0921 U+093C`) | ड़ (`U+0921 U+093C`) |
| **`uni2acii`**, Unicode in, ACII out | | | |
| ऩ (`U+0929`) | `C7` | `C7` | `C6 E9` |
| ऱ (`U+0931`) | `D0` | `D0` | `CF E9` |
| न + nukta (`U+0928 U+093C`) | `C6 E9` | `C7` | `C6 E9` |
| र + nukta (`U+0930 U+093C`) | `CF E9` | `D0` | `CF E9` |
| ऴ (`U+0934`) | `D2 E9` | `D2 E9` | `D2 E9` |
| ड़ (`U+095C`), and ड + nukta | `BF E9` | `BF E9` | `BF E9` |

No form writes the eight letters of U+0958 to U+095F as single code points: that is the one thing that the first version of the patch could do (section 15.6) and no longer does.

**Choosing the form.** The same choice can be made at four levels. Where more than one is given, the later row of this table wins:

| Level | How | Example |
|---|---|---|
| the build | the macro `NUKTA_FORM`, given when a converter is compiled; it sets the default form of that build | `make unicode CFLAGS="-Wall -Wno-unused -DNUKTA_FORM=NUKTA_NFC"` |
| the environment (a pipeline, an integration that starts the converters) | the variable `ROMENAGRI_NUKTA_FORM` | `ROMENAGRI_NUKTA_FORM=nfc iconv -futf8 -tutf16 \| uni2acii` |
| the command line | `-f FORM` or `--form=FORM`, on both converters | `acii2uni -f nfd in.acii out.utf16` |
| a function call | a program that includes `nukta.h` calls `nukta_set_form ("nfc")`, or sets `nukta_form`; `nukta_options()` reads the environment and the flags for it | `if (nukta_set_form (argv[1]) < 0) ...` |

The names are read in lower or upper case. An empty `ROMENAGRI_NUKTA_FORM` counts as not set. A name that is not a form, a flag without its value, and an option that the converter does not know are errors: a message on stderr, the usage line on stdout, exit status 1, and nothing is converted. `nukta_set_form` returns 0, or -1 for a name that is not a form and then changes nothing. The options come before the file names (`--` ends them), and the two file names are still given together or not at all. Tested in part (c).

**The warning layer.** `uni2acii` writes the low byte of a code point that `unicode.h` has no row for. Every converter of this kind does this, and it is a known bug of them (section 11.6): the low byte of U+00E9, an e with an acute accent, is `E9`, the nukta, so that नé is read back as a न with a nukta. The converter does not try to mend it: a character that has no ACII byte is a normal character, and what has been consumed as Unicode is not carried on in a mixed state. What the layer adds is a way to see it. With `-w` (or `--warn`), or with `ROMENAGRI_NUKTA_WARN=1` in the environment, `uni2acii` reports each such code point once, on stderr, with a note about the known bug and a count at the end (a character above U+FFFF is reported as its two UTF-16 units). Nothing is reported by default, the bytes written are the same with and without it, and `acii2uni` has no such option. For the text of C5 below, `uni2acii -w` writes:

```
uni2acii: note: a code point that unicode.h has no row for is written as its low byte, which ACII reads as another character; every converter of this kind does this (TRANSLITERATION.md, section 11.6)
uni2acii: warning: U+00E9 has no ACII byte and is written as its low byte E9, the nukta byte
uni2acii: 1 code point with no ACII byte was written as its low byte (0 further occurrences not listed)
```

**Writing (`uni2acii`).** For a code unit:

1. if the form is `nfd` and `nukta.h` lists it as a letter, write the byte of its consonant and `E9`;
2. otherwise, if `unicode.h` has a row for it, write the byte of the row. The table comes first: U+0929 stays `C7` and U+0931 stays `D0`, and a row that someone adds for one of the other nine, as recipe A does for U+0934, wins too. In the form `nfc` a row byte that is the consonant of a letter that has a byte of its own (`C6` for U+0928, `CF` for U+0930) waits for the next code unit: if that is U+093C, the byte of the letter is written (`C7`, `D0`) and the nukta is not, and otherwise the held byte is written as it always was; a newline and the end of the input end the wait. Only a byte that came from a row waits, so that a character that fell back to its low byte (Æ, U+00C6, whose low byte is `C6`) is never made into a nukta letter by the byte that it happens to share;
3. otherwise, if `nukta.h` lists it and its consonant has a byte in `unicode.h`, write that byte and `E9`;
4. otherwise write the low byte, as before (and report it, if the warning layer is on and the code unit is not an ASCII character).

**Reading (`acii2uni`).** A byte is written by its row in `unicode.h` or, if it has none, as the byte modulo 128, as it always was. In the form `nfd` a code point that `nukta.h` lists as a letter (the rows `C7` and `D0` give U+0929 and U+0931) is written as its consonant and U+093C. In the form `nfc` a byte is *held back* if it is the byte of the consonant of a letter that NFC composes (`C6`, `CF`, `D2`). The next byte decides. If it is `E9`, the converter writes the one code point of the letter and nothing for the `E9`. If it is anything else, the converter writes the held byte exactly as it always did and goes on with the new byte, which may itself be held back. A newline and the end of the input also end the wait. In the form `asis` there is no state at all.

The converters keep no other state and look at most one byte (or one code unit) ahead. Nothing is added to `unicode.h`: a nukta letter takes no byte of the free list of section 10.1.

### 15.3 The eleven letters

<!-- BEGIN GENERATED nukta-table -->

| Letter | Code point | Name | = | ACII of the pair | `uni2acii` before, after (default form) | Unicode NFC |
|---|---|---|---|---|---|---|
| ऩ | U+0929 | nnna | न + ◌़ | `C6 E9` | `C7`, `C7` | composes it |
| ऱ | U+0931 | rra | र + ◌़ | `CF E9` | `D0`, `D0` | composes it |
| ऴ | U+0934 | llla | ळ + ◌़ | `D2 E9` | `34` (the low byte: corruption), `D2 E9` | composes it |
| क़ | U+0958 | qa | क + ◌़ | `B3 E9` | `58` (the low byte: corruption), `B3 E9` | leaves it decomposed (composition exclusion) |
| ख़ | U+0959 | khha | ख + ◌़ | `B4 E9` | `59` (the low byte: corruption), `B4 E9` | leaves it decomposed (composition exclusion) |
| ग़ | U+095A | ghha | ग + ◌़ | `B5 E9` | `5A` (the low byte: corruption), `B5 E9` | leaves it decomposed (composition exclusion) |
| ज़ | U+095B | za | ज + ◌़ | `BA E9` | `5B` (the low byte: corruption), `BA E9` | leaves it decomposed (composition exclusion) |
| ड़ | U+095C | dddha | ड + ◌़ | `BF E9` | `5C` (the low byte: corruption), `BF E9` | leaves it decomposed (composition exclusion) |
| ढ़ | U+095D | rha | ढ + ◌़ | `C0 E9` | `5D` (the low byte: corruption), `C0 E9` | leaves it decomposed (composition exclusion) |
| फ़ | U+095E | fa | फ + ◌़ | `C9 E9` | `5E` (the low byte: corruption), `C9 E9` | leaves it decomposed (composition exclusion) |
| य़ | U+095F | yya | य + ◌़ | `CD E9` | `5F` (the low byte: corruption), `CD E9` | leaves it decomposed (composition exclusion) |

`NUKTA_BYTE` is `E9`, the byte of U+093C in `unicode.h`; the default `NUKTA_FORM` is 0 (asis).

<!-- END GENERATED nukta-table -->

The last column is not read from `nukta.h`. `tools/gen_doc_tables.py` takes it from Python's `unicodedata` (Unicode 15.1), and `tests/test_nukta.py`, part (a), requires that the `nfc` mark of every row (1 for the letters that NFC composes, 0 for the eight that it does not) agrees with it, and that the rows are exactly the code points of the Devanagari block whose NFD is a consonant and U+093C. The eight are what the Unicode Standard calls *composition exclusions*: precomposed characters that NFC does not produce (cited, section 12.1). The two rows that have a byte of their own in `unicode.h` keep it, so ऩ and ऱ have two spellings in ACII, the byte (`C7`, `D0`) and the pair (`C6 E9`, `CF E9`), and in the form `asis` they come out of `acii2uni` as they went in, one as the single code point and one as the pair. In the forms `nfc` and `nfd` the two spellings come out alike.

### 15.4 What does not change

- **`uni2acii` writes the same bytes as before for every other code unit of the BMP, in every form.** Observed on all 65,525 code units but the eleven letters (test (g)). The nine were the low byte before and are two bytes now; the two with a row are unchanged in `asis` and `nfc` and two bytes in `nfd`.
- **The default `acii2uni` writes what it wrote before,** byte for byte: on 30,000 random streams, on all 64,516 pairs `x y`, on all 64,516 triples `x E9 y` and on all 64,516 triples `x y E9` of bytes other than CR and LF (test (d)). The form `nfc` differs from it in the three pairs `C6 E9`, `CF E9` and `D2 E9` only (of the 64,516 pairs `x y`, these three), and the form `nfd` in the 1,012 pairs that hold `C7` or `D0`.
- **The default `uni2acii` differs from the converter of patch 0001 in the nine letters only.** Text that contains none of the nine single code points is converted exactly as before.
- **Nothing else reads `nukta.h`.** The decoder, the parser, the filters and the saral table are as before. Text that contained one of the nine single code points used to be damaged before it reached the filters; now it is not.
- **The extension recipes still work.** Recipe A gives U+0934 a byte of its own, and in the forms `asis` and `nfc` the table wins over the layer (section 8.2); in the form `nfd` the layer writes the pair.

### 15.5 Where the layer stops

1. **It does not reorder.** NFC and NFD move a nukta (combining class 7) in front of a halant (class 9) or an accent (class 220 or 230). The converters never reorder anything, and the layer does not start: ऩ् (U+0928 U+094D U+093C, bytes `C6 E8 E9`) comes back as it went in, in every form, where NFC writes U+0929 U+094D. A layer that folded across the halant would also have to tell a nukta from ISCII's soft halant, which is written `E8 E9` as well (conflict C8 of section 10.5). No decision was taken (C3). Observed (test (f), quick run): of 30,000 random streams, 28,981 have their marks in canonical order, and on those `nfc` equals Python's NFC and `nfd` equals its NFD of what the default converter writes, without an exception; the other 1,019 (1,009 of them with a nukta after a halant or an accent) have marks that NFC and NFD would reorder, and on every one of them they differ from the layer.
2. **The round trip is exact only up to canonical equivalence.** ड़ (U+095C) goes in and U+0921 U+093C comes out, in every form. The two look the same on a screen and are the same text for Unicode, but a byte comparison, or a search for one, does not find the other.
3. **Romenagri is not extended.** The decoder reads the pair as before, and `acii2rmn` still crashes on a halant followed by a nukta (`C6 E8 E9` ends with signal 11, section 11.4). The fifteen reserved keys (section 11.3) are untouched: ऱ्ह and ल्ह have always passed through the chain from Unicode, and the typed forms `lh`, `_rrh`, `_rdvr` and the others still crash `rmn2acii`.
4. **The low-byte problem remains for everything else.** U+00E9 (e with an acute accent) is written as `E9`, which is the nukta, and an `E9` after the byte of न, र or ळ is read as a nukta: नé comes back as न and a nukta (as ऩ in the form `nfc`), exactly as it did before the layer. Neither is the letter that went in. The warning layer makes it visible (C5); the cure is the one that section 11.6 names: deal with the characters that are not in the tables before `uni2acii`.
5. **The joiners are not handled.** ZWJ and ZWNJ still fall back to `0D` and `0C` (section 10.4).

### 15.6 What replaced `NUKTA_REBUILD`

The first form of this patch (zip no. 4) rebuilt `C6 E9`, `CF E9` and `D2 E9` as single code points by default, and chose the output by a macro, `NUKTA_REBUILD`, with three levels. It is gone, for three reasons that the author gave on 8 November: the output form is the user's to choose and not the policy of a build; the default must be what the converters always wrote; and Unicode's normalisation is a layer of its own that must not be mixed with the rule. Compiling with `-DNUKTA_REBUILD` stops the compiler with a message that names `NUKTA_FORM`.

| First form | Now |
|---|---|
| `NUKTA_REBUILD=0`: always two code points | the default, `asis` (also `-f asis`) |
| `NUKTA_REBUILD=1`, the old default: NFC | `-f nfc` (also `NUKTA_FORM=NUKTA_NFC`, and `ROMENAGRI_NUKTA_FORM=nfc`) |
| `NUKTA_REBUILD=2`: all eleven as single code points | none. Any normaliser splits the eight again, and the rule keeps one writing for a letter; a fourth form would be a table row away if it were wanted |
| (none: `uni2acii` ignored the level) | `-f nfd`, new, for both converters |

### 15.7 The challenges, in Devanagari, and what was decided

Each case below is a place where the layer, or the standard that it follows, asked for a decision or left a limit. The author decided each on 8 November; the decision stands first. Each is printed by `tests/test_nukta.py`, part (k), from a real run of the converters and the two filters, and each is asserted there: the tables quote that output, with the input and the output as Devanagari and as code points. A row says "all three" when the three forms give the same line; otherwise a row of its own is given for the forms that differ.

**C1. One letter in two spellings, and the eight composition exclusions.** ड़ can be typed as the single code point U+095C or as ड and a nukta (U+0921 U+093C); the same holds for क़ ख़ ग़ ज़ ढ़ फ़ and य़. Both spellings give `BF E9`. *Decision:* the output is not fixed to NFC, and Unicode is not to be confused with the emission layers: it keeps a layer of its own, the form (section 15.2). The decomposition is not left as an "or" either. It is done explicitly at level 1, because otherwise the sound of the modified consonant cannot be mapped: level 1 is where the consonants are mapped to their original sounds, before level 2 attaches the vowel signs. So the rule writes the consonant and the nukta, always, and no form writes the eight as single code points.

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| the single code point | ड़ (`U+095C`) | all three | `BF E9` | `_rda` | ड़ (`U+0921 U+093C`) |
| a letter and a nukta, as a keyboard types it | ड़ (`U+0921 U+093C`) | all three | `BF E9` | `_rda` | ड़ (`U+0921 U+093C`) |
| all eight, as single code points | क़ख़ग़ज़ड़ढ़फ़य़ (`U+0958 U+0959 U+095A U+095B U+095C U+095D U+095E U+095F`) | all three | `B3 E9 B4 E9 B5 E9 BA E9 BF E9 C0 E9 C9 E9 CD E9` | `kzakhzagzajza_rda_rdhaphzayza` | क़ख़ग़ज़ड़ढ़फ़य़ (`U+0915 U+093C U+0916 U+093C U+0917 U+093C U+091C U+093C U+0921 U+093C U+0922 U+093C U+092B U+093C U+092F U+093C`) |

**C2. ऩ ऱ ऴ against their pairs.** Unicode gave a code point of its own to some letters with a nukta and none to others, with no uniform rule, and that is the root of the problem. *Decision:* the layer is uniform inside: for all eleven, a character and a nukta. Nothing more is decided for this case (none). What comes out is the business of the form: ऩ and ऱ have two spellings in ACII (`C7` and `C6 E9`, `D0` and `CF E9`), and `acii2uni` reads each as before in `asis`, both as the single code point in `nfc` and both as the pair in `nfd`.

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| the single code points | ऩऱऴ (`U+0929 U+0931 U+0934`) | asis | `C7 D0 D2 E9` | `_nza_rralvrza` | ऩऱऴ (`U+0929 U+0931 U+0933 U+093C`) |
|  |  | nfc | `C7 D0 D2 E9` | `_nza_rralvrza` | ऩऱऴ (`U+0929 U+0931 U+0934`) |
|  |  | nfd | `C6 E9 CF E9 D2 E9` | `nzarzalvrza` | ऩऱऴ (`U+0928 U+093C U+0930 U+093C U+0933 U+093C`) |
| consonant and nukta, three times | ऩऱऴ (`U+0928 U+093C U+0930 U+093C U+0933 U+093C`) | asis, nfd | `C6 E9 CF E9 D2 E9` | `nzarzalvrza` | ऩऱऴ (`U+0928 U+093C U+0930 U+093C U+0933 U+093C`) |
|  |  | nfc | `C7 D0 D2 E9` | `_nza_rralvrza` | ऩऱऴ (`U+0929 U+0931 U+0934`) |

**C3. A nukta after a halant.** NFC would move the nukta in front of the halant and compose it (U+0929 U+094D), and `E8 E9` is also how ISCII writes a soft halant, which made `acii2rmn` crash on it before the layer (section 11.4). *Decision:* none taken. The layer leaves the sequence alone in every form (section 15.5, item 1).

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| न + halant + nukta (NFC: U+0929 U+094D) | ऩ् (`U+0928 U+094D U+093C`) | all three | `C6 E8 E9` | (acii2rmn crashes) | ऩ् (`U+0928 U+094D U+093C`) |

**C4. A nukta that does not follow a consonant directly.** After a vowel sign, after a space, at the start of a line: there is nothing to rebuild, and NFC agrees, because a vowel sign has combining class 0 and blocks the composition. *Decision:* no fixed format is locked in. The choice of NFC or NFD for what comes out is a user option, as a command-line flag, an environment variable, a build macro or a function call (section 15.2); the default stays aligned with what the converters did, and users and integrators have full control at every level.

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| न + sign I + nukta (NFC does not compose it either) | नि़ (`U+0928 U+093F U+093C`) | all three | `C6 DB E9` | (not run) | नि़ (`U+0928 U+093F U+093C`) |
| न + space + nukta | न ़ (`U+0928 U+0020 U+093C`) | all three | `C6 20 E9` | (not run) | न ़ (`U+0928 U+0020 U+093C`) |

**C5. The letter é is written as the nukta.** `uni2acii` writes U+00E9 as `E9`, its low byte, and `E9` is the nukta (section 11.6). After न, र or ळ the byte is read as a nukta, as it was before the layer, and in the form `nfc` the pair is composed. *Decision:* encodings are not mixed. Once Unicode, or any other input encoding, has been consumed, it does not survive in a mixed state: the é is a normal character that has no ACII byte and is treated like every other, so the question of Unicode mixing with it does not arise. What is added is a warning layer, which notes this known bug of such converters, off by default and enabled only by a flag or by the call that integrates the converter (section 15.2).

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| न + é: the é was never a nukta | नé (`U+0928 U+00E9`) | asis, nfd | `C6 E9` | `nza` | ऩ (`U+0928 U+093C`) |
|  |  | nfc | `C6 E9` | `nza` | ऩ (`U+0929`) |

**C6. The cluster ड़्व with the single code point.** Without the layer `uni2acii` wrote the low byte, `5C`, and `acii2rmn` lost it together with the halant behind it (section 15.1). *Decision:* it is not a case of its own and gets no special rule, no fix that names a cluster. It is resolved by the rule of C1: the precomposed consonant is broken into its base sound and the nukta before the halant and the adjunct consonant are bound at level 2, so the formation of clusters is general. The test passes the fifteen clusters of section 11.3 through the chain in all three forms (part (j)).

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| with the layer: the single code point | ड़्व (`U+095C U+094D U+0935`) | all three | `BF E9 E8 D4` | `_rdwa` | ड़्व (`U+0921 U+093C U+094D U+0935`) |
| with the layer: ड + nukta | ड़्व (`U+0921 U+093C U+094D U+0935`) | all three | `BF E9 E8 D4` | `_rdwa` | ड़्व (`U+0921 U+093C U+094D U+0935`) |
| patch 0001 alone: what it did before | ड़्व (`U+095C U+094D U+0935`) | asis | `5C E8 D4` | `wa` | व (`U+0935`) |

**C7. ऴ has no byte of its own.** ISCII's `D3` is free; recipe A of section 8.2 would use it. *Decision:* nothing is assigned or mapped into `D3`, and no slot is made for it. Every internal representation keeps the one rule, a character and a nukta: ळ and the nukta, `D2 E9`. Recipe A stays a tested recipe that is not shipped (section 10.4).

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| alone | ऴ (`U+0934`) | asis, nfd | `D2 E9` | `lvrza` | ऴ (`U+0933 U+093C`) |
|  |  | nfc | `D2 E9` | `lvrza` | ऴ (`U+0934`) |
| in a word | कऴन (`U+0915 U+0934 U+0928`) | asis, nfd | `B3 D2 E9 C6` | `kalvrzana` | कऴन (`U+0915 U+0933 U+093C U+0928`) |
|  |  | nfc | `B3 D2 E9 C6` | `kalvrzana` | कऴन (`U+0915 U+0934 U+0928`) |

**C8. Extended clusters: ऱ्ह, ल्ह and the like.** *Decision:* they are managed strictly as code point to code point mappings. The layer makes no assumption about how a font shapes them and takes nothing from the behaviour of an external transliteration; it adds nothing of its own to them, and they are mapped cleanly and deterministically, at the level of the architecture. The fifteen reserved keys of section 11.3 stay untouched; the author is working on them himself.

| Case | In | Form | ACII | Romenagri | Out |
|---|---|---|---|---|---|
| ऱ्ह and ल्ह | ऱ्हल्ह (`U+0931 U+094D U+0939 U+0932 U+094D U+0939`) | asis, nfc | `D0 E8 D8 D1 E8 D8` | `_rr_hal_ha` | ऱ्हल्ह (`U+0931 U+094D U+0939 U+0932 U+094D U+0939`) |
|  |  | nfd | `CF E9 E8 D8 D1 E8 D8` | `rz_hal_ha` | ऱ्हल्ह (`U+0930 U+093C U+094D U+0939 U+0932 U+094D U+0939`) |

### 15.8 What is tested

`tests/test_nukta.py` is the step `nukta` of `tests/run_all.sh`; `--full` raises the number of random streams from 30,000 to 200,000.

| Part | Establishes |
|---|---|
| (a) | the table against Python's `unicodedata`: the eleven rows are exactly the code points of U+0900-U+097F whose NFD is a consonant and U+093C; the `nfc` mark is 1 if and only if NFC composes the pair; `NUKTA_BYTE` is the byte of U+093C; the default form is `asis`; `D3` is not a byte of `unicode.h` |
| (b) | `uni2acii` in the three forms: what each of the eleven letters, and each consonant and nukta, is written as; patch 0001 alone wrote the low byte of the nine |
| (c) | how the form is chosen: the flag, the environment variable, the macro (builds compiled with `-DNUKTA_FORM`, without a warning under `-Wall -Wextra`), `nukta_set_form()` in a program that includes `nukta.h`, which of them wins, the error cases, and the old macro `NUKTA_REBUILD`, which stops the compiler |
| (d) | `acii2uni` in the three forms against a model of the rule, written in Python on top of what the unpatched converter writes for each byte, on random streams and on the exhaustive pairs and triples; `asis` equals the unpatched converter |
| (e) | `uni2acii` in the three forms against a model of the rule, on random streams and on the exhaustive pairs and triples of a set of code units that includes the low-byte characters (é, Æ) |
| (f) | Python's NFC and NFD as independent oracles for both converters, on streams whose marks are in canonical order, with negative controls and the measured limit of section 15.5 |
| (g) | `uni2acii` on the other 65,525 code units of the BMP: unchanged in every form; `D3` is never written |
| (h) | the edge cases of both converters in every form: the held byte at the end of a stream, before a newline and before a consonant; `E9 E9`; a halant or a vowel sign between; the empty input; the usage lines |
| (i) | the warning layer: nothing by default, each code point once under `-w`, `--warn` and `ROMENAGRI_NUKTA_WARN=1`, and the bytes unchanged |
| (j) | the whole chain in every form, on the eleven letters in both spellings and in three contexts, and on the fifteen clusters of section 11.3 (16 strings), with negative controls on patch 0001 alone and on the unpatched build |
| (k) | the cases of section 15.7, each asserted and printed |

The tests remove `ROMENAGRI_NUKTA_FORM` and `ROMENAGRI_NUKTA_WARN` from the environment of every call, so that a setting of the person who runs them cannot change a result. `tests/test_unicode.py`, part (d), classifies the unmapped code points as section 10.4 does and checks that the nine come out of the chain as a consonant and a nukta (and as NFC and NFD write them, with `-f`), and `tests/test_limitations.py` holds the one measurement of section 11.6 that changed (U+0934).

### 15.9 Decided, and left to the reader

Decided on 8 November and closed (section 15.7): the form is a user option and the default is what the converters always wrote (C1, C4); the rule is uniform, a character and a nukta, and is applied before anything is bound (C1, C2, C6); `ऴ` takes no byte of its own, `D3` is not assigned (C7); the clusters get no special cases (C6, C8); a mixed encoding is not repaired, only reported, on request (C5); no decision on a nukta after a halant (C3); the fifteen reserved keys are not touched (C8).

Left to the reader:

1. **The form for a pipeline.** The default is `asis`. A pipeline that compares or stores text in NFC sets `nfc` on both converters (`ROMENAGRI_NUKTA_FORM=nfc` does it for a whole script); one that wants every nukta letter as a pair sets `nfd`. The two converters should be given the same form, or a letter changes spelling on its way through.
2. **Reordering** (section 15.5, item 1): folding a nukta that follows a halant needs a decision between a nukta and ISCII's soft halant, which the converters do not make.
3. **A fourth form,** all eleven letters as single code points, is a table row and a few lines away. Any normaliser would split the eight again.
4. **The converters as functions.** The conversion loops are in the `main` of each program. `nukta_set_form()` and `nukta_options()` give a program that includes `nukta.h` the form and the options; if the loops themselves are to be called as functions, they would have to be moved out of `main`, which this patch does not do.
5. **Folding this patch into patch 0001.** Patch 0003 changes none of the code files that patch 0001 changes, so its code can move into patch 0001 as it is. This document and patch 0002 change with it, and would have to be generated again.

## Appendix A: the complete table

Every row of `acii.h`, in table order: row number, Romenagri key, ACII bytes, Unicode code points, meaning, the spelling in `aciihin.h` ("saral"), and which translator uses the row (section 11.2). Rows added by patch 0001, the Sanskrit characters, are marked **new**. This block is generated.

<!-- BEGIN GENERATED table-all -->

| # | Romenagri | ACII | Unicode | Meaning | saral | used by |
|--:|---|---|---|---|---|---|
| 0 | `` | `EF42` | - | ISCII attribute prefix `EF` + `B` (script = Devanagari); acii2rmn drops it | - | decoder |
| 1 | `__` | `5F` | - | a literal underscore `_` (the escape that keeps `_` free as the family marker) | - | decoder |
| 2 | `_a` | `A4` | U+0905 | letter a | `a` | both |
| 3 | `^a` | `-` | - | the inherent vowel written as a sign: invisible in ACII | - | neither |
| 4 | `_aa` | `A5` | U+0906 | letter aa | `aa` | both |
| 5 | `^aa` | `DA` | U+093E | vowel sign aa | `^aa` | both |
| 6 | `_i` | `A6` | U+0907 | letter i | `i` | both |
| 7 | `^i` | `DB` | U+093F | vowel sign i | `^i` | both |
| 8 | `_ee` | `A7` | U+0908 | letter ii | `i` | both |
| 9 | `^ee` | `DC` | U+0940 | vowel sign ii | `^i` | both |
| 10 | `_u` | `A8` | U+0909 | letter u | `u` | both |
| 11 | `^u` | `DD` | U+0941 | vowel sign u | `^u` | both |
| 12 | `_oo` | `A9` | U+090A | letter uu | `oo` | both |
| 13 | `^oo` | `DE` | U+0942 | vowel sign uu | `^oo` | both |
| 14 | `_ri` | `AA` | U+090B | letter vocalic r | `ri` | both |
| 15 | `^_ri` | `DF` | U+0943 | vowel sign vocalic r | `^ri` | both |
| 16 | `_ae` | `AB` | U+090E | letter short e | - | both |
| 17 | `^ae` | `E0` | U+0946 | vowel sign short e | - | both |
| 18 | `_aee` | `AC` | U+090F | letter e | `e` | both |
| 19 | `^aee` | `E1` | U+0947 | vowel sign e | `^e` | both |
| 20 | `_ai` | `AD` | U+0910 | letter ai | `ai` | both |
| 21 | `^ai` | `E2` | U+0948 | vowel sign ai | `^ai` | both |
| 22 | `_ow` | `AF` | U+0912 | letter short o | - | both |
| 23 | `^ow` | `E4` | U+094A | vowel sign short o | - | both |
| 24 | `_oa` | `B0` | U+0913 | letter o | `o` | both |
| 25 | `^oa` | `E5` | U+094B | vowel sign o | `^o` | both |
| 26 | `_ou` | `B1` | U+0914 | letter au | `ou` | both |
| 27 | `^ou` | `E6` | U+094C | vowel sign au | `^ou` | both |
| 28 | `_au` | `B2` | U+0911 | letter candra o | `o` | both |
| 29 | `^au` | `E7` | U+0949 | vowel sign candra o | `^o` | both |
| 30 | `_ao` | `AE` | U+090D | letter candra e | `ao` | both |
| 31 | `^ao` | `E3` | U+0945 | vowel sign candra e | `^ao` | both |
| 32 | `ka` | `B3` | U+0915 | letter ka | `ka` | both |
| 33 | `kha` | `B4` | U+0916 | letter kha | `kha` | both |
| 34 | `ga` | `B5` | U+0917 | letter ga | `ga` | both |
| 35 | `gha` | `B6` | U+0918 | letter gha | `gha` | both |
| 36 | `_nga` | `B7` | U+0919 | letter nga | `na` | both |
| 37 | `cha` | `B8` | U+091A | letter ca | `cha` | both |
| 38 | `chha` | `B9` | U+091B | letter cha | `chha` | both |
| 39 | `ja` | `BA` | U+091C | letter ja | `ja` | both |
| 40 | `jha` | `BB` | U+091D | letter jha | `jha` | both |
| 41 | `_yna` | `BC` | U+091E | letter nya | `na` | both |
| 42 | `ta` | `BD` | U+091F | letter tta | `ta` | both |
| 43 | `tha` | `BE` | U+0920 | letter ttha | `tha` | both |
| 44 | `da` | `BF` | U+0921 | letter dda | `da` | both |
| 45 | `dha` | `C0` | U+0922 | letter ddha | `dha` | both |
| 46 | `_nna` | `C1` | U+0923 | letter nna | `na` | both |
| 47 | `_ta` | `C2` | U+0924 | letter ta | `ta` | both |
| 48 | `_tha` | `C3` | U+0925 | letter tha | `tha` | both |
| 49 | `_da` | `C4` | U+0926 | letter da | `da` | both |
| 50 | `_dha` | `C5` | U+0927 | letter dha | `dha` | both |
| 51 | `na` | `C6` | U+0928 | letter na | `na` | both |
| 52 | `pa` | `C8` | U+092A | letter pa | `pa` | both |
| 53 | `pha` | `C9` | U+092B | letter pha | `pha` | both |
| 54 | `ba` | `CA` | U+092C | letter ba | `ba` | both |
| 55 | `bha` | `CB` | U+092D | letter bha | `bha` | both |
| 56 | `ma` | `CC` | U+092E | letter ma | `ma` | both |
| 57 | `ya` | `CD` | U+092F | letter ya | `ya` | both |
| 58 | `ra` | `CF` | U+0930 | letter ra | `ra` | both |
| 59 | `_rra` | `D0` | U+0931 | letter rra | - | both |
| 60 | `la` | `D1` | U+0932 | letter la | `la` | both |
| 61 | `wa` | `D4` | U+0935 | letter va | `wa` | both |
| 62 | `lvra` | `D2` | U+0933 | letter lla | `lvra` | both |
| 63 | `sha` | `D5` | U+0936 | letter sha | `sha` | both |
| 64 | `xa` | `D6` | U+0937 | letter ssa | `sha` | both |
| 65 | `sa` | `D7` | U+0938 | letter sa | `sa` | both |
| 66 | `_ha` | `D8` | U+0939 | letter ha | `ha` | both |
| 67 | `_m` | `A2` | U+0902 | sign anusvara | `n` | both |
| 68 | `_hh` | `A3` | U+0903 | sign visarga | `h` | both |
| 69 | `_na` | `A1` | U+0901 | sign candrabindu | `n` | both |
| 70 | `^za` | `E9` | U+093C | sign nukta | - | both |
| 71 | `\|` | `EA` | U+0964 | danda U+0964 | `\|` | both |
| 72 | `^` | `E8` | U+094D | halant U+094D (at the start of a token: the sign `^`) | `^` | both |
| 73 | `_rda` | `BFE9` | U+0921 U+093C | DDA + nukta: the parser's spelling of `_rd` + `a`; acii2rmn builds it in its nukta rule | `rda` | parser |
| 74 | `_rdha` | `C0E9` | U+0922 U+093C | DDHA + nukta: the parser's spelling of `_rd` + `ha`; acii2rmn builds it in its nukta rule | `rdha` | parser |
| 75 | `^ra` | `E8CF` | U+094D U+0930 | halant + RA. Dead: acii2rmn finds the halant row `^` first and the parser reads `^r` as text (section 11.2) | `^ra` | neither |
| 76 | `r` | `CFE8` | U+0930 U+094D | derived: what the parser writes for the letter `r` (RA, then the halant), see `ra` | `r` | neither |
| 77 | `kxa` | `B3E8D6` | U+0915 U+094D U+0937 | derived: what the parser writes for `k` followed by `xa` | `ksha` | neither |
| 78 | `_tra` | `C2E8CF` | U+0924 U+094D U+0930 | derived: what the parser writes for `_t` followed by `ra` | `tra` | neither |
| 79 | `j_yna` | `BAE8BC` | U+091C U+094D U+091E | derived: what the parser writes for `j` followed by `_yna` | `gya` | neither |
| 80 | `shra` | `D5E8CF` | U+0936 U+094D U+0930 | derived: what the parser writes for `sh` followed by `ra` | `shra` | neither |
| 81 | `_jza` | `80` | U+0979 | letter zha | - | both |
| 82 | `_nza` | `C7` | U+0929 | letter nnna | - | both |
| 83 | `_s` | `EB` | U+093D | sign avagraha | - | both |
| 84 | `_li` | `81` | U+090C | letter vocalic l **new** | `lri` | both |
| 85 | `_lee` | `82` | U+0961 | letter vocalic ll **new** | `lri` | both |
| 86 | `_ree` | `83` | U+0960 | letter vocalic rr **new** | `ri` | both |
| 87 | `^_li` | `84` | U+0962 | vowel sign vocalic l **new** | `^lri` | both |
| 88 | `^_lee` | `85` | U+0963 | vowel sign vocalic ll **new** | `^lri` | both |
| 89 | `^_ree` | `86` | U+0944 | vowel sign vocalic rr **new** | `^ri` | both |
| 90 | `_vd` | `87` | U+0965 | double danda **new** | `\|\|` | both |
| 91 | `_vua` | `88` | U+0951 | stress sign udatta **new** | - | both |
| 92 | `_vna` | `89` | U+0952 | stress sign anudatta **new** | - | both |
| 93 | `_vga` | `8A` | U+0953 | grave accent **new** | - | both |
| 94 | `_vca` | `8B` | U+0954 | acute accent **new** | - | both |
| 95 | `_om` | `8C` | U+0950 | om **new** | `om` | both |

<!-- END GENERATED table-all -->

## Appendix B: examples

Devanagari words with their code points, their ACII bytes, their Romenagri spelling, and whether `acii2rmn | rmn2acii` returns the ACII bytes exactly. This block is generated by running the models of the two programs on the real tables.

<!-- BEGIN GENERATED examples -->

| Devanagari | Unicode | ACII | Romenagri | exact round trip |
|---|---|---|---|---|
| राम | 0930 093E 092E | `CFDACC` | `raama` | yes |
| कृष्ण | 0915 0943 0937 094D 0923 | `B3DFD6E8C1` | `k_rix_nna` | yes |
| क्षत्रिय | 0915 094D 0937 0924 094D 0930 093F 092F | `B3E8D6C2E8CFDBCD` | `kxa_triya` | yes |
| ज्ञान | 091C 094D 091E 093E 0928 | `BAE8BCDAC6` | `j_ynaana` | yes |
| श्री | 0936 094D 0930 0940 | `D5E8CFDC` | `shree` | yes |
| ऋग्वेद | 090B 0917 094D 0935 0947 0926 | `AAB5E8D4E1C4` | `_rigwaee_da` | yes |
| कॢप्त | 0915 0962 092A 094D 0924 | `B384C8E8C2` | `k_lip_ta` | yes |
| कॣ | 0915 0963 | `B385` | `k_lee` | yes |
| कॄ | 0915 0944 | `B386` | `k_ree` | yes |
| ऌ | 090C | `81` | `_li` | yes |
| ॡ | 0961 | `82` | `_lee` | yes |
| ॠ | 0960 | `83` | `_ree` | yes |
| ॐ | 0950 | `8C` | `_om` | yes |
| हलोऽन्तराः | 0939 0932 094B 093D 0928 094D 0924 0930 093E 0903 | `D8D1E5EBC6E8C2CFDAA3` | `_haloa_sn_taraa_hh` | yes |
| क़ | 0915 093C | `B3E9` | `kza` | yes |
| ड़ | 0921 093C | `BFE9` | `_rda` | yes |
| ढ़ | 0922 093C | `C0E9` | `_rdha` | yes |
| ऴ | 0933 093C | `D2E9` | `lvrza` | yes |
| अ॒ग्निमी॑ळे | 0905 0952 0917 094D 0928 093F 092E 0940 0951 0933 0947 | `A489B5E8C6DBCCDC88D2E1` | `_a_vnagnimee_vualvraee` | yes |
| क॑ु | 0915 0951 0941 | `B388DD` | `ka_vuu` | yes |
| क॒ि | 0915 0952 093F | `B389DB` | `ka_vni` | yes |
| क़॑ा | 0915 093C 0951 093E | `B3E988DA` | `kza_vuaa` | yes |
| ॥ | 0965 | `87` | `_vd` | yes |

<!-- END GENERATED examples -->
