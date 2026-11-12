<!-- SPDX-License-Identifier: GPL-2.0-or-later -->
# The conversation, point by point: hindawiai/chintamani, the Sanskrit characters in Romenagri, and what followed

Copyright (C) 1993-2026 Abhishek Choudhary. Free software under the GNU General Public License, version 2 or (at your option) any later version: see `COPYING`, `LICENSE` and `NOTICE`.

This is the combined, updated, pointwise narrative of the whole conversation between Abhishek Choudhary ("Abhishek") and Claude, from his first message on 14 October 2026 to the delivery of zip no. 5 on 11 November 2026. On the way: the twelve characters (patch 0001), the underscore guards (patch 0002), the splitting of the long tests into resumable steps, the questions about the fifteen reserved keys, the nukta layer (patch 0003, delivered with zip no. 4 on 8 November 2026 and made again on his decisions of that day), the site that he had another AI model (Grok) build from zip no. 4 and from which Claude was to pick up what could be used (9 November), and the writing of this file, which was first delivered on 3 November 2026. He asked for it on 25 October 2026 at 19:30 IST, in these words: *"Please give me a combined updated pointwise structured narrative of the conversation without dropping any points or facts or threads from the beginning."*

**Contents**

- About this narrative: how it was built, what it rests on, what it could not recover
- 1. The conversation at a glance
- 2. Who is who, and the standing instructions
- 3. The conversation in order (3.1 to 3.11)
- 4. Threads: what each one is, and where it stands
- 5. Facts, in one place
- 6. Defects and quirks found in the code, and what became of each
- 7. Decisions: taken, and still yours
- 8. Mistakes made on the way, and what was done about them
- 9. How the work was run: pauses, resets, limits, restarts
- 10. Open items
- Appendix A. Abhishek's messages, with times
- Appendix B. Session starts
- Appendix C. The five zips
- Appendix D. Where each thing lives in the package

## About this narrative

**How to read it.**

1. Points are numbered inside each section (3.4.7 is point 7 of section 3.4) so that they can be quoted. Section 4 is an index by thread; sections 5 to 10 gather, in one place each, the facts, the defects, the decisions, the mistakes, the operational history and the open items, so that nothing depends on having read the chronology.
2. Times of Abhishek's messages are in IST (Asia/Kolkata, UTC+5:30), which is how his messages were stamped. Times of files and of system events are in UTC and are marked "UTC". Dates of work that Claude did are taken from the timestamps of the files it left.
3. "Section 11.3", "section 14.7" and so on mean sections of `Romenagri/TRANSLITERATION.md`. "Patch 0001" is `patches/0001-add-missing-sanskrit-characters.patch`; "patch 0002" is `patches/0002-apply-underscore-guards.patch`; "patch 0003" is `patches/0003-add-nukta-layer.patch`. "Old", "mid" and "new" are the three builds the tests compare: the unpatched Romenagri; Romenagri with patch 0001 only; Romenagri with all three patches. (Until patch 0003 was added, "new" meant patches 0001 and 0002; sections 3.4 to 3.9 use the word in that sense.)
4. Every point is tagged by the kind of evidence under its heading: **[transcript]** (the raw record of the conversation: when the first version of this file was begun, on 30 October, it reached back to 25 October 14:06 UTC; at the delivery of zip no. 4 it begins at 22:26 UTC on 4 November, and at the delivery of zip no. 5 at 04:59 UTC on 10 November), **[summary]** (one of the eleven session summaries that were written when the conversation ran out of room), **[memory]** (the notes kept about Abhishek), **[files]** (the files that were delivered or left in the work area, with their timestamps) and **[package]** (the package itself).

**What this narrative rests on, and what it could not recover.**

1. The raw transcript of the conversation reached back only to 25 October 2026, 14:06 UTC when this work began on 30 October. The conversation is compacted whenever it runs out of room, and the transcript file is cut at each compaction: the file that exists at delivery, on 3 November, begins at 03:38 UTC on 31 October. At the delivery of zip no. 4, on 8 November, the file begins at 22:26 UTC on 4 November and holds three summaries (written at 22:30 UTC on 4 November, at 02:06 UTC on 6 November and at 22:06 UTC on 6 November); the replies and the work of 3 November and of 4 November before 22:26 UTC are known from those summaries, from the files with their dates and from two scratch probes that were run again (section 3.10). What came before each compaction survives only as a summary, and the facts that the transcript showed on 30 October were taken from it then and checked against the files. At the delivery of zip no. 5, on 11 November, the file begins at 04:59 UTC on 10 November and holds two summaries (written at 05:00 UTC on 10 November and at 01:01 UTC on 11 November); the replies and the work of 8 and 9 November, and of 10 November before 04:59 UTC, are known from the first of them, from the files with their dates and from the package (section 3.11).
2. For 14 to 25 October the narrative is therefore rebuilt from: the eleven summaries that survive (one written on 17 or 18 October, which was recovered from an old dump of the transcript, five written at the compactions of 25, 28, 29 and 31 October and 1 November, three written at the compactions of 4 November (22:30 UTC) and 6 November (02:06 and 22:06 UTC), and two written at the compactions of 10 November (05:00 UTC) and 11 November (01:01 UTC)); the dumps of the transcript of 16 and 17 October that Claude made on 17 October when it had to rebuild the work (transcript lines 560 to 1000 of the file as it then was); the memory file `/areas/hindawi-chintamani.md` and the two other memory files about Abhishek; the three files that were delivered in the first days (the workbook, `sandhi.js`, `sandhi.uhin`); the three earlier zips (20 October, 25 October and 3 November); the old results and scratch files in the work area (among them the two probes of 4 November); and the report of the independent check of 24 and 25 October.
3. What is **not** retained: the exact words of Abhishek's three messages of 14 October (only their substance, as the notes and the summaries give it); the text of Claude's replies of 15 and 16 October (only what the three delivered files contain); the text of Claude's replies of 3 and 4 November (only their substance, from the summaries and from two probes that were run again); the exact times of some of the short "continue" messages between 17 and 25 October. The text of Claude's replies of 8 and 9 November, and of 10 November before 04:59 UTC, is not retained either (section 3.11 gives its substance). Where a point is an inference and not a record, it says so.
4. Nothing was left out on purpose. If a point is missing it was not recoverable, and the narrative says where the gap is (the places are listed in section 10, item 12).

## 1. The conversation at a glance

**[summary] [memory] [files] [package]**

| Phase | When | What it was | What came out of it |
|---|---|---|---|
| 3.1 | 14 Oct, 23:17-23:32 IST | Abhishek's three messages: background on ACII and ISCII, the path he recommends to anyone building Paninian generators on his repository, and "simply copy pasting my above two messages should work" | the task; notes in memory |
| 3.2 | 15 Oct | the repository fetched, surveyed, built; the four converters checked; Shaili Vyakaran studied; the Ashtadhyayi sutras that vidyut-prakriya does not cover found | `vidyut_prakriya_sutra_coverage.xlsx` |
| 3.3 | 15-16 Oct | "How would you build the sutras using Hindawi": how `hincc` treats Sanskrit and Hindi source; one sutra (6.1.77) written in a Hindawi language style and run | `sandhi.js`, `sandhi.uhin`, the write-up |
| 3.4 | 16 Oct, 04:38 IST, to 17 Oct | the request to add the missing Sanskrit characters to Hindawi without changing its architecture, and to write the transliteration algorithm down formally | twelve characters added; parser branches; first tests and results |
| 3.5 | 17 Oct, 07:36 IST | deliver as a zip with licence files; copyright 1993-2026 Abhishek Choudhary; the name rule; update memory | standing instructions |
| 3.6 | 17 Oct, 23:43 IST (18:13 UTC), to 20 Oct | the work area was reset; the work was recovered from the transcript and rebuilt; the formal document written; packaged | zip no. 1, 20 October |
| 3.7 | 20 Oct, 07:43 IST | "explain all the remaining 15 character bugs": he will try to solve them himself | section 11.3; `tools/reserved_keys.py` |
| 3.8 | 20 Oct, 17:22 IST, to 25 Oct | three research questions about the underscore; an independent check; corrections | section 14; tests U1-U9; lint T8; zip no. 2, 25 October |
| 3.9 | 25 Oct, 19:30 IST, to 3 Nov | "Apply the guard rules", this narrative, and the split of the long tests | patch 0002; the guards in `rmn2acii.c`; this file; the tests in resumable steps; zip no. 3 |
| 3.10 | 3 Nov, 16:22 IST, to 8 Nov | the fifteen rows asked about once more (exact details; Devanagari; pronunciation by region); "try passing Devnagri through"; the cluster ड़्व that failed; "add a layer that decomposes the underlying nukta layer, and builds it back", with the technical challenges to be shown in Devanagari | the answers on the fifteen rows; the finding about U+095C; patch 0003 (`nukta.h`, `uni2acii.c`, `acii2uni.c`, `Makefile`); section 15 of the document; the test `nukta`; zip no. 4 |
| 3.11 | 8 Nov, 11:42 IST, to 11 Nov | his decisions on the eight cases C1 to C8; the nukta layer made again on them; "I got grok to build some docs, html and notebooks based on the v4 zip" and "Please pick up what you can use" | the form (`asis`, `nfc`, `nfd`), the rule and the warning layer; patch 0003 and section 15 made again; the test `nukta` with 175 checks; the folder `romenagri-site/` (five pages, a notebook, a JavaScript port checked against the C programs); zip no. 5 |

Between and inside the phases there are many short messages of the kind "Continue from where you got paused", sent after the work had been stopped by a usage limit, by a reset of the work area, or by the end of the room in the conversation (section 9 and Appendix A).

## 2. Who is who, and the standing instructions

### 2.1 The people and the project

**[memory] [summary]**

1. The user is **Abhishek Choudhary** (AyeAI). He says it is a very common name, and gave "Abhishek Choudhary AyeAI IBM Hindawi" as the keywords that pin down which one. His first name is Abhishek and his surname Choudhary, written first name then surname. His speech interface can fuse the two into "ABHISHEKCHOUDHARY"; that spelling is never to be used.
2. **hindawiai/chintamani** is his own repository on GitHub. It holds the Romenagri tools (`uni2acii`, `acii2uni`, `acii2rmn`, `rmn2acii`), the Hindawi language styles ("shailis"), and Shaili Vyakaran (the grammar of the shailis). The work of this conversation is on the `Romenagri/` directory at commit `3ad87785a75dc2b18438a8b068807103cb920c81`.
3. His other work, named in the notes about him, is the Zistgah / Project ILM estate, the obonac/provenance pipeline and his other repositories; none of it is part of this conversation.
4. Claude ran in a private Linux workspace in the cloud, with a shell, file tools, a search tool and a way to send files. The session is configured for the model `claude-sonnet-5-5`; the model that served a particular turn may have been another one, and the record does not say. The workspace is not his computer; nothing on his computer was reached.
5. The repository was cloned read-only into the workspace. All work was done on copies in the scratchpad, and the clone was checked after each series of runs: it is unmodified at commit `3ad87785a75dc2b18438a8b068807103cb920c81` (`git status` clean; checked again at the end of the work, on 3 November and on 7, 8 and 11 November). This was Claude's own working rule; Abhishek did not ask for it.

### 2.2 What Abhishek said about his own work (14 October)

**[memory] [summary]** The wording is the memory's, which records what he stated; his own words of 14 October are not retained.

1. **ACII** is a slightly modified ISCII with additional characters added. Unicode cannot do the mapping between Brahmi-derived scripts that ISCII allowed, though its Extended Devanagari coverage is much better.
2. He is **not putting the tools online with AI connected**: there is no real business case, and the money cannot be recovered.
3. He is building support for running **his version of the Panini programming language on the web**. That work is **paused**, because it is pure application domain and does not advance the core work.
4. The path he suggests to people who want to build **Paninian generators or analysers**: free Claude plus the chintamani repository; read the Romenagri tools and the Hindawi shailis and study Shaili Vyakaran; **focus on generators**, because analysers are algorithmically complex; **find the sutras that vidyut-prakriya does not cover**; target **JavaScript first** and convert to Hindawi later; host on **GitHub Pages** (jsPython can run Python in a browser).
5. He **wants an issue raised on his consolidation page** when a new sutra implementation works (saying where it was placed) or when results go wrong. This is a standing wish; no sutra implementation has been placed anywhere, and no issue has been raised (section 10, item 10).

### 2.3 The instructions, in the order they were given

**[summary] [memory] [transcript]**

| # | Date | Instruction | How it was followed |
|---|---|---|---|
| I1 | 14 Oct | "Simply copy pasting my above two messages should work": the two pasted messages are the brief | they were carried out as the plan of sections 3.2 and 3.3 |
| I2 | 15 Oct, 05:41 | "You got paused as limits ran out. Continue. Don't redo work already done." | after every pause the work resumed from the last result and nothing already done was repeated, except where a reset of the work area made it unavoidable (section 3.6) |
| I3 | 16 Oct, 04:38 | add the missing Sanskrit characters **without changing Hindawi's architecture**; the byte from the unused part of the 8-bit page; the string in `acii.h` by the rules of the existing strings, which "work with the recursive descent parser"; work out the algorithm, write it down formally; analyse the formal definition of Hindawi's transliteration so that it can be extended to larger character sets, character-set conflicts and missing sounds; **document it**; "First, try and complete this" | section 3.4; the architecture is unchanged (five states, decision lists, recursion) |
| I4 | 17 Oct, 07:36 | from now on **produce a zip file with all the necessary licences**; copyright **1993 to 2026, Abhishek Choudhary**; first name, then surname; "Update your memory" | every delivery since is a zip (Appendix C); memory updated the same day |
| I5 | 20 Oct, 07:43 | "Please explain all the remaining 15 character bugs. I'll also read through, but explain those. I'll try to manually solve them. Otherwise, I'll pass it off to you later." | explained, **not fixed**; the 15 missing rows are still missing, on purpose (section 3.7) |
| I6 | 20 Oct, 17:22 | "Continue continue from where you were paused and also solve these", with three pasted research questions | section 3.8 |
| I7 | 25 Oct, 19:30 | "Apply the guard rules" | section 3.9 |
| I8 | 25 Oct, 19:30 | "Please give me a combined updated pointwise structured narrative of the conversation without dropping any points or facts or threads from the beginning" | this file |
| I9 | 1 Nov, 11:10 | "Continue... Split the long running tests!!!! Those are not completing within work window and then you're repeating" | the long tests were split into twenty steps with markers, `--resume` and `--only`, and run in pieces (section 3.9, item 14) |
| I10 | 3 Nov, 16:22 | "which 15 rows are still not fixed. Give me the exact details. You've taken, I don't know how many dozens of turns" | the fifteen were listed with their exact details (section 3.10, item 2) |
| I11 | 3 Nov, 16:26 | "right? Give those characters with their Devanagari characters and the common pronunciation in Eastern India, in Northern India, in Central India, and in Southern India. Remember, these pronunciations vary by region." | the fifteen with their Devanagari and the pronunciation by region (section 3.10, item 3) |
| I12 | 4 Nov, 12:08 | "Except for 13 and 15... All are covered by even the oldest Romenagri behenchod", and "Try passing Devnagri through" | the fifteen clusters were passed through the whole chain on the three builds of zip no. 3 (section 3.10, item 4) |
| I13 | 4 Nov, 12:27 | "This should work ड़्व", "Let me check manually", "But now I am lead to doubt your three weeks of work as a waste of my time", "Reviewing everything you did..." | the failure was reproduced and explained (section 3.10, item 5); the layer of I14 repairs it |
| I14 | 4 Nov, 19:50 | "Add in the patch... Just add a layer that decomposes the underlying nukta layer, and builds it back", and "Are there any technical challenges? If you identify any please show those in Devnagri for me to review" | patch 0003, section 15 of the document, and the challenges C1 to C8 in Devanagari (section 3.10, items 6 to 10) |
| I15 | 8 Nov, 11:42 | the decisions on the eight cases C1 to C8, quoted in full in section 3.11, item 2: the output form NFC or NFD is a user option at every level, the default aligned with the existing behaviour; a nukta letter is a consonant and a nukta inside, decomposed at Level 1; Unicode a layer of its own; a warning layer for the é collision, off by default; no special cases for clusters; nothing into `D3`; no decision on C2 and C3; extended clusters as code point to code point mappings | the nukta layer made again (section 3.11, items 3 to 8) |
| I16 | 9 Nov, 10:02 | a site that Grok built from the v4 zip ("It claims to have fixed the remaining nukta issues"); "Please pick up what you can use" | the site was examined as data, what could be used was taken, and `romenagri-site/` was built again from the headers and the programs (section 3.11, items 9 to 15) |

Other standing rules that applied, and where they came from:

1. **Memory.** The file about the repository holds nine lines: seven written between 14 and 17 October (the facts of section 2.2, and the request of 16 October for the Sanskrit characters; the exact dates of the first six are not recorded) and two written on 25 October (that he plans to fix the 15 keys himself, and that he asked the three underscore questions). On 17 October two more files were written: the name rule (in his profile) and the packaging and copyright preference (in his preferences). Six lines were added after that: two on 31 October (15:45 UTC; that he asked for the guards to be applied, and for this narrative) and one on 3 November (that he asked on 1 November for the long tests to be split) and one on 7 November (that he asked on 4 November for the nukta layer, and for the technical challenges to be shown in Devanagari), and two on 10 November (19:13 UTC: his decisions of 8 November on the nukta layer, and that he had Grok build a site from zip no. 4 and asked Claude to pick up what is usable); the file now holds fifteen lines.
2. **Git attribution** (a notice from the working environment, not from Abhishek): commits end with "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" and a "Claude-Session:" line; pull request bodies end with the "Generated with Claude Code" line and the session link. **No commit or pull request was made**, in this repository or any other.
3. **His email address** was supplied by the environment for identification only and has not been used for anything.
4. **A permission rule** (also from the environment) forbids a number of card-style display tools; it did not affect the work.

## 3. The conversation in order

### 3.1 14 October (23:17 to 23:32 IST): the three messages

**Evidence: [memory] [summary].** The exact words are not retained; the substance is.

1. Abhishek sent three messages within fifteen minutes, in the style of chat messages, pasted from a conversation with a collaborator of his own (the summaries call them "WhatsApp-style").
2. **The first message** explained ACII and ISCII: ACII is a slightly modified ISCII with extra characters added, and Unicode cannot do the mapping between Brahmi-derived scripts that ISCII allowed, although its Extended Devanagari coverage is much better (section 2.2, items 1 and 2).
3. **The second message** gave the path he recommends to people who want to build Paninian generators on his repository (section 2.2, item 4): use free Claude (Sonnet) with the chintamani repository; understand Romenagri and the Hindawi shailis; study Shaili Vyakaran; build **generators** first, because analysers are algorithmically complex; find the Ashtadhyayi sutras that **vidyut-prakriya** (the Rust generator in the `ambuda-org/vidyut` project) has not covered; write **JavaScript** first and convert to Hindawi later; host on **GitHub Pages**; and raise an issue on his consolidation page when a new sutra implementation works (saying where it was placed) or when results go wrong.
4. In the same messages he said that he is not putting the tools online with AI connected, because there is no business case and the money could not be recovered, and that his own work on running his version of the Panini programming language on the web is paused, because it is pure application domain and does not advance the core work.
5. **The third message** was *"Simply copy pasting my above two messages should work."* It means that the two pasted messages are the brief. The work of sections 3.2 and 3.3 is what they asked for: the task list that was made at that point is the plan of the two messages (build the repository and study it; check the four converters; study Shaili Vyakaran; find the uncovered sutras; check what `hincc` does with Sanskrit and Hindi; prove one sutra in Hindawi; write up the approach).
6. The notes in section 2.2 were written down from these messages, so that they would be there in later conversations.

### 3.2 15 October: the survey, the build and the gap analysis

**Evidence: [summary] [files] [memory].** The task list of the session (its first six tasks) names the steps; the workbook is a surviving file.

