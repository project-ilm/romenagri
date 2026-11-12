#!/usr/bin/env python3
# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
"""Writes onepagers/*.md and romenagri-site/docs/{script-*,navigator,open-issues}.html from results.json. usage: gen_pages.py <v6 dir>"""
import html, json, os, sys
V = sys.argv[1]; R = json.load(open(V + "/results.json")); S = R["scripts"]
N = {  # language(s), phonetic / dialect issues, research needed
 "bn": ("Bengali (Bangla)", "Inherent vowel is /ɔ/ not /a/; অ ও pair; ব/ভ, শ ষ স all /ʃ/ in speech; য় ড় ঢ় as separate letters; Sylheti and Rarhi/Barendri readings differ.", "Native-speaker phoneme table per dialect; policy for ড় ঢ় য় (precomposed vs nukta)."),
 "as": ("Assamese", "ৰ is /ɹ/ and ৱ /w/ (pivot: U+0931 and U+0979, a choice to confirm); শ ষ স are all /x/-ish in Assamese, not /ʃ/.", "Confirm pivots for ৰ ৱ; Assamese-specific phoneme table (it shares the Bengali block, so the map is the same file)."),
 "pa": ("Punjabi (Gurmukhi)", "Tones are not written; tippi/bindi and addak (gemination) need rules; ਙ ਞ rare; Majhi/Malwai/Doabi differ.", "Addak and tippi handling; tone-marking convention."),
 "gu": ("Gujarati", "Inherent-vowel deletion is regular in speech (schwa not pronounced word-finally); ળ; ૅ ૉ vowels.", "Schwa-deletion rule set; dialect tables (Kathiawadi, Surati)."),
 "or": ("Odia (Oriya)", "ଵ ୱ and ଯ/ଜ merge in speech; inherent vowel /ɔ/; ଣ ଳ.", "Native phoneme table; treatment of ୱ."),
 "ta": ("Tamil", "No voiced/aspirate series: one letter covers क ग, च ज, ट ड, त द, प ब by position; ழ ற ன pivoted to ऴ ऱ ऩ; Grantha letters ஜ ஷ ஸ ஹ are loan-only; Chennai/Madurai/Jaffna/Kongu differ.", "Positional voicing rules for a Tamil->Devanagari direction (the map is lossy backward); Grantha usage policy."),
 "te": ("Telugu", "ఁ ఀ; ఱ ఴ archaic; Telangana vs Coastal vs Rayalaseema differ in ఎ/ఏ and ళ.", "Archaic letter policy; dialect tables."),
 "kn": ("Kannada", "ೞ ಱ archaic (not mapped); /e/ and /o/ short/long pairs; Mysore/Dharwad/Coastal differ.", "Archaic letter policy (ೞ ಱ); dialect tables."),
 "ml": ("Malayalam", "Chillu letters ൺ ൻ ർ ൽ ൾ are written as consonant + virama in the pivot (forward only, lossy); ഴ ഩ റ pivoted to ऴ ऩ ऱ; /ə/ vs /ɨ/ for the vowel sign ് .", "Chillu policy (a pivot with a joiner or private code point would make them reversible); samvruthokaram."),
 "si": ("Sinhala", "Unicode names do not match Devanagari (KAYANNA, not KA): a name pairing finds almost nothing; prenasalised consonants and ඇ ඈ vowels (/æ/) have no Devanagari letter.", "A hand-built table (ISO 15919 pairs) and a decision on /æ/ and the prenasalised series. Not done in v6."),
 "brah": ("Brahmi (historic)", "No living readers: values are reconstructed; vowel length and anusvara conventions are scholarly choices.", "Which edition's conventions; the unmatched letters."),
 "kthi": ("Kaithi (Bhojpuri, Maithili, Magahi, historic)", "Regional practice varied; nukta and the dots differ.", "Native-reader review; nukta policy."),
 "gran": ("Grantha (Sanskrit in Tamil Nadu, Kerala)", "Matches the Sanskrit sounds; the unmatched are vowel signs and Vedic marks.", "Vedic accent marks; the nine unmatched code points."),
 "shrd": ("Sharada (Kashmiri, historic)", "Kashmiri has vowels (ɨ, ə, ɔ) that Devanagari lacks; Sharada signs for them are unmatched.", "Kashmiri vowel extensions; which Devanagari extension to use."),
 "modi": ("Modi (Marathi, historic)", "Cursive; a few letters are written differently by period.", "Period conventions; the unmatched letters."),
 "tirh": ("Tirhuta (Maithili, historic)", "Maithili phonology (long /ɛ/ /ɔ/) is richer than the Devanagari repertoire.", "Maithili vowel extensions."),
 "sidd": ("Siddham (Buddhist Sanskrit, historic)", "Liturgical; reading follows Sanskrit.", "Sanskrit-only scope; unmatched letters."),
 "newa": ("Newa (Nepal Bhasa)", "Tonal and vowel inventory differs from Devanagari.", "Nepal Bhasa phoneme table; the unmatched letters.")}
HEAD = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>%s</title><link rel="stylesheet" href="style.css"><link rel="icon" href="data:,"></head><body><header class="band"><div class="in"><h1>Romenagri v6</h1><nav><a href="index.html">Home</a> <a href="navigator.html">Navigator</a> <a href="open-issues.html">Open issues</a></nav></div></header><main class="in">'
FOOT = '<p><small>Copyright (C) 1993-2026 Abhishek Choudhary. GPL-2.0-or-later. Mapping layer only; the zip 5 core is used unchanged.</small></p></main></body></html>'
e = html.escape
def md(code):
    r = S[code]; n = N[code]
    t = ["# %s (%s), tier %s" % (n[0], r["script"], r["tier"]), "", "Mapping layer: `Romenagri/fltr_%s_hi` (script to Devanagari) and `fltr_hi_%s` (back); table `v6/maps/%s.csv`." % (code, code, code), "",
         "| Measure | Value |", "|---|---|", "| Repertoire (assigned code points of the block) | %d |" % r["repertoire"], "| Mapped to Devanagari (coverage) | %d (%s %%) |" % (r["mapped"], r["coverage_pct"]),
         "| **T1** reversible, script -> Devanagari -> script | %d = **%s %%** of the repertoire (%s %% of the mapped) |" % (r["T1_reversible"], r["T1_pct"], r["T1_pct_of_mapped"]),
         "| **T2** reversible through the zip 5 core | %d = **%s %%** of the repertoire (%s %% of the mapped) |" % (r["T2_reversible"], r["T2_pct"], r["T2_pct_of_mapped"])]
    c = r.get("corpus")
    if c: t.append("| Corpus `%s`, %d lines, exact lines back | T1 %s %%, T2 %s %% |" % (c["file"], c["lines"], c["T1_line_pct"], c["T2_line_pct"]))
    t += ["", "T2 losses are of two kinds: **mapping** (T1 already fails: %d letters) and **core limit** (the letter's Devanagari image does not survive zip 5 on its own: %d letters, v6 does not touch the core)." % (len(r["lost_by_mapping"]), len(r["core_limit"])), "",
          "- Collisions (several letters to one Devanagari letter): %s" % (", ".join("%s <- %s" % (k, " ".join(v)) for k, v in r["collisions"].items()) or "none"),
          "- Unmapped (no Devanagari counterpart yet): %s" % (" ".join(r["unmapped"]) or "none"), "- Core limit: %s" % (" ".join(r["core_limit"]) or "none"), "",
          "## Open issues for linguists", "", "- Phonetic fidelity and dialects: " + n[1], "- Research needed: " + n[2], ""]
    return "\n".join(t)
def page(code):
    r = S[code]; n = N[code]
    b = HEAD % e(n[0]) + "<h2>%s</h2><p>%s, tier %s. Layers <code>fltr_%s_hi</code> and <code>fltr_hi_%s</code>.</p>" % (e(n[0]), e(r["script"]), r["tier"], code, code)
    b += "<table><tr><th>Measure<th>Value</tr>" + "".join("<tr><td>%s<td>%s</tr>" % (k, v) for k, v in [
        ("Repertoire", r["repertoire"]), ("Coverage", "%s %% (%d mapped)" % (r["coverage_pct"], r["mapped"])), ("T1 reversibility", "%s %%" % r["T1_pct"]),
        ("T2 reversibility (through zip 5 core)", "%s %%" % r["T2_pct"]), ("Lost by the mapping / core limit", "%d / %d" % (len(r["lost_by_mapping"]), len(r["core_limit"])))]) + "</table>"
    c = r.get("corpus")
    if c: b += "<p>Corpus %s, %d lines: exact lines back T1 %s %%, T2 %s %%.</p>" % (e(c["file"]), c["lines"], c["T1_line_pct"], c["T2_line_pct"])
    b += "<h3>Unmapped</h3><p>%s</p><h3>Collisions</h3><p>%s</p><h3>Core limit (not changed in v6)</h3><p>%s</p>" % (e(" ".join(r["unmapped"]) or "none"), e("; ".join("%s <- %s" % (k, " ".join(v)) for k, v in r["collisions"].items()) or "none"), e(" ".join(r["core_limit"]) or "none"))
    return b + "<h3>Phonetic fidelity and dialects</h3><p>%s</p><h3>Research needed</h3><p>%s</p>" % (e(n[1]), e(n[2])) + FOOT