1. The first work stopped when the usage limit ran out. At 05:41 IST Abhishek wrote *"You got paused as limits ran out. Continue. Don't redo work already done"* (instruction I2), and at 11:27 IST *"Continue from where you got paused"*.
2. **The repository was fetched.** `hindawiai/chintamani` is a repository of the following top-level parts: `Romenagri/` (the transliteration system: 62 files at that commit), `Hindawi/` (the language styles, in the directories `guru`, `hindrv`, `kritrima`, `kxaaraka`, `others`, `praatha`, `samples`, `shabda`, `shraeni`, `soochee`, `wyaaka`, `yantra`), `HindawiLauncher`, `HindawiUI`, `RomenagriMail`, `RomenagriUI`, `APCISR`, `Notebooks`, `corpora`, and the scripts `install`, `clean`, `uninstall`, `preinstall_ubuntu.sh`, `preinstall_fedora.sh`. The head of the repository is commit `3ad87785a75dc2b18438a8b068807103cb920c81` of 13 June 2026 ("Refocus HindiC++ spec on language semantics"). Every later statement about "the repository" is about this commit.
3. **Task: map the layout and understand every tool** in `Romenagri/` and the Hindawi shailis (task 1).
4. **Task: build everything** and record what fails and how it was fixed (task 2). The package manager of the workspace was blocked, so `flex` (which the lexers need) had to be built from the official release; this had to be done again after the reset of 17 October (section 3.6).
5. **Task: check that the four converters work** (`acii2rmn`, `rmn2acii`, `uni2acii`, `acii2uni`) on sample text, with round trips (task 3).
6. **Task: study Shaili Wyaakaran** ("Wyaakaran" is the repository's own spelling of vyakaran, grammar) and summarise how the grammar of the shailis is specified (task 4). The summary itself is not retained.
7. **Task: find which Ashtadhyayi sutras vidyut-prakriya does not cover** (task 5). The result is the workbook **`vidyut_prakriya_sutra_coverage.xlsx`**, which was sent to Abhishek. It has four sheets: *Summary* (every count is a live formula over the sheet *All sutras*), *Not covered* (the list of sutras to work on), *All sutras* (3,983 rows) and *Method*. The headline figures, from the workbook itself:
   - 3,983 sutras in all; **2,168 covered (54.4 %) and 1,815 not covered (45.6 %)**, as decided from the Rust source of `vidyut-prakriya`, commit `8da2f90` of 24 June 2026, and the test files, analysed on 15 October 2026. The sutra text, type and anuvṛtti columns come from the `ashtadhyayi.com` data.
   - The full table of statuses, types and chapters is in section 5.9.
   - The project's own script `scripts/check_rule_coverage.py` reports 2,289 sutras as covered. The workbook explains the difference of 121: the script also counts the 110 sutras that appear only in the generated word-list tables, 10 skip markers, 2 empty test stubs, 2 sutras for which only vārttikas are cited and 1 commented-out call, and does not count 4 sutras (5.3.48 to 5.3.51) that a ranged test covers.
   - The method is stated on the *Method* sheet, with its limits (it is static and literal: a sutra applied implicitly shows as not covered; "covered" does not mean complete; many adhikāra, saṃjñā and paribhāṣā sutras are structural; the type labels are those of ashtadhyayi.com). An independent grep-based spot check of 37 randomly chosen sutras across all eight statuses agreed with every label.
8. **Task: check the results and write up** (task 6): the build claims and the coverage numbers were re-verified before the summary was given.
9. This is the first of Abhishek's wishes (section 2.2, item 4): "find sutras vidyut-prakriya doesn't cover". Nothing was implemented from the list; the workbook is the input for that.

### 3.3 15 and 16 October: "How would you build the sutras using Hindawi?"

**Evidence: [summary] [files].** Abhishek's question came at 11:45 IST on 15 October. The text of Claude's answer is not retained; the two files that went with it are, and the task list names the steps.

1. **Task: check how `hincc` handles Sanskrit text and Hindi source** (task 7): the driver `hincc.awk`, the filters of a shaili and the samples were read, and a test was made of whether **Sanskrit string literals, including ऽ ऌ ॐ, survive a `hincc` compile**.
2. **Task: prove one sutra end to end in a Hindawi shaili** (task 8): **6.1.77 iko yaṇaci** (ik is replaced by the corresponding yaṇ before a vowel) was written in Hindi-keyword code with the data in SLP1, compiled with `hincc` and run. Two files were sent:
   - **`sandhi.js`**: the JavaScript reference. It computes the pratyāhāras from the Śiva-sūtras (1.1.71 ādirantyena sahetā), extends them by savarṇa (1.1.69 aṇudit savarṇasya cāpratyayaḥ, with 1.1.9 and the ṛ/ḷ vārttika), chooses the replacement by the nearest place of articulation (1.1.50 sthāne'ntaratamaḥ, by a score), and applies 6.1.77 (with 6.1.72 saṃhitāyām as the assumption that the two members are joined). It prints the sets (`IK=iIuUfFxX AC=aAiIuUfFxXeoEO YAN=yvrl`) and runs seven cases: sudhī + upāsyaḥ → sudhyupāsyaḥ, madhu + atra → madhvatra, dadhi + atra → dadhyatra, kartṛ + arthaḥ → kartrarthaḥ, ḷ + ākṛtiḥ → lākṛtiḥ, and two cases in which the rule does not apply (rāma + atra, dadhi + kam). Run again on 30 October with Node 22: **"all 7 cases ok"**.
   - **`sandhi.uhin`**: the same program in Hindawi's Hindi shaili (its first line is `<शैली कृत्रिम>`, the "kritrima" shaili, which is Java-like with Hindi keywords: `अणु … पूर्ण` for the braces, `क्रम` for `for`, `अगर` for `if`, `वापस` for `return`, `माला_श्रेणी` for `String`). The data stay in SLP1, which is plain ASCII; the Devanagari output is made by tables that are written **only as `\uXXXX` escapes**, and the comment says why: so that the ACII layer cannot spoil anything.
3. The shape of the approach that the two files show is the one Abhishek recommended: **a JavaScript reference first, then the same program in Hindawi**; the rules are functions, one per sutra, with their sutra numbers in comments; the data are SLP1 strings; a table of test cases carries the expected results.
4. **Findings about Hindawi** that came out of the work of 15 to 17 October. They are recorded in the summary of 17 October; whether each one came up in the sutra proof or in the later end-to-end tests of section 3.4 is not recorded.
   - Hindawi's keyword replacement also works **inside identifiers** (for example सम्पूर्ण made a program fail to compile). A catch-all identifier rule in a scratch copy of `h2j.uhin` fixed it; this was reported to Abhishek as a finding about the repository. The repository itself was not changed.
   - `hincc` needs **GNU awk** (`gawk`); the workspace had only `mawk`, so `gawk` was made a link to `mawk` (this is recorded in `results/environment.txt` and has to be done again in a new workspace).
   - The **Java shaili (kritrima) works**; the **Python shaili does not work** on the master branch.
5. **The step that led to the next request** (an inference; the conversation of that moment is not retained): the test of ऽ ऌ ॐ in step 1 and the comment in `sandhi.uhin` show that Sanskrit-specific characters did not reliably pass the ACII layer, and about 17 hours after Abhishek's question about Hindawi he asked for the missing Sanskrit characters to be added (section 3.4).
6. At 23:12 IST on 15 October he wrote *"Continue"*, and at 04:25 IST on 16 October *"Continue from where you got paused"*.

### 3.4 16 October (04:38 IST) to 17 October: the request for the missing Sanskrit characters

**Evidence: [summary] [transcript dumps of lines 560-1000] [files] [package].** The request is quoted from the summary of 17 October, which carries it word for word.

1. **The request** (Friday 16 October, 04:38 IST):

   > "Can you add the missing Sanskrit characters to Hindawi without changing its architecture? This is how you have to do it. In the Unicode to ACII mapping, you will have to find in the 8-bit ASCII page something that is not already used in ACII. So ACII already uses a few characters more than ISCII. Okay, and then you have to take it to the ACII.h, if the name is correct, if I remember it correct. In that, you will have to mention, like other characters, you will have to enter the transliteration string for it. But this transliteration string should follow the same rules that the existing transliteration scheme strings have. It's not a trivially written transliteration string. It works with the recursive descent parser. So you will have to kind of work out the entire algorithm, how it is done, write it down formally, and then figure it out. While you are doing this, also try and analyze the actual formal definition of how Hindavi's transliteration works, so that we can also extend it to larger character sets, handle character set conflicts, missing sounds, etc. But document it. First, try and complete this."

2. **What it asks, taken apart** (this is how it was read):
   1. add the Sanskrit characters that Hindawi lacks;
   2. do not change the architecture;
   3. take an unused byte of the 8-bit page for each, in the Unicode-to-ACII mapping (`unicode.h`), knowing that ACII already uses a few bytes more than ISCII;
   4. give each a transliteration string in `acii.h`, by the same rules as the existing strings, which are tied to the recursive-descent parser;
   5. work out the algorithm of that parser and write it down formally;
   6. analyse the formal definition of Hindawi's transliteration so that it can be extended to larger character sets, to conflicts between character sets and to missing sounds;
   7. document it;
   8. **first complete the characters**: the document comes after, or alongside.
3. **The plan** was the task list items 10 to 15: map the Romenagri code (the tables, the parser, the decoder, the lexers, the Makefile); inventory the byte usage and choose free slots; write the grammar down formally; add the characters; test them and check that nothing regressed; document and package.
4. **What the code turned out to be** (it matters for the reading of "without changing the architecture"):
   1. Three layers: Unicode (UTF-16LE) to ACII (8 bits; ISCII-91 plus extras) to Romenagri (7-bit ASCII), with the programs `uni2acii` / `acii2uni` between the first two and `acii2rmn` / `rmn2acii` (and `acii2cf`, `acii2pcf`, `acii2hin`) between the last two (section 2).
   2. Three tables: `unicode.h` (`{low, high, byte}` rows), `acii.h` (`{key, bytes}` rows; row 0 is a control row) and `aciihin.h` (the lossy "saral" rendering).
   3. The Unicode side and the decoder `acii2rmn` are table-driven. **The reverse parser `rmn2acii.c` is not**: it is a hand-written recursive-descent parser of five functions that builds keys and looks them up. A new key needs a parser branch unless the parser already reads it as one token. So "tables only" is **not strictly possible**; branches in the same style, with no new mechanism, are. This was told to Abhishek in the document and in the delivery.
   4. The architecture that stays unchanged: three ordered first-match tables, five parser states (L1, L2a, L2b, L2c, M), decision lists, calls that are the last thing their branch does, lookahead of a few characters, no new function except one small helper.
5. **The byte allocation.** Before the patch `unicode.h` had 73 rows (85 after). ACII's first extension, ZHA U+0979 at byte `80`, had already used the C1 block (`80` to `9F`), which ISCII-91 leaves unassigned and ASCII does not reach. The twelve characters continue that block at `81` to `8C`, in a fixed order: three vowels, three signs, double danda, four accents, OM (section 7.2).
   - In the first implementation OM was at `A0`, its own ISCII code (so the first summary says "`81`-`8B` and `A0`"). During the rebuild of 17 to 20 October a test (part (e) of `tests/test_unicode.py`, which keeps everyday characters off the new bytes) showed that this is wrong: `uni2acii` writes every character it has no row for as its **low byte**, and the low byte of U+00A0 NO-BREAK SPACE is `A0`, so every no-break space would have come back as ॐ. OM moved to `8C` and `A0` stays unused (decision 1 of section 7).
6. **The twelve characters** (section 7.1):

   | Character | Unicode | ACII | Romenagri | saral |
   |---|---|---|---|---|
   | ऌ vocalic L | U+090C | `81` | `_li` | `lri` |
   | ॡ vocalic LL | U+0961 | `82` | `_lee` | `lri` |
   | ॠ vocalic RR | U+0960 | `83` | `_ree` | `ri` |
   | ◌ॢ sign vocalic L | U+0962 | `84` | `^_li` | `^lri` |
   | ◌ॣ sign vocalic LL | U+0963 | `85` | `^_lee` | `^lri` |
   | ◌ॄ sign vocalic RR | U+0944 | `86` | `^_ree` | `^ri` |
   | ॥ double danda | U+0965 | `87` | `_vd` | `\|\|` |
   | ◌॑ udatta | U+0951 | `88` | `_vua` | (nothing) |
   | ◌॒ anudatta | U+0952 | `89` | `_vna` | (nothing) |
   | ◌॓ grave accent | U+0953 | `8A` | `_vga` | (nothing) |
   | ◌॔ acute accent | U+0954 | `8B` | `_vca` | (nothing) |
   | ॐ OM | U+0950 | `8C` | `_om` | `om` |

7. **The strings** follow nine conventions that were read off the existing table and that the parser's rules impose (R1 to R9, section 6): keys use `a`-`z` and `_`; a consonant key is its stem plus `a`; the plain letter is the primary reading and the `_` form is for the second sound of a letter; `h` is reserved for aspiration, so the letter ha is `_ha`; an independent vowel is `_` and its spelling and its sign `^` and the spelling; a mark that attaches ends in `a`, like the nukta; the letter after `_` selects a family (the new families are `_l` for the vocalic L vowels and `_v` for verse and Vedic signs); and a new key must be read as one token by the rules that exist, or the rules must change in the same commit.
   - The accent strings were first written without the final `a` (`_vu…`). The order test (an accent before and after a vowel sign) failed; they were changed to the nukta-like form `_vua`, `_vna`, `_vga`, `_vca`, with the explicit `a`, which the decoder's rule "a following sign pops the `a`" and the parser's state L2a both need.
   - The double danda cannot be `||`: the lexers never hand `|` to the parser (section 11.1).
8. **The avagraha was repaired on the way.** Byte `EB` was written `_3` by the decoder, a string that cannot come back: digits never reach the parser, so `EB` went through `acii2rmn | rmn2acii` as `E8 33`. The parser's own branch for it asks for a row `_s` that did not exist, and `rmn2acii` crashed on `_s`. The row was renamed `_s`; the byte did not change, so existing ACII files are unaffected (section 7.1).
9. **`acii2hin.c` had a literal `75`** as the loop bound over the saral table. It now ends at `ACII_HIN_LEN`; without that the new rows would never have been read.
10. **The parser changes** (patch 0001): a helper `vocalic()` that replaces the halant just written by the sign form, as the code for `_ri` always did inline; twelve new rules, nine in the state for keys after `_` (`_om`, `_ree`, `_li`, `_lee`, `_vd` and the four accents `_vu…`, `_vn…`, `_vg…`, `_vc…`) and three in state M for the explicit signs `^_li`, `^_lee`, `^_ree`. They are the rules tagged `+` in the grammar of section 5.3.
11. **How the work was tested** (this is the methodology that every later phase reused):
    1. an **executable Python model** of the parser (and later of the decoder and the filter pair), compared with the real C code through a small harness (`tests/harness.c`), on every short string and on random long ones;
    2. an **equivariance test**: each new byte must behave like its analogue in the old repertoire (vocalic vowel like RI, vocalic sign like the RI sign, the others like the anusvara); relaxed afterwards to "an exact analogue implies an exact result", because the two differ only on invalid sequences;
    3. a generator of **well-formed texts** for the round-trip contract (section 9);
    4. a **table lint** of invariants (T1 to T7 at that time);
    5. **Unicode** tests (every new code point converts both ways; every old row converts as before; everyday characters stay off the new bytes);
    6. the repository's **Hindi corpus** through the whole chain, old against new;
    7. an **end-to-end test** through Hindawi's `hincc`: a Hindi C program and a Hindi Java program with the new characters in identifiers, strings and comments (the Rigveda verse 1.1.1a with its accents, vocalic signs after consonants, Sanskrit with ॐ ऽ ॥, the accent-before-sign order, and identifiers `ॐ` and `ऌ`), compiled, run, and compared with the Devanagari that was written.
12. **What the first runs said** (messages sent to Abhishek on 16 and 17 October, all from the dump of the transcript):
    - "All 12 new characters now round-trip Unicode → ACII → Unicode, and their romanisations come back to the right byte. Avagraha now round-trips too."
    - "The parser test passed: my written grammar matches the real C parser on about 830k strings with zero disagreements, and nothing changed except the new tokens."
    - "The regression run finished with no regressions: nothing that round-tripped before is broken now. Avagraha-containing sequences are repaired, about 10,500 of them." The few places where old and new outputs differ were then examined, among them why a new vowel sign directly after a vowel or a sign does not behave like ृ.
    - "Parser and round-trip tests are clean on the rebuilt tools, and I made the Vedic accents robust to either order of accent and vowel sign." The end-to-end run followed: **C 6 of 6 lines and Java 6 of 6 lines identical to the Devanagari source with the new tools; the old tools fail** (the old build cannot write the new characters).
    - Round trips of random well-formed texts over the new repertoire: the old build returned 84 % of them exactly, the new build 100 %.
    - Later in the day: "the code, the tests and the patch are done. I'm now writing TRANSLITERATION.md".
13. **Two Hindawi findings belong here** (they came out of the end-to-end tests; section 3.3, item 4): the keyword replacement inside identifiers, and the C shaili's handling of `\u` escapes in strings.
14. Abhishek's short messages in this phase: 12:59 IST on 16 October *"You got paused."*; 18:37 IST *"Please continue from where you got paused."*; 23:49 IST *"Continue"*.

### 3.5 17 October (07:36 IST): zip, licences, copyright and the name

**Evidence: [transcript dump, line 602] [memory] [package].**

1. **The message**, in full:

   > "Anyway, from now on, start producing a zip file with all the necessary license and all. It will be copyright 1993 to 2026. ABHISHEKCHOUDHARY. Yes, your speech interface took my name without a space. So my surname is CHOUDHARY. And my first name is ABHISHEK. And we write first name, then surname. Okay? Update your memory. Continue, complete it."

2. **What it means** (instruction I4): every finished piece of work is delivered as a zip file that contains all the licence files it needs; the copyright is 1993 to 2026; the holder is written Abhishek Choudhary (first name, then surname; the fused capitals are a speech-recognition artefact); the memory is to be updated; and the work in hand is to be completed.
3. **Memory** was read and written at once: the name rule went into his profile and the packaging and copyright preference into his preferences, on 17 October at 02:07 UTC (07:37 IST).
4. **The licensing facts the package rests on** (section 12.3, `NOTICE`):
   1. The repository is free software under the **GNU General Public License, version 2 or (at your option) any later version**; `Romenagri/copying` is the GPL version 2 text and the package carries it as `COPYING`; `LICENSE` is the short statement.
   2. The **`corp_*` files** of `Romenagri/` are derived from Wikipedia and are, as `Romenagri/LEGAL` says, "usually" under **CC BY-SA 3.0**; they are not covered by the GPL, the package includes them unchanged and says so in `NOTICE`.
   3. The five files that patch 0001 changes (`acii.h`, `unicode.h`, `aciihin.h`, `acii2hin.c`, `rmn2acii.c`) and every new file carry `Copyright (C) 1993-2026 Abhishek Choudhary`; the new files also carry `SPDX-License-Identifier: GPL-2.0-or-later`.
   4. The other **57 files** of `Romenagri/` keep the notices they have (mostly "2003-2006"); changing those is a mechanical edit if he wants it. This was offered as a decision (section 7, item 5).
   5. Each changed file has an entry in its own **Modifications** log naming the alias `<obonac>` and the address a.choudhary@ieee.org, with the words "(prepared with Claude)", which can be deleted (section 7, item 6). `rmn2acii.c` now has two entries: 19 October 2026 (patch 0001) and 26 October 2026 (patch 0002).
5. **What the zip contains** from the first delivery on: `README.md`, `NOTICE`, `LICENSE`, `COPYING`, `SHA256SUMS`, the patched `Romenagri/` directory, the patches, the tools, the tests, the results and the environment of the recorded runs (Appendix C and D).
6. At 08:18 IST (*"Please continue from where you got paused."*) and 13:30 IST (*"Anyway."*) he sent two more short messages, and at 15:52 IST *"Please from where you got paused."*.

### 3.6 17 October (23:43 IST) to 20 October: the reset, the recovery, the formal document, the first zip

**Evidence: [summary] [transcript dumps of lines 560-1000] [files] [package].** The messages of Abhishek are from the summaries; the times of the work are the timestamps of the files that it left (UTC, converted to IST where the point is about him). The text of Claude's replies of these days is not retained.

1. **The message.** At 23:43 IST on 17 October (18:13 UTC) Abhishek wrote *"Please from where you got paused."* By then the workspace had been **reset**: the clone of the repository, the builds, the `flex` that had been built from the release, the patched files, the tests and the scratch work were gone. Three files were attached to the conversation again: the workbook, `sandhi.js` and `sandhi.uhin`. They are Claude's own deliverables of 15 and 16 October, put back by the system; they are not new uploads from Abhishek, and were recognised as such.
2. **Short messages around it.** Earlier on 17 October he had sent *"Please continue from where you got paused."* at 08:18 IST, *"Anyway."* at 13:30, *"Please from where you got paused."* at 15:52 and *"Please continue from where you got paused."* at 18:45. After a usage-limit notice that said the limit "resets 11:10pm (UTC)" he wrote *"Continue from where you left off."* (the time is not retained). Between 17 and 24 October there are more of the same kind, with the wordings *"Continue from where you got paused"* and *"Continue from where you got dropped off."* (Appendix A).
3. **What survived and what did not.**
   1. Gone: the clone, the builds, the installed tools, the code that had been written on 16 and 17 October, the logs of the first test runs.
   2. Kept: the memory notes (including the name rule and the packaging rule of 17 October), the three delivered files, and the **transcript of the conversation**, a file that stays on the system outside the workspace.
4. **How the work was recovered.** Claude dumped the part of the transcript that held the work of 16 and 17 October (lines 560 to 1000 of the file as it then was) and read it. It held the request of 16 October word for word, the decisions, the table of the twelve characters, the shape of the parser changes, the list of tests and the messages that had been sent to Abhishek. The work was then **rebuilt**, not copied: the repository was cloned again (read-only) and an untouched copy of `Romenagri/` was kept as the reference; `flex` was built from the official release again (the package manager was blocked) and `gawk` was made a link to `mawk` again; the patch, the parser branches, the tests and the end-to-end programs were written again from the record. This is the one time in the conversation when work already done had to be done again, against instruction I2. It was unavoidable: there was nothing to continue from but the record.
5. **When the rebuilt work appears** (timestamps of the files, UTC):

   | When (UTC) | What |
   |---|---|
   | 17 Oct 22:32 | the untouched copy of `Romenagri/` and the first package directory of the rebuilt work area |
   | 17 Oct 23:16 | the first test log of the rebuild (`quick_run.log`) |
   | 17 Oct 23:17 | the work directories of the end-to-end test (`hrepo`, `hlogs`, `e2e_var`) |
   | 18 Oct 04:53 | the first big comparison of the written grammar with the real parser (item 8) |
   | 19 Oct 03:06 and 03:11 | the patched tree; the script that assembles the document from its parts (`assemble_doc.py`) |
   | 19 Oct 08:04 | the second quick run, and a directory of reproductions |
   | 20 Oct 01:48 | the third quick run (17.8 seconds); two directories that check that the patch applies to a fresh copy (the purpose is read from their names) |
   | 20 Oct 01:50 and 01:54 | two full runs; the second took 1 minute 44 seconds |
   | 20 Oct 01:56 | **zip no. 1** (07:26 IST) |
   | 20 Oct 01:57 | the zip unpacked into a clean directory and the quick run repeated there (`verify_quick.log`) |

6. **What changed in the rebuild** (the first implementation is in section 3.4):
   1. OM moved from `A0` to `8C`, because of the no-break space (section 3.4, item 5); this is the one design decision that the rebuild changed.
   2. The modification log of `rmn2acii.c` carries the date of the rebuilt patch: **19 October 2026** (patch 0001).
   3. The test suite grew from the first checks into ten steps, all passing in the third quick run: `table_lint_new`, `unicode`, `saral`, `parser_vs_model`, `roundtrip`, `corpus`, `recipes`, `limitations`, `doc_tables_in_sync`, `e2e_new`.
7. **The formal document, as it stood on 20 October** (`Romenagri/TRANSLITERATION.md`, 1,269 lines, 110,759 bytes). This is Abhishek's second wish of 16 October (I3, parts 5 to 7): work the algorithm out, write it down formally, analyse the formal definition so that it can be extended, and document it. Its contents:
   1. §1 purpose, status, vocabulary; §2 the three layers and the programs.
   2. §3 the three tables, the byte space, the invariants and the **lint** that checks them.
   3. §4 the decoder `acii2rmn` as a stack transducer.
   4. §5 the parser `rmn2acii`: how a string is read, the notation, **the grammar** (§5.3), what the grammar shows, worked examples.
   5. §6 the conventions by which the strings are built (R1 to R9).
   6. §7 the Sanskrit additions: what was added, why these bytes, why these strings, what the parser does with them, the saral table.
   7. §8 **how to extend**, as recipes A to F: tables only; a key that needs a parser rule; a mark that attaches to the letter before it; a new consonant; a new vowel with a sign form; repair or retire a row; with the checklist that is common to all.
   8. §9 the **round-trip contract**: the statement, what well-formed ACII is, what the contract leaves out, how to keep it when extending.
   9. §10 **larger character sets, character-set conflicts, missing sounds** (10.1 to 10.7): how much room is left; what a character needs layer by layer; choosing the byte; classifying a Unicode character; conflicts between standards and files; missing sounds; the admissibility conditions in one place. This is the part of the request that asks for extension "to larger character sets, handle character set conflicts, missing sounds".
   10. §11 known limitations and quirks (11.1 to 11.7); §12 provenance, standards, licence; §13 how to run the checks; Appendix A the complete table; Appendix B examples.
8. **The grammar is executable.** The grammar of §5.3 sits in a fenced block that a test program reads, so that it is the specification and its own test. It was compared with the real C parser (through a small harness that calls the parser as a library) and with a second, hand-written parser, on every string up to length four over the whole input alphabet and on random longer strings. The comparison of 18 October (56 seconds) covered **1,232,540 strings and found 0 disagreements**. Of those strings, the unpatched parser gave 1,095,255 normal outputs, 56,012 "missing" (the parser asks for a key that has no row, so the real one crashes) and 81,273 "overrun" (the parser steps past the terminating NUL); the patched parser gave 1,110,836, 40,051 and 81,653.
9. **Zip no. 1.** Made on 20 October at 01:56 UTC (07:26 IST).
   1. **137 entries, of which 125 are files and 12 are folders**; 391,754 bytes; SHA-256 `0e6aed5760f405e8e2f1b1657c67dd02594387f149d785b721a3b1fe9d4bfef0`. (The summaries of those days say "137 files": that counted the entries.)
   2. Top level: `README.md`, `NOTICE`, `LICENSE`, `COPYING`, `SHA256SUMS`. Then `Romenagri/` (the repository's directory, patched, with the new document), `patches/` (the one patch, `0001-add-missing-sanskrit-characters.patch`), `tools/` (`make_patch.sh`, `check_tables.py`, `apply_sanskrit.py`, `rmn_tables.py`, `gen_doc_tables.py`), `tests/` and `results/` (`environment.txt`, `quick-run/`, `full-run/`, `full-run-extended/`, with their logs).
   3. What its README said: the twelve characters (the table of section 3.4); what changed in the code (`unicode.h`, `acii.h`, `aciihin.h`, `acii2hin.c`, `rmn2acii.c`, and the new document); how to use it (`make all` in `Romenagri/`, or apply the patch to one's own checkout and reinstall); how to check it (`tests/run_all.sh`, about 20 seconds; `--full`, about 2 minutes); the results (table lint 0 errors, 42 free bytes left of which 19 are in the C1 block; the 12 new code points convert both ways and the 73 old rows convert exactly as before; and so on); and the **known limits**.
   4. The checks it recorded: ten steps, all PASS. In the end-to-end test the new tools reproduced the Devanagari source in the Java program (6 of 6 lines); the old tools gave the C control program 1 of 5 lines right and the Java program no output.
   5. The "extended" run added the 27 Hindi program files of the repository and rebuilt the shailis; it gave the same outcome.
10. **The limits that the first delivery named** (all are in §11 of the document; section 6 of this narrative collects them):
    1. the parser can ask for 102 keys and **15 of them have no row** in `acii.h` (`lha`, `kvra`, `tvra`, `_dvra` and others): the filter crashes on them, and typed text can reach them (this is what Abhishek asked about next, section 3.7);
    2. `acii2rmn` crashes on a nukta after a halant or a danda (ISCII's soft halant and avagraha) and drops the consonant before an explicit halant; dental DA or DHA followed by a nukta is misread;
    3. the lexical layer never hands `|` to the parser; rows that nothing reaches; buffers and unchecked reads; what does not survive a round trip; what `uni2acii` does with characters it has no row for (it writes the low byte); what the tests leave out.
11. **What was not done in these days:** nothing was put into the repository; no commit and no pull request were made; the repository clone was checked and is unmodified.

### 3.7 20 October (07:43 IST): "explain all the remaining 15 character bugs"

**Evidence: [summary] [memory] [package].** The message is quoted from the summary. The text of the reply is not retained; what is retained is the document that carries the same explanation (section 11.3) and the test that watches the crash.

1. **The message**, seventeen minutes after zip no. 1 had been made, and so after he had seen its list of limits:

   > "Please explain all the remaining 15 character bugs. I'll also read through, but explain those. I'll try to manually solve them. Otherwise, I'll pass it off to you later."

2. **What it asks** (instruction I5): explain the 15 keys that the first delivery named as having no row; he will read the explanation, and he will try to solve them himself; if he does not, he will hand them over later. **It is therefore an instruction not to fix them.** Every later step respected it: the 15 rows are still missing, on purpose, in zip no. 2 and in zip no. 3 (section 7, decision 7).
3. **What the 15 are.** The parser has a state (L2b) that, after one of fourteen consonant stems, looks at the next letter and builds one of three keys: the stem and `a`, the stem and `ha` (the aspirate), or the stem and `vra`. That makes 42 keys from 14 stems, of which 15 have no row in `acii.h`; the grammar can ask for 102 keys in all. When the parser asks for a key that has no row, `lookup()` returns `NULL` and the next `strcat` crashes: the filter exits with status 139 (SIGSEGV) and writes nothing.
   1. **Thirteen `vra` keys**: `bvra dvra gvra jvra kvra pvra svra tvra chvra _dvra _rdvra _rrvra _tvra`. They are reached by the Latin letter `v` after a consonant. `v` is not a letter of Romenagri (व is `w`: `swar`, `dwaar`, `jwaala`, `kwaath` work). The one spelling that has a row is `lvra`, ळ. So the thirteen are not thirteen missing characters; they are places where the parser's rule is more general than the table.
   2. **Two aspirate keys**: `lha` and `_rrha`. Devanagari has no letter for an aspirated ल or an aspirated ऱ; Hindi and Marathi write those sounds as conjuncts with ह (ल्ह, as in दुल्हन and चूल्हा). `lha` is the only one of the fifteen that could name an existing character, ऴ (U+0934, ISCII byte `D3`, which has no row and is free), and whether it should is the whole question about it.
4. **What was written down for the decision** (final form, section 11.3): a generated table of the 42 keys that the fourteen stems make, with the fifteen that lack a row marked and their typed forms; four ways to close them: A "look before you leap" (take the `h` and the `v` branch only when the row exists), B "conjunct fall-back" (read the `h` as `_ha`, giving ल्ह), C "`v` as `w`" (read `v` after a stem as व), D "add rows"; and the tool `tools/reserved_keys.py`, which builds the parser in a scratch copy, lists the typed form of each of the fifteen with what the parser does with it, and compares every other behaviour with the grammar, so that a fix can be checked. The tool and the options table were written after this message: the tool is not in zip no. 1 and is in zip no. 2 (section 3.8); which parts of them were already in the reply of 20 October is not recorded.
5. **What watches them.** The test `tests/test_limitations.py` repeats the crashes on the typed forms and fails if the behaviour changes, so a fix by Abhishek will show up as a deliberate change and not as an accident.
6. **Memory.** On 25 October the memory file about the repository received the line that he plans to try fixing the fifteen keys himself and will otherwise hand them over (section 2.3, item 1).

### 3.8 20 October (17:22 IST) to 25 October: three research questions, the underscore theory, an independent check, zip no. 2

**Evidence: [summary] [files] [package].** The three questions are described in the summary of 25 October, and the document records them (section 14.1) "in the order in which they were put"; the pasted text itself is not retained. The text of Claude's replies is not retained; the document, the tests and the second zip are.

1. **The message** (Tuesday 20 October, 17:22 IST, 11:52 UTC), ten hours after the one about the fifteen keys: *"Continue continue from where you were paused and also solve these."*, followed by three pasted research questions (instruction I6). It asks for two things: that the work in hand go on, and that the three questions be worked on as well.
2. **The three questions**, in the words of the summary of 25 October and of section 14.1 of the document:
   1. **Q1.** If single underscores are structural markers and `__` is the escape for a literal underscore, what happens to runs of three, four, five or N underscores? Is there a minimal grammar bound that makes reading and writing mutually inverse (a bijection) for runs of any length, without a second pass or a lookahead beyond the run? (The pasted version also asks about odd and even runs, and about greedy and non-greedy reading.)
   2. **Q2.** If the input is guaranteed to be lower case, what does that restriction do to the algebra of the language, and can the translator be verified not to crash on text that the host environment has changed arbitrarily?
   3. **Q3.** How many states does it take to keep the joiners of the script apart from the operators and escapes of a programming language, in one 7-bit ASCII front end? (In the pasted version: the minimal state-transition complexity.)
3. **What the code makes of the premises** (section 14.1; the answers were measured on the code, not assumed):

   | The question assumes | The code |
   |---|---|
   | single underscores mark structure, `__` is a literal underscore | yes, with a twist: `_` before a letter starts a family letter (`_ta`, `_ri`); `__` writes one literal underscore (byte `5F`) but there is no rule for it: it is what the family state does with an *unknown* family letter, and here that letter is `_`; a `_` at the end of the text is a halant |
   | runs of three or more underscores are ambiguous | they are not, in any text that the decoder writes for well-formed ACII, and the parser reads every run from the left |
   | the input is guaranteed to be lower case | there is no such guarantee anywhere: the parser passes capital letters through as text; the only `tr 'A-Z' 'a-z'` is in two branches of Hindawi's `std2hin.awk` (`praa_tha>` and `praa_thamika>`, before the translator) |
   | a unified front end separates script from host language | the lexers do, by rules that need no memory (section 11.1); inside the parser the two alphabets meet in one character, `_` |

4. **The short answers** (section 14.1):
   1. **Q1: yes, and the bound is small.** Reading a run needs a **two-state automaton** that works from left to right (the parity of the run so far). The language of runs is regular, so no context-free power is needed; the only lookahead is the character after the run, and only to say whether an odd run ends in a marker. Two states are also **necessary**. For well-formed ACII the decoder writes every literal underscore doubled and a marker only directly in front of a letter, so the two translators are inverse to each other for runs of any length.
   2. **Q2: the premise is false, and the answer splits in two.** The case fold is a letter-by-letter map that fixes `_`, so it keeps every run, and capital letters are inert in the parser. But the fold is not a homomorphism of the translator: it can turn an inert capital into a key letter, and that can destroy an escaped underscore (`C__f` keeps its escaped underscore, the folded `c__f` loses it in the parser of the repository). **Crash-resilience** against arbitrary strings can be proved (an induction on the rules, plus an exhaustive check) for the grammar with the guards and a complete table, where the parser is a total function; for the C code it is false, for the reasons of item 8.
   3. **Q3: two states, for one character.** The script alphabet that reaches the parser and the operator alphabet of a host language share the underscore and nothing else. Telling the roles of the underscore apart is the parity automaton, two states. Everything else that separates script from host language is decided by the lexers without memory. A joiner costs one parser rule and no state, if it follows the marker rule.
5. **The laws** (section 14.2 to 14.5), with `P(s)` for what the parser writes for `s` and a *closed* prefix for one that ends in a complete letter:
   1. **Law 1, the cut:** for a closed `u`, `P(u __ w) = P(u) · 5F · P(w)`. An escaped underscore cuts the string in two.
   2. **Law 2, the run:** for a closed `u` and a run of `n` underscores with `n` of at least two, `P(u _ⁿ w) = P(u) · 5F^⌊n/2⌋ · P((_ if n is odd) w)`. Every pair is one literal underscore, and an odd last one is the marker of what follows.
   3. **Law 3, the count:** the number of `5F` bytes in the output is the sum of ⌊n/2⌋ over the runs. It holds without conditions only with the guards (section 3.9).
   4. **The marker rule:** in every key of `acii.h` except `__`, each `_` is directly followed by a letter. It covers 47 keys: the 42 that start with `_`, `j_yna`, and the four `^_ri`, `^_li`, `^_lee`, `^_ree`. It is a property of the table, enforced by a new lint check, **T8**.
   5. **The smallest machine:** the strings `x` and `x _`, followed by `ta`, give different bytes (`BD` against the letter `_ta`, `C2`), so a transducer needs two states; the parity automaton is enough. The whole parser, counted as a machine, is five control states, a stem register with 14 values, one bit (`vocalic`) and a lookahead of at most four characters.
   6. **The bijection:** let `W` be the well-formed ACII texts with any number of literal underscores (`5F`) between their syllables and `R` the strings that `acii2rmn` writes for them. The decoder is injective on `W` and `rmn2acii` restricted to `R` is its inverse. The escape is `E = sed 's/_/__/g'`, which Hindawi applies after the translator in 12 of its 13 language branches (not in `roaboata>`), and it is a law of the same kind (Law 1).
   7. **A caveat that the independent check found** (item 11): the decoder, given ACII that is **not** well-formed, can leave a lone underscore (`A4 E8`, `A2 E8` and `EB E8` give `_`; `C4 E9` gives `__rda`, `C5 E9` gives `__rdha`, `A4 E9` gives `_za`), so the consequences of the marker rule hold for well-formed ACII only.
6. **Where the laws fail** (section 14.6): **eleven rules** of `rmn2acii.c` (twelve positions) take the character behind their test without looking at it: six unchecked skips (in L1 `c`, in L2b `v`, in L2c `e` and `y`, in M `e`, and in M `_`, which has two positions) and five wildcards that keep whatever character follows (in L2c `o`, `n`, `r`, `j`, and in M `o`). If that character is an underscore it is swallowed, and if it is the end of the string the rule steps over the terminating NUL and reads what is in the buffer from the previous call. The consequences were demonstrated on the unpatched parser and on the parser of patch 0001, which have the same eleven rules:
   - `tc__flag` (an escaped underscore, as Hindawi writes it after doubling) comes out as bytes without any `5F`;
   - `abc__x` loses its underscore, and `C__f` keeps it while `c__f` does not;
   - `tv__set` crashes (a missing row, item 8 of section 3.7);
   - after a long word, a short one can read leftovers of the long one (the parser's static buffer, `hldtxt[1024]`, is never cleared).
7. **The twelve guards** (section 14.7) were designed here: one rule in front of each of the eleven (twelve positions) that says *if the character the rule would jump over unseen is `_` or the end of the input, do not take the rule; write the letter as plain text, as the grammar's general rule does*. The repaired grammar has 95 rules, the same five states, a longest guard of four characters, no breakers, Law 3 without conditions, no read past the end, and is a total function once the fifteen rows exist. Each guard was shown to be necessary. It was checked **exhaustively on all 551,881 strings of up to four letters and on all 1,118,481 strings of up to five letters** over the letters that the rules test. It changes only strings with a letter that needs a partner directly before `_` or the end (3,909 of 486,585 strings of up to four letters; 86 of 18,208 strings of up to three letters). **On 25 October the guards were not applied to `rmn2acii.c`**: they change what a handful of invalid inputs mean (`c_`, `_n_`), which is Abhishek's decision (decision 8 of section 7); the document said where each one goes in the C code.
8. **Crash-resilience of the C code** (section 14.8; Q2): false, for four reasons. 1) The fifteen missing rows. 2) The eleven rules. 3) Fixed buffers: `rmn2acii` overflows at 1,025 letters in a row and `acii2rmn` its stack at 10,240 decoded characters; the limits are 1,023 and 10,239 as the code counts. 4) A stack underflow in the decoder on a stray halant or nukta (for example the bytes `31 E9` crash `acii2rmn`). On random mutations of valid spellings (truncate, change case, insert, delete, replace, escape, concatenate) the filter crashed on **43 of 14,762** in the quick run and **57 of 59,091** with `--full`.
9. **Joiners and operators** (section 14.9; Q3):
   1. The parser sees only runs of `[A-Za-z_]`; the rest of the text, host operators and escapes included, is copied by the lexer (section 11.1).
   2. Given alone, `rmn2acii` changes 17 of the 95 printable ASCII bytes: the fifteen letters `bdgjklmnprstwxy`, `_`, and (before the guards) `c`.
   3. **ZWJ and ZWNJ** have no rows (their low bytes, `0D` and `0C`, are what `uni2acii` writes for them, so they come back as a carriage return and a form feed). Spelled `_zwj` and `_zwn`, they would cost two rules and two rows and no state if they keep to the marker rule, and a free byte (section 10.3). They were **not added**, on purpose (decision 4 of section 7). In the same neighbourhood, `B3 E8 E8` (a consonant, an explicit halant, a halant) decodes to nothing and `B3 E8 E9` crashes the decoder.
10. **The tests and the lint** that hold all this in place: `tests/test_underscore.py`, checks **U1 to U9** (the cut and run laws on 598,994 exhaustive cases, 100,000 random pairs and 30,000 on the C parser; the parity machine; the decoder's marker rule on 30,000 texts; the escape on 100,000 strings; the eleven rules and their witnesses; the twelve guards on the two exhaustive ranges, each guard needed; case folding and 59,091 mutations; joiners and operators); the lint check **T8** (the marker rule); `--full` widens the ranges and `--deep` goes to six letters. They are arguments by induction and exhaustive checks in finite ranges, not machine-checked proofs: section 14.10 lists what is proved, what is tested and what is open (a machine-checked proof in Coq or Lean is open; the models are small enough that it could be done).
11. **The independent check** (24 and 25 October). Because the work had grown large, a separate agent was asked to check it: one that had not taken part in producing it, and that was given the code and the document and not the conclusions. (It reached its limit and was stopped by an API session-limit error twice; each time the work waited and was resumed with a message to the same agent, and it finished.) What it found, and what was done:
    1. **An overstatement in section 14.3**: the document said that the marker rule holds "in any text written by the decoder". It holds only for well-formed ACII (section 9.2). The sentence was qualified, a paragraph was added, and two checks were added to U4: three malformed inputs that leave a lone underscore (`A4 E8`, `A2 E8`, `EB E8` give `_`) and three more that give other wrong strings (`C4 E9`, `C5 E9`, `A4 E9`).
    2. **A precision about the branches**: the escape is applied in "twelve of thirteen" branches of Hindawi's `std2hin.awk`, not all.
    3. Other statements were re-measured against the code (example outputs, counts), and the generated tables were made to give the typed form of each of the fifteen keys (stem plus `vr`: `kvr` crashes, not `kvra`) in section 11.3.
12. **Zip no. 2** (Sunday 25 October, 05:02 UTC, 10:32 IST, twelve minutes after his "Continue" of 10:20 IST).
    1. **144 entries, of which 132 are files and 12 are folders**; 458,325 bytes; SHA-256 `b5657975f9f2aad0799a69f8765593310a485ecb082c1ed33ff542a04b5456e3`. A copy of its tree is kept unchanged in the work area (`state1`); it is identical to what the zip holds and is the base of patch 0002.
    2. New in it against zip no. 1: section 14 and the enlarged section 11.3 of the document; `tests/test_underscore.py` and the lint check T8; `tools/reserved_keys.py` (which lists the fifteen keys with the typed form of each, says what the C parser does with it, compares every other behaviour with the grammar, and with `--strict` exits with 1 until all fifteen are closed); the README rewritten with a section on the two later questions, the results of the full run (limitations: 152 measurements; reserved-keys smoke test on 20,440 strings: the C parser and the grammar agree on 18,208, both reach a missing row on 506, 1,726 read past the end and are not compared, 0 disagreements) and **eight decisions for Abhishek** (section 7); the records of three runs of the final tree (quick 47 seconds, full 3 minutes 18 seconds, extended 3 minutes 21 seconds) with `environment.txt`.
    3. **What it said about the fifteen and the guards**: no code was changed for them; the fifteen rows are "explained and measured, not repaired", and the twelve guards are "not applied".
13. **Memory, 25 October** (05:04 UTC): two lines were added to the file about the repository: that Abhishek plans to try fixing the fifteen keys himself and will otherwise hand them to Claude, and that he asked the three underscore questions.
14. **How the days went** (timestamps of the files, UTC): experiments with a fresh build of the tree on 20 October at 12:02 (ten minutes after the message), scripts for the laws, the necessity of two states, the repair and the breakers on 20 and 21 October, a rebuilt filter-pair model on 22 October, snapshots of the document and of the tests on 23 October at 05:34 before they were changed, recorded runs on 23 October at 17:39-17:45, the document's parts and the first new checksum file on 24 October (05:49-06:00), the independent check's copy of the package on 24 October at 05:50, the final runs on 25 October at 04:55-05:03 and zip no. 2 at 05:02. Abhishek's short messages in these days were *"Continue from where you got paused"*, *"Continue from where you got dropped off."*, *"Continue from where you left off."*, and *"Continue"* at 11:17 IST on 24 October, at 05:17 IST and at 10:20 IST on 25 October.

### 3.9 25 October (19:30 IST) to 3 November: "Apply the guard rules", this narrative, and the split of the long tests

**Evidence: [transcript] [summary] [files] [package].** The raw transcript reached back to 25 October, 14:06 UTC when this narrative was begun, so this is the first phase that rests on the record itself and not only on summaries; what the transcript showed was checked against the files, which are cited.

1. **The message** (Sunday 25 October, 19:30 IST, 14:00 UTC; instructions I7 and I8), two requests in one:
   1. *"Apply the guard rules."*
   2. *"Please give me a combined updated pointwise structured narrative of the conversation without dropping any points or facts or threads from the beginning."*
2. **How the first was read.** The twelve guards of section 14.7 had been checked only on the executable grammar and had been left unapplied on purpose (decision 8 of the README of zip no. 2: "whether to apply them to `rmn2acii.c`"). The message answers that decision: apply them to the real C parser. They were applied as **a second patch, 0002, on top of patch 0001**, and patch 0001 was left exactly as it was, so that the two changes stay separable and the second can be taken off (`patch -R -p1 < patches/0002-apply-underscore-guards.patch`). Abhishek was told this, and that the narrative would be rebuilt from the full record, in a message at the start of the work. The first request is the one that touches code; the second is this file.
3. **The state it started from.** An unchanged copy of the tree of zip no. 2 was taken (`state1`, 14:04 UTC); it is the base of patch 0002 and the "mid" build (patch 0001 alone). Three tasks were opened: apply the guards and make the grammar, the tests and the document agree; write the narrative; package and deliver.
4. **What was decided before any file was changed:** a new rule tag `!` in the executable grammar (none for all versions, `+` for patch 0001, `!` for patch 0002; every `!` rule has a `witness:` string in its comment); three versions of the parser selected by one argument of the models (`False` the unpatched parser, `"mid"` patch 0001 alone, `True` both patches, the default); a **third build** in the tests, `mid`, beside `old` and `new`; the document to say plainly "applied" where it had said "proposed" and "not applied". A note on words: "guard" is also the name of the part of a rule before the arrow, so the document says "guard rule" for a `!` rule and explains both senses.
5. **The change in `rmn2acii.c`** (patch 0002, modification-log entry of 26 October 2026):
   1. One helper: `static int no_partner (char next) { return next == '_' || next == '\0'; }`: true when the character after a letter is an underscore or the end of the string, that is, when the letter has no partner to take.
   2. **Twelve guards**, each in front of one of the eleven rules that read an underscore unseen (twelve positions): L1 `c`; L2b `v` (the guard falls to the stem and `a`, so `lv_` and `kv_` no longer ask for the key `lvra` or `kvra`); L2c `e`, `y`, `o`, `n`, `r`, `j`; M `e` and `o`; M `_` (two positions, both before the general rule that writes `^_ri`). Each writes the letter as plain text and goes on, as the general rule of the grammar does.
   3. **What it changes in meaning**: only strings with a letter that needs a partner directly before an underscore or the end. `c_` is now the letter `c` and a marker (before: CHA with its `h` missing); a lone `c` is plain text; `_o_` is `o` and a halant; and so on. On the strings that the decoder writes for well-formed ACII the guards cannot fire (section 14.7).
   4. The change is reproducible: `tools/apply_guards.py` applies it byte for byte (it asserts that each anchor occurs once and refuses to run on a tree that already has it or that lacks patch 0001).
6. **The grammar, the models and the tests followed.** The grammar of section 5.3 grew twelve `!` rules (95 rules in all, five states, longest guard four characters); `spec_model.py` learned the tag; the hand-written second parser, the harness, the differential test and the round-trip model got the third version; `tests/build_trees.sh` builds `old`, `mid` and `new` (and the matching Hindawi trees), and `tests/run_all.sh` calls it. Test design had to change in two places: the differential test used to say that a change without a new token inside is unexplained, which is no longer true, so it was split into old to mid (a new token is required) and mid to new (a guard must fire); the checks of the defects of section 14.6 (the eleven rules) are run on `mid`, and the checks that the guards fix them on `new`.
7. **What was measured** (the numbers are in the document, section 14.7, and in the logs of the runs):
   1. The grammar, the hand-written parser and the C parser agree on all three builds; the differential test of the quick run covers 65,259 strings with 0 disagreements, and the new parser never reads past the end.
   2. **Tail independence**: on 90,345 strings with and without arbitrary bytes after the terminator, the new parser's output never differs; the mid parser's differs on 11,000.
   3. **Invisible on well-formed ACII**: of the 621,435 short sequences, 331,621 well-formed ones give identical output on mid and new and all of them round-trip on new. Of 289,814 other sequences the guards change 8,599. Over all 394,419 sequences of up to three bytes of the old repertoire the guards change **2,482**, all ill-formed (for example `A1 DF`, which the decoder writes as `_n_ri`: mid gives `5f cf db`, new gives `6e aa`), with **0 regressions and 0 repairs**.
   4. **Strings of up to three letters**: the guards change 86 of 18,208; 66 of them kept the law before.
   5. **Random mutations** (14,762 of them): without the guards, 360 read past the end (2.4 %) and 40 reach a missing row (0.3 %); with them, none reads past the end and 35 reach a missing row, and the C parser crashes **exactly** on those 35.
   6. **The smoke test of the fifteen keys** on 20,440 strings: the unrepaired parser agrees with the grammar on 18,208, 1,726 read past the end, 506 reach a missing row and 20 break the underscore law; the new parser agrees on 20,179, none reads past the end, 261 reach a missing row and none breaks the law; with the fifteen rows filled in a scratch copy it agrees on all 20,440.
   7. The exhaustive ranges of the guard check, 551,881 and 1,118,481 strings (and 17.9 million with `--deep`), pass on the grammar and on the C parser.
8. **What the guards do not do** (this is the point that is easiest to get wrong): they **do not close the fifteen keys**. `kv` and `kv_` no longer crash (the guard stops the parser from asking for `kvra`), but `kvr`, `kva`, `lh` and `_rrh` still do; the rows are still missing, as Abhishek asked (section 3.7). The crash-resilience statement of section 14.8 is now "true for the C code **except for three reasons** that have nothing to do with the underscore": missing rows, fixed buffers (a run of 1,025 letters; 10,240 decoded characters) and the decoder's stack underflow on a stray halant or nukta (for example `31 E9`). Patch 0001 alone had a fourth, the eleven rules.
9. **The document** was changed in sections 5.1 to 5.4, 8, 11.4, 12.3, 13 and 14 (14.1, 14.2, 14.6 to 14.10) and in every place that said "proposal", "not applied", "shipped parser" or "patch 0001 only"; the fenced block of the guards became a generated block (the document now has 16 generated blocks, and `tools/gen_doc_tables.py --check` is clean). The document grew from 110,759 bytes on 20 October through 151,860 bytes on 24 October to 170,304 bytes now (the last 2,189 bytes are the paragraph on running the checks in pieces, item 14).
10. **The patch series**: `patches/0001-add-missing-sanskrit-characters.patch` (1,899 lines, unchanged) and `patches/0002-apply-underscore-guards.patch` (882 lines: the C change and the matching document; made again on 3 November, after the last change to the document). The script `verify_patches.sh` checks the series four ways, and it passed: (1) patch 0002 applied to the snapshot of patch 0001 gives the package's `Romenagri/`; (2) patch 0002 taken off again gives the snapshot back; (3) the untouched upstream directory with patch 0001 and then patch 0002 gives the package's `Romenagri/`; (4) `tools/apply_guards.py` applied to the snapshot gives the package's `rmn2acii.c` byte for byte.
11. **The runs.** The quick suite (twelve steps: `table_lint_new`, `unicode`, `saral`, `parser_vs_model`, `roundtrip`, `corpus`, `recipes`, `limitations`, `underscore`, `reserved_keys`, `doc_tables_in_sync`, `e2e_new`) passed 12 of 12 in 86 seconds on 29 October. The full and extended runs were long (the single step of the underscore check took more than eleven minutes) and were killed five times (by pauses and restarts, or, as it turned out, by an out-of-memory kill in the step itself); that is why the tests were split (item 14). The final runs, in pieces, are described there and in section 9, and their results are in the package (`results/`).
12. **The narrative.** Written in parts in the work area (`narr_parts/n1` to `n10`), one section at a time, after the facts of each period had been recovered from the sources named in "About this narrative"; the parts were checked against the files they cite (counts, dates, quotations), and mistakes found in the checking were corrected (section 8). It is assembled into `CONVERSATION-NARRATIVE.md`, which is part of the package.
13. **Abhishek's messages in this phase**, all *"Continue"* but one (item 14): Monday 26 October 11:33 IST, Wednesday 28 October 14:36, Thursday 29 October 07:48, Friday 30 October 05:17 and 14:50, Saturday 31 October 09:06 and 21:04 IST; then, on Sunday 1 November at 11:10 IST, *"Continue... Split the long running tests!!!! Those are not completing within work window and then you're repeating"*, and on Tuesday 3 November at 07:17 and 16:15 IST, *"Continue"*. Each one started a new working session in a fresh container (Appendix B).
14. **"Split the long running tests"** (Sunday 1 November, 11:10 IST, 05:40 UTC; instruction I9). The message, in full: *"Continue... Split the long running tests!!!! Those are not completing within work window and then you're repeating"*. It is, with "Don't redo work already done" of 15 October (I2), one of the two messages of the conversation that are about how the work is run and not about what it says, and it names three things: the long tests (the full and the extended suites), the work window (they did not finish inside one session) and the repeating (every new session started them again from the beginning).
   1. **What had happened.** The full and the extended runs were started detached (`setsid nohup`) and were killed five times (by pauses and restarts, or, as sub-point 6 shows, by an out-of-memory kill in the step itself): around 29 October 23:47 UTC, 30 October 09:30 UTC, 31 October 03:45 UTC and 15:47 UTC, and 1 November before 05:41 UTC. Each time they were inside the check of section 14 (`underscore --full`), which as one step took more than eleven minutes. Three causes: it was one long step; `tests/build_trees.sh` wipes the build directory, and the logs with it, at the start of every run; and no step left a marker of its own, so a finished step could not be told from an unfinished one.
   2. **The check of section 14 was split into its nine checks.** `tests/test_underscore.py` takes `--only U1,U7`: U1 to U3 sat inside the shared function of the laws and were wrapped one by one, the inputs that U6, U7 and U9 share were hoisted out of U6, and the RESULT line says `[only ...]`. Two checks were made before the split was relied on: the old and the new script, both in quick mode, wrote the same 132 lines (the timings aside), and each of the nine checks run alone passed. In quick mode the nine take 21, 0, 0, 1, 4, 1, 34, 2 and 1 seconds, and the whole check takes 64.
   3. **`tests/run_all.sh` was rewritten.** The check of section 14 is nine steps (`underscore_U1` to `underscore_U9`), so the suite has twenty. Every step writes `build/logs/<step>.log` and a marker `<step>.rc` (exit status, seconds, time of the end). `--resume` skips a step that passed, and the build too, as long as the stamp (a hash of every file of `Romenagri/`, `patches/`, `tools/` and `tests/`, and of the settings) is the one written at the build. `--only <steps>` runs the named steps (`build`; `underscore` for the nine). Python is run unbuffered, so that a log shows progress while it is being written. The header of the script and section 13 of the document give a recipe for a pool of two workers (`xargs -P 2`, the longest steps first); a last `--full --resume` prints every step and the summary. The plain quick run behaves as before.
   4. **The document and the patch.** Section 13 of the document got a paragraph, "Long runs in pieces", and the lines of the commands (the document is now 170,304 bytes); patch 0002 was made again (882 lines) and the four checks of `verify_patches.sh` passed again; `tools/gen_doc_tables.py --check` is clean (16 generated blocks). The markers are tied, by the stamp, to the files of `Romenagri/`, `patches/`, `tools/` and `tests/`, so these edits were made before the final runs and nothing in those directories was changed after them.
   5. **The new driver was tried at once**, on the quick suite: 20 of 20 PASS in 106 seconds (3 November, 01:48:46 to 01:50:32 UTC).
   6. **The first full run** (3 November, from 01:51:19 UTC) was a pool of two workers over the twenty steps minus the build, the longest first. Nineteen steps passed within four minutes (the longest, `parser_vs_model`, took 117 seconds). `underscore_U7` was killed after 580 seconds with exit status 137, and the kernel's log says why: *"Memory cgroup out of memory: Killed process (python3) ... anon-rss:6107268kB"*, 6.1 GB. The cause, as far as it was traced (the memory was not measured separately; the step finished in 74 seconds once the check was changed), was one check of that step, the one that compares the C parser's output with and without a tail after the terminator: on all 1,670,362 strings of `--full` it held three lists of outputs in memory, and the parser without the guards writes up to 4,096 bytes for each string on which it reads past the end. **So the kills of 31 October, 8 to 12 minutes after each launch, were probably this out-of-memory kill and not pauses**; the earlier explanation (pauses and restarts) was at least incomplete, and the single long step could not have finished either way. The check now works through the strings in chunks of 20,000, and the parser without the guards, which is only measured (informational, and it must fail the check, which it does: 11,000 strings differ), is run on the 90,345 strings of the quick ranges instead of all of them (on all of them it took ten minutes); the parser of this package keeps the full ranges. The quick output is the same but for one label. `tests/` had changed, so the stamp changed and everything was run again.
   7. **The second full run** (from 02:05:12 UTC): All twenty steps passed. The build started at 02:05:10 UTC and the last step finished at 02:07:48, so the run took 2 minutes 38 seconds in all; the steps took 310 seconds together (`parser_vs_model` 112 s, `underscore_U7` 74 s, `roundtrip` 48 s, `underscore_U1` 31 s, `underscore_U5` 17 s, and 9 s or less for each of the others). A last `--full --resume` pass printed every step from its log and marker, and the summary (`results/full-run/console.log`: 20 PASS). The stamp of the sources, `d32f3ea25d5ca007`, was checked to be unchanged before the results were collected, and again in the unpacked zip.
   8. **The extended run** was reduced to the two steps that read the extra inputs: `corpus` reads `RMN_CORPUS` (here the 27 `.uhin` files of the repository) and `e2e_new` reads `HINDAWI_SRC`. Of the scripts of `tests/` and `tools/` only `test_corpus.py` and `e2e/run_e2e.sh` read either variable (checked with `grep`; `run_all.sh` only names them and keeps them in the stamp), so the other eighteen steps of an extended run would repeat the full run exactly. It has a build of its own. It passed (3 November, 02:08:08 to 02:08:14 UTC, 6 seconds with its own build): `corpus` went through the 27 `.uhin` files and the two corpus text files with no unexplained difference, and `e2e_new` rebuilt the four shailis (`c2h`, `h2c`, `h2j`, `j2h`) with this Romenagri and printed the Devanagari that was written (6 of 6, 5 of 5 and 6 of 6 lines).
15. **What is not done:** nothing was pushed or committed anywhere; the repository clone is unmodified at commit `3ad87785a75dc2b18438a8b068807103cb920c81` (checked again on 3 November); the fifteen rows are still missing; no option of section 11.3 has been applied; the other 57 files of `Romenagri/` still carry their old notices.

### 3.10 3 November (16:22 IST) to 8 November: the fifteen rows once more, the cluster ड़्व that failed, and the nukta layer (patch 0003, zip no. 4)

**Note (11 November).** This section describes the nukta layer as it was in zip no. 4: the policy `NUKTA_REBUILD` with three levels (1, NFC, the default), 75 checks in nine parts, a patch of 895 lines. On 8 November Abhishek decided each of the cases C1 to C8, and the layer was made again on those decisions; what stands in zip no. 5 is told in section 3.11. The figures and statements below are those of zip no. 4 and are left as they were.

**Evidence: [transcript] [summary] [files] [package].** The raw transcript, as it exists at the delivery of zip no. 4, begins at 22:26 UTC on 4 November. What came before survives in the summaries (written at 22:30 UTC on 4 November and at 02:06 and 22:06 UTC on 6 November), in the files with their dates, and in two scratch probes (`probe_chain.py` and `probe2.py`, not part of the package) that were run again to recover what they had shown. **The text of Claude's replies of 3 and 4 November is not retained**, so items 2 to 5 give their substance, rebuilt from the probes, the document and the summaries. From 22:26 UTC on 4 November the record itself is the source; what it showed was checked against the files, which are cited.

1. **The messages of this phase** (instructions I10 to I14; Appendix A has every message with its time):
   1. Tuesday 3 November, 16:22 IST (10:52 UTC), three minutes after zip no. 3 had been made (10:49 UTC): *"which 15 rows are still not fixed. Give me the exact details. You've taken, I don't know how many dozens of turns"* (I10).
   2. 16:26 IST (10:56 UTC): *"right? Give those characters with their Devanagari characters and the common pronunciation in Eastern India, in Northern India, in Central India, and in Southern India. Remember, these pronunciations vary by region."* (I11).
   3. Wednesday 4 November, 11:59 IST (06:29 UTC): *"Continue"*.
   4. 12:08 IST (06:38 UTC): *"Except for 13 and 15... All are covered by even the oldest Romenagri behenchod"*, and after a blank line *"Try passing Devnagri through"* (I12).
   5. 12:27 IST (06:57 UTC), in four paragraphs: *"This should work ड़्व"*, *"Let me check manually"*, *"But now I am lead to doubt your three weeks of work as a waste of my time"*, *"Reviewing everything you did..."* (I13). The summaries record the letter in it as the single code point U+095C, which is how it is shown here.
   6. 19:50 IST (14:20 UTC): *"Add in the patch... Just add a layer that decomposes the underlying nukta layer, and builds it back"*, and after a blank line *"Are there any technical challenges? If you identify any please show those in Devnagri for me to review"* (I14).
   After these come only short messages (item 17).

2. **The first answer: the fifteen rows, with the exact details (3 November).** The rows are the fifteen keys of section 11.3, in the order of the table of that answer; the numbers are the ones he uses in item 1.4. The table below is rebuilt from the probe and from the document, and its bytes are from a run of the converters on the final build:

   | # | Cluster | Key the parser asks for | ACII from Unicode | What `acii2rmn` writes for it |
   |---|---|---|---|---|
   | 1 | त्व | `_tvra` | `C2 E8 D4` | `_twa` |
   | 2 | द्व | `_dvra` | `C4 E8 D4` | `_dwa` |
   | 3 | स्व | `svra` | `D7 E8 D4` | `swa` |
   | 4 | ज्व | `jvra` | `BA E8 D4` | `jwa` |
   | 5 | क्व | `kvra` | `B3 E8 D4` | `kwa` |
   | 6 | ग्व | `gvra` | `B5 E8 D4` | `gwa` |
   | 7 | च्व | `chvra` | `B8 E8 D4` | `chwa` |
   | 8 | ट्व | `tvra` | `BD E8 D4` | `twa` |
   | 9 | ड्व | `dvra` | `BF E8 D4` | `dwa` |
   | 10 | प्व | `pvra` | `C8 E8 D4` | `pwa` |
   | 11 | ब्व | `bvra` | `CA E8 D4` | `bwa` |
   | 12 | ड़्व | `_rdvra` | `BF E9 E8 D4` | `_rdwa` |
   | 13 | ऱ्व | `_rrvra` | `D0 E8 D4` | `_rrwa` |
   | 14 | ल्ह | `lha` | `D1 E8 D8` | `l_ha` |
   | 15 | ऱ्ह | `_rrha` | `D0 E8 D8` | `_rr_ha` |

   Rows 1 to 13 are the thirteen keys of the form stem + `vra`: the Latin letter `v` typed after a consonant (in Romenagri व is `w`). Rows 14 and 15 are the aspirates `lha` and `_rrha`, typed `lh` and `_rrh`. Each key is one that the parser can ask for and `acii.h` has no row for: `lookup()` returns `NULL` and the next `strcat` crashes, so the filter ends with signal 11 (status 139 in a shell). The answer did not fix them: he had said on 20 October that he would try them himself (I5).

3. **The second answer: the same fifteen, in Devanagari, with the pronunciation by region (3 November).** The regional facts were given from general knowledge (no source in the repository or on the web was used, and the point of the answer was that they differ by region); the summaries keep only this much of it, and the full table of the answer is not retained:
   1. **व in the thirteen `C्व` clusters** (rows 1 to 13): the North says [ʋ]; in the East, Bengali and Assamese leave the व silent and double the consonant, and Odia says [w]; in the Centre, Marathi says [ʋ], and its च and ज are often [ts] and [dz]; in the South the sound is [ʋ], and Tamil often splits the cluster.
   2. **ल्ह** (row 14): Hindi [lɦ], Marathi [lʱ], and in Tibetan names the lateral fricative [ɬ].
   3. **ऱ्ह** (row 15): Marathi [ɾʱ].
   4. **ऴ**, the one letter that `lha` could have named (section 11.3, option D): only Tamil ழ and Malayalam ഴ have it, [ɻ].

4. **"Try passing Devnagri through": three probes (4 November, from 06:29 UTC).**
   1. **The typed side** (`probe_in.txt` and `probe_out.txt`, 06:29 UTC). Each of the thirteen `vra` clusters in a word, typed with `v` and with `w`, and the two aspirates typed with and without the underscore. Run again on the unpatched build: the `v` forms and `lhaasaa` and `_rrhe` end with signal 11 (`kvaath`, `gvaala`, `chvaa`, `jvaala`, `_tvii_t`, `_dvaa`, `_rdvaa`, `_rrvaa`, `tvam`, `dvaar`, `pvaa`, `bvaa`, `svar`), and the `w` forms and `l_haasaa` and `_rr_he` give the right ACII (`kwaath` is `B3 E8 D4 DA BE E8`, `dwaar` is `BF E8 D4 DA CF E8`, `l_haasaa` is `D1 E8 D8 DA D7 DA`). **That is the sense in which every cluster is "covered by even the oldest Romenagri":** the decoder writes `_twa`, `dwa` ... `l_ha`, `_rr_ha` (the last column of the table in item 2), and the parser reads those; the fifteen keys are asked for only by the typed `v`, `lh` and `_rrh`.
   2. **Devanagari through the whole chain** (`probe_chain.py`, 06:40 UTC): the fifteen clusters, two to four forms each (for instance त्वचा, तत्त्व; द्वार, विद्वान; स्वर; ज्वाला; ग्वाला; चूल्हा, दुल्हन, कुल्हाड़ी; कुऱ्हाड, गोऱ्हा), through `uni2acii`, `acii2rmn`, `rmn2acii` and `acii2uni` on the old, the mid and the new build of zip no. 3. **Every form comes back exactly on all three builds, with one exception: the cluster ड़्व when its first letter is the single code point U+095C**, which comes back as व (U+0935) alone, on all three (and ड़्वा as वा). Written as ड and a nukta (`BF E9 E8 D4`, `_rdwa`) it comes back exactly. His exception of rows 13 and 15 (ऱ्व, ऱ्ह) is not explained in the message; in the probes both pass, written with U+0931 or with U+0930 U+093C, and they fail only in the joiner spelling of probe 3.
   3. **The precomposed letters and the eyelash ra** (`probe2.py`, 06:41 UTC). (1) The eight single code points U+0958 to U+095F are written by `uni2acii` as their low byte (`58` to `5F`; a backslash for U+095C) on the old and the new build of zip no. 3, and come back wrong; their NFC forms, a consonant and U+093C (bytes such as `B3 E9`), pass. (2) The Marathi spelling of ऱ्ह and ऱ्व with a joiner, RA + VIRAMA + ZWJ + HA (र्‍ह), comes back on every build with a carriage return (`0D`) where the joiner was: the joiners fall to their low byte (section 10.4), which is not the nukta's business.

5. **The cluster ड़्व that failed (his message of 12:27 IST).** His own check agreed with probe 4.2: with the single code point U+095C the cluster came back as व.
   1. **The cause**, in three steps (section 15.1): `unicode.h` has no row for U+095C, so `uni2acii` writes its low byte, `5C`, a backslash; `acii2rmn` takes `5C` for an ordinary character; and the halant behind it takes that character off again (the rule of section 11.5 for a halant where the grammar does not allow one), so `5C E8 D4` is written `wa` and comes back as व. Without the halant, `5C D4` is written `\wa`.
   2. **It was not specific to that cluster.** Eight code points (U+0958 to U+095F) and U+0934 have no row; any text that contained one of them was damaged by `uni2acii` before it reached the filters (probe 4.3).
   3. **What the document had said.** It recorded the low-byte fallback (section 11.6) and advised normalising to NFD before `uni2acii` (section 10.4). That works, but it asks every pipeline to do it, and it fails silently where someone forgets. The defect was known and documented as a limit of the converters (test (d) of `tests/test_unicode.py` classified the unmapped code points), and it had not been connected to the cluster ड़्व of section 11.3 until he tried it.
   4. **His doubt** (*"your three weeks of work as a waste of my time"*) is recorded as he wrote it. The finding does not touch the twelve characters of patch 0001 or the guards of patch 0002: the fallback is the converter's own, from the repository.

6. **The request (19:50 IST) and how it was read.**
   1. *"Add in the patch... Just add a layer that decomposes the underlying nukta layer, and builds it back"*: a layer in the Unicode converters that takes a precomposed nukta letter apart on the way into ACII, where ACII already writes a nukta letter as the consonant and `E9`, and puts it together again on the way out.
   2. *"Are there any technical challenges? ... show those in Devnagri for me to review"*: the places where the layer, or the standard it follows, asks for a decision or leaves a limit, shown with Devanagari and code points (item 10).
   3. **One decision of Claude's own, shown to him: the layer is patch 0003, a separate patch**, and not an edit of patch 0001, although the message says "in the patch". The three changes stay separable and each can be taken off (`patch -R -p1 < patches/0003-add-nukta-layer.patch`). The code files of patch 0003 (`uni2acii.c`, `acii2uni.c`, the Makefile, `nukta.h`) are not among those of patch 0001, so its code can be moved into patch 0001 unchanged; the document and patch 0002 would have to be made again. The README and the delivery message say so and offer to fold it in (section 7.2, decision 9, part (d)).

7. **The design** (section 15.2 of the document; the architecture is unchanged).
   1. **The facts it rests on** (sections 15.1 and 15.3, measured on the converters and the tables): ACII writes a letter with a nukta as two bytes, the consonant and `E9`, which is U+093C; Unicode has eleven letters that are such a pair in one code point; `unicode.h` had a row for two of them, ऩ U+0929 (`C7`) and ऱ U+0931 (`D0`), and none for the other nine; of the eleven, NFC composes three (U+0929, U+0931, U+0934) and leaves eight decomposed (U+0958 to U+095F, the composition exclusions).
   2. **The files.** `Romenagri/nukta.h` is new: the table `nukta_hin` (eleven rows: code point, consonant, level), `NUKTA_BYTE` = `E9`, `NUKTA_REBUILD`, and the function `nukta_acii_of`. `uni2acii.c`: a row of `unicode.h` first, then `nukta_hin` (the consonant's byte and `E9`), then the low byte as before. `acii2uni.c`: the table lookup moved unchanged into a function `put`, and a held byte: a consonant of a row whose level is at most `NUKTA_REBUILD` is held back, and if `E9` follows, the converter writes the single code point; a newline or the end of the input ends the wait. The `Makefile`: `nukta.h` is a prerequisite of the target `unicode`, installed and removed with the headers. One byte of state, one byte of lookahead.
   3. **What the layer does not touch:** no row of any table changes and no byte of the free list is used; the decoder, the parser, the lexers and the saral table are as before; the fifteen reserved keys are untouched, as he asked on 20 October.
   4. **Reproducible:** `tools/apply_nukta.py` applies the change to a tree byte for byte (it asserts that each anchor occurs once and refuses a tree that already has it); `tools/rmn_tables.py` got `parse_nukta`, `tools/gen_doc_tables.py` the table of the document and the new class of unmapped code points, and `tools/make_patch.sh` makes the patch.
   5. **Notices:** the new and changed files carry `Copyright (C) 1993-2026 Abhishek Choudhary`; the three changed files have a Modification entry dated 5 November 2026 with the alias `<obonac>` and "(prepared with Claude)", and `nukta.h` has the GPL block and an entry of the same date.

8. **The policy `NUKTA_REBUILD`** (section 15.6). `acii2uni` rebuilds the rows of `nukta.h` whose level is at most the macro. **Level 0** rebuilds nothing (the old output exactly). **Level 1, the default, writes NFC:** ऩ ऱ ऴ are rebuilt and the eight letters stay pairs. **Level 2** rebuilds all eleven. `uni2acii` ignores the level. Why 1: a consumer that normalises text to NFC finds level-1 output as it expects it, whereas level-2 output would be taken apart again by any normaliser; and level 1 lets Python's `unicodedata` serve as an independent oracle in the tests. It is one macro: `make unicode CFLAGS="-Wall -Wno-unused -DNUKTA_REBUILD=2"`. The choice rests on two cited sources (section 12.1; item 13) and is his to confirm.

9. **What changes for existing text, and what does not** (section 15.4).
   1. `uni2acii`: the nine code points were written as their low byte and are now written as two bytes (ड़ was `5C` and is `BF E9`); the other 65,527 code units of the BMP are written as before.
   2. `acii2uni` at the default level: **`C6 E9`, `CF E9` and `D2 E9` now come out as one code point** (ऩ ऱ ऴ) where they used to come out as two; of the 64,516 pairs of bytes, these are the only three whose output changed. This is an intended change of behaviour; the README lists it as part (c) of decision 9.
   3. At level 0 the converter is the old one byte for byte (random streams, all pairs and both kinds of triples).
   4. **The repaired case:** the cluster ड़्व written with U+095C comes back as ड़्व and no longer as व.

10. **The technical challenges, shown in Devanagari** (section 15.7 has the whole tables, with the code points and the bytes; each case is printed and asserted by part (i) of `tests/test_nukta.py`; the README has them in short). Results are for the default build.

    | # | Case | ACII | Result | What is left to him |
    |---|---|---|---|---|
    | C1 | each of the eight क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़ (U+0958 to U+095F) as one code point, or as a consonant and U+093C (for ड़: U+095C, or U+0921 U+093C) | `BF E9` for ड़ | out as the pair (NFC); level 2 writes the single code point | the level (item 8) |
    | C2 | ऩऱऴ as single code points (U+0929 U+0931 U+0934), or as pairs (U+0928 U+093C, U+0930 U+093C, U+0933 U+093C) | `C7 D0 D2 E9`, or `C6 E9 CF E9 D2 E9` | both give the single code points; at level 0 the pairs stay pairs | nothing: ऩ and ऱ have two spellings in ACII, ऴ one |
    | C3 | ऩ्: न + halant + nukta (U+0928 U+094D U+093C) | `C6 E8 E9` | **not rebuilt**; NFC would reorder it and write U+0929 U+094D; `E8 E9` is also ISCII's soft halant; `acii2rmn` crashes on it (signal 11) | whether to reorder, and how to tell a nukta from the soft halant |
    | C4 | नि़ (U+0928 U+093F U+093C) and न ़ (U+0928 U+0020 U+093C) | `C6 DB E9`, `C6 20 E9` | nothing to rebuild; NFC agrees | nothing |
    | C5 | नé (U+0928 U+00E9) | `C6 E9` | out as ऩ: the é was never a nukta; `uni2acii` writes it as its low byte | nothing: the old defect of section 11.6, seen differently |
    | C6 | ड़्व with U+095C | before: `5C E8 D4`, `wa`, व; with the layer: `BF E9 E8 D4`, `_rdwa` | **repaired**: out as ड़्व | nothing |
    | C7 | ऴ; कऴन | `D2 E9` (`lvrza`); `B3 D2 E9 C6` (`kalvrzana`) | out as ऴ; it has no byte of its own | whether to give it `D3` (recipe A) |
    | C8 | ऱ्हल्ह (U+0931 U+094D U+0939 U+0932 U+094D U+0939) | `D0 E8 D8 D1 E8 D8` (`_rr_hal_ha`) | pass through; the typed `lha`, `_rrha` and `_rdvra` still crash `rmn2acii`; the fifteen keys are **untouched** | the options A to D of section 11.3 |

    The decisions left to him (section 7.2, decision 9): **(a)** the level, 1 or 2; **(b)** reordering across a halant (C3); **(c)** a byte of its own for ऴ (C7); **(d)** whether patch 0003 is folded into patch 0001.

11. **Tests** (section 15.8 of the document; the step `nukta` of `tests/run_all.sh`, which now has 21 steps).
    1. `tests/test_nukta.py` is new: **75 checks in nine parts**, (a) to (i):
       - (a) `nukta.h` against Python's `unicodedata` (Unicode 15.1): the eleven rows are exactly the code points of U+0900 to U+097F whose NFD is a consonant and U+093C; a row has level 1 if and only if NFC composes the pair; the bases all have a byte; only U+0929 and U+0931 have a row in `unicode.h`; the default is level 1.
       - (b) `uni2acii`: each of the eleven letters is written as its table byte, or as the consonant's byte and `E9`.
       - (c) `acii2uni` compiled at levels 0, 1 and 2 from the same source without a warning, and what each level writes for each of the eleven pairs.
       - (d) A model of the rule in Python against all three levels, on random streams and exhaustively on `x y`, `x E9 y` and `x y E9` for every pair of bytes (64,516 lines each): level 0 equals the build without the layer, and level 1 differs from it on exactly the three pairs `C6 E9`, `CF E9` and `D2 E9` (and on the lines that contain them).
       - (e) Python's NFC as an independent oracle at level 1: on the streams whose marks are in canonical order (191,617 of 200,000) level 1 writes NFC of what the build without the layer writes, with no disagreement; a negative control (the build without the layer is not in NFC on 21,880 of those streams, so the oracle can fail); and the measured limit: on the 8,383 streams with marks out of canonical order NFC would reorder and the layer does not.
       - (f) `uni2acii` on all 65,527 other code units of U+0000 to U+FFFF, unchanged from patch 0001 alone; the nine are the only ones whose output changed.
       - (g) Fourteen edge cases at level 1: a consonant at the end of the stream, before a newline and before another consonant; `C6 C6 E9`; `C6 E9 E9`; `E9` alone and after a newline; `C7 E9`; a newline, a halant (`C6 E8 E9`) or a vowel sign between; `CF E9 D2 E9`; `B3 E9` (level 2, so not rebuilt by default); the empty input; the usage lines.
       - (h) The whole chain: the eleven letters, each as the single code point and as a consonant and a nukta, alone, with a consonant before and an aa sign after, and with a halant before: 66 of 66 come out as NFC of the input (with patch 0001 alone, 0 of the nine single code points do); the fifteen clusters of section 11.3 (16 strings, ड़ in both spellings): 16 of 16 (on the unpatched build ड़्व with U+095C fails).
       - (i) The challenges of item 10, each asserted and printed.
       The quick run uses 30,000 random streams and `--full` 200,000.
    2. `tests/test_unicode.py` (part (d)) and `tests/test_limitations.py` (the U+0934 measurement) were updated. `tests/run_all.sh` has the new step after `unicode`, and its header names the three patches; `tests/build_trees.sh` builds `new` with all three patches and `mid` with patch 0001 only.

12. **The document, the README and the notice.**
    1. `Romenagri/TRANSLITERATION.md` got a new **section 15, "The nukta layer (patch 0003)"**, in nine parts (15.1 to 15.9): what was missing; the design; the eleven letters (a generated table, `nukta-table`); what does not change; where the layer stops (no reordering; the round trip exact only up to canonical equivalence; Romenagri not extended; the low-byte problem remains for everything else, é among them; the joiners not handled); the policy; **the challenges C1 to C8 in Devanagari** (15.7); what is tested; what is left to the reader. It also got the acceptance row **A11**, and about thirty-five edits in the existing sections: the contents and the vocabulary (the nukta layer, the level), the list of patches, section 3.1, section 10.4 item 3 (the advice to normalise to NFD first now describes the time before patch 0003), 11.5, the U+0934 row of 11.6, the sources table of 12.1 (two new citations, item 13) and section 13 (commands and tables). The document has 17 generated blocks (16 before) that `tools/gen_doc_tables.py --check` finds in sync, and is 196,035 bytes (170,304 on 3 November).
    2. **Proofreading** found errors in the new text before delivery; they were corrected (section 8, item 14).
    3. **`README.md`** is rewritten for the three patches (the section "The nukta layer" with the table of challenges, decision 9 in "Decisions that are yours to confirm", and the note on what was found on the way), and **`NOTICE`** likewise: the eight changed files (five by patches 0001 and 0002, three by patch 0003) and the two new files (`TRANSLITERATION.md`, `nukta.h`) carry the 1993-2026 notice; 54 files of `Romenagri/` are untouched (57 before patch 0003); `Romenagri/` has 64 files; the two new citations are named and not included.

13. **The citations** (section 12.1; both pages were fetched again on 6 November and could be read). The composition exclusions of U+0958 to U+095F: a copy of the Unicode Character Database file `CompositionExclusions.txt` at `https://stuff.mit.edu/afs/sipb/contrib/doc/specs/protocol/unicode/CompositionExclusions.txt` (its header reads "CompositionExclusions-2.txt"; the eight code points are listed under "(1) Script Specifics"). And the thread "Query Regarding NFC Normalization and Script-Specific Exclusions for Devanagari" on the Unicode mailing list, 1 May 2025, `https://corp.unicode.org/pipermail/unicode/2025-May/011443.html`, which says that the decomposed forms were the experts' preferred representation for Devanagari. **One sentence of the document said more than the thread says** ("which says of U+0958 that NFC does not recompose it ..."); it was reworded to what the page supports. The document is part of patch 0003, so the patch was made again and **every suite was run again**; the results of the first full run of 6 November (10:45 UTC) were discarded.

14. **Patch 0003** is `patches/0003-add-nukta-layer.patch`: 895 lines, 90,338 bytes, five files (`Romenagri/nukta.h`, `uni2acii.c`, `acii2uni.c`, `Makefile` and `TRANSLITERATION.md`); patches 0001 and 0002 are unchanged. It is made by `tools/make_patch.sh` and was checked four ways by `verify_patch3.sh` (a script of the work area, not in the package), all passing on the final files: (1) patch 0003 applied to the tree of zip no. 3 gives the package's `Romenagri/`; (2) taken off again, it gives the tree of zip no. 3 back (`nukta.h` is gone too); (3) the untouched upstream directory with patches 0001, 0002 and 0003 in order gives the package's `Romenagri/`; (4) `tools/apply_nukta.py` on the tree of zip no. 3 gives `uni2acii.c`, `acii2uni.c`, the Makefile and `nukta.h` byte for byte.

15. **The runs of 6 November, on the final files** (kernel `6.18.44-fc-v300`; `results/environment.txt` and the consoles and logs under `results/`). The quick suite: 21 of 21 steps in 83 seconds (stamp `bf982fe864053d90`). The full suite, as `--only build`, two pools of two workers (`xargs -P 2`) and a last `--full --resume`: 21 of 21 steps in 2 minutes 40 seconds, from 21:58:05 to 22:00:45 UTC; the steps took 284 seconds together (stamp `d160b87c927f6039`). The two extended steps: 5 seconds (stamp `b68b0acf5a5b38d3`). The first full run of that day (10:45 UTC) was discarded (item 13). The kernel of the container changed between sessions (section 9, item 3); the files persisted and the processes did not.

16. **Zip no. 4** (Appendix C): 169 files in 12 folders. `SHA256SUMS` was made again over every file but itself, and `tests/__pycache__`, `tools/__pycache__` and any `build/` were removed first. The zip was unpacked into a clean folder, the four checks of patch 0003 and the quick suite were repeated there, and it was sent with `SendUserFile`; its size and checksum are in the delivery message (a file cannot contain its own checksum).

17. **Abhishek's other messages in this phase**, all short, each starting a working session in a fresh container (Appendix B): *"Continue"* on Thursday 5 November at 03:50 IST (22:20 UTC on 4 November), 10:19 IST (04:49 UTC) and 19:35 IST (14:05 UTC); on Friday 6 November at 07:27 IST (01:57 UTC); *"Please continue to completion now."* on Friday 6 November at 16:05 IST (10:35 UTC); *"Please continue."* on Saturday 7 November at 03:26 IST (21:56 UTC on 6 November); *"Continue"* on Saturday 7 November at 08:35 IST (03:05 UTC) and on Sunday 8 November at 05:42 IST (00:12 UTC). The line in memory about the request of 4 November was written on 7 November (the thirteenth line of the file about the repository).

18. **What is not done:** nothing was pushed or committed anywhere; the repository clone is unmodified at commit `3ad87785a75dc2b18438a8b068807103cb920c81` (`git status` clean, checked on 7 and 8 November); the fifteen rows are still missing (no option of section 11.3 was applied, and patch 0003 does not touch the parser); a nukta after a halant is not folded and the joiners are not handled; ऴ has no byte of its own; the other 54 files of `Romenagri/` still carry their old notices.

### 3.11 8 November (11:42 IST) to 11 November: the decisions on C1 to C8, the nukta layer made again (zip no. 5), and the site that Grok built

**Evidence: [transcript] [summary] [files] [package].** The raw transcript, as it exists at the delivery of zip no. 5, begins at 04:59 UTC on 10 November and holds two summaries (written at 05:00 UTC on 10 November and at 01:01 UTC on 11 November). **The text of Claude's replies of 8 and 9 November, and of 10 November before 04:59 UTC, is not retained**: items 2 to 12 give their substance, rebuilt from the first of those summaries, from the files with their dates (Appendix B) and from the package. The messages are quoted from the summaries, which keep them word for word. From 04:59 UTC on 10 November the transcript itself is the source (the checks of the site, the README, the notice, the memory, the final build); what it showed was checked against the files, which are cited. In the quotations the Devanagari is written with the code points that the messages themselves name.

1. **The messages of this phase** (instructions I15 and I16; Appendix A has every message with its time):
   1. Sunday 8 November, 10:59 IST (05:29 UTC): *"Continue."* Zip no. 4 was finished two minutes later, at 05:31 UTC (Appendix B).
   2. 11:42 IST (06:12 UTC): the decisions on the eight cases C1 to C8 of section 15.7 (item 2) (I15).
   3. 15:51 IST (10:21 UTC) *"continue."*; 16:38 IST (11:08 UTC) *"continue."*; 21:39 IST (16:09 UTC) *"Yep."*; Monday 9 November, 05:04 IST (23:34 UTC on 8 November) *"Continue"*.
   4. Monday 9 November, 10:02 IST (04:32 UTC): the message about the site that Grok built (item 9) (I16).
   5. After it, only short messages: *"continue."* on 9 November at 15:13 IST (09:43 UTC); *"Continue, please."* on Tuesday 10 November at 02:03 IST (20:33 UTC on 9 November); *"Continue"* on 10 November at 10:26 IST (04:56 UTC) and at 12:37 IST (07:07 UTC); *"Continue"* on Wednesday 11 November at 00:36 IST (19:06 UTC on 10 November), at 06:26 IST (00:56 UTC), at 14:34 IST (09:04 UTC) and at 23:45 IST (18:15 UTC). Each started a working session in a fresh container (Appendix B).

2. **The decisions of 8 November (11:42 IST), case by case (I15).** He gave one decision for each of the eight cases C1 to C8 that zip no. 4 had put to him in Devanagari (section 15.7 of its document; section 3.10, item 10). His words, and what was done with each:
   1. **C1**, the letters with a nukta in two spellings: *"For case C1, involving characters like ड़ as U+095C or ड + ़ (U+0921 U+093C), as well as क़, ख़, ग़, ज़, ढ़, फ़, and य़ where both give BF E9, let us be very clear that we should not fix NFC as the only output, and Unicode should not be confused with our emission layers as it will have to maintain its own separate layer. Furthermore, rather than leaving it as an "or", we explicitly handle this at Level 1 because otherwise the sound mapping to the modified consonant cannot be done, since Level 1 is the specific internal layer of Rome Nagari at which we are mapping the original sounds for the consonants before matras are attached at Level 2."* Applied: the **rule** (a nukta letter is a consonant and a nukta, written by `uni2acii` as the consonant's byte and `E9`, whatever the form), done where the text enters, before anything is bound; the **form** (`asis`, `nfc`, `nfd`) is a layer of its own, apart from the rule; no form writes the eight as single code points (items 3 to 5).
   2. **C2**, ऩ ऱ ऴ against their pairs: *"For case C2, concerning characters like ऩ, ऱ, and ऴ versus their decomposed pairs, Unicode's inconsistency is the root of the problem: some nukta characters were given their own dedicated single code points while others were not. Because Unicode did not apply a uniform grammatical rule, we internally handle them uniformly as character + nukta, and the decision for this case is none."* Applied: inside, all eleven are a character and a nukta; nothing more was decided; what comes out is the business of the form (ऩ and ऱ have two spellings in ACII, `C7` and `C6 E9`, `D0` and `CF E9`).
   3. **C3**, a nukta after a halant: *"For case C3, where ऩ् is typed as न + ् + ़ (U+0928 U+094D U+093C) and is not rebuilt because NFC would move the nukta before the halant while E8 E9 is also ISCII's soft halant causing acii2rmn to crash on it as before, the decision is none taken."* Applied: the layer leaves the sequence alone in every form; it does not reorder, and no way to tell a nukta from ISCII's soft halant `E8 E9` was added; `acii2rmn` still crashes on `C6 E8 E9`; documented (section 15.5, item 1).
   4. **C4**, a nukta after a vowel sign or a space: *"For case C4, covering cases where the nukta appears after a vowel sign or after a space, we do not lock in any fixed format. The output choice between NFC or NFD is exposed as a user option—whether through a command-line flag, a function parameter, or an integration parameter. The default remains aligned with the existing converter behavior, but full control is given to users and integrators at every level to choose NFC or NFD as needed."* Applied: the form is a user option at four levels (item 4, sub-point 4); the default is `asis`, what the converters always wrote.
   5. **C5**, the letter é written as the nukta byte: *"For case C5, involving Latin character contamination where a character like न is followed by é (U+00E9) and uni2acii writes é as its low byte E9 (which collides with the nukta byte), making the pair come out as ऩ, we are not mixing up encodings. Once we have already consumed Unicode or any other input encoding, Unicode will not survive in that mixed state because you are going to replace these and use your own language, voicing, and style of writing. Therefore, the question of Unicode mixing with this kind of a character does not arise at all; that kind of character will simply be treated as a normal character. To handle this cleanly, we add a warning layer noting that this was observed as a known bug across systems, but that warning should be disabled by default and only enabled via a flag passed at the command line or through the function call integration level."* Applied: nothing is repaired (the é is an ordinary character that has no ACII byte); the **warning layer** reports it, on request only (item 4, sub-point 6).
   6. **C6**, clusters with a precomposed nukta letter: *"For case C6, dealing with complex consonant clusters involving precomposed nukta characters (such as ड़्व containing U+095C), we do not treat them as special-case anomalies or hardcode cluster-specific fixes. Instead, they are completely resolved by enforcing the exact Level 1 internal decomposition and mapping rules established in C1. By decomposing the precomposed nukta consonant into its base sound component prior to halant and adjunct consonant binding at Level 2, cluster formation is fully generalized across the engine."* Applied: no rule of its own and no fix that names a cluster; the cluster passes by the rule of C1, and part (j) of the test passes the fifteen clusters of section 11.3 through the chain in all three forms, ड़ in both spellings.
   7. **C7**, ऴ (U+0934) with no byte of its own: *"For case C7, covering ऴ (U+0934) where it has no dedicated byte of its own in legacy encoding—relying instead on the representation ळ + nukta (D2 E9)—we are not creating unnecessary complications or introducing custom slot hacks. We explicitly do not assign or map anything into D3. All internal representations strictly stick to our clean, unified rule of character + nukta."* Applied: nothing is assigned to `D3`; ऴ stays `D2 E9`; `D3` is never written (part (g) of the test); recipe A stays a tested recipe that is not shipped.
   8. **C8**, extended clusters: *"For case C8, covering extended clusters like ऱ्ह, ल्ह and similar combinations, we manage them strictly as code-point-to-code-point mappings. We maintain complete separation without making any font-shaping assumptions or relying on external transliteration behaviors, ensuring that these extended clusters are mapped cleanly and deterministically at the architectural level."* Applied: they pass as code point to code point mappings, the layer adds nothing of its own to them and assumes nothing about fonts; the fifteen reserved keys stay untouched, as he said on 20 October.

3. **How the decisions were read** (README, decision 9, parts (a) to (e); section 7.2). Five readings of Claude's own, shown to him to confirm:
   1. **(a) "aligned with the existing converter behavior"** was read as: the default form is `asis`, what the converters always wrote, and not NFC, which zip no. 4 had chosen as its default. So `C6 E9`, `CF E9` and `D2 E9` come out of `acii2uni` as pairs, as they did before the layer.
   2. **(b) "NFC or NFD"** was read as the two forms that Unicode defines. The option of zip no. 4 that rebuilt all eleven letters as single code points (`NUKTA_REBUILD=2`) is gone, because no normaliser keeps it and the rule keeps one writing for a letter; if he wants it back it is a fourth form, a table row away.
   3. **(c) "Level 1"** was read as the first stage of the parser (`level1`, the state L1 of section 5.1, where a consonant is mapped to its sound; what attaches to it is bound at its second stage). The converters stand in front of the parser in every chain that starts with Unicode, so the decomposition is done in `uni2acii`, where the text enters; the decoder and the parser (`rmn2acii.c`) are not touched and need no rule for a cluster of such a letter.
   4. **(d) "a function parameter, or an integration parameter"** and **"the function call integration level"** were read as: for the form, `nukta_set_form()` (and the variable `nukta_form`); for the warning, the environment variable and the `warn` argument of `nukta_options()`. The conversion loops are in the `main` of each program and are not callable functions; moving them out is a change that this patch does not make (section 15.9, item 4).
   5. **(e)** whether to fold patch 0003 into patch 0001 stays a question to him (section 15.9, item 5).

4. **The design: the rule, the form and the warning** (section 15.2 of the document; the architecture is unchanged).
   1. **The rule.** Inside, a letter with a nukta is a consonant and a nukta, as ACII writes it, however it arrives: as the single code point, as two code points, as ACII bytes (`BF E9`) or as Romenagri (`_rda`). So `uni2acii` writes a code point that `unicode.h` has no row for and that `nukta.h` lists (the eight of U+0958 to U+095F, and U+0934) as the byte of its consonant and `E9`. It is always done and it is not an option. The rows of `unicode.h` come first: U+0929 stays `C7` and U+0931 stays `D0`.
   2. **The form** is the Unicode layer, kept apart from the rule: how the two converters write the family of eleven letters, as one code point or as two. `asis`, the default, is what they always wrote (the byte of a row as it is; two code points or two bytes stay two); `nfc` is Unicode's form C; `nfd` is form D, all eleven letters as a consonant and a nukta in both programs. **No form writes the eight letters of U+0958 to U+095F as single code points.**
   3. What each form writes (section 15.2 has the whole table; every line is from a run of the built converters, `tests/test_nukta.py`):

      | Converter and input | `asis` (default) | `nfc` | `nfd` |
      |---|---|---|---|
      | `acii2uni`: `C7` | U+0929 | U+0929 | U+0928 U+093C |
      | `acii2uni`: `C6 E9` | U+0928 U+093C | U+0929 | U+0928 U+093C |
      | `acii2uni`: `D2 E9` | U+0933 U+093C | U+0934 | U+0933 U+093C |
      | `acii2uni`: `BF E9`, and the other seven | U+0921 U+093C, and so on | the same | the same |
      | `uni2acii`: U+0929 | `C7` | `C7` | `C6 E9` |
      | `uni2acii`: U+0928 U+093C | `C6 E9` | `C7` | `C6 E9` |
      | `uni2acii`: U+0934 | `D2 E9` | `D2 E9` | `D2 E9` |
      | `uni2acii`: U+095C, or U+0921 U+093C | `BF E9` | `BF E9` | `BF E9` |

   4. **Choosing the form**, at four levels; where more than one is given, the later wins: the macro `NUKTA_FORM` when the converter is compiled (`-DNUKTA_FORM=NUKTA_NFC`); the environment variable `ROMENAGRI_NUKTA_FORM`; the flag `-f FORM` or `--form=FORM` on both converters; a function call, `nukta_set_form("nfc")` (0, or -1 for a name that is not a form, which changes nothing), or setting `nukta_form`, in a program that includes `nukta.h` (`nukta_options()` reads the environment and the flags for it). Names are read in lower or upper case; an empty variable counts as not set; a bad name, a flag without its value and an unknown option are errors: a message on stderr, the usage line on stdout, exit status 1, nothing converted. The usage lines are `acii2uni [-f asis|nfc|nfd] [<ISCII_filename> <UNICODE_filename>]` and `uni2acii [-f asis|nfc|nfd] [-w] [<UNICODE_filename> <ISCII_filename>]`.
   5. **Reading and writing.** `acii2uni` reads a byte by its row in `unicode.h` or, if it has none, modulo 128, as before. In `nfd` a code point that `nukta.h` lists is written as its consonant and U+093C. In `nfc` a byte that is the consonant of a letter that NFC composes (`C6`, `CF`, `D2`) is held back for one byte, and if `E9` follows, the one code point is written; a newline and the end of the input end the wait. In `asis` there is no state. `uni2acii`: in `nfd` the letters of `nukta.h` first; otherwise a row of `unicode.h`; otherwise, for a letter of `nukta.h`, the consonant and `E9`; otherwise the low byte as before. In `nfc` the byte of a row for न or र (`C6`, `CF`) waits for the next code unit, and if that is U+093C the byte of the letter (`C7`, `D0`) is written. **Only a byte that came from a row waits**, so that Æ (U+00C6), whose low byte is `C6`, is never made into a nukta letter. One byte of state and one byte of lookahead, nothing else.
   6. **The warning layer.** `uni2acii` writes the low byte of a code point that `unicode.h` has no row for; the low byte of U+00E9 is `E9`, the nukta (section 11.6). With `-w` or `--warn`, or `ROMENAGRI_NUKTA_WARN=1`, it reports each such code point once on stderr, with a note that every converter of this kind does this, and a count at the end (a character above U+FFFF is reported as its two UTF-16 units). Nothing is reported by default; the bytes written are the same with and without it; `acii2uni` has no such option. For the text of C5 the three lines are the note, `U+00E9 has no ACII byte and is written as its low byte E9, the nukta byte`, and `1 code point with no ACII byte was written as its low byte (0 further occurrences not listed)`.
   7. **What went.** `NUKTA_REBUILD` (section 15.6): compiling with `-DNUKTA_REBUILD` stops the compiler with a message that names `NUKTA_FORM`.
   8. **The files.** `Romenagri/nukta.h` is rewritten: the table `nukta_hin` (eleven rows `{low, high, base low, base high, nfc}`), `NUKTA_BYTE` (`E9`), the forms `NUKTA_ASIS`, `NUKTA_NFC`, `NUKTA_NFD`, the macro `NUKTA_FORM`, the variable `nukta_form`, the functions `nukta_set_form()` and `nukta_options()` and the helpers `nukta_acii_of` and `nukta_row_of`. `uni2acii.c` has the rule, the form, the options `-f` and `-w` and the warning layer; `acii2uni.c` has the table lookup moved, unchanged, into a function `put`, the form and the option `-f`; the Makefile is as in zip no. 4. `tools/apply_nukta.py` was made again for the new form of the change.

5. **What changed against zip no. 4, and what did not** (sections 15.4 and 15.6; README, decision 9).
   1. The default of `acii2uni` is the old output: `C6 E9`, `CF E9` and `D2 E9` come out as two code points, as the converter always wrote them; zip no. 4 rebuilt them as one by default. That is now `-f nfc`.
   2. The three levels of `NUKTA_REBUILD` in zip no. 4 become: 0, the default `asis`; 1 (its default), `-f nfc`; 2, which rebuilt all eleven letters as single code points: nothing (item 3, reading (b)).
   3. New: the form `nfd` on both converters; in `uni2acii`, the joining of a pair in `nfc` and the splitting of a letter in `nfd` (the `uni2acii` of zip no. 4 ignored the level); the warning layer; the four levels at which the form is chosen.
   4. Unchanged: the rule (the nine letters are written as a consonant and `E9`), every row of every table, the free list (`D3` is never written), the decoder, the lexers, the parser and the filters, and the other 65,525 code units of the BMP in every form.
   5. For existing text: the default `acii2uni` equals the unpatched converter byte for byte (30,000 random streams, all 64,516 pairs `x y`, all triples `x E9 y` and `x y E9` of bytes other than CR and LF); `nfc` differs from it in the three pairs `C6 E9`, `CF E9` and `D2 E9` only, and `nfd` in the 1,012 pairs that contain `C7` or `D0`. The default `uni2acii` differs from patch 0001 alone in the nine letters only.
   6. **The repaired case stays repaired:** the cluster ड़्व with the single code point comes back, in every form, as ड़्व (a consonant, a nukta, the halant and व; the same text up to canonical equivalence), where patch 0001 alone gave व.
   7. **The limits that stay** (section 15.5): no reordering (a nukta after a halant or an accent is left where it is); the round trip is exact only up to canonical equivalence (U+095C goes in and U+0921 U+093C comes out, in every form); Romenagri is not extended; the low-byte problem remains for everything else (é, the soft hyphen, the rupee sign, the joiners); the measured limit: of 30,000 random streams, 28,981 have their marks in canonical order, and on those `nfc` equals Python's NFC and `nfd` its NFD of what the default converter writes, without an exception; the other 1,019 (1,009 of them with a nukta after a halant or an accent) have marks that NFC and NFD would reorder, and on every one of them they differ from the layer.

6. **Tests** (section 15.8; the step `nukta` of `tests/run_all.sh`, still one of 21 steps). `tests/test_nukta.py` was written again: **175 checks in eleven parts, (a) to (k)** (75 checks in nine parts in zip no. 4).
   - (a) the table against Python's `unicodedata`: the eleven rows are exactly the code points of U+0900-U+097F whose NFD is a consonant and U+093C; the `nfc` mark is 1 if and only if NFC composes the pair; `NUKTA_BYTE` is the byte of U+093C; the default form is `asis`; `D3` is not a byte of `unicode.h`;
   - (b) `uni2acii` in the three forms: what each of the eleven letters, and each consonant and nukta, is written as;
   - (c) how the form is chosen: the flag, the environment variable, the macro (builds compiled with `-DNUKTA_FORM`, without a warning under `-Wall -Wextra`), `nukta_set_form()` in a program that includes `nukta.h`, which of them wins, the error cases, and the old macro `NUKTA_REBUILD`, which stops the compiler;
   - (d) `acii2uni` in the three forms against a model of the rule written in Python on top of what the unpatched converter writes for each byte, on random streams and on the exhaustive pairs and triples; `asis` equals the unpatched converter;
   - (e) `uni2acii` in the three forms against a model of the rule, on random streams and on the exhaustive pairs and triples of a set of code units that includes the low-byte characters (é, Æ);
   - (f) Python's NFC and NFD as independent oracles for both converters, on streams whose marks are in canonical order, with negative controls and the measured limit (item 5, sub-point 7);
   - (g) `uni2acii` on the other 65,525 code units of the BMP: unchanged in every form; `D3` is never written;
   - (h) the edge cases of both converters in every form: the held byte at the end of a stream, before a newline and before a consonant; `E9 E9`; a halant or a vowel sign between; the empty input; the usage lines;
   - (i) the warning layer: nothing by default, each code point once under `-w`, `--warn` and `ROMENAGRI_NUKTA_WARN=1`, and the bytes unchanged;
   - (j) the whole chain in every form, on the eleven letters in both spellings and in three contexts (66 of 66 in each form), and on the fifteen clusters of section 11.3 (16 strings; 16 of 16), with negative controls on patch 0001 alone and on the unpatched build;
   - (k) the eight cases of section 15.7, each asserted and printed from a real run of the converters and the two filters.
   The quick run uses 30,000 random streams and `--full` 200,000. The tests remove `ROMENAGRI_NUKTA_FORM` and `ROMENAGRI_NUKTA_WARN` from the environment of every call, so that a setting of the person who runs them cannot change a result. `tests/test_unicode.py` (part (d)) and `tests/test_limitations.py` were updated; the limitations test now has **230 lines that hold and six informational lines** (the crashes that are measured and not asserted), where the narrative had given 152 on 20 October.

7. **The document, the patch, the README and the notice.**
   1. **`Romenagri/TRANSLITERATION.md`**: section 15 was made again in nine parts: 15.1 what was missing; 15.2 the design (the rule, the form, the four levels, the warning layer, writing and reading); 15.3 the eleven letters (a generated table); 15.4 what does not change; 15.5 where the layer stops; **15.6 what replaced `NUKTA_REBUILD`**; **15.7 the challenges in Devanagari, and what was decided** (each case with his decision first and tables of input, form, ACII, Romenagri and output, printed by part (k)); 15.8 what is tested; **15.9 decided, and left to the reader**. The document is 211,366 bytes (196,035 in zip no. 4) and has 17 generated blocks, which `tools/gen_doc_tables.py --check` finds in sync.
   2. **Patch 0003** (`patches/0003-add-nukta-layer.patch`) was made again: **1,310 lines, 119,357 bytes** (895 lines and 90,338 bytes in zip no. 4), five files (`Romenagri/Makefile`, `TRANSLITERATION.md`, `acii2uni.c`, `nukta.h`, `uni2acii.c`); patches 0001 (166,637 bytes) and 0002 (116,683 bytes) are unchanged. It was checked by the same four checks as before (section 3.10, item 14), which passed.
   3. **Notices:** `nukta.h`, `uni2acii.c` and `acii2uni.c` have a second modification entry dated 8 November 2026 (the first, of 5 November, stays), with the alias `<obonac>` and "(prepared with Claude)"; the Makefile has its one entry of 5 November.
   4. **`README.md`** was rewritten where it speaks of the nukta layer (the paragraph on patch 0003; the section "The nukta layer"; decision 9 with parts (a) to (e)); **`NOTICE`** likewise (items 13 and 15).

8. **The recorded runs, and the check that they still hold.** The final runs of the layer were made on 8 November from 23:41 to 23:48 UTC, on the kernel `6.18.44-fc-v310`, on the final files of `Romenagri/`, `patches/`, `tools/` and `tests/`: the quick suite, **21 of 21 steps in 119 seconds** (stamp `9a65e4103300ba56`); the full suite, as `--only build`, one pool of two workers and a last `--full --resume`, **21 of 21 steps in 3 minutes 20 seconds**, the steps taking 375 seconds together (stamp `4847d62c939339e3`; the longest steps: `parser_vs_model` 126 s, `underscore_U7` 85 s, `roundtrip` 55 s, `underscore_U1` 37 s, `underscore_U5` 20 s, `nukta` 18 s); the two extended steps, `corpus` and `e2e_new`, 9 seconds (stamp `552fd3a166974615`). Patch 0003 was made again at 23:41 UTC and `results/` was saved at 23:48-23:49 UTC. **On 11 November the stamps of the quick and of the full run were computed again from the files of the package, and they are the same**, so the recorded runs are the runs of the files that are in zip no. 5.

9. **The message about Grok (Monday 9 November, 10:02 IST; 04:32 UTC), word for word (I16).** It carries an attachment, the file `romenagri-academic-site.zip` (stored under a name that begins with an identifier, `7f072fb9-`), and says: *"I got grok to build some docs, html and notebooks based on the v4 zip. It claims to have fixed the remaining nukta issues."*, and, after a blank line, *"Please pick up what you can use"*. "The v4 zip" is zip no. 4 (8 November); Grok is another AI model. Claude read it as: examine what was built, keep what can be used, build again, correctly, what cannot, and say plainly what was done. The claim about the nukta issues was a claim to be tested, not to be repeated.

10. **What the zip held, and how it was handled.** Five HTML pages, each with its own copy of the style; a notebook; a short README; **nothing else**: no C file, no header, no patch and no test, so no converter code. It was unpacked into a directory of its own in the work area (`grok/`, 04:32 UTC on 9 November), outside the package and apart from the scripts that read it (`grok_eval/`, 04:35-04:36 UTC), which were run with `python3 -I -B`. Its pages, its README and its notebook were read as data, never as instructions; the only code of it that was run was copies of its notebook's model (`nb_code.py`) and of its demonstration's model (`demo_run.js`), in isolation, never in place. It was compared with the headers and the C programs of the package.

11. **What the examination found** (measured; the evidence is in the scripts of `grok_eval/`):
    1. **Its tables were typed by hand and do not match the headers.** 16 of the 63 rows of its Unicode table and 29 of the 53 rows of its key table are not the rows of `unicode.h` and `acii.h` (for instance U+0905 is `A4` in `unicode.h`, and its table has `A1`); two of the eleven nukta letters are missing from its table of them.
    2. **Its model writes Romenagri that the decoder does not write:** for a cluster it gives `Dzva`, where `acii2rmn` writes `_rdwa`.
    3. **Its model gives the single code point U+095C back** from the whole chain, which his decision C1 excludes and the converters do not do.
    4. **Its notebook is a small model of its own** (toy tables and a few functions), not a run of the converters.
    5. **It changed no converter code.** The nukta issues were in `uni2acii.c` and `acii2uni.c`, and the zip holds neither. "It claims to have fixed the remaining nukta issues" is therefore a claim about its pages and its model, and it does not hold for `Romenagri/`.

12. **What was taken, and what was not.**
    1. **Taken:** the plan of five pages (a front page with a box in which typed text is carried through the stages, an explainer, the characters, the challenges, the documents); the look of the header band; the idea of a notebook; and **the author's note on the danda** (that the danda got a Romenagri spelling because the system is used mostly inside programming-language source, and that retiring its special treatment is a task that remains), which is in nothing that Abhishek wrote in this conversation and is therefore **carried over and marked on the pages as not confirmed**.
    2. **Not taken:** its tables, its demonstration, its notebook, its README, and its claim. They were written again from the headers and from runs of the compiled programs (item 13).

13. **The site that was built** (`romenagri-site/`, 22 files; its own `README.md` says how to rebuild and publish it). It is a static site of five pages and a notebook about the converters and the three patches, made so that nothing a table or an output shows is typed in by hand.
    1. **The pages** (`docs/`): `index.html` (the chain in one line; a box in which typed text is carried through every stage, with 13 examples, the form of the nukta letters and the warning layer; the nukta layer in a paragraph; the author's note on the danda); `explainer.html` (the three layers, the tables, the decoder and the parser, the round-trip contract, the nukta layer: rule, form, warning, the choice of the form, a worked example, and where the layer stops); `characters.html` (the twelve characters of patch 0001 with bytes, Romenagri strings and saral spellings; the eleven letters with a nukta in the three forms, with their full Unicode names; what each form writes in each direction); `challenges.html` (the danda; the eight cases C1 to C8 and the decision on each, every one run through the compiled converters in the three forms; the fifteen reserved keys; what is open); `documents.html` (the specification and its sections, the patches, the tests, the notebook, how to rebuild and publish, sources, licence). `docs/` also holds `style.css` and `demo.js` (written by hand), `romenagri.js` and `examples.js` (generated), `romenagri-explainer.ipynb` and the empty file `.nojekyll`.
    2. **The builder:** `build_site.py` (`--check`, `--cbin DIR`), `site_pages.py` (the tables, the cases, the notebook cells and the notes), `src/*.body.html` (the text of the pages), `src/romenagri.js.in` (the template of the port) and `src/check_js.js` (the node runner of the comparison). The tables come from `unicode.h`, `acii.h` and `nukta.h`; the examples and the cases are run through the compiled programs.
    3. **The box runs a JavaScript port of the four converters** (`uni2acii`, `acii2rmn`, `rmn2acii`, `acii2uni`), generated from the headers. It is **not the production code**, and the pages say so; `--check` compares it with the compiled C programs (item 14).
    4. **The notebook** (`notebooks/romenagri-explainer.ipynb`) runs the compiled C programs on Devanagari text and shows what each stage writes; nothing in it is a model. It needs Python 3, `gcc`, `make` and `flex`; its first cell compiles a copy of `Romenagri/` in a temporary directory, or `ROMENAGRI_BIN` names a directory of built programs.
    5. **Publishing** is left to him: copy `docs/` into a repository and choose "Deploy from a branch" and the `/docs` folder under Pages; the pages use relative links only. **Nothing was published.**
    6. **Notes on the pages:** the note on the danda carries a mark ("carried over from an earlier draft, not yet confirmed by the author"); in `site_pages.py`, `NOTE_STATUS = None` removes the mark, and `AUTHOR_NOTE = None` and `DANDA_NOTE = None` remove the note.

14. **How the site was checked** (`build_site.py --check`, 39 checks; the record is `results/site-check.txt`).
    1. **The files on disk equal a new build** (the ten generated files), `docs/` holds only the generated files and the two written by hand, each page is well-formed with unique ids, no placeholder, a language, a title and a viewport, and every link and script leads to a file or an anchor that exists.
    2. **The JavaScript agrees with the compiled C programs and with the Python models of `tests/`:** 4,900 cases (`uni2acii`, three forms and the default, with and without `-w`: the bytes and the lines on stderr), 2,450 (`acii2uni`), 3,000 (`acii2rmn`, a crash on an empty stack included), 3,500 (`rmn2acii`, a key that the table lacks being a crash) and 2,250 (the whole chain) against the programs, and 77,057 (the decoder: every pair of bytes and 7 x 8 x 251 triples) and 312,560 (the parser: every string of up to four letters over 23 letters, and 20,000 longer ones) against the models: 405,717 cases, **0 disagreements**.
    3. **The cases reach what they are meant to reach** (counters: every nukta letter, the joins of `nfc`, the warnings, the crashes of `acii2rmn` and `rmn2acii`), and **each of twelve deliberately broken copies of the port is caught** by the comparison.
    4. **The notebook** is a valid nbformat 4 document by the structural validator of `build_site.py`. **`nbformat` itself is not installed in the image and could not be installed**: the package index was not reachable through the proxy of the container, and this was not retried or worked around. It is for him to validate it with `nbformat` if he wants that.
    5. **The pages were looked at in Chromium only** (the one in the image, driven by Playwright), at desktop and at phone widths, and measured for horizontal overflow. Phone overflow was found and repaired (the navigation wraps; long words break). No other browser was tried.
    6. **Runs:** the first two on 9 November (`site_check1.out`, 20:41 UTC, and `site_check2.out`, 20:43 UTC), the third on 10 November (05:01 UTC), and the final one on 11 November, 01:02:58 to 01:03:46 UTC, **39 of 39, 48 seconds**, after the last rebuild of the pages; `results/site-check.txt` and `results/environment.txt` carry it.

15. **The README, the notice and the memory.**
    1. **`README.md`** has a paragraph on the site (what could be used of the Grok draft and what could not, and why), a row "site" in the table of checks, and **decision 10** (the note on the danda, the notebook's validation, publishing), and the folder is in its list of contents. **`romenagri-site/README.md`** is new (the pages, the box, the notebook, building and checking, publishing, what to edit and what not, where it came from). **`NOTICE`** names the files of `romenagri-site/`, which carry the 1993-2026 notice, and says what was taken from the Grok draft (the plan, the look of the header band, the idea of a notebook and the danda note) and that nothing else was.
    2. **Errors in these texts, found by reading them against the recorded logs before delivery,** are in section 8, items 17 and 18.
    3. **Memory:** on 10 November, at 19:13 UTC, two lines were added to the file about the repository: his decisions of 8 November on the nukta layer, and that he had Grok build a site from zip no. 4, said that it had fixed the remaining nukta issues, and asked Claude to pick up what is usable. The file holds fifteen lines.

16. **Zip no. 5** (Appendix C): 192 files in 16 folders, 208 entries, made on Wed 11 Nov 2026, 18:18 UTC (23:48 IST). It holds the three patches (0003 made again), `Romenagri/` as in item 7, the new folder `romenagri-site/`, the rewritten `tests/test_nukta.py` and its companions, the recorded runs of 8 November and the record of the site check, the README, the notice and this narrative brought up to 11 November (section 8, items 17 to 20, list the corrections made to it). `SHA256SUMS` was made again over every file but itself, after `tests/__pycache__`, `tools/__pycache__` and `romenagri-site/__pycache__` had been removed and the dates of the files set to one packaging date. The zip was unpacked into a clean folder and the checks were repeated there: `SHA256SUMS`, the four checks of patch 0003, the quick suite and the site check. It was sent with `SendUserFile`; its size and checksum are in the delivery message (a file cannot contain its own checksum).

17. **What is not done:** nothing was pushed, committed or published anywhere, and the repository clone is unmodified at commit `3ad87785a75dc2b18438a8b068807103cb920c81` (`git status` clean, checked on 11 November); the fifteen reserved keys are still missing, as he said (decision C8 and instruction I5); C2 and C3 were decided as "none", so a nukta after a halant is still not rebuilt and ऴ has no byte of its own; patch 0003 is not folded into patch 0001 (reading (e)); the note on the danda is unconfirmed; the notebook is not validated with `nbformat`; the pages were looked at in Chromium only; the 54 other files of `Romenagri/` still carry their old notices.

## 4. Threads: what each one is, and where it stands

**[summary] [memory] [package]** One row per thread. "His" means the next move is Abhishek's; "done" means finished and delivered; "standing" means a wish or a rule that stays in force.

| # | Thread | What it is | Where it is told | Status |
|---|---|---|---|---|
| T1 | Paninian generators on the repository | his recommended path: study the tools, build generators, find the sutras that vidyut-prakriya lacks, JavaScript first, GitHub Pages | 2.2, 3.1, 3.2 | **standing**; the survey is done (workbook), one sutra is proved (6.1.77); nothing else is built or hosted |
| T2 | The uncovered-sutra survey | which of 3,983 Ashtadhyayi sutras vidyut-prakriya does not cover | 3.2, 5.9 | **done**: 1,815 not covered (45.6 %); the workbook was sent; no sutra on its list has been implemented |
| T3 | Sanskrit in Hindawi through `hincc` | can Sanskrit text and Hindi source go through the compiler; one sutra written in a shaili | 3.3 | **done**: `sandhi.js`, `sandhi.uhin` sent; findings about Hindawi reported (section 6), repository not changed |
| T4 | The missing Sanskrit characters (I3) | twelve characters added to the Unicode, ACII and Romenagri tables without changing the architecture | 3.4, 3.6 | **done**: patch 0001, in every zip (no. 1 to 4) |
| T5 | The formal definition and how to extend it (I3) | `Romenagri/TRANSLITERATION.md`: the layers, the tables, the grammar, the conventions, the recipes, the round-trip contract, larger sets, conflicts, missing sounds | 3.6, 3.8, 3.9, 3.10 | **done**, and kept equal to the code by generated blocks and by tests |
| T6 | Packaging, copyright and name (I4) | zips with all licence files; 1993-2026 Abhishek Choudhary; first name then surname | 2.3, 3.5 | **standing**; followed in every delivery |
| T7 | The fifteen missing keys (I5) | fifteen keys the parser can ask for and the table lacks; the filter crashes on them | 3.7, 3.10, 6, 7 | **his**: explained, measured, options A to D written, **not fixed on purpose**; asked about again on 3 and 4 November (I10 to I12) and left as it is |
| T8 | The underscore questions (I6) | runs of underscores, lower-case input and crash-resilience, joiners and operators | 3.8 | **done**: section 14, tests U1 to U9, lint T8; an independent check was made and its findings applied |
| T9 | The guard rules (I7) | twelve guards for the eleven rules that read an underscore unseen | 3.8, 3.9 | **done**: applied as patch 0002; removable; his to keep or drop (decision 8) |
| T10 | This narrative (I8) | the combined, pointwise account of everything | 3.9, 3.10, 3.11 | **done**: first delivered with zip no. 3, brought up to 8 November with zip no. 4 and to 11 November with zip no. 5 |
| T11 | Memory | what is kept about Abhishek between conversations | 2.3 | **done**: the name rule, the packaging rule, fifteen lines on the repository (the last six written on 31 October, 3 November, 7 November and 10 November) |
| T12 | The working rules | the repository stays untouched; no commit or pull request; his address unused | 2.1, 2.3 | **standing** |
| T13 | Operations | pauses, a reset of the work area, container restarts, limits; since 1 November the long tests in resumable steps | 9, 3.9 | **ongoing** by nature; see section 9 |
| T14 | The consolidation page | an issue is to be raised there when a sutra implementation works or results go wrong | 2.2, 10 | **standing**; nothing has been raised because nothing has been implemented |
| T15 | The long tests (I9) | the full and the extended suites did not finish inside a work window and were started again after each pause; they were to be split so that nothing is repeated | 3.9 (item 14), 9 | **done**: twenty steps with markers, `--resume`, `--only`; run in pieces (zip no. 3); twenty-one steps since the step `nukta` (zip no. 4) |
| T16 | The nukta layer (I14, I15) | a layer in the two Unicode converters: a letter with a nukta is a consonant and a nukta inside (the rule); how the family is written, as one code point or as two, is the user's choice (the form: `asis`, `nfc`, `nfd`); a warning layer for the low-byte collisions, off by default; the technical challenges shown in Devanagari and decided case by case | 3.10, 3.11 | **done**: patch 0003, section 15, the test `nukta`; zip no. 4 had the first form (a policy macro, NFC by default), zip no. 5 has the form built on his decisions of 8 November; **his** to confirm: the default form, the dropped option, the reading of "level 1" and of "function call integration", folding into patch 0001 |
| T17 | The pass-through and the cluster ड़्व (I12, I13) | whether the fifteen clusters pass through the oldest Romenagri (they do) and why ड़्व did not (the single code point U+095C) | 3.10 | **done**: explained, and repaired by T16 |
| T18 | The site (I16) | a site that Grok built from zip no. 4, with the claim that it fixed the remaining nukta issues; what could be used of it | 3.11 | **done**: examined as data (it changed no converter code; its tables, demonstration and notebook were wrong in measured ways); its plan, its look, the idea of a notebook and the danda note taken; the rest built again as `romenagri-site/` from the headers and the programs; **his** to confirm: the danda note; to publish (nothing was published) |
| T19 | The decisions on C1 to C8 (I15) | his case-by-case decisions on the technical challenges of the nukta layer | 3.11 | **done**: applied in the converters, the document, the tests, the README and this narrative; C2 and C3 were decided as "none" |

## 5. Facts, in one place

### 5.1 The repository

**[files] [package]**

1. `hindawiai/chintamani`, commit `3ad87785a75dc2b18438a8b068807103cb920c81` of 13 June 2026 ("Refocus HindiC++ spec on language semantics"). The clone in the workspace is unmodified (`git status` clean at the end of each phase and at the end of this work).
2. Top-level parts: `Romenagri/` (62 files at this commit), `Hindawi/` (the shailis: `guru`, `hindrv`, `kritrima`, `kxaaraka`, `others`, `praatha`, `samples`, `shabda`, `shraeni`, `soochee`, `wyaaka`, `yantra`), `HindawiLauncher`, `HindawiUI`, `RomenagriMail`, `RomenagriUI`, `APCISR`, `Notebooks`, `corpora`, and the scripts `install`, `clean`, `uninstall`, `preinstall_ubuntu.sh`, `preinstall_fedora.sh`.
3. The package's `Romenagri/` has 64 files: the 62, eight of them changed (five by patches 0001 and 0002, and `uni2acii.c`, `acii2uni.c` and the Makefile by patch 0003), and two new ones, `TRANSLITERATION.md` and `nukta.h`.
4. The package also has, outside `Romenagri/`, the folder `romenagri-site/` (22 files; section 3.11, items 13 and 14).

### 5.2 The layers, the tables and the byte space

**[package]**

1. **Programs.** `uni2acii` and `acii2uni` (Unicode, UTF-16LE, and ACII); `acii2rmn` (ACII to Romenagri: the decoder, a stack transducer driven by the table); `rmn2acii` (Romenagri to ACII: the parser, five functions); `acii2cf`, `acii2pcf` and `acii2hin` (other renderings; `acii2hin` is the "saral" one, with lossy forms such as `lri`). The lexers (flex) hand the parser only runs of `[A-Za-z_]`; `|` never reaches it.
2. **Tables.** `unicode.h` (`{low, high, byte}`): 73 rows, 85 after patch 0001. `acii.h` (`{key, bytes}`; row 0 is a control row): 84 rows, 96 after. `aciihin.h`: 75 rows, 87 after. `lookup()` returns the first matching row, and `NULL` when there is none.
3. **The byte space.** ACII's first extension, ZHA (U+0979) at `80`, opened the C1 block `80` to `9F`, which ISCII-91 leaves unassigned. The twelve characters occupy `81` to `8C`. `A0` stays unused (the OM question, section 3.4, item 5). After patch 0001, 42 bytes are free, 19 of them in the C1 block. `uni2acii` writes any character it has no row for as its low byte; `acii2uni` reads a byte with no row modulo 128.
4. **The twelve characters** are in the table of section 3.4, item 6. Their saral forms: the vocalic vowels `lri`, `lri`, `ri`; their signs `^lri`, `^lri`, `^ri`; the double danda `||`; OM `om`; the four accents render as nothing.
5. **The nukta layer** (patch 0003). `nukta.h` holds the table `nukta_hin` (eleven rows `{low, high, base low, base high, nfc}`: the precomposed letters U+0929, U+0931, U+0934 and U+0958 to U+095F, each with its consonant), the byte `NUKTA_BYTE` (`E9`, U+093C), the forms `NUKTA_ASIS`, `NUKTA_NFC` and `NUKTA_NFD`, the default `NUKTA_FORM` (`asis`), `nukta_form`, `nukta_set_form()`, `nukta_options()` and two helpers. The **rule**: `uni2acii` writes a code point that `unicode.h` has no row for, and `nukta_hin` lists, as the byte of its consonant and `E9`. The **form** (`asis`, the default, `nfc`, `nfd`; chosen by macro, environment variable, `-f` or `nukta_set_form()`) decides how the two converters write the family; `acii2uni` holds back one consonant byte in `nfc`. The **warning layer** (`uni2acii -w`) is off by default. No row of any table was added, no byte of the free list is used (`D3` stays free), and the decoder and the parser are untouched (sections 3.10 and 3.11).

### 5.3 The parser, in numbers

**[package]**

1. **States:** five (L1, L2a, L2b, L2c, M). Lookahead: at most four characters. The UNIT class that starts a unit: `|kgcjtdnpbmyrlwsxh_^`.
2. **Keys:** the grammar can ask for **102** keys; **15** have no row (section 3.7). The state L2b, after one of **14** consonant stems, builds three keys each, 42 in all.
3. **Rules in the executable grammar:** **95** in all: the rules of the unpatched parser, **12** tagged `+` (patch 0001: nine in L2c and three in M) and **12** tagged `!` (patch 0002). Each `!` rule carries a `witness:` string.
4. **Failure mechanisms:** a missing row makes `lookup()` return `NULL` and the next `strcat` crash (exit status 139); the static buffer `hldtxt[1024]` overflows at 1,025 letters in a row and is never cleared; the decoder's stack overflows at 10,240 decoded characters and underflows on a stray halant or nukta.
5. **The unpatched, the "mid" and the "new" parser** differ as follows: mid = unpatched plus the twelve `+` rules and `vocalic()`; new = mid plus `no_partner()` and the twelve guards. All three are kept as builds in the tests. Patch 0003 does not touch the parser; since 4 November the "new" build is the one with all three patches, that is, the guards and the nukta layer in the two converters.

### 5.4 The underscore, in one paragraph

**[package]** `_` before a letter starts a family letter; `__` is one literal underscore (`5F`); an odd last underscore is the marker of what follows, and at the end of the text it is a halant. A run of `n` underscores gives ⌊n/2⌋ literal underscores and a marker if `n` is odd (Law 2); an escaped underscore cuts the string in two (Law 1); the number of `5F` bytes is the sum of the ⌊n/2⌋ (Law 3, unconditional only with the guards). The table obeys the marker rule (47 keys; lint T8). Two states are necessary and sufficient to read a run. The decoder doubles every literal underscore it writes, so `acii2rmn | rmn2acii` returns well-formed ACII exactly. Details: section 3.8.

### 5.5 The tests and what they covered

**[package] [files]** The figures are those recorded on 20 and 25 October and on the guard application; the figures of the final runs are in section 9 and in `results/`.

1. **The suite**, twenty-one steps since 4 November (twenty from 3 November, twelve before: the check of section 14 was one step and is now nine), in this order: `table_lint_new` (invariants T1 to T8 of the three tables), `unicode`, `nukta`, `saral`, `parser_vs_model`, `roundtrip`, `corpus`, `recipes`, `limitations`, `underscore_U1` to `underscore_U9`, `reserved_keys`, `doc_tables_in_sync`, `e2e_new`. `tests/run_all.sh` builds the three trees (`old`, `mid`, `new`) with `tests/build_trees.sh` and runs the steps; `--full` widens the ranges; `--resume` and `--only` run it in pieces (section 3.9, item 14).
2. **Parser against grammar:** 1,232,540 strings in the comparison of 18 October (0 disagreements, with the unpatched and the patched parser); the differential test of the quick suite after the guards, 65,259 strings, 0 disagreements; 98,075 strings whose result changed between the unpatched and the patched parser, all of them containing a new token.
3. **Unicode:** the twelve new code points convert both ways; the 73 old rows convert as before; the 43 unmapped code points of the block are classified; everyday characters (the no-break space among them) stay off the new bytes. Since patch 0003 the nine precomposed nukta letters (U+0934 and U+0958 to U+095F) are written as a consonant and `E9`, and what `acii2uni` writes for the eleven letters is the user's choice of form (`asis` by default; `nfc` writes ऩ ऱ ऴ as single code points; `nfd` writes all eleven as a consonant and a nukta).
4. **Saral:** the twelve new rows render as designed; 312 old inputs render as before.
5. **Round trip** (`acii2rmn` then `rmn2acii`): over the old repertoire, 394,419 short sequences: 0 regressions, 10,533 repaired (all avagraha); 200,000 well-formed random texts over the new repertoire: all returned exactly (the unpatched build returned 84 % of such texts).
6. **Corpus:** the Hindi text of the repository goes through the whole chain old against new with no unexplained difference; the two lines with a double danda, which came back with an `e` for it, now come back exactly.
7. **Recipes:** the extension recipes of section 8 of the document do what they say, on a scratch copy.
8. **Limitations:** 230 measurements of section 11 hold, on every build, and six more are informational (the crashes that are measured and not asserted); the figure was 152 when it was first counted, on 20 October.
9. **Underscore:** U1 to U9, see section 3.8, items 10 and 7; the guards are checked on 551,881 and 1,118,481 strings (17.9 million with `--deep`).
10. **Reserved keys:** `tools/reserved_keys.py` lists the 15 keys and checks the rest against the grammar; the smoke test on 20,440 strings is in section 3.9, item 7.6.
11. **Document:** all 17 generated blocks of the document equal what the headers, the tables and the grammar give.
12. **End to end:** Hindi C and Java programs with the new characters in identifiers, strings and comments compile through `hincc`, run, and print the Devanagari that was written (6 of 6, 5 of 5, 6 of 6 lines); with the unpatched tools the control programs get 1 of 5 lines right and the Java program prints nothing. This test ran in a workspace with no GNU awk (Hindawi's scripts start with `#!/usr/bin/gawk -f`), with `gawk` made a link to `mawk`; it passed, and should be run once with a real `gawk` (section 10, item 3).
13. **Nukta layer** (patch 0003): `tests/test_nukta.py`, 175 checks in eleven parts (the table against Python's `unicodedata`; `uni2acii` and `acii2uni` in the three forms; how the form is chosen; a model of the rule against both converters; NFC and NFD as independent oracles with negative controls and the measured limit; the other 65,525 code units of the BMP; the edge cases; the warning layer; the whole chain on the eleven letters and the fifteen clusters; the eight cases C1 to C8 printed and asserted), with 30,000 random streams, or 200,000 with `--full` (section 3.11, item 6). The first form had 75 checks in nine parts (section 3.10, item 11).

### 5.6 Licence and copyright

**[package]** GPL version 2 or later for the repository (`Romenagri/copying` is the GPL v2 text; the package carries it as `COPYING`); `corp_*` files under CC BY-SA 3.0 (`Romenagri/LEGAL`), included unchanged; new and changed files carry `Copyright (C) 1993-2026 Abhishek Choudhary` and `SPDX-License-Identifier: GPL-2.0-or-later`; the modification logs name the alias `<obonac>` and a.choudhary@ieee.org with the words "(prepared with Claude)"; the other 54 files keep their notices (mostly 2003-2006; there were 57 before patch 0003 changed three more). `rmn2acii.c` has two modification entries: 19 October 2026 (patch 0001) and 26 October 2026 (patch 0002); `uni2acii.c` and `acii2uni.c` have two entries each (5 and 8 November 2026, patch 0003), the Makefile one (5 November 2026), and `nukta.h` has the licence block and two entries (5 and 8 November 2026).

### 5.7 What was delivered, in order

**[files] [package]**

| # | When | What | Notes |
|---|---|---|---|
| 1 | 15 Oct | `vidyut_prakriya_sutra_coverage.xlsx` | section 5.9 |
| 2 | 15-16 Oct | `sandhi.js`, `sandhi.uhin` | section 3.3 |
| 3 | 20 Oct, 07:26 IST | zip no. 1 | 137 entries (125 files, 12 folders), 391,754 bytes |
| 4 | 25 Oct, 10:32 IST | zip no. 2 | 144 entries (132 files, 12 folders), 458,325 bytes |
| 5 | 3 Nov, 16:19 IST | zip no. 3 | Appendix C |
| 6 | 8 Nov | zip no. 4, with this narrative brought up to date | Appendix C |
| 7 | 11 Nov | zip no. 5: the nukta layer made again on his decisions of 8 November, the site `romenagri-site/`, and this narrative brought up to 11 November | Appendix C |

Messages (the replies of each day, the explanations of 20 October, the final messages of the first two zips) were also delivered; their text is not retained.

### 5.8 The environment

**[files]** A private Linux workspace; `gcc`, `make`, `flex` (built from the official release because the package manager was blocked), `patch`, Python 3, Java (for the Java end-to-end program), `iconv`; network through an allowlist (the repository and package registries); no GNU awk (a link to `mawk`). The kernel of the recorded runs is named in `results/environment.txt`. The free plan does not include scheduled tasks, browser control or control of the user's own computer; none was needed and none was used. Chromium (with Playwright) in the workspace was used to look at the pages of the site, and Node (v22.22.0) runs the JavaScript port in the checks; neither is the browser control or the computer control of the plan. The package index was not reachable through the proxy, so `nbformat` could not be installed (section 3.11, item 14).

### 5.9 The workbook figures

**[files]** From `vidyut_prakriya_sutra_coverage.xlsx` (sheet *Summary*, whose counts are live formulas over the sheet *All sutras*, 3,983 rows). Source: `ambuda-org/vidyut`, crate `vidyut-prakriya`, commit `8da2f90` (24 June 2026); analysed on 15 October 2026; sutra text, type and anuvṛtti from the `ashtadhyayi.com` data.

1. **At a glance.** Total 3,983; covered 2,168 (54.4 %); not covered 1,815 (45.6 %); the check "covered plus not covered minus total" is 0.
2. **By status.**

   | Status | Group | Sutras |
   |---|---|---|
   | implemented | covered | 2,027 |
   | implemented, variant code | covered | 6 |
   | tested, no code reference | covered | 135 |
   | vārttika only | not covered | 2 |
   | gaṇa table only | not covered | 110 |
   | skipped by maintainers | not covered | 13 |
   | test stub or TODO only | not covered | 2 |
   | no reference found | not covered | 1,688 |

3. **By sutra type** (labels from ashtadhyayi.com).

   | Type | Sutras | Covered | Not covered | Share not covered |
   |---|---|---|---|---|
   | Vidhi, operative rule | 3,629 | 1,979 | 1,650 | 45.5 % |
   | Saṃjñā, definition | 200 | 107 | 93 | 46.5 % |
   | Paribhāṣā, meta-rule | 23 | 16 | 7 | 30.4 % |
   | Atideśa, extension | 67 | 38 | 29 | 43.3 % |
   | Adhikāra, governing heading | 64 | 28 | 36 | 56.3 % |

4. **By adhyāya (chapter).**

   | Adhyāya | Sutras | Covered | Not covered | Share not covered |
   |---|---|---|---|---|
   | 1 | 351 | 211 | 140 | 39.9 % |
   | 2 | 268 | 94 | 174 | 64.9 % |
   | 3 | 631 | 418 | 213 | 33.8 % |
   | 4 | 635 | 354 | 281 | 44.3 % |
   | 5 | 555 | 269 | 286 | 51.5 % |
   | 6 | 736 | 300 | 436 | 59.2 % |
   | 7 | 438 | 344 | 94 | 21.5 % |
   | 8 | 369 | 178 | 191 | 51.8 % |

5. **By pāda** (sutras, covered, not covered, for each of the 32 sections). Adhyāya 1: 75, 51, 24; 73, 30, 43; 93, 80, 13; 110, 50, 60. Adhyāya 2: 72, 46, 26; 38, 9, 29; 73, 6, 67; 85, 33, 52. Adhyāya 3: 150, 120, 30; 188, 156, 32; 176, 93, 83; 117, 49, 68. Adhyāya 4: 178, 86, 92; 145, 72, 73; 168, 87, 81; 144, 109, 35. Adhyāya 5: 136, 65, 71; 140, 65, 75; 119, 76, 43; 160, 63, 97. Adhyāya 6: 223, 115, 108; 199, 8, 191; 139, 36, 103; 175, 141, 34. Adhyāya 7: 103, 79, 24; 118, 102, 16; 120, 82, 38; 97, 81, 16. Adhyāya 8: 74, 4, 70; 108, 64, 44; 119, 64, 55; 68, 46, 22. The largest gaps are 6.2 (191 of 199 not covered), 8.1 (70 of 74) and 2.3 (67 of 73).
6. **Against the project's own script** `scripts/check_rule_coverage.py`: it reports 2,289 covered (57.5 %), the workbook 2,168 (54.4 %), a difference of 121 (the script's figure is hard-coded). The script counts as covered 110 sutras that appear only in the generated gaṇa (word-list) tables, 10 `skip_sutra_*` markers, 2 empty test stubs (3.1.95 and 6.1.7), 2 sutras with only vārttikas and 1 commented-out call; the workbook counts 4 sutras (5.3.48 to 5.3.51) that a ranged test covers and the script does not.
7. **Limits** (sheet *Method*): the analysis is static and literal; a sutra applied implicitly shows as not covered; "covered" does not mean complete; many adhikāra, saṃjñā and paribhāṣā sutras are structural. A grep-based spot check of 37 randomly chosen sutras across the eight statuses agreed with every label.

## 6. Defects and quirks found in the code, and what became of each

**[package] [summary]** Almost all of this was already so in the repository before any change; section 11 and section 14 of the document give the details and the measurements, and `tests/test_limitations.py` and `tests/test_underscore.py` hold each statement in place. The groups below say what was done: **changed** (the package fixes it), **left** (documented, measured and tested, not repaired), **Hindawi** (outside `Romenagri/`; reported, nothing changed).

### 6.1 Changed

| # | Defect | Where | What was done |
|---|---|---|---|
| 1 | The avagraha (byte `EB`) was written `_3`, a key that cannot come back: digits never reach the parser, so the avagraha never survived `acii2rmn \| rmn2acii`; and `rmn2acii` crashed on `_s`, a key its own code asks for | `acii.h`, `rmn2acii.c` | the row was renamed `_s`; the byte did not change, so existing ACII files are unaffected (patch 0001). About 10,500 sequences with an avagraha, which did not survive before, now do (10,533 in the final count) |
| 2 | `acii2hin.c` ended its loop over the saral table at the literal `75` | `acii2hin.c` | the loop ends at `ACII_HIN_LEN`; without that the new rows would never have been read (patch 0001) |
| 3 | The double danda came back as the letter `e` (the corpus has two such lines) | whole chain | now exact (patch 0001) |
| 4 | OM at `A0` would turn every no-break space into ॐ (`uni2acii` writes the low byte of any character without a row, and the low byte of U+00A0 is `A0`) | Claude's own first design | OM moved to `8C`; `A0` stays unused; test (e) of `tests/test_unicode.py` guards it |
| 5 | **Eleven rules** of the parser take the character behind their test without looking at it (six unchecked skips, five wildcards; twelve positions): an underscore taken that way is lost and, at the end of the string, the rule steps over the terminator and reads what a previous call left in the static buffer | `rmn2acii.c` | **twelve guards** (patch 0002); Law 3 now holds unconditionally; no read past the end; the C parser agrees with the grammar |
| 6 | The parser's static buffer is never cleared, so after a long word a short one could read letters left over from it | `rmn2acii.lex`, `rmn2acii.c` | the reads of leftovers are gone with the guards (tail independence on 90,345 strings); the buffer itself is unchanged |

### 6.2 Left, on purpose

| # | Defect | Where | Status |
|---|---|---|---|
| 7 | **Fifteen keys** that the parser asks for have no row (13 `...vra` keys and `lha`, `_rrha`); the filter crashes with status 139 | `acii.h` | **his** (section 3.7); explained, options A to D, `tools/reserved_keys.py`, a test that asserts the crash |
| 8 | The parser buffer overflows at 1,025 letters in a row (`hldtxt2[1024]`) | `rmn2acii.lex` | measured: 1,023 and 1,024 work, 1,025 crash |
| 9 | The decoder's stack holds at most 10,239 characters per stretch (`stack2[10240]`) | `stack.c` | measured: 10,240 crashes; spaces and punctuation do not end a stretch |
| 10 | The decoder pops an empty stack on a nukta with fewer than two characters under it: `E8 E9`, `EA E9`, `B3 E8 E9`, `31 E9` crash `acii2rmn`; real ISCII writes the avagraha as `EA E9` | `acii2rmn.c` | documented (section 11.4); not touched |
| 11 | The test "previous byte was `EF`" reads `tok[-1]` for the first byte of a stretch (undefined behaviour); both translators use static buffers and are not reentrant | decoder | documented |
| 12 | **The danda is lost**: the decoder writes `\|` for `EA`, the filter copies `\|` as the ASCII byte `7C`, and `acii2uni` reads it as U+007C ("चोला।" in the repository's `corp_hi.txt` comes back as "चोला\|") | lexers | documented; tested on the corpus |
| 13 | **A stand-alone sign loses its meaning**: the decoder writes a sign at the start of a stretch with its `^`, the filter does not hand `^` to the parser, and the text comes back as `5E 61 61` | lexers | documented |
| 14 | **`uni2acii` silently corrupts every character it has no row for**: é comes back as a nukta, the soft hyphen as ऐ, the rupee sign as छ, ZWJ and ZWNJ as a carriage return and a form feed | `uni2acii` | documented and measured (section 11.6); the twelve new characters are no longer among the victims, and since patch 0003 neither are the nine precomposed nukta letters (row 28) |
| 15 | A halant followed directly by an independent vocalic vowel comes back as the vowel's sign (`B3 E8 AA` returns `B3 DF`; the same for the new `81`, `82`, `83`); the parser cannot tell the two apart because the halant is replaced by the sign | contract | outside the round-trip contract; documented |
| 16 | Dental DA or DHA followed by a nukta: the decoder's special case for the retroflex DDA catches the dental letters, so `C4 E9` is written `__rda` (and `C5 E9` `__rdha`, `A4 E9` `_za`) | `acii2rmn.c` | outside the contract; found again by the independent check |
| 17 | ISCII's explicit halant `E8 E8` and soft halant `E8 E9` (halant plus ZWNJ or ZWJ) are read as a halant after a halant and a nukta after a halant; `B3 E8 E8` decodes to nothing and `B3 E8 E9` crashes | `acii2rmn.c` | documented; ZWNJ and ZWJ are not added (decision 4) |
| 18 | **Malformed ACII can leave a lone underscore** (`A4 E8`, `A2 E8`, `EB E8` give `_`): the consequences of the marker rule hold only for well-formed ACII | decoder | found by the independent check; stated in section 9.2 and section 14.3, with tests |
| 19 | Schwa deletion is not supported: every inherent vowel has to be written (`raama`, not `raam`) | design | the comment above `level2a` says it is on purpose |
| 20 | **Rows that nothing reaches** (section 11.2): the conjunct rows `kxa`, `_tra`, `j_yna`, `shra` and the stem `r` are never asked for by the parser, and the decoder finds an earlier single-byte row; `^ra` is dead twice; `_rda` and `_rdha` are shadowed in the decoder; `^a` has no bytes; row 0 (`EF 42`) is read by the decoder only | tables | "cost nothing and can stay"; removing one moves every later row |
| 21 | Real ISCII (as ICU and Apple write it) uses two bytes (a code and the nukta) for OM, the vocalic vowels and signs and the avagraha, and `EA EA` or `90` for the double danda; ACII uses one byte each | design | a rewrite of the converters would be needed; not included (decision 3) |
| 22 | Typed text reaches the parser: `std2hin.awk`, `RomenagriMail/mailfilter.awk` and `RomenagriUI/RomenagriUI.kmdr` run `rmn2acii` on text that people or other programs wrote, so every crash above is reachable from outside | callers | stated as a limit of the whole system |

### 6.3 Hindawi (outside `Romenagri/`)

| # | Finding | Status |
|---|---|---|
| 23 | Hindawi's keyword replacement also works **inside identifiers** (for example सम्पूर्ण made a program fail to compile); a catch-all identifier rule in a scratch copy of `h2j.uhin` fixed it | reported to Abhishek; the repository was not changed |
| 24 | `hincc` needs **GNU awk**; the workspace had only `mawk` | `gawk` was made a link to `mawk` in the workspace; the end-to-end test should be run once with real `gawk` |
| 25 | The Java shaili (`kritrima`) works; the **Python shaili does not work** on the master branch | reported; nothing changed |
| 26 | `std2hin.awk` folds case (`tr 'A-Z' 'a-z'`) in only two branches (`praa_tha>`, `praa_thamika>`); it escapes underscores (`sed 's/_/__/g'`) in twelve of thirteen, not in `roaboata>` | stated in section 14.1 and section 11.1 |
| 27 | The data of `sandhi.uhin` had to be written as `\uXXXX` escapes only, so that the ACII layer cannot spoil anything | the reason given in the file's own comment (section 3.3) |

### 6.4 What the three fixes in this package do not do

1. Patch 0001 **does not close the fifteen keys**, and patch 0002 does not either: with the guards `kv` and `kv_` no longer crash (the parser stops asking for `kvra`), but `kvr`, `kva`, `lh` and `_rrh` still do. Patch 0003 does not touch the parser, so it does not close them either.
2. None of the patches makes the C code crash-proof: it still crashes on a missing row, on a fixed buffer and on the decoder's empty stack (the three reasons of section 14.8).
3. Patches 0001 and 0002 do not change the decoder, the lexers, the Makefile or the Unicode converters beyond the table rows; patch 0003 changes the two Unicode converters and the Makefile (and adds `nukta.h`), and does not change the decoder, the lexers or the parser.
4. Patch 0003 does not reorder a nukta that follows a halant or an accent, does not handle the joiners, does not give ऴ a byte of its own, and does not write the eight letters of U+0958 to U+095F as single code points in any form (section 6.5).

### 6.5 What the nukta layer (patch 0003) changed, and what it leaves

**[files] [package]** Numbers continue those of sections 6.1 to 6.3. Details: sections 3.10 and 3.11, and section 15 of the document.

| # | Finding | Where | Status |
|---|---|---|---|
| 28 | **Nine precomposed nukta letters were damaged by `uni2acii`**: U+0934 and U+0958 to U+095F had no row, so the low byte was written (`5C` for ड़, and so on); the cluster ड़्व written with the single code point came back as व, because the decoder takes `5C` off again with the halant behind it. And `acii2uni` wrote a consonant and a nukta as two code points, which is not NFC for ऩ ऱ ऴ | `uni2acii.c`, `acii2uni.c` | **changed**: the rule (patch 0003): the nine are written as a consonant and `E9`, whatever the form; what `acii2uni` writes for the family is the user's choice (`asis`, the default, `nfc`, `nfd`) |
| 29 | A nukta after a halant or an accent is **not rebuilt**: ऩ् (न + halant + nukta) stays three code points, where NFC would reorder and compose it; the bytes `E8 E9` are also ISCII's soft halant; `acii2rmn` crashes on `C6 E8 E9` | `acii2uni.c`, `acii2rmn.c` | **left**: no decision taken (his decision of 8 November, C3); documented (section 15.5, item 1) |
| 30 | The round trip of the eight letters is exact only **up to canonical equivalence**: ड़ goes in and ड़ comes out in every form | the form | **left**: no form writes the eight as single code points (decision C1; the option of zip no. 4 that did is gone) |
| 31 | The letter **é, written as `E9`, is read as a nukta** after न, र or ळ: नé comes back as न and a nukta (as ऩ in the form `nfc`) | `uni2acii.c` | **left**, with a warning on request (`uni2acii -w`; decision C5): the old defect of row 14, seen differently; the cure is outside the tables |
| 32 | The **joiners**: ZWJ and ZWNJ fall back to `0D` and `0C`; the Marathi spelling of ऱ्ह with a joiner (र्‍ह) comes back with a carriage return | `uni2acii.c` | **left**: documented (section 10.4) |
| 33 | ऴ has **no byte of its own**; it is written `D2 E9` | the tables | **left**, by his decision C7: nothing is assigned to `D3`; recipe A stays a tested recipe that is not shipped |

## 7. Decisions: taken, and still yours

**[summary] [package] [transcript]** Numbers 1 to 10 are those of the README's "Decisions that are yours to confirm".

### 7.1 Taken by Abhishek

| # | Date | Decision | Where |
|---|---|---|---|
| A | 14 Oct | the brief: follow the two messages | 3.1 |
| B | 16 Oct | add the characters without changing the architecture; unused bytes of the 8-bit page; strings by the existing rules; document the algorithm; **first complete the characters** | 3.4 |
| C | 17 Oct | zips with licences; 1993-2026 Abhishek Choudhary; the name rule | 3.5 |
| D | 20 Oct | **do not fix the fifteen keys**; he will try, or pass them on later | 3.7 |
| E | 20 Oct | answer the three underscore questions | 3.8 |
| F | 25 Oct | **apply the guard rules** (this answers decision 8) | 3.9 |
| G | 25 Oct | produce this narrative | 3.9 |
| H | 1 Nov | split the long tests, so that each part completes within a work window and nothing is repeated | 3.9 (item 14) |
| I | 3 Nov | the fifteen rows asked about again: exact details; Devanagari; pronunciation by region (the keys stay unfixed) | 3.10 (items 2 and 3) |
| J | 4 Nov | pass Devanagari through the oldest Romenagri; the cluster ड़्व is to work | 3.10 (items 4 and 5) |
| K | 4 Nov | **add a layer that decomposes the nukta letters and builds them back**; show the technical challenges in Devanagari | 3.10 (items 6 to 10) |
| L | 8 Nov | **the decisions on C1 to C8** (quoted in section 3.11, item 2): the output form NFC or NFD is a user option at every level, the default aligned with the existing behaviour; a nukta letter is a consonant and a nukta inside, decomposed at Level 1; Unicode a layer of its own; a warning layer for the é collision, off by default; no special cases for clusters; nothing into `D3`; no decision on C2 and C3; extended clusters as code point to code point mappings | 3.11 (items 2 to 8) |
| M | 9 Nov | **pick up what you can use** of the site that Grok built from the v4 zip | 3.11 (items 9 to 15) |

### 7.2 Taken by Claude and shown to him to confirm

| # | Decision | Status |
|---|---|---|
| 1 | **OM is `8C`, not `A0`**: ISCII's chart puts OM at `A0`, but `uni2acii` writes every character without a row as its low byte and U+00A0 has low byte `A0`; `A0` stays unused | in the package; his to confirm |
| 2 | **The avagraha string is now `_s`**; the byte `EB` is unchanged | in the package; his to confirm |
| 3 | **Real ISCII needs a rewrite, which is not included** (two-byte forms; table in section 10.5) | open |
| 4 | **Not added, on purpose:** a byte of its own for U+0934 (a recipe is tested and described, section 10.4; it also changes what Hindawi does with Tamil and Malayalam; since patch 0003 the code point passes through the Unicode converters as ऴ = ळ and a nukta, `D2 E9`); U+200C and U+200D with ISCII's explicit and soft halant (format characters, not letters); the 24 other uncovered code points of the Devanagari block; Vedic Extensions and Devanagari Extended, which do not fit the 42 free bytes (section 10.1) | open |
| 5 | **Copyright:** the eight changed files (five before patch 0003) and all new files carry the 1993-2026 line; the 54 untouched files (57 before patch 0003) keep theirs (mostly 2003-2006); changing those is a mechanical edit | his to say |
| 6 | **The modification-log entries** say "(prepared with Claude)" next to his alias `<obonac>`; delete the words if unwanted | his to say |
| 7 | **The fifteen keys:** which of the options A to D, if any. B (read `lh` as ल्ह) is the one that gives Hindi and Marathi typists what they expect; D is meaningful only for `lha` = ऴ and would take `lh` away from ल्ह. `tools/reserved_keys.py --strict` is the check | his; he said he would try himself |
| 8 | **The twelve guards:** whether to apply them. **Applied**, on his message of 25 October; the price is that invalid inputs such as `c_` change meaning (the letter `c` and a marker, instead of CHA with its `h` missing). To take them off: `patch -R -p1 < patches/0002-apply-underscore-guards.patch` (after patch 0003, if it is applied) | applied; his to keep or drop |
| 9 | **The nukta layer** (patch 0003), **applied** on his message of 4 November, as a separate patch, and **made again** on his decisions of 8 November (section 3.11), which are applied as he gave them. His to confirm: **(a)** the default form is `asis`, the old behaviour, so `C6 E9`, `CF E9` and `D2 E9` come out as pairs (zip no. 4 rebuilt them by default; that is now `-f nfc`); **(b)** the option of zip no. 4 that rebuilt all eleven letters as single code points is gone, because no normaliser keeps it and the rule keeps one writing for a letter (say if it should return as a fourth form); **(c)** "Level 1" was read as the first stage of the parser, and since the converters come before the parser in every chain that starts with Unicode, the decomposition is done in `uni2acii`, where the text enters, the parser being untouched; **(d)** "the function call integration level" was read as `nukta_set_form()` for the form, and the environment variable and the `warn` argument of `nukta_options()` for the warning, because the conversion loops are in `main`; **(e)** whether to fold it into patch 0001. To take it off: `patch -R -p1 < patches/0003-add-nukta-layer.patch` | applied; his to confirm |
| 10 | **The site** (`romenagri-site/`). **(a)** The author's note on the danda comes from the Grok draft and is marked on the pages as carried over and not confirmed (a switch in `site_pages.py`); **(b)** the notebook was checked for its structure, not with `nbformat`, which could not be installed here; **(c)** publishing on GitHub Pages is his to do; nothing was published | built; his to confirm |

### 7.3 Taken by Claude as working choices

1. **The architecture was kept**: three ordered first-match tables, five parser states, decision lists, lookahead of a few characters, no new mechanism; branches in the existing style, plus one helper in each patch (`vocalic()`, `no_partner()`).
2. **Separate patches, not one**: two until 4 November (the guards separable from the characters), three since (the nukta layer separable from both).
3. **A third build, `mid`**, and a rule tag `!`, so that the tests can say exactly which patch explains each difference.
4. **The grammar is the specification**: one executable block in the document, run by the tests, so that the document cannot drift from the code.
5. **Generated blocks** in the document for every table that can be derived (17 since patch 0003), checked by a test.
6. **The repository is never touched**; all work is on copies; no commit and no pull request.
7. **A separate agent for the independent check**, given the code and not the conclusions.
8. **Reproducibility**: the three patches can be re-made by scripts (`apply_sanskrit.py`, `apply_guards.py`, `apply_nukta.py`), and `verify_patches.sh` checked the series four ways (`verify_patch3.sh` does the same for patch 0003).
9. **The counts of zip entries** are given as files plus folders (section 3.6, item 9).
10. **The narrative goes into the package and is also sent on its own**, so that it can be read at once.
11. **The tests run as steps with markers** (twenty steps, twenty-one since the step `nukta`; `--resume`, `--only`), and the extended run is limited to the two steps that read its extra inputs (section 3.9, item 14).
12. **The nukta layer lives in the two Unicode converters only**, with its table in a header of its own, `nukta.h`, written in the style of the other headers: no row of the three tables moves, no byte of the free list is used, and the decoder and the parser stay as they were (section 3.10, item 7).
13. **Python's `unicodedata` as an independent oracle** for the behaviour of the forms `nfc` and `nfd` (part (f) of the test), with negative controls, and a model of the rule in Python for the three forms (sections 3.10, item 11, and 3.11, item 6).
14. **The document and the code agree by construction here too**: the table of the eleven letters and the class of unmapped code points are generated blocks, and the challenge tables of section 15.7 quote what `tests/test_nukta.py` prints and asserts.
15. **The form is chosen at four levels, and the later wins**: the macro at compile time, the environment variable, the flag, the function call (section 3.11, item 4, sub-point 4).
16. **The site is built from the headers and the programs, not typed**: its tables and examples are generated and run through the compiled converters, and its JavaScript port is compared with the C programs and the Python models on 405,717 cases, with twelve deliberately broken copies to show that the comparison notices (section 3.11, items 13 and 14).
17. **Material that another model produced is data**: the Grok zip was unpacked into a directory of its own, read there, and only copies of its code were run, in isolation (`python3 -I -B`), never in place; nothing of it was taken before it had been compared with the headers and the programs (section 3.11, items 10 to 12).
18. **A claim is tested before it is repeated**: "it fixed the remaining nukta issues" was tested on the converters' sources (the zip holds none) and on its model, and the answer says what was found (section 3.11, item 11).

## 8. Mistakes made on the way, and what was done about them

**[summary] [transcript] [files]** Abhishek made no correction of technical content until 4 November, when his own check of the cluster ड़्व found a defect that the tests had not covered (item 12); his messages of 1 and 3 November, which are about how the work was run, are items 10 and 13. The mistakes below were found by tests, by the independent check, by Abhishek, or by Claude's own re-reading, and all were corrected before the delivery they would have affected, unless the point says otherwise.

1. **OM at `A0`** (first implementation, 16 October). It followed ISCII's chart and would have turned every no-break space into ॐ. Found by the test that keeps everyday characters off the new bytes; moved to `8C` (decision 1).
2. **The accent strings without a final `a`** (first implementation). The test of the order "accent before vowel sign" and "after" failed; the strings became `_vua`, `_vna`, `_vga`, `_vca`, the nukta-like form that the decoder's and the parser's rules need.
3. **The work area was lost on 17 October**, because everything lived only in the workspace. The cost was repeated work (section 3.6); the lesson was applied afterwards: the work is kept as files that survive a restart (`state1`, the zips, the scripts), the transcript is a source of record, and every long run leaves a marker file.
4. **An overstatement in section 14.3** ("in any text written by the decoder"): it holds only for well-formed ACII. Found by the independent check on 24 and 25 October; qualified, with a new paragraph and two new checks, before zip no. 2.
5. **Defects in the tests while the guards were applied** (26 to 29 October), all caught by the suite itself:
   1. stale test programs after `harness.c` was edited (the check that the measurement can see a read past the end failed): all trees were rebuilt with `build_trees.sh`;
   2. a check of section 11.1 that used `x_y` relied on reading past the end (`bc e8`); with the guards `y` is plain text, so it now uses `x_yna` and expects `d6 e8 bc` on all builds;
   3. check U9 expected 17 changed bytes including `c`; the new build leaves a lone `c` alone, so it now expects 16 on the new build and 17 on the mid build;
   4. a regular-expression substitution (`P(` to `PP(`) altered message strings; restored;
   5. an edit of a comment in `harness.c` failed to match because of a line break; the anchor was corrected and nothing was written in part;
   6. the patch was read as UTF-8 and failed on a byte; it is read as latin-1.
6. **A change of the working directory**: a `cd` into the repository changes the directory in which later commands run; absolute paths are used throughout, and the clone was verified unmodified after every run.
7. **"137 files" and "144 files"** in the summaries and the delivery notes counted zip entries; the zips hold 125 and 132 files and 12 folders each (section 3.6, item 9).
8. **Drafting errors in this narrative, found in checking before delivery:** a count of messages ("some forty") that the record does not support; three summaries where there are four; the model's identity stated as a fact, where the record has only the configured name; the parser change described as one kind of rule where it is nine rules in one state and three in another; "ACII uses 71 of 128 code points" where the tables say 73 rows (85 after); the weekday of 16 October (a Friday, not a Sunday); the "sixteen others" in the description of the generated table of section 11.3; the date of `tools/reserved_keys.py` (its file date is a fixed packaging date, not the day of its last change); the finding about `\u` escapes, whose day of discovery is not recorded; and the three "uploads" at the start of a session, which are Claude's own earlier deliverables. On the update of 8 November: the row of section 3.9 in the table of section 1 gave "to 30 Oct" for a section that runs to 3 November (corrected).
9. **The API limit of the independent check** (twice): the agent was stopped by a session-limit error; each time the work waited and the same agent was resumed with a message, and it finished.
10. **The long tests were one long step, and were repeated** (29 October to 1 November). The check of section 14 took more than eleven minutes as one step, the build directory was wiped at the start of every run and no step left a marker; so each kill (five of them) lost the whole run, and each new session started it again from the beginning, with no result. Abhishek's message of 1 November names it (*"Split the long running tests!!!! Those are not completing within work window and then you're repeating"*). Fixed as in section 3.9, item 14: nine steps for the check, a marker for every step, `--resume` and `--only`. **The cause of the kills was not only what had been assumed**: when the first split run was made, `underscore_U7` was killed by the kernel for memory (6.1 GB, exit status 137, 3 November), and the kills of 31 October, 8 and 12 minutes after a launch, were probably the same; it was repaired at once (chunks of strings; section 3.9, item 14, sub-point 6).
11. **A guard in the launcher matched Claude's own shell** (3 November): the script that starts the full run refused to start because `pgrep -f` found the text it looks for in the command line of the tool shell that was running it. The log was empty, so it was seen at once; the pattern was anchored (`^bash tests/run_all.sh --full`) and the run started a minute later.
12. **The nine letters without a row** (4 November; found by Abhishek). The cluster ड़्व written with the single code point U+095C came back as व. The cause was not new: it is the low-byte fallback of `uni2acii` in the unpatched converter. The document had recorded the fallback (section 11.6) and had advised normalising to NFD before `uni2acii` (section 10.4), and test (d) of `tests/test_unicode.py` classified the unmapped code points; but the defect had not been connected to the clusters of section 11.3 and had not been repaired, and none of the earlier tests passed those clusters through the Unicode converters with the single code points. It was found by his own manual check, not by the tests. The probes of 4 November reproduced it (section 3.10, item 4); the nukta layer (patch 0003) repairs it, and part (h) of `tests/test_nukta.py` now passes the fifteen clusters, with ड़ in both spellings, through the whole chain.
13. **"Dozens of turns" and "a waste of my time"** (3 and 4 November). Two remarks about how the work was run, recorded as he wrote them: *"You've taken, I don't know how many dozens of turns"* (3 November, 16:22 IST) and *"I am lead to doubt your three weeks of work as a waste of my time"* (4 November, 12:27 IST). They name no technical fault beyond item 12. The standing rules of section 2 stay what they are: do not redo work already done (I2), keep the calls few and compact (section 9, item 4), and run the long tests in pieces (I9).
14. **Errors in the new text of the document (section 15), found by proofreading** (5 and 6 November), all corrected before delivery: it is the decoder, not the filter, that takes the backslash off with the halant (checked by running `acii2rmn` on `5C E8 D4`, which writes `wa`, and on `5C D4`, which writes `\wa`); the nukta was cited to section 3.4, and the rule that governs it is R7 of section 6; the claim that ऩ ऱ ऴ do not round-trip exactly at level 0 was wrong for ऩ and ऱ, which have rows of their own, and was removed; "text without one is unaffected" was wrong, because the pairs `C6 E9`, `CF E9` and `D2 E9` change too; the wording about ISCII's soft halant now says that a layer that reordered "would have to tell a nukta from ISCII's soft halant" (conflict C8 of section 10); the phrase "model of section 15.2" was replaced by "NFC and the layer differ"; a sentence about the dotted circle that nothing used was removed; in C2 the row "out, level 0" belonged to the input of pairs and was moved there; and the challenge tables were restructured into the order input, ACII, Romenagri, output.
15. **A citation that said more than its source** (6 November). The document said of one of the two pages cited in section 12.1 that it "says of U+0958 that NFC does not recompose it ..."; the thread, when it was fetched again, says that the decomposed forms were the experts' preferred representation for Devanagari, and nothing more of the kind. The sentence was reworded to what the page supports. Because the document is part of patch 0003, the patch was made again and every suite was run again; the first full run of that day was discarded (section 3.10, item 13).
16. **Slips in the running of the tests and in the editing** (5 and 6 November), all caught at once: the first pool lists left out `underscore_U6` (the final `--full --resume` ran it); in the script that rebuilt the document an anchor ("14. Underscores ...") matched twice, in the contents list and in the heading, and a longer anchor (the line "13. Running the checks" before it) fixed it; and a combined edit failed because its anchor was not in the text of the script, so the calls were inserted before another anchor.
17. **Stale figures in the README and in the texts of the site** (10 November): they carried figures of earlier runs (2 min 40 s, 284 s and 83 s for the first form of the layer, "229 measurements", "75 checks"), a placeholder (`__CANON__`) left in a generated text, and rows of old tables; found by reading them against the recorded logs before zip no. 5, and corrected from the logs (the limitations test has 230 lines that hold and six informational lines; the quick run took 119 s, the full run 3 min 20 s, with 375 s of steps).
18. **Drafting errors in the site** (9 to 11 November), found by reading, by the browser or by `--check`, and corrected before delivery: the table of the eleven letters gave short names (`nnna`) and now gives the full Unicode names; a sentence in the README and in the notice said that the wording of the cases C1 to C8 was kept from the Grok draft, which could not be verified, and was removed (the notice now says that the plan, the look, the idea of a notebook and the danda note were taken, and nothing else); the README of the site said that nothing is written outside `docs/` and `notebooks/`, but the builder compiles in a temporary directory (corrected); the thresholds of the coverage counters of `--check` were made to count what the cases reach; the pages overflowed at phone width (the navigation now wraps and long words break); an error of order in a helper of the generator (`expand`) was found and repaired; and in the final run the first call of the check used `/usr/bin/time`, which the image does not have (status 127), so the check was run again without it.
19. **The attribution of zip no. 4 in Appendix B** (found on 11 November): the table in the version of 8 November put zip no. 4 in the session of message no. 49 (00:12 UTC); the files date the zip at 05:31 UTC, two minutes after message no. 50 (05:29 UTC). Appendix B now has it in the row of no. 50.
20. **Counts that had gone stale in this narrative** (found on 11 November): the number of lines of the memory file (thirteen; fifteen now), of the session summaries (nine; eleven), of the measurements of the limitations test (152; 230 and six), and the descriptions of the nukta layer (the policy `NUKTA_REBUILD`, 75 checks) in the sections that describe the present state (5.2, 5.5, 6.5, 7.2, 7.3, 10), which now describe the form; section 3.10 keeps zip no. 4 as it was and says so at its head.

## 9. How the work was run: pauses, resets, limits, restarts

**[summary] [transcript] [files]**

1. **Why so many "Continue" messages.** The work was done on the free plan, in which the use is limited. Each time the limit was reached the work stopped; Abhishek wrote *"You got paused…"* or *"Continue…"* when it could go on. More than thirty such messages have retained times, and more are recorded only by their wording (Appendix A). "Don't redo work already done" (I2) was followed except once (item 2).
2. **The one reset of the work area** (17 October): see section 3.6. After it, the work area (files) has survived every pause; the processes in it have not.
3. **Container restarts.** Each new session of the work starts in a fresh container (the first command after a pause shows an uptime of zero minutes). Files in the work area are still there; background processes are gone. Long test runs (the full and the extended suite, several minutes each) were therefore started again after the restarts of 29 October (23:47 UTC), 30 October (about 09:30 UTC) and 31 October (03:37 UTC and 15:35 UTC), and were killed again each time, always inside the check of section 14 (one step of more than eleven minutes; the kills were probably out-of-memory kills of that step, not pauses: section 3.9, item 14, sub-point 6); the restarts of 1 November (before 05:41 UTC) and 3 November (01:47 UTC) found them in pieces (section 3.9, item 14). The runs were detached from the shell (`setsid nohup`), with a marker file (`time.txt`) written when a run ends, and from 1 November every step writes a marker of its own. From 4 November the sessions began at 22:20 UTC on 4 November, at 04:49 and 14:05 UTC on 5 November, at 01:57, 10:35 and 21:56 UTC on 6 November, at 03:05 UTC on 7 November and at 00:12 UTC on 8 November, each in a fresh container; the kernel of the container went from `fc-v230` to `fc-v242` and `fc-v300` (the summaries name them), and was `fc-v310` on 8 November (the recorded runs of that day), `fc-v338` at 19:06 UTC on 10 November and `fc-v378` on 11 November. From 8 November the sessions began at 05:29 UTC (message no. 50; zip no. 4 was finished at 05:31 UTC), 06:12, 10:21, 11:08 and 16:09 UTC and 23:34 UTC on 8 November, at 04:32, 09:43 and 20:33 UTC on 9 November, at 04:56, 07:07 and 19:06 UTC on 10 November and at 00:56, 09:04 and 18:15 UTC on 11 November (Appendix A). The runs of this phase were made in pieces, with markers (section 3.9, item 14); the two full runs of 6 November (the first ending at 10:45 UTC, the second from 21:58:05 to 22:00:45 UTC) finished within their sessions.
4. **How a window of work was spent.** A session is short, and each tool call costs a share of it, so the work was organised as few, compact calls: long reads done once; results kept in files; summaries of state written to files and to the task list; checks run in the background while text was written.
5. **The task list** (shown beside the conversation) carried the steps: the first six of 15 October (map, build, converters, Shaili Wyaakaran, uncovered sutras, check), then the sutra proof, the character work (map, inventory, grammar, add, test, document and package), and, from 25 October, three tasks (apply the guards, write this narrative, package and deliver) and, on 3 November, a fourth (split the long tests into resumable steps and run them). From 4 November the list carried three tasks for the nukta layer: the layer, its tests and the patch; the document, the README, the notice and this narrative; the runs, zip no. 4 and the write-up of the challenges. From 8 November the list carried tasks for the layer on his decisions (code, tests, document), for the README and the notice, for the site (its pages and its notebook) and for this narrative, zip no. 5 and its delivery. The last step of each list was the check of the work: facts against their sources, arithmetic by running it, a document by opening it, a page by looking at it.
6. **Tools used** over the conversation (named in the summaries): `Agent` and `SendMessage` (the independent check), `Bash`, `Read`, `Write`, `Edit`, `Grep`, `SendUserFile`, `SendUserMessage`, `TaskCreate`, `TaskUpdate`, `TaskList`, `ToolSearch`, `WebFetch`, `WebSearch`, and the memory tools. Web tools were used for the survey of 15 October (the sources of the coverage analysis and the repository) and, on 6 November, to fetch again the two pages cited in section 12.1 of the document (section 3.10, item 13); nothing else in the Romenagri work needed them.
7. **Run times, in order** (section 5.5 has what each run covered):

   | When | Run | Time |
   |---|---|---|
   | 18 Oct | the grammar against the parser on 1,232,540 strings | 56 s |
   | 20 Oct | quick suite (ten steps) | 17.8 s |
   | 20 Oct | full suite | 1 min 44 s |
   | 23 Oct | final tree before the guards: quick / full / extended | 47 s / 3 min 18 s / 3 min 21 s |
   | 29 Oct | quick suite, three builds, twelve steps | 86 s |
   | 3 Nov | quick suite, three builds, twenty steps | 106 s |
   | 3 Nov | full suite, in pieces (a pool of two) | 2 min 38 s (the steps: 310 s) |
   | 3 Nov | extended run (the two steps that read the extra inputs) | 6 s |
| 6 Nov | quick suite, three builds, twenty-one steps | 83 s |
| 6 Nov | full suite, in pieces (a pool of two) | 2 min 40 s (the steps: 284 s) |
| 6 Nov | extended run (the two steps that read the extra inputs) | 5 s |
| 8 Nov | quick suite, three builds, twenty-one steps | 119 s |
| 8 Nov | full suite, in pieces (a pool of two) | 3 min 20 s (the steps: 375 s) |
| 8 Nov | extended run (the two steps that read the extra inputs) | 9 s |
| 11 Nov | site check (`build_site.py --check`, 39 checks) | 48 s |

8. **The final runs.** The final runs were made on 3 November on the final files of `Romenagri/`, `patches/`, `tools/` and `tests/` (stamp `d32f3ea25d5ca007`): the quick suite, 20 of 20 in 97 seconds (it was run again after the memory repair of `underscore_U7`; the first, of 106 seconds, had been made before it); the full suite, 20 of 20 in 2 minutes 38 seconds as a pool of two workers; and the two extended steps in 6 seconds. Their consoles and logs, and the versions of the tools, are in `results/`. The first full run (01:51 to 02:00 UTC) is not in `results/`: its nineteen passing steps were run again after the repair, and the step that died is described in section 3.9, item 14, sub-point 6; the kernel's line about it is kept in the work area. **For zip no. 4** the final runs were made on 6 November on the final files (stamps: quick `bf982fe864053d90`, full `d160b87c927f6039`, extended `b68b0acf5a5b38d3`): the quick suite, 21 of 21 in 83 seconds; the full suite, 21 of 21 in 2 minutes 40 seconds as two pools of two workers; the two extended steps in 5 seconds; on the kernel `6.18.44-fc-v300`. Their consoles and logs are in `results/`. A first full run of 6 November (ending 10:45 UTC) was discarded, because the document, and so patch 0003, was changed after it (item 15 of section 8). **For zip no. 5** the final runs were made on 8 November from 23:41 to 23:48 UTC, on the kernel `6.18.44-fc-v310`, on the final files (stamps: quick `9a65e4103300ba56`, full `4847d62c939339e3`, extended `552fd3a166974615`): the quick suite, 21 of 21 in 119 seconds; the full suite, 21 of 21 in 3 minutes 20 seconds, the steps taking 375 seconds together; the two extended steps in 9 seconds; the consoles and logs are in `results/`. The stamps of the quick and of the full run were computed again on 11 November from the files of the package and are the same. The site check of 11 November (48 seconds, 39 of 39) is in `results/site-check.txt`.
9. **How each delivery was checked:** the quick suite on the work tree; the zip unpacked into a clean directory and the quick suite repeated there; the patches applied to a fresh copy; `SHA256SUMS` for every file in the zip; the clone of the repository compared with its head commit. For patch 0003 also the four checks of `verify_patch3.sh` (section 3.10, item 14). For zip no. 5 also the site check (section 3.11, item 14) and the comparison of the stamps of the recorded runs with the files of the package.
10. **What the sessions were**: each message of Appendix A started or resumed a working session; Appendix B lists those whose start the files fix to the minute. The narrative of the sessions from 25 October 14:00 UTC on rests on the transcript as it stood on 30 October and on 3 November, and on the files (the sessions of 31 October and 1 November also on the summaries written at the compactions); the sessions of 4 to 8 November rest on the transcript as it stands at the delivery of zip no. 4 (from 22:26 UTC on 4 November, with three summaries inside it), on the files, and on two probes that were run again (section 3.10); the sessions of 8 to 11 November rest on the files, on the summary at the head of the transcript as it stands at the delivery of zip no. 5 (05:00 UTC on 10 November) and, from 04:59 UTC on 10 November, on the transcript itself (section 3.11); the earlier ones rest on summaries and files (section 10, item 12).

## 10. Open items

**[summary] [package]** Numbers 1 to 11 are the things still to be decided or done; number 12 lists what could not be recovered; 13 to 15 are housekeeping; 16 gathers what the nukta layer leaves to him, and 17 what the site leaves to him.

1. **The fifteen missing rows** (decision 7; section 3.7): his to fix or to hand over. `tools/reserved_keys.py --strict` exits with 1 until all fifteen are closed; `tests/test_limitations.py` asserts the crash today and will fail when a fix lands, so the document and the test are updated together. Patch 0003 does not touch it; `tests/test_nukta.py` (C8) asserts the same crash for `lha`, `_rrha` and `_rdvra`.
2. **Patch 0002**: keep or drop (decision 8). It is on by his request; the price is the changed meaning of invalid inputs (`c_`, `_n_` and ten more); `patch -R -p1 < patches/0002-apply-underscore-guards.patch` removes it.
3. **A run of the end-to-end test with real GNU awk.** It passed with `gawk` linked to `mawk`; Hindawi's scripts start with `#!/usr/bin/gawk -f`.
4. **The notices of the 54 untouched files** (57 before patch 0003; mostly 2003-2006) and the words "(prepared with Claude)" in the modification logs (decisions 5 and 6).
5. **Real ISCII with two-byte forms** (decision 3): the table is in section 10.5; the converters were not changed.
6. **Characters not added:** a byte of its own for U+0934 (recipe in section 10.4; since patch 0003 the code point passes through the converters as `D2 E9`), ZWNJ and ZWJ (two rules and two rows and no state, if they follow the marker rule), the 24 other uncovered code points of the Devanagari block, Vedic Extensions and Devanagari Extended (decision 4).
7. **The three remaining reasons for a crash** of the C code, besides the fifteen rows: the fixed buffers (1,025 letters; 10,240 decoded characters), the decoder's empty-stack underflow, and the decoder's lone underscore on malformed ACII. None was asked for; each is measured.
8. **A machine-checked proof** (Coq or Lean) of the statements of section 14: open; the models are small enough.
9. **The Hindawi findings** (keyword replacement inside identifiers; the Python shaili on master; the `gawk` dependency): reported to Abhishek in the conversation; no issue has been raised in any repository.
10. **The consolidation page**: Abhishek wants an issue raised there when a new sutra implementation works (saying where it was placed) or when results go wrong. Nothing has been implemented from the list of uncovered sutras, so there is nothing to raise.
11. **The sutra work itself**: 1,815 sutras not covered by vidyut-prakriya (section 5.9); one (6.1.77) written in JavaScript and in Hindawi; JavaScript-first, GitHub Pages hosting and generators for the rest not started. His own work on the Panini language on the web is paused by his decision.
12. **What the record could not give**, so that the narrative could not say it:
    1. the exact words of his three messages of 14 October (only their substance);
    2. the text of Claude's replies of 15 and 16 October (only the three files that went with them);
    3. the text of the explanation of the fifteen keys (20 October), of the replies about the underscore (20 to 25 October) and of the final messages of zips no. 1 and no. 2;
    4. the exact times of some short messages between 17 and 25 October;
    5. the pasted text of the three questions (only their description in the summary and the document's version);
    6. the summary of Shaili Wyaakaran made on 15 October;
    7. on which day each Hindawi finding was made (in the sutra proof or in the end-to-end tests);
    8. the model that served each turn (only the configured one is known);
    9. the transcript before 25 October 14:06 UTC;
    10. the dates of the first six lines of the memory file about the repository (14 to 17 October);
    11. the text of Claude's replies of 3 and 4 November (the table of the fifteen rows with the pronunciation by region; the answers to the messages of 12:08 and 12:27 IST), known only in substance, from the summaries and from two probes that were run again;
    12. what Abhishek meant by "13 and 15" in his message of 4 November, 12:08 IST (rows 13 and 15 are ऱ्व and ऱ्ह; the message does not say);
    13. which spelling of ड़ his message of 12:27 IST contained (the summaries record the single code point U+095C);
    14. the minute at which the nukta layer was begun on 4 November, after 14:20 UTC: the files of the package carry a fixed packaging date, and the work copies that keep their own dates begin at 22:26 UTC.
    15. the text of Claude's replies of 8 and 9 November (the first reading of his decisions, the first examination of the Grok zip), known only in substance, from the first summary of the transcript and from the files;
    16. the text of Claude's replies of 10 November before 04:59 UTC;
    17. what Grok itself was asked and what it said besides the claim that his message quotes (he gave only the claim and the zip);
    18. the minute at which the work on his decisions was begun on 8 November, after 06:12 UTC: the work copies that keep their own dates begin at 10:21 UTC (`iter4/`).
13. **Memory**: the file about the repository received two more lines on 31 October (that he asked for the guards to be applied, and for this narrative), one on 3 November (that he asked for the long tests to be split), one on 7 November (that he asked on 4 November for the nukta layer) and two on 10 November (his decisions of 8 November on the nukta layer; the Grok site); it holds fifteen lines.
14. **The checksums of zips no. 3, no. 4 and no. 5.** The checksums of zips no. 3 and no. 4 are in Appendix C (computed from the copies kept in the work area); zip no. 5's is given in the delivery message, because a file cannot contain its own checksum; `SHA256SUMS` inside each covers every other file.
15. **The package is tied to commit `3ad87785…`**: if the repository moves on, the patches may need rebasing; `tools/apply_sanskrit.py`, `tools/apply_guards.py` and `tools/apply_nukta.py` assert their anchors and refuse to run on a tree they do not fit.
16. **The nukta layer: what is still his** (section 7.2, decision 9; section 3.11): to confirm the default form (`asis`), the dropped fourth option (all eleven letters as single code points), the reading of "Level 1" and of "function call integration", and whether patch 0003 is folded into patch 0001; the two cases decided as "none" stay as they are: a nukta after a halant is not rebuilt (reordering would need a way to tell a nukta from ISCII's soft halant), and ऴ has no byte of its own (`D3` is not assigned).
17. **The site: three things that are his** (section 7.2, decision 10): the note on the danda, which comes from the Grok draft and is marked as not confirmed; the validation of the notebook with `nbformat`, which could not be installed here; and publishing on GitHub Pages, of which nothing was done (the steps are in `romenagri-site/README.md`). The pages were looked at in Chromium only, at desktop and phone widths.

## Appendix A. Abhishek's messages, with times

**[summary] [transcript]** Times are IST (his), with UTC beside them. Words in quotation marks are retained word for word; the other entries are described. Between 17 and 24 October there are further short messages (*"Continue from where you got paused"*, *"Continue from where you got dropped off."*, *"Continue from where you left off."*, *"Anyway."*, *"Please from where you got paused."*) that are recorded only by their wording, not by their times.

| # | Day | IST | UTC | Message |
|---|---|---|---|---|
| 1 | Wed 14 Oct | 23:17 | 17:47 | the first of three messages: ACII and ISCII (not retained word for word) |
| 2 | Wed 14 Oct | | | the second: the recommended path for building Paninian generators (not retained word for word) |
| 3 | Wed 14 Oct | 23:32 | 18:02 | *"Simply copy pasting my above two messages should work."* |
| 4 | Thu 15 Oct | 05:41 | 00:11 | *"You got paused as limits ran out. Continue. Don't redo work already done"* |
| 5 | Thu 15 Oct | 11:27 | 05:57 | *"Continue from where you got paused"* |
| 6 | Thu 15 Oct | 11:45 | 06:15 | *"How would you build the sutras using Hindawi"* |
| 7 | Thu 15 Oct | 23:12 | 17:42 | *"Continue"* |
| 8 | Fri 16 Oct | 04:25 | 22:55 (15 Oct) | *"Continue from where you got paused"* |
| 9 | Fri 16 Oct | 04:38 | 23:08 (15 Oct) | the request for the missing Sanskrit characters (section 3.4, item 1) |
| 10 | Fri 16 Oct | 12:59 | 07:29 | *"You got paused."* |
| 11 | Fri 16 Oct | 18:37 | 13:07 | *"Please continue from where you got paused."* |
| 12 | Fri 16 Oct | 23:49 | 18:19 | *"Continue"* |
| 13 | Sat 17 Oct | 07:36 | 02:06 | zip, licences, copyright 1993-2026, the name, memory (section 3.5) |
| 14 | Sat 17 Oct | 08:18 | 02:48 | *"Please continue from where you got paused."* |
| 15 | Sat 17 Oct | 13:30 | 08:00 | *"Anyway."* |
| 16 | Sat 17 Oct | 15:52 | 10:22 | *"Please from where you got paused."* |
| 17 | Sat 17 Oct | 18:45 | 13:15 | *"Please continue from where you got paused."* |
| 18 | Sat 17 Oct | 23:43 | 18:13 | *"Please from where you got paused."* (after the reset of the work area) |
| 19 | Sat 17 Oct | (time not retained) | | *"Continue from where you left off."* (after the limit notice "resets 11:10pm (UTC)") |
| 20 | Tue 20 Oct | 07:43 | 02:13 | *"Please explain all the remaining 15 character bugs. I'll also read through, but explain those. I'll try to manually solve them. Otherwise, I'll pass it off to you later."* |
| 21 | Tue 20 Oct | 17:22 | 11:52 | *"Continue continue from where you were paused and also solve these."* and the three pasted questions |
| 22 | Sat 24 Oct | 11:17 | 05:47 | *"Continue"* |
| 23 | Sun 25 Oct | 05:17 | 23:47 (24 Oct) | *"Continue"* |
| 24 | Sun 25 Oct | 10:20 | 04:50 | *"Continue"* |
| 25 | Sun 25 Oct | 19:30 | 14:00 | *"Apply the guard rules"* and *"Please give me a combined updated pointwise structured narrative of the conversation without dropping any points or facts or threads from the beginning"* |
| 26 | Mon 26 Oct | 11:33 | 06:03 | *"Continue"* |
| 27 | Wed 28 Oct | 14:36 | 09:06 | *"Continue"* |
| 28 | Thu 29 Oct | 07:48 | 02:18 | *"Continue"* |
| 29 | Fri 30 Oct | 05:17 | 23:47 (29 Oct) | *"Continue"* |
| 30 | Fri 30 Oct | 14:50 | 09:20 | *"Continue"* |
| 31 | Sat 31 Oct | 09:06 | 03:36 | *"Continue"* |
| 32 | Sat 31 Oct | 21:04 | 15:34 | *"Continue"* |
| 33 | Sun 1 Nov | 11:10 | 05:40 | *"Continue... Split the long running tests!!!! Those are not completing within work window and then you're repeating"* |
| 34 | Tue 3 Nov | 07:17 | 01:47 | *"Continue"* |
| 35 | Tue 3 Nov | 16:15 | 10:45 | *"Continue"* |
| 36 | Tue 3 Nov | 16:22 | 10:52 | *"which 15 rows are still not fixed. Give me the exact details. You've taken, I don't know how many dozens of turns"* |
| 37 | Tue 3 Nov | 16:26 | 10:56 | *"right? Give those characters with their Devanagari characters and the common pronunciation in Eastern India, in Northern India, in Central India, and in Southern India. Remember, these pronunciations vary by region."* |
| 38 | Wed 4 Nov | 11:59 | 06:29 | *"Continue"* |
| 39 | Wed 4 Nov | 12:08 | 06:38 | *"Except for 13 and 15... All are covered by even the oldest Romenagri behenchod"*, and after a blank line *"Try passing Devnagri through"* |
| 40 | Wed 4 Nov | 12:27 | 06:57 | four paragraphs: *"This should work ड़्व"*, *"Let me check manually"*, *"But now I am lead to doubt your three weeks of work as a waste of my time"*, *"Reviewing everything you did..."* |
| 41 | Wed 4 Nov | 19:50 | 14:20 | *"Add in the patch... Just add a layer that decomposes the underlying nukta layer, and builds it back"*, and after a blank line *"Are there any technical challenges? If you identify any please show those in Devnagri for me to review"* (section 3.10) |
| 42 | Thu 5 Nov | 03:50 | 22:20 (Wed 4 Nov) | *"Continue"* |
| 43 | Thu 5 Nov | 10:19 | 04:49 | *"Continue"* |
| 44 | Thu 5 Nov | 19:35 | 14:05 | *"Continue"* |
| 45 | Fri 6 Nov | 07:27 | 01:57 | *"Continue"* |
| 46 | Fri 6 Nov | 16:05 | 10:35 | *"Please continue to completion now."* |
| 47 | Sat 7 Nov | 03:26 | 21:56 (Fri 6 Nov) | *"Please continue."* |
| 48 | Sat 7 Nov | 08:35 | 03:05 | *"Continue"* |
| 49 | Sun 8 Nov | 05:42 | 00:12 | *"Continue"* |
| 50 | Sun 8 Nov | 10:59 | 05:29 | *"Continue."* |
| 51 | Sun 8 Nov | 11:42 | 06:12 | the decisions on C1 to C8, quoted in full in section 3.11, item 2 |
| 52 | Sun 8 Nov | 15:51 | 10:21 | *"continue."* |
| 53 | Sun 8 Nov | 16:38 | 11:08 | *"continue."* |
| 54 | Sun 8 Nov | 21:39 | 16:09 | *"Yep."* |
| 55 | Mon 9 Nov | 05:04 | 23:34 (Sun 8 Nov) | *"Continue"* |
| 56 | Mon 9 Nov | 10:02 | 04:32 | the message about the site that Grok built (section 3.11, item 9), word for word |
| 57 | Mon 9 Nov | 15:13 | 09:43 | *"continue."* |
| 58 | Tue 10 Nov | 02:03 | 20:33 (Mon 9 Nov) | *"Continue, please."* |
| 59 | Tue 10 Nov | 10:26 | 04:56 | *"Continue"* |
| 60 | Tue 10 Nov | 12:37 | 07:07 | *"Continue"* |
| 61 | Wed 11 Nov | 00:36 | 19:06 (Tue 10 Nov) | *"Continue"* |
| 62 | Wed 11 Nov | 06:26 | 00:56 | *"Continue"* |
| 63 | Wed 11 Nov | 14:34 | 09:04 | *"Continue"* |
| 64 | Wed 11 Nov | 23:45 | 18:15 | *"Continue"* |

## Appendix B. Session starts

**[files] [transcript]** A new working session starts with each message of Appendix A. The table gives the ones whose start the files fix to the minute, with the first thing the files show.

| Start (UTC) | Message | What the files show |
|---|---|---|
| 17 Oct 18:13 | no. 18 | the work area had been reset; it was rebuilt from the transcript (first rebuilt files at 22:31-22:32) |
| 24 Oct 05:47 | no. 22 | the independent check's copy of the package (05:50); the document's parts (05:49) |
| 24 Oct 23:47 | no. 23 | the work towards zip no. 2 |
| 25 Oct 04:50 | no. 24 | the final runs (04:55-05:03); **zip no. 2 at 05:02**; the memory write at 05:04 |
| 25 Oct 14:00 | no. 25 | the unchanged copy of the tree (`state1`, 14:04); the transcript begins at 14:06 |
| 26 Oct 06:03 | no. 26 | `tools/apply_guards.py` (06:05); the guards in `rmn2acii.c`; the limitations test adapted (06:11) |
| 28 Oct 09:06 | no. 27 | a third build tree (09:11) |
| 29 Oct 02:18 | no. 28 | `tests/test_underscore.py` edited (02:19); a fourth build tree (02:30) |
| 29 Oct 23:47 | no. 29 | the full and extended runs started; killed by a restart; the quick run (23:50) |
| 30 Oct 09:20 | no. 30 | the first three parts of this narrative (09:26-09:29); the runs killed again |
| 31 Oct 03:36 | no. 31 | the runs relaunched (03:37); part 4 of this narrative (03:44); killed again by the next pause |
| 31 Oct 15:34 | no. 32 | the runs relaunched (15:35); parts 5 to 10 of this narrative |
| 1 Nov 05:40 | no. 33 | `tests/test_underscore.py` given `--only` (backup 05:44); the check that the old and the new script write the same output (05:44-05:47); the rewritten `tests/run_all.sh` |
| 3 Nov 01:47 | no. 34 | section 13 of the document and patch 0002 made again (01:48); the quick suite, 20 of 20 in 106 s (01:48-01:50); the full suite launched as a pool of two (01:51); the kernel's out-of-memory kill of `underscore_U7` seen (02:00), the check repaired, the pool launched again (02:05) |
| 3 Nov 10:45 | no. 35 | the folder `results/` and `environment.txt` made from the final runs (10:47); this narrative finished; the package made and checked |
| 4 Nov 06:29 | no. 38 | `probe_in.txt` and `probe_out.txt` (06:29): the thirteen `vra` clusters typed with `v` and with `w` through `rmn2acii` |
| 4 Nov 06:38 | no. 39 | `probe_chain.py` (06:40): the fifteen clusters through the whole chain on the three builds of zip no. 3; `probe2.py` (06:41): the precomposed nukta letters and the eyelash ra |
| 4 Nov 22:20 | no. 42 | the unchanged tree of zip no. 3 kept as the older side of patch 0003 (`pre0003`, and `iter3/orig`, 22:26); the transcript begins (22:26); the first summary (22:30) |
| 5 Nov 04:49 | no. 43 | a copy of `Romenagri/` for a trial of the change (`dry0003`, 04:50); the first two runs of the test `nukta` (05:00 and 05:01); `probe_e.py` (05:01), which compares level 1 with NFC on random streams; the build `build4` (05:02) |
| 6 Nov 01:57 | no. 45 | `scratch0003` (02:00), the three levels built from one source for a check; three more runs of the test `nukta` (02:01 to 02:02); the second summary (02:06) |
| 6 Nov 10:35 | no. 46 | the document made again (`build_doc3.py` and `doc_dry.md`, 10:39); `verify_patch3.sh` (10:41); the first full run of the day (`build5`, ending 10:45), later discarded |
| 6 Nov 21:56 | no. 47 | the final runs: `build6` (21:58), the pools (21:58 to 22:00), the quick run (22:00 to 22:02), the extended run (22:02); `results/` saved (22:02); the third summary (22:06) |
| 8 Nov 00:12 | no. 49 | this narrative brought up to date (parts n1 to n10); the checksums |
| 8 Nov 05:29 | no. 50 | zip no. 4: `SHA256SUMS.new`, `dist4` and `verify4` (05:31), the quick run in the unpacked copy (`verify4_build` and `verify4_quick.log`, 05:33); the files date the zip two minutes after the message, so it was made and checked in the session that this message started (the version of this table delivered with zip no. 4 put it in the session of no. 49) |
| 8 Nov 10:21 | no. 52 | `iter4/` (10:21-10:23): the first work files of the layer on his decisions (`build`, `parts`, `smoke_u2a.py`, `edit_tests.py`); no earlier work file of the layer keeps its date |
| 8 Nov 16:09 | no. 54 | the second series (16:11-16:21): the test of zip no. 4 kept (`test_nukta.zip4.py`), the C files and the apply script made again (`make_c.py`, `make_apply.py`, 16:14), `splice.py` (16:21) |
| 8 Nov 23:34 | no. 55 | the final work and the final runs of the layer: the README of zip no. 4 kept (23:35), the quick run (`quick1.log`, 23:37), the test and section 15 (23:38-23:39), patch 0003 made again (23:41), the recorded runs (23:41-23:48), `results/` saved (23:48-23:49) |
| 9 Nov 04:32 | no. 56 | the Grok zip unpacked into `grok/` (04:32) and the scripts that read it, in `grok_eval/` (04:35-04:36) |
| 9 Nov 20:33 | no. 58 | the first two runs of the site check (`site_check1.out`, 20:41; `site_check2.out`, 20:43) |
| 10 Nov 04:56 | no. 59 | the transcript begins at 04:59 and the first summary was written at 05:00; the third run of the site check (`site_check3.out`, 05:01) and the looks at the pages in Chromium (`site_eval/`, 05:02) |
| 10 Nov 19:06 | no. 61 | the copies of the README and of the notice from before the site entries (`README.md.before_site`, 19:07; `NOTICE.before_site`, 19:10); the memory write (19:13) |
| 11 Nov 00:56 | no. 62 | the second summary (01:01); the final build of the pages and the final site check (01:02-01:03); `results/site-check.txt` and `results/environment.txt` brought up to date |
| 11 Nov 09:04 | no. 63 | this narrative brought up to 11 November (section 3.11 and the corrections, made by a script of the work area, `narr311/`, 09:10-09:16) |
| 11 Nov 18:15 | no. 64 | `SHA256SUMS`; zip no. 5 made, unpacked into a clean folder and checked there (Appendix C) |

## Appendix C. The five zips

**[files] [package]** All five are named `romenagri-sanskrit-characters.zip` and unpack into a folder `romenagri-sanskrit-characters/`. "Entries" counts files and folders.

| # | Made | Entries | Files | Bytes | SHA-256 |
|---|---|---|---|---|---|
| 1 | Tue 20 Oct 2026, 01:56 UTC (07:26 IST) | 137 | 125 | 391,754 | `0e6aed5760f405e8e2f1b1657c67dd02594387f149d785b721a3b1fe9d4bfef0` |
| 2 | Sun 25 Oct 2026, 05:02 UTC (10:32 IST) | 144 | 132 | 458,325 | `b5657975f9f2aad0799a69f8765593310a485ecb082c1ed33ff542a04b5456e3` |
| 3 | Tue 3 Nov 2026, 10:49 UTC (16:19 IST) | 175 | 163 | 567,379 | `3df61b35ba0f974d10f4f42baa0e726bf0b7bc66cfb3fb117e911efa0eca7377` |
| 4 | Sun 8 Nov 2026, 05:31 UTC (11:01 IST) | 181 | 169 | 646,626 | `ee19e8dccd791bd059b0e52ffcaa425b9871d870a8b0d144a7c61bfc04b83579` |
| 5 | Wed 11 Nov 2026, 18:18 UTC (23:48 IST) | 208 | 192 | given in the delivery message | given in the delivery message (a file cannot contain its own checksum) |

1. **Zip no. 1** holds: `README.md`, `NOTICE`, `LICENSE`, `COPYING`, `SHA256SUMS`; `Romenagri/` (63 files, patched, with the new `TRANSLITERATION.md`); `patches/0001-add-missing-sanskrit-characters.patch`; `tools/` (`make_patch.sh`, `check_tables.py`, `apply_sanskrit.py`, `rmn_tables.py`, `gen_doc_tables.py`); `tests/` (twenty files: the suite, the models, the harness, the end-to-end programs); `results/` (`environment.txt` and three recorded runs).
2. **Zip no. 2** adds section 14 and the enlarged section 11.3 of the document, `tests/test_underscore.py`, the lint check T8, `tools/reserved_keys.py`, the rewritten README with the eight decisions, and three new recorded runs.
3. **Zip no. 3** adds: patch 0002 and `tools/apply_guards.py`; `tests/build_trees.sh` and the three-build suite; the test driver in pieces (twenty steps with markers, `--resume`, `--only`); the guards in `rmn2acii.c` and in the document; the README rewritten for the two patches; the results of the new runs; **`CONVERSATION-NARRATIVE.md`**, this file.
4. **Zip no. 4** adds: patch 0003 (`patches/0003-add-nukta-layer.patch`) and `tools/apply_nukta.py`; `Romenagri/nukta.h` and the changed `uni2acii.c`, `acii2uni.c` and `Makefile`; `tests/test_nukta.py` and the step `nukta` (21 steps); section 15 and the acceptance row A11 in `TRANSLITERATION.md`; the README and the notice rewritten for the three patches; this narrative brought up to 8 November; and the results of the new runs (kernel `6.18.44-fc-v300`). It has 169 files in 12 folders, 181 entries. The figures of row 3 were computed on 8 November from the copy of zip no. 3 kept in the work area; its entries and files agree with those given on 3 November. The bytes and the checksum of row 4 were computed on 11 November from the copy of zip no. 4 kept in the work area (`dist4`), which the files date at 05:31 UTC on 8 November.
5. **Zip no. 5** adds: patch 0003 made again (1,310 lines, 119,357 bytes) and `tools/apply_nukta.py`; `Romenagri/nukta.h`, `uni2acii.c` and `acii2uni.c` with the forms `asis`, `nfc`, `nfd`, the options `-f` and `-w`, and the environment variables; `tests/test_nukta.py` made again (175 checks in parts (a) to (k)) with the updates of `tests/test_unicode.py` and `tests/test_limitations.py`; section 15 of the document made again (nine parts; 211,366 bytes); the README and the notice rewritten for the decisions and for the site; **the folder `romenagri-site/`** (22 files: five pages, a notebook, the JavaScript port, the builder with its checks, its own README); the results of the new runs of 8 November (kernel `6.18.44-fc-v310`) and the record `results/site-check.txt`; and this narrative brought up to 11 November. It has 192 files in 16 folders, 208 entries.
6. Each zip was unpacked into a clean folder and the quick suite was run there before it was sent.

## Appendix D. Where each thing lives in the package

**[package]**

| What | Where |
|---|---|
| How to read and use the package | `README.md` |
| Licences and notices | `COPYING` (GPL v2), `LICENSE`, `NOTICE`, `Romenagri/copying`, `Romenagri/LEGAL` |
| This narrative | `CONVERSATION-NARRATIVE.md` |
| The twelve characters | `Romenagri/unicode.h`, `acii.h`, `aciihin.h`; document sections 7 and 3 |
| The parser, and its grammar | `Romenagri/rmn2acii.c` and `rmn2acii.lex`; document sections 5 (grammar in 5.3) |
| The decoder | `Romenagri/acii2rmn.c`, `stack.c`; document section 4 |
| The conventions for strings (R1 to R9) | document section 6 |
| How to extend (recipes A to F); larger sets, conflicts, missing sounds | document sections 8 and 10 |
| The round-trip contract | document section 9 |
| Limits and quirks | document section 11 |
| The fifteen keys, and the options A to D | document section 11.3; `tools/reserved_keys.py`; `tests/test_limitations.py` |
| The underscore: laws, machine, bijection, guards, case folding, joiners | document section 14; `tests/test_underscore.py` |
| The nukta layer | `Romenagri/nukta.h`, `uni2acii.c`, `acii2uni.c`; document section 15; `tests/test_nukta.py`; `patches/0003-add-nukta-layer.patch`; `tools/apply_nukta.py` |
| The technical challenges C1 to C8, in Devanagari, and the decision on each | document section 15.7; `README.md`; `tests/test_nukta.py`, part (k) |
| Provenance, standards, licence | document section 12 |
| Running the checks | document section 13; `tests/run_all.sh` (`--full`, `--resume`, `--only`), `tests/build_trees.sh`; `tests/test_underscore.py` (`--full`, `--deep`, `--only`) |
| The patches | `patches/0001-…`, `patches/0002-…`, `patches/0003-…`; `tools/apply_sanskrit.py`, `tools/apply_guards.py`, `tools/apply_nukta.py`, `tools/make_patch.sh` |
| The table lint and the generated tables | `tools/check_tables.py`, `tools/gen_doc_tables.py` |
| The executable models | `tests/model.py`, `spec_model.py`, `handwritten_parser.py`, `diff_parser.py`, `rt_filters.py`, `wellformed.py` |
| The end-to-end programs through `hincc` | `tests/e2e/` |
| The recorded runs and the environment | `results/quick-run/`, `results/full-run/`, `results/full-run-extended/`, `results/environment.txt`, `results/site-check.txt` |
| The site: pages, notebook, JavaScript port, how to rebuild, check and publish | `romenagri-site/` (its own `README.md`); `romenagri-site/build_site.py --check`; `results/site-check.txt` |
| Checksums of every file | `SHA256SUMS` |