D = V + "/romenagri-site/docs"; os.makedirs(D, exist_ok=True); os.makedirs(V + "/onepagers", exist_ok=True)
for c in S:
    open("%s/onepagers/%s.md" % (V, c), "w", encoding="utf-8").write(md(c) + "\n"); open("%s/script-%s.html" % (D, c), "w", encoding="utf-8").write(page(c))
rows = "".join("<tr><td>%s<td><a href='script-%s.html'>%s</a><td>%s %%<td>%s %%<td>%s</tr>" % (e(N[c][0]), c, e(S[c]["script"]), S[c]["T1_pct"], S[c]["T2_pct"], e(N[c][2])) for c in S)
P = R["perso"]
nav = HEAD % "Navigator" + "<h2>Language navigator</h2><p>Find the language, open its script page, read the research it needs. Percentages are the share of the script's repertoire that returns unchanged (T1 mapping only, T2 through the zip 5 core).</p><table><tr><th>Language<th>Script page<th>T1<th>T2<th>Research needed</tr>" + rows + "</table>"
nav += "<h2>Perso-Arabic (Unicode to Unicode)</h2><table><tr><th>Language<th>Result</tr><tr><td>Urdu<td>%d of %d alphabet letters return (%s %%); corpus lines exact: T1 %s %%, T2 %s %%. Lossy by design: ا ع ہ و ی ے and ث ذ ح خ غ ف ق collapse in Devanagari.</tr><tr><td>Sindhi<td>%d of %d extra letters have any Devanagari image through the Urdu layer; no layer of its own yet.</tr><tr><td>Shahmukhi (Punjabi)<td>%d of %d extra letters have an image through the Urdu layer.</tr></table>" % (P["urdu"]["T1_char_reversible"], P["urdu"]["letters_in_alpha_urdu"], P["urdu"]["T1_char_pct"], P["urdu"]["T1_line_pct"], P["urdu"]["T2_line_pct"], P["sindhi"]["with_devanagari_image"], P["sindhi"]["extra_letters"], P["shahmukhi"]["with_devanagari_image"], P["shahmukhi"]["extra_letters"])
open(D + "/navigator.html", "w", encoding="utf-8").write(nav + "<h2>Not built (tier C)</h2><p>Myanmar, Khmer, Tibetan, Thai, Lao, Javanese, Balinese: different consonant inventories; each needs a linguist-made table first.</p>" + FOOT)
oi = HEAD % "Open issues" + """<h2>Open issues for linguists</h2><h3>1. Orthographic, not phonetic</h3><p>Every v6 layer maps letter for letter. It preserves spelling, not sound. Bengali ব/ভ, Tamil's single stop letters, Urdu's vowel omission and the schwa rules of Hindi, Gujarati and Punjabi are not modelled.</p>
<h3>2. Dialect-level phonetic mapping</h3><p>The same letter is read differently by region and community. v6 ships one default table per script (<code>v6/maps/*.csv</code>). A dialect table would be a second CSV of the same shape plus a column for the sound; the generator would emit one <code>fltr_*</code> pair per dialect. Needed: a native-speaker phoneme table per dialect, with sources.</p>
<h3>3. Pivot choices to confirm</h3><p>Assamese ৰ to U+0931 and ৱ to U+0979; Tamil/Malayalam ழ ഴ to U+0934, ற റ to U+0931, ன ഩ to U+0929; Malayalam chillus to consonant+virama (forward only). U+0979 is not known to the zip 5 core.</p>
<h3>4. Core limits seen (not fixed, by instruction)</h3><p>Devanagari digits, several signs and a few letters do not survive Devanagari to Romenagri and back in zip 5; each script page lists them.</p>
<h3>5. Research needed</h3><p>Ground-truth corpora with native-reader judgement; loanword conventions; policies for conjuncts that exist in one script only; numerals and punctuation; a table for Sinhala and the tier C scripts.</p>""" + FOOT
open(D + "/open-issues.html", "w", encoding="utf-8").write(oi)
